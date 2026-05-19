- Decision: Accept
- Avg Score: 7.25
- Scores: 8, 8, 5, 8
Now I have a thorough understanding of the paper and all reviewer claims. Let me compose the final consolidated review.

## Summary

NeRM introduces a two-stage generative framework that combines a variational implicit neural representation with latent diffusion models for human motion synthesis. The key innovation is enabling training directly on motion data with varied native framerates (20–250 fps), avoiding the standard preprocessing of downsampling high-fps data and discarding low-fps samples, which allows direct generation of high-framerate motions without interpolation artifacts.

## Strengths

- **Multi-framerate training that preserves native data**: NeRM is trained directly on raw motion sequences with varied framerates (20–250 fps), avoiding downsampling or discarding. This is the paper's central contribution, and it is well-supported by Table 1: native-framerate training achieves FID 0.319 on HumanML3D versus 0.369 for the same model trained on a fixed 20 fps dataset, directly demonstrating the benefit of using raw data.

- **Direct high-framerate generation without interpolation artifacts**: NeRM generates motions at 100 fps directly, whereas prior methods (e.g., MLD) can only upsample their fixed low-framerate outputs. Table 2 reports clip-FID at 100 fps — NeRM achieves 0.057 versus 0.206 for MLD with interpolation — and Figure 4b provides a clear qualitative comparison showing NeRM avoids foot-sliding artifacts.

- **Variational INR + latent diffusion for diverse, conditional generation**: Unlike prior INR-based motion models (e.g., NeMF) which are deterministic or require per-sequence retraining, NeRM treats latent codes as a variational distribution and models their distribution with a diffusion model. Figure 5 shows NeRM achieves substantially better FID (0.308) than NeMF (0.638) on unconditional generation, and Tables 1 and 3 confirm competitive performance across text-to-motion and action-to-motion tasks.

- **New clip-FID metric**: The paper introduces clip-FID, a straightforward adaptation of FID to randomly extracted short clips at native framerates, making it sensitive to local artifacts (e.g., foot sliding) that global metrics miss. This is a useful evaluation tool for high-framerate motion quality.

- **Temporal sub-sampling capability**: As shown in Figure 4c, NeRM can generate a pose at any specific time step directly without first generating all intermediate frames — a property not supported by existing discrete-frame models.

## Weaknesses

### Fatal
None.

### Major

- **Unsupported claims about memory and efficiency**: The abstract and conclusion claim NeRM is "memory-friendly" and "highly efficient even when generating high-framerate motions," and the introduction motivates the approach partly on memory grounds ("decouple high-framerate synthesis from prohibitive memory requirements"). However, the paper provides **zero quantitative evidence** — no table, figure, or ablation reports GPU memory consumption, training time, or sampling speed for NeRM or any baseline. The only support is a qualitative argument that INRs avoid memory scaling with resolution (Section 1). This is a notable gap because efficiency is presented as a central selling point rather than a secondary remark. It does not invalidate the core contribution (multi-framerate training and direct high-fps generation) but weakens the credibility of the advertised advantages.

- **Missing ablation of the Codebook-Coordinate Attention (CCA) module**: The CCA module is presented as a key component that "enrich[es] the feature representation" of temporal coordinates (Section 3.1). However, no experiment isolates its contribution. The fixed-framerate variant of NeRM uses the codebook and achieves FID 0.369, but there is no comparison against a version without CCA, so the reader cannot tell whether CCA is essential or marginal. Given that CCA adds architectural complexity, its individual contribution should be quantified.

### Minor

- **Missing ablation of progressive training**: The progressive training schedule (fixed-framerate first, then multi-framerate) is described as important for convergence (Section 3.1) but is not ablated against direct multi-framerate training from scratch. This is a relatively minor gap since the main results do not rest on this choice.

- **No analysis of performance under extreme framerate variation**: The paper demonstrates that using native-framerate data improves aggregate results (Table 1), but does not analyze how the model behaves on the low end (e.g., data < 10 fps) or whether it successfully generalizes to framerates beyond those in the training distribution. A per-framerate-bin breakdown of reconstruction quality would strengthen the "arbitrary-framerate training" claim.

- **No limitations section**: The paper does not discuss cases where the model might struggle (e.g., very long sequences, rare action classes, extreme framerate mismatch). Adding a brief limitations discussion would improve completeness.

- **Unconditional generation results (Figure 5) lack confidence intervals**: Unlike Tables 1 and 3 which report 95% confidence intervals, Figure 5 is a bar chart without error bars or numerical values, making it harder to assess the significance of the reported differences.

### Trivial
None.

## Nice-to-Haves

- Provide memory and speed benchmarks (GPU memory, training/sampling time) at multiple framerates to substantiate the efficiency claims.
- Evaluate clip-FID on the fixed-framerate-trained variant of NeRM to help attribute high-framerate improvements to the representation versus the training data diversity.
- Include a more sophisticated upsampling baseline for high-framerate comparison (e.g., learned temporal interpolation) if feasible, to further validate the margin over interpolation.
- Analyze reconstruction error as a function of native framerate to directly validate the "arbitrary-framerate training" claim.

## Removed Points

These points were flagged in the input reviews but are removed with justification:

- **Criticism that high-framerate evaluation uses a "weak" baseline (interpolation) and clip-FID is not validated**: Other methods cannot generate high-framerate motions directly, so spherical linear interpolation is the standard practical baseline. clip-FID is a straightforward adaptation of the well-established FID metric. This criticism is scope-creepy (suggesting neural upsampling baselines that are separate research problems) and overstates the limitation. The paper handles this appropriately.

- **Missing hyperparameters (m, l_max, N, d) and codebook pretraining details**: These are implementation details that would typically be specified in an appendix or supplementary, which are stripped during parsing. Per policy, nitpicks about undisclosed hyperparameters are not included as weaknesses.

- **Criticism about only one high-framerate qualitative example**: This is a minor presentation preference, not a substantive flaw.

- **"No mention of any work that specifically addresses multi-framerate training"**: The reviewer correctly notes this is because NeRM is the first to do so — not a weakness.

- **Criticism that the codebook motivation feels "underspecified"**: The paper explicitly motivates the codebook as providing prior descriptors for coordinate-based networks when annotated data is limited (Section 1). This is adequately described.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add a single table reporting GPU memory (training/inference) and wall-clock sampling time** at 20, 60, and 100 fps comparing NeRM against MLD or another strong baseline. This would directly substantiate the strongest unsupported claim.
2. **Run an ablation on HumanML3D** removing CCA and/or training without progressive scheduling, reporting FID and clip-FID at conventional framerates. This would validate the design choices.
3. **Add a brief limitations paragraph** discussing scenarios where the model may underperform (e.g., very long sequences, actions with extreme framerate mismatches).
4. **Add error bars or numerical overlays to Figure 5** for consistency with the rest of the paper's presentation.
