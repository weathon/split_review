- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 3, 5, 6
I have now verified all key claims against the paper. Let me produce the consolidated review.

## Summary

This paper introduces MobileAgentBench, a benchmark for evaluating LLM-based mobile agents on Android. It provides 100 tasks across 10 open-source apps (SimpleMobileTools), with difficulty levels validated by three human experts. The key design innovation is a success-judgment mechanism that combines UI state checking (via UIAutomator) with Android Accessibility Service event monitoring, avoiding the false-positive pitfalls of action-sequence matching used by prior benchmarks. Integration requires fewer than 10 lines of Python code. The paper reports baseline evaluations of five existing agents (AndroidArena, AutoDroid, AppAgent, CogAgent, MobileAgent) across six metrics.

## Strengths

- **Table 1 uniquely positions MobileAgentBench as satisfying all four desired properties** (fully autonomous, realistic environment, success condition flexibility, low code invasiveness), whereas each prior benchmark (AppAgent, AITW, AndroidArena) misses at least two. This directly supports the paper's central claim about addressing limitations of existing benchmarks.

- **The Accessibility Service–based event monitoring solves a real, documented failure mode.** The paper illustrates (Fig. 1) how coordinate-based hit-testing (as used by LlamaTouch) fails when developers extend touchable areas beyond visible view borders. Using system-level accessibility events to detect clicks is technically sound and demonstrably more robust than bounding-box matching.

- **Integration requiring under 10 lines of code (Listing 1) is a concrete advantage.** The three-step pattern (import, orchestrate, call run) is clearly simpler than the "complicated data structures and tools" the paper attributes to LlamaTouch, lowering the barrier for adoption.

- **Task difficulty is defined by minimum steps cross-verified by three human experts independently** (Section 3.2). This provides an objective, reproducible basis for the easy/medium/hard classification used in Fig. 2, and is more rigorous than single-annotator or arbitrary thresholds.

- **Six-metric evaluation (SR, SE, latency, tokens, FN rate, FP rate) reveals agent behaviors not captured by success rate alone.** For example, AutoDroid's high FN rate (0.93) and AppAgent's high FP rate (0.40) offer actionable diagnostic insights beyond what prior benchmarks provide.

## Weaknesses

### Fatal

None.

### Major

1. **The benchmark's automated scoring mechanism is not validated against human judgment.** The paper claims MobileAgentBench provides "reliable and precise benchmarking outcomes" (abstract, line 49), but provides no evidence that its automated success/failure judgments agree with ground truth. For a benchmark paper, this is the central evidential gap: every reported baseline result (Table 2, Fig. 2) depends on this unvalidated mechanism. The paper validates task *difficulty* via three human experts (Section 3.2), but that is a separate matter. A validation study — e.g., having humans judge a held-out sample of task executions (stratified across agents and outcomes) and computing agreement (accuracy or Cohen's κ) with the benchmark's verdict — is needed to substantiate the reliability claim. Without it, the reader cannot distinguish genuine agent capabilities from artifacts of the detection logic.

2. **Agent baseline comparisons are framed more strongly than the evidence supports.** The contributions claim to "perform a solid and systematic comparison" of "state-of-the-art mobile LLM agents" (line 57), and Section 4 is titled "Experiments and Agent Evaluations." However, CogAgent is run with 4-bit quantization and *no history information* (Section 4.2, "vanilla flavor"), which is a significant handicap — its 8% success rate almost certainly underrepresents the agent's real capability. The paper is transparent about these configurations, but the framing conflates "demonstrating the benchmark on a convenience sample of agents" with "systematically evaluating state-of-the-art agents." The results are useful baselines for the benchmark, but the paper should not present them as definitive agent rankings or as evidence of a "solid and systematic comparison."

### Minor

3. **No confidence intervals or error bars on any metric.** With only 100 tasks, a reported success rate of 40% has a 95% confidence interval of roughly ±9.6%. Without statistical characterization, it is impossible to know whether the observed differences between agents (e.g., AutoDroid 0.27 vs. MobileAgent 0.26) are meaningful or noise. This is a standard expectation for benchmarks.

4. **The maximum-steps-as-2×-minimum-steps policy confounds task difficulty with the evaluation protocol.** The paper acknowledges (line 204) that this disadvantages easy tasks by giving agents very little room to correct mistakes (e.g., 1 extra step for a 1-step task). This means the reported success rates across difficulty levels are not directly comparable — the protocol itself makes easy tasks harder to "pass" in a sense. The paper should either switch to a fixed step limit or explicitly decompose this confound.

5. **FN and FP rate definitions are underspecified.** Section 4.1 defines FN Rate = N_early / M_failure and FP Rate = N_late / M_success, but does not explain how the benchmark operationally determines whether a failure was due to "early stopping" vs. other failure modes. Since the benchmark judges success independently, how is "early" distinguished from "the agent exhausted its steps"? This needs clarification.

6. **No ablation of the accessibility event listener.** The paper argues (Section 3.1) that UI-state-only checking is insufficient (e.g., the save-button-in-note-editing example) and adds the event listener to address this. However, no experiment measures how much the event listener improves detection accuracy. An ablation on a sample of edge-case tasks (comparing judgments with and without the event signal) would directly support the claimed benefit.

### Trivial

None.

## Nice-to-Haves

- An ablation study of the Accessibility Service event listener to quantify its contribution to detection accuracy.
- A discussion of the representativeness of the 10 SimpleMobileTools apps (all open-source, ad-free, simply structured) and how results might generalize to complex commercial apps.
- Reporting a random-agent baseline success rate to calibrate the reported SRs.

## Removed Points

These points were raised by reviewers but removed after verification against the paper:

- **"Timing issue: what if the event listener receives the click before UI state fully updates?"** — Purely speculative; no evidence this causes false outcomes. Not a concrete weakness.
- **"AndroidArena's low code invasiveness checkmark seems inconsistent since the paper later uses AndroidArena as an agent"** — The critic confuses AndroidArena-as-benchmark (Table 1) with AndroidArena's agent code used as an evaluation subject. These are distinct; the Table 1 comparison is about benchmark frameworks, not agent implementations.
- **"Missing reproducibility details (prompt templates, version numbers)"** — Standard implementation details a benchmark paper would include in supplementary materials; the paper references a project webpage. The PDF parser strips these sections.
- **"Should include a do-nothing/random agent baseline"** — A reasonable suggestion but not a standard requirement for benchmark publications, and not a weakness of the paper as submitted.
- **"The paper should discuss that SimpleMobileTools apps are simple"** — The paper explicitly states this: "These apps have simple and straightforward user interfaces" (line 121). The paper acknowledges this framing positively, and the limitation is implicitly scoped.

## Novel Insights

None beyond the paper's own contributions. Both the harsh critic and strength finder largely converge on the paper's stated claims; there is no unexpected synthesis that reveals a pattern not already visible in the paper.

## Suggestions

1. **Conduct a human-validation study of the scoring mechanism.** Have human judges evaluate a stratified sample of ~50–80 task executions (across agents and outcomes), compute agreement (accuracy + Cohen's κ) with the automated verdict. This single addition would most directly support the paper's reliability claim.
2. **Reframe the baseline agent results as "illustrative baselines for the benchmark" rather than "systematic comparison of SOTA agents."** Adjust the language in the contributions and Section 4 to avoid overclaim.
3. **Add confidence intervals (e.g., via Wilson score interval) to all reported success rates and efficiency metrics.** This is a straightforward addition that would significantly improve interpretability.
4. **Either justify the 2× minimum-step policy with a fixed alternative or add an ablation comparing both policies** to disentangle task difficulty from protocol constraints.
5. **Clarify how "early stopped" vs. "late stopped" are operationally determined** by the benchmark system, since these definitions underpin the FN and FP rate metrics.
