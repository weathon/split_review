Now I have sufficient calibration data. Let me write the final review.

## Summary

BIRD-INTERACT introduces a multi-turn, dynamic text-to-SQL benchmark built on LIVESQLBENCH that addresses limitations of prior benchmarks: static conversation histories and SELECT-only task scope. The key contributions are (1) a function-driven user simulator designed to prevent ground-truth leakage, with strong validation evidence; (2) two evaluation settings (c-Interact protocol-guided and a-Interact agentic); and (3) 900 tasks covering the full CRUD spectrum with injected ambiguities requiring clarification. The paper evaluates 7 LLMs and finds that SOTA models achieve only 8–17% success rates, with interesting interaction-mode-specific inversion patterns.

## Strengths

- **Function-driven user simulator with concrete reliability gains (Section 6, Figure 6, Table 3).** The paper identifies a genuine flaw in prior LLM-based simulators — ground-truth leakage — and introduces a two-stage function-driven approach that constrains responses to three symbolic actions (AMB, LOC, UNA). The USERSIM-GUARD evaluation (2,100 labeled questions) shows a 2.7% failure rate vs. up to 67.4% for baselines. The human alignment correlation study (100 tasks with human experts) shows improvement from r=0.61 (p=0.14, non-significant) to r=0.84 (p=0.02, significant). This is direct, measured evidence of improved evaluation integrity.

- **Memory grafting experiment cleanly isolates interaction skill from SQL generation ability (Section 5.2, Figure 5).** Replacing GPT-5's own ambiguity-resolution history with histories from Qwen-3-Coder and O3-mini, while keeping GPT-5's SQL generation, lifts success rate from 13.8% to 18.8–20.5%. This is a genuinely novel experimental design that demonstrates that communication effectiveness and SQL generation are separable capabilities — a finding that no single-turn benchmark could surface.

- **Dual evaluation settings reveal non-obvious, model-specific interaction behavior (Table 2).** GPT-5 ranks worst among 7 models in c-Interact (14.50% SR) but best in a-Interact (29.17% SR) — an inversion that a single-mode benchmark would miss entirely. This finding has practical implications for how models should be matched to deployment scenarios.

- **CRUD scope expansion is quantified and contrasted with prior work (Table 1).** 190 DM (data management) tasks out of 600 FULL tasks, covering Create/Update/Delete operations. The 93.33–93.50% inter-annotator agreement provides evidence of annotation consistency across the 12 recruited experts.

- **ITS experiment provides systematic evidence on the value of interaction turns (Section 5.2, Figure 4).** Varying user patience across 4 levels (0, 3, 5, 7) for 4 models in both settings shows monotonic improvement in c-Interact mode. Claude-3.7-Sonnet demonstrates clear scaling behavior.

## Weaknesses

### Fatal

None.

### Major

- **Single-run evaluations without any variance estimation (Section 5, line 163).** The paper states "conducting single runs due to cost" and all results in Table 2 (model rankings, per-category breakdowns, memory grafting, ITS analyses) derive from a single run per model per setting. While temperature=0 eliminates model-side stochasticity, the user simulator itself involves LLM calls (semantic parsing stage and response generation stage) whose variance is not characterized. Fine-grained differences in Table 2 — e.g., GPT-5 at 8.67% vs. Claude-Sonnet-3.7 at 8.33% on c-Interact overall SR — cannot be assessed for significance. Given that the paper draws comparative conclusions from these numbers (model rankings, mode effectiveness comparisons, ITS scaling claims), the evidential basis for fine-grained claims is weaker than the presentation implies. The benchmark *resource* is not invalidated, but numerical conclusions should be treated as suggestive.

### Minor

- **The "Idealized Performance" baseline is only shown as a dotted line in Figure 4; no numerical values are reported anywhere.** The ITS Law claim ("performance can match or surpass the idealized single-turn task") and the scaling analysis depend on this baseline, yet readers cannot quantitatively verify how far models are from idealized performance or which models satisfy the law.

- **The ambiguity injection methodology, while methodologically necessary, is closer to a controlled stress test than the "missing realism" claimed in the Abstract.** Ambiguities are pre-annotated with paired ground-truth SQL snippets; real-world ambiguity often arises from underspecification, conflicting requirements, or unstated assumptions that do not decompose neatly into annotated clarification points. The paper would benefit from more precise framing about what aspects of real-world interaction the benchmark captures well vs. poorly.

- **The user simulator's action space (AMB, LOC, UNA) is narrow — only three response modes.** Real users can offer alternative phrasings, express confusion, provide partial information, or change their minds. The validation in Section 6 demonstrates reliability and human *alignment* (correlation of task-level success rates) but does not demonstrate naturalistic *expressiveness*. For a benchmark claiming to model "dynamic interactions," the interaction space is quite constrained.

- **The ITS Law is proposed based on limited evidence.** Figure 4 shows that only Claude-3.7-Sonnet exhibits clear monotonic scaling in c-Interact; other models show mixed patterns. Claiming a "law" from one clear instance is premature.

- **The user simulator's own stochasticity is not discussed.** The simulator uses LLMs internally (semantic parser and response generator), which could introduce variance across runs even with temperature=0. This is relevant to the single-run concern above but is not addressed.

- **Memory grafting interpretation could be sharpened.** The experiment shows GPT-5 benefits from better interaction histories, but does not isolate whether the deficiency is in *communication per se*, question-asking *strategy*, or interaction *planning*. The paper attributes it broadly to "interactive communication abilities" (line 191).

- **The Avg. Cost column in Table 2 is not discussed in the text.** Unexplained variation — Claude-Sonnet-4 at $0.29 vs. O3-Mini at $0.07 in c-Interact — could illuminate practical deployability but is left for the reader to interpret.

### Trivial

None.

## Nice-to-Haves

- Report the idealized single-turn baseline success rates numerically (in a table alongside Figure 4).
- Add bootstrapped confidence intervals (e.g., sub-sampling across tasks) for main results.
- Break down user simulator response type proportions (how often AMB vs. LOC vs. UNA is triggered in practice).
- Specify the a-Interact scaffold/prompting strategy used for reported results (referenced as Appendix J.2, which was stripped).
- Discuss the user simulator's own LLM temperature and potential stochasticity.

## Removed Points

These points were removed from the inputs; treat them with caution if re-introducing.

- **"Reward weighting scheme not in main text"** (Harsh Critic): The paper explicitly states at line 173: "the reward structure allocating 70% to the primary sub-task and 30% to follow-up sub-tasks." This is factually incorrect; REMOVED.
- **"Distinct Test Cases count suggests low diversity"** (Harsh Critic): The paper reports 135/191 distinct test cases for LITE/FULL, but drawing a conclusion about low diversity without analyzing test case distribution across tasks is speculative; REMOVED.
- **"Budget awareness artificially influences behavior"** (Harsh Critic): The paper acknowledges this is intentional stress-testing design (Section 4, line 109: "stress-testing... to assess the system's ability to ask the right questions and plan effectively"); REMOVED as it is a design feature, not a weakness.
- **"a-Interact scaffold not specified"** (Harsh Critic): The paper references Appendix J.2 for scaffold details (stripped from parser). Downgraded to nice-to-have since the appendix likely contains this information.

## Novel Insights

The memory grafting experiment is the most genuinely novel methodological insight across the reviews — it provides a clean causal identification strategy for disentangling interaction skill from SQL generation skill that could be applied broadly in interactive benchmarks. The finding that GPT-5 inverts from worst to best across c-Interact and a-Interact is a non-obvious result that challenges the assumption that stronger models are uniformly better across interaction paradigms. Together, these findings suggest that what matters most for interactive text-to-SQL is not just SQL generation capability but the *match between interaction paradigm and model-specific strengths*.

## Suggestions

- Add bootstrapped confidence intervals to Table 2 by sub-sampling across tasks (this addresses the single-run concern without re-running the full evaluation).
- Report the idealized single-turn baseline as numerical values in a table to support the ITS Law claim.
- Include a limitations paragraph explicitly discussing the trade-off between controlled ambiguity injection and naturalistic interaction, and characterize what BIRD-INTERACT measures well vs. what it does not.
- Add a brief discussion of the cost variation in Table 2 to help readers interpret practical deployability.
- For the ITS Law, either provide additional evidence across more models or soften the claim to a "scaling pattern observed in some models."

## Score and Decision

**Calibration Report:**

*Round 1 (Bracketing):*
- Weak band (<3.5): Retrieved DB-GPT-Hub (3.75), TrustSQL (4.0) — both text-to-SQL benchmark papers with significant weaknesses
- Middle band (3.5–7.5): Retrieved τ-bench (6.50), CHASE-SQL (6.25), LiveCodeBench (6.25), HoloBench (6.25)
- Strong band (>7.5): Retrieved Spider 2.0 (8.0) — a very strong benchmark paper with real enterprise databases, no major weaknesses

*Round 1 bracket:* 5.0–7.0. BIRD-INTERACT is clearly stronger than TrustSQL (4.0) and DB-GPT-Hub (3.75), but substantially weaker than Spider 2.0 (8.0).

*Round 2 (Narrowing inside bracket):*
- τ-bench (6.50): Most directly comparable — both have user simulators, dynamic interactions, tool-using agents. τ-bench has no single-run issue but its simulator validation is less thorough. BIRD-INTERACT has stronger simulator validation (USERSIM-GUARD with 2,100 questions, significant human alignment) but has the single-run weakness. **Comparison: BIRD-INTERACT is slightly weaker than τ-bench, primarily due to the single-run issue.**
- LiveCodeBench (6.25): Benchmark paper criticized for limited novelty (dynamic benchmarking not new). BIRD-INTERACT's contributions (function-driven simulator, dual evaluation, memory grafting) are more novel. **Comparison: BIRD-INTERACT is comparable to LiveCodeBench.**
- CHASE-SQL (6.25): Method paper, not benchmark. **Comparison: Not directly comparable in genre.**
- HoloBench (6.25): Database operations benchmark. **Comparison: Comparable quality.**

*Final calibration:* The paper is in the 5.5–6.5 range. Comparing against τ-bench (6.50) is the sharpest anchor: BIRD-INTERACT has stronger simulator validation but has the single-run weakness. This places it slightly below τ-bench. Score = 6.0.

**Decision: Accept**

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>