Now let me write the final review with score and decision.

## Summary
This paper studies offline change point localization and inference in dynamic multilayer random dot product graphs (D-MRDPGs). It proposes a two-stage algorithm combining seeded binary segmentation with low-rank tensor estimation, establishes consistency in estimating the number and locations of change points, and derives limiting distributions of the refined estimators — stated to be the first such results in network change-point literature. Experiments on synthetic and real data demonstrate the method's practicality.

## Strengths
1. **First limiting distribution results for change point estimators in network data.** Theorem 2 derives the limiting distribution of the refined estimator in the vanishing-jump regime as the argmin of a two-sided Brownian-motion process, going beyond the high-probability bounds in prior work (Wang et al. 2021; Padilla et al. 2022). This is a genuinely novel theoretical contribution.
2. **Consistency guarantee for offline detection in multilayer networks.** Theorem 1 establishes consistency for a problem not previously addressed in the literature. The rate κ_k^{-2} log(T) is sharper than the online counterpart in Wang et al. (2025).
3. **Empirical superiority demonstrated across varied scenarios.** In Table 1, CPDmrdpg consistently outperforms gSeg and kerSeg across four scenarios. For example, in Scenario 2 (n=50), CPDmrdpg achieves |K̂−K|=0.00, d(C,Ĉ)=0.00, 100% coverage, while the best competitor kerSeg gives |K̂−K|=0.15, d(C,Ĉ)=1.53. The method also shows robustness when Model 1 assumptions are violated (Scenarios 2 and 3).
4. **Data-driven confidence intervals with strong coverage in simulations.** Table 2 shows 100% coverage for three of four scenarios at n=100, with narrow average lengths. This is a capability not supported by competing methods.
5. **Real-data interpretability.** The detected change points (1991, 1999, 2005, 2013) on agricultural trade networks align with verifiable geopolitical events, and no competing method produces a similarly interpretable set of detections.

## Weaknesses

### Major
- **Gap between theoretical independence assumption and practical implementation.** Theorem 1 and 2 assume four mutually independent adjacency tensor sequences {A(t), A'(t), B(t), B'(t)}. The paper states (line 89) that in practice, both stages are implemented using "the same two split tensor sequences via the odd-even splitting approach." The paper acknowledges this only as "imposed for theoretical convenience" without analyzing how the gap affects the guarantees. This disconnect means the reader cannot directly verify that the proven guarantees apply to the algorithm as actually run. While common in statistics, this deserves a more substantive discussion or a supplementary validation.
- **Confidence intervals in real-data analysis are confusing and potentially inconsistent.** Table 4 reports 95% CIs alongside Algorithm 1's output. For the change point at time point 20 (year 2005), the CI is (17.97, 18.05), which does not contain 20. For time point 28, the CI (25.99, 26.06) does not contain 28. The CIs are constructed around the final refined estimator η̂_k (eq. 5), not the Stage II estimates listed, but this is not explained in the table. The apparent mismatch raises concerns about finite-sample calibration (T=35, n=75) and at minimum requires clarification. If the η̂_k estimates indeed differ substantially from the Stage II estimates, this discrepancy itself warrants discussion.

### Minor
- **Experimental comparison relies on relatively weak baselines in the main text.** The main tables compare only against gSeg and kerSeg — generic change point detection methods not designed for network data. gSeg consistently returns infinite Hausdorff distances, making it a de facto negative baseline. More relevant network-specific competitors (Wang et al. 2025 for online D-MRDPG; Li et al. 2024 for deep learning) are mentioned but deferred to the appendix. The paper would be strengthened by at least one network-specific comparison in the main body.
- **Threshold selection bypasses the theoretical upper bound.** Theorem 1 requires τ to satisfy c_{τ,1} n√L log^{3/2}(T) < τ < c_{τ,2} κ²Δ. The paper sets τ = 0.1 n√L log^{3/2}(T), which satisfies the lower bound but provides no mechanism to check τ < c_{τ,2} κ²Δ. This is a known practical difficulty (κ is unknown), but the paper does not discuss when violations might occur or how they would manifest.
- **Low-rank structural assumption does not transparently follow from the model.** The paper candidly acknowledges (lines 175–179) that the low-rank structure of CUSUM-transformed weight matrices "may not directly or transparently reflect the explicit model structure." Since these Tucker ranks are central to the theoretical analysis and practical choice of TH-PCA input ranks, this ambiguity leaves it unclear when the theoretical results apply beyond carefully constructed simulations.

### Trivial
- The CUSUM statistic notation "u ∈ [t][s]" and "u ∈ [e][t]" in Definition 4 (line 79) is nonstandard and should be clarified (presumably meaning s < u ≤ t and t < u ≤ e).
- Table 1 reports only means over 100 Monte Carlo trials without standard deviations or standard errors, making it difficult to assess the statistical significance of differences between methods.
- The paper does not explain how practitioners should choose the latent dimension d for real data.

## Nice-to-Haves
- A discussion of how the CI procedure behaves when the vanishing-jump condition (κ_k → 0) does not hold, and whether there is a diagnostic for detecting when the approximation is reasonable.
- Sensitivity analysis comparing the odd-even split implementation against a proper four-way split on simulated data.
- Standard errors in Table 1.

## Removed Points
The following points raised by the harsh critic were removed after verification:
- **"Four-sequence issue labeled as fatal/structural":** The paper explicitly acknowledges this gap (line 89). While legitimate, this is a common convention in statistics papers — theory is proved under ideal independence, practical implementation approximates it. Demoted to Major.
- **"Missing comparison against Wang et al. (2021):"** Wang et al. (2021) is a single-layer method requiring non-trivial adaptation to multilayer data. Removed.
- **"More relevant competitors relegated to appendix":** The appendix exists in the original submission. Removed per Hard Rules (parser artifact).
- **"Real-data CIs showing confidence intervals exclude the point estimates themselves":** The harsh critic's phrasing is slightly misleading — the CIs are from the Section 3.1 procedure (centered at η̂_k from eq. 5), not directly around the Stage II estimates listed. However, the mismatch is genuinely confusing and is kept as Major with corrected framing.
- **Strength Finder's editorializing:** "Single most important piece of evidence" language removed. Specific strengths retained.
- **"Experiments with T=200 stretched thin for real data T=35":** Generic concern about asymptotic theory applied to finite samples. Removed.

## Novel Insights
None beyond the paper's own contributions. The observations about the four-sequence independence gap and the CI mismatch in Table 4 are useful diagnostic points but are straightforward once the paper is read carefully.

## Suggestions
1. Address the independence gap: either prove the theoretical results under a two-sequence odd-even split, or implement a proper four-way split in experiments to validate that the theory translates to practice.
2. Clarify Table 4: report the final refined estimates η̂_k alongside the CIs, and explain any discrepancy between Stage II estimates (the "Detected change points" listed) and η̂_k. If the final refinement systematically shifts estimates in the real data, discuss why.
3. Move at least one network-specific comparison from Appendix G.1 into the main body, or provide a stronger rationale for why gSeg/kerSeg are the appropriate baselines.
4. Add standard deviations or standard errors to Table 1.
5. Clarify the CUSUM notation in Definition 4 and explain how practitioners should choose the latent dimension d.

## Score and Decision

**Calibration**: I compared the paper against human-reviewed anchors in three rounds.

*Round 1 (bracketing)*: The paper clearly outranks papers in the 3.0–3.4 range (community detection / clustering) and does not reach the 8.0 level of top ML papers. Relevant middle-range anchors: Node Similarities under Random Projections (5.80, Accept), An Auditing Test for Behavioral Shift in LMs (5.50, Accept), Online Detection for Black-Box LLMs (5.25, Reject), and Change Point Detection via TV-HMM (4.75, Reject).

*Round 2 (narrowing)*: Against these anchors, the current paper has a stronger theoretical contribution (first limiting distributions for network change points) than all comparators and stronger empirical results than TV-HMM and the LLM detection paper. However, the independence gap and CI confusion are more substantial weaknesses than those of the Node Similarities paper (5.80) or the Auditing Test (5.50). The paper is closest in overall quality to the Auditing Test (5.50, Accepted) and the Node Similarities paper (5.80, Accepted), though it has more substantive practical gaps than either.

*Final calibration anchors*:
- Node Similarities under Random Projections (5.80, Accept, Round 2): Stronger presentation, cleaner claims; the current paper has a more significant theoretical result but messier practical validation.
- An Auditing Test (5.50, Accept, Round 2): Comparable mix of theory and practical gaps; this paper was accepted.
- Online Detection for Black-Box LLMs (5.25, Reject, Round 1): Weaker motivation and baselines; current paper is stronger.
- TV-HMM (4.75, Reject, Round 1): Weaker theory and experiments; current paper is clearly stronger.
- Exploring Edge Probability Graph Models (5.75, Reject, Round 2): Comparable score but rejected for limited validation; current paper has stronger experiments.

The paper's theoretical contribution (Theorem 2 — limiting distributions) is genuinely novel and significant. The empirical evidence, while limited by baseline choices, shows clear and consistent superiority. The two major weaknesses (independence gap, CI confusion) are addressable in a rebuttal/camera-ready version. On balance, the paper makes a meaningful contribution that warrants acceptance with revisions.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>