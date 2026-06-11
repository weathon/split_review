Now I have sufficient calibration data. Let me finalize the review.

**Calibration Analysis:**

Round 1 bracket: **5.5 – 6.5**

Key anchors retrieved across all rounds:
- **Wi-GATr** (wireless sim, geometric transformers): 7.00, Accept — stronger paper with real-world validation
- **Foundation Model for ECC**: 6.25, Accept — similar "foundation model" ambition, validation questioned
- **BayesPrompt** (prompt tuning): 6.25, Accept — prompt tuning, few-shot, limited domain
- **EM-GANSim** (EM simulation, wireless): 6.00, Reject — wireless domain, simulated-only, methodology gaps
- **DASFormer** (self-supervised signal): 5.25, Reject — self-supervised for signal data, insufficient comparison
- **C-MELT** (ECG pre-training): 5.50, Reject — self-supervised pretrain for signals
- **WiFi 3D Mesh**: 4.00, Reject — WiFi/CSI, limited novelty
- **NormWear** (wearable foundation model): 3.00, Reject — foundation model claim, rejected
- **Domain Prompt Few-Shot**: 3.25, Reject — prompt tuning, limited contribution

SigMap has cleaner ablations and stronger quantitative results than DASFormer (5.25) and C-MELT (5.50), but has a more damaging claim-evidence mismatch (zero-shot inflation) than EM-GANSim (6.00). It's comparable to Foundation Model for ECC (6.25) but the zero-shot claim is more problematic. Settling on **6.0**.

---

## Summary
SigMap proposes a wireless localization foundation model combining cycle-adaptive masked autoencoding for self-supervised pre-training on CSI data with geographic prompt tuning via GNNs that encode 3D building geometry as soft prompt tokens. The system is evaluated on ray-tracing simulated datasets (DeepMIMO, WAIR-D) for single-BS, multi-BS, and cross-scenario localization tasks.

## Strengths
- **Cycle-adaptive masking outperforms fixed masking baselines:** Table 3 shows adaptive masking achieves 0.673 m MAE and 84.5% CDF@1m, outperforming grid-masking (0.770 m, 80.3%) and strip-masking (0.753 m, 75.3%), directly validating the claim that standard masking allows periodic shortcut exploitation in CSI data.
- **Cross-scenario generalization with minimal labels:** Section 4.5 demonstrates 1.026 m MAE on unseen DeepMIMO O2 and 1.880 m on WAIR-D (100 cities), improving over LWLM by 53.2% and 44.3% respectively, with only ~100 target samples and a frozen backbone.
- **Geographic prompts yield substantial, ablated accuracy gains:** Table 4 shows a clean 3-step ablation: 3D map (1.564 m MAE) → 2D map (1.692 m) → no map (2.275 m), a 31% total improvement, providing specific evidence that the map-as-prompt mechanism meaningfully encodes environmental constraints.
- **Consistent SOTA across task configurations:** Tables 1 and 2 show SigMap achieves best MAE/RMSE/CDF@1m on both single-BS (1.564/5.675/60.5%) and multi-BS (0.673/1.099/84.5%) tasks, outperforming the best baseline LWLM by 34.4% and 18.7% in MAE.
- **Quantified parameter efficiency:** Table 5 documents that fine-tuning updates only 0.085M of 11.730M parameters (0.7%), completing 1000 fine-tuning epochs in 30 minutes with 0.83 ms/sample inference.

## Weaknesses

### Fatal
None.

### Major
- **"Zero-shot" claim is misleading — the evaluation is few-shot fine-tuning.** The abstract (line 9) and Section 1.2 (line 43) explicitly claim "strong zero-shot generalization to unseen environments." However, Section 4.5 (line 317) states: "only the downstream task heads are fine-tuned using limited target samples (approximately 100 instances per scenario), while the self-supervised backbone remains frozen," and the paper itself calls this "few-shot learning setup" (line 317). A frozen backbone with a task head fine-tuned on 100 labeled target samples is standard transfer learning, not zero-shot. This claim-evidence mismatch directly inflates the paper's stated contribution and undermines credibility. The authors should either present a genuine zero-shot experiment (no labeled target data) or reframe as "efficient few-shot adaptation."
- **NLoS-aware attention mechanism (Eq. 11) appears in results but is absent from methodology.** Section 4.2 (lines 247–251) introduces Eq. 11 as "the key advantage," using notation ($\mathbf{o}_s^{(i)}$, $\mathbf{W}_{\text{NLoS}}$, $\phi$) that never appears in Section 3. The methodology describes standard self-attention (Section 3.4) and multi-BS fusion attention (Eq. 9–10 in Section 3.5), neither of which matches Eq. 11. This creates a reproducibility and coherence problem: the reader cannot determine what model actually produced the reported results.

### Minor
- **All main results are in-domain (same scenario as pre-training).** The main results (Tables 1–4) use DeepMIMO O1_3p5, the same scenario used for pre-training (line 237). While the labeled fine-tuning split is separate from unlabeled pre-training data, the model has already seen CSI from this exact environment. The cross-scenario experiments (Section 4.5) partially address this but use a different protocol (frozen backbone + few-shot). This limits the strength of the "cross-scenario" framing for the main results.
- **No real-world measured data.** All evaluation uses ray-tracing simulated datasets (DeepMIMO, WAIR-D). For a paper claiming "foundation model" status with "strong generalization," the absence of any real-world measured CSI dataset is a notable limitation, as ray-tracing may not capture hardware imperfections, dynamic obstacles, or material-dependent propagation effects.
- **Large MAE-RMSE gap not discussed.** In Table 1, SIGMAP (w/ map) has MAE 1.564 m but RMSE 5.675 m (ratio 3.6×), much larger than for baselines (LWLM: 2.382/5.822, ratio 2.4×). This suggests heavy-tailed error distributions with severe outliers, which the paper does not acknowledge.
- **No variance/confidence intervals reported.** Results are "averaged over 5 independent runs" (line 239) but no standard deviations are shown. Given single-digit percentage differences between methods, this limits the reader's ability to assess statistical significance.

### Trivial
- **Numerical typo in Section 4.5.** Line 340 states "1.580 m on WAIR-D Scenario-2" but the table (line 336) shows 1.880 m. The 44.3% improvement matches the table value.
- **Table mislabeling.** The cross-scenario results table is referred to as "Table 4.5" (line 317) rather than receiving a proper sequential number.

## Nice-to-Haves
- Include at least one real-world measurement dataset, even small-scale, to validate practical applicability.
- Discuss the MAE vs RMSE gap — what percentage of samples have very large errors?
- The term "foundation model" is somewhat inflated for a ~11.7M parameter model pre-trained on a single simulated environment; consider more precise terminology or broader pre-training.

## Removed Points
These points are flagged to be removed, treat them with caution.
- **"Foundation model" terminology overstatement**: While valid, this is a soft concern — many papers in the field use this term loosely. The technical contribution stands regardless. Demoted to Nice-to-Have.
- **Limited baselines** (only 5 methods): The baselines chosen (OMP, CNN, SWiT, LWLM) are representative of the field. Not a significant weakness.

## Novel Insights
The combination of cycle-adaptive masking (disrupting periodic shortcuts in CSI) with geographic prompt tuning (GNN-encoded 3D map information as soft tokens) is a genuinely novel architectural concept for wireless localization. The ablation evidence (Tables 3–4) cleanly separates the contributions of each component, and the cross-scenario results suggest that environment-agnostic pre-training + environment-specific prompts is a viable paradigm for wireless signal processing generalization.

## Suggestions
1. **Fix the zero-shot claim.** Present a true zero-shot experiment where no labeled target data is used — the map prompt should enable this naturally. Alternatively, reframe as "efficient few-shot adaptation."
2. **Complete the methodology.** If the NLoS-aware attention (Eq. 11) is part of the model, describe it fully in Section 3 with proper notation. If not, remove from the results discussion.
3. **Report per-run variance** (standard deviation or confidence intervals).
4. **Fix the numerical typo** (1.580 → 1.880) and table numbering.

## Reporting: Score Calibration

**Round 1 bracket: 5.5 – 6.5.** All anchors:
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| 9TClCDZXeh (Wi-GATr) | 7.00 | 1 | Stronger: real-world validation, cleaner novel architecture |
| 7KDuQPrAF3 (ECC foundation) | 6.25 | 1 | Similar: foundation model claim, validation questioned, but no claim-evidence mismatch |
| DmD1wboID9 (BayesPrompt) | 6.25 | 1 | Similar: prompt tuning, few-shot, but domain-specific |
| 29JDZxRgPZ (EM-GANSim) | 6.00 | 1 | Related: wireless domain, simulated-only, methodology gaps |
| 1mjsP8RYAw (SFAVEL) | 6.00 | 2 | Similar: self-supervised pretrain, good ablations |
| 5fS03oP3q6 (C-MELT) | 5.50 | 2 | Similar: self-supervised pretrain for signals |
| 7ipjMIHVJt (DASFormer) | 5.25 | 1 | Similar: self-supervised for signal data, weaker ablations |
| q3WzT2mrhB (WiFi 3D Mesh) | 4.00 | 1 | Related: WiFi/CSI, limited novelty |
| XhdckVyXKg (NormWear) | 3.00 | 1 | Related: foundation model claim, rejected |
| YRJDZYGmAZ (Domain Prompt) | 3.25 | 1 | Related: prompt tuning for domain adaptation |

SigMap has cleaner ablations and stronger results than DASFormer (5.25) and C-MELT (5.50), placing it above 5.5. However, the zero-shot claim-evidence mismatch and NLoS attention methodology gap are more serious issues than what EM-GANSim (6.00) had. It's comparable to Foundation Model for ECC (6.25) but the misleading zero-shot claims are a more damaging credibility issue. Final score: **6.0**.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>