Now I have verified the paper claims against the reviewer's criticisms. Let me produce the final consolidated review.

---

## Summary

This paper introduces MobileAgentBench, a benchmark for evaluating LLM-based mobile agents on real Android devices. It defines 100 tasks across 10 open-source apps at three difficulty levels, judges task success via final UI state (view hierarchy) plus accessibility-event signals (rather than action-sequence matching), and requires fewer than 10 lines of integration code per agent. The authors evaluate five existing agents (AppAgent, AndroidArena, AutoDroid, CogAgent, MobileAgent) across six metrics. The core contribution is a benchmark that is fully autonomous, runs on real devices, supports multiple completion paths, and is easy to integrate.

## Strengths

1. **Fully autonomous evaluation on real devices.** The benchmark runs 100 tasks across 5 agents without any human intervention during execution (Section 3.1: "The whole process is fully automated and requires no human supervision"). This is demonstrated in practice by the results in Table 2, all obtained without manual oversight. Table 1 shows MobileAgentBench is the only benchmark satisfying all four criteria (fully autonomous, realistic environment, flexible success conditions, low code invasiveness).

2. **Flexible success condition that handles multiple completion paths.** By checking the *final UI state* rather than matching a fixed action sequence, the benchmark avoids false positives from redundant or reordered actions (Section 2.2 explicitly contrasts this with AndroidArena's subsequence-matching weakness). The paper correctly identifies that "there might be multiple paths towards task completion, but the final success state converges to one" (Section 3.1) — a well-motivated design choice.

3. **Low code invasiveness for integration.** A standard agent requires only a few method calls: import, initialization, orchestrator calls before/after each action, and `orchestrator.run`. The pseudocode in Listing 1 and the explicit claim of "fewer than ten lines of additional code" (Section 3.3) provide a concrete, verifiable usability advantage over existing benchmarks.

4. **Comprehensive multi-metric evaluation.** Six metrics (SR, SE, latency, tokens, FN rate, FP rate) are defined and reported for five agents in Table 2, enabling richer comparison than success-rate alone. The FN/FP rates, in particular, capture a practically relevant dimension — whether agents know when to stop.

5. **Difficulty categories validated by human experts.** Tasks are classified by minimum steps into easy/medium/hard, cross-verified by three human experts independently (Section 3.2), lending credibility to the difficulty-level analysis.

6. **Direct comparison with existing benchmarks.** Table 1 provides a clear, four-criterion comparison of MobileAgentBench against AITW, AndroidArena, and AppAgent, grounding the contribution in concrete deficiencies of prior work.

## Weaknesses

### Fatal
None.

### Major
1. **The benchmark's success-judgment accuracy is not validated.** The paper claims that tasks are judged by checking the final UI state (view hierarchy) plus app-event signals (e.g., save-button clicks). However, *no evidence is provided that this automated judgment is correct*: there is no human-verification experiment, no analysis of false positives or false negatives arising from the benchmark's own logic, and no discussion of edge cases (beyond the noted UIAutomator animation issue) where the checker might fail. For a benchmark paper whose reported baseline numbers rest entirely on this judgment, the absence of validation is a significant evidential gap. All reported success rates are on uncertain footing until this is addressed. A small human-agreement study (e.g., Cohen's κ on 50–100 sampled agent runs) would dramatically increase confidence.

2. **CogAgent is evaluated in a degraded configuration.** CogAgent is run with "no history information" and 4-bit quantization (Section 4.2). The model is explicitly designed to leverage multi-turn context; stripping history and quantizing to 4 bits measures a substantially weakened version. The paper acknowledges this ("naive agent implementation... limits the usage of history information" in Section 4.3), but presenting these results as a baseline alongside other agents — without prominently caveating them as a lower-bound estimate — is misleading. The CogAgent score of 8% SR is not representative of what the model can achieve in its intended use.

### Minor
1. **No multiple trials or confidence intervals for stochastic agents.** All LLM-based agents involve sampling (temperature > 0), yet each agent is evaluated only once (Section 4.2–4.3). No confidence intervals, standard deviations, or repeated-run statistics are reported. This makes it impossible to assess the reliability of the reported differences between agents.

2. **AutoDroid runs on a different Android version without analysis.** AutoDroid is executed on Android 9 while all other agents use Android 14 (Section 4.2). The paper notes this was necessary because "some of the dependency libraries do not support the newer Android systems," but does not discuss whether differences in OS version, window manager behavior, or UIAutomator output could confound the comparison. No control experiment (e.g., running a simple agent on both versions) isolates the OS effect.

3. **Step-limit design choice distorts difficulty-level comparisons.** The paper sets maximum execution steps to twice the minimum steps per task. The authors themselves observe that AppAgent has a *higher* success rate on medium tasks than on easy tasks because "easy tasks have very limited steps to correct" (Section 4.3). This means the "easy" category may penalize agents more for small early mistakes than "hard" tasks do, undermining the interpretability of difficulty-level comparisons. The issue is transparently acknowledged, but no sensitivity analysis (e.g., with a larger multiplier) is provided to show results are robust to this choice.

4. **Speculative interpretation of confounded comparison.** The paper notes that AutoDroid (text-only GPT-3.5) outperforms some GPT-4V agents and concludes that "the textual view hierarchy contains the most important information for GUI navigation tasks" (Section 4.3). This interpretation is confounded by agent architecture differences (not just backbone model) — no ablation within the same agent is performed to isolate the effect of visual vs. textual input. The claim is presented as an inference from a between-agent comparison, which is speculative.

5. **Method description lacks some implementation detail for reproducibility.** Section 3.1 describes using the Android Accessibility Service to capture click events, but the details of how an accessibility event is matched to a specific UI element (e.g., "the save button") are sparse. The paper says "we can use the view hierarchy to check if the note is edited correctly, and then mark the task as a success if the save button clicking signal is received afterwards," but implementors would benefit from a concrete example of a task definition Python snippet with its corresponding success-checking code.

### Trivial
- The FN/FP rate metrics (Section 4.1) depend on the benchmark's own task-completion judgment as ground truth; any errors in the benchmark's judgment propagate into these metrics. This is an inherent property of such metrics, not a flaw unique to this paper, but it reinforces the need for the validation study mentioned above.

## Nice-to-Haves
- **Per-app breakdown of success rates.** The paper shows difficulty-level breakdowns but not which apps are harder overall. This would help benchmark users understand which task domains drive agent failures.
- **Concrete example of a task definition.** Providing one full task-configuration Python snippet (e.g., "create a note") with its success-checking code would improve reproducibility.
- **Quantitative comparison with LlamaTouch's hit-test approach.** The paper argues that its accessibility-event approach is more accurate than LlamaTouch's coordinate-to-viewbox matching (Section 2.2), but does not quantify the improvement. A targeted experiment (e.g., measuring how often each method disagrees with ground truth on a sample of clicks) would sharpen the contribution.

## Removed Points
*These points were flagged to be removed from consideration; treat them with caution.*

- **Criticism that AITW should not be marked "Fully Autonomous" in Table 1.** The paper defines "fully autonomous" as "if the benchmark does not need human supervision or judgment" (line 51). Under this definition, AITW's static-dataset evaluation — where a script can autonomously compare agent actions to ground-truth sequences — qualifies. The reviewer's objection stems from a different interpretation of "autonomous" (the agent's ability to recover from off-path actions), not from an error in the paper.
- **Criticism that the paper does not compare with LlamaTouch.** The paper *does* compare methodologically (Section 2.2, lines 87–94), explaining the hit-test limitation of LlamaTouch and the proposed accessibility-service alternative. The criticism about missing quantitative comparison is valid and moved to Nice-to-Haves; the claim that no comparison exists at all is factually incorrect.
- **Criticism about Table 1 conflating "fully autonomous" with "realistic environment."** The table has separate columns for each criterion, and each is defined in the text (line 51). There is no conflation.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. **Run a human-validation study.** Sample 50–100 agent-task executions across agents, have human annotators independently judge success/failure, and report agreement (e.g., Cohen's κ) with the automated check. Characterize and fix any failure modes. This is the single highest-leverage improvement for establishing the benchmark's trustworthiness.
2. **Run each agent 3–5 times** with different random seeds (or LLM sampling settings) and report means and standard deviations for all metrics.
3. **Either fix the CogAgent configuration** (enable multi-turn history, use full precision or report both settings) **or prominently label it** as a degraded lower-bound baseline, noting that the results are not representative of CogAgent's intended capability.
4. **Perform a sensitivity analysis on the step-limit multiplier** (e.g., 3× or 4×) to check whether the anomalous "easy < medium" pattern persists. This would either validate the current design or reveal a needed adjustment.
5. **Provide at least one concrete task-definition Python snippet** in the paper or appendix to improve reproducibility.

## Score and Decision

The paper proposes a benchmark that addresses genuine limitations in mobile agent evaluation — real-device execution, flexible success conditions, and low integration overhead — and the design is well-motivated. The core contribution is real and fills a gap in the community. However, the absence of validation for the benchmark's own success judgments, combined with the CogAgent evaluation in a degraded configuration and the lack of multiple trials, means the reported baseline numbers are not yet as trustworthy as they should be for a benchmark paper. These issues are fixable with reasonably targeted additional work.

**Score:** 6.0  
**Decision:** Accept

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>