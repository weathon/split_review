Here is the final consolidated review:

---

## Summary

This paper develops a theoretical framework for understanding when data curation (pruning) helps or hurts generalization in high-dimensional binary classification. Using random matrix theory, the authors derive exact asymptotic scaling laws for test error under both label-agnostic and label-aware curation with imperfect oracles, and prove a key phase transition: when the data generator is strong, "keep hard" is optimal (less is more); when the generator is weak, "keep easy" or full-data training is optimal (more is more). The theory is validated on synthetic data, used to reinterpret recent LLM reasoning findings (LIMO, s1), and connected to ImageNet experiments and model collapse mitigation.

## Strengths

- **Theorem 2 (Optimal Pruning Strategy, Section 3.1)** provides a clean, analytically-derived phase transition that precisely answers the paper's central question: when generator quality ρ → 1 and the pruner is excellent, the optimal strategy flips from "keep easy" to "keep hard." This is the paper's most important theoretical contribution — it gives a concrete condition for when "less is more" versus "more is more."

- **Theorem 1 (Exact Test Error, Section 3.1)** derives a computable closed-form expression for asymptotic test error under label-agnostic curation using RMT deterministic equivalents. This provides a principled foundation for analyzing any pruning strategy through the constants p, γ, β, β̃.

- **Synthetic validation (Figure 1)** shows good quantitative agreement between theoretical predictions and finite-sample empirical results across four distinct regimes (varying data size and generator quality). The bottom-left quadrant (large n, strong generator) clearly exhibits the predicted "less is more" optimum at p ≪ 1, which is the paper's signature result.

- **Reconciliation of contradictory LLM reasoning findings (Section 4.2)** offers a genuinely interesting conceptual unification: LIMO/s1 succeed on average AIME performance because the base LLM is a strong generator (ρ→1) for typical problems, while Sun et al.'s "more is more" finding on hard AIME questions follows because the same LLM is a weak generator (ρ<1) for the hardest problems. This demonstrates the explanatory value of the framework beyond its explicit assumptions.

- **Model collapse mitigation experiment (Figure 3)** demonstrates a concrete practical benefit: iterative "keep hard" pruning stabilizes performance across rounds of pseudo-labeling (~30% error maintained), while training on all data degrades to ~52%. This connects the theory to a timely problem.

- **Geometric alignment constants (ρ, ρ_*, ρ_g, τ, Section 2.3)** are well-motivated and provide intuitive, interpretable quantities that connect directly to test error through E_test = (1/π) arccos ρ.

## Weaknesses

### Major

- **Overclaiming on ImageNet experiments (Section 4.3).** The paper claims these experiments "confirm our theoretical predictions" and "demonstrate that the same principles apply to large-scale vision tasks." In reality, the ImageNet setup violates virtually every assumption of the theory (Gaussian features → natural images, binary classification → multi-class, isotropic covariance → structured features). The main text provides no architecture name, no implementation details for how "keep easy"/"keep hard" are operationalized for multi-class ImageNet, no pruning threshold α, and no attempt to estimate the theoretical quantities ρ, ρ_*, ρ_g from the data. The connection is qualitative at best. The paper's own Limitations section acknowledges this disconnect, yet the claims in Sections 1 and 4.3 are not calibrated to match that acknowledgment. **This is the most significant weakness** — the empirical section attempts to do more than the evidence supports.

- **LLM reasoning section (Section 4.2) is post-hoc interpretation, not validation.** The paper presents tables from existing work and offers a narrative interpretation in terms of ρ. This is a reasonable conceptual discussion, but it is not an experiment — no ρ or ρ_* is measured, no controlled pruning study is performed, and no quantitative prediction is tested. Presenting this section between the synthetic experiments (4.1) and the ImageNet experiments (4.3) gives it the rhetorical weight of empirical validation, which it does not carry. The paper's introduction and conclusion should not count this as part of the "empirical confirmation."

### Minor

- **Missing experimental parameters in the main text.** The synthetic experiments (Figure 1) report n=100 and n=5000 but never state the dimension d or aspect ratio φ = d/n, nor do they explain how the "theoretical predictions" (solid lines) are generated from Theorem 1 (the formula involves Stieltjes transforms m, m̃, r whose definitions are deferred to the appendix). While these details may be in the stripped appendix, the main text should be minimally self-contained on experimental parameters.

- **Theorem 2 is derived only in the limit φ→0, λ→0 (data-rich, unregularized).** The paper does not discuss whether the qualitative phase transition (keep-hard vs. keep-easy) holds for finite φ or nonzero λ, which limits the practical relevance of the optimality result.

- **No error bars on theoretical predictions.** The empirical results have error bars, but the theoretical solid lines in Figure 1 are plotted without any finite-sample confidence intervals. Since Theorem 1 is asymptotic, quantifying how well it approximates the finite-n setting would strengthen the comparison.

- **Pruning threshold α not discussed.** The "keep hard" and "keep easy" strategies depend on a threshold α that controls the fraction kept, but the paper does not explain how α is set in experiments — is it chosen to match the desired pruning ratio p, or selected separately?

### Trivial

None.

## Nice-to-Haves

- A controlled experiment that varies φ explicitly and shows how well the asymptotic theory tracks finite-sample behavior would significantly strengthen the synthetic validation.
- For the ImageNet results, even naming the architecture (e.g., ViT-B/16 pretrained on ImageNet) and specifying how margin-based pruning is defined for the multi-class setting would make the presentation substantially more informative.
- A discussion of whether the qualitative conclusions of Theorem 2 extend to finite φ and λ would help practitioners understand the scope of the optimality result.

## Removed Points

These points from the harsh critic were removed or downgraded:

- **"The paper never reports d or φ"** — The main text omits these values, but the paper states "For a comprehensive set of validations, please see Figure 4 and Appendix B," which likely contains these details. Since the appendix is stripped by the parser, this criticism is partly about missing appendix content. Downgraded from major to minor.
- **"No explanation of how theoretical curves are computed from Theorem 1"** — The theorem says "Details in appendix," which is standard for theory papers. Partially removed per hard rules about stripped appendix content.
- **Claim about LIMO/s1 papers not being cited with specific details** — The tables cite the original papers. Removed per hard rules.
- **Formatting/style nitpicks** — Removed per hard rules.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Calibrate the empirical claims.** Reframe the ImageNet and LLM sections as "qualitative connections" or "analogous phenomena" rather than "confirmations." The paper would be more honest and defensible if it clearly distinguished between the synthetic validation (which actually tests the theory) and the real-world connections (which illustrate the theory's conceptual reach). This change would address the paper's most significant weakness.
2. **Add experimental parameters to the main text.** Reporting d (or φ) for the synthetic experiments would take one line and eliminate a reproducibility concern.
3. **Briefly describe how theoretical curves are generated.** A one-sentence description (e.g., "The theoretical curves are the asymptotic expression from Theorem 1 evaluated at the empirical values of p, γ, β, β̃ for each pruning strategy") would make Figure 1 interpretable without requiring the reader to reconstruct the appendix machinery.
4. **Add a sentence on the scope of Theorem 2.** Acknowledging that the optimality result holds in the φ→0, λ→0 limit and noting whether it is expected to hold more broadly would be an honest and helpful qualification.

## Score and Decision

**Round 1 bracketing (wide):**

Between 3.0 and 8.0. The lower anchor (3.0 papers: "Disentangling the Roles of Representation and Selection in Data Pruning," "Geometric Median Matching for Robust Data Pruning") are empirical pruning papers with weak or absent theory — the current paper is clearly stronger. The upper anchor at ~7.5-8.0 ("Scaling Laws for Associative Memories," "How Feature Learning Can Improve Neural Scaling Laws") are more rigorous theory papers with deeper technical analysis — the current paper is weaker due to its thinner empirical validation and overclaiming.

**Round 1 bracket: [4, 7]**

**Round 2 narrowing:**

- Anchor I9Dsq0cVo9 (avg 5.50, "Maximizing the Potential of Synthetic Data: Insights from RMT") — This is the most directly comparable paper: same RMT methodology, similar Gaussian assumptions, similar gap between theory and practice. The current paper tackles a broader question (difficulty-based pruning vs. label verification only) and has cleaner phase-transition results, but overclaims more on its ImageNet experiments. The current paper is **slightly stronger** than this anchor.
- Anchor VB2WkqvFwF (avg 4.33, "The Underlying Scaling Laws and Universal Statistical Structure of Complex Datasets") — Purely empirical RMT analysis of datasets. The current paper has a much stronger theoretical contribution. **Clearly stronger.**
- Anchor DKkQtRMowq (avg 5.75, "Improving Data Efficiency via Curating LLM-Driven Rating Systems") — Empirical LLM data curation paper. Hard to compare directly, but comparable in quality. **Slightly weaker** in terms of practical relevance, **slightly stronger** in theoretical depth.
- Anchor S04xvGXjEs (avg 6.00, "Collective variables of neural networks") — Theory paper with weaker connection to practice. **Comparable.**
- Anchor Bk13Qfu8Ru (avg 7.00, "Severing Spurious Correlations with Data Pruning") — Strong empirical paper with clear practical impact. The current paper's empirical validation is **substantially weaker** than this anchor.
- Anchor dEypApI1MZ (avg 7.20, "How Feature Learning Can Improve Neural Scaling Laws") — Strong theory with rigorous empirical scaling law verification. **Weaker** than this anchor.

**Final calibration:** The paper sits between the 5.50 anchor (Firdoussi et al. RMT paper) and the 6.25-7.00 anchors. It is a legitimate theoretical contribution with a clean phase-transition result, but its empirical overclaiming and thin experimental descriptions in the main text hold it back. The theoretical work itself is solid and could be of lasting value.

**MY FINAL SCORE: <score>6.0</score>**
**MY FINAL DECISION: <decision>Accept</decision>**