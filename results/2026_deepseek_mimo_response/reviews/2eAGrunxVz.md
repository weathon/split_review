Now I have all the data needed. Let me write the final review.

## Summary

This paper introduces Spherical Watermark, a lossless and encryption-free watermarking framework for diffusion models that converts binary watermarks into near-Gaussian noise via a pipeline of binary embedding (repetition + random padding mixing), unit-sphere projection, orthogonal rotation, and chi-square scaling. The method eliminates per-image key storage overhead required by Gaussian Shading, achieves ~4 orders of magnitude faster extraction than PRC Watermark, and demonstrates strong undetectability and adversarial robustness across comprehensive experiments on Stable Diffusion v1.5 and v2.1.

## Strengths

- **Novel binary-to-Gaussian mapping via spherical 3-designs.** The core contribution—projecting 3-wise independent binary codes onto the unit sphere, applying orthogonal rotation, and scaling by chi-square radius (Eqs. 9-10, Section 3.2)—is a technically elegant, principled approach to embedding binary watermarks in the Gaussian prior without cryptographic machinery. The proof chain through Theorems 3.1-3.2 and Lemmas 3.3-3.4 establishes a solid theoretical foundation for moment matching up to degree 3.

- **Empirical undetectability validated at multiple levels.** Table 1 shows FID matching unwatermarked output (48.1224 vs 48.1256 on COCO/SD v1.5). Figure 2 shows trained classifiers (MLP at latent level, ResNet-18 at image level) converge to ~50% chance accuracy for the proposed method and PRC Watermark, while Gaussian Shading (with fixed keys) is 97% detectable and Tree-Ring is 100% detectable at the latent level.

- **~4 orders of magnitude faster extraction than PRC Watermark.** Figure 4 shows extraction time of ~10⁻³·⁵s vs ~10¹·⁰s for PRC Watermark, directly demonstrating the computational advantage of avoiding belief-propagation decoding.

- **Superior adversarial robustness over all baselines.** Table 2 shows 98.12% ACC and 99.83% TPR under WEvade adversarial attacks, versus PRC Watermark's 97.69% and 95.38%. Lossy methods degrade sharply to 16–27% TPR. The paper provides a principled explanation (Appendix E): lossless embedding prevents adversaries from training classifiers to detect and then attack the watermark.

- **Graceful scaling with watermark capacity.** Figure 6(a) shows PRC Watermark fails entirely beyond l_m = 2000 under JPEG-70 compression, while the proposed method maintains high accuracy across all tested capacities—a concrete practical advantage for high-capacity watermarking.

- **Comprehensive ablation studies.** Figures 6(b,c) isolate module contributions (removing binary embedding makes noise trivially detectable; removing spherical mapping degrades robustness). Table 3 varies sparsity s and repetition N with expected monotonic degradation. Tables 4-5 test three ODE solvers and various generation/inversion timestep combinations, all showing stable results (≥99.85%).

## Weaknesses

### Fatal

None.

### Major

- **Theoretical overclaim: proofs show third-order moment matching, not statistical indistinguishability.** The introduction (line 26) states "we prove that the final noise is statistically indistinguishable from standard Gaussian noise," and Section 3.3 (line 157) claims "the final latent code **z**_w is distributed as N(**0**, **I**_{l_x})." However, the actual theorems only establish that **z**⁽²⁾ forms a spherical 3-design (Theorem 3.2), which guarantees matching up to third-order moments—not full distributional equivalence to Gaussian. The Gaussian is fully characterized by its first two moments, but matching up to third-order moments does not imply Gaussianity, and there is no formal reduction from 3-design to computational indistinguishability as defined in Eq. 2 (which requires |Pr[A(**z**_w)=1] − Pr[A(**z**)=1]| ≤ negl(ρ)). The abstract is more careful ("preserves the target prior up to third-order moments, and empirically demonstrate that it is statistically indistinguishable"), and the discussion (line 332) acknowledges "higher-order moments may deviate from the true prior." But the introduction and Section 3.3 make stronger claims that the proofs do not support. This matters because the paper positions itself alongside Gaussian Shading, which provides an *exact* distributional match.

- **Gaussian Shading comparison under degraded fixed-key mode only.** The paper runs all latent-based methods with "five fixed keys" (line 193) and notes "with fixed keys, Gaussian Shading no longer achieves true losslessness." Table 1 shows Gaussian Shading at FID 50.70 vs 48.12, and Figure 2 shows it is 97% detectable at the latent level. However, Gaussian Shading was designed to use unique per-image keys for provable losslessness. While the paper's argument that per-image keys are impractical due to storage overhead is valid, the reader cannot determine whether the proposed method's advantages extend beyond the fixed-key setting. Including Gaussian Shading with per-image keys as an upper-bound reference (at least for FID and undetectability) would clarify whether the contribution is "better lossless method" or "better method that avoids key management." The comparison with PRC Watermark (which also uses fixed keys) is convincing on its own.

### Minor

- **No error analysis for extraction rounding step.** Equation 13 (line 149) uses round() to recover binary bits after applying **C**⁻¹ to the estimated latent. This works because the chi-square-scaled radius r concentrates around √l_x, making r/√l_x ≈ 1, but no error probability bound is provided as a function of l_x. A brief analysis would clarify the minimum latent dimensionality required and strengthen the method description.

- **Storage cost of the fixed signature K = {T, C} is not stated.** The paper emphasizes eliminating per-image key storage, but the fixed signature consists of a 16384 × 16384 sparse binary matrix **T** and an l_c × l_c orthogonal matrix **C**. Explicitly stating the storage requirements would allow fair comparison with Gaussian Shading's per-image key overhead.

- **Notation error in Eq. 6** (line 84): "l_m = N × l_m" should be "l_{Nm} = N × l_m" to denote the total bits after repetition. The paper uses l_{Nm} correctly elsewhere (lines 153, 191).

### Trivial

None.

## Nice-to-Haves

- Security analysis under known-method attacks: the adversary knows the binary embedding + spherical mapping structure but not the specific secret K = {T, C}. Given that **T** is a fixed sparse binary matrix, multiple API queries (seeing many watermarked outputs) might potentially leak structure. Even a brief threat-model discussion would strengthen the security analysis.
- Discussion of generalization beyond Stable Diffusion to other generative models with Gaussian priors (mentioned briefly in line 332 but could be expanded).
- Analysis of why lossless embedding confers adversarial robustness could be formalized more rigorously.

## Removed Points

These points are flagged to be removed, treat them with caution:
- Formatting/typography artifacts from PDF parsing (typos, spacing, broken characters) — these are parser issues, not paper problems.
- Harsh critic's concern about the extraction rounding relying on chi-square concentration — this is real and kept as a minor point, but the method works in practice with l_x = 16384.

## Novel Insights

The paper's most novel insight is the connection between spherical t-designs and watermarking: by constructing a binary code with 3-wise independence properties (Theorem 3.1) and projecting onto the unit sphere, the authors obtain a spherical 3-design whose orthogonal rotation and chi-square scaling produces near-Gaussian noise. This eliminates the need for cryptographic primitives entirely—a genuinely different design philosophy from both Gaussian Shading (stream cipher) and PRC Watermark (error-correcting codes). The observation that lossless embedding provides inherent robustness against adversarial attacks (because adversaries cannot train classifiers to detect the watermark) is also insightful and well-supported by both the theoretical argument (Appendix E) and experimental evidence (Table 2).

## Suggestions

- Tighten theoretical claims in the introduction and Section 3.3 to match the abstract's more precise phrasing: "preserves the target prior up to third-order moments, with empirical indistinguishability confirmed by trained classifiers and FID."
- Add Gaussian Shading with per-image keys as a reference point for FID and undetectability comparisons to clarify the contribution's scope.
- Include a brief error probability analysis for the rounding-based extraction step (Eq. 13) as a function of l_x.
- State the storage cost of the fixed signature K = {T, C} explicitly.
- Fix the notation error in Eq. 6 (l_m = N × l_m → l_{Nm} = N × l_m).

## Reporting: Calibration Anchors

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| Secure Diffusion Model | fkNsgI1nye.md | 3.00 | 1 | Much weaker; tangentially related |
| Sample what you can't compress | vK8C37eHXM.md | 3.20 | 1 | Much weaker; different domain |
| Sparse Watermark LLM | jbfDg4DgAk.md | 3.00 | 1 | Weaker; LLM watermarking, limited scope |
| Image Anti-Forensics | hYEV8QmaOt.md | 3.40 | 1 | Much weaker; different problem |
| **PRC Watermark** | jlhBFm7T2J.md | **6.50** | 1 | **Direct competitor; paper outperforms in speed, adversarial robustness, capacity scaling** |
| Recipe for Watermarking DMs | HexshmBu0P.md | 5.33 | 1 | Weaker; recipe/framework paper, no novel method |
| SuperMark | T0ebbDO60R.md | 3.75 | 1 | Weaker; training-free but limited |
| **WIND/Hidden in the Noise** | ll2nz6qwRG.md | **5.83** | 1/2 | Weaker; builds on Tree-Ring, less theoretical depth |
| **Shallow Diffuse** | 1IwoEFyErz.md | **6.00** | 2 | Weaker; limited originality, poor presentation, DDIM-dependent |
| VideoShield | uzz3qAYy0D.md | 5.83 | 2 | Weaker; video-specific, limited evaluation |
| Watermark Removal via Regen | mDKxlfraAn.md | 6.40 | 2 | Different focus (attack paper), not directly comparable |
| **TabWak** | 71pur4y8gs.md | **7.20** | 2 | Comparable quality but different domain (tabular data); paper under review has stronger empirical evaluation in its domain |
| Lightweight Deep WM | j7b4mm7Ec9.md | 7.60 | 1/2 | Higher score but rejected; traditional deep watermarking, different paradigm |
| Targeted Attack | agHddsQhsL.md | 7.50 | 2 | Different topic (adversarial protection) |
| Water-Probe LLM | ujpAYpFDEA.md | 7.50 | 2 | Different topic (LLM watermark detection) |

**Round 1 bracket:** 6.0 – 7.5
**Round 2 narrowing:** 6.0 – 7.0 (clearly above Shallow Diffuse at 6.00, at or above PRC Watermark at 6.50, below TabWak at 7.20)
**Final score: 6.5** — The paper is at least as strong as its direct competitor PRC Watermark (6.50) with clear practical advantages (speed, adversarial robustness, capacity scaling, no key management), but theoretical overclaim and comparison fairness issues prevent it from scoring higher.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>