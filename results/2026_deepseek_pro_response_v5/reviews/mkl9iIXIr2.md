Now I have enough data to finalize. Let me compose the final review.

**Bracket analysis:**
- Round 1 bracketing placed this paper above the 5.25 anchors (WIerHtNyKr — rejected for incremental novelty) and comparable to the 6.50 anchor (iZgECfyHXF — accepted, novel bounds with restricted lower bound class).
- Round 2 narrowing: The paper sits close to OvU9u6wS2J (7.00 — accepted, novel problem framing with tight bounds but standard techniques) and slightly below wISvONp3Kq (7.33 — accepted, theory + experiments on real benchmarks).
- Final assessment: The paper's OIO-to-SOCO reduction is more technically novel than OvU9u6wS2J's techniques, but the L_max restriction and lack of combined dynamic lower bound are real constraints. Comparable to iZgECfyHXF in contribution level with slightly cleaner structure. Score: 7.0.

---

## Summary
This paper proposes the first algorithms for Online Inventory Optimization (OIO) with dynamic regret guarantees. The central technical insight is a two-stage projection strategy (Algorithm 2) that reduces OIO to Smoothed Online Convex Optimization (SOCO): Lemma 1 proves that the gap between the algorithm's constrained decision and the base learner's unconstrained decision is bounded by a switching-cost term scaled by cycle length. Combined with a doubling trick for unknown sell-out period L_max and the SOGD meta-algorithm for unknown path-length P_T, the algorithm achieves Õ(√(L_max(1+P_T)T)) dynamic regret without parameter tuning. The paper also provides the first lower bound for OIO, Ω(√(L_max T)), which matches the static regret upper bound and improves over all prior bounds by a √L_max factor.

## Strengths
- **Novel OIO-to-SOCO reduction (Lemma 1, Eq. 7):** The two-stage projection analysis proves that under Algorithm 2, the gap ∑⟨g_t, y_t − ŷ_t⟩ is bounded by 2G ∑(max_i L_t^i)‖ŷ_t − ŷ_{t+1}‖₁. This transforms the carryover stock constraint — which had previously blocked dynamic regret analyses because the comparator's feasible region C(0) is a strict superset of the algorithm's C(x_t) — into a standard SOCO switching cost. This is the technical core that enables all subsequent results and is a genuinely elegant insight.
- **First matching upper and lower bounds for OIO static regret (Theorem 5, Table 1):** The paper achieves Õ(√(L_max T)) upper bound and a matching Ω(√(L_max T)) lower bound, establishing near-optimality and resolving the open question from Hihat et al. (2023). The √L_max improvement over all prior O(L_max√T) bounds is substantial — regret is now sublinear in both T and L_max jointly.
- **Parameter-free algorithm via doubling trick (Algorithm 2, Theorem 4):** The algorithm tracks max observed cycle length (Eq. 9) and restarts the base learner with doubled L whenever the bound is exceeded. Combined with SOGD for unknown P_T, the final algorithm requires no oracle knowledge of either L_max or P_T, making it genuinely deployable without unrealistic assumptions.
- **Clean layered proof architecture:** Lemma 1 (projection gap → switching cost) → Lemma 2 (cycle length ≤ L_max) → Theorem 2 (generic base-learner regret) → Theorems 3–4 (OGD and SOGD instantiations). This modular structure isolates projection geometry, environmental difficulty, base-learner agnosticism, and specific algorithm choice, making the framework extensible.
- **New SOCO lower bound as byproduct (Corollary 1):** The Ω(√(L_max T)) OIO lower bound immediately implies an Ω(√(LT)) lower bound for SOCO, demonstrating the bidirectional value of the OIO-SOCO reduction.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
- **L_max constrains the adversary more than the "adversarial" framing suggests.** Definition 1 requires cumulative demand over L_max consecutive rounds to reach at least D for every item and every starting time. While the paper acknowledges this (lines 144–146, Remark 3) and shows that sublinear regret is impossible when L_max = Ω(T), the claim to handle "adversarial environments" (line 124) should be qualified: the adversary can choose demands adversarially but is structurally prevented from starving any item indefinitely. This is a modeling choice shared with prior work and not a flaw in execution, but readers should understand its restrictiveness.

- **No combined dynamic-regret lower bound incorporating P_T.** Theorem 5 provides Ω(√(L_max T)) for a static comparator, which matches the static upper bound. The dynamic upper bound (Theorem 4) includes a √(1+P_T) factor inherited from SOCO, and the paper notes the existing Ω(√((1+P_T)T)) lower bound from the OCO literature (Zhang et al., 2018b). However, no OIO-specific lower bound combining L_max and P_T factors is proved, leaving open whether the L_max × P_T interaction in the upper bound is tight. The paper's "near-optimal" claim applies cleanly to the static case; for the dynamic case, optimality depends on the SOCO lower bound transferring without degradation.

- **SOGD adaptation details are compressed.** The description of Algorithm 5 (SOGD meta-algorithm) and the bit sequence b_t^k (Eq. 11) are presented with minimal derivation, mostly importing Zhang et al. (2022a) as a black box. While this is acceptable for a modular contribution, the ℓ₁-norm switching cost adaptation (footnote 7) deserves more discussion of how it affects the regret analysis relative to standard ℓ₂-norm SOCO.

### Trivial
- The β parameter in Theorem 2 is discussed abstractly; showing the concrete values for OGD (β = 1/2) and SOGD explicitly in the main text would improve readability.
- The comparator class for dynamic regret could be stated more explicitly in the main text: while line 154 refers to an appendix discussion, a one-sentence summary of what constraints (if any) are placed on comparators beyond u_t ∈ C(0) would aid the reader.

## Nice-to-Haves
- A concise proof sketch of Lemma 1 in the main text would substantially aid reader comprehension, as this lemma is the paper's central technical innovation.
- A sketch of the lower bound construction for Theorem 5 would help readers understand how the Ω(√(L_max T)) result is proved.
- Discussion of whether the √(log T) factor in Theorem 4 (SOGD) is inherent to not knowing P_T, or whether it could be removed — this is a standard open question in SOCO.

## Removed Points
These points are flagged to be removed, treat them with caution:
- **"Lemma 1 proof sketch missing from main text" (Harsh Critic):** The appendix is stripped by the parser. Per review rules, weaknesses about missing appendix content are removed; proof deferral to appendix is standard practice for theoretical ICLR papers.
- **"No discussion of the L_max condition's restrictiveness" (Harsh Critic):** The paper explicitly discusses this at lines 144–146 and Remark 3, including the probabilistic extension and the relationship to prior work parameters (Shi et al., 2016; Hihat et al., 2023). The critic's claim of "no discussion" is factually incorrect.
- **"Doubling trick's restart mechanism deserves more analysis" (Harsh Critic):** The paper provides analysis of the additive term (Δ(L_max, β) in Theorem 2) and notes the subdominant condition T > L_max log² L_max (line 325). This is addressed.
- **"No discussion of whether √(log T) factor can be removed" (Harsh Critic):** This is an open research question in SOCO, not a paper flaw. It is included as a nice-to-have above.

## Novel Insights
The reduction from OIO to SOCO via the two-stage projection (Lemma 1) reveals a structural equivalence that runs in both directions: not only does SOCO technology yield OIO algorithms, but the OIO lower bound (Theorem 5) also implies a new SOCO lower bound (Corollary 1). This bidirectional connection is genuinely novel and suggests that other inventory constraints might yield further insights for online learning theory.

## Suggestions
- Add a brief proof sketch of Lemma 1 in the main text, even if only a half-page outline of the key inequalities and the role of the linear capacity constraint.
- Qualify the "adversarial environment" claim by explicitly noting that the L_max condition prevents indefinite demand starvation, referencing the lower bound result that shows this condition is necessary for sublinear regret.
- Explicitly state the comparator class constraints for dynamic regret in the main text (not just as an appendix pointer) to clarify what values P_T can take under feasibility.

## Calibration Anchors
| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| Variable Forward Regularization | lFzUHGebeb | 2.00 | R1 | Much weaker — flawed methodology, rejected |
| Adaptive Proximal Gradient | cya3eEczAx | 1.67 | R1 | Much weaker — significant gaps |
| Regret in Continuous Time Bandits | 4jzjexvjI7 | 2.33 | R1 | Much weaker — incomplete results |
| Computing Optimal Regularizers | Md783Qa2JX | 4.00 | R1 | Weaker — narrower scope, rejected |
| Uniform Wrappers | rbdlQE7HY7 | 3.67 | R1 | Weaker — less complete contribution |
| Adam Theoretical Foundations | Fj6Yv5rPRe | 4.25 | R1 | Weaker — less novel |
| Adaptive OCCO | WIerHtNyKr | 5.25 | R1 | Weaker — incremental novelty concerns, rejected |
| Decoupling Optimistic OMD | 6HfNB34x9I | 5.25 | R1 | Weaker — narrower contribution |
| Multitask in Continual Learning | Pin2kdWloe | 5.75 | R1 | Different domain, comparable quality |
| Hardness of ONCO | iZgECfyHXF | 6.50 | R1+R2 | Comparable — both have novel bounds with minor limitations; our paper's reduction is more elegant |
| Bandits with Anytime Knapsacks | qlzxeNESWI | 6.50 | R2 | Comparable — both have constrained adversarial settings |
| Contextual Bandits with Knapsacks | FCMpUOZkxi | 6.75 | R2 | Slightly weaker — more incremental |
| Trading-Volume Maximization | OvU9u6wS2J | 7.00 | R2 | Comparable — both have novel problem framing with tight bounds; our reduction is more technically novel |
| Sparse GLMs Varying Observations | wISvONp3Kq | 7.33 | R2 | Stronger — has theory + experiments on real benchmarks |
| Efficient Continual Finite-Sum | RR70yWYenC | 6.25 | R2 | Slightly weaker — narrower setting |
| (L0,L1)-Smooth Functions | GQ1Tc3vHbt | 6.50 | R2 | Comparable — both provide systematic understanding of function classes |
| Learning Solver Parameters | 5t57omGVMw | 8.00 | R1 | Stronger — more complete, broader impact |
| Tight Lower Bounds Hölder | fMTPkDEhLQ | 8.00 | R1 | Stronger — deeper technical results |
| Hidden Cost of Waiting | A3YUPeJTNR | 8.00 | R1 | Different domain, stronger impact |

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>