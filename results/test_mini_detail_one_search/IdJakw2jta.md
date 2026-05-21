Now I have a thorough understanding of the paper and the calibration anchors. Let me synthesize the final review.

## Summary

The paper introduces Long-Form Spatio-Temporal Video Grounding (LF-STVG), a new task of localizing targets in videos spanning 1–5 minutes, and proposes ART-STVG, an autoregressive transformer that processes frames sequentially with selective spatial/temporal memory banks and a cascaded decoder. The authors extend HCSTVG-v2 to create five LF-STVG benchmarks (1–5 min) and show that ART-STVG outperforms existing STVG methods by large margins, with the gap widening as videos get longer.

## Strengths

- **Large and consistent gains on all five LF-STVG benchmarks.** Table 1 shows ART-STVG outperforms all prior methods on every video length, with gains increasing from modest (e.g., +0.7% m.tIoU at 1 min vs. TA-STVG) to substantial (e.g., +6.8% m.vIoU at 3 min and +7.3% m.tIoU at 5 min). The trend that ART-STVG's advantage grows with video length directly supports the paper's core claim that autoregressive processing is better suited for long-form localization.

- **Ablations cleanly isolate the contribution of each component.** Table 2 shows temporal memory selection improves m.tIoU from 9.6% (all memories) to 23.0% (selected), a 13.4-point gain. Table 3 shows spatial memory selection adds 0.9% over unselected spatial memories. Table 4 shows the cascaded spatio-temporal decoder outperforms the parallel design by 1.5% m.tIoU and 2.8% vIoU@0.3. These experiments convincingly demonstrate that each design choice is meaningful.

- **Autoregressive streaming with memory selection is a principled departure from existing all-at-once approaches.** The paper motivates why processing all frames concurrently is problematic for long videos (GPU memory, irrelevant information) and proposes a natural alternative. ART-STVG also remains competitive on short-form STVG (59.2 vs. 60.4 m.tIoU, Table 7), showing it does not sacrifice short-video performance.

- **The paper addresses a genuinely under-explored problem.** While long-term video understanding has been studied in action detection and QA, long-form spatio-temporal grounding is new. Extending HCSTVG-v2 to 1–5 min provides a useful evaluation suite, even if the description of the extension process could be more detailed.

## Weaknesses

### Major

- **How baselines were evaluated on long videos is not specified, which undercuts the main experimental claim.** ART-STVG processes frames sequentially, so naturally handles videos of any length. Existing methods (TubeDETR, STCAT, CG-STVG, TA-STVG) were designed to process all frames simultaneously. A 3-minute video at 3.2 FPS is ~576 frames; a 5-minute video is ~960 frames. The paper never states how these baselines were adapted for inference on such long videos — whether frames were subsampled, a sliding window was used, or the methods were simply run to OOM. Without this information, the large gaps in Table 1 (e.g., ART-STVG 23.0% vs. TA-STVG 13.9% m.tIoU at 3 min) could partially reflect an unfair evaluation setup rather than genuine model superiority. This is the most consequential gap in the paper: the central comparison is uninterpretable without knowing the baseline protocol. The paper states "all methods including ART-STVG are trained exclusively on the HCSTVG-v2 training set (average video length 20 seconds) for fair comparison" (line 264), which addresses training but not inference.

### Minor

- **Computational cost is claimed as a motivation but never measured.** The paper argues that existing models face "computational bottlenecks because of high GPU memory requirements" (line 88) and that ART-STVG "resolves the computational bottleneck" (line 90). Yet no runtime, GPU memory, or inference speed results are reported for any method. This is a gap between the paper's narrative and its experimental support; it does not invalidate the accuracy results, but it weakens the practical argument.

- **No error bars or significance measures.** Results are reported from single runs. Several differences are modest (e.g., +0.7% m.tIoU on 1-min videos). While single-run evaluation is standard practice in the STVG literature (the TA-STVG paper accepted at ICLR 2025 also reports single runs), reporting variance would strengthen confidence, especially in the smaller-gap settings.

- **Dataset extension description is vague.** The paper states extensions are "based on original YouTube videos, not concatenated clips, and we manually review the extended videos to ensure their quality" (line 258). It does not specify how longer clips were selected, whether textual queries were re-verified against the longer segments, what the criteria for "quality" were, or how many videos were rejected. Since the entire evaluation rests on these benchmarks, more detail is needed for reproducibility.

- **Failure cases and limitations not discussed.** The absolute performance on 5-minute videos is low (15.0% m.tIoU), and the temporal memory selection (based on cosine-similarity event boundaries) is heuristic. The paper does not discuss these limitations or analyze failure modes (e.g., gradual transitions, multiple similar events). A brief limitations paragraph would improve the paper.

### Trivial

- Some figure references in the extracted text appear duplicated or slightly garbled, but these are parser artifacts and do not reflect the original submission.

## Nice-to-Haves

- The paper could be strengthened by re-running baselines with a controlled adaptation protocol (e.g., sliding window with aggregation) and showing ART-STVG still outperforms them, ideally with runtime/memory comparisons.
- Ablations at multiple video lengths (beyond just 3 min) would confirm the design choices generalize across scales.
- A discussion of temporal memory selection failure cases (e.g., gradual transitions, closely similar events) would be informative.

## Removed Points

- *Criticism about Equation (1) being garbled*: This is a parser artifact; the original formatting is standard.
- *Criticism about missing related works*: The review instructions forbid marking missing related works as a weakness.
- *Speculation about baselines OOM'ing*: The harsh critic speculated the baselines "would require enormous GPU memory — likely exceeding any reasonable budget." While the paper indeed does not explain how baselines were run, the reviewer cannot assert what did/didn't happen; I moved the core concern (lack of protocol documentation) to Major and removed the speculative framing.
- *Several generic strengths from the Strength Finder* (e.g., "addresses an important problem," "first to explore") were removed as too generic or sycophantic; the retained strengths are concrete and evidence-grounded.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Clarify the baseline inference protocol.** State explicitly: how many frames were fed to each baseline, what GPU hardware was used, whether subsampling or sliding windows were employed, and whether any baselines failed to run (OOM) on the longest videos. If subsampling was used, discuss how the frame rate was chosen to be fair.

2. **Provide computational cost measurements.** Report GPU memory usage and inference time per frame / per video for ART-STVG and baselines on at least one video length. This directly supports the claimed advantage of autoregressive processing.

3. **Expand dataset documentation.** Describe how extended clips were selected from original YouTube videos, whether text queries were validated against the longer clips, and what "manual review" entailed (e.g., inter-annotator agreement, rejection criteria).

4. **Add error bars** for at least the key comparisons (Tables 1 and 7) by running 3 seeds, or explain why single-run reporting is standard in this subfield.

5. **Add a brief limitations discussion** addressing the low absolute performance on 5-min videos and the heuristic nature of temporal boundary detection.

## Score and Decision

**Anchors used for calibration:**

| Path | Avg Score | Comparison |
|------|-----------|------------|
| WOzffPgVjF.md (TA-STVG) | 7.50 | Strong STVG paper with cleaner evaluation; ART-STVG tackles a harder problem but has a significant experimental gap that TA-STVG lacks |
| 8pusxkLEQO.md (ARLON) | 6.25 | Long-video generation paper with autoregressive+diffusion; ART-STVG has better component ablations but weaker computational reporting |
| yHj6EunfVQ.md (CoSPaL) | 5.50 | Weakly supervised STVG; ART-STVG has clearer novelty and stronger ablations |
| YCwN7wQA6W.md (Grounded-VideoLLM) | 4.25 | Rejected; ART-STVG has a genuinely new task and more convincing evidence |
| xYzOkOGD96.md (Grounded Video Caption) | 3.83 | Rejected for overclaiming; ART-STVG's claims are better justified |
| BwQUo5RVun.md (Weakly-sup Visual Grounding) | 3.00 | Rejected; ART-STVG is substantially stronger |
| 9Cu8MRmhq2.md (Norton) | 8.00 | Strong long-video paper with rigorous evaluation; ART-STVG is a step below in experimental completeness |

ART-STVG tackles a genuinely new task with a well-motivated architecture and strong ablations, placing it above clearly rejected papers. However, the failure to document how baselines were evaluated on long videos is a significant gap that prevents full confidence in the headline results. This places it below the strongest papers in the field (TA-STVG, Norton) and in the borderline range.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>