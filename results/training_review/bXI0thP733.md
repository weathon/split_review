Now I have all the information I need to write the consolidated review. Let me compose it.

## Summary

This paper proposes a backdoor defense that uses per-class normalizing flows on self-supervised (SimCLR) feature representations to detect and correct poisoned training data. The defense first trains a self-supervised feature extractor on the potentially poisoned dataset, then learns per-class generative models. By comparing the densities assigned by different class-conditional models, it identifies target classes and individual poisoned samples, then relabels the latter via generative classification before retraining. The paper evaluates on CIFAR-10, ImageNet, and VGGFace2 against six attack types, reporting ASR below 1% in most conditions, including against adaptive attacks (Adap-Patch/Adap-Blend) designed to evade latent-separability defenses.

## Strengths

1. **Novel defense paradigm combining self-supervised features with per-class generative modeling.** The approach of using normalizing flows on self-supervised representations for backdoor detection and correction is genuinely different from existing discriminative defenses (e.g., ABL, DBD, ASD). The paper provides a clear conceptual framework categorizing attacks as non-disruptive vs. disruptive based on their effect in self-supervised feature space (Section 3.2, Figure 1), and shows this taxonomy is predictive of the detection strategy that works.

2. **Strong empirical ASR reduction against adaptive attacks.** Against Adap-Patch and Adap-Blend (Qi et al., 2022) — attacks explicitly designed to evade latent-separability defenses — the method achieves ASR < 2% on CIFAR-10, while competing defenses (ABL, DBD, ASD) often show ASR *higher* than no defense (Section 5.2, Table 1). This is a non-trivial result: adaptive attacks that claim to break the entire family of latent-separability defenses are foiled by the switch from supervised to self-supervised features.

3. **Constructive relabeling mechanism.** Rather than discarding detected poisoned samples, the method reuses them as augmented data by relabeling via generative classification (Section 4.6). This preserves dataset size and avoids the information loss inherent to filtering-only defenses. The strong clean accuracy retention in Table 1 (e.g., 87.41% on CIFAR-10 BadNets vs. no-defense baseline of 89.98%) supports this design choice.

4. **Ablation studies on key design choices.** Table 3 compares SimCLR, CLIP, and supervised feature extractors, confirming that self-supervision is critical (ASR 0.3% vs. 45.3% for BadNets). Table 4 examines robustness across poisoning rates (5%–30%), with honest discussion of the degradation at higher rates.

## Weaknesses

### Fatal
None.

### Major

1. **The feature extractor is trained on the poisoned dataset without direct validation that self-supervised learning is robust to the considered poisoning.** Section 4.3 trains SimCLR on the potentially poisoned dataset $\tilde{\mathcal{D}}$, and the entire subsequent detection pipeline depends on the trustworthiness of these features. The paper provides indirect evidence (the overall method works in Table 1; Table 3 shows SimCLR outperforms supervised features) but never directly validates that SimCLR features learned on poisoned data remain semantically faithful — e.g., via kNN clean-label accuracy on features as a function of poisoning rate. The discussion of CLIP (Section 5.2) acknowledges that clean pre-trained extractors are an option but also notes they can themselves be backdoored, leaving the core issue unresolved. A formal argument or targeted experiment that SimCLR representations preserve semantic structure under the considered attacks would substantially strengthen the paper's foundation.

### Minor

2. **Hyperparameter selection procedure is unspecified for deployment.** The four detection thresholds ($\beta_{\mathrm{ND}}=0.6$, $\beta_{\mathrm{D}}=0.05$, $\lambda=0.75$, $\alpha=0.15$) are set "based on early validation experiments" (Section 5.1), but the paper provides no sensitivity analysis, no guidance on how to set these without clean validation data, and no evidence that the chosen values generalize across datasets and attack types. This is a common limitation in the defense literature, but it is compounded by the paper's claim of operating "without such requirement" (i.e., without clean data) for baselines like ASD.

3. **Incomplete attack coverage on ImageNet and VGGFace2 limits the generality of conclusions.** The paper states it omitted attacks on these datasets because "we were not able to reproduce the performance from their papers" (Section 5.1). The comparative tables for larger datasets therefore cover only a subset of attacks, making it unclear whether the defense's strong CIFAR-10 results transfer to the full attack suite at scale.

4. **Attack-type classification (non-disruptive vs. disruptive) is never evaluated as a separate step.** The same poisoning score $s_y(z)$ is interpreted with opposite semantics for non-disruptive vs. disruptive attacks (Section 4.5): "clean samples score higher than poisoned ones" for non-disruptive, but "poisoned samples will score significantly higher than clean samples" for disruptive. If this classification is wrong, the filtering removes the wrong samples. The accuracy of this meta-classification is never assessed, leaving a gap in the evaluation of the defense's decision pipeline.

5. **Relabeling accuracy vs. ASR discrepancy is not explained.** For example, on CIFAR-10 Adap-Patch, relabeling accuracy is 67.7% (Table 2) while ASR is 0.67% (Table 1). There is a plausible explanation — even incorrectly relabeled samples are not assigned the target class label, so the trigger-target association is never learned — but the paper does not provide this explanation, leaving readers confused about how such low relabeling accuracy coexists with near-perfect ASR reduction.

6. **Scalability concerns for large datasets.** ImageNet (1000 classes) requires training 1000 separate normalizing flows. The paper reports no computational cost (time, memory, or FLOPs) for this training stage, making it difficult to assess whether the defense is practical at scale.

7. **No statistical variance reported.** Tables 1–4 report point estimates of ACC and ASR without standard deviations, confidence intervals, or multiple runs. While single-run evaluation is common in the backdoor defense literature, it makes it impossible to assess whether the small ASR differences between methods (e.g., <1% in some conditions) are significant.

### Trivial

8. **Figure 1 (UMAP) visualizations are qualitative.** The paper's core motivation (Section 3.2) uses 2D UMAP projections to argue that poisoned samples preserve semantic structure in self-supervised features. No quantitative metric (centroid distance, kNN accuracy, intra/inter-class ratio) is provided. This does not undermine the paper's conclusions, which are validated experimentally, but weakens the stated theoretical foundations.

## Nice-to-Haves

- A variant of the defense that uses a clean pre-trained feature extractor (e.g., CLIP, DINO) as the default option, with training on the poisoned dataset reserved for when no pre-trained extractor is available. The paper already discusses this possibility (Section 5.2) but does not explore it as a concrete alternative.
- Sensitivity analysis for the four hyperparameters across a reasonable range, showing whether the method is robust to misspecified thresholds.
- An adaptive attack evaluation where the attacker explicitly optimizes to evade the per-class generative models (e.g., crafting triggers that stay within the target class manifold in SimCLR space).

## Removed Points

These points from the reviews were removed per the consolidation guidelines; they are listed for completeness but should not be weighed in the assessment:

- **Criticism about "first backdoor defense based on generative modelling" being overstated** (removed: per rules on missing related works, I cannot verify the existence of prior generative-model-based defenses).
- **Architecture mismatch claim** (removed: the paper does specify the architecture — ResNet-18 for CIFAR-10/ImageNet, DenseNet-121 for VGGFace2).
- **Typos/formatting nitpicks** (removed: parser artifacts, not author errors).
- **"No defense" ASR values not reported as error bars** (moved here from the harsh critic's stronger framing; the lack of variance is retained as Minor weakness #7 above but framed appropriately for the field's norms).
- **General writing quality complaints** (removed: structural organization critiques are subjective, and formatting issues are parser artifacts).
- **CLIP comparison undermines main pipeline** (removed: the paper itself discusses this trade-off and notes CLIP can also be backdoored; this is an acknowledged design discussion, not a weakness).
- **High poisoning rate limitation** (removed: the paper acknowledges this limitation explicitly in Section 5.2).

## Novel Insights

Beyond the paper's own contributions, a genuinely novel observation that emerges from the reviews is the *asymmetric robustness of self-supervised features under poisoning*. The harsh critic correctly notes the circular dependency risk, yet the strength finder's analysis of Table 1 shows the method works across diverse attacks. This tension suggests an interesting and under-explored property: self-supervised contrastive learning may be resilient to label-perturbation-based poisoning even when the poisons are in the training set, because the contrastive objective is agnostic to labels and the trigger-induced augmentations may not systematically distort positive-pair formation. If validated, this would be a meaningful insight for the community — but the paper does not articulate or test this hypothesis explicitly.

## Suggestions

1. **Directly validate feature extractor robustness.** Add an experiment that trains SimCLR on poisoned data, then evaluates the resulting features on a clean test set: report kNN top-1 accuracy of features, intra/inter-class feature distance ratios, or the percentage of poisoned samples whose nearest neighbors belong to their original (pre-poisoning) class. This would directly address the most serious concern about circular dependency.

2. **Provide a hyperparameter sensitivity analysis.** Vary each of $\beta_{\mathrm{ND}}, \beta_{\mathrm{D}}, \lambda, \alpha$ over a reasonable range (e.g., ±50% of chosen value) and show the impact on ASR/ACC. If a single setting works across attacks without tuning, state this; if not, provide a principled selection method that uses only the poisoned dataset.

3. **Evaluate the attack-type classification accuracy.** Report a confusion matrix showing how often the non-disruptive vs. disruptive classification (which determines the interpretation of $s_y(z)$) is correct, and show what happens to ASR when it is wrong.

4. **Explain the relabeling-vs-ASR discrepancy in the paper.** A short paragraph noting that even incorrectly relabeled samples (e.g., assigned to a non-original class) still do not receive the target-class label, so the trigger-target association is not learned — resolving the apparent tension between Table 1 (low ASR) and Table 2 (moderate relabeling accuracy).

5. **Report computational costs.** Provide wall-clock time and GPU-hours for the two main stages (SimCLR training, normalizing flow training per class × number of classes) to help practitioners evaluate scalability.

## Score and Decision

This paper presents a novel and well-motivated approach to backdoor defense, with strong empirical results — particularly against adaptive attacks that defeat prior defenses. The central design concern (training the feature extractor on the poisoned dataset) is mitigated by the empirical evidence that the overall method works, but the paper would benefit from explicit validation. The evaluation gaps (variance, attack coverage on larger datasets, missing attack-type classification assessment) are addressable and do not invalidate the core contribution. The paper makes a clear, useful contribution to the backdoor defense literature.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>