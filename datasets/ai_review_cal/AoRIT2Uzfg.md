- Decision: Reject
- Avg Score: 4.67
- Scores: 8, 3, 3
Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper proposes DRMGuard, the first dedicated backdoor defense for deep regression models (DRMs) in the image domain. The key insight is a feature-space observation — the ratio of angle variance (RAV) is consistently ≪0.1 for backdoored DRMs but not for benign ones — which the paper uses to formulate a reverse-engineering optimization with a feature-space regularization term plus a momentum reverse trigger (MTR). Experiments on two regression tasks (gaze estimation, head pose estimation) and four datasets show that DRMGuard outperforms adapted classification defenses (Neural Cleanse, FeatureRE) by a large margin.

## Strengths

- **First defense tailored to DRMs in the image domain.** The paper identifies and addresses a genuine gap: existing backdoor defenses are designed for classification models and fail for regression models due to continuous outputs and all-neuron backdoor behavior. This motivation is well-articulated (Section 1, Section 3.3).

- **Novel feature-space observation backed by theoretical analysis.** The paper derives RNV and RAV metrics from the regression output equation (Eq. 3–4) and demonstrates empirically (Table 1, Fig. 2) that RAV ≪ 0.1 is a consistent property of backdoored DRMs across four different attacks and two datasets. This observation is used to design the feature-space regularization term in the optimization (Eq. 5), which is the core methodological contribution.

- **Strong empirical results across diverse settings.** DRMGuard achieves 95–100% identification accuracy on MPIIFaceGaze and Biwi Kinect (Tables I–II), and ROC-AUC scores of 1.000 across all four attacks (Table III), substantially outperforming adapted baselines (Neural Cleanse max 0.940, FeatureRE max 0.730).

- **Ablation studies validate both design components.** Removing either the feature-space regularization term (FSRT) or the momentum reverse trigger (MTR) causes accuracy to drop to 50% (all models classified as backdoored) — Table VI. This provides clear evidence that both components are necessary.

- **Addresses both identification and mitigation.** The paper covers the full pipeline: detecting backdoored models and then fine-tuning to remove the backdoor behavior, demonstrating improvement in attack error (AE) and defending attack error (DAE) across multiple attacks (Table IV).

## Weaknesses

### Fatal
None.

### Major

1. **Statistical rigor is insufficient.** The evaluation uses only 10 backdoored + 10 benign models per condition. ROC-AUC scores of 1.000 are reported without confidence intervals, error bars, or any variance estimate. With only 20 models, a single misclassification changes AUC noticeably, and the reported perfect separation may not generalize. The threshold ε=0.03 and hyperparameters (λ₁, λ₂) appear tuned to this exact 20-model test bed — the ablation shows accuracy varying from 75% to 100% with λ₂ (Table VI), suggesting sensitivity. The paper should report bootstrap confidence intervals on AUC, show distribution plots of the identification metric (1/N Σ‖x′ᵢ−xᵢ‖₁) for benign vs. backdoored models, and ideally evaluate on a larger model population or use cross-validation.

2. **The adaptive attack evaluation does not demonstrate the claimed robustness.** The adaptive attack intentionally forces RAV close to 1, but its attack error (AE=5.71) is substantially higher than standard WaNet (AE=1.51) — i.e., the attack is self-limiting and compromises its own effectiveness. The paper's conclusion ("the adaptive attack cannot reduce the identification accuracy") is technically true but misleading without the caveat that the attack is significantly weaker. A meaningful adaptive attack would need to maintain low AE (comparable to standard WaNet) while bypassing the feature-space constraint. Until such an attack is demonstrated or argued impossible on fundamental grounds, the robustness claim is overstated. The paper's argument that this "proves that our feature-space observation is the key characteristic leading to the backdoor behavior" is a reasonable scientific interpretation, but it does not substitute for a stronger adaptive adversary.

3. **Adaptation of baselines (NC, FeatureRE) is under-described, raising fairness concerns.** The paper states these are generalized "by taking the potential target vector y_t as the optimization variable" (Section IV-A). For Neural Cleanse, the original method iterates over discrete class labels and uses MAD-based outlier detection — it is not obvious how either the candidate enumeration or the anomaly detection statistic is adapted to the continuous regression output space. The paper does not specify how many candidate target vectors are tried, how they are initialized, or how the detection rule is modified. If the adaptation is suboptimal, the comparison may be unfair. The authors should provide pseudocode or an algorithm box for the adapted baselines and report whether the optimization converged for each baseline.

4. **Architecture generalization is claimed but not tested.** The Discussion (Section V) states DRMGuard "can be generalized to different architectures," but the experiments use only ResNet18 for the feature extractor F (plus a dense layer for H). No architecture ablation is provided. This claim should either be supported with experiments (e.g., ResNet34, VGG16-based regressors) or removed.

### Minor

1. **Multiple-backdoor claim is unsubstantiated.** The paper states in a single sentence (Section IV-B) that "the results show that our method is effective on identifying DRMs with multiple backdoors" without any quantitative results, table, or figure. This claim should either be supported with experimental data or removed.

2. **Momentum reverse trigger mechanism is not fully described in the main text.** The paper states that MTR assigns "different weights to different regions" based on an attention map generated from gradients, but the actual mechanism (how the attention map is computed, how weights modulate the optimization) is only present in commented-out LaTeX, not in the visible text. The ablation (Table VI) shows MTR is critical, making the lack of description a reproducibility concern. (The details may appear in the appendix, but the main text should be self-contained on this point.)

3. **Mitigation evaluation omits clean performance.** DAE is reported only on poisoned test inputs (Table IV). The paper does not report whether mitigation degrades the model's accuracy on clean inputs — a standard requirement in backdoor defense evaluation. If clean accuracy drops significantly, the mitigation may not be practical.

4. **Limited task diversity.** The evaluation covers only two regression tasks (gaze estimation, head pose estimation). While these are reasonable choices, the paper claims broad applicability to "deep regression models in the image domain" without testing on other regression tasks (e.g., age estimation, facial landmark detection, object counting).

### Trivial
None.

## Nice-to-Haves

- Show distribution plots (e.g., violin plots or histograms) of the identification metric 1/N Σ‖x′ᵢ−xᵢ‖₁ for benign vs. backdoored models, rather than only reporting accuracy and AUC.
- Report the computational cost of reverse engineering (time per model, GPU hours) for practical deployment considerations.
- Test with additional trigger sizes/shapes and random seeds to validate the breadth of the RAV observation.
- Report DAE on clean test inputs to verify that mitigation does not harm benign performance.

## Removed Points

These points from the reviewers were considered but removed with justification:

- **Harsh Critic: "The statement about WaNet being the default setting is ambiguous"** — The paper's sentence "We consider gaze estimation task with MPIIFaceGaze dataset and the state-of-the-art input-aware attack WaNet" appears in the Defense Settings paragraph and, in context, clearly indicates the default setting for ablation studies. This is a clarity nitpick with minimal impact.

- **Harsh Critic: "The paper should report identification accuracy for all methods at a comparable false-positive rate"** — The paper compares methods via ROC-AUC, which is the standard metric for threshold-free comparison across methods that produce different score distributions. Identification accuracy at a fixed threshold is reported for DRMGuard but is not a natural metric for the baselines. This criticism misunderstands the comparison methodology.

- **Harsh Critic: "The paper should discuss whether the difference in mitigation results is significant"** — Subsumed by the main statistical-rigor weakness (Major #1). The lack of variance reporting is a general issue, not specific to this table.

- **Strength Finder: "Robustness to an adaptive attack"** (uncritically listed as a strength) — The adaptive attack is demonstrably weaker (higher AE), which compromises the robustness claim. As a verified weakness exists (Major #2), this strength is dropped per the rule that a verified weakness overrides a conflicting strength.

- **Strength Finder: Generic or sycophantic phrasing** — Phrases such as "superior empirical performance" and "significantly outperforms all defenses" are the paper's own claims. The strength is retained in substance (strong results), but without the uncritical superlative framing.

## Novel Insights

None beyond the paper's own contributions. The two reviewer inputs raised valid concerns about evaluation rigor and overclaiming, but no genuinely novel observation about the paper emerged that the authors themselves had not already touched on (e.g., the limitations of the adaptive attack, the small-sample concern, the need for better baseline documentation).

## Suggestions

1. **Add statistical rigor.** Bootstrap the 20-model evaluation to produce confidence intervals on AUC and accuracy. Show the distribution of the identification metric as a figure. Consider evaluating on a larger pool of models (e.g., 50 per condition) or using cross-validation.

2. **Strengthen the adaptive attack.** Design an adversary that maintains low AE (comparable to WaNet's 1.51) while raising RAV. If this is provably impossible (i.e., any effective backdoor in a DRM necessarily produces low RAV), make that theoretical argument explicit.

3. **Document baseline adaptations.** Provide pseudocode or an algorithm box showing exactly how Neural Cleanse and FeatureRE are adapted to regression, including how candidate target vectors are selected, how many are tried, and how the anomaly detection rule is modified.

4. **Support or remove the multiple-backdoor claim.** Add a table with quantitative results or explicitly mark it as future work.

5. **Report clean performance after mitigation.** Add a column showing the model's regression error on clean test inputs after mitigation.

6. **Remove or support the architecture generalization claim.** Either show results with at least one alternative architecture, or delete the claim from the Discussion.
