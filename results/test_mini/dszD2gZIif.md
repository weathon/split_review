## Summary

This paper proposes Swin4TS, which adapts the Swin Transformer architecture—specifically its window-based attention and hierarchical representation—to long-term time series forecasting. The model achieves O(ML) linear complexity in both time length (L) and number of channels (M) and supports both channel-independent (CI) and channel-dependent (CD) strategies. Empirical results on 8 benchmark datasets show competitive MSE/MAE numbers against 8 baselines.

## Strengths

- **Linear computational complexity in both L and M**: Section 5 formally derives O(ML) complexity for both Swin4TS variants, and Table 4 demonstrates that Swin4TS is the only Transformer-based model among those compared to achieve this. On the Electricity dataset, Swin4TS/CI achieves 0.12G FLOPs and 0.006s inference time per batch—concrete evidence of practical efficiency.

- **Flexible dual-strategy design (CI/CD) that adapts to dataset characteristics**: Table 1 shows Swin4TS/CD performs best on ILI and 3/4 ETT datasets while Swin4TS/CI performs best on Traffic and Electricity. The paper correctly identifies that CD can overfit complex multivariate correlations on datasets with many channels (Traffic, Electricity), while CI generalizes better there. This provides practical guidance for practitioners.

- **Ablation study validates the contribution of shift-window attention and hierarchical design**: Table 3 on ETTm1/ETTm2 shows that removing both increases MSE by 3.2% and 2.7% respectively, and removing either individually also degrades performance, directly supporting the claim that these Swin Transformer components are beneficial for time series.

- **Attention map visualization provides interpretability**: Figures 5 and 6 qualitatively demonstrate that Swin4TS/CD captures cross-channel correlations (patches with similar trends are highlighted) and that local attention captures periodicity while global attention captures anomalous trends, supporting the claim of multi-scale feature extraction.

## Weaknesses

### Fatal
None.

### Major

- **Uncontrolled look-back window lengths in baseline comparisons undermine the SOTA claim**. The paper (Section 4.1) uses L=512 for Swin4TS (L=108 for ILI), while FEDformer, Autoformer, TimesNet, MICN, N-HiTS, and Crossformer are evaluated at L=96, with the justification that "different models require suited L to achieve their best performance." This conflates architectural quality with input length advantage. Since longer look-back windows are known to benefit many forecasting models, the reported margins (e.g., 15.8% on ILI) may partially reflect this asymmetry rather than architectural superiority. The paper does not provide controlled experiments at equal input lengths, nor does it show Swin4TS at L=96 outperforming baselines at L=96. *Note: PatchTST and DLinear comparisons are fair since they also use L=336/512.* This weakness is the single most important factor in the evaluation—it casts doubt on the headline SOTA claims but does not invalidate the model's efficiency or architectural contributions.

### Minor

- **No positional encoding mechanism is discussed or justified**. The paper describes window-based attention applied to patches but never mentions how temporal order is encoded within patches or windows. In the original Swin Transformer, relative positional biases are critical. For time series, where temporal order is fundamental, this omission is a nontrivial design gap. The model may implicitly capture order through fixed window boundaries and sequential patch formation, but this should be clarified.

- **Main results (Tables 1, 2) report MSE/MAE without measures of variance.** No standard deviations or confidence intervals are provided for the headline numbers. Given that many reported differences between models are small (e.g., on Weather: Swin4TS/CI 0.253 vs. PatchTST 0.256), it is impossible to assess whether these improvements are statistically significant or within run-to-run noise.

- **Ablation study is limited to 2 datasets (ETTm1, ETTm2) and only the CD variant.** This narrow scope makes it difficult to assess whether the shift-window attention and hierarchical design are universally beneficial or specific to these datasets. An ablation on at least ILI (largest reported gain) and Traffic (largest channel count) would strengthen the generality claims.

### Trivial
None.

## Nice-to-Haves
- Controlled experiments where all baselines run at L=512 (or where Swin4TS runs at L=96 to match shorter-length baselines) to substantiate the SOTA claim.
- Including standard deviations across multiple random seeds in Tables 1 and 2.
- Extending the ablation to datasets beyond ETTm1/ETTm2.
- Clarifying whether baseline results are reproduced by the authors or taken from original papers, and discussing any differences in training setups.

## Removed Points
The following points from the Harsh Critic were removed because they contradict the instructions:

- **Critique that Section 4.3 claims lack quantitative evidence in the main text, with references to the appendix being "stripped."** The rule states: "REMOVE weaknesses about missing appendix, missing proofs in appendix, or absent references. The parser strips those sections from all papers; they exist in the original submission." The appendix content is present in the original submission and cannot be evaluated from the parser output.

- **Critique that the "randomness test" is "relegated to a one-sentence claim."** Same as above—this refers to appendix content stripped by the parser.

- **Strength about "Robustness and additional experiments" from the Strength Finder** — this refers exclusively to appendix content that cannot be verified.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Control for input length**: Re-run FEDformer, Autoformer, TimesNet, MICN, N-HiTS, and Crossformer at L=512 (or the longest length each model can handle given complexity constraints), or alternatively run Swin4TS at L=96 and show it remains competitive. Without this, the SOTA claim remains unsubstantiated.

2. **Add positional encoding**: Explicitly state whether relative position bias (as in the original Swin Transformer) or any other positional encoding is used. If none is used, justify why temporal order within patches can be disregarded or implicitly captured.

3. **Report variance**: Include standard deviations over at least 3 random seeds for all main tables, and consider statistical significance tests for close comparisons.

4. **Broaden the ablation**: Run the ablation study (shift-window attention, hierarchical representation) on ILI (largest reported gain) and Traffic (largest channel count, CI-dominated) to verify general importance across diverse dataset characteristics.

---

## Score and Decision

### Calibration Anchors

| Path | Avg Score | Comparison to this paper |
|------|-----------|--------------------------|
| iTransformer (JePfAI8fah.md) | 7.50 | Much stronger: cleaner idea (inverted transformer), fair comparison at same input lengths. This paper is significantly weaker. |
| Time-LLM (Unb5CVPtae.md) | 7.00 | Stronger: novel reprogramming approach, more thorough evaluation. This paper has comparable scope but less rigorous evaluation. |
| A Simple Baseline (oANkBaVci5.md) | 6.75 | Stronger: rigorous evaluation with novel attention mechanism. This paper has better efficiency analysis but weaker empirical validation. |
| TwinsFormer (BSsyY29bcl.md) | 5.80 | Comparable: both adapt Transformer designs for TS, both have evaluation concerns. TwinsFormer has slightly more thorough experiments. |
| VisiTER (DcG4YnbOT3.md) | 4.33 | Comparable: both use CV→TS transfer. VisiTER weaker on clarity but has similar evaluation scope. |
| VIPER (0Q1mBvUgmt.md) | 3.00 | Weaker: minimal novelty, flawed experiments. This paper has a clearer contribution and better efficiency analysis. |
| LST-Bench (2wwPG1wpsu.md) | 2.50 | Weaker: benchmark paper with very low novelty. This paper has genuine architectural contribution. |

The paper's core idea—adapting Swin Transformer's window attention and hierarchy for time series—is reasonable and yields a model with genuine practical advantages (linear complexity, flexible CI/CD). However, the main empirical claim (SOTA on 8 benchmarks) is undermined by the uncontrolled input length comparison. This is not a fatal flaw (the efficiency and architectural contributions remain valid), but it prevents confident acceptance. The paper is below the quality bar of accepted papers at this venue.

**MY FINAL SCORE: <score>4.5</score>**
**MY FINAL DECISION: <decision>Reject</decision>**