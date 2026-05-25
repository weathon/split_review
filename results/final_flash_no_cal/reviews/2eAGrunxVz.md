Now I have a thorough understanding of the paper. Let me construct the final consolidated review.

## Summary

This paper proposes Spherical Watermark, a lossless watermarking framework for diffusion models. It embeds binary watermarks into the initial Gaussian noise input without modifying the pretrained model, using a binary embedding matrix followed by spherical mapping (normalize → orthogonal rotation → chi-square scaling). The method eliminates per-image key storage (unlike Gaussian Shading) and avoids expensive cryptographic decoding (unlike PRC-based approaches). Theoretical analysis shows the watermarked noise matches a standard Gaussian up to third-order moments (spherical 3-design), and extensive experiments on Stable Diffusion v1.5/v2.1 across multiple datasets demonstrate competitive undetectability, strong robustness under attacks, dramatically lower computational overhead, and scalability to large watermark capacities.

## Strengths

- **Method-level innovation with clear practical advantages.** The paper's core technical contribution — replacing per-image key management with a fixed secret bijective transform plus fresh random padding — is practically significant. It solves the key-storage bottleneck of Gaussian Shading while avoiding the cryptographic complexity of PRC, and Figure 4 confirms ~4 orders of magnitude faster extraction than PRC. This is a crisp, well-motivated advance.

- **Strong empirical evidence for undetectability.** Table 1 shows that the method's FID values (e.g., 48.1224 vs. 48.1256 on COCO SD v1.5) are essentially identical to unwatermarked baselines, and Figure 2 demonstrates that both latent-level MLP classifiers and image-level ResNet-18 classifiers achieve chance-level accuracy (~50%) for the proposed method, matching the performance of PRC Watermark while surpassing Gaussian Shading and Tree-Ring which are easily detected.

- **Superior robustness under adversarial attacks.** In Table 2, Spherical Watermark achieves 98.12% ACC and 99.83% TPR under WEvade adversarial attacks, outperforming PRC Watermark (97.69%, 95.38%) and surpassing lossy methods by a wide margin. Figure 5 shows this advantage is consistent across 8 different attack types, often widening at higher distortion levels.

- **Ablation studies that actually verify design choices.** Figure 6(b) shows that removing the binary embedding module makes the latent noise trivially detectable; Figure 6(c) shows that removing the spherical mapping module crashes robustness under brightness adjustment. These controlled experiments cleanly isolate the contribution of each module.

- **Comprehensive evaluation scope.** The method is tested on two datasets (COCO, SDP), two model versions (SD v1.5, v2.1), multiple ODE solvers (DDIM, PNDM, DPM-Solver++), and varying timesteps, with consistent results. Table 4 and 5 confirm the method is robust to choices of solver and sampling schedule.

## Weaknesses

### Fatal

None.

### Major

- **Theoretical framing overclaims relative to what is proven.** The problem formulation (Section 3.1, Eq. 2–3) defines undetectability as computational indistinguishability with negligible error `negl(ρ)` — cryptographic language that implies a formal security guarantee against any polynomial-time adversary. What the paper actually proves (Section 3.3) is that the watermarked noise matches a standard Gaussian only up to **third-order moments** (via spherical 3-design). The paper acknowledges in the Limitations that "higher-order moments may deviate from the true prior," but this does not bridge the gap between the problem statement and what is theoretically established. The empirical evidence (classifier at chance, FID matching) is strong, but the text should align the theoretical claim with what is actually proven — e.g., "statistically indistinguishable up to third-order moments" or "empirically indistinguishable with moment guarantees." This is a framing issue, not an invalidation, but it needs to be corrected.

- **Multi-image undetectability is not addressed.** The paper evaluates undetectability for a single noise sample or image, but in practice a user generates many images with the same fixed watermark. Since the watermark bits are constant while random padding is fresh per image, an adversary collecting multiple watermarked noise vectors (or images) from the same user could potentially average out the padding variation and detect a residual signal correlated with the watermark. This scenario is neither analyzed, discussed, nor experimentally evaluated. While single-image undetectability is a necessary condition, the practical deployment scenario demands at least a discussion of whether the method remains undetectable under multi-sample attacks.

### Minor

- **PRC speedup comparison lacks implementation specifics.** The paper reports ~4 orders of magnitude faster extraction than PRC Watermark (Figure 4) but does not specify which PRC code parameters (code rate, block length, belief-propagation iterations) were used. The qualitative advantage is clear, but the exact factor depends on these choices, and readers cannot calibrate the claim without knowing them. The paper states "Unless noted otherwise, baselines use their default settings," but does not state what those defaults are for PRC.

- **Gaussian Shading comparison is asymmetric.** The paper compares against Gaussian Shading with fixed keys (which breaks its losslessness guarantee) rather than in its intended per-image-key mode. While the paper correctly notes this limitation, adding a row with per-image Gaussian Shading would provide a meaningful upper bound on robustness and clarify the trade-off the fixed-key approach makes.

### Trivial

- Eq. (6) contains a typo: `l_m = N × l_m` is mathematically inconsistent (should be something like `l_m' = N × l_m` or similar notation for the expanded dimension).
- Figure 2 caption refers to "True Ring" instead of "Tree-Ring" (the actual method name from Wen et al. 2023).

## Nice-to-Haves

- Measuring fourth-order statistics (e.g., marginal kurtosis) to quantify the empirical deviation from a true Gaussian, since the theory only guarantees up to third-order moments.
- A brief discussion of key management/revocation (what happens if the fixed secret signature `{T, C}` is leaked).
- A more systematic study of how DDIM inversion quality (reconstruction error) affects extraction accuracy, beyond the already-provided solver and timestep ablations.
- Sharpening the theoretical framing as noted in the Major weaknesses — this would be a straightforward but important improvement.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Harsh Critic Point 2 (3-wise independence proof concern based on missing appendix):** The critic flags that "because the appendix is not available for review, I must flag this as a potential structural weakness." Per the evaluation guidelines, criticisms about missing appendix content are removed — the parser strips appendix sections from all papers, and the proofs exist in the original submission. While the technical question about collisions across watermark bits is reasonable, the full proof is present in Appendix C of the original paper and cannot be evaluated here. This point is therefore removed rather than retained as a weakness.
- **Various section-by-section nitpicks:** Notes about the ODE solve direction being correct, about Table 1 FID clarification being needed, and about Figure 6(d) parameter specification are either confirming correctness or demanding detail that is already reasonably clear; these are removed.
- **Strength Finder's "Rigorous theoretical grounding" claim:** Taken at face value this overstates what is proven (moments up to order 3 ≠ "formal guarantee stronger than prior lossless schemes"), but the strength is better captured by the empirical results listed in the Strengths section above.

## Novel Insights

None beyond the paper's own contributions. The review process surfaces the gap between the cryptographic-style problem formulation and the actual moment-matching proof, which is worth the authors' attention, but this is a corrective observation rather than a novel insight about the method.

## Suggestions

1. **Revise the theoretical claims** in the problem formulation (Section 3.1) and abstract to match what is actually proven. Replace "computationally indistinguishable" / "negl(ρ)" language with phrasing like "statistically indistinguishable up to third-order moments" or "empirically indistinguishable with moment-matching guarantees." The Limitations section already partially does this; the front matter should be consistent.

2. **Add an analysis or experiment on multi-image undetectability.** Generate multiple images per user with the same watermark and test whether a classifier can distinguish sets of watermarked images from unwatermarked ones, or provide a theoretical argument for why averaging across images does not leak detectable patterns.

3. **Specify the PRC parameters** used for the computational comparison (code rate, block length, belief-propagation iterations) so readers can calibrate the speedup claim.

## Score and Decision

The paper proposes a clean, practically-motivated lossless watermarking scheme that achieves meaningful advantages over prior work (no per-image key storage, dramatically faster extraction, competitive robustness). The empirical evaluation is thorough and supports the core claims. The major weaknesses — theoretical overclaiming and the unaddressed multi-image scenario — are significant but addressable; neither invalidates the method's practical value. The work represents a solid contribution to the field of diffusion model watermarking.

**MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>**