Now I have sufficient calibration. Let me write the final review.

---

## Summary

This paper introduces Weight-Activation Subspace Iteration (WASI), a method for fine-tuning transformer models on resource-constrained devices by jointly decomposing both weight matrices and activation maps into low-rank subspaces. WASI extends prior activation-only subspace iteration (ASI) with a weight decomposition component (WSI), replaces ASI's brute-force rank search with dynamic programming, and demonstrates up to 62× training memory reduction and 1.4× wall-time speedup on a Raspberry Pi 5 for ViT classification, with limited LLM experiments on TinyLlama/BoolQ.

## Strengths

1. **Joint weight-activation compression is a novel integration.** Prior work compressed either weights (SVD-LLM) or activations (ASI/AMC) separately. WASI unifies both under a single subspace-iteration framework with controlled information loss via explained-variance thresholds and perplexity-based objectives. This is a concrete algorithmic contribution over existing piecemeal approaches.

2. **On-device latency validation on real hardware.** Figure 8 reports per-iteration time on a Raspberry Pi 5 across multiple compression levels, showing ~1.4× speedup at ε=0.9 against vanilla training. This is direct evidence that the method yields measurable wall-time gains on the hardware class it targets, which many memory-efficiency papers lack.

3. **WSI vs SVD comparison provides indirect validation of the subspace-iteration approach.** Figure 3b shows that WSI with one power iteration per step reaches comparable accuracy to recomputing full truncated SVD at every iteration while using 1.36× fewer FLOPs. At equal FLOPs, WSI outperforms SVD by ~35%. This substantiates the claim that subspace iteration is a viable replacement for repeated SVD during fine-tuning.

4. **Improved rank selection over ASI.** Section 3.3 replaces ASI's fixed-budget brute-force search with a dynamic-programming strategy that minimizes memory under target pre-tuning perplexity, reducing search cost from exponential to linear (stated in Appendix A.2). This is a clear algorithmic improvement.

5. **Experiments span vision transformers and a decoder-only LLM.** The paper evaluates on ViT, SwinT across five image-classification datasets, and TinyLlama on BoolQ, providing some evidence of generality beyond a single architecture.

## Weaknesses

### Major

1. **Missing comparison against LoRA or adapter-based methods.** The paper discusses LoRA at length in related work and explicitly argues that LoRA has drawbacks (co-existing frozen weights and adapters during training, full-model inference). Yet it never empirically compares WASI against LoRA on the same benchmarks. This is a significant gap because LoRA is the dominant parameter-efficient fine-tuning approach for transformers, and a practitioner evaluating on-device training options would need to see how WASI's accuracy, memory, and latency trade-offs compare. Was LoRA intentionally excluded? The paper's claim that LoRA's adapter overhead (frozen weights + adapters during training) is wasteful would be directly testable. Adding LoRA (and optionally LoRA+ or DoRA) as a baseline with measurements of training memory, inference memory, accuracy, and on-device latency is needed to substantiate the claimed advantages over existing practice.

2. **Subspace stability is validated only for rank counts, not for singular vectors.** The paper's core assumption (Section 3.3) is that the *singular vectors* (the subspace) remain stable across fine-tuning iterations, enabling subspace iteration with a warm-started basis. The only direct evidence (Figure 3a) shows that the *number of singular values* above a threshold stays roughly constant across epochs — this is rank stability, not subspace (singular vector) stability. The actual directions could rotate while the count stays fixed. The paper partially compensates with the indirect evidence of Figure 3b (WSI vs SVD comparison), which shows that WSI does not degrade convergence. However, without measuring principal angles between consecutive subspaces or the approximation error of WSI vs fresh SVD, the paper's claim that "the intrinsic subspace remains relatively stable" is not directly supported. This weakens the theoretical foundation of the method.

3. **TinyLlama experiment is too thin to support claims of LLM generality.** The LLM evaluation fine-tunes only the last 5 layers of TinyLlama on a single binary QA dataset (BoolQ) at extreme compression (ε=0.1). Accuracy is shown on a y-axis spanning only ~2 points (~64–66%) with no error bars or standard deviations. The paper claims "without accuracy loss," but the gap from vanilla is <1% and likely within noise. This single, thin experiment does not establish that WASI generalizes to larger language models, longer sequences, or more complex language tasks. The extreme compression ratios reported (953× activation memory, 30× weight memory) are artifacts of the very small retained rank at ε=0.1 and do not demonstrate utility at practical compression levels for LLMs.

### Minor

4. **Savings are reported primarily for linear layers, which may inflate headline numbers.** The paper states this upfront ("focusing on linear layers within multi-perceptron blocks for fair comparison with previous methods") and mentions extended results with attention layers in Appendix B.3 (which is stripped by the parser, so unverifiable). However, the headline claims of "62× memory reduction" and "2× FLOPs reduction" in the abstract are presented without clarifying that these apply to linear layers only. In a transformer, attention layers (QKV projections, attention score computation) consume significant memory and compute. The reader cannot assess what fraction of the total pipeline is compressed. The main text should present full-model numbers or at least clarify the proportion.

5. **No ablation isolating the contribution of WSI vs ASI.** The paper compares WASI to ASI (activation compression only), but ASI already includes activation compression for both WASI and ASI — so the comparison does not isolate the marginal benefit of adding weight compression (WSI). An ablation that compares (a) WASI full, (b) WASI with WSI only (no activation compression), and (c) WASI with ASI only (no weight compression) would clarify which component drives which savings and whether WSI is beneficial independently of activation compression.

6. **Numerical accuracy tables with error bars are missing.** The main results (Figures 5–7) are shown only as line plots with small markers, making precise comparison difficult. The paper does not report numerical accuracy, memory, or FLOPs values for key configurations in tabular form, nor does it report standard deviations or confidence intervals. For a paper claiming to "match vanilla accuracy" and "surpass vanilla" on CUB, the lack of variance reporting makes it impossible to assess whether differences are statistically significant.

### Trivial

7. Equation (9) uses the notation \(f_{\text{LR}}(\cdot)\) but does not define it in the main text; the reader must infer from context or consult the appendix.
8. The complexity analysis in Section 3.4 assumes equal rank for weights and activations for simplicity, but the actual algorithm may select different ranks for each, making the analysis a rough approximation.

## Nice-to-Haves

- A comparison against subnetwork training methods (e.g., dynamic subnetworks from Quélenec et al., which the paper cites) would broaden the positioning within the on-device learning literature.
- An analysis of the computational overhead of the subspace iteration itself (both WSI and ASI components) on the target hardware, to clarify how much of the 1.4× speedup comes from reduced matrix dimensions vs. the cost of basis updates.
- A discussion of limitations: WASI introduces new hyperparameters (ε for weights, perplexity target for activations); it may not work well for tasks requiring high-rank weight updates; the method has only been tested on classification and one QA task.

## Removed Points

- **Criticism about LoRA being the most relevant baseline and its omission being "decisive"**: While the missing LoRA comparison is a real weakness (retained as Major #1), the harsh critic characterized this as a "critical issue" that prevents acceptance in current form. The paper does compare against SVD-LLM (a low-rank model method derived from the LoRA family) and ASI, and it explicitly discusses why LoRA's design differs from WASI's goals. The omission weakens but does not invalidate the paper's contribution; the comparison is a major gap, not a fatal flaw.

- **Criticism that "the preliminary section over-promotes the WSI vs SVD result"**: This is a subjective judgment about presentation emphasis. The result (WSI is 1.36× cheaper than SVD recomputation) is a valid efficiency comparison even though vanilla training does not compute SVD — the purpose is to validate the subspace iteration mechanism against its exact counterpart, not against vanilla.

- **Criticism about the Raspberry Pi 5 batch size of 128 being "unusually large"**: The paper reports batch size = 128 for the on-device experiment. Without evidence that vanilla training could not fit with this batch size, this is speculation. The paper should report whether vanilla fit, but this is a minor presentation concern, not a structural weakness.

- **Claim that "f_LR is never defined in the main text"**: This is addressed in the paper: "where f_LR(·) denotes a linear operator applied in the low-rank space (see Appendix A.1)." The term is parenthetically defined with an appendix reference, which is acceptable.

- **Criticism about SVD-LLM being "of limited relevance" as a baseline**: SVD-LLM is a weight-compression method that produces low-rank models, making it a directly comparable baseline for the weight-compression aspect of WASI. The paper reasonably positions it as the most relevant weight-compression baseline.

- **Strength Finder point about "Stability assumption validated" (Figure 3a)**: The strength finder overstates this — Figure 3a shows rank stability (count of singular values), not subspace (singular vector) stability, as noted in Weakness #2. This strength is demoted because the evidence is incomplete.

- **Strength Finder claim about "Full SVD comparison with WSI" being a supporting strength**: This is a genuine strength and is retained in Strengths #3 above, appropriately calibrated.

- **Strength Finder claim about "Improved rank selection over ASI"**: Retained as Strength #4 above.

- **"The underlying principles apply broadly to any neural network trained with backpropagation" (conclusion overclaim)**: The harsh critic flagged this. It is a minor overclaim in the conclusion — the paper only tests transformers and a tiny LLM experiment. This is handled under Weakness #3 (thin LLM generality) rather than as a standalone point.

- **All formatting, typo, and missing-appendix criticisms**: Removed per instructions (parser artifacts).

## Novel Insights

The harsh critic's most valuable observation is the mismatch between what the paper claims about subspace stability (that singular *vectors* are stable) and what it actually validates (that singular *value ranks* are stable). This is not a fatal flaw — the WSI vs SVD experiment (Figure 3b) provides indirect evidence that the subspace iteration works — but it reveals that the paper's theoretical framing is slightly ahead of its evidence. The strength finder's most useful observation is that the on-device latency measurement on a Raspberry Pi 5 (Figure 8) is a concrete, hard-to-fake validation that distinguishes this paper from many memory-efficiency papers that only report theoretical FLOPs or memory ratios. Combined, these suggest the paper has a solid empirical core that would benefit from tightening the theoretical validation and broadening the baseline comparisons.

## Suggestions

1. **Add LoRA as a baseline.** Measure training memory (including adapter overhead), inference memory, and accuracy on ViT/CIFAR-10 and SwinT/Pets at comparable rank settings. This is the single most impactful addition.
2. **Validate subspace stability properly.** Measure the principal angle between consecutive WSI subspaces or the Frobenius-norm error of WSI's approximation against a fresh truncated SVD at each iteration. Show that this error remains bounded.
3. **Report full-model memory and FLOPs** (including attention layers) for at least one configuration, so readers can assess overall savings.
4. **Provide numerical accuracy tables with error bars** for key configurations (ε values, datasets). Replace or supplement the small-format line plots.
5. **Strengthen the TinyLlama experiment**: try less aggressive compression (ε=0.5, 0.8), report on more than one dataset, and include standard deviations.

## Score and Decision

**Calibration summary:**

**Round 1 — Bracketing:** Three queries on topics related to low-rank training, subspace methods, and transformer compression.
- Weak band (avg < 3.5): *Optimizing Attention* (3.00), *Implicit Bias in Matrix Factorization* (3.40), *Efficient Low-Rank Diffusion* (2.50), *On-Device Transfer Learning* (2.50). These are either withdrawn or rejected with weak/insufficient evidence. WASI is clearly stronger than these — it has more experiments, a clearer contribution, and on-device validation.
- Middle band (3.5–7.5): *SubTrack-Grad* (4.75, Reject), *LDAdam* (7.00, Accept Poster), *Efficient Learning with Sine-Activated Low-Rank* (7.00, Accept Poster), *Dobi-SVD* (6.20, Accept Poster).
- Strong band (avg > 7.5): *Small-scale proxies for large-scale Transformer training instabilities* (8.00), *Batched Low-Rank Adaptation* (8.00), *LoRA Done RITE* (8.67). WASI is clearly below these.

**Round 2 — Narrowing (bracket 4.0–6.0):**
- *Low-Rank Correction for Quantized LLMs* (5.00, Reject): Post-training quantization correction with low-rank matrices. WASI is comparable in experimental breadth but more novel in its joint training-time approach. WASI is slightly stronger.
- *Train Small, Infer Large* (6.20, Accept Poster): Memory-efficient LoRA training enabling 70B model on 20GB GPU. More impressive results than WASI, though the idea is more incremental (pruning + LoRA). WASI is weaker than this anchor.
- *One Initialization to Rule them All* (4.75, Reject): LoRA initialization via SVD of activations. Limited novelty. WASI is stronger — it has more technical contribution and on-device validation.
- *Structured MoE Compression via SVD* (5.00, avg of 6,6,3 — note: 3-reviewer paper, effective ~5.0): MoE-specific compression. WASI is comparable in contribution depth but on-device testing gives it an edge.

**Final position:** The paper is stronger than rejected anchors at 4.75–5.00 (SubTrack-Grad, EVA, LRC) because it has a clearer novel contribution (joint weight-activation training-time compression), on-device latency validation on real hardware, and experiments across multiple architectures. It is weaker than accepted anchors at 6.20+ (Train Small Infer Large, Dobi-SVD) because those papers have either more thorough experiments, stronger baselines, or more impressive empirical results. The missing LoRA comparison, thin LLM evaluation, and incomplete subspace validation prevent it from reaching the acceptance-tier. Score: 5.0.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>