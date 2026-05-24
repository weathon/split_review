Now I have all the information needed to produce the final consolidated review.

## Summary

This paper identifies a "self-stimulation" problem in time series forecasting — models use only historical values, ignoring external influences that drive real-world systems. The authors formalize this through a control-theoretic framework showing an irreducible error floor when influences are ignored. They introduce the IATSF paradigm (conditioning on textual influence descriptions), a leak-free temporally-synced benchmark across four domains, and FIATS — a lightweight LLM-free model that uses cross-attention with channel-specific queries (CASM) to fuse textual influence information. Experiments show FIATS substantially outperforms standard TSF baselines (36–44% MSE reduction) and large pretrained foundation models.

## Strengths

- **Core paradigm validated by strong empirical evidence.** On the FM Toy (where the theoretical error bound is zero), FIATS achieves near-zero error (MSE 0.003) while even billion-parameter foundation models produce errors 4–100× larger. On real-world systems (Atmospheric Physics, NYC Traffic, GAUD), FIATS consistently and substantially outperforms all baselines, including pretrained models like Chronos-L and MOIRAI-L. These results convincingly demonstrate that providing external textual influence information yields large gains over self-stimulated approaches. (Table 1, Sec. 6.1–6.3)

- **Ablation isolates the source of gains.** Removing influence inputs entirely ("Zero News") degrades performance by ~37% (e.g., MSE 0.182 → 0.249 at pred. len 96 on Atmospheric Physics). Removing channel descriptions ("Zero Desc.") also significantly degrades performance (0.182 → 0.209), providing evidence that the channel-specific CASM design contributes beyond simply having extra input features. (Table 3, Sec. 6.4)

- **Leak-free benchmark is a genuine community resource.** The Temporal-Synced IATSF benchmark explicitly enforces temporal alignment and independence of influences from system state. The inclusion of weather forecasts (as predictions, not observations), game developer logs, and clear criteria for what constitutes a valid influence addresses documented weaknesses in prior multimodal forecasting datasets. (Sec. 4)

- **Interpretability via CASM attention maps.** The attention weights in the CASM module reveal channel-specific sensitivity to influence sentences (e.g., the pressure channel attending to "Pressure" text in later layers), providing transparency beyond black-box baselines and aligning with the control-theoretic motivation. (Figures 3, 5, Sec. 6.4)

## Weaknesses

### Fatal

None.

### Major

- **Missing controlled comparison against a simpler fusion baseline that receives the same textual inputs.** The headline comparisons pit FIATS (with textual influences) against standard TSF baselines (without influences). While this supports the paradigm-level claim (influence-aware > self-stimulated), it does not distinguish whether the gains come from the *additional input information* or from the CASM/CAPS *architecture* specifically. A baseline using the same text embeddings with a trivial fusion method (e.g., concatenation + linear/MLP projection into the time series encoder) would isolate the architectural contribution. The "Zero Desc." ablation partly addresses this, but a direct architecture comparison is needed to fully substantiate claims that "architectural analyses (RQ4) attribute these gains to our principled design choices — CASM and CAPS — not model scale." (Sec. 5, Sec. 6.4)

### Minor

- **Theoretical "barrier" is pedagogically useful but technically basic.** Propositions 2.1 and 3.1 restate that (a) the MSE-optimal prediction of X_f given X_h is E[X_f | X_h], and (b) conditioning on more information reduces variance. The control-theoretic framing provides useful motivation for a TSF audience, but presenting these as novel "barriers" or "proofs" overstates the technical contribution. The error-bound in Eq. (3) for nonlinear systems also uses a first-order (linearized) expansion (∇_U F), which is an approximation rather than a rigorous bound without additional assumptions on F. (Sec. 2.2, Sec. 3.1)

- **Overstated language on the FM Toy results.** The paper claims "all self-stimulated models... fail spectacularly" on the FM Toy dataset. At the shortest horizon (pred. len 14), PatchTST achieves MSE 0.006 versus FIATS's 0.003 — both very small numbers. The gap widens substantially at longer horizons (0.168 vs 0.027 at len 120), making the claim fair for longer horizons but exaggerated for the shortest one. (Sec. 6.1, Table 1)

- **Noise robustness experiment lacks a comparative baseline.** Figure 6 shows FIATS degrades gracefully under influence noise, but without a baseline model that also receives the same noisy text inputs, it is unclear whether this robustness is specific to FIATS or would hold for any model using those inputs. (Sec. 6.4, Figure 6)

### Trivial

None.

## Nice-to-Haves

- Compare FIATS against a simple fusion baseline (concatenate text embeddings per channel + linear/MLP decoder) to isolate the architectural contribution of CASM.
- Report parameter counts and inference time to quantitatively support the "lightweight" claim.
- Add failure case analysis showing how the model behaves when influence inputs are misleading or absent (partially present in Figure 3's "missed second rainfall event" but not systematically analyzed).

## Removed Points

These points are flagged to be removed, treat them with caution:
1. **FIITS not defined** — The column appears in Table 1 but is undefined in the main text. The paper's appendices (which would define it, along with other implementation details) were stripped by the PDF parser. Per policy, missing-appendix criticisms are not valid against the original submission.  
2. **Look-ahead bias** — The paper explicitly states it uses weather *forecasts* (not observed future weather) as influences (Sec. 4.1: "Predictions of U_f from expert sources (e.g., weather reports)") and refers to Appendix B.3 for evaluation strategies. Since the appendix was stripped by the parser, this criticism is not actionable from the main text alone.  
3. **"Expert knowledge integration" not tested** — The paper lists this as a general advantage of textual modalities (Sec. 3.2), not as a specific empirical claim requiring dedicated experiments. This is a scope-creep criticism.  
4. **Unfair comparison invalidates results** (framed as fatal) — The comparison against self-stimulated baselines *is* the correct experimental design for the paradigm-level claim. The critic's framing that this "invalidates" results is incorrect; the issue is better characterized as a missing architecture-level control (handled in Major above).

## Novel Insights

The harsh critic's identification of the missing simple-fusion baseline interacts interestingly with the Strength Finder's praise of the ablation study: the "Zero Desc." ablation (removing channel descriptions) shows a performance drop, which *partially* addresses the concern, but the paper could have been strengthened by directly comparing CASM to a simpler fusion mechanism rather than requiring readers to infer the comparison from an ablation. This tension — between the paradigm claim (well-supported) and the architecture claim (partially supported) — runs through the entire evaluation and suggests the paper's strongest contribution is the *idea* of IATSF and the benchmark, rather than the specific FIATS architecture.

## Suggestions

1. Add a baseline that receives the same textual influence embeddings but uses a simpler fusion mechanism (e.g., concatenate text embeddings per channel and project through a linear layer into the decoder). This would cleanly separate the value of the IATSF paradigm from the value of the CASM architecture.
2. Tone down the characterization of the theoretical propositions as novel "barriers" — acknowledge they are standard conditional-expectation properties, and instead emphasize the value of applying this lens specifically to TSF.
3. Add a comparative baseline to the noise-robustness experiment (e.g., the simple fusion baseline described above) to show whether FIATS is specially robust or the robustness is generic to influence-conditioned models.
4. Report model size, FLOPs, or inference time to support the "lightweight / LLM-free" efficiency claim.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>