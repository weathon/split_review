Now I have enough context to write the meta-review.

## Summary
The paper introduces Long-Form Spatio-Temporal Video Grounding (LF-STVG) — extending the HCSTVG-v2 validation set to videos averaging 1–5 minutes — and proposes ART-STVG, an autoregressive transformer that processes frames sequentially with spatial and temporal memory banks (each governed by a similarity-based selection rule) and a cascaded spatial→temporal decoder that feeds ROI-pooled motion features from the spatial prediction into temporal grounding. ART-STVG reports large gains over four short-form STVG baselines on every extended benchmark while staying within 1.0–1.2 m.tIoU/m.vIoU of state-of-the-art on the original short-form benchmark.

## Strengths
- **Genuinely novel framing for STVG**: Treating STVG as a streaming, frame-by-frame autoregressive process (Sec. 3.2, Fig. 1/3) is a substantive departure from prior one-shot full-clip pipelines and is well-motivated by the memory bottleneck argument in Sec. 1.
- **Cascaded vs. parallel decoder is a clean architectural finding**: Table 4 shows the cascaded design (ROI-pooled motion features feeding the temporal decoder) gives +1.5/+1.4 m.tIoU/m.vIoU on LF-STVG-3min over a parallel ablation — a small but well-isolated and intuitive contribution.
- **Selective spatial memory ablation is coherent**: Table 3 (rows ❶→❷→❸: 21.3 → 22.1 → 23.0 m.tIoU) shows the spatial memory bank helps, and text-similarity-based selection adds further gain on top — a clean monotone story consistent with the paper's claims.
- **Large headline margins on extended LF-STVG benchmarks**: On the five extended LF-STVG splits, ART-STVG achieves the best m.tIoU/m.vIoU/vIoU@0.5/vIoU@0.7 in every cell (Table 1), with the 5-min m.tIoU nearly doubling the best prior method (15.0 vs 7.7).

## Weaknesses

### Fatal
None. The structural concerns below are serious but do not rise to outright invalidation, since the paper's own internal controls (Tab. 6, Table 1 "Baseline (ours)") at least partially probe them.

### Major

- **Long-form comparison primarily measures OOD behavior of baselines rather than long-form ability.** Sec. 4 ("all methods including ART-STVG are trained *exclusively* on the HCSTVG-v2 training set (average video length 20 seconds)") plus the design of TubeDETR/STCAT/CG-STVG/TA-STVG as fixed-input transformers means the baselines are evaluated 15× outside their training horizon at LF-STVG-5min. The paper never states the inference protocol used to feed 1–5 minute videos into baselines built for ~20-second inputs (sliding window? uniform subsampling? truncation?). Table 6's mitigation extends training only to 40s — still nowhere near 5 minutes. The headline claim that gains grow with video length (Fig. 2) is therefore confounded with "baselines get steadily more OOD." A matched-budget evaluation protocol is needed for the comparison to bear the weight the paper places on it.

- **Streaming-vs-memory contributions are conflated in "Baseline (ours)".** "Baseline (ours)" is ART-STVG without memory or selection but retains the streaming/autoregressive backbone, ROI-cascade design, and frame budget. On LF-STVG-3min, this baseline alone already reaches 16.7 m.tIoU — surpassing all four prior methods (best: TA-STVG 13.9). Similar patterns hold at 4min (9.9 vs 10.6) and 5min (9.2 vs 8.1). This strongly suggests that a non-trivial share of the gap to prior SOTA is attributable to streaming inference, not to the named contributions (memory bank, selection, cascade). The paper does not disentangle these, weakening the attribution of the gains.

- **Temporal-memory ablation tells an unaddressed story.** Table 2: row ❶ (no memory) 16.7 → row ❷ (all memory) 9.6 → row ❸ (selection) 23.0 m.tIoU. The temporal memory bank as a stand-alone module is *harmful*, and essentially all of its reported benefit comes from the TextTiling-style cosine-similarity selector — which uses no text query. The paper frames spatial and temporal memory banks symmetrically (Sec. 3.3/3.4), but Tab. 3 (rows ❶→❷ improves) and Tab. 2 (rows ❶→❷ degrades) show they behave oppositely as designs. A "selection-only, no bank" variant and a text-aware temporal selector are obvious missing controls.

- **Insufficient specification of the extended benchmark.** Sec. 4 states only that the extensions are based on original YouTube videos and manually reviewed. The position of the original ~20s GT segment inside the 1–5 minute clip (start/middle/end? random?), the nature of the surrounding content (any distractor activities involving similar entities or matching phrases?), and the fraction of foreground time the target occupies are not disclosed. Without this, m.tIoU on the 5-min split is closer to needle-in-haystack temporal retrieval than to "long-form" grounding, and the column-wise trends in Table 1 are not interpretable as evidence about the model.

### Minor

- **On the native domain, ART-STVG is slightly worse than SOTA.** Table 7: ART-STVG 59.2/39.2 vs. TA-STVG 60.4/40.2 m.tIoU/m.vIoU on the original HCSTVG-v2 validation set. The paper acknowledges this in one line. Combined with the Major concerns above, the case for the method rests entirely on the long-form benchmark.

- **Temporal-memory selection rule restricts context to only the most recent event boundary.** Sec. 3.4: "we only select memories corresponding to the event closest to current frame." For queries whose action unfolds across event boundaries (e.g., "stands up and walks…"), this is a strong inductive bias; the paper should test against keeping the K most-recent boundary segments to justify the rule.

- **Motion features use VidSwin with previous frames, partially breaking the strict "streaming" framing.** Sec. 3.1: "when applying VidSwin to extract motion features, previous frames are also used as input." The size of this lookback window during streaming inference on a 5-minute video is not specified.

- **Training horizon (64 frames, 20s) does not match the inference horizon claim.** Sec. 4 sets $N_f=64$ at 3.2 FPS, so training sequences are 20s. The streaming claim is therefore only tested at inference; Table 6's 40s training is the only deviation. The central thesis ("the model handles long videos") would be substantially strengthened by training on longer windows for the proposed model.

### Trivial

- No variance/standard deviations are reported anywhere, despite some ablation gaps (e.g., Tab. 4: +1.5 m.tIoU) being modest.
- The temporal-memory illustration (Fig. 6) does not clarify how event boundaries are thresholded from cosine similarities of adjacent memories.

## Nice-to-Haves

- Specify and report the long-form inference protocol used to feed 1–5 minute videos into SF-STVG baselines (sliding window vs. subsampling vs. truncation) and provide a matched-budget version of Table 1.
- Disclose placement of the GT segment within the extended video and any distractor structure; provide per-position analyses (target near beginning vs. middle vs. end).
- Add a "selection-only, no bank" control for both decoders to isolate the contribution of the selector from the bank.
- Train ART-STVG on horizons substantially longer than 40s to confirm the long-form thesis.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- *(Removed — speculative reproducibility)* "The autoregressive temporal loss is non-trivial and should not be deferred to supplementary." The loss formulation appendix exists in the original submission; parser stripping is not an author fault.
- *(Removed — Strength Finder generic claim)* "Memory selection strategies yield large and consistent gains" — overlaps directly with the Major weakness about temporal memory being harmful without selection; the weakness wins on the temporal side. The spatial side is retained as a Strength.
- *(Removed — Strength Finder borderline-superficial)* "First autoregressive transformer for long-form STVG" already absorbed into the genuine-novelty strength; not duplicated.
- *(Removed — generic)* "Long-form video understanding is an important task." Generic importance-of-problem framing.

## Novel Insights

The most useful insight that emerges from cross-reading the inputs is that the long-form gains are likely a composition of two largely independent effects: (i) streaming/autoregressive inference being a better fit for inputs longer than the training horizon, and (ii) text-conditioned spatial memory selection helping the spatial decoder. The temporal "memory bank" framing the paper foregrounds is actually carrying very little weight — Table 2 shows it is the selector, not the bank, doing the work, and the selector uses no text query. Reframing the contribution as "streaming STVG + event-boundary temporal gating + text-conditioned spatial memory" would more faithfully describe the evidence and would expose a sharper architectural claim.

## Suggestions

- Re-present Table 1 with a matched inference budget for the SF baselines (e.g., overlapping sliding-window inference at their native horizon) and explicitly state the protocol.
- Disclose the placement distribution of the original 20s GT window within the extended 1–5 minute clips, and add a per-position breakdown of m.tIoU.
- Add ablations isolating: streaming-only (current Baseline (ours)), selection-only (no memory bank, just event-boundary gating of current-frame attention), and bank-only — for both decoders.
- Replace the cosine-only temporal boundary heuristic with a text-aware variant and report the comparison; this addresses the asymmetry between the two memory designs.
- Train the proposed model on substantially longer clips (e.g., 2 min) and include this as a row in Table 6; the central thesis demands it.

## Axis Evaluation
- **Originality**: High. Streaming/autoregressive STVG is a fresh framing and the cascaded spatial→temporal design is a clean architectural idea.
- **Importance of research question**: Reasonable. Long-form STVG is a real gap, though the framing partly overlaps existing long-form video understanding literature.
- **Support for claims**: Weak-to-moderate. The headline claim of "ART-STVG is better at long-form" rests on a benchmark constructed in a way that systematically disadvantages baselines (OOD inputs) without a matched-budget protocol, and the "Baseline (ours)" already explains a large fraction of the gap.
- **Soundness of experiments**: Mixed. Ablations on the cascade and spatial memory are sound; the temporal-memory ablation directly contradicts the paper's symmetric framing without engagement; SF-STVG is slightly worse than SOTA.
- **Clarity**: Mostly clear. Architecture and ablations are presented straightforwardly; benchmark construction is the most under-specified part.
- **Value to the research community**: Moderate. The streaming framing and extended HCSTVG-v2 splits are useful; the empirical claims require a fairer protocol before they can be relied on.

## Score and Decision

**Anchors retrieved across rounds:**

Round 1 (bracketing):
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/bEvI30Hb2W.md` — LVM-NET, avg 3.0, reject. Long-form video reasoning via memory sampling; weaker contribution and limited validation than the paper under review.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/hWlCc7Iksi.md` — ARVideo, avg 3.4, reject. Autoregressive video pretraining; tangentially related, weaker.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/N581Nje6fH.md` — Robot episodic memory, avg 1.5, reject. Off-topic.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/YGWxpOI6Y0.md` — VideoGPT+, avg 3.4, reject. Video LMM, off-task.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/1DEHVMDBaO.md` — Adaptive Memory Mechanism, avg 4.6, reject. Closest analogue: memory bank + selection for long video; reviewers flagged marginal gains and memory-bank novelty concerns — same family of objections as the present paper, though our paper has a larger gain margin and a new task framing.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/xYzOkOGD96.md` — Grounded Video Caption Generation, avg 3.83, reject. New task + dataset + model; reviewers were skeptical of evaluation rigor — comparable concerns to our paper.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/14fFV0chUS.md` — TRACE, avg 6.75, accept. Causal autoregressive event modeling for VTG; cleaner contribution and broader evaluation than this paper.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/9Cu8MRmhq2.md` — Norton, avg 8.0, accept; far stronger.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/2dnO3LLiJ1.md` — ViT registers, avg 8.0, accept; far stronger and broader-impact.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/LbEWwJOufy.md` — TANGO, avg 8.5, accept; far stronger.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/kxnoqaisCT.md` — GUI grounding, avg 7.75, accept; far stronger.

**Round 1 bracket**: between 3.5 and 6. The paper is clearly stronger than the 3.0–3.8 anchors (it has a real method, a new task, and substantial ablations) but it is not at TRACE's 6.75 level (TRACE has a cleaner contribution attribution, broader benchmark coverage, and no comparable fairness concern).

Round 2 (narrowing):
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/tEei1bolt3.md` — Motion-Grounded Video Reasoning, avg 5.0, reject. New task + dataset + model; closest match in shape to our paper's contribution profile.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/wMRFTQwp1d.md` — VideoEval, avg 4.0, reject. New benchmark, narrower contribution.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/uHgVrGF2Wn.md` — LVBench, avg 4.5, reject. New long-video benchmark — similar in spirit to the extended LF-STVG splits.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/a1P5kh2oo8.md` — Vinoground, avg 5.75, reject. New benchmark with clean motivation.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/QWDFOOoV3U.md` — ResidualViT, avg 5.75, reject. Closest method-side analogue (efficient transformer for temporal grounding). Reviewers split 3/8/6/6 — the paper is methodologically clean but with reservations.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/ydH8nU5csJ.md` — DTVLT, avg 4.6, reject. New VLT benchmark; methodological concerns.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/7L2bpe7lfm.md` — Large-Scale Video CL, avg 4.5, reject. Memory-buffer methodology, mixed evidence.

**Narrowing**: The paper sits closest to AMM (4.6), LVBench (4.5), Motion-Grounded Reasoning (5.0), and ResidualViT (5.75). The fairness concern about the benchmark construction and the conflation of streaming-vs-memory contributions (Major weaknesses 1 and 2) are heavier than the typical reasons those anchors were rejected; the new task framing and clean architectural ablation pull it up slightly above the 4.0–4.5 benchmark-only papers. Compared to ResidualViT (5.75), our paper has stronger ablation breadth but the benchmark-fairness concern is unique and substantive.

Settling slightly below the Motion-Grounded Reasoning anchor (5.0): the paper's empirical case is undermined by an OOD-favoring benchmark protocol and by an internal control ("Baseline (ours)") that already captures much of the headline gap, so the attribution to its named contributions is unclear. Slightly above AMM (4.6) and LVBench (4.5) because the new task framing is genuinely useful and the long-form gain margins are large.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>