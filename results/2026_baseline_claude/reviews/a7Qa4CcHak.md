## Summary

Terminal-Bench 2.0 is a benchmark of 89 hard, realistic tasks designed to evaluate AI agents operating in command-line (terminal) environments. Tasks span software engineering, system administration, security, scientific computing, and other domains; each runs inside a unique Docker container with a human-written oracle solution and outcome-driven tests. The paper evaluates 21 model/agent combinations (32,155 trials), reports a performance ceiling of ~65% for the best frontier system, and provides both trajectory-level and command-level failure analyses to guide future development.

---

## Strengths

- **Rigorous, multi-stage verification.** The 7-step audit pipeline (automated CI + LLM checks → expert human review → adversarial exploit testing → post-merge auditing) with ~3 reviewer-hours per task is substantially more thorough than most benchmark papers. The explicit criteria for specificity, solvability, and integrity, together with adversarial agent probing for shortcuts, give the benchmark unusual reliability for an open-contribution dataset.

- **Broad, well-motivated evaluation.** Evaluating 21 model/agent combinations (six scaffold types, 16+ frontier models) and running each combination at least 5 times (32,155 total trials) provides strong empirical coverage. The cost/performance Pareto analysis is practically relevant for practitioners choosing models, and the finding that model selection typically outweighs scaffold choice is a crisp, useful result.

- **Two-tier failure analysis.** The trajectory-level taxonomy (Execution / Coherence / Verification) and the command-level taxonomy (Invocation, REPL, Runtime, App failure, Filesystem) are complementary and provide actionable diagnostics. Quantifying that "command not found" accounts for 24.1% of all command failures—and that command error rates range from 9.2% to 26.7% across models—is directly useful for agent developers.

- **Human vs. empirical difficulty calibration.** The finding that 93.3% of human-rated "hard" tasks are also empirically hard for models, but that 54.5% of human-rated "medium" tasks are empirically hard, is an insightful result that reveals where models systematically lack human-style creative or adversarial reasoning.

---

## Weaknesses

### Fatal
None.

### Major

1. **Small benchmark size limits statistical resolution.** With only 89 tasks, the 95% confidence intervals shown in Figure 1 are wide—a swing of even two or three tasks can meaningfully shift a model's rank. Models within ~5–10 percentage points of each other (e.g., Gemini 3 Pro at ~57% vs. Gemini 3 Flash at ~52%) may not be reliably distinguishable. Given the claimed purpose of ranking frontier systems, this is a genuine limitation: the benchmark can identify large gaps between model tiers but is underpowered for fine-grained ranking at the top.

2. **Agent–model confound in the main leaderboard.** Figure 1 and the primary result (GPT-5.2 with Codex CLI at 63%) mix agent and model contributions. Since Codex CLI is a first-party scaffold engineered specifically for GPT-5.2, its advantage may reflect scaffold tuning rather than pure model capability. While Terminus 2 is offered as a neutral scaffold, it was also built by the same team, and not all models were tested under all scaffolds. The paper acknowledges this but does not fully disentangle the confound; model rankings derived from Figure 1 should be interpreted cautiously.

### Minor

1. **Task selection bias is not fully characterized.** Of 229 crowd-sourced tasks, 89 were selected based on "the author's difficulty assessment." The precise criteria and the characteristics of the 140 excluded tasks are not reported, making it hard to assess whether the selection process systematically skews the distribution toward certain categories or skill areas.

2. **Contamination risk is acknowledged but not mitigated.** Internet access is required for realism, but it means agents can discover oracle solutions and task files at tbench.ai. The paper notes that no cheating has been observed in tens of thousands of trajectories, but trajectory inspection may not be reliable for detecting retrieval-augmented cheating. The Big-Bench canary string aids training corpus decontamination only; it does not prevent inference-time retrieval.

### Trivial

1. Error bars in Figure 7 (failure mode distributions) are absent; it is unclear whether the observed differences between models are statistically significant.

---

## Nice-to-Haves

- Including a held-out private test split (acknowledged as future work) would substantially address both contamination and overfitting concerns.
- Reporting all model × scaffold combinations rather than only best-per-model in the main table would allow cleaner disentanglement of scaffold vs. model contributions.
- The correlation between human-predicted and empirical difficulty ($r = 0.436$) is only moderate; reporting inter-rater agreement for the human difficulty labels would help contextualize this.
- Confidence intervals on Figure 7 failure rates would strengthen the error analysis conclusions.

---

## Novel Insights

The most notable novel insight beyond the benchmark numbers is the dissociation between human-intuitive and model-empirical difficulty: a large fraction of tasks rated "medium" by humans (54.5%) are empirically "hard" for frontier models, pointing specifically to tasks requiring adversarial or creative reasoning (XSS filter bypass, Redcode strategy) that models cannot solve through pattern-following alone. This is a well-supported, actionable finding that goes beyond generic "models fall short" claims. The complementary command-level analysis—identifying "command not found" (24.1%) as the dominant failure mode and showing uncorrelated turn count / token usage with success—further clarifies where engineering effort on agents would be best spent.

---

## Suggestions

- Add per-model, per-category resolution rate tables (beyond Figure 4 and Figure 1) to help researchers target specific weakness areas.
- For the agent-model confound, at minimum run each top-5 model under both its native scaffold and Terminus 2 and report both; this would cost relatively little and substantially clarify the model vs. scaffold effect.
- Quantify inter-rater reliability for the human difficulty labels (medium/hard) in Section 4.2, as the moderate correlation ($r = 0.436$) is harder to interpret without knowing labeler agreement.

---

## Score and Decision

Terminal-Bench 2.0 addresses a real and timely evaluation gap for agentic LLMs in terminal environments. The verification pipeline is genuinely rigorous, the evaluation is broad, and the failure analyses offer actionable insights. The primary weaknesses—small benchmark size (89 tasks) and partial agent-model confound—are significant for a ranking benchmark but do not invalidate the paper's core contributions. The infrastructure (Harbor harness, Docker-based tasks) and the dataset itself are valuable community resources.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>