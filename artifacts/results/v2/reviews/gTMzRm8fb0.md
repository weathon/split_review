Now I have all the information I need to construct the final review. Let me compile it.

## Summary of Calibration

**Round-1 Bracket:** 5.5 – 7.0

**Calibration anchors consulted (all rounds):**

| Path | Avg Score | Source | Comparison |
|------|-----------|--------|------------|
| Hh0Cg4epYY | 2.33 | r1-topic-low | Fundamentally flawed paper; GoalRank is clearly stronger |
| cya3eEczAx | 1.67 | r1-topic-low | Same — GoalRank is much higher quality |
| Zy7zGe5YfE | 3.00 | r1-topic-low | Same |
| Eg32tDGgF5 | 3.00 | r1-topic-low | Same |
| aDG34Bhbs1 | 4.80 | r1-topic-mid | Relevance embeddings — weaker empirical validation |
| sb1HgVDLjN | 6.67 | r1-topic-mid | Offline MBO by Learning to Rank — similar structure (theory+new objective+strong experiments), slightly cleaner narrative but no online test |
| 6tqgL8VluV | 6.00 | r1-topic-mid | Learned DB operations — different domain but similar quality tier |
| TVDUVpgu9s | 6.00 | r1-topic-mid | ZO-RankSGD — closest structural match: theory → new algorithm → experiments, similar weaknesses (theory-practice gap, limited experiments in some areas). GoalRank has stronger empirical validation (online A/B) but similar theory-algorithm disconnect |
| 4o4fDJL6I7 | 4.00 | r1-weakness-missing-ablation | NAS ranking loss eval — lower quality, limited novelty |
| BMqBvRPDhX | 6.00 | r1-weakness-missing-ablation | Logit distillation with ranking loss — similar distillation framing |
| XnX7xRoroC | 6.25 | r1-weakness-missing-ablation | Distilling RL into datasets — interesting but narrower scope |
| cbttLtO94Q | 6.25 | r1-weakness-eval-disconnect | How to evaluate reward models for RLHF — stronger evaluation methodology |
| 1FfzgglqI2 | 3.50 | r1-weakness-eval-disconnect | Binary Reward Labeling — weaker paper |
| 6GATHdOi1x | 5.75 | r2 | PreferDiff — similar recommender systems paper, less comprehensive experiments |
| 1PDz4Ny1N2 | 6.60 | r2 | Fairness in recommendation — strong theory + experiments, but different sub-area |
| Lz5lOSC0zg | 5.25 | r2 | Differentiable NDCG — similar optimization theme but weaker |
| rfdblE10qm | 8.00 | r1-topic-high | Strong LLM alignment theory paper — clearly higher quality than GoalRank |

**Narrowing:** Within the 5.5–7.0 bracket, the closest comparison points are ZO-RankSGD (6.0) and Offline MBO (6.67). GoalRank is structurally similar to ZO-RankSGD: both have a theoretical result that motivates a new optimization principle, followed by empirical validation. Both have some disconnect between theory and algorithm. GoalRank has stronger empirical validation (3 offline datasets + massive online A/B) than ZO-RankSGD (simulated + limited image generation), but the M confound is a more significant empirical gap than anything in ZO-RankSGD. Offline MBO (6.67) has a cleaner narrative and less confounded experiments, but no online validation. GoalRank sits between these two; I place it at 6.0.

**What the low-band anchors failed at:** Papers scoring ≤ 4.0 had fundamental issues (unsound methodology, unclear contributions, trivial impact, failure to validate core claims). GoalRank does not share those failures — it has a clear theoretical result, a well-defined algorithm, and strong empirical backing. Its weaknesses (missing ablation, theory-practice gap, overclaiming) are significant but addressable, not fatal.

---

## Final Review — GoalRank

---

## Summary

This paper proposes GoalRank, a generator-only (single-stage) ranking framework for recommender systems. The authors prove (Theorem 1) that for any finite (Multi-)Generator–Evaluator system, there exists a single generator-only model with strictly smaller approximation error to the optimal ranking policy, with error vanishing as model size grows. They derive a training objective based on group-relative normalization of a learned reward model's scores, enabling a large generator to be trained via cross-entropy against a group-constructed reference policy. Offline experiments on ML-1M, Amazon-Book, and an industry dataset show large gains over strong baselines, and an online A/B test on a platform with half a billion daily active users demonstrates consistent improvements in business metrics.

---

## Strengths

1. **Clean theoretical result (Theorem 1).** The theorem is correctly stated: for any finite set of bounded generators with an evaluator (soft mixture), there exists a single larger generator whose policy space achieves strictly smaller KL approximation error to the optimal ranking policy, and this error vanishes as the generator grows. This is a non-trivial application of capacity-based approximation arguments (convex hull vs. single larger network) and provides genuine motivation for the generator-only paradigm. The proof strategy (deferred to Appendix A) is sound and the paper is careful to use soft mixtures (which make the baseline stronger).

2. **Strong and consistent offline results across multiple datasets (Table 1).** GoalRank outperforms all baselines (7 G-only, 3 G-E, 3 MG-E with varying ensemble sizes) on ML-1M, Industry, and Amazon-Book across H@6, N@6, M@6, F1@6, and AUC. Improvements over the best baseline reach +25.39% (H@6) and +29.63% (M@6) on the Industry dataset. All improvements are reported as statistically significant (p < 0.05). The MG-E baselines are scaled up to 100 generators, providing a strong comparison point for the paper's core claim.

3. **Positive large-scale online A/B test (Table 4).** GoalRank deployed on a platform serving >500M daily active users yields improvements of +1.212% in Effective View and +0.149–0.197% in Watch Time over the production MG-E system. These results are statistically significant and provide real-world validation that goes beyond offline metrics — this is the strongest evidence in the paper.

4. **Empirical scaling law (Figure 3).** GoalRank's performance improves steadily from 1M to 0.1B parameters, while DNN, RankMixer, and PIER scaled to the same parameter counts show much weaker improvement. This directly corroborates the scaling claim of Theorem 1.

5. **Ablation studies on group size and reward model bias (Tables 2–3).** The ablation of group size |B| (3–100) shows optimal performance at 8–20 and demonstrates that even suboptimal choices still beat baselines. The noise injection experiment (λ = 0.0, 0.2, 0.5) shows graceful degradation, supporting robustness claims.

---

## Weaknesses

### Major

1. **Missing ablation: the auxiliary policy set M is a confound for the paper's core claim.** The paper's group construction requires an auxiliary set of ranking policies M (heuristic methods and lightweight neural models) to ensure sufficient reward gaps within each group B. Without M, the groups would contain only the current generator's own outputs — which the paper acknowledges yields insufficient diversity. This means GoalRank's training relies on distilling knowledge from M. The paper presents no ablation that removes M (e.g., constructing B from MCMC sampling, a replay buffer, or the MG-E system itself), so the source of GoalRank's substantial gains cannot be cleanly attributed to the "large generator" or the "group-relative principle" as opposed to distillation from auxiliary policies. This directly undermines the paper's central narrative (§3.1 theory → §3.2 algorithm → empirical superiority) because the training method depends on an ensemble in a way the theoretical framing does not account for. The missing comparison is not a minor footnote — it is necessary to validate the claimed contribution.

2. **Gap between the theory and the training objective.** Theorem 1 establishes that there *exists* a generator-only model with superior approximation error to π\*. The algorithm then minimizes KL(π\_θ ‖ π^ref) where π^ref is derived from a biased reward model via group-relative normalization. The paper claims to derive "an evidence upper bound" (abstract, §1, §5) but no such bound is ever formally stated or proven in the available text — the derivation in §3.2 is a standard algebraic reduction from entropy-regularized RL to cross-entropy against a softmax of rewards. No formal bound connects KL(π\_θ ‖ π^ref) to KL(π\_θ ‖ π\*), nor relates the approximation error of Theorem 1 (which concerns policy classes) to the training loss. The narrative presents Theorem 1 and the algorithm as a unified story, but rhetorically they remain two separate contributions. This is a structural weakness in the paper's argument chain, not merely a missing proof.

### Minor

3. **Overclaiming in the abstract and introduction.** The paper states that GoalRank "enjoys a scaling law as its size increases" (abstract), phrasing this as a property of the generator architecture. In reality, scaling is demonstrated only when the generator is trained with the proposed group-relative objective under a specific reward model. The same scaling curves for baselines (DNN, RankMixer, PIER) use their own standard losses, so the scaling advantage could reflect the training signal rather than the architecture. This conflation matters because the paper's theoretical scaling claim (Theorem 1) is about approximation error of a model class, while the empirical scaling (Figure 3) mixes architecture, objective, and training data composition. Separating these would require comparing e.g. DNN trained with the group-relative loss vs. with its standard loss at each scale.

4. **The "evidence upper bound" is invoked but never instantiated.** The phrase "evidence upper bound" appears in the abstract, introduction, and conclusion but never receives a formal definition or derivation. The derivation in §3.2 provides a standard reduction from an entropy-regularized RL objective to cross-entropy against a Boltzmann distribution over rewards — this is a well-known equivalence, not an "upper bound." Using this terminology without formal grounding weakens the paper's technical credibility.

5. **Offline evaluation metrics do not directly measure what the method optimizes.** The training objective maximizes the likelihood of π^ref constructed from a learned reward model (trained on long-view / watch-time feedback). The offline evaluation uses Hit Ratio, NDCG, and MAP against chronological ground truth (the last six interactions). These are different constructs: a ranking that maximizes expected user utility need not match the observed interaction order. The paper offers no correlational analysis showing that the reward model's list scores align with chronological ground truth. This disconnect limits the interpretability of the offline results, though the online A/B test does provide a complementary validation that partially addresses the concern.

### Trivial

6. The "generator-only" framing is primarily accurate at inference time. At training time the method uses auxiliary policies M, which is standard for distillation but could be clarified in the title and throughout to avoid confusion.

---

## Nice-to-Haves

- **Comparison with RL-based ranking methods (e.g., REINFORCE against the same reward model).** Such a comparison would isolate the benefit of the group-relative distribution from the general advantage of training against a learned reward.
- **Ablation where B is constructed solely from the MG-E system (instead of specialized M policies).** This would clarify whether the auxiliary set M provides unique value, or whether any sufficiently diverse set of candidate lists suffices.
- **Computational cost analysis (training FLOPs, inference latency) relative to MG-E baselines.** The paper mentions that GoalRank reduces inference cost (single generator vs. many), but provides no quantitative comparison.
- **Sensitivity analysis of the implicit temperature created by the μ\_B / σ\_B normalization** to different reward scales and group compositions.

---

## Removed Points

*These points appeared in reviewer inputs but were filtered after cross-checking against the paper.*

- **"The offline evaluation is fundamentally unaligned with the reward model" (weakened to Minor 5).** Using chronological held-out interactions as ground truth is standard practice in recommender systems evaluation. The online A/B test provides additional validation. The critic's framing overstated the severity.
- **"The scaling comparison (Figure 3) is apples-to-oranges" (removed).** DNN, RankMixer, and PIER are all scaled by the same parameter counts as GoalRank. Only MG-E is scaled by generator count, which is a natural axis for that baseline. The critic's proposed comparison (DNN trained with GoalRank's loss) is a valid suggestion but the current comparison is not misleading.
- **"Standardization does not remove additive or multiplicative bias" (removed — factually incorrect).** Subtracting μ\_B removes any constant additive bias. The paper's claim about partial-order preservation under large reward gaps is heuristic but not flawed in the way the critic stated.
- **"Theorem 1's reliance on universal approximation for continuous functions is a gap for discrete ranking" (removed).** Discrete functions are a subset of continuous functions; the universal approximation argument applies. This is a non-issue.
- **"Performance plateau (Figure 1d) is presented as universal without diagnosis" (removed).** This is motivation, not a technical claim. The single dataset shown is sufficient for motivating the research question.
- **"Missing comparison to RL baselines" (moved to Nice-to-Haves).** Standard ranking methods (DNN, DLCM, PRM, PIER, etc.) are the main baselines in this line of work. Requesting PPO/REINFORCE baselines is reasonable but non-standard for the paper's community.
- **"Missing computational cost analysis" (moved to Nice-to-Haves).**

---

## Novel Insights

None beyond the paper's own contributions. The reviews surface the theory-practice gap and the M confound as the central unresolved questions, but these are observations about the paper's framing rather than novel technical insights about the problem.

---

## Suggestions

1. **Ablate the auxiliary set M.** This is the single most important missing experiment. Compare GoalRank against a variant where B is constructed solely by sampling multiple lists from the current generator (e.g., using temperature scaling, dropout, or a small replay buffer). If performance collapses, the method should be reframed as an ensemble-distillation approach rather than a pure generator-only demonstration. If performance remains competitive, the paper's central claim is substantially strengthened.

2. **Formalize the connection between Theorem 1 and the training objective.** Derive (or at minimum state clearly as a conjecture) a bound relating KL(π\_θ ‖ π^ref) to the approximation error E(F\_M). The "evidence upper bound" should either be formally defined or the phrase should be removed from the paper.

3. **Disentangle architecture scaling from training-signal scaling.** Add a comparison where a DNN baseline is trained with the group-relative loss at the same parameter scales as GoalRank, so readers can see how much of the scaling advantage is due to the architecture vs. the objective.

4. **Provide a correlational analysis** between the reward model's list scores and the chronological ground-truth metrics, to validate the offline evaluation protocol.

---

## Score and Decision

**Calibration summary:** Round-1 bracket was 5.5–7.0. Within this bracket, the closest comparisons are ZO-RankSGD (6.0, structurally similar: theory→new optimization principle→experiments, with comparable strengths and weaknesses) and Offline MBO by Learning to Rank (6.67, cleaner narrative but no online validation). GoalRank has stronger empirical validation than ZO-RankSGD (offline across 3 datasets + massive-scale online A/B) but a more significant confound (missing M ablation). The paper's weaknesses are genuine but addressable, not fatal.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>