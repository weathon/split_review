Now I have a thorough understanding of the paper. Let me synthesize the final review.

## Summary

This paper proposes SONNET, a probabilistic day-ahead net load forecasting method for power grids with behind-the-meter (BTM) solar generation. It consists of three main components: (1) an unsupervised BTM solar disaggregation algorithm that separates net load into solar generation and load components using a physical solar model and iterative similarity-based optimization; (2) a Transformer architecture that uses self-attention on historical data and cross-attention between future weather forecasts and historical embeddings; and (3) a physical-model-based data augmentation method that simulates weather forecast errors during training to improve robustness. The method is evaluated on the U.S. DOE net load forecasting competition dataset across four diverse locations (TX, OR, GA, HI) and compared against the competition's top teams.

## Strengths

1. **Unsupervised solar disaggregation with near-supervised accuracy**: The paper develops a fully unsupervised algorithm that recovers solar generation and load from net load data alone, using only a regional solar capacity estimate. Table 1 shows RMSE, MASE, and CV values very close to a supervised learning bound across four simulated solar penetration levels. This is a practical contribution since utilities typically have capacity estimates but not ground-truth solar generation traces.

2. **Novel and coherent methodological integration**: The combination of unsupervised disaggregation, a Transformer with cross-attention between historical embeddings and future (forecast) variables, and physics-based data augmentation forms a non-trivial, well-motivated pipeline. The cross-attention mechanism allowing the model to "look up similar conditions from the past" given future weather forecasts (Section 4.2) is a clever architectural choice for this problem domain.

3. **Thorough ablation study isolating each component's contribution**: Tables 3–5 systematically remove disaggregation, data augmentation, exogenous variables, and vary predictor architectures and context lengths. This provides clear evidence that each component contributes positively. The data augmentation is shown to be particularly impactful for Hawaii (where solar penetration is highest and weather forecasts are least accurate).

4. **Real-world evaluation on a competitive benchmark**: The use of the DOE competition dataset provides a realistic and standardized test bed with four diverse climates and solar penetration levels (0.18–1.57 normalized capacity). Comparing against actual competition entries (90+ teams including commercial forecasters) grounds the evaluation in a practical, externally validated context.

## Weaknesses

### Major

1. **Factual discrepancy between text claim and table data for the "extreme errors" comparison**: The paper states (Section 5.3, Results paragraph): "even under the most challenging conditions with extreme forecast errors of weather features, SONNET still consistently outperforms these top teams (which, in comparison, perform with normal errors)." However, the table data (Table 2) shows that for TX and OR under the "Extreme" error scenario, SONNET's CRPSS falls below the "Best among all" competition entry (e.g., TX: 0.619 vs. 0.630; OR: 0.554 vs. 0.590). The blanket "consistently outperforms" claim is thus factually unsupported for at least two of four locations. This is not a methodology debate — it is a mismatch between the paper's own textual claim and its displayed results. The authors should either qualify the claim (e.g., "outperforms on average" or "outperforms for GA and HI") or explain why the comparison against "Best among all" per-location is not the intended comparison.

2. **Limited validation of the solar disaggregation component on a single, non-representative dataset**: The unsupervised disaggregation algorithm (a core claimed contribution) is validated only on a four-week dataset from Austin, TX (2015, 322 customers). This dataset differs substantially from the DOE competition data in time period (2015 vs. 2022–2023), location (single city vs. four diverse U.S. regions), and aggregation scale (322 customers vs. city/town populations). The ablation study (Table 3) shows that disaggregation contributes only marginal CRPSS improvement in some locations (e.g., TX: 0.642 → 0.643), raising the question of whether the disaggregation component's sophistication is justified by its practical forecasting benefit. The paper does not test whether disaggregation quality — and resulting forecasting gains — transfers to the actual competition sites.

3. **No statistical significance or uncertainty quantification for main forecasting results**: SONNET's CRPSS scores in Table 2 are reported as point estimates averaged over 20 experiments (each with 10 replicates), but no confidence intervals, standard deviations, or hypothesis tests are provided. Given that some comparisons involve small margins (e.g., the TX extreme scenario above), the reader cannot assess whether differences are meaningful or noise. This is a standard expectation for any paper making comparative performance claims.

### Minor

1. **The comparison with competition teams relies on simulated weather forecast errors whose fidelity is unvalidated**: SONNET is evaluated using errors sampled from normal distributions with empirically estimated standard deviations (Section 5.3), while competition teams used real (uncontrolled) weather forecasts. The paper states it wants to "ensure a fair comparison" but does not verify that the simulated "Normal" error distribution matches the actual forecast errors experienced by competition teams. While the overall approach is reasonable, the lack of validation that the simulation realistically reproduces real-world error patterns weakens the claim that the comparison is truly apples-to-apples.

2. **Limited test period and seasonal coverage**: The evaluation covers a 28-day competition period (June 18 – July 15, 2023). This single season/summer window may not capture performance across different seasons, especially for solar generation which varies significantly with time of year. The paper uses 1.5 years of training data but evaluates only on a narrow test window.

3. **Data augmentation only addresses weather forecast errors, not disaggregation errors**: The augmentation method (Section 4.3) perturbs weather features and recomputes solar generation through the physical model, but treats the disaggregation algorithm's output as fixed. Since disaggregation errors also affect the predictor's input, the robustness benefit is incomplete. This is acknowledged indirectly but not discussed as a limitation.

### Trivial

- None that survive the filtering rules.

## Nice-to-Haves

- Include reliability diagrams or mean binned pinball loss to verify probabilistic calibration; CRPSS alone can mask miscalibration.
- Test disaggregation on additional datasets (or synthetically on DOE data) to establish transferability of the unsupervised algorithm.
- Show case study examples contrasting high-solar and low-solar days to illustrate when disaggregation and data augmentation help most.
- Disclose key architectural hyperparameters (number of layers, heads, embedding dimension, patch length/stride) for reproducibility.

## Removed Points

These points were flagged by reviewers but are removed as per policy (see justifications below):

- **Criticism that the comparison with competition teams is "not apples-to-apples" because of different error characteristics**: The paper simulates errors from empirical distributions estimated from actual forecast errors. The "Normal" setting roughly matches real-world error levels, and "Extreme" is deliberately harder — which would make the comparison more conservative, not unfair. However, the *specific factual claim* of "consistently outperforms" is retained as a major weakness (see above) because it may contradict the table data for TX and OR.

- **Criticism that the idea of separating load and solar generation "already appears in cited works"**: This is a framing issue (not a weakness of the paper's contribution), and the paper properly cites prior work on this concept. The paper's contribution is in the specific unsupervised algorithm, Transformer architecture, and data augmentation.

- **Complaints about missing appendix sections (references to "7.1", "2.1", "2.2")**: The parser strips appendix content; these sections exist in the original submission.

- **Formatting/style nitpicks about the table images, figure placement, or typographical issues**: These are parser artifacts, not author errors.

- **Criticism that hyperparameters are not fully disclosed**: While some architectural details would be helpful, the core hyperparameters for reproducibility are not fully provided. Moved to Nice-to-Haves.

## Novel Insights

The most interesting observation emerging across the reviews and the paper data is the tension between the disaggregation algorithm's strong performance on its validation dataset (close to supervised bounds) and its marginal contribution to actual forecasting gains (TX: 0.642→0.643 in the ablation). This suggests either (a) the disaggregation quality degrades on the DOE data due to distribution shift (which the paper cannot test since DOE has no ground-truth solar), or (b) the Transformer predictor can implicitly learn solar patterns from weather features and net loads alone, making explicit disaggregation less additive than expected. The paper does not resolve which explanation holds, but the question is important for future work on this problem.

## Suggestions

1. **Fix the factual claim in Section 5.3**: Either qualify the "consistently outperforms" statement to acknowledge the TX and OR extreme-error results, or clarify whether the comparison is against the listed top six teams' scores (rather than the per-location "Best among all" entry). If the claim holds against the top six teams individually, the text should say so explicitly.

2. **Add confidence intervals to all main results**: Report standard deviations or 95% confidence intervals for Table 2 and Table 3 CRPSS scores, ideally using bootstrap over the 20×10 experiment replicates. This is necessary to assess whether reported differences are significant.

3. **Acknowledge the disaggregation validation gap in a Limitations section**: The paper should explicitly discuss that the disaggregation algorithm is validated on a single historical Austin dataset and that its quality on the DOE sites is unknown, with implications for the overall method's reliability.

4. **Provide a direct comparison on identical ground truth**: Even a small-scale experiment where SONNET is re-run using the actual weather forecasts (not simulated errors) from the competition period on a subset of days would strengthen the fairness of the comparison substantially.

## Score and Decision

The paper addresses a practically important and well-motivated problem with a creative combination of techniques. However, the core comparative claim is undermined by a factual inconsistency between the text and the displayed results for two of four locations under the extreme-error setting. Combined with limited disaggregation validation and absent uncertainty quantification, the paper in its current form does not fully substantiate its headline claims. The weaknesses are addressable, and the methodology has genuine merit, but the paper as presented requires substantial revision of its claims and analysis.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>