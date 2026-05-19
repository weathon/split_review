## Summary
This paper introduces Ablated Learned Temperature Energy (AbeT), an OOD detection method that combines a learned temperature (from Hsu et al.) with the energy score (from Liu et al.), and then removes a "forefront temperature constant" term that counteracts the desired score behavior. The key insight is that the learned temperature appears in two places in the energy score — one helpful (Exponential Divisor Temperature) and one harmful (Forefront Temperature Constant) — and ablating the harmful term substantially improves OOD separability. The paper evaluates on classification (CIFAR-10/100, ImageNet), semantic segmentation (Cityscapes → LostAndFound/RoadAnomaly), and object detection (PASCAL VOC → COCO).

## Strengths
1. **Ablation study cleanly isolates the core contribution.** Table 3 shows that removing the Forefront Temperature Constant (comparing the two-temperature energy vs. AbeT) reduces FPR@95 by 28.76% (CIFAR-10), 59.00% (CIFAR-100), and 24.81% (ImageNet). This is direct, well-controlled evidence that the specific design choice — removing the foreground constant — is responsible for a large fraction of the improvement, independent of any other architectural changes.

2. **Strong and consistent classification results on CIFAR (well-controlled).** On CIFAR-10 and CIFAR-100 (Table 1), AbeT and its variants (AbeT+ASH, AbeT+ReAct, AbeT+DICE) consistently outperform all baselines. These comparisons use the **same ResNet-20 architecture and identical training hyperparameters** (as stated on lines 175 and 180), so architecture mismatch is not a confound here. AbeT alone achieves FPR@95 of 12±2 (CIFAR-10) and 31±12 (CIFAR-100) vs. the best baselines at 20±1 and 37±34 respectively.

3. **Empirical analysis of how the method works without OOD training data (Section 5).** The paper provides two concrete quantitative findings: (a) the nearest ID neighbor of an OOD point has only 76.42% accuracy vs. 91.89% overall — showing OOD-proximal ID points are disproportionately misclassified; (b) the 99% CI of AbeT scores on misclassified ID points (−20.88±0.57) is much closer to zero than on correctly classified ID points (−33.29±0.93). These directly support the mechanistic explanation that the model learns OOD detection through exposure to misclassified ID examples during training.

4. **Minimal computational overhead.** The learned temperature adds only 64 parameters to a ResNet-20 (0.02% increase) and increases forward-pass time by <3% (Section 2.3.2), making the approach practical.

5. **Architecture robustness demonstrated.** Table 2 shows that AbeT maintains strong OOD performance on a DenseNet-121 with ImageNet as ID (FPR@95 32.99 vs. 41.00 for the next-best Gradient Norm), confirming gains are not specific to a single backbone.

## Weaknesses
### Fatal
None.

### Major

1. **Confounded evaluation in semantic segmentation — gains cannot be attributed to the score alone.** In Table 4, the baseline OOD scores (Entropy, MSP, SML, ML, MHLBS) are taken from standard Cityscapes-trained models (mIOU 81.39), while AbeT uses a model trained from scratch with learned temperature and cosine logit head (mIOU 80.56). Because the underlying models differ, the dramatic improvements (e.g., FPR@95 on LostAndFound drops from 15.56 to 3.42) could be due to the different training setup (learned temperature + cosine head improving calibration) rather than the AbeT score formulation itself. A controlled comparison — applying the same baseline scores (Max Logit, MSP, Entropy) to the same model that AbeT uses — is needed to isolate the score's contribution. This confound weakens the claim that AbeT generalizes to segmentation.

2. **ImageNet classification comparison uses mismatched architectures for key baselines.** In Table 1 (ImageNet column), three starred baselines (Energy+DICE, Energy+ReAct, Energy+ASH) use ResNet-50, while AbeT uses ResNetv2-101. The paper honestly footnotes this, but the result is that the best non-AbeT number on ImageNet (Energy+ASH at FPR@95 16±13 on ResNet-50) is not directly comparable to AbeT's 40±11 (base) or 7±3 (AbeT+ASH) on ResNetv2-101. This does not invalidate the paper — the CIFAR comparisons are well-controlled, and many non-* baselines share the same architecture — but it means the ImageNet column in Table 1 cannot be read as a clean leaderboard, and the claim of SOTA on ImageNet specifically relies on the AbeT+ASH variant.

3. **Abstract claim of 35.39% FPR@95 reduction is ambiguous about which variant produces it.** The abstract states: "AbeT lowers the False Positive Rate at 95% True Positive Rate (FPR@95) by 35.39% in classification (averaged across all ID and OOD datasets measured) compared to state of the art." From the data, this figure appears to correspond to the **AbeT+ASH** variant (average FPR@95 of (10+30+7)/3 ≈ 15.67 vs. best per-dataset baselines ≈ 24.33, yielding ~35.6% reduction). The base AbeT does not achieve this reduction on ImageNet, where it underperforms Energy+ASH. The abstract should explicitly attribute this number to the best-performing variant to avoid overstating the contribution of the base AbeT score.

### Minor

4. **No controlled ablation comparing AbeT score vs. other scores on the same trained model (even for classification).** The paper does not apply MSP, Energy, Max Logit, or other OOD scores to the same learned-temperature-trained model that AbeT uses. Such an ablation would directly measure whether the AbeT score formulation itself adds value beyond the improved model calibration from learned-temperature training. The classification results on CIFAR are reasonably controlled at the architecture level (same ResNet-20), but this missing experiment would strengthen the paper.

5. **ID performance drop in segmentation undiscussed.** The Cityscapes mIOU drops from 81.39 (baselines) to 80.56 (AbeT). While small, this drop is not mentioned or analyzed. It would be helpful to know whether this is a consistent cost of the architectural modification or within expected variation.

6. **Base segmentation architecture not specified.** The paper describes modifying "the Inner Product per-pixel in the final convolutional layer" but does not name the segmentation backbone or framework (e.g., DeepLabV3+, PSPNet) used. This makes it harder to reproduce or assess the computational baseline.

### Trivial
None.

## Suggestions
1. **For the segmentation and detection experiments:** Re-run baseline OOD scores (MSP, Max Logit, Entropy, Energy) on the *same* model that AbeT uses (i.e., the model trained with learned temperature + cosine logit head) and re-report the comparison. This is the single highest-leverage improvement — it would transform the confounded comparison into a clean ablation of the score itself.
2. **For the ImageNet comparison:** Retrain the three *-marked baselines (Energy+DICE, Energy+ReAct, Energy+ASH) on ResNetv2-101 using the same training setup, or at minimum include a ResNet-50 AbeT variant for direct comparison.
3. **Clarify the abstract:** State which variant (AbeT+ASH) achieves the 35.39% average reduction, and note that base AbeT is competitive on smaller benchmarks (CIFAR) while the combined variant excels on ImageNet.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>

## Questions


## Decision
Accept
