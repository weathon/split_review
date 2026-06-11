## Summary
ART-STVG is an autoregressive transformer for spatio-temporal video grounding that processes frames sequentially using spatial/temporal memory banks with task-specific selection (text-similarity for spatial; TextTiling-style boundary detection for temporal), and a cascaded spatial→temporal decoder. The paper also introduces LF-STVG, extending HCSTVG-v2 validation videos from 20s to 1–5 minutes via their original YouTube sources.

## Strengths
- Identifies a real gap (HCSTVG-v2 ~20s, VidSTG ~35s) and demonstrates a dramatic degradation of prior STVG methods on long videos (e.g., TA-STVG drops from 38.4 to 7.7 m.tIoU from 1min to 5min, Tab. 1).
- Concrete ablation showing temporal memory selection is essential (Tab. 2: 16.7 → 9.6 naive → 23.0 selective m.tIoU on LF-STVG-3min).
- Cascaded vs. parallel decoder ablation gives +1.5/+1.4 m.tIoU/m.vIoU (Tab. 4); the autoregressive design does not sacrifice short-form performance (Tab. 7: 59.2/39.2 vs. TA-STVG 60.4/40.2).
- Tab. 6 (40-second training) shows ART-STVG still leads under length-matched training (28.3 vs. 20.8 m.tIoU at 3-min), partially defending the architectural claim against protocol-mismatch concerns.

## Weaknesses

### Fatal
None.

### Major
- **Baseline adaptation protocol for 1–5 minute inference is unspecified.** Sec. 4.1 trains all methods on 20-second clips and evaluates at up to 5 minutes "for fair comparison," but never describes how parallel-processing baselines (TubeDETR, STCAT, CG-STVG, TA-STVG) consume the long videos (frame budget, subsampling, sliding window?). Their collapse may reflect protocol mismatch rather than architectural inferiority. Tab. 6 partly defends the claim at 40s, but no equivalent control is run at 1–5 min.
- **The headline gain is partially attributable to the autoregressive baseline, not the proposed memory.** Tab. 1 shows "Baseline (ours)" (no memory) already beats all prior methods at 3–5 min (e.g., 9.2 vs. 7.7–8.1 at 5min). The proposed memory adds another ~6 m.tIoU on top — meaningful, but more modest than the framing suggests.

### Minor
- **The benchmark stress-tests a single regime: a 20s event in long irrelevant surround.** Because only the validation videos are extended and the GT tube remains the original 20s segment, the evaluation does not cover multi-event or long-event long-form scenarios that the introduction motivates. The paper provides only "manual review" as benchmark quality control — no event-position distribution or distractor statistics.
- **"Memory" framing is overstated vs. "selection."** Tab. 2 shows naive temporal memory hurts (16.7 → 9.6) and selection is the entire benefit; Tab. 3 shows spatial memory contributes only ~1.7 m.tIoU total. The TextTiling-style event-boundary selection is doing most of the work and should be framed as the central contribution.
- **Causal/streaming details of temporal selection are under-specified.** Sec. 3.4 detects boundaries via adjacent-memory cosine similarity and keeps the "event closest to current frame." Since at frame i only memories 1…i exist, the right boundary of the current event isn't yet observable; the paper should clarify whether the selection is strictly causal and how event-end is predicted before completion.
- **SF-STVG slight underperformance** (Tab. 7) suggests the autoregressive design costs ~1 m.tIoU where global context is reachable; acknowledged but not analyzed.

### Trivial
None retained.

## Nice-to-Haves
- An analysis figure showing each baseline's performance vs. input frame budget, or sliding-window inference variants of baselines on 1–5 min.
- Sensitivity analysis of the TextTiling cosine threshold and correlation with downstream m.tIoU.
- LF-STVG benchmark statistics (event position distribution, distractor content, scene overlap with training).

## Removed Points
These points are flagged to be removed, treat them with caution:
- "Eq. 1 shows three identical bracketed sequences" — parser/typesetting artifact, not author error.
- "Loss function deferred to supplement" — appendix is stripped by the parser; cannot be evaluated.
- "No variance / multiple seeds" — single-run evaluation is standard for STVG benchmarks.
- Generic strengths ("well-motivated problem," "thorough ablations") demoted into concrete points above.

## Novel Insights
None beyond the paper's own contributions. The harsh critic's reframe — that the real contribution is event-boundary-driven selection rather than memory augmentation — is well-grounded but is implicit in the paper's own ablations.

## Suggestions
- Specify and report the inference-time adaptation protocol for each baseline; retrain at least one strong baseline at matched longer lengths (1–5 min) to control for train/test mismatch.
- Reframe the contribution around selection and isolate selection vs. memory more cleanly.
- Clarify causality at frame i; report a strictly causal variant if the current one peeks ahead.
- Provide LF-STVG benchmark statistics so readers can independently judge validity.

## Score and Decision

Anchors retrieved:
- Round 1 weak: ICR3swcnaa (3.0, Reject) — generic ST transformer; weaker. BwQUo5RVun (3.0). YGWxpOI6Y0 (3.4). MSxCBXD5C8 (3.0).
- Round 1 mid: xYzOkOGD96 (3.83, Reject) Grounded Video Caption — similar new-task framing but weaker reception. 4j9plQoOH1 (4.75, Reject) LongViTU. YCwN7wQA6W (4.25, Reject) Grounded-VideoLLM. tEei1bolt3 (5.00, Reject) Motion-Grounded Video Reasoning — quite similar in spirit (new task + dataset + method).
- Round 1 strong: 9Cu8MRmhq2 (8.0, Accept), 2dnO3LLiJ1 (8.0), Q6a9W6kzv5 (8.0), Cjz9Xhm7sI (8.0) — all clearly stronger contributions.
- Round 2 (4.5–6): tEei1bolt3 (5.0, Reject), a1P5kh2oo8 (5.75, Reject), ydH8nU5csJ (4.60, Reject), QWDFOOoV3U (5.75, Reject).
- Round 2 (5–7 streaming): JbPb6RieNC (5.80, Accept) StreamChat, 26oSbRRpEY (5.25, Reject), QETk0lBdVf (5.80, Reject), X4Rcxi9588 (5.50, Reject).

Round-1 bracket: 4–6. Round-2 narrowing: this paper is most comparable to Motion-Grounded Video Reasoning (5.0) — a new task with a benchmark and a focused method. ART-STVG has crisper ablations isolating selection mechanisms and cleaner architectural ideas, but it has a legitimate methodological concern (undescribed baseline adaptation protocol at long lengths) that reviewers will weigh against acceptance. It sits between the weaker 4.x rejects (Grounded-VideoLLM, DTVLT) and the 5.x cluster (Motion-Grounded, Vinoground, StreamChat). I score it slightly below Motion-Grounded Video Reasoning because the comparison fairness concern is more central to its headline claim.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>