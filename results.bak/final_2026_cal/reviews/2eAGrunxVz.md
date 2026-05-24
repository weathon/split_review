Now I have all the information needed. Let me write the final consolidated review.

## Summary

This paper introduces Spherical Watermark, a lossless watermarking framework for diffusion models that converts binary watermarks into Gaussian noise inputs without per-image key storage or cryptographic overhead. The method operates through three reversible modules: binary embedding (mixing repeated watermark bits with random padding via an invertible matrix over GF(2)), spherical mapping (projecting onto the unit sphere, orthogonal rotation, and chi-square scaling), and diffusion integration. The authors prove that the watermarked noise matches the standard Gaussian prior up to third-order moments (spherical 3-design), and provide extensive empirical evidence of undetectability, robustness, and computational efficiency across Stable Diffusion models.

## Strengths

- **Clean theoretical grounding with honest scope.** The paper provides a rigorous proof chain (Theorem 3.1 → Theorem 3.2 → Lemma 3.3 → Lemma 3.4) showing that the watermarked noise is a spherical 3-design, matching the standard Gaussian up to third-order moments. The limitations are openly acknowledged ("higher-order moments may deviate"), and the empirical classifier evidence convincingly fills the practical gap.

- **Near-perfect empirical undetectability verified by learned adversaries.** Figure 2 shows that a two-layer MLP trained on latent features achieves essentially chance accuracy (~50%) when distinguishing Spherical Watermark from unwatermarked noise, while Tree-Ring and Gaussian Shading (with fixed keys) are detected at 100% and 97% respectively. This directly validates that the practical indistinguishability follows from the theoretical design.

- **Four-orders-of-magnitude extraction speedup over PRC Watermark.** Figure 4 demonstrates that extraction time for Spherical Watermark is ~10⁻³·⁵ seconds versus ~10¹ seconds for PRC — a ~10,000× speedup. This is a genuine practical advance: the elimination of belief-propagation decoding makes large-scale provenance tracking feasible.

- **Superior robustness under adversarial attacks.** Table 2 shows Spherical Watermark achieves 98.12% bit accuracy and 99.83% TPR@1%FPR under adversarial attacks, compared to 97.69%/95.38% for PRC and catastrophic collapse (49-52% accuracy) for lossy methods. This directly supports the paper's claim that losslessness underpins robustness (Appendix E).

- **High capacity without degradation.** Figure 6(a) shows that under JPEG-70 compression, Spherical Watermark maintains near-100% accuracy across watermark lengths from 512 to 4,096 bits, while PRC collapses to ~50% beyond 2,000 bits. This is a meaningful practical advantage.

- **Thorough ablation and sensitivity analysis.** The paper systematically ablates each module (Figures 6b-c), key parameters (Table 3, Figure 6d), ODE solvers (Table 4), and timestep configurations (Table 5). All controlled experiments confirm the design rationale and show the method is not brittle to implementation choices.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Introduction overstates the theoretical guarantee.** The introduction (p.1 col.2) states "We theoretically analyze each intermediate distribution and prove that the final noise is statistically indistinguishable from standard Gaussian noise." The actual proof only guarantees moment-matching up to degree 3 (spherical 3-design). The abstract is precise ("up to third-order moments"), and the limitations section acknowledges the gap, but the introduction gives a stronger impression than the theorems deliver. This is a presentational inconsistency the authors should fix.

- **Theorem 3.1 assumes both m and r are i.i.d. Bernoulli(1/2), but m is fixed per user.** The theorem's joint-distribution framing is correct for the analysis, but in practice m is a fixed secret watermark and only r is fresh per invocation. The paper should explicitly argue that for any fixed m, the mixing via R (with disjoint padding groups from Algorithm 1) still yields the claimed marginal and (sufficiently) low-order independence properties over the randomness in r. As written, readers familiar with cryptographic watermarking will wonder whether a fixed m creates detectable structure. The empirical results show it does not, but the theoretical presentation should be tightened.

- **FID evidence is too noisy to bear the weight of the distribution-preservation claim on its own.** Table 1 shows FID differences between Original and DwtDct that are well within one standard deviation on some dataset/model combinations (e.g., COCO SD v1.5: 48.30 vs 48.13, difference 0.17, std ~1.4), yet the paper claims "only PRC Watermark and our method match the original in FID, whereas other methods incur distribution shifts." This specific claim would be better supported by reporting a more sensitive distributional distance (e.g., MMD in latent space) or by explicitly acknowledging the noise level. The core undetectability claim is already well-supported by the classifier experiments (Figure 2), so the FID overstatement is not fatal, but it should be corrected.

### Trivial
None.

## Nice-to-Haves

- **Security analysis of the fixed secret key under multiple-image observation.** The paper assumes the signature K = {T, C} is secret and fixed, but does not analyze whether an adversary with access to many watermarked images (and the ability to invert the diffusion process) could estimate C or T. Since the mapping from watermark to noise is deterministic given K, this is a relevant threat model worth discussing as a limitation or addressing with a brief argument about information-theoretic hardness.

- **Classifier AUC or TPR@lowFPR for undetectability.** Figure 2 shows accuracy converging to ~50% over training epochs, which is convincing. Reporting the final AUC or the TPR at a fixed low FPR would align with standard practice in security evaluation and make the undetectability claim more directly comparable to future work.

- **Comparing spherical 3-design to exact Gaussian via MMD or Wasserstein distance.** The theoretical gap between 3-design and exact uniformity on the sphere could be directly quantified with an empirical distributional distance (e.g., MMD with a kernel that captures higher-order moments), which would strengthen the claim that third-order matching suffices for practical indistinguishability.

## Removed Points

*"encryption-free is slightly overstated"* — The paper uses "encryption-free" to contrast with PRC's cryptographic error-correcting codes, not to claim the absence of secret parameters. The term is used appropriately in context. Removed.

*"WEvade attack should be described in more detail in the main text"* — The paper cites Appendix F.4 for details, which is standard practice in conference papers. Removed.

*"losslessness may be compromised by ODE inversion error"* — The paper already addresses this through repetition count N and experiments with different solvers/timesteps. Removed.

*"missing related works"* — No external verification available. Removed per instructions.

## Novel Insights

The key insight that emerges from synthesizing the reviews is that Spherical Watermark occupies a genuinely new point in the design space: it achieves the theoretical ideal of losslessness (matching Gaussian moments) *simultaneously* with the practical benefits of encryption-free operation and 10,000× faster extraction. Prior work forced a trade-off: per-image keys (Gaussian Shading) or heavy cryptography (PRC). The paper's innovation is recognizing that a carefully constructed spherical 3-design, combined with a fixed orthogonal rotation and independent chi-square scaling, is sufficient for both theoretical approximate-Gaussian guarantees and strong empirical robustness — without needing cryptographic primitives at all. This design principle may generalize to other generative models with Gaussian priors.

## Suggestions

1. **Tighten the introduction** to match the actual theoretical scope: replace "prove that the final noise is statistically indistinguishable from standard Gaussian noise" with "prove that the watermarked noise matches all moments up to third order, and provide strong empirical evidence of practical indistinguishability."

2. **Add an explicit argument** (even a paragraph) that Theorem 3.1's independence properties hold for a fixed m over the randomness in r, explaining why the disjoint-padding-group construction in Algorithm 1 suffices.

3. **Replace or supplement the FID comparison** with a more sensitive distributional metric (MMD on latent representations, or Wasserstein distance between empirical noise distributions) to cleanly support the distribution-preservation claim.

4. **Report classifier AUC** (or TPR@1%FPR for undetectability) alongside the accuracy-vs-epoch plots in Figure 2 for standardized comparison.

## Score and Decision

**Calibration Report:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| rjhF7b7n6g — Dataset Watermarking for Fine-tuning | 3.00 | 1 (bracket <3.5) | Weaker: narrower scope, less theory |
| cNEshxVcWg — NullGuard | 3.00 | 1 (bracket <3.5) | Weaker: less comprehensive evaluation |
| rb7rnOSa2g — Latents-Inv | 2.00 | 1 (bracket <3.5) | Weaker: withdrawn |
| 3aBWTYGcaT — Watermarking DLMs | 5.00 | 1 (bracket 3.5–7.5) | Weaker: less compelling empirical evidence |
| 5ifzhjMCKq — Guidance Watermarking | 5.00 | 1 (bracket 3.5–7.5) | Weaker: tuning complexity, limited attacks |
| oTGJZtrprx — Hiding in the Phase | 5.00 | 1 (bracket 3.5–7.5) | Weaker: weaker theory, mixed reviews |
| yGNLtD7VQ2 — Exposing Vulnerabilities | 4.00 | 1 (bracket 3.5–7.5) | Weaker: attack paper, not a constructive method |
| st1hrLTP14 — Self-Re-Watermarking Trap | 6.00 | 2 (narrow 5.5–6.5) | Comparable: novel threat model but narrower evaluation |
| 92fliNrbxY — CheckMate | 6.40 | 2 (narrow 5.5–6.5) | Slightly weaker: graph-specific, less practical advantage |
| wyucYNGPiW — PAI / Attack-Resistant | 6.50 | 2 (narrow 6.0–7.5) | Slightly weaker: less theory, limited ablation |
| EhDgP69DJG — PMark | 7.00 | 2 (narrow 6.0–7.5) | Comparable quality: clean theory + strong experiments, different domain (LLM watermarking) |

**Round-1 bracket:** [6.5, 7.5] — The paper is clearly above the ~5.0 watermarking papers in both theoretical depth and empirical thoroughness.

**Round-2 narrowing:** The paper compares favorably to PAI (6.5) on theoretical grounding and is most comparable to PMark (7.0, LLM watermarking) in terms of clean theory + thorough experiments. The practical speedup and the elegance of the encryption-free design push it slightly higher.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>