Here is my final consolidated review.

## Summary

This paper introduces Long-Form Spatio-Temporal Video Grounding (LF-STVG), a new problem setting where the target must be localized in videos spanning 1–5 minutes rather than the typical <1 minute. The authors propose ART-STVG, an autoregressive transformer that processes frames one at a time with spatial and temporal memory banks and selective memory strategies. On extended LF-STVG benchmarks, ART-STVG substantially outperforms existing STVG methods (e.g., 15.0 vs. 7.7 m.tIoU on 5-minute videos) while remaining competitive on short-form STVG.

## Strengths

1. **First to formally define and tackle LF-STVG.** The paper explicitly identifies a gap between existing STVG research (videos <1 minute) and practical needs (minutes-to-hours), and it is the first to explore the long-form setting. This provides a clear basis for future work in this direction.

2. **Clean and well-motivated architectural design.** The autoregressive frame-by-frame processing is a principled choice for long videos — it avoids the GPU memory bottleneck of processing all frames at once and naturally handles arbitrary video lengths. The spatial and temporal memory banks with selective retrieval are simple yet effective, and the cascaded spatio-temporal decoder (using spatial output to assist temporal localization) is a sensible design improvement over parallel decoders.

3. **Strong and widening empirical margins.** The performance gap over existing methods grows with video length: on LF-STVG-1min, ART-STVG leads TA-STVG by 0.7 m.tIoU; on LF-STVG-5min, the gap widens to 7.3 m.tIoU (Table 1). The gap is even larger in the training-on-longer-videos setting (Table 6: 28.3 vs. 20.8 m.tIoU). This trend directly supports the core claim that autoregressive streaming with selective memory is increasingly beneficial for longer videos.

4. **Comprehensive ablations validating key design choices.** The ablation study convincingly demonstrates the contribution of each component:
   - Selective temporal memory: +13.4 m.tIoU over using all memories (Table 2)
   - Selective spatial memory: +0.9 m.tIoU over all memories (Table 3)
   - Cascaded decoder: +1.5 m.tIoU over parallel (Table 4)
   - The N_s parameter is stable across a reasonable range (Table 5)

5. **Competitive short-form performance.** ART-STVG achieves 59.2 m.tIoU on HCSTVG-v2 (vs. SOTA TA-STVG at 60.4), demonstrating that the autoregressive design does not sacrifice short-video capability.

## Weaknesses

### Fatal

None.

### Major

1. **Single-dataset evaluation limits generalizability.** All LF-STVG results come from extending the HCSTVG-v2 validation set only. The paper acknowledges this ("it is the only dataset which provides available source videos"), but it means the long-form claims rest entirely on one domain (complex multi-person YouTube scenes). Generalizability to other long-video settings (surveillance, egocentric, movies) is untested. This is the most significant limitation of the current evaluation.

2. **No variance or statistical significance reporting.** All tables report single-run results. Given the large swings in ablations (e.g., no temporal memory → all memories → selective memory: 16.7 → 9.6 → 23.0 m.tIoU), it is important to know whether these differences are stable across runs. This is standard practice for empirical papers and would substantially strengthen confidence in the results.

### Minor

1. **The temporal memory collapse (16.7 → 9.6) merits deeper analysis.** The paper correctly attributes this to "irrelevant information" from multiple events. However, a 7.1-point drop from simply including extra memories is unusually large and suggests the cross-attention in the temporal decoder is sensitive to distractor content. While the selection mechanism recovers to 23.0, a brief analysis of why the drop is this severe (e.g., attention weight distribution with vs. without selection) would increase trust in the architecture's robustness.

2. **No runtime or memory comparison.** The paper motivates ART-STVG partly by "computational bottlenecks" of full-video methods, yet never reports GPU memory, training time, or inference speed. For a method that processes frames one at a time, runtime comparison against batch-processing baselines is important to validate the claimed practical advantage.

3. **The temporal boundary detection heuristic is not ablated.** Temporal memory selection uses adjacent cosine similarity to detect event boundaries, with an implicit threshold. The paper does not study sensitivity to this threshold or compare against alternatives. While this is a reasonable heuristic, the lack of any analysis leaves open the question of how robust performance is to this design choice.

4. **Unbounded memory bank growth.** The paper inserts all past query memories without removal or summarization. A brief discussion of truncation strategies for hour-long videos would be appropriate, even if it is outside the current scope.

### Trivial

None.

## Nice-to-Haves

- Adding a second source of long-form videos (e.g., extending portions of VidSTG or adapting clips from Ego4D with synthetic queries) would greatly strengthen generalizability.
- Reporting standard deviations over 3 seeds for main tables and key ablations.
- Providing inference wall-clock time and peak GPU memory for a 3-minute video across methods.
- Ablating the temporal boundary detection threshold.

## Removed Points

These points were raised in the input reviews but are removed or downgraded for the reasons stated:

- **"Multimodal encoder mixes modalities without cross-modal alignment, could dilute positional structure"** — This is speculative. The approach is standard concatenation + self-attention, which works well empirically (competitive short-form results). No evidence of harm is presented.
- **"The paper does not comment on why the temporal memory drop is this severe"** — The paper *does* comment: "This is because the long-term video often contains multiple events, and using all temporal memories may introduce irrelevant information." The criticism about magnitude is kept (Minor weakness 1 above), but the claim that it is unaddressed is factually wrong.
- **"Missing related works"** — Per instructions, I cannot verify this without external sources.
- **"Formatting/presentation nitpicks"** — Removed as parser artifacts or non-substantive.
- **"Strawman weaknesses"** about hyperparameters not being disclosed for baselines — The paper states baselines were trained using "provided source codes," which is standard practice.
- **"General claim that evaluation lacks rigor"** — Too broad. Replaced with specific, verifiable weaknesses above.

## Novel Insights

The harsh critic identified a genuinely interesting pattern: the Baseline (ours) in Table 1 without any memory already outperforms prior methods on the longest videos (e.g., 9.2 vs. 7.7 m.tIoU on 5min). This suggests the autoregressive streaming structure itself provides a significant advantage over batch-processing methods on long videos, independent of the memory mechanisms. The paper mentions this but does not highlight it as a finding — yet it is a clean signal that the core design choice (streaming vs. all-at-once) is the right one for this task. The memory selection then adds substantial additional gains on top.

## Suggestions

1. **Add variance reporting.** Report mean ± std over 3 seeds for Table 1 (LF-STVG benchmarks), Table 2 (temporal memory ablation), and Table 6 (training on longer videos). This would address the most actionable concern about result reliability.

2. **Add a runtime/memory table.** Report inference wall-clock time and peak GPU memory for a representative 3-minute video for ART-STVG and the main baselines (TubeDETR, STCAT, TA-STVG). This would validate the computational motivation.

3. **Analyze the temporal memory collapse.** Add a brief analysis (even in the supplementary) showing attention weight statistics with vs. without temporal memory selection — e.g., average attention entropy or the fraction of attention mass on relevant event boundaries.

4. **Acknowledge and bound the single-dataset limitation more explicitly.** A paragraph discussing which video domains the method is expected to transfer to and which it might struggle with would strengthen the paper's intellectual honesty.

5. **Provide the temporal boundary detection threshold** (implicitly used in the text) and a brief sensitivity analysis.

## Score and Decision

**Round 1 bracket (calibration):** After querying three bands (weak ≤3, middle 4–7, strong ≥8) with topic-matched search, the paper clearly does not fall in the weak or strong bands. The most relevant anchors in the middle band are STVG-R1 (4.67, Accept Poster), VTG-Reasoner (4.00, Reject), HiTeA (5.50, Accept Poster), Memento (5.50, Accept Poster), Invert4TVG (6.00, Accept Poster), and OmniSTVG (6.67, Accept Poster).

**Round 2 narrowing:** Reading the full reviews for these anchors shows ART-STVG is:
- Clearly stronger than STVG-R1 (4.67) — cleaner method, defines a new problem
- Comparable to HiTeA (5.50) and Memento (5.50) — similar level of contribution and rigor
- Slightly weaker than Invert4TVG (6.00) — Invert4TVG has stronger multi-dataset validation
- Weaker than OmniSTVG (6.67) — OmniSTVG contributes a large new dataset (10K videos) alongside its task definition

**Final score:** 6.0. The paper pioneers a new problem with a well-designed method and strong results, but is held back by single-dataset evaluation and missing variance/runtime reporting. This is a solid poster-level contribution — the core idea is sound, and the weaknesses are clearly addressable.

**Anchors used:**
- `/home/wg25r/review_agent/human_reviews_2026/IeqzZmCG9y.md` (3.00, Round 1) — Unrelated paper; much weaker
- `/home/wg25r/review_agent/human_reviews_2026/zuPxAZgT9F.md` (4.67, Rounds 1,2) — STVG-R1; similar domain but less novel method; ART-STVG is stronger
- `/home/wg25r/review_agent/human_reviews_2026/vIecIscDJf.md` (5.50, Rounds 1,2) — HiTeA; training-free long-video grounding; comparable quality
- `/home/wg25r/review_agent/human_reviews_2026/PaMyTXkyY4.md` (4.00, Round 1) — VTG-Reasoner; long-video grounding with RL; ART-STVG is stronger
- `/home/wg25r/review_agent/human_reviews_2026/QQCrZXWG9s.md` (6.00, Rounds 1,2) — Invert4TVG; temporal video grounding; similar quality but stronger multi-dataset eval
- `/home/wg25r/review_agent/human_reviews_2026/FtdbdoGbk3.md` (5.50, Round 2) — Memento; streaming video with memory; comparable approach philosophy
- `/home/wg25r/review_agent/human_reviews_2026/azcQJtcYTE.md` (6.67, Round 2) — OmniSTVG; new STVG task with large dataset; stronger benchmark contribution
- `/home/wg25r/review_agent/human_reviews_2026/BOFzC3xndr.md` (4.67, Rounds 1,2) — ViTL; long-video QA; less relevant domain
- `/home/wg25r/review_agent/human_reviews_2026/D6v3B6oTDA.md` (5.00, Round 2) — Video-STR; spatio-temporal reasoning with RL
- `/home/wg25r/review_agent/human_reviews_2026/CxpKHWqT1n.md` (5.00, Round 2) — MomentSeg; video segmentation
- `/home/wg25r/review_agent/human_reviews_2026/95sD6KKq51.md` (6.00, Round 2) — ScaleLong; long-video understanding benchmark

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>