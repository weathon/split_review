- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 8, 6, 8
Now I have verified all claims against the paper. Let me produce the final consolidated review.

---

## Summary

AndroidWorld presents a dynamic, parameterized benchmarking environment for autonomous agents that control Android devices. Its core technical contributions are (1) **system-state-based reward signals** computed by inspecting the Android filesystem, SQLite databases, and system settings via ADB — more robust than UI-matching or regex-based rewards — and (2) **dynamic task parameterization** where each task is instantiated with randomly sampled parameters from a controlled seed, yielding effectively unlimited unique task instances while preserving reproducibility. The benchmark spans ~100 tasks across ~10 real Android apps plus 92 MiniWoB++ mobile tasks. The paper also releases M3A, a multimodal ReAct+Reflexion agent, and reports baselines against an adapted SeeAct agent on two foundation models (GPT-4 Turbo, Gemini 1.5 Pro). A robustness analysis on 6 tasks across 2 apps demonstrates that agent performance varies significantly across parameter configurations and even across runs with identical parameters due to model non-determinism.

---

## Strengths

1. **Dynamic task parameterization with demonstrated impact.** Section 3.3 describes how each task is instantiated from randomly sampled parameters using a controlled seed. Section 4.4 (Figure 3) empirically validates that performance varies significantly across different parameterizations (p < 0.05 for "add expense" and "edit note" tasks), and that even with a *fixed* seed the agent's performance varies due to model non-determinism. This provides concrete evidence that static benchmarks miss important robustness challenges.

2. **System-state-based reward signals that are accurate and reusable.** Section 3.4 explains how rewards are computed by inspecting the Android filesystem, SQLite databases, and system settings via ADB, rather than relying on superficial UI changes. Table 2 provides concrete validation code examples (e.g., `event_exists(event)`, `message_exists(phone_number, message, messaging_db)`). The method reuses the same validation logic across disparate apps (file management, note-taking, media playback), as described in Section 3.4.

3. **Comprehensive positioning against existing benchmarks.** Table 1 (Section 2) compares AndroidWorld with 20+ prior environments across dimensions (interactive environment, number of apps/tasks, reward method, platform). The table makes a clear quantitative case: AndroidWorld is the only mobile interactive environment that simultaneously supports unlimited task instances, spans more apps than any prior mobile interactive benchmark, and scores rewards via device state rather than regex or UI matching.

4. **Useful cross-platform baseline demonstrating the web-to-mobile gap.** Table 3 reports that SeeAct (adapted from desktop web) achieves only 15.5% on AndroidWorld vs. 30.6% for M3A (GPT-4 Turbo, a11y tree). This concretely shows that web-optimized agents transfer poorly to mobile, confirming the need for mobile-specific research and providing a baseline for future work.

5. **Rigorous robustness analysis using statistical testing.** Section 4.4 applies Wilson binomial proportion confidence intervals (95%) and significance tests (p < 0.05) across seed groups, showing that different parameterizations cause high intra-task variance. This is the strongest evidence in the paper that dynamic evaluation is necessary for reliable agent assessment.

---

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Robustness analysis covers only 6 tasks from 2 apps (Expenses and Markor).** The paper claims in the Abstract that "task variations can significantly affect agent performance" and draws general conclusions about the need for dynamic parameterization. However, the evidence in Section 4.4 (Figure 3) is limited to add/edit/delete operations on two apps. Whether this sensitivity generalizes to the other 7–8 apps and ~90 tasks is unknown. The findings are compelling as a demonstration but do not yet support broad claims about the necessity of dynamic evaluation across the full benchmark. Broader coverage (even a stratified sample across 4–5 apps) would substantially strengthen this core claim.

2. **No human performance number is provided in the submitted manuscript.** The human success rate is given only as `\humanresult` (a LaTeX macro placeholder). While this is clearly intended for the camera-ready version under anonymous review, its absence means the reader cannot calibrate task difficulty. If human performance is also low (e.g., <60%), the benchmark might be unreasonably hard or contain ambiguous tasks. The authors should confirm this number will be present in the final version.

3. **Only one random seed is used for the main benchmark results (Table 3).** Line 244 states "We set the seed to 30." Given that Section 4.4 demonstrates non-trivial performance variance even with a fixed seed (due to model non-determinism), the main results should ideally include confidence intervals or be averaged over multiple seeds. The robustness section acknowledges this problem but the main evaluation does not incorporate it.

4. **The step budget is described as "task-specific" but no details are given.** Line 244 says the evaluation uses "a task-specific step budget." Without knowing how these budgets were set, how they vary across tasks, or whether agents are bottlenecked by them, the reader cannot fully interpret the success rates. This should be specified.

5. **Limited baseline agent diversity.** The paper compares only its own M3A and an adapted SeeAct web agent. While SeeAct is a reasonable starting point, including at least one additional mobile-specific baseline (e.g., a prompting strategy from AppAgent, or a simpler heuristic agent) would increase the benchmark's immediate utility as a comparative platform. The paper acknowledges that SeeAct was designed for web and transfers poorly — its primary role is as a negative baseline.

### Trivial
None.

---

## Nice-to-Haves

- It would be informative to verify (or discuss) whether all parameter instantiations for each task template produce solvable states, or whether some parameter combinations could lead to impossible conditions that unfairly penalize agents.
- Additional baselines from existing mobile agents (CogAgent, AppAgent, or agents from AndroidArena/AitW) would increase the benchmark's adoption value, though the paper's primary contribution is the benchmark itself, not SOTA agent results.

---

## Removed Points

- **"Overclaiming 'infinite' tasks" (Harsh Critic #4):** The paper states "millions of unique task goals" (line 31) and "practically infinite set" (line 155). The former is mathematically accurate given the parameter ranges described, and the latter is used with explicit comparison to MiniWoB++ which makes the same claim. This is a framing issue without substance.
- **"Missing comparison to CogAgent/AppAgent" as a critical issue:** The harsh critic framed this as a "methodological gap," but the paper's contribution is the benchmark, not novel agent results. The SeeAct comparison is sufficient to demonstrate benchmark utility. Additional baselines would be welcome but their absence is not a gap. Moved to Minor (#5 above) and Nice-to-Have.
- **"Human performance withheld" as a major issue:** The `\humanresult` macro is clearly a placeholder for anonymous submission. The paper explicitly states the human result will be provided. This is a non-issue for the submitted manuscript but is kept as Minor (#2 above) to confirm it will be in the final version.
- **Generic complaints about "one-size-fits-all" evaluation rigor:** Various critiques about missing confidence intervals, limited statistical rigor for the full experiment, etc. are partially addressed by the robustness analysis (Section 4.4) which directly investigates this concern. The main results use a single seed per task, consistent with standard practice in benchmark papers, and the robustness analysis explicitly investigates variance.
- **Strength Finder's generic/superficial strengths:** Removed generic strengths that simply restate the problem importance (e.g., "addressed an important problem") without specific evidence. Only retained strengths with concrete, verifiable support in the paper.

---

## Novel Insights

The most interesting observation to emerge across both reviews is the tension between the paper's two central claims: (1) that dynamic parameterization is essential because performance varies with task parameters, and (2) that the benchmark supports "millions of unique task goals." The robustness analysis convincingly demonstrates (1) on a small set of tasks but the reviewer correctly notes this creates a scalability burden — if every parameter change can shift performance, then characterizing an agent's capability requires exhaustive or stratified sampling across parameter space. This is not a flaw in the paper but an implication worth articulating: dynamic benchmarks shift the evaluation problem from "score on N static tasks" to "distribution of scores over a parameter space," which demands more careful experimental design (e.g., stratified sampling, effect size reporting) than most current practices provide. The paper's robustness analysis is a good first step but also reveals how much more methodology is needed.

---

## Suggestions

1. **Broaden the robustness analysis to a stratified sample of 10–15 tasks across 4–5 apps** before publication, to substantiate the claim that sensitivity to parameters is a general phenomenon rather than specific to Expenses/Markor.
2. **Report confidence intervals or multi-seed averages for the main results in Table 3**, or at minimum acknowledge the single-seed limitation and provide variance estimates from the robustness analysis as a reference.
3. **Document the step budgets** (per task or by category) so readers can interpret whether agents are failing from capability limits or budget constraints.
4. **Ensure human performance is included as a concrete number in the camera-ready version.**
5. **Consider adding one lightweight baseline** (e.g., AppAgent-style prompting or a random-action agent) to establish a floor for the benchmark.

---
