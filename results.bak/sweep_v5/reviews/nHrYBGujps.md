Now I have all the information needed. Let me synthesize the final review.

## Summary

This paper introduces BIRD-INTERACT, a benchmark for evaluating text-to-SQL systems in dynamic, multi-turn interaction settings. It converts 900 single-turn tasks from LIVESQLBENCH into interactive scenarios by injecting ambiguities and adding state-dependent follow-up sub-tasks, covering the full CRUD spectrum across BI and DM domains. A key technical contribution is a function-driven user simulator that prevents ground-truth leakage by constraining LLM responses to three predefined action types (AMB/LOC/UNA). The benchmark defines two evaluation settings — *c*-Interact (protocol-guided conversation) and *a*-Interact (autonomous agentic planning) — with budget-constrained awareness. Experiments on 7 frontier LLMs show GPT-5 achieves only 8.67% (c-Interact) and 17% (a-Interact) success, demonstrating substantial room for improvement. Additional analyses (memory grafting, Interaction Test-time Scaling, action distribution) provide insights into the interaction-specific challenges that go beyond SQL generation ability.

## Strengths

1. **Function-driven user simulator with human-aligned validation.** The two-stage mapping (semantic parser → constrained action → controlled response) demonstrably reduces unanswerable-query failure from 67.4% to 2.7% on USERSIM-GUARD (Figure 6), where the 2,100 reference action labels were provided by human experts. The human alignment study (Table 3) further shows that the function-driven simulator achieves a statistically significant 0.84 Pearson correlation (p=0.02) with human users on 100 tasks, versus 0.61 (p=0.14) for the baseline — directly supporting the claim that the simulator produces realistic evaluation outcomes without human intervention.

2. **Dual evaluation settings that reveal qualitatively different model capabilities.** The *c*-Interact vs. *a*-Interact settings (Table 2) capture distinct failure patterns: GPT-5 is worst in *c*-Interact (14.50% SR) but best in *a*-Interact (29.17% SR), while Gemini-2.5-Pro shows the reverse pattern. This demonstrates that the benchmark measures something beyond what single-turn or static-history evaluations capture — namely, how models handle constrained conversational protocols vs. autonomous planning under budget constraints.

3. **Memory grafting experiment isolates communication skill from SQL ability.** Giving GPT-5 the interaction histories of stronger models (O3-mini, Qwen-3-Coder) lifts its success rate from 13.8% to 20.5% (Figure 5), providing direct evidence that the bottleneck in *c*-Interact is interactive communication strategy, not SQL competence. This is a clever experimental design that substantiates the claim that existing evaluations miss a critical dimension of capability.

4. **Comprehensive task design covering full CRUD spectrum with state-dependent follow-ups.** Beyond the SELECT-only scope of prior multi-turn benchmarks, BIRD-INTERACT includes DML/DDL operations and follow-ups that depend on modified database states from preceding queries. With 600 full-set + 300 lite-set tasks spanning 191 test cases, and up to 13.64 interactions per task, the benchmark provides a substantially richer evaluation than existing alternatives like CoSQL and SParC.

## Weaknesses

### Fatal
None.

### Major

1. **No evaluation of existing multi-turn text-to-SQL systems.** The paper motivates BIRD-INTERACT by arguing that existing multi-turn benchmarks (CoSQL, SParC, LEARN-TO-CLARIFY) are inadequate, yet the experiments only test general-purpose LLMs with generic prompts. No existing multi-turn system (e.g., models fine-tuned on CoSQL, or agent frameworks from prior work) is evaluated. Without this comparison, the central claim that BIRD-INTERACT captures *different* capabilities or reveals *new* limitations — beyond what existing benchmarks already expose — is only partially supported. The paper would be substantially strengthened by demonstrating that a model fine-tuned on CoSQL/SParC performs no better on BIRD-INTERACT than general-purpose models, or that its failure modes are qualitatively different.

2. **Single runs without confidence intervals.** Table 2 reports a single run per model per setting. Although temperature=0 reduces variance, it does not eliminate it, especially for the small success-rate differences between models (e.g., 14.50% vs 18.50% SR in c-Interact priority). The paper acknowledges this constraint (Section 5: "conducting single runs due to cost") but several analyses (memory grafting improvements of ~5-7 percentage points, action distribution patterns) would benefit from at least 3 runs on a subset to establish confidence. This limits the reliability of fine-grained model comparisons.

3. **The Interaction Test-time Scaling claim is overgeneralized.** The paper claims an "ITS Law" where performance improves monotonically with interaction opportunities. However, Figure 4 shows that only Claude-3.7-Sonnet clearly exhibits this pattern. Other models plateau or decline, especially in *a*-Interact. The paper should either qualify the claim as model-dependent or report which models satisfy the ITS law and which do not.

### Minor

1. **No human performance baseline on the benchmark tasks.** While the paper provides human alignment for the simulator (Table 3), it does not report human performance on BIRD-INTERACT tasks themselves. This makes it hard to calibrate whether the 8.67% GPT-5 success rate indicates a genuinely difficult benchmark or one with unreasonably strict evaluation criteria. This is a common omission in benchmark papers and does not invalidate the findings, but including it would strengthen confidence in the benchmark's difficulty calibration.

2. **Action distribution analysis does not connect to success.** The paper reports that *submit* and *ask* actions dominate (60.87%), but does not analyze whether successful agents show different action proportions than unsuccessful ones. Linking action patterns to outcomes would make this analysis significantly more actionable for future research.

3. **Budget parameter choices (B_base=6, λ_pat=3) are not ablated.** The budget formulas and default values are clearly stated, but without ablation over different settings, it is unclear how sensitive the results are to these choices. This is especially relevant since the paper draws conclusions about budget-constrained behavior from a single budget configuration.

4. **ITS analysis lacks statistical rigor for the "ITS Law" definition.** The paper defines the ITS Law as scaling to match idealized single-turn performance, but only one model (Claude-3.7-Sonnet) approaches this. The other models would need significantly more turns or may never reach the idealized baseline. The framing overreaches relative to the evidence.

### Trivial
None.

## Nice-to-Haves
- Ablation of budget parameters (B_base, λ_pat) to show sensitivity of model rankings.
- Correlation analysis between single-turn (BIRD/LIVESQLBENCH) performance and BIRD-INTERACT performance.
- Failure mode breakdown: are failures due to ambiguity resolution, SQL errors, state dependency, or budget exhaustion?
- Example interaction trajectories from actual model runs (success and failure) to illustrate the challenge granularity.

## Removed Points

The following points from the input reviews are removed with justification:

1. **"No human evaluation of simulator's action classification"** (Harsh Critic Issue 3, sub-point). REMOVED — factually incorrect. The paper explicitly states USERSIM-GUARD comprises "2,100 questions with reference actions labeled by human experts." Ground-truth actions are human-annotated. The LLM judge evaluates simulator outputs against these human labels.

2. **"Injected ambiguities may lack realism"** (Harsh Critic Issue 4). REMOVED — speculative concern without specific evidence. The paper reports 93% inter-annotator agreement and validates the benchmark through human alignment studies. Without evidence that the anomalies are artificial or unrealistic, this is conjecture.

3. **"Missing free-mode evaluation"** (Multiple Harsh Critic notes). REMOVED — the paper explicitly scopes free-mode as future work (Section 8). Criticizing a paper for not doing what it explicitly deferred is not a valid weakness.

4. **"Missing related works / prior work discussion"** (Multiple mentions). REMOVED per instructions — I cannot verify the existence of missing references.

5. **"Comparison to other benchmarks should quantify that models behave differently on BIRD-INTERACT"** (Harsh Critic, Section-by-section note). REMOVED — partially addressed. The paper shows qualitative differences through the memory grafting experiment and the divergent model rankings across c-Interact vs a-Interact (Table 2). The request for quantitative evidence of behavioral divergence is reasonable but more of a nice-to-have than a weakness.

6. **Strength Finder's generic strengths.** Several Strength Finder entries (e.g., "the paper identifies a genuine gap," "the benchmark covers a broad range") are generic observations that any benchmark paper would satisfy. These are not specific enough to retain as strengths. The concrete, evidenced strengths (simulator validation, dual evaluation settings revealing distinct patterns, memory grafting) are retained.

## Novel Insights

The most interesting finding unique to this review is the asymmetry in how different LLMs handle structured conversation (*c*-Interact) versus autonomous planning (*a*-Interact). GPT-5 being the worst at *c*-Interact but best at *a*-Interact, while Gemini-2.5-Pro shows the opposite pattern, suggests that different training and architectural choices produce fundamentally different "interaction personalities." This is a genuinely novel observation from the benchmark, and it points toward the need for interaction-mode-aware evaluation — a dimension absent from all prior text-to-SQL benchmarks. The memory grafting result reinforces this: giving GPT-5 someone else's interaction history fixes much of its deficit, implying that the bottleneck is not what it knows about SQL but how it asks questions.

## Suggestions

1. Evaluate at least one existing multi-turn text-to-SQL system (e.g., a model fine-tuned on CoSQL, or a prior agent framework like MAC-SQL) on BIRD-INTERACT. This is the single most impactful addition to substantiate the benchmark's novelty claim.
2. Report 3 runs (with confidence intervals) on the LITE 300-task subset for the main results table to establish measurement reliability.
3. Qualify the ITS Law claim to reflect that only a subset of models exhibits clean scaling behavior, and report which models satisfy the law.
4. Add an analysis linking action distributions to task success/failure in *a*-Interact.
5. Include a human performance baseline on a subset of tasks (50-100) to calibrate benchmark difficulty.

## Score and Decision

**Calibration anchors** (all retrieved in the single batch search):

| Path | Avg Score | Comparison to this paper |
|------|-----------|-------------------------|
| τ-bench | 6.50 | Similar tool-agent-user interaction benchmark with LLM user simulators. BIRD-INTERACT has stronger simulator validation (human alignment study) but narrower domain focus. Comparable quality. |
| AgentBench | 6.20 | Broad agent benchmark with 8 environments and 27 models. BIRD-INTERACT has deeper analysis in one domain (memory grafting, ITS) but fewer models. Both accepted. |
| CHASE-SQL | 6.25 | Text-to-SQL method paper reaching SOTA on BIRD. BIRD-INTERACT focuses on evaluation rather than methods; different contribution type, comparable rigor. |
| DialSim | 5.00 | Dialogue simulator with data leakage concerns. BIRD-INTERACT has stronger validation and avoids the data contamination issue; clearly stronger. |
| DB-GPT-Hub | 3.75 | Text-to-SQL benchmarking suite criticized for lacking novelty and insufficient contribution. BIRD-INTERACT has substantially more technical innovation (function-driven simulator, dual settings, interaction analyses). |
| NmILZXKcOi (DB-GPT-Hub) | 3.75 | (Same as above) |
| 7ZeoPg3eTA (TrustSQL) | 4.00 | Text-to-SQL reliability benchmark. BIRD-INTERACT addresses a more challenging and underexplored problem space. |
| roNSXZpUDN (τ-bench) | 6.50 | (Same as τ-bench above) |

Positioned relative to these anchors, the paper is a solid benchmark contribution. Its core technical contribution (function-driven user simulator) is validated with human data, which is stronger than typical benchmark work. The dual evaluation settings and memory grafting experiment provide genuine insight. The main weakness — absence of comparison to existing multi-turn systems — is a real gap that prevents the paper from fully proving its novelty claim, but it does not invalidate the benchmark's value.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>