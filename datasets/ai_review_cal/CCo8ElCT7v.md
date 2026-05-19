- Decision: Reject
- Avg Score: 4.25
- Scores: 3, 6, 5, 3
Now I have a thorough understanding of the paper. Let me write the final consolidated review.

## Summary

This paper presents an empirical comparison of Vision Transformers (ViT B32) against five CNN architectures (ResNet50, VGG16, Inception V3, MobileNet V2, EfficientNet B0) for face identification and verification. The models are trained on VGG Face 2 and evaluated on five datasets (LFW, ROF, SCface, UPM-GTI-Face, VGG Face 2) covering occlusions, distance variation, and surveillance quality. The central claim is that ViT outperforms CNNs in accuracy and robustness while offering competitive inference speed and smaller memory footprint.

## Strengths

- **Consistent top-tier identification accuracy across evaluation**: ViT achieves the highest test accuracy (99.81%) and is the only model with perfect top-5 accuracy (100%) on the VGG Face 2 evaluation set (Table 2). This is a concrete, verifiable result.

- **Multi-dataset, multi-challenge evaluation design**: The study uses five datasets covering face identification, verification, occlusions (sunglasses, masks), distance variation (3–30m), and surveillance-quality imagery. This breadth strengthens the generality of the observed patterns — ViT's advantage is not dataset-specific.

- **Quantitative evidence of robustness to distance and occlusions**: On SCface (Fig. 4), ViT maintains better AUC at medium/long distances. On ROF (Fig. 5), ViT achieves higher AUC and lower EER across mask, sunglasses, and combined occlusion conditions. On UPM-GTI-Face unmasked (Fig. 6a), ViT maintains AUC 0.63 at 30m while CNNs fall to ~0.5 (random). These patterns are consistent across multiple independent datasets.

- **Inference speed competitive relative to parameter count**: ViT is 23.81% slower than MobileNet despite having ~7× more parameters (Table 2). The paper provides the raw inference times, allowing readers to assess the trade-off.

## Weaknesses

### Fatal
None.

### Major

- **Identical hyperparameters across all architectures undermine the central comparison.** All six models are trained with exactly the same settings (Adam, lr=0.0001, batch 256, 25 epochs). The paper acknowledges this limitation ("we remain aware that networks might indeed perform optimally with distinct hyperparameter settings") but provides no mitigation — no hyperparameter search, no sensitivity analysis, no alternative training regimes. ViTs are known to benefit from AdamW + learning rate schedules, while CNNs typically use SGD+Momentum with decay. The observed performance gap could partly reflect different sensitivity to this specific training recipe rather than architectural superiority. The paper's core claim — "ViT outperforms CNNs in accuracy and robustness" — would be substantially stronger if the relative rankings were verified to be stable across different hyperparameter configurations. This is the most significant methodological limitation and should be addressed in any revision.

- **Memory footprint claim is stated as a finding but not empirically supported.** The abstract and conclusion states that ViTs have "a smaller memory footprint" than CNNs, and the paper argues this from architectural principles. However, no empirical measurements (peak GPU memory during training or inference) are reported. The only quantitative data provided is parameter count (Table 2), where ViT B32 (85.8M) is actually larger than most CNNs (ResNet50: 23.5M, Inception: 21.8M, MobileNet: 3.5M). The memory footprint claim concerns activation maps during training, which is a plausible architectural difference, but presenting it as a finding without measurement is a gap. The paper should either provide measured memory usage or reframe this as a known architectural characteristic from prior work.

### Minor

- **Inference speed claim is overstated.** The abstract and conclusion say ViT's inference speed is "rivaling even the fastest Convolutional Neural Networks." Table 2 shows ViT is 23.81% slower than MobileNet (the fastest CNN), and the paper's own text in §3.4 more accurately says "aligning with some of the fastest CNNs." The framing in the abstract/conclusion should match the more measured language in the evaluation section, since being 23.8% slower than the fastest competitor does not constitute "rivaling" it.

- **VGG outperformance on UPM-GTI-Face masked scenario is dismissed rather than investigated.** ViT ranks second to VGG (4% higher AUC) on this specific condition. The paper calls this "a non-reproducible anomaly" and speculates about feature detection without providing evidence. Running multiple trials or analyzing why VGG succeeds on small, masked images would be more informative. However, this is a single case on a small dataset (11 subjects), so it does not threaten the overall findings.

- **No measures of variance or statistical significance.** All accuracy, AUC, and EER results are reported as point estimates. For a comparative study claiming architectural superiority, the paper would benefit from multiple runs with different seeds or bootstrapped confidence intervals, especially on datasets where differences are small (e.g., LFW where all AUCs > 0.99) or where rankings could be noise-driven.

- **ViT's validation accuracy (99.81%) exceeds its training accuracy (98.86%), which is unusual and warrants investigation.** The paper interprets this as "overfitting has not yet occurred," which is one plausible explanation, but does not explore whether it could reflect a data split issue (e.g., validation images being systematically easier). This does not invalidate the results but would benefit from clarification.

### Trivial
None.

## Nice-to-Haves
- Include ViT B16 (patch size 16) as an additional ViT variant, since 224/32 = 7×7 patches is quite coarse for face recognition.
- Ablate the effect of ImageNet pre-training: all models are pre-trained, so ViT's advantage could partly reflect better transfer rather than intrinsic architectural superiority for faces.
- Report per-subject breakdowns for face verification to reveal whether ViT's advantage is uniform or concentrated in certain conditions.

## Removed Points

- **"Fewer epochs claim referenced to supplementary materials not included"**: Removed per hard rule — the parser strips supplementary materials; they exist in the original submission.
- **"The paper does not discuss the validation > training issue"**: Removed as factually incorrect — the paper does discuss it (§3.3), attributing it to no overfitting having occurred yet.
- **Harsh critic's specific inference time numbers (ResNet 0.156s, Inception 0.163s, etc.)**: These appear to come from Table 2 (an embedded image). The paper's text only explicitly states the 23.81% slower comparison with MobileNet. The critic's broader qualitative point about overstated framing is kept in Minor.
- **"Unfair comparison if asymmetry favors the baseline"**: Not applicable; no such claim was made.
- **Strengths that are generic or conflict with weaknesses**: The Strength Finder's point about "Controlled hyperparameter setup and reproducibility" is partially removed from Strengths because the identical hyperparameter approach is both a reproducibility feature (fixed seeds, public code) and the paper's main weakness. The reproducibility aspect (public implementation, fixed hardware/seed) is kept; the "controlled hyperparameter" framing is merged into the weakness section.

## Novel Insights

The most interesting observation across the reviews is the tension between the paper's methodological simplicity (identical hyperparameters, single ViT variant, no variance reporting) and the consistency of its empirical findings across multiple challenging datasets. The occlusion and distance-robustness results on ROF, SCface, and UPM-GTI-Face are independently informative even if the absolute accuracy comparisons are confounded by the hyperparameter issue. If a revision adds hyperparameter sensitivity analysis and memory measurements, the core findings about ViT's relative strengths under challenging conditions (distance, occlusions) would be well-supported. The consistent pattern — ViT excels precisely where local features are insufficient (occlusions, long distance) — aligns with the architectural motivation (global self-attention) and is the paper's most compelling contribution.

## Suggestions

1. **Address the hyperparameter limitation**: Either (a) tune each model with a small grid search over learning rate/optimizer and show rankings are stable, or (b) run multiple configurations and report which trends hold across regimes. At minimum, acknowledge that the comparison reflects performance under one specific training protocol rather than claims of architectural superiority.

2. **Provide measured GPU memory**: Report peak memory usage during training (for a fixed batch size) and inference for each model. This would either substantiate or appropriately qualify the memory footprint claim.

3. **Run a small ablation on UPM-GTI-Face masks**: 2–3 runs with different seeds would resolve whether VGG's outperformance is a statistical fluctuation or a real phenomenon worth investigating.

4. **Tone down the inference speed language**: Replace "rivaling even the fastest CNNs" with the more accurate "competitive with the faster CNNs, though 23.8% behind MobileNet" or similar.

5. **Consider adding ViT B16**: Given the coarse 7×7 patch grid of B32 on 224×224 inputs, B16 (14×14 patches) may be more representative of ViT's potential for face recognition.
