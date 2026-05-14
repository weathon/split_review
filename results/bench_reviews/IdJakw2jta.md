## Summary
The paper introduces Long-Form Spatio-Temporal Video Grounding (LF-STVG), extends HCSTVG-v2 validation videos to lengths of 1–5 minutes, and proposes ART-STVG, an autoregressive transformer that processes frames sequentially with spatial and temporal memory banks plus simple text-similarity / TextTiling-based memory selection, organized through a cascaded spatial→temporal decoder. Experiments show large gains over non-streaming STVG baselines as video length grows, with internal ablations supporting each design choice.

## Strengths
- The streaming/autoregressive formulation is a natural architectural fit for long-form STVG and directly addresses the GPU-memory bottleneck of dense-clip methods (Sec. 3).
- The memory selection ablations (Tab. 2, Tab. 3) provide a useful, somewhat counterintuitive negative result: naïve "use all memories" actually *hurts* temporal grounding (m.tIoU 16.7 → 9.6), and selection recovers and exceeds it (→23.0). This is concrete evidence that selection is structurally necessary, not cosmetic.
- The cascaded spatial→temporal decoder produces a modest but consistent gain over the parallel design (+1.5/+1.4 m.tIoU/m.vIoU, Tab. 4), with a clear inductive-bias justification.
- Releasing extended LF-STVG splits of HCSTVG-v2 (1–5 min) gives the community a concrete testbed for this setting.
- Competitive (though not SOTA) on short-form HCSTVG-v2 (Tab. 7: 59.2/39.2 vs. TA-STVG 60.4/40.2), showing the streaming design does not collapse on the standard benchmark.

## Weaknesses

### Fatal
None.

### Major
- **No streaming / memory-bank baseline for LF-STVG.** Every external baseline in Tab. 1 (TubeDETR, STCAT, CG-STVG, TA-STVG) is a non-streaming model trained on 20-second clips and applied wholesale to 5-minute videos. Their catastrophic degradation (vIoU@0.7 → 0.0 at 4–5 min) is largely an artifact of being out of distribution architecturally, not evidence that ART-STVG's *memory selection / cascade* is responsible for the gap. Sec. 2 even reviews memory-bank long-video methods (MA-LMM, etc.) that would be the natural baselines, but none is adapted to STVG and compared. The "Baseline (ours)" is the only streaming comparator, and it is an internal ablation. Without an external streaming/memory baseline, the LF-STVG claim is supported only by "any streaming beats no streaming." This is the central evidential weakness.
- **Single, self-constructed benchmark for the headline claim.** All LF-STVG numbers come from extending the ~2,000-sample HCSTVG-v2 *validation* split (target events are the original 20-s clip, padded with surrounding YouTube context from the same source video). The justification — "only HCSTVG-v2 provides source videos" — is plausible but means the benchmark may embed a relatively benign "padded-needle" structure where the target event is a coherent chunk surrounded by less-relevant context, rather than competing among multiple plausible events. There is no external corroboration and no analysis of the target/surround relationship.

### Minor
- **Train/test scale mismatch is real but unanalyzed.** Training uses N_f=64 frames; inference on 5-min videos sees ~960 frames, so memory banks grow ~15× beyond what is seen at training time. No eviction/normalization policy is described, and there is no scan over memory-bank size or analysis of selection-score statistics across video length. Tab. 6 (training on 40-s clips → 23.0→28.3 on 3-min m.tIoU) confirms the distribution gap matters but does not characterize it.
- **"Closest-event" temporal-memory assumption is strong and untested.** Sec. 3.4 selects only the TextTiling event closest to the current frame, implicitly assuming the target is the most recent event. Failure-mode analysis stratified by target-event position in the video would be informative; none is provided.
- **Spatial memory selection diversity.** Top-N_s by similarity to a fixed text feature could collapse to a few near-duplicate memories. No diversity statistic (e.g., fraction of memories ever selected) is reported beyond a single qualitative attention-map figure (Fig. 5).
- **SF-STVG is slightly below SOTA.** ART-STVG trails TA-STVG by ~1.2/1.0 on HCSTVG-v2 (Tab. 7). Acknowledged by the authors, but worth noting that the case for the method relies almost entirely on LF-STVG.
- **No variance reporting.** Several ablation gaps (e.g., Tab. 3 ❶→❷ +0.8 m.tIoU; Tab. 5 N_s sweep within ~0.5 points) are small enough that seed-level noise is plausible.
- **Baseline architecture deferred to supplement.** Since "Baseline (ours)" is the only streaming reference point in Tab. 1, having its architecture in the main text would meaningfully improve readability.

### Trivial
- Tab. 2 / Tab. 3 column header "m.vIoT" appears to be a typo for "m.vIoU" (treated as formatting; flagged only for the authors' attention).

## Nice-to-Haves
- Adapt at least one long-video memory architecture (e.g., MA-LMM, MeMViT, TallFormer) to STVG and add it to Tab. 1.
- Coarse repurposing of VidSTG (using its original source videos) as a second LF-STVG benchmark.
- Stratify LF-STVG-5min results by where the target event sits in the video; report m.tIoU per stratum.
- Memory-bank statistics over time (sizes, selection-score distributions) to show the mechanism is doing what is claimed at scale.
- A side-by-side qualitative comparison against a streaming baseline (not against TubeDETR).

## Removed Points
*These points are flagged to be removed; treat them with caution.*
- **"Baselines were not designed for 5-min video, so the comparison is structurally unfair."** Partially fair (kept as a Major weakness in the form of "missing streaming baseline"), but the asymmetry favors the baselines being given an unfair *disadvantage* the authors created, and applying off-the-shelf SOTA to a new regime is standard practice when introducing a new setting; the harsh critic frames this more strongly than warranted.
- **"Loss function deferred to supplementary."** Reproducibility nit about deferred content; out of scope per review rules.
- **"Missing related work / memory-bank citations."** Cannot be independently verified; per rules, external-reference completeness is not graded here. (The paper does cite MA-LMM, MeMViT-style memory work in Sec. 2.)
- Strength: "the paper addresses an important problem" / "first to study LF-STVG" — generic and tautologically tied to the authors' own definition; removed.
- Strength: "comprehensive ablation study" — kept implicitly via specific Tab. 2/3/4 evidence; the generic phrasing is dropped.

## Novel Insights
The clearest insight that emerges beyond the paper's own contributions is the *destructive* effect of unselected temporal memory (Tab. 2: adding all memories nearly halves m.tIoU). This says something nontrivial about temporal cross-attention in long-form grounding — that the relevant inductive bias is not "more context is better" but "event-local context dominates" — and is worth a more central framing than the paper currently gives it. Otherwise, none beyond the paper's own contributions.

## Suggestions
- Add at least one streaming / memory-bank baseline (MA-LMM, MeMViT, or a TallFormer-adapted variant) to Tab. 1; this is the single most important fix.
- Build a second LF-STVG split from VidSTG or similar to corroborate the headline result.
- Report memory-bank statistics and selection behavior as a function of video length; describe any eviction/normalization policy.
- Stratify by target-event position to characterize the "closest event" assumption.
- Pull the "Baseline (ours)" architecture description into the main paper.

## Evaluation
- **Originality:** Moderate — autoregressive streaming + selective memory is a sensible but not radical recombination of known ideas (memory banks, TextTiling, cascaded decoders) applied to STVG.
- **Importance of question:** Real — STVG on multi-minute video is genuinely under-served.
- **Claims well supported?** Partially — internal ablations are clean, but the headline LF-STVG claim leans on a single self-constructed benchmark with no streaming baselines.
- **Soundness of experiments:** Mixed — solid ablations, but the comparison set in Tab. 1 cannot, by itself, isolate the contribution of the memory/cascade design from the contribution of "being streaming at all."
- **Clarity:** Reasonable; main paper is readable but load-bearing details (baseline architecture, loss) live in the supplement.
- **Value to community:** Moderate — the extended LF-STVG splits and the autoregressive framework are usable starting points, even if the empirical case needs strengthening.

## Score and Decision

Anchors retrieved (all from `calibration_search`; read the ones marked ✓ in full):

- `uHgVrGF2Wn.md` — LVBench, avg 4.50 (Reject). Long-video benchmark paper criticized for limited evaluation depth — comparable single-benchmark concern; this paper is methodologically richer.
- `tEei1bolt3.md` — Motion-Grounded Video Reasoning, avg 5.00 (Reject). New spatiotemporal-grounding task + dataset + model; closest in spirit. ART-STVG is roughly comparable: stronger method/ablation story, weaker independent-benchmark story.
- `le4IoZZHy1.md` — CG-Bench, avg 6.20 (Accept). Long-video benchmark, manually curated, larger and broader than this paper's single extended split.
- `Wto5U7q6I2.md` — TemporalBench, avg 4.20 (Reject). Fine-grained temporal benchmark, criticized for narrow evaluation.
- `1DEHVMDBaO.md` — Adaptive Memory Mechanism (long-form video, ViT memory bank), avg 4.60 (Reject). Most architecturally analogous: memory bank for long videos with selection. Similar profile; reviewers found contribution incremental.
- `JbPb6RieNC.md` — StreamChat (streaming video, memory), avg 5.80 (Accept). Streaming long-video method; closer to the architectural target this paper should have benchmarked against.
- `wkbx7BRAsM.md` — Autoregressive Transformers as Zero-Shot Video Imitators, avg 7.00 (Accept). Different topic; sets a high-band anchor.
- `qnAZqlMGTB.md` — StreamingBench, avg 5.75 (Reject). Streaming-video benchmark; comparable single-source benchmark concern.
- `4j9plQoOH1.md` — LongViTU, avg 4.75 (Reject). Long-form video understanding dataset; auto-generated single-source benchmark criticism analogous to here.
- `2D0uXQbntW.md` — InfiniBench, avg 6.00 (Reject). Long-video benchmark, broader scope than this paper.
- `28L2FCtMWq.md` — Ground-A-Video, avg 6.50 (Accept). Tangentially related (grounded video editing); high-band reference.
- `exKHibougU.md` — LLM-grounded Video Diffusion, avg 6.00 (Accept).
- `xYzOkOGD96.md` — Grounded Video Caption Generation, avg 3.83 (Reject). Low-band anchor; clearly weaker than ART-STVG, which has clean ablations and a more focused method.
- `BwQUo5RVun.md` — Weakly-supervised visual grounding, avg 3.00 (Reject). Low-band anchor; far weaker than this paper.
- `EuoHhIqvRD.md` — Synthetic data for visual grounding, avg 3.50 (Reject).

Calibration: ART-STVG is clearly above the 3.0–4.0 band (those papers are weaker on both method and ablations). It sits in the same neighborhood as Motion-Grounded (5.0), AMM (4.6), StreamChat (5.8), StreamingBench (5.75) — papers that propose a new long/streaming-video method or benchmark with reasonable ablations but a self-constructed or single-source evaluation regime. It is plausibly slightly above the AMM/Motion-Grounded band because the ablations are sharper and the negative-result finding is genuinely informative, but below CG-Bench/InfiniBench-level acceptance candidates because the headline comparison set is structurally weak (no streaming baseline) and rides on a single extended benchmark.

MY FINAL SCORE: <pineapple>5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>