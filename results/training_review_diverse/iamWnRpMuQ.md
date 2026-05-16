Now I have all the information I need to write the consolidated review. Let me synthesize.

---

## Summary

This paper proposes UGDA, a three-stage method for reward model refinement in RLHF. UGDA uses reward model ensembles to collect policy interaction data, then selects a subset via a two-stage criterion (reward variance uncertainty + gradient-based influence computed on policy checkpoints). The selected samples are relabeled by GPT-4, projected onto the reward model's score distribution, and used to refine the reward model via MSE regression, after which the policy is retrained. The method aims to address the off-distribution problem in reward modeling without collecting new human preference data.

## Strengths

1. **Novel two-stage data selection combining uncertainty and gradient influence.** The idea of selecting interaction data for reward model refinement using *both* reward variance (uncertainty) and gradient-based influence scores is novel in the RLHF context. The ablation study (Figure 4) confirms that removing either component degrades performance, validating the combined design.

2. **UGDA achieves competitive or superior policy performance on clean external benchmarks.** On instruction-following benchmarks (AlpacaEval, Arena-Hard, MT-Bench) shown in Figure 3 and RewardBench (Figure 6), UGDA outperforms baselines. These benchmarks are uncontaminated by the data leakage issue and provide independent evidence that the method works.

3. **Robustness to noisy preference data is demonstrated.** Under 20% label noise in the reward training data (Table 3), UGDA shows smaller degradation relative to baselines (e.g., Gemma-7B helpful Avg_Reward drops 3.2% vs. PPO's 4.2%) and maintains the best absolute scores.

4. **Reward model evaluation confirms downstream benefits.** Reward model accuracy on HH test sets (Figure 7) and RewardBench scores (Figure 6, all categories except Reasoning) show UGDA-refined reward models outperform baselines, supporting the claim that the refinement improves reward quality.

5. **Practical efficiency via low data budget and GPT-4 relabeling.** Only 25% of interaction data is selected for refinement, and GPT-4 serves as a cost-effective substitute for human annotation (Table 1 reports high similarity with human labels).

## Weaknesses

### Fatal
None.

### Major

1. **Data leakage in gradient-based influence evaluation on HH dataset.** The validation samples used to compute influence scores (Eq. 10–11) are the *instructions and chosen responses from the HH test sets* (Section 5.1, line 214). The same test sets are then used to report the main policy evaluation results (Table 2, Table 3) and reward model accuracy (Figure 7). Because the influence function selects interaction data that maximizes gradient similarity to these test-set examples, the data-selection process benefits from knowledge of the test distribution. This gives UGDA an informational advantage over baselines that do not use the test set at any stage. **The HH results in the main comparison tables are potentially inflated and cannot be taken at face value.** The external benchmarks (AlpacaEval, Arena-Hard, MT-Bench, RewardBench) are not contaminated, so the method's core claims have partial support, but the paper's primary quantitative evidence (Table 2) is compromised.

### Minor

2. **Structural mismatch between influence target and refinement objective.** The gradient-based influence (Eq. 10–11) measures how much training an interaction sample *z* would reduce the *policy's* loss on validation examples. However, the selected samples are used to refine the *reward model*, not the policy directly. The paper's justification (line 137: "The main goal of the reward model is to optimize the policy") provides a reasonable intuition but no formal or empirical analysis of why influence on the policy's loss should transfer to reward model refinement. The ablation shows the combined approach works, but the independent contribution of the gradient component is confounded with this conceptual gap.

3. **No sensitivity analysis for selection thresholds γ and η.** Both thresholds are fixed at 0.5 (selecting 25% of interaction data), with no ablation or analysis showing how performance varies with the selection budget (e.g., 10%, 25%, 50%). Since the number of selected samples directly determines GPT-4 API cost and refinement computation, this is a practically relevant missing analysis.

4. **Robustness experiment tests label noise rather than distribution shift.** The paper's central thesis is that UGDA addresses distribution shift from policy interaction. However, the robustness experiment (Table 3) flips 20% of preference pairs in the *original reward training data* — testing label noise, not distribution shift. A more relevant test would vary the degree of distribution shift (e.g., number of PPO steps before data collection) or inject noise into the interaction data before selection.

5. **Quantile-based reward projection (Eq. 13) makes a strong distributional assumption.** Mapping GPT-4's 1–5 ordinal scores onto the reward model's empirical quantiles assumes the reward model's score distribution aligns with a five-level ordinal scale. The added Gaussian noise ε does not correct systematic misalignment, and the impact of projection errors on the refinement loss (Eq. 14) is not studied. Additionally, the human vs. GPT-4 similarity comparison (Table 1) is reported for only a single prompt — a very narrow validation.

6. **Projection dimension for random projections is not reported for main experiments.** The robustness experiment mentions a projection dimension of 8192 (line 249), but the main experiments do not specify this value, hampering reproducibility.

7. **Ensemble size k=3 is used without justification or sensitivity analysis.** The paper does not analyze whether results are sensitive to the number of ensemble members (e.g., k ∈ {2, 3, 5}).

### Trivial

8. **RLR baseline description could be more explicit.** While the paper states that RLR uses random selection of 25% of interaction data with GPT-4 annotation (line 216), it does not explicitly confirm whether the same MSE refinement loss is used. The description is adequate for a baseline but would benefit from a one-sentence clarification.

## Nice-to-Haves

- Replace the test-set-derived validation samples with a held-out portion of the HH *training* set for influence computation, and re-report the HH results. This would eliminate the leakage concern and make the HH test-set results trustworthy.
- Disentangle the uncertainty and gradient selection criteria further: report the overlap between the two criteria, and report ablation results on external benchmarks (not just HH) to verify that gains on clean benchmarks are not masking HH-specific leakage.
- Add a sensitivity analysis on γ and η (e.g., 10%, 25%, 50% selection budgets) and on ensemble size k.

## Removed Points

- **Criticism about RLR baseline under-description (original):** The paper does describe RLR as random selection of 25% of interaction data with GPT-4 annotation (line 216). While the MSE loss is not explicitly stated, the fair-comparison framing makes it clear the same pipeline is used. This is a minor clarity issue, not a genuine weakness. → Moved to Trivial.

- **"The quantile projection is too strong an assumption" as a major point:** While the assumption is noted, quantile-based normalization is standard practice for aligning distributions from different sources. → Downgraded to Minor.

- **Strength Finder's claimed strengths that were generic:** All five strengths from the Strength Finder are specific and evidence-backed. None are removed.

## Novel Insights

The reviews collectively surface a tension not explicitly discussed in the paper: UGDA uses gradient influence computed on the *policy* to select samples for *reward model* refinement, but the paper never articulates when and why this transfer should hold. If the reward model is a good approximation of human preferences, then the policy's loss landscape is mediated by the reward model's outputs, creating an indirect link — but this connection weakens if the reward model is itself off-distribution (precisely the problem UGDA aims to solve). This circular dependence is a blind spot in the current exposition.

## Suggestions

1. **Fix the data leakage before any resubmission.** Use a held-out portion of the HH *training* set (or a separate validation set) for influence computation. Re-run the HH evaluations and verify that UGDA still outperforms baselines on the clean test set.
2. **Add sensitivity analyses** for selection thresholds (γ, η), projection dimension, and ensemble size k. These are low-cost experiments that would significantly strengthen the paper.
3. **Either provide analysis justifying the policy→reward-model influence transfer, or** compute the gradient influence on the reward model's own parameters instead of the policy's, which would be conceptually cleaner.

## Score and Decision

**Originality:** 7/10 — The uncertainty-gradient combination for reward model data selection is novel.  
**Importance of question:** 8/10 — Off-distribution reward modeling is a recognized problem in RLHF.  
**Claims support:** 4/10 — The main HH results are compromised by data leakage; external benchmarks partially support the claims.  
**Soundness:** 5/10 — The method's pipeline is logically presented, but the evaluation has a structural flaw.  
**Clarity:** 6/10 — The three-stage pipeline is clearly described; some experimental details are missing.  
**Value to community:** 6/10 — The idea of selective interaction-data reuse for reward refinement is valuable, but the current evidence is insufficiently reliable.

The paper introduces a well-motivated method with a novel data selection strategy. However, the data leakage on the HH test set (using test data as validation for influence computation while evaluating on the same test set) undermines the primary quantitative evidence. The external benchmarks provide some support, but the main results in Table 2 cannot be trusted as presented. A revised version that fixes this issue could be a solid contribution.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>