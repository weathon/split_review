Now I have a thorough understanding of the paper and all reviewer claims. Let me construct the final consolidated review.

## Summary

COAT introduces two innovations — Dynamic Range Expansion (DRE) for optimizer state quantization and Mixed-Granularity Activation Quantization — to compress both optimizer states and activations into FP8 during training. The paper demonstrates 1.54× end-to-end memory reduction, 1.43× training speedup over BF16, and near-lossless accuracy on LLM pretraining (OLMo-1B, 22B tokens), LLM fine-tuning, and VLM training.

## Strengths

- **Dynamic Range Expansion reduces optimizer quantization error substantially**: Table 1 (the quantization error table) shows that applying DRE to both first- and second-order moments using E4M3 reduces the MSE of the effective update term m/√v from 20.10 (E4M3 without expansion) to 12.31 — a 1.63× improvement. This directly supports the claim that optimizer-state quantization can be nearly lossless with DRE.

- **Mixed-Granularity Activation Quantization targets the real bottleneck**: Table 2 (activation memory decomposition) provides a clear breakdown showing non-linear layers account for ~50% of activation memory in Llama-style models, while linear layers contribute <25%. COAT's strategy of per-group quantization for non-linear layers and per-tensor quantization for linear layers achieves a 1.65× achieved activation memory reduction (theoretical 1.69×), and this decomposition insight itself is practically valuable.

- **End-to-end memory and speed gains are practically demonstrated**: Table 7 shows COAT achieves 1.54× peak memory reduction (e.g., Llama-2-7B on 4 GPUs: 55.1 GB → 35.6 GB) and 1.45× speedup over BF16. Critically, COAT enables full-parameter training of Llama-2-7B on a single H100 (where BF16 and TE OOM), and doubles feasible batch sizes in distributed settings (e.g., Llama-2-13B on 4 GPUs: batch size 1 → 2, yielding 2.25× speedup). These are practically useful results that go beyond theoretical claims.

- **Accuracy is validated across multiple tasks and settings**: The paper reports perplexity/accuracy on LLM pretraining (OLMo-1B, 22B tokens), LLM fine-tuning (math reasoning), and VLM SFT (VILA1.5-7B), with COAT consistently matching BF16 and TransformerEngine baselines within noise.

- **DRE is shown to generalize beyond E4M3/E5M2**: Table 8 (ablation with DE8 format) shows DRE reduces quantization error from 10.54 to 7.47 when applied to DE8, a 1.41× improvement, demonstrating the method's generality.

## Weaknesses

### Fatal
None.

### Major

- **Missing head-to-head comparison with other FP8 training frameworks that also compress optimizer states**: The paper cites FP8-LM (Peng et al., 2023) and Fishman et al. (2024) as related work but never compares against them empirically. Since COAT's core advance is quantizing *both* optimizer states and activations to FP8, comparing against methods that quantize optimizer states (even partially) would clarify whether COAT's specific techniques (DRE, mixed-granularity quantization) offer a meaningful accuracy/efficiency advantage over simply applying existing methods. The comparison to TransformerEngine (which deliberately does *not* quantize second-order momentum or non-linear activations) does not substitute for this. Without these baselines, the reader cannot assess the marginal benefit of COAT's approach over the closest competing methods.

- **The "nearly lossless" claim is supported by limited-scale pretraining**: The largest full pretraining experiment is OLMo-1B at 22B tokens. The OLMo-7B experiment runs only 1000 steps (~4B tokens) of continued pretraining from a checkpoint — insufficient to detect small but compounding quantization errors that may emerge over hundreds of thousands of steps. Fine-tuning and VLM experiments test only the fine-tuning regime where models start from pretrained weights. A single large-scale convergence run (e.g., full 7B pretraining) or multiple seeds with statistical significance testing would substantially strengthen the core accuracy claim.

### Minor

- **Dynamic range definition is mathematically incomplete**: The definition $\mathcal{R}_X = \max(|X|) / \min(|X|)$ (Section 4.1) is undefined when any element of a quantization group is exactly zero — a scenario that, while rare in FP32 optimizer states, is not acknowledged or addressed. The paper should specify a clamping strategy (e.g., $\min(|X|, \epsilon)$) or argue why this case cannot arise in practice. (This is a minor concern because optimizer states are almost never exactly zero, but the omission leaves the formal definition incomplete.)

- **Group Scaling is advocated without accuracy validation against alternatives**: The paper claims Group Scaling is "simpler and more flexible" than TransformerEngine's delayed scaling and "could be even better in precision" (Section 5.2), but provides no experiment comparing the two methods in terms of model accuracy. While Group Scaling computes the same per-tensor max as just-in-time scaling (so quantization error is identical), the claim about improved precision relative to delayed scaling is unsupported. The speed comparison (Figure 4b) is helpful but not sufficient to validate the claimed precision advantage.

- **"Fewer than 1% of values have large magnitudes" is stated without evidence** (Section 4.1, line 111). This quantitative claim about optimizer state sparsity is not backed by a figure, table, or citation. It should be supported with data or removed.

- **End-to-end speedup numbers conflate two effects**: The speed ratios in Table 7 compare COAT at its maximum achievable batch size to BF16 at BF16's maximum batch size. For example, the 2.25× speedup for Llama-2-13B on 4 GPUs is primarily driven by doubling the batch size (better hardware utilization) rather than FP8 arithmetic. The single-layer latency table (Table 4) provides cleaner isolation (1.47–1.57× speedup at equal batch size), but the paper does not disentangle these factors in the end-to-end results, making the headline speedup numbers less analytically informative.

- **Missing ablations**: The paper would benefit from (1) an ablation of DRE (train without DRE to measure accuracy impact), (2) comparison of per-group vs per-block vs per-tensor activation quantization in actual training (not just quantization error), and (3) a study of varying group size for optimizer quantization.

- **Computational overhead of the expand function is not measured**: Computing $k = \log_{\mathcal{R}_X}(\mathcal{R}_{\text{E4M3}})$ and applying $f(x) = \text{sign}(x)|x|^k$ per group per step involves logarithms and exponentiation. The paper does not report the wall-clock overhead of these operations, which is relevant for the end-to-end speed claims.

### Trivial

None that survive filtering.

## Nice-to-Haves

- Zoomed-in loss curves for early and late training stages to visually confirm absence of divergence.
- A sensitivity analysis of handling near-zero values in dynamic range computation.
- Reporting equal-batch-size speedup separately from max-batch-size speedup for end-to-end results.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **TE linear activation memory (3.33U) questioned**: The reviewer claimed TE does not reduce activation memory for linear layers. However, TE stores the FP8 GEMM inputs (activations) in FP8 for the backward pass, making the 3.33U figure (half of 5.66U) reasonable. The paper's footnote also notes this is based on their implementation. This criticism is based on a misunderstanding of TE's capabilities. REMOVED.

2. **Figure axis labeling nitpicks**: The reviewer complains about unlabeled axes in figures. These are formatting artifacts of the PDF extraction process and/or minor presentation issues. REMOVED per formatting-artifact rule.

3. **Ablation of DRE with DE8 called "tangential"**: The reviewer claims this table is "not a focused ablation." However, showing DRE's compatibility with DE8 demonstrates generality and is a legitimate supporting experiment. The specific combination tested (E4M3+Expand / DE8+Expand combinations) provides useful information. REMOVED as non-issue.

4. **"Could be strong with revisions" softening**: The reviewer implies the paper could be acceptable if fixed. This is not a weakness. REMOVED as irrelevant to the critique of the paper's current form.

## Novel Insights

Beyond the paper's own contributions, the most noteworthy observation from the reviews is the tension between the paper's theoretical framing (dynamic range expansion as a principled alignment of distribution to representation format) and the practical incompleteness of that framing (undefined at zero). This is a case where a mathematically elegant method has a corner case that is negligible in practice but needs to be explicitly sealed. The broader lesson for the quantization literature: per-group dynamic range as a concept is powerful but requires specifying a minimum-value clamp or alternative formulation for robustness. The reviewer-derived suggestion of clamping $\min(|X|)$ to a small epsilon is pragmatic and would not affect results while resolving the theoretical gap.

## Suggestions

1. **Add direct comparisons to FP8-LM and Fishman et al.'s approach** for at least the optimizer quantization error table (Table 1) and ideally the OLMo-1B pretraining experiment. This is the single most impactful change to strengthen the paper.

2. **Specify handling of zero-valued elements** in the dynamic range definition, e.g., clamping $\min(|X|)$ to a small epsilon or $2^{-16}$.

3. **Measure and report the computational overhead** of computing $k$ and applying $f/f^{-1}$ per step, perhaps as a fraction of total step time.

4. **Run a longer convergence experiment** — at minimum, extend the OLMo-7B continued pretraining to match the OLMo-1B's 22B token scale, or provide statistical significance with multiple seeds for the 1B experiment.

5. **Provide an ablation training without DRE** to quantify the accuracy impact of the expand function directly.

6. **Disentangle speedup sources** in end-to-end results by reporting equal-batch-size throughput alongside the max-batch-size results.

## Score and Decision

The paper addresses a genuine practical problem (memory-efficient FP8 training) with well-motivated solutions. The core technical contributions — Dynamic Range Expansion for optimizer states and Mixed-Granularity Activation Quantization — are sound and supported by clear analysis. The end-to-end memory savings and batch-size gains are demonstrably useful.

However, the paper has meaningful gaps: missing comparisons against closely related FP8 training frameworks, incomplete formal specification (zero-handling in dynamic range), unsupported quantitative claims, and limited-scale accuracy validation for the "nearly lossless" claim. These are fixable in revision, and none invalidate the core contribution, but they collectively prevent full confidence in the paper's strongest claims.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>