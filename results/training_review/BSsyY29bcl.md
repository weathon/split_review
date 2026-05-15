Now I have all the information I need. Let me compose the final review.

---

## Summary

TwinsFormer introduces a dual-stream Transformer architecture for time series forecasting that explicitly models interactions between trend and seasonal decomposed components. Unlike prior methods that learn trend and seasonal representations via independent branches, TwinsFormer feeds seasonal components through attention/FFN modules with a subtraction mechanism (residual-style) and uses the seasonal branch's outputs as supervisory signals for a trend branch processed through lightweight interactive modules (convolutions, gates). The method achieves competitive results across 13 real-world benchmarks, ranking first in many settings against 10 baselines including iTransformer, PatchTST, and TimeMixer.

## Strengths

- **Consistent state-of-the-art performance across diverse benchmarks**: On 13 real-world datasets spanning long-term and short-term forecasting, TwinsFormer achieves the highest average rankings across most settings, outperforming 10 strong baselines. Concrete improvements include a 6.2% MSE reduction on ECL and 5.1% on Traffic over iTransformer (Tables 1, 2). The experimental coverage is extensive — 13 benchmarks is a thorough evaluation by community standards.

- **Systematic ablation studies verify each design component**: Table 3 independently ablates the decomposition design, the subtraction mechanism, the interactive module's inputs (E_T', A_S, F_S), and the gate mechanism across four datasets. Each component's removal or replacement causes a measurable performance drop, confirming that the proposed elements — not just the base Transformer — contribute to the results.

- **The core motivation is well-grounded**: The paper identifies a genuine limitation of existing decomposition-based forecasting — that the moving-average decomposition yields imperfectly disentangled trend/seasonal components, and independently processing them risks overlooking residual couplings. The interactive dual-stream design is a reasonable and creative response to this problem.

- **Plug-and-play compatibility is demonstrated (conceptually)**: Table 4 shows the interactive strategy applied to five different Transformer variants (Transformer, Informer, Autoformer, Flowformer, Periodformer) with reported improvements across the board, suggesting the framework's generality beyond the specific iTransformer backbone used in main experiments.

## Weaknesses

### Fatal
None.

### Major

- **The compatibility experiment (Table 4) is critically under-specified, undermining a core claim**. The paper describes this as demonstrating that the interactive strategy is a "plug-and-play module" for existing Transformer variants, but no dataset is named for this experiment, no experimental configuration is given, and there is no indication of which prediction lengths were evaluated. The reported improvements (28–47% relative MSE reduction) are extraordinarily large — a 46.9% improvement on Autoformer would be a striking result, but without specifying the evaluation setup, the reader cannot assess whether the baselines were fairly tuned. This does not invalidate the main results (Tables 1, 2), but since the plug-and-play claim appears in the abstract and the method section, the evidence presented for it is insufficient.

### Minor

- **Per-horizon results and variance estimates are absent from all main tables**. Results in Tables 1 and 2 are reported as averages across prediction horizons (S ∈ {96,192,336,720} for long-term, S ∈ {12,24,48,96} for short-term) with a single number per entry and no standard deviations or confidence intervals. This obscures whether TwinsFormer's advantage is consistent across horizons or concentrated at specific settings, and makes it impossible to assess the statistical significance of small-margin improvements (e.g., 0.138 vs. 0.147 MSE on ECL). While aggregated reporting and single-run evaluation are common in the field, the paper's strong claim of "state-of-the-art" would be more convincing with per-horizon breakdowns and variance information.

- **The "rationality analysis" (§3.2, Equations 8–10) is labeled in a misleading way**. The derivation shows that after simplifying away all non-linear transformations (attention, FFN, convolutions, sigmoids, gate mechanisms), the sum of the two streams equals the original decomposition sum (X_s + X_t). This is an algebraically trivial observation about the subtraction-and-compensation structure. The paper claims this "perfectly fits the requirements of the decomposition design without bringing in redundant signals," but this overstates what the analysis demonstrates. The method's practical effectiveness must stand entirely on the experimental results, which it does — the analysis adds no real theoretical insight. The authors should either remove this section or reframe it as a simple consistency check rather than a "rationality analysis."

- **The "18 out of 22 average settings" claim is ambiguous**. The paper claims TwinsFormer "ranks in the top 1 among 11 models on 18 out of the 22 average settings," but the structure of Tables 1 and 2 (9 long-term datasets + 4 short-term datasets, each with MSE and MAE, plus "Avg" rows) does not straightforwardly yield 22 settings. The authors should clarify what precisely constitutes an "average setting."

- **Lookback length sensitivity (Figure 4) is shown on only three datasets**. While the trend (improving performance with longer lookback) is noteworthy, showing this on the full set of datasets would strengthen the claim. Additionally, the relevant comparison — how other strong baselines behave at different lookback lengths under the same conditions — is not provided, making it unclear whether this is a unique property of TwinsFormer or a general improvement from better attention mechanisms.

- **Several design choices are presented without justification**. The interactive module uses three specific convolution kernel sizes (1×1, 3×3, 5×5) and the gate mechanism uses four separate 1×1 convolutions, but no rationale or ablation is provided for these architectural choices. While not every design parameter needs exhaustive justification, readers may wonder whether these choices were tuned or arbitrary.

### Trivial
None of substance beyond minor presentation issues attributable to the parser.

## Nice-to-Haves

- Report per-horizon breakdowns and standard deviations for main results (Tables 1, 2).
- For the lookback length analysis, include how other leading baselines (e.g., iTransformer, TimeMixer) behave on the same datasets under identical conditions.
- Vary the moving-average kernel size used for decomposition and show sensitivity.
- Add an ablation that compares the full interactive design against a simple additive ensemble of two independent streams (no interaction at all) to directly measure the benefit contributed by the interaction.

## Removed Points

The following points raised by reviewers are removed with justification:

- **"The claim of being 'perhaps the first to our best knowledge' is weak"** — This is a reasonable and common framing. The related work section explicitly discusses prior decomposition-based methods and states the novel aspect (interaction between components). The claim is sufficiently scoped.

- **"Missing related work discussion (e.g., TimeMixer, MICN)"** — The paper cites TimeMixer in the related work section (line 34: "TimeMixer (Wang et al., 2024) mixes multiscale decomposable components for time series forecasting"). The harsh critic's claim that this is missing is factually wrong.

- **"Missing hyperparameters (hidden dimensions, number of layers, dropout rates, learning rates)"** — Details that typically appear in the appendix, which is stripped by the parser. The hard rules require removing criticisms about missing appendix content.

- **"Efficiency analysis incorrectly states that N for most Transformer-based models is affected by lookback length"** — This statement is factually correct for most Transformer time series models (e.g., Autoformer, FEDformer, PatchTST, Reformer), which apply attention across the time dimension. The paper is not referring to iTransformer (which also uses variate tokens), and the sentence is a general comparison, not a claim about iTransformer specifically.

- **"The paper incorrectly states complexity O(N^2) when iTransformer handles sequence length via linear projection"** — The paper's O(N²) claim refers to the number of variates N, not sequence length. In iTransformer (the adopted backbone), attention is across N variates, so the complexity is indeed O(N²) in terms of variates. The critic conflates two different notions of N.

- **"Strawman" criticisms about missing baseline comparison fairness** — The critic suggests "no comparable results from the original papers or a fair re-implementation are provided" for Table 4, but the "Before" column presumably is a re-implementation. The issue is lack of dataset specification, not missing original-paper comparisons.

- **Strength Finder's claim about the rationality analysis being a "theoretical rationale"** — This conflicts with the verified weakness that the analysis is a tautology. Per the rules, when a strength and verified weakness disagree, the weakness wins. Removed.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a meaningful tension: the paper's core idea (interactive dual-stream decomposition) is well-motivated and empirically effective, but the presentation overreaches in two ways — claiming theoretical support where there is only a trivial algebraic consistency, and claiming plug-and-play generality without adequate experimental specification. The discrepancy between the strong main results and the under-supported secondary claims is the central takeaway.

## Suggestions

1. **Specify the compatibility experiment fully**: Name the dataset, prediction lengths, model configurations, and training setup used for Table 4. If the experiment was on a single dataset (e.g., Weather or ECL), state this explicitly and discuss potential dataset dependence. If possible, report results on multiple datasets to strengthen the plug-and-play claim.

2. **Rephrase or remove the "rationality analysis"**: Either rename it to something like "Consistency check" and clarify that it only verifies sum preservation under linear simplification, or replace it with a more meaningful analysis (e.g., gradient flow, representation correlation between streams).

3. **Clarify the "18 out of 22" claim**: Provide a precise enumeration of what constitutes an "average setting" so the reader can verify the count against the tables.

4. **Include per-horizon results** in supplementary material at minimum, ideally in the main text or appendix, and report standard deviations over multiple runs.

## Score and Decision

This paper introduces a well-motivated architecture for time series forecasting with clearly presented experiments on extensive benchmarks and thorough ablation studies. The core contribution — a dual-stream interactive design that couples trend and seasonal learning — is novel and empirically validated. The main weaknesses are (a) an under-specified compatibility experiment that does not adequately support the plug-and-play claim, and (b) several presentation issues (oversold rationality analysis, ambiguous claims, missing variance). None of these are fatal to the paper's core contribution, and all are addressable in revision. The paper represents a solid contribution to the field.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>