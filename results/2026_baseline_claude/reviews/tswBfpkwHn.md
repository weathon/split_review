## Summary

This paper provides the first theoretical analysis of the training dynamics and in-context learning (ICL) generalization of a one-layer Mamba model, particularly in the presence of additive outliers in context examples. The key theoretical finding is that Mamba's nonlinear gating layer can suppress corrupted context examples, enabling robust ICL even when the fraction of outliers approaches 1, contrasted with a one-layer linear Transformer (obtained by removing the gating) that tolerates only α < 1/2. The paper further characterizes the ICL mechanism: linear attention selects examples sharing the query's relevant pattern (analogous to induction heads), while nonlinear gating suppresses outliers and introduces recency bias.

---

## Strengths

- **First training dynamics analysis for Mamba ICL.** Prior theory work on Mamba (Li et al., 2024b; 2025b) only analyzed loss landscapes (global minima), not whether SGD reliably finds them. Theorems 1–2 provide the first quantitative convergence and generalization guarantees for Mamba trained with corrupted prompts, filling a genuine theoretical gap.

- **Clean architectural isolation.** By unifying both models under formulation (3) and obtaining the linear Transformer as a special case (G = 1), the paper isolates exactly what nonlinear gating contributes. Theorems 3–4 for the Transformer follow the same proof template, making the comparison apples-to-apples with respect to the gating as the single variable.

- **Mechanistic characterization that explains observed phenomena.** Corollaries 1 and 2 provide concrete, quantitative descriptions of what each component learns: attention concentrates on same-pattern examples while gating values decay exponentially with index distance and collapse near zero on outlier-containing examples. This directly explains the empirical Mamba-outperforms-Transformer result on noisy regression reported by Park et al. (2024).

- **Robustness gap is sharp and theoretically grounded.** The contrast α < 1/2 (Transformer) versus α < min(1, p_a l_tr/l_ts) (Mamba) is not a loose bound artifact; it reflects the fundamental difference that nonlinear gating can push corrupted-example weights to near zero, while uniform gating cannot do better than majority vote. Experiments in Figure 2 precisely corroborate this threshold behavior.

- **Experiments directly test theoretically predicted thresholds.** Synthetic experiments confirm the α ≈ 1/2 breakdown for linear Transformers and the continued accuracy of Mamba up to α ≈ 0.8, as well as the exponential decay of gating values (Figure 4) and attention concentration (Figure 3), providing strong empirical evidence for the theoretical claims.

---

## Weaknesses

### Fatal
None.

### Major

1. **Comparison is against linear (not softmax) Transformer.** The paper establishes Mamba's superiority over a linear Transformer (G = 1), which is notably weaker than real Transformers using softmax attention. Softmax attention already implements a form of nonlinear weighting that may confer similar outlier suppression. While Remark 6 acknowledges this and mentions Appendix B.1 experiments, the main body theorems only compare to the weakest possible Transformer baseline. The claim "Mamba is theoretically more robust than Transformers" is therefore overstated relative to what the theory actually shows.

2. **Setting A = −I_m significantly restricts scope.** Real Mamba learns the state decay matrix A as a learnable parameter, and its input-dependent selection mechanism is the source of Mamba's expressiveness. Fixing A = −I_m makes all hidden dimensions decay at the same rate and removes the selectivity that distinguishes Mamba from earlier SSMs like S4. The theoretical insight about the gating thus applies to a model that is architecturally meaningful but less expressive than deployed Mamba. The paper needs stronger discussion of what properties of real Mamba this analysis captures versus misses.

### Minor

1. **The α → 1 robustness claim requires careful interpretation.** Condition (c) in Theorem 2 states α < min(1, p_a l_tr/l_ts). For α to approach 1, one needs either l_ts << l_tr (much shorter test prompts) or p_a → 1 (nearly all training examples corrupted). The latter contradicts Condition (8), which requires l_tr ≳ (1-p_a)^{-1} log M_1, growing as p_a → 1. The headline "α can approach 1" is technically valid but requires conditions that are not obviously practical. A clearer numerical example of achievable (p_a, α) pairs would clarify this.

2. **Test outlier constraint (Condition (a), Theorem 2) is non-trivial.** Requiring test outliers to be positive linear combinations of training outlier directions (summing to L > 0) excludes outliers that are orthogonal to all training outlier patterns. The practical range of this condition relative to real data poisoning attacks deserves more discussion.

3. **Experiments are exclusively synthetic.** All results use hand-crafted orthogonal patterns with known ground-truth structure. While sufficient to verify the theoretical predictions, even a small-scale natural language experiment (e.g., sentiment classification with injected trigger phrases as in the James Bond example of Figure 1) would substantially increase confidence in the practical relevance.

### Trivial
- The notation in Equation (11) defining V' has what appears to be a parsing issue (the condition "∑ λ_i v_i^* + ∑ λ_i ≥ L > 0") — the intended condition is likely ∑ λ_i ≥ L, but the text is ambiguous.

---

## Nice-to-Haves

- An experiment comparing Mamba with softmax-attention Transformer (not just linear Transformer) on the synthetic ICL task with outliers would directly address the main concern and quantify whether the theoretical gap is reflected empirically in more realistic models.
- A sensitivity analysis showing how the required batch size B_M (which exceeds B_T by a term involving V²κ_a^{-2}) scales with V (number of outlier patterns) would help practitioners understand training cost implications.
- Exploring what happens when test outliers lie outside the positive cone of training outlier patterns would clarify the boundary conditions of the robustness result.

---

## Novel Insights

The most genuinely novel mechanistic insight is the dual role of the Mamba gating weight w in the trained model: it must simultaneously (a) produce large σ(w^T p) on clean, same-pattern examples to promote them in the product-form gating, and (b) produce large σ(w^T p) on outlier-containing examples to suppress them (since large intermediate sigmoid values cause downstream products to be near zero via the complementary 1−σ(·) terms). This creates a beneficial asymmetry: outlier-heavy examples "burn" the gating budget of all subsequent context examples, but because outliers are detected early, clean same-pattern examples survive in the accumulation. This mechanism is absent from linear attention by definition and explains the α < 1/2 vs. α → 1 robustness gap in a structurally principled way. The analogy to induction heads (Corollary 1) in the context of linear attention is also a notable observation: different attention variants may converge to similar feature-selection strategies even when their architectural forms differ substantially.

---

## Suggestions

1. Revisit the wording around "Mamba can maintain robust ICL even when α → 1" — the abstract and introduction state this without the conditioning on p_a l_tr/l_ts ≥ 1, which could mislead readers about the generality of the result.
2. Provide at minimum a brief empirical comparison of Mamba vs. softmax-attention Transformer on the same synthetic setup (beyond linear Transformer) to make the theoretical comparison more practically grounded, even if the theory focuses on the linear case.
3. Add a clearer discussion of the gap between the analyzed Mamba (A = −I, one layer) and Mamba as deployed in practice, including which qualitative properties are expected to generalize and which may not.

---

## Score and Decision

The paper makes a genuine and technically non-trivial first step in the theoretical understanding of Mamba's ICL training dynamics. The characterization of the gating mechanism and its role in outlier suppression is insightful, and the theoretical comparison cleanly isolates the contribution of gating. The primary concern is that the comparison baseline (linear Transformer, not softmax) and the simplified model (A = −I) limit the scope of the conclusions relative to the headline claims. These are meaningful but not fatal weaknesses within the norms of theoretical ML analysis.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>