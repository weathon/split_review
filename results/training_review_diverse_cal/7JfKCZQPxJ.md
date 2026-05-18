Now I have a thorough understanding of the paper and all reviewer claims. Let me produce the consolidated review.

## Summary

This paper proposes STREAM (Spatio-TempoRal Evaluation and Analysis Metric), a new evaluation framework for video generative models that independently assesses spatial quality (fidelity via STREAM-F and diversity via STREAM-D) and temporal naturalness (STREAM-T). STREAM-T analyzes temporal dynamics by computing FFT on per-frame DINO features, fitting power-law distributions, measuring skewness per feature dimension, and computing histogram correlation between real and generated videos. STREAM-S computes the mean frame feature (zero-frequency FFT component) and applies k-NN based precision/recall. The method overcomes FVD's 16-frame limit by operating on per-frame image embeddings, and provides bounded [0,1] scores. The paper validates STREAM on synthetic CATER data, real UCF-101/Kinetics-600 with controlled distortions, and on actual generative models, reporting Spearman correlations of 0.9 (realism) and 0.6 (temporal naturalness) with human judgment.

## Strengths

- **First metric enabling separate assessment of spatial and temporal video quality**: STREAM provides three interpretable sub-scores (STREAM-T for temporal flow, STREAM-F for fidelity, STREAM-D for diversity), while FVD collapses everything into a single opaque number. This is demonstrated concretely in Table 1, where TATS has mediocre FVD (693.27) but high STREAM-T (0.9832) and STREAM-F (0.9120)—insights a single FVD score cannot provide (§4.2.2).

- **Empirical grounding through controlled experiments**: The paper systematically validates that STREAM-T responds to temporal distortions (frame swaps, random translation, stop scenes) while remaining invariant to spatial noise (luminance, color jitter, gaussian noise), and vice versa for STREAM-S. These behaviors are demonstrated on both synthetic CATER data (Figures 2-4) and real UCF-101/Kinetics-600 (Figures 5-6), with consistent results (§4.1, §4.2.1).

- **Operates on arbitrary video lengths**: By using per-frame image embeddings, STREAM handles videos of any length without constraint. Table 2 evaluates 128-frame videos where FVD cannot be directly applied (requiring sliding-window approximation sFVD), and STREAM reveals dramatic declines in temporal quality with increasing video length (e.g., TATS drops from STREAM-T=0.9832 at 16 frames to 0.0302 at 128 frames) (§4.2.3).

- **Quantitative human correlation as external validation**: The paper reports Spearman correlations of 0.9 for realism and 0.6 for temporal coherence with human judgment, with FVD showing weaker correlation for both aspects (§4.2.2). This provides evidence that STREAM's rankings align with human perception beyond synthetic experiments.

- **Bounded, interpretable scores**: All STREAM sub-metrics produce values in [0,1], enabling direct comparison and clear interpretation, unlike FVD which is unbounded and only permits relative assessment (§1 contribution (2), Tables 1-2).

## Weaknesses

### Fatal

None.

### Major

None. The weaknesses below are meaningful but do not invalidate the paper's core claims.

### Minor

- **Limited theoretical and empirical justification for the skewness-based design of STREAM-T**: The paper builds a multi-stage pipeline (FFT → power-law fitting → skewness computation → histogram correlation) but does not empirically validate the power-law assumption on real video data, nor does it justify why skewness of the fitted distribution is the right statistic rather than simpler or alternative choices (the power-law exponent α directly, the cumulative spectrum, or some distance between raw spectra). The paper explains why skewness is preferred over mean/variance (to avoid low-frequency dominance, §3.3), but does not compare against the exponent α or whole-spectrum distances. Given that the temporal metric's Spearman correlation with human judgment is a moderate 0.6—and that this correlation is the primary evidence for STREAM-T's validity—the lack of deeper investigation into why this particular feature (and not alternatives) captures temporal naturalness leaves the design insufficiently justified. This is the paper's most significant gap.

- **STREAM-S discards frame-level spatial detail**: By taking the mean of all frame features (zero-frequency FFT component) and applying precision/recall on these video-level vectors, STREAM-S loses all frame-level variation. A video with one sharp frame and many blurry frames yields the same mean as one where all frames are moderately sharp. The paper acknowledges the practical necessity (per-frame P&R suffers from "small spheres" problem, §3.4) but does not validate what information is lost against per-frame baselines (e.g., averaged per-frame FID or LPIPS). This limitation should be explicitly discussed rather than implied.

- **Saturation of STREAM-T for short videos**: On 16-frame UCF-101 generation, all models achieve STREAM-T scores between 0.9616 and 0.9843—extremely tight clustering (Table 1). While these correlate with human judgment (0.6), the paper does not calibrate whether such small numerical differences are operationally useful for model comparison or diagnosis. The long-video results (0.03–0.83 spread in Table 2) are clearly more informative, so the metric's value is context-dependent. The paper should discuss this saturation regime explicitly.

- **No ablation on embedding network choice**: The paper uses DINO as the image encoder and provides a qualitative justification for avoiding video-specific embeddings (§3.2). However, no ablation compares DINO against alternative image embeddings (e.g., CLIP, supervised ResNet) to test whether STREAM's findings are robust to the embedding choice.

- **No k-NN sensitivity analysis for STREAM-S**: The k-NN parameter for precision/recall is set to k=5 with no justification or ablation (§3.4). The original improved precision/recall paper notes sensitivity to this parameter, making an ablation necessary.

- **Algorithm 1 pseudocode is ambiguous**: The input declaration says "real feature X, fake feature Y" (singular), but the loop iterates over datasets 𝒳 and 𝒴. The output construction of γ_𝒳 from {γ_X; for all X∈𝒳} confirms X is an individual video, but the input specification and loop semantics need clarification.

- **Computational cost not discussed**: STREAM requires a per-frame DINO forward pass (one per frame), while FVD uses a single I3D forward on a 16-frame clip. For long videos, STREAM becomes proportionally more expensive. A note on runtime or scalability would be helpful.

### Trivial

- Contribution (1) in §1 states "STREAM is the first evaluation metric that can separately assess the temporal and spatial aspects of videos" without the qualifier "to the best of our knowledge" that appears in the abstract (§1). Minor inconsistency.

- No explicit discussion of failure cases or temporal artifact types where STREAM-T may not degrade as expected (beyond translation, swapping, and stop scenes tested).

## Nice-to-Haves

- **Deeper theoretical analysis**: Validate empirically that the power-law assumption holds on real video data, and compare skewness against alternative statistics (power-law exponent α, cumulative spectrum distance) on the same controlled-distortion experiments to justify the design choice.
- **Validation of STREAM-S against per-frame baselines**: Compare STREAM-S rankings with averaged per-frame metrics (e.g., frame-wise FID or LPIPS averaged over frames) to quantify what the averaging loses.
- **Analysis of saturation**: Demonstrate that even the small STREAM-T differences for short videos are statistically consistent and meaningful, perhaps through bootstrapped significance tests or a calibrated interpretation guide (e.g., "STREAM-T > 0.97 indicates strong temporal coherence").
- **Code release** to facilitate adoption and reproducibility.

## Removed Points

These points from the reviewers were evaluated against the paper and removed for the following reasons:

1. **"Human study details are in the appendix; we must trust its execution"** — The rules require removing weaknesses about missing appendix content; the appendix is stripped by the parser and exists in the original submission.
2. **"0.9 correlation for realism is surprisingly high and raises questions about study control"** — Speculation without evidence; the paper reports the number and refers to the appendix for details.
3. **"Related work does not discuss per-frame FID/LPIPS"** — Scope creep; the paper focuses on video-level metrics, not per-frame image metrics that are non-standard for video generation evaluation.
4. **"Code not mentioned"** — While reasonable as a suggestion, the rules deprioritize reproducibility nitpicks; moved to Nice-to-Haves.
5. **Criticism that "the paper should also cover Y/domain Z/additional tasks" (implicit in some demands)** — These would broaden the paper beyond its stated scope.
6. **"Missing failure-case analysis"** — While kept as trivial, the reviewer's framing as a major gap is disproportionate; the paper tests three distinct temporal distortions, which is standard coverage for a benchmark paper.

## Novel Insights

The most interesting observation emerging from the reviews is the tension between STREAM's key strength and its key weakness: the spatial/temporal decomposition that makes STREAM valuable also introduces methodological trade-offs that are not fully resolved. The temporal metric (STREAM-T) achieves clean separation from spatial factors in controlled experiments, but its moderate human correlation (0.6) and the multi-step design (FFT → power-law → skewness → histogram correlation) raise the question of whether a simpler spectral statistic might work as well or better. Meanwhile, the spatial metric (STREAM-S) achieves the desired decomposition by collapsing frames to their mean, but this very collapse sacrifices frame-level spatial detail that simpler alternatives (averaged per-frame FID) would retain—albeit without the clean spatial/temporal separation. The paper has not yet validated which of these trade-offs is more consequential in practice, leaving room for follow-up work to benchmark STREAM-S directly against frame-averaged spatial metrics or to simplify STREAM-T's pipeline.

## Suggestions

1. Add an empirical validation of the power-law assumption on real video data (e.g., plot fitted power-law lines against empirical amplitude spectra for sample videos from UCF-101/Kinetics).
2. Add an ablation comparing STREAM-T's skewness against using the power-law exponent α directly, or a distance between raw amplitude spectra, on the existing controlled-distortion experiments.
3. Add an ablation comparing DINO against at least one alternative image embedding (e.g., CLIP or supervised ResNet) on the model ranking experiment (Table 1).
4. Add a k-NN sensitivity analysis (k=3,5,7,10) for STREAM-F and STREAM-D on one benchmark configuration.
5. Clarify Algorithm 1's input specification and loop semantics.
6. Include a brief limitations paragraph explicitly discussing the mean-frame averaging trade-off and the saturation regime for short videos.
7. Add a note on computational cost (e.g., time per video vs. FVD).

## Score and Decision

- **Originality**: 4/5 — The idea of separate spatial/temporal evaluation for video is novel and timely; the specific methodology (FFT on per-frame embeddings, power-law skewness comparison) is a creative design.
- **Importance**: 4/5 — Video generation evaluation is an important open problem; the limitations of FVD are widely recognized and STREAM addresses a real need.
- **Claims support**: 3/5 — The core claims are supported but the temporal metric's validation has gaps (moderate human correlation, unvalidated design choices, saturation for short videos).
- **Soundness**: 3/5 — Experimental design is generally solid with controlled toy experiments, real-data validation, and human study; however, missing ablations (embedding choice, k-NN sensitivity) weaken the methodological rigor.
- **Clarity**: 4/5 — Well-structured and clearly written; Algorithm 1 has minor ambiguity.
- **Value**: 4/5 — The metric is likely useful as a diagnostic tool, especially for longer videos; the decomposition into spatial/temporal/diversity components is genuinely informative.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>