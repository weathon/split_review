Now I have all the information I need to synthesize the review. Let me write the consolidated final review.

## Summary

This paper proposes SONNET, a probabilistic day-ahead net load forecasting method with three main contributions: (1) an unsupervised behind-the-meter (BTM) solar disaggregation algorithm that recovers solar generation and load traces from net load observations alone, achieving near-supervised accuracy; (2) a Transformer architecture that jointly processes historical data and future weather forecasts via self-attention and cross-attention mechanisms; and (3) a physics-model-based data augmentation method to improve robustness to weather forecast errors. The method is evaluated on the U.S. Department of Energy's net load forecasting competition dataset across four diverse locations (TX, OR, GA, HI) with varying solar penetration levels and compared against the top competition teams as well as standard baselines.

## Strengths

- **Unsupervised solar disaggregation achieves near-supervised accuracy.** Table 1 shows that the proposed unsupervised algorithm attains RMSE, MASE, and CV values very close to a supervised physical model across four different solar penetration levels (0.18–1.57). This directly supports the claim that BTM solar traces can be recovered without ground-truth solar data, enabling disaggregation-based forecasting in realistic utility settings.

- **SONNET outperforms all DOE competition teams, including under extreme forecast errors.** Table 2 reports CRPSS scores where SONNET, even under "Extreme" weather-forecast errors (2× empirical error), exceeds the best competition entry at every location. This demonstrates a clear advance over the verifiable state-of-the-art on a challenging real-world benchmark.

- **Data augmentation materially improves robustness to weather forecast errors.** The ablation study in Table 3 shows that removing data augmentation leads to a clear CRPSS drop, especially for the high-solar-penetration site HI (0.291 vs. 0.345 with augmentation). This confirms the practical value of the physics-based augmentation.

- **Systematic ablation studies isolate each component's contribution.** Tables 3–5 separately remove solar disaggregation, data augmentation, exogenous variables, and the Transformer architecture (comparing against LSTM, MLP, and XGBoostLSS). Each ablation quantifies the marginal gain from each design choice, giving clear empirical support.

- **Evaluation across diverse climates and solar penetration levels.** The DOE dataset covers four U.S. locations with very different weather patterns and normalized solar capacities from 0.18 to 1.57, providing strong evidence of generalizability.

## Weaknesses

### Fatal
None.

### Major

- **The comparison to competition top teams uses simulated weather forecast errors rather than the actual forecasts available during the competition period, creating a confound.** The paper states it aims to "ensure a fair comparison with the competition results" (Section 5.3) but does so by adding independent Gaussian noise to ground-truth weather data, calibrated to empirical error standard deviations. The paper does not specify what weather forecasts the competition teams used, nor does it validate that the simulated error distribution (independent Gaussian draws) matches the spatiotemporal structure of actual forecast errors during the competition period (June 18–July 15, 2023). Real forecast errors can exhibit autocorrelation, heteroscedasticity, and non-Gaussian tails that independent draws do not capture. While the multi-level testing under "Challenging" (1.5×) and "Extreme" (2×) error settings provides a useful robustness check — showing SONNET wins even with unrealistically large errors — the paper overstates the comparison by claiming it "ensures a fair comparison." The central claim of "significantly outperforming the state-of-the-art" would be substantially strengthened by either (a) evaluating on actual weather forecasts from the competition period, or (b) transparently framing the results as a controlled simulation study rather than a direct competitive comparison.

### Minor

- **No uncertainty quantification reported for the main CRPSS results.** Table 2 reports CRPSS averages over 20 experiments × 10 replicates = 200 independent runs, yet provides no standard deviations, confidence intervals, or distributions. Without these, the reader cannot assess whether the observed improvements over the best competition teams (typically 0.02–0.04 CRPSS) are statistically meaningful. Given that the paper already performs multiple runs, computing and reporting these intervals is straightforward and would substantially strengthen the empirical case.

- **The solar disaggregation component is validated only on a separate dataset (Austin, TX) rather than on the competition sites.** The paper acknowledges this is "impossible to perform using the DOE competition dataset due to the absence of BTM solar generation data" (Section 5.1), which is reasonable. However, this means the disaggregation quality is demonstrated only for one climate region (Texas summer), and its generalization to the diverse climates of the four competition sites (including HI's tropical conditions) is assumed rather than tested. A discussion of how well the approximation might hold across different climates and building types would strengthen the paper.

- **No direct comparison against existing disaggregation-based net load forecasting methods.** The paper discusses Wang et al. (2018) and Jia et al. (2023) in Related Work but does not include them as baselines. While the competition top teams represent strong and verifiable state-of-the-art benchmarks, a head-to-head comparison with these prior disaggregation-based approaches under the same evaluation protocol would directly validate the paper's claim that its particular combination is superior. The omission is noted but is not severe since these prior methods lack the competition dataset results for comparison.

### Trivial
None.

## Nice-to-Haves

- Validate the data augmentation strategy against a noise model structurally different from the training-time augmentation (e.g., errors with temporal autocorrelation) or against real weather forecast residuals to demonstrate genuine generalization.
- Provide a brief discussion of computational cost (training time, inference latency, model size) for practical deployment considerations.
- Add a sensitivity analysis that propagates disaggregation quality uncertainty into the final forecasting performance (e.g., how much does CRPSS degrade if the estimated tilt/capacity is off by 10%?).
- Report the source of weather forecast data used to estimate empirical error standard deviations σ_f.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Architecture description lacks key details (layers, heads, hidden dimensions)** — Removed per parsing rules: these would be in the appendix, which is stripped by the parser. The main text provides the architecture's structure and the paper references standard Transformer components.
- **"Data augmentation evaluation may conflate training and testing conditions"** — Removed because this is structurally identical to the weather forecast comparison concern above (it is the same underlying issue). Training augmentation matching test noise is proper methodology; the deeper question about real vs. simulated forecasts is already addressed in the Major weakness.
- **"Transformer without disaggregation already matches top teams"** — Removed because the paper explicitly presents this as a finding (Section 5.4: "even without employing the solar disaggregation step... our transformer-based model significantly outperforms state-of-the-art methods"), and then shows that adding disaggregation further improves performance. This is not a weakness; it demonstrates multiple layers of contribution.
- **"No uncertainty quantification" framing as severe** — Downgraded from Major (as framed by the Harsh Critic) to Minor because the paper does run 200 independent trials per setting, providing meaningful averaging; the gap is systematic across all four locations and three error levels. The absence of reported variance is a presentation gap, not a structural flaw.
- **Formatting/style nitpicks and missing appendix references** — Removed per parsing rules.

## Novel Insights

The paper's most interesting finding is that unsupervised disaggregation — using only net load data and rough capacity estimates — can recover BTM solar traces with accuracy close to supervised learning, and that feeding these disaggregated traces into the forecasting model yields measurable improvements over using raw net load alone. The ablation study in Table 3 reveals that even without disaggregation, the Transformer+augmentation combination already exceeds competition best results, suggesting that the architecture and augmentation are the primary drivers of improvement. However, disaggregation adds consistent value across locations, particularly where solar penetration is moderate (GA: 0.63 capacity ratio), confirming that the decomposition helps most where both load and solar are significant fractions of net load.

The cross-attention mechanism between historical patches and future weather forecasts is a conceptually clean design: it allows the model to retrieve analogous historical patterns given forecasted conditions, which is well-suited to the net load forecasting task where weather is the primary source of uncertainty. The paper's systematic ablation of each component (disaggregation, augmentation, architecture, exogenous variables, context length) provides unusually complete evidence for a forecasting paper about where performance gains originate.

## Suggestions

1. **Address the weather forecast comparison directly.** Either (a) obtain and evaluate on actual weather forecasts from the competition period (tracking down NAM/GFS/HRRR archives for those dates would make the comparison rigorous), or (b) if this is infeasible, clearly reframe the experimental setup as "controlled simulation study with multi-level error scenarios" rather than claiming a "fair comparison." This is the single change that would most strengthen the paper.

2. **Report confidence intervals for all CRPSS values.** With 200 runs already collected, this is a trivial addition (bootstrap or empirical standard deviation) that would substantially improve statistical rigor.

3. **Frame the competition comparison more carefully.** The current language ("significantly outperforms the state-of-the-art" and "ensures a fair comparison") overstates what the simulation-based evaluation can support. A more measured claim — e.g., "SONNET achieves higher CRPSS than the best competition entries under simulated weather forecast errors at multiple noise levels" — would be more defensible.

4. **Add a brief discussion of how disaggregation quality from Austin, TX might generalize** to the different climates and building stocks of the four competition locations.

## Score and Decision

The paper presents a well-motivated combination of techniques with strong methodological contributions and extensive experiments on a challenging real-world benchmark. The three core components (unsupervised disaggregation, cross-attention Transformer, physics-based augmentation) are each validated individually. The main weakness is that the headline comparison to competition teams uses simulated rather than actual weather forecasts, creating a confound in the central claim. This is a real limitation but not fatal — the multi-condition testing and independent baseline comparisons (Tables 3–5) provide converging evidence of the method's effectiveness. With revision to either validate on real forecasts or recalibrate the claims, this paper makes a solid contribution.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>