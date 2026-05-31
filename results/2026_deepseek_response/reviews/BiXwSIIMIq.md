Now I have enough information for calibration. Let me compose the final review.

## Summary
2-3 sentence summary of the paper's contribution.

The paper proposes AC-DC, a three-stage score-based denoiser (auto-correction via additive Gaussian noise, directional correction via conditional Langevin dynamics, and score-based denoising) specifically designed to mitigate manifold mismatch when integrating score functions into ADMM-based plug-and-play frameworks. It provides convergence guarantees for ADMM-PnP with the AC-DC denoiser under both fixed step sizes (weakly nonexpansive setting) and adaptive step sizes (nonconvex setting). Experiments across seven inverse problems on FFHQ and ImageNet show that the method achieves competitive or best quantitative results against several baselines.

## Strengths
- **Novel AC-DC denoiser design directly motivated by the manifold mismatch problem.** The three-stage pipeline (AC → DC → denoising) is a principled architectural contribution addressing a known weakness of score-based PnP methods. The AC stage aligns iterates with noisy data manifolds via Gaussian perturbation, while the DC stage uses Langevin dynamics targeting the conditional distribution \(p(\mathbf{z}_{\sigma^{(k)}}|\mathbf{z}_{\text{ac}}^{(k)})\) to refine alignment before score-based denoising. This is clearly illustrated in Algorithm 1 and Figure 1.
- **Non-trivial convergence theory extending ADMM-PnP to score-based denoisers.** Theorem 2 proves that the AC-DC denoiser satisfies a weakly nonexpansive condition with high probability under smoothness and coercivity assumptions (Assumptions 2–3), enabling fixed-point ball convergence from Theorem 1. Theorem 3 further removes convexity of the data-fidelity term under an adaptive step-size schedule. This extends prior ADMM-PnP theory (Ryu et al., 2019; Chan et al., 2016) to the diffusion score setting, which is a meaningful theoretical advance.
- **Broad empirical evaluation across diverse inverse problems.** The method is evaluated on super-resolution, Gaussian deblurring, motion deblurring, random inpainting, box inpainting, phase retrieval, and HDR reconstruction on two datasets (FFHQ and ImageNet) against seven baselines (DPS, DAPS, DDRM, DiffPIR, RED-diff, DCDP, PMC). This breadth of evaluation is a strength.

## Weaknesses

### Fatal
None.

### Major
- **Table 1 contains unexplained inconsistencies in PMC entries.** The PMC baseline appears multiple times in the same task rows with different metrics (e.g., Super-resolution FFHQ: PSNR 27.761 vs 23.774, SSIM 0.639 vs 0.421), and some PMC rows are entirely blank (e.g., Inpainting Random, Gaussian Blur). This is not a parser artifact—the table as presented is ambiguous about what these entries correspond to. Since quantitative evaluation is the primary empirical evidence for the method's advantage, this inconsistency undermines trust in the reported numbers. The authors must clarify whether these are different PMC variants, different noise levels, or a reporting error, and correct the table. (See lines 324–325, 334, 339–340, 355–356, 364–366.)
- **No variance or confidence intervals reported for any metric.** All PSNR, SSIM, and LPIPS values are reported as point estimates averaged over 100 images. Many improvements over the strongest baseline (DAPS) are small—often <1 dB in PSNR. Without standard deviations or some measure of variability, it is impossible to assess whether these gains are statistically significant. This is a standard expectation for empirical papers in this field, and its absence weakens the evidence for the claimed improvements.

### Minor
- **The convergence theory assumes the DC Langevin step reaches stationarity, but the practical algorithm uses only J=10 steps.** Theorems 2 and 3 both state: "assume that the DC step reaches the stationary distribution for each k." A footnote (line 207) directs readers to Appendix E.2 for counterparts removing this assumption, which is a partial mitigation. Nevertheless, the main theoretical results are presented for an idealized version of the algorithm, creating a gap between the theory and the finite-step implementation tested. The paper would benefit from explicitly stating in the main text what guarantee—if any—holds for finite J.

### Trivial
- **Equation (9) has confusing notation.** The symbols \(\mathbf{z}_\sigma^{(k)}\) and \(\mathbf{z}_{\sigma^{(k)}}\) appear to be used interchangeably, and \(\mathbf{s}^{(k)}\) is redefined mid-line, making the derivation hard to follow (lines 125–129).
- **The rationale for specific hyperparameter schedules is not explained.** The schedules \(\eta^{(k)} = 5\times10^{-4}\sigma^{(k)}\) and \(\sigma_{s^{(k)}} = 0.1/\sqrt{\sigma^{(k)}}\) are given without justification or ablation, which hinders reproducibility.

## Nice-to-Haves
- Extend the DC ablation (currently only on phase retrieval, Figure 5) to at least one more task (e.g., super-resolution or deblurring) to demonstrate generality.
- Report number of score function evaluations (NFEs) per method to enable a fair comparison of computational cost.
- Validate the Gaussian approximation for the DC conditional likelihood empirically (e.g., by comparing against a Monte Carlo estimate on a small set of examples).

## Removed Points
These points were flagged by reviewers but are removed as invalid, speculative, or irrelevant per the filtering guidelines:
- *Criticism of missing related works*: Removed per policy—cannot verify existence of unmentioned works.
- *Criticism about "counterparts removing this assumption" being unverifiable*: The paper explicitly cites Appendix E.2; the appendix is stripped by the parser, not absent in the original.
- *Criticism about unfair comparison favoring baselines*: The asymmetry (if any) favors baselines, not the proposed method.
- *Generic "evaluation lacks rigor" without concrete anchor*: Replaced with the specific verified concerns (Table 1, no error bars).
- *Strengths about the problem being "important" without evidence*: Removed as generic.
- *Suggestion to discuss D-AMP connection*: This is a nice-to-have, not a weakness.
- *Speculation about "overpromising" in introduction*: The paper's claims are appropriately scoped given the results.

## Novel Insights
None beyond the paper's own contributions. The review process did not surface a genuinely novel observation about the paper that the authors themselves did not articulate.

## Suggestions
1. **Fix Table 1 urgently.** Explain what the duplicate/blank PMC entries mean, or remove them if they are errors. Add footnotes or column notes to disambiguate.
2. **Add error bars or credible intervals** for all quantitative metrics. At minimum, report standard deviations over the 100 test images. For small improvements over DAPS, perform a simple significance test.
3. **In the main text, clarify the theory-practice gap.** State explicitly what the convergence guarantee is for the algorithm as actually run (J=10) versus the idealized version. Summarize the Appendix E.2 result at a high level.
4. **Add a compute table** reporting NFEs for each method to support fair comparison.

## Score and Decision

### Calibration

**Round 1 bracket anchors:**
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/mHkbi3XM58.md` | 3.25 | R1 (weak) | Clearly weaker paper — unrelated topic, low novelty |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/dAavOuxZvo.md` | 3.00 | R1 (weak) | Clearly weaker — heuristic approach |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/HXjXPQU3yJ.md` | 6.25 | R1 (mid) | **Most comparable anchor** — PnP-ADMM with convergence theory, prior mismatch. Similar scope/theory contribution. Our paper has broader experiments but worse table presentation. Comparable quality. |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/x7d1qXEn1e.md` | 6.25 | R1 (mid) | Restoration model as implicit prior. Stronger theory, weaker experiments. |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/kNPcOaqC5r.md` | 5.75 | R1 (mid) | Learned proximal networks. Comparable theoretical depth. |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/Z9Odi09Rv9.md` | 4.75 | R1 (mid) | Diffusion inverse solver, weaker—had baseline comparison issues. Our paper is stronger. |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/6EUtjXAvmj.md` | 8.00 | R1 (strong) | Clearly stronger — tight theory, clean experiments. |

**Round 1 bracket:** Between 5.0 and 6.5 — the paper is clearly above the 3-4 range but below the exceptional 8-range papers.

**Round 2 narrowing anchors:**
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/1YO4EE3SPB.md` | 5.50 | R2 (lower) | Variational perspective on diffusion inverse problems. Accepted after rebuttal. Comparable in having real contributions with addressable weaknesses. |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/kRBQwlkFSP.md` | 6.75 | R2 (upper) | Diffusion state-guided projected gradient. Stronger empirical validation. |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/DsEhqQtfAG.md` | 6.50 | R2 (upper) | Decomposed diffusion sampler. Stronger on medical imaging + speed. |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/nHESwXvxWK.md` | 4.00 | R2 (lower) | MC-guided diffusion. Wide score variance but generally weaker. |

**Final position relative to anchors:** The paper is comparable to the 5.50 variational perspective paper (which was accepted) and slightly below the 6.25 PnP-ADMM mismatch paper (which was rejected due to theory-experiment disconnect). The AC-DC denoiser is a genuinely novel design, and the convergence theory is non-trivial—but the Table 1 inconsistency and lack of error bars are notable empirical weaknesses that need to be addressed. I place the paper just above the 5.50 variational paper (which had weaker experimental breadth) but below the 6.25 mismatch paper (which had cleaner empirical reporting despite fewer tasks).

**Final Score: 5.5**

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>