Now I have verified all claims against the paper. Let me produce the final review.

## Summary

This paper identifies an information leakage issue in existing online time series forecasting (OTSF) evaluations — where predictions are evaluated on time steps already used for backpropagation — and proposes a redefined setting that ensures models are only evaluated on genuinely unseen future steps. To address the resulting challenge of sparse supervisory signals, the authors propose DSOF, a dual-stream framework combining experience replay ("slow stream") with temporal difference learning ("fast stream") on a teacher-student residual architecture. The teacher backbone is frozen during online updates; a lightweight 3-layer MLP student refines predictions.

## Strengths

- **Clear identification and formalization of a concrete methodological flaw in prior OTSF evaluations**: Section 1.1 and Figure 1 precisely describe how in prior work (Pham et al., 2023; Zhang et al., 2023, 2024a), at t=12 the model evaluates predictions for timestamps t=9–11 that were already used for backpropagation at t=11. The redefined setting (Section 3.1) cleanly eliminates this — the model is evaluated only on time steps that have never received gradient feedback, and H equals the number of genuinely unknown future steps.

- **Temporal-difference learning enables immediate updates despite incomplete ground truth**: Under the no-leakage setting, at time i+1 only one ground-truth value (x_{i+1}) is available for an H-step forecast made at time i. The TD loss (Section 3.3.2, Equations 5–6) constructs pseudo-labels by combining the one real observation with the teacher's predictions for the remaining H−1 steps, weighted by geometric decay γ. This allows the model to learn from new data immediately rather than waiting H time steps for complete supervision — a practical innovation directly addressing the core challenge.

- **Consistent improvement over batch learning across diverse backbones and datasets**: Table 2 (Section 4.1) shows DSOF achieves lower MSE than batch learning on all six datasets (ECL, ETTh2, ETTm1, Exchange, Weather, Traffic) and across all eight backbone architectures spanning linear, convolutional, and transformer families. The ECL dataset shows reductions exceeding 50% with FSNet and NSTransformer backbones.

- **Model-agnostic design validated on three architectural families**: DSOF is tested with linear (DLinear, FITS, TimeMixer), convolutional (FSNet, OneNet), and transformer (iTransformer, PatchTST, NSTransformer) backbones, supporting the claim of broad applicability.

## Weaknesses

### Fatal

None.

### Major

- **Frozen backbone vs. overstated claims of online adaptation**: The paper states explicitly (line 113) that "the teacher model's parameters θ^(T) remain fixed" while only the student model updates. The student is a three-layer MLP with hidden dimension 16 — a tiny fraction of the total parameters. Yet the paper repeatedly claims it "facilitates the online training of time series deep learning models" (Section 3), "enables various types of models to adapt to temporal shifts in real-time data" (abstract, conclusion), and that DSOF enables models to "adapt to temporal shifts" (conclusion). The backbone — which constitutes essentially all of the model's capacity — never adapts. What actually adapts is a lightweight residual corrector. This is a significant mismatch between the claimed scope and the actual mechanism. The paper would be stronger if it explicitly framed the contribution as "online refinement of forecasts via a lightweight corrector on a frozen backbone" rather than "online training of deep forecasting models."

- **The main experimental comparison is against a trivial baseline, and the novel component is not reliably beneficial**: Table 2 compares DSOF (online updating with a student) against batch learning (the teacher model with no updating at all). This merely establishes that online updating beats no updating — which is already the premise of the entire OTSF literature and does not validate DSOF's specific design. More critically, the paper reports (line 164) that "in some cases, running the model without the student model gives better results." The full DSOF method is not consistently better than DSOF-without-the-student. The paper attributes this to hyperparameter robustness (the student reduces sensitivity to learning rate), but this means the core contribution — the residual student MLP — does not reliably improve accuracy, raising the question of what the residual correction strategy contributes beyond the dual-stream update mechanism alone.

### Minor

- **TD pseudo-label construction risks reinforcing teacher bias without analysis**: The fast stream (Section 3.3.2) constructs pseudo-labels for unobserved future steps by concatenating the single real observation with the teacher model's *own* predictions. Since the teacher is frozen, any systematic bias in the teacher is propagated into the pseudo-labels. The geometric decay factor γ mitigates this for distant steps but also means the TD loss is most influential for near-future steps where the teacher's predictions are already most reliable. The paper does not provide ablation in the main text isolating the contribution of the TD loss from the experience replay (Section A is referenced but stripped by the parser). This makes it difficult to assess whether the TD component adds meaningful value beyond the replay buffer.

- **The information leakage critique is not empirically quantified**: The paper claims prior OTSF evaluations have information leakage and that this "leads to biased evaluation outcomes, leading to an overestimation of the model's effectiveness" (Section 1.1). However, the paper does not re-evaluate any prior method under both the old and new protocols to quantify the magnitude of this overestimation. Without this, the reader cannot distinguish between a genuine source of inflation and a minor technical discrepancy in protocol alignment.

- **Notation inconsistency in Equation 6**: The TD loss ℓ_TD^(i-1) takes as arguments a prediction made at time i-1 (superscript i-1) and pseudo-labels formed at time i (superscript i). However, the inner sum uses x̂_j^(i) and x̃_j^(i) — both with superscript (i). The relationship between the superscript, the step index j, and the original prediction time is unclear. This makes the equation harder to interpret than it should be.

### Trivial

None.

## Nice-to-Haves

- **Runtime or computational cost comparison**: Online learning involves a trade-off between accuracy and update speed. DSOF runs both ER and TD updates per time step. Reporting wall-clock overhead versus batch learning and DGrad would help assess deployment feasibility.

- **Analysis of when batch learning beats DSOF**: The paper acknowledges (line 134) that "in some cases, batch learning outperforms online approaches" but attributes this speculatively to normalization choices. A systematic analysis of what characterizes these failure cases would strengthen the paper.

- **Buffer size sensitivity**: The replay buffer size N_B is a key hyperparameter governing the adaptation-speed/stability trade-off. If this analysis is in the appendix, a brief summary in the main text would be helpful.

## Removed Points

These points were flagged by reviewers but are removed or demoted for the following reasons:

- **"Information leakage contribution is incremental/not substantive"** — This is a value judgment about the contribution's significance, not a verifiable weakness. The paper's identification of the issue is concrete and well-described (Section 1.1, Figure 1). Whether this rises to a "substantive research contribution" or a "note on experimental hygiene" is a matter of opinion, not a factual flaw; I retain it as Minor (contributions could be stronger with quantification) rather than removing the concern entirely, but I do not accept the framing that it is negligible.

- **"DGrad strips away all innovations of prior methods"** — Not supported by the paper. The paper states it modified the *setting* (delayed feedback), not the methods themselves. DGrad retains the original FSNet/OneNet architectures and update mechanisms, just with delayed gradients. The critic's characterization goes beyond what the paper describes.

- **"Table 3 baselines are weak" (TFCL, DER++)** — The paper explicitly acknowledges these are vision-domain continual learning methods "not tailored for time series forecasting" and uses them as additional baselines, not as the primary comparison. The primary comparison in Table 3 is DGrad (adapted prior OTSF methods). Calling baselines "weak" is reasonable criticism but the paper is transparent about their limitations.

- **"Experience replay discards older data — catastrophic forgetting"** — The paper explicitly justifies this choice (line 88): unlike continual learning, their objective is minimizing cumulative MSE, so they retain only recent samples. This is a design choice, not an oversight.

- **"No analysis of buffer size N_B"** — Likely in the appendix (Section A is referenced for further analyses). Parser strips appendix content.

- **"Equation 1 typo (bateh)"** — Removed per hard rules on typos/formatting artifacts.

- **"Tables 2 and 3 are images"** — Formatting artifact from PDF parsing.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Reframe the contribution honestly**: Explicitly state that the backbone is frozen and what adapts is a lightweight residual corrector. Remove phrasing like "online training of deep learning models" and "enabling various types of models to adapt" unless the backbone itself is updated.

2. **Quantify the information leakage**: Re-run at least one prior method (e.g., FSNet) under both the old protocol and the new protocol and report the difference in MSE. This would substantiate the claim that prior evaluations are inflated.

3. **Provide ablation isolating TD loss from ER in the main text**: Show results for (a) slow stream only (ER, no TD), (b) fast stream only (TD, no ER), (c) both streams, (d) neither. This is essential for understanding which mechanism contributes what.

4. **Clarify Figure 3 / Table 3 interpretation**: Address explicitly why DSOF without the student sometimes outperforms full DSOF, beyond hyperparameter robustness. If the student is primarily a stabilizer rather than accuracy booster, say so clearly.

5. **Fix Equation 6 notation**: Ensure the superscripts on x̂ and x̃ inside the sum are consistent with the superscripts on the loss function arguments.

## Score and Decision

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>