Now I have all the information needed. Let me produce the final consolidated review.

---

## Summary

This paper proposes DRMGuard, the first backdoor defense specifically designed for deep regression models (DRMs) in the image domain. It identifies a key feature-space observation — that in backdoored DRMs, the angles between feature vectors and weight vectors become highly concentrated (Ratio of Angle Variance ≪ 0.1) — and formulates a reverse-engineering optimization that jointly minimizes output variance and enforces a feature-space regularization term derived from this observation. The method is evaluated on two regression tasks (gaze estimation, head pose estimation) across four datasets under four backdoor attacks, and compared against four adapted classifier defenses.

## Strengths

1. **First defense tailored to the unique output/feature-space characteristics of DRMs in the image domain.** The paper correctly identifies why existing classifier defenses fail for DRMs: (a) the continuous output space makes enumeration of target vectors infeasible, and (b) backdoor behavior in DRMs involves all feature neurons rather than just a few. DRMGuard's reverse-engineering formulation (Eq. 7) leverages the novel RAV observation directly. (Sections 1, 3.3, 3.4)

2. **Strong empirical identification performance.** DRMGuard achieves 100% ROC-AUC across all four backdoor attacks (BadNets, IA, WaNet, Clean Label) on MPIIFaceGaze, dramatically outperforming adapted classifier defenses Neural Cleanse (average 0.379) and FeatureRE (average 0.599) (Table 3). This directly supports the claim that existing defenses are ineffective for DRMs.

3. **Effective backdoor mitigation that surpasses existing methods.** After mitigation, DRMGuard achieves the lowest defense attack error (DAE=3.29) and the highest attack error (AE=15.36), indicating the backdoor behavior is effectively unlearned (Table 5). The method outperforms Fine-tuning, Fine-pruning, and ANP on both metrics.

4. **Comprehensive evaluation scope.** The method is tested on gaze estimation (MPIIFaceGaze, ColumbiaGaze) and head pose estimation (Biwi Kinect, Pandora) under both input-independent (BadNets, Clean Label) and input-aware (IA, WaNet) attacks, with identification accuracy of 70–100% (Table 2). Multi-backdoor models are also considered (Section 4.2).

5. **Ablation studies validate the necessity of each component.** Removing the feature-space regularization term (FSRT) or the momentum reverse trigger (MTR) drops identification accuracy from 95% to 50% (all benign models misclassified as backdoored), confirming both components are essential (Table 6).

6. **Adaptive attack analysis demonstrates fundamental nature of the observation.** An attack designed to force RAV to 1 results in significantly higher attack error (AE=5.71 vs 1.51 for WaNet) while still being detected at 95% accuracy (Table 7), indicating the feature-space characteristic is structurally inherent to successful backdoors in DRMs.

## Weaknesses

### Fatal
None.

### Major

1. **Missing clean test performance after backdoor mitigation.** The mitigation results (Tables 4 and 5) report only AE (distance to target vector) and DAE (distance to correct annotations on the *poisoned* test set). These show that after mitigation, the model no longer outputs the target vector on poisoned inputs. However, the paper never reports whether performance on *clean* (non-poisoned) inputs has degraded. If fine-tuning with reversed triggers reduces accuracy on clean inputs — e.g., because the reversed triggers introduce distribution shift — then the defense may not be practically useful. Reporting clean test error (e.g., gaze angle error or head pose MAE on a clean test set) for both the original and mitigated models is a standard expectation for backdoor mitigation evaluation, and its absence is a meaningful gap that weakens the practical utility claim.

### Minor

2. **Insufficient detail on baseline adaptations.** The paper adapts Neural Cleanse (NC) and FeatureRE from classifiers to regression by "taking the potential target vector y_t as the optimization variable" (line 220). This is a single-sentence description. For NC in particular, the original method relies on class-specific anomaly detection (MAD outlier detection) to flag suspicious target classes — a mechanism that has no natural counterpart in continuous regression output. The paper does not describe how "outlier" target vectors were detected in the adapted version, or what hyperparameters were used. Without this documentation, the reader cannot rule out that the reported ROC-AUC scores (NC: 0.270–0.940, FeatureRE: 0.545–0.730) underrepresent what these methods could achieve with a more careful, principled adaptation. This directly affects the central comparative claim.

3. **Momentum reverse trigger (MTR) is insufficiently specified.** The ablation study shows MTR is critical (without it, all benign models are misclassified as backdoored). Yet the paper provides only a one-sentence description: MTR "assigns different weights to different regions to balance the attention of the DRM on the image" (line 189). The key mechanism (how attention weights are computed, how they interact with the generative model G_θ, and how they prevent the trivial solution) is not formalized. Given that MTR is shown to be essential, this lack of specification undermines reproducibility.

4. **Hyperparameter sensitivity with limited guidance.** The defense settings differ substantially between tasks (λ₁=20, λ₂=800 for gaze; λ₁=10, λ₂=100 for head pose), and the ablation shows identification accuracy drops to 75% at λ₂=600 vs 100% at λ₂=1000. The paper attributes the difference to "given task difference" without principled guidance for how a practitioner should select these values on a new task. This suggests the method may require nontrivial per-task tuning.

5. **Performance variation across datasets not discussed.** Identification accuracy ranges from 70% (ColumbiaGaze) to 100% (Biwi Kinect), but the paper offers no analysis of why certain datasets yield substantially worse performance. Understanding these failure modes would help assess the method's reliability and scope.

6. **Adaptive attack evaluation limited to one λ_adp value.** The adaptive attack (Section 4.5) uses a single value λ_adp=0.02. While the results show the attack degrades AE and cannot evade detection, exploring a range of λ_adp values would provide stronger evidence that the feature-space observation is genuinely fundamental rather than merely fragile.

### Trivial

7. **Architecture of G_θ not specified.** The generative model G_θ used to model the trigger function is mentioned (line 90) but its architecture (e.g., U-Net, small CNN) and training hyperparameters are not provided.

## Nice-to-Haves

- A scatter plot or histogram showing the distribution of RAV values for benign vs. backdoored models across all attacks/datasets would crystallize the paper's core observational contribution. (Note: RAV is defined as σ²(poisoned_angles)/σ²(benign_angles), so the values in Table 1 already encode the comparison; a direct visualization would further strengthen presentation.)
- An intermediate λ₂ sweep (e.g., 700, 900) in the ablation to better characterize the sensitivity landscape.
- A brief rule-of-thumb for selecting λ₂ on new tasks (e.g., based on output variance magnitude or RAV on benign data).

## Removed Points

These points are flagged to be removed — treat them with caution:

- **"Missing RAV for benign models" (Harsh Critic #1):** This criticism misunderstands the metric. RAV is defined as a ratio whose denominator *is* the benign angle variance (Eq. 7). The RAV values in Table 1 (e.g., 0.0433) directly quantify the contrast between backdoored and benign: the poisoned-angle variance is only 4.33% of the benign-angle variance. Reporting separate "RAV for benign models" is not a meaningful request — RAV inherently captures the comparison. The identification results (95% accuracy, FP=1/10) further confirm that benign models do not exhibit the RAV ≪ 0.1 pattern. This is a factual misunderstanding by the reviewer.

- **"First defense claim needs clarification about image domain" (Harsh Critic Other Observation):** The paper already acknowledges Li et al. (2021) on line 52 and clearly states the distinction ("low-dimensional vectors" vs "high-dimensional image domain"). The paper's handling of this is adequate.

## Novel Insights

The most insightful observation across the reviews is the tension between the RAV-based detection and the adaptive attack analysis: the adaptive attack that forces RAV ≈ 1 simultaneously degrades the attack's own effectiveness (AE rises from 1.51 to 5.71). This suggests a deeper structural trade-off — that concentrated feature-space angles (RAV ≪ 0.1) are not merely a contingent artifact of existing attacks but may be a necessary condition for achieving a low-error backdoor in DRMs. If this trade-off is general, it could ground a provably robust defense: any backdoor strong enough to be useful (low AE) must necessarily be detectable via RAV. The paper's single λ_adp data point hints at this but does not explore it rigorously; probing this trade-off across multiple λ_adp and attack configurations would substantially strengthen the theoretical contribution.

## Suggestions

1. **Report clean test performance after mitigation** as an additional row in Tables 4/5 (e.g., "Clean MAE" or "Clean Error"). This is the single most impactful addition.
2. **Expand the baseline adaptation documentation.** Describe how NC's outlier detection was handled for the continuous output space, and list any hyperparameters.
3. **Formalize the MTR mechanism.** Provide the attention-weight computation, the momentum update rule, and how the weighted perturbation integrates with the optimization objective.
4. **Discuss the ColumbiaGaze (70%) and Pandora (85%) failure modes.** Analyze whether lower accuracy stems from dataset characteristics (e.g., smaller size, less diversity) or task-specific factors.
5. **Explore a range of λ_adp values** in the adaptive attack to strengthen the claim that the feature-space observation is fundamental.

## Score and Decision

The paper addresses a genuine, underexplored problem, proposes a novel and well-motivated approach, and demonstrates strong empirical results across multiple tasks, datasets, and attacks. The main weaknesses are (a) the absence of clean test performance after mitigation, which is a standard expectation, and (b) the insufficient detail on baseline adaptations and the MTR component — both addressable in revision. No weakness threatens the core claims: the RAV-based identification is clearly effective, and the ablation studies convincingly attribute this to the proposed components. With the suggested additions, this would be a solid contribution to the backdoor defense literature.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>