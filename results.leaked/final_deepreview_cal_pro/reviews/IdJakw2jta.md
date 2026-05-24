Now I have a thorough understanding of the paper and the calibration anchors. Let me write the final consolidated review.

---

## Summary
This paper introduces Long-Form Spatio-Temporal Video Grounding (LF-STVG), extending the STVG task from short clips (~20s) to videos of 1–5 minutes. The authors propose ART-STVG, an autoregressive transformer that processes frames sequentially with two memory banks (spatial and temporal) augmented by simple selection strategies, and a cascaded spatial-to-temporal decoder. They construct five long-form benchmarks by extending HCSTVG-v2's validation set, and demonstrate that ART-STVG substantially outperforms existing STVG methods on these benchmarks while remaining competitive on short-form STVG.

## Strengths
- **Well-defined new problem with new benchmarks.** The paper identifies and formalizes LF-STVG, a practically motivated extension of STVG to longer videos. Five long-form benchmarks (1–5 min) are created by extending HCSTVG-v2 validation videos from original YouTube sources, with manual quality review. This addresses a genuine gap between current research and real-world applications.
- **Thorough and well-structured ablation studies.** Each component of ART-STVG is ablated cleanly: temporal memory selection (m.tIoU drops from 23.0% → 9.6% when removed, Table 2), spatial memory selection (23.0% → 22.1% without selection, Table 3), and cascaded vs. parallel decoder design (23.0% → 21.5%, Table 4). The ablations are internally consistent and clearly demonstrate each component's contribution.
- **Competitive short-form performance.** On the original HCSTVG-v2 validation set (Table 7), ART-STVG achieves m.tIoU 59.2% / m.vIoU 39.2%, trailing only TA-STVG (60.4%/40.2%) while outperforming most prior methods. This demonstrates the autoregressive design does not catastrophically sacrifice short-video performance.
- **Clear and intuitive architecture.** The sequential processing paradigm (Fig. 1), dual memory bank design (Fig. 3), and cascaded spatial-to-temporal connection are well-motivated and clearly described. The qualitative attention map visualizations (Fig. 5) help illustrate how selective spatial memory improves focus on target regions.

## Weaknesses

### Fatal
None.

### Major
- **Inference protocol for baseline methods is not described in the main text.** The paper's central claim — that ART-STVG decisively outperforms existing STVG methods (TubeDETR, STCAT, CG-STVG, TA-STVG) on long videos — depends on how those baselines were evaluated on videos of 1–5 minutes when they were designed to process all frames at once. The main text states only that all methods are trained on 20-second clips, but does not specify whether baselines processed all frames, used uniform downsampling, or applied some windowing strategy at inference. The paper references supplementary material for additional details (line 387), and Table 6 mentions using "provided source codes" of compared methods, suggesting these details may exist in the stripped appendix. However, the absence of this information from the main paper makes it difficult to fully assess the fairness of the headline comparison. This should be addressed in a rebuttal by explicitly describing the inference protocol and justifying why it gives baselines a fair chance.

### Minor
- **Claims about hour-long videos are not empirically supported.** The abstract and introduction motivate the work by referencing videos of "several minutes or even hours," but the longest evaluation is 5 minutes. While the streaming architecture theoretically supports longer videos, no results or analysis justify extrapolation to hour-long scales, and the memory bank's append-only design (line 206: "without removing any existing memories") would grow unboundedly at such lengths.
- **No discussion of computational cost or memory footprint.** The paper argues that existing methods face "computational bottlenecks" (line 88–89) and positions ART-STVG as resolving this, yet provides no measurements of GPU memory usage, inference latency per frame, or memory bank growth. For a method marketed for long-video efficiency, these practical metrics are important.
- **Memory selection strategies are heuristic with limited motivation.** Spatial memory selection uses similarity to text features, and temporal memory selection uses cosine similarity of adjacent memories (inspired by TextTiling). While the ablations show these work well, the paper provides no deeper justification for why these particular heuristics were chosen over alternatives, nor analysis of when they might fail.
- **Evaluation limited to one dataset family.** The benchmarks extend only HCSTVG-v2 (the only STVG dataset with available source videos). Testing on even one additional video source would strengthen confidence in generalizability.

### Trivial
- The paper lacks a limitations section. Explicitly acknowledging the reliance on pre-extracted motion features (VidSwin), the absence of memory pruning, and the 5-minute evaluation cap would improve transparency.
- The "Baseline (ours)" architecture description is deferred to supplementary material (line 266); its relationship to ART-STVG (e.g., whether it uses the cascaded design and same autoregressive propagation) should be summarized in the main text.

## Nice-to-Haves
- A controlled length-scaling experiment where all models (including baselines) are constrained to the same input frame budget (e.g., 64 frames sampled by different strategies) would help isolate the effect of the autoregressive architecture from the effect of seeing more/fewer frames.
- A qualitative failure-case analysis on 5-minute videos, showing where memory selection succeeds vs. fails, would make the method's behavior more interpretable.
- Training on even longer videos (beyond the 40-second extension in Table 6) could further validate the method's scaling properties.

## Removed Points
*These points were flagged for removal and should be treated with caution.*

- **"Comparison with existing methods is undocumented and may be unfair" (as a fatal flaw).** While the concern about undocumented inference protocol is valid (retained as Major above), the harsh critic framed this as a fatal, unverifiable flaw. However, since the paper references supplementary material that likely contains these details, and since it cannot be ruled out that the protocol is fair, this cannot be treated as fatal based on the main text alone. Downgraded to Major.
- **"Baseline (ours) is underdescribed."** The paper states the baseline architecture is in the supplementary material (stripped by the parser). Per instructions, weaknesses about missing appendix content are removed from the main weakness list. The trivial-tier note above captures the presentation concern.
- **"The paper lacks an appendix."** The appendix was stripped by the parser; the original submission includes one.
- **Criticism about the spatial/temporal memory selection being heuristic with "no motivation beyond it works."** Retained as Minor since it's factually accurate and substantive, but weakened since empirical validation is a legitimate form of support in systems papers.
- **Strength Finder's "the problem is important" framing** — retained only where grounded in specific evidence; generic importance claims without anchors were dropped.

## Novel Insights
The cascaded spatio-temporal decoder design — where the spatial grounding output (bounding box) is used to extract fine-grained target motion features via RoI pooling before temporal decoding — is a genuinely novel architectural insight. Rather than treating spatial and temporal grounding as parallel tasks (as all prior STVG work does), this design exploits the natural dependency: knowing *where* the target is helps determine *when* the event occurs. Table 4 validates this with a 1.5% m.tIoU gain over the parallel design, and the design principle may transfer to other spatio-temporal localization tasks.

## Suggestions
- In rebuttal, explicitly describe the inference protocol used for baseline methods on long-form videos (frame sampling strategy, maximum frames processed, any truncation/windowing). If frame budgets were matched or the protocol was designed to give baselines the best possible chance, state this clearly.
- Add a brief discussion of memory bank growth and potential mitigation strategies (e.g., fixed-capacity banks with eviction policies) to strengthen the claim of scalability to hour-long videos.
- Include at least ballpark computational metrics (e.g., GPU memory per frame, frames-per-second at inference) to substantiate the efficiency motivation.

## Score and Decision

**Calibration trace:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| 1DEHVMDBaO (AMM for long-form video) | 4.60 | R2 | ART-STVG is stronger: larger improvements, more baselines, better ablations |
| yHj6EunfVQ (CoSPaL for WSTVG) | 5.50 | R1 | ART-STVG is stronger: cleaner architecture, better internal ablations, clearer motivation |
| O8FkMqNF1M (Language Repository) | 5.50 | R2 | Comparable; both have novel architectures for long video with some evaluation concerns |
| QWDFOOoV3U (ResidualViT) | 5.75 | R1 | ART-STVG has broader evaluation and more dramatic results on its target problem |
| 14fFV0chUS (TRACE for VTG) | 6.75 | R2 | TRACE is slightly stronger: broader dataset coverage, more principled framework |
| 9Cu8MRmhq2 (Norton) | 8.00 | R1 | Norton is clearly stronger: multiple tasks, principled OT framework, flawless reviews |

**Bracket:** Round 1 placed the paper between 5.50 (CoSPaL, LangRepo) and 8.00 (Norton). Round 2 narrowed to approximately 5.5–6.75. ART-STVG is substantially stronger than the 4.60–5.50 anchors (better ablations, clearer motivation, larger gains) but falls below the 6.75 TRACE anchor (narrower evaluation scope, less principled framework). The evaluation protocol concern prevents it from reaching the high-6 range, but the strong internal ablations and well-defined new problem keep it above the 5.5 threshold.

**Final score: 6.0.** The paper makes a solid contribution by defining a new problem, constructing benchmarks, and proposing a well-ablated solution. The evaluation protocol concern and limited generalization are real but addressable weaknesses that do not invalidate the core contribution.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>