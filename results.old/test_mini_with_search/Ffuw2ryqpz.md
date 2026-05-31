Now I have sufficient calibration data. Let me compose the final review.

## Summary

Real3D introduces the first Large Reconstruction Model (LRM) system that can be trained on single-view real-world images, breaking the prior bottleneck of requiring synthetic 3D assets or multi-view video captures. The core technical contributions are: (1) a pixel-level cycle-consistency loss with stop-gradient and curriculum learning on pose range to prevent degeneration; (2) a CLIP-based semantic loss with hard-negative mining to avoid the multi-head problem; and (3) an automatic data curation pipeline for selecting unoccluded instances. The evaluation spans four test sets (MVImageNet, CO3D, OmniObject3D, and an in-the-wild RealData collection) with both NVS metrics where ground truth exists and semantic/self-consistency metrics where it does not. Real3D consistently outperforms strong baselines (including TripoSR and multi-view-trained LRM*) and shows monotonic improvement with more real data.

## Strengths

1. **First demonstration that LRMs can be trained on single-view real images with convincing gains.** The paper is the first to show that self-training on single-view real images improves LRMs, validated across four diverse test sets. On MVImageNet, Real3D achieves 20.53 PSNR on GT novel views vs. TripoSR's 19.81 and LRM*'s 20.16 (Table 1). The gain over TripoSR (Δ=0.72) is larger than what LRM* achieves using multi-view real data (Δ=0.41), directly supporting the claim that single-view real data is both more scalable and more effective.

2. **Well-designed losses with careful regularization that demonstrably prevent trivial solutions.** The paper identifies two failure modes — cycle-consistency degeneration and the CLIP multi-head problem — and proposes specific remedies (stop-gradient + curriculum, hard-negative mining) that are each validated by ablations (Table 2). The degradation to 17.78 PSNR with end-to-end cycle-consistency and 17.89 with naive CLIP loss convincingly shows these design choices are non-trivial.

3. **Thorough evaluation and ablation.** The paper evaluates on four diverse datasets (real/synthetic, in-domain/out-of-domain) with complementary metrics. The ablation table (Table 2) isolates each component — input-view loss, clean data, semantic guidance (with naive vs. proposed variants), cycle-consistency (with e2e vs. stop-gradient), and curriculum — providing clear attribution for each proposed contribution.

4. **Data scaling demonstrated.** The paper shows that performance improves monotonically as more real images are added (Fig. 3), supporting the core thesis that single-view real data offers a viable path for scaling LRMs.

## Weaknesses

### Fatal
None.

### Major

1. **Data curation pipeline is critically underspecified.** The paper claims automatic data curation as a contribution (abstract, Sec. 3.2), yet the entire description is: "we develop an automatic occlusion detection method leveraging the synergy between instance segmentation and single-view depth estimation" — approximately three sentences with no details on which models are used, how depth and segmentation are combined, what thresholds/filters are applied, or what the failure modes of this pipeline are. The ablation shows curation provides a measurable gain (19.18 vs. 18.79 PSNR), but the method as presented is a black box. This is a reproducibility gap for a claimed contribution.

### Minor

2. **Self-consistency metric is plausibly circular.** For the RealData test set (Table 2, right panel), where no ground-truth novel views exist, the paper evaluates "self-consistency": render a novel view, reconstruct it, render back to the original viewpoint, and measure reconstruction fidelity. This metric could be inflated if the model learns to produce renderings that are easy to reconstruct (e.g., blurry or textureless). The paper partially mitigates this by also reporting semantic similarity metrics (CLIP/LPIPS/FID) on the same dataset and, crucially, demonstrating gains on GT metrics for the other three test sets. The issue is not fatal, but the paper would be strengthened by validating on a dataset where both self-consistency and GT NVS metrics are available (e.g., MVImageNet test set) to show they correlate.

3. **No discussion of failure cases or systematic limitations.** The limitations section only mentions constant intrinsics. Missing is any characterization of when the model produces degenerate geometry (flat shapes, missing back-sides, artifacts from the cycle loop). Qualitative examples in Fig. 4 all show successful reconstructions; a systematic failure analysis would help readers understand the method's boundaries.

4. **Missing sensitivity analysis for the curriculum schedule.** The ablation confirms that curriculum helps vs. no curriculum (19.18 vs. 18.63 PSNR), but does not explore sensitivity to the starting/ending angles, linear vs. exponential schedules, or whether the semantic loss could also benefit from curriculum coordination (it uses a fixed θ′=120°, φ′=45° throughout training).

5. **CLIP-based semantic loss uses fixed pose range disconnected from curriculum.** The pixel-level curriculum progresses from 15° to 90°, but the semantic loss uses a fixed wider range (θ′=120°, φ′=45°). The paper does not discuss whether this mismatch creates conflicting gradients or whether the semantic loss could benefit from the same curriculum.

### Trivial
- Typo: "perfrormance" (line 380).

## Nice-to-Haves
- Provide a block diagram or pseudocode for the occlusion detection pipeline, even if full pseudocode is in the appendix.
- On MVImageNet or CO3D, plot self-consistency vs. actual NVS quality per-sample to validate the metric.
- Show a few representative failure cases alongside the successes — this would make the limitations section more informative than just the constant-intrinsics point.

## Removed Points
- **"Table 1 is dense and hard to parse"** — Removed as a pure formatting/style nitpick.
- **"Baseline TripoSR confusion"** — Removed. The paper states "All TripoSR results are after fine-tuning" and baseline row is clearly the original model checkpoint. The ambiguity about whether it's the same initialization is resolved by context: the baseline is the Objaverse-trained checkpoint, and Real3D starts from that checkpoint.
- **"Data scaling figure not provided"** — Removed. The figure is referenced (Fig. 3 via `\input{graphs/data_ratio_all}`) and was almost certainly in the original PDF but lost in text extraction from the PDF parser.
- **"Missing related works"** — Removed per rules (cannot confirm without external sources).
- **"Missing appendix/proofs"** — Removed; these exist in the original submission.

## Novel Insights
None beyond the paper's own contributions. The reviewers did not identify any connection or implication the authors themselves missed.

## Suggestions
- Add 2–3 paragraphs in Sec. 3.2 describing the curation pipeline: which segmentation model (SAM?), which depth estimator, how occlusion is detected from their synergy, and thresholds used.
- On any dataset with GT novel views (e.g., MVImageNet test), compute both self-consistency and NVS metrics per-sample and show a scatter plot to validate that the self-consistency metric tracks actual reconstruction quality.
- Include a subsection on failure modes with representative qualitative examples, even if in an appendix.
- Add an ablation varying the curriculum schedule (starting/ending angles, schedule shape) and optionally coordinating the semantic loss range with the curriculum.

## Score and Decision

**Calibration anchors used:**

| Path | Avg Score | Round | Comparison |
|---|---|---|---|
| `/home/.../TjeVPTtSwa.md` (Extend3D) | 3.00 | R1 | Much weaker; withdrawn paper with unclear contribution |
| `/home/.../91GG9IUOCh.md` (Surf3R) | 2.00 | R1 | Much weaker; unclear pipeline |
| `/home/.../Xo1h3mIN9O.md` (SceneMaker) | 3.00 | R1 | Much weaker; limited novelty |
| `/home/.../tiQaO3f1QB.md` (PRISM) | 2.67 | R1 | Much weaker; limited validation |
| `/home/.../TPJEZDn5zo.md` (SceneFuse-3D) | 5.50 | R1, R2 | Weaker; training-free pipeline with less novelty |
| `/home/.../9fqGBSLBX8.md` (Splat and Distill) | 4.67 | R1 | Weaker; mixed reviews, less convincing contribution |
| `/home/.../z0QLeooEEf.md` (ReconViaGen) | 5.50 | R1, R2 | Weaker; some concerns about novelty |
| `/home/.../tIVCfVnIHo.md` (Lyra) | 7.00 | R1, R2 | Comparable; similar self-training paradigm for 3D, similar evaluation breadth |
| `/home/.../kI27Niy4xY.md` (VIST3A) | 8.00 | R1 | Stronger; unanimous high scores, more ambitious framework |
| `/home/.../y4yajRJWiS.md` (LaRI) | 6.00 | R2 | Slightly weaker; different task |
| `/home/.../9LYsvna4Sk.md` (Unsup. Mesh Param.) | 6.50 | R2 | Comparable in score; different topic |
| `/home/.../c1jWNZ1Zqg.md` (Var. Inf. Cyclic) | 6.67 | R2 | Less relevant (general cycle-consistency theory) |
| `/home/.../v2skNLbrfF.md` (ORCaS) | 6.00 | R2 | Less relevant (depth completion) |

**Round 1 bracket:** 5.5–7.0. Real3D is clearly above the weak anchors (2–3) and below the 8.0 unanimous-accept level. Within the 4.67–7.0 middle band, it sits at the higher end due to its clear motivation, novel loss design, and thorough evaluation.

**Round 2 narrowing:** Compared to Lyra (7.0, the most topically similar paper), Real3D has a comparable contribution level. Lyra's self-distillation from video diffusion is clever but was critiqued as a straightforward combination; Real3D's loss design with careful degeneration prevention is arguably more technically novel. However, Real3D has the underspecified data curation weakness and the self-consistency metric concern. The 6.5 anchor (mesh parameterization paper) provides a reference for the score level: that paper had clear contributions but some concerns about incremental novelty and evaluation gaps.

**Final score: 6.5** — a solid paper with a clear, significant contribution that outweighs its presentational gaps. All weaknesses are addressable and none threaten the core claims.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>