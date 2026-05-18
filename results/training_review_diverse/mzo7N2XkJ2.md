Now I have everything I need. Let me compose the consolidated review.

## Summary

This paper addresses the problem of defending against convolution-based unlearnable examples (UEs) — a threat that prior defenses fail against. The authors propose COIN, a defense that applies random bilinear interpolation to corrupt the class-wise multiplicative noise pattern, and EPD, an edge-pixel based detection scheme. They also introduce two new convolution-based UEs (VUDA and HUDA). Extensive experiments across CIFAR-10/100 and ImageNet subsets with four architectures demonstrate that COIN dramatically outperforms 11 existing defenses (e.g., 72.41% vs. 47.04% next-best on CIFAR-10 with CUDA), and EPD achieves strong detection accuracy (89.21% on CIFAR-10, 99.91% on ImageNet20).

## Strengths

- **First effective defense against convolution-based UEs with large, consistent margins.** COIN raises test accuracy on CUDA-attacked CIFAR-10 from 24.92% (undefended) to 72.41%, outperforming the next best defense (AT at 47.04%) by over 25 percentage points (Table 1). On CIFAR-100 the advantage is 47.41% vs. 33.85%. This advantage holds across all three convolution-based UEs, four architectures, and four datasets (Tables 1–3, ImageNet results in Table 2).

- **Novel detection scheme EPD with strong empirical performance.** EDP leverages the observation that convolution-based UEs bias edge pixels toward black, achieving ACC of 89.21% (AUC 0.891) on CIFAR-10 and 99.91% (AUC 0.998) on ImageNet20 across seven diverse UE mixture settings (Table 4). The method is simple yet effective for the tested attack configurations.

- **Analysis of the defense mechanism via GMM provides a clear conceptual motivation.** The paper formalizes convolution-based UEs as multiplicative matrix perturbations in a GMM, defines metrics Θ_imi (intra-class inconsistency) and Θ_imc (inter-class consistency), and empirically validates that increasing these metrics mitigates the attack in the low-dimensional setting (Figure 3). This provides a clean conceptual framework that motivates the defense design, even if the connection to real images is heuristic.

- **Extensive evaluation against a wide range of baselines.** The paper compares against 11 SOTA defenses (AT, ISS-J/G, ECLIPSE, AVATAR, AA, OP, DP-SGD, Cutout, Mixup, CutMix) across four datasets and four architectures. The consistent advantage of COIN across all settings convincingly demonstrates the failure of existing approaches and the effectiveness of the proposed method.

## Weaknesses

### Fatal

None.

### Major

- **The theoretical GMM analysis is not formally connected to the real-image defense COIN.** The paper derives a random matrix A_r in the low-dimensional GMM space and shows it increases Θ_imi and Θ_imc. However, the actual defense (COIN) uses bilinear interpolation in the image domain, and the paper's argument for the connection is a single sentence: "we regard the previous process of multiplying A_r as a random linear interpolation process" (line 261). This is a heuristic analogy, not a derivation. The paper does not compute Θ_imi or Θ_imc for the image-domain defense, nor does it show that bilinear interpolation preserves the mathematical properties of A_r. COIN works well empirically, but the paper's framing gives the impression of a principled derivation when in reality the GMM analysis serves as inspiration. This gap is not fatal — the empirical results stand on their own — but the paper should be honest about this (e.g., frame COIN as inspired by the GMM analysis rather than following from it).

### Minor

- **No confidence intervals or multiple-seed runs for a randomized defense.** COIN's bilinear interpolation parameters are drawn from a uniform distribution, yet all results are reported as single numbers without standard deviations or ranges. For a method with inherent randomness, reporting variability across seeds (≥3–5) is standard practice and would help the community assess the stability of the defense. The large margins of improvement suggest the conclusion is robust, but the methodological rigor is incomplete.

- **No evaluation of COIN on clean (unattacked) data.** The paper does not report test accuracy when COIN is applied to clean training data without any UEs. This makes it difficult to assess the "collateral damage" of the defense — i.e., how much COIN degrades normal training. Since practical deployment would require knowing this cost, its absence is a gap.

- **No consideration of adaptive adversaries.** The evaluation assumes a static threat model where the attacker generates UEs without knowledge of the defense. The paper does not test whether an attacker aware of COIN could craft convolution-based UEs robust to random bilinear interpolation (e.g., by simulating the defense during attack generation or using kernels designed to survive such transforms). For a paper claiming the "first defense," this limits the strength of the claim. An experiment with a simple adaptive variant would significantly strengthen the paper.

- **Hyperparameter analysis for α is limited to CUDA.** The impact of α is only shown for CUDA on CIFAR-10 (Figure 5a). It is not shown for VUDA, HUDA, or the ImageNet experiments, so it is unclear whether the chosen α=2.0 is near-optimal across settings.

- **EPD's reliance on black-edge artifact is not analyzed for generality.** The paper observes that convolution-based UEs (CUDA, VUDA, HUDA) have biased edge pixels but does not analyze why this artifact occurs or whether it is a necessary property of convolution-based UEs. An attacker using different kernels (e.g., with periodic padding or learned kernels) might evade detection. The empirical results are strong for the tested attacks, but the detection mechanism is fragile in principle.

### Trivial

- VUDA and HUDA are simply vertical/horizontal stripe kernel variants of CUDA. While they serve a useful purpose for evaluation breadth, they are not conceptually novel. This does not detract from the paper's main contributions but inflates the contribution list.

## Nice-to-Haves

- An ablation study on the detection threshold θ in EPD to show robustness to reasonable variations.
- A discussion of the computational cost of applying random bilinear interpolation per image during training (e.g., throughput impact).
- Evaluation of EPD on a wider variety of convolution kernels (e.g., random kernels, Gaussian kernels) to test generalization of the edge artifact assumption.

## Removed Points

- The harsh critic's claim that "the paper claims COIN is effective against some bounded UEs (URP, OPS) in a single sentence, but no numbers are given" — this is factually incorrect. Line 456 explicitly states: "improves test accuracy from 16.8%, 28.4% to 81.1%, 80.1%." The numbers are present.

## Novel Insights

None beyond the paper's own contributions. The reviewers identified the theory-method gap and missing methodological rigor (confidence intervals, adaptive adversaries), which are standard concerns rather than novel observations.

## Suggestions

1. **Reframe the GMM analysis as inspiration, not derivation.** The empirical results are strong enough to stand on their own. A more honest framing would increase, not decrease, the paper's credibility. Remove claims that COIN "follows from" or "extends" the GMM analysis without formal connection.

2. **Add multi-seed results.** Re-run the main experiments (or at least a representative subset, e.g., CIFAR-10 with ResNet18) with 5 random seeds and report mean ± std.

3. **Add clean-data accuracy with COIN.** Report test accuracy when COIN is applied to clean datasets to quantify the defense's impact on normal training.

4. **Add at least one simple adaptive attack experiment.** For example, generate CUDA UEs while simulating COIN's interpolation during the attack optimization, or design a convolution kernel less affected by random interpolation, and report whether COIN's accuracy degrades significantly.

5. **Expand the hyperparameter analysis of α** to include VUDA and HUDA settings.

## Score and Decision

This paper tackles an important and timely problem (defending against convolution-based UEs, where no prior defense works) and provides strong empirical evidence that COIN is dramatically more effective than 11 existing defenses across diverse settings. The core empirical contribution is real and significant. The main weaknesses are: (1) the theoretical motivation is not formally connected to the actual defense method, creating an overclaimed "principled design" narrative, and (2) the evaluation lacks statistical rigor (no confidence intervals) and adaptive adversary analysis — standard expectations for a defense paper. These weaknesses are addressable in revision and do not invalidate the core empirical finding. The paper makes a genuine contribution to the field and deserves a fair hearing, but the presentation overclaims the theory-method connection and the evaluation needs stronger rigor.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>