- Decision: Reject
- Avg Score: 4.75
- Scores: 3, 6, 5, 5
Now I have sufficient verification of the claims. Let me construct the consolidated review.

## Summary

The paper proposes denoising-assisted (DA) classifiers for diffusion guidance: instead of feeding only the noisy image to a diffusion classifier, the DA-classifier receives both the noisy image **x** and the corresponding denoised estimate **\hat{x}** (obtained via a pretrained score network) as simultaneous inputs. The authors show that this simple architectural modification improves classification accuracy on diffused test examples (Table 1), yields perceptually more structured classifier gradients (Figures 2–4), and improves conditional generation FID/IS (Table 2) on CIFAR10 and ImageNet. They also present a theoretical analysis linking the Jacobian ∂\hat{x}/∂x to the covariance of the conditional mean, and extend the approach to semi-supervised learning.

---

## Strengths

- **Clear and consistent quantitative improvements in both classification and generation.** Table 1 shows higher test accuracy for the DA-classifier on CIFAR10 and ImageNet, and Figure 1 confirms this advantage across all noise scales. Table 2 shows FID improvements (CIFAR10: 2.91→2.62, ImageNet: 9.18→8.42) and IS improvements at roughly matched precision/recall. These are the paper's strongest pieces of evidence.

- **Simple, modular architecture with minimal overhead.** The DA modification adds only an extra input convolution to process the denoised image, reuses the pretrained score network without retraining it, and does not alter the sampling algorithm (Section 3, "Experiment setup"). This makes the contribution easy to adopt in practice.

- **Theoretical perspective on gradient structure.** Theorem 1 (Section 3) connects the Jacobian ∂\hat{x}/∂x to the covariance matrix Cov[\bar{x}_t|x], providing a conceptual explanation for why DA-classifier gradients align more with perceptual features. Even though the analysis assumes optimality, it offers a useful lens for understanding the empirical observations.

- **Semi-supervised gains demonstrated.** Figure 6 and Table 3 show that the DA-classifier outperforms the noisy classifier in the Score-SSL semi-supervised setting, and the approach is sensibly adapted from FixMatch to the diffusion setting.

---

## Weaknesses

### Fatal
None. No verified weakness invalidates the paper's core claims.

### Major

1. **Missing baseline: a classifier trained on the denoised input alone.** The paper compares the DA-classifier (noisy + denoised inputs) against a noisy classifier (noisy input only), but never trains or evaluates a classifier that receives *only* the denoised image \hat{x} (and time t) as input. Such a baseline is needed to disentangle two effects: (a) the benefit of the dual-input architecture with gradient flow through the denoiser, versus (b) the simpler explanation that a cleaner input alone suffices for the gains. The zeroing-out experiment on line 90 ("we zeroed out one of the input images…") only measures the *trained* DA-classifier with one channel silenced at test time; it does not answer whether a classifier trained from scratch on \hat{x}-only would match or exceed the DA-classifier's accuracy and generation quality. Without this baseline, the paper's central claim — that the *combination* of noisy and denoised inputs specifically delivers the improvements — is not fully supported by the evidence presented.

### Minor

2. **Gradient evaluation is entirely qualitative.** Figures 2–4 show min-max normalized gradients that appear more structured for the DA-classifier, but no quantitative metrics (e.g., gradient-class correlation, overlap with semantic segmentation, or class-conditional saliency fidelity) are provided. The paper states "improved perceptual alignment" as a key benefit (abstract, line 14), yet this claim rests solely on visual inspection, which is subjective, especially when both gradient maps are contrast-enhanced (Figure 4). This does not invalidate the paper's other quantitative results, but it limits the strength of the gradient-alignment narrative.

3. **Theoretical analysis has limited practical applicability.** Theorem 1 characterizes ∂\hat{x}/∂x under the assumption of *optimal* score-network parameters, and the paper itself acknowledges on line 128 that "in practice, the score-function is parameterized by unconstrained, flexible neural architectures that do not have exactly symmetric jacobian matrices." The theorem only addresses the second term of Eq. (8); the first term's contribution is not theoretically analyzed. While the theory provides a useful intuition, it does not constitute a rigorous or verifiable explanation of the observed improvements under realistic conditions.

4. **ImageNet DA-classifier has a fine-tuning advantage.** For ImageNet, the DA-classifier is initialized from the *pretrained noisy classifier* and fine-tuned with an added input convolution (line 76), while the noisy classifier baseline is the original pretrained checkpoint without comparable fine-tuning. This confound weakens the directness of the ImageNet comparison. However, the CIFAR10 results — where both classifiers are trained from scratch — show consistent DA-classifier improvements, partially mitigating this concern.

5. **Semi-supervised framework is a conceptually incremental adaptation.** The Score-SSL framework applies FixMatch's pseudolabeling + consistency regularization to the diffusion setting, using diffusion noise as augmentation. While the implementation is not trivial, the conceptual novelty is limited, and the paper's own numbers (Figure 6, DA-classifier ~86% on CIFAR10 with 4000 labels vs. FixMatch at reported 93.58%) show a notable gap to discriminative semi-supervised methods. The paper fairly notes these are not directly comparable, but the framing as "competitive with discriminative semi-supervised models" (line 170) overstates the case.

### Trivial
None.

---

## Nice-to-Haves

- **Quantify gradient alignment** using a metric such as the gradient's dot product with class-specific saliency maps or its effect on class-conditional image editing. This would substantiate the "perceptual alignment" claim beyond visual inspection.
- **Report variance or confidence intervals** for the main results in Tables 1 and 2. While single-run evaluation is common in this benchmark setting, variance estimates would strengthen reliability.
- **Ablate the contribution of the two gradient terms** in Eq. (8) during generation (e.g., by scaling each term separately) to directly test whether the second term drives the improvements as hypothesized.

---

## Removed Points

These points are flagged to be removed; treat them with caution.

1. *"Theorem 1 equation box is empty / broken."* — This is a PDF-parser artifact; the original submission contained the equation. The text surrounding the theorem (lines 122–128) conveys the claimed result (∂\hat{x}/∂x = Cov[\bar{x}_t|x]). Removed per the rule about parser artifacts.
2. *"No confidence intervals or statistical tests."* — Single-run evaluation without confidence intervals is standard practice for large-scale diffusion benchmarks (FID/IS on 50k samples). This is a community-standard issue, not a specific weakness of this paper. Moved to Nice-to-Haves.
3. *Missing related works.* — Per instructions, the reviewer cannot verify missing citations.
4. *Various formatting/style nitpicks* — Parser artifacts, not author errors.
5. *Strength Finder generic strengths* — Some claimed strengths ("this paper addressed an important problem") are generic and removed.

---

## Novel Insights

None beyond the paper's own contributions. The two reviews and my own reading did not surface a perspective on the work that the authors themselves had not already expressed.

---

## Suggestions

1. **Add the denoised-only classifier baseline.** Train a classifier that takes only \hat{x} and t as input, using the same architecture (minus the noisy-image input convolution) and training protocol. Report its accuracy, FID when used for guidance, and a qualitative gradient comparison. This single experiment would resolve the most significant uncertainty about the paper's contributions.
2. **Quantify the gradient comparison.** Compute a simple correlation or overlap metric between the classifier gradients and the clean image's class-discriminative regions (e.g., using the ImageNet segmentation benchmark or the gradient's class-conditional fooling rate).
3. **Disambiguate the ImageNet experiment.** Report results with the noisy classifier fine-tuned under the same schedule as the DA-classifier (or train both ImageNet classifiers from scratch, as was done for CIFAR10), to rule out the fine-tuning confound.

---

**Originality:** Moderate — the dual-input idea is simple but appears new in the diffusion classifier context.

**Importance of question:** The problem of improving diffusion classifier quality for guidance is timely and relevant.

**Claims supported:** The core accuracy and generation improvements are supported; the gradient-alignment and mechanistic attribution claims are less well-supported.

**Soundness:** Solid but with a notable gap (missing denoised-only baseline).

**Clarity:** Adequate; the paper sections are well-structured.

**Value to community:** The DA-classifier is a simple, easy-to-adopt modification that yields measurable improvements. The semi-supervised framework is more incremental.
