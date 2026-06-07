## Summary

This paper proposes Ground-A-Video, a training-free framework for multi-attribute video editing that integrates grounding information (bounding boxes + captions) with spatially-continuous guidance (depth maps). The method introduces three technical components: Modulated Cross-Attention to handle per-frame optimized null embeddings, Cross-Frame Gated Attention to apply grounding tokens in a temporally consistent way, and optical-flow-guided latent smoothing. The core idea—using spatial grounding to disentangle complex multi-attribute edits—is well-motivated and addresses a genuine limitation of existing video editing methods.

## Strengths

1. **Well-motivated technical approach to a real problem.** The paper identifies concrete failure modes in multi-attribute video editing (omitting edits, modifying wrong elements, mixing edits, failing to preserve unchanged regions) and proposes grounding-based spatial disentanglement as a principled solution. The three attention mechanisms each address a specific, clearly articulated weakness in the existing pipeline.

2. **Systematic ablation isolating each component's contribution.** Table ablation-quantitative removes each of the four proposed components and reports CLIP Text-Align and Frame-Con for each removal. Every component contributes positively (full model: 0.837 Text-Align, 0.970 Frame-Con; worst removal "w/o Groundings": 0.802, 0.960). This provides controlled evidence for each design decision.

3. **Cross-Frame Gated Attention clearly addresses a temporal consistency failure.** The paper identifies (lines 294–295) that applying GLIGEN's image-level gated attention independently per frame causes the same grounding entity to be projected differently across frames. The ablation (Fig. ablation:attention-Right) shows that frame-independent gating can produce worse results than no groundings at all—a concrete failure mode that Cross-Frame Gated Attention fixes.

4. **Modulated Cross-Attention solves a real technical problem.** The paper recognizes that per-frame null-text optimization produces variant unconditional embeddings that cause appearance inconsistencies across frames, and proposes merging them during the unconditional CFG branch (Eq. in Sec. method:inflation-inversion). This is a clean solution to a problem that prior inflated-SD methods addressed via fine-tuning.

## Weaknesses

### Major

1. **Evaluation on only 20 videos with no statistical rigor.** The evaluation uses a subset of 20 videos from DAVIS (line 376) with no description of how they were selected. No confidence intervals, standard deviations, or significance tests are reported anywhere. The CLIP metric differences between the proposed method and the next-best baseline are tiny (Text-Align: 0.837 vs. 0.833, difference 0.004; Frame-Con: 0.970 vs. 0.963, difference 0.007). Without error bars, the reader cannot assess whether these differences are meaningful or within the noise of a 20-video sample. This undermines the quantitative claims of superiority.

2. **User study documentation is insufficient and the results are internally inconsistent with the automatic metrics.** The user study reports huge gaps (Edit-Acc: 4.13 vs. 2.99; Preserve-Acc: 4.24 vs. 3.13; Frame-Con: 4.01 vs. 3.05 on a 1–5 scale), yet the automatic CLIP metrics show near-ties. The paper documents only the number of participants (28) and the rating scale (1–5). It does not mention whether the study was blinded, how videos were sampled or ordered, whether participants were shown methods in random order, or report any inter-rater reliability or per-method variance. While CLIP Text-Align and user-perceived edit accuracy are not identical quantities, the magnitude of the discrepancy (a near-tie on automated metrics but a landslide in human ratings) is unusual and demands explanation. This gap weakens the credibility of the user study as evidence.

3. **The manual refinement step is unquantified and uncontrolled.** The pipeline requires manual refinement of both the source prompt and the groundings (lines 144, 163, 252: "manually refined," "handcraft editing phase," "handcraft modifications"). The paper does not describe whether baselines received equivalent manual prompt engineering per video, nor does it quantify how many groundings were modified, how much time the refinement takes, or whether results degrade without it. This makes it difficult to assess the fairness of the comparison and the true generality of the method.

### Minor

4. **No computational cost analysis.** The pipeline uses SD + ControlNet + GLIGEN's gated attention + GLIP + RAFT + ZoeDepth + BLIP-2—a heavy stack. The paper provides no runtime, VRAM requirements, or inference latency for generating an 8-frame video. This matters for practical applicability and for assessing the "accessible, zero-shot" framing.

5. **Limited discussion of failure cases.** The limitations section (line 556) mentions only "misleading groundings." Many plausible failure modes are unexamined: inconsistent GLIP detections across frames, depth map inaccuracies, overlapping bounding boxes for different edit targets, and what happens when the optical flow estimate is poor. A more thorough discussion would strengthen the paper.

6. **Flow-guided smoothing shows negligible quantitative impact.** The ablation reports Frame-Con values of 0.970 (threshold 0.2), 0.968 (threshold 0.3), and 0.964 (threshold 0.4). These differences are within the noise range given the 20-video evaluation, so the claim that smoothing "effectively eliminates artifacts" (line 504) rests primarily on qualitative examples.

### Trivial

None.

## Nice-to-Haves

- A breakdown of results by edit complexity (single-attribute, multi-attribute non-overlapping, multi-attribute overlapping) would make the contributions of grounding clearer.
- Discussion of how the method scales to longer videos (beyond 8 frames) given the cross-frame attention computation.
- Reporting per-video standard deviations or bootstrapped confidence intervals for both CLIP metrics and the user study.

## Removed Points

The following points from the harsh critic were removed after verification against the paper:

- **"TAV baseline comparison is unfair"** — The paper adds ControlNet to TAV's inflation logic (line 398), which is *favorable* to the baseline, not unfair. The critic's framing was reversed.
- **"Gen-1 depth guidance is unclear"** — Line 400 states that "methods with ControlNet uniformly employed depth guidance." Gen-1 does not use ControlNet, so this criticism misreads the sentence.
- **"Zero-shot framing is misleading"** — The paper consistently uses "zero-shot" and "training-free" to mean no fine-tuning of network weights (lines 8, 141, 552), which is standard usage. Manual prompt refinement does not undermine this framing.
- **"Frame-Con metric rewards blurriness"** — This is speculative and applies symmetrically to all compared methods.
- **"Cross-Frame Gated Attention computational cost scaling"** — No evidence of computational bottlenecks is provided in the paper; this is a speculative concern.
- **"First claim needs careful scoping"** — The paper uses "to our knowledge" (line 57), which is an appropriate qualifier.
- **Strength about user study being a large-margin advantage** — While the data shows a large gap, the weakness about poor documentation and inconsistency with automatic metrics undermines this as a strength. Strength about optical flow smoothing being "model-agnostic and well-motivated" — The quantitative evidence for its effectiveness is weak (differences within noise), so this is overstated.

## Novel Insights

Beyond the paper's own contributions, the most notable observation from synthesis is the tension between the paper's two evaluation signals: the automatic CLIP metrics show the proposed method as only marginally better than baselines (differences of ≤0.015), while the user study reports a >1-point gap on a 5-point scale. This pattern often arises when automatic metrics are insufficiently sensitive to the specific quality the method improves (here, spatial disentanglement of edits). The paper would benefit from either (a) a metric designed to measure per-attribute edit accuracy with spatial specificity, or (b) an explicit argument about why CLIP metrics are expected to compress the advantage. Currently neither is provided, leaving the evaluation in an uncomfortable state.

## Suggestions

1. **Increase evaluation size and add statistical reporting.** Even 40–60 videos with per-video standard deviations and bootstrapped confidence intervals would substantially strengthen the quantitative claims.
2. **Document the user study thoroughly.** Add details on blinding, randomization, participant demographics, inter-rater reliability, and per-method score distributions. Address the discrepancy between automatic metric margins and user study margins explicitly.
3. **Quantify the manual refinement step.** Report how many groundings are modified per video on average, time cost, and whether the method can run without refinement on a held-out test set.
4. **Report computational cost.** Provide VRAM usage and per-video runtime for the full pipeline.
5. **Add a per-attribute edit accuracy metric.** Design a metric (e.g., using segmentation masks) that measures whether each intended edit was applied to the correct spatial region, to better capture what the method improves.

## Score and Decision

The paper identifies a real problem and proposes a sensible, well-motivated solution with three technically reasonable components. The core contribution—using grounding information for spatially-disentangled multi-attribute video editing—is likely valid. However, the evaluation is not strong enough to support the claimed conclusions at a top-tier venue. The test set is small (20 videos, unselected), no statistical measures are reported, the user study is inadequately documented and its results are internally inconsistent with the automatic metrics, and a manual refinement step is uncontrolled. These are not fatal to the method's potential, but they prevent the current version from being accepted.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>