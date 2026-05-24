Now I have a thorough understanding of the paper and the calibration anchors. Let me write the final consolidated review.

## Summary
This paper introduces Long-Form Spatio-Temporal Video Grounding (LF-STVG) as a new task and proposes ART-STVG, an autoregressive transformer that processes video frames sequentially with spatial and temporal memory banks and selection strategies. The method extends the HCSTVG-v2 validation set to 1–5 minute versions and reports large improvements over four strong baselines. While the problem framing is well-motivated and the method design is sensible with thorough ablations, a critical omission in the experimental reporting — the test-time frame processing protocol for baseline methods — prevents full verification of the headline claims.

## Strengths
1. **New problem formulation with practical relevance.** The paper identifies and formalizes LF-STVG, a natural extension of STVG to minute-long videos. The gap between existing 20-second benchmarks and real-world applications (minutes to hours) is clearly motivated and well-articulated.

2. **Well-designed autoregressive architecture with memory selection.** The streaming design inherently avoids the GPU memory bottleneck of full-frame parallel processing. The text-similarity spatial memory selection and event-boundary temporal memory selection are simple, intuitive, and convincingly ablated (e.g., temporal memory selection improves m.tIoU from 9.6 to 23.0 on LF-STVG-3min, Tab. 2).

3. **Thorough ablation study isolating each component.** Tables 2–6 systematically verify temporal memory selection, spatial memory selection, cascaded vs. parallel design, spatial memory size, and training with longer videos. Each ablation uses multiple metrics (m.tIoU, m.vIoU, vIoU@0.3, vIoU@0.5), providing strong evidence for the design choices.

4. **Competitive short-form performance while targeting long videos.** On HCSTVG-v2 (20-second videos), ART-STVG achieves 59.2 m.tIoU / 39.2 m.vIoU (Tab. 7), trailing only the dedicated short-form SOTA (TA-STVG, 60.4/40.2) while substantially outperforming the baseline without memory (46.2/29.9). This demonstrates that the method does not sacrifice short-video accuracy for long-video capability.

## Weaknesses

### Major
1. **Undisclosed test-time frame processing protocol for baselines (undermines main empirical claims).** The paper states (Sec. 4) that all methods are "trained exclusively on the HCSTVG-v2 training set" (20-second videos, 64 frames at 3.2 FPS), but never specifies how baselines (TubeDETR, STCAT, CG-STVG, TA-STVG) process 1–5 minute test videos. Existing DETR-based STVG models are built for fixed-length inputs (typically 64 frames). If they were evaluated by feeding only 64 subsampled frames, they would see ~20 seconds of content while ART-STVG sees the full video sequentially — artificially inflating the reported improvement. If they processed all frames, any GPU memory or architectural adaptations needed should be disclosed. Without this information, the large gaps in Table 1 (e.g., ART-STVG 15.0 m.tIoU vs. TA-STVG 7.7 on LF-STVG-5min) cannot be properly interpreted. This gap extends to Table 6 (training on 40-second videos), where test-time processing is similarly unspecified.

2. **Incomplete documentation of the benchmark extension.** The paper extends the HCSTVG-v2 validation set to 1–5 minutes but does not clarify: (a) whether ground-truth temporal intervals remain the same as the original 20-second annotations or were updated for longer videos; (b) whether additional occurrences of the target object/event in the extended portions were annotated; (c) basic statistics of the extended benchmarks (e.g., distribution of target interval duration relative to video length). These details are necessary for reproducibility and for interpreting what the task actually measures.

### Minor
3. **No ablation isolating the benefit of the streaming/autoregressive design from the memory components.** The baseline in Table 1 is "similar architecture but without memory and memory selection modules" — but remains autoregressive. An experiment running ART-STVG in a "parallel" mode (processing all frames at once with the same memory banks) would isolate whether the gains come from streaming or from the memory/selection modules.

4. **No GPU memory or runtime comparison.** The paper motivates ART-STVG partly as solving the "computational bottleneck" of parallel methods, but provides no direct measurement (GPU memory consumption vs. video length, inference time per frame) to substantiate this claim.

### Trivial
5. Minor labeling issues: Table 2 column header says "m.vIoT" instead of "m.vIoU"; Figure 2 caption mentions "m_Ap@1 (%) and m_Ap@5 (%)" which are not defined as metrics in the paper.

## Nice-to-Haves
- Sensitivity analysis for the temporal memory event-boundary threshold (the temporal memory selection is inspired by TextTiling, but the paper provides no ablation on the detection threshold).
- Qualitative failure cases (e.g., when the target event appears multiple times, or when distractors cause incorrect memory selection).
- Comparison with memory-augmented video understanding models cited in related work (e.g., MA-LMM) adapted to STVG.

## Removed Points
- *"Unclear how baseline methods processed long videos at test time (Structural)"* → Kept as Major weakness #1. The harsh critic framed this as "structural"; I agree it is a major omission.
- *"Missing annotation details for extended LF-STVG benchmarks (Evidential)"* → Kept as Major weakness #2.
- *"No comparison against non-autoregressive variant of ART-STVG"* → Demoted from Major to Minor (#3). The streaming vs. parallel comparison is a useful isolation experiment but the paper already has a thorough ablation of the memory components, which are the primary novelty.
- *"Figure 2 metrics inconsistency"* → Kept as Trivial (#5).
- *"Missing related works"* → Removed per rule (cannot verify).
- *"Missing appendix proofs/supplementary"* → Removed per rule (parser strips appendices).
- *"Sensitivity to temporal memory bank size"* → Demoted to Nice-to-Have.
- *"Failure analysis or more qualitative examples"* → Demoted to Nice-to-Have.
- *"Running time"* → Changed to Minor weakness #4 (lack of GPU memory/runtime comparison).
- Strength Finder's claim about "creation and public release of LF-STVG evaluation datasets" → Weakened: the datasets are a contribution but the release status is not explicit.
- Strength Finder's claim about SOTA on "five newly created long-form benchmarks" → The benchmarks are extended validation sets, not fully new test sets; kept as a strength but reframed more precisely.

## Novel Insights
None beyond the paper's own contributions. The core observation — that autoregressive frame processing with selective memory banks can handle longer videos than existing parallel STVG methods — is the paper's own contribution.

## Suggestions
1. **Disclose the test-time protocol explicitly**: state exactly how many frames were input to each baseline model at each video length (e.g., "all baselines processed 64 uniformly sampled frames" or "all baselines processed all frames with gradient checkpointing"). If baselines were subsampled, justify why this is a fair comparison or re-run with a matched number of frames.
2. **Add GPU memory and inference time measurements** for ART-STVG vs. at least one baseline (e.g., TA-STVG) across video lengths.
3. **Provide basic statistics of the extended benchmarks** (target interval duration distribution, ratio of target duration to video length) and clarify whether ground-truth annotations were modified.
4. **Add one experiment**: run ART-STVG in a parallel mode (process all frames at once with the same memory banks) to isolate the benefit of streaming vs. memory components.

## Score and Decision

**Calibration anchors (all retrieved):**

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/WOzffPgVjF.md` (TA-STVG) | 7.50 | **Higher** — Clean evaluation protocol on established benchmarks; no ambiguities about test-time processing. TA-STVG's experiments are fully verifiable from the paper, unlike the current one. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/14fFV0chUS.md` (TRACE) | 6.75 | **Higher** — Well-executed evaluation on multiple benchmarks with clear experimental design. The current paper's problem framing is stronger, but the evaluation is less transparent. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/yHj6EunfVQ.md` (CoSPaL) | 5.50 | **Comparable** — Novel problem framing with some methodological concerns; accepted despite missing ablations. The current paper has more thorough ablations but a more critical evaluation gap. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/O8FkMqNF1M.md` (LangRepo) | 5.50 | **Comparable** — Novel framework for long-video understanding with evaluation transparency concerns that contributed to rejection. The current paper has a similar pattern of interesting ideas undermined by evaluation gaps. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/1DEHVMDBaO.md` (Adaptive Memory) | 4.60 | **Lower** — Memory-based method for long videos but with weaker empirical results and limited novelty. The current paper has clearer contributions and stronger ablations. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/bEvI30Hb2W.md` (LVM-Net) | 3.00 | **Lower** — Poor performance vs. baselines, limited evaluation. The current paper is substantially stronger in both method and results. |

The paper makes a genuine contribution by formulating LF-STVG and proposing a well-motivated streaming architecture. The method is sensible, and the ablations provide clear evidence for each design choice. However, the experimental comparison that forms the paper's headline result is compromised by the absence of the test-time processing details for baselines. This omission is not a minor presentation issue — it directly affects whether the reported improvements reflect genuine superiority or an evaluation artifact. Until this is resolved, the central claims are not fully verifiable. This places the paper below the stronger, cleanly-evaluated papers in its area (6.5–7.5) but above papers with weak contributions or poor results (3.0–4.5). Score reflects that the contributions are real but the main empirical evidence is currently incomplete.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>