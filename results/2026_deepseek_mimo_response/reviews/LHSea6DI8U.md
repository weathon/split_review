Now I have enough calibration data. Let me finalize my assessment.

**Calibration Summary:**

Round 1 bracket: The paper sits between the rejected continual forecasting papers (TFMoE 4.00, SKI-CL 5.33) and the accepted EAC (6.75). Initial bracket: 5.0-7.0.

Round 2 narrowing: The paper is clearly stronger than DyGPrompt (6.00, accepted with uniform 6s) given its much stronger empirical results and more practical contribution. It's comparable to but slightly below Fast/Slow Streams (7.00, accepted with 8,6,6,8), which had a more novel methodological insight. The paper's overclaiming about distributional drift and missing ablations prevent it from matching EAC's score (6.75).

Final comparison:
- vs. TFMoE (4.00): Clearly stronger — multiple datasets, better baselines, comprehensive evaluation
- vs. SKI-CL (5.33): Stronger — better empirical results, more comprehensive
- vs. DyGPrompt (6.00): Stronger contribution with better experiments
- vs. EAC (6.75): Claims to outperform empirically, but EAC had cleaner contribution with theoretical analysis; this paper has overclaiming issues
- vs. Fast/Slow Streams (7.00): Below — FS had a more novel insight (information leakage)

**Final score: 6.0**

This paper is a solid empirical contribution with strong results on traffic datasets, but is held back by overclaiming about distributional drift handling and missing critical ablations. It clearly outperforms rejected papers in the same space and has a coherent framework, but doesn't quite reach the level of the best accepted papers in the area.

## Summary

This paper proposes STBP, a framework for continual spatio-temporal forecasting that combines a frozen general-purpose backbone (FreNet for frequency-domain temporal processing + DLGA for dual-stream linear graph attention) with an incrementally expandable contextual pattern bank of per-node trainable embeddings. The backbone is jointly trained with the pattern bank initially, then frozen while only the pattern bank expands and fine-tunes in subsequent periods. Experiments on three streaming datasets show substantial improvements over CSTF baselines, particularly on traffic datasets (21%+ MAE reduction over the best baseline EAC).

## Strengths

- **Large, consistent performance gains on traffic datasets**: STBP reduces average MAE by 21.44% and 21.93% over the best baseline (EAC) on PEMS-Stream and CA-Stream respectively (Table 1), with gains across all three metrics (MAE, RMSE, MAPE) and all forecasting horizons (3, 6, 12 steps). This is a substantial and consistent improvement.

- **Ablation demonstrates backbone importance**: The "w/o Backbone" variant (replacing FreNet+DLGA with CNN/GCN from prior CSTF methods) shows significant degradation (Figure 4), and the backbone alone (without pattern bank) already matches EAC's performance, providing evidence that both components contribute independently and that the backbone design itself is a meaningful contribution.

- **Interpretable pattern bank structure**: t-SNE visualizations (Figures 3, 6) show meaningful clusters in the pattern bank, with nodes in the same cluster exhibiting similar temporal dynamics and new nodes correctly grouping into existing clusters after incremental expansion—validating the relevance/heterogeneity distinction without explicit clustering constraints.

- **Few-shot robustness**: Under 10% data setting, STBP outperforms all baselines by 16-19% margin over second-best EAC on PEMS-Stream and CA-Stream (Table 2), demonstrating effective knowledge transfer from historical periods.

- **Practical efficiency**: Despite a more complex backbone, STBP incurs only minimal training time overhead compared to lightweight baselines like EAC (Figure 8), with linear attention reducing spatial complexity from O(N²) to O(N).

## Weaknesses

### Fatal
None.

### Major

- **Distributional drift mitigation claim is overstated relative to the frozen-backbone design**: The paper repeatedly frames the backbone as "mitigating distributional drift" (lines 26, 108, 112, 120, 238) as one of its four key challenges (line 24). However, after τ=1, the entire backbone—including the learnable frequency-domain embedding F_τ—is frozen (lines 86-87). A frozen backbone cannot adapt to new distributional shifts. The paper argues that low-frequency components are "more resilient to distributional changes" (line 120), but this is asserted without evidence—no analysis shows that the learned frequency features actually remain effective as distributions shift. Adaptation in τ>1 occurs only through the pattern bank's gating interaction with the frozen backbone (Eq. 5), which is a much weaker mechanism than the framing implies. The paper should either provide empirical evidence (e.g., visualizing FFT spectra stability across periods) or reframe the backbone's role as capturing generalizable temporal patterns rather than "mitigating distributional drift."

- **Missing critical ablations**: The ablation study (Section 5.3, Figure 4) tests Retrain, Online, w/o Backbone (replacing entire backbone with CNN/GCN), and w/o DLGA. However: (1) There is no FreNet-specific ablation—replacing FreNet with a standard temporal module (TCN, GRU) while keeping DLGA intact. The "w/o Backbone" variant conflates FreNet and DLGA contributions. (2) The three pattern bank components P^(0) (input gating), P^(1) (output scaling), P^(2) (attention key) each play distinct roles (Eqs. 5, 9), but their individual contributions are never isolated. (3) The gating mechanism (Eq. 5) is not compared against simpler integration strategies (e.g., direct addition or concatenation). Without these ablations, it is difficult to determine which design choices actually drive the performance gains versus which are incidental.

### Minor

- **Unexplained dataset-dependent performance gap**: STBP achieves 21%+ MAE reductions on traffic datasets but only 2.35% on AIR-Stream (line 238). On AIR-Stream RMSE, the difference is 37.76 vs. 37.83 (0.07), well within reported standard deviations (±0.30 and ±0.60). The MAPE improvement is more meaningful (6.5%), but the paper never discusses what properties of traffic vs. air quality data cause this discrepancy or whether the method's advantages are domain-specific (e.g., strong periodicity in traffic data aligning well with frequency-domain processing).

- **Pattern bank parameter drift during incremental fine-tuning**: At τ>1, the entire P'_τ (including old node parameters from P_{τ-1}) is fine-tuned (line 98: "Only the expanded contextual pattern bank P'_τ is fine-tuned during training"), with no regularization or partial freezing to prevent old embeddings from drifting. While experiments show it works in practice, this could reintroduce forgetting at the node-embedding level. The paper does not analyze or constrain this drift.

### Trivial

- **Privacy claim unsupported**: Line 104 claims the pattern bank supports "privacy protection" because it stores "high-level abstractions rather than raw historical data." This claim requires formal substantiation (e.g., information-theoretic or differential privacy analysis) and should either be substantiated or removed.

## Nice-to-Haves

- Analysis of what makes AIR-Stream different from traffic datasets and why STBP's advantages diminish there would strengthen claims of domain generality.
- Reporting tabular training time and memory numbers (currently only in scatter plots in Figure 8) would improve reproducibility.
- Characterizing incremental period details (nodes added per period, temporal span) directly in the main text rather than deferring to appendix would help readers understand the continual learning difficulty.

## Removed Points

These points are flagged to be removed, treat them with caution.

- The harsh critic's concern about Table 1 formatting being "severely garbled" is a PDF parsing artifact, not an author error. Removed.
- The few-shot experiment "favoring STBP" concern was partially kept as Minor, but the structural advantage (frozen pre-trained backbone) IS the core contribution of the paper—the comparison validates CSTF methods' advantage in low-resource settings.
- The strength about "prompt-based gating mechanism" was dropped as it's a reasonable but not exceptionally novel integration strategy compared to existing prompt tuning approaches.
- The strength about "privacy/storage efficiency from not storing raw data" was dropped as the privacy claim is unsubstantiated (see Trivial weakness).

## Novel Insights

The paper's most interesting empirical finding is that the frozen backbone alone (without pattern bank) matches EAC's performance, while the pattern bank with a simpler backbone also matches EAC—yet their combination far exceeds both. This suggests genuine complementarity between backbone and pattern bank that goes beyond simple stacking, and validates the paper's core thesis that bridging strong STGNNs with continual learning strategies yields emergent benefits. The t-SNE analysis of the pattern bank showing autonomous clustering without explicit clustering constraints is also a noteworthy finding.

## Suggestions

1. Add a FreNet ablation: replace FreNet with TCN/GRU while keeping DLGA and pattern bank, to isolate FreNet's contribution.
2. Add individual P^(i) ablations to show which pattern bank components matter most.
3. Either provide empirical evidence that frequency features remain stable across periods or reframe the backbone's role more modestly.
4. Discuss the AIR-Stream performance gap—analyze domain-specific properties that explain the difference.

## Calibration Report

**Anchors retrieved:**

| Paper | Avg Score | Round | Relevance |
|-------|-----------|-------|-----------|
| CeGNN (0je4SA7Jjg) | 3.40 | 1 | Low - spatiotemporal dynamics, not continual learning |
| STGAT forex (5x9kfRXhBd) | 3.00 | 1 | Low - forex forecasting |
| DIRAD (ZHTYtXijEn) | 2.33 | 1 | Low - continual structural adaptation |
| Domain-grounding (TYyzypZrgU) | 2.50 | 1 | Low - spatiotemporal reasoning |
| TFMoE (vJGKYWC8j8) | 4.00 | 1 | High - continual traffic forecasting, clearly weaker |
| EAC (FRzCIlkM7I) | 6.75 | 1 | Very high - main baseline, accepted (3,8,8,8) |
| C²INet (5IvTw0qMKj) | 4.67 | 1 | Medium - continual trajectory prediction |
| SKI-CL (URCfZ2NgaR) | 5.33 | 1 | High - continual MTS forecasting, rejected |
| Weather nowcasting (Cjz9Xhm7sI) | 8.00 | 1 | Low - spatio-temporal but not continual |
| Online GNN eval (KbetDM33YG) | 8.00 | 1 | Low - GNN distribution shifts |
| LinOSS (GRMfXcAAFh) | 8.00 | 1 | Low - time series SSM |
| FITS (bWcnvZ3qMb) | 8.00 | 1 | Low - time series frequency domain |
| DyGPrompt (kVlfYvIqaK) | 6.00 | 2 | Medium - dynamic graph prompt learning |
| ST Knowledge Distillation (akKNGGWegr) | 5.25 | 2 | Medium - spatio-temporal distillation |
| Fast/Slow Streams (I0n3EyogMi) | 7.00 | 2 | Medium - online time series forecasting |
| In-context Time Series (dCcY2pyNIO) | 6.25 | 2 | Medium - time series forecasting |

**Round 1 bracket**: 5.0–7.0 (clearly above rejected continual forecasting papers at 4.0-5.3, comparable to EAC at 6.75)

**Round 2 narrowing**: The paper is stronger than DyGPrompt (6.00) given its much stronger empirical results, but below Fast/Slow Streams (7.00) which had a more novel methodological insight. The overclaiming about distributional drift and missing ablations hold it slightly below EAC (6.75), despite claiming superior empirical performance.

**Final score: 6.0** — a solid empirical contribution with strong traffic results and a coherent framework, held back by overclaiming and missing ablations.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>