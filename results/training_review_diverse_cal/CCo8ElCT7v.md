Now I have verified all claims against the paper. Let me synthesize the consolidated review.

## Summary

This paper presents an empirical comparison of Vision Transformers (ViT B32) against five CNN architectures (ResNet-50, VGG-16, Inception V3, MobileNet V2, EfficientNet B0) on face identification and verification tasks. Evaluations span five datasets (VGG Face 2, LFW, SCface, ROF, UPM-GTI-Face) covering challenges including distance variation, occlusions, and surveillance conditions. The core finding — that under the chosen training protocol ViT consistently achieves the highest accuracy, strongest robustness to distance and occlusion, and competitive inference speed — is generally supported by the experimental evidence.

## Strengths

- **ViT achieves 100% top-5 identification accuracy on VGG Face 2**, the only model to do so, while also attaining the highest overall accuracy (Table 2). This directly supports the paper's central claim of ViT superiority in face identification.
- **Strong distance robustness demonstrated across two datasets**: On SCface, ViT significantly outperforms all CNNs at medium and long distances (Figure 4); on UPM-GTI-Face at 30 meters, ViT maintains AUC of 0.63 while CNNs drop to near 0.5 (random) (Figure 6a). This is the paper's strongest and most distinctive finding.
- **Occlusion robustness on ROF**: ViT achieves the highest AUC for both mask and sunglasses occlusions (Figure 5), consistent with the theoretical advantage of global self-attention being less disrupted by local occlusions.
- **Competitive inference speed despite larger parameter count**: ViT is only 23.81% slower than the fastest CNN (MobileNet) while having ~7× the parameters (Table 2), an interesting efficiency result.
- **ViT shows less overfitting during training**: ViT's validation accuracy (99.81%) exceeds its training accuracy (98.86%) at epoch 25, while CNNs show the opposite pattern (Section 3.3), suggesting better generalization under the fixed training budget.
- **Evaluation across five diverse, challenging datasets** provides ecological validity and covers multiple real-world face recognition challenges (unconstrained conditions, distance, occlusions, surveillance, mask+occlusion).

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **AUC/EER values are in figure legends only, not tabulated.** The paper claims ViT achieves the "highest AUC value and lowest EER" (line 105) and states these metrics are displayed in the ROC curve legends (line 112), but no numerical table exists. A reader cannot perform precise cross-dataset comparisons or extract exact values without reading values from figures. Adding a table with AUC and EER for every dataset/condition would substantially strengthen the paper.

- **No statistical significance or variability estimates.** Experiments use fixed seeds (single run). Given known variance in deep network training, differences of a few percent in AUC cannot be evaluated as stable or significant. This is especially problematic for the UPM-GTI-Face masked scenario (only 11 subjects, 484 images), where VGG surpasses ViT by 4% AUC and the paper dismisses this as a "non-reproducible anomaly" (line 117) — a claim that requires variance estimates to support. Bootstrapped confidence intervals or multi-seed runs would address this.

- **Memory footprint claim is asserted but not experimentally measured.** The abstract and conclusion claim ViT has a "smaller memory footprint," and Section 2.1 provides a theoretical argument. However, no peak GPU memory, activation memory, or model size measurements are reported. The only quantitative data is parameter counts (Table 2), where ViT (85.8M) actually exceeds most CNNs tested. Without measurement, this claim is unsupported.

- **Embedding extraction pipeline for verification is underspecified.** The paper does not state which layer provides the embedding, its dimensionality, or the similarity metric used to produce the ROC curves (cosine similarity, Euclidean distance, etc.). These details are necessary for reproducibility and for interpreting the verification results.

- **Model capacity confounds the architecture comparison.** ViT B32 (85.8M params) is compared against ResNet-50 (23.5M), MobileNet V2 (3.5M), etc. The claim that "ViTs outperform CNNs" conflates architecture with capacity. While parameter counts are reported, a controlled comparison (matching FLOPs or parameter budget) or a discussion of how scale affects the conclusions would strengthen the architecture-level claims.

- **Fixed training schedule may disadvantage CNNs.** All models use the same hyperparameters (0.0001 LR, Adam, 25 epochs). The authors acknowledge this (line 48), but the observation that CNNs overfit while ViT does not could partially reflect a suboptimal training regime for CNNs rather than a genuine architectural advantage. Training loss curves or convergence analysis would help assess this.

### Trivial

- The "83.33% loss reduction" (line 86) is mathematically correct (relative error reduction from 1.14% to 0.19%) but is presented without explicit framing, which could confuse readers unfamiliar with relative error metrics.
- The paper characterizes VGG's better performance on UPM-GTI-Face masked as a "non-reproducible anomaly" (line 117), but this is speculative without statistical evidence. A more measured statement acknowledging the small dataset size as a plausible cause would be appropriate.

## Nice-to-Haves

- Report FLOPs or MACs, which would complement inference time and parameter counts for a fuller efficiency picture.
- Report training time per model, which is practically relevant for practitioners choosing an architecture.
- Add a scatter plot of accuracy vs. parameter count (or inference time) to help separate architecture effects from capacity effects.
- The paper trains with softmax loss for closed-set identification but evaluates verification with embeddings from the same model. Discussing how verification performance might change with metric learning losses (ArcFace, CosFace) would add useful context.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *"The paper lacks a dedicated related work section on face recognition architectures"* — Per instructions, I cannot assess missing related works as I lack external sources to verify their presence or absence.
- *"No cross-dataset generalization evaluation (e.g., trained on VGG Face 2, tested on a different large dataset)"* — This is factually wrong: the paper already trains on VGG Face 2 and tests on LFW, ROF, SCface, and UPM-GTI-Face, which are all held-out datasets. This criticism misunderstands the experimental design.
- *"No open-set identification results"* — Scope creep. The paper clearly defines its scope as closed-set identification and verification; demanding open-set evaluation would change the paper's nature.
- *Several demanding suggestions from the "Missing Parts" section* (human studies, multi-seed runs at prohibitive cost) — These are practically infeasible for an academic submission and/or demand practices not standard for this type of benchmark paper.

## Novel Insights

None beyond the paper's own contributions. The reviews largely recapitulate the paper's results rather than generating new observations about them.

## Suggestions

1. **Add a table of AUC and EER values** for every dataset and condition (LFW; SCface per-distance and combined; ROF per-occlusion-type; UPM-GTI-Face per-distance and combined). This is the single highest-leverage improvement.
2. **Specify the embedding extraction pipeline**: which layer provides the feature vector, its dimensionality, and the similarity/distance metric used for verification scoring.
3. **Measure and report peak GPU memory** during training (and optionally inference) to substantiate the memory footprint claim, or else tone down the claim to match the theoretical discussion.
4. **Add confidence intervals or bootstrapped error bars** on AUC/EER for the smaller datasets (especially UPM-GTI-Face, where claims about anomalies are made).
5. **Soften the "non-reproducible anomaly" characterization** of VGG's UPM-GTI-Face masked result, as this conclusion is unsupported without variance estimates.
6. **Include training loss/accuracy curves** (or at least final convergence status) to support the overfitting discussion and address the concern that CNNs might improve with more epochs or tuned schedules.

## Score and Decision

**Originality**: Moderate. This is a comparative study, not a novel method, which is appropriate for a benchmark paper.  
**Importance of research question**: High. The ViT-vs-CNN question in face recognition is timely and practically relevant.  
**Claims well-supported**: Partially. The accuracy, distance robustness, and occlusion robustness claims are supported by the data presented. The memory footprint claim is unsupported.  
**Soundness of experiments**: Adequate but improvable — the evaluation covers diverse datasets but lacks statistical rigor and precise methodological documentation.  
**Clarity of writing**: Generally clear; the main experimental design and results are communicated effectively.  
**Value to community**: Useful as a reference benchmark for practitioners choosing architectures for face recognition.

The paper makes a real contribution by systematically evaluating ViT against multiple CNNs on face-specific challenges (distance, occlusion, surveillance) that go beyond generic image classification benchmarks. The weaknesses are substantive but addressable — none invalidate the core findings. This is a solid empirical contribution that with the suggested revisions would become a strong reference paper.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>