## Summary

This paper proposes Spherical Watermark, a lossless watermarking framework for diffusion models that embeds binary watermarks into the Gaussian noise prior without per-image key storage. The method uses a binary embedding module (mixing watermark bits with random padding via an invertible matrix over 𝔽₂) followed by a spherical mapping module (projection onto the unit sphere, orthogonal rotation, chi-square scaling). The authors prove that the intermediate representation is a spherical 3-design (matching the uniform distribution on the sphere up to degree-3 moments) and provide empirical evidence of indistinguishability via near-chance classifier accuracy and preserved FID. Extraction replaces the belief-propagation decoding used by prior lossless methods (PRC) with simple matrix-vector multiplication, yielding dramatic speedups.

## Strengths

- **Theoretical grounding via spherical 3-design analysis.** Theorem 3.1 (3-wise independence of the mixed bitstream) and Theorem 3.2 (spherical 3-design on the unit sphere) together establish that watermarked noise matches the standard Gaussian distribution up to third-order moments. This goes beyond prior lossless methods: Gaussian Shading relies on stream-cipher arguments and PRC on cryptographic error-correcting codes, neither of which provides distributional moment matching. The empirical validation (ResNet-18 accuracy near 50%, Figure 2) confirms the predicted indistinguishability.

- **Eliminates per-image key storage while preserving losslessness.** Unlike Gaussian Shading (unique key+nonce per image) and PRC (pseudorandom coding with heavy cryptographic operations), Spherical Watermark uses a single fixed signature 𝒦 = {𝐓, 𝐂} — two matrices constructed during a build phase — with no per-image secrets. The ablation study (Figure 6(d)) confirms undetectability is stable across parameter variations, showing the fixed-signature design does not sacrifice distributional fidelity.

- **Extraction is roughly four orders of magnitude faster than PRC Watermark.** Figure 4 reports extraction time ≈10⁻³·⁵ s for Spherical Watermark versus ≈10¹ s for PRC. This speedup is structurally motivated: PRC requires belief-propagation decoding, while Spherical Watermark uses matrix-vector multiplication and rounding (Equation 13). This is a concrete, practically relevant advantage for scalable deployment.

- **Sustains high detection accuracy across a watermark capacity range where PRC fails completely.** Figure 6(a) shows ACC under JPEG-70 compression as a function of watermark capacity. Spherical Watermark maintains high accuracy up to lₘ ≈ 3000 bits, while PRC's decoding deteriorates rapidly beyond lₘ = 2000. This demonstrates a meaningful robustness advantage over the leading lossless competitor.

## Weaknesses

### Major

- **Rotation matrix implementation gap between theory and practice.** The theory assumes **C** ∈ ℝ^{lₓ × lₓ} — a full-dimensional orthogonal rotation. A footnote (Section 3.2) states that "in practice, l_c is chosen as a factor of l_x (e.g., l_c = ⌊√(l_x)⌋)" to balance expressiveness with efficiency. With the default l_x = 16384, this gives l_c = 128. But a **C** ∈ ℝ^{128×128} matrix cannot directly rotate a 16384-dimensional vector **z^(2)**. The paper never explains how this mismatch is resolved — whether **z^(2)** is partitioned into groups, reshaped into a matrix, or handled via some other mapping. Each plausible resolution would break the theoretical guarantee that the rotated vector remains a spherical 3-design on the full sphere S^{lₓ-1}, because rotation in a subspace does not uniformly mix all coordinates. Without this detail, the core implementation is not reproducible from the description, and the connection between theory and practice is unclear.

### Minor

- **Mismatch between the formal undetectability definition and the actual theoretical guarantee.** Equation (2) defines undetectability via full computational indistinguishability (PPT adversary, negligible function in a security parameter ρ), but the theory only establishes a spherical 3-design — i.e., matching up to degree-3 polynomials. The conclusion states watermarked inputs are "provably... indistinguishable from a standard Gaussian prior" without qualification. While the abstract is more precise ("up to third-order moments") and Section 5 acknowledges higher-order deviations, the formal definition and some framing sentences overclaim relative to what the theory strictly proves. This mismatch is worth correcting.

- **Gaussian Shading comparison uses a deliberately broken configuration.** The paper tests Gaussian Shading with fixed keys and notes "with fixed keys, Gaussian Shading no longer achieves true losslessness" (Section 4.1), then reports 97% detectability. Presenting this degraded result as evidence of superiority is slanted, since Gaussian Shading was designed around per-image unique keys. The primary fair comparison with PRC Watermark (which uses fixed keys) is more credible. The Gaussian Shading result should be separated from the main undetectability claims or caveated more prominently.

- **PRC implementation details not reported.** The ~4-order speedup over PRC is compelling but the paper does not report which PRC code parameters, belief propagation settings, library, or hardware were used. This would strengthen the reproducibility of the efficiency comparison.

### Trivial

- The FID comparison measures FID against the unwatermarked output distribution rather than against real images (the standard practice). The numbers in the mid-to-high 40s are high by typical FID standards, confirming an internal comparison. A brief footnote would clarify this for readers.

## Nice-to-Haves

- Formal higher-order statistical tests (maximum mean discrepancy, energy distance, or Kolmogorov-Smirnov tests on marginal distributions) would strengthen the empirical indistinguishability claims beyond binary classifier accuracy.
- A more systematic discussion of the rate-fidelity-robustness trade-off: 512 bits of watermark with 31-fold repetition and 512 bits of random padding in a 16384-dimensional latent space represents a very low effective information rate. The paper acknowledges this indirectly in the ablation but would benefit from a dedicated discussion.

## Removed Points

These points were flagged for removal; treat them with caution:

- **"Computational efficiency comparison appears uncalibrated"** (Harsh Critic point 4): The claim that the speedup "strongly suggests implementation-level differences" is speculation. The paper attributes the speedup to replacing BP with matrix-vector multiplication, a legitimate algorithmic advantage. Without evidence of implementation bias, this criticism is unfounded.
- **"Binary embedding matrix construction depends on random permutations"** (Harsh Critic section note): The build-phase construction of **R** from random permutations is standard for a method using a fixed secret key. The source of randomness and repeatability are standard engineering decisions, not a weakness.
- **"Missing related works"**: Per the hard rules, this cannot be verified without external sources and is not included.
- **Strength Finder items that are generic or conflict with verified weaknesses**: Some strengths about "addressing an important problem" or being "well-motivated" are too generic to retain. The four strengths listed above are concrete and evidence-backed.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface an independent novel insight that the paper itself does not present.

## Suggestions

1. **Resolve the rotation matrix implementation gap explicitly.** Specify exactly how **C** ∈ ℝ^{l_c × l_c} is applied when l_c < l_x (e.g., by partitioning **z^(2)** into blocks, applying **C** to each block, or reshaping). State whether any approximation is introduced and how it affects the spherical 3-design guarantee. This is essential for reproducibility.

2. **Align the theoretical claims with what is actually proven.** Replace "provably indistinguishable from standard Gaussian" with "proven to match the standard Gaussian up to third-order moments, with empirical evidence confirming practical indistinguishability throughout." Update the formal definition in Equation (2) to match the 3-design guarantee rather than full PPT indistinguishability, or add a remark explaining that the security parameter is realized via the dimensionality (l_x → ∞ asymptotics).

3. **Relegate the Gaussian Shading detectability result to a separate discussion** rather than presenting it alongside the main undetectability comparison. Make clear that this result reflects a deliberately altered setting (fixed keys) and is not a fair comparison under Gaussian Shading's designed operating conditions.

4. **Report the specific PRC implementation** (code parameters, belief propagation settings, library) used for the timing comparison to increase reproducibility.

## Score and Decision

**Score calibration summary:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| `/home/.../LqB8cRuBua.md` (Diffusion SigFormer) | 2.00 | R1 | Unrelated topic; not comparable |
| `/home/.../RFJGFrMvYj.md` (TCIG) | 1.50 | R1 | Unrelated; not comparable |
| `/home/.../T0ebbDO60R.md` (SuperMark) | 3.75 | R1 | Weaker method and evaluation; this paper is stronger |
| `/home/.../zqo2eKjSWH.md` (Stable Signature is Unstable) | 4.50 | R1 | Attack paper, not directly comparable |
| `/home/.../9XEBFywIW7.md` (Spread them Apart) | 4.40 | R1 | Less theory, narrower experiments; this paper is stronger |
| `/home/.../HexshmBu0P.md` (A Recipe for Watermarking) | 5.33 | R1/R2 | Recipe/survey paper with limited novelty; this paper has stronger theory and novel method |
| `/home/.../ll2nz6qwRG.md` (Hidden in the Noise/WIND) | 5.83 | R2 | Two-stage method, accepted; comparable quality, but this paper has stronger theory |
| `/home/.../ETFfXGM3e4.md` (SAT-LDM) | 5.50 | R2 | Training-based watermarking; this paper is comparable but different approach |
| `/home/.../uHdf9F1tY4.md` (DiffusionShield) | 5.50 | R2 | Data copyright protection; comparable quality |
| `/home/.../1IwoEFyErz.md` (Shallow Diffuse) | 6.00 | R2 | Rejected despite good theory; this paper has more thorough experiments |
| `/home/.../jlhBFm7T2J.md` (PRC / Undetectable Watermark) | 6.50 | R1/R2 | **Key anchor.** The paper compares against this. PRC is more complete (no reproducibility gap) and accepted with 6.50. This paper has comparable strengths but a notable implementation gap, placing it slightly below. |
| `/home/.../mDKxlfraAn.md` (Image Watermarks are Removable) | 6.40 | R2 | Attack paper, not directly comparable |

**Round 1 bracket:** 5.0–6.5 (between "Spread them Apart" at 4.40 and PRC at 6.50).

**Round 2 narrowing:** The paper sits between Shallow Diffuse (6.00, rejected with limited experiments) and SAT-LDM/DiffusionShield (~5.50). It is cleaner than the rejected papers at 5.33–5.50 but has a concrete reproducibility gap (rotation matrix) that the PRC anchor (6.50) does not suffer from.

**Final score: 5.5.** The paper has genuine contributions (spherical 3-design theory, fast extraction, no per-image keys, strong empirical results) but the rotation matrix implementation gap is a real weakness that prevents the paper from reaching the level of the PRC anchor (6.50). Addressing this gap could raise the score.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>