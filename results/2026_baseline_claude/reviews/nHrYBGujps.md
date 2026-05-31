## Summary

BIRD-INTERACT is a multi-turn interactive text-to-SQL benchmark that extends LIVESQLBENCH with dynamic, agentic evaluation. Its primary contributions are: (1) a function-driven two-stage user simulator that prevents ground-truth leakage and handles unanswerable queries robustly; (2) dual evaluation settings—protocol-guided (*c*-Interact) and open-ended agentic (*a*-Interact)—both with budget-constrained awareness testing; (3) 900 tasks covering the full CRUD spectrum with ambiguity injection, state-dependent follow-up sub-tasks, and hierarchical knowledge bases. Experiments with 7 frontier LLMs yield at most ~17% end-to-end success, and analysis reveals model-specific interaction biases, memory grafting effects, and interaction test-time scaling behavior.

---

## Strengths

- **Fills a genuine gap with careful engineering.** The benchmark is the first to couple full-CRUD text-to-SQL with dynamic multi-turn evaluation, a realistic user simulator, and state-dependent sub-tasks. The three-category taxonomy of ambiguity types (surface-level, knowledge-chain, environmental) is principled and well-explained.

- **Function-driven user simulator is a substantive methodological contribution.** The two-stage design (semantic parsing to constrained symbolic actions, then controlled response generation) directly addresses the known failure modes of LLM-as-user-simulator: ground-truth leakage and task drift. On USERSIM-GUARD, the approach reduces UNA failure rates from ~67% (baseline) to ~3%, a dramatic improvement that is clearly quantified and independently evaluated.

- **Human alignment study (Table 3) is compelling.** Pearson correlation of 0.84 (*p* = 0.02) between function-driven simulator rankings and human rankings, compared to 0.61 (*p* = 0.14) for the baseline, provides external validity for the simulator's fidelity. Running this over 7 models × 100 tasks is a meaningful cost commitment.

- **Memory grafting experiment cleanly isolates a hypothesis.** Using one model's clarification history to bootstrap another model's SQL generation is a creative diagnostic that cleanly separates communication ability from generation ability, yielding a clear, interpretable result.

- **Action distribution analysis provides novel empirical insight.** The finding that models devote ~61% of actions to *submit* and *ask*, at the expense of cheaper knowledge-retrieval and schema-exploration actions, is a concrete, actionable observation about LLM decision-making under resource constraints.

---

## Weaknesses

### Fatal
None.

### Major

1. **Budget constraint implicitly leaks oracle information.** In *c*-Interact, the clarification budget is set as τ_clar = m_amb + λ_pat, and in *a*-Interact as B = B_base + 2·m_amb + 2·λ_pat. Since m_amb equals the number of annotated ambiguities per task, a model that knows the total budget can infer the oracle count of ambiguities. In the *c*-Interact protocol this matters especially: a model can count remaining budget turns to know when it has asked "enough" ambiguity-resolving questions. This conflates budget-awareness skill with ambiguity-detection skill and undermines the benchmark's difficulty claims. The authors do not analyze whether models exploit this signal.

2. **Single-run evaluation limits reliability of rankings.** All 7 models are evaluated at temperature=0 with a single pass due to cost, which the authors acknowledge. Given the very low absolute success rates (most models 8–25%), small numbers of tasks in some categories, and the sensitivity of multi-turn chains (one missed turn propagates), the standard error around these estimates could be material. This is particularly consequential for rankings between close-scoring models (e.g., Claude-Sonnet-3.7 at 8.33% vs. GPT-5 at 8.67% follow-up SR in *c*-Interact).

3. **ITS claim in the abstract is overstated relative to evidence.** The abstract and Section 5.2 assert that "performance improves monotonically with additional interaction opportunities across multiple models." Figure 4 shows this holds clearly only for Claude-3.7-Sonnet in *c*-Interact mode; in *a*-Interact, performance curves are flat or decrease for most models. The ITS Law as stated is not universally demonstrated and the conclusions drawn should be qualified.

### Minor

1. **Small correlation sample size.** Table 3's Pearson correlation is computed over only 7 system model rankings. While the p-values are informative, n=7 leaves wide confidence intervals on the correlation estimates. A bootstrap confidence interval would strengthen the claim.

2. **State-dependency evaluation conflates difficulty sources.** Follow-up sub-tasks depend on DB state changes from prior sub-tasks. When follow-up SR is lower, it is unclear how much is attributable to longer context, state tracking failure, or cascading errors from sub-task 1 failures (since sub-task 2 is only unlocked after successful sub-task 1). Disentangling these would sharpen the analysis.

3. **No free-mode *a*-Interact results are reported**, though the authors acknowledge this is planned as future work. This leaves open the key question of whether poor *a*-Interact performance reflects interaction strategy quality or budget management under stress conditions.

### Trivial

- The GPT-5 "8.67% of tasks" framing in the abstract refers to follow-up sub-task SR (the hardest metric), which could mislead readers who expect an overall completion rate. The priority sub-task SR for GPT-5 is 14.50%.

---

## Nice-to-Haves

- A budget-oblivious oracle ablation (hide the exact total budget but keep constraints) would isolate how much the oracle ambiguity count influences model behavior.
- Bootstrapped confidence intervals on SR for key comparisons in Table 2 would make reliability claims more precise without requiring re-runs.
- Reporting the fraction of interactions consumed by each model (relative to budget) would illuminate the budget-utilization patterns that drive efficiency differences.

---

## Novel Insights

Beyond the benchmark itself, two insights stand out as broadly transferable. First, the function-driven simulator design—mapping free-form user questions to constrained symbolic actions before generating responses—is a general recipe for controllable, leakage-free evaluation that applies to any interactive NLP benchmark, not only text-to-SQL. Second, the memory grafting experiment constitutes a clean methodology for attributing multi-turn agent failures to communication strategy versus generation quality, and the clear dissociation between GPT-5's poor clarification performance and strong generation performance suggests that interaction-quality alignment may be undertrained or undertested in RLHF pipelines for frontier models.

---

## Suggestions

- Decouple m_amb from the budget signal: assign a fixed per-task budget drawn from a distribution that doesn't directly reveal the oracle ambiguity count, or at minimum, ablate whether models exploit this signal.
- Provide bootstrapped SRs or at least error bars derived from sub-group variance to enable statistical comparison between models.
- Clarify in the ITS discussion which models satisfy the ITS Law; avoid claiming monotonic multi-model improvement when only one model clearly demonstrates it.
- Consider a small free-mode experiment (no budget constraint) on the LITE set to give context for the stress-mode results.

---

## Score and Decision

The paper makes genuine, well-validated contributions: a novel benchmark that captures multi-turn realistic database interaction, a methodologically sound user simulator with strong empirical validation, and several analytically useful experiments. The major weaknesses—budget oracle leakage, single-run reliability, and overstated ITS claims—are real but do not invalidate the core benchmark or its principal findings. For a benchmark paper evaluated on its contribution to the community, this is a solid contribution with actionable room for improvement.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>