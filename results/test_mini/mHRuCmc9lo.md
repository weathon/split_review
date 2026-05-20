Now I have all the information needed. Let me write the final consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses
### Fatal
### Major
### Minor
### Trivial

## Nice-to-Haves

## Removed Points

## Novel Insights

## Suggestions

## Score and Decision

Let me construct the final review carefully.

---

Let me check one more thing about the "scope limitation" the harsh critic raised — whether the paper acknowledges its scope.

Looking at the paper (line 25): "policy a(·) : [0, 1]^d → A mapping predictions to actions"
Line 48: "can we derive optimal decision-making policies under weaker and more practical conditions than full calibration?"

The paper is clearly scoped to policies that map forecasts to actions. The critic acknowledged this. This is not a weakness.

Now let me also verify what the paper says about the "adversarial evaluation" methodology — specifically, is there any description of how the worst-case distributions are constructed?

Lines 273-278: Describes adversarial performance as "altering the test-time outcome distribution in two ways: (i) a worst case tailored to the plug-in policy, and (ii) a worst case induced by the robust dual, tailored to the robust policy. In both cases, the adversarial distributions respect the ℋ-calibration constraints..."

Line 299: "We use the calibration data to substitute any population level expectation that is needed to be computed to derive a_robust."

There's no explicit description of how the test-time samples are generated to conform to the worst-case q*. This is indeed under-described.

Now let me finalize.## Summary

This paper studies how a decision maker should act on forecasts that satisfy only partial (ℋ-)calibration guarantees, rather than the intractable ideal of full calibration. The authors characterize the minimax-optimal decision policy under any finite-dimensional ℋ via a duality argument (Theorem 3.1), then show a sharp transition: when ℋ contains the decision-calibration indicators {𝟙_{R_a}} (which are tractable to guarantee), the optimal robust policy collapses to the simple plug-in best response to the forecast, recovering the same "trustworthiness" semantics as full calibration (Theorems 4.1–4.2). For cases where decision calibration is unavailable, the paper shows how structural properties of common training pipelines (e.g., self-orthogonality from squared-loss training) induce usable ℋ-classes and tractable robust policies, with illustrative experiments on two regression datasets.

## Strengths

1. **Decision calibration recovers plug-in minimax optimality (Theorems 4.1–4.2, Section 4.1).** Prior work only established that decision calibration implies no swap regret (Zhao et al., 2021; Noarov et al., 2023), which does not rule out policies that improve over the plug-in best response via a more sophisticated mapping from predictions to actions. Theorem 4.1 provides a strictly stronger guarantee: under decision calibration (or any superset thereof), the plug-in best response is minimax-optimal among *all* forecast-based policies. The invariance argument (Eq. 7, line 195–199) showing that the adversary cannot reduce the plug-in policy's utility below its nominal value under decision-calibration constraints is elegant and correct.

2. **General characterization of the optimal robust policy for arbitrary finite-dimensional ℋ (Theorem 3.1, Section 3).** The duality-based closed form — computing multipliers λ* via a finite-dimensional concave program, then pointwise constructing q*(v) via convex minimization — provides a unified, computationally actionable recipe that subsumes prior special cases (Rothblum & Yona, 2023 handled only 1D outcomes and approximate full calibration). The exposition of the two-step procedure (line 141–147) makes the practical implementation clear.

3. **Self-orthogonality guarantee from squared-loss training (Proposition 4.4, Section 4.2).** The observation that any model with a linear last layer trained to a stationary point of MSE automatically satisfies an ℋ-calibration condition (ℋ = {hⱼ(v) = vⱼ}) is clean and practically useful. It connects the robust decision framework to standard regression pipelines without requiring any additional algorithmic intervention.

4. **Empirical results consistent with theoretical predictions (Section 5, Table 1).** The experiments on Bike Sharing and California Housing confirm that the robust policy derived from the self-orthogonality condition outperforms the plug-in best response under calibration-preserving adversarial evaluation, with only mild degradation under nominal i.i.d. conditions — matching the theoretical saddle-point predictions.

## Weaknesses

### Fatal
None.

### Major
None. The theoretical results are internally consistent, well-scoped, and correctly reasoned.

### Minor

1. **Adversarial evaluation methodology is under-described (Section 5).** The paper reports worst-case utilities under two adversarial distributions (tailored to the plug-in policy and to the robust policy), but does not explain *how* these distributions are constructed from finite data. For ℋ = {h(v)=v}, the robust policy requires computing λ* via the dual objective G(λ) on calibration data, then for each test forecast ν evaluating q*(ν) via a 1D convex minimization. To then evaluate performance under "the worst-case distribution," one would need to actually sample outcomes according to q*(f(X)) at test time — the paper does not specify how this sampling is done or how the "adversary" is realized. This is a reproducibility gap, though the experiments are acknowledged as illustrative.

2. **The headline collapse result (Theorems 4.1–4.2) is not empirically validated.** The experiments test a *different* ℋ-class (self-orthogonality, ℋ = {v}), not the decision-calibration class ℋ_dec = {𝟙_{R_a}}. While the self-orthogonality experiments demonstrate the framework's applicability in a practical setting, they do not showcase the paper's central conceptual contribution: that decision calibration collapses the robust policy to plug-in best response. A synthetic experiment (e.g., post-hoc recalibration to enforce the decision-calibration constraints, then comparing plug-in vs. robust policy) would have directly demonstrated this surprising result.

3. **Scope of experiments is limited (Section 5).** Only two datasets and one ℋ-class are tested. The bin-wise calibration case (Proposition 4.5) — which would be easy to implement via histogram binning and would demonstrate the framework's breadth — is not experimentally evaluated. Given that the experiments are presented as validation of the overall framework rather than just the self-orthogonality case, including at least one additional ℋ-class would strengthen the empirical evidence.

### Trivial
None.

## Nice-to-Haves

- **Empirical demonstration of the "sharp transition."** Gradually adding test functions to ℋ (starting from empty, then decision-calibration indicators 𝟙_{R_a}, then larger sets) and showing that the robust policy transitions from minimax-conservative to plug-in best response exactly at ℋ_dec would provide compelling visual evidence for the collapse result described in Figure 2.

- **Concrete guidance on achieving decision calibration in practice.** The paper cites prior work on multicalibration, but a brief concrete example (e.g., "one can run the algorithm of Noarov et al. (2023) on the forecaster to obtain decision-calibration guarantees") would make the framework more actionable for practitioners.

## Removed Points

These points were considered and removed with justification:

- *"Scope limitation: decision maker could use raw features X rather than forecast f(x)."* The paper explicitly assumes policies mapping predictions to actions (line 25: "a(·) : [0,1]^d → 𝒜") and is internally consistent. The critic acknowledged this framing is reasonable. This is a scope choice, not a weakness.

- *"The plug-in best-response policy achieves higher utility only among forecast-based policies."* Same as above — the paper's scope is clearly stated. Removed.

- *"Missing appendix / proofs / references."* The parser strips these sections from all papers; they exist in the original submission.

- *"Missing comparison to prior work on X."* I cannot verify the existence of unmentioned related work without external sources.

## Novel Insights

The harsh critic's identification of the invariance argument as the key technical step — that under decision calibration, the utility of the plug-in best-response policy is invariant to the adversary's choice of q ∈ 𝒬 — is a genuinely useful lens that goes beyond the paper's own presentation. The paper states this fact (lines 195–199) but does not highlight it as the core conceptual engine driving the collapse. Structuring the exposition around this invariance would make the proof of Theorem 4.1 immediately transparent: "the adversary cannot hurt a_BR, and a_BR is optimal under the nominal, therefore it is minimax optimal." This reframing also clarifies why the collapse is so clean — it follows from the specific structure of the indicator constraints, not from any heavy machinery.

## Suggestions

1. **In the experiments section, describe the adversarial evaluation procedure explicitly.** For each of the two adversarial settings (worst-case for plug-in; worst-case for robust), state: (a) how λ* is computed from calibration data (e.g., bisection on G(λ) for the 1D case), (b) how q*(ν) is constructed for each test forecast ν, and (c) how test-time outcome samples are generated to respect q*. This would resolve the reproducibility concern.

2. **Consider adding an experiment that directly validates the decision-calibration collapse.** A simple setup: post-process a forecaster on a held-out split to approximately satisfy ℋ_dec = {𝟙_{R_a}} (e.g., via recalibration in each decision region), then compare a_BR vs. a_robust under an adversary that respects ℋ_dec. The prediction (from Theorem 4.1) is that both policies achieve essentially the same utility.

3. **In Theorem 3.1, make the dual problem's form explicit.** The statement currently gives the structure of q* in terms of λ*, but does not state the dual objective itself (which is deferred to the proof). Including the dual objective's form (similar to G(λ) in the 1D self-orthogonality case, lines 245–247) in the main theorem statement would improve readability.

4. **Acknowledge the experimental limitation more directly.** A sentence like "Our experiments validate the framework for the self-orthogonality case; validating the decision-calibration collapse is left for future work" would set appropriate expectations.

## Score and Decision

**Calibration procedure:**

**Round 1 (Bracketing):** Searched for "robust decision making calibration forecasts minimax optimal policy" with three bands. Weak anchors (avg < 3.5): papers scoring ~3.0 with fundamental methodology flaws (e.g., missing proofs, broken optimization procedures). Middle anchors (3.5–7.5): papers scoring 4.0–7.0, including several on decision calibration and robust decision-making. Strong anchors (> 7.5): papers scoring 8.0 in different domains (embodied navigation, matrix sign methods). The paper clearly falls in the middle band — it has no fatal flaws but is not a cross-domain landmark result.

**Bracket: 4.0–7.5.**

**Round 2 (Narrowing):** Searched within (4.5, 6.5) and (6.0, 8.0) for topically similar papers.

Key anchors read in full:
- **vAU1fo1zRV ("Dimension-Free Decision Calibration for Nonlinear Loss Functions", avg 7.00, Accept Poster).** Closely related (decision calibration, theory+experiments). Has lower bounds and dimension-free algorithms. The present paper has a different scope (minimax decision-making under partial calibration vs. achieving decision calibration) and a more surprising conceptual result (the collapse). The present paper is slightly weaker in technical depth (no lower bounds) but comparable overall in quality and significance.
- **m5zdEywl57 ("Persuasive Prediction via Decision Calibration", avg 6.00, Reject).** Also on decision calibration with a game-theoretic framing. Was rejected primarily for lack of empirical evaluation and modeling concerns. The present paper is clearly stronger (has experiments, cleaner theoretical setup, better motivated). 
- **bt4Ahpemmi ("Conformal Robustness Control", avg 6.50, Accept Oral).** Robust decision-making with theory and experiments. The present paper has stronger theoretical guarantees but less extensive experiments. Comparable quality.
- **xRjOrcj08o ("Conformalized Decision Risk Assessment", avg 5.00, Accept Poster).** Decision-making with uncertainty quantification. The present paper has a more original theoretical contribution and cleaner results.

**Final determination:** The paper is most comparable to the 6.5–7.0 anchors. It has sound theory, a genuinely surprising result, and clear writing — stronger than the 6.0 papers. The main limitations (experiments not testing the headline result, limited ℋ-class coverage, under-described adversarial evaluation) are real but minor relative to the theoretical contribution. The paper sits slightly below the 7.00 "Dimension-Free Decision Calibration" anchor, which had both upper and lower bounds and more extensive technical machinery.

**Anchors retrieved (all rounds):**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| NNqi3tBcZr.md | 3.00 | R1 | Weaker — fundamental issues (missing proofs, incremental) |
| MY7GQ5rOyK.md | 3.00 | R1 | Weaker — different domain, lower quality |
| BoOu1X1fkT.md | 3.00 | R1 | Weaker — flawed methodology |
| yP6TzcUi4k.md | 3.00 | R1 | Weaker — different domain, lower quality |
| aJRZzDiGe5.md | 3.33 | R1 | Weaker — different domain |
| vAU1fo1zRV.md | 7.00 | R1, R2 | Comparable but slightly stronger technical depth |
| bt4Ahpemmi.md | 6.50 | R1, R2 | Comparable — similar scope, slightly weaker theory |
| xRjOrcj08o.md | 5.00 | R1 | Weaker — narrower contribution |
| m5zdEywl57.md | 6.00 | R1, R2 | Weaker — no experiments, modeling concerns |
| YVzvi34qyc.md | 4.00 | R1 | Weaker — narrower scope |
| Ahdsg2nkNH.md | 8.00 | R1 | Different domain — not comparable |
| kkBOIsrCXh.md | 8.00 | R1 | Different domain — not comparable |
| oBXfPyi47m.md | 8.00 | R1 | Different domain — not comparable |
| qOyF214xmg.md | 8.00 | R1 | Different domain — not comparable |
| yRtgZ1K8hO.md | 8.00 | R1 | Different domain — not comparable |
| 4AjfwNnWAV.md | 5.33 | R2 | Weaker — narrower calibration measurement focus |
| gnJWVJSc3V.md | 4.67 | R2 | Weaker — LLM calibration, different domain |
| 1Q85tfZaOa.md | 5.50 | R2 | Weaker — classification error estimation |
| e4xANXjA9W.md | 6.00 | R2 | Comparable — similar robustness framing, smaller experiments |
| XNbVoi9mfr.md | 6.50 | R2 | Different domain — human assessment |
| 0sCyk9Tr5J.md | 6.50 | R2 | Different domain — LLM semantic calibration |
| BqOmsYIe7M.md | 6.50 | R2 | Different domain — credal prediction |

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>