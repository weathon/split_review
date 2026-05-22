Now I have enough information to synthesize the final review. Let me produce it.

## Summary

This paper introduces Long-Form Spatio-Temporal Video Grounding (LF-STVG), extending short-form STVG to videos of 1–5 minutes, and proposes ART-STVG, an autoregressive transformer that processes frames sequentially with spatial and temporal memory banks. The memory banks use text-guided similarity selection (spatial) and event-boundary detection (temporal) to retrieve relevant context. A cascaded spatio-temporal decoder connects spatial grounding to temporal localization via ROI pooling. On extended HCSTVG-v2 benchmarks, ART-STVG substantially outperforms prior methods (e.g., +9.1 m.tIoU over TA-STVG on 3min), while remaining competitive on short-form STVG.

## Strengths

- **First systematic treatment of long-form STVG with a purpose-built architecture.** Unlike prior STVG methods that process all frames at once (which is infeasible for multi-minute videos), ART-STVG's autoregressive streaming design naturally accommodates variable-length inputs. Table 1 and Figure 2 show the performance gap over prior methods widens as video length increases from 1 to 5 minutes (e.g., from +0.7/+0.9 to +7.3/+5.5 m.tIoU/m.vIoU), directly supporting the claim that the architecture is better suited for long videos.

- **Memory selection strategies are validated to be critical through careful ablation.** Table 2 shows that using all temporal memories collapses performance to 9.6 m.tIoU (worse than no memory at 16.7), while selective temporal memory raises it to 23.0 — a 6.3-point gain over the no-memory baseline and 13.4 over the all-memory variant. Table 3 shows a similar though smaller pattern for spatial memory (+1.7 over no memory, +0.9 over all memories). These ablations isolate the contribution of each component.

- **Cascaded spatio-temporal decoder provides consistent improvements.** Table 4 shows the cascade design outperforms a parallel design by 1.5 m.tIoU and 1.4 m.vIoU, supporting the idea that fine-grained spatial information from the spatial decoder helps temporal localization in long videos.

- **Competitive short-form performance despite being designed for long videos.** Table 7 shows ART-STVG (59.2 m.tIoU, 39.2 m.vIoU) is within 1.2% of the current SOTA (TA-STVG, 60.4/40.2) on HCSTVG-v2, demonstrating the autoregressive design does not sacrifice short-video capability.

- **Thorough hyperparameter analysis.** Table 5 systematically varies N_s (number of selected spatial memories), identifying the optimal value and showing the model is not overly sensitive to this choice (22.5–23.0 m.tIoU across 16–48).

## Weaknesses

### Major

- **Insufficient documentation of the dataset extension's ground-truth handling.** The paper extends the HCSTVG-v2 validation set from 20-second clips to 1–5 minute videos by sourcing longer segments from the original YouTube videos. It states "we manually review the extended videos to ensure their quality" but does **not** explain the annotation mapping process: How are the original spatial (bounding box) and temporal (start/end) annotations adapted for the longer videos? Are frame-level box annotations simply carried over with adjusted timestamps? Are new frames outside the original 20-second window assigned any ground truth? Without this clarification, a reader cannot fully verify the validity of the LF-STVG evaluation. The paper should describe the remapping procedure, any quality checks performed on re-annotated data, and whether any samples were discarded. This is the most significant weakness and should be resolved in a revision or rebuttal.

- **The computational motivation for the autoregressive design is asserted but not demonstrated.** The Introduction claims existing methods "cause computational bottlenecks because of high GPU memory requirements for simultaneous feature learning and target localization in all video frames," and that ART-STVG resolves this. Yet the paper provides no GPU memory measurements, no inference time comparisons, and no throughput analysis for videos of varying lengths. Since all methods (including ART-STVG) are trained on 20-second clips and tested on longer videos, the claimed computational advantage is never directly tested. The paper would be strengthened substantially by reporting peak GPU memory and per-frame runtime for ART-STVG vs. a non-autoregressive baseline at multiple video lengths.

### Minor

- **Temporal memory ablation framing is somewhat misleading.** Table 2 shows the selective temporal memory achieves 23.0 m.tIoU, which the paper reports as "13.4% gains (❷ v.s. ❸)." However, ❷ (all memories, 9.6) is a degraded state — worse than the "no memory" condition (❶, 16.7). The gain *from the relevant baseline* (no memory → selective memory) is +6.3, which is still substantial but significantly smaller than the headline 13.4. The paper should reframe this result transparently, noting that memory selection recovers from a degraded state and provides a net +6.3 over no memory.

- **Spatial memory bank grows without bound.** The paper explicitly states: "we update the memory bank by simply adding the query as a new memory, without removing any existing memories" (Sec. 3.3). While the *decoding* uses only the top N_s=32 memories, the *selection step* computes similarity between the text query and every memory — an operation linear in video length. For a 5-minute video at 3.2 fps (960 frames × K decoder blocks), this could involve tens of thousands of similarity computations per frame. The paper should either analyze this cost, introduce a forgetting mechanism or fixed-capacity buffer, or acknowledge this as a limitation.

- **No analysis of where ART-STVG fails.** The paper reports aggregate metrics but does not analyze failure modes (e.g., queries referring to early vs. late events, cases where event boundary detection fails, or queries involving objects that appear intermittently). Such analysis would help the community understand the method's limitations and guide future work.

### Trivial

- The baseline is described as "similar architecture to our ART-STVG but without memory and memory selection modules" with details deferred to supplementary. Since the baseline's strong improvement over prior methods on LF-STVG (e.g., 16.7 vs. 13.6 on 3min) suggests the autoregressive design itself is beneficial, this should be discussed transparently in the main paper.

## Nice-to-Haves

- A comparison with a simple chunking baseline (e.g., split long video into 20-second windows, run a standard STVG method per window, aggregate results) would help disentangle whether ART-STVG's advantage comes from the autoregressive design or simply from avoiding the information overload of processing all frames.
- Reporting results with error bars or multiple seeds would improve reliability, though single-run evaluation is standard in this field.
- The temporal memory selection uses heuristic boundary detection (cosine similarity of adjacent memories). An ablation comparing this to a learned boundary predictor or alternative segmentation methods would strengthen the contribution.

## Removed Points

- **Equation (1) feature ordering "error":** The harsh critic noted the appearance feature appears twice and motion is missing from the braces. This is a PDF parsing artifact; the text and surrounding context clearly describe all three features (appearance, motion, textual). The equation formatting is a parser issue, not an author error.
- **Criticism about only extending the validation set (not training set):** The paper explicitly explains this is because HCSTVG-v2's test annotations are not public, and results are conventionally reported on the validation set. Extending the validation set for evaluation while training on the original training set is a standard evaluation protocol for domain/task shifts.
- **"Any autoregressive design helps" criticism of baseline:** The baseline is described as having the same architecture minus memory — it is therefore autoregressive by construction. The paper explicitly frames the baseline as measuring the contribution of memory/selection, which is fair. The baseline's improvement over prior methods is an interesting finding but not a flaw.
- **Missing related works / comparison to memory mechanisms from VQA:** The paper adequately cites and distinguishes from related work in the Related Work section. Recommending additional comparisons to methods outside the paper's stated scope is scope creep.
- **Formatting/style nitpicks:** All typos, grammar issues, broken references ("see supplementary material"), and presentation concerns are parser artifacts from PDF extraction, not author errors.

## Novel Insights

The harsh critic's observation about the temporal memory ablation — that the 13.4% gain is measured from the degraded all-memory state rather than the no-memory baseline — is a genuinely insightful catch that the paper's own framing obscures. The net improvement of selection over no memory is +6.3 (not +13.4), which is still meaningful but changes the narrative from "memory selection is critical" to "memory selection recovers from information overload and adds moderate gains." The paper's strength is not diminished by this reframing, but future versions should adopt the more honest baseline. Additionally, the observation that the baseline (autoregressive, no memory) already outperforms all prior methods on 3+ minute videos suggests that the streaming design itself — independent of the memory contributions — may be the primary driver of long-video capability, with memory selection providing a meaningful but secondary refinement. The paper does not sufficiently disentangle these effects.

## Suggestions

1. **Clarify the dataset extension protocol:** Provide a step-by-step description of how ground-truth spatio-temporal annotations are mapped from original 20-second clips to the extended 1–5 minute videos. If annotations are simply carried over with adjusted temporal offsets, state this explicitly. Report any quality checks or rejection criteria.

2. **Report GPU memory and runtime:** Add a table or figure showing peak GPU memory consumption and per-frame inference time for ART-STVG vs. a representative non-autoregressive method (e.g., TubeDETR) at various video lengths (20s, 1min, 3min, 5min). This directly validates the claimed computational motivation.

3. **Reframe the temporal memory ablation:** Present the improvement from the no-memory baseline (❶→❸, +6.3 m.tIoU) alongside the recovery from the all-memory condition (❷→❸, +13.4) to give a complete picture.

4. **Acknowledge and bound the memory growth issue:** Either implement a forgetting mechanism, set a fixed capacity for the memory bank, or explicitly analyze the computational cost of the text-to-memory similarity computation as video length grows.

## Score and Decision

**Calibration report:**

Round 1 bracket: Searched for anchors in three score bands. Weak anchors (score < 3.5) were substantially weaker than the paper — action recognition papers scoring 3.0 with basic methodologies. Middle anchors (3.5–7.5) included TRACE (6.75, Accept), "Look, Remember and Reason" (6.50, Accept), ARLON (6.25, Accept), Motion-Grounded (5.00, Reject), ResidualViT (5.75, Reject). Strong anchors (>7.5) were in different subfields (gesture generation, portrait animation, GUI grounding) with average scores 7.75–8.50.

Round 2 narrow: Queried (4.5–6) and (6–7.5) bands on video grounding topics. Read anchors: TRACE (6.75), ARLON (6.25), "Look, Remember and Reason" (6.50), Vinoground (5.75).

- **TRACE (6.75):** VTG via causal event modeling with video LLMs. Also had documentation clarity concerns but strong results. ART-STVG is comparably thorough in experiments but has a dataset documentation gap that TRACE does not. **ART-STVG is slightly weaker → 6.0–6.25.**
- **ARLON (6.25):** Autoregressive + diffusion for long video generation. Had missing ablation and missing efficiency analysis. ART-STVG has stronger ablations but a similar documentation weakness. **Comparable → 6.0–6.25.**
- **"Look, Remember and Reason" (6.50):** Grounded video reasoning with surrogate tasks. Strong methodology but tested on simple/synthetic datasets. ART-STVG uses real-world data with more extensive evaluations. **Comparable → ~6.25.**
- **Vinoground (5.75):** Benchmark paper, novelty concerns. ART-STVG is a method paper with stronger novelty. **ART-STVG is stronger → above 5.75.**

Final bracket: 5.75–6.5. The paper sits at the middle-to-upper end: clear contributions (first LF-STVG work, novel architecture, strong empirical validation) are held back by a significant documentation gap (dataset annotation process) and a missing experiment (computational efficiency). Comparable to ARLON (6.25) and slightly weaker than TRACE (6.75) due to the dataset documentation issue.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>