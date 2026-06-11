Now I have solid anchors. Let me finalize:

**Comparison Summary**:
- **"An undetectable watermark" (PRC, 6.50)**: The direct baseline. Had notable weaknesses: inferior robustness to Gaussian Shading/StegaStamp, undetectability only tested with ResNet-18, FID computed on only 500 images, significant content changes. The paper under review directly addresses PRC's key limitation (computational overhead — 4 orders of magnitude faster), provides stronger theory (spherical 3-design vs. PRC's loose bound), has more comprehensive evaluation, and achieves better robustness.
- **"Shallow Diffuse" (6.00)**: Training-free watermarking but limited evaluation, incremental over Tree-Ring, poor presentation, only 4 fixed-parameter attacks. Our paper is clearly stronger.
- **"Hidden in the Noise" (5.83)**: Two-stage watermarking, limited to one diffusion model, unclear theory, missing experimental details. Our paper substantially exceeds this.

The paper under review is clearly stronger than all these anchors. Its combination of rigorous theory, comprehensive experiments, practical efficiency gains, and honest limitations puts it solidly in the **7.0–7.5** range. The remaining weaknesses (l_c specification gap, imprecise terminology, Gaussian Shading comparison nuance) are minor and addressable.

---

## Summary
Spherical Watermark proposes a lossless watermarking framework for diffusion models that maps binary watermarks into Gaussian noise without requiring per-image cryptographic keys. The method uses three stages: (1) a binary embedding module that mixes repeated watermark bits with random padding via an invertible matrix T to produce a 3-wise independent bitstream, (2) a spherical mapping module that normalizes bits to the unit sphere, applies an orthogonal rotation, and scales by a chi-square-distributed radius to recover Gaussian noise, and (3) diffusion integration. The paper proves the watermarked noise is a spherical 3-design (matching Gaussian moments up to degree 3) and demonstrates through experiments that it is empirically indistinguishable from standard Gaussian noise while offering extraction speeds ~4 orders of magnitude faster than PRC Watermark.

## Strengths
- **Rigorous theoretical decomposition**: The paper cleanly decomposes the embedding pipeline into four stages with provable properties at each — 3-wise independence (Theorem 3.1), spherical 3-design (Theorem 3.2), rotation invariance (Lemma 3.3), and chi-square scaling (Lemma 3.4). This structured chain of reasoning is interpretable and independently verifiable, and the connection between 3-wise independent binary codes and spherical 3-designs is a novel theoretical insight not present in prior lossless watermarking work.
- **Practical advantages over prior lossless methods**: The method eliminates per-image key storage and cryptographic overhead, using only two fixed pre-computed matrices (T and C). Extraction is roughly four orders of magnitude faster than PRC Watermark (Figure 4), and the self-inverse property T⁻¹ = T over 𝔽₂ simplifies implementation.
- **Comprehensive undetectability evidence**: The paper validates undetectability through FID scores statistically indistinguishable from unwatermarked baselines across four model/dataset combinations (Table 1), latent-level MLP classifiers achieving only chance accuracy (Figure 2, left), and image-level ResNet-18 classifiers similarly failing to distinguish watermarked images (Figure 2, right). This three-pronged evaluation is more thorough than what prior lossless watermarking papers have reported.
- **Strong robustness under adversarial conditions**: Under WEvade adversarial attacks (Table 2), the method achieves 98.12% ACC and 99.83% TPR, outperforming PRC Watermark (97.69% ACC) and Gaussian Shading (88.06% ACC). The method also sustains high detection rates across the full tested watermark capacity range unlike PRC Watermark, which fails beyond l_m = 2000 (Figure 6a).
- **Thorough ablation studies**: Figure 6(b–c) provides direct causal evidence that both the binary embedding and spherical mapping modules are necessary, each addressing distinct requirements (independence vs. robustness). Tables 4–5 show robustness to ODE solver choice and timestep counts. Table 3 demonstrates expected tradeoffs between sparsity s and robustness with clear trends.
- **Honest treatment of limitations**: Section 5 explicitly acknowledges the spherical 3-design gap (higher-order moments may deviate), vulnerability to strong inversion-breaking attacks, and scope limitations regarding editing/forgery scenarios.

## Weaknesses

### Fatal
None.

### Major
- **Rotation matrix dimension is underspecified (l_c gap between theory and practice)**. Equation (10) and the theoretical analysis in Section 3.3 assume C ∈ ℝ^{l_x × l_x} operates directly on the full l_x-dimensional vector. However, footnote 1 states that in practice l_c = ⌊√l_x⌋ (≈128 for l_x = 16384) for computational and storage efficiency. How a 128×128 rotation matrix is applied to a 16384-dimensional vector is never described — is it applied block-wise, tiled, or is some other construction used? The theoretical analysis assumes a full-dimensional orthogonal transformation; the paper needs to specify the practical construction and confirm whether the theoretical guarantees (spherical 3-design, rotation invariance) carry over under the practical l_c < l_x scheme.

### Minor
- **Gaussian Shading comparison omits the original (per-image-key) version as a reference**. The paper explicitly notes that "with fixed keys, Gaussian Shading no longer achieves true losslessness" (line 193) and uses this degraded version as the baseline. While the paper's motivation — that per-image key storage is impractical — is reasonable, including the original Gaussian Shading's performance as a reference row would let readers assess the concrete fidelity/robustness tradeoff of eliminating per-image keys.
- **"Encryption-free" terminology is imprecise**. The method still relies on a secret signature K = {T, C} that "is kept fixed and secret during runtime to prevent unauthorized removal" (Section 3.2). The genuine contribution — eliminating per-image cryptographic operations (stream ciphers, PRCs) — is better captured by phrasing like "cryptography-free" or "eliminating per-image key management," since the scheme does maintain a fixed secret.
- **Introduction slightly overstates the theoretical guarantee**. Line 26 states "we theoretically analyze each intermediate distribution and prove that the final noise is statistically indistinguishable from standard Gaussian noise." What is proved is a spherical 3-design (moment matching up to degree 3), which is a weaker property than distributional indistinguishability. The abstract and Section 5 qualify this properly, but the introduction's phrasing should match what the theorems actually establish.

### Trivial
- **The negl(ρ) cryptographic framing in Section 3.1 is decorative**. The problem formulation uses negl(ρ) and references a security parameter ρ, but the actual construction does not instantiate a security parameter — the "negligible" error comes from majority-vote decoding, not computational hardness. This framing does not harm correctness but adds unnecessary formalism.
- **TPR@1%FPR abbreviated as "TPR"** may cause momentary confusion with standard True Positive Rate, though it is clearly defined in Section 4.1.

## Nice-to-Haves
- Including an empirical higher-order moment test (e.g., kurtosis of linear projections or a Mardia-type multivariate kurtosis test) would directly probe the gap between the 3-design guarantee and full distributional match, complementing the classifier-based undetectability tests.
- Reporting the storage footprint of the signature K = {T, C} for the experimental settings would help practitioners assess deployment costs.

## Removed Points
These points are flagged to be removed, treat them with caution:

- **Harsh Critic: rotation matrix breaks 3-wise independence across blocks.** The harsh critic speculates that block-wise application of C "would introduce cross-block dependencies not accounted for in the 3-wise independence analysis." This is speculation about an unspecified construction; the paper's theoretical analysis uses l_c = l_x and is internally consistent. The specification gap is real but the claim that it breaks the theory is unverified.
- **Harsh Critic: abstract claims distributional indistinguishability theoretically.** The abstract says "We theoretically prove that the watermarked noise distribution preserves the target prior up to third-order moments, and empirically demonstrate that it is statistically indistinguishable." This correctly scopes theory to third-order moments and attributes indistinguishability to empirical demonstration. The harsh critic's reading is incorrect.
- **Harsh Critic: PRC "fails under strong attacks" is unsubstantiated.** The harsh critic cites PRC's 97.69% ACC under adversarial attack as evidence the claim is wrong. The paper's claim refers to attacks "exceeding the code's designed distortion bounds," and the paper's own experiments show PRC degrading to 93.52% under post-processing and failing beyond l_m = 2000 under JPEG-70 — supporting the claim.
- **Harsh Critic: classifier-based undetectability tests use "modest classifiers."** The fact that modest classifiers detect other methods at 97-100% accuracy but fail on this method at chance level is strong evidence, not weak evidence. More powerful classifiers might also fail given the spherical 3-design property.
- **Harsh Critic: Figure 4 lacks exact timing numbers.** The figure includes approximate values and the text explicitly states "roughly four orders of magnitude." The paper's claim is about orders of magnitude and the figure supports this adequately.
- **Harsh Critic: extraction uses different guidance scale than generation.** The mismatch (guidance 7.5 for generation, 1.0 for inversion) is standard practice for DDIM inversion in diffusion watermarking; not a weakness of this paper specifically.
- **Harsh Critic: no comparison with Wei et al. 2024.** The paper explicitly states Wei et al.'s methods are "limited to merely verifying the presence of watermark, not supporting large-scale provenance" (lines 32-33). Comparing against detection-only methods for a bit-extraction paper is inappropriate.
- **Strength Finder: "addressed an important problem."** Removed as generic — not a concrete, paper-specific strength.

## Novel Insights
None beyond the paper's own contributions. The theoretical connection between 3-wise independent binary codes and spherical 3-designs is the paper's novel contribution and is well-developed.

## Suggestions
- Specify exactly how the rotation matrix C of dimension l_c × l_c (with l_c < l_x) is applied in practice, and confirm whether the theoretical guarantees require modification for that case.
- Calibrate the introduction's theoretical claim (line 26) to match what is proved: replace "statistically indistinguishable" with precise language about moment matching up to degree 3, and reserve the indistinguishability claim for the empirical evidence.
- Report the original Gaussian Shading (with per-image keys) as a reference row in Tables 1–2 to let readers assess the fidelity/robustness cost of eliminating per-image keys.
- Consider replacing "encryption-free" with a more precise term like "cryptography-free" or stating the contribution as "eliminating per-image key management."

## Score and Decision

### Calibration Anchors

| Paper | Avg Score | Round | Comparison |
|-------|-----------|-------|------------|
| "A Recipe for Watermarking Diffusion Models" | 5.33 | R1 | Empirical recipe, limited novelty, PSNR <30dB, only 3 distortion types. Our paper substantially exceeds this. |
| "Hidden in the Noise: Two-Stage Robust Watermarking" | 5.83 | R1 | Two-stage detection-only framework, one model, unclear theory. Our paper has stronger theory, broader evaluation, and bit-level extraction. |
| "Shallow Diffuse" | 6.00 | R2 | Training-free, limited attacks (4 fixed-parameter), incremental over Tree-Ring. Our paper has more comprehensive evaluation and stronger theory. |
| "An undetectable watermark for generative image models" (PRC) | 6.50 | R2 | Direct baseline. Weaker robustness, inferior efficiency, looser theory. Our paper addresses PRC's key limitations and provides stronger theoretical grounding. |
| "TabWak: A Watermark for Tabular Diffusion Models" | 7.20 | R2 | Different domain (tabular data). Comparable quality but hard to directly compare. |

**Round 1 bracket**: 6.5–8.0. The paper clearly exceeds the 5.33–5.83 anchors and the 6.0–6.5 anchors on theoretical depth, experimental breadth, and practical impact.

**Round 2 narrowing**: The paper is stronger than the PRC watermark paper (6.50) — which it directly improves upon — in almost every dimension: better theory, faster extraction by 4 orders of magnitude, more comprehensive evaluation, better robustness under adversarial attacks. It sits clearly above 6.50. The remaining issues (l_c specification, terminology, Gaussian Shading reference) are minor and addressable.

**Final score: 7.0**. The paper makes a solid, well-executed contribution with a novel theoretical framework, strong empirical results, and practical advantages. The specification gap regarding the rotation matrix dimension and minor imprecisions in framing prevent it from scoring higher, but these do not undermine the core contributions.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>