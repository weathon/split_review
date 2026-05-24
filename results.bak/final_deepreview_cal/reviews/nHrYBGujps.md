Now I have all the information needed. Let me compose the final review.

## Summary
This paper introduces BIRD-INTERACT, a benchmark for evaluating text-to-SQL systems through dynamic, multi-turn interactions. It contributes (1) a function-driven user simulator designed to prevent ground-truth leakage, (2) two evaluation settings — protocol-guided (c-Interact) and autonomous agentic (a-Interact), and (3) a suite of 900 tasks covering full CRUD operations with state-dependent follow-up sub-tasks. The benchmark reveals that even the strongest models achieve low success rates (GPT-5: 8.67% in c-Interact, 17% in a-Interact), and that interaction strategy is a capability partially separable from SQL generation skill.

## Strengths

1. **Carefully designed interactive benchmark that addresses real gaps in existing text-to-SQL evaluation.** Prior multi-turn benchmarks (COSQL, SParC) use static conversation transcripts shared across all models, which cannot measure a model's own interaction skill. BIRD-INTERACT replaces this with a genuinely dynamic environment where the model's clarification choices directly shape the interaction trajectory. The ambiguity injection methodology (superficial, knowledge chain breaking, environmental) is well-thought-out and the state-dependent follow-up sub-tasks go beyond the SELECT-only scope of prior work.

2. **Function-driven user simulator with stronger validation than comparable work.** Section 6 shows the simulator reduces unanswerable-question leakage from 67.4% (baseline) to 2.7% (Figure 6), and achieves a 0.84 Pearson correlation with human users (p=0.02, Table 3). This is substantially more validation than related simulators in MINT or τ-bench provide for their own simulators, and gives reasonable confidence that the benchmark measures interactive ability rather than simulator artifacts.

3. **Two complementary evaluation settings that reveal distinct interaction-mode preferences.** The contrast between c-Interact and a-Interact (Table 2) surfaces genuine variation across models — GPT-5 ranks worst in c-Interact (14.50% SR) but best in a-Interact (29.17% SR), while Gemini-2.5-Pro shows the opposite pattern. This demonstrates the benchmark can differentiate interaction strategies from SQL generation skill in a way static benchmarks cannot.

4. **Budget-constrained evaluation with cost analysis.** The paper reports per-task costs alongside success rates, enabling comparisons of efficiency. This is practical and relevant for deployment decisions.

## Weaknesses

### Fatal
None.

### Major

1. **Simulator response content is not directly validated for AMB/LOC actions.** The USERSIM-GUARD evaluation (Section 6) validates that the simulator correctly *classifies* questions into AMB/LOC/UNA categories, but does not evaluate whether the *content* of the generated responses is appropriate — neither too revealing nor too vague. The paper states "quality control ensures that ambiguous queries are unsolvable without clarification yet fully reconstructable once clarifications are provided" (line 86), but the evidence for this claim rests on the action classification accuracy and the human correlation study, both of which are indirect. A direct evaluation (e.g., human annotation of a sample of generated clarifications for informativeness and leakage) would substantially strengthen this central methodological contribution. As written, the benchmark results depend on a component whose output quality is assumed rather than measured.

2. **Memory grafting experiment has uncontrolled confounds that weaken the communication-deficiency claim.** The experiment compares GPT-5 with grafted histories from Qwen-3-Coder / O3-mini against GPT-5 with its own interaction history. Without a control condition where GPT-5 receives a graft from *its own successful runs* (if any), it is impossible to attribute the improvement to the *quality* of the other models' communication versus the simple fact that the grafted histories contain successful resolution patterns. The baseline "without memory grafting" includes GPT-5's own potentially unsuccessful interactions, which may contaminate the context. This confound means the conclusion that GPT-5 lacks "effective communication schema" is not as strongly supported as claimed.

### Minor

3. **The ITS Law claim is overstated for several models.** The paper states an "ITS Law" where performance improves monotonically with additional interaction turns. However, Figure 4 shows this pattern clearly only for Claude-3.7-Sonnet in c-Interact; other models show flatter or more variable trends. Qwen-3 in c-Interact is essentially flat. The law is defined as a conditional ("a model satisfies this law if...") which softens the claim, but the presentation still implies a broader empirical regularity than the data support.

4. **c-Interact vs. a-Interact comparisons conflate multiple dimensions.** The two settings differ in interaction protocol, action space, budget computation, and debugging rules simultaneously. The paper's observation that GPT-5 performs poorly in c-Interact but well in a-Interact is interesting, but attributing this to "communication abilities" (even as a hypothesis) is speculative. The paper appropriately hedges with "we hypothesize," but several conclusions (e.g., "interaction mode emerged as the decisive factor") outrun the experimental design.

5. **Results are from single runs.** Table 2 reports success rates without confidence intervals or error bars. The paper acknowledges this ("single runs due to cost," line 177), but many of the reported differences (e.g., 8.67% vs. 8.33%) are within the range of noise for single-run evaluations. Bootstrapped confidence intervals on the LITE set would strengthen reliability claims.

6. **The human correlation study (Table 3) has limited sample size.** With only 100 tasks, the 0.84 Pearson correlation (p=0.02) is significant but the result could be partially driven by task difficulty rather than per-turn simulator alignment. A per-interaction agreement metric or controlling for task difficulty would strengthen this evidence.

### Trivial
None.

## Nice-to-Haves
- A control for the memory grafting experiment where GPT-5 receives a graft from its own successful interactions (or a random interaction history of equivalent length) would clarify whether the improvement is due to information content or communication quality.
- Analysis of which types of *ask* actions (productive vs. unproductive) models take could deepen the action distribution analysis.
- Reporting average budget used vs. budget allocated would complement the cost-per-task numbers.

## Removed Points
These points were flagged by reviewers but removed after verification against the paper:

- **Criticism about the existence/release status of LIVESQLBENCH, GPT-5, Qwen3-235B-A22B-Instruct-2507, and "AMG"** — removed per instructions: the paper cites these and they are assumed to exist.
- **Claim that simulator validation is entirely absent** — the paper does validate action classification accuracy on USERSIM-GUARD (Figure 6) and provides a human correlation study (Table 3). The criticism was reduced from "fatal flaw" to "major" because the evidence is indirect rather than absent.
- **Criticism that memory grafting histories are from "successful runs"** — the paper does not state this; given the source models' SR of ~18.5%, most histories are from unsuccessful runs. This specific sub-point is incorrect.
- **Formatting/style nitpicks and missing appendix details** — removed per instructions (parser artifacts, not author errors).
- **Criticism about missing related work** — removed per instructions (cannot verify existence of missing citations).

## Novel Insights
The observation that GPT-5 underperforms in the structured conversational setting (c-Interact) but excels in the open-ended agentic setting (a-Interact), while Gemini-2.5-Pro shows the reverse pattern, is genuinely interesting and suggests that benchmark design choices about interaction protocols can qualitatively change which models appear "best." This has implications beyond text-to-SQL — it suggests that single-mode interactive evaluation may produce misleading leaderboards. The memory grafting experiment (despite its confounds) also sketches a methodology for disentangling interaction skill from task skill that future work could refine into a controlled evaluation paradigm.

## Suggestions
- **Directly validate simulator response content**: Have human annotators judge a sample (e.g., 200) of generated simulator responses for (a) appropriateness of information revealed, (b) consistency with the ground-truth ambiguity, and (c) absence of answer leakage. Report agreement rates. This single addition would substantially address the most significant concern about the benchmark.
- **Add controls to the memory grafting experiment**: Include a condition where GPT-5 receives a graft from its *own* successful runs (or a scrambled/irrelevant history of equal length) to isolate whether improvement is due to the quality of the communication or simply the presence of successful resolution information.
- **Report bootstrapped confidence intervals** on BIRD-INTERACT-LITE for the main results, given single-run evaluations on the full set.
- **Tone down the ITS Law claim** to acknowledge that scaling behavior varies substantially across models, or restrict the claim to the specific models that exhibit it.

## Score and Decision

### Calibration Anchors

**Round 1 (Bracketing):**
- Weak band (avg < 3.5): Avg6hmtgHE (3.40), RuY1r1PDdQ (3.00), b1vVm6Ldrd (3.00) — none of these are benchmark papers of comparable quality.
- Middle band (3.5–7.5): NmILZXKcOi / DB-GPT-Hub (3.75), WYdpjwKQma / LAIA-SQL (5.00), CvGqMD5OtX / CHASE-SQL (6.25), BAglD6NGy0 / ROUTE (6.25).
- Strong band (avg > 7.5): XmProj9cPs / Spider 2.0 (8.00), GGlpykXDCa / MMQA (8.00), YrycTjllL0 / BigCodeBench (9.00).

**Round 1 bracket:** 5.5–7.5. The paper is stronger than method papers in the 5–6 range but not at the impact level of Spider 2.0.

**Round 2 (Narrowing):**
- jp3gWrMuIZ / MINT (6.75) — most directly comparable: both are multi-turn interaction benchmarks with LLM user simulators. BIRD-INTERACT has more careful simulator validation (USERSIM-GUARD + human study) but narrower domain scope. Comparable in quality, perhaps slightly below MINT's breadth but exceeding it in benchmark construction rigor for its domain.
- roNSXZpUDN / τ-bench (6.50) — directly comparable on user-simulator-based interactive evaluation. BIRD-INTERACT provides more validation of its simulator. Slightly stronger or comparable.
- Dpqw0namg3 / LAM Simulator (6.00) — less directly relevant.
- 8w22WLy2R8 / MemSim (5.25), W1x77vRucB / DialSim (5.00) — lower quality.
- zAdUB0aCTQ / AgentBench (6.20) — broader agent benchmark but less focused.
- CvGqMD5OtX / CHASE-SQL (6.25) — method paper, less relevant.

**Final score:** 6.5. The paper is comparable to MINT (6.75) in quality but narrower in scope; slightly stronger than τ-bench (6.50) in terms of simulator validation; and clearly above method papers in the 5–6 range. The benchmark construction is thoughtful, the simulator validation is better than related work, and the findings are informative. The main weakness is the incomplete validation of simulator response content, which prevents a higher score.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>