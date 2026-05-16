Now I have a thorough understanding of the paper and the reviews. Let me write the consolidated review.

## Summary

This paper proposes MC-MoE, a training-free compression framework for MoE-LLMs that combines Pre-Loading Mixed-Precision Quantization (PMQ) and Online Dynamic Pruning (ODP). PMQ allocates different bit-widths to experts via an integer programming model that balances activation frequency, routing weight, and quantization reconstruction error. ODP dynamically prunes one of the top-2 experts for low-confidence tokens while protecting a small fraction of important tokens (identified by a norm-and-attention metric) to mitigate attention decay. At 2.54 bits, MC-MoE compresses Mixtral 8×7b by 76.6% with only 3.8% average accuracy loss on eight zero-shot benchmarks, and on activated parameter count alone the compressed model outperforms the full-precision LLaMA2-13b.

## Strengths

1. **Novel combination of static quantization and dynamic pruning for MoE-LLMs.** The paper is the first to jointly optimize mixed-precision quantization (pre-loading phase) and online expert pruning (inference phase) for MoE models in a training-free manner. Prior work addressed each technique separately (Li et al. 2024 on quantization, Lu et al. 2024 on pruning), making the co-design a genuine contribution.

2. **PMQ's multi-factor IP formulation yields large empirical gains.** At 2.54 bits, PMQ achieves 67.50% average accuracy on eight zero-shot tasks, outperforming BSP (49.07%, +18.4 pp) and Hessian-based allocation (67.18%, +0.3 pp). The advantage widens at lower bit-widths: at 1.57 bits, PMQ reaches 54.49% vs. 45.91% for Hessian (+8.6 pp) (Table 1). These gains are directly attributable to jointly considering frequency, routing weight, and reconstruction error.

3. **ODP's token protection mechanism is effective and efficient.** Protecting just 2% of the most important tokens reduces perplexity from 6.46 to 6.24 (weight-only pruning baseline) while barely affecting the computation compression ratio (15.1% → 14.8%) (Fig. 8). The attention-decay analysis (Fig. 4) provides a clear empirical motivation for why weight-only pruning fails and why token-aware protection helps.

4. **Extreme compression that surpasses larger dense models.** At 2.54 bits, MC-MoE compresses Mixtral 8×7b to 16.24 GB total (3.96 GB activated per token) while outperforming the 26.03 GB LLaMA2-13b on the LM-Eval benchmark suite (66.94% vs. 65.19%) (Table 3). This demonstrates that highly compressed MoE models can beat full-precision dense models of larger size.

5. **Generalizes to larger MoE models.** Results on Mixtral 8×22b (141B parameters) show similar trends: at 2.54 bits with ODP, accuracy drops only ~5% from the full-precision model while reducing activated parameters to 10.96 GB (Table 3), confirming scalability.

6. **Systematic ablation of design choices.** The paper ablates random vs. single-factor vs. multi-factor bit allocation (Fig. 5_1, 5_2), the token-protection ratio (Fig. 8), and the effect of masking all experts for unimportant tokens (Fig. 9), providing clear evidence that each component is necessary.

## Weaknesses

### Fatal
None.

### Major

1. **Speedup measurements are confounded by GPU count and cannot be trusted.** Table 3 reports speedups of 1.63×–1.89× for quantized models over the 16-bit baseline. However, the caption states: "16-bit Mixtral 8×7b uses 2 A100-80GB GPUs... quantized models are tested on one A100-80GB GPU." Comparing single-GPU throughput against multi-GPU throughput conflates the effect of model compression with the overhead of model parallelism (inter-GPU communication, different batching characteristics, etc.). The reported speedups likely overstate the true benefit of compression. The authors should either (a) measure the 16-bit model on a single GPU with CPU offloading or tensor parallelism to fit, or (b) report FLOP-based speedup estimates or memory-footprint reduction separately, and (c) report latency/throughput on identical hardware. This weakness undermines the inference-efficiency claims but does not invalidate the memory-compression or accuracy results, which remain independently valuable.

### Minor

1. **Token-importance metric (Eq. 6) is under-specified.** The paper does not state which layer's (or which block's) attention map **A** is used in computing \(I_j\). The equation \(I_j = \|\mathbf{t}_j\|_1 \cdot \frac{\sum_{j\leq i \leq L} A_{j,i}}{L-j}\) uses the notation \(A_{j,i}\) without clarifying whether the indexing is (query, key) or (key, query). Depending on the convention, the sum over \(j \leq i \leq L\) may mostly capture self-attention (which is uninformative) or may capture attention from later tokens, which is the intended effect. This ambiguity affects reproducibility but the overall approach — protecting tokens with high attention scores and feature magnitudes — is well-motivated and the empirical results demonstrate its effectiveness regardless of indexing details.

2. **PMQ objective hyperparameters α, β, γ are not reported.** The IP objective (Eq. 4) uses three hyperparameters \(\alpha, \beta, \gamma\) that balance activation frequency, routing weight, and quantization error. Their values are never stated anywhere in the paper, and no sensitivity analysis is provided. While the paper shows the full method works, the absence of these values makes replication difficult and leaves open the question of how sensitive the results are to these choices.

3. **No variance or error bars on accuracy results.** All average accuracy numbers in Tables 1–3 are reported as point estimates without standard deviations, confidence intervals, or multiple-run statistics. For a 2.54-bit PMQ vs. Hessian difference of 0.32 pp (67.50% vs. 67.18%), it is unclear whether this difference is statistically significant. The LLM evaluation community often uses single runs for large-scale benchmarks, but reporting at least the range or bootstrap intervals would strengthen the reliability claims.

4. **Computational overhead of ODP is not measured.** Computing the token importance \(I_j\) requires the attention map and the sum in Eq. 6, which has non-negligible memory and latency overhead. The paper does not report wall-clock time with and without ODP on the same input, so it is unclear whether the 15% reduction in activated parameters translates to a real speedup after accounting for the overhead of importance computation.

5. **"Act Params (GB)" column is ambiguous.** The column reports the size of activated weights after quantization (including scaling factors), but the runtime memory footprint during the forward pass also includes dequantized buffers and attention tensors. The paper clarifies that "the parameter calculation of the compressed model includes the compressed weights and quantizer parameters," but this should explicitly distinguish between stored model size and runtime memory usage.

### Trivial

1. **Notation glitch in Eq. 6.** The text says "importance of the \(i\)-th token" but the variable is \(I_j\) with index j. This is a minor inconsistency.

## Nice-to-Haves

- **Ablation of PMQ hyperparameters.** A sensitivity study varying \(\alpha, \beta\) (e.g., 0, 0.5, 1, 2) on PPL at 2.05 bits would help understand how critical the multi-factor weighting is.
- **ODP wall-clock time.** A latency comparison (tokens/second) with and without ODP on identical hardware, for the same batch configuration.
- **Calibration sensitivity.** PMQ and ODP are calibrated on 128 sequences from C4. An analysis of how performance changes when calibrated on different domains (e.g., code, math) would strengthen the robustness claims.
- **Discussion of limitations.** The paper could acknowledge that calibration data may not transfer to all deployment scenarios and that the token-importance metric adds some overhead.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Criticism that the Hessian baseline is not properly adapted / not described.** The paper contains a footnote reference (\ref{a:hessian}) that was stripped by the parser; the description likely existed in the original submission. Per the rule about parser-stripped content, this criticism is removed.
- **Criticism about "first to explore" overstatement.** The claim is specifically about the *combination* of static quantization and dynamic pruning for MoE-LLMs, which is distinct from prior work on each technique separately. While the combination is incremental in some sense, the paper's claim is accurately scoped and not an overstatement.
- **Figure 9 masking all experts.** The reviewer calls this "much more aggressive" — it is intentionally an extreme ablation to show that protecting important tokens (rather than masking unimportant ones) is the right strategy. This is a legitimate experimental comparison, not a flaw.
- **Criticism about F-norm performing similarly above 2 bits.** The paper explicitly acknowledges this ("When the average bit-width exceeds 2-bit, the F-norm is similar to the PPL curve of PMQ") and explains that the advantage emerges below 2 bits. The paper does not claim PMQ dominates at all bit-widths.
- **Criticism about BSP comparison granularity.** The difference in granularity (block-wise vs. expert-wise) is a descriptive observation, and the paper still compares them on the same metric (average bit-width and accuracy). The comparison is fair as BSP is the best available MoE-specific mixed-precision baseline.

## Novel Insights

The reviews surface an interesting tension in the paper: the token-importance metric (Eq. 6) is simultaneously the most novel element of ODP and the least rigorously validated. The paper shows empirically that protecting attention-important tokens works, but the specific design of Eq. 6 — combining ℓ1 norm with a forward-looking attention sum — is neither justified against alternatives (e.g., H2O-style accumulated received-attention) nor ablated. If the authors can show that this specific formulation outperforms simpler alternatives (e.g., just using ℓ1 norm, or just using attention), the contribution would be significantly strengthened. Conversely, the PMQ component is well-validated empirically but its IP objective's hyperparameters are a blind spot; the fact that the method works without careful hyperparameter tuning (if that is the case) could itself be a finding worth reporting.

## Suggestions

1. **Fix the speedup measurement:** Re-run the 16-bit baseline on a single GPU (with CPU offloading or model parallelism that fits the model), or report speedup as the reduction in activated parameter FLOPs plus a separate memory-footprint reduction table. Remove the current speedup numbers or clearly label them as "projected speedup assuming identical hardware."
2. **Specify the attention block and indexing for Eq. 6:** State explicitly which block's attention map is used (e.g., the last MoE layer, or all layers averaged) and clarify the convention for \(A_{j,i}\).
3. **Report α, β, γ values** used in all experiments, and provide at least a small sensitivity study (varying one parameter at a time) to show the method is robust.
4. **Add a wall-clock ablation** comparing throughput with and without ODP on the same GPU.
5. **Add error bars** (or at least multiple-seed ranges) for the main tables to help readers assess significance.

## Score and Decision

This paper makes a solid contribution: a training-free, effective combination of mixed-precision quantization and dynamic pruning for MoE-LLMs, supported by extensive experiments across two model scales and eight benchmarks. The core accuracy and memory-compression results are convincing. The main weakness — the GPU-count confound in speedup measurements — is significant and damages the inference-efficiency claims, but the memory savings and accuracy retention stand on their own. The remaining issues (under-specified hyperparameters, missing ablation details, unmeasured ODP overhead) are addressable in revision.

The paper's strengths (novel combined approach, strong empirical results at extreme compression, scalability) outweigh its weaknesses. With corrected speedup measurements and the minor clarifications, this would be a strong paper. In its current form, the paper is still a positive contribution with one flawed but separable claim.

**Score:** 6.5

**Decision:** Accept

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>