## Summary

This paper proposes a user-side input obfuscation framework for privacy-preserving inference that works by "domain shifting" — transforming input images into a different part of the input space before sending them to a cloud-based classifier (the "oracle model"). Two variants are presented: (1) a model-specific (whitebox, "out-of-place") approach that maps inputs to a non-significant domain using an encoder trained jointly with a decoder through the oracle, and (2) a model-agnostic (blackbox, "in-place") approach that permutes class membership via GAN-based cross-class image translation, requiring only the top-1 class label from the oracle. The authors demonstrate faithful classification recovery (e.g., 98% fidelity on MNIST, ~90% on CIFAR-10) with very low obfuscation overhead (~0.5ms on MNIST) compared to cryptographic alternatives.

---

## Strengths

- **User-side-only mechanism requiring no oracle model modification**: The encoder/decoder pipeline operates entirely on the user's side, and the commercial DL model remains completely unmodified (lines 16–17, 35). This is a meaningful differentiator from HE/MPC approaches like CryptoNets or Delphi, which require the service provider to re-implement models using cryptographic primitives.

- **Model-agnostic variant operates under pure blackbox access**: The in-place domain-shifting method requires only the top-1 class label from the oracle model (lines 188–190). The encoder/decoder is trained without any access to the oracle's internals, and the paper correctly identifies the necessary condition (in-domain obfuscation enables consistent outputs across different oracle models). This makes the method directly applicable to real-world commercial APIs that expose only class predictions.

- **Dramatically lower inference latency than cryptographic privacy schemes**: The out-of-place method completes inference in ~0.5 ms on MNIST and ~1.2 ms on CIFAR-10 (Section 5.3, lines 370–372). The paper explicitly contrasts these with prior HE/MPC results (0.481s in Juvekar et al. 2018; 472s in Liu et al. 2017 on comparable tasks). These are concrete speed improvements of multiple orders of magnitude.

- **GAN+DDPM hybrid encoder is a practical solution to a real failure mode**: The paper identifies that GAN-based encoders alone produce low-quality images on complex datasets (CIFAR-10, ImageNet), degrading oracle accuracy. It addresses this by chaining a GAN (class-to-class transformation in latent space) with a DDPM/Stable Diffusion (visual quality) — a pragmatic architectural decision documented in lines 254–255.

- **Systematic evaluation across five datasets and multiple oracle architectures**: Experiments cover MNIST, Fashion-MNIST, CIFAR-10, Tiny-ImageNet, and ImageNet, with oracle models spanning MLPs, CNNs, Vision Transformers, Swin Transformers, and ConvNeXt (Tables 1–4). The fidelity/accuracy results are consistent across diverse settings.

---

## Weaknesses

### Fatal
None.

### Major

- **The privacy evaluation is insufficient to support the paper's core claim.** The paper uses SSIM² between the original and obfuscated input as its primary privacy metric (Section 5, lines 335–337, 347). Low SSIM demonstrates perceptual dissimilarity but is **not a measure of privacy against an adversary**. Images can look very different (low SSIM) while still leaking substantial information through reconstruction attacks, membership inference, or attribute inference. The paper provides:
  - No evaluation against any known privacy attack (model inversion, reconstruction, membership inference).
  - No formal privacy guarantees (no differential privacy, no information-theoretic bound).
  - No discussion of what kind of information the obfuscated images might leak beyond class labels.
  
  For the model-agnostic approach, the paper correctly argues that class-level information is hidden (uniform class distribution, lines 200–201, 349), but this addresses only one axis of privacy. The obfuscated image is generated from an embedding of the original; nothing in the evaluation checks whether pose, background, texture, or identity-specific features leak through. A paper whose central contribution is "privacy-preserving" cannot rely solely on a perceptual similarity metric as its privacy evidence.

- **No baselines or comparisons against other input-obfuscation methods.** The paper compares only against cryptographic approaches (HE/MPC) for latency (Section 5.3), but never compares against non-cryptographic input-obfuscation methods such as:
  - Differential privacy for inference (noise addition with known ε guarantees).
  - Simple baselines like Gaussian noise, JPEG compression, or downsampling at comparable fidelity levels.
  - Adversarial perturbation-based privacy methods.
  
  Without such comparisons, the reader cannot assess where the proposed method sits on the privacy-utility Pareto frontier relative to alternatives. The claim of "preserves privacy with minimal impact on classification performance" (abstract) has no baseline for calibration.

### Minor

- **Notational error in the SSIM objective (Eqs. 4–5)**: The equations define the obfuscation loss as SSIM²[**f(x)**, EN(x)], where **f(x)** was defined earlier (line 57) as the oracle model's class-label output (a categorical variable). Computing mean intensity, variance, and covariance of a class label is mathematically meaningless. The surrounding text (line 164) correctly states the SSIM should be between **x** and EN(x), making this a clear typo. While this does not affect the actual implementation (any implementor would follow the text), it signals a proofreading gap in a core formulation.

- **Quantification of accuracy drops on complex datasets is vague**: For the model-agnostic approach on CIFAR-10 and ImageNet, the paper states only "there are accuracy drops" (line 354) without specifying how large they are. The relevant table (Table 4) is an image extracted by the parser whose precise numbers are not paraphrased in the text. The reader cannot assess the severity of the degradation.

- **Latency comparison with HE/MPC lacks a caveat about fundamentally different security models**: Section 5.3 presents latency numbers (0.5ms vs. 0.481s vs. 3.58s) without explicitly noting that HE/MPC methods provide **provable cryptographic security** while the proposed method offers no formal privacy guarantees. While the paper's introduction and background sections do discuss HE/MPC, the latency comparison table/figure would benefit from a clear caveat that speed gains come at the cost of a fundamentally weaker (and unevaluated) security model.

- **No confidence intervals or variance estimates** are reported for any experimental metric (fidelity, accuracy, SSIM²). Single-run point estimates make it impossible to assess the stability or statistical reliability of the results.

- **The model-agnostic approach's resource assumptions partially undercut its motivation**: The user needs labeled training data and the ability to train GANs (and for complex datasets, Stable Diffusion-scale DDPMs). If a user possesses labeled training data and the compute to train generative models capable of cross-class image translation in latent space, it is reasonable to ask why they cannot train a classifier directly. The paper does not acknowledge or address this tension.

### Trivial

- The notational error in Eqs. (4)–(5) described above (f(x) where x is intended).

---

## Nice-to-Haves

- Implementing reconstruction attacks, membership inference, or attribute inference attacks to provide a meaningful privacy evaluation.
- Comparing against simple obfuscation baselines (additive Gaussian noise, JPEG compression, random cropping) to contextualize the privacy-utility trade-off.
- Reporting whether the model-specific (out-of-place) encoder remains robust when the oracle model is updated, fine-tuned, or replaced.

---

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh critic claim: "The SSIM notational error reveals confusion in the objective (structural — affects reproducibility)."** — The notation error is real but minor; the text on line 164 unambiguously states the correct formulation (SSIM between x and EN(x)). No implementor would be confused. Downgraded to Minor.
- **Harsh critic claim: "The comparison against HE/MPC methods is structurally unfair and misleading."** — The paper provides necessary context in Sections 1–2 about HE/MPC security properties. The latency comparison is factually correct. The paper should add a caveat, but calling this "structurally unfair" overstates the issue. Partially merged into Minor weakness above.
- **Strength Finder claim: "SSIM² as a principled obfuscation objective."** — Kept implicitly through the method description; removed as a standalone strength because it partially conflicts with the verified weakness about SSIM being insufficient as a privacy metric. SSIM² as an *optimization objective* for perceptual obfuscation is reasonable, but the paper uses SSIM² values as *evidence of privacy*, which is the core gap.
- **Harsh critic claim about model-agnostic resource assumptions being "structural"** — This is a reasonable observation but not structural; it is a tension worth noting but does not invalidate the approach. Moved to Minor.

---

## Novel Insights

None beyond the paper's own contributions.

---

## Suggestions

1. **Replace SSIM²-based privacy evaluation with adversarial evaluation.** The single highest-leverage improvement is to implement reconstruction attacks, membership inference attacks, and attribute inference attacks on the obfuscated images. If the method withstands these, that would constitute genuine privacy evidence. If not, the paper needs to honestly characterize the scope of privacy it provides (currently limited to class-level obfuscation, which is demonstrable for the model-agnostic variant).

2. **Add non-cryptographic baselines.** Compare against simple Gaussian noise addition, JPEG compression, and DP-based inference at comparable fidelity levels. This would let readers see where the proposed method sits on the privacy-utility Pareto frontier.

3. **Quantify all accuracy drops precisely in the text.** For the model-agnostic CIFAR-10 and ImageNet results, report the exact accuracy numbers rather than saying "there are accuracy drops."

4. **Add a caveat to the latency comparison** explicitly noting that HE/MPC provides cryptographic security guarantees while the proposed method does not, and that the speed comparison is between fundamentally different threat models.

5. **Report statistics (mean ± std or confidence intervals) for all experimental metrics** across multiple runs.

---

## Score and Decision

The paper introduces a genuinely novel domain-shifting framework for input obfuscation with two well-motivated variants, strong fidelity results on simple datasets, and impressive latency figures that meaningfully improve over HE/MPC approaches. The model-agnostic variant's ability to operate with only blackbox (top-1 label) access is a practical contribution.

However, the paper's central claim — that it "preserves privacy" — is inadequately supported. The sole privacy metric (SSIM²) measures perceptual dissimilarity, not resistance to adversarial inference. No attack evaluation is conducted, no formal privacy guarantees are offered, and the paper overstates what it demonstrates. Combined with the absence of non-cryptographic baselines and vague quantification of the accuracy drop on complex datasets, the paper in its current form does not meet the bar for a top venue.

The core ideas have merit and a substantially revised version with proper adversarial evaluation and honest scope characterization could be competitive.

**MY FINAL SCORE: <score>4.0</score>**
**MY FINAL DECISION: <decision>Reject</decision>**