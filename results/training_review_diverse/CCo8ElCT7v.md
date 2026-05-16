Now I have a thorough understanding of the paper and can verify each reviewer claim against the actual content. Let me compose the final consolidated review.

## Summary

This paper presents an empirical comparison of Vision Transformers (ViT B32) against five CNN architectures (ResNet50, VGG16, InceptionV3, MobileNetV2, EfficientNetB0) for face identification and verification tasks. The study uses five datasets (VGG Face 2, LFW, SCface, ROF, UPM-GTI-Face) designed to probe robustness to distance degradation and real-world occlusions. The paper reports that ViT achieves the highest accuracy on VGG Face 2, is more robust to distance variation (SCface, UPM-GTI-Face) and occlusion (ROF), and has competitive inference speed.

## Strengths

- **ViT's robustness to distance degradation is demonstrated with concrete evidence.** On the SCface dataset, ViT maintains significantly higher AUC at long and medium distances compared to all five CNNs (Figure 4), while at close distance the gap narrows. On UPM-GTI-Face (Figure 6a, unmasked), ViT sustains AUC above random at 30m (0.63) while CNNs fluctuate around 0.5. These findings probe a dimension (distance) that prior generic ViT-vs-CNN studies did not measure, and the evidence is specific and replicable from the paper's figures.

- **ViT's occlusion resilience using real-world occlusions is clearly shown.** On the ROF dataset (Figure 5), ViT consistently achieves higher AUC and lower EER than every CNN across mask, sunglasses, and combined occlusion scenarios. This is a task-relevant architectural insight — the global self-attention mechanism provides a concrete advantage over local-feature CNNs when portions of the face are obscured — and is supported by visual evidence from the ROC curves.

- **The dataset selection is well-motivated for the task.** Beyond standard LFW, the inclusion of SCface (surveillance distance), ROF (real occlusions from masks/sunglasses), and UPM-GTI-Face (joint distance and masks) targets specific failure modes that matter in practical face recognition, making the comparison more informative than a generic image classification benchmark.

- **Reproducibility infrastructure is provided.** The implementation is publicly available (stated in Section 3), and training details including fixed seeds, hardware configuration, and hyperparameters are documented.

## Weaknesses

### Fatal
None.

### Major

- **Fixed hyperparameters without sensitivity analysis confound the core accuracy claims.** All six models are trained with identical settings (image size 224, batch 256, 25 epochs, Adam, LR 0.0001). The paper acknowledges this limitation (Section 3) but does not mitigate it — no learning rate sweeps, no architecture-appropriate optimizer comparisons (CNNs often prefer SGD with momentum; ViTs benefit from AdamW/cosine schedules), and no validation that all models converged properly. The central claim that "ViTs outperform CNNs in terms of accuracy" rests on an experimental design that cannot cleanly separate architecture effects from hyperparameter effects. While this weakness primarily affects the accuracy comparisons, the robustness findings (distance, occlusion) are somewhat less sensitive to this issue because they involve relative behavior under challenging conditions rather than raw accuracy maximization.

### Minor

- **Memory footprint advantage is asserted without empirical measurement.** The abstract and conclusion claim ViTs have a "smaller memory footprint" than CNNs, and Section 2.1 provides a theoretical argument about activation maps vs. tokens. But no actual memory measurements (peak GPU memory, model size on disk) are reported anywhere. For a claimed advantage listed as a key finding, this omission weakens credibility.

- **Counter-evidence is dismissed unscientifically.** On UPM-GTI-Face masked, VGG outperforms ViT by +4% AUC. The paper calls this "an isolated case that seems to be a non-reproducible anomaly" (Section 3.4). Calling a result obtained from the same experimental protocol as all other results a "non-reproducible anomaly" without attempting replication is not valid scientific reasoning. The appropriate response would be a dispassionate discussion of the conditions under which ViT's advantage diminishes — which the paper partially does ("small dataset, very small and occluded images due to masks") but undercuts with the "anomaly" framing. This damages the paper's objectivity.

- **No uncertainty quantification for any result.** All comparisons are based on single-run results with no confidence intervals, standard deviations, or bootstrapped error bands reported. Given that accuracy and AUC can vary across random seeds and data splits, the absence of variance measures makes it impossible to assess whether reported differences (e.g., ViT's +4% on various metrics) are statistically meaningful.

- **Ambiguous and potentially erroneous writing about training/validation accuracy (Section 3.3).** The text states "ViT results on the validation set were still superior to those of the training set by a large margin. Specifically, ViT's accuracy rose from 98.86% to 99.81%." It is unclear whether the 98.86% refers to training accuracy (making validation > training, which is unusual and needs explanation) or to an early validation checkpoint. The claim that validation exceeding training "indicates that overfitting has not yet occurred" conflates two separate phenomena (underfitting vs. a possible data distribution mismatch).

- **The paper generalizes from one ViT variant.** Only ViT B32 is tested, but conclusions are drawn about "Vision Transformers" as a class. More recent ViT variants (DeiT, Swin, etc.) may behave differently for face recognition.

- **Inference speed discussion is sparse.** The text only explicitly compares ViT to MobileNet ("23.81% slower"), even though Table 2 reportedly contains times for all six models. The abstract's claim of "impressive inference speed, rivaling even the fastest Convolutional Neural Networks" is overstated given the paper's own data shows ViT is 23.81% slower than the fastest CNN (MobileNet).

### Trivial

- The phrase "rivaling even the fastest Convolutional Neural Networks" in the abstract is a stretch. The data shows ViT is 23.81% slower than MobileNet. "Competitive" or "close to" would be more accurate than "rivaling."

## Nice-to-Haves

- A learning rate sweep or optimizer comparison for at least a subset of architectures would substantially strengthen the core claim.
- Attention map visualizations or embedding space analysis (e.g., t-SNE) could deepen the understanding of why ViT is more robust to occlusion and distance.
- Testing additional ViT variants (DeiT, Swin, etc.) would strengthen generalization claims.
- Reporting GPU memory measurements for training and inference would substantiate the memory footprint claim without additional experiments.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Strength: "Carefully controlled experimental methodology for fair comparison"** — This strength from the Strength Finder conflicts with the verified Major weakness about fixed hyperparameters. The controlled design is a valid methodological choice, but the specific settings may not be equally appropriate for all architectures, and this caveat is central enough that framing it as a strength would be misleading without acknowledging the limitation.

- **Strength: "Superior accuracy and zero overfitting under identical training conditions"** (second part of Core strength #3 from Strength Finder) — The "zero overfitting" claim is undermined by the ambiguous/confusing writing about training vs. validation accuracy in Section 3.3, as noted in Minor weaknesses.

- **Harsh critic's claim that "Table 2 reports inference time per batch for only some models"** — Table 2's caption states it includes inference time for all models ("accompanied by the inference time per batch of 256 images"). The text singles out MobileNet for discussion, which is standard practice; there is no evidence the full comparison is missing.

- **Harsh critic's claim that "the choice of ViT B32 is somewhat arbitrary" and that newer variants should be used** — While testing more variants would strengthen the paper, using ViT B32 is a defensible choice as it is the original, most widely studied ViT architecture. This is scope creep rather than a genuine flaw.

- **Harsh critic's claim that the paper should include learning curves** — Not a standard requirement for this type of comparison paper; the training results (Table 1) and code availability provide sufficient information.

## Novel Insights

The reviews surface two insights worth noting beyond the paper's own contributions. First, the tension between the paper's fixed-hyperparameter design and its strong comparative claims is real but asymmetric in its impact: the accuracy comparisons are most vulnerable, while the robustness findings (distance and occlusion) are architectural properties that are less sensitive to optimizer choice or learning rate. Second, the paper would benefit from a lower-stakes framing — positioning itself as a task-specific empirical study of "how ViT and CNNs behave differently under face-specific challenges" rather than "ViT outperforms CNNs" — which would both better match the evidence and make the acknowledged methodological limitations easier to accept. The robustness findings are the paper's genuine contribution, not the accuracy leaderboard.

## Suggestions

1. **Reframe the paper's contribution.** Shift from "ViTs outperform CNNs" to a nuanced analysis of "when and why ViTs differ from CNNs in face recognition" — emphasizing the robustness results (distance, occlusion) which are the strongest evidence, and treating accuracy under default settings as informative but not definitive.
2. **Either add empirical memory measurements or remove the memory footprint claim from the abstract and conclusions.**
3. **Treat the VGG result on UPM-GTI-Face masked honestly** — present it as evidence that ViT's advantage is not universal, and discuss the conditions (small dataset, severe occlusion + distance) where VGG remains competitive.
4. **Add uncertainty quantification** — at minimum report AUC with bootstrapped confidence intervals for the verification datasets.
5. **Clarify the ambiguous training/validation accuracy discussion** in Section 3.3.

## Score and Decision

This paper makes a genuine contribution by probing ViT-vs-CNN differences under face-specific challenges (distance degradation, real-world occlusions) that prior generic classification studies did not measure. However, the fixed-hyperparameter experimental design undermines the accuracy claims, the memory footprint claim is unsupported, counter-evidence is dismissed rather than analyzed, and no uncertainty quantification is provided. These issues are addressable in revision but collectively prevent acceptance in the current form.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>