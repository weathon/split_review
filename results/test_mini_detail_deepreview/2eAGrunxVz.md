Now let me write the final consolidated review.

## Summary

The paper proposes Spherical Watermark, an encryption-free lossless watermarking framework for diffusion models. The method embeds binary watermarks into the Gaussian noise input of a diffusion model via three modules: (1) binary embedding (mixing repeated watermark bits with random padding via an invertible binary matrix), (2) spherical mapping (projecting the result onto the unit sphere, applying an orthogonal rotation, and scaling by a chi-square-distributed radius to reconstruct standard Gaussian noise), and (3) diffusion integration. The authors prove that watermarked noise matches the Gaussian prior up to third-order moments (spherical 3-design) and provide extensive empirical validation on Stable Diffusion, showing strong undetectability (FID within 0.01 of original, near-50% classifier accuracy), robustness (95%+ ACC under attacks), and computational efficiency (≈4 orders of magnitude faster extraction than PRC).

## Strengths

1. **Encryption-free lossless design eliminates per-image key storage.** Unlike Gaussian Shading (which requires a unique key+nonce per image) and PRC (which uses heavy cryptographic encoding/decoding), the proposed method uses a fixed Signature (T, C) — two matrices stored once. The computational efficiency results (Figure 4, ~4 orders of magnitude faster extraction than PRC) directly evidence this practical benefit.

2. **Strong empirical undetectability supported by multiple metrics.** The FID values in Table 1 are within 0.01 of the original unwatermarked distribution (e.g., 48.1224 vs. 48.1256 on COCO SD v1.5), matching only PRC in this regard while all other baselines show clear degradation. The classifier-based detection experiments (latent-level and image-level) additionally support the claim that the watermarked distribution is practically indistinguishable from standard Gaussian noise.

3. **Superior robustness across a wide range of attacks.** Under adversarial attacks (WEvade), Spherical Watermark achieves 98.12% ACC and 99.83% TPR, substantially outperforming lossy methods (RivaGAN: 52.31% ACC) and marginally surpassing the best lossless competitor (PRC: 97.69% ACC, 95.38% TPR). Post-processing robustness is also strong, with sustained high performance across eight attack types (Figure 5).

4. **Scalability to long watermarks.** Figure 6(a) shows that Spherical Watermark maintains near-perfect ACC under JPEG-70 compression as watermark length l_m increases from 512 to 4000, while PRC's accuracy collapses below 50% beyond l_m=2000. This is a practically important advantage for large-scale provenance tracking.

5. **Systematic ablation studies validate each module.** Figure 6(b) shows that omitting binary embedding makes latent noise detectable (classifier accuracy jumps well above 50%); Figure 6(c) shows robustness under brightness adjustment drops dramatically without spherical mapping. These results confirm the modular design rationale.

## Weaknesses

### Fatal
None.

### Major

1. **Mismatch between problem formulation and actual theoretical guarantee.** Equation (2) defines undetectability as *computational indistinguishability*: for any probabilistic polynomial-time adversary A, |Pr[A(z_w)=1] - Pr[A(z)=1]| ≤ negl(ρ). The theoretical analysis, however, only establishes that the watermarked noise matches the standard Gaussian up to *third-order moments* (via the spherical 3-design construction, Theorem 3.2 and Lemma 3.3). Moment matching to degree 3 does **not** imply computational indistinguishability — a distinguisher could exploit fourth- or higher-order statistics. The paper acknowledges this gap in Section 5 ("higher-order moments may deviate from the true prior"), but the problem formulation in Section 3.1 sets a cryptographic standard that the paper does not meet. This framing should be relaxed (e.g., to "moment matching to third order, with empirical support for practical indistinguishability") to honestly reflect the actual guarantee.

2. **Figure 2 does not visually present the proposed method's classifier results.** The figure caption only describes "True Ring" and "PRC watermark" (two methods). The text claims "our method remain[s] indistinguishable" but neither the plotted data nor numerical accuracy values for the proposed method are shown in this figure. While Table 1 (FID) and the text provide some support for undetectability, the primary undetectability figure — central to the paper's core claim — should include the proposed method's results alongside baselines. *(Note: this may be partly a parser artifact where the actual PDF figure contains more information than the extracted text describes; still, as presented in the parsed manuscript, the evidence is incomplete.)*

### Minor

1. **Gaussian Shading baseline uses fixed keys, weakening the comparison.** The paper acknowledges that "with fixed keys, Gaussian Shading no longer achieves true losslessness" (Section 4.1). The original Gaussian Shading uses per-image keys and is lossless. While comparing both methods under fixed-secret settings is a valid way to isolate the key-storage advantage, the narrative positions the method as superior to "lossless approaches" while comparing against a non-lossless variant. A fairer presentation would either (a) include the true lossless Gaussian Shading (with per-image keys) as a separate row in Table 2, noting the key-storage overhead as a separate practical dimension, or (b) more prominently caveat that the baseline is intentionally weakened.

2. **The FID reference distribution should be clarified.** Table 1's caption says "FID value for different watermarking methods" and the text says "measured against the unwatermarked output distribution." If FID is computed between two sets of synthetic images (watermarked vs. unwatermarked, both generated by the same model), the values (~48) are in a range typically associated with real-vs-synthetic FID rather than synthetic-vs-synthetic. The paper should explicitly state what the reference distribution is and whether standard FID interpretation applies.

3. **Computational efficiency comparison (Figure 4) measures only transform time, excluding diffusion inversion.** The paper transparently states this ("excluding any diffusion sampling or inversion procedures"), but since ODE inversion (~50 steps) is the dominant cost in extraction for all methods, reporting only the transform time overstates the practical speedup. Including end-to-end extraction times (transform + inversion) would give a more complete picture.

4. **Ablation on modules uses only one attack setting (brightness).** Figure 6(c) tests robustness under brightness adjustment only, concluding that spherical mapping is "essential for restoring robustness." Testing additional attacks (e.g., JPEG, Gaussian blur, median filter) would strengthen this claim.

### Trivial
None.

## Nice-to-Haves
- Include classical multivariate normality tests (e.g., Henze-Zirkler, energy test) on the watermarked noise vectors to directly verify distributional closeness beyond the binary classifier.
- Report full ROC curves for the extraction results rather than only TPR@1%FPR, especially since Gaussian Shading (fixed-key) achieves 98.43% ACC under post-processing — close to the proposed method's 95.02%.
- Quantify the deviation of higher-order moments (e.g., kurtosis comparison) to bound the gap between the theoretical guarantee and practical indistinguishability.

## Removed Points
These points are flagged to be removed; treat them with caution:

- **Criticism about spherical 3-design "glossed over":** The harsh critic claimed the distribution over vertices derived from z^(1) is not uniform and that Theorem 3.2's claim is not established. However, Theorem 3.1 proves 3-wise independence of z^(1) as Bernoulli(1/2) bits. The mapping v = 2z^(1) - 1 gives ±1-valued variables that are also 3-wise independent. The set of normalized ±1/√(l_x) vectors on the sphere arising from a 3-wise independent distribution over hypercube vertices IS a spherical 3-design — this is a known mathematical fact that the paper correctly invokes. The criticism misunderstands the relationship between 3-wise independence and spherical design.

- **Criticism about "missing appendix" content:** The harsh critic faults the paper for "appendix dependence." The parser strips appendices from all papers; they exist in the original submission. This is not a valid criticism.

- **Criticism about "overclaimed" abstract:** The abstract states "We theoretically prove that the watermarked noise distribution preserves the target prior up to third-order moments" — this is accurate. The issue is solely with Eq. (2)'s framing, not the abstract's claim.

- **Strength Finder's generic strengths:** Removed strengths that are generic or conflict with verified weaknesses (e.g., "provable and empirically verified statistical indistinguishability" ignores the theoretical gap noted above; "superior robustness" conflates with the weakened Gaussian Shading baseline issue).

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. **Recalibrate the theoretical framing in Section 3.1.** Replace the cryptographic indistinguishability language (PPT adversaries, negligible functions) with a more precise statement: "We prove that the watermarked noise distribution matches the standard Gaussian prior up to third-order moments (spherical 3-design), and empirically demonstrate that this suffices for practical undetectability against learned classifiers and statistical tests." This honestly reflects what the paper achieves and avoids setting a bar that cannot be met.

2. **Complete Figure 2** by adding the proposed method's classifier accuracy curves (and numerical values) alongside Tree-Ring, Gaussian Shading, and PRC. If the original submission already does this and the parser dropped it, add explicit accuracy numbers in the caption or surrounding text.

3. **Reorganize the Gaussian Shading comparison.** Add a row for lossless Gaussian Shading (per-image keys) in Table 2 to show what the absolute best-case baseline achieves, alongside the fixed-key variant. Discuss the practical trade-off (key storage vs. slight robustness loss).

4. **Clarify the FID reference distribution** in the Table 1 caption (e.g., "FID between watermarked images and unwatermarked images from the same model and prompt set").

## Score and Decision

**Calibration Anchors:**

**Round 1 (Bracketing):**
| Paper | Path | Score | Round | Comparison |
|-------|------|-------|-------|------------|
| SuperMark | T0ebbDO60R.md | 3.75 | 1 | Much weaker — lacks novelty, poor SSIM/PSNR, limited contribution. Current paper is substantially stronger. |
| PRC Watermark | jlhBFm7T2J.md | 6.50 | 1 | Closely related baseline. PRC has stronger theoretical guarantees (cryptographic PRC) but weaker robustness and slower extraction. Current paper trades theoretical rigor for practical benefits (no key storage, faster, more robust). Comparable overall. |
| Hidden in the Noise | ll2nz6qwRG.md | 5.83 | 1 | Similar domain (noise-based watermarking). That paper had incomplete evaluation and limited theory; this paper has more thorough experiments and genuine theoretical grounding. Slightly stronger. |
| A Recipe for Watermarking | HexshmBu0P.md | 5.33 | 1 | Training-based approach with limited novelty and weaker evaluation. Current paper is stronger on both theory and experiments. |

**Round 2 (Narrowing):**
| Paper | Path | Score | Round | Comparison |
|-------|------|-------|-------|------------|
| Shallow Diffuse | 1IwoEFyErz.md | 6.00 | 2 | Similar score range. That paper had good theory but limited attacks and incomplete ablation. Current paper has more comprehensive evaluation but overclaimed theory. Roughly comparable; current paper slightly weaker due to theoretical framing issue. |
| SAT-LDM | ETFfXGM3e4.md | 5.50 | 2 | Training-based with theoretical generalization bounds but questionable experimental design. Current paper has cleaner experimental setup and clearer contribution, but analogous overclaiming of theoretical guarantees. Comparable. |
| SuperMark (revisited) | T0ebbDO60R.md | 3.75 | 2 | Already compared above. |

**Round 1 bracket:** 5–7.
**Round 2 narrowing:** The paper sits closest to the 5.5–6.0 range.
**Final score:** 5.5. The paper has a genuine contribution (encryption-free lossless watermarking with strong empirical validation) and is clearly stronger than low-scoring papers in this space. However, the major weakness — a mismatch between the cryptographic-level problem formulation and the (more modest) third-order moment-matching proof — prevents it from reaching the 6+ tier of the PRC watermark paper, which actually delivers on its theoretical claims. With honest recalibration of the theoretical framing and completion of Figure 2, this could be a 6+ paper.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>