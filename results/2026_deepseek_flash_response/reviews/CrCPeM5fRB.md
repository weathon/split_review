## Summary

This paper proposes the Signal Dice Similarity Coefficient (SDSC), a structure-aware metric for time-series self-supervised representation learning that extends the Dice Similarity Coefficient from segmentation masks to continuous signed signals. SDSC replaces only the reconstruction loss (MSE) in the SimMTM framework while keeping the contrastive objective fixed, enabling a controlled comparison. A hybrid loss combining SDSC with MSE via uncertainty-based weighting is also introduced. Experiments on forecasting and classification benchmarks show SDSC achieves comparable performance to MSE in forecasting and modest improvements (~1.2 pp) in frozen-encoder in-domain classification.

## Strengths

1. **Table 1 provides direct quantitative evidence of MSE's limitations**: The inverted signal (phase reversal) receives MSE = 0.0200, masquerading as high-quality reconstruction, while SDSC correctly scores it 0.0000. The zero signal and 2× scaled signal produce identical MSE = 0.4995 despite being structurally opposite, while SDSC distinguishes them (0.0000 vs. 0.6667). This directly validates the paper's core motivation.

2. **Table 3 and Figure 3 provide controlled evidence that SDSC-based pre-training induces better structural alignment at the same MSE level**: At a fixed MSE (1.5 ± ε), SDSC-trained models achieve higher SDSC values (center ~0.56 vs. ~0.54) with lower variance than MSE-trained models. This demonstrates that the training objective causally affects the structural quality of representations, beyond what the metric itself captures.

3. **Clean controlled experimental design**: The paper keeps the contrastive loss (InfoNCE) identical to the original SimMTM formulation and varies only the reconstruction loss. As stated: "any downstream performance differences should be attributed to the reconstruction objective." This cleanly isolates the contribution of structure-aware reconstruction from contrastive learning effects.

4. **Principled hybrid loss**: Rather than overclaiming SDSC as a universal replacement, the paper identifies that SDSC ignores amplitude and proposes a hybrid loss with uncertainty-based weighting (Kendall et al., 2018). The hybrid achieves the best forecasting results overall, showing the two objectives are complementary.

## Weaknesses

### Major

1. **Pre-training MSE values for classification (Table 2) are implausibly high and unexplained**: Table 2 reports Avg (Classification) pre-training MSE of 50.3 (MSE-trained), 74.0 (SDSC-trained), and 120.0 (PCC). The paper states "All time-series inputs are z-score normalized per channel" (mean 0, variance 1). For such data, a trivial zero-predictor achieves MSE ≈ 1, and the forecasting Avg MSE values (0.48–0.63 on similarly normalized data) confirm the scale behaves as expected. Values of 50–120 imply errors of ~7–11 standard deviations per point on average, which is not physically plausible if the MSE is a per-point average. The MAE values also show a large discrepancy (3.5–4.5 for classification vs. 0.34–0.74 for forecasting). The paper offers no explanation — whether MSE is summed rather than averaged across channels/timesteps, whether different normalization applies, or whether a bug exists. This discrepancy undermines confidence in the pre-training analysis for classification, even if the internal relative ordering between methods is preserved.

2. **The claimed benefits of SDSC are confined to a narrow regime**: SDSC outperforms MSE in only one of five evaluation settings (frozen-encoder in-domain classification, ~1.2 pp improvement on the average of accuracy/precision/recall/F1). In forecasting (Table 4), MSE and SDSC are essentially identical (0.295 vs. 0.294 avg MSE). In frozen-encoder cross-domain classification, SDSC is slightly worse (47.28 vs. 47.63). In fine-tuned classification both in-domain (74.21 vs. 74.46) and cross-domain (83.29 vs. 84.65), SDSC is worse. Meanwhile the abstract claims benefits "particularly in in-domain and low-resource scenarios," yet no low-resource experiments appear in the main paper's four experimental tables. The paper's framing in abstract and introduction is broader than the evidence supports.

3. **No uncertainty or statistical significance estimates**: All experiments use "fixed random seeds across all runs." Without multiple trials or variance estimates, it is impossible to assess whether the small observed differences (e.g., the ~1.2 pp improvement in frozen in-domain classification) are meaningful or within noise range. Given that SDSC underperforms MSE in several settings, the stability of the frozen-encoder advantage is questionable. This is a standard expectation for comparative performance claims.

### Minor

4. **Results tested on only one backbone architecture (SimMTM)**: While the controlled design is a strength, generalizability to other SSL frameworks (TI-MAE, TS2Vec, TimesNet, etc.) is unknown. The paper acknowledges this as future work, but it limits the strength of conclusions.

5. **SDSC is not shift-invariant or warp-invariant**: The paper acknowledges this limitation. However, for real-world tasks where time-shifted but otherwise identical waveforms are common (physiological signals with variable latencies), SDSC would penalize them heavily. The paper does not investigate how severe this limitation is in practice, and the need for the hybrid loss partly reflects this gap.

6. **"Low-resource" claim in abstract lacks main-paper support**: The abstract and introduction claim benefits "in low-resource scenarios," but no low-resource experiments are shown in the main paper's tables. If these results exist in the (stripped) appendix, explicit cross-references and summary numbers are needed in the main text.

### Trivial

7. **Lemma 1 (bounding SDSC in [0,1]) is only in the appendix**: This fundamental property should be stated in the main text.

## Nice-to-Haves

- A deeper qualitative analysis of *why* SDSC helps in frozen-encoder classification, e.g., t-SNE/UMAP visualizations of representations learned with MSE vs. SDSC, or case studies of where the two models disagree on test samples.
- Ablation of the uncertainty-based weighting in the hybrid loss: how do λ_sdsc and λ_mse vary across datasets, and are the learned weights interpretable?
- Head-to-head training with DILATE or SoftDTW (acknowledged as future work due to compute constraints), since these are natural structure-aware baselines.

## Removed Points

These points were flagged by reviewers but removed with justification:

- "Table 2 as self-confirming" — REMOVED: This is expected behavior, not a flaw; the paper is transparent that each loss optimizes its own objective.
- "Forecasting benchmark not sensitive enough" — REMOVED: Speculative; all methods including MSE itself produce similar results, which could equally indicate the task is well-solved.
- "Zero-crossings issue could artificially depress SDSC" — REMOVED: Speculative; no experimental evidence that this causes practical problems.
- "Missing dataset details, appendix contents" — REMOVED: Standard appendix material stripped by the parser.
- Criticisms framed as general area sweeps without specific anchors (e.g., "the evaluation lacks rigor") — REMOVED per filtering rules.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Resolve the MSE discrepancy in Table 2 for classification pre-training**: Clarify whether MSE is reported as per-point average, sum across time/channels, or computed on a different scale. This single issue would resolve substantial reviewer concern.
2. **Add uncertainty quantification**: Multiple seeds (3–5) with standard deviations for the main downstream results (Tables 4–6).
3. **Narrow claims to match evidence**: Either add low-resource experiments or remove the claim from abstract/intro; similarly, acknowledge that SDSC's advantage is limited to frozen-encoder in-domain classification rather than claiming broader improvements.
4. **Add qualitative analysis**: Visualizations of representations (t-SNE/UMAP) to directly connect SDSC's structural objective to downstream behavior.

## Score and Decision

**Calibration anchors used:**

| Path | Avg Score | Round | Comparison to this paper |
|------|-----------|-------|------------------------|
| TILDE-Q (`Dxl0EuFjlf.md`) | 6.00 | R1 | Slightly stronger — more extensive forecasting experiments across architectures, still rejected at ICLR |
| TILDE-Q (`7egJb0X9m2.md`) | 5.00 | R2 | Similar — both propose shape-aware losses with marginal improvements and no variance estimates; SDSC has additional MSE anomaly |
| Patches SSL (`WS7GuBDFa2.md`) | 6.25 | R1 | Stronger — achieves SOTA on benchmarks, thorough ablations, accepted |
| Structure-preserving CL (`sz7HdeVVHo.md`) | 5.25 | R2 | Similar — both have novelty concerns and incomplete evaluation |
| DynaCL (`nphsoKxlFs.md`) | 4.00 | R1 | Weaker — more limited experiments and results |
| Hybrid Loss (`Y89o3LAEHX.md`) | 2.00 | R1 | Much weaker — marginal improvements, poor experimental design |

**Round 1 bracket:** [3.5, 6.0]  
**Round 2 narrowing:** Paper is weaker than TILDE-Q (5.00–6.00, rejected) due to the unexplained MSE anomaly, narrower claimed benefits, and no variance estimates. It is clearly stronger than the 2.00–4.00 anchors. Final calibrated score: **4.5**.

The paper presents a clean and well-motivated idea, but the experimental validation does not support its claims at the standard required by ICLR. The most significant concern is the unexplained pre-training MSE values for classification (50–120 on z-score normalized data), which undermines trust in the experimental pipeline. Beyond this, the positive results are confined to a single narrow setting with modest improvements and no uncertainty quantification, while the abstract claims broader benefits that lack evidentiary support. The paper has the foundations of a useful contribution, but needs substantial strengthening (resolving the MSE anomaly, adding variance estimates, narrowing claims) to be competitive at a top venue.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>