Now I have all the information needed. Let me construct the final review.

## Summary

This paper extends deep reinforcement learning for periodic review inventory control to handle general "quantity-over-time" (QOT) arrival dynamics — where orders arrive in multiple shipments with stochastic yields — and arbitrary order quantity post-processing (e.g., minimum order and batch size constraints). Building on the exogenous decision process framework of Madeka et al. (2022), the authors develop a generative model (Gen-QOT) for the arrival process and train a policy (QOT-DirectBP) via differentiable simulation. Real-world A/B tests across thousands of products at a large e-retailer show statistically significant reward improvements of 2.7–3.5% over a production base-stock system, and off-policy validation confirms the dynamics model generalizes to new policies.

## Strengths

- **First work to handle general inventory arrival dynamics with multiple shipments, stochastic yields, and post-processing constraints in an RL framework.** The paper documents these real-world phenomena empirically (Figure 1 shows that orders frequently arrive in multiple shipments with varying inter-arrival times; Figure 2 documents supplier fill rate distributions). The related work section convincingly argues that prior work in inventory control assumes either single-shipment lead times or simpler yield structures, and that post-processing constraints like minimum order quantities are handled by heuristics without theoretical guarantees.

- **Real-world A/B tests with statistically significant profitability improvements over a production base-stock system.** Two randomized control trials of QOT-DirectBP (Trials 2 and 3 in the A/B test table) show reward increases of 3.5% and 2.7% (both significant at 95% confidence), along with sales increases of 3.4% and 1.8%. The multi-trial design (including the VLT-DirectBP trial) and the comparison of simulator predictions to actual treatment effects on inventory level (Figure 10) add credibility.

- **Thorough off-policy validation of the dynamics model.** Using data from the A/B test, Tables 5 and 6 (off-policy calibration and quantile loss) show that the difference in Gen-QOT's forecast performance between the control (on-policy) and treatment (off-policy) arms is not statistically significant. This directly supports the key assumption required for valid backtesting and is a methodological contribution beyond what most inventory control papers provide.

- **Multi-criterion evaluation of the generative model.** The paper goes beyond standard lead-time forecasting metrics (Criterion 1) to evaluate cumulative receipt calibration (Criterion 2), classifier calibration for zero/first receipt events (Criteria 3–4), and arrival time calibration (Criterion 5). This thoroughness is appropriate for a model that will be used for downstream policy evaluation.

## Weaknesses

### Fatal
None.

### Major
None. The real-world A/B test evidence directly supports the paper's core claim — that RL policies with Gen-QOT dynamics outperform production base-stock systems. No individual weakness undermines this central finding.

### Minor

- **The backtest comparison of VLT-DirectBP vs. QOT-DirectBP (Table 4) evaluates both policies only on the Gen-QOT simulator, creating a home-field advantage.** The paper acknowledges this ("While it is unsurprising that the policy trained on the simulator used in evaluation performs best"), but the 8% gap shown could partly reflect evaluation bias rather than genuine superiority of the QOT model. The paper does not include the complementary experiment — evaluating both policies on a VLT simulator to show where each excels, or a head-to-head real-world A/B test of VLT vs. QOT policies. This weakens the claim that QOT dynamics yield better policies than VLT dynamics in practice; what is firmly established is that QOT-DirectBP beats the base-stock baseline in the real world.

- **Gen-QOT is evaluated against only a direct lead-time forecasting baseline for standard metrics; comparisons against other generative approaches are deferred to the appendix.** For Criterion 1 (lead-time metrics), the direct prediction baseline is appropriate, but Gen-QOT is statistically significantly worse on the P50, P70, and P90 quantile losses (confidence intervals in Table 1 exclude zero). The paper describes this as "competitive," which is accurate for CRPS and lower quantiles but downplays the degradation on central quantiles. The paper references an ablation study over architectures in the appendix (which exists in the original submission), but a brief summary of the key finding in the main text would help readers assess whether the specific Gen-QOT architecture is well-motivated.

- **The calibration of cumulative receipts shows systematic bias: all coefficients in Table 2 are significantly greater than 1 (e.g., 1.055–1.153, with CIs excluding 1 by wide margins).** This means the model systematically underpredicts cumulative arrivals (actual > predicted). The paper presents this data honestly but does not discuss the potential downstream impact on the RL policy — underpredicted arrivals could cause the policy to order more inventory than necessary, which is consistent with the increased inventory levels observed in the A/B tests (11.1% and 3.3% increases in Trials 2 and 3). An analysis of whether this bias is correctable or inherent to the modeling approach would strengthen the paper.

- **The theoretical framing (Section 3.3) claims learnability under Assumption 1 (accurate forecast of exogenous supply and arrival shares), but Remark 1 notes that in practice the authors forecast arrivals directly conditional on the action.** The conditional distribution p(arrivals | action, history) depends on the policy through the action, so the theoretical guarantees from Madeka et al. — which assume exogenous processes are modeled independently of actions — do not automatically extend. The paper's off-policy validation effectively addresses this concern empirically, but the theoretical discussion could be clearer about the relationship between the theory and the practical shortcut.

### Trivial

- The paper could more explicitly acknowledge in Section 4.1 that Gen-QOT trades off pure lead-time accuracy (where it is statistically significantly worse on central quantiles) for a richer arrival profile that benefits the downstream control task. This trade-off is implicit but worth stating directly.

## Nice-to-Haves

- **Sensitivity analysis of the post-processor f_p.** The paper introduces the post-processor as an important practical contribution but does not ablate it. How does policy performance change when the post-processor is removed? This would help quantify the value of the paper's handling of this constraint.

- **Cross-evaluation of VLT-DirectBP on a VLT simulator and QOT-DirectBP on a QOT simulator** (with the corresponding cross-evaluation numbers) would complete the backtest comparison. Even if the result is that each policy wins on its own simulator, this would confirm the "Sim2Real" framing and show the methods are both sound.

- **A generative baseline** (e.g., a simpler autoregressive model predicting arrival shares directly, or a VAE-based approach) for the arrival forecasting task, even if only on a subset of products, would help isolate the value of Gen-QOT's specific architectural choices.

- The paper could briefly discuss the economic interpretation of the inventory increases observed alongside reward improvements in the A/B tests (Trials 2 and 3). Whether the additional inventory cost is justified by the sales and reward gains depends on holding costs, which are not included in the reward definition.

## Removed Points

These points are flagged for removal per the review instructions; treat them with caution.

- **Criticism about missing appendix content (ablation study details, Gen-QOT architecture description, full calibration results).** Per instructions: the parser strips appendix sections from all papers; they exist in the original submission. The paper explicitly references \Cref{sec:neural-ablation}, \Cref{sec:genqot}, and other appendix sections.

- **Criticism that Gen-QOT lacks comparisons against VAEs or GANs.** The paper's primary contribution is to inventory control, not generative modeling. The architectural ablation (in the appendix) addresses architectural sensitivity. Demanding fundamentally different generative families is scope creep.

- **Claim that the theoretical guarantees are "misleading" or that the conditional forecasting approach does not fit the exogenous framework.** The paper explicitly states (Remark 1) that forecasting arrivals conditional on the action is a *practical choice*, and the learnability claim is tied to Assumption 1 (accurate forecast of exogenous variables). The arrivals are a deterministic function of exogenous variables ($U_t$, $\rho_t$) and the action; conditional on the action, forecasting arrivals is equivalent to forecasting the exogenous variables. The off-policy validation empirically confirms that the approach works.

- **Criticism about Trial 1 being "barely discussed."** The paper states this is the same trial described in prior work and uses it to validate the simulator (Figure 10), which is an appropriate and non-redundant treatment.

- **Claim that "first work" assertions should be further qualified.** The paper already uses "To the best of our knowledge" in both the abstract and Section 1.

- **Criticism about "the authors should add X" where X is a wishlist item rather than a structural flaw** (e.g., "sensitivity analysis of the post-processor," "brief summary in main text" of appendix content). These have been moved to Nice-to-Haves.

## Novel Insights

The reviews do not surface a genuinely novel perspective on the paper beyond its own contributions. The core observation — that a real-world A/B test validates the practical value of richer arrival dynamics in inventory control — is the paper's own contribution, not something the reviews add.

## Suggestions

1. **Add a sentence in Section 4.1 explicitly acknowledging the trade-off:** Gen-QOT is slightly worse on pure lead-time quantile metrics (P50, P70, P90) but captures the full arrival profile needed for the control task. This turns a potential weakness into a reasoned design choice.
2. **Include a brief discussion of the systematic calibration bias** (Table 2 coefficients > 1). State whether this is correctable (e.g., by recalibrating forecasts) and note the potential downstream effect on order quantities.
3. **Add a statement in Section 3.3 clarifying that** the theoretical guarantees apply under Assumption 1 (forecasting exogenous variables), while the practical shortcut of forecasting arrivals conditional on the action is a simplifying approximation validated empirically in Section 4.3.

## Score and Decision

This paper makes a clear, practically motivated contribution to an important applied problem. The real-world A/B tests provide compelling evidence that the overall approach works, and the off-policy validation is a methodological strength not commonly seen in this literature. The weaknesses are real but minor — none undermine the core finding that QOT-DirectBP outperforms production systems. The backtest comparison is acknowledged as biased by the authors themselves; the calibration bias is presented transparently; the theoretical framing gap is closed by empirical validation. With small expositional improvements, this paper will be a solid contribution at the intersection of reinforcement learning and inventory control.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>