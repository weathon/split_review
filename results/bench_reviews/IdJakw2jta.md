Now I have a thorough understanding of the paper and calibration anchors. Let me compile the final review.

---

## Summary

This paper introduces Long-Form Spatio-Temporal Video Grounding (LF-STVG), a new task that extends STVG to 1–5 minute videos, and proposes ART-STVG, an autoregressive transformer that processes frames sequentially with spatial and temporal memory banks augmented by memory-selection strategies and a cascaded spatio-temporal decoder. The authors construct extended test sets from HCSTVG-v2 at five video-length tiers and show that ART-STVG substantially outperforms existing short-form STVG methods on these long-form benchmarks, while remaining competitive on standard short-form evaluation.

## Strengths

- **Novel problem formulation with constructed benchmarks.** The paper identifies a genuine gap between short-form STVG research and real-world long-video applications, and builds five extended test sets (LF-STVG-1min through -5min) from HCSTVG-v2 source videos. The benchmarks are constructed from original YouTube videos (not concatenated clips) and manually reviewed for quality (Section 4, lines 571–586).

- **Well-motivated and carefully ablated architecture.** The autoregressive streaming design is a natural fit for long videos and is supported by thorough ablations: temporal memory selection raises m_tIoU from 9.6% (all memories) to 23.0% (Table 2), spatial memory selection adds 0.9 m_tIoU (Table 3), and the cascaded decoder outperforms a parallel design by +1.5 m_tIoU (Table 4). These component-level gains are substantial and internally consistent.

- **Strong empirical performance with controlled internal baseline.** ART-STVG achieves 23.0% m_tIoU on LF-STVG-3min vs. 13.9% for TA-STVG, with the gap widening as video length increases (Table 1). Critically, the paper includes a controlled autoregressive baseline (same architecture minus memory banks) that ART-STVG dramatically exceeds across all video lengths, providing a clean within-architecture comparison.

- **Efficiency advantage for long videos.** ART-STVG uses 7.9 GB GPU memory vs. ~25 GB for comparable one-stage methods on 64 frames (Table 8), directly demonstrating the computational bottleneck of all-at-once processing that motivates the streaming design.

- **Competitive on short-form STVG.** ART-STVG achieves 59.2 m_tIoU on HCSTVG-v2 (Table 7), trailing TA-STVG by only 1.2 points, showing the autoregressive design does not inherently sacrifice short-clip accuracy.

## Weaknesses

### Fatal

None.

### Major

- **Baseline inference protocol for existing methods on long videos is not described.** Section 4.1 states that all methods are trained exclusively on 20-second clips but provides no details on how TubeDETR, STCAT, CG-STVG, and TA-STVG — models designed to process all frames at once — were run on 1–5 minute videos containing hundreds of frames. The paper's own efficiency analysis (Table 8) shows these methods require ~25 GB for only 64 frames. How did they handle 3–5 minute videos? Were frames subsampled? Was a sliding window used? Did any methods hit OOM? Without this information, readers cannot assess whether the reported near-zero scores for existing methods on longer videos (e.g., TA-STVG at 7.7 m_tIoU on 5-min) reflect genuine grounding failure or an artifact of the inference setup. The paper's internal baseline comparison (autoregressive with vs. without memory) provides a controlled anchor, but the headline comparison with published methods is under-specified. This can be addressed in rebuttal by disclosing the protocol.

### Minor

- **Zero-shot length-generalization framing not foregrounded.** The abstract and introduction present LF-STVG as a new task without clearly stating that all evaluation is zero-shot length generalization (trained on 20-second clips, tested on 1–5 minute videos). The paper does disclose this in Section 4.1 (lines 622–624) and partially addresses it via Table 6 (training on 40-second videos helps all methods), but a reader of the abstract alone would not understand this constraint. The framing is not dishonest — the disclosure exists — but the contribution would be more precisely characterized as "length-generalized STVG" rather than a fully realized LF-STVG with matched training and test distributions.

- **Memory bank scalability not characterized beyond 64 frames.** The efficiency analysis (Table 8, Appendix C) only reports numbers for 64 frames, aligned to the short-form training length. For a method whose core justification is handling longer videos, an analysis of GPU memory usage and inference time as a function of video duration (e.g., at 1, 2, 3, 4, 5 minutes) would substantially strengthen the paper. That said, the memory selection strategies (top-Ns = 32 for spatial; nearest-event for temporal) naturally cap the attention computation regardless of bank size, so this is more of a missing characterization than a scalability flaw.

- **Heuristic temporal memory selection relies on TextTiling-based boundary detection.** Table 2 shows a striking dependence: using all temporal memories drops m_tIoU to 9.6% while the boundary-detection heuristic recovers to 23.0%. If the TextTiling heuristic produces poor boundaries (e.g., for videos with subtle event transitions), performance could degrade sharply. The failure case analysis in Appendix D acknowledges indistinct event boundaries as a failure mode, but the paper does not quantify how often the boundary heuristic makes errors independently of the overall grounding task.

### Trivial

- The paper defers the loss function (Section 3.5) to supplementary material; a brief in-text summary would aid readability.
- Some table formatting artifacts from PDF extraction make parts of the method section hard to parse, though these are parser issues, not author errors.

## Nice-to-Haves

- A learned attention-based selection over the spatial memory bank (replacing the text-similarity heuristic) could be explored, as could learned temporal memory selection.
- Error bars or per-video diagnostic distributions would provide better insight into performance variance, though single-run evaluation is standard in STVG.
- Comparison with memory-augmented long-video understanding models (e.g., MA-LMM, MovieChat) adapted to STVG would contextualize the memory design, but the paper discusses conceptual differences with these works in Appendix F.

## Removed Points

These points are flagged to be removed, treat them with caution.

**From Harsh Critic — Critical Issue 1 (claiming the comparison "invalidates the paper's principal experimental contribution"):** While the baseline protocol is indeed under-described (kept as a major weakness above), the harsh critic's conclusion that this alone invalidates the paper is unjustified. The paper provides a controlled internal comparison (autoregressive baseline without memory), thorough component ablations (Tables 2–5), and cross-length trends (Table 1) showing ART-STVG's advantage grows with video length. The existing methods' scores are not "near-zero" in a way that suggests catastrophic failure — they show plausible degradation patterns (TA-STVG: 38.4 → 25.3 → 13.9 → 10.1 → 7.7 across 1–5 min). The paper also explicitly acknowledges these methods face computational bottlenecks (lines 126–131) that motivate the streaming design. The missing detail is a transparency issue, not evidence of invalid results.

**From Harsh Critic — Critical Issue 2 (claiming "training–test mismatch misrepresents the LF-STVG problem"):** The paper discloses the training regime in Section 4.1 (lines 622–624) and partially addresses it with longer-training experiments in Table 6. The abstract could be more precise, but the paper does not hide this constraint and the harsh critic's characterization as "misrepresents" is overstated.

**From Harsh Critic — "No error bars or per-video diagnostics" (Section-by-Section on 4.1):** Single-run evaluation without confidence intervals is standard practice in STVG benchmarking (see, e.g., all compared methods in Table 1 and the short-form results in Table 7, none of which report error bars). Demanding them here while accepting their absence in all cited prior work is a double standard. The same applies to the harsh critic's demand for "per-video diagnostics."

**From Harsh Critic — "Memory-bank baselines: Compare against memory-augmented long-video models" (Missing Experiments #3):** The paper already discusses differences with existing memory-based video understanding methods in Appendix F (lines 1239–1271), noting their memory serves global context while ART-STVG's is task-specific. Direct empirical comparison would require adapting models designed for VQA to STVG, which is beyond reasonable scope.

**From Harsh Critic — "Learned vs. heuristic selection" (Deeper Analysis #3):** This is a reasonable future direction, not a missing experiment. The paper proposes and validates heuristic selection; exploring learned alternatives is scope creep.

**From Strength Finder — generic strengths:** All three strengths from the Strength Finder are specific and evidence-backed. None were dropped.

## Novel Insights

The paper's most interesting finding is the interaction between memory banks and selection strategies: naively accumulating all memories *hurts* performance (Table 2: all temporal memories drops m_tIoU from 16.7% to 9.6%), but with intelligent selection the same memory bank provides a dramatic 13.4-point gain. This "memory is harmful unless selected" dynamic is counter-intuitive and implies that for long-form video tasks, the primary challenge is not storing history but knowing *which* history is relevant. The cascaded spatial→temporal design (+1.5 m_tIoU over parallel) further suggests that fine-grained spatial cues can bootstrap temporal reasoning in ways not exploited by prior STVG methods.

## Suggestions

- In rebuttal, clearly describe the inference protocol used for existing STVG methods on long-form videos (frame count, any subsampling, whether any models encountered OOM, and how those cases were handled). Even a brief statement would resolve the major weakness.
- Add a sentence to the abstract clarifying the zero-shot length-generalization evaluation setting.
- Report GPU memory and inference time for ART-STVG at 1-min, 3-min, and 5-min video lengths (not just 64 frames) in a revision.
- Consider quantifying the TextTiling boundary-detection accuracy independently of the full STVG pipeline to provide insight into the temporal memory selection reliability.

## Score and Decision

**Anchor comparison:**

| Anchor | Avg Score | Comparison |
|--------|-----------|------------|
| `/home/wg25r/review_agent/human_reviews_2026/azcQJtcYTE.md` (OmniSTVG) | 6.67 | New STVG task + dataset + model with cleaner experimental execution. Our paper has comparable ambition but less rigorous baseline description. Below this. |
| `/home/wg25r/review_agent/human_reviews_2026/gVbPWbA97s.md` (StreamingVLM) | 6.00 | Streaming approach for long videos with its own benchmark. More thorough efficiency characterization and clearer baseline protocol. Our paper is slightly below. |
| `/home/wg25r/review_agent/human_reviews_2026/QQCrZXWG9s.md` (Invert4TVG) | 6.00 | Temporal video grounding with inversion tasks. Solid contribution with good ablations. Our paper has broader scope (spatial + temporal) but less experimental clarity. |
| `/home/wg25r/review_agent/human_reviews_2026/vIecIscDJf.md` (HiTeA) | 5.50 | Training-free temporal grounding for long videos. Limited novelty but decent results. Our paper has more architectural novelty and better ablations. Comparable tier. |
| `/home/wg25r/review_agent/human_reviews_2026/YCoUgpYqGP.md` (Open-o3 Video) | 5.00 | Grounded video reasoning. Dataset + training contribution. Our paper has clearer task definition and stronger ablations. |
| `/home/wg25r/review_agent/human_reviews_2026/BOFzC3xndr.md` (ViTL) | 4.67 | Long video QA with similar experimental transparency gaps. Our paper has more thorough component ablations and a cleaner internal baseline. Above this. |
| `/home/wg25r/review_agent/human_reviews_2026/zuPxAZgT9F.md` (STVG-R1) | 4.67 | STVG with RL, marginal improvements over baselines. Our paper demonstrates larger performance gains and more substantive architectural contributions. Above this. |
| `/home/wg25r/review_agent/human_reviews_2026/WZB5wh0qVR.md` (VideoMolmo) | 3.33 | Weak architecture novelty. Our paper is clearly above. |
| `/home/wg25r/review_agent/human_reviews_2026/8I8NNAcosC.md` (VideoITG) | 3.00 | Withdrawn. Our paper is clearly above. |

The paper introduces a genuinely new problem (LF-STVG), constructs evaluation benchmarks, proposes a well-motivated method with strong ablations, and demonstrates clear performance improvements. The major weakness — unspecified baseline inference protocol — is a transparency issue that can be resolved in rebuttal rather than a fundamental flaw. The paper's internal baseline comparison and component ablations provide controlled evidence that does not depend on the external baseline protocol. Compared to anchors, it sits between HiTeA (5.50) and StreamingVLM (6.00), with stronger novelty than HiTeA but less experimental rigor than StreamingVLM.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>