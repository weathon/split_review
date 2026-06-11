## Summary
BIRD-INTERACT is a dynamic interactive text-to-SQL benchmark of 900 tasks (FULL=600, LITE=300) spanning the full CRUD spectrum across BI and DM use cases. Its core contributions are (i) a two-stage function-driven user simulator that maps clarification requests to symbolic actions (AMB/LOC/UNA) to curb ground-truth leakage, (ii) two evaluation protocols (c-Interact and a-Interact) with budget-constrained awareness, and (iii) an empirical study of 7 frontier LLMs including memory-grafting and Interaction Test-Time Scaling (ITS) analyses.

## Strengths
- **Function-driven simulator with concrete validation.** USERSIM-GUARD shows the UNA-failure rate dropping from 67.4% → 2.7% (Fig. 6); human-alignment Pearson rises from 0.61 to 0.84 (Table 3). This is a meaningful methodological advance over prior LLM-as-user simulators.
- **Memory-grafting experiment is a clean causal probe.** Providing GPT-5 with other models' interaction histories raises its SR from 13.8% → 18.8–20.5% (Fig. 5), dissociating communication strategy from raw SQL generation — a non-obvious, practically useful finding.
- **Real scope extension beyond prior multi-turn SQL benchmarks.** Full CRUD coverage, executable test cases, BI vs DM split, and state-dependent follow-up sub-tasks (Sec. 3.2) genuinely go past COSQL/SPaRC-style static transcripts.
- **The c-Interact vs a-Interact ranking inversion (GPT-5 last → first; O3-Mini first → mid; Table 2) is a substantively informative cross-paradigm finding for benchmark design.**

## Weaknesses

### Fatal
None.

### Major
- **Headline analytical claims depend on small deltas with no variance reporting.** §5 states "single runs due to cost" at T=0. Memory-grafting deltas (~5–7pp; Fig. 5) and ITS curves (Fig. 4) rest on margins plausibly within run-to-run noise — even at T=0 the simulator and tool calls introduce stochasticity. A small seed study on LITE for top models would convert several "interesting deltas" into defensible findings.
- **"Interaction Mode Emerged as the Decisive Factor" (§5.1) is broader than the evidence.** The two settings differ simultaneously in protocol, action space, prompt structure, and budget formula (τ_clar = m_amb+λ_pat vs B = 6+2m_amb+2λ_pat). Without an ablation that holds budget/information access constant and varies only the scaffolding, the cross-setting ranking inversion cannot be causally attributed to interaction paradigm.

### Minor
- **"ITS Law" is overclaimed.** Fig. 4 itself shows several model/setting cells are flat or slightly decreasing; only Claude-3.7-Sonnet in c-Interact exhibits the cited monotonic scaling. Naming a single-model regularity a "Law" overstates the pattern.
- **Hard termination on q₁ failure (§4.1) conflates capabilities in Table 2.** Follow-up SR is conditional on q₁ success but reported as if marginal. Reporting q₂ SR conditional on q₁ pass would let readers separate generation from interaction skill — precisely the distinction the paper wants to surface.
- **Budget constants are not motivated or sensitivity-tested.** B_base=6, the 2× multiplier on a-Interact relative to c-Interact, and the 70/30 reward split are introduced without justification; the 2× multiplier could itself drive part of the ranking inversion.
- **Memory-grafting controls are limited.** Only two donor models; upper-bound (GT-derived clarifications) and lower-bound (failed/weaker-model histories) baselines would convert §5.2 from suggestive to compelling.
- **BI vs DM difficulty interpretation is potentially confounded.** Table 1 shows DM has substantially fewer distinct test cases; the claimed difficulty gap may partly reflect diversity rather than reasoning load.
- **Downstream simulator failure is unbounded.** USERSIM-GUARD validates the simulator on a static labeled set; parsing errors on actual benchmark trajectories are not measured, and could differentially advantage/penalize models that phrase clarifications differently.

### Trivial
None.

## Nice-to-Haves
- Conditional q₂|q₁ SR reported alongside marginal SR.
- Sensitivity sweeps over budget constants (B_base, the a-Interact multiplier, reward split).
- A direct baseline-simulator vs function-simulator comparison on the *benchmark itself* (not only USERSIM-GUARD) to quantify downstream SR shift.
- Soften "ITS Law" or extend across more models.

## Removed Points
These were flagged in inputs but pulled out — treat with caution:
- *"Inter-annotator agreement metric is not specified in the main text"* — details are deferred to the appendix that the parser stripped; not a true author error.
- *"0.84 vs 0.61 correlations have overlapping confidence intervals"* — speculative without quantification; standard comparison at N=100 with reported p-values is acceptable.
- Generic "evidence is weak / comparisons may be unfair" sweeps from the harsh critic without specific anchors.

## Novel Insights
None beyond the paper's own contributions. The memory-grafting decomposition of generation vs. interaction capability is itself the paper's most novel insight.

## Suggestions
- Run ≥3 seeds on LITE for top-3 models; report variance for memory grafting and ITS.
- Add a matched-budget, matched-information c/a ablation isolating scaffold from setting.
- Add GT-clarification upper-bound and failed-history lower-bound controls to memory grafting.
- Report q₂ SR conditional on q₁ pass.
- Soften "ITS Law" framing or extend across models.

## Calibration

Round-1 anchors (bracketing):
- ReKWjKvkJE.md (3.40, weak) — text-to-SQL method paper, far weaker scope.
- Avg6hmtgHE.md (3.40, weak) — unrelated multi-entity QA, much weaker.
- lMW9d1AqC9.md (1.67, weak) — pseudo-scientific framing, not comparable.
- b1vVm6Ldrd.md (3.00, weak) — ToM benchmark, weaker execution.
- NmILZXKcOi.md (3.75) — DB-GPT-Hub benchmark, narrower than BIRD-INTERACT.
- CvGqMD5OtX.md (6.25) — CHASE-SQL method paper, accepted.
- BAglD6NGy0.md (6.25) — ROUTE, accepted text-to-SQL method.
- 7ZeoPg3eTA.md (4.00) — TrustSQL benchmark, narrower.
- WYdpjwKQma.md (5.00) — LAIA-SQL.
- XmProj9cPs.md (8.00) — Spider 2.0; comparable ambition but more scope/realism, slightly above BIRD-INTERACT.
- Q6a9W6kzv5.md (8.00), GGlpykXDCa.md (8.00), HnhNRrLPwm.md (8.00) — strong benchmark anchors in adjacent areas.

Round-1 bracket: **6 to 8**, given BIRD-INTERACT is clearly above mid-tier text-to-SQL method papers and roughly in the league of ambitious benchmarks like Spider 2.0 / PARTNR / WildBench but with single-seed and overclaim limitations.

Round-2 anchors (narrowing):
- JAMxRSXLFz.md (7.33) — Active Task Disambiguation; similar clarification/ambiguity theme; BIRD-INTERACT has a larger benchmark contribution but weaker analytical rigor.
- CvGqMD5OtX.md (6.25), BAglD6NGy0.md (6.25) — accepted text-to-SQL method papers; BIRD-INTERACT is a more ambitious benchmark contribution.
- T5QLRRHyL1.md (7.00) — PARTNR multi-agent benchmark; comparable in ambition; BIRD-INTERACT is more focused but with similar overclaim concerns.
- n6mLhaBahJ.md (6.75) — HAZARD simulator benchmark; similar tier.
- k5VHHgsRbi.md (6.80) — MME-RealWorld; comparable.
- MKEHCx25xp.md (7.33) — WildBench; comparable in benchmark contribution.

Round 2 narrows the bracket to **6.5–7.5**. BIRD-INTERACT's simulator+benchmark contribution and memory-grafting insight place it near PARTNR/WildBench (~7), while overclaim and single-seed pull it slightly below Spider 2.0 (8.0).

MY FINAL SCORE: <score>7</score>
MY FINAL DECISION: <decision>Accept</decision>