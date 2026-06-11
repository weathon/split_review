Now let me write the final review with the calibrated score.

## Summary

BIRD-INTERACT is a benchmark for evaluating interactive, multi-turn text-to-SQL systems that addresses two key gaps in prior work: (1) existing multi-turn benchmarks use static conversation transcripts rather than model-specific dynamic interaction trajectories, and (2) they are limited to SELECT-only queries. The benchmark constructs 900 tasks across full CRUD operations, injects controlled ambiguities requiring clarification, provides a function-driven user simulator that demonstrably reduces ground-truth leakage, and offers two evaluation settings (c-Interact and a-Interact). Seven LLMs are evaluated, revealing that even the strongest models achieve only 8.67–17.00% end-to-end success on the full set.

## Strengths

1. **Function-driven user simulator with strong, multi-faceted validation.** The two-stage approach (semantic parser → constrained AMB/LOC/UNA actions) directly addresses the ground-truth leakage problem that plagues prior LLM-based simulators. Evaluation on USERSIM-GUARD (2,100 labeled questions) shows failure rates drop from up to 67.4% (baseline) to 2.7% (Figure 6). Human-alignment correlations (Table 3) improve from 0.54–0.61 (not significant) to 0.79–0.84 (p<0.05), providing quantitative evidence that the simulator reflects real interaction patterns—a validity check that few benchmark papers in this area provide.

2. **Dual evaluation settings that reveal model-specific interaction-mode preferences.** The c-Interact vs. a-Interact distinction is well-motivated and empirically informative: GPT-5 is the worst model in c-Interact (14.50% SR) but the best in a-Interact (29.17% SR). The memory grafting experiment (Figure 5) causally attributes GPT-5's c-Interact weakness to communication strategy rather than SQL generation capability, validating that the two settings measure genuinely distinct skill dimensions.

3. **Full CRUD task scope is a meaningful expansion.** 190 of 600 tasks in the FULL set (31.7%) cover data management operations (INSERT, UPDATE, DELETE, schema modifications)—substantially broader than the SELECT-only scope of COSQL, SParC, and LEARN-TO-CLARIFY. Results confirm BI and DM tasks pose systematically different challenges (DM success rates are consistently higher across all models), validating the expanded scope.

4. **State dependency between sub-tasks.** Follow-up sub-tasks depend on database states modified by preceding queries, forcing models to reason about evolving state—a realistic requirement absent from prior multi-turn datasets.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **"ITS Law" framing overstates the evidence.** Section 5.2 defines an "ITS Law" where a model satisfies the law if, with enough turns, its performance can match or surpass the idealized single-turn task. However, Figure 4 shows at most one model (Claude-3.7-Sonnet in c-Interact) exhibiting a clear upward trend, and even that model does not convincingly surpass the idealized baseline within the shown patience range. In a-Interact, performance is flat or declining for all models. Calling this a "law" implies a generality the data do not support; "interaction test-time scaling" as an empirical observation for specific models and settings is more appropriate.

2. **Follow-up sub-tasks are always limited to n=2.** Every task has exactly one priority sub-task and one follow-up sub-task (line 46: "in our implementation, each task consists of two related sub-tasks (n=2)"). While a practical design choice, this means BIRD-INTERACT evaluates a single follow-up rather than extended multi-turn reasoning spanning many rounds. The limitation should be more clearly acknowledged as a scope constraint rather than implied as comprehensive multi-turn evaluation.

3. **Synthetic ambiguity injection raises ecological validity questions.** Ambiguities are systematically injected and paired with clean clarification sources, enabling controlled evaluation. However, manufactured ambiguities may differ from naturally occurring ones—real ambiguities tend to be messier, involve implicit assumptions, and lack clean resolution paths. The human alignment study (n=100 tasks) partially addresses this by showing rank-order consistency, but does not validate whether the *kinds* of ambiguities match real-world ones. A more explicit discussion of this trade-off would strengthen the paper's credibility.

4. **Single-run evaluations limit confidence in fine-grained comparisons.** Results are based on a single run per model per setting (temperature=0). While this is standard practice in text-to-SQL benchmarking, several comparative claims depend on small gaps (e.g., GPT-5 at 14.50% vs. Claude-Sonnet-3.7 at 18.00% in c-Interact priority SR). Adding bootstrap confidence intervals (resampling over tasks) would increase confidence in these comparisons without requiring additional API runs.

5. **No qualitative analysis of failure modes.** The paper reports *that* models achieve low success rates but provides little analysis of *how* they fail—e.g., do they fail to ask for clarification? ask the wrong questions? generate invalid SQL? struggle with state-dependent follow-ups? Such analysis would increase the benchmark's utility for guiding future research.

### Trivial
None.

## Nice-to-Haves
- Clarify how many of the 600 tasks are modifications of LIVESQLBENCH tasks versus entirely new tasks.
- Provide a brief explanation for why LITE has more ambiguities per task (5.16) than FULL (3.89), despite having cleaner databases.
- Show a few worked interaction examples beyond the high-level Figure 1 to give concrete sense of task difficulty.

## Removed Points
Points flagged for removal, treat with caution:
- Harsh critic's concern about budget formula constants (B_base=6, 2× multiplier): minor design detail; formulas are clearly stated and conceptually motivated. Not a substantive weakness.
- Harsh critic's concern about no task hardness stratification: reasonable suggestion but not a weakness of the current contribution.
- Strength finder's identification of "ITS analysis with formalized ITS Law" as a strength: this conflicts with verified weakness #1 (overclaimed framing). Per the rules, when strength and weakness disagree, the weakness wins.
- Harsh critic's criticism about single-run evaluations being a "serious evidential weakness": temperature=0 single-run evaluation is standard practice in the field. Demoted to minor weakness to acknowledge the comparative limitation without overstating it.

## Novel Insights
The most interesting novel observation is the interaction-mode dissociation revealed by the memory grafting experiment: GPT-5's poor c-Interact performance is causally attributable to communication strategy rather than SQL competence, since grafting other models' interaction histories onto GPT-5 substantially improves its success rate. This finding—that strong single-turn SQL generators can fail in interactive settings due to *how* they interact, not *what* they know—goes beyond a simple model ranking and points to a concrete research direction. The methodological implication is that the two evaluation settings are not interchangeable: c-Interact and a-Interact stress fundamentally different capabilities.

## Suggestions
1. Rename "ITS Law" to "Interaction Test-Time Scaling" and temper the claims to match the evidence (one model in one setting shows a trend).
2. Add bootstrap confidence intervals (resampling over tasks) to the main results in Table 2 to strengthen comparative claims without additional API runs.
3. Add a qualitative analysis of failure modes—a taxonomy with examples of common error patterns—to increase the benchmark's diagnostic utility.
4. Acknowledge the n=2 follow-up limitation and the synthetic ambiguity trade-off more explicitly in the main text.

## Calibration

**Round 1 (Bracketing).** Searched for papers on "interactive multi-turn text-to-SQL benchmark evaluation" across three score bands:
- Weak (<3.5): Retrieved DB-GPT-Hub (3.75) and TrustSQL (4.00) as most relevant — both clearly weaker than BIRD-INTERACT.
- Middle (3.5–7.5): Retrieved CHASE-SQL (6.25), ROUTE (6.25) — method papers not directly comparable.
- Strong (>7.5): Retrieved Spider 2.0 (8.00, unanimous 8s) — clearly stronger (real-world enterprise data, no major weaknesses noted).

**Round 2 (Narrowing).** Searched for "interactive text-to-SQL benchmark multi-turn evaluation LLM user simulator" within (4.5, 6.0) and (6.0, 8.0):
- MINT (6.75, scores 6/8/8/5): Broader scope (20 models, 8 datasets) but weaker simulator validation. BIRD-INTERACT is comparably strong with deeper domain focus and better simulator validation.
- τ-bench (6.50, scores 6/6/6/8): Similar benchmark paper with dynamic user-agent interaction; similar quality and similar weaknesses. BIRD-INTERACT has stronger simulator validation (USERSIM-GUARD + human alignment).
- MemSim (5.25, scores 5/5/5/6): Simulator benchmark but weaker overall.

**Bracket:** Round 1 bracket was 4–7. Round 2 narrowed this to approximately 6.0–6.75. BIRD-INTERACT is clearly above TrustSQL (4.00) and DB-GPT-Hub (3.75), is comparable to τ-bench (6.50) and slightly below MINT (6.75), and is clearly below Spider 2.0 (8.00).

**Anchors consulted:** Spider 2.0 (8.00, Round 1), TrustSQL (4.00, Round 1), DB-GPT-Hub (3.75, Round 1), MINT (6.75, Round 2), τ-bench (6.50, Round 2), MemSim (5.25, Round 2), DialSim (5.00, Round 2).

**Final score:** 6.5 — a solid benchmark paper with a genuine technical contribution (the function-driven simulator with strong validation), a few minor framing issues (ITS Law), and scope limitations (n=2 follow-ups, synthetic ambiguity) that do not invalidate the core contribution.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>