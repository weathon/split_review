Now I have all the evidence needed. Let me produce the consolidated review.

## Summary

This paper proposes a zero-reference, self-supervised framework for joint denoising and low-light enhancement. The method generates paired sub-images from a single low-light input via (1) neighboring pixel masking (sub-sampling 2×2 patches to produce two 1/4-resolution images with shared reflectance but different noise realizations) and (2) gamma correction applied to one sub-image to create an illumination difference while keeping the reflectance approximately consistent. It further introduces a DCT-based frequency-domain decomposition module (FIcoder) to extract illumination and multi-band frequency priors, which guide a transformer-based reflectance extraction network (REFnet) via cross-attention. The framework is trained end-to-end with a retinex decomposition loss, a self-supervised enhancement loss, and a regularization term. Experiments on LOLv1, LOLv2, SICE, and SIDD show that the method achieves state-of-the-art performance among zero-reference and unpaired approaches across multiple metrics.

## Strengths

1. **Physically grounded self-supervised training-pair generation.** The derivation of paired sub-images with controlled differences in noise (via pixel masking) and illumination (via gamma correction) from a single low-light image (Sec. 3.2, Eqs. 5–8) is principled and novel. This enables zero-reference joint denoising and enhancement with a clear theoretical basis, supporting the paper's main claim of a self-supervised framework.

2. **DCT-based frequency-domain degradation decomposition with quantitative validation.** The use of DCT masks to decompose the input into four frequency bands plus an illumination prior, integrated via a learned encoder (FIcoder) to guide reflectance extraction (Sec. 3.3, Fig. 4), is well-motivated. The ablation study (Tab. 3) confirms each prior contributes meaningfully: removing all priors drops ~0.9 dB PSNR, adding illumination prior recovers ~0.6 dB, and full priors give the best results.

3. **State-of-the-art performance across real-world benchmarks.** The method achieves highest PSNR/SSIM/LPIPS on LOLv1 and LOLv2 (Tab. 1), and best BRISQUE/CLIPIQA on SIDD (Tab. 2) among compared zero-reference and unpaired methods. Qualitative results (Figs. 5–7) show clear improvements in denoising, color fidelity, and illumination handling over methods like EnlightenGAN, RUAS, and Zero-DCE.

4. **Comprehensive ablation studies on key design choices.** Ablations on denoising design (neighborhood masking + regularization, Tab. 4), hybrid priors (Tab. 3), and gamma factor (Fig. 9) provide systematic evidence that each component contributes to performance. The ablation on the gamma enhancement factor (Fig. 9, right) explicitly explores the trade-off between illumination difference and the validity of the Taylor approximation.

## Weaknesses

### Major

1. **The core assumption that sub-image reflectance maps can be treated as equal is unexamined for the cases where it is most likely to fail.** The method forces \(\|R_1 - R_2\|_2^2\) via \(\mathcal{L}_R\) (Eq. 13), based on the claim that \(R_1\) and \(R_2\) "share the same ground truth reflectance" (line 122). However, adjacent pixels in a 2×2 patch can have genuinely different true reflectance at edges, texture boundaries, and fine details. Minimizing L2 distance between reflectance maps that are *not* equal in the ground truth could force the network to produce a smoothed average, losing high-frequency detail. The paper acknowledges that \(R_1\) and \(R_2\) are "highly similar in pixel values" (line 103) and includes a regularization term \(\mathcal{L}_{reg}\) (Eq. 15) that checks consistency at the original scale. But neither a quantitative justification of "how similar" adjacent-pixel reflectance truly is, nor a synthetic-data validation showing that the constraint does not erase legitimate detail, is provided. The ablation (Tab. 4) shows that removing masking hurts performance, but this does not validate the equality assumption — it only shows the paired structure helps overall. This is the central training signal of the method, and while the empirical results are strong, the assumption deserves direct validation (e.g., on synthetic data with known ground-truth reflectance).

### Minor

2. **Gap between the Taylor approximation and the actual gamma range used.** The derivation (Eqs. 8–10) relies on \(R^{\lambda-1} \approx 1\) when \(\lambda\) is "close to 1." However, the method samples \(\sigma \in (1.3, 1.7)\), giving \(\lambda = 1/\sigma \in (0.59, 0.77)\), which is not close to 1. For a typical reflectance \(R=0.5\), the multiplier \(R^{\lambda-1}\) can be 1.23–1.32 — a 23–32% error in the effective noise magnitude. The paper's own ablation (Fig. 9, right) and discussion (lines 259–260) acknowledge that higher \(\sigma\) (lower \(\lambda\)) "does not conform to the assumption," and the chosen range reflects an empirical sweet spot rather than a regime where the theory is exact. This does not invalidate the method, but the theoretical derivation is presented as tighter than it actually is; a more careful treatment (e.g., not absorbing \(R^{\lambda-1}\) into the noise) would improve rigor.

3. **SIDD evaluation uses no-reference metrics only and does not specifically test low-light enhancement.** The paper reports BRISQUE and CLIPIQA on SIDD and claims this demonstrates "enhancement capability in challenging low-light scenes" (line 228). However, SIDD is primarily a denoising benchmark; ground-truth clean images exist but are not used in this evaluation. No-reference perceptual metrics are weakly correlated with enhancement quality. Additionally, the paper tests the method on SIDD but not on a dedicated low-light denoising benchmark. This weakens but does not invalidate the claim of generalization to joint denoising and enhancement.

4. **LCnet is ablated only visually, not quantitatively.** The ablation of the Light Correction Network (LCnet, Fig. 8 left) is shown only as a visual comparison. Given that LCnet is a core architectural component, reporting PSNR/SSIM with and without it on at least one benchmark (e.g., LOLv1) would strengthen the paper.

5. **The "interpretable" claim is overstated.** The title and introduction emphasize interpretability, but the paper provides no post-hoc analysis of what the network learns, how the degradation representations correspond to physical quantities, or how cross-attention separates degradations. The method is "physically grounded" (using Retinex theory and DCT priors), which is a strength, but this does not constitute interpretability in the standard sense (e.g., prototypical reasoning, concept attribution, or feature visualization). This is a presentation issue rather than a technical flaw.

### Trivial

6. **Missing quantitative detail on the REFnet/LUMnet architecture.** The description of "transformer blocks," "gating modules," and "cross-attention" (line 124) is too generic. The paper would benefit from specifying layer counts, head dimensions, and how Q/K/V are assigned in the cross-attention mechanism.

## Nice-to-Haves

- A synthetic-data experiment (e.g., using clean high-resolution images with known reflectance, sub-sampled with the 2×2 masking strategy) to quantify whether the enforced equality of \(R_1\) and \(R_2\) causes systematic blurring at edges versus uniform regions.
- A more accurate noise-model derivation that avoids the \(R^{\lambda-1}\approx1\) approximation by keeping the full Taylor expansion or constraining \(\lambda\) to a range where the error is demonstrably negligible.
- A breakdown of SIDD results on low-light versus normal-light subsets, or replacement with a proper low-light denoising benchmark.

## Removed Points

These points were flagged by reviewers but are removed from the main evaluation for the reasons stated:

- **"Resemblance to Noise2Noise is not discussed"** – The paper explicitly discusses N2N in Section 2 (lines 79–90) and builds on it. This is not a weakness.
- **"Does not compare with supervised methods"** – The paper is a zero-reference method; comparing against supervised methods is outside scope. The reviewer's framing implies an unfair expectation.
- **"Ablation gains on priors are modest"** – 0.6 dB PSNR improvement is meaningful for zero-reference methods on real data. This conflates subjectivity with weakness.
- **"SIDD has no low-light condition"** – SIDD does contain challenging lighting conditions, including low-light scenes (the paper's Fig. 7 caption calls it a "real-world low-light image from the SIDD dataset"). The concern about SIDD's relevance is retained in Minor weakness #3 but the absolute claim that SIDD has "no low-light condition" is removed as factually incorrect.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a genuinely novel observation about the work that the paper itself does not already state or imply.

## Suggestions

1. **Validate the reflectance equality assumption directly.** Create a synthetic dataset where the ground-truth reflectance is known (e.g., clean high-resolution images), apply the 2×2 masking, and check whether the learned \(R_1\) and \(R_2\) deviate from the ground truth in structured ways (edges, fine textures). Even a single-figure analysis would substantially strengthen the paper's claim.

2. **Acknowledge and quantify the Taylor approximation error.** Either modify the derivation to explicitly keep \(R^{\lambda-1}\) as a multiplicative factor on the noise (removing the approximation), or provide a numerical simulation showing that for the chosen \(\lambda\) range the error is negligible in practice.

3. **Add a quantitative ablation for LCnet.** Report PSNR/SSIM on LOLv1 with and without LCnet, similar to how the other ablations are handled.

4. **Either add an evaluation on a low-light denoising dataset (e.g., a real low-light subset of SIDD) or adjust the claim about SIDD to accurately reflect that it primarily tests denoising performance.**

5. **Tone down or better justify the "interpretable" claim.** If the term is meant to mean "physically grounded" or "principled," state this explicitly. If the authors intend a stronger notion of interpretability, include a post-hoc analysis (e.g., attention visualization, probe of the degradation representation).

## Score and Decision

The paper presents a genuinely novel self-supervised training strategy with strong empirical results across four benchmarks. The main concerns are (a) the unexamined core assumption about reflectance equality and (b) a gap between the theoretical derivation and the actual parameter regime. Neither is fatal — the empirical results are consistent and the method clearly outperforms comparable zero-reference approaches — but both warrant direct validation before the theoretical claims can be fully accepted. The paper makes a substantial empirical contribution that would benefit from tightening the theoretical narrative.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>