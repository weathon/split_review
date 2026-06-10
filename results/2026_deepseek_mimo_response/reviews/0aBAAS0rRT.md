## Summary
This paper proposes SigMap, a foundation model for wireless localization combining cycle-adaptive masked pre-training on CSI data with geographic prompt tuning via GNN-processed 3D maps. The approach achieves strong benchmark results and demonstrates cross-scenario few-shot transfer using ~100 labeled samples and only 0.085M trainable parameters.

## Strengths
- **Cycle-adaptive masking addresses a real shortcut-learning problem and is well-validated**: The paper identifies that generic masking allows interpolation shortcuts over periodic CSI patterns and proposes cross-correlation-based adaptive masking (Eq. 6, Section 3.3). Table 3 directly validates: adaptive masking achieves 0.673m MAE / 84.5% CDF@1m vs. grid-only (0.770m / 80.3%) and strip-only (0.753m / 75.3%).
- **Geographic prompt tuning yields large, consistent improvements across tasks**: The GNN-based map-as-prompt mechanism (Section 3.4, Algorithm 1) delivers a 31% MAE reduction for single-BS localization (1.564m vs. 2.275m, Table 1) and 14.7% for multi-BS (0.673m vs. 0.789m, Table 2), with only 0.085M trainable parameters (Table 5).
- **Strong cross-scenario transfer with minimal labeled data**: On unseen environments (DeepMIMO O2 and WAIR-D with 100 real-world city scenes), SIGMAP achieves 1.026m and 1.880m MAE, outperforming LWLM by 53.2% and 44.3% (Section 4.5), using frozen backbone and ~100 target samples.
- **Parameter-efficient design with practical deployment implications**: Fine-tuning requires only 0.085M parameters (0.7% of total), completes in 30 minutes for 1000 epochs, and inference takes 0.83ms/sample (Table 5).
- **Thorough multi-dimensional evaluation**: Experiments span single-BS NLoS, multi-BS collaborative, masking ablation, map modality ablation, cross-scenario generalization, and parameter efficiency analysis.

## Weaknesses

### Fatal
None

### Major
- **Zero-shot claim directly contradicted by few-shot experimental setup**: The abstract (line 9) and Section 1.2 contributions (line 43) explicitly claim "strong zero-shot generalization." However, Section 4.5 states: "only the downstream task heads are fine-tuned using limited target samples (approximately 100 instances per scenario)... This few-shot learning setup demonstrates the method's ability to rapidly adapt to new environments" (lines 317-318). Zero-shot means deploying with no target-domain data; the actual setup uses ~100 labeled samples per scenario. This mismatch appears in the abstract, contributions, and conclusion — it is not a peripheral misstatement but affects the paper's central framing.

- **Key model component (NLoS-aware attention) absent from methodology section**: Equation 11, defining the NLoS-aware attention mechanism with parameters W_NLoS and function φ, appears for the first time in Section 4.2 (Main Results, lines 247-251) and is described as "the key advantage" of the method. This component introduces new trainable parameters and an explicit attention mechanism over LoS/NLoS path decomposition, yet is never described in Section 3 (Methodology, Sections 3.1–3.5). A reader following the methodology cannot reconstruct the full model, undermining reproducibility.

### Minor
- **Numerical inconsistencies between text and tables**: Line 340 states "1.580 m on WAIR-D Scenario-2" but Table at line 336 shows 1.880m; verified: (3.375−1.880)/3.375 = 44.3%, confirming the table is correct. The same line reports "0.4% of parameters" while Section 4.6 (line 352) reports "0.7%" (0.085M/11.815M ≈ 0.72%). Likely typos, but concerning in a paper whose contribution rests on quantitative evidence.

- **Pre-training scope narrow for "foundation model" framing**: Pre-trained exclusively on DeepMIMO O1_3p5 — one ray-tracing configuration from one simulator (line 237). Cross-scenario transfer to WAIR-D partially mitigates this, but the pre-training diversity is limited relative to what the framing promises.

- **No real-world experimental validation**: All experiments use ray-tracing simulated data (DeepMIMO and WAIR-D). The gap between simulated and real CSI is well-documented in wireless literature. Even one real-world dataset would substantially strengthen practical relevance.

- **Radar chart (Figure 5) includes metrics not reported in results**: The chart shows axes "oss_scenario, NLoS, AoA, ToA" (lines 283–287) but only MAE, RMSE, and CDF@1m are reported in any result table. The plotted values for these additional axes are unsubstantiated by data in the paper body.

### Trivial
- **Cycle-adaptive masking specification incomplete**: The formula for d_final is never given explicitly; the paper says it is determined through "cross-correlation analysis" (Section 3.3). The relationship between strip-mask and grid-mask variants (Figure 3) to the single "adaptive" strategy described is also unclear from the methodology.

## Nice-to-Haves
- Report standard deviations or confidence intervals for all results (averages over 5 runs stated but no variance reported in any table).
- Ablate GCN depth and compare global pooling against spatially-aware pooling to assess prompt capacity.
- Conduct a genuine zero-shot experiment (no target fine-tuning at all) to cleanly delineate prompt-only contribution from few-shot adaptation.

## Removed Points
These points are flagged to be removed, treat them with caution.
- Harsh critic's concern about baselines being "few in number" — the baselines (OMP, CNN, SWiT, LWLM) span classical, deep learning, and recent SSL approaches and are adequate.
- Generic concern about "more specific evidence that existing methods fail" — the comparison tables demonstrate this directly.
- Concern about GCN with global pooling being "too simple" — the ablation in Table 4 provides evidence the mechanism works, and the 8% degradation from 3D to 2D is discussed by the authors.

## Novel Insights
The paper's key insight — that geographic 3D maps can serve as lightweight soft prompts enabling cross-scenario wireless localization with minimal fine-tuning — is genuinely novel and well-supported by experimental evidence. The cycle-adaptive masking strategy addressing CSI periodicity is a practical contribution to self-supervised wireless representation learning. The combination of periodicity-aware pre-training and map-as-prompt fine-tuning in a unified framework is the paper's most distinctive contribution.

## Suggestions
- Rename all "zero-shot" claims to "few-shot" or "data-efficient" throughout abstract, contributions, and conclusion to match the actual experimental setup.
- Move the NLoS-aware attention mechanism (Eq. 11) and its description into Section 3 (Methodology) so the model is fully specified in one place.
- Fix numerical errors on line 340: "1.580 m" → "1.880 m" and "0.4%" → "0.7%".

## Calibration Report

### Anchors Retrieved

**Round 1 (Bracketing):**
- `/XhdckVyXKg.md` — NormWear (foundation model for wearable sensing), avg 3.0, Reject — SigMap is substantially stronger with clearer methodological novelty and better evaluation.
- `/ntSP0bzr8Y.md` — PowerGPT (foundation model for power systems), avg 3.0, Reject — SigMap has more targeted contributions and stronger empirical validation.
- `/LqB8cRuBua.md` — Diffusion SigFormer (signal recognition), avg 2.0, Reject — SigMap is far stronger in every dimension.
- `/7zJDTnogdG.md` — ECG Foundation Model, avg 3.33, Reject — SigMap is more focused with stronger results.
- `/9TClCDZXeh.md` — Wi-GATr (wireless simulation with geometric transformers), avg 7.0, Accept — Stronger than SigMap: has real-world validation, equivariant architecture novelty, and no claim-evidence mismatches.
- `/29JDZxRgPZ.md` — EM-GANSim (EM simulation with GANs), avg 6.0, Reject — Comparable to SigMap; SigMap has more framework novelty but similar limitations (sim-only, missing details).
- `/eTWRCiMQ1z.md` — Self-Supervised PINN for pose estimation, avg 5.25, Reject — SigMap is stronger with clearer contributions and more thorough evaluation.
- `/S2WUJUETyc.md` — Sound Source Localization with DAS/PINN, avg 4.0, Reject — SigMap clearly stronger.
- `/oZtt0pRnOl.md` — Privacy-Preserving ICL, avg 8.0, Accept — Not topically related; much stronger paper.
- `/rfdblE10qm.md` — Reward Modeling for LLM Alignment, avg 8.0, Accept — Not topically related.
- `/KIgaAqEFHW.md` — miniCTX (theorem proving), avg 8.0, Accept — Not topically related.
- `/OI3RoHoWAN.md` — GenSim (robotic simulation), avg 8.0, Accept — Not topically related.

**Round 2 (Narrowing):**
- `/OHll7EfuSi.md` — Weight-Based Performance Estimation, avg 4.67, Reject — SigMap is stronger with more concrete contributions.
- `/Hjp1V6zlZi.md` — Extreme Universal Domain Adaptation, avg 5.0, Reject — SigMap has more domain-specific novelty and stronger results.
- `/7ipjMIHVJt.md` — DASFormer (self-supervised pretraining for DAS), avg 5.25, Reject — Similar paradigm (self-supervised pretraining for signal processing) but SigMap has clearer methodological novelty and more thorough evaluation.
- `/SYnIf4LxAG.md` — Cross-Modality Prompt Transfer, avg 6.5, Accept — Most comparable anchor. Both explore prompt tuning for cross-domain transfer. SigMap has stronger domain-specific results but the zero-shot claim issue and missing methodology are concerns that this anchor didn't have.
- `/dKlxDx2SoS.md` — Prompt Learning with Quaternion Networks, avg 6.67, Accept — SigMap is roughly comparable in contribution scope.
- `/74vnDs1R97.md` — Understanding Visual Concepts Across Models, avg 5.8, Accept — SigMap is comparable or slightly stronger.
- `/26XphugOcS.md` — Zero-Shot Continuous Prompt Transfer, avg 7.0, Accept — Stronger than SigMap with cleaner methodology.

### Bracket and Calibration Logic
- **Round 1 bracket**: 5.0–6.5. The paper is clearly stronger than rejected papers at 3–5.25 but has issues (zero-shot claim mismatch, incomplete methodology) that prevent it from reaching the 6.5–7.0 range of accepted papers like Wi-GATr and Cross-Modality Prompt Transfer.
- **Round 2 narrowing**: 5.5–6.5. The paper is better than DASFormer (5.25, Reject) due to more novel framework design and stronger results. It is comparable to EM-GANSim (6.0, Reject) but arguably has more methodological novelty. It falls short of Cross-Modality Prompt Transfer (6.5, Accept) due to the claim-evidence mismatch and structural methodology gap.
- **Final score**: 6.0. The paper sits at the border — it has genuine novelty and strong results, but the major weaknesses (zero-shot mislabeling, missing methodology component) are real and substantive rather than cosmetic. These issues are fixable but currently undermine the paper's credibility.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>