Now I have all the information I need. Let me write the final consolidated review.

## Summary

The paper proposes SigMap, a wireless localization foundation model that combines two innovations: (1) a cycle-adaptive masking strategy for self-supervised pre-training that prevents shortcut learning from periodic CSI patterns, and (2) a "map-as-prompt" framework that encodes 3D geographic information via GNNs into lightweight prompt tokens for parameter-efficient cross-scenario adaptation. The paper reports state-of-the-art performance on single-BS and multi-BS localization tasks using DeepMIMO data, and demonstrates few-shot generalization to unseen scenarios (DeepMIMO O2 and WAIR-D).

## Strengths

- **Novel and well-motivated masking strategy with clear empirical support.** The cycle-adaptive masking directly addresses the problem of models exploiting periodic shortcuts in CSI data. Table 3 shows concrete improvements: adaptive masking achieves 0.673 m MAE and 84.5% CDF@1m, outperforming grid-masking (0.770 m) and strip-masking (0.753 m) on multi-BS localization. This is a genuine contribution that addresses a domain-specific challenge.

- **Parameter-efficient design with practical appeal.** Table 5 shows only 0.085M trainable parameters during fine-tuning (0.7% of total), with inference at 0.83 ms/sample and fine-tuning completing in 30 minutes. The geographic prompt mechanism (Algorithm 1, Section 3.4) is cleanly designed and the paper demonstrates that even 2D map information retains most of the benefit (Table 4: 1.692 m vs 1.564 m MAE), making the approach practical for settings where only coarse geographic data is available.

- **Strong single-BS and multi-BS localization results.** SIGMAP achieves 1.564 m MAE for single-BS NLoS localization (34.4% better than LWLM's 2.382 m, Table 1) and 0.673 m MAE for multi-BS localization (improving over the next-best SIGMAP w/o map at 0.789 m, Table 2). The map-as-prompt contribution is well-demonstrated by the consistent gap between w/ map and w/o map variants across all tasks.

- **Physically grounded formulation.** Section 2 provides a clear connection between the CSI signal model (Eq. 1), ray-tracing (Eq. 2), and the localization objective (Eq. 3), establishing a sound foundation for the proposed method's design choices.

## Weaknesses

### Fatal
None.

### Major

- **The generalization comparison is uncontrolled — the paper's headline claim rests on it.** Section 4.5 evaluates generalization by fine-tuning only task heads with ~100 samples while the backbone remains frozen, but it is never stated whether the sole external baseline (LWLM) was evaluated under the same frozen-backbone few-shot protocol or retrained with its original full-data supervised pipeline. The generalization table compares SIGMAP w/ map, SIGMAP w/o map, and LWLM only — SWiT, CNN, and OMP are absent entirely. Since cross-scenario generalization is the paper's primary contribution claim, having this supported by a single baseline under unknown conditions is a significant evidential gap.

- **Numerical discrepancy between text and table for WAIR-D results.** The text in Section 4.5 states "SIGMAP reaches...1.580 m on WAIR-D Scenario-2," but the table shows 1.880 m MAE for that entry. The percentage improvement (44.3%) is consistent with 1.880 m, confirming the text value is a typo. This error appears in the paper's headline result and must be corrected.

- **NLoS-aware attention mechanism (Eq. 11) is introduced in the results section but absent from the methodology.** Equation 11 defines $\mathbf{W}_{\text{NLoS}}$ and $\phi$ with no prior introduction in Section 3. The paper attributes SIGMAP's single-BS performance advantage to "our NLoS-aware attention mechanism" (Section 4.2), yet this mechanism has no architectural description, no discussion of where it fits in the task head, and no definition of $\phi$. A core component of the method is presented without specification.

### Minor

- **Abstract claims "zero-shot generalization" but the method uses few-shot fine-tuning.** The abstract states the model exhibits "strong zero-shot generalization in unseen environments," and Section 1.2 claims "strong zero-shot generalization." However, Section 4.5 explicitly fine-tunes task heads with ~100 target samples and describes this as "few-shot learning setup." This is a misleading characterization that should be corrected.

- **The geographic prompt compresses all 3D spatial information into a single vector without justification or ablation.** Algorithm 1 performs GlobalMeanPool over all graph node features and projects through a single MLP to produce one prompt vector $\mathbf{g}_{\text{prompt}} \in \mathbb{R}^{D_p}$. For complex urban environments with hundreds of buildings, this is a strong information bottleneck. The paper does not justify why a single global vector is sufficient, nor does it ablate the number of prompt tokens. The 8% MAE gap between 3D and 2D maps (Table 4) could partly reflect this compression ceiling.

- **No standard deviations or confidence intervals are reported.** All tables present single-point results despite claiming "averaged over 5 independent runs." Without variability measures, it is impossible to assess whether performance differences (e.g., 0.673 vs 0.789 in Table 2) are statistically meaningful.

- **Cycle-adaptive masking computation is under-specified.** Equation 6 references $d_{\text{final}}$ and $j_0$ with only verbal descriptions ("detected periodicity shift," "starting offset") and mentions "row-wise cross-correlation" without an equation, search range, or computational cost analysis. The paper's first core innovation deserves a pseudocode block comparable to Algorithm 1.

- **Radar chart axes are undefined.** Figure 5 includes axes labeled "oss_scenario," "NLoS," "AoA," "ToA" that are never defined or referenced in corresponding tables. The figure is uninterpretable without explanation.

### Trivial

- Table labeling: the generalization table is referenced as "Table 4.5" alongside an existing "Table 4," creating ambiguity.

## Nice-to-Haves

- Ablate the prompt mechanism: vary the number of prompt tokens (1 vs. 4 vs. 8), compare GNN-based prompt against a simple MLP baseline on raw coordinates, and compare against alternative map encodings (e.g., rasterized occupancy grids).
- Provide a control using SigMap's backbone with standard random masking to disentangle the cycle-adaptive masking contribution from architectural/scale differences with baselines.
- Apply the same few-shot fine-tuning protocol to LWLM and SWiT for controlled generalization comparison.

## Removed Points

These points are flagged to be removed, treat them with caution.

- **"Baselines are too few"** — While only four baselines are compared, this is common in domain-specific wireless localization papers where few published methods are directly comparable. The real issue is the uncontrolled generalization comparison (kept above), not the baseline count per se.
- **MAE-vs-RMSE inconsistency in Table 3** — The critic notes adaptive masking has best MAE but not best RMSE compared to strip-masking. While true, this is not inherently problematic; MAE and RMSE weight outliers differently, and the adaptive masking still dominates on CDF@1m. This is a minor observation that does not undermine the masking contribution.
- **"Eq. 6 references undefined parameters"** — While the parameters could use more specification, the harsh critic's framing that they are entirely undefined is overstated: the text does describe them qualitatively (kept as a minor point above regarding under-specification).
- **Formatting/typo concerns** — Any parsing artifacts in the extracted text are not paper issues.
- **Strength about "comprehensive evaluation"** — Removed because the evaluation has verified gaps (uncontrolled generalization, missing baselines in generalization table, no std deviations) that contradict a claim of comprehensiveness.

## Novel Insights

The key novel insight is that wireless CSI data has domain-specific periodicity structures that generic masking strategies (random, grid, strip) fail to handle — models exploit these periodic shortcuts rather than learning meaningful signal representations. The cycle-adaptive masking strategy is a principled solution to this domain-specific problem. Additionally, the map-as-prompt framework demonstrates that geographic information can be efficiently encoded through graph neural networks and injected as soft prompts, enabling cross-scenario transfer with minimal parameter updates — a promising direction for wireless foundation models.

## Suggestions

1. **Fix the WAIR-D MAE typo** (1.580 → 1.880) in Section 4.5.
2. **Correct "zero-shot" to "few-shot"** in the abstract and Section 1.2.
3. **Specify the NLoS-aware attention mechanism** (Eq. 11) in Section 3 with proper architectural detail.
4. **Report standard deviations** across the 5 runs for all tables.
5. **Control the generalization comparison** by applying the same frozen-backbone few-shot protocol to LWLM (and ideally SWiT).
6. **Define radar chart axes** in Figure 5's caption or provide corresponding disaggregated tables.

## Calibration Report

**Round 1 anchors (bracketing):**
| Anchor ID | Topic | Avg Score | Round | Comparison |
|---|---|---|---|---|
| XhdckVyXKg | Foundation model for wearable sensing | 3.00 | 1 | Weaker: narrower scope, no clear novelty |
| 7zJDTnogdG | ECG foundation model | 3.33 | 1 | Weaker: less domain-specific innovation |
| ntSP0bzr8Y | Foundation model for power systems | 3.00 | 1 | Weaker: generic application |
| DYXl6P70aH | Foundation model for remote sensing | 3.00 | 1 | Weaker: only benchmarking |
| 9TClCDZXeh | Wireless simulation with Geometric Transformers | 7.00 | 1 | Stronger: real-world validation, novel architecture |
| 7KDuQPrAF3 | Foundation model for error correction codes | 6.25 | 1 | Similar: ambitious but limited validation scope |
| k2uUeLCrQq | Motion foundation model for wearables | 6.75 | 1 | Stronger: billion-scale pretraining, thorough eval |
| 7ipjMIHVJt | Self-supervised pretraining for earthquake monitoring | 5.25 | 1 | Weaker: weaker baselines, application-focused |
| PdaPky8MUn | Fair comparison of long-sequence models | 8.00 | 1 | Stronger: fundamental methodology contribution |

**Round 1 bracket: 5.0–7.0**

**Round 2 anchors (narrowing):**
| Anchor ID | Topic | Avg Score | Round | Comparison |
|---|---|---|---|---|
| cADpvQgnqg | Foundation models for hypernetworks | 5.50 | 2 | Similar: limited validation but novel concept |
| 29JDZxRgPZ | EM simulation with conditional GANs | 6.00 | 2 | Similar: wireless domain, GAN approach |
| rAX55lDjtt | Acoustic prompt tuning for LLMs | 4.60 | 2 | Weaker: prompt tuning but less validated |
| uiBLOcyTIA | Next location prediction with LLMs | 5.25 | 2 | Weaker: LLM application, rejected |
| MBBRHDuiwM | Unsupervised representation learning (URLOST) | 6.40 | 2 | Similar: missing error bars, interesting method |
| WcOohbsF4H | Spatio-temporal masked ECG modeling | 7.00 | 2 | Stronger: thorough SSL baselines, cleaner eval |
| VmJdqhuTCh | Frequency-guided masking for SSL | 6.50 | 2 | Similar: domain-specific masking innovation |
| LokR2TTFMs | 3D MAE for point clouds | 6.50 | 2 | Similar: MAE contribution, good validation |

**Round 2 bracket: 5.5–6.5**

**Final calibration:** SigMap is weaker than ST-MEM (7.00, thorough SSL baselines, clean evaluation) and Wi-GATr (7.00, real-world validation, novel architecture), but stronger than DASFormer (5.25, weak baselines, rejected) and the Acoustic Prompt Tuning paper (4.60, rejected). It is comparable to URLOST (6.40, interesting method but missing error bars) and FECCT (6.25, ambitious but limited validation). The uncontrolled generalization comparison and numerical error pull it below the 6.4–7.0 anchors, but the genuine innovations and strong main results keep it above the rejected ~5.0 papers. Final score: 6.0.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: Accept