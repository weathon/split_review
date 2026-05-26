Now I have a thorough understanding of the paper and the calibration landscape. Let me produce the final review.

## Summary

The paper introduces Spherical Watermark, a lossless watermarking framework for diffusion models. The core technical idea converts binary watermarks into Gaussian noise via: (1) a binary embedding module that mixes repeated watermark bits with random padding using an invertible matrix T, (2) a spherical mapping that normalizes to the unit sphere, applies an orthogonal rotation C, and scales by a chi-square-distributed radius to produce noise that matches the standard Gaussian prior. The authors claim this is the first encryption-free lossless scheme (no per-image key storage), prove the result is a spherical 3-design matching moments up to order three, and provide experiments on Stable Diffusion showing undetectability, robustness, and efficiency.

---

## Strengths

**1. Encryption-free design with concrete efficiency gains.** Unlike Gaussian Shading (requires per-image key+nonce) and PRC (heavy cryptographic decoding), Spherical Watermark uses a fixed secret signature K={T,C}. This is empirically validated in Figure 4, which shows extraction time ~10^{-3.5}s — roughly four orders of magnitude faster than PRC. The design is clean and the efficiency advantage is well-supported.

**2. Theoretical moment-matching guarantee.** Theorems 3.1–3.2 and Lemmas 3.3–3.4 prove that the watermarked noise z_w is a spherical 3-design, matching the standard Gaussian prior's mean, covariance, and third-order moments. This is a formal guarantee stronger than heuristic watermarking methods, and the proof chain (3-wise independent binary code → spherical 3-design → orthogonal rotation invariance → chi-square scaling) is technically sound as far as it goes.

**3. Strong adversarial robustness.** Table 2 reports 99.83% TPR@1%FPR under WEvade attacks, outperforming PRC (95.38%) and Gaussian Shading (99.23%) under the same attack. Lossy methods collapse (e.g., DwtDct: 16.15%). This advantage is consistent with the paper's Appendix E argument that lossless schemes are inherently harder to adversarially detect.

**4. Scalability to long watermarks.** Figure 6(a) shows that under JPEG-70 compression, Spherical Watermark maintains high bit-accuracy at watermark lengths up to 4000 bits, whereas PRC fails completely beyond 2000 bits. This is a practically meaningful advantage for large-scale provenance tracking.

**5. Ablations validate design choices.** Figure 6(b) shows that omitting the binary embedding module makes the latent trivially distinguishable (classifier accuracy >> 50%); Figure 6(c) shows that omitting the spherical mapping causes a sharp robustness drop under brightness adjustment. These experiments confirm the necessity of each module.

**6. Computational efficiency.** Embedding is ~10^{-2}s and extraction ~10^{-3.5}s, both substantially faster than Gaussian Shading and PRC (Figure 4). The advantage stems from avoiding iterative belief-propagation decoding and per-image cryptographic operations.

---

## Weaknesses

### Major

**1. Critical inconsistency between Figure 2 caption and the body text regarding central undetectability evidence.**
 Section 4.2 states: "According to Figure 2, both Tree-Ring and Gaussian Shading (with fixed keys) are easily detected with accuracies of 100% and 97%, while PRC Watermark and our method remain indistinguishable." However, the Figure 2 caption (lines 217–221) reads: "Each plot compares 'True Ring' (blue line) and 'PRC watermark' (orange line)." The caption describes only two methods per subplot and does not mention Gaussian Shading or the proposed method at all. The 100%, 97%, and near-chance (50%) accuracy numbers attributed to Figure 2 appear nowhere else in a table or figure. This is not a minor typo — the paper's central empirical claim of undetectability for the proposed method is explicitly anchored to a figure whose caption describes content that cannot support the text's quantitative statements. The results may well be correct (the actual figure may contain all four methods), but the paper as presented to a reviewer contains a factual mismatch between a figure's caption and the claims made from it, preventing independent verification. This must be resolved for the paper to be evaluable.

**2. Gaussian Shading compared under crippled conditions that break its core losslessness guarantee.**
 The paper states in Section 4.1: "Note that with fixed keys, Gaussian Shading no longer achieves true losslessness." All latent baselines are evaluated with five fixed keys, and the undetectability comparison (Figure 2, Table 1) then shows Gaussian Shading as detectable (97% accuracy) while the proposed method is undetectable (50%). The degradation in Gaussian Shading's undetectability is a direct consequence of forcing fixed keys — a condition that violates the method's design principle. Gaussian Shading's entire claim to losslessness is predicated on per-image keys. The comparison is therefore not between the proposed method and Gaussian Shading as intended and described in the literature; it is between the proposed method and a version of Gaussian Shading that the authors acknowledge is broken. The paper would need to either (a) compare against properly keyed Gaussian Shading on undetectability and image quality, then separately discuss the key-storage trade-off as an ablation, or (b) clearly restrict all comparative claims to the "no per-image keys" regime and adjust the framing accordingly. As written, the undetectability and FID results against Gaussian Shading are invalid as evidence of superiority.

**3. Theoretical claim overreach relative to proof.**
 The paper's formal definition (Eq. 2) requires computational indistinguishability (negligible advantage for any polynomial-time adversary), and Section 3.3 claims that z_w "is distributed as N(0, I_{l_x})" — an exact distributional statement. However, the actual proof only establishes that z^{(2)} and z^{(3)} are spherical 3-designs (matching moments up to degree three). A spherical 3-design is a *finite* set of points, not a continuous distribution; the resulting z_w is a mixture of chi-radius-scaled discrete directions, not a multivariate Gaussian. Lemma 3.3 acknowledges this implicitly ("as l_x → ∞, the marginal law converges to N(0, 1/l_x)"). The paper's own limitations section (line 332) acknowledges "higher-order moments may deviate from the true prior." This gap between what is advertised (exact distributional identity / computational indistinguishability) and what is proven (moment matching up to order three with asymptotic convergence of marginals) is significant. The theoretical framing should be calibrated to match the actual guarantees.

### Minor

**4. Figure 5 caption inconsistency.**
 The text (line 273) states "In Table 2 and Figure 5, we compare our method with PRC Watermark under varied distortions." But the Figure 5 caption (lines 277–279) describes the comparison as "'Our' method (solid lines with markers) against 'Diffusion' (dashed lines with markers)." The legend mentions "REC ACC" and "DNR ACC" while the caption mentions TPR. It is unclear what "Diffusion" refers to — whether it is PRC, a diffusion-model baseline, or a labeling error. Combined with the Figure 2 issue, this erodes confidence in the experimental presentation.

**5. Notation error in Equation 6.**
 The equation writes "l_m = N × l_m", which is mathematically self-contradictory (unless N=1 or l_m=0). The intended meaning is likely l_{Nm} = N × l_m. This ambiguous reuse of l_m propagates through the method description.

### Trivial

**6. High FID standard deviations relative to between-method differences.**
 Table 1 reports FID with standard deviations of ~1.0–1.5 across all methods. The differences between "Original" and "Ours" are on the order of 0.003–0.3 (e.g., COCO SD v1.5: 48.1256 vs 48.1224). While the near-identical means support the claim that Ours matches the original, the high variance means that individual runs could show substantially different rankings. Including confidence intervals or effect sizes would strengthen the claim.

---

## Nice-to-Haves

- **Extraction guarantee on random padding r:** The paper should explicitly state that extraction does not require knowing r (T^{-1} recovers the full vector, and r is discarded). The current description implies this but could be clearer (it's ambiguous whether the padding is recoverable from the inverted latent after noise from the diffusion process).
- **Ablation of the rotation matrix C:** The method relies on orthogonal rotation C to break coordinate structure. An ablation comparing "with C" vs "identity C" on undetectability and robustness would demonstrate the necessity of this design choice.
- **PRC parameter tuning:** The paper criticizes PRC for difficult parameter tuning but evaluates it at default settings. A brief exploration or statement about how default parameters were chosen would strengthen the comparison fairness.

---

## Removed Points

The following points from the reviewers were removed after cross-checking against the paper:

- **"Figure 2 disaster — fatal discrepancy"** (from Harsh Critic, point 1): Demoted from Fatal to Major. The caption-to-text mismatch is real and serious, but it is plausible the figure itself contains all four methods and the caption is erroneous/incomplete. This does not necessarily invalidate the paper's claims, but it does prevent verification. Placed in Major.

- **"Deliberately unfair baseline evaluation of Gaussian Shading — straw-man"** (from Harsh Critic, point 2): Demoted from implied Fatal to Major. The paper acknowledges the fixed-key limitation. The comparison is valid under the "no per-image keys" regime that the paper advocates. However, the paper's framing treats the undetectability and FID results as evidence of general superiority, which overreaches given the condition. Placed in Major.

- **"Overclaim of theoretical guarantee"** (from Harsh Critic, point 3): Kept as Major but reframed from "title and definitions claim lossless" to a more precise calibration issue. The paper does prove moment-matching up to order three and the limitations section acknowledges the gap. The problem is the exact-distribution claim in Section 3.3 vs what is actually proven.

- **"PRC baseline tuning"** (from Harsh Critic, Section-by-Section notes): Removed. The paper uses default settings for all baselines. Singling out PRC for potential suboptimal tuning without evidence that different parameters would change results is speculative. If anything, this is a Nice-to-Have.

- **"FID missing run statistics"** (from Harsh Critic): Removed from Major, moved to Trivial. The high standard deviations are reported. The means are nearly identical, supporting the claim. A statistical test would be nice but is not required — the similarity is visually obvious from the table.

- **"Extraction guarantee on random padding"** (from Harsh Critic, Missing Parts): Moved to Nice-to-Have. The extraction procedure is described clearly enough (T^{-1} recovers the full vector, majority vote over first l_{Nm} entries). An explicit statement would improve clarity but the information is present.

- **"Ablation of rotation matrix C"** (from Harsh Critic): Moved to Nice-to-Have. A worthwhile addition but not a missing essential experiment.

- **Strength Finder, point 3** ("Empirical undetectability confirmed by classifier and FID"): Removed because the Figure 2 inconsistency undermines the empirical undetectability claim. Per the filtering rules, a strength that depends on a verified weakness being false must be removed.

- **Generic strengths about "addresses an important problem"**: Removed per filtering rules. The paper's strength is in its specific technical contribution and results, not in the general importance of watermarking.

---

## Novel Insights

The key insight that emerges from the reviews is that Spherical Watermark occupies an interesting point in the design space that the existing comparison papers (Gaussian Shading, PRC) do not cover: it forgoes per-image cryptographic keys entirely, achieving this by embedding randomness into the codeword itself via random padding r mixed with watermark bits through a sparse binary matrix R. The spherical 3-design guarantee provides a weaker but still meaningful form of distribution preservation than full computational indistinguishability. The practical question is whether the elimination of per-image key management is worth the trade-off in theoretical guarantee strength and the (partially confounded) empirical undetectability relative to Gaussian Shading. The paper would be strengthened significantly by directly acknowledging this trade-off rather than claiming across-the-board superiority.

---

## Suggestions

1. **Fix Figure 2.** Rewrite the caption to accurately describe all methods plotted. If the figure does contain all four methods, make this explicit. If the numeric accuracies (100%, 97%, 50%) are from a different experiment or table, cite the correct source.

2. **Re-evaluate Gaussian Shading fairly.** Add an experiment comparing against properly keyed (per-image) Gaussian Shading on undetectability. Separately present the fixed-key comparison as an ablation showing the cost of forgoing per-image keys. Restrict comparative claims accordingly.

3. **Calibrate theoretical claims.** Replace "z_w is distributed as N(0, I)" in Section 3.3 with a statement about spherical 3-design and moment matching. The formal definition (Eq. 2) of computational indistinguishability should be either proven or softened to match the actual guarantee.

4. **Fix Figure 5 caption** to correctly identify the comparison method (PRC vs "Diffusion").

5. **Fix Equation 6 notation** (l_m = N × l_m). Use a distinct variable for the expanded length.

---

## Score and Decision

### Anchor Comparison

| Anchor | Avg Score | Query Bucket | Comparison |
|--------|-----------|--------------|------------|
| jlhBFm7T2J (PRC watermark) | 6.50 | topic-mid | Closest related work; accepted with concerns about experiment adequacy but strong theoretical foundation. Current paper has more serious reporting issues and a weaker theoretical guarantee. |
| ll2nz6qwRG (Hidden in the Noise) | 5.83 | topic-mid | Solid empirical watermarking paper; accepted. Current paper has comparable technical merit but worse presentation issues. |
| jbfDg4DgAk (Sparse Watermark) | 3.00 | topic-low | Rejected for missing baselines and limited novelty. Current paper has a more novel technical idea but similar severity of presentation issues. |
| BXMoS69LLR (Blind Baselines MI) | 4.50 | weakness-unfair | Rejected for framing issues despite empirical contribution. Comparable in having a real contribution undermined by methodological concerns. |
| T0ebbDO60R (SuperMark) | 3.75 | topic-low | Rejected for limited novelty. Current paper is stronger technically. |

The low-band topic anchors failed at providing coherent, verifiable experimental support for their core claims — the current paper shares this failure with respect to Figure 2. The Gaussian Shading comparison issue is a further methodological concern absent from the mid-band accepted papers. The theoretical overclaim is present in the mid-band papers (PRC paper was also critiqued for loose theoretical bounds) but the current paper's issue is more acute because the gap between claim and proof is larger.

The paper has a genuine technical contribution (spherical design for encryption-free lossless watermarking) and several well-supported results (efficiency, scalability, adversarial robustness). However, the Figure 2 inconsistency undermines the central undetectability claim, the Gaussian Shading comparison is confounded, and the theoretical framing overreaches. These issues collectively prevent acceptance in the current form. The paper could become acceptable after substantial revisions to the experimental reporting and comparative evaluation.

**MY FINAL SCORE: <score>4.0</score>**
**MY FINAL DECISION: <decision>Reject</decision>**