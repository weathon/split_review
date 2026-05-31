Now let me do the calibration search.Round 1 bracket: **4.5 – 6.5** (moderate contributions with evaluation concerns). Let me narrow.Now I have enough information to write the final review. Let me synthesize everything.

---

## Summary

This paper introduces Long-Form Spatio-Temporal Video Grounding (LF-STVG), extending STVG from ~20-second clips to 1–5 minute videos. The authors propose ART-STVG, an autoregressive transformer that processes video frames sequentially with spatial and temporal memory banks, selective memory strategies inspired by TextTiling, and a cascaded decoder design that feeds spatial localization cues to temporal grounding. Five new benchmark splits (LF-STVG-1min through LF-STVG-5min) are created by extending the HCSTVG-v2 validation set. ART-STVG substantially outperforms existing STVG methods across all benchmarks.

---

## Strengths

- **Consistent, growing margin on LF-STVG**: ART-STVG achieves m.tIoU/m.vIoU of 39.1/26.1 at 1 min, 31.8/21.3 at 2 min, down to 15.0/10.0 at 5 min — consistently above all baselines across every split of Table 1, with the gap widening as videos grow longer, exactly as the streaming hypothesis predicts.

- **Memory selection is strongly validated**: Table 2 shows that using all temporal memories without selection degrades m.tIoU from 16.7% (no memory) to 9.6% — well below no-memory performance — while selective temporal memory lifts it to 23.0%. This 13.4-point gain provides clear, concrete evidence that relevance-filtered memory is necessary and that the temporal boundary detection (TextTiling-inspired) works.

- **Cascaded decoder validated by ablation**: Table 4 confirms cascaded > parallel decoder design (23.0 vs 21.5 m.tIoU), providing focused evidence that routing spatial localization features into the temporal decoder is beneficial.

- **Competitive on SF-STVG**: ART-STVG achieves 59.2/39.2 m.tIoU/m.vIoU on HCSTVG-v2 (Table 7), outperforming all methods except TA-STVG (by 1.2/1.0 points), showing the streaming architecture does not catastrophically hurt short-form performance.

- **Robustness under longer training**: Table 6 shows ART-STVG at 28.3 m.tIoU when all methods are trained on 40-second videos, vs. the best competitor at 21.0 — a 7.3-point gap. This confirms the advantage holds under fairer training conditions and is not purely a training-length artifact.

---

## Weaknesses

### Fatal
*None.*

### Major

- **Unspecified inference procedure for full-sequence baselines.** Section 4.1 states that "all methods including ART-STVG are trained exclusively on the HCSTVG-v2 training set (average video length 20 seconds)," but does not state how TubeDETR, STCAT, CG-STVG, and TA-STVG are *run at inference* on 1–5 minute videos. These architectures process all frames simultaneously; at 3.2 FPS, a 5-minute video has ~960 frames — far beyond the 64-frame training length. It is unclear whether baselines receive all 960 frames (requiring extreme memory), are subsampled to 64 frames, or processed via a sliding window with post-processing. This matters because: the Baseline (streaming, no memory, Table 1-e) already slightly outperforms TA-STVG at 5 minutes (9.2 vs 7.7 m.tIoU), suggesting that sequential processing per se provides some advantage over forced temporal subsampling of full-sequence methods, independent of the memory mechanism. If baselines are subsampled, Table 1 partly measures "full-frame processing vs. severe temporal subsampling" rather than the claimed architectural comparison. The paper should specify the baseline inference procedure explicitly and ideally include a controlled comparison where all methods process the same number of frames.

- **Benchmark limited to extended validation set only.** The LF-STVG splits are extensions of the HCSTVG-v2 *validation* set only (2,000 samples). No LF-STVG training split exists. Every method (including ART-STVG) is trained on 20-second clips and evaluated out-of-distribution on 1–5 minute videos. As a result, the benchmarks conflate "architectural advantage on long videos" with "generalization across a 6× domain shift in video length." The absence of a dedicated LF-STVG training set limits the claims about which approach is best *for* LF-STVG vs. which approach generalizes *better from* short to long videos. This should be explicitly acknowledged as a limitation.

### Minor

- **Drop from no-memory to all-memory baseline not explained.** Table 2 shows m.tIoU drops from 16.7% (no memory, row ❶) to 9.6% (all memories without selection, row ❷). The paper simply states that "irrelevant information" is to blame, but the magnitude (below no-memory performance) suggests either optimization instability introduced by the memory cross-attention, or overfitting to noise during training when all memories are active. A brief empirical diagnosis (e.g., whether the drop holds at evaluation time only or also during training) would strengthen the argument for the selection mechanism.

- **Asymmetric impact of spatial vs. temporal memory not addressed.** Table 3 shows spatial memory selection contributes 0.9% m.tIoU gain over all-memory (22.1→23.0%), while Table 2 shows temporal selection contributes 13.4% (9.6→23.0%). Both components are listed symmetrically in the contributions list, but their impacts differ by an order of magnitude. The paper should acknowledge that temporal memory selection is the dominant driver and frame the spatial component accordingly.

### Trivial

- The spatial and temporal memory selection mechanisms contribute very differently but are listed as equal contributions in Section 1. Adjusting the emphasis would give a more accurate picture of what drives the gains.

---

## Nice-to-Haves

- An analysis of ART-STVG performance by temporal position of the target event within the long video (early/middle/late) would provide direct evidence that the streaming architecture succeeds precisely because it does not need to subsample and can locate late-occurring targets.
- A figure or table showing memory bank size growth and its effect on inference latency/memory footprint would ground the "computational bottleneck" claims made in the introduction for a system intended for practical long-video deployment.
- A per-video type or scene complexity breakdown could reveal whether selective temporal memory is more critical in videos with many distinct events.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

1. **Harsh Critic – Loss function deferred to supplementary (Minor/missing appendix)**: The paper states in Section 3.5 "Due to limited space, please see our loss function in supplementary material." Per the hard rules, the supplementary/appendix exists in the original submission; criticizing its deferral is not valid.

2. **Harsh Critic – Baseline architecture deferred to supplementary**: The Baseline architecture is described as being "in supplementary material due to limited space." Same rule applies.

3. **Harsh Critic – "Memory bank grows unboundedly" as a practical deployment concern**: The paper is an ICLR methods paper with experimental focus; inferring that unbounded growth is a fatal scalability issue (without evidence from the paper of actual GPU OOM or time blowup at the tested video lengths) is speculative. Downgraded to Nice-to-Have.

4. **Strength Finder – "competitive results on SF-STVG" as unconditional strength**: The Baseline model achieves only 46.2% m.tIoU (well below all competing methods at 53.9–60.4%), meaning the autoregressive architecture itself is at a significant disadvantage on SF-STVG. ART-STVG largely recovers this gap (59.2%), which is a real strength, but the framing as competitive must be understood relative to a significantly weaker architectural starting point.

5. **Human finder similarities** – Not applicable here as no human-finder output was supplied that identifies issues from unrelated papers.

---

## Novel Insights

The most interesting methodological insight in this paper is the inversion of performance ranking when adding unfiltered memory: Table 2 shows that injecting *all* temporal memories makes performance *worse* than having *no* memory (9.6% vs. 16.7% m.tIoU), while filtered memory achieves 23.0%. This is a strong empirical signal that in long-form video settings, irrelevant temporal context actively degrades grounding — not just fails to help — and that the boundary-aware event-centric memory selection is doing real work rather than providing marginal filtering gains. This insight generalizes beyond STVG: for any streaming localization system operating over long, multi-event videos, structured temporal segmentation of memory is more important than the memory mechanism itself.

---

## Suggestions

1. **Specify baseline inference procedures explicitly** (e.g., in a table footnote or appendix): For each competing method, state the exact number of frames seen at test time and how they are sampled from a 5-minute video. If subsampling was used, add an ablation where ART-STVG is also subsampled to the same frame count (its sequential design can accommodate this easily). This single addition would substantially resolve the central evaluation ambiguity.

2. **Acknowledge the validation-only benchmark as a limitation**: Add one sentence in Section 4 or 5 noting that the LF-STVG splits extend only the validation set, making all evaluations zero-shot (trained short, tested long). Discuss what purpose-built LF-STVG training data would require, e.g., long YouTube clips annotated with temporal and spatial grounding from scratch.

3. **Investigate and briefly explain the no-memory > all-memory phenomenon**: Even one or two sentences diagnosing whether this occurs at inference time on long or short videos, or whether it is a training-time optimization issue, would significantly strengthen confidence in the memory selection design.

---

## Score and Decision

**Calibration anchors:**

| Path | Avg Score | Round | Comparison to this paper |
|---|---|---|---|
| bEvI30Hb2W.md | 3.00 | R1 (weak) | Much weaker — no novel task, generic memory method |
| MSxCBXD5C8.md | 3.00 | R1 (weak) | Unrelated anomaly detection, clearly weaker |
| R6sIi9Kbxv.md | 4.00 | R1 (mid) | LLM video understanding, no new task, marginal contribution |
| 4j9plQoOH1.md | 4.75 | R1 (mid) | Long-video QA dataset, similar scope but no method contribution |
| YCwN7wQA6W.md | 4.25 | R1 (mid) | Temporal grounding in LLMs, less focused ablations |
| 9Cu8MRmhq2.md | 8.00 | R1 (strong) | Clearly stronger theoretical foundation, no evaluation concerns |
| 1DEHVMDBaO.md | 4.60 | R2 | Memory mechanism for long-video ViT — similar domain, weaker evaluation, weaker ablations than this paper |
| JbPb6RieNC.md | 5.80 | R2 | Streaming video LLM with memory + benchmark — similar structure (method + benchmark), accepted at 5.80 |
| tEei1bolt3.md | 5.00 | R2 | Motion-grounded video reasoning, new task + benchmark — comparable scope |
| le4IoZZHy1.md | 6.20 | R2 | Long-video benchmark only, no new method — accepted at 6.20 but narrower contribution |

**Round 1 bracket: 4.5–6.5.**

**Round 2 narrowing:** The paper is better than 1DEHVMDBaO (4.60) — the STVG paper has more focused contributions, significantly better ablations, and a new problem definition. It is comparable to tEei1bolt3 (5.00) in scope (new task + method + benchmark). It is weaker than JbPb6RieNC (5.80) because the benchmark quality is limited (validation-only) and the inference procedure ambiguity is a real concern. The paper is weaker than le4IoZZHy1 (6.20) despite having a richer method contribution, because its benchmark lacks a proper training split and the evaluation comparison has the unspecified inference issue.

The paper lands closer to 5.0 than to 5.8 due to: (1) the major evaluation ambiguity around how full-sequence baselines handle long videos at inference time (unaddressed), and (2) the benchmark's limitation to a validation-only extension. These are substantive concerns that would require non-trivial work to resolve. However, the problem formulation is genuine, the method is well-ablated and includes an important insight (unfiltered memory hurts), and the contributions are real.

**Final score: 5.0**

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>