Now let me write the final review, integrating the verified information.

## Summary

This paper establishes a theoretical framework connecting certified machine unlearning with ℓ₂-regularized continual learning. It decomposes the post-unlearning excess risk into two components—continual learning excess risk and unlearning loss—and provides bounds for both. The paper adapts gradient-based (natural forgetting) and Hessian-based certified unlearning methods to the continual learning setting, deriving approximation error bounds and noise mechanisms for (ε,δ)-certified guarantees. Experiments on MNIST with a linear softmax model are presented.

## Strengths

1. **Novel problem framing and theoretical decomposition.** The paper is the first to formally connect certified unlearning with continual learning under a unified framework. Decomposing post-unlearning excess risk into a continual-learning excess-risk term (Equation 7) and an unlearning-loss term (Equation 6) is a clean and insightful formulation that provides a principled way to analyze the trade-off between retention and forgetting.

2. **Extension of excess-risk bounds to nonlinear convex models.** Theorem 3.1 (Equation 8) extends prior linear-model analysis (Lin et al., 2023) to strongly convex losses in ℓ₂-regularized continual learning, providing an explicit upper bound that captures task heterogeneity and sample-size effects.

3. **Two adaptation algorithms with theoretical guarantees.** Theorem 4.1 adapts gradient-based certified unlearning to continual learning by leveraging the natural forgetting of ℓ₂-regularized updates, achieving zero storage overhead. Propositions 5.1 and 5.2 adapt Hessian-based unlearning with a tighter second-order bound under Hessian-Lipschitz smoothness. Both come with explicit approximation-error bounds that determine the noise for (ε,δ)-certification.

4. **Trade-off analysis between unlearning and continual learning.** The paper correctly identifies that the regularization parameter λ affects excess risk and unlearning loss in opposite directions, and that the Hessian-based method introduces a dependence on unlearning request ordering. The forgetting-enhanced Hessian method (Section 5.3) provides a storage–accuracy trade-off.

## Weaknesses

### Fatal
None.

### Major

1. **The central comparative claim is contradicted by the paper's own experimental evidence.** The abstract and contributions state that the Hessian-based algorithm "largely outperforms" the gradient-based algorithm and "achieves lower unlearning loss." However, Figure 2(b) shows the opposite: the natural forgetting algorithm achieves a lower approximation error (unlearning loss) across *all* reported λ values (~0.08–0.10 vs. ~0.20–0.24 for the Hessian algorithm). The Hessian algorithm never outperforms natural forgetting on this metric in the presented experiment. No accuracy comparison for post-unlearning excess risk between the two algorithms is provided either (Table 1 shows only the Hessian algorithm). This mismatch between claim and evidence is a fundamental presentational failure that must be resolved.

2. **Hessian-based algorithm exceeding the retrain baseline is unexplained and raises concerns about experimental methodology.** In Table 1, at λ=30 the Hessian-based algorithm achieves 71.59% accuracy while perfect retraining achieves only 71.05%. Since the algorithm is designed to approximate the retrained model, consistently exceeding retraining (without error bars or multiple runs) suggests either an artifact in the evaluation setup or a meaningful phenomenon that is not discussed. The paper provides no comment on this discrepancy.

3. **Theorem 3.1 contains index errors that make the bound trivially incorrect as written.** Equation (8) includes the terms `ρ^{τ_j - τ_j} ||w_{τ_j}^* - w_{τ_j}^*||` (which equals 1 × 0 = 0) and `L ρ^{τ_k} Σ_{i=2}^k ||w_{τ_i}^* - w_{τ_i}^*||` (also 0). These are clearly typesetting errors where distinct indices (e.g., τ_i and τ_j) collapsed into identical indices. While the intended meaning is likely correct, the bound as printed is mathematically wrong, and a reader cannot assess its actual form without guessing the intended index substitution.

### Minor

1. **Experimental evaluation is too limited to validate the theoretical claims.** The experiments use only MNIST with a linear softmax model. Cross-entropy loss is not μ-strongly convex (Assumption 2.1), which the paper acknowledges but does not justify beyond "showing more general results." There are no error bars, confidence intervals, or multiple random seeds. Only one unlearning sequence pattern is shown in the main text (the sequence table is in the appendix, stripped by the parser). The forgetting-enhanced Hessian method (Section 5.3) receives no experimental evaluation despite being presented as a contribution.

2. **The "exact second-order approximation" claim (Section 5.1) is overstated.** The paper states that Algorithm 2 "robustly achieves an exact second-order approximation to the retrained model for any unlearning sequence," but Propositions 5.1 and 5.2 provide first-order and second-order *upper bounds*, not exactness. The transition from the Taylor-expansion sketch to the complex update rule (13) could benefit from clearer exposition.

3. **No comparison to prior continual-learning unlearning work.** The paper cites Liu et al. (2022) and Chatterjee et al. (2024) as heuristic prior work but does not compare against them experimentally, making it difficult to contextualize the practical significance of the certified guarantees.

### Trivial

- None beyond the index issues in Theorem 3.1 (listed as Major because it affects interpretability of the bound).

## Nice-to-Haves

- Provide post-unlearning excess risk (accuracy) for *both* algorithms in Table 1, not just the Hessian-based method, to enable a direct comparison.
- Evaluate the forgetting-enhanced Hessian method (Section 5.3) experimentally to support its claimed contribution.
- Include error bars or confidence intervals based on multiple random seeds.
- Report accuracy at multiple ε,δ settings rather than a single noise regime.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Harsh Critic Issue 3 (derivation of Equation 9).** The critic questions whether subtracting deleted tasks from the exponent in ρ^{t-s-n} is justified. This reasoning is intuitively correct: deleted tasks asymmetrically affect the two models, and subtracting them from the exponent makes ρ^{·} larger, which correctly increases the bound. The formula is consistent with the intended intuition. The proof is in the appendix (stripped by the parser), which the main paper references. This is not a demonstrated error.
- **Harsh Critic's claim that the Hessian algorithm "becomes marginally better" at λ > 40.** The figure description shows natural forgetting at ~0.08 and Hessian at ~0.20 for λ ≥ 40. The Hessian algorithm is *never* better. The critic misread the figure. The valid core of the criticism (claim contradicts evidence) is kept in Major weakness 1.
- **Strength Finder's claim about "Table 2 in Appendix E."** This is a reference to the appendix, which was stripped. The content exists in the original submission. I keep the core observation (limited unlearning sequences shown in main text) as Minor weakness 1.
- **Harsh Critic's point about "missing error bars."** Partially valid; kept as Minor weakness 1 (merged with other experimental limitations).
- **Strength Finder's strengths that are generic/overly broad.** Dropped generic praise (e.g., "timely problem," "well-illustrated Figure 1") that lacked specific evidence anchors. The concrete, evidenced strengths are retained.

## Novel Insights

None beyond the paper's own contributions. The key insight—decomposing post-unlearning excess risk into continual-learning excess risk and unlearning loss—is the paper's own framing, and no reviewer surfaced a genuinely different perspective on the work.

## Suggestions

1. **Fix the central claim contradiction.** Either revise the claim about Hessian-based outperformance to be consistent with the evidence, or provide additional experiments (across multiple λ values with error bars) that demonstrate the Hessian method's advantage on post-unlearning excess risk (not just unlearning loss). The conclusion, abstract, and contributions must be aligned with what the data show.

2. **Correct the index errors in Theorem 3.1.** The terms ρ^{τ_j-τ_j} and ||w_{τ_j}^* - w_{τ_j}^*|| should involve distinct indices (e.g., τ_i and τ_j).

3. **Explain the Hessian-exceeding-retrain result in Table 1.** If this is due to randomness, provide error bars. If there is a systematic reason (e.g., different evaluation procedure), document it clearly.

4. **Expand the experimental evaluation.** Add at minimum: (a) accuracy comparison for both algorithms on post-unlearning excess risk, (b) multiple random seeds with standard deviations, (c) at least one additional dataset (e.g., CIFAR-10), and (d) evaluation of the forgetting-enhanced Hessian method from Section 5.3.

5. **Tone down the "exact" claim** for the Hessian-based algorithm—the bounds are approximation guarantees, not exactness.

## Score and Decision

**Calibration report:**

*Round 1 (bracketing):* Three queries on certified unlearning theory and CL theory.
- Low band (<3.5): e.g., hvTFoDsgCe (avg 2.50), PS0YpCMzkb (avg 2.00), WNUDOLYlbh (avg 3.00)
- Middle band (3.5–7.5): r6Z3BXDrzO — "Impossibility of Retrain Equivalence" (avg 4.50, Reject); IPqUBL4R9x — "Distributional Machine Unlearning" (avg 6.00, Accept); vT5ZpD7AB4 — "Robust Certified Unlearning Under Distribution Shift" (avg 4.50, Reject); zZZKAytEGm — "Why Some Models Resist Unlearning" (avg 4.00, Reject)
- Upper band (>7.5): oBXfPyi47m (avg 8.00, RL paper, unrelated)

*Round-1 bracket:* [4.0, 6.0]

*Round 2 (narrowing):* Topic-anchored queries within (4.0, 6.0) and (3.5, 5.5).
- hWw269fPov — "PAC-Bayes bounds for cumulative loss in CL" (avg 5.33, Accept Poster). Stronger experiments than the paper under review.
- NE2yIxdo1w — "Forgetting and Generalization in CL via NTK" (avg 5.50, Accept Poster). Stronger experiments and more thorough validation.
- DqvnwRe1Vw — "The Illusion of Forgetting" (avg 4.00, Withdrawn/Reject).

*Comparison:* The paper under review has a more novel problem framing than any of these anchors (first to connect certified unlearning with CL), but its experimental validation is substantially weaker than the 5+ anchors. The claim-evidence mismatch is a significant weakness not present in those papers. The paper is comparable to the 4.5-range anchors (r6Z3BXDrzO, vT5ZpD7AB4) in overall quality.

*Final score:* **4.5** — the theoretical contribution is genuine and the problem framing is timely, but the experimental evaluation is insufficient to validate the claims, and a central claim is contradicted by the presented evidence. Major revisions are required.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>