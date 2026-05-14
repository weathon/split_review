Now let me write the final consolidated review.

## Summary

Terminal-Bench introduces a benchmark of 89 hard, realistic tasks run inside Docker containers in command-line terminal environments. The tasks span 16 categories (software engineering, security, scientific computing, etc.) and were contributed by 93 crowd-sourced authors, then subjected to a seven-stage verification pipeline (automated CI, LLM checks, expert human review, adversarial exploit detection, post-merge trajectory audits). The paper evaluates 16 frontier models across 6 agent scaffolds in 32,155 trials, reporting that the best-performing system (GPT-5.2 + Codex CLI) achieves ~65% resolution, with most systems scoring far lower. A command-level error taxonomy categorizes 3,800 sampled failures and identifies "command not found" (24.1%) as the dominant failure mode.

---

## Strengths

- **Best-in-class multi-stage verification pipeline.** The audit process (Figure 3) includes automated checks, LLM-based review, expert human review, adversarial exploit detection, and post-merge trajectory auditing — roughly three person-hours of review per task. This is genuinely thorough and sets a high bar for benchmark quality assurance.

- **Command-level error taxonomy with actionable quantification.** Section 4.4 analyzes 3,800 sampled command failures and reports granular subcategories (e.g., "command not found" 24.1%, "file not found" 11.1%, "app failure" 9.6%). This is the paper's most novel analysis and provides concrete, actionable direction for improving terminal-based agents.

- **Large-scale, reproducible evaluation.** 32,155 trials across 16 models and 6 agents using a standardized Harbor harness, with pinned Docker images and open-source infrastructure. The scope of evaluation is substantial.

- **Trajectory-level failure analysis with validated taxonomy.** Section 4.3 applies a taxonomy (Execution/Coherence/Verification) validated to 93% Cohen's κ on calibration trials, showing distinct failure profiles between closed-source and open-weight models.

- **Diverse, genuinely hard task composition.** Tasks range from fixing an OCaml garbage collector (24 hours expert-estimated) to differential cryptanalysis of the FEAL cipher — clearly beyond toy problems. 51.4% of tasks are estimated at >1 hour for an expert.

---

## Weaknesses

### Fatal
None.

### Major

- **Model-agent confound in the headline results.** Figure 1 reports "Task resolution rate per model" but uses a different agent scaffold for different models, chosen "to maximize performance" (GPT-5.2 with Codex CLI, Claude Opus 4.5 with Terminus 2, etc.). The observed ordering conflates model quality with agent quality — a reader cannot determine whether GPT-5.2 leads because it is the best model or because Codex CLI is the best agent. The paper acknowledges this in Section 3.1 ("agent and model performance are hard to decouple") and does provide some analysis of agent effects (e.g., a 17% swing for Gemini 2.5 Pro when switching from OpenHands to Terminus 2), but the main figure is still labeled and positioned as a model ranking. The trajectory-level error analysis (Section 4.3) correctly holds the agent constant (Terminus 2), but this should be the primary rather than secondary comparison. **Authors must rework the presentation so that the fixed-scaffold comparison is the headline result, with best-agent-per-model as secondary.**

### Minor

- **Contamination risk acknowledged but not addressed.** Section 5 notes that models could be trained on the public dataset and that only a canary string is used for decontamination. The paper explicitly declines to create a private test set ("outside the scope of this paper"). Training cutoff dates of evaluated models are not reported. While this is a common issue across benchmark papers, it undermines the benchmark's lasting value for tracking progress.

- **No human performance baseline.** The paper claims tasks are "hard" and "realistic" but provides no human evaluation. Even a small-scale study (3–5 experts on a subset of tasks) would substantiate the difficulty claims.

- **Benchmark size limits fine-grained analysis.** With 89 tasks, 95% confidence intervals in Figure 1 are wide enough that many model pairs are not statistically distinguishable. 29% of tasks fall into Software Engineering, while 5 categories have only 1–2 tasks each, making category-level analysis unreliable.

- **Human difficulty estimates are from task authors, not independent evaluators.** Table 1 reports expert and junior time estimates provided by the task authors themselves. The correlation between human-predicted and empirical difficulty (r=0.436) is modest, and although the paper honestly acknowledges this, the benchmark's difficulty stratification relies on these subjective labels.

- **"Command not found" failures are not root-caused.** Section 4.4 identifies "command not found" as the most frequent failure (24.1%) but does not analyze whether this stems from hallucinated commands, environment misconfiguration, or genuine lack of command knowledge — three causes with very different implications for improvement.

- **LLM-as-judge validation on small samples.** The command-level taxonomy validation reports 82.0% agreement on 50 annotations across 10+ subcategories, and the trajectory-level κ=93% is based on only 20 calibration trials. Both are thin for the granularity of the taxonomies.

### Trivial

- The paper cites "$1B in run-rate revenue" from Anthropic in the introduction but this is an attributed quote ("Anthropic claims") — it reads as a motivation, not an empirical claim about the benchmark.
- Figure captions should explicitly state both the model and agent names for every entry, not just in the table but in the main text description.

---

## Nice-to-Haves
- **Task-level variance analysis:** Which tasks drive the ranking differences between models? A correlation matrix across tasks would reveal whether the benchmark measures a single latent ability or multiple independent skills.
- **Agent effect quantification:** For models that can be run on multiple agents, report the full performance gap distribution to bound how much variance in Figure 1 is due to agents versus models.
- **Failure trajectory diagrams:** Concrete examples of successful and failed trajectories for the same task would make the error taxonomy more actionable.

---

## Removed Points
These points are flagged to be removed — treat them with caution:
1. **"10 categories have 1-2 tasks each"** — The paper actually has 5 categories with 1-2 tasks (Games, Video Processing, Data Querying, Optimization, Personal Assistant). The critic exaggerated.
2. **"The $1B revenue claim is unverifiable"** — The paper attributes this to Anthropic (2025) with explicit attribution ("Anthropic claims"). Per hard rules, removing criticisms that question the existence of cited references.
3. **"The LLM check creates an incentive to fix surface issues"** — Speculative claim without evidence in the paper.
4. **"Cost analysis does not control for retries/different reasoning budgets"** — The paper states models were run with provider defaults for reasoning effort, which is a standard approach.
5. **"The taxonomy is generic and could describe any agent benchmark"** — While the three high-level categories (Execution, Coherence, Verification) are broad, the paper provides domain-specific subcategories (Appendix D, stripped by parser). The command-level taxonomy (Section 4.4) is terminal-specific.
6. **"Missing appendix/proofs"** — The parser strips those sections; they exist in the original submission.

---

## Novel Insights
The most interesting finding from the review process is the tension between the paper's rigorous benchmark construction methodology and its somewhat careless presentation of results. The verification pipeline is genuinely state-of-the-art — the seven-stage process with adversarial exploit detection and post-merge auditing goes well beyond what most benchmark papers do. Yet the headline figure undermines this care by conflating two variables (model and agent) that the paper itself acknowledges are hard to decouple. This disconnect suggests that the field of agent benchmarking needs clearer norms around reporting standards: when a benchmark is interactive and agent-dependent, "best model + best agent" results and "fixed scaffold" results should be presented as co-equal primary analyses, not as a headline ranking with the caveat buried in the caption. The command-level error taxonomy (e.g., "command not found" at 24.1%) is the paper's most novel contribution and points to a concrete engineering target: agents need better command discovery and environment awareness, not just better reasoning.

---

## Suggestions
1. **Restructure the results section.** Make Figure 1 show all models evaluated on Terminus 2 (the neutral scaffold) as the primary comparison. Move the best-agent-per-model results to a secondary figure or table.
2. **Report training data cutoffs** for all evaluated models relative to the benchmark's release date, and commit to a private hold-out set for future decontaminated evaluation.
3. **Add a human baseline** (even 3–5 experts on a 20-task subset) to substantiate the claim that tasks are "hard."
4. **Expand the command-level error analysis** to diagnose why "command not found" occurs (hallucination vs. misconfiguration vs. knowledge gap).
5. **Report task-level pass rates** across models and compute reliability metrics (e.g., split-half reliability) for the benchmark.

---

## Score and Decision

### Calibration Anchors
All anchors returned by `calibration_search` (paths and scores):

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `/home/wg25r/review_agent/human_reviews_2026/9gw03JpKK4.md` (Gaia2) | 8.00 | Superior benchmark paper — cleaner methodology, no model-agent confound, more innovative concept. Terminal-Bench is clearly weaker. |
| `/home/wg25r/review_agent/human_reviews_2026/uobROwBsJm.md` (MCPMark) | 7.33 | Similar benchmark paper with 127 tasks, uses same agent for all models (no confound). Terminal-Bench has stronger verification but weaker presentation of results. |
| `/home/wg25r/review_agent/human_reviews_2026/0sPCSssY2r.md` (LiveMCPBench) | 5.50 | Rejected — similar size (95 tasks), LLM-as-judge evaluation. Terminal-Bench has better verification (programmatic tests) and more models, but LiveMCPBench has no confound issue. Terminal-Bench is slightly stronger. |
| `/home/wg25r/review_agent/human_reviews_2026/2H03gm4Rq6.md` (TRACE) | 5.00 | Accepted Poster — framework for evolving benchmarks, different contribution type. Comparable quality. |
| `/home/wg25r/review_agent/human_reviews_2026/aZFjp5wqck.md` (AgentVQA) | 4.00 | Rejected — weak motivation, unclear contribution. Terminal-Bench is stronger. |
| `/home/wg25r/review_agent/human_reviews_2026/dAn82lpLx4.md` (Agent's Marathon) | 3.00 | Rejected — unrealistic abstraction. Terminal-Bench is stronger. |
| `/home/wg25r/review_agent/human_reviews_2026/SxFOEwQLMT.md` (WetBench) | 2.00 | Rejected — fundamentally flawed methodology (LLM simulates experiments). Terminal-Bench is much stronger. |

### Positioned Score
Terminal-Bench sits between LiveMCPBench (5.50, Reject) and MCPMark (7.33, Accept). Its benchmark construction and verification pipeline are stronger than LiveMCPBench's, but the model-agent confound in the headline results is a significant methodological issue that MCPMark avoids. The paper has genuine contributions — the verification pipeline, command-level error taxonomy, and large-scale evaluation — but the presentation of results is misleading in its current form and requires major revision. I place it closer to the accept boundary than the reject one, conditional on addressing the confound.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>