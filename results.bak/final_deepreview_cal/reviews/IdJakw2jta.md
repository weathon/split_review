Now I have sufficient calibration. Let me write the final consolidated review.

## Summary
This paper introduces Long-Form Spatio-Temporal Video Grounding (LF-STVG), extending the task to videos of 1–5 minutes, and proposes ART-STVG, an autoregressive transformer that processes frames sequentially with spatial and temporal memory banks augmented with selection strategies. A cascaded decoder design passes fine-grained spatial information to the temporal head. On extended HCSTVG-v2 benchmarks, ART-STVG substantially outperforms existing STVG methods (e.g., 23.0 vs. 14.2 m.tIoU on LF-STVG-3min) while remaining competitive on short-form STVG.

## Strengths
1. **First systematic exploration of LF-STVG with a dedicated benchmark extension.** The paper extends the HCSTVG-v2 validation set to five lengths (1–5 minutes), creating LF-STVG-1min through LF-STVG-5min. This is the first benchmark enabling evaluation of STVG methods at minute-scale durations, directly supporting the paper's claim of opening a new problem setting.

2. **Consistent and large-margin improvements over all prior methods on long videos.** In Table 1, ART-STVG outperforms every compared method (TubeDETR, STCAT, CG-STVG, TA-STVG) across all five video lengths and all metrics. The gap grows with video length — e.g., TA-STVG drops to 7.7 m.tIoU on 5-minute videos while ART-STVG maintains 15.0 — which provides direct evidence that the autoregressive+memory framework is effective for long-form grounding.

3. **Well-ablated memory selection mechanism.** Table 2 shows that temporal memory without selection *harms* performance (16.7 → 9.6 m.tIoU), while selection recovers and exceeds it (23.0). This 13.4-point swing cleanly validates the central design claim. Spatial memory selection (Table 3) and the cascaded decoder (Table 4) are similarly ablated. These ablations give confidence that the reported gains come from the proposed components, not confounding factors.

4. **Competitive short-form performance despite long-form design.** ART-STVG achieves 59.2 m.tIoU on standard HCSTVG-v2 (20s videos), trailing the specialist TA-STVG by only 1.2 points and outperforming all other prior methods. This demonstrates that the autoregressive approach does not sacrifice short-video capability — an important sanity check for a long-video method.

## Weaknesses

### Fatal
None.

### Major

1. **How baselines were run on long videos is not specified.** The paper's central comparative claim (Table 1) rests on evaluating TubeDETR, STCAT, CG-STVG, and TA-STVG on 1–5 minute videos. These methods were designed for ~20-second clips and process all frames jointly. The paper acknowledges in the introduction that joint processing of long videos causes "computational bottlenecks because of high GPU memory requirements," yet it never describes what modifications, subsampling, or sliding-window strategies were used to make these baselines run on 960-frame (5 min @ 3.2 fps) inputs. Without this information, the reader cannot assess whether the comparisons are fair — for example, if baselines were forced to aggressively downsample frames, the degradation would be expected and would not reflect a genuine advantage of the autoregressive design. This is the single most significant gap in the evidence chain. A single sentence specifying the inference protocol (e.g., "all baselines were tested with N uniformly sampled frames per video" or "using the code's default settings") would address it.

2. **Dataset extension procedure is under-documented.** The LF-STVG datasets extend HCSTVG-v2 validation samples to 1–5 minutes using "original YouTube videos, not concatenated clips," with manual review. But key details are missing: (a) how many of the 2,000 validation videos were successfully extended, and how many were discarded (if any); (b) how temporal annotations were re-anchored from the original 20-second clips to the longer timeline; (c) whether a video with multiple occurrences of the target event was handled and how the ground-truth event was identified. While the extension effort is commendable, these omissions limit reproducibility and raise questions about annotation reliability.

### Minor

3. **Temporal memory selection algorithm is underspecified.** Section 3.4 describes detecting event boundaries via "points with lower similarities" between adjacent temporal memory features, inspired by TextTiling. The paper does not specify the threshold or detection rule (e.g., local minimum criterion, quantile threshold, or learned gate). Since Table 2 shows that this selection is responsible for a 13.4-point gain, the imprecision is a reproducibility concern. A concrete specification (even a simple heuristic with one hyperparameter) would resolve this.

4. **Baseline performance pattern on 1-minute videos is not discussed.** On LF-STVG-1min, the baseline (ART-STVG without memory) achieves 30.1 m.tIoU — *worse* than TubeDETR (32.5) and all other methods. Yet on longer videos, the baseline surpasses all competitors. This crossover pattern could simply reflect that autoregressive processing benefits longer videos more, but the paper does not explain or acknowledge it. Discussing this would strengthen the narrative.

5. **No runtime or memory comparison despite efficiency motivation.** The introduction motivates autoregressive processing partly on computational efficiency grounds ("it causes computational bottlenecks because of high GPU memory requirements for simultaneous feature learning"). Yet the paper reports no runtime or GPU memory measurements to support this claim, even on the short-form benchmark where all methods could feasibly be profiled.

### Trivial
None.

## Nice-to-Haves
- An analysis of *why* using all temporal memories degrades performance (from 16.7 to 9.6 m.tIoU) — e.g., a visualization showing which frames the selection mechanism retains vs. discards.
- A breakdown of cascaded decoder gains: does the cascade primarily improve spatial grounding, temporal grounding, or both?
- A failure analysis explaining where ART-STVG still struggles on 5-minute videos (15.0 m.tIoU indicates substantial room for improvement).

## Removed Points
These points were raised by reviewers but are not included as weaknesses in the main review. Treat them with caution:
- *"The paper never justifies that query features capture event-level changes rather than frame-level appearance differences"* — The temporal memory selection mechanism is conceptually grounded in TextTiling, and Figure 6 provides qualitative support. The claim is not critical to the method's validity.
- *"N_s choice is not discussed"* — N_s is ablated in Table 5 (16/32/48); the paper picks 32 as optimal. This is sufficient.
- *"Missing related work"* — Cannot verify without external sources.
- *"Formatting/style nitpicks"* — Parser artifacts, not author errors.
- *"Code release promise is noted but the paper itself should enable replication"* — Code release is standard practice and the paper provides substantial architectural detail; requesting full replication from the paper text alone is excessive for a systems paper.
- *"Generalization beyond HCSTVG-v2"* — The paper explains that HCSTVG-v2 is the only dataset providing source videos for extension. This is a practical constraint, not an oversight.
- *"All metrics drop sharply as video length increases"* — This is a consequence of task difficulty; the paper presents it as such. The key comparison is against baselines, not absolute numbers.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. In the main text or supplementary, add one sentence specifying exactly how each baseline was run on long videos (frame count, subsampling, GPU configuration). This is the single change that would most strengthen the paper.
2. Provide dataset extension statistics: number of videos extended, number discarded, and how temporal annotations were mapped to the longer timeline.
3. Specify the temporal memory boundary detection rule concretely (e.g., "a boundary is marked when cosine similarity between consecutive temporal memories falls below the 20th percentile of all pairwise similarities").
4. Include a table of runtime/memory for ART-STVG vs. baselines on at least the short-form benchmark.

## Score and Decision

### Calibration Report

**Round 1 (Bracketing):** Queried three bands on spatio-temporal video grounding / long-form video understanding / autoregressive memory.

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| 2HdZPEQUig (Object-Centric Learning) | 3.00 | R1 | Much weaker — marginal video contribution, low scores. Current paper is clearly stronger. |
| ICR3swcnaa (Action Recognition STD-Former) | 3.00 | R1 | Rejected paper on a separate task. Current paper is far more coherent and better evaluated. |
| MSxCBXD5C8 (Anomalous Action Recognition) | 3.00 | R1 | Similar score band. Current paper has stronger contributions. |
| bEvI30Hb2W (LVM-NET long video) | 3.00 | R1 | Rejected paper on long video reasoning. Current paper has more thorough evaluation. |
| xYzOkOGD96 (Grounded Video Caption) | 3.83 | R1 | Rejected paper on grounded captioning. Current paper cleaner in contribution. |
| 14fFV0chUS (TRACE temporal grounding) | 6.75 | R1 | Accepted paper on video temporal grounding. TRACE has clearer methodology; current paper has larger evaluation gaps. Current paper is slightly weaker. |
| 1DEHVMDBaO (Adaptive Memory ViT) | 4.60 | R1 | Rejected paper. Current paper is substantially stronger in both results and ablation. |
| wkbx7BRAsM (AR Transformers zero-shot video) | 7.00 | R1 | Accepted paper. Different domain (video imitation). Current paper is not as strong. |
| 9Cu8MRmhq2 (Multi-granularity Correspondence) | 8.00 | R1 | Strong accept. Significantly more rigorous evaluation. Current paper is below this. |

**Round 1 bracket:** Narrowest plausible range is **4.5–6.75**. The paper is clearly above the reject-level papers (3.0–4.6) and below the strong accepts (7.5+).

**Round 2 (Narrowing):** Queried inside (4.5, 6.0) and (5.5, 7.5) on spatio-temporal grounding and autoregressive video topics.

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| tEei1bolt3 (Motion-Grounded Video Reasoning) | 5.00 | R2 | Rejected paper. Similar task novelty but weaker experiments. Current paper is stronger. |
| a1P5kh2oo8 (Vinoground) | 5.75 | R2 | Rejected benchmark paper. Different contribution type. Current paper has clearer method contributions. |
| yHj6EunfVQ (CoSPaL WSTVG) | 5.50 | R2 | Weakly supervised STVG paper. Similar domain. Current paper has comparable rigor but a clearer task contribution. |
| QWDFOOoV3U (ResidualViT) | 5.75 | R2 | Rejected paper on temporal grounding. Current paper is more complete. |
| le4IoZZHy1 (CG-Bench) | 6.20 | R2 | Accepted benchmark paper. Similar-level documentation gaps but stronger dataset. Current paper comparable in quality. |
| 8pusxkLEQO (ARLON video generation) | 6.25 | R2 | Accepted paper. Different domain. Similar level of methodological contribution and gap documentation. |
| QETk0lBdVf (Long Context Transfer) | 5.80 | R2 | Rejected paper. Current paper has stronger results. |

**Final score determination:** The paper sits between CoSPaL (5.50) and TRACE/CG-Bench (6.20–6.75). It is stronger than the 5.50 paper because its results are cleaner and its task definition is more novel. It is slightly weaker than TRACE (6.75) because of the unaddressed evaluation protocol gap. Comparing to CG-Bench (6.20, accepted), the current paper has similar documentation gaps but contributes a method rather than just a benchmark, which is arguably a harder contribution to validate. **Score: 6.0.**

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>