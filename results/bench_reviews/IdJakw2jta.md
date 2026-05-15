Now I have a thorough understanding of both the paper and the anchor scores. Let me produce the final consolidated review.

---

## Summary

This paper introduces ART-STVG, a memory-augmented autoregressive transformer for Long-Form Spatio-Temporal Video Grounding (LF-STVG). Unlike existing STVG methods that process all video frames simultaneously, ART-STVG processes frames sequentially, maintaining spatial and temporal memory banks with selective retrieval strategies. A cascaded decoder design routes fine-grained spatial predictions into the temporal decoder. The paper extends the HCSTVG-v2 validation set to 1–5 minute videos (LF-STVG-1min through 5min) and demonstrates substantial improvements over prior STVG methods, with margins that grow as video length increases. Competitive short-form results confirm the architecture does not sacrifice performance on standard benchmarks.

## Strengths

- **Clear and well-motivated architectural design**: The autoregressive pipeline with separate spatial/temporal decoders, selective memory banks, and cascaded RoI feedback is logically structured. Each component addresses a specific challenge in long-form grounding (irrelevant content filtering, event boundary detection, spatial-to-temporal information flow).

- **Strong and consistent experimental gains on LF-STVG**: On LF-STVG-3min, ART-STVG achieves 23.0% m.tIoU versus 14.2% from the next best method (CG-STVG). The performance gap widens as video length increases (Table 1), directly supporting the claim that the autoregressive approach handles long videos more effectively.

- **Thorough internal ablations**: Tables 2–5 isolate the contributions of temporal memory selection (16.7% → 23.0% m.tIoU), spatial memory selection (21.3% → 23.0%), cascaded vs. parallel decoder design (21.5% → 23.0%), and the number of selective spatial memories (Ns). These controlled experiments provide direct evidence for each design choice.

- **Competitive short-form performance**: On the standard HCSTVG-v2 validation set (Table 7), ART-STVG achieves 59.2% m.tIoU / 39.2% m.vIoU, only 1.2/1.0 points behind the best dedicated short-form method (TA-STVG), showing the autoregressive design does not sacrifice short-video capability.

- **Novel memory selection strategies**: The spatial memory selection (via text–memory similarity) and temporal memory selection (via adjacent cosine similarity for event boundary detection, inspired by TextTiling) are creative, well-motivated, and empirically validated. The qualitative visualizations (Figures 5–6) effectively illustrate their operation.

## Weaknesses

### Fatal
None.

### Major

- **Computational efficiency claim is unsubstantiated**: The paper repeatedly asserts that the autoregressive design "resolves the computational bottleneck" of processing all frames at once (Section 1, line 90), yet no empirical runtime, GPU memory, or throughput comparison against any baseline is provided. This is a core motivating claim that the experiments do not validate. A simple wall-clock time or peak-memory plot across video lengths would substantially strengthen the paper.

### Minor

- **Loss function deferred entirely to supplementary material**: Section 3.5 provides only a single sentence stating the loss is in the supplementary. While conference page limits motivate this, the main paper should include at least a concise summary of how the spatial box loss and temporal start/end losses are formulated and combined, as the loss design directly affects the model's optimization behavior and the interpretation of ablation results.

- **Baseline inference protocol on long videos is not specified**: The paper does not describe how non-autoregressive baselines (TubeDETR, STCAT, CG-STVG, TA-STVG) process long videos at test time (e.g., frame subsampling, sliding windows, or full-sequence processing). While these are published methods with established defaults, the protocol directly affects the fairness of the comparison and should be stated. The results are still interpretable given the consistent degradation patterns across all methods, but the omission weakens reproducibility.

- **LF-STVG framing could be more precise**: The paper introduces LF-STVG as a new problem setting, yet all models (including ART-STVG) are trained exclusively on 20-second clips. The evaluation is more accurately described as zero-shot length generalization rather than a fully realized long-form STVG task with long-form training data. The paper transparently discloses the training setup (Section 4.1), so this is a framing refinement rather than a methodological flaw.

- **Training clip length of 64 frames at 3.2 FPS equals exactly 20 seconds**, matching the original HCSTVG-v2 video length. For inference on 5-minute videos, the model never experiences a temporal context exceeding 20 seconds during training. While the paper is transparent about this, the limitation is not discussed, and Table 6 (training on 40-second videos) shows that all methods benefit from longer training clips, suggesting this is a nontrivial constraint.

### Trivial

- **Memory bank grows without bound**: The paper acknowledges that memories are added "without removing any existing memories" (line 206). For 5-minute videos at 3.2 FPS this means ~960 entries per bank partition, which is manageable but worth noting as a scalability consideration for hour-long videos.

- **Temporal memory boundary detection threshold is not reported**: The cosine-similarity-based event boundary detection is inspired by TextTiling, but the specific threshold value for identifying boundaries is not stated in the main paper. Only qualitative results are shown (Figure 6).

## Nice-to-Haves

- A quantitative evaluation of the temporal memory segmentation accuracy (e.g., how well the cosine-based boundary detection aligns with ground-truth event boundaries) would strengthen the temporal memory selection analysis.
- Sensitivity analysis of performance to the FPS sampling rate, which determines both temporal granularity and effective context length.
- Comparison or discussion of how the approach relates to or could integrate with recent MLLM-based video grounding methods.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"The experimental comparison on long-form videos is fatally underspecified and likely unfair"** (Harsh Critic Issue 1, rated as "fatal"): The paper clearly states that all methods use the same training data (HCSTVG-v2, 20s videos) and the baselines are published methods with standard inference protocols. The consistent degradation pattern across all methods as video length increases is robust evidence. The harsh critic's assertion that "the results in Table 1 and Figure 2 have no interpretable meaning" is an overstatement — the relative trends and large margins are meaningful regardless of specific test-time implementation details. The specification gap is real but minor.

- **"The problem setting is misrepresented as a new task rather than a zero-shot length-generalisation test"** (Harsh Critic Issue 2): The paper transparently states training is on 20-second videos (Section 4.1). It introduces LF-STVG as a problem to explore and creates extended evaluation benchmarks. The claim that this is "misleading" is too harsh given the clear disclosure.

- **"No ablation explores alternative selection criteria (e.g., visual similarity, temporal proximity)"** (Harsh Critic section-by-section): The paper explicitly ablates the spatial memory selection mechanism (Table 3) and shows it improves performance. Demanding an exhaustive ablation of every possible alternative selection criterion is scope creep.

- **Strength Finder claim "Autoregressive streaming avoids computational bottlenecks"**: This is a paper claim, not independently verified by experiments. Weakened to reflect that the computational efficiency argument, while architecturally plausible, lacks empirical validation.

- **Strength Finder generic statements** about "clear conceptual design" and "competent writing" — these are kept only where supported by specific evidence.

## Novel Insights

The paper's memory selection strategies represent a genuinely novel synthesis: spatial selection via text-query similarity (borrowing from cross-modal retrieval) and temporal selection via adjacent-frame cosine similarity (borrowing from text segmentation / TextTiling). The insight that these two distinct selection mechanisms, applied in separate decoder streams, can be combined in a cascaded autoregressive architecture for long-form STVG is not obvious and is well-validated by the ablations. The finding that using *all* temporal memories actually hurts performance (9.6% vs. 16.7% without memory, Table 2) while selective memory dramatically helps (23.0%) provides a clean demonstration of the "irrelevant context" problem in long videos — a insight that may generalize beyond STVG.

## Suggestions

- Add a runtime/memory comparison (e.g., wall-clock time and peak GPU memory vs. video length) against at least one baseline to substantiate the computational bottleneck claim. This can be a single figure.
- Include a brief loss function summary in Section 3.5 even if full details remain in the supplementary — a few sentences on spatial (L1/GIoU) and temporal (binary cross-entropy per frame) loss formulation would suffice.
- Describe the baseline inference protocol (e.g., "baselines run with their default settings, processing all frames at the stated FPS").
- Discuss the 20-second training context limitation and its implications for very long videos (3–5 min), perhaps with a brief acknowledgment that Table 6 (40s training) shows room for improvement.

---

**Anchor comparison:**

| Anchor | Path | Avg Score | Comparison |
|--------|------|-----------|------------|
| OmniSTVG | `azcQJtcYTE.md` | 6.67 | Stronger contribution: new task + large-scale dataset (10K videos) + solid baseline. ART-STVG has comparable technical novelty but a weaker dataset contribution (validation-only extension vs. full benchmark). |
| STVG-R1 | `zuPxAZgT9F.md` | 4.67 | Similar-tier STVG paper. STVG-R1 has RL novelty but fairness concerns in comparison. ART-STVG has stronger architectural novelty, cleaner ablations, and fairer comparisons. |
| LongVTG-R1 | `8H1HmGH8ua.md` | 3.50 | Both tackle long-video grounding. LongVTG-R1 has overclaimed QA generalization and limited gains. ART-STVG has clearer claims, larger margins, and better-validated architecture. |
| VTG-Reasoner | `PaMyTXkyY4.md` | 4.00 | Both address long-video grounding with length generalization. VTG-Reasoner has limited novelty and missing comparisons. ART-STVG's architectural contribution is more substantial. |
| Video-in-the-Loop | `BOFzC3xndr.md` | 4.67 | Long-video QA with grounding. Different task but similar ambition level. ART-STVG has more direct and cleaner experimental validation of its core claim. |
| StreamMem | `wARprQ4toq.md` | 4.00 | Streaming video understanding with memory. ART-STVG has similar streaming motivation but stronger task-specific validation and larger experimental margins. |

ART-STVG sits clearly above the rejected papers (3.50–4.67 range for comparable long-video grounding work) due to genuine architectural novelty and strong ablations. It falls below OmniSTVG (6.67) which contributed both a new task definition and a large-scale dataset. The paper's core weakness — unsubstantiated computational efficiency claims — is addressable and does not threaten the main experimental findings.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>