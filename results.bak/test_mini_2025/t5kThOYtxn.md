Now I have sufficient calibration data. Let me write the final consolidated review.

---

## Summary

This paper introduces *stable bandit algorithms*—algorithms for which the number of pulls of each arm, normalized by a non-random sequence, converges in probability to 1. Under this stability condition, the sample means become asymptotically normal (Lemma 1), enabling standard Gaussian confidence intervals without debiasing or martingale post-processing. The paper proposes two families: a 2-batch Explore-Then-Commit algorithm (Algorithm 1) and a B-batch elimination algorithm (Algorithm 3), proves they are stable, gives explicit non-random scalars for the pull counts, and shows that the data-dependent variant (Algorithm 2) attains regret within a factor of 4 of the asymptotic lower bound. The core message is that algorithm design, rather than post-hoc correction, can resolve the tension between regret minimization and valid inference.

## Strengths

- **Lemma 1 cleanly connects stability to asymptotic normality.** If an algorithm satisfies Eq. (1) (pull counts converge in probability to non-random scalars), then the Martingale CLT gives √n_{a,T}(μ̄_{a,T}−μ_a) → N(0, σ²_a). This provides a crisp sufficient condition for classical inference on bandit data. (Section 3.1)

- **Theorem 1 gives explicit, verifiable stability conditions for a concrete 2-batch algorithm.** For Algorithm 1, the non-random scalars n₁^*, n₂^* are provided in Eqs. (8)–(9) as a function of β = lim mΔ²/(8 log T), turning the abstract definition of stability into a checkable property. The partial proof in Section 4 for β ≤ 1 is logically sound and clearly presented. (Section 3.2.2)

- **Corollary 2 demonstrates that stability and near-optimal regret are compatible.** Algorithm 2 achieves n_{2,T}/(4 log T / Δ²) → 1 and a regret bound R_T ≤ 16 log T / Δ + lower-order terms, matching the asymptotic lower bound (liminf R_T / log T ≥ 4/Δ) up to a constant factor of 4. This directly supports the paper's central thesis. (Section 3.2.3)

- **The paper identifies and formalizes the instability of common algorithms.** Lemma 2 (citing Zhang et al. 2020) shows that the naive ε-greedy ETC algorithm produces non-Gaussian limiting distributions when Δ = 0, motivating the need for the proposed stable designs. (Section 3.2.1)

- **Theorem 2 extends the stable framework to B-batch settings with fixed per-batch pulls, showing the concept generalizes beyond the 2-batch case.** (Section 3.3)

## Weaknesses

### Fatal
None.

### Major
None. The paper has no structural flaw that invalidates its core claims.

### Minor

1. **The experimental evidence is too thin to fully support the "free inference" claim.** Only one figure (two density plots for arm 1 of two algorithms) is provided. The paper would substantially benefit from even a small simulation study showing (a) coverage of nominal 95% confidence intervals from the stable algorithms across a range of Δ values, (b) coverage from an unstable algorithm to illustrate the failure mode, and (c) a comparison of interval widths or regret. As written, the empirical claim of "free inference" is supported only by a visual inspection of two density plots at T=1000.

2. **The title oversells "Optimal Regret."** The paper itself states the regret bound is within a factor of 4 of the asymptotic lower bound (Section 3.2.3). While "optimal up to a constant factor" is accurate, the unqualified "Optimal Regret" in the title could mislead readers into thinking the lower bound is matched. The title should be qualified (e.g., "Near-Optimal Regret with Free Inference").

3. **All results are strictly for two arms.** The paper mentions "multi-armed bandits" in its contributions and abstract, but every theorem, lemma, and algorithm is tailored to K=2. The Discussion (Section 5) mentions the K-armed case as future work but does not explain the challenges. This limits the practical significance of the results.

4. **The β > 1 case of Theorem 1 is deferred to the appendix with only a brief note.** Section 4 provides a detailed proof for β ≤ 1 but only states "The proof of the case β > 1 is similar, and the details are moved to Appendix." A brief sketch in the main text (even 3–4 lines explaining how the analysis changes when mΔ²/(8 log T) → β > 1) would improve completeness, especially since the non-random scalars differ between the two regimes (Eqs. 8 vs. 9).

### Trivial
None.

## Nice-to-Haves

- A brief heuristic explanation for why the B-batch algorithm (Algorithm 3) achieves the same asymptotic scalars as the 2-batch algorithm (Eq. 14 vs. Eq. 9) despite the fixed batch size m. The current presentation treats this as a corollary of the appendix proof, but the invariance to batch structure is interesting and deserves a short intuitive remark.
- A discussion of how the choice of bonus term q_T (Corollary 1) affects the trade-off between regret and the speed at which asymptotic normality kicks in. The paper notes that any q_T dominating √(2 log log T) works, but does not discuss whether a smaller q_T would yield tighter regret bounds at the cost of slower convergence to normality.
- A comparison table or paragraph contrasting the proposed approach with existing post-processing methods (debiased estimators, Martingale CLT methods) in terms of CI width, coverage accuracy, and computational overhead.

## Removed Points
These points were considered but removed with justification:

- *"B-batch stability is insufficiently supported / relies on the appendix"* — Removed per hard rules: the paper states the proof is in Section A.3, which was stripped by the parser.
- *"Stability is a known structural property, not a new concept"* — Removed as a strawman: the paper acknowledges the connection to Lai & Wei (1982) and does not claim the definition itself is the primary contribution. The contribution is in designing *algorithms* that achieve stability.
- *"Lindeberg condition is hand-waved"* — Removed: the paper's brief justification (bounded third moment, sub-Gaussian rewards) is standard and sufficient for a conference paper at this level.
- *"The framing of 'two historically conflicting paradigms' is overblown"* — Removed as a presentation opinion, not a factual weakness.
- *"Section 2 should note that scaling requires knowing the sub-Gaussian parameter"* — Removed as a trivial clarification; the paper states this is a standard assumption.
- *"Data-dependent stopping proof is not provided"* — Removed per hard rules: the proof is deferred to the appendix (stripped).
- *"B-batch scalars are the same as 2-batch, which is surprising"* — Moved to Nice-to-Haves as a request for exposition rather than a weakness.
- *"Missing comparison with existing inference methods"* — Moved to Nice-to-Haves as scope beyond what a theoretical paper requires.
- *"K-armed extension should be more prominently stated as a limitation"* — Retained as Weakness #3 but in a compressed form.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions

1. **Add a small simulation study** with 3–4 panels: (a) coverage of nominal 95% CIs for both arms under Algorithm 1 or 2, (b) coverage for an unstable algorithm (e.g., naive ε-greedy ETC) to show the failure, (c) average regret. This would directly substantiate the "free inference" narrative at low cost.
2. **Qualify the title** (e.g., "Near-Optimal Regret with Free Inference").
3. **Add a few lines sketching the β > 1 case** of Theorem 1 in Section 4, explaining how the analysis changes when the exploration phase is sufficient to identify the better arm.
4. **Acknowledge the 2-arm limitation more prominently** in the introduction or as a bullet point, rather than only in the final Discussion section.

---

## Score and Decision

**Round 1 bracket:** The paper sits between the weak bandit-theory anchors (avg ~2.3, papers with fundamental issues) and the strong anchors (avg 8.0, outstanding papers). The relevant band is the middle range. Anchors:
- "{Weak} Dynamic Assortment Selection and Pricing" (avg 3.0, Reject) — much weaker paper with unclear central contribution
- "{Weak} Regret measure in continuous time limit" (avg 2.33, Reject) — unclear practical relevance
- "{Middle} Breaking the log(1/Δ2) Barrier" (avg 5.75, Accept Poster) — comparable quality: solid theory, limited experiments, mixed reviews. The paper under review has a cleaner conceptual contribution and better exposition.
- "{Middle} Almost Optimal Batch-Regret Tradeoff" (avg 7.0, Accept Poster) — stronger paper with matching upper/lower bounds and a new concentration inequality. The paper under review is weaker than this anchor.
- "{Middle} Sample-Efficiency in Multi-Batch RL" (avg 6.33, Accept Poster) — stronger theoretical lower bound results.
- "{Middle} Second Order Bounds for Contextual Bandits" (avg 6.0, Accept Poster) — comparable level: theory paper without experiments, mixed reviews (5,8,6,5). The paper under review is of similar quality.
- "{Middle} Only Pay for What Is Uncertain" (avg 6.20, Accept Poster) — theory + experiments. The paper under review has a more novel conceptual contribution but weaker experiments.
- "{Middle} Pairwise Elimination" (avg 5.75, Accept Poster) — comparable: solid theory, some experiments, clean contributions.
- "{Strong} The Hidden Cost of Waiting" (avg 8.0, Oral) — clearly stronger paper
- "{Strong} Learning to Relax" (avg 8.0, Spotlight) — clearly stronger paper

**Round 2 narrowing:** Within the (4, 7.5) bracket, the paper is most comparable to papers scoring 5.75–6.2. It has a genuinely novel concept (stable algorithms) and clean theory, but is limited by thin experiments and the 2-arm scope. It is stronger than the weakest middle anchors (e.g., the 4.75 "Algorithmic Stability Unleashed" Reject) and comparable to accepted poster papers at the 5.75–6.2 level.

**Final score:** 6.0. The paper makes a clear, novel contribution with sound theory. The weaknesses (minimal experiments, title overreach, 2-arm scope) are fixable and do not undermine the core intellectual contribution, but they prevent the paper from reaching the 7+ tier.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>