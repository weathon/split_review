## Summary

This paper proposes HiTNet, a dual-stream network for multimodal sentiment analysis under frame-level missingness. The hippocampal-inspired intra-modal enhancement stream uses semantic memory modules with dynamic retrieval and sparse activation networks to reconstruct missing features from residual intra-modal information. The thalamic-inspired inter-modal regulation stream uses confidence perception and adaptive cross-modal completion for quality-aware fusion. Experiments on MOSI, MOSEI, and SIMS show competitive results across a range of missing rates, with particular robustness under extreme (90%) missing data.

## Strengths

- **Systematic component-level ablation (Table 3).** The paper removes each module (SMM, CPM, intra-stream, inter-stream) and each auxiliary loss (L_ubl, L_cp, L_rec) and reports the effect on multiple metrics across two datasets. Most removals produce measurable degradation, providing direct evidence that the proposed components contribute to the overall performance. This goes beyond many papers that only ablate the final fusion step.

- **Generalization to modality-level missingness (Table 4).** The architecture, designed for frame-level missingness, is also evaluated on the harder setting of entirely missing modalities. On {V} and {A} single-modality conditions, HiTNet achieves ~59% Acc-2, a ~10% absolute improvement over the next-best baseline. This shows the confidence-based inter-modal regulation stream captures something genuinely useful about cross-modal quality beyond its primary training regime.

- **Residual gating mechanism (Eq. 3) addressing a known failure mode.** The paper correctly identifies that prior memory-based approaches (Lang et al., 2025; Pipoli et al., 2025) risk retrieving irrelevant content when the query is corrupted by missingness. The residual gate that scales the memory contribution before adding it to the original features is a concrete architectural improvement over direct lookup-and-replace.

- **Qualitative evidence at extreme missing rates (Figure 5).** Confusion matrices at 90% missing frames show LNLN collapsing predictions onto the neutral class while HiTNet maintains predictions across multiple sentiment categories. This visual evidence corroborates the aggregate metrics and makes the robustness claim concrete.

## Weaknesses

### Major

- **The headline "1.5%–2.0% average accuracy improvements" is not uniformly supported by the reported numbers (Tables 1–2).** Against P-RMF (the strongest baseline): MOSEI Acc-2 improves only +0.15%, SIMS Acc-2 improves +0.35%, SIMS Acc-5 improves +0.79%. On SIMS, HiTNet underperforms P-RMF on MAE (0.504 vs 0.500) and Corr (0.389 vs 0.414). The 1.5–2.0% range is only clearly reached by MOSEI Acc-7 (+2.56%) and possibly some specific per-missing-rate numbers deferred to the appendix. The paper should either qualify the claim more carefully or report a proper average across all metrics.

- **The confidence-perception module (CPM) is trained to predict the missing rate, which conflates "intrinsic completeness" with a purely statistical property (Section 3.5, Eq. 8).** The training target is $\hat{s}_m = 1 - r_m$ where $r_m$ is the missing ratio. A modality with 10% missing rate could lose the most informative frames while one with 70% missing rate retains them. The paper claims the CPM assesses "intrinsic completeness and confidence of modality $m$" (line 115), but the training signal only captures the proportion of zeros in the input — not the information value of what remains. This weakens the claim that the inter-modal stream "dynamically integrates high-quality cross-modal information while suppressing redundant interference."

- **TETFN baseline values on MOSEI appear anomalous (Table 1).** TETFN shows identical Acc-2 (69.76/67.68), F1 (65.69/63.29), and MAE (1.087) on both MOSI and MOSEI, and the Acc-7 of 30.30 is identical across datasets as well. The Acc-2 of 69.76 on MOSEI is 8+ points below the next-worst method (ALMT: 76.64/77.54). Since these numbers are "reported as in LNLTN" (line 189), the error may originate there, but the authors should verify and correct them before comparison.

- **No statistical significance measures.** Results are averaged over three seeds but no standard deviations, confidence intervals, or significance tests are reported. Many improvements over P-RMF are under 1%, and without variance estimates it is unclear whether these differences are meaningful.

### Minor

- **Loss weights vary dramatically across datasets** (Section 4.3, line 185): $\gamma$ (reconstruction loss weight) is 0.1 on MOSI and SIMS but 9.0 on MOSEI — a 90× range. This degree of sensitivity suggests the loss weighting is not robust and the reconstruction signal may be operating very differently across datasets. The paper references Appendix B.1 but the main text should briefly discuss why such extreme variation is necessary.

- **Ablation contains counterintuitive results that are not discussed (Table 3).** On MOSI, removing the utilization balance loss (w/o L_ubl) gives Acc-7 of 35.41 vs the full model's 35.26 — higher on this metric. On SIMS, removing the reconstruction loss (w/o L_rec) gives F1 of 79.03 vs 77.33. The paper states each loss is "indispensable" but these exceptions are not acknowledged. On most other metrics the full model leads, so this is not a fatal contradiction, but it warrants discussion.

- **Baseline adaptation for methods designed for complete data is unclear** (Section 4.4). MISA, Self-MM, MMIM, CENET, and TETFN were designed for complete data. The paper says results are "as in LNLTN" but does not state whether these baselines were adapted for the missing-data setting or run out-of-the-box on zero-filled inputs. Comparing a missing-data-specific method against unadapted baselines stacks the comparison.

### Trivial

- Figure 3 only shows missing rates up to 0.5, yet the abstract's strongest claim (72.20% at 90% missing on MOSEI) is deferred to the appendix. A reader evaluating the headline claim should be able to verify it from the main paper.
- The row label "w/o $L_{abs}$" in Table 3 appears to be a typo for $L_{ubl}$ (utilization balance loss).

## Nice-to-Haves

- The CPM could be trained on a more meaningful signal, such as a downstream task performance prediction for each modality separately, rather than the missing rate.
- The semantic memory module retrieves a single memory unit (arg max, Eq. 2). Top-k retrieval with weighted combination could be more robust and should be ablated.
- Storing memories from the half of training samples with zero missing rate (as used in the training protocol, line 179) rather than from all samples could reduce the accumulation of corrupted entries.

## Removed Points

- **"Semantic memory module stores and retrieves corrupted representations (structural/fatal)"** — removed. The input features $x_m$ used for memory storage and retrieval are from data with missing frames, but (1) the residual gating mechanism (Eq. 3) is specifically designed to handle this, and (2) during training, "half of the samples for each modality are randomly set to have zero missing rate" (line 179), so the memory bank accumulates a useful mix of clean and representative entries. This is a design choice common in memory-augmented networks, not a structural flaw.
- **"CPM predicts a known experimental parameter"** — removed. The model does NOT receive $r_m$ as input during testing; it must infer the missing rate from the features $x_m$. Predicting this from the data is a legitimate learning task.
- **"Worse than P-RMF on F1 on SIMS"** — removed. This is factually incorrect: HiTNet F1 (77.33) beats P-RMF F1 (74.65). The critic confused LNLT (79.43) with P-RMF.
- Various formatting/style nitpicks and missing appendix content (stripped by parser) — removed per hard rules.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the gap between the paper's claimed "intrinsic completeness" assessment and what the CPM actually learns (missing-rate prediction), and the selective framing of the 1.5–2.0% improvement claim — both useful for the authors to address but not novel observations about the field.

## Suggestions

1. **Re-calibrate the headline claim.** Report the average improvement across all metrics and datasets, and qualify it with the range observed. Avoid implying 1.5–2.0% is universal.
2. **Replace or augment the CPM training signal.** Consider training the confidence score to predict the downstream classification accuracy achievable from that modality's features (e.g., via a separate classification head per modality), making it a genuine measure of informativeness.
3. **Verify and correct the TETFN baseline.** Cross-check the MOSEI numbers against the original TETFN paper or re-run the baseline.
4. **Add standard deviations** to the main tables, or at minimum report them for key comparisons against the strongest baseline.
5. **Discuss the counterintuitive ablation results** (w/o L_ubl on MOSI, w/o L_rec on SIMS) and explain why the full model is still preferred.

## Score and Decision

**Calibration details:**

*Round 1 (bracketing):* Searched for "multimodal sentiment analysis missing data" papers across three bands. Weak anchors (avg 2.40–3.33) were clearly weaker papers on different problems. Middle anchors (4.50–6.00) were the relevant comparison set. Strong anchors (8.00) were on different topics (CLIP analysis, LVLM benchmarks) and not directly comparable.

*Round 2 (narrowing):* Searched for memory network / brain-inspired / confidence-estimation multimodal papers in the 4.0–7.0 range. Key anchors:
- **Sparse MoE as a New Retriever** (5.50, Reject): Similar in scope (retrieval-based approach for missing modalities). Criticized for limited novelty and unclear presentation. HiTNet has better presentation and more specific architectural contributions but similar-level weaknesses in overclaiming. Slightly weaker than this anchor.
- **SURE** (5.00, Reject): Uncertainty estimation for missing modalities. Criticized for ambiguous motivation and weak loss justification. HiTNet is comparable — both have reasonable methodology undermined by overclaiming and design-reality gaps.
- **Robust Multimodal Learning with Missing Modalities** (4.50, Reject): Parameter-efficient adaptation. Criticized as a straightforward application of existing techniques. HiTNet is clearly stronger.
- **MiDl** (6.00, Accept): TTA for missing modalities. Criticized for computational overhead and questionable assumptions but had a novel problem formulation and strong experiments. HiTNet is weaker than this anchor.
- **PGMF** (5.67, Reject): MSA using MLLM distillation. Criticized for limited novelty. HiTNet is comparable or slightly weaker.

The paper sits between SURE (5.00) and MoE-Retriever (5.50), closer to SURE given the overclaiming about 1.5–2.0% improvements and the gap between what the CPM is claimed to do and what it actually does. The methodological contribution (dual-stream architecture, residual gating, thorough ablation) is real but not enough to overcome these calibration issues at a high-stakes venue.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>