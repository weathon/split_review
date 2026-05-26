Now I have a thorough understanding of the paper and the calibration landscape. Let me write the final consolidated review.

## Summary
2-3 sentence summary...

## Strengths
...

## Weaknesses
...

## Calibration Report

Let me document the anchor comparison process.

**Round 1 Bracket (wide):** I searched for topical anchors in low (<3.5), mid (3.5-7.5), and high (>7.5) bands, plus weakness-anchored queries for overclaimed theoretical guarantees and unfair baseline comparisons.

**Round 2 Narrowing (inside the bracket):** I searched for anchors in (4.5, 6.5) on the most topically relevant terms.

**Anchor List:**

1. **fkNsgI1nye** — "Secure Diffusion Model Unlocked" (avg 3.00, reject, r1-low). Poorly structured paper with unclear experiments. Our paper is substantially stronger.
2. **jbfDg4DgAk** — "Sparse Watermarking in LLMs" (avg 3.00, reject, r1-low). Unrelated domain (LLM watermarking). Not comparable.
3. **vK8C37eHXM** — "Sample what you can't compress" (avg 3.20, reject, r1-low). Unrelated topic.
4. **HexshmBu0P** — "A Recipe for Watermarking Diffusion Models" (avg 5.33, reject, r1-mid & r2). Similar domain. Had unclear copyright scenario and limited novelty. Our paper has clearer contribution.
5. **T0ebbDO60R** — "SuperMark" (avg 3.75, reject, r1-mid & r2-weakness). Similar domain, criticized for limited novelty. Our paper is stronger.
6. **ll2nz6qwRG** — "Hidden in the Noise" (avg 5.83, accept, r1-mid & r2). Similar domain (distortion-free diffusion watermarking). Accepted despite some overclaiming concerns. Our paper has comparable quality but similar issues.
7. **uHdf9F1tY4** — "DiffusionShield" (avg 5.50, reject, r1-mid & r2). Similar domain, mixed reviews.
8. **1IwoEFyErz** — "Shallow Diffuse" (avg 6.00, reject, r2). Similar topic (diffusion watermarking). Stronger theoretical foundation but weaker evaluation. Our paper is comparable.
9. **ETFfXGM3e4** — "SAT-LDM" (avg 5.50, reject, r2 & r2-weakness). Similar domain, criticized for unclear motivation. Our paper is slightly stronger.
10. **uzz3qAYy0D** — "VideoShield" (avg 5.83, accept, r2). Video watermarking, accepted despite mixed reviews.
11. **jln7IcheW6** — "Pseudo- vs. True-Randomness" (avg 4.33, reject, r2-weakness). LLM watermarking, different domain.
12. **0SpkBUPjL3** — "Unremovable Watermarks for Open-Source Language Models" (avg 3.75, reject, r2-weakness). LLM watermarking, different domain.

**Round 1 bracket:** The paper sits between 4.5 and 6.5. It is clearly stronger than SuperMark (3.75) and comparable to Shallow Diffuse (6.00) and Hidden in the Noise (5.83).

**What did the low-band anchors fail at, and does the paper share those failures?** Low-band anchors (3.0-3.75) failed due to unclear scenarios, missing baselines, poor presentation, and limited novelty. The paper under review does NOT share these failures — it has a clear method, comprehensive evaluation, and genuine novelty. The weakness-anchored queries showed that papers with overclaimed theoretical guarantees scored between 3.75 and 6.0, which is consistent with my bracket.

**Final determination:** Score 5.5. The paper has a novel method and solid empirical evaluation, but is held back by a mismatch between the theoretical claims (computational indistinguishability) and what is actually proven (moment matching up to 3rd order). This is an addressable issue, and with proper revisions the paper could be a strong contribution.

Let me now write the full review.Now I have all the information needed. Let me write the final consolidated review.

## Summary

The paper introduces Spherical Watermark, a framework for embedding watermarks into the Gaussian noise prior of diffusion models without per-image key storage. The method operates in three stages: (1) a binary embedding module mixes repeated watermark bits with random padding via an invertible matrix T over 𝔽₂, (2) a spherical mapping module normalizes the resulting binary vector onto the unit sphere, applies an orthogonal rotation, and scales by a chi-square-distributed radius to produce a vector that is approximately Gaussian, and (3) this watermarked noise is used as the initial latent in Stable Diffusion. The paper provides theoretical analysis of moment matching up to third order and empirical results on undetectability, robustness, and computational efficiency.

## Strengths

1. **Novel method design with a clear practical advantage.** The binary embedding + spherical mapping approach is a genuinely novel construction for lossless watermarking that eliminates per-image key storage. The claimed advantage — avoiding key management overhead while maintaining losslessness — is demonstrated concretely: extraction is roughly **four orders of magnitude faster** than the PRC baseline (Figure 4), and the method sustains high detection accuracy across watermark capacities where PRC completely fails (Figure 6a, beyond l_m=2000). This practical improvement is the paper's clearest contribution.

2. **Comprehensive evaluation across diverse settings.** The experimental suite is thorough: two datasets (COCO, SDP), two model versions (SD v1.5, SD v2.1), multiple ODE solvers (DDIM, PNDM, DPM-Solver++), a wide range of post-processing attacks (Gaussian noise, brightness, blur, JPEG, median filter, resize), and adversarial attacks from WEvade. The ablation studies (Tables 3–5, Figure 6) isolate the contribution of each module and parameter. This level of coverage exceeds what is typical in this space.

3. **Strong empirical undetectability and robustness.** The binary classifier experiments (Figure 2) show that Spherical Watermark achieves near-50% accuracy (indistinguishable from random), matching the PRC baseline, while lossy methods and Gaussian Shading with fixed keys are easily detected. Under adversarial attacks (Table 2), Spherical Watermark achieves ACC 98.12% and TPR 99.83%, outperforming both PRC (97.69/95.38) and Gaussian Shading (88.06/99.23), consistent with the paper's theoretical analysis linking losslessness to adversarial robustness (Appendix E).

## Weaknesses

### Fatal
None.

### Major

1. **Mismatch between the problem formulation's cryptographic language and the actual theoretical guarantee.** Section 3.1 defines undetectability using computational indistinguishability with a security parameter ρ and negligible function negl(ρ) (Eq. 2–4). However, the theoretical analysis in Section 3.3 only establishes moment matching up to third order and asymptotic convergence of marginal laws. No bound on total variation or KL divergence is given, no computational reduction is provided, and the security parameter ρ is never instantiated. The paper acknowledges in Section 5 that "higher-order moments may deviate from the true prior," but the problem formulation promises a stronger guarantee that the theory does not deliver. This gap between advertised and proven guarantees undermines the central claim of "provable losslessness." **Fix:** Either (a) replace the computational indistinguishability setup with a statistical moment-matching statement that accurately reflects what is proven, or (b) provide a rigorous distance bound between the watermarked distribution and 𝒩(0,I).

### Minor

1. **Gaussian Shading comparison uses the weakened fixed-key variant without also reporting the per-image-key version.** The paper acknowledges (Section 4.1) that "with fixed keys, Gaussian Shading no longer achieves true losslessness," and the experiments show that fixed-key Gaussian Shading is easily detected (97% classifier accuracy). The comparison is reasonable for the paper's "encryption-free" claim (both methods use fixed keys), but the paper also claims to "outperform existing lossless approaches." Including Gaussian Shading with per-image keys (its intended lossless configuration) would strengthen this claim by showing that Spherical Watermark matches its undetectability while offering practical advantages. Without this comparison, the reader cannot fully evaluate the trade-off.

2. **Inversion error of the diffusion ODE solver is not quantified.** The extraction pipeline (Eq. 12) relies on an approximate inverse of the diffusion ODE. The paper acknowledges this approximation (Section 5) but does not report the latent-space reconstruction error ‖\hat{z}_T − z_T‖² or how it varies with solver steps, guidance scale, or attack strength. Reporting this would help assess how much error the spherical mapping's redundancy can tolerate.

3. **Fixed secret key (T,C) security not discussed.** The paper's "encryption-free" framing is accurate in that per-image keys are eliminated, but the method still depends on a fixed secret key (T,C) whose compromise would break all watermarks. Key management, rotation, and the security implications of a single point of failure are not discussed. This trade-off relative to per-image key schemes deserves explicit treatment.

### Trivial

- Eq. 6 writes "l_m = N × l_m" instead of "l_{Nm} = N × l_m," a minor notation issue that does not affect understanding.
- The matrix indexing in Algorithm 1 (R[i,j,G] with three dimensions then reshaped) is slightly confusing; a clearer notation would help reproducibility.

## Nice-to-Haves

- **Confidence intervals or statistical significance tests** for the undetectability experiments (near-50% accuracy over 5 runs). A test against the null hypothesis would strengthen the claim of indistinguishability.
- **A discussion of what constitutes an "inversion-breaking" attack** (mentioned in Section 5). The paper identifies this failure mode but does not characterize the attack strength needed to trigger it.
- **Extended analysis of the spherical 3-design claim.** While the claim that 3-wise independent hypercube vertices form a spherical 3-design is mathematically sound (it follows from moment matching up to degree 3), a self-contained proof sketch in the main text would benefit readers unfamiliar with the spherical design literature.

## Removed Points

These points were flagged for removal but are retained here for transparency:

1. **"Spherical 3-design claim may not hold"** (Harsh Critic #3) — **REMOVED.** The Harsh Critic asserted that 3-wise independence is insufficient for a spherical 3-design. This is incorrect: for normalized hypercube vertices {±1/√n}ⁿ with independent entries, 3-wise independence implies that all moments up to order 3 match the uniform spherical measure. The first, second, and third moments of such a set are exactly those of the uniform sphere. The claim is well-founded.

2. **"Unfair comparison with Gaussian Shading" characterized as a structural flaw** (Harsh Critic #2, in part) — **DOWNGRADED to Minor.** The comparison against fixed-key Gaussian Shading is reasonable for the paper's stated goal (encryption-free, no per-image keys). The paper is transparent about this choice ("Note that with fixed keys, Gaussian Shading no longer achieves true losslessness"). The missing per-image-key comparison is a completeness gap, not an unfair comparison. Retained as a Minor weakness.

3. **"Formatting/style nitpicks"** — **REMOVED** per instructions.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface an unexpected angle that the paper itself did not articulate.

## Suggestions

1. **Tone down the theoretical claim in the problem formulation.** Replace the computational indistinguishability setup (Eq. 2–4) with a statistical moment-matching statement that matches what is actually proven: "the watermarked noise matches the standard Gaussian up to third-order moments, and empirical tests confirm that higher-order deviations are undetectable by trained classifiers." This aligns the claims with the evidence.

2. **Add a comparison against Gaussian Shading with per-image keys** on the FID and classifier-based undetectability metrics. If the results show comparable undetectability, the paper's practical advantage (no key storage) is cleanly isolated. If Gaussian Shading with per-image keys also achieves 50% detection, the paper should state this explicitly and reframe the contribution as practical rather than statistical.

3. **Report latent-space reconstruction error** (e.g., ‖\hat{z}_T − z_T‖²) in the ablation section (alongside Table 4), broken down by solver, number of steps, and attack type. This would directly quantify the approximation error that the spherical mapping must tolerate.

## Score and Decision

<score>5.5</score>
<decision>Accept</decision>