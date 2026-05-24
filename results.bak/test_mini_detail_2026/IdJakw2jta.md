## Summary

This paper introduces Long-Form Spatio-Temporal Video Grounding (LF-STVG), a new problem setting for localizing targets in videos spanning 1–5 minutes (compared to the standard ≤20 seconds). To address the memory bottlenecks that prevent existing STVG methods from handling longer videos, the authors propose ART-STVG, an autoregressive transformer that processes frames sequentially with selective spatial and temporal memory banks and a cascaded spatio-temporal decoder. ART-STVG substantially outperforms prior STVG methods on newly extended LF-STVG benchmarks (e.g., 15.0% vs. 8.1% m.tIoU on 5-minute videos) while remaining competitive on short-form STVG.

## Strengths

1. **Well-motivated, novel architecture for streaming long videos.** ART-STVG processes frames one at a time with spatial and temporal memory banks, directly addressing the GPU memory bottleneck that limits existing STVG methods (which process all frames in one pass). This is a principled design choice well suited to the long-video setting (Section 3.2, Figure 1).

2. **Memory selection strategies clearly boost performance.** Tables 2 and 3 show that selective temporal memory improves m.tIoU from 16.7% (no memory) to 23.0% (+6.3 points), and selective spatial memory adds a further +0.9% over using all memories. Figure 5 visually confirms that selective memory focuses attention on the target region. These ablations cleanly isolate each component's contribution.

3. **Cascaded spatio-temporal decoder is validated.** Table 4 shows the proposed cascaded design (spatial → temporal decoder) outperforms a parallel design by 1.5% m.tIoU and 1.4% m.vIoU on LF-STVG-3min, supporting the claim that fine-grained spatial information aids temporal localization in long videos.

4. **State-of-the-art results on LF-STVG with convincing trends.** Table 1 shows ART-STVG consistently outperforms all prior methods (TubeDETR, STCAT, CG-STVG, TA-STVG) across five extended benchmarks (1–5 min). The gap grows with video length — a 0.7% m.tIoU advantage on 1-min videos widens to 7.3% on 5-min videos — consistent with the claim that the autoregressive architecture's advantage compounds for longer inputs.

5. **Competitive short-form performance.** Table 7 shows ART-STVG achieves 59.2% m.tIoU on HCSTVG-v2 (20 sec), only 1.2% behind the current best TA-STVG, demonstrating that the long-form design does not sacrifice short-video capability.

6. **Robustness to training video length.** Table 6 shows that when all methods are trained on 40-second (vs. 20-second) videos, ART-STVG still dominates (28.3 vs. 20.8 m.tIoU for the next best TubeDETR), confirming the advantage is not merely from training data differences.

## Weaknesses

### Major

- **Underspecified dataset extension protocol.** The paper extends HCSTVG-v2 validation videos from 20 seconds to 1–5 minutes, stating only that extensions are "based on original YouTube videos, not concatenated clips" and "manually review[ed]...to ensure their quality" (Section 4, lines 254–258). It does not specify how the ground-truth temporal intervals and spatial annotations were defined for the longer videos. The original HCSTVG-v2 provides spatio-temporal tubes for 20-second clips; when the same clip is embedded in a longer video, the evaluation assumes the ground-truth interval carries over (same event, same frames, now positioned in a longer timeline). This interpretation is reasonable and standard, but the paper should state it explicitly. Without this clarity, readers cannot verify whether the evaluation metrics (m.tIoU, m.vIoU) are computed against a well-defined ground truth, which undermines confidence in the empirical results. **Impact**: A clear documentation gap that must be fixed — the authors should describe the annotation protocol for the extended videos, including whether the original temporal boundaries were reused or new annotations were obtained.

- **Frame budget for baselines is not reported.** The paper does not specify how many frames each baseline method (TubeDETR, STCAT, CG-STVG, TA-STVG) processed during inference on the 1–5 minute evaluation videos. ART-STVG processes frames sequentially at 3.2 fps (~576 frames for 3 min), while prior STVG methods typically sample a fixed number of frames (e.g., 36–64) due to GPU memory constraints. If baselines received an order of magnitude fewer frames than ART-STVG, the performance gap could partly reflect differential access to visual content rather than architectural superiority alone. Table 6's controlled experiment (training all methods on 40-sec videos) partially mitigates this concern, but the inference-stage frame budgets remain unstated. The authors should report how many frames each method used during evaluation, and ideally include a controlled experiment where baselines are given similar temporal coverage (e.g., via sliding-window or chunking).

### Minor

- **Results reported only on one dataset (HCSTVG-v2 extension).** The paper acknowledges that HCSTVG-v2 "is the only dataset which provides available source videos" (Section 4), which is a practical constraint, but the limitation to a single benchmark weakens the generality of the findings. The authors could mitigate this by evaluating on other long-video temporal grounding datasets (e.g., Charades-STA extended, ActivityNet) or by discussing the scope more directly.

- **No confidence intervals or variance estimates.** All results in Tables 1–7 are reported as single numbers. Given that the absolute m.tIoU values on longer videos are low (e.g., 15.0% on 5-min) and the improvements on 1-min videos are modest (0.7% over TA-STVG), variance estimates (multiple seeds or bootstrap) are needed to assess whether the reported gains are statistically meaningful.

- **Baseline architecture deferred to supplementary.** The baseline — described as having "similar architecture to our ART-STVG but without memory and memory selection modules" — is critical for interpreting Table 1 and all ablations but is only defined in the supplementary material. A brief definition in the main text would aid readability.

- **Low absolute performance on longer videos deserves discussion.** ART-STVG achieves only 15.0% m.tIoU on 5-minute videos (Table 1e). While this substantially exceeds baselines (next best: 8.1%), the low absolute numbers suggest the task is extremely challenging. The paper would benefit from failure analysis or qualitative examples showing where the model breaks down (e.g., event outside memory capacity, drift in spatial tracking).

### Trivial

- The "deconcat" step in Equation 2 splits fused features back into appearance/motion/text components, but since self-attention mixes all tokens, the resulting components are no longer modality-pure. The paper should clarify what "enhanced" means in this context.
- The spatial query is initialized to zeros (Section 3.2). A brief justification or citation to DETR-style initialization would be useful.
- No inference cost (GPU memory, speed) comparison with baselines, despite this being a key motivation for the autoregressive design.

## Nice-to-Haves

- An experiment giving baselines more frames via sliding-window or chunked inference to equalize temporal coverage and isolate the architectural benefit.
- Inference-time GPU memory usage and latency comparison on the longest videos.
- Human evaluation or inter-annotator agreement on the extended dataset annotations, if available.
- A discussion of why ART-STVG's m.tIoU drops from 39.1% (1 min) to 15.0% (5 min) — how much of this is due to the autoregressive drift vs. the task becoming harder.

## Removed Points

- **Weakness about dataset validity being "fatal" / "unverifiable"**: The harsh critic claimed the annotation ambiguity makes the entire evaluation uninterpretable. This is an overstatement. For HCSTVG-v2, the ground-truth annotations (temporal intervals + bounding boxes per frame) are defined for the original 20-second clips. When extended to longer videos from the same YouTube source, the same event occurs in the same contiguous segment; the ground-truth carries over implicitly. The paper should clarify this, but the results are not unverifiable. Downgraded from the critic's "Fatal" to a Major documentation gap.

- **Weakness about comparison being "fundamentally unfair" due to frame counts**: The critic argued that if baselines use fewer frames than ART-STVG, the comparison is "fundamentally unfair." However, the baselines' inability to process all frames due to GPU memory constraints is *precisely* the limitation that ART-STVG is designed to overcome. The comparison is valid for demonstrating the architectural advantage, though the paper should still report the frame budgets for transparency. Downgraded from "fundamentally unfair" to a Major documentation gap.

- **Weakness about memory selection being "heuristic"**: The critic called the similarity-based memory selection "heuristic but plausible." This is standard practice in memory-augmented models and is not a genuine weakness — it is a design choice supported by ablation evidence.

- **Strengths from Strength Finder about the problem being "important" / "timely" / "well-motivated"**: These are generic praise about the research topic, not specific evidence of contribution quality. Removed as they add no information specific to this paper's execution.

- **Strength about "Systematic ablation study isolates each component's contribution"**: While partly true, the ablation is on a single dataset length (3-min) only, limiting its generality. Rephrased as a minor concern rather than a standalone strength.

- **Strength about "Robustness to training video length"**: This is a genuine strength and is retained.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the dataset documentation and baseline fairness concerns but do not add fundamentally new observations about the method or problem.

## Suggestions

1. **Clarify the annotation protocol for LF-STVG datasets.** Explicitly state whether the original 20-second temporal intervals and per-frame boxes were reused, and how the extended videos were aligned with the original source videos. If the ground-truth carries over unchanged, say so directly.

2. **Report frame budgets for all baselines during inference.** For each baseline method on each LF-STVG benchmark (1–5 min), state the number of frames processed and the sampling strategy. Consider adding a controlled experiment where baselines use sliding windows or chunked processing to match ART-STVG's temporal coverage.

3. **Report variance.** Run each experiment with at least 3 random seeds or report bootstrap confidence intervals for the main metrics.

4. **Expand the baseline description to the main paper.** At minimum, state whether the baseline uses the same autoregressive decoder without memory banks, or a different architecture entirely.

5. **Add inference cost analysis.** Report GPU memory usage and per-video inference time for ART-STVG vs. baselines on the longest videos to substantiate the claimed efficiency advantage.

6. **Include failure analysis.** With absolute m.tIoU around 15% on 5-minute videos, qualitative examples of successes and failures would significantly strengthen the paper.

## Score and Decision

**Bracketing (Round 1)**: The paper was compared against three calibration bands:
- Weak band (<3.5): WZB5wh0qVR (3.33, withdrawn), 8I8NNAcosC (3.00, withdrawn), oUSQnvL8xA (2.80, withdrawn), W3QN1SERzH (3.33, withdrawn). All are rejected/withdrawn papers. The current paper is clearly stronger — it has a well-designed architecture and credible experimental results.
- Middle band (3.5–7.5): zuPxAZgT9F (4.67, accepted poster), PaMyTXkyY4 (4.00, withdrawn), XOuHTBLrPP (4.50, reject). The current paper has stronger methodological novelty than XOuHTBLrPP and PaMyTXkyY4, and comparable contributions to zuPxAZgT9F (STVG-R1).
- Strong band (>7.5): kkBOIsrCXh (8.00, poster), kI27Niy4xY (8.00, oral), DM0Y0oL33T (8.00, oral), oBXfPyi47m (8.00, poster). These are substantially different topics (navigation, text-to-3D, RL, multimodal reasoning) with stronger empirical rigor. The current paper is not in this league.

**Initial bracket**: 4.0–6.0.

**Narrowing (Round 2)**: 
- wARprQ4toq (4.00, reject, StreamMem): Streaming video memory method, rejected for limited novelty. The current paper has more architectural innovation.
- BO4zC3xndr (4.67, reject, Video-in-the-Loop): Long-video QA framework. Similar scope; the current paper has comparable quality.
- FtdbdoGbk3 (5.50, accepted poster, Memento): Ultra-long streaming video memory framework. The current paper is slightly weaker on dataset rigor but has comparable method contribution.
- azcQJtcYTE (6.67, accepted poster, OmniSTVG): New STVG task + large-scale manually annotated dataset. The current paper is notably weaker on dataset construction rigor.
- gygGCVXeh3 (5.33, accepted poster): Domain-specific benchmark. Not directly comparable.
- QQCrZXWG9s (6.00, accepted poster): Temporal grounding with inversion tasks. Stronger evaluation.

The current paper is clearly above the 4.0 reject-level papers (due to stronger architectural novelty) but below the 6.0+ strong-accept papers (due to weaker dataset rigor and evaluation controls). It sits closest to the 4.67–5.50 band. Within that band, it is comparable to STVG-R1 (4.67, accepted poster) and Memento (5.50, accepted poster) — both had similar experimental gaps but were ultimately accepted.

**Final score**: **5.0**. This reflects a paper with genuine contributions (new problem, well-designed method, thorough ablations) that is held back by two significant experimental documentation gaps: an underspecified dataset annotation protocol and unreported baseline frame budgets. The core ideas are sound, and the weaknesses are addressable with additional clarity and controlled experiments, placing this at a borderline-accept level.

**Round-3 optional**: Not needed — the bracket is well-resolved with Round 2 anchors.

**Decision**: **Accept** (borderline). The paper introduces a genuinely new problem and a well-designed solution. The main concerns are documentation and clarity, not fundamental flaws. With the suggested revisions to clarify the dataset protocol and report baseline frame budgets, the paper would be suitable for presentation.

**Anchors considered:**
- zuPxAZgT9F (STVG-R1, avg 4.67, accepted poster): Similar domain; STVG-R1 had comparison fairness concerns and limited datasets. The current paper has stronger architectural novelty but similar experimental gaps. Current paper is slightly stronger overall. Read in full.
- PaMyTXkyY4 (VTG-Reasoner, avg 4.00, withdrawn): Similar long-video temporal grounding topic. The current paper has more novel architecture (vs. GRPO application). Current paper is stronger. Read in full.
- XOuHTBLrPP (TAR-TVG, avg 4.50, reject): Temporal grounding with RL. The current paper has more architectural novelty. Current paper is stronger. Read in full.
- FtdbdoGbk3 (Memento, avg 5.50, accepted poster): Streaming video memory. Comparable scope and quality; current paper is slightly weaker on dataset rigor. Read in full.
- azcQJtcYTE (OmniSTVG, avg 6.67, accepted poster): New STVG task + large dataset. Current paper is weaker on dataset construction. Preview only.
- wARprQ4toq (StreamMem, avg 4.00, reject): Streaming video memory. Current paper is stronger. Preview only.
- BO4zC3xndr (Video-in-the-Loop, avg 4.67, reject): Long-video QA. Current paper is comparable or slightly stronger. Preview only.
- WZB5wh0qVR, 8I8NNAcosC, oUSQnvL8xA, W3QN1SERzH: All <3.5, withdrawn/rejected. Current paper is clearly stronger. Previews only.
- kkBOIsrCXh, kI27Niy4xY, DM0Y0oL33T, oBXfPyi47m: All 8.0, different topics. Not directly comparable. Previews only.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Accept</decision>