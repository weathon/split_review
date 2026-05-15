Now I have all the evidence I need to verify each claim against the paper. Let me construct the final review.

---

## Summary

MobileAgentBench proposes a benchmark for mobile LLM agents that uses Android Accessibility Service events combined with final UI state checking to determine task completion, avoiding the false-positive problems of prior action-sequence-matching approaches (e.g., AndroidArena). The benchmark offers 100 tasks over 10 open-source apps, supports fully autonomous execution on real devices, and requires "fewer than ten lines of additional code" for agent integration. Five agents are evaluated across six metrics to provide baseline results.

## Strengths

- **Low-code integration, well-demonstrated.** The paper provides pseudocode (Listing 1) showing that integrating the benchmark requires only `orchestrator.before_one_action()` / `orchestrator.after_one_action()` calls around the agent's action loop. This directly supports the "minimally invasive" claim and lowers the adoption barrier for non-Android developers.

- **Principled success-condition design that avoids a known failure mode.** The paper identifies a concrete false-positive case in AndroidArena (subsequence matching: next→previous→next still matches GT but fails the task) and proposes final-UI-state checking augmented with Accessibility Event signals for tasks without direct UI reflection (e.g., saving a note). This is a genuine improvement over action-sequence-based approaches.

- **Fully autonomous, real-device evaluation pipeline.** The benchmark runs without human supervision (Section 3.1), switches tasks automatically, and supports both physical devices and emulators, which is a clear advantage over AppAgent's manual-verification approach and AITW's static-screenshot setup.

- **Systematic multi-agent evaluation with diverse metrics.** Five agents (AndroidArena, AutoDroid, AppAgent, CogAgent, MobileAgent) are evaluated on six metrics (SR, SE, latency, tokens, FN rate, FP rate), providing the community with concrete baselines and revealing interesting failure patterns (e.g., CogAgent's high FN rate due to naive implementation, AppAgent's high FP rate from poor graceful stopping).

## Weaknesses

### Fatal

None. While the paper has significant gaps, none entirely invalidate the core contribution of the benchmark framework design.

### Major

- **The benchmark's own success-judgment accuracy is never validated against human ground truth.**  
  The paper proposes a detection mechanism combining UI state matching and Accessibility Event listening, but never verifies whether this mechanism *correctly* identifies task completion. Without comparing the benchmark's judgments to human-labeled ground truth (e.g., on a held-out subset), every agent success rate reported in Table 1 rests on an unverified oracle. The paper reports agent FN/FP rates (early/late stopping), but these tell us nothing about errors made by the *benchmark itself*. If the benchmark declares success when a task is actually incomplete (or vice versa), every derived metric is unreliable. This is the most significant gap for a benchmark paper, which by its nature asks the community to trust its evaluations.

- **Uncontrolled confounds undermine head-to-head agent comparisons.**  
  AutoDroid runs on Android 9 while all other agents run on Android 14 (line 169), a difference the paper acknowledges but does not control. CogAgent is evaluated with 4-bit quantization and a "vanilla" no-history implementation (line 173), which the paper notes as a likely cause of its low success rate but presents in the main comparison table regardless. The comparison between AppAgent and other agents attributes its higher SR to "self-exploration," but no ablation turns this feature off to substantiate the claim (line 194). These uncontrolled variables prevent reliable conclusions about relative agent performance.

### Minor

- **No mention of evaluation runs or variance.**  
  All agent results in Table 1 are presented as point estimates with no indication of whether they come from a single run or multiple runs, and no standard deviations or confidence intervals are reported. Given the stochasticity of LLM outputs and the 100-task set, single-run results have unknown reliability. While the 100-task size provides some robustness, the omission should be noted and ideally addressed.

- **Difficulty metric based solely on minimum human steps is not validated against actual agent difficulty.**  
  Task difficulty is defined by minimum human steps (line 123), but this does not capture factors that make tasks hard for agents (e.g., precise icon localization, multi-branch navigation). No inter-annotator agreement is reported for the three human experts who verified the step counts. The surprising result that AppAgent performs better on medium than easy tasks is attributed to the step-limit artifact (2× minimum steps), which suggests the difficulty categorization may be conflated with the evaluation protocol rather than reflecting intrinsic task difficulty.

- **The evaluation omits agents discussed in the paper's own related work.**  
  Octopus v2 is cited (line 71) as a relevant mobile agent but is not included in the evaluation. While no evaluation can cover every agent, the paper would benefit from either including more agents or justifying the selection more explicitly.

### Trivial

- The paper states that CogAgent's high FN rate (1.0) means it "always stop[s] early when the task is not finished yet" (line 194), but an FN rate of 1.0 also means the agent *never* produces false positives, which is a notable property that goes unremarked.

## Nice-to-Haves

- An ablation disabling Accessibility Event listening and using only UI state checking would quantify the added value of event signals over pure state-based judgment.
- A per-task confusion matrix showing which tasks each agent succeeds/fails on would reveal systematic failure categories (e.g., tasks requiring text input, icon recognition, multi-step navigation).
- A step-limit sensitivity analysis with different multipliers (e.g., 1.5×, 3×) would show whether the difficulty-level results are robust or an artifact of the 2× choice.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Table 1 inconsistency: AppAgent marked ✗ for fully autonomous but evaluated autonomously."** — Removed because Table 1 compares *benchmarks*, not agents. The ✗ means AppAgent's *original evaluation methodology* (their paper) requires human supervision. There is no inconsistency when AppAgent the agent is evaluated by MobileAgentBench's autonomous pipeline. This is a reviewer misunderstanding.

- **"Does not discuss whether Accessibility Service can detect clicks on modified touchable areas."** — The paper already discusses extended touchable areas (Fig. 1, lines 87–94). The Accessibility Service captures Android system events, which fire for any handled touch regardless of visible bounds. The paper adequately addresses this technical concern.

- **"Lacks formal specification of success judgment logic."** — The paper describes the mechanism at a level appropriate for a systems/benchmark paper (UI state + event signals). A formal state-transition model would be a nice addition but is not a required standard for this type of contribution.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface an insight about the paper that the paper itself does not already articulate.

## Suggestions

1. **Validate the benchmark's own judgment.** Manually label task success on a sample of agent runs (e.g., 30–50 per agent) and report precision/recall of the benchmark's automated judgments against human labels. This is the single most important addition for establishing trust in the benchmark.

2. **Control or acknowledge confounds in agent comparison.** Either re-run AutoDroid on Android 14 (if practical) or present it as a separate setting rather than in the main comparison table. Add an ablation of AppAgent's self-exploration feature to substantiate the claim that it benefits SR.

3. **Report variance estimates.** Specify the number of runs and report means with standard deviations or confidence intervals, even if only over 2–3 runs.

4. **Report inter-annotator agreement** for the three human experts who verified task difficulty levels (e.g., Fleiss' κ) to support the difficulty categorization.

---

## Score and Decision

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>