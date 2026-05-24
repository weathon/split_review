Now I've carefully read the full paper. Let me verify each claim against the actual content and produce the consolidated review.

Some key findings from reading the paper:

1. **Temporal grounding**: Eq. (7) says `h_i ∈ ℝ²` represents start/end probabilities per frame. Figure 6 shows probability curves. How per-frame probabilities become a single interval for m.tIoU is not explicitly stated in the main paper — the loss function is deferred to supplementary (Section 3.5: "Due to limited space, please see our loss function in supplementary material").

2. **Dataset extension**: Section 4 (Datasets) says extensions are "based on original YouTube videos, not concatenated clips" and "manually reviewed" - but doesn't clarify whether the original 20-second temporal annotation is maintained as-is within the longer video.

3. **Computational cost**: No runtime/memory comparison is provided.

4. **Memory growth**: Section 3.3 confirms "without removing any existing memories" — memory is unbounded.

Let me now produce the final consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses
// List only reasonable points. Rank by severity.
// Not every paper has weaknesses at every tier. Leave a tier empty (or write "None") if nothing qualifies.

### Fatal
// Errors that invalidate the paper's core claims or results.
// Most papers have none. Leave empty if none apply.

### Major
// Issues that a reviewer would weigh against acceptance, and that the authors should fully resolve in a rebuttal.

### Minor
// Issues worth the authors' attention but unlikely to change an accept/reject decision.

### Trivial
// Small issues the authors should fix but that carry no weight in evaluation.

## Nice-to-Haves
- suggestion that would improve but is not a core flaw

## Removed Points
// Points from the input reviews that should not appear in the main review

## Novel Insights
One paragraph synthesizing genuinely novel observations.

## Suggestions
- specific actionable suggestion

## Score and Decision## Summary

This paper introduces Long-Form Spatio-Temporal Video Grounding (LF-STVG), a new problem setting where videos span minutes rather than tens of seconds. The authors propose ART-STVG, an autoregressive transformer that processes frames sequentially with spatial and temporal memory banks, selective memory retrieval strategies, and a cascaded spatio-temporal decoder design. On newly extended LF-STVG benchmarks (1–5 minutes), ART-STVG substantially outperforms existing STVG methods (e.g., on 3-minute videos, 23.0 m.tIoU vs. 13.9–14.2 for prior methods), and it remains competitive on short-form STVG.

## Strengths

1. **Large and consistent gains across all video lengths** — Table 1 shows ART-STVG outperforms TubeDETR, STCAT, CG-STVG, and TA-STVG on every LF-STVG benchmark (1–5 minutes), with the gap widening on longer videos (e.g., on 5-minute videos: 15.0 m.tIoU vs. 7.7–8.1 for prior methods). This directly validates the core claim that ART-STVG is more effective for long-form STVG.

2. **Memory selection strategies are convincingly validated** — Ablations in Tables 2 and 3 demonstrate that selective memory retrieval significantly outperforms both "no memory" and "all memories" baselines. Notably, using all temporal memories *hurts* performance (9.6 m.tIoU vs. 16.7 without memory), while selection recovers and surpasses it (23.0 m.tIoU), showing a non-trivial insight that irrelevant historical information degrades grounding.

3. **Cascaded decoder design shows clear benefits** — Table 4 demonstrates that the proposed cascaded spatio-temporal decoder (23.0 m.tIoU) outperforms a parallel design (21.5 m.tIoU), validating the claim that fine-grained spatial information assists temporal localization.

4. **Thorough ablation study** — The paper systematically ablates temporal memory selection (Table 2), spatial memory selection (Table 3), decoder architecture (Table 4), number of selected memories (Table 5), and training video length (Table 6), providing clear evidence for each design choice.

5. **New LF-STVG benchmark** — The paper extends HCSTVG-v2 to 1–5 minutes using original YouTube videos, creating a standardized evaluation setup that fills a gap in the literature.

6. **Competitive on short-form STVG** — Table 7 shows ART-STVG achieves 59.2 m.tIoU / 39.2 m.vIoU on HCSTVG-v2, close to the state-of-the-art TA-STVG (60.4/40.2), demonstrating that the autoregressive design does not sacrifice short-video accuracy.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Temporal interval prediction from per-frame probabilities is underspecified** — Eq. (7) states that the temporal head outputs per-frame start and end probabilities `h_i ∈ ℝ²`. Figure 6 illustrates start/end probability curves. However, the paper never describes how these per-frame probabilities are converted into a single predicted temporal interval `[t_start, t_end]` for computing m.tIoU (e.g., thresholding, argmax, or some other aggregation). The loss function is deferred to the supplementary. While this does not invalidate the comparative results (since all methods are evaluated under the same protocol), it is a documentation gap that should be closed in the main paper.

2. **Dataset extension procedure lacks detail on temporal annotations** — The paper states that LF-STVG datasets are extended from original YouTube videos and "manually reviewed to ensure their quality," but does not specify how temporal ground-truth labels are defined for the longer videos. The original HCSTVG-v2 uses 20-second clips with event annotations; when extending to 1–5 minutes, it is natural to keep the original event interval unchanged within the longer video. This should be stated explicitly to avoid ambiguity.

3. **Memory grows unbounded with no capacity discussion** — Section 3.3 states that memory is updated "without removing any existing memories." As videos grow to tens of minutes or hours in practical applications, unbounded memory growth could become a bottleneck. The paper does not discuss capacity limits, compression, or eviction strategies, nor does it report how memory size affects runtime or performance on the longest videos tested.

4. **No empirical efficiency comparison despite efficiency motivation** — The introduction motivates ART-STVG by citing the "computational bottleneck" of processing all frames at once. Yet the paper provides no comparison of GPU memory, inference time, or throughput between ART-STVG and existing methods, especially on the longest (5-minute) videos. This leaves the efficiency claim unsubstantiated.

### Trivial

None.

## Nice-to-Haves

- Report inference-time GPU memory and runtime for ART-STVG vs. a representative baseline (e.g., TA-STVG) on at least one video length to substantiate the efficiency motivation.
- Provide a quantitative evaluation of temporal memory segmentation quality (e.g., precision/recall of detected event boundaries against ground-truth event changes), complementing the qualitative illustration in Figure 6.
- Analyze failure cases on longer videos to understand whether errors stem from complete misses, inaccurate boundaries, or spatial mislocalization.

## Removed Points

The following points from the input reviews were removed with brief justification:

- **"Critical gap: temporal grounding procedure unspecified → invalidates core experimental evidence"** — The harsh critic labeled this as "fatal" and claimed it invalidates the evaluations. While the paper does not describe the conversion from per-frame probabilities to a single interval, this is a documentation gap, not a fatal flaw. The same evaluation pipeline is applied consistently to all methods; relative comparisons remain valid. Downgraded to Minor.
- **"Supplementary material for loss function / baseline architecture is missing"** — The parser strips Appendix sections from all papers. Weaknesses about missing appendix content are removed per the review rules.
- **"Absolute numbers on 4/5-minute videos are very low (m.tIoU ~15%)"** — This describes task difficulty, not a flaw in the paper. The baselines are even lower, and the paper's contribution is relative improvement.
- **"Temporal memory selection only evaluated qualitatively"** — The paper provides a qualitative illustration (Fig. 6), which is standard for this type of contribution. A quantitative evaluation would strengthen but is not a deficiency.
- **"Related work is shallow"** — Generic criticism without a specific actionable anchor.
- **Several generic "Missing Experiments" and "Deeper Analysis Needed" suggestions from the harsh critic** (e.g., "test on full range after training on 40-second clips," "compare to temporal action localization methods") — These are outside the stated scope or speculative. Merged a subset into Nice-to-Haves.
- **Strength: "Autoregressive processing avoids global memory bottleneck"** — Kept as a design-level claim but noted that empirical verification is absent. This does not appear as a standalone weakness since the paper's primary contribution is accuracy.

## Novel Insights

The most interesting finding is the negative result in Table 2: using *all* temporal memories (without selection) dramatically lowers m.tIoU from 16.7 to 9.6, demonstrating that naive accumulation of historical temporal information in long videos actively harms performance. This supports the paper's core insight that *selective* memory — not simply more memory — is critical for long-form STVG. The finding that the performance gap between ART-STVG and prior methods widens as videos grow longer (Table 1) also provides compelling evidence that the autoregressive-with-selective-memory design addresses a structural limitation of existing parallel-processing approaches, rather than just being an incremental improvement.

## Suggestions

1. Add one sentence in Section 3.2 or 3.5 specifying how per-frame start/end probabilities `h_i^s, h_i^e` are converted into a single predicted interval (e.g., "the start frame is taken as the frame with maximum start probability, and the end frame as the frame with maximum end probability" — or whatever the actual procedure is). This is the single most important fix.

2. Clarify in the Datasets paragraph (Section 4) that the temporal ground-truth annotations for LF-STVG are the original HCSTVG-v2 annotations kept as sub-intervals within the extended longer videos.

3. Add a brief note on practical memory management for very long videos (e.g., a sliding-window scheme or memory compression), even if only as a discussion point in the conclusion.

## Score and Decision

MY FINAL SCORE: <score>8.0</score>
MY FINAL DECISION: <decision>Accept</decision>