Now I have a thorough understanding of the paper and can verify the reviewer claims against the actual text. Let me synthesize the final review.

---

## Summary

This paper formalizes the problem of recovering causal relations from temporally aggregated i.i.d. data, where the true causal process has finer time resolution than the observation interval. It proposes two definitions of consistency — **functional consistency** (for FCM-based methods) and **conditional independence consistency** (for constraint-based methods) — and analyzes conditions under which each holds after aggregation. The key theoretical contributions are: (1) a necessary and sufficient condition for CI consistency in chain/fork structures expressed via conditional densities, (2) a sufficient condition showing that partial linearity preserves CI consistency, (3) the observation that collider structures automatically survive aggregation, and (4) a characterization showing that functional consistency is hard to achieve in nonlinear settings. The theoretical findings are supported by five simulation experiments.

---

## Strengths

- **Formalization of consistency concepts.** The paper introduces two precise, actionable definitions — functional consistency (Definition 4) and conditional independence consistency (Definition 6) — that explicitly capture what it means for causal discovery results to be "recoverable" from aggregated i.i.d. data. This conceptual framework cleanly separates the different requirements of FCM-based vs. constraint-based methods, and is used throughout the theoretical analysis.

- **Necessary and sufficient condition for CI consistency in chain/fork structures (Theorem 6).** The characterization expressed via conditional densities is mathematically precise and goes beyond the common observation that "aggregation breaks d-separation." The subsequent decomposition into density terms involving only two components each (lines 265–269) is insightful, and the derived sufficient conditions (Corollaries 2–4) — especially that partial linearity ensures CI consistency — are non-trivial and directly testable.

- **Collider structure automatically preserves CI consistency (Remark 1).** The clean observation that colliders are unaffected by aggregation (because the individual $Y_t$ nodes are colliders for $X_t$ and $Z_t$) is correct and practically useful — it tells practitioners that conditional independence tests involving colliders are robust to aggregation.

- **Experimental support for the CI consistency theory (Table 1).** The kernel CI test results cleanly separate the four linear/nonlinear combinations and show that whenever at least one link is linear the conditional independence $\overline{X} \perp\!\!\!\perp \overline{Z} \mid \overline{Y}$ is preserved (rejection rate ~5% at 5% significance), while the fully nonlinear case fails (58% rejection). This directly corroborates Corollary 4.

- **LiNGAM experiment (Figure 2) demonstrates functional consistency degradation with $k$.** The experiment shows Direct LiNGAM accuracy dropping from near 100% to random guess as $k$ increases from 1 to 100, even in the linear non-Gaussian case. This concretely illustrates the functional consistency challenge and the central-limit-like effect of aggregation on non-Gaussianity.

---

## Weaknesses

### Fatal

None.

### Major

- **The experiments never validate the alignment approximation on actual time-delay data.** All five experiments generate data directly from the aligned (instantaneous) model — none generate data from a time-delay VAR(1) with known lagged structure, aggregate with large $k$, and then apply non-temporal causal discovery to see whether the results match the true summary graph. The paper's motivating scenario is that the aligned model approximates aggregated time-delay data, but this crucial link is never empirically tested. The paper mentions a fourth experiment "to investigate the impact of the $k$ value and to justify the approximations" (line 301), but results are not presented in the extracted text. Without this validation, readers cannot assess whether the theoretical findings (which are about the aligned model) actually transfer to the real-world problem that motivated the paper.

- **The functional consistency results provide limited practical guidance.** Theorem 3 constructs $\hat{f}$ as a conditional expectation — while mathematically correct, this is essentially the optimal predictor and the paper acknowledges this (line 149, citing Rao-Blackwell). Theorem 4 states that the necessary and sufficient condition is independence of $N$ from $\overline{X}$, which is a restatement of the definition. The subsequent discussion (line 159) correctly notes that checking this is "challenging" and that constant conditional variance is necessary but not sufficient. The paper offers no practically verifiable condition for functional consistency in nonlinear settings beyond the already-known linear case (Gong et al. 2017). The novelty over prior work is therefore limited to a formalization of why it is hard, rather than usable conditions.

### Minor

- **The CI experiment uses only $k=2$.** While the theoretical framework works for any finite $k$, the experiment fixes $k=2$ throughout. It would be informative to show whether the CI consistency results degrade as $k$ increases (e.g., $k=5,10,50$) — does partial linearity continue to guarantee consistency at higher aggregation levels, or does the central limit effect on the conditioning variable $\overline{Y}$ eventually break it?

- **The claim of being "first" to discuss this in nonlinear cases (line 31) is somewhat overreaching.** The paper's treatment of functional consistency in nonlinear settings correctly identifies the difficulty but does not provide practically usable necessary/sufficient conditions. The CI consistency analysis for nonlinear cases is more substantive, but the claim as stated in the introduction is broader than what is delivered.

- **The alignment approximation (Section 2.2) is presented as a heuristic motivation, not a rigorous result.** The paper is transparent about this (line 88: "This section merely provides a simple example"), and the boundary-term argument ($\overline{Y'} - \overline{Y} \to 0$) is algebraically correct for large $k$. However, the paper does not discuss mode of convergence, required process conditions (stationarity, ergodicity, mixing), or the rate at which the approximation error becomes negligible. While this does not invalidate the paper's core theory (which concerns the aligned model), it limits the strength of the connection between the theory and the motivating real-world scenario.

### Trivial

None.

---

## Nice-to-Haves

1. **Direct validation on aggregated time-delay data.** Generate data from a VAR(1) with known time-lagged structure (including both linear and nonlinear $f$), aggregate with varying $k$, apply PC/GES/Direct LiNGAM to the aggregated i.i.d. data, and compare the discovered graph to the true summary graph. This would directly validate the alignment approximation.

2. **CI experiment with larger $k$.** Run the conditioning test for $k=5,10,50$ to show whether the failure of CI consistency for chain/fork gets worse, stabilizes, or whether partial linearity continues to guarantee correctness.

3. **A concrete example where both functional and CI consistency fail.** Show a fully nonlinear time-delay model, aggregate it, apply both FCM and constraint-based methods, and present the estimated graph vs. ground truth. This would make the negative result more compelling for practitioners.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic Issue 3 (Corollary 4 is "likely incorrect"):** The critic claims that the partial linearity condition for chain/fork models is not properly justified and likely incorrect, arguing that "$N_t$ would then contain $Z_{t-1}$." This is a misreading. Corollary 4 (line 288) states: *"If $f_Z(Y_t,Z_{t-1},N_{Z,t})$ is of the form $\alpha*Y_t+N_t$"* — this is a **sufficient condition** asserting that when the function simplifies to a linear form that does **not** depend on $Z_{t-1}$, then $\overline{Z} \perp\!\!\!\perp Y_{1:k}\mid\overline{Y}$ follows. Under this assumption, $Z_t = \alpha Y_t + N_{Z,t}$, so $S_Z = \alpha S_Y + \sum N_{Z,t}$ and $\sum N_{Z,t}$ is independent of $Y_{1:k}$ by construction. The result is mathematically correct; the critic's objection is based on ignoring the IF-condition. **Removed as factually incorrect.**

- **Harsh Critic Issue 1's claim that the alignment approximation "invalidates the link between the theoretical conclusions and the real-world problem":** The paper explicitly states (line 102) that *"all the theoretical results in this paper consider the aggregation of the instantaneous underlying model, also referred to as the aligned model"* and that results apply to the time-delay model *only* when $k$ is large and $g(k)$ is appropriate. The approximation is presented as motivation (line 88: "This section merely provides a simple example to illustrate why..."), not as a core theorem. The paper scopes its claims honestly. **Removed as overstatement** — the approximation is heuristic but the paper does not claim a rigorous result.

- **Claim that Theorems 3–4 are "tautological" with "minimal contribution":** Theorem 3 derives the explicit form of $\hat{f}$ for nonlinear additive noise models (extending beyond Gong et al.'s linear analysis). Theorem 4 provides a necessary and sufficient condition that correctly reveals why the problem is hard — the conditional variance of $\sum f(X_i)$ must be constant. While the practical utility is limited, calling these results "tautological" is inaccurate. **Removed as too harsh.**

---

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any novel observation that the paper itself does not already present.

---

## Suggestions

1. **Add an experiment validating the alignment approximation on time-delay VAR data.** This would be the single most impactful addition — it directly addresses the largest gap between the theory and the motivating problem. Even a simple linear VAR with $k$ ranging from small to large would substantially strengthen the paper.

2. **Expand the CI experiment to larger $k$ values.** Showing that the partial-linearity result holds (or degrades) as $k$ grows would make the CI consistency analysis more compelling.

3. **Provide a brief derivation sketch for Corollary 4** (the partial-linearity sufficient condition). The result is correct but nontrivial — a short derivation (or a reference to an appendix) would help readers understand why linearity in one link suffices.

4. **Tone down the "first" claim in the introduction** (line 31) to better match what is delivered. The paper could say "the first to provide a formal analysis of both functional and CI consistency for general (nonlinear) cases under temporal aggregation."

5. **Discuss the convergence mode** for the alignment approximation more precisely. A short remark noting that if $\text{Var}(Y_t) < \infty$ then $\overline{Y'} - \overline{Y} \to 0$ in $L^2$ (or in probability) would strengthen the motivation without requiring a full asymptotic treatment.

---

## Score and Decision

The paper tackles an important and under-studied problem, provides a useful formal framework, and delivers genuine theoretical insights about conditional independence consistency under aggregation. The partial-linearity sufficient condition and the collider robustness result are clean and practically relevant. The experiments support the theory. The main weaknesses are (a) the empirical validation never bridges the gap between the aligned model and actual time-delay data, and (b) the functional consistency results are largely formal negative results without practical conditions. These are real but not fatal limitations.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>