Now I have a thorough understanding of the paper. Let me compile the final consolidated review.

---

## Summary

This paper proposes UGDA (Uncertainty-Gradient based Data Augmentation), a method to improve reward modeling in RLHF by selectively retraining the reward model on on-policy interaction data. UGDA operates in three stages: (1) training reward LoRA ensembles to quantify uncertainty via reward variance, (2) selecting interaction samples that are both high-uncertainty and high-influence (using gradient-based influence scores from Xia et al., 2024), and (3) relabeling selected samples via GPT-4 (with quantile projection to the proxy reward distribution) and refining the reward ensembles with an MSE loss. Experiments on the HH dataset with Gemma-2B/7B reward models and Gemma-7B policy show improvements over several baselines.

## Strengths

1. **Novel combination of uncertainty and gradient-based selection for reward model refinement.** The core idea — that on-policy interaction samples should be filtered by both reward-ensemble uncertainty (variance) and gradient-based influence on validation subtasks before being used to retrain the reward model — is sensible and addresses a real problem (reward model off-distribution during RLHF). The ablation study (Figure 4) shows that removing either the uncertainty filter (UGDA(UN)) or the gradient filter (UGDA(GR)) degrades performance, providing evidence that both components contribute.

2. **Practical GPT-4 relabeling pipeline with quantile projection.** The paper designs a prompt for GPT-4 to assign 1–5 scores and projects these onto the empirical quantiles of each reward LoRA's output distribution (Equation 13). This allows using an expert (GPT-4) to provide training targets while preserving the scale and distribution of the proxy reward model, avoiding distribution mismatch. Table 1 reports similarity between GPT-4 and human labels, suggesting the approach is feasible.

3. **Robustness to noisy preference data is demonstrated.** Table 3 shows that under 20% label flipping noise, UGDA suffers less performance degradation across most metrics compared to baselines, and Figure 5 shows UGDA still leads in GPT-4 pairwise comparisons. This is a useful practical result not explored in prior reward model refinement works.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claims are supported by the experimental results, and no fundamental methodological flaw invalidates the contribution.

### Minor

1. **Gradient influence computation is underspecified on one critical detail.** The paper adopts the Adam influence framework (Xia et al., 2024) in Section 4.2, referencing "each model checkpoint θ₁,…,θ_N" and "gradients obtained from LoRA," but never explicitly states **which model** these checkpoints come from. The natural reading is that they are reward model LoRA checkpoints (from the Stage 1 training), since the goal is to select data for reward model refining. However, the paper also frames the goal as "identify influential samples for policy optimization" and uses validation subtasks from the HH dataset (helpful/harmless), which are policy-relevant rather than reward-model validation tasks. The connection between influence computed on the reward model trajectory and usefulness for policy-relevant reward model retraining needs clarification. This does not invalidate the method — the formulation in Definition 1 and Equations (10–12) is mathematically well-defined regardless — but the ambiguity makes the paper harder to reproduce and assess.

2. **No sensitivity analysis for key selection thresholds (γ, η).** The thresholds are fixed at γ=0.5 (top 50% by uncertainty) and η=0.5 (top 50% by influence), yielding 25% of interaction data. The paper provides no analysis of how performance varies with these choices. While the ablation (Figure 4) shows that both components are needed, it does not test different threshold values, leaving the robustness of the method to these hyperparameter choices unexamined.

3. **The reward relabeling pipeline has unvalidated design choices.** (a) The quantile projection (Equation 13) maps GPT-4's 1–5 ordinal scores onto quintiles of the PPO reward distribution — a sensible heuristic, but the paper provides no analysis of whether this mapping actually produces better reward targets than alternatives (e.g., direct score regression, no projection, or using raw ensemble scores). (b) The additive noise ε∼N(0,0.01) is introduced without explanation of its purpose. (c) While Table 1 reports "high degree of similarity" between GPT-4 and human labels, no quantitative metrics (e.g., Cohen's κ, accuracy per score level, sample size) are given in the text. These design choices are not unreasonable, but the paper would benefit from validating that they improve reward model accuracy compared to simpler alternatives.

4. **Interaction data collection details are underspecified for reproducibility.** The paper states that interaction samples are collected in D_inter during policy optimization, but does not specify: how many PPO steps are run before collecting, whether data is collected once or periodically throughout training, or the total size of D_inter (only that 25% is selected from it). A simple statement of dataset sizes and collection frequency is needed.

5. **Computational cost is not discussed.** The method requires: (a) training k reward LoRAs (k=3), (b) running PPO with reward ensembles, (c) computing gradient influence with random projection on LoRA checkpoints, (d) calling GPT-4 for relabeling, and (e) retraining the reward model. This is substantially more expensive than standard PPO. A discussion of overhead relative to the baselines would help practitioners assess the practical trade-off.

6. **Single noise level tested for robustness.** The robustness experiment (RQ3) uses only one noise condition (20% label flip). Testing multiple noise levels or types would strengthen the claim of robustness.

7. **Reasoning underperformance on RewardBench is not analyzed.** Figure 6 shows UGDA underperforms on the "Reasoning" category of RewardBench. The paper speculates that "there are only few samples about the reasoning task in the filtered interaction data" but provides no analysis of the selected data's reasoning content. This is a minor gap given the overall positive results.

### Trivial

- In Equation (2), "strenth" should be "strength."
- The phrase "data augmentation" in the title and throughout the paper is somewhat misleading — the method selects and relabels existing data rather than generating new synthetic data. "Data selection and relabeling" or "refining" would be more accurate, though this does not affect technical correctness.

## Nice-to-Haves

- Sensitivity analysis for γ and η (e.g., 0.3, 0.5, 0.7) would increase confidence in the method's robustness.
- Validation of the quantile projection by comparing reward model accuracy with vs. without the projection step.
- Analysis of what kind of data the uncertainty and gradient criteria select — a qualitative example or distribution analysis would strengthen motivation.
- Reporting error bars or variance across runs for the ablation study (Figure 4).
- Testing multiple noise levels (e.g., 10%, 30%) for the robustness experiment.

## Removed Points

These points were flagged by reviewers but are removed after verification:

- **"Baseline comparison is misleading / deceptive"** — The paper states that "0% represents the baselines without data augmentation" in discussing Table 2, meaning unmodified PPO/LCB/UWO results ARE reported alongside the versions with 25% random retraining. The comparison is therefore against both unmodified and modified baselines. The reviewer's claim that the comparison is "only against modified baselines" is factually incorrect based on the paper's own text. The claim is removed.
- **"RLR is not defined in the paper"** — RLR is explicitly defined as "Reward LoRAs Retraining" in Section 5.1 (line 216). The reviewer missed this. Removed.
- **"The paper calls this 'data augmentation' but no new data is generated"** — This is a semantic quibble. Relabeling existing data to create new training targets is a recognized form of data augmentation.
- **"Llama2-13B evaluator may have distributional biases"** — Using a larger reward model as an automated evaluator is a standard practice in RLHF evaluation (Gao et al., 2023), and the paper also uses GPT-4 evaluations and standard benchmarks. This is not a valid criticism of this paper.
- **"The gradient influence is likely misapplied / unfalsifiable"** — The reviewer overstates this concern. The methodology follows the standard Adam influence framework (Xia et al., 2024) and is mathematically well-defined and reproducible once the model identity is clarified. The ambiguity is real but minor (see Weakness #1).
- **"Only one noise condition tested"** — This is a minor/nice-to-have request, not a structural flaw. The paper shows a clear result under the tested condition.

## Novel Insights

The reviews do not surface any insight beyond the paper's own contributions. The observation that uncertainty (reward ensemble variance) may be insufficient alone for data selection — because not all high-uncertainty samples are influential for the reward model's policy-relevant performance — is the paper's own contribution, confirmed by its ablation study.

## Suggestions

1. **Clarify which model's checkpoints and loss are used in the gradient influence computation (Section 4.2).** If these are reward model LoRA checkpoints, state this explicitly and explain why influence on HH validation subtasks is the right objective for selecting data to refine the reward model.

2. **Add a validation experiment for the quantile projection.** Show that the projected rewards produce better reward model accuracy on a held-out set compared to alternatives (e.g., no projection, direct score regression, raw ensemble scores).

3. **Report the size of D_inter and D'_train in absolute numbers** alongside the percentage (25%).

4. **Add a brief computational cost comparison** (e.g., total GPU-hours for PPO vs. UGDA vs. baselines with retraining) so practitioners can assess the practical trade-off.

5. **Include sensitivity analysis for γ and η** or at minimum acknowledge these as hyperparameters that may need tuning.

## Score and Decision

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>