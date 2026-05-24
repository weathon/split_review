Now let me write the final consolidated review.

## Summary
The paper proposes RTA (Regression-based Test-time Adaptation), which replaces entropy-based view selection in CLIP TTA with a regression model (LightGBM decision tree) trained to predict pseudo-label cross-entropy loss from logits. The key insight is that there is a learnable mapping between logits and loss that generalizes across distributions, enabling a single offline-trained model to guide view selection at test time without per-instance updates. RTA is evaluated on ImageNet variants, 10 cross-domain datasets, and 3 multi-label datasets with two backbones, outperforming prior entropy-based TTA methods on average.

## Strengths
1. **Novel and well-motivated approach**: The idea of learning a regression mapping from logits to cross-entropy loss for view selection is genuinely novel in the CLIP TTA literature. The ceiling experiment (Tables 1–2) clearly motivates why better view selection is valuable — using ground-truth labels to select views yields massive gains over entropy-based selection (e.g., +25.9 ppt on ImageNet-A with ViT-B/16), establishing a justified upper bound.

2. **Comprehensive empirical evaluation**: The paper evaluates on 5 ImageNet variants + 10 cross-domain datasets + 3 multi-label datasets with two backbone architectures (RN50 and ViT-B/16), covering significantly more benchmarks than most TTA papers. The multi-label results (Tables 5–6) are particularly strong — RTA consistently outperforms ML-TTA across all three datasets and both backbones (e.g., 53.25 vs. 51.58 mAP on MSCOCO with RN50).

3. **Lightweight, one-time offline training**: The regression model uses LightGBM (max depth 5, 16 leaves, 100 rounds), with no test-time gradient updates needed. This contrasts favorably with methods requiring per-instance prompt tuning or memory banks. The ablation in Figure 5 shows that even 1,000 training samples already yield strong results, and performance stabilizes by ~5k samples.

4. **Empirical evidence for the logits-loss relationship**: Figure 2 (t-SNE visualization) shows clear clustering by loss, and Figure 3 reports Spearman rank correlations with statistical significance — providing two independent sources of evidence that a learnable mapping exists.

## Weaknesses

### Fatal
None.

### Major
- **Overclaimed "consistently outperforms" on cross-domain benchmarks**: The paper states "Across 10 cross-domain datasets, RTA consistently outperforms prior adaptation methods" (Sec. 5.1). In Table 4 (ViT-B/16), BCA outperforms RTA on 5 out of 10 datasets individually (Pets, Flowers, DTD, EuroSAT, SUN) — it is BCA that wins on more individual datasets. RTA achieves a higher *average* (68.70 vs. 68.59) but does not "consistently outperform" in the strict sense. The claim should be tempered to "achieves the highest average accuracy" or similar.

- **Data source for regression training not disclosed**: The paper states "we select ImageVal-12k as the regression mapping data" (Sec. 5.1). The name suggests a 12k subset of the ImageNet validation set, but this is never confirmed or defined. This is a transparency issue: if ImageVal-12k is indeed drawn from the standard ImageNet validation set (which serves as the test set for the ImageNet-family benchmarks), the regression model's training images share the same distribution as the test images for those benchmarks. While the model uses only pseudo-labels and learns a logit→loss mapping (not an image classification mapping), the paper should clarify the source and discuss any implications.

### Minor
- **Mapping transfer from original to augmented views unverified**: The regression model is trained exclusively on original (unaugmented) images (Sec. 4.2: "we only need to learn the regression mapping function based on the original image... without the need for additional data augmentation"). At test time, it is applied to augmented views (random crops, flips, color jitter). The paper does not provide any analysis (e.g., correlation between predicted loss and actual loss on augmented views) to verify that the mapping transfers, despite the fact that augmentation systematically shifts the logit distribution.

- **No comparison against a max-confidence baseline**: A natural baseline is selecting views with the highest softmax confidence (maximum predicted probability), which also requires no auxiliary training. This baseline is discussed in related work (e.g., Kim et al., 2020) but not included in any table. Without it, the specific advantage of the regression-based loss prediction over a simpler alternative is unclear.

- **Computational overhead not quantified**: The paper claims "negligible additional cost" but does not report inference time. For each of 64 views per test image, the regression model must predict a loss value. The runtime relative to baselines (Zero, TPT, BCA) should be quantified.

### Trivial
- In Table 4, the TDA method appears twice for ViT-B/16 (rows 7 and 8 from the bottom), likely a formatting artifact.

## Nice-to-Haves
- An ablation of the regression model choice (linear regression, small MLP vs. LightGBM) would strengthen the "lightweight" claim and show the mapping is non-trivial.
- Pseudo-label noise analysis: the regression targets depend on CLIP pseudo-labels with a confidence threshold of 0.8. The paper could report pseudo-label correctness on the regression set and test noise sensitivity.
- Statistical significance measures (confidence intervals or standard errors) would be helpful given the small margins (0.5–2%) on some datasets.

## Removed Points
These points are flagged to be removed, treat them with caution:

1. **Criticism that ceiling TTA results are implausible** — Removed. The ceiling experiment uses ground-truth labels (an oracle) to select top-k views. It is intentionally an upper bound meant to motivate the approach. The numbers are within expectation: with 64 random views of an ImageNet-A image, at least one view is likely to have high CLIP confidence on the true label. The reviewer misunderstood this as a claimed achievable result rather than an oracle bound.

2. **Criticism that ImageVal-12k leakage is a "structural" / "fatal" issue** — Demoted to Minor (addressed above). The regression model uses pseudo-labels, learns a logit→loss mapping (not classification), and generalizes to non-ImageNet datasets where leakage is irrelevant. The real issue is transparency about the data source, not fatal leakage.

3. **Criticism that "the claim that LCE selection is a 'free lunch' is unsupported"** — Removed. The paper uses "free lunch" to describe the learned regression mapping (not LCE), and the empirical results support the claim that the mapping transfers.

4. **Strength about "consistently outperforms" from Strength Finder** — Relaxed. As noted in Major weaknesses, the claim is overstated for cross-domain results, though the average is highest.

5. **Various formatting/style nitpicks, missing appendix content, generic reproducibility concerns** — Removed per filtering rules.

## Novel Insights
The reviews surface an interesting tension that the paper itself does not fully address: the ceiling experiment (using true labels) gives far larger gains (+25.9 ppt on ImageNet-A) than RTA's regression model recovers from pseudo-labels (~1.6 ppt over Zero on ImageNet-A). This gap between the oracle bound and what regression on pseudo-labels achieves suggests either (a) the pseudo-labels are too noisy to learn the true mapping, or (b) the logit→loss mapping from original images does not fully transfer to augmented views. The paper does not diagnose this gap, which would be a natural extension. Additionally, the multi-label results are noticeably stronger than the single-label results, which is interesting because it suggests the regression mapping may be especially effective when the output space involves multiple active logits — a dimension worth further exploration.

## Suggestions
1. Clarify the source of ImageVal-12k — is it a subset of the ImageNet training set, validation set, or an external collection?
2. Add a simple max-softmax-probability baseline for view selection.
3. Temper the "consistently outperforms" language on cross-domain results to "achieves the highest average accuracy."
4. Add a brief analysis (even in the appendix) of the correlation between predicted loss and actual loss on augmented views to verify mapping transfer.
5. Report inference time (ms/image) relative to baselines.

## Score and Decision
**Initial bracket (Round 1)**: Based on calibration search, the weak anchors (score < 3.5) are withdrawn/rejected papers averaging 2.50; middle anchors (3.5–7.5) include closely related TTA papers (BaFTA: 5.50, ML-TTA: 6.25, DeYO: 7.00); strong anchors (>7.5) are all 8.00 (oral/posters with substantially stronger theoretical or empirical contributions). The paper sits in the 5.0–7.5 bracket.

**Narrowing (Round 2)**: Examining anchors in narrower bands confirms the paper is above BaFTA (5.50, Reject) — RTA has more comprehensive experiments, a more novel core idea, and stronger multi-label results. It is comparable to ML-TTA (6.25, Accept Poster) — both have similar empirical scope, though RTA covers more benchmarks. It is below DeYO (7.00, Accept Spotlight) — DeYO provides theoretical grounding for its findings, while RTA is primarily empirical. L2C (6.25, Accept Poster) is comparable. Final score placed at 6.0 based on: a novel core idea, comprehensive experiments, but overclaimed language on cross-domain results, the ImageVal-12k transparency gap, and the unverified mapping transfer — none fatal, but enough to keep it at "marginally above acceptance" rather than a stronger accept.

**Anchors retrieved across all rounds**:
- pdzHpQbGrn.md (2.50, R1) — Withdrawn; substantially weaker in rigor and results.
- JIlIYIHMuv.md (2.50, R1) — Withdrawn; unrelated continual learning paper.
- yyIHdaSDUU.md (2.50, R1) — Withdrawn; unrelated VLM encoder paper.
- j1FLTvgyAh.md (2.50, R1) — Reject; few-shot prompt learning, less comprehensive eval.
- 75PhjtbBdr.md (6.25, R1/R2) — Accept Poster (ML-TTA); directly comparable, RTA matches or exceeds its scope.
- VLuJL8cnGk.md (5.00, R2) — Reject; 3D paper, not comparable.
- 9w3iw8wDuE.md (7.00, R1) — Accept Spotlight (DeYO); similar entropy-limitation motivation, stronger theory.
- KNtcoAM5Gy.md (5.50, R1/R2) — Reject (BaFTA); similar domain, weaker experiments and novelty.
- TPZRq4FALB.md (8.00, R1) — Accept Poster; multi-modal TTA, stronger.
- 5Ca9sSzuDp.md (8.00, R1) — Accept Oral; CLIP interpretability, not directly comparable.
- 1aF2D2CPHi.md (8.00, R1) — Accept Oral; data-free distillation, not comparable.
- tqh1zdXIra.md (8.00, R1) — Accept Oral; HPO paper, not comparable.
- lF9QXpfNHm.md (4.67, R2) — Withdrawn; open-world TTA, weaker eval.
- iGbuc9ekKK.md (5.75, R2) — Accept Poster; 3D CLIP, not comparable.
- kIP0duasBb.md (6.67, R2) — Access denied, not read.
- sEMJ1PLSZR.md (6.25, R2) — Access denied, not read.
- TD3SGJfBC7.md (6.25, R2) — Accept Poster (L2C); comparable scope, RTA has more datasets.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>