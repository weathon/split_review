## Summary

This paper investigates representational limitations in value decomposition for cooperative MARL. It makes three contributions: (1) a theorem proving that Linear Mixing Functions (LMF) achieve correct representation only in "decomposable" MMDPs — a restrictive class requiring independent transitions and additive rewards — implying LMF fails in most MARL problems; (2) a Mixing for Unbounded Difference (MUD) framework that rescales SMMF's bounded output differences into an unbounded range, achieving what the paper defines as complete representational capacity (range coverage of \((-\infty, \mathcal{Q}(s,\mathbf{u}^*)]\) under the IGM constraint); (3) the identification of Optimal Representational Interference (ORI) — cross-interference between action-value representations during training that can leave the formal capacity unrealized — along with heuristic gradient-shaping mitigations (MUD-SmG and MUD-StG).

## Strengths

- **Theorem 3.3 provides a precise formal characterization of when LMF fails.** The paper proves that the action-value function is linearly factorizable iff the MMDP is decomposable (independent sub-transitions + additive sub-rewards). This formalizes an intuitive boundary condition for VDN-style methods and is the first explicit necessary-and-sufficient condition of its kind. The result is cleanly stated and the definitions (Definition 3.1) are precise.

- **The MUD framework identifies and addresses a genuine structural limitation of SMMFs.** The paper correctly observes that an SMMF's output range is bounded (the difference \(\Delta f\) between the greedy and a non-greedy action is capped), and proposes a two-stage rescaling mechanism (Eq. 9–10) to extend the range to \((-\infty, \mathcal{Q}(s,\mathbf{u}^*)]\). The reasoning about boundedness (Eq. 8 and surrounding text) is logically sound for discrete action spaces.

- **The identification of Optimal Representational Interference (ORI) is a worthwhile conceptual contribution.** The paper articulates a problem distinct from representational capacity: even when the function class has sufficient range, training dynamics can fail because shared local Q values create cross-interference that drowns out the gradient for optimal actions. The optimal representation ratio \(w^*\) (Eq. 11) provides a measurable diagnostic for this phenomenon.

- **The toy game experiments (Section 5.1) cleanly validate Theorem 3.3.** The paper constructs a decomposable and an indecomposable variant of a simple grid-world task and shows that LMF achieves near-zero RMSE in the former but not the latter, while MUD succeeds in both. This is a well-designed small-scale verification of the theoretical claim.

- **The matrix-game results (Fig. 7) trace \(w^*\) over training**, providing direct evidence linking the ORI phenomenon (measured via \(w^*\)) to suboptimal convergence, and showing that MUD-SmG/StG progressively raise \(w^*\) toward 1 while baselines do not.

## Weaknesses

### Fatal
None.

### Major

- **Experimental validation is too narrow to support the paper's stronger practical claims.** The evaluation is limited to a custom 4×4 grid world (98 states), a 2-agent 3×3 single-step matrix game, and a predator-prey variant. No results are reported on standard multi-agent benchmarks (SMAC, MPE, or any commonly used value-decomposition testbed). Since the paper claims that MUD-SmG and MUD-StG "outperform baselines and address the problem" (line 22), this claim rests on thin empirical evidence — three small-scale environments where the gap over QPLEX is modest in the predator-prey setting and only clearly visible in the matrix game. Standard benchmarks would be needed to assess whether ORI is a serious problem in practical scenarios and whether gradient shaping confers meaningful gains at scale.

- **The gradient-shaping solutions for ORI are heuristic with no theoretical backing.** The paper defines \(w^*\) (Eq. 11) and proposes MUD-SmG (exponential decay, Eq. 12) and MUD-StG (step function, Eq. 13) to increase it, but provides no analysis of convergence properties, no characterization of fixed points under the modified gradient, and no guidance on how these heuristics relate to the underlying optimization. The justification ("reducing the gradient according to the value of \(\Delta\mathcal{F}\) improves the optimal representational weight") is intuitive but informal. The hyperparameter \(\alpha\) in MUD-StG is introduced without any sensitivity analysis or selection guidance.

### Minor

- **Disconnect between theoretical assumptions and experimental setting.** The theoretical analysis in Section 3 assumes full observability (MMDP) and on-policy data distribution (line 82), but the predator-prey experiments use partial observation and off-policy Q-learning with replay. The paper does not discuss whether the theoretical results (which are about representational capacity, a static property of the function class) are expected to transfer, or whether the ORI analysis generalizes to the partially observable, off-policy case. While this gap is common in the MARL literature, the paper would benefit from explicit acknowledgment.

- **The "complete representational capacity" claim for MUD is defined relative to range coverage (lines 138–142), not functional universal approximation.** The paper's argument that MUD achieves this range-based definition is sound, but the phrase "complete representational capacity" could mislead readers into inferring a universal approximation property. The paper should more prominently clarify what its definition entails and what it does not (e.g., that achieving the range goal does not guarantee that any arbitrary IGM-satisfying function can be represented).

- **No error bars or confidence intervals are reported in any figure.** The paper shows single-curve learning trajectories without standard deviation shading or multiple-seed aggregation. This makes it hard to assess the statistical significance of performance differences between methods.

### Trivial
None.

## Nice-to-Haves

- A hyperparameter sensitivity analysis for MUD-StG's \(\alpha\) would help practitioners apply the method.
- The relationship between MUD and QPLEX (line 177) is stated but not derived; a brief derivation would strengthen the framing.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Criticism that MUD's "complete representational capacity" claim is "false as stated" and conflates range coverage with functional completeness.** The paper explicitly defines "complete representational capacity" in terms of range (lines 138–142: \(R(\mathcal{F}_\theta) = (-\infty, \mathcal{Q}(s,\mathbf{u}^*)]\)), not functional universal approximation. The paper's argument for MUD achieving this range-based definition is logically presented. The critic imposes a different definition of completeness.
- **Criticism that hyperparameters, network architectures, training budgets, and number of runs are omitted.** Such details are standard in appendices, which the parser strips from the extracted text.
- **Criticism that the proof of Theorem 3.3 is absent from the main text.** The proof likely resides in the appendix, which was stripped by the parser.
- **Criticism that Eq. 4 (strict monotonicity) uses a ratio condition "not then used in the main analysis."** The ratio condition is used directly in the boundedness argument (lines 152–158) to derive \(\Delta f_\theta' \ge \Delta f_\theta\).
- **Criticism that Figure 2's example does not satisfy independent transitions.** The paper explicitly states "agents would not collide with each other" as an assumption of the example.
- **Criticism that the strict monotonicity definition is "not obviously equivalent to standard monotonicity."** The paper defines monotonicity (Eq. 3, partial derivative ≥ 0) separately from strict monotonicity (Eq. 4, ratio condition), and both are standard in this context.
- **Formatting nitpicks** (readability of figures, garbled text references like "Fig.7.2") — these are parser artifacts, not author errors.
- **Strength Finder's claim of "state-level error bars"** in the toy game experiment — the bars show per-state RMSE values, not error bars (measures of uncertainty).
- **Strength Finder's claim of "scalability in complex partial-observation tasks"** — the predator-prey setting is simple; "complex" is an overstatement.

## Novel Insights

The most interesting observation emerging across the reviews is that the paper separates two distinct failure modes for value decomposition — representational capacity (can the function class express the target?) and representational interference (does training realize that capacity?). The ORI problem, formalized through the optimal representation ratio \(w^*\), is a genuinely underappreciated issue: even with a complete mixing function, the shared local Q values create a coupling during gradient descent that can drown out the signal for optimal actions. However, the paper's proposed fix (gradient shaping) is heuristic, and the reviews correctly identify that a proper theoretical treatment of this coupling — e.g., analyzing the gradient flow dynamics and identifying when gradient shaping avoids suboptimal fixed points — would significantly strengthen the contribution. The reviews also converge on the view that the experimental scope is too narrow; testing on SMAC or MPE would establish whether ORI is a practically relevant obstacle or an artifact of small toy settings.

## Suggestions

1. **Add standard benchmarks.** Evaluate MUD-SmG/StG on at least 5–10 SMAC maps and/or MPE tasks, with comparison to QMIX, QPLEX, WQMIX, and VDN. Report median returns with interquartile ranges over 10+ seeds.
2. **Provide an ablation study** comparing MUD (without gradient shaping), MUD-SmG, MUD-StG, and alternative ORI heuristics to isolate whether the specific exponential/step forms matter.
3. **Clarify the scope of the "completeness" claim.** Either rename it (e.g., "range completeness") or add a brief remark explaining what it does and does not guarantee, to avoid misleading readers.
4. **Add a discussion of the theory–experiment gap** (full observability/on-policy assumptions vs. partial observability/off-policy experiments) and argue why the core findings should transfer.
5. **Report error bars** (standard deviation across seeds) for all experimental figures.
6. **Provide guidance on selecting \(\alpha\)** for MUD-StG, or report a sensitivity sweep.

## Score and Decision

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>