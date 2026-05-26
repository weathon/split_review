Now let me write the final comprehensive review.

## Summary

The paper addresses online inventory optimization (OIO) with carryover stock constraints in non-stationary adversarial environments. It proposes a two-stage projection algorithm that connects OIO to Smoothed Online Convex Optimization (SOCO), achieving a dynamic regret bound of Õ(√(L_max(1+P_T)T)) without requiring prior knowledge of environmental parameters. The paper also provides an improved static regret bound O(√(L_max T)) and, as a separate contribution, the first lower bound Ω(√(L_max T)) for the OIO setting.

## Strengths

1. **Novel technical connection between OIO and SOCO.** Lemma 1 shows that under the two-stage projection strategy, the carryover stock constraint's regret contribution can be bounded by a switching-cost term proportional to L_max, leading to the clean reduction: "OIO → SOCO with switching cost 2G L_t^* ‖ŷ_t − ŷ_{t+1}‖₁." This is the key technical insight and is genuinely novel.

2. **First lower bound for OIO (Theorem 5).** The paper provides an Ω(GD√(L_max T)) lower bound for any algorithm in the OIO setting. This resolves an open question raised by Hihat et al. (2023) and establishes that the √(L_max) factor in the upper bound is unavoidable. The corollary that this constrains the SOCO lower bound is an interesting cross-pollination.

3. **Adaptation to unknown environmental parameters.** The algorithm does not need L_max or P_T a priori. The doubling-trick mechanism (Algorithm 2, lines 7–9) handles unknown L_max, while the SOGD meta-algorithm (Algorithm 5) adapts to unknown P_T automatically. This is a practical advantage over methods that require tuning to these parameters.

4. **Clear problem framing and honest scope boundaries.** The paper cleanly explains why static regret is inadequate (the d_t = Dt/T example), why the carryover stock constraint creates difficulty for dynamic regret, and acknowledges limitations (lead time, fixed costs, convex capacity). The definition of L_max (Definition 1) is well-motivated and the paper explicitly notes when sublinear regret is impossible (L_max = Ω(T)).

## Weaknesses

### Major

None.

### Minor

1. **"Near-optimal" claim without a joint lower bound.** The paper claims a "near-optimal dynamic regret guarantee" in the abstract and introduction. The evidence for this is: (a) Theorem 5 provides a static lower bound Ω(√(L_max T)), which only covers the L_max factor for P_T = 0; (b) the standard OCO lower bound Ω(√((1+P_T)T)) (Zhang et al., 2018b) covers the P_T dependence but does not incorporate OIO constraints. No joint lower bound Ω(√(L_max(1+P_T)T)) is established for the OIO setting. The paper does transparently "discuss the optimality" and relies on the common practice of component-wise optimality claims, but the abstract's phrasing is stronger than what the main text can fully substantiate. The paper would benefit from qualifying this as "optimal in L_max (via the static lower bound) and matching the optimal path-length dependence of standard OCO."

2. **Parameter translation in Table 1 is deferred to appendix without main-text justification.** The abstract claims a "√(L_max) improvement" over prior work, and Table 1 reports prior bounds as O(L_max√T) by translating demand-specific parameters (1/γ, 1/μ, D, ρβ, 1/l) into L_max. The main text provides only a footnote listing the mapping (footnote 2) and a remark that L_max is "essentially the same" as prior parameters (Remark 3), with full justification deferred to the appendix. Since this is a headline contribution, at least a sketch of why the mapping is valid (e.g., why L_max ≤ 1/μ or L_max ≤ 1/γ) would make the main text self-contained and strengthen the narrative.

3. **Linear capacity constraint only.** The paper assumes a linear capacity constraint (∑ y_t^i ≤ D), whereas the closely related work of Hihat et al. (2023) handles general convex constraints. The paper acknowledges this limitation but the scope restriction is non-trivial — the analysis of Lemmas 5 and 6 relies on the linear structure. A reader may reasonably ask whether the core contribution (the OIO-to-SOCO connection) extends to convex constraints or is an artifact of the linear assumption.

4. **The SOGD algorithm (Alg. 5) and the projection operator Π_{𝒞(x_{t+1})} receive limited exposition.** Algorithm 5 is complex (combining K experts via Discounted-Normal-Predictor with conservative updates), and the paper offers little intuition for how the combiners work. The projection operator Π_{𝒞(x_{t+1})} (projection onto a capped simplex with lower bounds) is used repeatedly but never discussed — a note on its closed form or computational cost would aid reproducibility.

### Trivial

None.

## Nice-to-Haves

- A brief intuitive explanation of how the SOGD combiners (Alg. 4) work, even one paragraph, would make the paper more accessible to readers unfamiliar with the technique.
- A note on the closed-form solution of Π_{𝒞(x_{t+1})} (projection onto a capped simplex with lower bounds) would improve reproducibility.

## Removed Points

- **Criticism about "near-optimal" being unsupported (from Harsh Critic point 1):** Kept as Minor weakness 1 (reduced from the critic's framing as a major issue, because component-wise optimality claims are standard practice and the paper discusses the evidence transparently).
- **Criticism about parameter translation being unargued (from Harsh Critic point 2):** Kept as Minor weakness 2 (reduced from the critic's framing, because the main text does provide the mapping in a footnote and references the appendix; the issue is presentation quality, not mathematical correctness).
- **Strength Finder's claims about "adaptation to unknown parameters" and "computational efficiency":** These are legitimate strengths backed by specific content and are retained.
- **Formatting/style nitpicks, reproducibility complaints about missing appendix:** Removed per guidelines (parser artifacts, appendix exists in original submission).

## Novel Insights

The main novel insight from the review process is that the two-stage projection strategy (feed the subgradient to a base learner that ignores carryover stock, then project onto the feasible region) is a surprisingly clean reduction. It bypasses the fundamental difficulty that the comparator u_t and the decision y_t live in different feasible regions — a problem that has blocked dynamic regret analysis in prior OIO work. The observation that the resulting penalty is exactly a switching-cost term (connecting to SOCO) is the kind of insight that makes the contribution feel natural in retrospect but was non-obvious.

## Suggestions

1. In the abstract and Section 1.1, qualify the optimality claim: "optimal in the L_max factor (via the static lower bound, Theorem 5) and matching the optimal path-length dependence of standard OCO; a fully joint dynamic lower bound for OIO remains open."
2. Add a short paragraph in Section 1.1 or Section 3.1 sketching why L_max subsumes the prior works' parameters (e.g., "For i.i.d. demand with mean μ, L_max ≤ ⌈D/μ⌉, matching the 1/μ dependence in [2,7]"). This makes the Table 1 comparison self-contained.
3. Add a brief note on Π_{𝒞(x_{t+1})} — the projection onto a capped simplex with lower bounds can be computed by a water-filling algorithm in O(N log N) time.
4. Consider adding one sentence of intuition for the SOGD combiners in Section 4.3.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>