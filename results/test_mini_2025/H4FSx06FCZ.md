Now I have enough calibration data. Let me produce the final consolidated review.

## Summary

This paper proposes SecureGS, a steganography framework for 3D Gaussian Splatting that embeds hidden 3D objects, images, or bits into a 3DGS scene. It builds on Scaffold-GS and introduces two key components: (1) a hybrid decoupled Gaussian encryption representation that stores hidden Gaussian points *implicitly* via private MLPs rather than as explicit attributes in the point cloud file, achieving file-format security; and (2) a region-aware density optimization (RDO) strategy that adaptively grows original-scene anchor points at hidden-object locations, visually concealing the hidden geometry in the visualized point cloud. Experiments show improvements over GS-Hider in rendering fidelity, speed, storage, and geometric security.

## Strengths

1. **Hybrid decoupled Gaussian encryption achieves file-format security without fidelity loss.** The method stores hidden Gaussian offsets implicitly via a private MLP (Eq. 4–5) rather than as explicit attributes, so the published point cloud has the same structure as standard Scaffold-GS. This directly addresses the format-security gap of prior methods. Table 1 shows SecureGS outperforms GS-Hider by 1.16 dB in original-scene PSNR and 1.66 dB in hidden-object PSNR while using 43% less storage and running ~2.7× faster.

2. **Region-aware density optimization (RDO) meaningfully improves geometric structure security.** Section 3.4 diagnoses how GS-Hider and SecureGS without RDO expose hidden geometry in the point cloud. RDO adaptively lowers the splitting threshold inside the hidden-object bounding box, forcing original-scene anchor points to cover hidden ones. Figure 7 provides visual evidence that SecureGS with RDO produces point clouds visually indistinguishable from unmodified Scaffold-GS, while GS-Hider and SecureGS w/o RDO reveal the hidden object's shape.

3. **Decoupled rendering enables scene-level and object-level extraction — a capability absent from prior methods.** SecureGS can extract hidden 3D objects with or without background (object-level PSNR = 38.21 dB, Table 1). GS-Hider and 3DGS+StegaNeRF can only hide the object together with the original scene's background because they decode a complete RGB image. This is a practical advantage for applications needing the hidden object in isolation.

4. **100% bit-hiding accuracy with far better rendering quality than NeRF baselines.** Table 3 reports 100.00% bit accuracy on Blender dataset vs. 92.69% (NeRFProtector) and 62.15% (CopyRNeRF), while also achieving the best PSNR (33.84 dB). This is achieved by decoding bits directly from anchor-point features, enabling cross-validation across voxels.

5. **Strong robustness to random anchor-point pruning.** Table 2 shows that even after randomly pruning 20% of anchor points, hidden-message PSNR remains 33.90 dB (SSIM 0.981) and original-scene PSNR stays above 24.96 dB. This has practical value for 3D asset transmission where point-cloud degradation may occur.

## Weaknesses

### Fatal
None.

### Major

1. **Security evaluation is entirely qualitative — no quantitative security metric is provided.** The paper's title and core contribution emphasize security, yet the evidence for geometric-structure security is limited to three visual comparisons in Figure 7. There is no quantitative measure: no detectability experiment (e.g., can a classifier distinguish SecureGS containers from normal Scaffold-GS containers?), no statistical analysis of point-cloud feature distances, and no systematic attack model. This is a significant gap for a paper whose headline claim is security. The file-format security aspect is well-supported (same attribute set as Scaffold-GS), but the geometric security claim would be substantially strengthened by even a simple quantitative measure (e.g., Chamfer distance between normal and SecureGS point clouds, or a binary classification experiment).

### Minor

1. **Missing comparison with 3D-GSW for bit-hiding.** The paper states in Section 4.1 that "there is still no 3DGS steganography work for bit hiding available," yet 3D-GSW (Jang et al., 2024b) is cited in the related work as a 3DGS watermarking method that embeds and extracts bit messages. While watermarking and steganography have different threat models, a comparison (or at minimum a discussion of why comparison is not straightforward) would strengthen the evaluation. The 100% bit-accuracy result would be more impactful if contextualized against 3D-GSW's decoding robustness.

2. **Some fidelity/storage/speed advantages are inherited from the Scaffold-GS backbone rather than steganography-specific components.** Table 1 shows Scaffold-GS itself achieves 27.62 dB original-scene PSNR, 142.91 FPS, and 161 MB. SecureGS (scene-level) achieves 27.75 dB, 131.71 FPS, and 267 MB — close to the baseline. The paper's improvements over GS-Hider (which uses standard 3DGS) are real, but the magnitude of improvement in storage and FPS partly reflects the backbone choice rather than the steganography modules. An ablation isolating the backbone effect would clarify this.

3. **No standard deviations or confidence intervals reported in main tables.** Results vary across scenes (e.g., bicycle PSNR ranges from 25.01 to 25.33 across methods), and per-scene numbers are provided, but average values without variance make it difficult to assess whether improvements are systematic. Reporting repeated-run statistics is standard practice.

4. **Robustness evaluation tests only random pruning.** Section 4.4 tests only random anchor-point pruning. Real-world adversaries may apply more systematic attacks (e.g., subsampling, smoothing, re-optimization attacks). The claim that SecureGS is "robust enough to the degradation of point clouds" is somewhat overstated given the narrow attack test.

### Trivial

1. **Inconsistent naming: "GS-Header" appears in Table 1 and Figure 1 caption instead of "GS-Hider".** The paper uses "GS-Hider" correctly in most places but "GS-Header" in the table and figure captions. Should be corrected for consistency.

2. **Table 1 column header "KL." should be "KI." (kitchen).** The column label for kitchen is "KL." in Table 5 while "KI." in Table 1.

## Nice-to-Haves

- A binary classification experiment (can an adversary distinguish SecureGS containers from normal Scaffold-GS point clouds?) would directly quantify the geometric security claim.
- An ablation of the RDO threshold parameter (r_down) showing the trade-off between hidden-object PSNR and security would give practitioners practical guidance.
- Testing with hidden objects of larger spatial extent or finer geometric detail would strengthen the generality claim.

## Removed Points

- **"Missing related work on X":** The paper adequately covers relevant prior work (GS-Hider, GaussianStego, 3D-GSW, NeRF watermarking methods) in Section 2.2. Criticisms about missing references are unfounded or pertain to methods outside the paper's scope.
- **"Figure 1 caption OCR duplication":** This is a PDF-parser artifact, not an author error.
- **"The 3DGS+StegaNeRF baseline is weak":** The paper acknowledges this is a variant adapted from StegaNeRF and it serves to show why 2D-view-decoding fails for 3DGS. This is a valid baseline for illustrating a limitation, not a weakness of the paper.
- **Generic "evaluation lacks rigor" / "could be confounders" claims without specific anchors:** Removed as speculation without concrete evidence.

## Novel Insights

The harsh critic's observation that the Scaffold-GS inheritance confounds some fidelity/speed claims is well-taken and provides a useful perspective for reading the paper: the paper's main contribution is the combination of a security-aware representation (implicit vs. explicit hidden Gaussians) with a security-aware density optimization (RDO), and these contributions are evaluated against GS-Hider which uses a different (and weaker) backbone. A cleaner ablation would be "GS-Hider modified to use Scaffold-GS's architecture" — but this would be a significant engineering effort and is not standard practice for conference papers. The paper's current evaluation, comparing to GS-Hider and showing that SecureGS approaches Scaffold-GS's performance while adding security, is reasonable.

## Suggestions

1. **Add a quantitative security experiment.** At minimum, compute the Chamfer distance between the point clouds of SecureGS containers and normal Scaffold-GS containers, and show that SecureGS containers are closer to normal than GS-Hider containers. A binary-classification detectability experiment would be even stronger.
2. **Compare against or discuss 3D-GSW for the bit-hiding task**, even if the comparison is not one-to-one due to different threat models.
3. **Report standard deviations** across multiple runs or random seeds for main results.
4. **Extend robustness evaluation** beyond random pruning to include at least one systematic attack (e.g., random subsampling, smoothing).
5. **Fix the "GS-Header" → "GS-Hider" typo** in Table 1 and Figure 1 captions.

## Score and Decision

### Calibration Anchors

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| WATER-GS (H48OMCCiI7) | 4.00 | R1, R2 | Similar topic (3DGS watermarking); SecureGS has stronger novelty and better comparison with prior work |
| 3DGS-Det (9SmukfhJoF) | 5.25 | R2 | Different task; comparable evaluation thoroughness |
| MVGS (X7XgNI0Eym) | 4.75 | R2 | Different task; SecureGS has stronger empirical results |
| DirectTriGS (FL6112vyty) | 5.00 | R2 | Different task; comparable contribution scope |
| 3D Vision-Language GS (SSE9myD9SG) | 6.40 | R2 | Different task; comparable evaluation quality |
| Poison-splat (ExrEw8cVlU) | 7.50 | R2 | Similar security focus; Poison-splat has quantitative evaluation of its core claim |
| Lightweight Predictive 3DGS (PbheqxnO1e) | 7.00 | R1, R2 | Stronger evaluation, accepted poster |
| DreamGaussian (UyNXMqnN3c) | 8.50 | R1 | Oral-level work, far stronger contribution |

**Round-1 bracket:** The paper clearly sits above the 3.5-and-below band (avg scores 2.5–3.4 for unrelated or weak papers) and below the 7.5+ band (oral/spotlight-level work with comprehensive evaluation). The plausible range is between 4.0 and 7.5.

**Round-2 narrowing:** Within (3.5, 6.5), the strongest anchor is 3D Vision-Language GS at 6.40 (accepted poster). Within (6.5, 8.5), Poison-splat at 7.50 (accepted spotlight) serves as an upper bound. SecureGS has a clearer technical contribution than WATER-GS (4.00) but a weaker security evaluation than Poison-splat (7.50), which quantitatively validated its core security claim. Relative to 3D Vision-Language GS (6.40), SecureGS has a more significant evaluation gap (qualitative-only central claim) but comparable methodological novelty. I place the paper slightly below 6.40 due to the qualitative-only security evaluation gap for a paper whose title and central contribution is security.

**Final score:** 5.5 — a solid paper with real contributions held back by a significant evaluation gap for its core claim. The method is sound and improvements over GS-Hider are well-demonstrated, but the security evaluation needs quantitative evidence to fully support the paper's thesis.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>