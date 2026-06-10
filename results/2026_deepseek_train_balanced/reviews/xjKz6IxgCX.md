## Summary

This paper introduces SafeWatch, an MLLM-based video guardrail model with two architectural innovations: Parallel Equivalent Policy Encoding (PEPE) to eliminate positional bias from policy order, and Policy-Aware Adaptive Pruning (PAP) to selectively prune video tokens based on per-policy relevance. The authors also introduce SafeGuard, a 2M-video benchmark dataset spanning six safety categories annotated via a multi-agent consensus pipeline. Experiments report substantial gains over baselines on SafeGuard (28–29%), existing benchmarks (13.6%), and zero-shot generalization to new policies and tasks.

## Strengths

- **PEPE is a principled architectural solution to a real problem.** The paper identifies that autoregressive MLLMs exhibit positional bias when policies are concatenated sequentially (lines 130–132), and PEPE addresses this by encoding each policy chunk independently with equivalent RoPE embeddings, masking cross-policy attention, and decomposing large QK matrices into parallel blocks (Eq. 3, lines 135–142). This is clearly differentiated from prior prompting-based approaches.

- **PAP achieves 90% visual token pruning with <1% accuracy loss.** The paper demonstrates that pruning up to 90% of video tokens based on policy-specific cross-attention relevance scores yields negligible degradation (line 285), while random pruning at the same rate degrades the SFT baseline significantly. This is a concrete, measured efficiency gain.

- **Consistent improvements across multiple evaluation settings.** SafeWatch shows strong results on in-distribution evaluation (SafeGuard-Real: +29.2%, SafeGuard-GenAI: +27.2%), on five existing benchmarks (+13.6% average), on three unseen policy categories (+5.6%), and on new prompting tasks (+15.6%). The generalization results provide the most robust evidence of the method's value.

- **Multi-agent consensus annotation pipeline for dataset construction.** The annotation pipeline (Section 4.2, lines 212–217) uses multiple MLLM agents to propose, discuss, and reach consensus with a GPT-4o judge, plus sampled human verification. This is a scalable approach to producing multi-label annotations with explanations at the 2M-video scale.

- **Safety-aware event sampling is well-motivated.** Rather than uniform or dense frame sampling, the paper uses lightweight TransNetV2 segmentation to identify safety-relevant events and samples one frame per event (lines 115–116). This is a task-specific adaptation grounded in the observation that unsafe behaviors are consistent within events.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **The headline in-distribution results conflate architectural merit with training data advantage.** The abstract and introduction lead with the claim that SafeWatch "outperforms all SOTA video guardrails on SafeGuard by 28.2%" and "by 29.2%/27.2%" on the two subsets. SafeWatch was trained on SafeGuard's training split; every baseline (GPT-4o, Gemini-1.5 Pro, LlavaGuard-34B, etc.) was evaluated zero-shot. The reported margins therefore reflect both the method's quality and the expected benefit of having been trained on the evaluation distribution. This is standard practice (train/test split within a single dataset) and not a methodological error, but the framing implies a general superiority that the evidence does not fully support. The generalization experiments to existing benchmarks, new policies, and new tasks (which *do* test transfer) are the more informative comparisons and deserve the prominence currently given to the in-distribution results.

2. **PAP's cross-policy token selection merging is underspecified.** Algorithm 1 selects top-*K* visual tokens per policy (line 162) and then "Update[s] KV cache and discard[s] pruned features" before decoding a single output (guardrail flags for all policies + one explanation). When different policies select *different* subsets of visual tokens, how are these subsets reconciled into a single KV cache? The paper does not specify whether the selected sets are unioned, intersected, weighted, or handled by some other mechanism. This matters because the union of per-policy top-*K* selections could approach the full token set in the worst case (if different policies attend to different tokens), undermining the claimed efficiency.

3. **Apparent inconsistency between 90% token pruning and 10% latency reduction.** The paper states that PAP reduces inference overhead by "10% on average" compared to InternVL2-8B (line 50), and separately that "SafeWatch maintains a performance drop of less than 1% even when pruning up to 90% of video tokens" (line 285). A 90% reduction in video tokens should yield a proportionally larger speedup unless video token processing is not the bottleneck — yet the paper states that "inference costs are also dominated by the number of video tokens" (line 146). This tension needs explanation (e.g., if autoregressive response decoding dominates runtime, or if PAP's own computation offsets the savings). The 0.4-second absolute reduction reported (line 254) partially addresses this but does not resolve the relative inconsistency.

4. **Frame-by-frame evaluation of image-based guardrail baselines may disadvantage them.** Open-source guardrail models (LlavaGuard-34B, Holmes-VAD, LLamaGuard3V-11B) "do not natively support video input" and are evaluated by feeding them individual frames and union-aggregating outputs (line 236). This is a reasonable approximation but introduces unknown degradation relative to a native video pipeline. The large performance gap against these baselines may partly reflect this mismatch, and the paper provides no analysis of whether the frame-by-frame union operation is a fair way to extend them to video.

5. **The aggregate relevance score r_i (Eq. 9) is computed but plays no role in the algorithm.** Equation 9 averages per-token relevance scores r_i^j to produce a scalar r_i per policy, and the paper claims this "indicates that the video is more likely to violate the corresponding policy" (line 181). However, the actual token selection (Eq. 10, line 162) uses the per-token scores r_i^j, not the aggregate r_i, and the downstream pipeline does not reference r_i. This claim is both unsubstantiated and unused.

### Trivial

- The paper claims SafeWatch is "the first MLLM-based video guardrail model designed to follow a comprehensive collection of safety policies" (line 40), yet cites Holmes-VAD as a baseline designed for guardrail tasks. The claim should be qualified (e.g., "first with parallel policy encoding and adaptive pruning").
- The connection to sparse autoencoders (line 133) as an inspiration for PEPE is a non sequitur — SAEs decompose representations into interpretable directions, while PEPE decomposes input text into parallel chunks. The reference does not support the design.
- The statement that "a higher relevance score r_i essentially indicates that the video is more likely to violate the corresponding policy" (line 181) is asserted without evidence.

## Nice-to-Haves

- Report inter-annotator agreement (between MLLM agents, or between MLLM and human) on the SafeGuard test set to quantify annotation quality and address concerns about circular evaluation.
- Include an error analysis (false positive / false negative breakdown by category) to help practitioners understand failure modes.
- Report training cost (GPU hours) since the three-stage pipeline on 2M videos is non-trivial.
- Discuss privacy/consent considerations for collecting user-produced videos from demographic groups (line 207).

## Removed Points

These points were flagged in the reviews but removed as inappropriate or unsupported under the filtering rules:
- **Criticism about open-source release timing/license** — The paper states the project is open-sourced (line 14). Per rules, questioning release status of cited tools is not permitted.
- **Criticism about missing appendix content** — The parser strips appendix sections from all papers; they exist in the original submission.
- **Criticism that no analysis of annotation agreement/failure modes qualifies as a core weakness** — These are useful additions but not required for the paper's core contribution; moved to Nice-to-Haves.
- **Several generic "area-of-concern" sweep criticisms from the Harsh Critic** that lacked concrete anchors in the paper text (e.g., general speculation about confounders without specific evidence).

## Novel Insights
None beyond the paper's own contributions.

## Suggestions

1. **Restructure the results hierarchy.** Move the generalization experiments (existing benchmarks, new policies, new prompting tasks) to primary position in the abstract and main text. Present the in-distribution SafeGuard results as a sanity check ("the model performs well on its training distribution") rather than as the primary evidence of superiority.
2. **Specify the cross-policy token merging mechanism in PAP.** Clarify how per-policy top-*K* selections are reconciled into a single KV cache — union, intersection, or some other rule. Add a worst-case analysis of pruning ratios under this mechanism.
3. **Provide a latency breakdown** showing where inference time is spent (video encoding, policy encoding under PEPE, cross-attention, response decoding) to resolve the apparent inconsistency between 90% token pruning and 10% overall latency reduction.
4. **Add controlled ablations in the main paper** (not just the appendix): PEPE vs. sequential policy encoding, PAP vs. random pruning at the same retention rate. The appendix references these; they should be front and center.
5. **Remove or substantiate the interpretive claim about r_i** (Eq. 9, line 181). Either provide evidence that the aggregate relevance score correlates with violation likelihood, or remove the claim.
6. **Qualify the "first" claim** on line 40 to avoid confusion with existing MLLM-based video guardrail models cited as baselines.

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>