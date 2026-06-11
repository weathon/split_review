Now I have all the calibration data I need. Let me write the final consolidated review.

## Summary

This paper introduces Long-Form Spatio-Temporal Video Grounding (LF-STVG), extending STVG from 20-second clips to 1–5 minute videos, and proposes ART-STVG, an autoregressive transformer with spatial/temporal memory banks and a cascaded decoder design. The method processes frames sequentially, uses text-guided memory selection to retrieve relevant past context, and funnels spatial grounding output into the temporal decoder. On extended HCSTVG-v2 benchmarks, ART-STVG outperforms existing short-form STVG methods on longer videos while maintaining competitive short-form performance.

## Strengths

1. **Autoregressive streaming with memory shows clear advantages over all-at-once methods as videos lengthen.** Tab. 1 shows that as video length increases from 1min→5min, the best existing method (TA-STVG) drops from 38.4→7.7 m.tIoU (~80% relative decline), whereas ART-STVG drops from 39.1→15.0 (~62% relative). The gap widens monotonically (+0.7 at 1min, +7.3 at 5min). This directly validates the core thesis that frame-by-frame autoregressive processing is better suited for long-form STVG.

2. **Strong ablation evidence for the temporal memory selection mechanism.** Tab. 2 (rows ❶–❸) shows a striking result: using all temporal memories degrades performance _below_ the no-memory baseline (16.7→9.6 m.tIoU, a 7.1-point drop), while the proposed selection strategy recovers and exceeds it (9.6→23.0, +13.4 points). This provides non-trivial evidence that memory selection is essential — not merely a refinement — for the temporal decoder.

3. **Cascaded spatial→temporal decoder design demonstrably outperforms the parallel design used by prior methods.** Tab. 4 reports cascaded achieves 23.0 vs. parallel 21.5 m.tIoU (+1.5), directly supporting the claim that funneling fine-grained spatial target information into temporal localization helps in long videos.

4. **Competitive short-form performance confirms the autoregressive design does not sacrifice standard-task capability.** Tab. 7 shows ART-STVG at 59.2/39.2 vs. the state-of-the-art TA-STVG at 60.4/40.2 (within 1.2/1.0 points), while outperforming CG-STVG, STVGFormer, and others. This addresses a natural concern about streaming architectures on short videos.

## Weaknesses

### Major

1. **Central empirical comparison confounds architectural superiority with distribution robustness.** All baseline methods (TubeDETR, STCAT, CG-STVG, TA-STVG) are trained on the original HCSTVG-v2 training set (20-second clips) and tested on videos 3–15× longer. These methods were designed and tuned for the short-form regime; testing them far outside their training distribution guarantees a disadvantage that is not purely architectural. Tab. 6 (training all methods on 40-second clips and testing on 3-minute videos) partially mitigates this — ART-STVG still leads (28.3 vs. 20.7 m.tIoU for TA-STVG) — but even there the test set remains well beyond the 40-second training distribution for all methods. The paper frames its main result (Tab. 1) as showing ART-STVG "significantly outperforms" existing approaches, but the current evidence cannot distinguish between genuine architectural superiority and differential robustness to distribution shift. A controlled comparison where existing methods are reasonably adapted to long videos (e.g., sliding-window inference with aggregation) would substantially strengthen the claim.

### Minor

2. **Temporal decoding pipeline underspecified.** The model predicts per-frame start/end probabilities \(h_i \in \mathbb{R}^2\) (Eq. 7), but the paper never explains how these per-frame signals are converted into a single predicted temporal interval for tIoU computation. Thresholding? Smoothing? Non-maximum suppression? This is a non-trivial design choice that directly affects all reported tIoU numbers. (The loss function is deferred to supplementary material, which is acceptable, but the inference-time temporal aggregation should be in the main paper.)

3. **Memory bank grows without bound.** Section 3.3 states the memory bank is updated by "simply adding the query as a new memory, without removing any existing memories." For a 5-minute video at 3.2 FPS (~960 frames) with \(K\) decoder blocks, the bank accumulates \(K \times 960\) entries. While only \(N_s=32\) memories are selected per step via attention, the bank itself grows unbounded, and the paper provides no discussion of practical limits, computational scaling, or whether a forgetting/eviction mechanism would be needed for longer videos.

4. **Static text-based spatial memory selection has a blind spot.** Spatial memory selection is based on similarity between each stored memory and the _textual feature_ (Sec. 3.3, Fig. 4a). Since the text query is fixed across all frames, the similarity scores are static with respect to memory content. This means the selection effectively retrieves "which past frames had visual features text-similar to the query," which could miss frames where the target's appearance changes substantially (e.g., pose change, occlusion, lighting shift). The strong results in Tab. 3 suggest this heuristic works in practice, but the limitation deserves discussion.

5. **"All memories" temporal baseline collapse is not deeply analyzed.** Tab. 2 shows that adding all temporal memories drops performance from 16.7→9.6 m.tIoU — a 7.1-point _decrease_ from having no temporal memory at all. The paper attributes this to irrelevant information, but the magnitude suggests a more systematic issue: perhaps the temporal cross-attention attends to the wrong memories in a structurally harmful way. An analysis of attention weights or a diagnosis of what goes wrong would strengthen the paper.

6. **No confidence intervals or variance reported.** With ~400 test samples per video length (2,000 validation samples split across five lengths), the numerical differences between methods could be within noise. Single-run results without variance or statistical significance testing weaken the reliability of the reported rankings.

7. **Extended dataset construction details are sparse.** The paper states the extensions are "based on original YouTube videos, not concatenated clips" and manually reviewed, but does not describe how longer segments were selected from source videos (e.g., are they temporally centered on the original 20-second clip? arbitrarily selected?), or explicitly commit to releasing the extended annotations. This affects reproducibility.

### Trivial

8. The motion backbone (VidSwin-tiny) is frozen during training without justification. Given the temporal decoder relies on RoI-pooled motion features, unfreezing or fine-tuning it could yield further gains.

## Nice-to-Haves

- **Controlled comparison with adapted baselines:** The single highest-value improvement would be to adapt existing methods to long videos (e.g., sliding-window chunking or training on matched-length clips) and compare against ART-STVG under those conditions. This would directly address the main evaluation concern.
- **Qualitative failure analysis:** The paper reports aggregate metrics but provides no concrete examples comparing where ART-STVG succeeds and baselines fail. A few visual examples with attention maps (beyond Fig. 5) would ground the claims.
- **Computational cost comparison:** The introduction motivates ART-STVG partly on computational grounds ("computational bottlenecks," "high GPU memory requirements"), but no runtime or memory measurements are provided.
- **Discussion of the baseline crossover:** The "Baseline (ours)" (autoregressive w/o memory) underperforms existing methods on LF-STVG-1min (30.1 vs. TA-STVG 38.4 m.tIoU) but overtakes them on longer videos. This is an interesting finding about the value of the autoregressive design itself vs. the memory components, and deserves discussion.

## Removed Points

The following points raised by reviewers were filtered under the review consolidation rules:

- **"Absolute performance numbers are low and their practical meaning is unclear"** — This criticism is generic and could apply to any novel-task paper establishing first baselines. The paper does not claim production-ready performance.
- **"No annotation protocol is described"** at the level the harsh critic demanded — The videos are extended from source YouTube videos (not new annotations created), with annotations inherited from the original HCSTVG-v2 validation set. The setup is standard for extending grounding benchmarks.
- **"The loss function and baseline architecture are deferred to supplementary"** — Removed because the parser strips appendices from all papers; these exist in the original submission.
- **"Dataset release not promised"** — The paper commits to releasing code and models; dataset release is not explicitly promised but the paper does not say it won't be released.
- **Strength: "Fair evaluation protocol with all methods trained on identical 20-second data"** — Dropped because the major weakness about comparison fairness conflicts with this claimed strength.
- **Several formatting/style criticisms** — Removed as parser artifacts.
- **Several overly generic "Strengthening the Paper" points** — Moved to Nice-to-Haves.

## Novel Insights

Both reviewers correctly identify the key tension: the paper's strongest empirical claim (that ART-STVG "significantly outperforms" existing methods on long videos) rests on an experimental design that necessarily disadvantages existing methods by testing them outside their design regime. However, this tension is partly inherent to introducing a new task variant — there is no established evaluation protocol for LF-STVG, and any first comparison will involve methods not designed for it. The paper's Tab. 6 (training on 40-second clips) is a genuine attempt to address this, but it remains a partial fix. The more interesting insight is that the ablations (Tab. 2-5) provide strong internal validity for the method's components even if the external comparison against baselines is imperfect. The temporal memory selection finding — where adding _more_ information (all memories) actively _harms_ performance — is particularly noteworthy and suggests a fundamental challenge for memory-augmented transformers in long-video settings that deserves deeper investigation.

## Suggestions

1. **Run baselines with a sliding-window adaptation:** Process long videos in 20-second chunks with existing methods and aggregate predictions (e.g., via NMS or voting). This directly addresses the fairness concern and would isolate whether ART-STVG's advantage is architectural or merely due to out-of-distribution testing.
2. **Add a "fair comparison" table where all methods are trained on 1-minute+ clips** (not just 40-second as in Tab. 6), even if computational limits require a subset. This would be the cleanest test of the central claim.
3. **Specify the temporal decoding procedure** (per-frame probabilities → interval) explicitly in the main paper.
4. **Add confidence intervals** (e.g., bootstrapping) for the main Tab. 1 results given the small per-length test sets (~400 samples).
5. **Include a computational cost comparison** (training time, inference throughput, GPU memory) to support the computational motivation in the introduction.
6. **Add a qualitative analysis** with successful and failed cases to build intuition about when the autoregressive+memory design helps.

## Score and Decision

**Calibration anchors (all rounds):**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| MI0UiWeqOl (Poly-Autoregressive Modeling) | 2.33 | R1 | Much weaker; methodologically flawed |
| ReccFdn4zE (Cross Attention Odd Shapes) | 2.00 | R1 | Much weaker; domain mismatch |
| N581Nje6fH (Long Horizon Episodic) | 1.50 | R1 | Much weaker |
| ARVideo (3.40) | 3.40 | R2 | Weaker; incremental contribution to self-supervised video |
| xYzOkOGD96 (Grounded Video Caption) | 3.83 | R1/R2 | Weaker; limited model comparison |
| Wto5U7q6I2 (TemporalBench) | 4.20 | R2 | Weaker; benchmark-only paper |
| 1DEHVMDBaO (Adaptive Memory) | 4.60 | R2 | Weaker; marginal improvements, missing ablations |
| tEei1bolt3 (Motion-Grounded Video Reasoning) | 5.00 | R1/R2 | Comparable; both new tasks with evaluation concerns |
| O8FkMqNF1M (Language Repository) | 5.50 | R1 | Comparable; similar quality, different issues |
| QETk0lBdVf (Long Context Transfer) | 5.80 | R2 | Slightly stronger; clearer empirical story |
| 8pusxkLEQO (ARLON) | 6.25 | R1 | Stronger; accepted |
| 14fFV0chUS (TRACE) | 6.75 | R1/R2 | Stronger; cleaner evaluation, accepted |

**Round 1 bracket:** (4.5, 6.0)

**Round 2 narrowing:** The paper is clearly above the 3.83 and 4.60 anchors and comparable to the 5.00–5.50 anchors. It is weaker than the accepted anchors at 6.25–6.75 due to the evaluation fairness concern. The paper has genuine contributions (new task, well-motivated architecture, strong ablations) but the central empirical claim is undermined by a comparison that necessarily disadvantages baselines. This places it in the borderline-reject range.

**Final score:** 5.0

**Decision rationale:** The paper introduces a worthwhile problem and a well-designed method, but the evaluation does not convincingly support the strongest claim ("significantly outperforms") due to an unfair baseline comparison that the Tab. 6 mitigation only partially addresses. The missing temporal decoding specification and lack of confidence intervals further weaken the empirical contribution. The method and task are promising, but the paper requires substantial revisions to the evaluation design before its claims can be accepted.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>