- Decision: Reject
- Avg Score: 4.00
- Scores: 6, 3, 3
Now I have all the information needed. Let me write the final consolidated review.

## Summary
This paper tackles defense against convolution-based unlearnable examples (UEs), a class of attacks that use class-wise multiplicative convolutional noise without norm constraints. The authors propose: (1) **COIN**, a defense that applies random bilinear interpolation to disrupt the class-wise multiplicative structure of convolution-based UEs, and (2) **EPD**, an edge-pixel-based detector to distinguish convolution-based UEs from bounded UEs. They also introduce two new convolution-based attacks (VUDA, HUDA) to broaden the evaluation. COIN outperforms 11 SOTA defense methods by large margins (e.g., 72.41% vs. 47.04% on CIFAR-10 against CUDA), and EPD achieves 89.21% detection ACC on CIFAR-10 and 99.91% on ImageNet20.

## Strengths
1. **Strong empirical defense results against convolution-based UEs.** COIN achieves consistently large improvements over existing SOTA defenses across all evaluated settings. On CIFAR-10 against CUDA (Table 1), COIN attains 72.41% average test accuracy across four architectures — a 25.37 percentage point gain over the best existing defense (AT, 47.04%). Similar margins hold on CIFAR-100 (47.41% vs. 33.85%), ImageNet datasets (Table 2), and against the two new attacks VUDA and HUDA (Table 3, ~72–73% vs. ~33–49%).

2. **Principled motivation via GMM-based analysis.** The paper formalizes two metrics — intra-class matrix inconsistency (Θ_imi) and inter-class matrix consistency (Θ_imc) — and experimentally validates in a low-dimensional GMM setting (Figure 3) that increasing either metric improves test accuracy on convolution-based UEs. This provides a clear justification for the design of a random multiplicative defense.

3. **Introduction of two new convolution-based UEs (VUDA and HUDA).** These attacks expand the limited scope of convolution-based UE research beyond the existing CUDA attack, and COIN defends against them effectively (Table 3). This is a useful contribution to the community for future benchmarking.

4. **Broad and diverse experimental evaluation.** The defense is tested across 4 architectures (ResNet18, VGG16, DenseNet121, MobileNetV2) and 4 datasets spanning resolutions from 32×32 to 224×224, with 11 baseline methods, giving comprehensive coverage.

5. **Effective detection of convolution-based vs. bounded UEs.** EPD achieves ACC of 89.21% (CIFAR-10) and 99.91% (ImageNet20) across multiple combination settings (Table 4), showing the edge-pixel heuristic is informative for distinguishing convolution-based from bounded UEs.

## Weaknesses

### Fatal
None.

### Major
1. **EPD is not evaluated on clean (unpoisoned) images.** All detection scenarios (S₁–S₇, Section 5.5) mix only convolution-based UEs with bounded UEs — clean samples are never included. In practice, a defender would need to distinguish convolution-based UEs from *both* bounded UEs and clean data. Without measuring false positive rates on clean images, the reported ACC (89.21%) is an incomplete characterization because mistakenly applying COIN to a clean sample would degrade its utility, while missing a convolution-based UE would leave the attack intact. The paper explicitly states that clean examples are left untouched (line 363), making this evaluation gap consequential.

2. **No end-to-end evaluation of the detection+defense pipeline.** Defense experiments (Tables 1–3) assume the defender knows all samples are convolution-based UEs and applies COIN universally. Detection experiments evaluate EPD in isolation. There is no experiment that chains EPD → COIN to measure final test accuracy when detection errors occur. Since EPD's CIFAR-10 accuracy is ~89%, roughly 11% of convolution-based UEs would be misclassified and left undefended, while some non-convolutional samples would be incorrectly transformed. The paper claims "the first detection and defense approach" but validates only the components separately, not the combined system.

3. **EPD's core heuristic (black edges) is adversary-circumventable without evaluation.** The detection relies on the observation that convolution-based UEs have black-biased edge pixels due to zero-padding. An adversary aware of this defense could trivially circumvent it (e.g., using reflection padding, post-processing edge pixels, or padding with small random values). The paper does not evaluate robustness against such adaptive attacks, which limits the practical security claim of the detection scheme.

### Minor
1. **No comparison with simple geometric augmentations as baselines.** The paper does not compare COIN against standard augmentations that also apply multiplicative/spatially-varying transformations (random cropping with bilinear interpolation, random affine, random rotation, random resizing). Since these also involve bilinear interpolation and could plausibly disrupt class-wise multiplicative noise, their absence makes it unclear whether COIN's success is due to its specific design or simply to applying *any* spatially varying multiplicative operation. Including even a subset of these would strengthen the claim that COIN's particular formulation is meaningful.

2. **The GMM analysis motivates but does not formally connect to the image-domain method.** The paper defines Θ_imi and Θ_imc, designs a random matrix A_r that increases them in GMM space, and validates in Figures 3–4. However, the extension to real images via bilinear interpolation is analogical, not formal: interpolation is not a global matrix multiplication in pixel space, and no bounds or measurements are provided to show that Θ_imi/Θ_imc actually increase when COIN is applied to images. The empirical results stand on their own, but the theoretical framing is more motivational than foundational.

3. **EPD is not compared against a simpler baseline (e.g., threshold on mean edge intensity).** The feature extraction (summing pixel values along four edges → 12-dim vector → linear SVM) is reasonable, but the paper does not ablate the SVM component against a simple decision threshold on total edge darkening. A one-dimensional threshold would be even simpler and might achieve similar performance; showing that the SVM provides meaningful improvement would strengthen the design.

### Trivial
None of consequence beyond what is covered above.

## Nice-to-Haves
- Include clean samples in detection evaluation (S₁–S₇ could be extended to include a clean class).
- Add end-to-end detection+defense experiment quantifying accuracy under pipeline errors.
- Compare COIN with standard geometric augmentations (random crop, random rotation, random affine) to clarify whether the specific design is necessary.
- Report precision/recall or a confusion matrix for EPD rather than only ACC and AUC.
- Test COIN's sensitivity to the attack strength parameter a_y and to different convolution kernel sizes beyond the default settings.

## Removed Points
- **"Missing related work"**: Removed — not verifiable without external sources; the paper's coverage of UE defenses is adequate.
- **"Baseline hyperparameters may not be optimized"**: Removed — this is a generic concern applicable to nearly all ML papers; no specific evidence of mistuning was provided.
- **"Minimal implementation details"**: Removed — the paper provides reasonable training details (SGD, 80 epochs, momentum 0.9, learning rate) and any remaining formatting artifacts are parser issues.
- **"The paper's code and reproducibility"**: Removed — speculation about missing code; standard practice for anonymized submissions.
- **Strength: "Clear connection between low-dimensional theory and practice"**: Demoted — the connection is analogical/intuitive rather than rigorous, as noted in Minor Weakness #2. The GMM analysis is a useful motivation but not a formal bridge to the pixel-domain method.

## Novel Insights
The reviews surface a recurring tension in the paper's structure: the theoretical GMM analysis and the practical image-domain method (COIN) are connected by analogy rather than formal derivation, yet the paper frames the theory as explanatory for why COIN works. This leaves a gap — the reader cannot tell whether COIN's design is uniquely informed by the theory or whether many random transformations would achieve similar effects. The critic's suggestion to test simple augmentations (random crop, rotation) directly operationalizes this question. Additionally, the detection scheme's reliance on a specific, easily-circumvented observable property (black edges) is a structural vulnerability that could limit real-world applicability unless the paper explicitly scopes its threat model to non-adaptive adversaries.

## Suggestions
1. **Extend EPD evaluation to include clean samples** — report false positive/negative rates on clean data and compute detection accuracy when clean images are mixed with UEs.
2. **Run an end-to-end experiment** where EPD → COIN is applied to a mixed dataset (convolution-based UEs + bounded UEs + clean) and measure final test accuracy, showing the cost of detection errors.
3. **Add a few simple geometric augmentation baselines** (random crop with bilinear interpolation, random affine) to COIN's comparison set to demonstrate that the specific design of COIN matters beyond being "any random multiplicative transform."
4. **Acknowledge and discuss the adaptive adversary concern** for EPD — either scope the threat model appropriately or evaluate robustness against circumvention strategies (e.g., reflection padding).
