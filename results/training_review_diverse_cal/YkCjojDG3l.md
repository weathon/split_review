I have thoroughly verified the claims against the paper. Let me now synthesize the final review.

---

## Summary

PolySketchFormer replaces softmax attention with a degree-4 polynomial attention mechanism and approximates it using polynomial sketches (Ahle et al., 2020), achieving linear-time (in context length) attention with provable sketch approximation guarantees. It further contributes a block-based algorithm for causal lower-triangular multiplication that reduces the sequential bottleneck of Performer's cumulative sum approach. Empirically, on 110M-parameter language models (Wiki-40B, PG-19), PolySketchFormer achieves perplexities within 2–3 points of softmax attention while delivering 2.1×–4.5× training speedups over FlashAttention at context lengths 8k–32k. A 730M-parameter model shows a 14.6 perplexity vs. softmax's 14.4, and a 4-layer 32k-context model demonstrates the largest speedup.

## Strengths

1. **Theory-guided approach to sub-quadratic attention that sidesteps the SETH barrier.** The paper correctly identifies that approximating softmax attention in sub-quadratic time is hard under SETH (Alman & Song, 2023) and shows that polynomial attention, by contrast, admits an *exact* linear-time algorithm via the tensor product formulation (Section 1). While this is a circumvention rather than a "breaking" of the barrier, the insight is technically sound and well-motivated.

2. **Provable sketch approximation with sketch size independent of hidden dimension.** Theorem 2.2 (instantiated from Ahle et al., 2020) shows that the sketch size needed for the AMM guarantee depends only on $\varepsilon$ and $p$, not on the head dimension $h$. This breaks the $O(n h^{p+1})$ cost of exact polynomial attention. Theorem 2.5 further shows that "tensoring" the sketch preserves nonnegativity with only a constant-factor loss in approximation quality — a clean theoretical solution to the sign problem.

3. **Novel block-based algorithm for causal lower-triangular multiplication.** Section 3 and Theorem 3.1 propose a block-wise approach (Figure 4) that reduces the sequential RNN-style dependence of Performer's cumulative sum algorithm. The analysis of the trade-off between block size $b$, parallelism, and computational cost ($O(n r (b+d))$) is insightful and connects to the chunk-based designs of Hua et al. (2022).

4. **Empirical evidence that degree-4 polynomial attention is a viable softmax replacement.** Figure 2 shows that on two datasets (Wiki-40B, PG-19) across context lengths 512–4k, exact degree-4 polynomial attention achieves perplexities within <1 point of softmax. This is a meaningful finding independent of the sketching contribution.

5. **Significant training speedups over FlashAttention at long contexts.** Table 2 and the 32k-context experiment demonstrate 2.1× (8k), 3.3× (16k), and 4.5× (32k) training step speedups. Figure 1 shows that attention latency per token for PolySketchFormer stays nearly flat while FlashAttention grows linearly with context length. This is the paper's strongest practical contribution.

## Weaknesses

### Major

1. **Missing comparisons against other linear-time attention mechanisms.** The paper compares PolySketchFormer against softmax, exact polynomial, FlashAttention (quadratic), and Performer (discarded due to a data leak). There is no empirical comparison against any other working linear transformer — e.g., Linear Attention (Katharopoulos et al., 2020), Random Feature Attention (RFA), or cosFormer. Since PolySketchFormer is presented as a practical linear-time architecture, showing that it outperforms (or is competitive with) existing linear transformers in either quality or speed is essential. The current evaluation makes it impossible for readers to judge whether PolySketchFormer improves upon the linear-transformer state of the art.

2. **The block algorithm's advantage is asserted but not empirically isolated.** The paper claims that the block-based algorithm gives "significant speedups over the cumulative sum algorithm" (abstract) and cites the sequential bottleneck identified by Hua et al. (2022). However, no experiment measures the speed of the cumulative sum version versus the block version for the *same* sketch configuration. Without this ablation, the claimed speedups from the block algorithm remain unverified — the overall speed numbers conflate the sketch computation and the block multiplication.

3. **Theoretical guarantees stop short of the normalized attention output.** The paper provides AMM guarantees (Theorem 2.2, 2.5) for the unnormalized Gram matrix $\tilde{\mathbf{Q}}\tilde{\mathbf{K}}^\top \approx (\mathbf{Q}\mathbf{K}^\top)^p$, but the final attention output is $\mathbf{O} = \operatorname{diag}(\mathbb{It}_\triangle(\tilde{\mathbf{Q}}\tilde{\mathbf{K}}^\top)\mathbf{1})^{-1} \cdot \mathbb{It}_\triangle(\tilde{\mathbf{Q}}\tilde{\mathbf{K}}^\top)\mathbf{V}$. The per-row normalization (division) is a nonlinear operation that can amplify approximation errors, especially when rows have very different total weights. The paper presents no analysis of how sketch error propagates through the causal mask and the row-wise softmax-like division. While this gap is common in the kernel attention literature (Performer has the same limitation), the paper's claim of "provable guarantees" (abstract) for the overall architecture is not fully substantiated for the actual output.

### Minor

4. **"Breaking the SETH barrier" framing is overstated.** The SETH hardness result of Alman & Song (2023) applies to approximating *softmax* attention output. The paper replaces softmax with a polynomial function — this is a circumvention, not a refutation of the barrier. The actual technical contribution (showing polynomial attention can be approximated in sub-quadratic time via sketches, building on Ahle et al., 2020) is valid and valuable, but the "break" rhetoric should be tuned down to reflect the circumvention accurately.

5. **Data leak claim about the open-source Performer is asserted without supporting evidence.** The paper states that "there is a data leak in the open-sourced version of Performer which inadvertently leads to information flow from future tokens during training" (Section 5). No evidence, minimal reproduction, or diagnostic is provided. If this is a known issue, it should be documented; otherwise the claim reads as a post-hoc dismissal of the baseline. The paper should either provide evidence or acknowledge that Performer results were omitted for other reasons.

6. **Sketch size choice ($r=32$, giving 1024 columns after tensoring) is not justified against the theory.** The theoretical sketch size from Theorem 2.2 is $r \leq C p/\varepsilon^2$, but the paper does not state what value of $\varepsilon$ the chosen $r=32$ corresponds to, nor does it provide an empirical measurement of the approximation error on actual Q/K matrices. The choice is motivated only by a speed-quality trade-off, which is reasonable but leaves the link between theory and practice incomplete.

7. **Theorem 2.5's JL-moment conditions are not verified for the constructed sketch.** The paper states "Results from Section 4 of Ahle et al. (2020) can be used to show that [the sketch] satisfies the requirements" (Section 2.1), but does not provide even a proof sketch or a precise pointer to which results apply. For a paper claiming provable guarantees, this is more hand-wavy than one would hope.

### Trivial

8. None of substantive concern beyond the above.

## Nice-to-Haves

- **Memory-usage analysis.** The paper reports training latency but does not report peak memory usage of PolySketchAttention vs. FlashAttention at long contexts, even though memory is often the bottleneck for long-context training. Reporting this would strengthen the practical contribution.
- **Backward pass cost.** The paper mentions rematerialization but does not report how much slower the backward pass is relative to the forward pass, which affects overall training throughput.
- **Block size sensitivity.** The paper uses $b=256$ in all experiments but provides no analysis of how performance varies with $b$. A small ablation would help validate the trade-off claimed in Section 3.
- **Exact polynomial training cost transparency.** The paper trains exact degree-4 polynomial models at context lengths up to 4k for 125k steps. While this is *feasible* (the $O(n h^{p+1})$ cost is ~$4.4\times 10^{12}$ ops/layer at n=4096, which an A100 can sustain), stating the actual training time in GPU-hours would help readers calibrate the experiment's cost and confirm feasibility.

## Removed Points

These points were found to be factually wrong or based on misreading of the paper:

- **"Feasibility of the exact polynomial attention experiments is unclear and likely impossible"** — REMOVED. The critic claimed the exact degree-4 polynomial experiments are "likely impossible" at the reported scales. The paper explicitly describes the cumulative sum algorithm for exact computation with complexity $O(n h^{p+1})$. For $h=64, p=4, n=4096$, this is ~$4.4\times10^{12}$ ops/layer. On an A100 GPU (~156 TFLOPS FP32), this is ~0.028 sec/layer ~ 0.34 sec/forward pass for 12 layers. With 32 A100s over 125k steps, training is expensive but feasible within academic compute budgets. The paper also reports that polynomial models go OOM at 8k/16k, which is consistent with the tensor formulation. The critic's claim is factually incorrect.

## Novel Insights

Beyond the paper's own contributions, the key observation emerging from the reviews is that **Polynomial Sketch Attention occupies a distinct and potentially valuable position in the design space**: it achieves genuine $O(n)$ time (not just $O(n)$ with large constants) while avoiding the strict assumptions about bounded norms or specific kernel choices that constrain other linear transformers. The block algorithm insight — that the causal mask computation can be parallelized via blocking rather than relying on the sequential cumulative sum — directly addresses a practical bottleneck that has plagued linear transformers since Performer (as noted by Hua et al., 2022), yet remains underexplored in the literature. This algorithmic insight, separable from the polynomial sketch contribution, could benefit other linear attention mechanisms as well.

## Suggestions

1. **Add at least one working linear transformer baseline.** Compare PolySketchFormer against Linear Attention (Katharopoulos et al.) or RFA on the same architecture and datasets. This is the single most important addition to the empirical evaluation.

2. **Ablate the block algorithm.** Compare the cumulative sum version versus the block version for the same sketch size, ideally reporting both latency and throughput. This would substantiate the claimed speedups.

3. **Acknowledge the normalization gap and discuss its practical significance.** Add a sentence or paragraph noting that the provable guarantees apply to the unnormalized Gram matrix and that the normalization step is not analyzed — similar to the honest discussion in the paper about negative entries in the sketches (lines 67–68).

4. **Provide evidence for the Performer data leak claim** or remove it and instead acknowledge that Performer was excluded for reasons that could not be independently verified.

5. **Report memory usage** alongside latency, as this is often the binding constraint for long-context training.

## Score and Decision

The paper makes a genuine contribution: it introduces a novel combination of polynomial sketches and a block-based causal algorithm that yields practical speedups at long context lengths. The theoretical grounding (AMM guarantees, nonnegativity via tensoring) is sound as far as it goes, and the empirical validation demonstrates real engineering value. However, the evaluation has two significant gaps — missing comparisons against other linear transformers and no ablation isolating the block algorithm — and the theoretical analysis is incomplete (normalization not analyzed). These issues are addressable but currently weaken the paper.

**Score:** 5.0

**Decision:** Borderline Accept — the core idea and results are solid, but the evaluation gaps prevent a stronger rating. The paper would be strengthened substantially by addressing the missing baselines and block algorithm ablation.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>