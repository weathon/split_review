I now have a complete understanding of the paper and all reviewer inputs. Let me construct the final consolidated review.

## Summary

This paper proposes a framework for learning "failure-aware plans" from few demonstrations, integrating: (1) an LSTM-based Action Model for segmenting trajectories into action fragments, (2) Dynamic Movement Primitives (DMPs) for action controllers, and (3) a meta-learned (MAML) transformer-based Detect Model that checks whether each action execution succeeded or failed. The Detect Model is pre-trained on random labeled trajectories using episode-based binary classification tasks (distinguishing action-stage pairs), then fine-tuned on few user demonstrations where the positive class is the end-stage of a successful action. Experiments on a Fetch robot in Gazebo (pick-and-place) show 88.2% detection accuracy with only 5 demonstrations, outperforming a rule-based baseline.

## Strengths

1. **Addresses a practically important gap in plan execution.** The paper correctly identifies that most LfD work on task planning neglects online failure detection during execution. Formalizing "failure-aware plans" and building an end-to-end framework that integrates segmentation, control, and detection is a useful systems contribution.

2. **Clear sample-efficiency evidence against the implemented baseline.** In Table 1, the proposed method with 5 demonstrations achieves 88.2% accuracy (SeR), substantially higher than the adapted Konidaris et al. baseline at 5 demonstrations (79.4%), and competitive with the baseline at 100 demonstrations (89.3%). This demonstrates that the overall approach (pre-training + meta-learning + fine-tuning) is data-efficient relative to this specific baseline.

3. **Ablation confirms fine-tuning is essential.** The "Ours (no-ft)" variant achieves only 17.6% accuracy and zero successful executions, cleanly showing that the pre-trained model alone is insufficient and task-specific fine-tuning is critical.

4. **Convergence analysis and reusable detectors.** Figure 3 shows the Detect Model converges in ~10–15 gradient steps. Table 3 shows detectors trained on a 4-step task transfer to an 8-step variant with 88.0% accuracy, supporting reusability.

5. **Honest discussion of limitations.** The paper acknowledges that actions with fewer state features (move, transport) yield lower accuracy, and that more data does not uniformly improve all detectors.

## Weaknesses

### Major

1. **No ablation isolating meta-learning from standard pre-training.** This is the most significant weakness. The paper claims meta-learning (MAML) is the reason for sample-efficient fine-tuning, but the experimental design does not isolate this. There is no comparison against:
   - Training the same Detect Model from scratch on just 5 demonstrations
   - Standard supervised pre-training on D_M (e.g., multi-task stage classification) followed by fine-tuning
   
   The only comparison is against the rule-based baseline (which is a different method entirely) and the "Ours (no-ft)" ablation (which shows pre-training alone is insufficient — but not that meta-learning is better than alternative pre-training). The reported gains could simply reflect the benefit of having a large pre-training dataset, not the specific meta-learning procedure. This gap undermines the paper's central methodological claim.

2. **Baseline comparison is insufficient and poorly described.** The baseline from Konidaris et al. (2018) is described as using "a similar network as our method to learn action failure detectors by the descriptions of the learned plan," with further details deferred to supplementary material. The reader cannot determine what "rule-based" component remains, how the baseline is trained, or whether the comparison is fair. Furthermore, there is no baseline that controls for pre-training: a simpler baseline — the same network trained from scratch on 5 demonstrations without any pre-training — would directly test whether the pre-training (regardless of method) provides an advantage. Without this, the outperformance claim conflates pre-training data volume with methodological superiority.

3. **Detection task formulation has an unexamined gap.** The Detect Model is fine-tuned with positive = end-stage of a successful demonstration, negative = other stages (start, middle) of the same or different actions. This means the model learns to recognize the successful end-stage, not actual failure states. The assumption — never validated — is that failure states (e.g., cup slipping during transport) will not resemble the successful end-stage and thus will be correctly classified as failures. This approach is defensible (it is a form of postcondition verification / one-class classification) and the test-time evaluation does involve real failures from physics-engine randomness, which provides some support. However, the paper never analyzes whether failure states actually distribute outside the successful end-stage manifold, nor what types of failures this approach might miss. This gap between the operationalized task (stage classification) and the stated goal (failure detection) should be acknowledged and, ideally, validated.

### Minor

4. **Evaluation limited to one task (pick-and-place) in simulation.** Only the Fetch robot in Gazebo is tested. The "generalization" experiment reuses the same four action types (move, pick, transport, place) in longer sequences — it does not test transfer to new action types, new task structures (e.g., assembly, pouring), or real hardware. While acceptable for a proof-of-concept, this narrowness limits the support for claims of generality.

5. **Confusing metric definitions and missing detection-specific metrics.** The paper defines TN as "a positive evaluation (indicating falsehood)" (Section 4.2), which is contradictory terminology. More importantly, no precision, recall, or F1 scores are reported for the failure detection task, and the base rate of failures is not reported. Without these, it is difficult to assess whether the reported accuracy is meaningful (e.g., a model that almost always predicts "success" could achieve high accuracy if failures are rare). The task-level metrics (#ES, #EF) are useful but incomplete for evaluating detection performance.

6. **Action Model segmentation accuracy is not evaluated.** The LSTM-based Action Model is critical for producing the fine-tuning dataset D_N from user demonstrations. If segmentation is inaccurate, D_N is noisy and detection performance suffers. The paper provides no evaluation of segmentation accuracy, leaving a significant unknown in the pipeline's error propagation.

7. **Some terminology and claims are vague.** Phrases like "discriminatively captures the state features" and "second-order differentiation" (a standard property of MAML) are used without sufficient explanation of their role. The claim that meta-learning "enhances the sensitivity of the loss function towards the newly constructed tasks" is not justified with analysis.

### Trivial

8. Metric definitions in Section 4.2 use non-standard phrasing (e.g., "a positive evaluation (indicating falsehood)") that should be clarified for standard ML audiences.

9. Several architectural details (transformer encoder specifications, LSTM dimensions, meta-learning hyperparameters) are deferred to the supplementary material, making the paper hard to assess in isolation.

## Nice-to-Haves

- Report precision, recall, and F1 for failure detection alongside accuracy, along with base failure rates.
- Evaluate the Action Model's segmentation accuracy to quantify error propagation.
- Test on at least one additional task domain or on real hardware to strengthen generality claims.
- Include a discussion of the types of failures the current formulation might miss (e.g., failures whose states resemble successful middle stages).

## Removed Points

The following criticisms from the original reviews were removed or downgraded per the filtering guidelines:

- **"Pre-training data is expensive to obtain"** — The paper operates entirely in simulation, where random trajectory data with automated labeling is cheap to generate. The "few demonstrations" claim refers to user demonstrations for new tasks, not the pre-training corpus, which is standard for meta-learning approaches. This criticism evaluates the paper against real-world deployment standards not claimed by the simulation-based study.

- **"Missing related work on plan execution monitoring"** — Per policy, I cannot verify the existence of unmentioned work. The paper's related work section (Section 2) does cite literature on action execution monitoring (Pettersson, 2005; Goel et al., 2000; Stavrou et al., 2016; Park et al., 2018; Vallachira et al., 2019; Inceoglu et al., 2021, 2023) and positions its contribution as addressing plan-level (not standalone action) failure detection. This framing is a defensible scope choice.

- **"Action failure detection is mis-specified / not failure detection"** — This criticism overstates the issue. The paper's approach (verifying whether the execution state matches the successful end-stage) is a well-established paradigm for detecting anomalies — it is postcondition verification, not "stage-localization." The test-time evaluation does involve real execution failures from physics randomness, providing direct evidence that the approach works for its stated purpose. The concern is real but belongs at the Minor level (as captured in Weakness 3 above), not as a structural invalidation of the contribution.

- **Weaknesses about formatting, typos, missing appendix content** — These are parser artifacts from PDF extraction, not author errors.

## Novel Insights

The most substantive observation from the review process is that the paper's evaluation design conflates two distinct claims — (a) that pre-training on diverse trajectory data helps, and (b) that meta-learning specifically helps more than alternative pre-training strategies. The existing experiments convincingly support (a) via the comparison with the no-fine-tuning baseline, but provide no evidence for (b). This conflation is common in applied meta-learning papers and should be addressed by the authors in future work.

## Suggestions

1. **Isolate the meta-learning contribution.** Add ablations comparing MAML pre-training against: (i) training from scratch on 5 demos, (ii) standard supervised pre-training on D_M followed by fine-tuning, and (iii) the current no-fine-tuning baseline. Without these, the core methodological claim is unsupported.

2. **Clarify and standardize the metrics.** Fix the contradictory definitions of TP/TN/FP/FN, report precision, recall, and F1, and report base failure rates so readers can contextualize accuracy.

3. **Provide a from-scratch baseline.** Train the same network architecture on just the 5 user demonstrations without any pre-training, to quantify the benefit of the pre-training data itself (separate from meta-learning).

4. **Evaluate segmentation accuracy.** Quantify the Action Model's performance to assess error propagation through the pipeline.

5. **Expand evaluation scope.** Adding even one more task type (e.g., a simple assembly or pouring task) or a real-robot experiment would substantially strengthen claims of generality.

## Score and Decision

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>