Now I have a thorough understanding of the paper and calibration anchors. Let me write the consolidated review.

---

## Summary

This paper establishes a first-order equivalence between activation steering and influence functions: any activation steering vector can be represented as a signed influence re-weighting over training data, and conversely, any influence re-weighting admits a corresponding minimum-norm steering vector (the Influence-Aligned Steering vector, or IAS). The paper introduces a geometric diagnostic ω(x)—the cosine of the smallest principal angle between two Jacobian subspaces—that bounds the irreducible error of steering and tells practitioners when steering can fully substitute for weight-space edits. Additional results include a spectral-optimality recipe for maximizing logit change under a norm budget and a generalization bound for low-rank steering. Experiments verify the first-order equivalence (cosine ≈ 0.978), validate ω's monotonic increase with layer depth, compare IAS against CAA on detoxification, and demonstrate the spectral direction on ResNet-50.

## Strengths

- **Conceptual unification of two disconnected fields.** The paper bridges activation steering and influence functions under one first-order lens. While the underlying linear algebra is straightforward, the connection has not been made explicit before, and the unified framework yields productive downstream results (ω diagnostic, spectral optimality). This conceptual bridge is genuinely novel and useful to the interpretability community.

- **The ω(x) alignment diagnostic is practical and well-supported.** Theorem 5.1 gives a tight bound on steering error in terms of a single cheap-to-compute scalar. The empirical validation (Fig. 2, median ω rising from 0.64 to 0.94 across layers) confirms the theoretical prediction and provides an actionable layer-selection heuristic. This is the paper's strongest practical contribution — a principled "steer or retrain?" decision rule.

- **Strong first-order empirical verification.** Across 5,000 prompt–token pairs on GPT-2 Medium, the predicted IAS logit shift matches the actual shift with cosine 0.978 (Fig. 1), confirming the linear-regime theory holds well for small edits.

- **Generalization analysis for low-rank steering.** Theorem 6.1 bounds the Rademacher-complexity increase from rank-k IAS, showing the excess risk vanishes as width and sample size grow. This provides theoretical reassurance that low-rank steering does not catastrophically harm generalization — a practically relevant concern.

## Weaknesses

### Major

- **The steer-to-data mapping — one of the paper's three headline contributions — is never demonstrated.** The abstract and introduction prominently claim "a constructive algorithm for mapping undesired behaviors back to causal training examples" (contribution i). Corollary 1 states there exists an L1-minimal signed measure over training data. Section 4 says "see Section 7" for the practical payoff of identifying training examples. But Section 7 contains zero experiments validating this claim: no training examples are identified, no causality is verified, no connection is shown between a steering vector and specific data points. A paper whose introduction promises data provenance but whose experiments never deliver it has a significant gap between claims and evidence.

- **Insufficient experimental scope for the claimed contributions.** Beyond the missing steer-to-data experiment, the empirical section is thin. The spectral optimality experiment (Section 7.4) compares the spectral direction only against random directions — a low bar that any top eigenvector of a PSD matrix would clear. No comparison is made against existing steering baselines (e.g., CAA's mean-difference direction, gradient-based directions) for this claim. The detoxification experiment (Section 7.1) uses only GPT-2 Medium with a single layer choice, limiting generality. For a paper proposing a "unified framework" and a "practical workflow," the experiments provide only partial validation.

### Minor

- **Core equivalence rests on straightforward linear algebra.** The steer–influence duality follows directly from the chain-rule factorization: any Δh satisfying J_{h→y}Δh = J_{ω→y}Δω reproduces the logit shift of a parameter perturbation, and the minimum-norm solution is the Moore–Penrose pseudoinverse. This does not diminish the conceptual value of the bridge, but it means the paper's theoretical depth is modest — the subsequent bounds (principal angles, spectral optimality) are standard techniques applied to the resulting Jacobian matrices. The paper would benefit from acknowledging this simplicity more directly rather than presenting the equivalence as a deep theoretical result.

- **IAS underperforms CAA on the only direct comparison.** In Table 1, CAA achieves both lower toxicity (0.0150 vs. 0.0164) and lower perplexity (13,291 vs. 13,701) than IAS on GPT-2 Medium detoxification. The paper does not claim IAS is a superior steering method, but the result is presented without discussion, leaving the reader to wonder whether the theoretically principled IAS offers any practical advantage over a simpler heuristic. A brief analysis would strengthen the paper.

- **Scalability of the steer-to-data mapping is unaddressed.** Corollary 1 constructs an L1-minimal measure over the training set, which requires solving a linear program in |Z| variables — computationally infeasible at scale. The paper provides no approximation, heuristic, or small-scale demonstration. Without a feasible algorithm, the steer-to-data contribution remains purely conceptual.

- **Layer and hyperparameter choices lack sensitivity analysis.** Layer ℓ=8 for GPT-2 Medium is chosen via a heuristic (ω ≥ 0.7), and no sensitivity analysis is provided for the damping parameter φ. The ω heuristic itself is reasonable, but the paper would benefit from showing that results are not brittle to these choices.

### Trivial

- The affine independence assumption needed for uniqueness of the L1-minimal measure in Corollary 1 is stated but its plausibility in practice is not discussed.

## Nice-to-Haves

- A small-scale demonstration of the steer-to-data mapping (e.g., on a curated subset of 100–1,000 training examples) would go a long way toward validating the paper's central claim, even if the full-scale version remains computationally challenging.
- A comparison of the spectral direction against the mean-difference direction used in CAA (or a simple gradient-based direction) would strengthen the spectral optimality claim.
- An experiment following the claimed diagnostic workflow — use ω to decide whether to steer or edit weights, and show this decision improves outcomes — would demonstrate the practical value of the framework end-to-end.

## Removed Points

*These points were flagged for removal. Treat them with caution.*

- **"Triviality of the core equivalence" as a fatal flaw.** The harsh critic argued the equivalence is trivial linear algebra and thus not a novel contribution. While the math is indeed straightforward, the conceptual bridge between two disconnected research areas is genuinely novel, and the downstream diagnostic/optimization tools are not obvious consequences. Removed as a fatal criticism; retained as a minor observation.

- **"Experiments do not support claimed contributions — the only direct comparison is negative."** Partially removed. The claim that experiments provide *no* evidence is wrong: the first-order equivalence verification (cosine 0.978) and the layer-depth alignment analysis are positive, validating evidence. The remaining valid portion (undemonstrated steer-to-data mapping, thin spectral comparison) is retained in the Major and Minor sections.

- **"Key proofs are sketchy / rely on unjustified assumptions."** The harsh critic claimed affine independence is unverified. The paper states this as an explicit assumption for the L1-minimality uniqueness — this is standard practice for theoretical statements. The assumption is acknowledged. Removed as a substantive criticism; retained as a trivial note.

- **"The generalization bound adds little beyond prior art."** The paper explicitly credits Pinto et al. and the contribution is clearly scoped as an application of their result to the IAS setting. This is not claimed as a major novel contribution. Removed as a criticism.

- **"The No-Free-Lunch result is a repackaging of the same bound."** Theorem 6.2 is indeed a corollary of Theorem 5.1, which the paper presents transparently. This is not a weakness — it shows the same geometric quantity has both positive (alignment bound) and negative (impossibility) implications. Removed.

## Novel Insights

The most novel insight emerging from this work is that a single geometric quantity — the smallest principal angle cosine ω(x) between the activation–logit and parameter–logit Jacobian subspaces — serves as a unified certificate for both the fidelity of steering (when ω is large) and its impossibility (when ω is small). This collapses what previously required trial-and-error into one cheap computation, and the empirical validation that ω increases monotonically with layer depth provides an immediately actionable heuristic for practitioners. This diagnostic perspective — using subspace geometry to decide between inference-time and weight-space interventions — is not present in prior work and represents a genuine conceptual contribution beyond the linear-algebraic equivalence itself.

## Suggestions

- **Demonstrate the steer-to-data mapping, even at small scale.** This is the single most important improvement. Take a known steering vector (e.g., the toxicity-reducing vector), compute the top-weighted training examples via the L1-minimal measure construction on a tractable subset, and verify that those examples are semantically related to toxicity. Without this, the paper's most distinctive claimed contribution remains unvalidated.

- **Add a spectral-direction baseline comparison.** Compare the spectral direction from Theorem 5.3 against CAA's mean-difference direction and a naive gradient-based direction. The current comparison against random directions is insufficient to demonstrate practical value.

- **Discuss the CAA vs. IAS result in Table 1.** Acknowledge that IAS is not claimed to outperform existing steering methods, and explain what the reader should take away from the comparison (e.g., that IAS achieves comparable performance while providing theoretical guarantees that CAA lacks).

- **Provide a sensitivity analysis for φ and layer choice.** Even a brief ablation in an appendix would strengthen confidence in the results.

## Score and Decision

### Anchor comparison

| Path | Avg Human Score | Comparison to paper under review |
|------|-----------------|----------------------------------|
| `/home/wg25r/review_agent/human_reviews_2026/qQvaZ9yc9h.md` | 2.00 | Much weaker — scattered observations, no actionable items, insufficient evidence. Our paper has clear theoretical contributions and purposeful experiments. |
| `/home/wg25r/review_agent/human_reviews_2026/I3IeAZvxB4.md` | 3.33 | Weaker — automated AS method with limited scope and thin evaluation. Our paper has stronger theoretical grounding. |
| `/home/wg25r/review_agent/human_reviews_2026/XyQ5ui62mm.md` | 4.50 | Most comparable — unification paper (Bayesian framework for ICL + steering), 5-task empirical validation, rejected. Our paper has broader theoretical scope (any model) but weaker empirical execution and one undemonstrated headline claim. |
| `/home/wg25r/review_agent/human_reviews_2026/dGQubVJQx6.md` | 5.00 | Slightly stronger — identifiability theory for SAE concepts, both theoretical and empirical contributions. Our paper's empirical gaps place it below this anchor. |
| `/home/wg25r/review_agent/human_reviews_2026/JenMBia97B.md` | 5.50 | Stronger — more comprehensive experiments, accepted-contribution level. Our paper doesn't reach this empirical bar. |
| `/home/wg25r/review_agent/human_reviews_2026/YEBpZVm70i.md` | 5.50 | Stronger — substantial methodological contribution (BIF) with strong scaling results, accepted poster. |
| `/home/wg25r/review_agent/human_reviews_2026/EDPvNhTOLK.md` | 6.00 | Stronger — novel VI formulation for constrained IF, more substantial mathematical contribution. |
| `/home/wg25r/review_agent/human_reviews_2026/ZecACxqqKo.md` | 3.60 | Weaker — applied IF to SAM, limited novelty. Our paper has a more original conceptual bridge. |
| `/home/wg25r/review_agent/human_reviews_2026/8epkNiuAQC.md` | 4.67 | Comparable — stagewise data attribution with theory + experiments. Similar balance of theory and evidence; our paper has a larger gap between claims and experiments. |

The paper under review sits closest to the XyQ5ui62mm (4.50) and 8epkNiuAQC (4.67) anchors. It has a genuinely novel conceptual bridge and a practical diagnostic tool, but one of its three headline contributions is entirely undemonstrated and the experimental scope is limited. The ω(x) diagnostic and first-order equivalence verification are real strengths, and a revised version that demonstrates the steer-to-data mapping could merit a higher score. In its current form, the gap between claims and evidence is too large for acceptance.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>