Now I have all the information I need. Let me synthesize the final review.

---

## Summary

This paper proposes NSMP, a neural-symbolic message passing framework for Complex Query Answering (CQA) over Knowledge Graphs. NSMP integrates a frozen pre-trained neural link predictor with symbolic reasoning based on TensorLog-style adjacency matrices and fuzzy logic, and introduces a dynamic pruning strategy that prevents variable nodes from passing messages until their own state has been updated. The method requires no training on complex query datasets and claims interpretability via fuzzy set representations. Experiments on FB15k-237 and NELL995 show NSMP outperforms prior message-passing CQA models (LMPNN, CLMPT), achieves competitive results with the state-of-the-art neural-symbolic method FIT, and provides 2× to >150× speedup over FIT.

## Strengths

- **Novel integration of neural and symbolic reasoning in a message-passing CQA model.** The neural-symbolic message encoding function ϱ = N(f(ρ) + μ) genuinely fuses a neural component (inferred embeddings from the pre-trained link predictor, via ρ) with a symbolic component (TensorLog-style matrix operations, via μ). This is the first work to bring both modalities together within the message-passing paradigm for CQA, and the approach demonstrably works — NSMP outperforms all prior purely neural message-passing models (LMPNN, CLMPT) across both positive and negative query types (Tables 1, 2).

- **Dynamic pruning strategy validated by targeted ablation.** The dynamic pruning mechanism (Section 4.2.1) that filters messages from uninitialized variable nodes is directly ablated in Table 4. Removing it consistently lowers MRR across all settings (e.g., from 25.7 → 24.6 on BetaE positive queries), providing clean evidence that the strategy reduces noise and improves performance.

- **Clean empirical demonstration of efficiency gains over the state-of-the-art.** Figure 3 reports speedups of 2× to over 150× relative to FIT (Yin et al., 2024), with the largest gains on cyclic queries (69×–150×) where FIT's complexity becomes exponential. The complexity analysis (Section 4.3) correctly identifies the source: NSMP's O(|V|²) complexity for all query types vs. FIT's O(|γ|^n) on cyclic queries.

- **No training on complex query datasets.** NSMP uses a frozen pre-trained link predictor and has no trainable parameters (Section 4.2.3). This is a practical advantage over most neural CQA models, which require large, hard-to-collect complex-query training data.

## Weaknesses

### Fatal

None.

### Major

- **The paper's primary claimed contribution — the neural-symbolic integration — is not isolated or ablated.** The paper states that "for the first time, [it] integrates neural and symbolic reasoning within a message passing CQA model" and frames this integration as its central novelty. Yet the only ablation experiment (Table 4) tests dynamic pruning (w/o DP), not the integration itself. There is no experiment comparing NSMP (full) against a version that replaces ϱ with the purely neural component f(ρ) alone (keeping dynamic pruning and fuzzy aggregation), or against a version using only the symbolic component μ. Without this, a reader cannot assess whether the symbolic machinery adds value beyond the neural message passing, or whether the symbolic component dominates. The performance gains over prior neural message-passing models could plausibly come entirely from dynamic pruning and the specific fuzzy aggregation rules rather than from the integration per se. This is an evidential gap that weakens the paper's core thesis.

### Minor

- **The key hyperparameter λ (balancing neural and symbolic contributions, Eq. 19) is neither reported nor studied.** λ controls the relative weight of the symbolic fuzzy vector vs. the neural embedding similarity in the final answer. The paper provides no sensitivity analysis or default value. Given that the balance between neural and symbolic is central to the claimed contribution, the absence of this information is a concrete gap.

- **The argmax computation for the neural message encoding ρ (Eqs. 3–6) is underspecified.** The paper defines ρ as an argmax over the embedding space but does not describe how this is computed in practice (gradient descent, closed-form solution for linear scoring functions, etc.). It states "Following previous works (Wang et al., 2023c; Zhang et al., 2024a)," which is reasonable for a borrowed subroutine, but a brief explanation of how the argmax is tractable for ComplEx (e.g., the score without sigmoid is linear in the head embedding when the tail and relation are fixed) would make the paper more self-contained and reproducible.

- **No sensitivity analysis for the hyperparameter α in negated symbolic inference (Eq. 9–10).** α appears in the fuzzy negation formula but its value is never disclosed or studied.

- **Interpretability is claimed but not demonstrated.** The paper argues that fuzzy set representations provide interpretability (Sections 1, 4.1), but no qualitative example, visualization, or case study of intermediate fuzzy vectors is provided. This makes the interpretability claim aspirational rather than evidenced.

### Trivial

- **Notational ambiguity in f(ρ) (Eq. 11).** The function f is defined as taking the output of ρ as input, but the notation f(ρ) instead of f(ρ(...)) is ambiguous. Clarifying that f operates on the inferred embedding would help readability.

- **No justification for choosing the product t-norm (Hadamard product) over other fuzzy logic t-norms (e.g., minimum) for message aggregation (Eq. 17).** A brief rationale or citation would strengthen the presentation.

## Nice-to-Haves

- **Ablation of the neural-symbolic integration** (as described in the Major weakness) would be the single most impactful addition. Specifically: compare NSMP (full) against NSMP-neural-only (replace ϱ with f(ρ), no μ) and NSMP-symbolic-only (replace ϱ with μ, no f(ρ)), keeping dynamic pruning fixed.
- **A sensitivity study for λ** (e.g., varying λ ∈ {0, 0.25, 0.5, 0.75, 1} on a subset of queries) would show whether results are robust and how much each component contributes.
- **A concrete interpretability example** (e.g., top-5 entities in the fuzzy vector of an intermediate variable) would make the interpretability claim tangible.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"Similarity function S is never defined."** — Removed because the paper *does* define it at line 169: "Depending on the selected pre-trained neural link predictor, S can either be an inner-product-based or a distance-based scoring function." The critic missed this explicit statement.

2. **"Figure 3 does not compare inference time to other message-passing models (LMPNN, CLMPT)."** — Removed as scope creep. The efficiency comparison with FIT is the relevant one, since FIT is the state-of-the-art neural-symbolic competitor that NSMP is designed to improve upon. Comparing speed against prior message-passing models (which are already slower to train and require complex-query training) is not necessary to support the paper's efficiency claims.

3. **"The paper should include missing related works."** — Removed per policy: as a reviewer I cannot independently verify the existence of unmentioned works.

4. **Formatting and typographical nitpicks.** — Removed per policy; these are parser artifacts, not author errors.

## Novel Insights

None beyond the paper's own contributions. The reviews identify the same core contributions and gaps that the paper itself presents: the neural-symbolic integration and dynamic pruning strategy are clearly described, and the missing ablation for the integration is the main structural gap.

## Suggestions

1. **Run the neural-vs-symbolic ablation experiments** (NSMP-neural-only and NSMP-symbolic-only) to directly support the integration claim.
2. **Report the default values for λ and α and add a brief sensitivity study for λ.**
3. **Add 1–2 paragraphs describing how the argmax in ρ is computed** (e.g., noting that for ComplEx the score without sigmoid is linear, so the argmax reduces to a solvable linear system).
4. **Include a small qualitative example** showing the fuzzy vector for an intermediate variable node to make the interpretability claim concrete.

## Score and Decision

This is a solid method paper with a clear contribution: it is the first to combine neural link prediction with symbolic fuzzy-logic reasoning within the message-passing paradigm for CQA, and it demonstrates strong empirical performance with substantial efficiency gains over FIT. The dynamic pruning strategy is well-motivated and validated. The main weakness is that the paper's central claim—the value of the neural-symbolic integration—rests on a circumstantial case rather than a direct ablation. The missing λ value and α value are smaller but still notable gaps. These issues are addressable and do not invalidate the paper's core results, but they prevent the paper from being a strong accept.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>