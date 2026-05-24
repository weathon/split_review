Now I have sufficient calibration context. Let me write the final consolidated review.

## Summary

This paper proposes Spherical Watermark, a lossless watermarking framework for diffusion models that maps binary watermarks to Gaussian noise via a three-module pipeline: binary embedding (mixing watermarks with random padding for 3-wise independence), spherical mapping (projecting onto the unit sphere, orthogonal rotation, and chi-square scaling), and diffusion integration. The key claimed advantages are: no per-image key storage (unlike Gaussian Shading), fast extraction (unlike PRC), theoretical guarantees of undetectability, and strong empirical robustness. Experiments on Stable Diffusion show FID matching the original distribution, near-chance classifier detection, and high extraction accuracy under post-processing and adversarial attacks.

## Strengths

- **Novel encryption-free lossless watermarking design.** The paper introduces an elegant spherical-mapping approach that eliminates the per-image key management required by Gaussian Shading and the heavy cryptographic decoding of PRC. The method maps binary watermarks → unit sphere → rotated sphere → chi-square-scaled Gaussian noise using only a fixed signature (T, C), which is a genuine architectural contribution over prior lossless schemes.

- **Strong empirical undetectability.** Figure 2 shows that a ResNet-18 classifier trained on image-level data achieves only chance-level accuracy (~50%) for Spherical Watermark, while Tree-Ring and Gaussian Shading (with fixed keys) are detected at 100% and 97% accuracy. Table 1 reports FID values nearly identical to the original (48.12 vs 48.13 on COCO SD v1.5), confirming no measurable distribution shift.

- **Orders-of-magnitude faster extraction than PRC.** Figure 4 shows extraction time at roughly 10⁻³.⁵ seconds for Spherical Watermark versus 10¹ seconds for PRC Watermark (four orders of magnitude slower). This directly addresses the practical latency bottleneck of cryptographic lossless schemes.

- **Superior robustness under adversarial attacks.** Table 2 shows that under WEvade adversarial attacks, Spherical Watermark achieves 98.12% ACC and 99.83% TPR, while all lossy methods (DwtDct, DwtDctSvd, RivaGan, Tree-Ring) drop below 27% TPR. This empirically validates the paper's claim that losslessness underpins robustness.

- **Thorough ablation studies.** Figure 6(b)-(c) verifies that omitting binary embedding makes the noise trivially detectable and omitting spherical mapping collapses robustness. Table 4/5 show independence from ODE solver choice and timestep schedule — the method works reliably across DDIM, PNDM, and DPM-Solver++.

## Weaknesses

### Major

- **Theoretical guarantee is overstated relative to what is proved.** The paper claims in Section 3.3 that "the final latent code z_w is distributed as N(0, I_lx)" and in the Conclusion that watermarked inputs are "provably and empirically indistinguishable from a standard Gaussian prior." However, the proof only establishes that z^(2) forms a spherical 3-design (matching moments of the uniform spherical distribution up to degree 3), and Lemma 3.3 shows convergence of marginals to Gaussian only in the limit l_x → ∞. The theoretical result is *approximate moment-matching up to third order*, not exact distributional equality or computational indistinguishability as defined in Eq. (2). The Discussion section (Section 5) does acknowledge that "higher-order moments may deviate," but the framing in Sections 1, 3.3, and 6 overclaims. This is a significant disconnect between claimed and actual guarantees. *(Evidence: Section 3.3 line "we provide theoretical guarantees that... the final latent code z_w is distributed as N(0, I_lx)" vs. the Discussion acknowledgment. The abstract itself is more careful: "preserves the target prior up to third-order moments.")*

### Minor

- **Gaussian Shading baseline evaluated in a weakened configuration without a per-image-key comparison.** The paper states (Section 4.1) that "with fixed keys, Gaussian Shading no longer achieves true losslessness" and then evaluates it with exactly that configuration, producing degraded undetectability (97% detection) and FID (50.70 vs. 48.12). While this comparison is informative for the practical scenario where key storage is undesirable, the paper does not also report Gaussian Shading in its intended lossless mode (per-image keys) to isolate whether the advantage comes from the spherical design or from the evaluation configuration. The PRC comparison provides a fairer baseline, but the absence of a proper Gaussian Shading baseline weakens the claim of superiority. *(Evidence: Section 4.1, experimental settings; Table 1 FID values.)*

- **Overly broad claim about lossy vs. lossless watermarking.** The paper states (Section 3.1) that "lossy watermarking can be easily broken by adversarial attacks, whereas lossless watermarking remains unaffected." This is only demonstrated for one specific adversarial attack (WEvade). The statement should be qualified as applying to the tested attack, not universalized. *(Evidence: Section 3.1, last paragraph.)*

### Trivial

- None.

## Nice-to-Haves

- Provide a comparison with Gaussian Shading using per-image keys (even if only in the appendix) to fully support the claim that Spherical Watermark's undetectability is competitive with the lossless variant of Gaussian Shading, not just the fixed-key variant.
- Include a brief discussion of false positive rates for watermark detection on unwatermarked images (beyond the implicit control at 1% FPR via TPR@1%FPR).
- Summarize the WEvade adversarial attack parameters (strength, budget, threat model) in the main text rather than deferring entirely to the appendix.

## Removed Points

These points are flagged to be removed — treat them with caution:

- *"The spherical 3-design argument is imprecise and underspecified in the main text."* — The proof details are deferred to Appendix C, which is standard for ICLR papers. The main text defines spherical t-design (Definition 3.1) and states the theorem clearly. Without access to the appendix, this criticism cannot be evaluated, and deferring proofs is standard practice.
- *"The paper does not discuss the false positive rate of watermark detection."* — The paper evaluates TPR@1%FPR, which inherently controls FPR at 1%. This is standard in the watermarking literature and sufficient.
- *"The paper should include confidence intervals for FID values."* — Table 1 already reports mean and standard deviation (1-sigma error bars), which is the standard reporting format for FID.
- *Various formatting/style nitpicks and speculation about unobtainable appendices.* — Removed per filtering rules.

## Novel Insights

None beyond the paper's own contributions. The reviews do not identify a perspective on the work that the authors themselves have not already acknowledged or addressed (e.g., the Discussion section already notes higher-order moment deviation).

## Suggestions

1. **Tighten theoretical framing.** Replace "provably distributed as N(0,I)" in Sections 3.3 and 6 with "provably matches the standard Gaussian up to third-order moments, with empirical evidence of statistical indistinguishability." This matches what is actually proved and eliminates the disconnect.
2. **Add a Gaussian Shading per-image-key comparison** (ideally in an appendix or extended Table 1/Figure 2) to show what happens when Gaussian Shading operates in its intended lossless mode. This would strengthen the empirical comparison.
3. **Qualify the claim about lossy vs. lossless watermarking** in Section 3.1 to reference the specific adversarial attack tested.

## Score and Decision

**Round 1 bracket (bracketing):** Weak anchors (avg ~3.0-3.2, all withdrawn/reject) vs. middle anchors (avg 4.4-6.5, mix of reject and accept) vs. strong anchors (avg 7.6-8.0, accept oral/spotlight). The paper is clearly above the weak anchors (which had fundamental methodology or presentation issues) and below the strong anchors (which are near-flawless works). This places the paper in the 4.5–7.0 range.

**Round 2 narrowing (within 4.5–7.0):** I retrieved and read the full reviews of:
- *O13fIFEB81.md* (avg 4.40, "Robust Watermarking for Diffusion Models" — withdrawn/reject): Had poor presentation, unclear methodology, and limited novelty. **Spherical Watermark is notably stronger** — clearer writing, more novel approach, better experiments.
- *HexshmBu0P.md* (avg 5.33, "A Recipe for Watermarking Diffusion Models" — reject): Limited novelty, PSNR below 30dB. **Spherical Watermark is stronger** — better theoretical grounding (even if overclaimed), better FID/quality, more thorough evaluation.
- *uzz3qAYy0D.md* (avg 6.00, "VideoShield" — accept poster): Moderate novelty (applying Gaussian Shading to video), some presentation issues. **Comparable in quality** — both have novel applications and solid experiments, but VideoShield faces more scrutiny on comparison baselines and has fewer theoretical overclaim issues.
- *f8S3aLm0Vp.md* (avg 6.50, "DIAGNOSIS" — accept poster): Novel problem framing, clean claims, thorough experiments. **Slightly weaker than DIAGNOSIS** — the theoretical overclaim issue is a clear flaw in Spherical Watermark that DIAGNOSIS does not have.

The paper sits between the 5.33 (reject) and 6.50 (accept poster) anchors. It is clearly stronger than the reject-level paper (clearer contribution, better experiments) but slightly below the 6.50 DIAGNOSIS paper due to the theoretical overclaim issue. I place it at **6.0**: a solid paper with a good practical contribution and strong experiments, held back by overstated theoretical guarantees that should be corrected. This is within the range of accepted papers at this venue.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>