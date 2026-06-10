## Summary

This paper proposes an LSTM-based Conditional GAN for generating synthetic vehicle velocity sensor time-series data conditioned on speed setpoint commands. The evaluation has three components: (1) quantitative metrics (MMD, Discriminative Score, Predictive Score) comparing generated data to held-out real data; (2) testing the generated data against the INDRA intrusion detection system, finding a 47.05% detection rate versus 88–100% for standard attacks; and (3) a qualitative demonstration of the model integrated into a validated vehicle model under varying speed commands.

## Strengths

- **Concrete IDS evasion benchmark with comparison to four standard attack types.** Table 1 / Section 3.2 reports that the generative model's synthetic data achieves only 47.05% detection by the INDRA IDS, benchmarked against sawtooth (91.18%), random (100%), plateau (88.24%), and replay (91.18%) attacks. These numbers provide a specific, interpretable reference point for the synthetic data's similarity to real data.

- **Conditional generation demonstrated in a closed-loop vehicle model with dynamic setpoint variation.** Section 3.3 shows the generative model integrated into the Eriksson et al. (2016) vehicle model, tracking a driving scenario where the speed setpoint is reduced by 10 km/h at 100-second intervals. This goes beyond static held-out evaluation and demonstrates online conditional generation capability.

- **Multi-metric evaluation framework.** The paper employs three distinct metrics (MMD, Discriminative Score, Predictive Score) from the established Yoon et al. (2019) framework and reports them per velocity setpoint, providing multidimensional validation beyond a single metric.

## Weaknesses

### Fatal
None.

### Major

- **No baselines or ablations — the core methodological claim is unevaluated.** The paper's central contribution is its LSTM-Conditional GAN architecture, yet the evaluation contains zero comparisons against any other generative model: not a vanilla GAN, not a VAE, not a simpler LSTM without adversarial training, not a non-conditional GAN, not even the TSGAN cited in the Related Work. Without baselines, it is impossible to determine whether the LSTM component adds value, whether the conditional mechanism is beneficial, or whether the GAN framework is necessary at all. A simple LSTM-based autoregressive predictor could potentially produce the same or better results. *This gap affects every contribution bullet listed in the introduction.*

- **No numerical values reported for the primary quality metrics.** The three quantitative metrics (MMD, Discriminative Score, Predictive Score) are central to the evaluation, yet none are reported numerically in the text. The MMD evaluation (Section 3.1) states only that it "converges relatively quickly" — no convergence value, no final MMD number. The DS and PS are shown exclusively in Figure 2 (an image) and the text says they are "consistent and comparable to" Yoon et al. (2019) without stating what the actual values are. For a paper whose title and contributions center on "high fidelity," the absence of any reported numerical fidelity measure prevents the reader from verifying the core claim. The IDS detection rates are reported numerically (47.05%, etc.), but the generative quality metrics that directly support the paper's central thesis are not.

- **Extremely limited evaluation scope relative to the claims.** The model is trained on a single sensor type (velocity) across 7 speed setpoints (30–90 km/h in 10 km/h increments), with 6 used for training and 1 held out for testing. Claims in the abstract and introduction about applicability to "wide range of vehicle networks" and "real-world scenarios" are not supported by experiments on a single sensor with 6 training profiles. The paper acknowledges this limitation in the conclusions but does not connect it to the breadth of its own claims.

### Minor

- **The IDS evasion result is a natural consequence of the model working correctly, not a demonstrated attack.** The IDS is an anomaly detector trained to flag deviations from normal traffic. The generative model is trained to produce in-distribution data. The fact that in-distribution data is not flagged as anomalous is expected. While the paper frames this as a "potential" security threat, it does not construct or evaluate an actual attack scenario (e.g., an attacker replacing a real sensor reading with synthetic data that simultaneously evades the IDS and masks a system-level fault). The comparison to plateau attacks (88.24% detection) is a comparison of apples to oranges — plateau attacks are designed to look different from normal data, so comparing their detection rate to in-distribution synthetic data does not reveal a security vulnerability.

- **The vehicle model integration (Section 3.3) is entirely qualitative.** The claim that the model "successfully follows the operational dynamics" rests on visual inspection of Figure 5 alone. No quantitative error metric (RMSE, MAE, maximum deviation) is reported between the generated sensor data and the actual sensor data under the same driving conditions.

- **Data source is not identified.** The paper never states where the velocity sensor data comes from — whether it was collected from a real vehicle, extracted from a simulation, or generated from the Eriksson et al. vehicle model itself. This is a basic reproducibility gap.

### Trivial
None.

## Nice-to-Haves

- Adding even a single baseline (e.g., a non-conditional LSTM-GAN or a VAE) would substantially strengthen the paper.
- Reporting the numerical MMD convergence value, DS, and PS for each speed profile in the text would make the evaluation verifiable.
- Providing confidence intervals or running the IDS experiment across multiple random seeds would improve robustness.

## Removed Points

Points flagged by reviewers but removed per filtering rules:

- *"Broken citation 'cmu' appearing in Section 2"* — This is a parser-induced formatting artifact; the original submission likely has a proper citation. Removed per formatting-artifact rule.
- *"Missing training hyperparameters (learning rate, optimizer, batch size, epochs, number of LSTM layers)"* — Removed per rule to remove nitpicks about undisclosed hyperparameters and trivial implementation details.
- *"OSU-Cyberlab (2024) and cha (2023a)/(2023b) cannot be verified"* — Removed per rule that prohibits questioning the existence or availability of cited references.
- *Strength Finder's claim that the paper provides "multi-metric evaluation with per-setpoint resolution" as a major strength* — Partially retained but weakened because the numerical values are not reported in the text, only shown in an image. The structure of the evaluation is valid but its evidential value is limited.
- *"Limited data / unspecified amount"* — The paper does report "approximately 40,000 samples over 380 seconds" (line 110), so this criticism is inaccurate. Removed.

## Novel Insights

None beyond the paper's own contributions. The reviewer inputs do not surface an observation about the paper that goes deeper than what the authors state.

## Suggestions

1. **Add at least one baseline** — a non-conditional LSTM-GAN and/or a simple LSTM autoregressive predictor trained with MSE. Without this, the reader cannot evaluate whether the proposed architecture is better than straightforward alternatives.
2. **Report numerical values for all three quality metrics** (MMD at convergence, DS and PS per speed profile) in the text or in a table.
3. **Provide a quantitative error metric for the vehicle model integration** (e.g., RMSE between generated and real sensor trajectories).
4. **Clarify the data source** and state what the velocity data originates from.
5. **Either construct a concrete attack scenario** that demonstrates system-level harm from the synthetic data, or reframe the IDS experiment explicitly as a fidelity check rather than a security finding.
6. **Broaden the evaluation** beyond a single sensor type and a small set of speed profiles before making claims about general applicability to vehicle networks.

## Score and Decision

This paper addresses a real need (synthetic data for vehicle systems), and the IDS evasion numbers provide a concrete demonstration that the model produces in-distribution data. However, the absence of any baselines, the failure to report numerical values for the primary generative quality metrics, and the extremely narrow evaluation scope (one sensor, six training profiles) prevent the paper from supporting its central claims. For a top-tier venue like ICLR, the evidence is insufficient to assess the contribution's significance or novelty relative to existing approaches.

MY FINAL SCORE: <score>3.0</score>
MY FINAL DECISION: <decision>Reject</decision>