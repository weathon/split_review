Now I have enough calibration data. Let me finalize the review.

**Round 1 Bracket**: The paper sits in the 3.5–7.5 range. Nothing below 3.5 is comparable (those are clearly weaker papers). Nothing above 7.5 matches (those are analysis/theory papers, not method papers for VL-CL).

**Round 2 Narrowing**: The paper is clearly stronger than C-CLIP (6.50, Accept) and comparable to EFC (7.00, Accept). PI-CCA has a more novel conceptual contribution and broader evaluation than C-CLIP, with comparable analysis depth to EFC but with the Figure 3 credibility concern.

**Final score**: 7.0 — comparable to EFC (7.00). PI-CCA has a genuinely novel insight, principled method, SOTA results across 4 benchmarks, and comprehensive analysis. The Figure 3 credibility issue and missing error bars on Table 1 are real but fixable concerns that don't invalidate the core contribution.

---

## Summary
This paper proposes PI-CCA, a replay-free continual learning framework for vision-language models that recasts catastrophic forgetting as alignment-geometry drift and preserves cross-modal alignment via a compact CCA certificate storing top-k canonical correlations and sketched canonical subspaces. The method adds spectral preservation, subspace-angle, and prompt-invariance losses during LoRA-based adaptation, achieving state-of-the-art replay-free results across four benchmarks (MTIL, X-TAIL, VLCL, ConStruct-VL).

## Strengths
- **Novel and principled conceptual framework**: The paper's core insight — recasting VL-CL forgetting as alignment-geometry drift in the whitened cross-modal covariance and preserving CCA invariants rather than proxy signals — is a clear conceptual advance over prior work. The distinction from Mod-X (off-diagonal similarity matching), ZSCL (logit distillation), and C-CLIP (contrastive consolidation) is drawn precisely in §1–2.
- **SOTA results across four diverse benchmarks**: PI-CCA achieves best replay-free results on MTIL (76.8 Avg), X-TAIL (68.1 Avg), VLCL (48.6/37.4 I2T/T2I R@1), and ConStruct-VL (75.2 FA, 2.7 AF). On VLCL it even surpasses GIFT, which uses diffusion-generated synthetic replay, demonstrating that geometric preservation can substitute for data retention (Table 2).
- **Thorough component-wise ablation (Table 3)**: Each loss term is individually zeroed with quantified drops: spectral (λ₁=0) causes −2.5 on MTIL Avg and −2.3 on VLCL I2T R@1; subspace (λ₂=0) causes −2.2 and −2.7; prompt invariance (λ₃=0, M=0) causes −1.5. Design choices are validated: sorted surrogate vs. Hungarian yields <0.1 difference; Gaussian vs. SRHT sketches behave similarly.
- **Prompt-invariance mechanism is well-designed and empirically validated**: Averaging sketched projectors over M prompt perturbations (Eq. 5–6) eliminates sign/rotation ambiguity without Procrustes alignment. The stress test (Fig 4) demonstrates meaningful robustness: R@1 retains 46.9 vs. 44.5 without invariance at s=1.0, with flatter degradation curves for both ID and OOD templates.
- **Task-order robustness (Fig 5)**: Evaluation over 20 independently shuffled MTIL sequences with narrow IQRs (Avg ≈ 76.0–77.4) directly addresses sensitivity to task ordering.

## Weaknesses

### Fatal
None.

### Major
- **Credibility issue with Figure 3 correlations**: The paper claims Pearson r = 1.00 in two scatter-plot panels and r = 0.99 in the other two, with Spearman ρ = 1.00 across all four (lines 228–232). Simultaneously, the text describes "realistic scatter" and shows 95% confidence intervals on the least-squares fit. A Pearson r of exactly 1.00 implies all points lie on a perfect line, which is incompatible with "realistic scatter." This analysis is presented as the paper's primary interpretive evidence for claim (iii) — that "alignment-geometry stability predicts retention/transfer trends" — and the contradictory reporting undermines its credibility. Possible explanations include a trivially small number of data points or a tautological relationship. The authors should report the number of scatter points, correct the correlation values, and compute confidence intervals on r and ρ.

- **Missing error bars on Table 1**: Table 2 (VLCL, ConStruct-VL) reports standard deviations across seeds (e.g., 48.6 ± 1.0), but Table 1 (MTIL, X-TAIL) reports only point estimates. On X-TAIL, the margins over the next-best method are small: 0.7 pp Avg over RAIL (67.4) and 0.7 pp Last over DIKI (66.2). Without variance, these differences may be within noise. Since the paper already reports ± values in Table 2, the omission is inconsistent.

### Minor
- **"Constant memory" claim is imprecise**: The abstract and contributions (line 25) claim "constant-memory." The certificate itself is O(hk) values (constant in backbone dimension), per §3.2. However, the streaming EMA (Eq. 12) maintains full covariance matrices Σ_vv ∈ ℝ^{d_v×d_v}, Σ_tt ∈ ℝ^{d_t×d_t}, Σ_vt ∈ ℝ^{d_v×d_t}, which is O(d²) memory — manageable but not "constant in d." The paper should qualify the claim.
- **No computational overhead comparison vs. baselines**: Figure 2 reports PI-CCA's wall-clock times and memory but not those of baselines on the same hardware. The method adds differentiable SVD (block power iteration), Newton-Schulz whitening, and M prompt forward passes per batch, all adding non-trivial overhead. A per-step comparison against C-CLIP, DIKI, and RAIL would complete the efficiency story.

### Trivial
- Circular notation on line 51: θ_v = (θ_v, φ_v) uses the same symbol for backbone parameters and the full parameter tuple.

## Nice-to-Haves
- Add a brief limitations paragraph discussing conditions where CCA invariants might be insufficient (e.g., when new tasks require fundamentally different canonical directions).
- Report the number of data points in each Figure 3 panel and analyze sensitivity to the prompt perturbation distribution P.

## Removed Points
These points are flagged to be removed, treat them with caution.
- **Code availability concern**: The harsh critic noted code cannot be released during review. Per rules, we do not flag reproducibility concerns about code release; the paper states code will be released in camera-ready.
- **Garbled formula at line 129**: A parser artifact, not a paper problem.
- **Missing related works**: Cannot verify existence of external references not cited.
- **Missing appendix/proofs**: The parser strips appendices; the original submission contains them.

## Novel Insights
The paper's most novel contribution is the recasting of VL continual forgetting as alignment-geometry drift in the canonical subspace/spectrum of the whitened cross-modal covariance. While the Figure 3 correlation values appear unreliable, the underlying insight — that preserving CCA invariants is more principled than regularizing proxy signals — is well-supported by the ablation study (Table 3) which shows both spectral and subspace terms are individually necessary (−2.5 and −2.2 on MTIL Avg respectively). This conceptual framing provides interpretability beyond standard ablations and is a genuine advance for the VL-CL community.

## Suggestions
- Fix Figure 3: report the number of data points per panel, correct correlation values to reflect actual scatter (likely strong but imperfect), and compute proper confidence intervals on r and ρ.
- Add ± standard deviations to Table 1, matching Table 2's reporting style.
- Clarify the "constant memory" claim: state the certificate is O(hk) but the EMA covariance cache is O(d²).
- Add a brief wall-clock and memory comparison of PI-CCA vs. C-CLIP, DIKI, and RAIL on the same hardware.

## Calibration Anchors Retrieved

| Path | Avg Human Score | Round | Comparison |
|------|----------------|-------|------------|
| JIlIYIHMuv.md (LVLM-CL) | 2.50 | 1 | Clearly weaker; lacks principled method and comprehensive evaluation |
| gNoqEdT2wO.md (MCIL benchmark) | 2.33 | 1 | Clearly weaker; benchmark-only contribution |
| WM5G2NWSYC.md (Projected Subnetworks) | 2.00 | 1 | Clearly weaker; limited method and evaluation |
| TxIrMD6lAN.md (Task-Specific Adapters) | 3.00 | 1 | Weaker; limited evaluation and less principled |
| k9NYnsC4Mq.md (PROOF) | 5.67 | 1 | Weaker; less principled method, rejected |
| sb7qHFYwBc.md (C-CLIP) | 6.50 | 1, 2 | PI-CCA clearly stronger: more principled, broader eval, better results |
| 9aZ2ixiYGd.md (VL Synergy) | 5.00 | 1 | Weaker; less comprehensive |
| G9Ea7mlqGO.md (CLIP Online CL) | 3.80 | 1 | Weaker; limited contribution |
| CagdoUkvvl.md (Relaxed Alignment) | 4.50 | 1 | Weaker; less comprehensive |
| Hcb2cgPbMg.md (Spectral Regularization) | 6.25 | 2 | PI-CCA stronger: cross-modal focus, broader benchmarks, more analysis |
| TLADT8Wrhn.md (TiC-CLIP) | 6.25 | 2 | Different contribution type (benchmark); PI-CCA is method-focused |
| 7D9X2cFnt1.md (EFC) | 7.00 | 2 | Comparable quality; both have principled methods and strong eval. PI-CCA has Figure 3 issue but more diverse analysis |
| MB53uAZKSc.md (TiC-LM) | 6.25 | 2 | Different domain; PI-CCA is more comprehensive as a method paper |
| uAFHCZRmXk.md (Modality Gap) | 8.00 | 1 | Stronger but analysis paper, not comparable type |
| cmXWYolrlo.md (Geometric Inductive Biases) | 7.50 | 2 | Stronger; theoretical analysis paper |

**Round-1 bracket**: 3.5–7.5 (nothing below 3.5 is comparable; nothing above 7.5 matches the method-paper type).

**Round-2 narrowing**: PI-CCA is clearly above C-CLIP (6.50) and spectral regularization (6.25), and comparable to EFC (7.00). The Figure 3 credibility issue and missing Table 1 error bars are significant but fixable, while the core method and evaluation are strong. Score: **7.0**.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>