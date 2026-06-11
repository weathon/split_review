Now I have all the information needed. Let me write the final review.

## Summary
Spherical Watermark proposes an encryption-free, lossless watermarking framework for diffusion models that converts binary watermark bits into approximately Gaussian noise through a pipeline of binary embedding (mixing with random padding), projection onto the unit sphere, orthogonal rotation, and chi-square scaling. The method eliminates per-image key storage requirements of prior lossless schemes while achieving near-perfect undetectability (FID matching original output, ~50% classifier detection accuracy), superior adversarial robustness (99.83% TPR under WEvade attacks), and ~4 orders of magnitude faster extraction than PRC Watermark.

## Strengths
- **Novel and elegant design with strong practical payoff**: The pipeline from binary bits → unit sphere → orthogonal rotation → chi-square scaling is mathematically clean. The key insight (Eq. 13) that chi-square scaling preserves sign patterns, enabling lossless extraction via simple rounding without complex decoding, is a genuine design contribution that yields dramatic speedup.
- **Empirical indistinguishability convincingly demonstrated**: Table 1 shows FID of 48.1224 vs 48.1256 for unwatermarked output (COCO/SD v1.5); Figure 2 shows both latent-level and image-level classifiers achieve ~50% accuracy (chance level), while Tree-Ring (100%) and Gaussian Shading (97%) are detected. These results directly support the losslessness claim.
- **Significant computational efficiency gain**: Figure 4 shows extraction time ~10⁻³·⁵s vs ~10¹·⁰s for PRC Watermark — roughly four orders of magnitude faster due to eliminating belief-propagation decoding. This is a substantial practical advantage.
- **Superior adversarial robustness**: Table 2 shows 98.12% ACC and 99.83% TPR under adversarial WEvade attacks, outperforming all baselines including PRC Watermark (97.69%/95.38%) and lossy methods that collapse (e.g., RivaGAN: 52.31%/26.75%).
- **Eliminates a real deployment bottleneck**: Fixed signature K = {T, C} replaces per-image key management, addressing a genuine practical challenge identified in Gaussian Shading.
- **Comprehensive ablations**: Figures 6(b)-(c) cleanly isolate module contributions; Tables 3-5 ablate sparsity s, repetition count N, ODE solvers, and timestep schedules, confirming the method is robust across configurations.

## Weaknesses

### Fatal
None.

### Major
- **Gap between theoretical claim and proof for Gaussian indistinguishability**: The abstract states the procedure "recovers exact multivariate Gaussian noise" (line 9), and the theoretical analysis (Section 3.3) claims z_w is "distributed as N(0, I_{l_x})" (line 157). However, the proof chain establishes that z⁽²⁾ is a spherical 3-design (matching moments up to degree 3, Theorem 3.2), not an exact uniform distribution on the sphere. Lemma 3.4's polar decomposition result assumes exact uniformity of u on S^{n-1}, but z⁽³⁾ is only a spherical 3-design. The paper does not bound higher-order moment deviation or formally establish computational indistinguishability from the 3-design property alone. Section 5 acknowledges "higher-order moments may deviate from the true prior," but the theoretical framing in the abstract and Section 3.3 overclaims relative to what is proven. The empirical evidence (classifier experiments, FID) strongly supports practical indistinguishability, but the theoretical contribution should be precisely scoped: the proof guarantees third-order moment matching, with the stronger Gaussian claim resting on empirical evidence plus the reasonable heuristic that l_x = 16384 suffices.

- **Gaussian Shading comparison uses a deliberately degraded variant**: The paper states "with fixed keys, Gaussian Shading no longer achieves true losslessness" (line 193). Since Gaussian Shading was designed around per-image keys/nonces, freezing these breaks its lossless guarantee — its stream cipher produces correlated outputs. This means the undetectability comparison (97% detected, Figure 2) and adversarial robustness comparison (ACC=88.06, Table 2) are against a crippled version of the strongest baseline. The paper's systems-level argument (per-image key management is impractical) is defensible, but the paper does not clearly frame this as a comparison of deployment-ready configurations rather than a method-level comparison. An explicit framing statement would prevent misleading conclusions.

### Minor
- **Storage cost of fixed signature not quantified**: The paper's key practical argument is eliminating per-image key storage, but does not report the actual storage footprint of the fixed signature (T and C). T is sparse and can be stored compactly, but C is a dense l_c × l_c orthogonal matrix (128×128 or l_c = ⌊√l_x⌋ per footnote 1). Quantifying this would complete the practical deployment argument.

- **Same-user multi-image attack not discussed**: When the same user generates multiple images with the same watermark bits, an adversary with access to multiple watermarked images can potentially average out noise and recover the watermark more easily. This is a standard concern in watermarking and deserves at least a brief discussion.

### Trivial
None.

## Nice-to-Haves
- A quantitative bound on higher-order moment deviation (even a loose one showing it is negligible at l_x = 16384) would substantially strengthen the theoretical contribution.
- Brief summary of the losslessness→robustness argument from Appendix E in the main text would improve internal coherence.
- Discussion of the gap between l_c < l_x (used in practice per footnote 1) and the l_c = l_x case analyzed in the theory.

## Removed Points
These points are flagged to be removed, treat them with caution:
- Harsh critic's claim that tracing accuracy is "only presented for COCO + SD v2.1" without acknowledging Figure 5: Figure 5 explicitly shows "ACC and TPR values under Attacks, averaged over two datasets and two models" (line 281), so robustness results do cover all settings in aggregated form. The criticism is partially valid for Table 2 but overstated.
- Harsh critic's notation inconsistency (Eq. 6): Appears to be a parser formatting artifact; the paper uses consistent notation internally.
- Strength Finder's claim about "rigorous theoretical chain": The theoretical chain is well-structured but has a genuine gap (3-design vs exact uniform), so calling it "rigorous" overstates the case. This strength is retained in modified form under "novel and elegant design."

## Novel Insights
The paper's most novel insight is that the polar decomposition of Gaussian noise (uniform direction × chi-square radius) can be approximated via a simple binary-to-sphere-to-rotation pipeline without cryptographic machinery. The observation that chi-square scaling preserves sign patterns — making extraction trivial via rounding regardless of the radius realization — is the key design insight that makes the whole scheme work and yields the dramatic speedup over PRC Watermark's belief-propagation decoding. Combined with the elimination of per-image key management, this represents a genuine advance in practical lossless watermarking.

## Suggestions
1. Temper the theoretical claim in the abstract from "recover exact multivariate Gaussian noise" to "approximately recover multivariate Gaussian noise" or qualify that "exact" holds through third-order moments, reserving the stronger indistinguishability claim for the empirical results.
2. Explicitly frame the Gaussian Shading comparison as comparing deployment-ready configurations (all methods under fixed keys) rather than comparing the watermarking schemes as designed.
3. Quantify the storage cost of the signature {T, C} to complete the practical deployment argument.
4. Add a brief discussion of multi-image attacks when the same user's watermark is reused.

## Reporting: Calibration Anchors

| Round | Anchor | Avg Score | Relation |
|-------|--------|-----------|----------|
| R1 | PRC Watermark (jlhBFm7T2J.md) | 6.50 | Direct competitor; Spherical WM improves on its key limitations |
| R1 | Hidden in the Noise (ll2nz6qwRG.md) | 5.83 | Similar topic; Spherical WM has stronger experiments and analysis |
| R1 | Shallow Diffuse (1IwoEFyErz.md) | 6.00 | Rejected at 6.0; Spherical WM is more novel and better evaluated |
| R1 | DIAGNOSIS (f8S3aLm0Vp.md) | 6.50 | Different problem; similar quality tier |
| R1 | SuperMark (T0ebbDO60R.md) | 3.75 | Weaker watermarking paper; Spherical WM is much stronger |
| R1 | Recipe for Watermarking (HexshmBu0P.md) | 5.33 | Rejected; less rigorous |
| R1 | Stable Signature Unstable (zqo2eKjSWH.md) | 4.50 | Attack paper; less relevant |
| R2 | TabWak (71pur4y8gs.md) | 7.20 | First in tabular domain; comparable novelty, Spherical WM has stronger experiments |
| R2 | Image Watermarks Removable (mDKxlfraAn.md) | 6.40 | Attack paper; accepted at 6.4 |
| R2 | VINE/Robust Watermarking (16O8GCm8Wn.md) | 6.40 | Benchmark paper; accepted |
| R2 | SAT-LDM (ETFfXGM3e4.md) | 5.50 | Rejected; weaker theoretical and empirical support |

**Round 1 bracket**: 6.0–8.0. Spherical WM is clearly above the 5.5–6.5 rejected/weakly-accepted papers (Shallow Diffuse 6.0R, Hidden in the Noise 5.83A) and comparable to PRC Watermark (6.50A) which it directly improves upon. TabWak (7.20A) provides an upper anchor for a "first" paper with theoretical guarantees and comprehensive experiments.

**Final narrowing**: 6.5–7.5. The paper's practical contributions (4 orders of magnitude speedup, elimination of key management, superior robustness) place it above PRC Watermark (6.50). The theoretical overclaim and degraded Gaussian Shading comparison prevent it from reaching the TabWak level (7.20). **Final score: 7.0.**

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>