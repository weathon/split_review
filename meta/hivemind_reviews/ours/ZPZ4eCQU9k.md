## Summary
This paper proposes xLSTM-Mixer, a multivariate time series forecasting architecture that combines a per-variate linear forecast (NLinear) with a stack of sLSTM blocks that process variates as sequence elements, plus a multi-view mixing strategy that reverses the embedding dimensions to produce two forecasts that are reconciled. On standard long-term forecasting benchmarks (Weather, Electricity, Traffic, ETT), the model achieves best results in 18/28 MSE and 22/28 MAE settings, outperforming Transformer, MLP, and recurrent baselines.

---

## Strengths
1. **Strong and consistent empirical results.** Table 1 shows xLSTM-Mixer achieves best MSE in 18 out of 28 settings and best MAE in 22 out of 28 settings across four datasets, outperforming xLSTMTime, TimeMixer, PatchTST, iTransformer, and others. The improvements are particularly notable on Weather and ETTm1 datasets.

2. **Comprehensive ablation study.** Table 3 systematically evaluates eight configurations (all combinations of NLinear time mixing, sLSTM blocks, initial embedding token, and multi-view mixing) across two datasets and four horizons. The study confirms that all components contribute positively, and removing time mixing (#7) degrades MAE by 3.4% on ETTm1 at horizon 96.

3. **Novel architectural design.** Combining an NLinear temporal forecast with sLSTM blocks that stride over variates (rather than time) is a sensible and well-motivated design choice. The weight-sharing across variates in the linear stages provides regularization, and the use of only sLSTM (not mLSTM) is justified by the need for cross-variate interaction.

4. **Qualitative analysis of learned initial tokens.** Figure 3 decodes the learnable soft-prompt tokens and shows they capture dataset-specific seasonal patterns, providing evidence that the initialization mechanism learns meaningful conditioning beyond a learned bias.

5. **Robustness and sensitivity analysis.** The paper systematically examines sensitivity to hidden dimension (Figure 4) and lookback length (Figure 5), showing that the model scales well with both and maintains low variance.

---

## Weaknesses
### Fatal
None.

### Major
None. The weaknesses below are addressable in revision and do not invalidate the paper's core contributions.

### Minor

1. **Central claim about marching direction is not directly tested.** Contribution (i)—"marching over the variates instead of the temporal axis yields better results"—is asserted but never directly verified. All ablation configurations process variates as tokens (with or without NLinear time mixing); there is no comparison against an sLSTM-over-time variant (where tokens are all variates at a single time step). A direct ablation comparing sLSTM-over-variates vs. sLSTM-over-time (with matched capacity) would substantiate this claim.

2. **Multi-view mixing lacks sufficient justification.** The paper describes reversing the order of latent dimensions within each variate's embedding (Section 3.3) and attributes the benefit to "multi-task learning." However, no intuition is provided for why dimension reversal in particular is helpful, nor does the ablation test alternative views (e.g., reversing variate order, random permutation, dropping one view). The component contributes empirically (configurations #2, #4, #6 degrade when removed), but its design rationale is underspecified.

3. **"Joint time-variate mixing" language overstates the sLSTM's role.** The paper repeatedly states that the sLSTM blocks "jointly mix time and variate information" (lines 42, 125, 156–157). In practice, temporal mixing is handled primarily by the NLinear forecast and up-projection, while the sLSTM processes variates as tokens containing time-encoded information. This separation is a design feature, not a flaw, but the framing should be more precise: time and variate mixing are *sequential* (linear→sLSTM), not *joint* within the recurrent block.

4. **Computational cost not reported.** Despite citing efficiency as a motivation for avoiding Transformers (lines 31–32), the paper does not report parameter counts, training time, or inference speed for any model. This makes the efficiency claims unverifiable and limits practical guidance for practitioners.

### Trivial

- The lookback length used in the main experiments (Table 1) is not stated explicitly, only implied by "We generally follow the established benchmark procedure" (line 212). While this convention is standard in the field (lookback=96), the paper should state it explicitly for completeness.

---

## Suggestions
1. **Add a marching-direction ablation.** Compare the current design (sLSTM over variates) against a variant where the sLSTM processes time steps as tokens (all variates at each time step), matched for parameter count. This directly tests your central architectural claim.

2. **Provide intuition for multi-view mixing.** Explain why reversing the *dimension order* within tokens is expected to help—e.g., does it assign each sLSTM head a different dimensional grouping? Does it break a positional bias in the block-diagonal recurrence? The current "multi-task learning" framing is too generic.

3. **Correct the "joint mixing" language.** Clearly state that time mixing (NLinear + up-projection) and variate mixing (sLSTM) are *sequential* stages, and that the architecture's innovation is their combination, not a unified recurrent operator.

4. **Explicitly state the lookback length** used in the main experiments in the main text (not deferred to appendix).

5. **Report parameter counts** and, if possible, training/inference time to support efficiency claims.

---

## Score and Decision

This paper makes a credible contribution: a well-designed recurrent architecture with strong empirical performance and thorough analysis. The weaknesses are real but minor—imprecise language, untested central claim, missing justification for one component—and are addressable in revision. The core results and architectural insights are sound and valuable to the community.

**Originality:** The combination of NLinear + sLSTM over variates + multi-view is novel in the time series forecasting space, building sensibly on xLSTM and MLP-Mixer ideas.

**Importance of research question:** Addressing recurrent-model resurgence and effective mixing strategies is timely.

**Claims well-supported:** Strongly supported by benchmarks; the marching-direction sub-claim is not directly tested.

**Soundness of experiments:** Generally sound; the ablation study is thorough; minor gaps in reporting.

**Clarity:** Good overall; the multi-view description is clear (dimension reversal) but its motivation is not.

**Value to community:** A well-performing, efficient recurrent alternative to Transformers—likely to be useful for practitioners.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>

## Questions


## Decision
Accept
