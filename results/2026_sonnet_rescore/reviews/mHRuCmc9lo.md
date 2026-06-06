## Summary

This paper introduces a minimax framework for decision-making when forecasts satisfy only a partial ("ℋ-calibration") guarantee — specifically, that forecast residuals are uncorrelated with a test class ℋ. The central contribution is Theorem 3.1 (characterization of the minimax-optimal policy via duality) and Theorems 4.1–4.2 (showing a sharp threshold: once ℋ contains the decision-calibration indicators {1_{R_a}}, the minimax-optimal policy collapses to the familiar plug-in best response). This upgrades the previously known regret-based semantics of decision calibration to a stronger minimax-optimality guarantee, and provides a clean decision-theoretic target for practitioner use. The framework is instantiated for self-orthogonality (free from MSE training) and bin-wise calibration, and confirmed empirically on two regression datasets.

---

## Strengths

- **Duality characterization of the minimax-optimal policy (Theorem 3.1):** The optimal robust rule is factored as a two-step procedure — compute the adversarially tilted belief $q^*(v)$ via a finite-dimensional dual, then best-respond to it. This yields a closed-form, efficiently computable policy for *any* finite-dimensional ℋ, addressing the decision-maker side of the problem in full generality.

- **Sharp collapse to plug-in best response (Theorems 4.1–4.2):** The paper rigorously establishes that once ℋ ⊇ ℋ_dec = {1_{R_a} : a ∈ A}, the adversary's tilt vanishes (q* = v a.e.) and the robust rule reduces to the plug-in best response. The invariance argument — that the decision-calibration constraints zero out the adversary's leverage on E[u(a_BR, q(f(X)))] — is clean and convincing. This is a genuine upgrade over the regret-based guarantees previously known for decision calibration.

- **Self-orthogonality from squared-loss training (Proposition 4.4):** A model with a linear head trained to a first-order stationary point of MSE automatically satisfies E[f(X)(Y − f(X))^T] = 0, providing a pipeline-induced ℋ-calibration guarantee without any post-hoc correction. The derivation of the associated dual program (including the concave objective G(λ) and its efficient optimization) makes the result directly implementable.

- **Closed-form robust policy under bin-wise calibration (Proposition 4.5):** The worst-case belief reduces to the bin-conditional mean m_j, and the robust action is simply the best response to m_j. This requires no additional optimization beyond standard histogram-binning recalibration, demonstrating practical breadth.

- **Empirical confirmation of theoretical predictions (Table 1):** Under adversaries consistent with ℋ-calibration, the robust policy achieves higher utility than the plug-in rule when each is evaluated against its worst-case distribution, and does not underperform under the robust-policy worst case — precisely as predicted by the saddle-point property. Results are shown on both Bike Sharing (0.393 vs. 0.412 plug-in vs. robust under the plug-in adversary) and California Housing (0.155 vs. 0.166).

---

## Weaknesses

### Fatal

None.

### Major

- **Experimental validation uses only theoretically-constructed adversaries, not natural distribution shifts.** Section 5 compares plug-in and robust policies under (i) i.i.d. evaluation and (ii) two adversarial conditions that are explicitly described as "altering the test-time outcome distribution" by solving constrained optimization problems. As the paper states, "the adversarial distributions respect the ℋ-calibration constraints and are therefore indistinguishable, from the decision-maker's perspective, from i.i.d. test draws given an ℋ-calibrated forecaster." The experiment confirms a prediction that follows directly from the saddle-point property of the same theoretical machinery used to construct the adversary — it provides no independent evidence that the robust policy delivers practical benefit under *naturally occurring* distribution shifts of the kind motivating the practical framing in Section 1 and 6. For a paper whose primary contribution is theoretical, this is a bounded weakness, but the paper's practical claims (Section 6 mentions "calibration-preserving distribution shift" and applicability to "bike-sharing demand forecasting or housing investment") are not empirically grounded by this experiment. A temporal or geographic data split — where self-orthogonality is approximately preserved — would substantially strengthen these claims.

### Minor

- **No standard errors or confidence intervals in Table 1.** The reported utility differences (e.g., 0.393 vs. 0.412 on Bike Sharing) are from a single 60/20/20 split with no stated random seeds. These gaps could be within noise, making the magnitude of the claimed robustness gain uninterpretable. Multiple random splits or resampling would be straightforward to add.

- **Unverified claim about utility parameterization robustness.** Section 5 states "The qualitative conclusions of this Section remain the same under other reasonable parameter choices" for (α, C(·)), without any verification or sensitivity analysis. This is an easy claim to back up empirically.

- **Practical obstacle to decision calibration not fully addressed.** Decision calibration requires knowing the downstream action set A and utility function u at training/post-processing time (since ℋ_dec = {1_{R_a}} depends on both). While the paper notes this can serve multiple decision makers simultaneously (Corollary 4.3), the common scenario in which downstream decision problems are unknown at training time — and one must fall back to self-orthogonality or bin-wise calibration, which provide strictly weaker robustness guarantees — is mentioned only briefly. Being more explicit about this gap between the aspirational result (Theorem 4.1) and the practically achievable regime (Propositions 4.4–4.5) would improve honest framing.

### Trivial

- **Strong duality justification deferred without acknowledgment.** The existence of a saddle point in Theorem 3.1 requires strong duality for the minimax program over the non-compact infinite-dimensional set Q. The paper mentions "the identity map q(v) = v is always in Q" (Section 2), which is exactly Slater's condition and justifies strong duality, but this connection is not made explicit in the main text near Theorem 3.1. A single clarifying sentence would close this gap for readers.

---

## Nice-to-Haves

- Including at least one natural distribution shift experiment (e.g., temporal or geographic split of Bike Sharing/California Housing) where ℋ-calibration is approximately preserved by construction, so that the practical robustness story can be independently validated rather than purely theory-internal.
- A brief empirical check of how well E[f(X)(Y − f(X))] ≈ 0 is satisfied on the calibration split (since the MLP only approximately reaches a stationary point), and how this residual calibration error connects to performance in Table 1.
- A finite-sample guarantee of the form "the empirical robust policy achieves minimax utility within ε with high probability over the calibration split" would strengthen the claim that the framework is deployable, not just theoretically principled. The paper mentions Appendix B covers approximate calibration; a brief empirical instantiation would ground this.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh critic's concern that the linearity assumption (Assumption 2.1) "oversells" the high-stakes motivation:** While the tension exists, the paper explicitly and correctly addresses it: "Utilities that are nonlinear in v, for example, risk-averse utilities depending on outcome variance, fall outside our framework and represent an important direction for future work" (Section 2 and Section 6). Linearity is standard in the calibration literature (Foster & Vohra 1997; Kleinberg et al. 2023; Roth & Shi 2024). The concern is valid but already acknowledged; retaining it as a weakness would be redundant.

---

## Novel Insights

The most novel conceptual insight is the *sharpness* of the decision calibration threshold: rather than a gradual transition from conservative to plug-in behavior as ℋ grows, the minimax-optimal policy collapses *discontinuously* to the plug-in best response the moment ℋ crosses the decision-calibration boundary. This is not obvious a priori — one might expect richer ℋ classes to produce a spectrum of intermediate policies. The invariance argument driving this result (that decision-calibration constraints exactly neutralize the adversary's leverage over the plug-in policy's expected utility) is elegant and of independent theoretical interest. The identification of self-orthogonality as a "free" pipeline-induced calibration guarantee further suggests that many deployed regression models already satisfy a useful ℋ-calibration without any deliberate effort, making the robust decision framework immediately actionable in common practice.

---

## Suggestions

1. Add a natural-shift experiment (temporal or geographic split) to provide independent empirical grounding for the practical robustness claims in Section 6.
2. Report results across multiple random splits (or report confidence intervals) so the magnitude of the utility gap in Table 1 is interpretable.
3. Add a one-sentence strong duality/Slater justification near Theorem 3.1 for completeness.
4. Expand the discussion of the gap between the theoretical aspirational result (plug-in optimality via decision calibration) and the practically achievable regime (self-orthogonality/bin-wise calibration), including when each is recommended in practice.

---

**Originality:** High — the sharp threshold characterization and the minimax-optimality upgrade of decision calibration are genuinely novel.

**Importance:** High — identifies a principled, tractable target for trustworthy ML-based decision-making that scales to high-dimensional outcomes.

**Claims supported:** Theoretical claims are rigorously supported; empirical claims are valid but partially self-confirming.

**Soundness:** Strong — proofs are correct and assumptions are standard and well-justified.

**Clarity:** Excellent — the interpolating property, sharp transition, and practical instantiations are clearly presented.

**Community value:** Significant — provides a clean decision-theoretic characterization of decision calibration that connects the calibration and robust decision-making literatures.

---

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>4</claims_supported>
<soundness>4</soundness>
<clarity>5</clarity>
<community_value>4</community_value>
</subscores>