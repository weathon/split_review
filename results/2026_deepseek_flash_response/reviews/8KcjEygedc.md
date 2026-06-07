Now I'll write the final consolidated review.

## Summary

This paper develops a random-matrix-theory (RMT) framework to derive exact asymptotic test error formulas for high-dimensional binary classification under data curation (pruning). It analyzes label-agnostic and label-aware pruning rules and identifies a phase transition in optimal strategy: when the generator (labeler of training data) is strong (ρ→1) and the pruner is excellent (ρ_*→1), "keep hard" is optimal; when the generator is weak (ρ<1) but the pruner is excellent, "keep easy" is optimal. The paper presents synthetic validation, ImageNet experiments, and qualitative connections to LLM reasoning benchmarks.

## Strengths

1. **Exact asymptotic test error characterization under pruning (Theorem 1).** The paper provides a precise analytical formula for the test error of pruned ridge regression that goes beyond the empirical scaling-law observations of prior work (Sorscher et al., 2022). The RMT machinery is appropriate for this class of problems, and the synthetic experiments (Figure 1) show good agreement between theory and finite-sample simulation across multiple regimes.

2. **Analytical phase transition in optimal pruning strategy (Theorem 2).** The result that "keep hard" is optimal when ρ→1 and "keep easy" when ρ<1 (under an excellent pruner) provides a mathematically precise condition for a phenomenon that has previously been discussed only empirically. This insight cleanly unifies seemingly contradictory heuristics.

3. **Extension to label-aware curation (Theorem 3).** The generalization of the analysis to pruning rules that combine difficulty and correctness subsumes prior work (Feng et al., 2025; Firdoussi et al., 2024) as a special case, creating a more general theoretical framework.

4. **Unified interpretive lens for contradictory LLM findings.** Section 4.2 shows that the opposing results of LIMO/s1 ("less is more" on average AIME performance) and Sun et al. ("more is more" on hard AIME questions) are both consistent with the theory: the same base model acts as a strong generator for average problems but a weak generator for the hardest ones, so different strategies become optimal. This qualitative unification is valuable even if not quantitatively rigorous.

## Weaknesses

### Major

1. **Theorem 2 (the headline optimality result) is proven only in the φ→0 (n≫d) limit, which is inadequately communicated.** The functional F(q) in Eqn (12) is defined via the triple limit φ→0, λ→0, d,n→∞ with d/n→φ. This regime (n much larger than d) is the classical low-dimensional regime, distinct from the proportional-limit regime φ∈(0,∞) that motivates the paper's RMT framework. The paper does not state whether Theorem 2 holds for φ>0, how the phase transition shifts with φ, or even clarify that the theoretical curves in Figures 1–3 come from the finite-φ formula (Theorem 1) or the φ→0 formula (Theorem 2). This creates an unacknowledged gap between the proven optimality result and the experiments presented as validating it.

2. **The claim to "show analytically that data curation can avert model collapse" overstates what is delivered.** The paper's contribution list asserts establishing "phase boundaries where uncurated training diverges while curated training remains stable." However, Theorems 1–3 analyze only a single round of pruning with a fixed generator (w_g). The iterative dynamics of self-training — where the generator changes at each round — are not analyzed theoretically. The only support is a single experiment (Figure 3) comparing "keep hard" against "all data," without baselines like random pruning or "keep easy" in the iterative setting. The analytical claim about model collapse is not supported by the paper's theoretical framework.

3. **The LLM reasoning analysis (Section 4.2) is purely qualitative and does not constitute the "rigorous justification" claimed in the contributions.** While the contribution list promises "a rigorous justification for why methods like LIMO and s1 succeed," Section 4.2 only provides a verbal reinterpretation of existing benchmark numbers in terms of ρ. No quantities from the theory (ρ, ρ_*, ρ_g, φ, p, or test error curves) are estimated or fitted to the LLM data. There is no quantitative demonstration that the crossover is consistent with the theory's predictions. The paper should either reframe this as a qualitative discussion or add quantitative evidence.

### Minor

4. **The ImageNet experiments (Section 4.3) lack detail for reproducibility and rigorous validation.** The main text does not specify the model architecture, how "hard"/"easy" was operationally defined on images, the dimensionality d, the number of trials, or the regularization λ used. While Appendix B is referenced for "comprehensive validations," it was stripped by the parser. The main text alone provides only a high-level description insufficient for empirical confirmation.

5. **The synthetic experiments (Section 4.1) do not state the dimensionality d**, so the aspect ratio φ = d/n cannot be determined. Since the theory depends critically on φ and the phase transition is claimed to depend on data scale, this omission is relevant for interpreting the match between theory and simulation.

6. **Theorem 2 assumes ρ_*→1 (excellent pruner) in both cases**, limiting its practical scope. The paper does not discuss what happens with a moderate or poor pruner, which is the common case in practice.

7. **The conceptual gap between "difficulty" in the Gaussian model (margin |x^⊤w_o| to a linear boundary) and "difficulty" in LLM reasoning (problem-solving complexity) is not addressed.** The paper asserts the connection without justification, weakening the claimed analogy between the theory and the LLM results.

### Trivial

None.

## Nice-to-Haves

- A finite-φ analysis of the optimal pruning strategy (using the general formula from Theorem 1), or at minimum a numerical investigation showing the phase transition persists at finite φ.
- Estimating ρ from LLM benchmarks to provide quantitative support for the LLM analysis, or reframing Section 4.2 as qualitative discussion rather than validation.
- Including the ImageNet setup details (architecture, difficulty metric) in the main text.

## Removed Points

- **Harsh Critic point about RMT technical challenge (dependence between p_i and x_i):** The critic notes the dependence between p_i and x_i makes the resolvent analysis non-trivial. This is a standard technical detail in RMT work; the paper is not required to discuss every technical challenge in the main text. Removed as a non-issue.
- **Harsh Critic point about LLM tables using different metrics (Pass@1 vs Avg@8):** This is a minor formatting detail that doesn't affect the paper's claims.
- **Harsh Critic point about squared loss for binary classification:** The paper's limitations section already acknowledges the simplified setting. This is scope-appropriate for a theoretical paper.
- **Strength Finder point about "analytical demonstration that pruning can avert model collapse":** This conflicts with Major Weakness #2 above. Removed because the claimed strength is not supported by the paper's theoretical content.
- **Strength Finder claim that the paper "establishes phase boundaries where uncurated training diverges while curated training remains stable":** Overstated given that no theoretical analysis of iterative dynamics is provided. Removed as conflicting with verified weakness.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

The paper's strongest asset is its theoretical core (RMT analysis of pruned ridge regression with difficulty-based and correctness-based oracles). To strengthen the paper, the authors should: (1) clearly communicate the φ→0 scope of Theorem 2 and ideally provide finite-φ numerical validation that the qualitative pattern persists; (2) either add quantitative evidence to the LLM section or honestly reframe it as interpretive discussion rather than "rigorous justification"; (3) remove or substantially qualify the model collapse claim since no theoretical analysis of iterative dynamics is provided; (4) add experimental details (architecture, difficulty metric, d, trials) for ImageNet to the main text.

## Calibration Anchors

**Round 1 — Bracketing (all queries on "theoretical analysis of data pruning/curation in high-dimensional learning RMT"):**

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| EOPLy80bBm — Disentangling Roles of Representation and Selection in Data Pruning | 3.00 | R1 | Weaker paper; more empirical, less theoretical depth |
| e2F0mJJeN0 — Geometric Median Matching for Robust Data Pruning | 3.00 | R1 | Weaker paper; lacks the RMT theoretical machinery |
| I9Dsq0cVo9 — Maximizing Potential of Synthetic Data: Insights from RMT | 5.50 | R1 | **Most comparable** — same methodology (RMT for pruned binary classification), similar Gaussian assumptions, similar gap-to-practice concerns. My paper has slightly more overclaims and less thorough empirical validation. |
| FT4gAPFsQd — How Sparse Can We Prune A Deep Network | 6.00 | R1 | Stronger empirical validation than my paper |
| et5l9qPUhm — Strong Model Collapse | 8.00 | R1 | Significantly stronger — cleaner theory, better validated |
| Bk13Qfu8Ru — Severing Spurious Correlations with Data Pruning | 7.00 | R1 | Different focus; stronger experiments |
| VB2WkqvFwF — Underlying Scaling Laws of Complex Datasets | 4.33 | R2 | Less focused on actionable theoretical results |
| 93XT0lKOct — Data Pruning by Information Maximization | 6.00 | R2 | Method paper; more thorough experiments |
| DKkQtRMowq — Improving Data Efficiency via Curating LLM-Driven Rating Systems | 5.75 | R2 | Stronger empirical component |

**Bracket:** Round 1 placed the paper between 4.0 and 6.0. Round 2 narrowed this by comparison with the most directly comparable anchor (Maximizing Synthetic Data via RMT, avg 5.50). My paper has comparable theoretical depth but more overclaims and sparser experimental details, placing it slightly below this anchor.

**Final Score: 5.0**

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>