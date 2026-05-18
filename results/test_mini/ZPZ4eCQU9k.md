## Summary

The paper proposes xLSTM-Mixer, a multivariate time series forecasting model that combines a channel-independent NLinear forecast with sLSTM-based refinement and multi-view mixing. The model processes variates as sequence elements (rather than time steps) through sLSTM stacks, uses learnable initial tokens inspired by soft prompting, and reconciles two views (original and reversed embeddings) via a linear projection. On standard long-term forecasting benchmarks, xLSTM-Mixer achieves the best MSE in 18/28 settings and best MAE in 22/28 settings, outperforming Transformer, MLP-mixer, and convolutional baselines.

## Strengths

- **Strong empirical performance across diverse benchmarks.** xLSTM-Mixer achieves top-1 results in 18/28 MSE and 22/28 MAE settings across multiple datasets (Weather, Electricity, ETT variants), consistently outperforming strong baselines including TimeMixer, PatchTST, iTransformer, and the prior xLSTMTime. The competitive gains on Weather (4.6% MAE over TimeMixer) and ETTm1 (2.4% MAE over TimeMixer) are non-trivial.

- **Comprehensive ablation study isolating each component's contribution.** Table 3 systematically ablates time mixing (NLinear), sLSTM blocks, the initial embedding token, and multi-view mixing across ten configurations and two datasets. The study cleanly demonstrates that all components contribute positively, with sLSTM blocks and time mixing identified as the most critical elements — removing either causes measurable drops (e.g., 3.4% MAE increase on ETTm1 at horizon 96 without time mixing).

- **Clean architectural narrative and good motivation for design choices.** The three-stage pipeline (linear forecast → sLSTM refinement → view reconciliation) is clearly described and each stage is justified. The learning of initial tokens from soft prompting in LLMs, the transposition to variate-axis processing, and the weight-sharing regularization are well motivated.

- **Empirical validation of robustness to longer lookback windows.** Figure 5 shows that xLSTM-Mixer monotonically improves with increasing lookback length, and that its advantage over transformer-based baselines widens at longer contexts — a practical benefit of the linear-complexity recurrent design.

## Weaknesses

### Fatal

None.

### Major

- **No error bars or uncertainty quantification on the main results (Table 1).** The main table reports only point estimates (MSE, MAE) averaged over four horizons, with no indication of variance across seeds or runs. Given that many baselines are highly competitive and margins are often small (2–4% MAE), the reader cannot assess whether the reported improvements are statistically reliable. The paper does compute standard deviations in the sensitivity analyses (Figures 4 and 5), so the infrastructure exists — the omission from the main table is a significant reporting gap. This is the single most important weakness because it undercuts the paper's central claim of "state-of-the-art performance."

- **The claim that variate-axis marching is superior is asserted but never tested in a controlled manner.** Contribution (i) states that "marching over the variates instead of the temporal axis yields better results if suitably combined with temporal mixing." However, no ablation keeps the sLSTM architecture fixed and varies only the marching direction (variate vs. time). Every comparison is to fundamentally different models (Transformers, MLP-mixers, CNNs). An experiment where the sLSTM processes the time axis (each token is the full variate vector at one time step) with identical architecture would directly test this claim. Without it, the paper's most distinctive design rationale is unsubstantiated.

- **The multi-view mixing ablation does not isolate the effect of reversal.** Configuration #6 in the ablation removes multi-view mixing entirely. But a proper ablation would compare against a variant that uses two forward passes with the *same* (non-reversed) embedding and shared weights. This would distinguish whether the benefit comes from the reversal itself or simply from processing the input twice with weight sharing. The paper's explanation ("multi-task learning settings are known to benefit training") is too generic to justify the specific design choice.

### Minor

- **No computational cost comparison (runtime or memory).** The paper claims linear scaling in variates, but provides no wall-clock times, parameter counts for the full architecture, or FLOPs comparisons against baselines. Given that sLSTM has recurrent (and therefore sequential) overhead, practitioners need to know the efficiency trade-offs.

- **The learnable initial token shows only a small positive effect, and the paper acknowledges this honestly.** The ablation (#3 vs. #1) shows that removing the initial token yields results that are "still competitive." This is not a fatal weakness — many components have small individual effects — but it means the claimed novelty of the initial token is modest.

- **No error breakdown by variate on high-dimensional datasets.** On Traffic (862 variates), aggregate metrics may mask poor performance on a subset of channels. A per-variate error distribution would give a more honest picture of robustness.

- **The mLSTM is dismissed as "less suited for joint mixing" (Section 2.2) without empirical backing.** This claim about the relative suitability of sLSTM vs. mLSTM for joint mixing is asserted without evidence. While it is a secondary point, a brief justification or reference would help.

### Trivial

None.

## Nice-to-Haves

- **Direct comparison with xLSTMTime under identical settings (lookback, horizon, normalization).** The paper mentions that xLSTMTime is hard to reproduce but does not report a re-implementation. A controlled comparison would strengthen the claim of improvement over the prior xLSTM-based approach.
- **Analysis of why reversal helps.** Visualizing the two latent forecasts (y' and y'') before fusion — e.g., their correlation or per-variate errors — could shed light on the mechanism behind multi-view mixing.
- **Testing on datasets with very few or very many variates** to explore the acknowledged limitation of variate-axis processing.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The paper's strongest claim rests on thin evidence" (invalidates contribution).** The harsh critic claims the lack of error bars "invalidates the paper's primary empirical contribution." This is an overstatement. Many accepted time series papers report point estimates without error bars in main tables. The absence is a genuine weakness, not a fatal flaw.
- **"Phrasing like 'resurgence of recurrent models' implies a larger shift than warranted."** This is a style/subjective complaint about framing, not a scientific weakness.
- **"Several design choices are not justified: why reverse, why weight sharing, why up-projection?"** These are reasonable design choices grounded in prior work (MLP-Mixer for weight sharing, SSMs for up-projection). The paper provides adequate motivation.
- **Strength Finder claims about "SOTA" framing.** The strength about "achieving SOTA across diverse benchmarks" is kept substantively (it's supported by Table 1) but the strength about ablation completeness is retained — the claim that the ablation is "more granular than many time series papers" is debatable but the ablation is genuinely thorough.
- **"Comparison to transformer-based models in Fig. 6 is anecdotal."** The figure is an example forecast visualization, not a quantitative comparison. It serves a qualitative purpose.
- **"41/56 conflates MSE and MAE."** The paper reports 18/28 MSE + 22/28 MAE = 40/56, and the conclusion says 41/56. This 1/56 discrepancy is minor and the claim is clearly broken down by metric.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add standard deviations or confidence intervals to the main results table (Table 1).** Report the mean and std. dev. over at least 3 seeds per dataset-horizon combination. This is the single change that would most strengthen the paper.

2. **Add a controlled ablation of the marching direction.** Process the time axis (each token = variate vector at one time step) with the same sLSTM architecture. This would directly test the paper's central design thesis and significantly strengthen the contribution.

3. **Add a controlled ablation of the reversal in multi-view mixing.** Compare the full model against a version with two forward passes on the *same* (non-reversed) embedding with shared weights.

4. **Report wall-clock inference times and parameter counts** alongside the benchmark results so practitioners can evaluate the efficiency-accuracy trade-off.

## Score and Decision

**Calibration anchors (retrieved batch, all returned):**

| Anchor | Avg Score | Comparison to this paper |
|--------|-----------|--------------------------|
| FITS (bWcnvZ3qMb) | 8.00 | Superior: clearer novel insight (frequency-domain interpolation), extreme parameter efficiency, stronger experimental rigor (std dev reported). |
| Oscillatory SSM (GRMfXcAAFh) | 8.00 | Superior: strong theoretical proofs combined with solid empirical work. |
| DAM (4NhMhElWqP) | 7.00 | Stronger: broader scope (foundation model), zero-shot transfer, more ambitious. |
| Periodicity Decoupling (dp27P5HBBt) | 6.75 | Comparable but stronger: similar level of empirical results, slightly better ablation rigor. |
| Vision-LSTM / xLSTM (SiH7DwNKZZ) | 5.60 | Very similar: both adapt xLSTM to a new domain with some architectural innovations. Both have questions about incremental novelty and experimental gaps. ViL underperformed at larger scales; this paper's results are somewhat stronger but have similar rigor issues. |
| Revisiting LTSF (T97kxctihq) | 5.00 | Weaker than this paper: primarily an investigation/analysis paper with limited methodological contribution. |
| TF-score (RDLvnUJ5JZ) | 3.00 | Weaker: sloppy mathematical work, limited novelty. |
| LST-Bench (2wwPG1wpsu) | 2.50 | Weaker: benchmark paper with very limited novelty. |

The paper is most comparable to Vision-LSTM (5.60) — both are domain adaptations of xLSTM with solid results but incomplete experimental validation of specific design claims. This paper's empirical results are stronger than ViL's, but the lack of error bars in the main table and the untested marching-direction claim are important gaps. The method is sensible and the results are promising enough to warrant further development, but the evidence as presented is not yet fully convincing.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>