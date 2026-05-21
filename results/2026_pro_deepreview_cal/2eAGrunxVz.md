Now I have a thorough understanding of the paper and the calibration anchors. Let me write the consolidated review.

## Summary
This paper introduces Spherical Watermark, a training-free watermarking framework for diffusion models that maps binary watermarks into Gaussian noise via a three-stage pipeline: (1) a binary embedding matrix that mixes repeated watermark bits with random padding, (2) normalization onto the unit sphere followed by orthogonal rotation, and (3) chi-squared scaling. The authors prove that the resulting watermarked noise matches a standard Gaussian up to third-order moments (spherical 3-design), and they provide empirical evidence of distributional indistinguishability through FID preservation and classifier-based undetectability tests. The method eliminates per-image key storage, outperforms the PRC Watermark baseline in robustness and computational efficiency (extraction is ~4 orders of magnitude faster), and demonstrates strong tracing accuracy under diverse attacks.

## Strengths
- **Novel and elegant encoding pipeline.** The combination of a carefully designed binary embedding matrix (Theorem 3.1: 3-wise independence via disjoint padding subsets) with spherical normalization, secret rotation, and chi-squared scaling is genuinely original. The design is invertible by construction, enabling efficient extraction via majority-vote decoding across N repeated blocks.
- **Strong empirical evidence for undetectability.** FID values are nearly identical to the unwatermarked baseline across two diffusion backbones and two prompt datasets (e.g., 48.12 vs. 48.13 for SD v1.5 on COCO in Table 1). Latent-level MLP and image-level ResNet-18 classifiers achieve near-chance accuracy (~50%), while competing lossless methods (Tree-Ring, Gaussian Shading with fixed keys) are easily detected (Figure 2). This is convincing evidence that the method preserves the latent distribution in practice.
- **Comprehensive robustness and ablation studies.** The method is evaluated under eight attack types (Table 2, Figure 5), consistently exceeding 95% accuracy after JPEG, blur, and brightness perturbations, and maintaining 98.12% under adversarial attack (WEvade). Module-level ablations (Figures 6b–c) confirm that both the binary embedding and spherical mapping are individually necessary. Hyperparameter sensitivity is thoroughly examined across padding length, sparsity, repetition count, ODE solvers, and timestep schedules (Tables 3–5).
- **Significant practical advantages over PRC Watermark.** Extraction is approximately four orders of magnitude faster (Figure 4). Capacity scaling is dramatically better: PRC Watermark fails beyond l_m = 2000 while Spherical Watermark maintains high detection rates (Figure 6a). Robustness under strong distortions shows larger margins over PRC (Figure 5).

## Weaknesses

### Major
None.

### Minor
- **Theoretical guarantee is moment-matching, not full distributional equivalence.** The proofs establish that the watermarked noise forms a spherical 3-design, matching the Gaussian prior up to third-order moments (Theorems 3.1–3.2, Lemma 3.3–3.4). A spherical 3-design is a discrete set of points; sampling from it does not yield a continuous uniform distribution on the sphere. Consequently, the product with a chi-squared radius does not provably yield an exact standard multivariate Gaussian — only one whose first three moments match. The paper acknowledges this in Section 5 ("higher-order moments may deviate from the true prior"), but the title and framing as "lossless" overstate the theoretical strength relative to methods like Gaussian Shading that have full distributional guarantees via cryptographic sampling. The empirical evidence largely fills this gap, but the claim of provable losslessness should be qualified.
- **Formal security parameter ρ is stated but never instantiated.** Section 3.1 defines undetectability and traceability in terms of a security parameter ρ with negligible functions (Eqs. 2–4). No concrete value or bound for ρ is provided, and the remainder of the paper makes no connection between the theoretical or empirical results and this formal definition. Either ρ should be concretely defined or the formal definition should be softened to match what is actually proved and tested.
- **Practical dimensionality reduction for C is under-explained.** Footnote 1 states that in practice l_c = ⌊√l_x⌋ (e.g., 128 vs. 16384 latent dimensions) to balance expressiveness with efficiency. The theoretical analysis assumes l_c = l_x, and the paper does not analyze how the spherical-design properties are affected when the rotation operates in a substantially lower-dimensional subspace. The storage implications of full-size C are appropriately noted through this design choice, but a brief justification of why the reduced dimension still suffices would strengthen the presentation.

### Trivial
- The undetectability classifier evaluation uses only MLP and ResNet-18. While these show strong results, testing with a statistical two-sample test (e.g., MMD) could further corroborate the indistinguishability claim. This does not weaken the existing evidence, which is already strong.

## Nice-to-Haves
- A kernel two-sample test (e.g., MMD with RBF kernel) on the latent vectors would complement the classifier-based undetectability results and more directly test for higher-order moment deviations.
- Analysis of how the reduced practical dimension l_c = ⌊√l_x⌋ affects the spherical-design moment-matching guarantees.
- A table reporting the concrete storage cost of the signature H = (T, C) at the practical dimension would help readers assess deployment feasibility.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **Harsh Critic: "The mapping does not yield standard Gaussian noise, and the proof does not establish it."** — REMOVED as a Fatal/Major claim. The paper does NOT claim to prove exact Gaussianity; it proves moment matching up to degree 3 (spherical 3-design) and presents the polar decomposition lemma (Lemma 3.4) as the framework for understanding why the noise approximates a Gaussian. Section 5 explicitly acknowledges that higher-order moments may deviate. The distinction between proven theory and empirical evidence is clearly maintained. This is retained as a Minor weakness about framing, not a fatal flaw.
- **Harsh Critic: "The undetectability evaluation is insufficient — MLP and ResNet-18 have limited capacity."** — REMOVED as a standalone major criticism. These are standard classifier choices for this type of evaluation. The FID results provide complementary distribution-level evidence. The classifiers achieving ~50% accuracy while easily detecting competing methods is informative. This is moved to Trivial.
- **Harsh Critic: "Figure 5's legend is confusing ('Our' vs. 'Diffusion')."** — REMOVED. This is a PDF parser artifact; the extracted figure caption auto-generated these labels. The original paper likely has clear labels.
- **Harsh Critic: "Storage footprint of C at full size would be enormous (~1 GB)."** — REMOVED as inaccurate. The paper explicitly addresses this in Footnote 1 with the practical choice l_c = ⌊√l_x⌋. The harsh critic's calculation ignores this footnote.
- **Harsh Critic: "Attack configurations not itemized clearly."** — REMOVED. The paper states that attack details are provided in Appendix F.4 and F.5. The parser stripped appendices; this information exists in the original submission.
- **Strength Finder: "Rigorous theoretical analysis proves exact Gaussian recovery."** — MODIFIED. The theoretical analysis is solid but proves moment matching, not full distributional equivalence. The strength is retained in qualified form.
- **Strength Finder: "The method's Fréchet Inception Distance matches that of the unwatermarked model."** — RETAINED. This is accurate and well-supported by Table 1.

## Novel Insights
The paper's most genuinely novel insight is the use of a spherical 3-design — mediated by a carefully constructed binary embedding matrix that achieves 3-wise independence — as a bridge between discrete watermark bits and continuous Gaussian noise, without requiring per-image cryptographic keys. Prior lossless methods (Gaussian Shading, PRC) rely on stream ciphers or pseudorandom codes to sample noise that is exactly Gaussian; this paper instead constructs an approximately Gaussian distribution through deterministic geometric transformations, trading exact distributional equivalence for dramatically simpler extraction and stronger empirical robustness. The discovery that matching only up to third-order moments is sufficient for practical undetectability (as validated by FID and classifier tests) while enabling orders-of-magnitude faster extraction is a valuable finding for the community.

## Suggestions
- Reframe the "lossless" terminology to "distribution-preserving" or "moment-preserving" to accurately reflect what is theoretically proven (third-order moment matching) vs. what is empirically demonstrated (statistical indistinguishability). This would not weaken the contribution and would preempt the most significant criticism.
- Either concretely instantiate the security parameter ρ in Section 3.1 with actual bounds derived from the scheme's dimensions, or replace the formal cryptographic-style definition with a more appropriate information-theoretic or statistical formulation.
- Include a brief analysis (even a paragraph) on why the reduced practical rotation dimension l_c = ⌊√l_x⌋ does not compromise the moment-matching properties or image quality. Alternatively, report results with l_c = l_x for a small subset of experiments to validate the approximation.
- Add an MMD or similar two-sample test result on the latent vectors to complement the classifier-based undetectability evidence.

## Score and Decision

**Calibration summary:**

| Paper | Avg Score | Round | Comparison |
|-------|-----------|-------|------------|
| SuperMark | 3.75 | 1 | Our paper is substantially stronger — much better image quality, theoretical analysis, and evaluation breadth |
| A Recipe for Watermarking DMs | 5.33 | 1 | Our paper has more novelty (novel encoding pipeline vs. empirical recipe), better fidelity results |
| SAT-LDM | 5.50 | 1 | Different paradigm (training-based); our paper is training-free with competitive results |
| Hidden in the Noise (WIND) | 5.83 | 1,2 | Our paper has more comprehensive evaluation (2 models, 2 datasets), theoretical analysis, and broader attack coverage |
| Shallow Diffuse | 6.00 | 2 | Our paper has better evaluation (8 attack types vs. 4), more thorough ablations, better presentation |
| An undetectable watermark (PRC) | 6.50 | 2 | Our paper directly improves upon this: 4× faster extraction, better robustness, better capacity scaling; similar theoretical depth |
| TabWak | 7.20 | 2 | First-of-its-kind contribution in a new domain; our paper is strong but operates in a more crowded space; TabWak is a stronger contribution for its novelty premium |

**Round-1 bracket:** 5.5–7.5 (anchored between Hidden in the Noise at 5.83 and TabWak at 7.20).

**Round-2 narrowing:** The paper's closest comparator is "An undetectable watermark" (PRC) at 6.50, which it directly improves upon in robustness, efficiency, and capacity. The paper is clearly above the 5.5–6.0 range (Hidden in the Noise, Shallow Diffuse) and below the 7.0+ range (TabWak's first-of-its-kind novelty premium). The theoretical framing overstatement (calling moment-matching "lossless") and the uninstantiated security parameter prevent it from reaching TabWak-level strength. Score: **6.5**.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>