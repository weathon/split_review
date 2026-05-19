- Decision: Reject
- Avg Score: 5.33
- Scores: 6, 5, 5
Now I have all the information I need. Let me write the consolidated review.

## Summary

This paper proposes an agentic framework (Advisor, Grounding, Monitor, Robotic agents) that uses VLM-powered agents to generate Python-based guidance functions at test time. These guidance functions modify a base policy's action distribution to improve task success. The method is evaluated on RLBench tasks with Act3D and 3D Diffuser Actor base policies, and on two real-world tasks (multi-button pressing, chess piece reaching).

## Strengths

1. **Novel integration of multi-agent VLM framework with existing policy action distributions.** Rather than treating VLMs as planners that replace the policy, the framework generates lightweight guidance functions that compose with any base policy's action distribution via a weighted combination (Eq. 4, §3.4). This design preserves the base policy's low-level control while injecting high-level task awareness at test time.

2. **Multi-granular object search is a concrete improvement over existing perception pipelines.** Section 3.2 describes a grounding agent that, when an object is not found, searches for semantically similar objects or higher-level containers (e.g., cup→mug→shelf), then crops and re-searches. The chessboard example (Figure 7) qualitatively demonstrates this working end-to-end, which is a genuine enhancement over Segment and Track Anything's single-pass detection.

3. **Demonstration across multiple policy classes, training regimes, and real-world settings.** The framework is tested with Act3D (trained on 5/10/25 demos), 3D Diffuser Actor (5 demos), and a RandomPolicy, on 10 simulated tasks and 2 real-world tasks (§4.1–4.2). This breadth supports the claim of policy-agnostic applicability.

4. **Open-source release** of code, models, and system prompts (stated in §5 and Reproducibility Statement), which supports reproducibility and further research.

## Weaknesses

### Major

1. **Unequal evaluation protocol between guided and baseline policies.** The paper states: "Guidance is iteratively generated for the failure cases. For the failed rollouts, our policy improvement framework ran for 5 iterations" (§4.2, line 213), and Table 1 is captioned "by applying 5 iterations of guidance improvement over unsuccessful rollouts" (line 222). This means the guided policy receives up to 5 rollout attempts per task variation (each with a refined guidance function), while the baseline policies (Act3D, 3D Diffuser Actor) are evaluated with a single attempt. The reported improvements in Table 1 therefore conflate the benefit of the VLM-generated guidance with the benefit of multiple attempts. A baseline that simply retried with randomized action noise or a simple recovery heuristic might achieve similar gains — the paper does not control for this. **Why this is major:** it directly affects the primary quantitative evidence in Table 1, which is the main support for the paper's core claim. The issue is fixable (report first-iteration performance; give baselines comparable retry opportunities), but as presented the numbers do not isolate the contribution of the guidance mechanism.

2. **The specific VLM used is never disclosed.** The paper refers only to "Vision Language Model" and "Language Model" throughout (e.g., §3.2). Without knowing which VLM was used (GPT-4V? LLaVA? Gemini?), the experiments are not reproducible and it is impossible to assess how much of the reported performance depends on the specific model's capability. The appendix is said to contain prompts but not the model identity.

### Minor

3. **No variance or statistical significance reporting.** All results in Table 1 are single numbers; the paper mentions "fixed seeds" and "temperature was set as zero" (§5), suggesting a single deterministic run. Given stochasticity in action sampling, perception, and VLM tool-call outputs, multiple independent runs with error bars are needed to assess whether improvements are reliable. (This is a standard expectation for empirical robotics papers; the absence weakens but does not invalidate the results.)

4. **Framing of "learning new skills from scratch" is overstated.** In the learning-from-scratch experiments (§4.4), the Act3D policy uses random weights and 100% guidance is applied. The policy weights are never updated; the "learning" consists entirely of iterative refinement of the VLM-generated guidance code. The paper itself notes "the product of the iterative learning from scratch is the generated guidance script" (line 313). The abstract and introduction describe this as "learning to perform certain tasks from scratch without any demonstrations" (line 32), which conflates trial-and-error code refinement with policy learning. This is a significant contribution — zero-shot task execution with failure-driven code refinement — but should be framed accurately.

5. **Missing baseline comparisons against existing VLM-based planning methods.** Related work (§2) discusses Code as Policies, ProgPrompt, Visual Programming, and Eureka, but no quantitative comparison is provided against these approaches on the same benchmarks. While the paper's method differs architecturally, a comparison would contextualize the claimed benefits. This is a gap rather than a flaw, as the paper focuses on policy-guidance rather than plan generation.

### Trivial

6. **The guidance factor α is only tested at 1% and 10% for the main experiments** (Table 1) and at 100% for learning-from-scratch. A wider sweep would better characterize the trade-off.

7. **The dynamics model used in real-world experiments is not explicitly specified.** Section 3.4 mentions forward kinematics as one possibility, but it is unclear whether the real-world setup uses forward kinematics, a learned model, or the simulator.

## Nice-to-Haves

- Ablation study comparing the multi-agent architecture vs. a single VLM agent generating guidance directly, to justify the four-agent design.
- Ablation of the multi-granular search component with quantitative success rates (with/without hierarchical search).
- Reporting success rates with multiple random seeds (3–5) and error bars.
- A baseline that allows the original policy to retry with random noise or a simple recovery heuristic, to isolate the value of VLM-generated guidance.

## Removed Points

- **Harsh critic's claim that the evaluation issue is "not fixable by adding ablation experiments" (§Critical Issues, #1):** This is incorrect — the issue can be fixed by reporting first-iteration guided results or providing baselines with multiple attempts. The problem is significant but fixable.
- **Harsh critic's statement that "the reported improvements are uninterpretable":** Overstated. The improvements are real but conflated with the multi-attempt structure; they are interpretable as "guidance + iterative refinement helps" but not as "guidance alone helps."
- **Criticism that learning-from-scratch results show guidance only controls Cartesian position:** The paper explicitly states this limitation (line 284), so it is already acknowledged.
- **Request for quantitative real-world success rates:** While valuable, real-world results are presented as qualitative demonstrations (a common practice in robotics papers when focus is on the simulation benchmark).

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Fix the evaluation protocol.** Report the guided policy's success rate on the *first iteration only* (before any failure-driven refinement) alongside the final iteration results. Also, give baselines the same number of attempts with a simple recovery heuristic (e.g., re-sample from the base policy's distribution). This cleanly separates the value of the VLM guidance from the value of multiple attempts.
2. **Disclose the specific VLM used.** This is critical for reproducibility and for readers to assess the method's dependency on model capability.
3. **Reframe the "learning from scratch" claims** as "zero-shot task execution with iterative VLM-guided code refinement" to match what is actually demonstrated.
4. **Add error bars or confidence intervals** from multiple runs (3–5 seeds) to the main results in Table 1.
