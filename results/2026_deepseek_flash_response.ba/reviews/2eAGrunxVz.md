Now I have a solid calibration. Let me synthesize the final review.

**Bracket**: Round 1 placed the paper between 5.0 and 7.0. Round 2 anchors: PRC Watermark (6.50, Accept) — stronger theory, weaker empiricals; Shallow Diffuse (6.00, Reject) — comparable scope but less thorough evaluation; Hidden in the Noise (5.83, Accept) — similar approach, less thorough; SAT-LDM (5.50, Reject) — weaker overall. Spherical Watermark has stronger empirical evidence and computational efficiency than PRC Watermark, but its theoretical overclaim and confounded comparison pull it down. The paper sits around 5.5.

---

## Summary

This paper proposes Spherical Watermark, a lossless watermarking framework for diffusion models that converts binary watermark bits into noise matching a standard Gaussian prior through a three-step pipeline: binary embedding (mixing repeated watermark bits with random padding via an invertible matrix), spherical mapping (normalizing to the unit sphere, applying an orthogonal rotation, and scaling by a chi-square-distributed radius), and diffusion integration. The method eliminates per-image key management (a practical limitation of Gaussian Shading) and avoids the heavy cryptographic overhead of PRC Watermark. The core theoretical claim is that the watermarked noise preserves the target prior up to third-order moments via a spherical 3-design construction, supported by extensive experiments on undetectability, robustness, and computational efficiency.

## Strengths

- **Elegant spherical 3-design construction with theoretical backing**: The paper proves (Theorems 3.1–3.2, Lemma 3.3–3.4) that the watermarked noise matches the Gaussian prior up to third-order moments via a spherical 3-design argument. The chain of reasoning from 3-wise independent bitstream → spherical 3-design → orthogonal rotation → chi-square scaling is more principled than the heuristic designs in prior lossless schemes. This is a genuinely clever connection between combinatorial designs and Gaussian noise generation.

- **Strong empirical undetectability via learned classifiers (Figure 2)**: Two trained classifiers (latent-level MLP and image-level ResNet-18) cannot distinguish Spherical Watermark samples from unwatermarked ones (near 50% accuracy), while Tree-Ring (100%) and Gaussian Shading with fixed keys (97%) are trivially detectable. This directly tests the threat model an adversary would use.

- **Quantified computational efficiency advantage over PRC (Figure 4)**: Extraction is roughly four orders of magnitude faster than PRC Watermark (~10^−3.5 seconds vs. ~10^1.0 seconds), and the comparison isolates the transform time (excluding diffusion sampling/inversion). This is a concrete, measurable advantage attributable to algorithm design, not implementation.

- **Thorough ablation isolating module contributions (Figure 6(b)(c))**: Omitting binary embedding makes the latent noise trivially distinguishable; omitting spherical mapping causes robustness to collapse under brightness adjustment. This modular decomposition evidence is rare among watermarking papers and convincingly demonstrates that both components serve distinct, necessary roles.

- **Sustained accuracy across watermark capacities where PRC fails (Figure 6(a))**: Spherical Watermark maintains high detection rates as watermark length grows, while PRC Watermark's decoding deteriorates rapidly and fails entirely beyond l_m = 2000.

- **Robustness under adversarial attacks (Table 2)**: Achieves 99.83% TPR under WEvade attacks versus 95.38% for PRC Watermark and 6–27% for lossy methods, directly supporting the claim of superior robustness.

## Weaknesses

### Major

1. **Theoretical overclaim in the introduction and contributions list does not match what is proven.** The abstract correctly states "theoretically prove that the watermarked noise distribution preserves the target prior up to third-order moments, and empirically demonstrate that it is statistically indistinguishable." However, the introduction (line 26) says "prove that the final noise is statistically indistinguishable from standard Gaussian noise," and the contributions list (line 28) similarly says "the watermarked noise distribution is statistically indistinguishable from a standard multivariate normal distribution." The theory section itself is more careful — it uses "≈" in Lemma 3.4 and acknowledges higher-order deviations in the Limitations — but the front-matter claims go beyond what the spherical 3-design argument can support. A 3-moment match is meaningfully weaker than the "statistical indistinguishability" that Lemma 3.4's converse would require (uniform distribution on the sphere, then chi-square scaling). This gap between headline claims and actual proof is a significant issue for a venue like ICLR that values theoretical rigor. The paper's genuine contribution — a 3-moment match with strong empirical evidence — does not need inflated claims to be impressive. (Verified: Introduction ln 26, Contributions ln 28; compare with Section 3.3's use of "≈" and Limitations Section.)

2. **Gaussian Shading detectability comparison confounds two separate factors.** The paper states (Section 4.1) "Note that with fixed keys, Gaussian Shading no longer achieves true losslessness," then uses Figure 2 to show Gaussian Shading (with fixed keys) is detectable at 97% accuracy while Spherical Watermark is not. This comparison simultaneously varies two factors: (a) the watermarking construction (spherical mapping vs. stream-cipher sampling), and (b) key management (fixed key vs. per-image key). The detectability gap is then attributed to the method's design, but it may partially reflect the degraded configuration Gaussian Shading was evaluated in. A fair comparison would evaluate Gaussian Shading in both its native (lossless, per-image key) configuration and the fixed-key configuration, then separate the detectability and key-management axes. As presented, the detectability comparison overstates the method's advantage. (Verified: Section 4.1 "Note that with fixed keys...", Figure 2.)

### Minor

1. **Gap between "set is a spherical 3-design" and uniform distribution over the sphere required by Lemma 3.4.** Theorem 3.2 proves the *set* of possible z^(2) values (vertices of the hypercube projected to the unit sphere) is a spherical 3-design. Lemma 3.4 requires that the *distribution* of z^(3) be uniform on the sphere. A spherical 3-design guarantees the set matches uniform averages up to degree 3, but the paper does not characterize the sampling distribution over this set. Three-wise independence of z^(1) (Theorem 3.1) does not guarantee uniform distribution over all 2^{l_x} possible strings — it guarantees only that every 3-tuple of coordinates is independent. This is a subtle gap in the theoretical chain, though the empirical evidence supports practical indistinguishability. (Verified from Theorem 3.1, Theorem 3.2, Lemma 3.4.)

2. **FID comparisons are not strongly discriminating.** In Table 1, most methods (including lossy ones like DwtDct) produce FIDs within the 1-sigma error bars of the original. For example, on SD v2.1/COCO: Original 46.81 ± 1.06, DwtDct 46.98 ± 1.01, PRC 46.75 ± 1.07, Ours 46.81 ± 1.10. The claim that "only PRC Watermark and our method match the original in FID" is technically true (Ours is closest), but the discriminating power of FID at these error levels is weak. The paper's undetectability case rests primarily on the classifier experiments, which are stronger evidence.

### Trivial

- "Encryption-free" is slightly overstated. The method uses a fixed secret signature K = {T, C} (a fixed key), which is simpler than per-image key management but is not literally encryption-free. "Key-management-free" or "per-image encryption-free" would be more precise.

## Nice-to-Haves

- **Additional statistical tests for undetectability**: The paper relies solely on trained classifiers (MLP, ResNet-18) and FID. Adding standard two-sample tests (e.g., MMD, energy distance) or higher-moment comparisons (kurtosis, fourth-order cross-moments) would strengthen the empirical case, especially given the theoretical gap at higher-order moments. While not required (classifier-based evaluation is standard in the field), these would be a valuable addition given the strength of the claim.

- **Characterize the sampling distribution over the spherical 3-design set**: A brief analysis of whether the 3-wise independent construction yields a distribution close to uniform over the hypercube vertices would help close the theoretical gap noted in Minor weakness 1.

## Removed Points

These points from the inputs are excluded with justification:

- **"Weak tests for undetectability (critic wanted MMD, energy distance, etc.)"**: Moved to Nice-to-Have. Classifier-based detection is standard in the watermarking literature; the paper uses two distinct classifier architectures (MLP and ResNet-18) and FID, which is a reasonable evaluation suite. The critic's demand for additional tests is not standard practice.

- **"Inversion error analysis insufficient"**: Removed. Table 5 already provides an extensive ablation across varying generation/inversion timestep combinations, showing extraction accuracy above 99.9% in most settings. The critic's concern about rounding error from imperfect inversion is addressed by the N-repetition majority voting the paper describes.

- **"Missing comparison with Gaussian Shading in native configuration"**: This is already covered in the Major weakness about the confounded comparison. The critic's suggestion to add this comparison is valid; restating it as a separate weakness would be redundant.

- **Formatting/notation nitpicks**: Removed per instructions (parser artifacts).

- **Strength Finder generic strengths**: Removed claims like "addresses an important problem" or "well-organized related work" as generic. Keep only concrete, evidence-grounded strengths.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

- **Recalibrate the theoretical claims in the introduction and contributions list.** Replace "prove that the final noise is statistically indistinguishable from standard Gaussian noise" with language matching what is actually proven: "prove that the watermarked noise matches the target prior up to third-order moments via a spherical 3-design, and empirically demonstrate practical indistinguishability through classifier-based tests." The current framing overpromises relative to the theory, and fixing this would remove the most serious weakness.

- **Add a detectability comparison with Gaussian Shading in its native (per-image key) configuration.** Report this alongside the fixed-key comparison and discuss the key-management overhead separately. This would cleanly separate the method's detectability advantage from its key-management advantage.

- **Consider adding a brief discussion of the sampling distribution over the spherical 3-design set.** Clarify that 3-wise independence of z^(1) does not guarantee uniform distribution over all binary strings, and discuss what this implies (and does not imply) for the theoretical guarantee.

- **Minor:** Replace "encryption-free" with a more precise phrase such as "per-image encryption-free" or "key-management-free" to avoid confusion.

## Score and Decision

All anchors considered across both rounds:

| Path | Avg Score | Round | Comparison to This Paper |
|------|-----------|-------|--------------------------|
| fkNsgI1nye.md | 3.00 | R1 | Much weaker (privacy-preserving inference, not watermarking) |
| jbfDg4DgAk.md | 3.00 | R1 | Much weaker (LLM sparse watermark, different domain) |
| hYEV8QmaOt.md | 3.40 | R1 | Much weaker (image anti-forensics) |
| T0ebbDO60R.md | 3.75 | R2 | Weaker (super-resolution based, training-free) |
| HexshmBu0P.md | 5.33 | R1/R2 | Weaker (recipe paper, less theoretical depth, less thorough evaluation) |
| ETFfXGM3e4.md | 5.50 | R1/R2 | Comparable (training-based, different approach; similar score band) |
| uHdf9F1tY4.md | 5.50 | R2 | Comparable (data copyright watermark, different scope) |
| ll2nz6qwRG.md | 5.83 | R2 | Comparable-to-slightly-weaker (similar scope, less thorough evaluation) |
| uzz3qAYy0D.md | 5.83 | R2 | Comparable (video watermarking, different modality) |
| 1IwoEFyErz.md | 6.00 | R1/R2 | Comparable (robust watermarking, less theoretical analysis) |
| LdIlnsePNt.md | 6.00 | R2 | Different domain (LLM watermark), comparable rigor |
| f8S3aLm0Vp.md | 6.50 | R1 | Different problem (detecting unauthorized data usage, not watermarking) |
| **jlhBFm7T2J.md** | **6.50** | **R1/R2** | **PRC Watermark — stronger theoretical guarantee, weaker empirical results** |
| UchRjcf4z7.md | 6.50 | R2 | Different problem (attack paper, not watermarking method) |

**Round 1 bracket**: [5.0, 7.0], determined by clear separation from weak anchors (<3.5) and strong anchors (>7.5).

**Round 2 narrowing**: The PRC Watermark paper (6.50) has a stronger cryptographic guarantee but weaker empirical results (robustness, efficiency). Spherical Watermark has stronger empiricals but a notable theoretical overclaim. Among anchors in the 5.5–6.0 range (SAT-LDM, Hidden in the Noise, Shallow Diffuse), Spherical Watermark's evaluation is more thorough, but its overclaim in the introduction makes it a weaker submission than its empirical core alone would suggest. The paper sits between 5.0 and 6.0, closer to 5.5 when considering that the most critical issues (overclaim, confounded comparison) are cleanly addressable but currently detract from the presentation at a top venue.

The strongest comparable anchor — the PRC Watermark paper at 6.50 — was accepted with reviewers noting it had the "first undetectable watermark" as a novelty advantage and a cleaner cryptographic guarantee. Spherical Watermark has a different kind of contribution (elegant construction, practical efficiency) but its weaker theoretical framing and overclaim place it below that anchor. Among the 5.5–6.0 anchors, Spherical Watermark has more empirical depth than most, which pulls it toward the upper end of that band, but the overclaim issue is non-trivial for ICLR's standards.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>