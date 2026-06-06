Now I have enough information to write a thorough review.

---

## Summary
This paper proposes "shape morphing," a statistical preprocessing technique for exogenous variables in time series forecasting. The core idea is to compute a rolling-window statistical measure (correlation, covariance, entropy, mutual information, or FARM) between each exogenous channel and the target series, then use this "morph ratio" to rescale the amplitude of the exogenous series before feeding it into a transformer model. An extensive ablation study across 7 datasets, 5 transformer architectures, 5 saliency functions, 5 window sizes, and 4 forecast horizons is presented to evaluate this preprocessing strategy.

---

## Strengths

- **Broad ablation coverage**: The study spans 5 transformer models × 7 datasets × 5 saliency methods × 5 window sizes × 4 forecast horizons. The scale of the empirical sweep is commendable and provides a panoramic view of when morphing helps and when it does not.

- **Interpretability and simplicity**: The morphing approach is conceptually transparent. Using information-theoretic quantities (mutual information, correlation, covariance, entropy) as attention weights is intuitive and requires no additional learned parameters. This plug-and-play property is practically attractive.

- **Notable improvements on some models**: For Crossformer the approach yields an average +31.9% improvement in MSE across datasets, and for ETTh1/ETTh2 at most horizons the gains are consistent and substantial. The motivation that transformer permutation-invariance hampers channel-dependency learning is well-grounded in prior literature.

---

## Weaknesses

### Fatal
None that fully invalidate the core idea, but the evaluation methodology described under Major weaknesses comes close.

### Major

1. **Oracle/best-case reporting inflates all results.** Table 1 and the headline improvement numbers are obtained by selecting, for each (dataset, model, horizon) triple, the best-performing combination from a grid of 5 saliency methods × 5 window sizes. This is an oracle configuration that would not be available in practice. There is no separate validation set used for hyperparameter selection; the "best" is picked against the test set implicitly. The conclusion itself acknowledges the problem: *"Morphing is not universally better when used blindly (typical median effect ≈ 0%)."* This directly undermines the abstract's positive framing—improvements in 73% of cases are inflated by optimistic configuration selection, not by the method being reliably useful.

2. **No comparison to a fixed default configuration.** A critical missing experiment is a single, reasonably-chosen default (e.g., rolling correlation with window 751, without per-dataset tuning), compared across all settings. Without this, it is impossible to know whether the method is useful when deployed without oracle knowledge of which saliency function and window size will work best.

3. **Missing results for ECL and TrafficL impair conclusions.** ECL has 320 exogenous variables and TrafficL has 861—precisely the high-dimensional settings where exogenous handling matters most. Yet most forecast horizons for these datasets are absent due to "computational overflow." Two of seven datasets are thus largely unavailable, and the summary statistic of "73% improvement rate" is computed on a biased subset.

4. **No comparison to linear/CI baselines or state-of-the-art exogenous methods.** The paper motivates morphing by the observation that CI linear models often outperform CD transformers. However, Table 1 never shows whether morphing finally allows any transformer to match or beat a DLinear/NLinear baseline. A 31.9% improvement for Crossformer is impressive, but if Crossformer starts from a poor baseline (its ETTh2 MSE of 1.82 at horizon 720 vs. PatchTST's 0.245), the absolute improvement may be modest and the model may still lag far behind simpler baselines. Comparisons against CATS (mentioned in the appendix, unavailable here) and other exogenous-aware methods should be in the main paper.

5. **Significant degradation in important settings is underemphasized.** The Weather dataset shows −116.7% and −101.4% degradation for Autoformer at h=192 and h=336 respectively, and Crossformer shows −46.7% at h=720. These are large performance collapses that are glossed over in the analysis. Understanding when morphing hurts is as important as when it helps.

### Minor

1. The toy example demonstrates a ~6% MSE reduction with Ridge regression on synthetically constructed data where the relevance intervals are known by design. Its connection to the real experimental settings (transformer models, hundreds of exogenous variables, long horizons) is loose and does not constitute evidence for the approach beyond illustration.

2. The paper describes the forecasting procedure as iterative one-step-ahead with target history extended by previous forecasts, but exogenous data use "original information." The morphing ratio r_t requires simultaneous access to both x_t and y_t up to the current time. In truly online settings, the morph ratio for the forecast period would require the future target values—this causal boundary is not carefully discussed.

3. For state-of-the-art models like PatchTST, improvements are almost universally below 2% (often 0.0–0.1%), which is within noise for most benchmarks, yet these are grouped together with Crossformer's large improvements in the headline "73% of cases" statistic.

### Trivial

None that warrant mention beyond parser artifacts.

---

## Nice-to-Haves
- Report results with a validation-set-selected configuration (rather than oracle test-set best) to give a more honest picture of practical utility.
- Include a proper comparison against DLinear/NLinear baselines to contextualize whether morphing closes the CI-CD performance gap.
- Report median and variance of performance across morphing configurations in addition to the best, to show how sensitive the method is to configuration choices.

---

## Novel Insights
The observation that statistical rolling-window relevance measures approximate transformer attention weights (Figure 1, comparing TFT and FARM) is genuinely interesting and motivates decoupling saliency detection from model training. The hypothesis that preprocessing exogenous series with statistical attention allows transformer models to focus solely on target-series dynamics—rather than jointly learning cross-channel dependencies—is a reasonable and underexplored direction. However, the experimental evidence as presented does not yet demonstrate that this insight translates into reliable, configuration-agnostic improvements.

---

## Suggestions
- Add a table showing performance with a fixed default saliency configuration (e.g., rolling correlation, window=751) vs. no morphing to demonstrate robustness beyond oracle selection.
- Explicitly include DLinear/PatchTST-CI as reference baselines in all main tables to show whether morphing closes the gap.
- Investigate and discuss the large degradations on Weather at longer horizons; a principled explanation of failure modes would strengthen the paper significantly.
- Address the causal validity of morphing in truly online settings where future target values are unavailable.

---

## Score and Decision

The morphing idea is simple and intuitive, and the ablation is comprehensive in scope. However, the primary quantitative claims rest on oracle best-case configuration selection rather than a principled evaluation methodology. The self-acknowledged median effect of ≈ 0% and the absence of validation-set-based hyperparameter selection mean the advertised improvements are not reliably reproducible without knowing the answer in advance. Missing results for the two most complex datasets, the lack of comparison to linear baselines, and the unexplained large degradations on Weather further weaken the contribution. As currently presented, the paper is better suited for a workshop or as preliminary work requiring a more rigorous evaluation design.

MY FINAL SCORE: <score>3</score>
MY FINAL DECISION: <decision>Reject</decision>