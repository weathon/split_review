## Summary
SparseFW applies the Frank-Wolfe (FW) algorithm to LLM pruning by relaxing the combinatorial mask selection problem into a tractable convex program over the convex hull of binary masks. The method accounts for inter-weight interactions (unlike greedy baselines Wanda and RIA) and provides theoretical approximation guarantees connecting the rounded relaxed solution to the original combinatorial problem. Experiments across Gemma-2, Yi-1.5, DeepSeek, Qwen2.5, and LLaMA-3 at 50%, 60%, and 2:4 sparsity show consistent, if uneven, improvements in perplexity and zero-shot accuracy.

---

## Strengths

- **Principled unification of prior methods.** The paper cleanly derives that Wanda and RIA are both instances of greedy single-weight removal for the same underlying objective (Equations 4–7), and that RIA is simply Wanda applied to a rescaled weight matrix. This is a genuine and useful contribution independent of SparseFW.

- **Theoretical guarantees with two interpretable error sources.** Lemma 1 decomposes the suboptimality into an optimization error (O(k/T), vanishing with iterations) and a thresholding error (controlled by Hessian curvature and ‖M_cont − M_thresh‖₁). Figure 4 empirically validates both terms, showing the continuous mask improving steadily while the thresholded mask tracks the declining threshold residual. This level of theory-to-experiment alignment is rare in the LLM-pruning literature.

- **Memory-efficient formulation.** Precomputing G = XX^T and H = WG reduces dependence on the full activation tensor from O(d_in × N·L) to O(d_in²), making the method agnostic to sequence length and calibration batch size in the per-iteration cost. The sample-vs-iteration ablation (Figure 3) directly exploits this: more samples improve quality at no extra FW iteration cost.

- **Broad, reproducible experiments.** Results span 5 modern architectures, 3 sparsity regimes, 2 warmstarts, and multiple seeds; code is promised. The per-layer breakdown in Figure 2 gives fine-grained evidence that FW improves the local objective across virtually all layers and matrix types.

---

## Weaknesses

### Fatal
None. No single error invalidates the paper's core claims.

### Major

1. **Vanilla FW consistently underperforms baselines; the method only works with α=0.9.** Section 2.3 explicitly states that "setting α=0.0 (full FW without any fixed weights) consistently yields worse results than the baselines." The fix—holding 90% of the mask frozen according to Wanda saliency scores and only optimizing the remaining 10%—is pragmatic, but it fundamentally reframes what SparseFW actually does: it is a local refinement of a Wanda mask over a small subset of weights, not a general replacement of greedy selection. The paper's framing ("we consider the convex relaxation... which fully accounts for interactions between weights") overstates the scope of the optimization actually performed. Why the local objective improvement from full FW fails to translate to lower perplexity is attributed to a "local–global objective mismatch," but this mismatch is precisely the central challenge in layerwise pruning and deserves more analysis. The paper does not characterize when this mismatch is severe or why fixing 90% of the mask resolves it.

2. **No comparison to SparseGPT.** The paper excludes SparseGPT on grounds that it performs weight reconstruction rather than mask selection. However, SparseGPT is the most widely cited method and the most credible point of comparison at 50% and 60% sparsity. Readers cannot determine whether SparseFW is competitive with the state-of-the-art end-to-end, especially since SparseGPT can be substantially stronger than Wanda at 60% sparsity and above. Even a single table showing this comparison would substantially strengthen or contextualize the claims.

3. **FW convergence is O(1/T) but the thresholding residual plateaus above zero.** Figure 4 (right) shows the average threshold residual stabilizing around 0.12 at 5000 iterations rather than converging to zero. FW converges to a vertex of C_k only in the pairwise or away-step variants; the vanilla variant used here converges to the interior of C_k. The paper acknowledges this ("as long as the relaxed solution is not at a vertex, the thresholding error remains nonzero") but does not discuss whether away-step or pairwise FW variants, which do converge to vertices, would close this gap.

### Minor

1. **Inconsistent improvements at 50% sparsity.** At the most common benchmark sparsity level, the gains are within noise for several models (e.g., Yi-1.5-9B: 6.58 vs 6.58; DeepSeek-7B: 7.89 vs 7.79 for SparseFW(Wanda)), and in some cases SparseFW(Wanda) slightly underperforms the Wanda baseline. The claim of "consistent gains" should be qualified to higher-sparsity regimes.

2. **Missing wall-clock time comparison.** The paper argues that "spending more resources once to improve performance is worthwhile," but provides no concrete timing data (e.g., seconds per layer or total pruning time) for SparseFW versus Wanda/RIA. Without this, readers cannot evaluate the practical cost–benefit trade-off.

3. **Learning rate schedule is fixed but not justified.** The η_t = 2/(t+2) schedule is standard for FW, but given that the problem is warm-started from a binary mask (already at a vertex), the early large steps may be counterproductive. No ablation of alternative schedules is presented.

### Trivial
- The bounds in Lemma 1 involve λ_max(Q), but Q is defined only informally in the main text; the relationship to G = XX^T is noted but the exact form of Q is not given until the appendix.

---

## Nice-to-Haves
- An analysis of when the local–global objective mismatch is large (e.g., correlation with model size, sparsity level, or layer position) would substantially deepen understanding of the α heuristic.
- Experiments with pairwise or away-step FW variants to test whether vertex convergence improves the thresholded mask quality.
- Comparison to SparseGPT at 50% and 60% sparsity on at least one model.

---

## Novel Insights
The paper's most novel contribution, beyond SparseFW itself, is the algebraic derivation that Wanda and RIA are special cases of greedy single-weight pruning for the same quadratic objective, and that RIA amounts to Wanda on a rescaled weight matrix. This unifying view clarifies the design space of mask-selection methods and motivates the convex relaxation approach. The empirical observation that even 10% FW optimization (α=0.9) on top of a Wanda mask yields consistent gains across diverse architectures suggests that a small amount of interaction-aware refinement is highly cost-effective, even if full FW optimization fails—a practically actionable finding that the current framing somewhat obscures.

---

## Suggestions
- Reframe the presentation to position SparseFW as a calibrated refinement of saliency-based masks rather than a full replacement of greedy selection; this would align the theoretical framing with the practical finding that α=0.9 is necessary.
- Add a timing table comparing total pruning time (CPU/GPU hours) for SparseFW vs Wanda vs RIA for a representative model.
- Investigate away-step or pairwise FW to reduce the thresholding residual plateau and potentially relax the need for the α heuristic.
- Test generalization of the α=0.9 finding across sparsity levels to determine whether it is a model-independent constant or varies with regime.

---

## Score and Decision

The paper makes a genuine contribution: a principled convex-relaxation view of LLM pruning with theoretical guarantees, a clean unification of prior greedy methods, and consistent empirical improvements at higher sparsity. The main limiting factor is the disconnect between the theoretical framing (full convex optimization of mask interactions) and the practical reality (90% of the mask must be fixed by the greedy baseline for the method to work). This tension is acknowledged but not resolved. Compared to the ICLR 2026 pool, this sits above the mean in originality and theoretical rigor, with solid but uneven empirical results.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>