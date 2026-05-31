## Summary

This paper studies how a decision maker should optimally act when given predictions that satisfy weaker forms of calibration than full calibration. The authors formalize a family of *H*-calibration guarantees (where the richness of the test class H controls calibration strength), pose a minimax robust decision problem over outcome distributions consistent with these guarantees, and characterize the optimal robust policy via convex duality. Their central result is a sharp phase transition: once H contains the *decision calibration* indicators {1_{R_a}}, the minimax-optimal robust policy collapses exactly to plug-in best response—just as it does under the far more demanding full calibration. They also derive closed-form robust policies for squared-error regression (self-orthogonality) and bin-wise calibration, and verify the theory on two real-world datasets.

---

## Strengths

- **Elegant and genuinely surprising main result.** Theorem 4.1 shows that decision calibration—not full calibration—is the precise threshold at which best response becomes minimax optimal. This is non-obvious: one might expect a gradual interpolation, but instead there is a sharp collapse. The result substantially upgrades the known guarantees of decision calibration (previously: no swap regret) to full minimax optimality across *all* forecast-based policies.
- **Unifying framework with practical reach.** The H-calibration family cleanly subsumes full calibration, decision calibration, bin-wise calibration, and the self-orthogonality conditions that follow structurally from squared-loss training. Theorem 3.1 provides a single dual characterization that specializes gracefully to each case, and Proposition 4.4 makes robust policies "free" for any practitioner who trains a linear-head model to MSE stationarity.
- **The interpolating and sharp-transition properties are well-articulated.** The paper clearly shows that the robust policy varies monotonically with the richness of H (Figure 1), and that the transition happens at exactly the decision calibration level (Figure 2). Corollary 4.3 (simultaneous optimality across multiple decision problems) is a clean and useful consequence.
- **Duality argument is clean and computationally useful.** Theorem 3.1 provides both an analytical characterization and an efficient computation: the multipliers λ* solve a finite-dimensional concave program, and q*(v) requires only a pointwise convex minimization. Pointwise computability is noted explicitly, making deployment practical for finite action sets with linear utility.

---

## Weaknesses

### Fatal
None.

### Major

- **Thin experimental evaluation.** The experiments consist of two small tabular datasets (Bike Sharing, California Housing), a two-layer MLP, one-dimensional outcomes, and a three-action set. The utility differences between plug-in and robust (Table 1) are modest—e.g., 0.393 vs 0.412 under adversarial evaluation for Bike Sharing (~5% improvement). More importantly, the "adversarial" evaluation is constructed by the same dual that derives a_robust, making the comparison for "worst-case for robust" nearly tautological (the robust policy is defined to maximize exactly this). What is missing is evaluation under realistic distribution shifts (e.g., covariate shift, temporal splits) that respect H-calibration without being artificially constructed to probe one policy or the other. The experiments confirm that the theory does not break, but they do not demonstrate meaningful practical gain.

- **Linearity of utility is a significant restriction.** Assumption 2.1 requires u(a, v) to be linear in v. While this is standard in the calibration literature and covers the multiclass expected utility setting, it excludes common practical settings such as risk-averse objectives, threshold-based decisions, or nonlinear outcome transformations. The paper acknowledges this but does not provide a path for extension beyond a brief note on basis linearization, which "is not always low dimensional enough to be practical."

### Minor

- **Proposition 4.5 (bin-wise calibration) is relatively straightforward.** The result that the robust rule under bin-wise calibration best-responds to bin means is intuitive and its proof is essentially immediate from the structure of the constraints; the main novelty is noticing that histogram binning is already a form of H-calibration. While useful, it adds limited theoretical depth.
- **The self-orthogonality constraint H = {h(v) = v} is very weak in 1-D.** A single linear moment constraint yields a small ambiguity set, and in practice the robust and plug-in policies may rarely differ. The experiments confirm this: the i.i.d. gap is only about 1 utility point, and the adversarial gap is small. More experiments with stronger H-calibration guarantees would be informative.

### Trivial
None worth noting.

---

## Nice-to-Haves

- An experiment in which the forecaster is explicitly trained or post-processed to achieve decision calibration, verifying that the gap between robust and plug-in closes empirically.
- A worked example in a multiclass setting (d > 1) beyond the appendix, since the paper's main motivation involves high-dimensional outcomes.

---

## Novel Insights

The sharpest genuine insight is the phase-transition result: the hierarchy of minimax-optimal decision rules, parameterized by the richness of H, does *not* produce a dense continuum but instead collapses abruptly at the decision-calibration threshold. This means that the substantially easier-to-guarantee decision calibration condition (requiring only |A| moment constraints vs. the exponentially-many constraints of full calibration) already gives the decision maker everything that full calibration would: best response is minimax optimal and no alternative policy can improve on it in the worst case over H-consistent distributions. This reframes decision calibration not merely as a regret bound but as a trustworthiness certificate with the same decision-theoretic semantics as full calibration, applicable even in high-dimensional outcome spaces where full calibration is computationally intractable.

---

## Suggestions

- Add experiments under realistic distribution shifts (temporal, geographic, covariate-shifted splits) that do not require constructing the adversary explicitly, to better convince practitioners that the robust policy offers real-world benefit.
- Extend or discuss the case of continuous action sets (e.g., A = [0, 1]), even if the utility must remain linear and the optimization becomes more delicate, as this covers important practical settings like threshold setting or portfolio allocation.
- Consider a numerical comparison against the binary-outcome robust policy of Rothblum & Yona (2023) on the same datasets when applicable, to directly situate the contribution.

---

## Score and Decision

The paper delivers a theoretically sound, conceptually clean contribution: a principled minimax framework for partially-calibrated decision making, a sharp and surprising characterization of decision calibration as the exact threshold for best-response optimality, and efficiently computable robust policies from structural training properties. The main weakness is an experimental section that is too thin to establish practical impact and that relies on adversarial constructions closely tied to the theory itself. Nonetheless, the theoretical contributions are meaningful and well-executed for the calibration/decision-making research community at ICLR.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>