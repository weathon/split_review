Now I'll write the final review.

## Summary

This paper proposes a conformal prediction procedure for constructing lower prediction bounds (LPBs) for counterfactual survival times under general right-censored data. The core idea is to transform the problem into weighted conformal inference under covariate shift between the population and the observed-event subpopulation, using a reweighting scheme based on estimates of p(e=1|X,W=w). The paper claims to achieve "exact" marginal coverage (as opposed to PAC-type guarantees from prior work) and provides a doubly robustness property.

## Strengths

1. **Well-motivated problem and clear framing.** Extending conformal LPBs to counterfactual survival analysis with general right-censored data is a relevant and practically important direction. The paper correctly identifies that prior work (Gui et al., 2024; Davidov et al., 2025) provides only PAC-type guarantees, and a framework with distribution-free coverage would be valuable.

2. **Empirical demonstration of robustness to outliers.** Figure 3 provides compelling evidence that the proposed method maintains coverage near the nominal 90% level under injected outliers (N(1,2), N(10,2), N(20,2)), while competing PAC-type methods (Focus, Fused) suffer dramatic coverage drops. This experiment directly demonstrates the practical advantage of marginal (vs. PAC) coverage.

3. **LPB optimization procedure.** The τ* optimization (Section 4.1, lines 162–166) that selects τ to maximize the LPB for each test point while preserving coverage guarantees is a practical and thoughtful contribution.

4. **Validation on real clinical data.** Application to a lung cancer dataset with four radiochemotherapy regimens shows LPB trends consistent with clinical knowledge (VMAT > IMRT, induction/concurrent chemotherapy benefits), supporting practical applicability.

## Weaknesses

### Fatal

1. **Mathematical error in the core derivation (Equation 1, step (iii)).** The critical inequality step (iii) claims:

   ℙ(T ≤ a | X=x, W=w) × 1/p(e=1|...) ≤ ℙ(T ≤ a, e=1 | X=x, W=w) × 1/p(e=1|...)

   Since 1/p(e=1|...) > 0, this reduces to:

   ℙ(T ≤ a | X=x, W=w) ≤ ℙ(T ≤ a, e=1 | X=x, W=w).

   By the law of total probability, ℙ(T ≤ a | X=x, W=w) = ℙ(T ≤ a, e=1 | X=x, W=w) + ℙ(T ≤ a, e=0 | X=x, W=w), and the second term is non-negative. Therefore the inequality runs in the **opposite direction** — the paper's claimed "upper bound" on the miscoverage probability is actually a lower bound. The paper references Lemma A.1 (in the appendix, stripped from this version) for this step, but no standard probability result reverses this inequality without additional assumptions that are not stated in the main text. The main text gives no hint of what additional conditioning or assumption would justify the claimed direction.

   **Why this is fatal:** The entire calibration chain in Equation (1) is designed to show that the weighted conformal procedure provides an upper bound on the miscoverage probability α, which then guarantees coverage ≥ 1−α. If this inequality is wrong, the theoretical justification for the coverage guarantee collapses. The method may still perform reasonably in experiments (as Figure 1 suggests), but the paper's central advertised contribution — a theoretically guaranteed LPB with exact marginal coverage — is unsupported by the derivation provided.

### Major

2. **Coverage guarantee is for a shifted target distribution.** The abstract and introduction repeatedly claim "exact marginal coverage" for counterfactual survival times T(w) over ℙ_X × ℙ_{T(w)|X}. However, Theorem 4.1 provides coverage for ℙ_X × ℙ_{T(w)|X, e=1} — the distribution conditional on being uncensored. The paper asserts this is "sufficient" (line 140) but provides no justification. Since censored individuals systematically differ from uncensored ones (they have C < T, implying longer potential survival times), the guarantee does not extend to patients with the longest survival times, who are precisely those where the LPB matters most clinically. The paper does not bound or discuss this gap.

3. **Theorem 4.1 is not an "exact" guarantee.** The bound is ℙ(·) ≥ 1 − α − ½𝔼[|ω̃ − ω|], which includes an additive penalty for weight estimation error. The abstract claims "an LPB ... with an exact miscoverage guarantee" and the contributions claim "a distribution-free exact guarantee." Neither is an accurate description of what Theorem 4.1 establishes. Standard conformal prediction provides exact finite-sample marginal coverage (up to exchangeability). This paper provides a bound that degrades with weight estimation quality, which is more comparable to an approximate or asymptotically exact guarantee.

### Minor

4. **Step (ii) in Equation (1) is not justified by the tower property.** The paper states that step (ii) follows from the "tower property," but the tower property (𝔼[Y] = 𝔼[𝔼[Y|Z]]) does not produce the factor 1/p(e=1|X,W=w) that appears. This step would need a different justification (e.g., importance sampling / Radon-Nikodym reweighting), which is not provided in the main text.

5. **Algorithm 1 discards all censored observations in calibration.** The calibration set I_cal^{(w)} is restricted to individuals with e_i = 1 and W_i = w. In high-censoring regimes or with imbalanced treatments, this could drastically reduce the effective calibration sample size. The paper does not discuss the efficiency or finite-sample implications of this data reduction.

6. **Theorem 4.2 (doubly robustness) is asymptotic.** While this is standard for doubly robust results, it is much weaker than the finite-sample conformal guarantees that motivate the paper. The gap between the asymptotic claim and the finite-sample practice is not discussed.

7. **The real data is from an in-house clinical dataset not publicly available,** limiting independent reproducibility. This is a common limitation in clinical ML research but should be noted.

### Trivial

8. Table 1 reports LPB values (0.411, 0.778, 1.19, 1.57) without specifying the time unit (years, months, or standardized units), making the values difficult to interpret.

## Nice-to-Haves

- Discussion of how large the gap is between ℙ_{T(w)|X} and ℙ_{T(w)|X, e=1} as a function of censoring rate.
- Efficiency analysis of the calibration step under varying censoring rates.
- Clarification of Lemma A.1 or an alternative justification for step (iii) in Equation (1).

## Removed Points

Points flagged for removal; treat with caution:
- "Missing related works" — removed per policy (cannot verify external references from memory).
- "Baselines not clearly defined in main text" / "simulation settings not in main text" — standard for conference papers; details belong in appendix.
- "Typos/formatting/style nitpicks" — these are parser artifacts, not author errors.
- Criticisms about Lemma A.1 being in the appendix — per policy, appendix sections are stripped by the parser; this cannot be held against the authors. However, the inequality direction issue is independently verifiable from the main text regardless of Lemma A.1's contents.
- "The paper lacks a finite-sample guarantee for the target distribution" — merged with weakness #2.
- Strength Finder: "Addresses an important problem" — removed as generic/superficial.
- Strength Finder: "First exact marginal coverage guarantee" — this conflicts with verified weaknesses (the derivation is unsound), so it cannot stand as a strength.
- "The comparison to Davidov et al. (2025) should be more precise" — speculative framing suggestion.
- "No analysis of what happens to the guarantee under the shifted target distribution" — merged with weakness #2.
- "The experimental evaluation could be more comprehensive" — removed as generic.

## Novel Insights

The harsh critic's identification of the inequality sign error in Equation (1)(iii) is a genuinely insightful observation — the paper asserts an inequality that reverses the standard law-of-total-probability direction without adequate justification. This insight is not discussed in the paper itself and reveals a structural flaw in the theoretical contribution.

## Suggestions

1. **Correct or provide a valid alternative to the derivation in Equation (1).** The authors need to either (a) fix the inequality direction at step (iii) with a correct IPCW-type argument that establishes the desired upper bound (e.g., using proper IPCW weights 1/ℙ(C > T|X) rather than the current 1/p(e=1|X,W=w) factor), or (b) restructure the derivation so that the upper bound on miscoverage follows from sound probability. Without this, the paper's central theoretical claim is unsupported.

2. **Calibrate the language throughout.** Replace "exact" with "distribution-free bound" or "approximately exact" and clearly state what distribution the coverage guarantee applies to.

3. **Discuss the gap from conditioning on e=1.** Provide a bound or empirical analysis of how coverage degrades for the unconditional target ℙ_X × ℙ_{T(w)|X} compared to the conditional one.

4. **Provide the time unit in Table 1** and clarify the scale of reported LPB values.

MY FINAL SCORE: <score>3.0</score>
MY FINAL DECISION: <decision>Reject</decision>