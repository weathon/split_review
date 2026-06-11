Now I have enough calibration to make a final scoring decision. Let me summarize the comparison:

- **"Shallow Diffuse" (6.00)**: Training-free with low-dimensional subspace approach. Our paper has a more rigorous theoretical chain (spherical 3-design), more comprehensive evaluation (adversarial attacks, multiple solvers), and clearer practical advantages. Our paper is stronger.
- **"PRC Watermark" (6.50)**: The most direct comparison. PRC introduced the undetectable watermark concept with high novelty; our paper improves on PRC's key weaknesses (speed ~10,000× faster, no per-image keys, better robustness) with a cleaner spherical 3-design framework. Both share framing overclaim tendencies. Our paper is comparable but with clear practical advantages.
- **"TabWak" (7.20)**: Different domain (tabular), "first-of-its-kind" novelty driving higher scores. Our paper doesn't have that level of domain-first novelty since it builds on the established latent-space watermarking paradigm.

**Final score: 6.5** — comparable to PRC Watermark (the most relevant anchor), with practical improvements offsetting similar framing concerns.

Now let me write the final review with all required elements.Now let me write the final review.

## Summary
Spherical Watermark proposes a latent-space watermarking framework for diffusion models that maps binary watermark bits to approximately Gaussian noise via three reversible modules — binary embedding, spherical projection with orthogonal rotation, and chi-square scaling — without requiring per-image key material. The theoretical analysis proves the watermarked noise forms a spherical 3-design (matching the Gaussian prior up to third-order moments), and experiments on Stable Diffusion v1.5 and v2.1 demonstrate FID scores essentially identical to unwatermarked baselines, near-chance classifier detection, and extraction approximately 10,000× faster than PRC Watermark.

## Strengths
- **Rigorous stepwise theoretical chain**: Theorem 3.1 establishes 3-wise independence of the binary code via the specially constructed block-triangular matrix T; Theorem 3.2 proves this yields a spherical 3-design; Lemma 3.3 shows orthogonal rotation preserves the design property; Lemma 3.4 (polar decomposition) completes the chain to approximate Gaussian. Each step is clearly stated and correctly argued.
- **Empirically indistinguishable FID from unwatermarked baseline**: Table 1 shows Spherical Watermark FID of 48.1224 vs. 48.1256 for the original on SD v1.5 (COCO), and 46.8132 vs. 46.8146 on SD v2.1 — differences well within error bars. Only PRC Watermark achieves comparable fidelity among all tested methods.
- **Dramatic computational efficiency gain**: Figure 4 shows extraction at ~10^(-3.5) seconds vs. ~10^1 seconds for PRC Watermark — roughly four orders of magnitude faster, eliminating the belief-propagation decoding bottleneck that made PRC expensive to deploy.
- **Strong adversarial robustness**: Table 2 shows 98.12% ACC under WEvade adversarial attacks vs. 88.06% for Gaussian Shading and 97.69% for PRC Watermark. The TPR gap is also notable: 99.83% vs. 99.23% (Gaussian Shading) and 95.38% (PRC Watermark).
- **Careful ablation isolating module contributions**: Figure 6(b) shows omitting binary embedding makes noise trivially detectable by a classifier; Figure 6(c) shows omitting spherical mapping causes robustness to collapse under brightness adjustment. Both modules are individually necessary and their theoretical properties have measurable empirical consequences.
- **Robustness across solver and timestep configurations**: Tables 4–5 demonstrate that switching between DDIM, PNDM, and DPM-Solver++, or varying generation/inversion steps from 10 to 50, causes negligible accuracy degradation (all ACC ≥ 96%).

## Weaknesses

### Fatal
None.

### Major
- **Cryptographic indistinguishability framing overstates the actual theoretical guarantee**: Section 3.1 formulates the problem using the language of computational security — "computationally indistinguishable," a "probabilistic polynomial-time adversary," and error bounded by "negl(ρ)" (Equations 2–3). What Section 3.3 actually proves is that the watermarked noise matches the standard multivariate normal distribution up to third-order moments (a spherical 3-design scaled by a chi-distributed radius). These are fundamentally different guarantees: moment-matching up to degree 3 does not imply computational indistinguishability, as a polynomial-time adversary could in principle exploit a 4th-order statistic. The paper acknowledges this gap in Section 5 ("higher-order moments may deviate from the true prior"), but the formal problem statement remains misaligned with the actual proof. The paper should either replace the cryptographic formulation with distributional-distance metrics or provide justification for why 3rd-order matching implies the claimed level of indistinguishability.

### Minor
- **"Lossless" label is imprecise given the 3rd-order guarantee**: The paper uses "lossless" to describe a method that preserves the Gaussian prior only up to third-order moments, while prior work (e.g., Gaussian Shading with per-image keys) achieves exact distribution preservation. The abstract simultaneously claims "exact multivariate Gaussian noise" and "up to third-order moments," which are contradictory. "Approximately distribution-preserving" or "moment-matching" would more accurately characterize the method.
- **"Encryption-free" framing obscures continued dependence on a shared secret**: The method still requires a fixed signature (T, C) shared between embedder and extractor. If T or C is leaked, an adversary can both extract and remove watermarks. What the paper eliminates is per-image key material (nonces) and cryptographic primitives (stream ciphers, PRCs), not all secrets. "Stateless" or "fixed-signature" watermarking would better characterize the contribution.
- **Gaussian Shading comparison omits the intended per-image-key configuration**: The paper evaluates Gaussian Shading only with fixed keys (acknowledged at line 193–194). While the paper's motivation — avoiding per-image key management — is legitimate and well-argued, the reader cannot quantify the fidelity/robustness trade-off being made. Reporting Gaussian Shading results with per-image keys on a subset of the data would strengthen the comparative evaluation.
- **No error-propagation analysis for extraction reliability**: The extraction step (Eq. 13) rounds Ĉ⁻¹ ẑ_T to recover binary values, but the paper does not discuss the conditions under which this rounding succeeds — i.e., what inversion error level causes bit flips. A brief analysis relating inversion error to bit-error rate would close the gap between the embedding-side distribution theory and extraction reliability.

### Trivial
- The abstract states "exact multivariate Gaussian noise" in one sentence and "up to third-order moments" in the next, creating an internal inconsistency that should be resolved.

## Nice-to-Haves
- Discuss key rotation: in deployment, what happens when the signature (T, C) must be rotated? Can previously watermarked content be re-verified under a new signature?
- Discuss the inversion error introduced by using empty-prompt DDIM inversion (∅) during extraction while generation uses a text prompt. This is standard practice in diffusion inversion literature but deserves qualitative discussion since it is the primary source of bit flips during extraction.

## Removed Points
These points are flagged to be removed, treat them with caution.
- **"No experiment measuring whether watermarked images are different for the same prompt"** (Harsh Critic): The harsh critic acknowledges this is inherent to all input-space watermarking and not a flaw. Removed as out of scope.
- **Request to verify T⁻¹ = T over F₂ with a proof** (Harsh Critic): The block-triangular structure with identity diagonal blocks makes this property immediate; requesting a formal proof is a nitpick. Removed.
- **Question about how rotation is applied when l_c ≠ l_x** (Harsh Critic): The paper explicitly sets l_c = l_x for notation in the main text (line 113) and addresses the practical variant in Footnote 1. Removed as already addressed.
- **Request for "a more powerful classifier" in undetectability tests** (Harsh Critic): The paper already tests both a 2-layer MLP and ResNet-18. This is a generic "could test more" complaint that would apply to almost any paper. Removed.

## Novel Insights
The paper's integration of spherical t-designs from algebraic combinatorics into diffusion-model watermarking is genuinely novel. The construction of T as a block-triangular matrix with row-sparsity-controlled R (Algorithm 1), designed to ensure 3-wise independence while enabling simple inversion (T⁻¹ = T over F₂), is an elegant bridge between coding theory and distribution matching. The three-module decomposition (binary embedding → spherical mapping → diffusion integration) cleanly separates the independence, distribution-matching, and model-interface concerns, making the method easier to analyze and extend than prior approaches that tightly couple these concerns.

## Suggestions
- Replace the cryptographic indistinguishability formulation in Section 3.1 with a definition grounded in moment-matching or distributional distance (e.g., bounding total variation or Wasserstein distance between the watermarked and true Gaussian distributions). The spherical 3-design result is concrete and valuable without cryptographic framing.
- Add a brief error-propagation analysis connecting inversion error ‖ẑ_T − z_w‖ to bit-error rate after rounding in Eq. 13. This would meaningfully link the distribution theory to extraction reliability.
- Report Gaussian Shading results with per-image keys on a small subset (e.g., 100 images) to quantify the storage-vs-fidelity trade-off, or explicitly argue that this comparison is unnecessary given the paper's focus on eliminating per-image keys entirely.

## Score and Decision

**Calibration anchors considered:**

| Paper | Path | Avg Score | Round | Comparison |
|-------|------|-----------|-------|------------|
| A Recipe for Watermarking DMs | HexshmBu0P | 5.33 | R1 | Training-based, limited novelty, PSNR <30dB — clearly weaker |
| Hidden in the Noise (WIND) | ll2nz6qwRG | 5.83 | R1,R2 | Fourier-based two-stage, limited evaluation — our paper stronger |
| Shallow Diffuse | 1IwoEFyErz | 6.00 | R2 | Low-dimensional subspace, training-free, limited attacks — our paper stronger |
| PRC Watermark (undetectable) | jlhBFm7T2J | 6.50 | R1,R2 | Most direct comparison — our paper improves speed/robustness with similar framing concerns |
| TabWak | 71pur4y8gs | 7.20 | R2 | Different domain (tabular), first-of-kind novelty — our paper below this |

**Round 1 bracket**: 5.5 – 7.5, anchored by PRC Watermark (6.50) as the closest comparable.

**Round 2 narrowing**: Shallow Diffuse (6.00) below us, PRC Watermark (6.50) as near-peer, TabWak (7.20) above us. The paper meaningfully improves upon PRC Watermark in practical dimensions (speed, robustness, key management) while sharing similar framing overclaim tendencies. It does not reach the domain-first novelty of TabWak.

**Final score**: 6.5 — comparable to PRC Watermark, with clear practical advantages (orders-of-magnitude faster extraction, no per-image keys, better adversarial robustness, cleaner theoretical framework) offset by the mismatch between the cryptographic framing in Section 3.1 and the spherical 3-design guarantee actually proved in Section 3.3.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>