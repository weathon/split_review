Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper introduces Long-Form Spatio-Temporal Video Grounding (LF-STVG), a new task targeting target localization in videos spanning minutes rather than tens of seconds. The authors propose ART-STVG, an autoregressive transformer that processes frames sequentially using spatial and temporal memory banks with selection strategies and a cascaded spatial-to-temporal decoder. They create five LF-STVG benchmarks (1–5 minutes) by extending HCSTVG-v2, and show substantial improvements over existing short-form STVG methods, with gains growing on longer videos (e.g., +6.9 m.tIoU on 5-minute videos). The method also achieves competitive results on the original short-form benchmark.

## Strengths

- **Clear and well-motivated new task formulation.** LF-STVG fills a genuine gap: existing STVG research focuses on videos under a minute, while real applications (surveillance, video retrieval) routinely involve multi-minute footage. The paper articulates why processing all frames at once (the existing paradigm) is fundamentally unsuitable for long videos, making the case for an autoregressive streaming approach.

- **Consistent and significant outperformance across all five LF-STVG benchmarks.** Table 1 shows ART-STVG surpassing all prior methods (TubeDETR, STCAT, CG-STVG, TA-STVG) on every video length, with the advantage widening on longer videos (e.g., +0.7/0.9% on 1-minute → +6.9/5.5% on 5-minute for m.tIoU/m.vIoU). This directly validates the core thesis that autoregressive streaming with selective memories is the right design for long videos.

- **Ablation studies support every major design choice.** Controlled experiments (Tables 2–5) quantify the contribution of each component: selective temporal memory (+13.4% m.tIoU over all-memory), selective spatial memory (+0.9%), cascaded decoder over parallel (+1.5%), and the memory size hyperparameter. These ablations are cleanly isolated and provide direct evidence that gains come from the proposed mechanism, not confounds.

- **Creation of the first LF-STVG evaluation benchmarks.** The paper extends the HCSTVG-v2 validation set to five controlled video-length conditions (1–5 minutes) using original YouTube videos (not concatenated clips), enabling reproducible evaluation for the new task.

- **Competitive on short-form STVG despite being designed for long-form.** ART-STVG achieves 59.2 m.tIoU on HCSTVG-v2, trailing the SOTA (TA-STVG) by only 1.2% (Table 7), demonstrating that the autoregressive design does not sacrifice short-form capability.

## Weaknesses

### Major

- **Evaluation protocol for baselines on long videos is not disclosed.** The paper compares ART-STVG against methods (TubeDETR, STCAT, CG-STVG, TA-STVG) originally designed to process all frames at once with full self-attention, on videos of 1–5 minutes (960+ frames at 3.2 FPS). It does **not** describe how these baselines were adapted — were frames subsampled? Was a sliding window used? Were the methods modified to avoid memory overflow? The paper states only that all methods were "trained exclusively on the HCSTVG-v2 training set" (Sec. 4.1), which addresses training fairness but not evaluation feasibility. Without this information, the reader cannot assess whether the reported baseline numbers reflect genuine limitations of those methods or a mismatched evaluation protocol. This is the most significant weakness because it affects trust in the paper's central quantitative claim. The authors should explicitly describe the evaluation protocol used for each baseline on each LF-STVG benchmark.

### Minor

- **The "all temporal memories" ablation shows all-memory (9.6% m.tIoU) performing worse than no-memory (16.7%), which is discussed but not deeply analyzed.** The paper attributes this to "irrelevant information" from multiple events. However, since the model is trained on 20-second videos (small memory banks) and tested on 5-minute videos (large, noisy banks), the catastrophic drop may partly reflect a training/inference capacity mismatch that the selection strategy compensates for. The paper would benefit from analyzing why adding memory (even with selection) helps so dramatically compared to no memory, and whether the selection heuristic is merely patching this mismatch rather than providing genuine long-range context.

- **Figure 2 axis labels are inconsistent with the paper's metrics.** The bar charts in Figure 2 show "m_Ap@1 (%)" and "m_Ap@5 (%)" on the y-axes, while the paper's evaluation uses m.tIoU, m.vIoU, and vIoU@R (Table 1). This discrepancy is confusing and should be harmonized.

- **No error bars or variance estimates.** Given the complexity of the task and the moderate evaluation set sizes (~2,000 validation samples extended to 1–5 minutes), reporting standard deviations or confidence intervals across runs would strengthen the reliability of the claimed improvements.

- **Baseline architecture description is deferred to supplementary.** The "Baseline (ours)" row in Table 1 is important for understanding the contribution of the memory and selection modules, but its architecture is only briefly summarized ("similar architecture … without memory and memory selection modules") with a reference to supplementary material. A short description of whether it uses the cascaded design and autoregressive decoder would aid reproducibility.

### Trivial

- The figure caption in Figure 2 refers to metrics ("m_Ap@1", "m_Ap@5") that do not match the text and tables (m.tIoU, m.vIoU).

## Nice-to-Haves

- **Computational cost comparison.** The paper motivates ART-STVG partly by the computational bottleneck of processing all frames at once, but provides no GPU memory or runtime comparison. A simple table showing peak memory and inference time per frame (or per video) for ART-STVG vs. baselines on a 5-minute video would concretely validate this motivation.
- **Alternative selection strategies.** The paper's memory selection heuristics (text-similarity for spatial, event-boundary cosine-similarity for temporal) are simple and effective, but the paper does not test whether learned alternatives (e.g., attention-based gating) would further improve performance, leaving the optimality of the heuristics an open question.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *"First to explore LF-STVG claim needs more justification"* — The paper states "To our best knowledge, this paper is the first to explore the LF-STVG problem" (Sec. 1). The paper explicitly discusses that existing STVG methods process all frames at once (incompatible with long videos) and that no prior STVG datasets exist for videos longer than a minute. This is sufficient justification for a first-exploration claim in a conference paper.
- *"Spatial memory selection only gives 0.9% gain"* — This is presented as an ablation finding, not a weakness. A 0.9% gain is a positive result supporting the design, not a failure. The paper does not overclaim it.
- *"Training on 40-second videos uses a different training set"* — Table 6's 40-second experiment is explicitly described as an additional investigation using an extended training set, with all methods retrained for fair comparison. This is a valid experimental design, not a confounding factor.
- *"The paper should check whether existing methods could be trivially adapted"* — This is scope-creep. The paper's claim is that no prior work *explicitly* targets LF-STVG, which is factually correct. Whether existing methods could be adapted is an empirical question that the paper partially answers by evaluating them on the new benchmarks.
- *"Qualitative analysis could be larger"* — The existing qualitative results (Figures 5 and 6) are adequate. More examples would always be nice, but their absence is not a weakness.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Disclose the evaluation protocol for all baselines on long videos.** State exactly how many frames each baseline received, whether a sliding window or subsampling was used, and any modifications made to avoid memory overflow. This is the single most important fix.
2. **Add an analysis of the all-memory failure mode.** Discuss whether the 9.6% → 16.7% drop (all-memory vs. no-memory) reflects a training/inference memory bank capacity mismatch, and whether the selection strategy primarily mitigates this mismatch or provides genuine long-range context.
3. **Harmonize Figure 2's axis labels** with the metrics used in the paper (m.tIoU, m.vIoU).
4. **Add error bars or variance estimates** to the main tables (at least for the key comparisons).
5. **Include a computational cost table** (GPU memory, inference time) to validate the motivation.

## Score and Decision

**Calibration Protocol**

*Round 1 (Bracketing):* Searched for "spatio-temporal video grounding long videos" with band filters. Weak band (avg<3.5) returned papers scoring 3.00 (action recognition, object-centric learning). Middle band (3.5–7.5) returned CoSPaL (5.50, WSTVG), Grounded-VideoLLM (4.25), Motion-Grounded (5.00). Strong band (>7.5) returned papers on gesture video reenactment (8.50), dynamic radiance field (8.00), and long-form correspondence learning (8.00) — these address different problem settings and are not directly comparable. **Round-1 bracket: between 3.5 and 7.5.**

*Round 2 (Narrowing):* Searched within (4.5–6.5) for STVG/autoregressive/long-video topics, and (5.5–7.0) for new task/benchmark papers. Found ARLON (6.25, long video generation with AR+DiT), Language Repository (5.50, long video QA), InfiniBench (6.00, long video benchmark), CG-Bench (6.20, long video benchmark). Read full reviews of CoSPaL (5.50), Motion-Grounded (5.00), Grounded-VideoLLM (4.25), ARLON (6.25), and InfiniBench (6.00). 

**Comparison:** The current paper is clearly stronger than Grounded-VideoLLM (4.25) and Motion-Grounded (5.00), which had significant novelty and validity concerns. It is somewhat stronger than CoSPaL (5.50, accepted), which had unresolved questions about unfair comparison and module ablation. It is comparable to but slightly weaker than ARLON (6.25, accepted), which had its own evaluation gaps but benefited from clearer comparison baselines. The paper's main transparency gap (undisclosed baseline evaluation protocol) places it below the 6.0–6.25 range but above the 5.0–5.5 range.

**Final score: 5.5**

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| 2HdZPEQUig | Object-centric learning | 3.00 | 1 (weak) | Much weaker; no task definition, unclear contribution |
| ICR3swcnaa | Diffusion action recognition | 3.00 | 1 (weak) | Much weaker; limited novelty and evaluation |
| MSxCBXD5C8 | Anomalous action recognition | 3.00 | 1 (weak) | Much weaker; narrow scope |
| bEvI30Hb2W | LVM-NET long video | 3.00 | 1 (weak) | Much weaker; limited results |
| xYzOkOGD96 | Grounded video caption | 3.83 | 2 (mid) | Weaker; task less clearly defined |
| YCwN7wQA6W | Grounded-VideoLLM | 4.25 | 2 (mid) | Weaker; limited novelty, unfair comparison concerns |
| tEei1bolt3 | Motion-grounded reasoning | 5.00 | 2 (mid) | Weaker; motion understanding definition concerns |
| yHj6EunfVQ | CoSPaL WSTVG | 5.50 | 2 (mid) | Comparable; both have evaluation transparency concerns, but current paper has clearer task novelty |
| O8FkMqNF1M | Language Repository | 5.50 | 2 (mid) | Comparable; both address long-video understanding |
| IryGDUHxDE | Unsupervised AR action rec | 5.25 | 2 (mid) | Comparable; similar autoregressive approach |
| 2D0uXQbntW | InfiniBench | 6.00 | 2 (mid) | Slightly stronger on paper but rejected due to data concerns |
| le4IoZZHy1 | CG-Bench | 6.20 | 2 (mid) | Slightly stronger; cleaner evaluation |
| 8pusxkLEQO | ARLON | 6.25 | 2 (mid) | Slightly stronger; clearer baseline comparisons |
| 9Cu8MRmhq2 | Multi-granularity corresp. | 8.00 | 1 (strong) | Stronger; more mature evaluation |
| LbEWwJOufy | TANGO gesture reenactment | 8.50 | 1 (strong) | Stronger; different domain, polished evaluation |
| QQ6RgKYiQq | MovingParts | 8.00 | 1 (strong) | Stronger; different domain, thorough analysis |
| vaEPihQsAA | CyberHost | 7.60 | 1 (strong) | Stronger; different domain |

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>