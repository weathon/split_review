Now I have sufficient calibration data. Let me finalize the review with the score.

**Calibration Summary:**

| Anchor | Path | Score | Round | Comparison |
|--------|------|-------|-------|------------|
| TabWak | 71pur4y8gs | 7.20 | R2 | Stronger — first-in-domain novelty premium; our paper is not at this level |
| Lightweight Deep Watermarking | j7b4mm7Ec9 | 7.60 | R2 | Stronger — higher reviewer confidence |
| Ambient Diffusion Scaling | qZwtPEw2qN | 6.80 | R2 | Different topic, not directly comparable |
| Noise Map Guidance | mhgm0IXtHw | 6.67 | R2 | Different topic |
| PRC Watermark (undetectable) | jlhBFm7T2J | 6.50 | R1 | Closest competitor — our paper improves on speed/capacity/robustness but shares overclaim issues; comparable |
| Shallow Diffuse | 1IwoEFyErz | 6.00 | R1,R2 | Our paper is clearly stronger — more thorough experiments, cleaner theory |
| Hidden in the Noise (WIND) | ll2nz6qwRG | 5.83 | R1,R2 | Our paper is clearly stronger |
| SAT-LDM | ETFfXGM3e4 | 5.50 | R2 | Our paper is stronger |
| A Recipe for Watermarking DMs | HexshmBu0P | 5.33 | R2 | Our paper is stronger |
| Spread them Apart | 9XEBFywIW7 | 4.40 | R1 | Our paper is stronger |
| SuperMark | T0ebbDO60R | 3.75 | R1 | Our paper is stronger |

**Round 1 bracket:** 5.5–7.0. **Round 2 narrowed to:** ~6.0. The paper is clearly stronger than the 5.33–6.00 anchors and roughly comparable to the PRC Watermark at 6.50, but the three Major weaknesses (overclaimed "statistically indistinguishable," theory-practice gap on block-wise rotation, misleading "encryption-free" framing) pull it slightly below PRC. **Final score: 6.0.**

Now let me write the final review.## Summary
This paper introduces Spherical Watermark, a lossless watermarking framework for diffusion models that embeds binary watermarks into the Gaussian latent noise without modifying model weights. The core innovation is a two-stage mapping: a binary embedding module that mixes repeated watermark bits with random padding via a fixed invertible matrix T to achieve 3-wise independence (Theorem 3.1), followed by a spherical mapping module that normalizes, orthogonally rotates, and chi-square-scales the result to approximate a standard Gaussian (Theorems 3.2, Lemmas 3.3–3.4). The method avoids per-image cryptographic keys by using a single fixed secret signature with fresh random padding per image. Experiments on Stable Diffusion v1.5/v2.1 show near-identical FID to unwatermarked generation, near-chance classifier detection, and superior robustness under adversarial attacks compared to both lossy and lossless baselines.

## Strengths
- **Rigorous theoretical chain from binary bits to Gaussian noise**: The paper constructs a multi-step proof: 2-wise and 3-wise independence of z^(1) via mixing matrix T (Theorem 3.1), spherical 3-design property of z^(2) (Theorem 3.2), preservation under orthogonal rotation (Lemma 3.3), and polar decomposition connecting chi-square scaling to multivariate normality (Lemma 3.4). This directly supports the undetectability claim and distinguishes the method from prior schemes relying on cryptographic rather than distributional guarantees.
- **Empirical FID parity with unwatermarked generation**: Table 1 shows Spherical Watermark achieves FID scores virtually identical to the original unwatermarked model across all four dataset–model combinations (e.g., 48.1224 vs. 48.1256 on SD v1.5/COCO), whereas every method except PRC Watermark incurs measurable degradation.
- **Near-chance classifier detection at both latent and image levels**: Figure 2 shows both a latent-level MLP and an image-level ResNet-18 achieve approximately 50% test accuracy — indistinguishable from random guessing — while Tree-Ring (100%) and Gaussian Shading with fixed keys (97%) are easily detected.
- **Extraction speed advantage of roughly four orders of magnitude over PRC Watermark**: Figure 4 demonstrates extraction in ~10^{−3.5} seconds versus PRC's ~10^{1.0} seconds, arising from simple matrix operations rather than belief-propagation decoding.
- **Superior adversarial robustness**: Table 2 shows 98.12% bit accuracy under WEvade attacks versus 88.06% for Gaussian Shading and 97.69% for PRC Watermark, while lossy schemes degrade catastrophically.
- **Thorough ablation studies**: Figures 6(b)–6(c) confirm both binary embedding and spherical mapping modules are essential. Table 3 quantifies the sparsity–robustness trade-off. Tables 4–5 confirm robustness across ODE solvers and timestep schedules. Figure 6(a) shows sustained accuracy up to 4000-bit capacity where PRC collapses beyond 2000 bits.

## Weaknesses

### Major
- **"Statistically indistinguishable" claim is overstated relative to what is proved**: The abstract, introduction, and conclusion repeatedly claim the watermarked noise is "statistically indistinguishable" from standard Gaussian. However, Theorems 3.1–3.2 and Lemmas 3.3–3.4 prove matching only up to third-order moments (spherical 3-design). The paper's own Discussion (Section 5) acknowledges that "higher-order moments may deviate from the true prior," directly contradicting the strong indistinguishability language. The empirical evidence (MLP and ResNet-18 at ~50% accuracy) does not close this gap — higher-capacity classifiers or non-parametric two-sample tests could potentially detect deviations in higher moments. This mismatch between claimed and proved guarantees appears prominently in the abstract and affects the paper's credibility.
- **Theory-practice gap on the block-wise rotation**: The theoretical analysis in Section 3.3 assumes a full orthogonal rotation on all of S^{l_x−1}. However, Footnote 1 reveals that in practice l_c = ⌊√l_x⌋ (≈128 for l_x=16384), meaning C is applied block-wise. Under this construction, the rotated vector z^(3) lies on a product of smaller spheres (S^{127})^{128}, not on S^{16383}. Consequently, the chi-square scaling with l_x=16384 degrees of freedom — which Lemma 3.4 requires to produce a standard multivariate normal — does not apply cleanly when the directional component comes from a product distribution on smaller spheres. The paper provides no analysis of how this practical compromise affects distributional fidelity, nor does it specify the exact block construction (block-diagonal? strided permutation?).
- **"Encryption-free" framing is potentially misleading**: The term appears in the title, abstract, introduction, and experimental sections. While the method does not use cryptographic encryption primitives (AES, stream cipher, etc.), it still relies on a fixed secret Signature K = {T, C} that must be kept confidential — the paper itself states K is "kept fixed and secret during runtime to prevent unauthorized removal" (Section 3.2). "Encryption-free" suggests zero secret material, which is inaccurate. The genuine contribution — fixed-key lossless embedding with per-image randomness from padding — is strong enough without this overstatement.

### Minor
- **TPR@1%FPR metric lacks calibration detail**: The paper does not specify how the 1% FPR threshold is calibrated (number of negative users, similarity score distribution, threshold-setting procedure).
- **Limited undetectability classifier evaluation**: Only a two-layer MLP (latent-level) and ResNet-18 (image-level) are evaluated. More convincing evidence would include non-parametric two-sample tests (e.g., MMD, energy distance) or a demonstration that detection accuracy fails to improve regardless of classifier capacity.
- **Unequal watermark lengths across baselines**: Traditional methods (DwtDct, DwtDctSvd, RivaGAN) use 32-bit watermarks while latent-based methods use 512-bit. A shorter message is intrinsically easier to recover, making the extraction accuracy comparison somewhat unfair. The paper acknowledges this discrepancy but does not discuss how it affects the comparison.
- **Mismatch between PPT formulation and actual guarantees**: The problem formulation (Eqs. 2–4) uses computational-indistinguishability language with PPT adversaries and negl(ρ) terms, but the actual construction provides information-theoretic guarantees (moment matching up to degree 3). The PPT framing is not the appropriate lens for statistical guarantees.
- **Extraction rounding step lacks justification**: Eq. 13 applies rounding to (C^{−1} ẑ_T + 1)/2 without normalizing by the radius r. This works because r/√l_x ≈ 1 in probability for large l_x, but the paper never states this reliance or quantifies the approximation error.

## Nice-to-Haves
- Add an MMD or energy-distance test between watermarked and unwatermarked latent vectors to strengthen undetectability evidence beyond classifier-based evaluations.
- Either implement a full l_x × l_x rotation (using structured orthogonal transforms to reduce O(l_x²) cost) or provide an explicit analysis of how the block-wise approximation affects the distribution (e.g., KL divergence or total variation bound).
- Replace "statistically indistinguishable" with precise language: "matches Gaussian up to third-order moments" for theory, and "not detectable by MLP/ResNet-18 classifiers" for empirics.

## Removed Points
These points are flagged to be removed, treat them with caution:

- **Harsh Critic: "Appendix F.4 not included"** — Removed per hard rules; the parser strips appendices from all papers. The original submission includes this material.
- **Harsh Critic: "missing proofs in appendix"** — Removed per hard rules; appendix content stripped by parser.
- **Harsh Critic: "Wei et al. (2024) omitted from comparison"** — The paper does cite Wei et al. and describes their contributions (lines 32–33: "Wei et al. provide a unified analytical framework for diffusion watermarking and instantiate several distribution-preserving schemes"). A deeper comparison would strengthen the paper but the paper does not omit them.
- **Harsh Critic: "The undetectability classifiers are low-to-moderate capacity" implying fatal weakness** — The classifiers used (MLP, ResNet-18) are standard for this type of evaluation. This is retained as a minor weakness (limited evaluation) but demoted from the critic's more severe framing.

## Novel Insights
The paper's combination of (a) a fixed invertible binary mixing matrix with disjoint padding assignments to achieve 3-wise independence, and (b) the spherical-design-to-Gaussian pipeline, represents a genuinely clever synthesis. The insight that fresh random padding per image can replace per-image cryptographic state while still refreshing the watermark's randomness is practically valuable and well-motivated. The spherical 3-design framing — connecting combinatorial properties of the mixed bitstream to distributional guarantees on the sphere — is an elegant theoretical perspective that could inspire follow-up work in other domains where discrete-to-continuous mappings need distributional fidelity guarantees.

## Suggestions
- Recalibrate language throughout: replace "statistically indistinguishable" with "matches Gaussian up to third-order moments" for theory and "not detectable by evaluated classifiers" for empirics. Similarly, replace "encryption-free" with "fixed-key" or "single-signature."
- Address the block-wise rotation gap: specify the exact construction and either analyze its distributional effect or implement a full rotation using structured orthogonal transforms.
- Clarify the TPR@1%FPR calibration procedure and discuss the 32-bit vs. 512-bit asymmetry in baseline comparisons.

## Score and Decision

**Calibration:** Across two rounds of retrieval, the paper was compared against 12 human-scored anchors. It is clearly stronger than WIND (5.83), Shallow Diffuse (6.00), SAT-LDM (5.50), and A Recipe for Watermarking DMs (5.33). It is roughly comparable to the PRC Watermark paper (6.50) — improving upon it in speed, capacity scaling, and adversarial robustness but sharing similar overclaim tendencies, with the additional theory-practice gap on the block-wise rotation. It falls clearly below TabWak (7.20). The three Major weaknesses (overclaimed indistinguishability, block-wise rotation gap, misleading "encryption-free" framing) pull the score to the lower end of the accept range. **Final score: 6.0.**

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>