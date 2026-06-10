## Summary

This paper extends the exogenous-decision-process framework for periodic review inventory control to handle two real-world complexities that prior work (including Madeka et al., 2022) does not address: orders arriving in multiple shipments over time (which the paper formalizes as a Quantity-Over-Time or QOT model), and downstream post-processing of order quantities to satisfy vendor constraints (minimum order quantities, batch sizes). The authors build a deep generative model (Gen-QOT) for the arrival process, incorporate it into a differentiable replay simulator, and train RL policies via DirectBackprop. The core evidence is a real-world A/B test where QOT-DirectBP achieved statistically significant reward improvements of 2.7–3.5% over a production base-stock system, alongside rigorous off-policy validation confirming that Gen-QOT's calibration generalizes to the shifted action distribution induced by the learned policy.

## Strengths

- **First formalization of multi-shipment arrivals and order post-processing.** Section 1 (Figures 1–2) presents real data from a large e-retailer showing that orders routinely arrive in multiple shipments with stochastic yields, and that post-processing creates "end-to-end" yields exceeding 100%. The QOT model (Eq. 3–5) generalizes the standard single-shipment stochastic-lead-time model, and Section 5.2 (Table 4) quantifies the practical impact: ignoring these dynamics costs ~8% in discounted reward relative to the QOT-based simulator.

- **Real-world A/B test with statistically significant improvements.** Section 5.3 (Table 5) reports results from three multi-month A/B tests covering thousands of products. Trials 2 and 3 of QOT-DirectBP show statistically significant (95% confidence) reward increases of 3.5% and 2.7%, with corresponding sales increases of 3.4% and 1.8%, outperforming a sophisticated base-stock production system deployed in the real supply chain.

- **Rigorous off-policy validation of the dynamics model.** Section 5.3.3 (Tables 6–7, Figure 11) directly validates Assumption 1 by comparing Gen-QOT forecast errors between treatment and control arms of the A/B test. The differences in calibration and quantile loss are not statistically significant (e.g., 95% CIs for cumulative receives calibration include zero at all weeks 1–9). This is critical because it confirms that the learned dynamics model generalizes to the different action distribution induced by the RL policy, which is necessary for the theoretical reduction to supervised learning.

- **Multi-criteria evaluation of the generative model.** Section 4.1 defines five distinct evaluation criteria and provides quantitative results on both in-time and out-of-time holdouts. Tables 1–3 show competitive CRPS/quantile loss versus direct VLT forecasting, near-perfect arrival time calibration, and cumulative receives calibration coefficients close to 1.0 (1.06–1.15).

- **Demonstration of yield-adaptive ordering behavior.** Figure 8 shows that QOT-DirectBP's mean order quantity increases relative to VLT-DirectBP as the observed fill rate decreases, indicating the policy learns to compensate for stochastic yields at the product level — a behavior that the classical VLT model cannot capture.

## Weaknesses

### Major

- **Missing QOT-informed heuristic baseline isolates source of improvement incompletely.** The only non-RL baseline is a standard newsvendor (base-stock) policy. There is no baseline that uses the QOT model with a simple heuristic policy (e.g., adjusting base-stock levels using the QOT model's expected cumulative arrival distribution to account for stochastic yields and multi-shipment timing). Without this control, the reader cannot determine whether the headline improvement (QOT-DirectBP outperforming production) is driven by the QOT dynamics model itself or by the RL optimization on top of it. If a QOT-informed heuristic matched QOT-DirectBP's performance, the paper's contribution would be the QOT model rather than RL — which is still valuable but should be framed differently. The paper's central claim about RL adding value over classical systems would be substantially stronger with this baseline.

### Minor

- **A/B test results are modest and Trial 2 shows substantially increased inventory.** The reward improvements of 2.7–3.5% are practically meaningful for a large-scale supply chain but not dramatic. More importantly, Trial 2 shows an 11.1% increase in inventory level alongside the 3.5% reward gain. Since the reward function already accounts for holding costs, this is not necessarily a problem, but it raises the question of whether some of the improvement is driven by holding more inventory rather than by smarter ordering. The paper acknowledges that Trial 3 was specifically designed to hold similar inventory to the production system, which is good practice, but the Trial 2 result deserves more discussion. Additionally, Trial 1 (VLT-DirectBP) shows a 31.1% increase in order quantity with no significant reward improvement — a negative result that the paper presents neutrally but does not analyze.

- **Cumulative receives calibration shows systematic underprediction bias.** Table 2 reports regression coefficients of 1.05–1.15 for predicted vs. actual cumulative arrivals, meaning Gen-QOT systematically underpredicts cumulative arrivals by 5–15%. The paper acknowledges this ("not perfectly calibrated") but does not analyze how this bias affects the learned policy. A simulator that systematically underestimates how much inventory will arrive would encourage over-ordering, which could partly explain increased inventory levels in the A/B tests (particularly Trial 2). A sensitivity analysis using a calibrated version of Gen-QOT would strengthen the paper.

- **Backtest comparison (Table 4) is necessarily favorable to the proposed method and does not validate absolute quality.** The paper evaluates VLT-DirectBP and QOT-DirectBP *under QOT transition dynamics* and the authors note "it is unsurprising that the policy trained on the simulator used in evaluation performs best." This comparison quantifies the model-mismatch penalty (~8%) rather than providing an absolute measure of QOT-DirectBP's quality. The real-world A/B tests partially address this, but those tests do not include a VLT-DirectBP vs QOT-DirectBP head-to-head in the actual supply chain (Trial 1 was run at a different time on different products). The paper's framing should more clearly distinguish between what the backtest demonstrates (model mismatch cost) and what it does not (absolute superiority in reality).

- **The assumption that ρ_{t,j} > 0 for all j (line 120) is restrictive.** This implies every order necessarily has some arrival in every future period up to L, which is unrealistic for many products where some lead times are deterministic and shorter than L. While arbitrarily small positive values maintain the formal structure, the paper does not discuss the practical implications or whether this assumption could cause issues for products with sparse arrival patterns.

### Trivial

- The paper references \Cref{sec:genqot} and \Cref{sec:featurization} for full model description and feature details, but these appendix sections are not present in the submitted manuscript (presumably stripped during compilation). While this is standard practice for conference papers, the main text could benefit from a slightly more detailed architectural overview to improve self-containedness.
- The backtest period (2019-02 to 2020-02) includes the early weeks of the COVID-19 pandemic. A brief discussion of whether results are robust to excluding that period would be helpful.

## Nice-to-Haves

- **Per-product variability in A/B test results.** The paper reports aggregate treatment effects across "thousands of products." A forest plot or distribution of per-product treatment effects would help assess whether the aggregate improvement is broad-based or driven by a subset of products, especially given the modest overall effect sizes.
- **Statistical significance method for backtest confidence intervals.** Table 4 reports confidence intervals on the difference from baseline, but the paper does not state whether these are computed via bootstrapping over products, time periods, or some other method.
- **COVID period robustness check.** The backtest period includes early 2020 pandemic weeks which caused massive supply chain disruptions. Checking robustness to excluding that period would strengthen the results.

## Removed Points

These points were raised by reviewers but are either factually incorrect, reflect parser artifacts, or fail the filtering criteria:

- *"Gen-QOT model is effectively a black box in the main paper"* — REMOVED because the paper references \Cref{sec:genqot} for full architectural details, which is an appendix section. The parser strips appendix content from all papers; the details exist in the original submission. The main text provides a reasonable high-level description (autoregressive, RNN decoder, log-likelihood minimization). This is standard practice for ICLR submissions.
- *"Zero-order handling in the simulator is problematic (division by zero)"* — REMOVED because this is a trivial implementation detail. When a_t = 0, the sampled arrivals would be zero, and the rescaling step would not be applied in practice. The paper does not need to explicitly address this edge case.
- *"The backtest comparison is not informative"* — WEAKENED to minor (above). The paper acknowledges the limitation and the comparison still quantifies the model mismatch cost, which is informative.
- *"The Gen-QOT model specification should be in main text"* — REMOVED per appendix rule. Full architectural details in the appendix is standard practice.
- *"The learnability result is entirely borrowed"* — The paper explicitly states "this follows immediately" from Theorem 2 of Madeka et al. This is honest framing, not a weakness. The paper is primarily an empirical contribution.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add a QOT-informed heuristic baseline.** Construct a base-stock or constant-order policy that uses Gen-QOT's expected cumulative arrival distribution to set target stock levels (accounting for mean yield and arrival timing). If QOT-DirectBP still outperforms this baseline, the claim that *RL optimization* adds value over *having a better dynamics model* is substantially stronger. If it does not, reframe the contribution around the QOT model itself.

2. **Analyze the calibration bias and its consequences.** Estimate what the 5–15% cumulative receives underprediction implies for learned ordering behavior. Run a sensitivity analysis with a calibrated version of Gen-QOT to isolate the bias's impact on A/B test outcomes (particularly inventory levels in Trial 2).

3. **Report per-product treatment effect distributions** for the A/B tests to help readers assess whether the aggregate improvements reflect broad-based gains or a small subset of products.

4. **Include a brief architectural summary of Gen-QOT in the main text** (e.g., number of parameters, key feature groups, training budget) to improve self-containedness for readers who do not consult the appendix.

## Score and Decision

The paper addresses a genuine practical gap — inventory arrivals in real supply chains are far more complex than the standard single-shipment model — and provides a workable formulation (QOT) plus a generative modeling approach (Gen-QOT) validated through rare and valuable real-world A/B tests. The off-policy validation is a methodological strength. However, the absence of a QOT-informed heuristic baseline prevents the paper from isolating whether RL optimization or the better dynamics model drives the improvement, which is a significant gap in the evidence chain. The modest effect sizes and systematic calibration bias further temper the contributions. The paper is a solid empirical contribution with clear practical value, but the framing overstates what the evidence can definitively claim.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Reject</decision>