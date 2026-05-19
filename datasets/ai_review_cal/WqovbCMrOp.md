- Decision: Reject
- Avg Score: 5.80
- Scores: 5, 6, 6, 6, 6
Now I have thoroughly verified the paper against both reviews. Let me construct the final consolidated review.

## Summary

This paper studies the effect of temporal aggregation on non-temporal causal discovery, formalizing two notions of recoverability — **functional consistency** (for FCM-based methods) and **conditional independence consistency** (for constraint-based methods). The paper provides necessary and sufficient conditions for both, showing that functional consistency is generically hard in nonlinear settings (even linear-non-Gaussian aggregation degrades identifiability), while conditional independence consistency can be preserved under partial linearity. The theoretical analysis of the three fundamental trivariate structures (chain, fork, collider) reveals that colliders are naturally robust to aggregation, while chains and forks require at least one causal edge from the middle variable to be linear.

---

## Strengths

1. **Formalization of two distinct consistency notions.** The paper introduces *functional consistency* (Definition on additive noise models) and *conditional independence consistency* (Definition 6) as principled criteria specifically tailored to FCM-based and constraint-based methods respectively. Prior work (Fisher 1970, Gong et al. 2017) analyzed only linear or restrictive settings without general definitions. This framing clarifies what "recoverability" means in a way that maps cleanly onto how practitioners use each class of methods.

2. **Characterization of when conditional independence consistency holds and fails for trivariate structures.** The key theoretical result (Theorem 3, the necessary and sufficient condition involving an integral over $Y_{1:k}$, and its sufficient Corollaries 1 and 2) shows that partial linearity — e.g., $f_Z$ being linear in $Y_t$ — is sufficient to preserve the required CI for chain/fork structures. The paper also correctly identifies that collider structures are naturally robust. This goes beyond the earlier linear-only analysis and provides specific, testable guidance.

3. **Explicit construction of the aggregated function for additive noise models.** Theorem 1 provides an exact formula for $\hat{f}$ as a conditional expectation, linking it to Rao-Blackwellization. This gives a concrete handle on why the functional consistency condition is hard to satisfy in the nonlinear case, and leads to a precise necessary-and-sufficient condition (Theorem 2).

4. **Experiment showing identifiability collapse under aggregation for linear-non-Gaussian data.** Section 5.1 (Figure 4) demonstrates that Direct LiNGAM's accuracy drops from ~100% to random guessing as $k$ increases, confirming that temporal aggregation destroys the non-Gaussianity signal that linear FCM-based methods rely on. This is clean experimental support for a key claim.

5. **Approximation argument linking time-delay models to instantaneous aligned models.** Section 2.2 provides a clear mathematical justification (Eq. 2) that for large $k$, aggregation of a lagged VAR model is indistinguishable from aggregation of the aligned instantaneous model, with the difference vanishing as $k\to\infty$. This bridges the theoretical framework with real-world settings.

---

## Weaknesses

### Fatal

None.

### Major

1. **Empirical evaluation is substantially thinner than the paper's experiment list suggests.** The paper states it "conducted five simulation experiments" (Section 5), but of these:
   - Experiment 1 (PC/FCI/GES on 4-variable aggregated data) — results not shown.
   - Experiment 4 ($k$-value effect and justification of approximations) — results not shown.
   - Experiment 5 (PC algorithm with skeleton prior) — results not shown.
   
   Only Experiments 2 (Direct LiNGAM, Section 5.1) and 3 (CI test, Section 5.2) have reported results. Furthermore, the CI experiment explicitly says it tested chain, fork, and collider structures (line 334), but only reports results for the **fork** structure (line 339: "We report the rejection rate for fork structure"). The chain and collider results are mentioned but not shown. The "Due to the page limit" caveat (line 301) is noted, but for a paper whose core claims rest on empirical support, having only one of three trivariate structures reported is a significant gap.

2. **Positive theoretical results for conditional independence consistency require conditions close to linearity.** The paper frames itself as addressing the "general (nonlinear) case" (line 31), but the sufficient conditions (Corollary 2) boil down to requiring the causal mechanism *from Y to Z* or *from Y to X* to be linear. This is a relatively narrow condition. The necessary and sufficient condition (Theorem 3) is an integral equation over the latent $Y_{1:k}$ that is theoretically correct but not practically verifiable — as the paper notes, it does not provide actionable intuition beyond what the corollaries already say. The result is that the paper's positive findings are significantly narrower than the ambitious opening framing suggests.

### Minor

1. **Functional consistency analysis for additive noise models is largely a negative result without boundary characterization.** The paper correctly identifies that the condition in Theorem 2 is "challenging" to satisfy, provides a conditional variance argument, and correctly concludes that functional consistency is hard in the nonlinear case. However, it does not characterize *specific families* of $f$ and distributions of $X_t$ where the condition either holds or fails (e.g., polynomial $f$ with Gaussian $X_t$). The paper's contribution is nevertheless legitimate — identifying the difficulty is a valid result — but the analysis stops short of the deeper characterization one might hope for.

2. **CI experiments only use $k=2$ (minimal aggregation).** While the theory applies to any finite $k$ for the aligned model, showing results at only $k=2$ leaves open whether the empirical patterns hold across aggregation levels. Varying $k$ (e.g., 2, 5, 10) would strengthen the demonstration.

3. **The "different regions" analysis (Section 3.2) adds limited insight.** Theorem 4 essentially states that any two bivariate continuous distributions can be represented as an SEM in either direction, which is a known property. The paper acknowledges this ("due to a lack of constraint, it is always possible to find a consistent function; however, such a function can exist in both directions"). The inclusion is reasonable as a completeness note, but it does not meaningfully extend the paper's contributions.

### Trivial

- There is a minor labeling inconsistency: the CI results table is labeled `\label{experiment result}` (line 316) but referenced as `Table \ref{experiment result2}` (line 339).

---

## Nice-to-Haves

- **Characterize explicit function families for the functional consistency condition.** Providing concrete examples of $f$ and distributions where Theorems 1–2 yield either success or failure would turn a negative result into a more informative boundary. For instance, analyzing polynomial $f$ with Gaussian $X_t$ or other tractable families.
- **Report the chain and collider CI experiment results** (presumably in the appendix) to complete the empirical picture.
- **Vary $k$ in the CI experiments** to demonstrate robustness of the theoretical conditions across aggregation levels.
- **Discuss practical guidance.** The paper honestly acknowledges not providing a solution; even brief practical recommendations (e.g., "if temporal aggregation is suspected, constraint-based methods may be more reliable than FCM-based methods, provided some linearity exists") would increase impact.

---

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Harsh critic's claim about missing discussion of prior work on coarsened/ecological data (Greenland & Rothburn, King, etc.):** Removed per instructions — the reviewer cannot confirm the existence or relevance of these references without external sources.
- **Harsh critic's claim about missing experimental details (kernel bandwidth, regularization):** Removed as a reproducibility nitpick about trivial implementation details.
- **Harsh critic's claim about column labels I–VI being poorly explained:** Removed — the table caption actually explains the columns ("For column VI, the closer to 5%, the better. For all other columns I to V, a higher rate is better"). The critic misread this.
- **Strength Finder's misattribution of Theorem 4 to the CI result:** The relevant theorem for CI consistency is Theorem 3 (labeled `ci main theorem`). Theorem 4 is about functional consistency across different regions. The substantive content of the strength is still correct when referring to the right theorem.
- **Harsh critic's claim about the collider not being experimentally verified:** The collider consistency result is a *theoretical* claim (Remark 1), not an experimental one. The paper correctly proves it from the structure of the aligned model. The critic conflates theoretical proof with experimental verification.
- **Harsh critic's criticism about aligned model vs. time-delay model handling:** The paper actually addresses this carefully (lines 100–102), explicitly stating that all results apply to the aligned model for any finite $k$, and only require large $k$ when connecting to the time-delay model. The paper also notes when $k$ is too small for this approximation, temporal discovery should be used instead.

---

## Novel Insights

None beyond the paper's own contributions. The reviews surface the framing-vs.-scope tension and the experimental thinness, but these are observations about presentation and completeness, not novel technical insights that the reviews discovered independently.

---

## Suggestions

1. **Report the chain and collider CI experiment results in the main text**, even if briefly, to match the claim that all three structures were tested. A small table or a single sentence summarizing the collider/chain results would substantially strengthen the empirical support.
2. **Vary $k$ in the CI experiments** (e.g., $k \in \{2,5,10\}$) to demonstrate that the theoretical conditions are robust across aggregation levels, especially since the aligned model theory applies for any finite $k$.
3. **Temper the "general nonlinear" framing slightly** to match the partial-linearity conditions of the positive results. The paper's actual contribution — showing that full nonlinearity destroys consistency but partial linearity can salvage it — is valuable and should be advertised straightforwardly.
4. **Add a practical guidance paragraph** to the conclusion. Even without providing a complete solution, a short discussion of *which* scenarios are more or less safe for causal discovery under aggregation would increase the paper's impact.

---
