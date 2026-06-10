Now I have enough calibration data. Let me write the final review.

**Calibration anchors retrieved:**

Round 1:
- 28TLorTMnP.md (2.50, weak) - LLM alignment with listwise rewards, rejected - too different topic
- aYYZBPoSHb.md (3.40, weak) - Multi-objective alignment, rejected - weaker than our paper
- EVZnnhtMNX.md (3.00, weak) - Convex optimization for DPO, rejected - weaker contribution
- fTdhM7q1o2.md (3.00, weak) - Reward learning with ties, rejected
- pzmbxkCBiq.md (5.00, mid) - Likelihood over-optimisation in DAAs, rejected - empirical concerns
- oK1zJCWBqf.md (5.80, mid) - Soft Preference Optimization, rejected
- Nvw2szDdmI.md (7.00, strong) - Distributional optimization with convergence guarantees, accepted
- Lz5lOSC0zg.md (5.25, mid) - Differentiable NDCG ranking, rejected
- rfdblE10qm.md (8.00, strong) - Rethinking reward modeling, accepted
- NN6QHwgRrQ.md (8.00, strong) - Multi-human-value alignment, accepted
- TTrzgEZt9s.md (8.00, strong) - DRO with bias/variance reduction, accepted
- zl0HLZOJC9.md (8.00, strong) - Probabilistic learning to defer, accepted

Round 2:
- EW62GvCzP9.md (4.67, mid-low) - Peer prediction for model eval, rejected - interesting idea, significant weaknesses
- f7ZEcoSdXQ.md (4.75, mid-low) - Incentivizing data collection in FL, rejected
- yCEf1cJDGh.md (5.25, mid) - Truthful aggregation of LLMs, rejected - limited novelty, insufficient experiments
- o1RqSVIf3c.md (4.25, mid-low) - Bayesian preference elicitation, rejected
- JJ46kIfPio.md (4.00, mid-low) - Learning to persuade population, rejected
- JQQDePbfxh.md (6.50, mid-high) - Private mechanism design via quantile estimation, accepted - strong theoretical novelty, lacks experiments
- lvSMIsztka.md (7.50, strong) - Faster approximation of probabilistic values, accepted
- A3YUPeJTNR.md (8.00, strong) - Cost of waiting for accurate predictions, accepted
- jJXZvPe5z0.md (6.67, mid-high) - No-regret dynamics in IR games, accepted
- NO6Tv6QcDs.md (6.50, mid-high) - Limits to scalable evaluation, accepted
- ylhKbwJrjC.md (4.67, mid-low) - Mechanism design with MAB, rejected
- z1Jq1PLQWs.md (5.67, mid) - Dueling in the dark, rejected

**Round 1 bracket:** Between 4.5 and 6.5 — the paper has a clean theoretical contribution (better than the 4-5 range rejected papers) but a significant evaluation gap (worse than the 6.5+ accepted papers).

**Round 2 narrowing:** The paper is clearly above "Truthful Aggregation" (5.25, rejected) which has similar themes but less theoretical depth. It's comparable to "Peer Prediction" (4.67, rejected) in having interesting ideas with empirical concerns, but our paper has more complete theory. It's below "Private Mechanism Design" (6.50, accepted) which has stronger novelty. I'd place it around 5.5.

## Summary
This paper proposes Aligned Scoring Rules (ASR) for textual information elicitation in peer grading, building on Wu & Hartline (2024)'s reduction framework. The authors optimize over separate proper scoring rules via convex programming to minimize MSE between the proper score and a reference score (instructor or LLM-Judge), preserving provable properness. Experiments on peer grading data show large improvements over non-aligned baselines.

## Strengths
- **Clean convex optimization formulation (Program 2, Corollary 3.4):** By optimizing over separate scoring rules with 6 variables per dimension, the alignment problem is convex with linear properness constraints and boundedness constraints, guaranteeing global optimality. This is explicitly contrasted with the non-convex max-over-separate alternative.
- **Provably proper while aligning to non-proper references (Theorems 3.2/3.3, Program 2 constraints):** The core contribution converts non-proper reference scores into proper ones — addressing a genuine gap where prior work achieved properness but not alignment, and direct reference scores achieved alignment but not properness.
- **Large empirical improvements (Table 1):** ASR reduces MSE by over 5× vs. EGPT(AV) (9.541→1.730 for instructor; 7.053→2.003 for LLM-Judge) and more than doubles Pearson correlation (0.294→0.717; 0.328→0.705).
- **Dual reference score validation (Section 5.2, Table 1):** Demonstrates ASR works with both instructor and LLM-Judge scores, with documented correlation (r=0.554), providing evidence for LLM-Judge as a scalable substitute.

## Weaknesses

### Fatal
None.

### Major
- **No train/test split — all metrics reflect optimization fit, not generalization.** ASR is optimized by minimizing MSE against the reference score over the entire dataset (Program 2, Section 3.2), and the reported metrics (Table 1) evaluate on that same data. The paper mentions "training data D" (line 358) for the Best Constant Score baseline but never defines a separate test set. With 6m free parameters per assignment cluster (6 variables per dimension × m dimensions, where m is unreported) and roughly 36–64 peer reviews per cluster, the parameter-to-data ratio is concerning. The baselines EGPT(AV) and EGPT(MV) are fixed functions from prior work with no data-dependent optimization, so comparing ASR against them on training data inherently favors the optimized method. Cross-validation or holdout evaluation within each cluster is essential to validate the empirical claims.

- **Number of summary dimensions m never reported.** Each assignment cluster has 6m ASR parameters. The paper never reports m for any assignment, making it impossible to assess the parameter-to-data ratio or overfitting risk. From the paper's example (Section 2.2, 4 dimensions for one induction homework), m could range from 3–10+, yielding 18–60+ parameters for 36–64 data points. This directly matters given the absence of cross-validation.

### Minor
- **Moderate correlation described as "high."** The paper states "There is a high correlation between the Instructor Score and LLM-Judge score" with Pearson r=0.554 (line 320). r=0.55 means ~30% shared variance — moderate at best. When ASR is aligned to LLM-Judge scores, alignment quality depends on what LLM-Judge measures, and this moderate correlation bounds that quality.
- **No per-assignment variance reported.** Table 1 aggregates across 22 assignments without standard deviations or per-assignment breakdowns, making it hard to assess result reliability.
- **V-shaped scoring rule codomain inconsistency.** Definition 2.4 states S: [0,1]×[0,1]→[0,1/2], but the formula produces values up to 1 (when θ=1, r>p: S = 1/2 + 1/2·(1-p)/(1-p) = 1). Minor notation issue.

### Trivial
None.

## Nice-to-Haves
- Cross-validation within each assignment cluster to validate generalization.
- Report m per assignment and discuss parameter-to-data ratios.
- Brief interpretability illustration in the main text (currently deferred to Appendix C, despite being listed as a contribution in the abstract).
- Discussion of what reference score is available at deployment time.

## Removed Points
- Harsh critic's "baseline comparison is structurally unfair" as a separate weakness: merged with the no-train/test-split issue since they are the same underlying concern (ASR optimized, baselines not, evaluated on same data).
- Harsh critic's codomain issue framed as "structural": demoted to minor notation inconsistency.

## Novel Insights
The key tension in this paper is between a clean theoretical contribution (convex optimization of aligned proper scoring rules with provable properness) and a significant empirical gap (no generalization evaluation, unreported parameter counts). The theory is sound and the framework is useful, but the reported experimental gains cannot be distinguished from overfitting without cross-validation. If the results hold out-of-sample, this would be a substantially stronger paper.

## Suggestions
1. Add cross-validation: optimize on a subset of reviews per cluster, evaluate on held-out reviews.
2. Report m (number of summary dimensions) per assignment and discuss the parameter-to-data ratio.
3. Report mean ± std across assignments in Table 1.
4. Fix the V-shaped scoring rule codomain in Definition 2.4 (should be [0,1] not [0,1/2]).

## Reporting

All anchors retrieved:

**Round 1:**
- 28TLorTMnP.md (2.50) - LLM alignment with listwise rewards; weaker contribution
- aYYZBPoSHb.md (3.40) - Multi-objective alignment ORPO; weaker contribution
- EVZnnhtMNX.md (3.00) - Convex DPO; weaker contribution
- fTdhM7q1o2.md (3.00) - Reward learning with ties; weaker contribution
- pzmbxkCBiq.md (5.00) - Likelihood over-optimisation; rejected, comparable empirical concerns
- oK1zJCWBqf.md (5.80) - Soft Preference Optimization; rejected
- Nvw2szDdmI.md (7.00) - Distributional optimization for diffusion; accepted, stronger convergence guarantees
- Lz5lOSC0zg.md (5.25) - Differentiable NDCG ranking; rejected
- rfdblE10qm.md (8.00) - Rethinking reward modeling; accepted, stronger theory + experiments
- NN6QHwgRrQ.md (8.00) - Multi-value alignment palette; accepted
- TTrzgEZt9s.md (8.00) - DRO with bias/variance reduction; accepted
- zl0HLZOJC9.md (8.00) - Probabilistic learning to defer; accepted

**Round 2:**
- EW62GvCzP9.md (4.67) - Peer prediction for model eval; rejected, similar pattern of interesting idea with empirical gaps
- f7ZEcoSdXQ.md (4.75) - Incentivizing data collection FL; rejected
- yCEf1cJDGh.md (5.25) - Truthful aggregation of LLMs; rejected, our paper has stronger theory and results
- o1RqSVIf3c.md (4.25) - Bayesian preference elicitation; rejected
- JJ46kIfPio.md (4.00) - Learning to persuade population; rejected
- JQQDePbfxh.md (6.50) - Private mechanism design; accepted, stronger novelty but lacks experiments entirely
- lvSMIsztka.md (7.50) - Faster probabilistic value approximation; accepted
- A3YUPeJTNR.md (8.00) - Cost of waiting for predictions; accepted
- jJXZvPe5z0.md (6.67) - No-regret dynamics IR games; accepted
- NO6Tv6QcDs.md (6.50) - Limits to scalable evaluation; accepted
- ylhKbwJrjC.md (4.67) - Mechanism design with MAB; rejected
- z1Jq1PLQWs.md (5.67) - Dueling in the dark RLHF; rejected

**Bracket:** Round 1 placed the paper between 4.5 and 6.5. Round 2 narrowed to 5.0–6.0. The paper is clearly above the rejected papers at 4.0–5.25 (which have weaker theory and/or less empirical substance) but below the accepted papers at 6.5+ (which have stronger novelty or fewer methodological gaps). The closest anchor is "Private Mechanism Design" (6.50, accepted), which has stronger novelty but zero experiments — our paper has more extensive experiments but a fundamental evaluation flaw. Our paper is also clearly above "Truthful Aggregation" (5.25, rejected) which shares similar themes but has less theoretical depth and weaker results. Final score: 5.5 — the theoretical contribution is solid and the paper is well-written, but the lack of generalization evaluation is a significant gap that prevents a higher score.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>