Now let me write the final consolidated review.

## Calibration Summary

**Round 1 bracket (weak/mid/strong):** 
- Weak band (<3.5): kNsgI1nye (3.00), jbfDg4DgAk (3.00), vK8C37eHXM (3.20), hYEV8QmaOt (3.40) — all irrelevant or poorly scored
- Mid band (3.5–7.5): HexshmBu0P (5.33), jlhBFm7T2J/PRC (6.50), T0ebbDO60R (3.75), ll2nz6qwRG/WIND (5.83)
- Strong band (>7.5): j7b4mm7Ec9 (7.60, lightweight watermarking, reject), 84n3UwkH7b (8.00, memorization, accept)

**Round 2 narrowing (4.5–8.0):** ETFfXGM3e4/SAT-LDM (5.50), uHdf9F1tY4/DiffusionShield (5.50), 71pur4y8gs/TabWak (7.20), mDKxlfraAn (6.40)

**Final score position:** The paper is clearly stronger than the 5.33–5.83 cluster (Recipe, WIND, SAT-LDM). It is comparable to the PRC paper (6.50) but offers genuinely new theoretical machinery (spherical 3-designs) and practical advantages (encryption-free, 4× faster extraction). TabWak (7.20) is in a different domain but similarly strong on theoretical+empirical grounds. Setting the score at **7.0** reflects that this paper is slightly stronger than PRC (6.50) due to its novel theoretical framework and practical advantages, and sits comfortably below TabWak's 7.20 (which claimed "first" in its domain).

---

## Summary

This paper proposes Spherical Watermark, an encryption-free, lossless watermarking framework for diffusion models. The method maps binary watermarks to Gaussian noise through three modules: (1) a binary embedding module that mixes repeated watermark bits with random padding via an invertible matrix, (2) a spherical mapping module that projects the binary code onto the unit sphere, applies an orthogonal rotation, and scales by a chi-square-distributed radius to recover standard multivariate Gaussian noise, and (3) integration with the diffusion model's pipeline. The authors provide theoretical analysis proving the watermarked noise matches the target Gaussian prior up to third-order moments (spherical 3-design), and empirically demonstrate near-chance classification accuracy for detection, preserved FID scores, superior robustness under adversarial attacks, and roughly four orders of magnitude faster extraction than the leading lossless competitor (PRC Watermark).

## Strengths

- **Novel theoretical framework:** The paper introduces spherical 3-designs and chi-square-radius scaling to the watermarking literature for diffusion models. Theorems 3.1–3.2 and Lemmas 3.3–3.4 provide a clean, rigorous proof chain showing that the watermarked noise preserves the target Gaussian prior up to third-order moments — a formal guarantee that goes beyond what prior encryption-free lossless schemes provide.

- **Encryption-free practical design:** By using a fixed secret signature K = (T, C) — an invertible binary embedding matrix plus an orthogonal rotation matrix — the method eliminates per-image key storage and nonce management required by Gaussian Shading, and avoids the heavyweight cryptographic constructs (belief-propagation decoding) required by PRC Watermark. This is a genuine practical advantage for large-scale deployment.

- **Empirical evidence is strong and well-rounded:** The evaluation spans undetectability (latent-level MLP and image-level ResNet-18 classifiers, FID in Table 1), tracing accuracy under clean, post-processing, and adversarial conditions (Table 2), computational efficiency (Figure 4, ~4 orders of magnitude faster extraction than PRC), capacity scaling (Figure 6a), and ablations confirming the necessity of each module (Figures 6b–6c). The results consistently support the paper's claims.

- **Superior robustness under adversarial attacks:** Table 2 shows that under WEvade adversarial attacks, lossy schemes collapse (DwtDct: 16.15% TPR, RivaGAN: 26.75% TPR) while Spherical Watermark achieves 99.83% TPR@1%FPR, outperforming even PRC Watermark (95.38%) and Gaussian Shading (99.23%). This is attributed to the lossless design preventing attackers from learning effective discriminators.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Ambiguous watermark capacity description for traditional baselines.** The paper states traditional methods (DwtDct, DwtDctSvd, RivaGAN) are "configured to embed 32-bit watermarks" but then says "All schemes are evaluated with 512-bit watermarks, except Tree-Ring." These two statements appear contradictory. If traditional methods were evaluated at 32-bit while latent methods at 512-bit, comparing bit-level ACC and TPR directly (Table 2) conflates payload size with method quality. The authors should clarify whether the traditional methods were reconfigured to 512 bits or compared at their native capacity, and discuss the fairness implications.

- **"Provably indistinguishable" in the abstract overstates the theoretical guarantee.** The theory proves matching up to third-order moments (spherical 3-design), which the paper itself honestly acknowledges in Section 5 ("higher-order moments may deviate from the true prior"). The abstract's phrasing should be qualified to match the theoretical scope.

- **Undefined acronyms in Figure 5.** The figure caption and OCR text refer to "REC ACC" and "DNR ACC" without definition in the main text. The paper should define these terms, and should clarify whether "Diffusion" in Figure 5 refers to PRC Watermark (as implied by the text) or something else.

- **Ablation on modules lacks quantitative numbers.** The paper states that omitting binary embedding makes the latent noise "trivially distinguishable" (Figure 6b) and omitting spherical mapping "drops robustness dramatically" (Figure 6c), but reports no classification accuracy or TPR numbers for these ablations. Reporting the actual metrics would strengthen the analysis.

- **The 16k×16k rotation matrix cost is acknowledged but not evaluated.** The footnote mentions using a smaller l_c (e.g., floor(√l_x)) for efficiency, but all experiments use l_c = l_x. The impact of dimension reduction on the theoretical guarantees and empirical performance is not assessed.

### Trivial
None.

## Nice-to-Haves
- The authors could extend the undetectability evaluation beyond simple MLP/ResNet-18 classifiers to include statistical tests (e.g., maximum mean discrepancy) or higher-order moment tests to further validate the distributional match.
- An analysis of the maximum degree of moment deviation (beyond 3rd order) and whether it matters for any practical attack would strengthen the limitations discussion.

## Removed Points
These points were considered but removed from the main review for the reasons indicated:

1. **Figure 2 inconsistency (Harsh Critic).** The critic claimed the caption mentions only "True Ring" and "PRC watermark" while the text discusses all four methods. The figure content is an embedded image whose alt-text/OCR may not capture the full legend. Per the hard rule on parser artifacts, this is not an author-level error.

2. **Gaussian Shading with fixed keys misrepresented (Harsh Critic).** The paper explicitly states: "Note that with fixed keys, Gaussian Shading no longer achieves true losslessness." The paper does not misrepresent this — it clearly acknowledges the limitation.

3. **Computational cost of rotation matrix (Harsh Critic).** The paper acknowledges this in a footnote and mentions dimension reduction. The criticism does not identify a concrete error in the paper.

4. **Reproducibility/random seeding (Harsh Critic).** The request to specify how randomness is seeded is a minor implementation detail that goes beyond standard expectations for a conference paper.

5. **Statistical significance / zero variance results (Harsh Critic).** The near-zero std values are standard for deterministic-adjacent operations and do not indicate a problem.

6. **Demanded equalizing watermark capacity (Harsh Critic).** This would require modifying traditional methods beyond their architecture's capacity. The main comparisons in the paper are among latent-based methods (Tree-Ring, Gaussian Shading, PRC, Ours) where capacity is equalized, and that is where the paper's strongest claims lie.

7. **Selected Strength Finder strengths removed:** Several claimed strengths were generic ("the problem is important," "the paper is well-written") and were removed for lack of specificity.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

- Clarify the watermark capacity used for traditional baselines (Table 2). If they were evaluated at 32-bit rather than 512-bit, add a caveat to the comparison and ideally provide a controlled experiment at matching payload sizes.
- Add quantitative metrics (classification accuracy, TPR) to the module ablation study (Figures 6b–6c) rather than relying on qualitative statements.
- Define "REC ACC" and "DNR ACC" in the main text, and ensure the legend of Figure 5 consistently labels the compared method.
- Tone down "provably indistinguishable" in the abstract to something like "provably matches up to third-order moments and empirically indistinguishable."

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>