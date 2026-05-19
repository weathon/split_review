Now I have a comprehensive understanding of the paper. Let me produce the final consolidated review.

## Summary

X-PlugVid proposes a unified framework to adapt pretrained image-based spatial-control plugins (e.g., ControlNet, T2I-Adapter) to video diffusion models without per-plugin retraining. The method introduces a spatial-temporal adapter to bridge the domain and modality gaps, a high-pass filter on adapter inputs to eliminate low-quality/low-frequency components from the diffusion prior, and a timestep remapping strategy that injects richer features from later image-model denoising steps into earlier video-model steps. Extensive experiments on I2VGen-XL and Hotshot-XL show compatibility with multiple plugin types and improved FID/optical flow error over prior controllable video generation methods.

## Strengths

- **Timestep remapping strategy is well-motivated and ablated convincingly.** The paper identifies (via PCA-based denoising trajectory visualization in Fig. 6 and frequency analysis in Fig. 3) that early-step features from the image model contain insufficient information for guidance. The remapping function (Eq. 2, Fig. 5) addresses this by mapping later image-model timesteps to earlier video-model timesteps. The ablation in Table 2 and Fig. 8 systematically studies n=1,2,4,1000 and demonstrates that n=2 substantially outperforms synchronous timesteps (n=1), while also showing that excessively strong guidance (n=1000) degrades quality. The visual comparison of adapter outputs with/without remapping (Fig. 9) provides direct evidence that the remapping produces sharper, more temporally consistent guidance features.

- **High-pass filtering is grounded in a principled analysis and validated.** The paper analyzes the frequency characteristics of ControlNet outputs vs. diffusion model feature maps (Fig. 3), finding that ControlNet produces predominantly high-frequency patterns at every timestep while the diffusion prior contains low-frequency, low-quality components. The high-pass filter (Eq. 1) is directly motivated by this finding. Ablation results (Table 2, "High-pass filter only" vs. "No filter & no remapping") show measurable improvements in FID and optical flow error, supporting the claim that filtering low-quality components benefits both quality and consistency.

- **First unified framework enabling image-to-video plugin transfer without per-plugin retraining.** This is a genuine contribution: whereas prior work (ControlVideo, Control-A-Video) requires per-plugin training or per-model adaptation, X-PlugVid trains a single adapter that works with all spatial-control plugins (ControlNet, T2I-Adapter) and multiple video backbones (I2VGen-XL, Hotshot-XL, SVD). Table 1 shows competitive quantitative results against prior methods on the Panda70M validation set, and qualitative results (Fig. 7) demonstrate the breadth of compatibility.

- **Mechanistic analysis of ControlNet and X-Adapter provides a clear foundation.** The visualizations in Fig. 2 and Fig. 3 go beyond simply proposing a method, offering insight into why ControlNet works (high-frequency pattern injection at every timestep) and why X-Adapter's synchronous timestep mapping is suboptimal (early-step features are too weak). This analysis is presented as a self-contained motivation for the paper's design choices.

## Weaknesses

### Major

- **Metrics do not directly measure the paper's primary claim of controllability.** The paper uses FID (distributional distance) and optical flow error (motion consistency between generated and reference videos). Neither metric directly quantifies how faithfully the generated video adheres to the spatial condition (e.g., depth map or canny edges). The paper frames optical flow error as a "spatial control" metric (line 169), but optical flow measures frame-to-frame motion, not spatial condition fidelity. Standard practice in the controllable generation literature includes task-specific metrics such as depth RMSE (for depth conditions) or edge F1 / Chamfer distance (for edge conditions). Without these, the quantitative superiority claim in Table 1 is weakened — improvements in FID and flow error could arise from factors unrelated to condition adherence (e.g., better overall video quality from a different backbone). The qualitative results (Fig. 7) mitigate this concern but do not fully replace direct quantitative measures of control.

- **Baseline comparison setup is underspecified.** The paper reports comparisons against ControlVideo, Control-A-Video, and VideoComposer on the Panda70M validation set, but does not state: (1) which base video backbone each baseline method uses, (2) whether these baselines were retrained on Panda70M data or used off-the-shelf with their original weights, and (3) whether the conditioning inputs (depth maps, canny edges) were computed using the identical preprocessing pipeline across all methods. These details are necessary to assess whether the reported margins (e.g., FID 22.3 vs. 27.8) reflect a genuine advantage of X-PlugVid or differences in backbone quality, data overlap, or preprocessing. The comparison as presented is insufficiently controlled.

### Minor

- **Temporal attention module is underspecified.** The paper states only that a "temporal attention (Vaswani et al., 2017) module" is added to ensure temporal coherence (line 93). It does not specify the type of attention (self-attention over frames? cross-attention with a reference frame?), number of heads, feature dimensions, or where precisely in the adapter architecture the temporal modules are inserted relative to the mapping layers. Reproducibility would benefit from additional detail.

- **Generalization claim in Section 5.1 lacks evidence.** The paper states: "we implement timestep remapping and high-pass filter upon X-Adapter and achieve better results" (line 253) — but provides no quantitative results, ablation, or even qualitative example to support this. This claim about transferability to the image-to-image setting is presented as a demonstration of generality but is not backed by any experimental data in the paper.

- **No training convergence or validation analysis.** Training is done on a 100K-pair subset of Panda70M for 5 epochs with batch size 8. The paper does not discuss whether 5 epochs is sufficient for convergence, nor does it analyze whether the adapter generalizes beyond this fixed training subset.

### Trivial

- None. (The paper is generally well-written and no trivial formatting/issues warrant mentioning.)

## Nice-to-Haves

- A human evaluation (e.g., preference study on condition fidelity and video quality) would strengthen the controllability claims, since automated metrics for generation quality are known to be imperfect.
- Failure case analysis: the paper shows only successful generations. Examples where the condition is conflicting, extremely detailed, or involves large motion would help characterize the method's limitations.

## Removed Points

- Harsh critic's claim that "the paper does not justify why the image model must run alone during the first stage" — REMOVED. The paper explains (line 135) that the two-stage inference aligns with the remapping strategy: at inference start, the video model is at timestep T while the image model's remapped timestep is T/n; the image model runs alone from T to T/n to produce the richer features that remapping requires. This is adequately justified.
- Harsh critic's claim that "the claim 'previous works overlook this point' is vague" — REMOVED. The paper specifically identifies X-Adapter as the work that overlooks high-frequency injection at every timestep (line 86: "one important aspect X-Adapter overlooks").
- Harsh critic's speculations about VideoComposer being "not optimized for single-condition" and Control-A-Video having "advantage or disadvantage depending on data overlap" — REMOVED as speculative assertions without evidence in the paper.
- Harsh critic's question about "whether the same conditioning inputs were extracted from the Panda70M videos at test time" — PARTIALLY RETAINED. The broader concern about underspecified baseline setup is retained (Major weakness 2), but the specific speculation about different preprocessing lacking evidence is removed from the severity it was given.
- Strength Finder's strength about SOTA — RETAINED as stated, since Table 1 does show numerical improvements, but the metric concern (Major weakness 1) qualifies this strength and the reader should weigh both.
- Strength Finder's claim about "supporting strengths" of mechanistic analysis — RETAINED as a genuine supporting strength since it is concrete and specific to the paper.

## Novel Insights

The harsh critic and strength finder together surface an important tension: the paper's core methodological contribution (timestep remapping, high-pass filtering, spatial-temporal adapter) is well-motivated by mechanistic analysis and well-validated by ablation, but the evaluation against prior work relies on metrics that do not directly measure the central claim of condition adherence. This suggests a pattern in the controllable generation literature where task-specific control metrics (depth error, edge F1) are underused in favor of generic quality metrics, leaving a gap between methodological contributions and their measured evidence. The paper would benefit from adopting the controllability metrics that are standard in the conditioning literature from which it draws inspiration (e.g., ControlNet evaluations report depth RMSE).

## Suggestions

1. Add direct controllability metrics: depth RMSE (using a pretrained depth estimator) for depth-conditioned generation and edge F1 or Chamfer distance for edge-conditioned generation. Re-run the comparison in Table 1 with these metrics.
2. Clarify the baseline comparison: specify the exact backbone used for each baseline, whether baselines were retrained or used off-the-shelf, and how the conditioning inputs were preprocessed (same pipeline for all methods).
3. Provide architectural details for the temporal attention module (self-attention vs. cross-attention, number of heads, feature dimensions, insertion points).
4. Either provide quantitative results for the X-Adapter generalization claim (Section 5.1) or remove the claim as unsupported.
5. Add error bars or confidence intervals to Table 2 to assess the reliability of the ablation comparisons.

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>