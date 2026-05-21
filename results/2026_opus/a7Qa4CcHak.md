Now I have a solid understanding of the paper. Let me proceed with calibration searches.Initial bracket: between **6 and 8.5**, with closest spiritual anchors being MLE-Bench (8.00) and Cybench (8.67) — both real-world task benchmarks with curated tasks, multi-model frontier evals, and high acceptance. The lower band (AgentBench/AgentQuest at 6.2-6.25) feels too low for a paper with this curation rigor and scope. Let me narrow.## Summary
Terminal-Bench is a curated benchmark of 89 hard, realistic terminal tasks, each with a containerized environment, oracle solution, and verification tests. The paper releases the dataset, the Harbor harness, and a neutral scaffold (Terminus 2), and reports a large-scale evaluation (16 models × 6 agents, 32,155 trials) showing the best system resolves ~63% of tasks, accompanied by trajectory-level and command-level failure taxonomies.

## Strengths
- **Rigorous multi-phase audit pipeline.** Section 2.3 and Figure 3 specify automated CI checks (oracle passes, dummy-solution fails), an adversarial exploit pass, contributor checklists, and three independent human reviewers averaging ~3 reviewer-hours per task. This is materially more thorough than most agent benchmark construction in the literature.
- **Validated human-vs-empirical difficulty alignment.** Figure 6 reports r = 0.436 (p < 0.001) between human-predicted and empirical (Terminus 2) difficulty, with 93.3% of human-hard tasks also empirically hard, providing concrete evidence the curation captures genuinely difficult problems.
- **Detailed failure analysis with measured agreement.** Sections 4.3–4.4 give both trajectory-level (Cohen's κ = 0.93 on 20-trial calibration; 90% judge–human agreement on 120 traces) and command-level (92.4% agreement on 66 pairs) taxonomies. The finding that "command not found" alone accounts for 24.1% of command failures is a concrete, actionable diagnostic.
- **Broad evaluation scope.** Section 3 reports 32,155 trials across 16 models × 6 agents, with first-party APIs for closed models, a neutral scaffold (Terminus 2) for fair model comparison, and a Pareto cost–performance frontier (Figure 5).
- **Diverse, long-horizon task mix.** Table 1 documents tasks ranging from <1 hour to >1 week of expert time (including fix-ocaml-gc at ~24h expert / ~240h junior), and Figure 4 shows 16 categories with no single one dominating — broader than CTF-only or Kaggle-only contemporaries.

## Weaknesses

### Fatal
None.

### Major
- **Statistical discipline does not match what 89 tasks can adjudicate.** Section 4 makes paired ordering claims ("model selection is usually more important than agent scaffold," 52% vs. 17% gaps) from differences between paired model–scaffold combinations without reporting paired bootstrap CIs on the differences. Several frontier-model orderings in Figure 1 (Opus 4.5 vs. Gemini 3 Pro at 58% vs. 57%; Gemini 3 Flash vs. GPT-5 at 52% vs. 50%) sit inside the per-model 95% CIs already shown. The headline claims would be defensible with task-paired bootstrap intervals on the differences, or rank-stability under resampling; without them, the prose overstates what the benchmark can adjudicate. The 52%-vs-12% Codex CLI gap (GPT-5.2 vs. GPT-5-Nano) is real, but the more interesting close comparisons are not properly qualified.

### Minor
- **Selection process from 229 → 89 is under-described.** Section 2.2 says tasks were selected based on "the author's difficulty assessment and a quality assessment," but does not report the distribution of rejection reasons or how the difficulty threshold was applied. This matters because §4.2's "empirical difficulty" is derived from Terminus 2 pass-rates on the same selected set; if selection partially filtered on difficulty, the reported correlation with human difficulty (r = 0.436) is partially mechanical. A short paragraph on rejection reasons and a note acknowledging this circularity would close the loop.
- **Best-of-scaffold presentation cuts against the model-vs-scaffold attribution claim.** Figure 1 reports "the agent scaffold that maximizes performance" per model (caption), then §4 leans on this figure to argue model > scaffold. A uniform-scaffold leaderboard in the main text (e.g., all models on Terminus 2) alongside the best-of view would make the decomposition rigorous; the matrix exists, but the summary obscures rather than supports the claim.
- **Per-category claims rest on very few items.** Figure 4 shows 11 of 16 categories with ≤5 tasks (Personal Assistant, Optimization, Video Processing, Data Querying each = 1). The paper does not lean heavily on per-category numbers, but readers will; a sentence flagging the per-category sample sizes would be appropriate.
- **Contamination handling for audit runs is not made concrete.** §5 acknowledges the canary string and defers a private test set. Given that Phase 2 of the audit pipeline (Figure 3) runs Terminus + frontier models on every PR and persists trajectories for replay, a sentence on whether provider opt-out flags were used during audit runs would strengthen the contamination discussion.
- **Reported correlations should include coefficients.** §4.1 asserts "essentially no correlation between turns per trial and success" and that token count "does not necessarily correlate with better performance"; with 21 model–agent combinations the actual coefficients and CIs should be reported, not stated as bare findings.
- **Abstract phrasing.** "Frontier models and agents score less than 65%" essentially rounds the top score up; "the best system resolves about 63% of tasks" would be more precise.

### Trivial
- The "in contrast to the synthetic environments used by other benchmarks" framing in §6 is sharper than needed — the real contrast is terminal-centric, outcome-driven, expert-authored tasks, which is the case already supported.
- Cost numbers in Figure 5 would be clearer if specified as best-of-5 vs. mean-of-5 and tied to the API price points used.

## Nice-to-Haves
- A small test–retest variance study (e.g., re-running the top three models on all 89 tasks at two times) to quantify noise from internet access and package fetching.
- An explicit longitudinal-use plan: held-out shard, rotation of tasks, or contamination-resistance strategy as the benchmark is rerun against newer models.
- Inter-reviewer agreement statistics for human task verification (the paper reports LLM-judge calibration but not reviewer agreement during the audit).
- A reasoning-effort sensitivity sweep for at least one model family (since Kimi K2 Thinking vs. Instruct re-orderings are consistent with effort being a real moderator).
- A brief appendix-pointer summary of which 26 benchmarks were ported into the Terminal-Bench format and what was lost in conversion (§2.1, fn. 1).

## Removed Points
These points are flagged to be removed; treat them with caution.

- *"Headline-claim power vs. dataset size could invalidate ordering"* (from harsh critic) — retained in Major above but stripped of the speculative quantification that the ±10-point CI claim was a property the paper failed to acknowledge: the paper *does* show 95% CIs in Figure 1. Only the discussion's overreach beyond those CIs is the real issue.
- *"Trajectory leakage during audit is a structural concern"* — demoted to Minor. The paper acknowledges contamination openly in §5; the harsh critic's escalation to structural depends on what provider-side logging actually does, which is not knowable from the paper.
- *Per-category numbers being unreliable* — demoted to Minor since the paper itself does not anchor headline claims on those numbers.
- *Strength: "addresses an important problem / terminal is ubiquitous"* (generic framing strength) — removed as low-information sycophancy; the contribution stands on artifact quality, not on importance-of-problem.
- *Strength: "16 categories ensure breadth"* — kept (Figure 4) but merged into the diverse-task-mix strength above; the bare category count is less informative than the long-horizon distribution in Table 1.

## Novel Insights
None beyond the paper's own contributions. The most striking empirical finding — 24.1% of command failures are "command not found," concentrated in invocation rather than reasoning — is the paper's own observation in §4.4 and deserves to be surfaced more prominently than the current placement.

## Suggestions
- Replace per-model independent CIs in Figure 1 with task-paired bootstrap CIs on the *differences* between adjacent models, or report rank-stability under resampling, to qualify close orderings.
- Add a uniform-scaffold leaderboard (all models on Terminus 2) as a primary figure alongside the best-of-scaffold view, so the model-vs-scaffold decomposition is visibly supported.
- Add a one-paragraph breakdown of why 140 of 229 contributed tasks were rejected (broken / too easy / duplicated / too narrow), and acknowledge that §4.2's empirical-difficulty correlation is partially shaped by the selection criterion.
- State in §5 whether provider opt-out / no-training flags were used during the Phase-2 audit runs that persisted trajectories.
- Reword the abstract from "less than 65%" to "the best system resolves about 63% of tasks."
- Surface the "command not found = 24.1%" finding in the introduction or conclusion as an actionable signal for scaffold designers.

---

### Evaluation Axes
- **Originality:** Moderate — incremental over SWE-Bench/Cybench/MLE-Bench, but the terminal-centric, outcome-driven, broadly-categorized framing is distinct and well-motivated.
- **Importance of question:** High — terminal agents now drive substantial real production usage; a hard, audited benchmark is timely.
- **Support for claims:** Mostly strong, but the leaderboard ordering and model-vs-scaffold prose claims outrun what 89-task evaluation rigorously supports.
- **Soundness of experiments:** Strong overall — 32,155 trials, ≥5 seeds, calibrated LLM judges with reported agreement, neutral scaffold for fair model comparison.
- **Clarity:** High; the audit pipeline figure and tables are well-organized.
- **Value to research community:** High — the released artifact (dataset + Harbor + Terminus 2 + error taxonomies) is the kind of infrastructure others will use.

### Calibration Anchors

Round 1 retrieved (one call, three bracketed queries):
- `koza5fePTs.md` — *Planning Capabilities of LLMs*, avg 2.00 (Round 1, weak band). Far weaker than the paper under review — small targeted benchmark, narrow scope, rejected.
- `nE3flbe88p.md` — *TeamCraft*, avg 3.25 (Round 1, weak band). Multi-agent Minecraft benchmark; less rigorously curated, narrower domain.
- `BltaWJZMeR.md` — *DataSciBench*, avg 3.20 (Round 1, weak band). Data-science LLM benchmark with semi-automated GT, weaker curation than Terminal-Bench.
- `oWm80iR1m9.md` — *SOP-Agent*, avg 3.00 (Round 1, weak band). Not a benchmark paper per se; off-topic.
- `zAdUB0aCTQ.md` — *AgentBench*, avg 6.20 (Round 1, middle band). Comparable in framing (LLM-as-agents on 8 environments) but less curated and older; Terminal-Bench is clearly more rigorous.
- `fp6t3F669F.md` — *AgentQuest*, avg 6.25 (Round 1, middle band). Long-horizon interactive games; lighter curation.
- `AC5n7xHuR1.md` — *AgentHarm*, avg 6.75 (Round 1, middle band). 110 harmful agent tasks; comparable scope but different topic.
- `T5QLRRHyL1.md` — *PARTNR*, avg 7.00 (Round 1, middle band). Large-scale embodied benchmark with simulation-in-loop verification.
- `6s5uXNWGIh.md` — *MLE-Bench*, avg 8.00 (Round 1, strong band; read in full). 75 Kaggle competitions, comprehensive scaffold/model eval, contamination analysis. The strongest direct analogue: similar rigor, similar audit-style curation, similar multi-model eval. Terminal-Bench is broader in task categories but narrower in number of tasks; rigor is comparable.
- `tc90LV0yRL.md` — *Cybench*, avg 8.67 (Round 1, strong band; read in full). 40 CTF tasks, careful curation, first-solve-time as objective difficulty, multi-model + multi-scaffold eval. Methodologically very similar to Terminal-Bench, but narrower domain. Terminal-Bench has broader scope and a more detailed failure taxonomy; Cybench has a sharper, more measurable difficulty proxy.
- `Q6a9W6kzv5.md` — *PhysBench*, avg 8.00 (Round 1, strong band). VLM physical-world benchmark; off-topic.
- `XmProj9cPs.md` — *Spider 2.0*, avg 8.00 (Round 1, strong band). Real-world text-to-SQL, 632 problems; comparable in real-world ambition.

Round 1 bracket: **7.5–8.5**, anchored by MLE-Bench (8.0) and Cybench (8.67) as the most directly comparable curated, frontier-evaluation, real-environment benchmarks. The 6.2–6.7 anchors (AgentBench, AgentQuest) are clearly weaker in curation rigor and modern evaluation breadth than Terminal-Bench.

Round 2 retrieved (one call, three narrowing queries):
- `VTF8yNQM66.md` — *SWE-bench*, avg 6.25 (Round 2; read in full). 2,294 real GitHub issues; the foundational SWE benchmark. Larger N but older, narrower scope, less detailed error analysis. Terminal-Bench has comparable rigor with broader task types and a richer evaluation matrix.
- `MMwaQEVsAg.md` — *Commit0*, avg 6.67 (Round 2). Library generation from scratch; comparable interactive-environment philosophy, smaller eval scope than Terminal-Bench.
- `chfJJYC3iL.md` — *LiveCodeBench*, avg 6.25 (Round 2). Contamination-free code eval over time; complementary but narrower in agentic scope.
- `JbOsMrwjZ3.md` — *BioCoder*, avg 6.25 (Round 2). Bioinformatics code benchmark; narrower domain.
- `6s5uXNWGIh.md` — *MLE-Bench*, avg 8.00 (Round 2 re-hit).
- `Q6a9W6kzv5.md` — *PhysBench*, avg 8.00 (Round 2 re-hit).
- `tc90LV0yRL.md` — *Cybench*, avg 8.67 (Round 2 re-hit).
- `KsUh8MMFKQ.md` — *Thin-Shell Object Manipulations*, avg 8.00 (Round 2). Off-topic.
- `sf1u3vTRjm.md` — *ML-Bench*, avg 5.75 (Round 2). Repo-level ML code generation, rejected; weaker curation than Terminal-Bench.

Round 2 places Terminal-Bench above the 6.0–6.7 anchors (SWE-bench, Commit0, LiveCodeBench, AgentBench): those papers are foundational but Terminal-Bench has a more disciplined curation pipeline, much broader multi-model evaluation, and richer error taxonomies. It is most directly comparable to MLE-Bench (8.0) — similar curation effort, similar multi-model rigor, similar scope of evaluation. It does not quite reach Cybench's level of methodological novelty (first-solve-time as a measurable difficulty proxy is sharper than empirical-difficulty thresholds), and its statistical-discipline gaps on 89 tasks pull it slightly below 8.5. Final placement: ~8.0, comparable to MLE-Bench and slightly under Cybench.

## Score and Decision

MY FINAL SCORE: <score>8.0</score>
MY FINAL DECISION: <decision>Accept</decision>