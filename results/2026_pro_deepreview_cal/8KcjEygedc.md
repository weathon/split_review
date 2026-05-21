Now I have sufficient calibration. Let me synthesize my final review.

**Calibration anchor summary:**

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| Maximizing Potential of Synthetic Data | I9Dsq0cVo9 | 5.50 | R1 | Direct predecessor; current paper extends with optimality theorem and broader validation |
| Strong Model Collapse | et5l9qPUhm | 8.00 | R1 | Same author; deeper theory on collapse, current paper broader but less deep on collapse |
| Exploring Learning Complexity | FN7n7JRjsk | 6.67 | R2 | Empirical pruning paper; current paper stronger theoretically |
| Severing Spurious Correlations | Bk13Qfu8Ru | 7.00 | R2 | Empirical pruning; different contribution type |
| GIO | 3NnfJnbJT2 | 7.00 | R2 | Empirical data selection; current paper more theoretical |

**Bracket:** Round 1 placed the paper between ~5.5 and ~8.0. Round 2 narrowed to ~5.5–7.0. The paper is clearly stronger than Firdoussi et al. (5.50) due to the novel optimality theorem and broader validation, but below the 7.0+ empirical papers due to some theoretical gaps and interpretive LLM connection. I place it at **6.0**.

---

## Summary

This paper develops a theoretical framework using random matrix theory to characterize when data curation (pruning) improves generalization in high-dimensional binary classification with ridge regression. The key theoretical contribution is an exact asymptotic test-error formula (Theorem 1) and a characterization of the optimal pruning strategy: a strong generator benefits from keeping hard examples ("less is more"), while a weak generator benefits from keeping easy examples (Theorem 2). The paper extends this to label-aware curation (Theorem 3) and validates predictions through synthetic simulations, ImageNet experiments, and interpretive connections to LLM reasoning benchmarks.

## Strengths

- **Theorem 1 provides a genuinely useful analytical tool**: the exact asymptotic test-error formula (Equation 9) compresses the effect of any symmetric pruning function into four interpretable scalar constants (Equation 8), enabling precise comparison of curation strategies within the framework.

- **Theorem 2 delivers a clean, non-obvious insight**: the optimal pruning strategy flips depending on generator quality — "keep hard" is optimal for a strong generator while "keep easy" is optimal for a weak generator. This is the paper's central conceptual contribution and it is well-motivated and proved.

- **Theorem 3 meaningfully extends the framework to label-aware curation**, which is the setting relevant to methods like LIMO and s1. The extension requires modifying only the key constants (Equation 13) while preserving the same analytical structure.

- **Synthetic validation is thorough and well-matched to theory**: Figure 1's 2×2 grid across data-scale × generator-quality shows close agreement between theoretical curves and empirical simulations, and correctly identifies the bottom-left quadrant (large n, strong generator) as the lone regime where aggressive pruning beats full-data training.

- **ImageNet experiments demonstrate generality**: Figure 2 shows a crossover from "keep easy" being better at small data scale (weak generator) to "keep hard" being better at large data scale (strong generator), reproducing the predicted phase transition in a real vision task, and Figure 3 shows curation preventing performance degradation in iterative pseudo-labeling.

## Weaknesses

### Fatal

None.

### Major

- **No optimality theorem for label-aware curation.** Theorem 2 characterizes the optimal pruning strategy for the label-agnostic setting, but no analog is provided for the label-aware setting of Theorem 3. Since the motivating real-world methods (LIMO, s1) are inherently label-aware — they filter on label correctness — this gap leaves the paper's central optimality result disconnected from its motivating applications. The LLM discussion in Section 4.2 must fall back on the label-agnostic Theorem 2 to interpret label-aware methods.

- **Incomplete synthetic validation of Theorem 2(B).** Theorem 2(B) states that for a poor generator with an excellent pruner, "keep easy" uniquely minimizes test error. Figure 1, presented as the theory validation, only compares "keep hard" against a random baseline across all four quadrants — it never evaluates "keep easy" in the poor-generator regime. The prediction that "keep easy" is optimal for weak generators is therefore untested in the synthetic setting that directly matches the theory's assumptions. The ImageNet experiments (Figure 2) do compare both strategies and show the predicted crossover, but these use deep models far from the Gaussian/linear assumptions of the theory.

### Minor

- **LLM connection is interpretive, not derived from the framework.** Section 4.2 uses the theory as a lens to interpret third-party benchmark tables (Tables 1 and 2), but no attempt is made to estimate the theoretical constants (ρ, ρ∗) in those settings, to verify that the curation strategies in LIMO/s1 correspond to the "keep hard" defined by the oracle projection x⊤w_o, or to rule out alternative explanations. The paper is honest about this being an interpretation ("our theory provides a novel explanation"), but the gap between the framework's requirements and the actual data used in those studies limits the strength of this contribution.

- **ImageNet experimental description lacks key details.** The paper does not specify the model architecture, how pseudo-labels are generated, how "keep easy" and "keep hard" are operationalized (e.g., threshold on confidence? margin?), or how error rates are computed. These omissions affect reproducibility and make it difficult to assess how closely the experiments instantiate the theoretical setup.

- **Limited engagement with prior theoretical pruning work.** Sorscher et al. (2022) is cited and its setup is mentioned as a special case, but the paper does not clearly contrast its theoretical predictions with the difficulty-score-based pruning analyzed there, nor with subsequent theoretical analyses of data pruning.

### Trivial

- Theorem 1's presentation in the main text is opaque: the Stieltjes transforms m, m̃, r and their relationship to the constants in Equation 8 are not explained, making it impossible for a reader to grasp the structure of the solution without consulting the (stripped) appendix.

- The paper repeatedly defers extensions (non-isotropic covariance, general results) to the appendix without even a sketch in the main text, making it hard to assess the scope of the theoretical insights.

## Nice-to-Haves

- Derive an analog of Theorem 2 for the label-aware setting — this would directly connect the optimality theory to LIMO/s1.
- Quantify ρ and ρ∗ in at least one LLM reasoning setting to move the Section 4.2 analysis from interpretive to derived.
- Include a direct "keep easy" curve in Figure 1's poor-generator panels to directly validate Theorem 2(B) in the synthetic setting.
- Provide a brief sketch or table in the main text showing how the constants p, γ, β, β̃ evaluate for the "keep hard" and "keep easy" strategies, so readers can see the pruning ratio and alignment parameters enter the test error without the appendix.
- Discuss how the isotropic and symmetric-pruning assumptions affect applicability to ImageNet and LLM settings.

## Removed Points

These points are flagged to be removed — treat them with caution.

- **Harsh critic #1: "Unsupported claim of analytical model‑collapse prevention."** The harsh critic claims the paper contains no analytical treatment of model collapse, only the empirical Figure 3. However, the paper explicitly references "Also see Appendix C" (line 172) in connection with model collapse. Per the review protocol, criticisms about content deferred to the stripped appendix are removed, as the material exists in the original submission.

- **Harsh critic #5: "Overclaiming in the abstract and introduction."** The harsh critic claims the paper does not deliver "exact scaling law curves" and "phase transition curves." But Theorem 1 does provide an exact asymptotic formula (with constants computable from Equation 8), and Theorem 2 does characterize a phase transition in optimal pruning strategy as a function of generator quality. The language is appropriate for what the paper delivers. The only genuine overclaim is the model-collapse point (addressed above), which relates to stripped appendix content.

- **Strength Finder: "Principled reconciliation of LLM reasoning paradoxes."** While the paper does provide an interpretive framework for LLM results, calling this a "principled reconciliation" overstates the contribution — no theoretical quantities are estimated, and the connection is asserted rather than derived. This strength is retained but with the caveat already noted under Minor Weaknesses.

- **Harsh critic section-by-section notes on limited discussion of symmetric pruning and isotropic assumptions.** The paper does acknowledge the isotropic simplification and notes that general results are in the appendix. This is a presentation preference, not a substantive weakness.

- **Harsh critic: "No comparison with existing theoretical work on data pruning beyond citing them."** This is partially valid (see Minor Weaknesses above) but the harsh critic's framing as a missing comparison is softened — the paper positions itself relative to Firdoussi et al. and Feng et al. clearly.

## Novel Insights

The paper's core insight — that the optimal curation strategy depends on generator quality in a cleanly characterizable way — is genuinely novel and well-supported by the theory. The identification that "keep hard" is only optimal when the generator is already strong while "keep easy" dominates for weak generators provides a principled explanation for the contradictory "less is more" vs. "more is more" findings in the literature. This reframes data curation from a heuristic to a principled decision governed by measurable quantities (ρ, ρ∗, n), which is a meaningful conceptual advance over prior work that treated curation strategies as universally applicable.

## Suggestions

- Prioritize deriving the label-aware optimality theorem — this is the most impactful missing piece, as it would directly connect the theory to LIMO/s1 without relying on the label-agnostic Theorem 2 as a proxy.
- For the LLM section, consider a small controlled experiment (even in simulation) where generator quality is systematically varied and both "keep easy" and "keep hard" are tested, rather than relying exclusively on third-party benchmark tables. This would demonstrate the framework's predictive power rather than just its interpretive flexibility.
- In the ImageNet experiments, specify the model, pseudo-labeling protocol, and how "keep easy/hard" thresholds are set. Even a brief footnote would substantially improve reproducibility.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>