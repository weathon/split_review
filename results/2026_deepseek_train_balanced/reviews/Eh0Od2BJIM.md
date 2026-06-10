## Summary

HyperAttention proposes an approximate attention mechanism with near-linear time complexity under relaxed assumptions (no bounded entries or bounded stable rank required, unlike KDEFormer and Alman & Song 2023). The algorithm uses sortLSH to identify large attention entries and uniform column sampling for matrix multiplication, with a recursive extension for causal masking. Empirical results show speedups over FlashAttention on single layers (up to 54× non-causal, 5.4× causal at n=131k) and on real LLMs (1.5× inference speedup for ChatGLM2 at 32k context with moderate perplexity degradation).

## Strengths

- **Genuine theoretical advance**: Theorem 1 achieves O(d·n^{1+o(1)}) runtime with spectral guarantees under the conditions α=n^{o(1)} and κ=n^{o(1)}, relaxing the bounded-entry and bounded-stable-rank assumptions of prior work (KDEFormer, Alman & Song 2023). This is a meaningful step beyond existing lower bounds.

- **Algorithmic simplification**: Eliminates KDE-based importance sampling, replacing it with uniform sampling or row-norm sampling of V, which is both provably sufficient and practically simpler (lines 53–54, 59–60). The modular design allowing integration with FlashAttention is also well-motivated.

- **First provable near-linear time attention with causal masking**: The recursive partitioning scheme (Algorithm 3) extends theoretical guarantees to causal attention, which was not supported by KDEFormer or Alman & Song 2023.

- **Empirical support for α = n^{o(1)}**: Section 4.4 measures α on real models (T2T-ViT, ChatGLM2) and shows α/n decreases with n, providing concrete evidence that one of the two key theoretical conditions holds in practice.

- **Task-specific robustness analysis**: Table 1 characterizes which tasks tolerate approximation better (summarization, code completion) and which degrade more (QA), offering actionable guidance for practitioners.

## Weaknesses

### Fatal

None.

### Major

- **κ is never empirically measured.** The condition number κ (ratio of max to min unmasked row sums) appears at the 7th power in the sample complexity bound (Lemma 3.1: m = Ω(κ⁷α²/ε⁶ log n)). The paper frames its conditions as "empirically verifiable" (lines 56, 93) but provides no measurement of κ for any model, layer, head, or dataset. The theory requires κ = n^{o(1)}; if κ is large in practice, the bound is vacuous and the "near-linear time" label on real data is unsupported. This is a significant gap between the theoretical framing and the empirical work — one of two core parameters is entirely unaddressed.

- **No comparison against any other approximate attention method.** The abstract claims HyperAttention "outperforms existing methods" (line 9), but the experiments compare only against FlashAttention (exact attention). While FlashAttention is the right exact baseline, the claim of superiority over *approximate* methods (Reformer, BigBird, Longformer, Scatterbrain, linear attention) is entirely unsubstantiated. Showing that an approximation is faster than exact computation is the minimum bar; what matters for practitioners is the accuracy–speed trade-off relative to other approximations.

### Minor

- **Theory–experiment gap on spectral error.** Theorem 1 guarantees a spectral-norm bound, yet no experiment measures the actual approximation error (spectral norm, Frobenius norm, or cosine similarity). Evaluation relies entirely on downstream perplexity and task scores, which conflate approximation error with model robustness. This decouples the theoretical guarantee from the empirical validation — a direct error measurement would be the single most impactful addition.

- **α validation limited to n ≤ 9k for LMs (Fig. 7), while speedup claims go to n = 131k.** The paper shows a decreasing trend but over an order-of-magnitude gap. The trend is suggestive but not conclusive without evidence at larger n.

- **α computation for LMs excludes the first 32 columns** (line 406) because they "often contain heavy entries." The initial tokens carry critical context (instructions, prompts, document beginnings), so this exclusion is a nontrivial caveat to the claim that α = n^{o(1)} holds "in practice."

- **No ablation study.** HyperAttention combines sortLSH mask generation, uniform column sampling, clipping thresholds, and a lower-bound mechanism. No experiment isolates any component. For example, would uniform sampling alone (dropping sortLSH) achieve similar accuracy? This makes it difficult to attribute empirical results to specific design choices.

- **Big-Theta used as an assignment in Algorithm 2** (line 229: `C_i ← Θ(...)`). Theta is asymptotic notation, not a concrete value. An implementation requires a specific constant, but none is provided, affecting exact reproducibility.

- **No variance information.** All perplexity values and speedups are single numbers without error bars, confidence intervals, or run-to-run variability.

### Trivial

- **Synthetic single-layer experiment data generation not specified** (Section 4.3). Q, K, V dimensions are given (d=64, 12 heads) but not their distribution or provenance. If inputs are random, attention matrices are nearly uniform, making approximation artificially easy.

## Nice-to-Haves

- Direct measurement of the spectral (or Frobenius) approximation error on a single layer to connect Theorem 1 to practice.
- A single comparison against at least one approximate attention baseline (e.g., Reformer or a fixed-sparsity mask) to substantiate the "outperforms" claim.
- Measurement of κ on real attention matrices across layers, heads, datasets, and sequence lengths.
- Ablation of the sortLSH component to quantify its marginal contribution.
- Pareto frontier of the perplexity–speedup trade-off by varying b and m.

## Removed Points

- *Criticism about 54× speedup conflating synthetic and real results*: the paper clearly separates the single-layer synthetic experiments (Section 4.3) from model-level experiments (Section 4.2), and the abstract states both the 50% inference speedup and the 5-fold single-layer speedup in distinct sentences. The distinction is transparent.
- *Criticism about reused random indices creating theoretical dependencies* (line 346): the paper explicitly describes this as a practical optimization, and the concern is speculative without evidence of empirical harm. Removed per the rule against speculative-fatal claims.
- *Criticism about LSH overhead not discussed*: a plausible detail to elaborate but not a substantive weakness for a paper at this level.
- *Strength about causal masking being "absent from prior work"*: while prior theoretical work (KDEFormer, Alman & Song) does not handle causal masking, the paper's broader statement about sparse/low-rank approximations (line 25) is overly broad. Since I cannot independently verify all cited methods, this strength is removed per the hard rule.
- *Generic strengths*: "the problem is important," "the paper is well-written" — these are superficial and removed.

## Novel Insights

None beyond the paper's own contributions. The most notable cross-review observation is the asymmetry in empirical validation: the paper spends effort validating α (one of two key parameters) but entirely omits any measurement of κ, which enters at the 7th power. This gap is significant but becomes obvious upon careful reading rather than representing a novel synthesis.

## Suggestions

- **Measure κ empirically** on real attention matrices (across layers, heads, datasets, sequence lengths) to validate the second key theoretical condition. This is the single most important addition.
- **Add at least one approximate attention baseline** (e.g., Reformer or a fixed-sparsity pattern) to substantiate the claim of "outperforming existing methods."
- **Measure direct approximation error** (spectral norm or Frobenius norm of Att − Approx on a single layer) to bridge theory and experiments.
- **Include an ablation** removing the sortLSH component to quantify its contribution.
- **Report variance** (error bars, confidence intervals) for all numerical results.
- **Replace the Big-Theta in Algorithm 2** line 229 with a concrete constant or an explicit range.
- **Extend α validation to larger n** (e.g., 32k, 64k) to reduce the extrapolation gap.

## Score and Decision

The paper makes a genuine theoretical contribution: a simpler, provably near-linear time attention algorithm with relaxed assumptions, plus causal masking support absent from prior theoretical work. The algorithmic simplification (eliminating KDE in favor of uniform sampling) is clean and well-motivated.

However, the empirical evaluation has significant gaps for ICLR standards. The second key parameter κ is never measured. No approximate attention baselines are compared against. The spectral error guarantee is never tested. There are no ablations, no error bars, and key validation (α) stops at n=9k while claims extend to n=131k. The paper's own framing emphasizes "empirically verifiable" conditions and "outperforming existing methods," but the evidence does not match the scope of these claims.

The theoretical contribution is solid enough that the paper could be competitive with substantial additional empirical work (κ measurement, baselines, ablations, direct error measurement). In its current form, the empirical gaps are too large for acceptance at ICLR.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>