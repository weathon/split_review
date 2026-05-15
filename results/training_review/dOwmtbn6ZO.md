Now I have a thorough understanding of the paper and all reviews. Let me write the consolidated review.

## Summary

This paper proposes AVUA, an LLM-based agent framework for video understanding that dynamically samples frames based on the input query (query-adaptive sampling), uses an evaluator and refiner for self-reflective reasoning, and stores past trajectories in long-term memory. Evaluated on EgoSchema, Ego4D NLQ, MovieChat, and NextQA, the method accesses dramatically fewer frames than baselines while achieving competitive or improved accuracy (e.g., 66.98% vs. 62.4% on EgoSchema using 14.27 frames vs. 180 frames).

## Strengths

- **Query-adaptive dynamic frame sampling drastically reduces frame usage while improving accuracy, confirmed across multiple benchmarks.** On EgoSchema the method accesses only 14.27 frames (0.26%) yet achieves 66.98%, surpassing agent baselines using 180 frames (LifelongMemory 62.4%, VideoAgent 60.2%) (Table 1). On MovieChat it uses 13.59 frames vs. MovieChat's 2048, raising accuracy from 62.3% to 84.8% (Table 3). On Ego4D it accesses 80% fewer frames than agent baselines while improving IoU=0.5 by ~10 points (Table 2). This directly validates the core claim that query-adaptive sampling can simultaneously improve efficiency and effectiveness.

- **Feedback-driven reasoning (evaluator + refiner) is critical for strong performance, convincingly shown by ablation.** The full method outperforms the plain ReAct baseline by ~25 points on EgoSchema (66.98% vs. 42.02%) and ~16 points on Ego4D IoU=0.3 (19.51 vs. 3.71) (Table 4). Ablating the evaluator drops EgoSchema accuracy from 66.98 to 50.1 — the largest single-component drop — confirming that self-reflective feedback materially boosts reasoning quality.

- **Long-term memory provides consistent gains across benchmarks.** Removing memory reduces EgoSchema accuracy by ~12 points (66.98 → 55.1%) and Ego4D IoU=0.3 by more than half (19.51 → 9.09) (Table 4). This validates the design choice of storing and retrieving semantically similar past trajectories.

- **The method demonstrably adapts its sampling to textual cues in questions, providing direct evidence of query-awareness.** On NextQA, questions with temporal cues (e.g., "at the end") access on average 10.56 frames, while questions without cues access 12.26 frames (Section 5.2). Figure 2 shows higher frame-access ratios at temporal locations indicated by the cue — concrete behavioral evidence of adaptivity.

## Weaknesses

### Fatal

None.

### Major

- **The MovieChat result (84.8% vs. 62.3%) is difficult to interpret due to inconsistent evaluation protocols and potential judge bias.** The paper uses Claude-3.5-sonnet as an automatic judge for its own open-ended outputs, while baseline numbers (VideoChat, VideoLlaMA, VideoChatGPT, MovieChat) are likely drawn from papers using different evaluation protocols. The 22-point improvement — far larger than gains on any other benchmark — cannot be taken at face value without (a) ensuring consistent evaluation across all methods, (b) verifying with a blinded human evaluation or a second independent judge (e.g., GPT-4), and (c) clarifying whether the baseline numbers were re-evaluated under the same protocol. This undermines what would otherwise be the paper's most striking result.

- **The ablation baseline (ReAct) is weak, making the relative gains appear larger than they might be against a stronger controller.** On EgoSchema, plain ReAct achieves only 42.02% — far below even simple non-agent methods like LongViViT (56.8%) and LLoVi (57.6%). The paper frames this as evidence that "Agents Without Guidance are Suboptimal Reasoners," which is supported, but the gap between the full method and a minimally-prompted baseline overstates the practical improvement. A stronger ReAct variant (e.g., with chain-of-thought prompting or a simple frame-selection heuristic) would provide a more meaningful comparison.

### Minor

- **Efficiency is reported only as frames accessed, which is necessary but not sufficient.** The method makes multiple LLM calls per video (policy generation, planner loops, sampler invocations, evaluator, refiner). Each call adds latency, token cost, and monetary expense that could exceed the cost of processing all frames with a simpler baseline. Without reporting total LLM calls, wall-clock time, or API cost, the claim that the method "enhances efficiency" is incomplete. The Limitations section acknowledges API latency but does not quantify the trade-off.

- **No comparison against alternative query-adaptive frame selection methods.** The paper's novelty rests on query-adaptive sampling, yet no baseline uses a similar principle (e.g., CLIP-based retrieval of relevant frames \cite{romero2024question}, or other adaptive samplers cited in the related work). Such a comparison is needed to isolate whether gains come from the adaptive selection itself or from the agentic reasoning loop (evaluator + refiner + memory).

- **No statistical reliability is reported for any result.** Given LLM stochasticity, the improvements on NextQA (+1.4%) and Ego4D IoU=0.3 (+2.1%) could fall within noise. Single-run results are common in this area, but the lack of multiple runs or confidence intervals weakens confidence in the precision of reported gains — especially for the smaller-margin improvements.

### Trivial

- **Several implementation details are underspecified.** The long-term memory retrieval mechanism says it uses "semantic similarity of question type" (line 88) but does not specify the embedding model or retrieval top-k. The description of the Sampler as "another instantiated LLM" (line 82) does not clarify whether it is the same model with a different prompt. The mapping of which tools are used for which benchmark is not provided.
- **The frame percentage notations are inconsistent across tables.** Table 4 reports Ego4D frame percentage as 0.002% while Table 5 reports NextQA as 1.1% — these use different denominators (total video frames), which is fine but should be explicitly normalized or explained to avoid confusion.

## Nice-to-Haves

- An efficiency frontier plot (accuracy vs. frame count) with the proposed method and baselines, including total LLM call cost as a secondary axis.
- A human evaluation or second-model verification for the MovieChat open-ended results.
- A comparison against a simplified variant that processes the same number of frames (~14) through a single strong multimodal LLM (e.g., GPT-4V) without the agent loop, to disentangle the contribution of the base model from the agent architecture.

## Removed Points

**These points are flagged to be removed; treat them with caution:**

- *Criticism about Introduction/Fig 1 being "overstated" about VideoAgent* — The paper correctly distinguishes between query-adaptive *sampling* (what VideoAgent does not do: it samples uniformly at 1fps) and query-adaptive *retrieval* (what VideoAgent does: retrieve from pre-built memory). This is an accurate characterization, not an overstatement.
- *Criticism about the ReAct baseline being "extremely poor"* — The paper deliberately uses a minimally-prompted ReAct as a lower bound to show that "Agents Without Guidance are Suboptimal Reasoners" (Section 5.2). This is intentional exposition, not a flaw. The critic's suggestion of a stronger ReAct baseline is valid but framed as a negative when the paper correctly treats it as a baseline to improve upon.
- *Suggestion to add a column to Table 1* — This is a formatting suggestion, not a weakness.
- *Frames percentage inconsistency* — Different benchmarks have different total frame counts (Ego4D: ~15,660 frames at 30fps; NextQA: ~1,320 frames). The percentage notations are consistent within each table and the difference is a trivial labeling choice.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a novel observation that the paper itself does not already articulate.

## Suggestions

1. **Fix the MovieChat evaluation.** Either re-evaluate all baselines under the same protocol (using Claude-3.5-sonnet as judge with the same confidence threshold) or provide human evaluation on a subset. Report agreement statistics between the LLM judge and human annotators.
2. **Add total computation cost.** Report average LLM calls per video, total tokens consumed, and approximate wall-clock time or API cost alongside frames accessed. This gives a complete efficiency picture.
3. **Add a query-adaptive baseline.** Compare against CLIP-based frame retrieval (e.g., \cite{romero2024question}) or another method that selects frames based on the query without the full agent loop.
4. **Report confidence intervals.** Run each experiment at least 3 times and report mean ± std, especially for the smaller-margin improvements on NextQA and Ego4D.
5. **Strengthen the ReAct baseline.** Add a version with chain-of-thought prompting or a simple frame-selection heuristic to provide a more competitive lower bound.
6. **Specify implementation details.** Clarify the embedding model for memory retrieval, whether the Sampler uses the same LLM with a different prompt, and the tool-benchmark mapping.

## Score and Decision

**Originality:** 7/10 — The combination of query-adaptive sampling with evaluator/refiner feedback and long-term memory is novel, though individual components build on existing ideas (ReAct, Reflexion, memory retrieval).

**Importance of research question:** 8/10 — Efficient long-form video understanding is an important and timely problem.

**Claims support:** 5/10 — The frame-efficiency claim is well-supported; the MovieChat claim is not reliably supported; the overall accuracy gains are modest on most benchmarks.

**Soundness of experiments:** 6/10 — Ablation studies are thorough and well-designed. But the MovieChat evaluation protocol is questionable, no adaptive baselines are compared, and the ReAct baseline is too weak to serve as a meaningful anchor.

**Clarity of writing:** 7/10 — The method is clearly described and Figure 1 provides a helpful overview. Some implementation details are missing.

**Value to the research community:** 7/10 — The framework design and ablation results are useful; the code and methodology could serve as a foundation for future work on adaptive video agents.

**Overall:** This paper presents a well-motivated framework with strong ablations and clear evidence that query-adaptive sampling can reduce frame usage substantially. The main concerns are the unreliable MovieChat evaluation, incomplete efficiency accounting, and missing adaptive baselines. These are addressable in revision.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>