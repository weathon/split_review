Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper introduces Long-Form Spatio-Temporal Video Grounding (LF-STVG), extending the problem to videos of 1–5 minutes, and proposes ART-STVG — an autoregressive transformer that processes frames sequentially with selective spatio-temporal memory banks and a cascaded decoder. The authors extend HCSTVG-v2's validation set to create LF-STVG benchmarks and demonstrate that ART-STVG substantially outperforms existing methods across all lengths while remaining competitive on short-form STVG.

## Strengths

1. **First systematic exploration of LF-STVG** — The paper identifies a genuine gap in the literature (STVG research is limited to <1-minute videos) and creates extended benchmarks from HCSTVG-v2 source videos. This provides a standardized evaluation protocol that future work on this problem can build on.

2. **Consistent and large improvements across all lengths** — Table 1 shows ART-STVG outperforms all prior methods on every LF-STVG benchmark. At 5 min, ART-STVG achieves 15.0% m.tIoU vs. 8.1% for the next best (CG-STVG), nearly doubling the prior best. The performance gap widens with video length (from +1.8% at 1 min to +7.3% at 5 min vs. TA-STVG), directly supporting the claim that the autoregressive design is better suited for longer videos.

3. **Memory selection ablations strongly validate the mechanism** — Table 2 shows that using all temporal memories (9.6% m.tIoU) is *worse* than no memory (16.7%), but selective temporal memory raises this to 23.0% — a 13.4-point gain. This directly validates that selection, not just the presence of memory, is critical. The paper correctly explains why (multiple events in long videos introduce irrelevant information).

4. **Cascaded decoder design validated** — Table 4 shows cascaded (23.0% m.tIoU) outperforms parallel (21.5%), supporting the claim that leveraging spatial fine-grained cues to assist temporal localization is beneficial.

5. **Competitive short-form performance** — ART-STVG achieves 59.2% m.tIoU on HCSTVG-v2 (Table 7), only 1.2 points behind the best short-form specialist TA-STVG, demonstrating that the autoregressive design does not sacrifice short-video capability.

6. **Training with longer videos further widens ART-STVG's advantage** — Table 6 shows when all methods train on 40s videos, ART-STVG achieves 28.3% vs. 20.8% for the next best, confirming the design better exploits longer training sequences.

## Weaknesses

### Fatal

None.

### Major

1. **LF-STVG dataset annotation process undocumented** — The paper states "we extend only the validation set to lengths of 1 to 5 minutes" and that extensions are "based on original YouTube videos, not concatenated clips, and we manually review the extended videos to ensure their quality" (line 200). However, it does **not** describe how ground-truth annotations (spatial bounding boxes, temporal event boundaries) were obtained for the extended portions beyond the original 20-second clips. Were the existing 20-second annotations placed within longer videos? Were new annotations created for the additional portions? With what protocol and inter-annotator agreement? This is a significant reproducibility gap. While it does not invalidate the *internal* comparisons (all methods are evaluated on the same data), it undermines the experimental foundation for future work that would use these benchmarks.

2. **No computational cost analysis** — The paper claims ART-STVG resolves the "computational bottleneck" of processing all frames at once, but provides no measurements of FLOPs, inference time, or GPU memory for ART-STVG vs. baselines on long videos. The per-frame computation (ResNet-101 + VidSwin + multimodal encoder producing ~2,530 tokens per frame) is substantial, and without quantitative evidence, the efficiency claim is unsupported.

3. **No discussion of limitations** — The conclusion (Section 5) is a straightforward summary with no acknowledgment that absolute performance on long videos remains low (best method achieves only 15% m.tIoU on 5 min), that evaluation is limited to a single source dataset (HCSTVG-v2), or that the temporal memory selection heuristic (TextTiling-inspired cosine similarity) may fail on videos with gradual transitions or overlapping events. A limitations section would strengthen the paper's scientific rigor.

### Minor

1. **"Autoregressive streaming" framing is imprecise** — The paper describes processing "one frame at a time" in a "streaming" fashion. However, Section 3.1 notes that VidSwin motion extraction uses previous frames as input, and the memory banks accumulate information across frames. The method is better described as memory-augmented frame-by-frame decoding with a growing context window rather than a pure streaming architecture. The paper would benefit from de-emphasizing "streaming" and foregrounding the memory mechanisms.

2. **No failure-case analysis for temporal memory selection** — The TextTiling-inspired heuristic (cosine similarity of adjacent frame features) is used to detect event boundaries. The paper does not analyze when this heuristic fails (e.g., gradual transitions, overlapping events, nested events) or provide an error analysis of its predictions.

3. **tIoU metrics are very low across all methods** — While ART-STVG consistently outperforms baselines, the absolute performance on LF-STVG-5min (15.0% m.tIoU) is very low. The paper acknowledges this indirectly through comparisons but does not directly calibrate reader expectations about the difficulty of the task.

### Trivial

None.

## Nice-to-Haves

- Qualitative grounding results (predicted tubes/boxes overlaid on long videos) showing both correct and incorrect predictions would help interpret the low absolute metrics and build intuition about what ART-STVG does well vs. poorly.
- Analysis of memory bank capacity and growth for very long videos (hours) would strengthen the practical applicability argument.

## Removed Points

These points were raised by reviewers but are removed for the following reasons:

- **"Baseline comparison is rhetorically stacked"** — REMOVED. The paper explicitly states all methods are "trained exclusively on the HCSTVG-v2 training set (average video length 20 seconds) for fair comparison" (line 206). Table 6 further shows ART-STVG maintains its dominance when all methods train on 40s. The comparison is fair.
- **"All-memory worse than no-memory is a red flag"** — REMOVED. The paper directly acknowledges and explains this result: "the long-term video often contains multiple events, and using all temporal memories may introduce irrelevant information" (line 214). This finding motivates the selection mechanism; it is not a flaw.
- **"5 minutes is not truly long-form"** — REMOVED. The paper appropriately scopes its contribution as an extension from 20 seconds to 1–5 minutes, which is a significant step for the STVG task. Framing this as a weakness constitutes scope creep.
- **"No qualitative results"** — REMOVED. The paper includes attention maps (Figure 5) and temporal memory illustrations (Figure 6), which are qualitative visualizations.
- **"Missing related works"** — REMOVED per hard rules (cannot confirm existence of external sources).
- **Generic/superficial strengths** from Strength Finder (e.g., "addressed an important problem", "well-written") — REMOVED or merged into concrete strengths above.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface a pattern or framing that the authors themselves do not already articulate in the paper.

## Suggestions

1. **Document the LF-STVG annotation process** in detail: who annotated, the annotation protocol, how ground truth was extended from 20s clips to 1–5 minute videos, inter-annotator agreement metrics, and quality control steps.
2. **Add computational cost measurements** (inference time per frame, total inference time per video, peak GPU memory) for ART-STVG vs. all baselines on videos of varying lengths.
3. **Add a limitations section** acknowledging the low absolute performance on long videos, single-dataset evaluation, potential failure modes of the TextTiling-inspired heuristic, and scope boundaries (1–5 min vs. true hour-long videos).
4. **Tone down the "streaming" framing** and emphasize memory selection and cascaded decoder as the primary contributions, which is where the actual novelty and performance gains lie.

## Score and Decision

**Score: 6.0**

**Decision: Accept**

### Calibration Anchors

**Round 1 — Bracketing:**
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| YGWxpOI6Y0 | 3.4 | R1 | Much weaker — marginal improvements, no clear contribution |
| bEvI30Hb2W | 3.0 | R1 | Much weaker — limited experiments |
| ICR3swcnaa | 3.0 | R1 | Much weaker — different task, less rigorous |
| MSxCBXD5C8 | 3.0 | R1 | Much weaker — different task |
| 1DEHVMDBaO | 4.6 | R1 | Weaker — marginal gains (<1%), only 2 baselines, missing ablations |
| 14fFV0chUS | 6.75 | R1 | Slightly stronger — well-documented, strong SOTA but on different (VTG) task |
| YCwN7wQA6W | 4.25 | R1 | Weaker — missing key analyses, limited baselines |
| tEei1bolt3 | 5.0 | R1 | Weaker — novelty concerns, task definition issues |
| 9Cu8MRmhq2 | 8.0 | R1 | Stronger — top-tier paper with rigorous analysis |
| 2dnO3LLiJ1 | 8.0 | R1 | Stronger — top-tier theoretical contribution |

**Round 2 — Narrowing:**
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| le4IoZZHy1 (CG-Bench) | 6.2 | R2 | **Comparable** — strong benchmark contribution with fully documented annotation; similar quality level |
| a1P5kh2oo8 (Vinoground) | 5.75 | R2 | Slightly weaker — benchmark-only paper, narrower scope |
| 5ddsALwqkf (Neptune) | 5.33 | R2 | Weaker — missing baselines, auto-generated annotations raise quality concerns |
| wkbx7BRAsM | 7.0 | R2 | Stronger — different domain (video imitation), cleaner evaluation |
| 8pusxkLEQO | 6.25 | R2 | Comparable — different domain (video generation), solid but not flawless |
| QWDFOOoV3U | 5.75 | R2 | Slightly weaker — mixed scores, unclear contribution |

**Round 1 bracket:** 4.5–6.5  
**Final score rationale:** The paper is clearly stronger than anchors at 4.6–5.33 (which had marginal results, limited experiments, or novelty issues) and comparable to anchors at 5.75–6.25. It is slightly weaker than the 6.75 anchor (TRACE) primarily due to the dataset annotation documentation gap. Score **6.0** reflects solid, well-supported contributions with significant weaknesses that are addressable in a revision (annotation documentation, computational cost analysis, limitations section).

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>