Now I have all the information needed. Let me construct the final calibration analysis and produce the review.

**Round 1 Bracket:**
- Weak anchors (<3.5): avg scores 3.00-3.20 — clearly below the current paper
- Middle anchors (3.5-7.5): avg scores 3.75-5.83 — the current paper is stronger than most of these
- Strong anchors (>7.5): avg scores 7.60-8.00 — not at this level

**Initial bracket:** [5.0, 7.0]

**Round 2 Narrowing:**
- PRC watermark paper (jlhBFm7T2J, avg 6.50, Accept): Most comparable. The current paper has a truly novel theoretical approach (spherical 3-design) vs PRC's adaptation of cryptographic codes. The current paper is stronger empirically (robustness, speed) but overclaims its theoretical guarantee compared to PRC's more rigorous cryptographic proof.
- Shallow Diffuse (1IwoEFyErz, avg 6.00, Reject): Less novel than current paper (limited improvement over Tree-Ring).
- SAT-LDM (ETFfXGM3e4, avg 5.50, Reject): Training-based, less relevant.

The current paper is clearly above the 5.33-5.83 range but below the PRC paper's 6.50 (due to the overclaiming issue and figure-text mismatch). Final score: **6.0**.

Here is my final review:

## Summary
Spherical Watermark proposes an encryption-free, lossless watermarking scheme for diffusion models. It replaces per-image key storage (required by Gaussian Shading) and heavy cryptographic decoding (required by PRC) with a fixed signature built from a binary embedding matrix and an orthogonal rotation. Watermark bits are mixed with random padding, projected onto the unit sphere, rotated, and scaled by a chi-square radius. The paper proves third-order moment matching with standard Gaussian via spherical 3-designs and reports strong empirical results: near-chance detectability, FID scores matching unwatermarked output, 99.83% TPR@1%FPR under adversarial attacks, and ~4 orders of magnitude faster extraction than PRC.

## Strengths
1. **Novel theoretical grounding via spherical 3-designs:** The paper connects watermarking to spherical t-design theory (Definition 3.1, Theorem 3.2), proving that the mapped points on the unit sphere match uniform moments up to degree 3. This is a genuinely novel mathematical foundation absent in prior lossless watermarking work, providing formal abstraction for why the watermarked noise resists low-order statistical tests. (Section 3.3)

2. **Elimination of per-image key management:** The encryption-free design uses a fixed, secret Signature (matrices T, C) built once during an offline phase, avoiding the impractical per-image key/nonce storage required by Gaussian Shading. This is a concrete practical improvement for real-world deployment. (Section 3.2 Build Phase)

3. **Strong empirical undetectability:** Binary classifiers (two-layer MLP on latents, ResNet-18 on images) achieve near-chance accuracy (~50%) when distinguishing watermarked from unwatermarked samples (Figure 2), and FID scores are virtually identical to the unwatermarked baseline across two datasets and two model versions (Table 1, Ours FID: 48.12 vs Original 48.13 on COCO SD v1.5).

4. **Orders-of-magnitude faster extraction than PRC:** By avoiding belief-propagation decoding, Spherical Watermark achieves extraction times roughly 4 orders of magnitude faster than PRC Watermark (~10^1 s → ~10^{-3.5} s) (Figure 4).

5. **Superior robustness under adversarial attacks:** The method achieves 99.83% TPR@1%FPR under the WEvade attack, outperforming PRC Watermark (95.38%) and Gaussian Shading (99.23%) (Table 2). The paper provides theoretical justification (Appendix E) for why lossless methods are inherently robust to adversarial detection.

6. **Comprehensive ablation study:** Ablations confirm that binary embedding provides necessary independence (removing it makes noise trivially detectable, Figure 6b) and spherical mapping provides robustness (removing it collapses performance under brightness changes, Figure 6c). Parameter sensitivity is explored across s, N, l_m, and ODE solvers (Tables 3, 4, 5).

7. **Sustained accuracy at large capacities:** Under JPEG-70 compression, the method maintains nearly 100% accuracy even beyond 2000-bit watermark lengths, while PRC Watermark collapses (Figure 6a).

## Weaknesses

### Fatal
None.

### Major
1. **Overclaimed losslessness guarantee relative to what is proven.** The paper defines losslessness via computational indistinguishability (Eqs. 2-3: `|Pr[A(z_w)=1] - Pr[A(z)=1]| ≤ negl(ρ)`) and the Section 3.3 header states "the final latent code z_w is distributed as N(0, I_lx)." However, the actual theoretical analysis only proves that z^{(2)} is a spherical 3-design (Theorem 3.2), which is an *approximation* to the uniform spherical distribution, not exact uniformity. Lemma 3.4 correctly uses ≈: "z_w = r z^{(3)} ≈ N(0, I_lx)." The problem is that a spherical 3-design guarantees third-order moment matching, which is neither necessary nor sufficient for the computational indistinguishability defined in Eqs. 2-3 — a polynomial-time adversary could exploit higher-order moment differences. This gap between the claimed guarantee (cryptographic-level losslessness) and the actual proof (third-order moment matching) is structural and affects the paper's central narrative. The paper should reframe "losslessness" as "provable third-order moment matching with strong empirical undetectability."

2. **Mismatch between textual undetectability claims and Figure 2.** The text (Section 4.2) states: "According to Figure 2, both Tree-Ring and Gaussian Shading (with fixed keys) are easily detected with accuracies of 100% and 97%." However, the Figure 2 caption (lines 217-219) only describes curves for "True Ring" and "PRC watermark" — with no mention of Gaussian Shading or the proposed method. The reported accuracy numbers (100%, 97%) cannot be mapped to any labeled curve in the caption. This discrepancy undermines the credibility of the undetectability evaluation and needs immediate correction.

### Minor
3. **Asymmetric baseline comparison for Gaussian Shading.** The paper evaluates Gaussian Shading with fixed keys and explicitly notes that "with fixed keys, Gaussian Shading no longer achieves true losslessness" (line 193). The resulting 97% detectability is then used as evidence of GS's inferiority. This places GS in a deliberately weakened configuration while Spherical Watermark operates in its intended configuration. A fairer comparison would report GS with per-image keys as a reference upper bound on undetectability, or at least quantify the undetectability cost of fixing the key.

4. **Imprecise description of extraction process.** The paper states (line 153): "The first l_{Nm} entries of x̂ correspond to N repeated copies of the watermark message." Given the block structure of T = [[I, R], [0, I]] and T^{-1} = T over F_2, the recovered first entries are ẑ^{(1)}_{1:l_m} + R·ẑ^{(1)}_{l_m+1:} (mod 2). The cancellation of the R term depends on the padding segment being recovered *exactly*; the paper does not discuss this cancellation or bound the noise from inversion errors on the padding. While empirical results suggest the majority vote handles this, the explanation is incomplete.

### Trivial
5. **Theoretical vs. practical rotation matrix dimensions.** The theoretical analysis assumes l_c = l_x for the orthogonal rotation C, but the footnote (line 121) states that in practice l_c = floor(sqrt(l_x)). The impact of this reduced-dimensional rotation on the spherical 3-design property is not analyzed; the rotation on a lower-dimensional subspace may not preserve the 3-design guarantee in the full space.

## Nice-to-Haves
- Run higher-order statistical tests (e.g., Mardia's multivariate normality test, fourth-order cumulant tests) on the latent noise to strengthen the empirical undetectability case beyond a single MLP classifier.
- Discuss the security model if the secret Signature K is leaked — the method becomes completely invertible, so a threat model and possible mitigations would be valuable.
- Explicitly discuss the information rate trade-off (512/16384 ≈ 3%) and how capacity, redundancy, and robustness interact.
- Extend experiments to a non-Stable-Diffusion model family to demonstrate generality beyond SD v1.5 and v2.1.

## Removed Points
- Missing related works: Cannot verify; not included per instructions.
- Typos/formatting issues: Parser artifacts, not author errors.
- Reproducibility concerns about undisclosed hyperparameters: The paper provides substantial implementation details.
- Speculative concerns lacking paper evidence: e.g., what "could" go wrong without being grounded in specific paper content.
- Appendix content missing: Parser strips appendices from all papers.
- Security model concern about K leakage (as a weakness): This is an assumption of the method (signature is kept secret), not a flaw. Moved to nice-to-have.
- Capacity rate criticism (3% being "very low"): This is inherent to the design choice of redundancy for robustness, acknowledged via ablation.
- Generic/superficial strengths from Strength Finder: e.g., "addressed an important problem" — removed.
- Strength about "Rigorous theoretical guarantee of distribution preservation": Tempered — the guarantee is rigorous for third-order moments but falls short of the paper's stronger claims.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. Reframe "losslessness" throughout to match what is actually proven: "provable third-order moment matching with empirical undetectability" rather than claiming full computational indistinguishability.
2. Fix Figure 2: ensure all discussed methods (Tree-Ring, Gaussian Shading, PRC, Ours) appear with consistent labels matching the text, and update the caption accordingly.
3. Add a reference experiment for Gaussian Shading with per-image keys to quantify the undetectability cost of fixed-key usage.
4. Expand the extraction description to explicitly show how the R-mask cancels in the noiseless case and discuss the impact of inversion noise on padding recovery.
5. Add higher-order statistical normality tests on the latent noise to strengthen empirical undetectability.

## Score and Decision

**Calibration Anchors:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| jbfDg4DgAk.md (Sparse Watermarking LLMs) | 3.00 | R1 | Much weaker, unclear methodology |
| fkNsgI1nye.md (Secure Diffusion Inference) | 3.00 | R1 | Different topic, weaker |
| QKqWnNkwPL.md (Self-distillation) | 3.00 | R1 | Not watermarking |
| vK8C37eHXM.md (Sample what you can't compress) | 3.20 | R1 | Not watermarking |
| HexshmBu0P.md (Recipe for Watermarking DMs) | 5.33 | R1, R2 | Less novel "recipe" paper; current paper stronger |
| T0ebbDO60R.md (SuperMark) | 3.75 | R1 | Different approach; current paper stronger |
| ll2nz6qwRG.md (WIND - Hidden in the Noise) | 5.83 | R1, R2 | Accepted; less theoretical novelty; current paper comparable or stronger |
| uHdf9F1tY4.md (DiffusionShield) | 5.50 | R1 | Training-based; different setting |
| jlhBFm7T2J.md (PRC - Undetectable Watermark) | 6.50 | R2 | Most comparable; has rigorous cryptographic guarantee but heavy overhead; current paper more novel approach but weaker guarantee claim |
| 1IwoEFyErz.md (Shallow Diffuse) | 6.00 | R2 | Good but limited novelty over Tree-Ring; current paper more novel |
| ETFfXGM3e4.md (SAT-LDM) | 5.50 | R2 | Training-based; less relevant |

**Round 1 Bracket:** [5.0, 7.0]
**Round 2 Narrowing:** The most directly comparable anchor (PRC paper at 6.50, Accept) has a more rigorous theoretical guarantee but worse efficiency and robustness. The current paper is more novel in its approach but overclaims its theoretical guarantee, placing it slightly below the PRC anchor. Above the Shallow Diffuse anchor (6.00) due to greater novelty. Final position: **6.0**.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>