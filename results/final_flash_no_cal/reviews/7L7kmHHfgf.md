Now I have thoroughly read the paper. Let me verify each reviewer claim against the actual content before writing the final review.

## Final Consolidated Review

Let me now synthesize everything.

## Summary

PIRN proposes a prototype-driven intra-modal reconstruction framework with cross-modal normality communication for few-shot multimodal anomaly detection. The three components — Balanced Prototype Assignment (BPA), Adaptive Prototype Refinement (APR), and Multimodal Normality Communication (MNC) — address codebook collapse, train-test distribution shift, and cross-modal synergy under limited data. The method is evaluated on MVTec-3D-AD, Eyecandies, and Real-IAD D3.

## Strengths

1. **Consistent gains over controlled strong baselines**: PIRN outperforms the strongest baseline INP-Former (adapted with the same ViT-B/14 DINOv2 backbone and input resolution, per lines 191–192) by +3.9 AUROC_I (5-shot), +3.7 (10-shot), and +2.4 (50-shot) on MVTec-3D-AD (Table 1). This provides controlled evidence that the proposed modules, not merely a stronger backbone, drive the gains.

2. **Ablations validate each component**: Table 2 shows that removing BPA, APR, or MNC from the full model degrades performance (baseline 0.828 → full 0.922 AUROC_I on 10-shot MVTec-3D-AD). Table 7 further shows balanced OT aggregation outperforms global/top-k averaging in APR.

3. **Significant efficiency advantage**: PIRN achieves the best AUROC_I (0.922) with 103.36G FLOPs (85% fewer than FIND's 728.46G) and 17.49ms latency (4.35× faster than FIND), per Table 4.

4. **Interpretability analysis**: Figure 4 visualizes that anomalous tokens undergo larger feature displacement than normal tokens during prototype-based reconstruction, providing direct evidence that the codebook faithfully captures normality.

5. **Strong Real-IAD localization**: PIRN achieves the best average AUROC_P (0.961) on Real-IAD D3 and leads in 13/20 categories (Table 8), despite using only two modalities vs. D³M's three.

## Weaknesses

### Major
- **Missing FIND from the main few-shot comparison (Table 1).** FIND (Li et al., 2025) is cited in the implementation details (line 148) and benchmarked in the efficiency table (Table 4) with AUROC_I = 0.921 on 10-shot MVTec-3D-AD — essentially tied with PIRN's 0.922. Yet FIND does not appear in the central accuracy comparison of Table 1. If FIND is a relevant SOTA method, its omission from the main table weakens the claim of "consistently superior performance." The paper should either include FIND in Table 1 or explain why direct accuracy comparison is inappropriate (e.g., different data pre-processing, evaluation protocol, or test set).

- **Unclear / potentially contradictory ablation results in Table 2.** Row 4 of Table 2 reports AUROC_I = 0.967 with AUPRO = 0.947, while the full model (Row 5) reports 0.922 with AUPRO = 0.966 — both under the same 10-shot MVTec-3D-AD setting. If Row 4 is a configuration with a subset of the full model's modules, its higher AUROC_I contradicts the paper's statement that "removing each component from the full model results in a consistent performance drop" (line 270). The checkmark pattern in the extraction is garbled, so the exact configuration of Row 4 cannot be verified from the available text. The authors must clarify what each row represents and resolve this numerical discrepancy.

### Minor
- **APR's robustness to anomaly contamination is argued theoretically but not empirically verified.** Section 3.3 argues that anomalous tokens contribute weakly to prototype updates due to OT balancing and low affinity, but no controlled experiment (e.g., comparing static prototypes vs. APR on normal-only vs. mixed test sets, or measuring prototype drift on anomalous inputs) is provided. While the overall ablation (Table 2) shows APR improves performance, this does not directly confirm that the *mechanism* resists anomaly contamination as claimed.

- **No statistical significance reported.** Results are given as point estimates without standard deviations or multiple-seed runs. In few-shot settings (5, 10 shots) where variance can be substantial, this makes it difficult to assess whether the observed margins (e.g., +3.7 AUROC_I over INP-Former at 10-shot) are statistically stable.

- **No limitations or failure case discussion.** The paper does not include a limitations section. Potential issues worth discussing include: sensitivity to surface-normal estimation quality, the uniform prototype assignment constraint (Eq. 1) forcing equal prototype usage even when a sample lacks some normal patterns, and the risk of APR adapting to anomalous features in challenging cases.

- **The codebook size ablation (Table 5) is conducted in the all-shot rather than few-shot setting**, which is the paper's central focus. The few-shot regime may exhibit different sensitivity to K.

### Trivial
- The first column header in Table 2 reads "BFA" rather than "BPA" (likely a typo in the original paper).

## Nice-to-Haves
- Include a controlled comparison where M3DM, CFM, and other MAD baselines are re-implemented with the same frozen DINOv2 backbone and surface-normal inputs, to fully isolate the effect of the proposed modules from backbone strength.
- Add an analysis of prototype drift (e.g., plot of average prototype change magnitude on normal vs. anomalous test samples) to empirically validate APR's claimed robustness.
- Break down the computational cost of APR (GRU update per sample) in the efficiency analysis.

## Removed Points
These points are flagged to be removed — treat them with caution:

1. **"Uncontrolled backbone is a critical flaw that may explain the entire performance gap"** — This is inaccurate. INP-Former, the strongest baseline, is explicitly stated to use the same ViT-B/14 DINOv2 backbone and input resolution as PIRN (line 191-192). The gains over INP-Former are controlled. The critic's claim that the performance gap "may largely reflect the encoder quality" is speculative and contradicted by the controlled INP-Former comparison. Other baselines (M3DM, CFM, etc.) use their original backbones, which is standard practice.

2. **"No similar adaptation [to two streams] performed for other baselines"** — The other baselines (M3DM, CFM, 3D-ADNAS) are already multimodal methods that natively handle both RGB and 3D. No "adaptation to two streams" is needed. The adaptation was only necessary for INP-Former because it is originally a 2D method.

3. **"Both codebook size and decoder depth ablations are in the all-shot setting"** — Table 6 (decoder depth) is explicitly conducted in the 10-shot setting (Table 6 caption: "Ablation on the number of decoder layers in the 10-shot setting"). Only Table 5 (codebook size) is in the all-shot setting. This criticism is factually incorrect for Table 6.

4. **"Table 2 has a formatting error (checkmark pattern inconsistent)"** — The checkmark rendering is a PDF extraction artifact; all rows show all three checkmarks due to garbled character encoding. The actual submitted paper likely has clear checkmark patterns. However, the numerical discrepancy (0.967 vs 0.922) is retained as a Major weakness because it is a substantive concern.

## Novel Insights

None beyond the paper's own contributions. The reviews largely converge on the paper's stated strengths and raise standard evaluation concerns (baseline fairness, statistical rigor, mechanism verification) without offering a novel analytical perspective on the method.

## Suggestions
1. Include FIND in the main few-shot comparison table (Table 1) or provide a clear justification for its exclusion.
2. Clarify the configuration of each row in Table 2, especially the row achieving 0.967 AUROC_I, and resolve the apparent contradiction with the full model's 0.922.
3. Report results with multiple random seeds (at least 3) for few-shot settings and include standard deviations.
4. Add an empirical analysis of APR's robustness to anomalous inputs (e.g., prototype drift on normal vs. anomalous test samples).
5. Include a limitations section discussing potential failure cases and the scope of the claims.

## Score and Decision

The paper presents a well-motivated method with three clearly described components and generally solid experimental validation. The controlled comparison against INP-Former (same backbone) demonstrates real gains. The efficiency advantages are substantial. However, the omission of FIND from the main accuracy comparison and the unclear ablation configuration in Table 2 are notable issues that should be addressed before acceptance. The remaining concerns (statistical significance, APR verification) are standard weaknesses that do not invalidate the core contributions.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>