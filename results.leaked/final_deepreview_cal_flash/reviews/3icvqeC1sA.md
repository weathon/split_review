## Summary

ChaosNexus presents a foundation model for forecasting chaotic dynamical systems, built on a novel U-Net-style multi-scale Transformer (ScaleFormer) with mixture-of-experts layers and a wavelet-based frequency fingerprint. The model is pretrained on ~20K synthetic chaotic ODE systems and evaluated on 9,300 held-out synthetic systems plus a real-world weather forecasting benchmark (WEATHER-5K). It achieves state-of-the-art zero-shot performance on synthetic chaotic benchmarks (sMAPE@128 = 68.9, correlation dimension error = 0.203) and remarkably low zero-shot temperature MAE (< 1°C on 5-day global forecasts) that outperforms baselines trained from scratch on the target domain. The scaling analysis revealing that cross-system generalization is driven by system diversity rather than per-system data volume is a practically useful insight.

## Strengths

1. **Multi-scale ScaleFormer architecture is well-motivated and empirically supported.** The U-Net-style hierarchical encoder-decoder with patch merging/expansion directly targets the inherent multi-scale temporal structure of chaotic dynamics — a genuine limitation of single-resolution foundation models (Panda, DynaMix). Section 3.2 provides clear mathematical formulation, and Figure 5's attention visualizations confirm that shallow layers capture local oscillations while deep layers synthesize global structures.

2. **State-of-the-art zero-shot results on large-scale synthetic benchmark.** On 9,300 held-out chaotic systems, ChaosNexus achieves competitive point-wise accuracy (sMAPE@128 = 68.9) and the best attractor statistics (correlation dimension error = 0.203, KL divergence = 1.206) among all compared foundation models including Panda, Chronos-L, TimeMoE, and DynaMix. The Wilcoxon signed-rank tests (p < 0.05/0.01) confirm statistical significance against Panda (Figure 2).

3. **Impressive zero-shot transfer to real-world weather forecasting.** Without any fine-tuning on the target data, ChaosNexus achieves < 1°C MAE on 5-day global temperature forecasts, substantially outperforming competitive baselines (FEDFormer, PatchTST, Koopa, CrossFormer) trained from scratch on 473K target-domain samples (Figure 3). This demonstrates genuine transfer from synthetic chaotic pretraining to a real chaotic system.

4. **Scaling analysis provides a practically valuable design principle.** The controlled experiments (Figure 4b,c) cleanly separate the effects of data volume vs. system diversity, showing that generalization benefits from increasing the number of training systems but not from increasing per-system trajectories. This insight can inform dataset construction for future scientific foundation models.

5. **Composite training objective is well-matched to the problem.** The combination of MSE (short-term accuracy), MMD regularization (attractor fidelity), and MoE load-balancing loss is principled, and the strong D_frac and D_step metrics validate its effectiveness for long-term statistical preservation.

## Weaknesses

### Major

- **Weather MAE pattern across horizons is unexplained.** In Figure 3, ChaosNexus zero-shot achieves a nearly constant ~0.8°C MAE across all prediction horizons (24h to 120h), while every baseline shows the expected increasing trend with lead time. The paper reports this result without discussion or analysis. While direct multi-step forecasting (not autoregressive) could partially explain a flatter error profile, a constant error across 5 days for a chaotic system requires physical justification. Possible explanations exist (error dominated by systematic components the model captures well, chaotic component saturating quickly), but the paper does not provide them. The authors should report lead-time-resolved error, show variance across stations, include RMSE alongside MAE, and explain the flat profile. If this result is correct, a brief discussion would strengthen it; if there is an evaluation artifact, it must be corrected. This does not invalidate the paper's core claims, but it is the most significant unresolved question.

### Minor

- **Key ablation for the core contribution is not in the main text.** The paper identifies the multi-scale ScaleFormer as its primary architectural novelty, but the main body contains no controlled experiment isolating the encoder-decoder hierarchy from the other components (MoE, wavelet fingerprint, MMD regularization). The paper refers to "extensive ablation studies" in Appendix A, but the main text should present a single-scale variant comparison or a component ablation table to substantiate the central claim. Including such an experiment in the main body would substantially strengthen the paper.

- **MMD regularization formulation is ambiguous.** Equation (10) sums kernel evaluations over full trajectories (treating each entire trajectory as a sample), yet the text describes it as minimizing divergence between "state distributions." A trajectory-level MMD and a state-level MMD have fundamentally different effects for chaotic systems. The paper references Appendix C.4 for details, but the main text should clarify whether κ operates on individual states (with averaging over time) or on full sequences, and justify the choice for attractor preservation.

- **Panda baseline not shown in the main weather figure (Figure 3).** The paper states in Section 4.2 that Panda results exist in Appendix A.6 (Table 9) and that "ChaosNexus also outperforms Panda on many variable forecasting tasks." Panda is the most directly comparable model — a foundation model pretrained on the same corpus. Including Panda in the main weather bar chart (or at least referencing Table 9 in the caption/text) would make the real-world evaluation more interpretable.

- **Loss hyperparameters λ₁ and λ₂ not reported.** Section 3.4 introduces weighted losses (ℒ = ℒ_mse + λ₁ℒ_balance + λ₂ℒ_reg) but never states the values used. Sensitivity to these weights is not discussed. This is a minor reproducibility gap.

### Trivial

- Figure 3 caption and table use approximate values (~0.8, ~3.5, etc.) with no precision indicators. Including exact values or confidence intervals would improve precision.

- The claim in the abstract/intro that "existing architectures operate at a single resolution" is an overstatement when applied to the broader time-series foundation model literature, though it is accurate for Panda and DynaMix specifically.

## Nice-to-Haves

- The frequency fingerprint ablation (performance with vs. without the wavelet scattering conditioner) would quantify the contribution of this component.
- The multi-scale feature analysis (Section 4.4) is currently qualitative; correlating attention patterns with quantitative metrics (e.g., what fraction of test systems show Toeplitz-like vs. block patterns) would strengthen the claim.
- Controlled diversity scaling where total time points are fixed while the number of systems varies (described in text, but a dedicated figure would confirm the conclusion).
- Reporting the MAE for all weather variables (not just temperature) in the main text would give a more complete picture.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"Central contribution not directly ablated" (Harsh Critic #2) — presented as fatal/fundamental.** The paper explicitly states that "extensive ablation studies" exist in Appendix A. The removal of the appendix during parsing does not mean the studies do not exist. Per the conventions of this review, this criticism is demoted to the Minor tier above (main-text presentation), not treated as a fatal flaw. The criticism as originally framed ("the paper's primary contribution is not supported by the experimental design") overstates what is verifiable from the available text.

2. **"Panda comparison on weather is absent" (Harsh Critic #4).** The paper states that Panda results exist in Appendix A.6 (Table 9). Panda is evaluated on weather data; it is simply not shown in the main Figure 3 bar chart. This is a presentational choice, not an omission. Demoted to Minor above.

3. **"MMD kernel ambiguity is fatal" framing.** The ambiguity is real but limited to the main-text notation; the paper references Appendix C.4 for the full specification. Demoted to Minor.

4. **Pure formatting/style nitpicks** from the harsh critic's section-by-section notes (e.g., "the text calls it a 'frequency fingerprint' which is somewhat misleading") are removed as presentation preferences, not substantive weaknesses.

5. **Strength Finder's generic strengths** (e.g., "the problem is well-motivated", "important research question") are removed. Only concrete, evidence-backed strengths are retained.

6. **Scaling analysis comment about Figure 4(c) caption** — the text states the experimental design explicitly; requesting the same in the caption is a formatting preference.

## Novel Insights

The reviews surface a genuinely interesting tension that the paper itself does not fully address: the near-constant weather MAE across horizons could be interpreted either as a remarkable achievement (the model has captured all predictable structure and the residual is irreducible noise) or as a signal that the zero-shot model is essentially producing a climatological/diurnal-cycle forecast that happens to achieve low error on the deterministic component. Resolving this tension — through lead-time-resolved diagnostics, comparison with simple baselines like "predict the mean diurnal cycle," or analysis of which frequency bands the model captures — would substantially sharpen the paper's contribution. The scaling insight (diversity > volume) is genuinely novel and well-evidenced, and it provides actionable guidance for the community regardless of how the weather MAE question is resolved.

## Suggestions

1. **Provide a detailed analysis of the weather MAE across horizons.** Show RMSE, report variance across stations, and explain whether the constant error is expected given the model's direct multi-step forecasting strategy. If the model is effectively predicting the deterministic components (diurnal+seasonal) with the chaotic component contributing constant noise, state this explicitly and discuss its implications.

2. **Add a single-scale ablation to the main text.** Construct a variant of ChaosNexus without the encoder-decoder hierarchy (single-scale Transformer with the same MoE layers, fingerprint, and MMD loss) and compare. This directly validates the core architectural claim.

3. **Clarify the MMD kernel** — specify whether it operates on individual states or full trajectories, and justify the choice.

4. **Include Panda in the main weather figure** or at minimum reference Table 9 in the caption so readers do not need to find the appendix.

5. **Report λ₁ and λ₂ values** and brief sensitivity analysis.

6. **Add a simple "predict the mean diurnal cycle" baseline** to the weather experiments to calibrate what the 0.8°C MAE means.

## Score and Decision

### Calibration Report

**Round 1 (Bracketing):**
- Low band (< 3.5): PowerGPT (3.00, Reject), FIA-Net (2.50, Reject), TF-score (3.00, Reject), Lookback Window (3.25, Reject), Financial TS (1.80, Reject). These reject-level papers are substantially weaker than ChaosNexus.
- Mid band (3.5–7.5): DAM (7.00, Accept) — strong foundation model paper with some ablation concerns; FMint (4.50, Reject) — ODE foundation model, weaker experiments; WaveToken (5.50, Reject) — wavelet-based tokenization, incremental; GIFT-Eval (5.25, Reject) — benchmark paper; Reservoir Transformer (4.25, Reject).
- High band (> 7.5): Oscillatory SSM (8.00, Accept), FITS (8.00, Accept), TimeMixer++ (8.00, Accept), ACSSM (8.00, Accept), Feedback Neural ODE (8.00, Accept). These are strong accept papers; ChaosNexus does not match this tier.

**Round 1 bracket:** Between 4.5 and 7.5, with plausible narrow range 5.5–6.5.

**Round 2 (Narrowing):**
- CirT (6.00, Accept) — weather/chaotic forecasting with geometric transformer. Similar quality: both have novel architecture for chaotic systems, strong results, but some missing ablations/comparisons. ChaosNexus has more evaluation dimensions (synthetic + real) but a more concerning weather MAE pattern. Roughly comparable.
- Zero-shot Imputation for Dynamical Systems (6.25, Accept) — ODE foundation model, strong zero-shot results, some methodological concerns. Slightly stronger execution than ChaosNexus.
- Typhoon Trajectory Prediction (6.25, Accept) — physics-conditioned approach, solid paper. Comparable.
- In-context Fine-tuning (5.60, Reject) — incremental approach to time series FMs. Weaker than ChaosNexus.
- Time-MoE (7.33, Accept) — large-scale MoE foundation model. Stronger in scope and scale than ChaosNexus.

**Final placement:** ChaosNexus is comparable to CirT (6.00) and slightly weaker than Zero-shot Imputation (6.25) due to the unaddressed weather MAE concern. It is stronger than WaveToken (5.50, Reject) and FMint (4.50, Reject). The paper has a genuine architectural contribution, strong empirical results overall, and a practically useful scaling insight. The main unresolved issue (weather MAE pattern) is important but addressable in rebuttal and does not invalidate the core claims.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>