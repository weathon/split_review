Now I have a clear calibration picture. Let me compose the final consolidated review.

## Summary

This paper introduces Long-Form Spatio-Temporal Video Grounding (LF-STVG) and proposes ART-STVG, an autoregressive transformer with spatial and temporal memory banks and a cascaded spatio-temporal decoder. The method processes frames sequentially rather than all at once, making it suitable for minute-long videos where existing STVG models fail due to computational and architectural constraints. The paper also extends the HCSTVG-v2 validation set to create LF-STVG benchmarks at five video lengths (1–5 minutes). Experiments show substantial improvements over existing methods (e.g., 23.0% vs. 13.9% m.tIoU on 3-minute videos) and competitive results on short-form STVG.

## Strengths

1. **Large, consistent performance advantage on long-form videos.** ART-STVG substantially outperforms all existing STVG methods across every video length (1–5 minutes), with the gap widening as videos get longer. On 3-minute videos it achieves 23.0% m.tIoU vs. 13.9% for the strongest prior method TA-STVG (Table 1c). The improvements are 6–9% m.tIoU on 2–5 minute benchmarks, far beyond what could be attributed to noise. This directly validates the paper's central claim that the autoregressive memory-augmented design is better suited for long-form localization.

2. **Selective memory is cleanly ablated and shown to be critical.** The ablation study (Tables 2–3) demonstrates that using all temporal memories without selection actually hurts performance (9.6% m.tIoU vs. 16.7% without any memory), while the proposed selection strategy boosts m.tIoU to 23.0%. For spatial memory, selection yields consistent additional gains (22.1% → 23.0%). The attention visualizations (Figs. 5–6) corroborate that selection focuses the model on relevant context. This is clean, evidence-backed validation of a non-obvious design choice.

3. **Cascaded spatio-temporal decoder is a well-motivated and validated architectural contribution.** The cascaded design, which feeds fine-grained spatial features from the spatial decoder into the temporal decoder via RoI pooling, outperforms a parallel decoder architecture by 1.5% m.tIoU and 1.4% m.vIoU (Table 4). This is a simple but effective idea that is clearly explained and directly supported by the ablation.

4. **Competitive on short-form STVG despite being designed for long videos.** ART-STVG achieves 59.2% m.tIoU on the standard HCSTVG-v2 benchmark (Table 7), coming within 1.2 points of the current SOTA (TA-STVG) and outperforming most prior methods. This demonstrates that the autoregressive framework does not sacrifice short-form capability.

## Weaknesses

### Fatal

None.

### Major

1. **LF-STVG benchmark construction is under-documented, specifically regarding ground-truth annotations.** The paper states that the extended videos (1–5 min) are based on original YouTube videos and were "manually reviewed," but it never clarifies how ground-truth annotations were obtained for the extended portions. The original HCSTVG-v2 provides spatial bounding boxes and temporal intervals only for a 20-second segment. Without knowing (a) whether the same 20-second annotations are used as ground truth for the longer videos, (b) how spatial grounding is evaluated on frames outside the original annotation window, or (c) whether new annotations were created (and if so, via what protocol and with what quality assurance), the experimental results cannot be fully interpreted or reproduced. This is the single most important issue the authors must address.

2. **Temporal inference procedure is unspecified.** The model outputs per-frame start and end probabilities \(h_i^s, h_i^e\) (Eq. 7), but the paper never explains how these are converted into a single predicted temporal interval, which is necessary to compute tIoU. Common choices (thresholding, argmax over the probability curves, dynamic programming) can produce very different results, and the paper provides no sensitivity analysis or even a description of the method used. Without this, the temporal grounding numbers are not properly linked to the model's outputs.

### Minor

1. **Training and testing distribution shift is not discussed.** Models are trained on 20-second videos (64 frames) but evaluated on up to 5-minute videos (~960 frames). While the 40-second training experiment (Table 6) partially addresses this, the paper does not discuss how the autoregressive model handles the distribution shift or whether the memory bank capacity (\(N_s = 32\) spatial memories) generalizes across video lengths. A brief discussion would improve the reader's understanding.

2. **Temporal memory selection relies on a specific heuristic whose failure modes are not analyzed.** The selection strategy assumes the target event is the one closest to the current frame (via TextTiling-style boundary detection). Events that are temporally distant but visually similar could be missed. The paper acknowledges this implicitly but does not discuss when the heuristic might fail or how robust it is across different video structures.

### Trivial

None.

## Nice-to-Haves

- An analysis of memory capacity scaling: how does performance change as the number of stored spatial memories (\(N_s\)) varies for different video lengths? The current ablation tests three values of \(N_s\) on 3-minute videos, but the optimal \(N_s\) may not be constant across video lengths.
- A summary of the loss function in the main paper (currently deferred to supplementary).
- A brief limitations discussion acknowledging potential failure modes of the memory-selection heuristics.

## Removed Points

- **Typo "m.vIoT" in Tables 2–3:** This is a PDF parsing artifact; the original submission does not contain this error.
- **Reproducibility details about undisclosed hyperparameters (batch size, epochs, etc.):** Per protocol, nitpicks about standard hyperparameters missing from the main text are removed. The paper provides the learning rates, optimizer, frame length, and backbone initialization, which are the critical details.
- **Criticism that the comparison does not isolate the model's ability to handle long sequences:** All methods (including ART-STVG) are trained on identical 20-second videos and tested on longer videos. The architecture is the independent variable. The claim that a comparison to an autoregressive baseline is missing is also invalidated by the paper's own baseline (without memory), which shows large gains from the memory components.
- **Claim that the numbers are "uninterpretable" or the benchmark is invalid:** The benchmark is valid but under-documented. The evaluation protocol is standard for STVG (the original 20-second annotations serve as ground truth within a longer context), but this needs to be explicitly clarified.
- **Request for discussion of GPU memory limits causing baseline degradation:** Speculative; the paper is not required to diagnose why baselines perform poorly.

## Novel Insights

None beyond the paper's own contributions. The key insights — that processing frames autoregressively with selective memory banks enables long-form STVG, and that cascading spatial→temporal decoding helps temporal localization — are already well articulated in the paper. The reviews do not surface genuinely new observations about the method's implications beyond what the authors themselves present.

## Suggestions

1. **Clarify the LF-STVG benchmark construction in detail.** State explicitly: (a) whether the original 20-second annotations are retained as ground truth for the longer videos, (b) how spatial evaluation is performed on frames outside the original annotation window, and (c) what "manually reviewed" entails. If new annotations were created, describe the protocol and provide quality metrics.
2. **Specify the temporal inference procedure.** Describe exactly how \(h_i^s\) and \(h_i^e\) (per-frame start/end probabilities) are converted into a single predicted interval. Provide a sensitivity analysis for any thresholds or parameters involved.
3. **Add a limitations section** discussing when the temporal memory selection (TextTiling-based boundary detection) might fail, and how the fixed number of selected memories interacts with different video lengths.
4. **Briefly discuss the train/test distribution shift** and why the autoregressive design is robust to it despite being trained on only 64-frame clips.

## Score and Decision

### Calibration Report

**Round 1 — Bracketing (wide):**
- Query 1 (topic: "spatio-temporal video grounding autoregressive transformer long videos", score < 3.5):
  - hWlCc7Iksi (3.40, reject): Self-supervised video pretraining, not directly comparable; weaker contributions.
  - MI0UiWeqOl (2.33, reject): Poly-autoregressive modeling for interacting entities; not in video grounding domain.
  - ICR3swcnaa (3.00, reject): Action recognition with diffusion transformer; different task, weaker results.
  - lvgsPjRtLM (2.50, reject): Video generation; different task.
  - YGWxpOI6Y0 (3.40, reject): Video LMM; different task.
  
- Query 2 (topic: "spatio-temporal video grounding memory bank selection long form", 3.5 < score < 7.5):
  - 1DEHVMDBaO (4.60, reject): Adaptive memory for video understanding; marginal gains, limited baselines. **Weaker than our paper** — our empirical gains are far larger and ablations are more thorough.
  - tEei1bolt3 (5.00, reject): Motion-grounded video reasoning; new dataset, some methodological concerns.
  - O8FkMqNF1M (5.50, reject): Language repository for long video; different approach, mixed reviews.
  - UX9lljSZqX (6.25, reject): Temporal filtering for video grounding; some acceptance interest but ultimately rejected.
  - yHj6EunfVQ (5.50, accept): Weakly supervised STVG with self-paced learning; comparable quality, had clarity issues but accepted. **Our paper has similar strengths with slightly larger empirical gains but similar documentation gaps.**

- Query 3 (topic: "video grounding temporal localization benchmark construction long videos", score > 7.5):
  - 9Cu8MRmhq2 (8.00, accept): Long-term noisy video correspondence learning; strong, well-executed work. **Stronger than our paper** in polish and evaluation rigor.
  - Various accept papers at 7.6–8.5: Strongly accepted, not directly comparable.

**Initial bracket: 5.0 – 6.5**

**Round 2 — Narrowing (within bracket):**
- Query 1 (4.5 < score < 6.0):
  - 1DEHVMDBaO (4.60, reject): Already discussed above.
  - QWDFOOoV3U (5.75, reject): ResidualViT for zero-shot temporal grounding; mixed reviews (3,8,6,6). **Our paper has stronger empirical support for claims.**
  - yHj6EunfVQ (5.50, accept): Already discussed above.
  - IryGDUHxDE (5.25, reject): Unsupervised AR model for action recognition; different task.

- Query 2 (6.0 < score < 7.5):
  - 14fFV0chUS (6.75, accept): TRACE — causal event modeling for VTG; well-received with 8,6,5,8 scores. **Stronger than our paper** — more polished, fewer documentation gaps.
  - fCi4o83Mfs (6.75, accept): Temporal reasoning benchmark; different contribution type.
  - sHAvMp5J4R (6.80, accept): Temporal reasoning transfer; well-executed.

**Final anchor comparisons:**
Our paper is clearly stronger than the 4.6 anchor (marginal gains, limited ablations). It is comparable to the 5.5 anchor (CoSPaL, accepted) — both have solid contributions with some clarity issues. It is weaker than the 6.75 anchor (TRACE, accepted) which is more polished and has fewer documentation gaps.

### Final Score and Decision

The paper addresses a relevant underexplored problem with a well-motivated method. The empirical results are strong and the ablations convincingly support the design choices. The main weaknesses are documentation gaps (benchmark annotation protocol, temporal inference procedure) that are significant but addressable. The core contributions — the autoregressive formulation for LF-STVG, the selective memory design, and the cascaded decoder — are novel and well-supported by evidence.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>