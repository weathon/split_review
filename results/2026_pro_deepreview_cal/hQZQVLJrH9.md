## Summary

This paper establishes a first-order equivalence between activation steering and influence functions, two previously disconnected techniques for controlling and interpreting neural networks. The authors construct an "Influence-Aligned Steering" (IAS) vector that reproduces the logit shift of any influence-based parameter update, prove a converse mapping, and introduce a geometric diagnostic γ that determines when steering can faithfully substitute for weight-space editing. The framework is supported by empirical evidence showing near-perfect collinearity (cosine 0.978) between predicted and actual logit shifts across 5000 token pairs.

## Strengths

- **Genuinely novel theoretical connection.** The paper bridges two active but separate research areas (activation steering and influence functions) under a unified first-order framework. Theorem 4.2 establishes a closed-form mapping from any steering vector to a signed training-data measure and vice versa — this is not an incremental extension but a new conceptual link. The near-perfect cosine of 0.978 in Figure 1 across 5000 prompt–token pairs provides strong quantitative evidence that the IAS construction works as claimed.

- **Practical geometric diagnostic.** The scalar γ(x) — the cosine of the smallest principal angle between activation-to-logit and parameter-to-logit Jacobian subspaces — provides an intuitive, computable feasibility check for when steering can replace weight-space editing. Theorem 5.1 bounds the logit error by √(1−γ²), and the monotonic increase of γ with layer depth (0.64 to 0.94, Figure 2) confirms the diagnostic's practical utility and yields a simple layer-selection heuristic.

- **Generalization bounds for low-rank steering.** Theorem 6.1 quantifies the Rademacher-complexity cost of adding a rank-k IAS correction, showing it vanishes as width d and sample size n grow. This provides theoretical reassurance that activation steering need not catastrophically hurt generalization, and offers practical guidance (prefer low k, small α).

## Weaknesses

### Fatal
None.

### Major

- **Incomplete proof for ℓ₁-minimality claim (Corollary 1).** Corollary 1 asserts that the signed measure ρ_s constructed from a steering vector has minimal ℓ₁ norm among all measures that reproduce the same first-order logit shift. The proof sketch — "if another measure achieved the same shift with smaller ℓ₁ norm, one could scale ρ_s down and still match the shift, contradicting α as steering magnitude" — does not establish optimality. The argument conflates ρ_s's norm with α without proving that any competing measure ν must satisfy ||ν||₁ ≥ |α|. This claim is central to the paper's practical promise of pinpointing the "fewest" training examples, and its validity remains unestablished as written. A proper proof or a weaker, qualified statement is needed.

- **Unclear objective in spectral optimality theorem (Theorem 5.3).** The theorem states that the top eigenvector of Σ maximizes "the expected first-order logit change," but never specifies the expectation's distribution or the precise optimization objective. The quantity being maximized appears to involve a specific test input x (via ||∇_h f_θ(x)||), yet Σ is constructed from per-example influence quantities g_z averaged over the training set, with no explicit dependence on x. The link between the optimization problem and the eigenvector recipe is stated rather than derived, leaving the result's interpretation and practical grounding unclear. The experiment (Figure 3) only compares the spectral direction against random directions, not against any competitive baseline, so the practical advantage over simpler alternatives is not demonstrated.

- **Ambiguous statement of the No-Free-Lunch theorem (Theorem 6.2).** The theorem claims that for every activation perturbation Δh and "the corresponding (best-possible) parameter perturbation Δθ," the ratio ||J_{h→y} Δh|| / ||J_{θ→y} Δθ|| is bounded by γ(x). The phrase "corresponding (best-possible) parameter perturbation" is never defined, making the theorem uninterpretable. Does it mean the minimum-norm Δθ achieving the same logit shift as Δh? Or vice versa? Without a precise definition, the result's meaning and implications cannot be assessed.

- **Missing data-attribution experiments.** The paper's most distinctive practical promise — mapping a steering vector back to causal training examples via the measure ρ_s — is never demonstrated. No top-weighted training documents are shown, no case study traces a behavior (e.g., toxicity) to specific training examples, and no quantitative evaluation of attribution quality is provided. This capability is highlighted in the abstract, Section 4, and Corollary 1 as a key contribution, but it remains entirely aspirational in the empirical sections.

### Minor

- **Algebraic error in Eq. (2) (Section 3.2).** The dual derivation states λ* = -(J_{h→y} J_{h→y}^T)^† J_{θ→y} Δθ and Δh* = J_{h→y}^T J_{θ→y} Δθ. Substituting the λ* expression into Δh* = J_{h→y}^T λ* yields Δh* = -J_{h→y}^T (J_{h→y} J_{h→y}^T)^† J_{θ→y} Δθ, not J_{h→y}^T J_{θ→y} Δθ. The pseudoinverse is missing. Theorem 5.2 later states the correct form (J_{h→y}^†), so this is a presentation error rather than a fundamental mistake, but it occurs in the paper's central IAS construction and should be corrected.

- **Spectral experiment lacks baselines (Figure 3).** The ResNet-50 experiment shows the spectral direction produces a shift far outside random (p≈0.005), but provides no comparison to natural baselines such as the top singular vector of J_{h→y} or standard steering vectors. Without such comparisons, the evidence supports only that the spectral direction is "not random," not that it is practically superior.

- **Detoxification experiment does not evaluate the framework's distinctive claims (Table 1).** The GPT-2 detoxification comparison (IAS vs. CAA) is a standard steering evaluation. It does not measure γ, does not construct ρ_s to trace toxicity back to training examples, and does not test the spectral direction from Theorem 5.3. The result shows IAS works comparably to CAA, which is useful but does not validate what makes this paper different from existing steering work.

- **Slope deviation in Figure 1 not discussed.** The predicted vs. actual logit shifts show a slope of 1.50 rather than 1.0 — the actual shift is systematically 50% larger than the first-order prediction. While the cosine (0.978) confirms collinearity, the systematic scaling discrepancy might indicate higher-order effects that could affect the duality constructions at practical steering magnitudes. The paper would benefit from discussing this.

### Trivial

- The dual variable λ* is introduced as a "Fisher-metric certificate of effort" and a pre-check for steer-vs-retrain decisions (Section 3.2), but is not computed or used in any experiment.

## Nice-to-Haves

- Quantify the residual from Theorem 4.2 in a realistic setting (beyond the bound in Eq. 3) to give practitioners a sense of when the steering–influence equivalence degrades meaningfully.
- Compare the spectral steering direction against the principal singular vector of J_{h→y} to justify the additional complexity of constructing Σ.
- Discuss the sensitivity of the IAS construction to the damping parameter λ and to the Gauss-Newton approximation, particularly for architectures beyond GPT-2.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Harsh critic claim: "The paper does not discuss sensitivity to damping parameter λ or Gauss-Newton approximation."** The paper references Appendix D.1 for damping and explicitly notes that replacing H with a Gauss-Newton approximation does not change the first-order theory (Section 2). The appendix is stripped in this version but exists in the original. While more discussion would help, this is not a missing element.

- **Harsh critic claim: "Explicit algorithmic procedure for constructing ρ_s is missing."** The paper describes the construction in Section 4 and Corollary 1. The level of detail, while not fully algorithmic, is sufficient for a theoretical paper. This is a style preference, not a substantive gap.

- **Harsh critic speculation about Theorem 6.2 "reversing the intended message."** The harsh critic speculates about what the theorem "should" be saying. The real issue is the undefined term ("best-possible parameter perturbation"), which is already captured as a major weakness. The speculation about direction reversal is removed.

- **Strength Finder claim: "Spectral optimality provides a principled method."** Weakened. The theorem statement is unclear and the experiment lacks baselines, substantially reducing the strength of this contribution. The basic idea is interesting but not well-executed.

## Novel Insights

The most striking empirical finding is the near-perfect collinearity (cosine 0.978) between IAS-predicted and actual logit shifts at non-infinitesimal steering magnitudes. This goes beyond simply confirming linearity; it suggests that the activation-to-logit Jacobian captures nearly all the directional information needed to map between steering and influence, even when the scaling deviates from unity (slope 1.50). This implies that the principal-angle diagnostic γ may be the right summary statistic for deciding between activation-space and weight-space editing, and that the fundamental geometry — not just first-order approximation quality — determines when steering can substitute for retraining.

## Suggestions

- **Repair Corollary 1:** Either provide a rigorous proof under the stated affine-independence assumption (likely involving uniqueness of the representation, not the scaling argument in the sketch) or restate the result as "ρ_s is one natural measure achieving the shift with ℓ₁ norm |α|" without claiming minimality.
- **Clarify Theorem 5.3:** Explicitly define the expectation and state the optimization problem being solved. Derive the connection to Σ from first principles rather than asserting it.
- **Clarify Theorem 6.2:** Define "corresponding (best-possible) parameter perturbation" precisely, e.g., as the minimum-norm Δθ satisfying J_{θ→y} Δθ = J_{h→y} Δh, and verify the inequality direction.
- **Demonstrate data attribution:** Add at minimum one qualitative example showing that a toxicity-reducing steering vector highlights genuinely toxic training documents via ρ_s. This is the paper's most distinctive promised capability and its absence is the largest empirical gap.
- **Add a baseline to Figure 3:** Compare the spectral direction against the top singular vector of J_{h→y} (or a standard CAA vector) to quantify whether the influence-derived direction offers a nontrivial advantage.
- **Fix Eq. (2):** Correct Δh* to include the pseudoinverse, matching the λ* expression and Theorem 5.2.

## Score and Decision

**Calibration anchors considered:**

| Paper | Score | Round | Comparison |
|-------|-------|-------|------------|
| Measuring Effects of Steered Representation | 3.00 | R1 | Our paper is substantially stronger — genuine theoretical novelty vs. incremental empirical study |
| Weak Correlations as Principle for Linearization | 2.33 | R1 | Our paper is far stronger — clear claims and evidence vs. vague theory |
| From Steering Vectors to Conceptors | 5.00 | R1, R2 | Our paper has more novel theory (steering↔influence vs. generalization of existing steering) and stronger core evidence (cosine 0.978) |
| Steering LLMs with Activation Engineering (CAA) | 5.00 | R2 | Different paper type — CAA is a practical method paper; ours is theoretical. Our paper has more conceptual novelty but comparable experimental completeness issues |
| Versatile Influence Function (non-decomposable losses) | 5.50 | R2 | Similar theoretical ambition. That paper likely has more complete proofs; our paper has a more ambitious conceptual unification but significant gaps |
| Confident Directions for Steering | 5.50 | R2 | Both have theoretical frameworks with presentation issues. Our paper's theory-practice connection is tighter (cosine 0.978 vs. disconnected theory) |
| Understanding Impact of Human Feedback via Influence Functions | 6.33 | R2 | That paper delivers fully on its applied claims with solid experiments. Our paper has more theoretical novelty but weaker experimental validation |
| Improving Instruction-Following via Activation Steering | 7.00 | R1, R2 | That paper delivers completely on its claims with comprehensive experiments. Our paper has theoretical ambition but significant gaps in both theory presentation and experiments |
| Influence Functions for Diffusion Models | 8.00 | R1 | Our paper is clearly weaker — less rigorous theory, much weaker experiments |

**Round 1 bracket:** 5–7. The paper sits above the weak band (3.0) and below the strong band (7.5+). It has genuine theoretical novelty but significant gaps in rigor and experimental validation.

**Round 2 narrowing:** The paper is comparable to but somewhat stronger than the 5.50 "Versatile Influence Function" and "Confident Directions" papers in theoretical novelty, but the combination of an algebraic error in the core equation, an incomplete proof for a key corollary, two unclearly stated theorems, and missing experiments for the most distinctive claim prevent it from reaching the 6.0+ tier where papers begin to be accepted. Score: **5.5**.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>