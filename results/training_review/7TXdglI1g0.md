Now I have all the information needed to produce the consolidated review.

---

## Summary

This paper proposes **Bisection Projection (BP)**, a framework for correcting infeasible neural network predictions in constrained optimization. The key idea is to train an Interior Point Neural Network (IPNN) to predict low-eccentricity interior points within the constraint set, then apply bisection along the line from those interior points to infeasible predictions to recover feasible solutions. The method works for general compact sets with non-empty interior (not just convex or ball-homeomorphic sets), and the paper provides theoretical bounds on feasibility, optimality loss, and runtime complexity, supported by experiments on QCQP, SOCP, AC-OPF, and joint chance-constrained problems.

## Strengths

1. **First feasibility guarantee for general compact sets beyond ball-homeomorphic constraints**: Prior work (LCL23; LCL24) was restricted to ball-homeomorphic sets. This paper develops BP for any compact set satisfying Assumption 1 (non-empty interior), which includes convex, non-convex, and non-ball-homeomorphic sets. Theorem 2 proves feasibility with bounded optimality loss. This is a genuine advance over the state of the art.

2. **Novel eccentricity-modulated interior point selection**: The paper introduces eccentricity of interior points (Definition 4.1) and establishes its connection to bisection-induced projection distance (Proposition 4.1). The IPNN loss function (Equation 6) combines an adversarial penalty with a smoothed eccentricity term. Table 3 validates this design: ME-IPNN (with eccentricity minimization) with a single IP outperforms vanilla IPNN with 8 IPs on projection distance (e.g., 0.081 vs 0.099 for QCQP).

3. **Strong empirical results on non-convex real-world problems**: BP achieves 100% feasibility across all four test problems (convex QCQP, SOCP, non-convex AC-OPF on 14-bus and 118-bus networks, and joint chance-constrained inventory management). Runtime is orders of magnitude faster than solver-based projection and warm-start methods, and faster than homeomorphic projection (e.g., AC-OPF: 2.8 ms for BP vs 28.9 ms for H-Proj). Gradient-based D-Proj fails catastrophically on AC-OPF (30.4% feasibility on OPF_14bus).

4. **Clean decomposition of optimality loss**: Theorem 2 decomposes the optimality loss into three interpretable terms — initial NN prediction error (ε_pre), eccentricity (ℰ), and finite-step bisection error (2^(-K)·diam) — each with an exponential convergence rate. The sensitivity analysis in Table 3 confirms that projection distance decreases as the number of IPs increases, consistent with Proposition 5.1.

5. **Comprehensive sensitivity analysis**: Table 3 systematically validates the key design choices: (a) the adversarial penalty ensures all IPNN predictions are feasible (rate 1.0), (b) the eccentricity loss reduces projection distance, (c) more IPs reduce projection distance with modest runtime increase. This corroborates the theoretical predictions.

## Weaknesses

### Fatal
None.

### Major
None. The concerns raised by reviewers do not rise to the level of invalidating the paper's core contributions. See below for how each is addressed.

### Minor

1. **Proposition 4.1 lacks intuitive justification in the main text**. The bound connecting eccentricity to worst-case projection distance is central to the paper's theory, but the main text states it without any proof sketch or geometric intuition. While the full proof exists in the appendix (stripped by the parser), the relationship between the *range* of boundary-to-IP distances and the *line-segment* projection distance is not self-evident. Adding 2–3 sentences of intuition (e.g., a triangle inequality argument connecting the infeasible point, the optimal boundary point, and the projected boundary point) would significantly improve readability and reviewer confidence. The paper's theoretical contribution is not invalidated — this is a presentation issue.

2. **The problem setup assumes only continuity of f, but the optimality bound in Theorem 2 requires Lipschitz continuity**. Section 3 states "the objective function f(x,θ) is continuous and can be non-convex." The optimality loss bound (part (ii) of Theorem 2, which is garbled in the parsed text) uses the Lipschitz constant of f. This is a minor but real inconsistency — the Lipschitz assumption should be stated explicitly alongside the continuity assumption. Easily fixable and does not affect the paper's core claims.

3. **Theorem 1's sufficient conditions are acknowledged as practically difficult, but no fallback is discussed**. The paper candidly notes that C₀ may be unbounded for discontinuous constraint sets, and that exact verification is NP-hard. This is good self-awareness. However, a practical user of the method has no guidance on what to do if IPNN outputs an infeasible interior point (e.g., fall back to a fast convex feasibility solve for a single IP). The paper's Section 7 identifies this as a future direction, which is appropriate, but a brief discussion of practical mitigation strategies would strengthen the presentation.

4. **Experimental validation could be broadened to geometrically more challenging sets**. The four test problems (two convex, two non-convex) are real-world and relevant, but they are all "nice" in practice (smooth manifolds, scenario-based convex approximations). The paper claims generality for "general compact sets" under Assumption 1, which includes non-star-shaped sets and disconnected components. Testing on such sets (e.g., a torus in 3D, a set with a hole, a disconnected constraint set) would more directly substantiate the generality claim. This is not a fatal gap — the bisection method is provably correct for any set with non-empty interior — but the claim of "general" is broader than the empirical scope.

5. **No statistical significance reported for key numerical results**. Table 3 reports projection distances (e.g., 0.081 vs 0.099) and runtimes without confidence intervals or standard deviations. Given that these are averaged over test instances, some measure of variability would strengthen the claims, especially when comparing methods with small absolute differences.

6. **Number of boundary samples (b) used per θ in IPNN training is not specified**. The eccentricity loss (Equation 7) requires boundary samples {yⱼ}. Knowing the batch size b and how boundaries are sampled across Θ during training would aid reproducibility. This is a standard experimental detail that should be included.

### Trivial

- The claim "first work to guarantee NN solution feasibility over general compact sets" (line 23) is qualified with "To our knowledge" but could be softened slightly to avoid any perception of overclaim — the bisection-from-interior-point technique itself is standard, and the novelty is in the IP selection and analysis framework.

- The batch selection rule (Equation 3) chooses the projected point with minimum deviation but is presented without analysis of how this compares to alternative selection strategies (e.g., minimizing projected distance). This is a minor gap in theoretical analysis but well-motivated heuristically.

## Nice-to-Haves

- A 2D visualization showing IP locations relative to the constraint boundary, the NN infeasibility region, and the resulting projected points would make the eccentricity concept more intuitive.
- A comparison with a simple baseline where the IP is chosen as (an approximation of) the Chebyshev center would further validate the eccentricity-aware IP selection.
- Adding a brief proof sketch or geometric lemma for Proposition 4.1 in the main text (not just the appendix) would improve accessibility.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Ball-homeomorphic sets include all convex sets is false"** — The paper states a standard topological fact (compact convex sets with non-empty interior are homeomorphic to a ball). The reviewer's objection about construction difficulty is irrelevant to the mathematical claim. REMOVED (factually wrong).

- **"Proposition 4.1 argument appears circular"** — Without access to the appendix proof (stripped by the parser), the reviewer speculates about circularity but does not demonstrate an error. The bound is standard in structure (triangle inequality + eccentricity covering). The intuition criticism is valid and kept in Minor #1; the circularity accusation is unsupported. REMOVED (speculative).

- **"Figure 1 / Algorithm 1 missing"** — Parser artifacts; these exist in the original submission. REMOVED (formatting artifact).

- **"Theorem 1 is practically vacuous"** — The paper explicitly acknowledges the practical limitations of both sufficient conditions (lines 208–211). The theorem provides valid theoretical sufficient conditions, which is standard practice. The fallback discussion gap is kept as Minor #3. REMOVED (paper already addresses).

- **"First work claim overstatement"** — The claim is qualified with "To our knowledge" and refers specifically to feasibility guarantees for general compact sets, not to the bisection technique itself. The novelty lies in the full framework (eccentricity + IPNN + bisection + guarantees). REMOVED (reasonable claim).

## Novel Insights

A genuinely interesting observation emerging from the reviews is the subtle tension between the theoretical guarantee of generality (Assumption 1 covers all compact sets with non-empty interior) and the practical dependence on the eccentricity bound. For geometrically pathological sets (e.g., disconnected components, sets with holes), the bisection method still works mechanically, but the eccentricity ℰ could be large, making the optimality loss bound proportionally loose. This means the method's *practical* power on real problems (AC-OPF, SOCP, etc.) comes from the fact that those constraint sets have small "local eccentricity" near the optimal boundary region — a property that the IPNN exploits but that the paper's theory doesn't fully characterize. Understanding when real-world constraint sets naturally admit low-eccentricity interior points near the optimal boundary is an open question that the paper's framework surfaces nicely.

## Suggestions

1. Add 2–3 sentences of geometric intuition for Proposition 4.1 in the main text (e.g., a triangle inequality argument showing how the projection distance decomposes into prediction error plus boundary-to-IP distance range).
2. State the Lipschitz continuity assumption on f explicitly alongside the continuity assumption in Section 3.
3. Specify the number of boundary samples (b) used per θ in IPNN training and how they are sampled across Θ.
4. Add confidence intervals or standard deviations for the key metrics in Tables 2 and 3.
5. Include a brief discussion of what to do if IPNN outputs infeasible IPs in practice (even if the adversarial penalty makes this rare).

## Score and Decision

The paper makes a genuine contribution to the learning-to-optimize literature. The BP framework is simple, general, and empirically effective. The theoretical analysis is solid (with proofs in the appendix), and the experiments convincingly show advantages over existing methods. The weaknesses are all addressable — none threaten the core claims. I recommend acceptance.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>