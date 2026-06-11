Now writing the final consolidated review.

---

## Summary

This paper proposes the Signal Dice Similarity Coefficient (SDSC), a structure-aware metric for time-series self-supervised representation learning. SDSC extends the Dice Similarity Coefficient from semantic segmentation to continuous, signed time-series by measuring signed amplitude overlap at each time step via a Heaviside function on sign products and a min-of-absolute-values operation. A sigmoid-based differentiable approximation enables use as a training loss, and a hybrid loss combining SDSC with MSE via homoscedastic uncertainty weighting is proposed. The method is evaluated by replacing only the reconstruction loss in SimMTM (keeping the contrastive InfoNCE fixed) and testing on forecasting and classification benchmarks.

## Strengths

- **Compelling demonstration of MSE's structural blindness (Table 1):** The constructed test cases are crisp and persuasive — a phase-inverted signal receives MSE=0.0200 but SDSC=0.0000, and a constant-zero signal vs. a 2×-scaled waveform both yield MSE=0.4995 while SDSC correctly distinguishes them (0.0000 vs. 0.6667). These are not edge cases but common failure modes in time-series reconstruction, directly motivating the need for a structure-aware alternative.

- **Rigorous experimental isolation of the reconstruction objective:** The paper integrates SDSC exclusively into the reconstruction branch of SimMTM while keeping the contrastive objective (InfoNCE) identical to the original formulation (Section 3.3, Eq. 9; Section 4). This means any observed downstream differences are attributable solely to the reconstruction loss, enabling clean causal attribution — a genuine methodological strength.

- **Well-supported diminishing-returns finding:** Two converging lines of evidence: (a) Figure 3a shows a weak Pearson correlation of −0.324 between MSE and SDSC under MSE-based pre-training, indicating better MSE does not reliably imply better structural fidelity; (b) Table 4 shows SDSC-pre-trained models achieve comparable downstream forecasting accuracy (Avg MSE 0.294 vs. MSE-baseline 0.295) despite substantially worse pre-training MSE, demonstrating that structural alignment alone is sufficient and excessive MSE minimization yields diminishing returns.

- **Hybrid loss with principled uncertainty weighting:** The paper adopts Kendall et al.'s homoscedastic uncertainty weighting (Eq. 8) to let the model learn the trade-off during training, providing a practical off-the-shelf option when the importance of amplitude vs. structure is unknown a priori.

- **Honest acknowledgment of limitations:** The paper explicitly notes SDSC underperforms MSE on the epilepsy dataset (which relies on amplitude patterns), that cross-domain fine-tuned results favor baselines, and that SDSC is "not tolerant to global shifts or warping." The conclusion states improvements are "moderate" and acknowledges SoftDTW/DILATE remain stronger in certain settings.

## Weaknesses

### Fatal

None.

### Major

- **The central claim of improved representation quality is weakly supported by the evidence.** On forecasting (Table 4), the Avg numbers are MSE=0.295 vs. SDSC=0.294 — a difference in the third decimal place. On fine-tuned in-domain classification (Table 6), MSE achieves 79.66% accuracy vs. SDSC's 79.60%, and PCC actually outperforms both at 79.76%. The frozen-encoder in-domain result (Table 5) shows a more meaningful gain (76.38% vs. 75.45%), but this is one setting. The abstract claims that "enforcing structural fidelity enhances semantic representation quality," but the evidence supports parity/sufficiency ("comparable") more than improvement. The diminishing-returns argument (that structural alignment alone suffices) is genuinely interesting and better-supported, but the paper frames itself as proposing an improvement.

- **No statistical significance or variance is reported for any downstream results (Tables 4–6).** The paper mentions "fixed random seeds across all runs" (Section 4) but provides no standard deviations, confidence intervals, or multi-seed statistics. Given that reported differences are frequently in the third decimal place (e.g., forecasting MSE of 0.294 vs. 0.295, classification accuracy of 79.66 vs. 79.60), readers cannot judge whether these differences are noise. This omission undermines the quantitative comparisons.

### Minor

- **Table 2 caption overstates the finding.** The caption states "SDSC shows the most robust results overall," but training with L_sdsc = 1 − SDSC naturally optimizes SDSC, making high SDSC scores for SDSC-based models tautological. The surrounding text is appropriately cautious, but the caption framing could mislead readers.

- **"Low-resource" claim in the abstract lacks main-text support.** The abstract and introduction both mention improved performance "in low-resource scenarios," but no low-resource experiments appear in the main body. Supporting experiments may exist in the stripped appendix, but a claim central enough for the abstract should be briefly evidenced in the main text.

- **Only one backbone (SimMTM) is tested.** The paper acknowledges this limitation ("We leave integration into additional pretraining frameworks ... as future work, noting compute constraints," Section 5), and the choice of SimMTM is well-justified for isolating the reconstruction loss. However, it limits claims about SDSC's generality across architectures.

- **Narrow SDSC dynamic range in Figure 3a.** Under MSE-based pre-training on ETTh1, SDSC values span only [0.50, 0.62]. While this is specific to one condition and the range is wider across models in Table 2 (0.45–0.78), a brief discussion of when the metric's discriminative power narrows would strengthen the analysis.

### Trivial

- The "low-resource" claim should be either removed from the abstract and introduction or accompanied by a brief mention of supporting evidence in the main text.

## Nice-to-Haves

- Testing on at least one additional backbone (e.g., a masked-autoencoder like TI-MAE) would strengthen generality claims.
- A brief sensitivity analysis of α in the main text, or at minimum a statement of how sensitive results are to α = 10 vs. other values, would help readers.
- Discussion of when the narrow SDSC dynamic range becomes a practical concern.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **HC: "The metric's inability to handle temporal shifts is acknowledged but under-examined."** REMOVED. The paper explicitly states SDSC is "alignment-free and computationally linear, but not tolerant to global shifts or warping" (Section 1). This is an explicit design choice, not an unexamined limitation.

- **HC: "The SoftDTW results are notably weak on pre-training metrics, which is surprising."** REMOVED. This is an observation about a baseline, not a paper weakness.

- **HC speculative concerns about stripped appendix content (α sensitivity analysis).** REMOVED per the rule that stripped appendix content is assumed to exist. The paper references the α analysis as Appendix A.3 and discusses α's role in the main text (lines 131–132).

- **HC: "The effect size is tiny: the SDSC distribution shifts from ~0.54 to ~0.56."** PARTIALLY REMOVED. The narrow dynamic range is retained as a Minor observation, but the claim that the shift is "hard to take seriously" is removed — the paper also reports reduced variance and IQR (Table 3), which is a valid observation regardless of raw shift magnitude.

- **HC: Request for compute time analysis and testing on larger datasets/larger models.** REMOVED as generic criticisms that could apply to virtually any paper.

- **HC: "The paper attempts to reframe this null result by arguing that 'comparable downstream performance between MSE and SDSC does not necessarily imply the superiority of MSE.'"** REMOVED as stated. The paper's argument here is actually a substantive point about diminishing returns and metric overestimation, not a post-hoc rationalization. The paper is honest that improvements are "moderate."

- **SF: Generic strengths about addressing an "important problem."** REMOVED. Only concrete, evidence-backed strengths retained.

## Novel Insights

Beyond the paper's own contributions, the reviews highlight an important tension: the paper's strongest empirical finding is not that SDSC beats MSE, but that SDSC matches MSE on downstream tasks despite substantially worse pre-training MSE. This diminishing-returns argument — that structural alignment alone is sufficient and excessive amplitude minimization adds little for downstream performance — is more novel and better-supported than the "SDSC improves representation quality" framing. A reframed paper centered on this sufficiency argument would align claims with evidence more precisely. Additionally, the observation that PCC outperforms both MSE and SDSC in fine-tuned in-domain classification (Table 6) suggests that correlation-based objectives may deserve more attention in this space, which the paper does not explore.

## Suggestions

- Reframe the central narrative from "SDSC improves representation quality" to "structural alignment alone is sufficient for downstream performance, and SDSC exposes the diminishing returns of amplitude-focused objectives." This better aligns claims with evidence.
- Add variance estimates (standard deviations across 3–5 seeds) to Tables 4–6. Without these, the marginal quantitative comparisons are uninterpretable.
- Move at least a summary of low-resource experiments into the main text if they are to be claimed in the abstract.
- Consider briefly discussing the practical significance of the narrow SDSC dynamic range observed in Figure 3a.

## Calibration Anchors

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| qU1GtrDDst (Financial time series CPC) | 1.80 | R1 | Much weaker — limited evaluation, unclear contribution |
| V8YwPdoSlr (CHRONOS) | 3.50 | R1 | Weaker — poor writing, limited to ECG, unclear methodology |
| GITAR (tkN0sLhb4P) | 4.75 | R1 | Weaker — missing decoder details, insufficient baselines |
| TILDE-Q v1 (7egJb0X9m2) | 5.00 | R2 | SDSC is somewhat stronger — cleaner metric formulation, better experimental isolation |
| Structure-preserving CL (sz7HdeVVHo) | 5.25 | R1 | SDSC is comparable — more novel metric, similar empirical strength |
| TILDE-Q v2 (Dxl0EuFjlf) | 6.00 | R2 | SDSC is slightly weaker — TILDE-Q tests on more models, has more extensive experiments |
| Rethinking Uniformity Metric (3pf2hEdu8B) | 6.00 | R1 | SDSC is weaker — less theoretical depth |
| Patch Embedding (WS7GuBDFa2) | 6.25 | R1 | SDSC is weaker — less clear empirical gains |

**Round 1 bracket:** 4.5–6.0. **Round 2 narrowing:** SDSC sits above TILDE-Q (5.00) in formulation quality and experimental design, comparable to the structure-preserving CL paper (5.25), but below the clear accepts (6.00+). The marginal improvements and missing variance reporting anchor it in the borderline-reject range.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>