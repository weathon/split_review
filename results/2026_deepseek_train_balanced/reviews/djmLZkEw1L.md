## Summary

IAM4VP proposes an implicit stacked autoregressive model for video prediction that combines aspects of autoregressive and non-autoregressive approaches. It uses a Multiple-In-Single-Out (MISO) architecture with continuous time embeddings to emulate multiple specialized models with a single network, and a "future queue" that accumulates the model's own predictions during inference to provide temporal context. The method achieves state-of-the-art results across five benchmark datasets (Moving MNIST, TrafficBJ, Human3.6, SEVIR, ICAR-ENSO), with particularly large margins on complex real-world data.

## Strengths

- **State-of-the-art results across five diverse benchmarks with substantial margins (Tables 2, 3, 7)**: On Human 3.6, IAM4VP achieves MSE 12.6 vs. SimVP's 31.6 (nearly 3× better); on ICAR-ENSO, MSE is 1.563 vs. Earthformer's 2.546 (nearly 40% improvement). These are not incremental gains, and the breadth across synthetic, traffic, human motion, weather radar, and climate data demonstrates generality.

- **Temporal interpolation capability from implicit design (Section "Dense Inference for VP", Fig. ab3)**: Because the model conditions on a continuous time variable *t* via sinusoidal positional encoding, it can perform inference at finer intervals than trained on. The paper connects this to a practical need in geostationary satellite data where temporal resolution varies across satellite generations — a capability that neither autoregressive (ConvLSTM/PredRNN) nor non-autoregressive (SimVP) models naturally support.

- **Component-level ablation quantifying each design decision (Table 4/tab:able1)**: The paper decomposes performance contribution per component — ConvNeXt predictor (+4.8 MSE improvement), STR refinement, stacked autoregressive masking, and Learned Prior fine-tuning. This enables readers to assess which choices are most impactful.

- **Qualitative experiment validating the future queue mechanism (Appendix, Fig. a1)**: The paper compares IAM4VP outputs under correct-order, random-shuffle, and all-zero future queue configurations, showing that the queue's temporal ordering genuinely affects predictions. This proactively addresses a natural concern about whether the mechanism is functional.

## Weaknesses

### Fatal
None.

### Major

- **The motivating experiment (Table 1) confounds architectural choice with a 10× disparity in parameters and training budget, undermining the paper's central narrative claim.** The paper argues that "the multi-input components, rather than the multi-output, significantly influence performance" by comparing SimVP-S MIMO (20.4M params, 2K epochs, MSE 23.5) against SimVP-S MISO-Multi Model (204M params = 10×20.4M, 20K epochs, MSE 18.7). A MIMO baseline trained for 20K epochs is provided (MSE 21.4), but its parameter count remains 20.4M — one-tenth the MISO-Multi Model's total capacity. Because the MISO-Multi Model uses ten separate models, attributing its advantage to "multi-input" rather than to simply having 10× the capacity and 10× the training compute is not supported by the evidence as presented. A controlled comparison matching total parameter count (e.g., a single MIMO model with ~204M parameters trained for 20K epochs) would be needed to determine whether the advantage is architectural or a resource effect. This matters because the entire motivation of IAM4VP rests on the premise that MISO architectures can outperform MIMO.

- **The "No Error Accumulation" claim for IAM4VP in Table 1 (table:properties) is overstated.** The table assigns IAM4VP a checkmark for "No Error Accumulation" alongside non-autoregressive models that genuinely have zero error accumulation because they predict all frames independently from observed frames only. However, the paper's own Figure 6 (right panel) shows that IAM4VP's error *does* increase with time step — the trend is less steep than SimVP's, but it is not flat. The paper's own text (line 404) states "the error in both methods increases as the time step increases." The Appendix further shows that corrupting the future queue degrades performance (Fig. a1), confirming the model is sensitive to errors in its own predictions. "Reduced error accumulation" would be accurate; "no error accumulation" is not, and conflates IAM4VP's behavior with genuinely non-autoregressive models.

### Minor

- **The mask generator M_g (Eq. 4) is critically underspecified for reproducibility.** The paper states: "Random(·) is a function that selects a random number of random indices." The ablation shows this component is essential: "Stacked Autoregressive w/o M_g" achieves MSE 25.2 at 10K (worse than the 23.5 baseline at 2K), while "w/ M_g" achieves 15.8 at 10K — a 9.4-point swing. A component this impactful requires a precise definition: how many indices are selected, from what distribution, and how does selection depend on the time step *t*? Without this, the core stacked autoregressive mechanism cannot be independently reproduced.

- **The training procedure uses ground-truth future frames (teacher forcing) for the future queue, creating a train-test gap that is acknowledged but not quantified.** Algorithm 1 initializes the future queue Q_f from ground-truth features e(y_i). During inference, the queue is filled with the model's own predictions. While the Learned Prior (LP) is introduced to address this and the paper acknowledges the issue, no experiment measures the distributional gap between ground-truth and predicted queue features, or demonstrates that the LP fully closes it. This leaves open a meaningful exposure bias concern.

- **No variance, standard error, or confidence intervals are reported for any experiment.** All main results appear to come from single runs. Given that the paper makes SOTA claims across five datasets and that some comparisons are tight (e.g., SEVIR CSI-M: 0.4607 vs. 0.4419 for Earthformer), the lack of uncertainty quantification makes it impossible to assess whether reported advantages are statistically significant.

- **The cumulative ablation design makes it difficult to isolate the stacked autoregressive contribution independently of preceding components.** The marginal gain of the stacked autoregressive with M_g (MSE 15.8 at 10K) over the implicit MISO + STR (MSE 16.2 at 10K) is only 0.4 MSE points. By comparison, the ConvNeXt predictor (+4.8) and STR contribute more. While the paper frames the stacked autoregressive as the core novelty, the ablation does not cleanly demonstrate its standalone benefit from the accumulated improvements of prior components.

### Trivial
None.

## Nice-to-Haves

- A precise specification of the mask generator M_g with concrete parameters (number of indices, distribution type) would resolve the reproducibility gap.
- An analysis comparing the feature-space distribution between ground-truth and predicted queue entries, and how the Learned Prior affects this gap, would strengthen the claim that exposure bias is mitigated.
- Inference-time FLOPs or runtime comparison against MIMO models would be useful since IAM4VP requires iterative decoding through the future queue.
- The initial MSE_i values used for the validation-error-based sampling strategy (Eq. 3) could be clarified.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *Criticism: MIMO-VP only reported on MNIST, not on other datasets.* — The paper uses the asterisk (*) to note these are from the original paper. This is standard practice; re-implementation of every baseline on every dataset is not strictly required.
- *Criticism: SimVP and MIMO-VP excluded from weather benchmarks.* — The paper explicitly acknowledges this limitation in the Table 7 caption. Already addressed.
- *Criticism: decoder architecture confound in the MISO-Autoregressive comparison.* — The paper states they modified the *same* SimVP model; the decoder structure change *is* the intervention being tested. Speculative.
- *Criticism: "does not specify how the model handles variable-length outputs."* — Fixed-length output is an explicitly discussed design choice and acknowledged as a limitation. Already addressed.
- *Criticism: "where do initial MSE_i values come from" in the sampling strategy.* — Reasonable implementation question but very minor; belongs in a code release.
- *Strength: "Controlled experiment disproving the necessity of multiple-output"* — Conflicts with the verified Major weakness #1 about the confounded comparison.
- *Strength: generic praise about problem importance or superficial observations.* — Lacks a specific evidence anchor in the paper.

## Novel Insights

Beyond the paper's own contributions, the reviews surface a productive tension: the paper's narrative frames the stacked autoregressive mechanism as the central innovation, but the cumulative ablation suggests that STR and the ConvNeXt predictor contribute comparable or larger performance gains. This is not a fatal problem — ablation orders are arbitrary — but it means the paper's key claimed novelty is difficult to isolate and evaluate independently.

## Suggestions

1. Re-run the motivating experiment (Table 1) with matched total parameters: train a single MIMO model with ~204M parameters for 20K epochs. If the MISO-Multi Model advantage holds, the narrative claim is credible; if not, reframe the motivation around the actual empirical finding (implicit MISO + stacked autoregressive works well, not that MISO inherently dominates MIMO).
2. Replace the "No Error Accumulation" checkmark in Table 1 with "Reduced Error Accumulation" to accurately reflect the empirical behavior shown in Figure 6.
3. Provide a precise, reproducible description of the mask generator M_g with concrete parameters.
4. Report results with multiple seeds or confidence intervals for at least the main benchmarks to establish statistical significance.
5. Add an analysis of the feature-space gap between ground-truth and predicted queue entries, and quantify how the Learned Prior bridges this gap.
6. Include MIMO-VP results on TrafficBJ and Human3.6 (if feasible to re-implement), or at minimum discuss the likely comparative performance, to strengthen the SOTA claims.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>