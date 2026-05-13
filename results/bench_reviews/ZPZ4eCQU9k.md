## Summary

xLSTM-Mixer is a multivariate time series forecasting model combining three stages: (1) a channel-independent NLinear initial forecast with time mixing, (2) sLSTM refinement that strides over variates (treating each variate's full time series as a single token, adapted from iTransformer), and (3) multi-view mixing that processes both the original and dimension-reversed up-projected embedding through shared-weight sLSTM blocks before a learned linear reconciliation. The paper demonstrates state-of-the-art long-term forecasting performance on standard benchmarks (18/28 MSE, 22/28 MAE settings) backed by a thorough ablation study.

---

## Strengths

- **Strong benchmark performance with an honest win-count framing**: Table 1 shows xLSTM-Mixer achieves the best MSE in 18/28 cases and best MAE in 22/28 cases across Weather, Electricity, Traffic, and ETT datasets, including clear MAE improvements over TimeMixer (+4.6% on Weather) and xLSTMTime (+2% on Weather). The paper also transparently acknowledges underperformance on Traffic and ETTh2.

- **Thorough ablation study with 10 configurations**: Table 3 systematically evaluates all combinations of the four key components (NLinear time mixing, sLSTM blocks, initial embedding token, multi-view mixing) on Weather and ETTm1. Quantified drops are provided: removing time mixing raises MAE by 3.4% on ETTm1 at horizon 96; removing everything except time mixing on Weather at 192 yields a 13.7% degradation.

- **Interpretable initial embedding token visualization**: Figure 2 (decoded soft-prompt tokens across datasets and horizons) provides concrete evidence that the learned initial embeddings capture dataset-specific seasonal structure that evolves with prediction horizon—a meaningful and verifiable interpretability contribution.

- **Lookback length robustness grounded in architectural advantage**: Figure 4 provides variance-quantified evidence (shaded std. dev.) that xLSTM-Mixer consistently improves with longer lookback windows, an advantage directly tied to its absence of quadratic self-attention—this is a genuine architectural finding, not a generic claim.

- **Code release and reproducibility**: Source code is provided explicitly, and the paper explicitly addresses xLSTMTime's reproducibility problems by committing to full reproducibility of its own results.

---

## Weaknesses

### Fatal
None.

### Major

- **Absence of Mamba/SSM-based time series baselines, despite explicit positioning in the SSM resurgence**: The introduction frames xLSTM-Mixer squarely within the "resurgence of recurrent and state space models" and cites SSMs directly. Yet the comparison set contains only one recurrent competitor (xLSTMTime, which the paper also identifies as hard to reproduce and weak) and several older Transformer variants (Autoformer, FEDFormer) that are well-known to underperform on these benchmarks. Several Mamba-adapted time series models (e.g., S-Mamba, Mamba4TS variants) exist in this space. Their absence means the headline claim—that xLSTM specifically outperforms other linear-time sequential models—is unsupported; the comparison conflates "better than attention-based models" with "best among recurrent/SSM approaches." This is a meaningful gap given the paper's own framing.

- **Core novel component (multi-view mixing) lacks a principled mechanistic ablation**: Section 3.3 specifies that the "reversed embedding" inverts the order of the D-dimensional latent feature axis—not time reversal (which has clear temporal semantics) and not variate reversal (which would test ordering sensitivity). After FC^up, the D-dimensional coordinates carry no natural ordering; reversing them produces a permuted but semantically equivalent representation. The ablation confirms multi-view mixing helps, but offers no experiment isolating *dimension reversal specifically* from *running the sLSTM twice*. A minimal control—two forward passes with identical inputs (no reversal)—would distinguish ensemble variance reduction from the claimed representation diversification. Without this, the mechanistic story is unsupported even though the empirical benefit is real.

### Minor

- **Ablation confined to 2 of 8 benchmark settings, with no ablation on the harder failure cases**: Table 3 covers only Weather and ETTm1. The paper explicitly acknowledges that Traffic and ETTh2 are challenging, attributing this to outliers. However, it provides no ablation on these datasets—so whether the identified component contributions generalize to the failure regimes is unknown. Extending the ablation to at least one of the underperforming datasets would substantially strengthen the claims.

- **sLSTM vs. mLSTM choice is asserted, not empirically validated**: Section 2 states mLSTM "treat[s] sequence elements independently, making it impossible to learn relationships between them directly," and uses this as the architectural justification for choosing sLSTM exclusively. This is architecturally motivated reasoning, but given that the original xLSTM paper itself shows mLSTM to be stronger in language tasks, a single ablation row comparing sLSTM to mLSTM within this architecture is the minimum needed to validate this design choice empirically.

- **Lookback length and hidden dimension claims are demonstrated on one dataset each**: The claim that "larger hidden dimensions consistently enhance performance" (Figure 3) is demonstrated only on Electricity. The lookback robustness claim (Figure 4) is shown only on ETTm1. Generalizing these findings from a single dataset each is overstated; the presentation should be more qualified.

### Trivial
None that survive filtering.

---

## Nice-to-Haves

- Bidirectional/multi-order variate traversal (analogous to BiLSTM) as an alternative "two views" mechanism would provide a cleaner theoretical basis and simultaneously test variate ordering sensitivity.
- A correlation or probing analysis of what the sLSTM hidden state retains across variate tokens would directly support the claim of cross-variate interaction through recurrent state propagation.
- Reporting variance on the main comparison table (Table 1) would help contextualize the significance of 2–4.6% MAE improvements that are currently given as point estimates.
- A brief analysis of *why* Traffic and ETTh2 are challenging for this model (e.g., high variate count for Traffic, outlier structure for ETTh2) would bound the model's applicability and guide future work.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"Novelty relative to iTransformer + sLSTM substitution" (Harsh Critic)**: The criticism that the paper should include a baseline directly substituting attention in iTransformer with sLSTM is a reasonable suggestion for ablation but does not undermine the paper's contributions. The full pipeline (NLinear initialization + soft prompt token + multi-view mixing) is the contribution, not just the backbone swap. Moved to nice-to-have territory and partially addressed in the ablation study already.

- **"Improvements are small and within run-to-run noise" (Harsh Critic)**: Without variance in Table 1, this is a plausible concern, but standard practice in this community is single-run evaluation. The 4.6% MAE improvement over TimeMixer on Weather and the consistent pattern of wins (22/28 MAE) across diverse datasets make variance noise an unlikely full explanation. Moved to nice-to-have (reporting variance in main table).

- **"Win-count framing obscures competitive baselines" (Harsh Critic)**: The paper explicitly calls out iTransformer and TimeMixer as competitive and acknowledges the Traffic/ETTh2 failures. The win-count framing is acknowledged to be imperfect, but this is a presentation preference, not a substantive error.

- **Variate ordering sensitivity discussion**: The paper explicitly acknowledges this limitation (Section 3.2: "While this is empirically not a significant limitation, we leave investigations into how to find a suitable ordering for future work.") This is a scoped limitation statement, not an evasion.

---

## Novel Insights

The paper surfaces a concrete and underexplored issue: the soft-prompt initialization token (η) in the sLSTM—visualized in Figure 2—learns dataset-specific and horizon-dependent patterns that serve as a "dataset fingerprint" conditioning the recurrent dynamics before any variate token is processed. This is a notable architectural insight with potential applicability to other sequential models applied to time series: rather than random or zero initialization of the recurrent state, a learned dataset-conditional initialization is both low-cost and interpretable. The observation that this token reveals seasonal structure at longer horizons is non-trivial and deserves further investigation. The dimension-reversal multi-view idea, while mechanistically underspecified, also points toward a more general principle of input perturbation as regularization in recurrent forecasting models—an underexplored direction compared to dropout-based alternatives.

---

## Score and Decision

**Evaluation on key axes:**
- *Originality*: Moderate. Core computational kernel (variate-as-token sLSTM processing) adapts iTransformer's tokenization; NLinear initialization is from prior work. The soft-prompt token and multi-view mixing are novel but the latter is mechanistically underspecified.
- *Importance of research question*: High. Long-term multivariate forecasting with efficient recurrent models is timely and practically relevant.
- *Claim support*: Good overall, but the missing Mamba baselines and unvalidated multi-view mechanism are real gaps.
- *Soundness of experiments*: Generally sound, with the ablation limitation to 2/8 datasets as the main gap.
- *Clarity of writing*: Good; the architecture description is clear and the failure cases are honestly acknowledged.
- *Value to community*: Real: provides a well-documented, reproducible, state-of-the-art recurrent baseline with thorough analysis. The paper improves on xLSTMTime substantially and provides a foundation for future recurrent forecasting work.

**Anchor comparison:**

| Path | Avg Human Score | Comparison |
|------|----------------|------------|
| `/deepreview_13k_calibration/7oLshfEIC2.md` (TimeMixer) | 5.67 (Accept) | Very similar scope: empirical forecasting method with MLP mixing, similar benchmark coverage and novelty level. xLSTM-Mixer has a more detailed ablation but a weaker core mechanistic justification. |
| `/deepreview_13k_calibration/Te5v4EcFGL.md` (PatchMixer) | 6.00 (Reject) | Similar empirical approach; PatchMixer was rejected despite strong results, partly on clarity and motivation. xLSTM-Mixer has more thorough analysis but missing Mamba baselines. |
| `/deepreview_13k_calibration/1CLzLXSFNn.md` (TimeMixer++) | 8.00 (Accept) | Stronger: broader task coverage (forecasting + classification + imputation), more novel multi-scale framework. xLSTM-Mixer is more narrowly scoped. |
| `/deepreview_13k_calibration/nclyFUZpX9.md` (Poly-Mamba) | 4.00 (Reject) | Weaker: fundamental ad hoc design choices, poor presentation, smaller improvements. xLSTM-Mixer is clearly stronger. |
| `/deepreview_13k_calibration/lmShn57DRD.md` (GRformer) | 4.00 (Reject) | Weaker: shallower analysis, less thorough evaluation. xLSTM-Mixer clearly outclasses this. |
| `/deepreview_13k_calibration/oANkBaVci5.md` (Simple Baseline MTSF) | 6.75 (Accept) | Stronger novelty framing (LLM-based, different contribution type). xLSTM-Mixer is more experimentally thorough. |
| `/deepreview_13k_calibration/KMCJXjlDDr.md` (Timer-XL) | 5.67 (Accept) | Comparable: strong empirical paper on time series with thorough evaluation. xLSTM-Mixer is similar in quality and scope. |
| `/deepreview_13k_calibration/RDLvnUJ5JZ.md` (TF-score) | 3.00 (Reject) | Much weaker: minimal evaluation, insufficient theoretical grounding. Not comparable. |
| `/deepreview_13k_calibration/2wwPG1wpsu.md` (LST-Bench) | 2.50 (Reject) | Much weaker benchmark paper with no methodological contribution. Not comparable. |

The paper is most comparable to TimeMixer (5.67, accepted) and Timer-XL (5.67, accepted) in terms of scope, novelty, and experimental rigor. The missing Mamba baselines are a more pointed gap than most weaknesses in those papers, but the ablation and analysis are notably more thorough than average for the field. Anchoring against the 5.5–6.0 range, accounting for the major gap in SSM baselines (which is compounded by the paper's own framing), a score of **5.5** is appropriate—this is a real but incremental empirical contribution at the borderline of acceptance.

**Score: 5.5**
**Decision: Accept (borderline)**

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>