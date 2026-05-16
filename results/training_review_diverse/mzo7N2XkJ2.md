Here is my final consolidated review.

---

## Summary

This paper proposes the first defense against convolution-based unlearnable examples (UEs). It introduces EPD, an edge-pixel-based detector to identify convolution-based UEs, and COIN, a defense that applies random bilinear interpolation to disrupt class-wise multiplicative noise. The paper also introduces two new convolution-based UEs (VUDA and HUDA) for broader evaluation. On CIFAR-10 against CUDA, COIN achieves 72.41% average test accuracy versus 47.04% for the next best defense (AT), a 25.37% absolute improvement. The detection scheme EPD achieves 89.21% ACC and 0.891 AUC on CIFAR-10.

## Strengths

- **First effective defense against convolution-based UEs, with strong empirical results.** Table 1 shows that 11 prior defenses all fail against CUDA (marked ✗), while COIN succeeds (✓). In Table 2, COIN's 72.41% average on CIFAR-10 against CUDA dwarfs the next best defense AT (47.04%), and similar margins hold on CIFAR-100 (47.41% vs. 33.85%). These are genuine, large-margin improvements over existing methods that were specifically designed for bounded UEs.

- **Principled theoretical motivation via GMM analysis.** The paper defines two quantitative metrics (Θ_imi for intra-class matrix inconsistency and Θ_imc for inter-class matrix consistency), validates the hypothesis that increasing these improves accuracy in a low-dimensional GMM setting (Figure 3), and designs a random matrix A_r that achieves this. This formal grounding distinguishes the work from ad-hoc trial-and-error approaches.

- **Expands the attack landscape with two new convolution-based UEs (VUDA and HUDA).** The paper designs vertical and horizontal filter-based convolution UEs, providing broader evaluation benchmarks. COIN achieves 72.44% and 73.05% average accuracy against VUDA and HUDA respectively on CIFAR-10 (Table 5), while all existing defenses remain near or below 50%, confirming generalization.

- **Simple yet effective detection scheme (EPD).** EPD uses only summed edge pixel values across RGB channels with a linear SVM. On CIFAR-10 it achieves 89.21% ACC and 0.891 AUC across four diverse UE combinations; on ImageNet20 it achieves 99.91% ACC and 0.998 AUC (Table 4). The detection is computationally efficient and directly motivated by a clear visual observation.

## Weaknesses

### Major

- **Missing comparison against generic random augmentations.** COIN applies random bilinear interpolation with per-pixel offsets sampled from U(−α, α). Many well-known transformations produce similar effects: random affine, random perspective, elastic deformation, random displacement fields, or RandAugment. The paper compares only against fixed defense methods (AT, ISS, AVATAR, ECLIPSE, etc.) but never against any simple random-warp baseline. If generic random augmentations achieve comparable defense against CUDA, then COIN's specific bilinear-interpolation design is not the cause — heavy randomization is. This gap directly affects the paper's claim that COIN represents a *novel* defense mechanism rather than the rediscovery that strong random warps break convolution-based UEs. The paper's core empirical result (COIN works) remains, but the novelty of the *specific design* is unsubstantiated without this comparison.

- **The theoretical GMM analysis is not shown to connect to the actual COIN operation on real images.** The paper defines Θ_imi and Θ_imc in a low-dimensional GMM space, validates the hypothesis there, designs a random matrix A_r that increases these metrics, and then "regards the previous process … as a random linear interpolation process" to motivate bilinear interpolation on images (Section 3.2 → Section 4.1). However, the paper never measures whether COIN actually increases Θ_imi or Θ_imc on real images (those metrics are defined for matrices, not for bilinear interpolation coefficients), nor does it empirically verify that the mapping from the GMM construction to bilinear interpolation is more than an analogy. The GMM analysis serves as plausible motivation but is not a demonstrated justification for the specific design. The paper should either (a) approximate the equivalent linear operation of bilinear interpolation and measure its effect on class-conditional variance, or (b) explicitly reframe the GMM section as an intuition/ablation rather than a theoretical grounding.

### Minor

- **No end-to-end evaluation of the EPD + COIN pipeline.** EPD detection accuracy and COIN defense accuracy are reported separately. A false negative means a convolution-based UE goes undefended; a false positive means COIN is applied to non-convolutional samples (potentially degrading them). The paper acknowledges that COIN "cannot be effective for all types of UE" but does not quantify the harm. An end-to-end experiment that applies EPD first, then COIN only on detected samples, and reports final test accuracy is needed to demonstrate practical effectiveness.

- **VUDA and HUDA are relatively weak attacks, which tempers the significance of defending against them.** The w/o-defense baseline for VUDA is ~41% and for HUDA ~40% on CIFAR-10 (Table 5), compared to ~25% for CUDA (random guessing is 10%). These attacks are effectively blurring filters that still leave the model far above chance. COIN's strong performance against them is partly because the attacks are weak. This does not invalidate the results but should be interpreted with caution.

- **Overclaiming on ImageNet100 results.** The abstract claims "a significant improvement on the CIFAR and ImageNet datasets." On ImageNet100 (Table 2), COIN's average (37.48%) is only 0.88% above AT (36.60%), and on ResNet18 specifically, AT (37.82%) slightly outperforms COIN (37.80%). The claim of "significant improvement" is accurate for ImageNet20 (60.9% vs. 52.5%) and CIFAR datasets, but overstated for ImageNet100.

- **The experimental protocol for Figure 3 (hypothesis validation) is underspecified.** The paper states that the top row varies Θ_imc while Θ_imi remains constant, and the bottom row varies Θ_imi while Θ_imc remains constant — both "via changing parameter a_y." How does changing a single parameter (a_y, the CUDA tridiagonal matrix parameter) independently control one metric while holding the other fixed? The paper does not explain this protocol, making the validation difficult to interpret or reproduce.

### Trivial

- **Typo in equation:** In Section 4.1, line 281 shows `{\omega_y}_i = {s_x}_i - {m_y}_i` when it should be `{s_y}_i - {m_y}_i` (using `s_x` instead of `s_y`).

## Nice-to-Haves

- A quantitative characterization of the edge-pixel bias that EPD relies on (histograms of edge pixel values for convolution-based vs. bounded UEs) would strengthen the detection motivation.
- Clarifying the boundary effects of the modulo-arithmetic-based shift (the random matrix A_r uses circular shifts, which is not standard for image interpolation) would aid reproducibility.
- Reporting standard deviations across multiple runs for the main results would increase confidence, though single-run evaluation is common in this benchmark setting.

## Removed Points

- **"Learning rate is listed as 0."** — This is a parser artifact from PDF extraction (the actual value is 0.1). Per rules, formatting artifacts are not author errors.
- **"Figure 5 axis labels missing"** — The figure caption states it shows "The impact of α," and the resolution issue is likely a PDF extraction artifact.
- **Generic strengths from the Strength Finder** — The summary paragraph of strengths is duplicative of the bulleted strengths above; no unique content was lost.
- **Criticism that the paper's GMM analysis is "ornamental" (in the strong sense)** — The paper explicitly frames the GMM-to-image connection as an analogy/intuition, not a formal proof. The concern about the gap is valid (kept above as a major weakness), but the characterization "ornamental" overstates the issue.
- **Criticism that VUDA/HUDA column headers in Table 1 are "redundant"** — This is a presentational non-issue.

## Novel Insights

The key novel insight from the reviews is a framing question that the paper does not adequately address: is the mechanism that makes COIN effective *specific to its bilinear interpolation design*, or is it simply the general principle that strong random pixel-level warping breaks class-wise convolutional perturbations? The paper's own GMM analysis suggests the latter (any random matrix that increases Θ_imi/Θ_imc works), which implies that many random transformations should work. The absence of a comparison against simpler random augmentations leaves this question open and weakens the paper's claim about the specific design being meaningful.

## Suggestions

1. **Add baseline comparisons against generic random augmentations.** Test random affine, random perspective, elastic deformation, and random displacement fields with comparable distortion magnitude (tuned to match COIN's α=2.0). If these achieve similar defense, the paper should reframe its contribution as "random warping suffices to break convolution-based UEs" and focus on the detection scheme and the characterization of why warping works. If COIN outperforms these baselines, the specific bilinear design is validated.

2. **Evaluate the EPD + COIN pipeline end-to-end.** Train on a mix of convolution-based and bounded UEs, apply EPD detection, apply COIN only to detected samples, and report final test accuracy along with false positive/negative rates.

3. **Clarify the GMM-to-image connection.** Either (a) approximate the linear operation of bilinear interpolation and measure its effect on Θ_imi/Θ_imc, or (b) explicitly state that the GMM analysis provides intuition but does not formally constrain the image-domain design.

4. **Tone down the "significant improvement" claim for ImageNet100** or qualify it with the specific margins.

5. **Fix the typo in Equation (ω_y)** and explain the protocol for independently varying Θ_imc and Θ_imi in Figure 3.

## Score and Decision

The paper tackles an important problem and presents the first empirical demonstration of an effective defense against convolution-based UEs, with impressive margins over 10 existing methods. The core empirical finding is genuine and valuable. However, the paper has significant gaps: it does not compare against simple random augmentation baselines that could produce the same effect, the theoretical framing is not substantiated for real images, and the detection+defense pipeline is not evaluated as a whole. The missing baseline comparison is the most serious issue, as it leaves unclear whether COIN's specific design matters or whether heavy randomization alone is responsible.

These gaps are addressable in a major revision. On balance, the empirical contribution is strong enough to warrant acceptance pending the addition of the missing baselines and pipeline evaluation.

**MY FINAL SCORE:** <pineapple>6.0</pineapple>
**MY FINAL DECISION:** <orange>Accept</orange>