Here is my consolidated meta-review.

---

## Summary

This paper extends the exogenous decision process (EDP) framework for periodic-review inventory control to handle **general arrival dynamics** (multiple shipments per order, stochastic yields) and **arbitrary downstream post-processing** of order quantities (minimum-order constraints, batch sizes) — two realistic complexities that prior work (Madeka et al., 2022) did not address. The authors propose a quantity-over-time (QOT) arrival model, build a deep generative model (Gen-QOT) to forecast arrivals conditional on actions, and train a DirectBackprop policy in a differentiable simulator. The paper provides backtest evidence that the QOT-based policy outperforms a VLT-based policy, validates off-policy generalization of the dynamics model using A/B test data, and demonstrates via two real-world trials that the QOT-DirectBP policy improves reward (2.7–3.5%) over a production base-stock system.

## Strengths

- **First work to model general arrival dynamics and order post-processing in a learnable framework.** The paper formally defines the QOT arrival model (supply $U_t$, arrival shares $\boldsymbol\rho_t$, post-processor $f_p$) and shows it subsumes multiple real-world complexities — multiple shipments, stochastic yields, minimum/batch constraints — that previous RL inventory work treated simplistically or not at all (Abstract, Section 3.1, Fig. 1–2). This is a genuine modeling contribution.

- **Rigorous off-policy validation of the dynamics model.** Using data from the treatment and control arms of the real-world A/B test, the paper compares Gen-QOT forecast errors across arms and finds no statistically significant degradation (Tables 5–6, Fig. 8). This directly tests Assumption 1 (accurate forecast under policy shift) in a live setting — a validation step absent from prior work (Madeka et al.) and uncommon in the RL-for-supply-chain literature.

- **Real-world A/B test evidence.** Two randomized trials (Trials 2 and 3) show that QOT-DirectBP achieves statistically significant reward improvements (3.5%, 2.7%) over a production base-stock system at a large e-retailer, covering thousands of products over several months (Section 5.3, Table 3). Such live operational validation is rare and adds credibility.

- **Evidence that the QOT simulator better captures reality than the VLT simulator.** Figure 9 compares the real-world inventory treatment effect of VLT-DirectBP (Trial 1) against rollouts from both simulators; the QOT simulator's estimate contains the true point estimate within its CI, while the VLT simulator's does not. This provides indirect evidence that the QOT dynamics are a more faithful approximation of the real supply chain.

## Weaknesses

### Fatal

None.

### Major

- **Backtest comparison (Table 4) evaluates both policies only on the QOT simulator.** The 8% gap between QOT-DirectBP and VLT-DirectBP is measured entirely in the Gen-QOT environment. Since VLT-DirectBP was trained under VLT dynamics, evaluating it primarily on QOT dynamics creates an asymmetric advantage for QOT-DirectBP. To strengthen the methodological claim, the paper should also evaluate both policies on a VLT simulator and, ideally, on real historical data via off-policy evaluation or counterfactual simulation. The paper partially acknowledges this ("unsurprising" that the QOT-trained policy wins on the QOT simulator), and Figure 9 provides supporting evidence that the QOT simulator is more faithful to reality — but the direct policy comparison remains incompletely validated.

### Minor

- **Gen-QOT underperforms the direct lead-time forecast on standard VLT metrics, yet is described as "competitive."** Table 1 shows that Gen-QOT is statistically *worse* on P50, P70, and P90 quantile loss (CIs entirely above zero), and not distinguishable on CRPS. The paper should be more transparent about this trade-off. The justification — that Gen-QOT models richer dynamics that the direct model cannot represent (multiple shipments, sample paths) — is reasonable, but the framing could mislead readers about the forecasting quality.

- **Systematic calibration bias.** The cumulative-receives calibration coefficients (Table 2) are consistently above 1 (1.05–1.15) with CIs excluding 1, indicating Gen-QOT systematically overestimates cumulative inventory received by 5–15%. The paper acknowledges this but does not discuss its impact on downstream policy quality.

- **No ablation isolating the post-processor's contribution.** The post-processor $f_p$ is listed as a key element of the contribution, yet the experiments never isolate its effect (e.g., training a policy with and without the post-processor). It is unclear whether the post-processor meaningfully changes policy behavior or is a trivial convenience.

### Trivial

None.

## Nice-to-Haves

- A direct real-world A/B comparison between QOT-DirectBP and VLT-DirectBP (same time period, concurrent randomization) would be the cleanest evidence for the QOT model's superiority. However, the paper's main A/B claim is against production baselines, not VLT, so this is an extension rather than a missing requirement.
- Evaluating both policies on a VLT simulator (the reverse asymmetry of Table 4) would clarify whether QOT-DirectBP generalizes well, or only when evaluated on its home simulator.
- A diagnosis of why VLT-DirectBP failed in Trial 1 (reward flat, inventory −15%) would strengthen the motivation for QOT and help identify whether the failure was due to VLT dynamics or other factors.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Critic's Issue 1 (A/B test does not isolate QOT contribution):** The critic states that the paper's central claim — that QOT yields superior policies — is unsupported because the A/B test compares QOT-DirectBP only against production baselines, not against VLT-DirectBP. However, the paper's central A/B claim is that QOT-DirectBP *outperforms production baselines* (which is demonstrated). The QOT-vs-VLT comparison is made in the backtest (Table 4), not in the A/B test. The critic misattributes the evidentiary claim. A *weakened* version of this concern (that a direct real-world head-to-head would strengthen the paper) is retained in Nice-to-Haves above.

- **Critic's claims about missing post-processor ablation and missing backtest on VLT simulator:** These are retained as weaknesses above (post-processor ablation as Minor; VLT simulator backtest as Major).

- **Critic's claim about "no ablation isolating post-processor effect":** Actually kept as a minor weakness above — it's a valid point.

- **Critic's statements about Trial 1 analysis being missing:** This is moved to Nice-to-Haves since it's a missed opportunity for deeper analysis, not a requirement.

- **Critic's "Obvious Next Steps" about theoretical characterization:** This is a suggestion for future work, not a weakness of the current paper.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add a backtest evaluation of both QOT-DirectBP and VLT-DirectBP on a VLT simulator to complete the bidirectional comparison. This would test whether QOT-DirectBP catastrophically underperforms when the world is VLT-like and would strengthen the claim that QOT dynamics are a better approximation.
2. Include an ablation experiment isolating the post-processor (policy trained with and without $f_p$) to quantify its empirical impact.
3. In Table 1, adjust the language from "competitive" to a more precise characterization — e.g., "Gen-QOT achieves comparable or slightly worse standard VLT metrics but captures richer arrival dynamics that the direct model cannot represent."
4. Provide a brief analysis of why VLT-DirectBP failed to improve reward in Trial 1 (was it model misspecification, action distribution shift, or something else?).

## Score and Decision

The paper makes a meaningful contribution by extending inventory control to realistic arrival dynamics and order post-processing, with rare real-world A/B test validation. The major weakness is that the central policy comparison (QOT vs. VLT) relies on a backtest that evaluates both policies only on the QOT simulator. While Figure 9 provides supporting evidence that the QOT simulator is more faithful to reality, a bidirectional backtest and/or real historical counterfactual evaluation would substantially strengthen the case. The paper otherwise presents sound methodology, thorough off-policy validation, and genuine empirical value.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>