Now I have a thorough understanding of the paper. Let me write the review.

---

## Summary

Spherical Watermark is a lossless, encryption-free watermarking framework for diffusion models. The core idea is to embed binary watermark bits into the Gaussian noise input of a diffusion model via three reversible modules: (1) a binary embedding that mixes watermark bits with random padding through a sparse binary matrix; (2) a spherical mapping that normalizes to the unit sphere, applies an orthogonal rotation, and scales by a chi-square-distributed radius to produce approximately Gaussian noise; and (3) a diffusion integration module that feeds this noise into a pretrained model. The authors prove that the resulting noise distribution satisfies a spherical 3-design and matches the standard Gaussian up to third-order moments, providing a lossless watermark that requires no per-image cryptographic key management, is computationally efficient (extraction ~4 orders of magnitude faster than PRC Watermark), and is robust to common post-processing and adversarial attacks.

---

## Strengths

- **Elegant technical construction backed by coherent theory.** The polar decomposition of Gaussian noise (direction on sphere × chi-square magnitude) is a well-known fact, but its deliberate exploitation as a watermarking primitive is genuinely novel. The chain of results — Theorem 3.1 (3-wise independence of z⁽¹⁾), Theorem 3.2 (z⁽²⁾ is a spherical 3-design), Lemmas 3.3–3.4 (rotation preserves the design; chi-square scaling recovers Gaussian moments) — forms a clean and internally consistent theoretical framework.

- **Meaningful practical advantages over prior lossless methods.** The four-orders-of-magnitude extraction speedup over PRC Watermark (belief-propagation decoding eliminated entirely) and the elimination of per-image key storage (unlike Gaussian Shading) are quantitative, reproducible claims that address genuine deployment barriers. These are not marginal improvements.

- **Thorough experimental validation.** The paper compares against six baselines (traditional and latent-based), tests across two prompt datasets, evaluates both classifier-based undetectability and tracing accuracy under clean/post-processing/adversarial conditions, includes ablation studies on every module and all hyperparameters, and tests sensitivity to ODE solver and timestep choices. The experimental design is notably careful: latent-level MLP classifiers and image-level ResNet-18 classifiers are used to probe distributional shifts at both levels.

- **Honest discussion of limitations.** Section 5 explicitly acknowledges that only third-order moments are matched (higher-order moments may deviate) and that inversion-breaking attacks can still compromise recovery. This transparency is appreciated and strengthens confidence in the paper's claims.

---

## Weaknesses

### Fatal
None.

### Major

- **Mismatch between the formal security definition and what is theoretically proved.** Section 3.1 states a computational indistinguishability requirement: |Pr[A(z_w)=1] − Pr[A(z)=1]| ≤ negl(ρ). However, what is proved (Theorems 3.1–3.2, Lemmas 3.3–3.4) is only that z_w matches N(0, I_{l_x}) up to third-order moments via the spherical 3-design property. A spherical 3-design does *not* equal the uniform distribution on the sphere; it merely matches polynomial statistics of degree ≤ 3. Consequently, an adversary exploiting fourth-order statistics (e.g., kurtosis-based distinguisher, or a higher-order moment test on coordinates) could in principle distinguish z_w from a true Gaussian — violating the stated definition. The paper acknowledges this in Section 5, but the mismatch is already present in the formal claim. The security parameter ρ is never tied to any concrete construction parameter, so the "negl(ρ)" framing has no operational meaning.

- **Comparison with Gaussian Shading is handicapped.** The paper evaluates Gaussian Shading with *fixed* keys across all users, explicitly noting that "with fixed keys, Gaussian Shading no longer achieves true losslessness." This handicapped configuration is then used to show that Gaussian Shading is detectable (97% classifier accuracy). The fair comparison should be acknowledged as a design trade-off: Gaussian Shading with per-image keys is truly lossless but costly; Spherical Watermark is approximately lossless without per-image keys. Framing fixed-key Gaussian Shading as the direct comparison understates the paper's actual trade-off.

### Minor

- **Security of the "encryption-free" signature.** K = {T, C} is described as "kept fixed and secret," but the paper does not formally analyze what breaks if K is leaked or partially compromised. With per-image cryptographic keys, individual compromises are bounded. With a single fixed signature, a single key leak allows an adversary to both forge watermarks for arbitrary users and strip all watermarks. A brief security discussion around K's protection requirements would be appropriate.

- **Majority-vote decoding produces no confidence score.** The extraction decision is a hard majority vote, and the paper reports ACC and TPR@1%FPR but does not discuss how the 1%-FPR threshold is set or calibrated when there are 100 users, each with a different 512-bit message. The computation of TPR@1%FPR in a multi-message tracing setting (rather than binary detection) deserves a brief clarification.

### Trivial

- The abstract uses "exact multivariate Gaussian noise" but the construction only achieves approximate Gaussianity (up to 3rd-order moments). This slight overstatement is corrected later in the paper.

---

## Nice-to-Haves

- A study of how undetectability degrades as l_x decreases (e.g., for video diffusion models or other architectures with smaller latent spaces) would clarify how much of the empirical indistinguishability is due to high dimensionality versus the spherical design structure itself.

- A concrete binding between the security parameter ρ and the construction parameters (l_x, N, s) — even heuristically — would help practitioners reason about the security margin.

---

## Novel Insights

The central insight is that the polar decomposition of standard Gaussian noise can be *reversed constructively*: by separately controlling the directional component (via a spherical 3-design derived from discrete binary codes) and the magnitude component (by independently sampling from the chi-square distribution), one obtains approximately Gaussian noise without any cryptographic operations. The use of spherical t-designs as a bridge between combinatorial coding theory and continuous probability distributions is a contribution that may find use in other randomness-embedding problems beyond watermarking. Additionally, the demonstration that a sparse, non-cryptographic binary mixing matrix suffices to achieve 3-wise independence of a high-dimensional binary vector (Theorem 3.1), enabling downstream moment-matching, is a clean result with potentially broader applicability.

---

## Suggestions

- Formally bound the total variation distance between z_w and N(0, I_{l_x}) as a function of l_x, even in a simple asymptotic form. This would replace the "up to third-order moments" claim with a quantitative approximation guarantee and make the security analysis precise.
- Report Gaussian Shading's performance under *both* per-image key and fixed-key regimes in the comparison tables, making the trade-off explicit rather than implicit.
- Include a brief analysis of worst-case failure — specifically, what is the minimum l_x at which empirical classifier accuracy remains near 50%?

---

## Score and Decision

The paper offers a genuinely novel technical construction (spherical mapping for lossless watermarking), provides a coherent theoretical framework, demonstrates meaningful practical advantages (speed, no key management), and validates claims thoroughly across varied experimental conditions. The primary concern — the gap between the stated computational indistinguishability security definition and the third-order moment-matching actually proved — is acknowledged in the paper and is compensated by strong empirical evidence. The minor issue with the Gaussian Shading comparison framing does not invalidate the results. This is a solid, well-motivated contribution to an important and timely problem area.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>