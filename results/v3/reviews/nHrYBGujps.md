Now I have enough information to write the final review. Let me compile everything.

## Anchor List (All Rounds)

| Anchor ID | Avg Score | Source Round/Bucket | Comparison |
|-----------|-----------|---------------------|------------|
| XmProj9cPs (Spider 2.0) | 8.00 | R1-topic-high | Gold-standard text-to-SQL benchmark. BIRD-INTERACT has a similar benchmark contribution but weaker analytical narrative and overclaiming issues. |
| CvGqMD5OtX (CHASE-SQL) | 6.25 | R1-topic-mid / R2 | Method paper, not a benchmark. Different contribution type, so less directly comparable. |
| BAglD6NGy0 (ROUTE) | 6.25 | R2 | Method paper. Not directly comparable. |
| RaSLSUCKz0 (SQL-GEN) | 5.67 | R2 | Method paper. Not directly comparable. |
| 7ZeoPg3eTA (TrustSQL) | 4.00 | R1-topic-mid | Benchmark with dataset reliability concerns. BIRD-INTERACT has stronger empirical validation (simulator analysis, inter-annotator agreement). |
| NmILZXKcOi (DB-GPT-Hub) | 3.75 | R1-topic-mid | Engineering-focused benchmark, criticized for overclaiming and lack of novelty. BIRD-INTERACT has stronger novelty but shares some overclaiming issues. |
| E2RyjrBMVZ (Quantifying Variance) | 4.17 | R1-weakness-single-run | Paper about evaluation variance. Mixed reception. |
| BltaWJZMeR (DataSciBench) | 3.20 | R1-topic-low | Benchmark with serious methodology flaws. BIRD-INTERACT is substantially stronger. |
| lMW9d1AqC9 (unrelated) | 1.67 | R1-topic-low | Poor paper, not relevant. |

**Round-1 bracket:** Between 4.0 and 6.5.
**Round-2 narrowing:** The paper sits in the 4.5–5.5 range. The core benchmark contribution is genuine and well-validated (stronger than TrustSQL/DataSciBench/DB-GPT-Hub), but the analytical overclaims (especially ITS "Law" contradicted by its own data) prevent it from reaching the 6+ range.

**What did the low-band anchors fail at, and does this paper share those failures?** DataSciBench (3.20) failed at weak validation methodology and unclear contributions — BIRD-INTERACT does NOT share these (Section 6 provides strong validation). TrustSQL (4.00) failed at dataset quality assurance — BIRD-INTERACT's 93.33% inter-annotator agreement and rigorous simulator guard evaluation are better. DB-GPT-Hub (3.75) failed at overclaiming — and BIRD-INTERACT DOES share this failure: the ITS "Law" claim (Introduction line 36: "performance improves monotonically") is contradicted by its own Figure 4. This overclaim is the paper's most significant weakness.

Now let me write the final review.

---

Let me think more about whether I should mention the "no specialized dialog-based baselines" as a weakness. The harsh critic says this weakens the validation of the benchmark. I think this is a genuine limitation but standard for benchmark papers — Spider 2.0 also didn't test every specialized method. However, the lack of ANY dialog-based system is notable since the benchmark is specifically about interaction. I'll keep it as a minor weakness.

Let me also think about whether the Memory Grafting criticism should be elevated. The harsh critic says it's underdetermined. The paper's conclusion is "a more effective communication schema is required" — this is actually quite modest. While better controls would strengthen it, the conclusion is reasonable given the experiment. I'll keep it as minor.

OK, I'm ready to write the final review.## Summary

BIRD-INTERACT introduces a benchmark for evaluating LLMs on dynamic multi-turn text-to-SQL tasks. The key contributions are: (1) a function-driven user simulator designed to prevent ground-truth leakage and task deviation, validated extensively in Section 6; (2) two complementary evaluation settings — *c*-Interact (protocol-guided conversation) and *a*-Interact (open-ended agentic planning); and (3) a 900-task suite spanning the full CRUD spectrum with ambiguity injection, follow-up sub-tasks, and executable test cases. The benchmark convincingly shows that frontier models struggle — GPT-5 achieves only 8.67% success in *c*-Interact and 17.00% in *a*-Interact — and reveals previously unmeasurable interaction-strategy variance (e.g., GPT-5 goes from worst in *c*-Interact to best in *a*-Interact).

## Strengths

- **Well-validated function-driven user simulator.** Section 3.3 identifies the critical flaw in naive LLM-based simulators (ground-truth leakage, task deviation) and proposes a two-stage approach constraining responses to `AMB()`, `LOC()`, `UNA()` actions. Section 6 provides direct evidence: the function-driven approach achieves only 2.7% failure on Unanswerable queries vs. up to 67.4% for baselines (Figure 6), and reaches 0.84 Pearson correlation with human users vs. 0.61 for standard LLM simulators (Table 3). This directly validates the fairness of the evaluation environment.

- **Dual evaluation settings reveal interaction-mode variance.** The *c*-Interact and *a*-Interact protocols (Section 4, Figure 3) with budget-constrained awareness capture meaningful behavioral differences. Table 2 shows a striking reversal: GPT-5 is the worst performer in *c*-Interact (8.67% SR) but the best in *a*-Interact (17.00% SR). This proves the benchmark measures interaction-strategy variance that static-history evaluations fundamentally cannot capture.

- **Full CRUD scope with principled ambiguity taxonomy.** The benchmark moves beyond the SELECT-only focus of prior work (Table 1) and introduces a three-part ambiguity taxonomy (superficial, knowledge with chain-breaking, environmental) in Section 3.2. The state-dependent follow-up sub-tasks require models to reason over modified database states, adding realism absent in prior benchmarks.

- **High annotation quality.** Inter-annotator agreement of 93.33% (Table 1) from 12 expert annotators through a multi-stage selection process demonstrates systematic quality control.

- **Benchmark enables diagnostic analyses impossible in static settings.** The Memory Grafting experiment (Figure 5) and ITS analysis (Figure 4) leverage the dynamic interaction framework to isolate interaction skill from SQL generation skill — an analytic capability no prior text-to-SQL benchmark provides.

## Weaknesses

### Fatal
None.

### Major

- **The Interaction Test-Time Scaling (ITS) claim contradicts the presented data.** The Introduction (line 36) states: *"We also observe Interaction Test-time Scaling (ITS), where performance improves monotonically with additional interaction opportunities across multiple models."* However, Figure 4's caption explicitly states: *"In c-Interact mode, performance generally increases with patience, while in a-Interact mode, it remains relatively flat or slightly decreases."* The paper's own figure description contradicts the monotonicity claim. The ITS Law definition in Section 5.2 (matching/surpassing single-turn performance) is also a weaker statement than "monotonic improvement," creating internal inconsistency. The more interesting finding — the *divergence* between modes (c-Interact benefits from more turns, a-Interact does not) — is underanalyzed while the unsupported monotonicity claim is foregrounded. This overclaim weakens the paper's analytical credibility.

### Minor

- **Memory Grafting experiment is underdetermined.** Providing GPT-5 with other models' *successful* interaction histories gives it both a communication pattern AND the resolved ambiguity content. The performance improvement (13.8% → 20.5%) could reflect the oracle effect (receiving correct information) rather than improved communication skills. The paper's conclusion — *"a more effective communication schema is required"* — is reasonable but would be strengthened by controls: (a) failed interaction histories (does improvement reverse?), (b) GPT-5's own successful histories (can it learn from itself?), or (c) an analysis of whether GPT-5's generated questions improve under grafting.

- **Realism-controllability trade-off not acknowledged.** The paper frames its contribution as restoring "high-fidelity realism" (Abstract) but the function-driven simulator is explicitly designed for *controllability* — mapping queries to exactly three pre-defined actions derived from pre-annotated templates. This is a legitimate design choice, but the framing conflates "controlled, cheat-proof evaluation" with "realistic interaction." A real user can respond in ways the simulator cannot. The paper would benefit from explicitly stating: *"We sacrifice conversational breadth to achieve the control necessary for fair, reproducible evaluation."*

- **No dialog-based text-to-SQL baselines.** The evaluation tests only general-purpose LLMs with standard prompting. No existing dialog-based systems (e.g., methods designed for SParC or CoSQL) are adapted to the benchmark. Including even one simple dialogue-state-tracking baseline would strengthen the claim that the benchmark measures *interaction skill* specifically rather than general LLM competence.

- **Single runs without variance estimates.** The paper acknowledges "conducting single runs due to cost" (line 163). For a benchmark making comparative claims between models (e.g., ordering in Table 2), the lack of error bars or confidence intervals means the reliability of fine-grained model rankings cannot be assessed. Bootstrapping on task subsets or reporting variance on smaller models would address this.

### Trivial

- **Action cost calibration in Appendix J** could use sensitivity analysis — the *a*-Interact results are shaped by the relative costs of actions (e.g., "Get DB Schema" costs 2 while "Retrieve Knowledge" costs 1), and it's unclear how robust findings are to these choices.

## Nice-to-Haves

- **Task portability discussion.** The benchmark builds on LIVESQLBENCH. A brief discussion of how the annotation pipeline could be extended to new databases (and who maintains the infrastructure) would help potential adopters.
- **Qualitative analysis of *a*-Interact action sequences** under different budgets. The paper notes models favor trial-and-error over exploration (Section 5.2) but doesn't analyze *why* more budget hurts performance. A case study of action cascades would be illuminating.
- **Free-mode evaluation.** The paper mentions (Future Work, Section 8) that the budget-constrained *a*-Interact is a "stress-mode" setting. Including free-mode results (even on the Lite set) would help distinguish resource-constrained behavior from natural interaction strategy.

## Removed Points

These points were surfaced by reviewers or the strength finder but removed per the filtering rules:

1. **"Absence of specialized interaction baselines weakens the validation of the benchmark"** — This is kept in Minor but was softened from the harsh critic's framing as a "critical issue." Benchmark papers typically test general models; including specialized baselines is a nice-to-have, not a requirement for validity.
2. **"The ITS analysis demonstrates monotonic performance improvement... confirms the benchmark measures interaction capability"** — Strength Finder's claim about ITS. Partially removed because the ITS law claim is contradicted by the data; kept as a strength about the *benchmark enabling* such analyses, not the validity of the claimed law.
3. **"Missing related works"** — Removed per instructions (DO NOT mention missing related works).
4. **"Writing quality / presentation"** — Removed per instructions.
5. **"Reproducibility concern about undisclosed hyperparameters"** — Removed per instructions (trivial implementation details).

## Novel Insights

The most novel observation emerging from the review process is not in the paper's analytical claims but in its data: the *reversal* of model rankings between *c*-Interact and *a*-Interact (GPT-5 goes from worst to best) is a striking finding that deserves deeper investigation than the paper currently provides. This suggests that interaction mode is a first-order design decision that interacts with model-specific inductive biases — a finding that, if systematically explored, could meaningfully inform how practitioners deploy LLMs for database tasks. The fact that no model exceeds ~30% SR despite strong single-turn SQL performance (models achieve 70%+ on BIRD) confirms the benchmark's difficulty, but the paper's attempt to explain *why* (ITS Law, communication deficits) overreaches the evidence.

## Suggestions

1. **Reframe the ITS finding.** Remove the "monotonic" claim from the Introduction. Instead, present the *divergence* between *c*-Interact (improves with turns) and *a*-Interact (doesn't) as the core finding — it is more interesting, better supported, and genuinely novel.
2. **Acknowledge the realism-controllability trade-off explicitly** in Section 3.3. Replace "high-fidelity" framing with "controlled, reproducible, and cheat-proof evaluation" to inoculate against a predictable critique.
3. **Add control conditions to Memory Grafting.** Provide GPT-5 with failed interaction histories or its own successful histories to isolate whether the benefit comes from communication patterns or resolved-ambiguity content.
4. **Report confidence intervals** on the Lite set (300 tasks, cheaper to evaluate) to give readers a sense of ranking reliability, even if full-set single runs remain the primary results.
5. **Qualitatively analyze *a*-Interact failures.** The flat/decreasing performance with more budget is the paper's most surprising result — a small case study of agent action sequences would be far more valuable than the current ITS framing.

## Score and Decision

**Round-1 bracket:** 4.0–6.5 (based on topic-band and weakness-anchored queries). The low-band anchors (DataSciBench 3.20, DB-GPT-Hub 3.75, TrustSQL 4.00) failed at validation quality, novelty, or overclaiming. BIRD-INTERACT exceeds them on validation and novelty but shares the overclaiming failure mode (ITS "Law").

**Round-2 narrowing:** Queries within (4.5, 6.5) returned method papers (CHASE-SQL 6.25, ROUTE 6.25) and SQL-GEN (5.67). These are method contributions, not benchmarks, so direct comparison is limited. The narrowed bracket (4.5–5.5) reflects that BIRD-INTERACT's core benchmark is clearly a genuine contribution (above 4.0), but the analytical overclaims and minor gaps prevent it from reaching the 6+ level where a paper would have both strong contributions and rigorous analytical framing.

**Final score:** 5.0 — The paper makes a solid, well-validated benchmark contribution that fills a genuine gap. The function-driven simulator and dual evaluation settings are well-designed and validated. However, the ITS overclaim (a direct contradiction between the Introduction's monotonicity assertion and Figure 4) is a meaningful flaw in the analytical narrative that prevents a higher score, and several minor issues (Memory Grafting underdetermination, realism framing, no variance estimates) accumulate.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>