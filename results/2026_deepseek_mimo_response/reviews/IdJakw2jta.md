Now I have good calibration data. Let me finalize my assessment.

**Round 1 bracket: 4.5 – 6.5**

**Round 2 anchors read:**
- CoSPaL (5.50, Accept) — Weakly supervised STVG with self-paced learning. Very topically relevant, comparable novelty level.
- Motion-Grounded Video Reasoning (5.00, Reject) — New task + benchmark for video grounding. Less technically developed than ART-STVG.
- ResidualViT (5.75, Reject) — Efficient zero-shot temporal video grounding. Comparable novelty, similar single-dataset concerns.

**Comparison:**
- ART-STVG is clearly better than Motion-Grounded (5.00): stronger method, more extensive ablations, more focused contribution.
- ART-STVG is comparable to CoSPaL (5.50): both combine established techniques for STVG, both have meaningful results but also significant limitations. ART-STVG has the more interesting insight (memory selection) but the baseline comparison issue.
- ART-STVG is comparable to ResidualViT (5.75): similar novelty level, similar single-benchmark limitation.

**Final score: 5.5** — Borderline. The paper has genuine strengths (new problem formulation, interesting memory selection insight, strong ablations) but the baseline comparison fairness, very low absolute performance, and train-test extrapolation gap are real concerns that prevent a higher score.

---

## Summary
This paper introduces Long-Form Spatio-Temporal Video Grounding (LF-STVG), extending STVG from ~20-second to 1–5-minute videos, and proposes ART-STVG, an autoregressive transformer with spatial/temporal memory banks and selective memory strategies. The authors extend the HCSTVG-v2 validation set to longer durations and demonstrate that ART-STVG degrades more gracefully than existing methods as video length increases.

## Strengths
- **Clear empirical evidence of the long-form STVG gap (Table 1):** Existing methods degrade catastrophically with video length (TA-STVG m.tIoU drops from 38.4% at 1min to 7.7% at 5min), while ART-STVG degrades more gracefully (39.1% to 15.0%), providing concrete quantitative motivation for the problem.
- **Temporal memory selection is essential, not optional (Table 2):** Using all temporal memories actually *hurts* performance (m.tIoU drops from 16.7% to 9.6%), while selective memory dramatically improves it to 23.0%. This non-trivial finding — that naive memory augmentation is harmful for long videos — is the paper's most interesting insight and has implications beyond STVG.
- **ART-STVG outperforms baselines even when retrained on longer videos (Table 6):** When existing methods are retrained on 40-second videos using their source codes, ART-STVG still achieves 28.3% vs. best baseline at 21.0% m.tIoU, showing the advantage is not solely an artifact of test-time autoregressive processing.
- **Progressive improvement gap grows with video length (Figure 2):** The performance margin over baselines increases monotonically from 1 to 5 minutes, directly supporting the claim that autoregressive processing with selective memory is specifically suited for long-form video.
- **Competitive short-form performance (Table 7):** ART-STVG achieves 59.2 m.tIoU on standard HCSTVG-v2, only 1.2% behind TA-STVG (60.4%), demonstrating the autoregressive framework does not entirely sacrifice short-form capability.
- **Systematic ablation evidence:** Each proposed component (temporal memory selection, spatial memory selection, cascaded decoder) is validated with controlled ablations (Tables 2–5), and the cascaded decoder provides measurable gains (1.5% m.tIoU, Table 4).

## Weaknesses

### Fatal
None.

### Major
- **Baseline fairness — compared methods are architecturally unsuited for the proposed benchmarks.** All baselines (TubeDETR, STCAT, CG-STVG, TA-STVG) are non-autoregressive methods that process all frames at once, designed for short videos. The paper's own motivation (Section 1) argues this approach is "fundamentally unsuitable" for long videos. Table 6 partially mitigates this by retraining baselines on 40-second videos, but 40 seconds is still far from 3–5 minutes. Meaningful comparisons would include sliding-window inference with temporal NMS, frame subsampling for existing methods, or memory-augmented long-video architectures adapted for STVG. Without such adapted baselines, the relative gains primarily demonstrate that short-video architectures fail on long videos.

- **Train-test sequence length mismatch (15× extrapolation) with no analysis.** The model is trained on 64 frames (~20 seconds at 3.2 FPS, line 194) but tested on sequences up to ~960 frames (5 minutes). This 15× extrapolation is significant for an autoregressive model with growing memory banks. The paper provides no analysis of whether memory bank quality degrades over very long sequences, how performance varies with position within a long video, or whether there are failure modes associated with this length gap.

- **Very low absolute performance on longer benchmarks, unaddressed.** On LF-STVG-5min, even ART-STVG achieves only m.tIoU = 15.0, m.vIoU = 10.0, vIoU@0.5 = 11.4 (Table 1e). These extremely low numbers mean the model is failing for most test samples at 5 minutes. While relative improvements over baselines are large, the paper does not discuss what these absolute numbers imply about task tractability, annotation quality for longer segments, or whether the task definition needs revision.

### Minor
- **Single benchmark — entire LF-STVG evaluation rests on extended HCSTVG-v2 validation set.** The paper acknowledges HCSTVG-v2 is "the only dataset which provides available source videos" (line 200). Understandable for a first exploration, but the extension methodology is underspecified: how are longer segments identified from source videos, how are temporal annotations created, and how is event ambiguity in longer context verified? The paper states they "manually review the extended videos" but provides no details on criteria or inter-annotator agreement.

- **No computational cost comparison despite claiming to resolve "computational bottleneck."** Sections 1 and 3.2 claim ART-STVG resolves the computational bottleneck of processing all frames at once, but no wall-clock time or GPU memory comparisons are provided. The autoregressive approach with growing memory banks may have its own scaling issues.

- **Notation error in Equation 5 and line 114.** $\tilde{f}_i^m$ is used for both the original motion feature (input to RoI) and the RoI-pooled output. Line 114 reads "Compared to $\tilde{f}_i^m$, $\tilde{f}_i^m$ is focused more on the target region" — clearly meant to be different symbols.

- **No quantitative analysis of temporal memory selection accuracy.** The TextTiling-inspired event segmentation is the most novel component, but only one visualization (Fig. 6) is shown. Measuring event boundary detection accuracy against ground truth would strengthen the contribution.

- **Baseline (ours) performs very poorly on short videos (Table 7):** 46.2/29.9 vs. TA-STVG's 60.4/40.2, indicating the autoregressive architecture is substantially harmful for short videos. This pattern warrants more discussion.

### Trivial
- **Equation 1 notation:** The same indexing ($f_i^1, f_i^2, \dots$) is reused for all three modality features, which is confusing.

## Nice-to-Haves
- Analysis of memory bank behavior over long sequences (does performance degrade in later portions of a 5-minute video?)
- Comparison to memory-augmented long-video understanding methods adapted for STVG
- Qualitative failure case analysis to understand when and why the method breaks down
- Clarification of Figure 2 metrics (m_Ap@1, m_Ap@5) vs. Table 1 metrics (m.tIoU, m.vIoU)

## Removed Points
These points are flagged to be removed, treat them with caution:
- **Loss function in supplementary material:** Standard practice due to space constraints; not a flaw.
- **Ablations only on LF-STVG-3min:** Reasonable for a first exploration and clearly stated.

## Novel Insights
The paper's most genuinely novel observation is that naive temporal memory augmentation actually harms performance (Table 2: using all memories drops m.tIoU from 16.7% to 9.6%), while the proposed selective strategy recovers and substantially exceeds the no-memory baseline. This counter-intuitive finding — that for long-form video understanding, memory management (what to remember and forget) matters more than memory capacity — is practically important and could inform broader long-video understanding research beyond STVG.

## Suggestions
- Add baselines with sliding-window inference or frame subsampling for existing STVG methods to make comparisons more informative.
- Analyze the train-test length extrapolation gap, potentially with experiments varying test-time sequence length.
- Report computational costs (wall-clock time, GPU memory) to substantiate the "computational bottleneck" claim.
- Provide quantitative evaluation of temporal memory selection's event boundary detection accuracy.
- Discuss the low absolute performance numbers and their implications for task tractability.

## Calibration Report

**All anchors retrieved:**

| Round | Paper | Avg Score | Path | Relevance |
|-------|-------|-----------|------|-----------|
| 1 | LVM-NET | 3.00 | bEvI30Hb2W | Long-form video reasoning with memory — weaker method, much lower results |
| 1 | VideoGPT+ | 3.40 | YGWxpOI6Y0 | Video understanding with encoders — different task |
| 1 | Spatio-temporal Diffusion Transformer | 3.00 | ICR3swcnaa | Action recognition — different task |
| 1 | Weakly supervised visual grounding | 3.00 | BwQUo5RVun | Visual grounding — different setting |
| 1 | Grounded-VideoLLM | 4.25 | YCwN7wQA6W | Video temporal grounding — rejected, comparable topic |
| 1 | TRACE | 6.75 | 14fFV0chUS | Video temporal grounding via causal modeling — stronger paper, accepted |
| 1 | Grounded Video Caption | 3.83 | xYzOkOGD96 | Video captioning + grounding — different task |
| 1 | ResidualViT | 5.75 | QWDFOOoV3U | Zero-shot temporal video grounding — comparable novelty |
| 1 | Multi-granularity correspondence | 8.00 | 9Cu8MRmhq2 | Long video correspondence — accepted, much stronger |
| 1 | ViT Registers | 8.00 | 2dnO3LLiJ1 | ViT feature maps — accepted, different topic |
| 1 | AR Diffusion | 8.00 | tyEyYT267x | Language models — accepted, different topic |
| 1 | MovingParts | 8.00 | QQ6RgKYiQq | Dynamic NeRF — accepted, different topic |
| 2 | CoSPaL | 5.50 | yHj6EunfVQ | Weakly supervised STVG — very relevant, accepted |
| 2 | Motion-Grounded Video Reasoning | 5.00 | tEei1bolt3 | New grounding task + benchmark — rejected |
| 2 | Long Context Transfer | 5.80 | QETk0lBdVf | Long video understanding — rejected |
| 2 | Visual Context Window Extension | 5.50 | X4Rcxi9588 | Long video understanding — rejected |
| 2 | ARLON | 6.25 | 8pusxkLEQO | Long video generation — accepted |
| 2 | Language Repository | 5.50 | O8FkMqNF1M | Long video understanding — rejected |
| 2 | Vinoground | 5.75 | a1P5kh2oo8 | Video temporal reasoning — rejected |
| 2 | VideoGLUE | 5.50 | q20O1J9ujh | Video understanding evaluation — rejected |
| 2 | CG-Bench | 6.20 | le4IoZZHy1 | Long video QA benchmark — accepted |

**Round 1 bracket: 4.5 – 6.5**

**Round 2 narrowing:** ART-STVG is clearly above Motion-Grounded (5.00), comparable to CoSPaL (5.50) and ResidualViT (5.75), and below TRACE (6.75). The paper's strengths (new problem, interesting insight, strong ablations) place it at the level of CoSPaL, while its weaknesses (baseline fairness, low absolute numbers, train-test gap) prevent it from reaching the TRACE tier.

**Final score: 5.5** — The paper is a reasonable first exploration of a valid problem direction with genuinely interesting insights (memory selection), but experimental validation is limited by baseline fairness concerns and very low absolute performance.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>