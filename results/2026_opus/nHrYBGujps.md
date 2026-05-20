Now I have enough calibration data. Let me write the final review.

## Calibration Summary

**Round 1 — Bracketing**
- Weak (<3.5): `Avg6hmtgHE.md` (3.4, multi-entity QA — unrelated topic but a reject); `lMW9d1AqC9.md` (1.67); `RuY1r1PDdQ.md` (3.0); `a2rSx6t4EV.md` (2.33). Far weaker than this paper.
- Middle (3.5–7.5): `roNSXZpUDN.md` τ-bench (6.5, **read in full** — most similar to BIRD-INTERACT, LLM-based user simulator, multi-turn agent dialogue); `W1x77vRucB.md` DialSim (5.0); `NmILZXKcOi.md` DB-GPT-Hub (3.75); `p97nsl3Fvq.md` LPE-SQL (4.0).
- Strong (>7.5): `6s5uXNWGIh.md` MLE-Bench (8.0); `Q6a9W6kzv5.md` PhysBench (8.0); `tc90LV0yRL.md` Cybench (8.67); `YrycTjllL0.md` BigCodeBench (9.0).

Bracket: 5.5–7.0. BIRD-INTERACT is clearly above the weak band; clearly below the BigCodeBench/MLE-Bench tier (which are transformative); sits closest to τ-bench.

**Round 2 — Narrowing**
- `CvGqMD5OtX.md` CHASE-SQL (6.25, text-to-SQL method, weaker analog); `WYdpjwKQma.md` LAIA-SQL (5.0 reject); `RaSLSUCKz0.md` SQL-GEN (5.67 reject); `BAglD6NGy0.md` ROUTE (6.25 accept).
- `zAdUB0aCTQ.md` AgentBench (6.2 accept); `n6mLhaBahJ.md` HAZARD (6.75 accept); `T5QLRRHyL1.md` PARTNR (7.0 accept); τ-bench again (6.5).
- `NUD03NBDOE.md` ActionReasoningBench (6.75); `fp6t3F669F.md` AgentQuest (6.25); `oKn9c6ytLx.md` WebArena (6.33).

τ-bench is the most direct comparator: also a benchmark with LLM-based user simulator, dynamic database state, multi-turn agent evaluation. BIRD-INTERACT has broader scope (CRUD vs SELECT, two protocols, larger annotation effort, novel function-driven simulator with documented leakage reduction, memory-grafting analysis), but it inherits similar concerns about simulator validity and single-run rankings. It sits at or slightly above τ-bench.

---

## Summary
BIRD-INTERACT is a benchmark for interactive text-to-SQL that converts the static LIVESQLBENCH suite into a dynamic, multi-turn evaluation with 900 tasks covering the full CRUD spectrum. The paper contributes (i) ambiguity injection and follow-up sub-task annotation pipelines, (ii) a two-stage function-driven user simulator that constrains responses through AMB/LOC/UNA actions to reduce ground-truth leakage, and (iii) two evaluation protocols (c-Interact, a-Interact) with budget-constrained awareness. Empirical analyses include Memory Grafting (isolating interaction skill from SQL skill) and Interaction Test-Time Scaling.

## Strengths
- **Function-driven simulator measurably reduces leakage.** On USERSIM-GUARD (Figure 6, Sec. 6), UNA failure rates drop from up to 67.4% (baseline) to 2.7%, while AMB/LOC stay near 90%. The mechanism (semantic-parsing the system's question into a constrained action, then generating the response) is reusable.
- **CRUD scope with state-dependent follow-ups.** Table 1 shows 190 DM tasks in FULL plus state dependency between sub-tasks (Sec. 3.2), genuinely extending beyond the SELECT-only norm of COSQL/SParC; 93.50% inter-annotator agreement.
- **Dual evaluation protocols expose model-specific tradeoffs.** Table 2 shows that the same model can rank top in a-Interact and bottom in c-Interact (e.g., GPT-5: 29.17% a-Interact priority vs 14.50% c-Interact priority), which is a non-trivial diagnostic property and motivates reporting both protocols.
- **Memory Grafting is a creative analytical probe.** Figure 5 / Sec. 5.2 show GPT-5's c-Interact SR moves from 13.8% → 18.8% (Qwen-3-Coder history) and 13.8% → 20.5% (O3-mini history), supporting the claim that the bottleneck is communication, not generation. (See weaknesses for caveats on its statistical strength.)
- **Interaction Test-Time Scaling.** Figure 4 demonstrates monotonic SR gains with patience for Claude-3.7-Sonnet in c-Interact approaching the idealized single-turn ceiling — a clean empirical statement of the ITS hypothesis.

## Weaknesses

### Fatal
None.

### Major
- **The budget formula leaks the annotated ambiguity count m_amb into the prompt.** Sec. 4.1 defines τ_clar = m_amb + λ_pat and Sec. 4.2 defines B = 6 + 2m_amb + 2λ_pat, while Sec. 4 explicitly states the system is told remaining budget ("budget-constrained awareness"). One of the skills the benchmark claims to measure — recognizing how many ambiguities to clarify — is partially handed to the model as a counting hint. The paper acknowledges only a future "free-mode" (Sec. 8) without reporting any results under a budget independent of m_amb. This conflates planning with bookkeeping in every reported number under stress mode, including the ITS curves in Figure 4 that are parameterized by λ_pat while still leaking m_amb. — Matters because the central thesis is about strategic interaction skill.
- **Headline rankings rest on single runs with thin margins.** Sec. 5 reports single runs "due to cost," yet the narrative in Sec. 5.1 ("Interaction Mode Emerged as the Decisive Factor") rides on small absolute gaps (e.g., a-Interact priority: GPT-5 29.17% vs Claude-Sonnet-4 27.83%; c-Interact priority: GPT-5 14.50% vs Gemini-2.5-Pro 25.00%). With an LLM-based simulator and N≈300 in the LITE subset where some analyses run, single-run rankings between adjacent models are not statistically supported. The benchmark itself is fine; the strong claims about which model "wins" in which mode are overclaimed.
- **Memory Grafting evidence is too thin for its causal claim.** Figure 5 reports per-task deltas of 5–7 absolute points from a single run, with no control where GPT-5 receives a *worse* model's history, a randomized/shuffled history, or its own history under a different seed. Without those controls, the conclusion that the deficit is specifically *communicative* (rather than a generic "more context helps" effect) is plausible but not established by this experiment. The mechanism is presented as a finding rather than as suggestive evidence.

### Minor
- **USERSIM-GUARD improvements are dominated by UNA.** Figure 6 shows AMB and LOC at ~90% parity for baseline and proposed simulators; the headline gain is on UNA (40%→90%+), which is precisely the category constructed alongside the proposed guard. The "reliability" framing in Sec. 6 is therefore narrower in practice than the prose suggests — primarily, the guard refuses leakage-eliciting questions and that works. Worth noting in the paper itself.
- **Alignment study is underpowered.** Table 3 reports Pearson 0.84 (p=0.02) vs 0.61 (p=0.14) over n=7 system models on n=100 tasks (Sec. 6). With n=7 the correlation gap has wide confidence intervals; the rank swap is sensitive to one or two task choices. Should be reported as suggestive with bootstrap CIs.
- **No anchor baseline against single-turn LIVESQLBENCH in Table 2.** "Idealized performance" appears only in Figure 4 dotted lines, not in the main table. Without that anchor, readers cannot decompose how much difficulty comes from the underlying SQL hardness inherited from LIVESQLBENCH versus from the new interaction layer that is the paper's contribution.
- **No per-ambiguity-category breakdown.** Sec. 3.2 defines five ambiguity categories (intent, implementation, one-shot knowledge, knowledge-chain breaking, environmental), but no table reports per-category success rates or per-category distribution. Without that, it is hard to evaluate whether difficulty is dominated by one category.
- **LOC retrieval failure modes are not surfaced.** The AST-based LOC retrieval (Sec. 3.3) is the simulator's most fragile component and Figure 6 still shows ~90% on it. Whether LOC errors correlate with task difficulty or with specific models — which would bias rankings — is deferred entirely to the appendix.

### Trivial
- The reward weights in Figure 3 (0.7 + 0.2) and the body text in Sec. 5.1 ("70% to the primary sub-task and 30% to follow-up sub-tasks") disagree numerically. Probably the missing 0.1 is the debugging penalty budget, but this should be stated explicitly.
- The c-Interact vs a-Interact comparison conflates protocol-specific accounting (the "+n" debugging credit only exists in c-Interact) with model-intrinsic interaction preference. The mode-comparison conclusion in Sec. 5.1 would be cleaner if either the accounting were normalized or the limitation were stated.

## Nice-to-Haves
- A free-mode (no budget-encoded m_amb) result on at least the LITE set, even a small one, would substantively address the leakage concern.
- Bootstrap CIs or a permutation test on the n=7 alignment correlations.
- Reporting whether the c-only and a-only orderings disagree across model pairs (and how often) would turn the protocol-pair observation from a side remark into a defensible methodological claim.
- An action-distribution figure normalized by useful actions per success would let the "trial-and-error vs exploration" claim in Sec. 5.2 stand on its own.

## Removed Points
These points are flagged to be removed, treat them with caution.
- *"Headline claims are not statistically supported in the broad sense" → kept only the specific instances of close rankings; removed the broader sweep about single runs being categorically inadequate, since single-run evaluation is the standard practice for expensive frontier-model benchmarks.*
- *"Heavy dependence on LIVESQLBENCH and the boundary of novelty is not crisp" — the paper does state the contribution boundary in Sec. 3.1 ("its primary contribution is to convert this static benchmark into a dynamic, interactive setting") and Table 1 quantifies what is new. The boundary is acknowledged; the rest is a request for more isolation experiments, kept as the "no LIVESQLBENCH single-turn baseline" minor weakness only.*
- *"60.87% submit+ask is reported as inefficient but those are correct under cost multipliers" — kept as a trivial weakness about normalization, removed the stronger framing because the paper's "future work should incentivize broader tool utilization" hedge is reasonable.*
- Strength Finder's claim about ITS being a general "law" — demoted, kept as ordinary empirical observation rather than law-level evidence.

## Novel Insights
None beyond the paper's own contributions. The most original observations — that protocol-style interaction can rank a top single-turn model last while an agentic style ranks it first, and that GPT-5's c-Interact deficit appears to be communicative rather than generative — are the paper's own contributions and remain interesting if the analytical weaknesses above are addressed.

## Suggestions
- Report at least one configuration with a fixed budget B that does *not* encode m_amb on the LITE set. If rankings hold, the leakage criticism dissolves; if they shift, that itself is a finding worth foregrounding.
- Add control conditions to Memory Grafting: (i) graft a worse model's history, (ii) graft GPT-5's own history from a different seed, (iii) graft randomized/shuffled history. Run at least 3 seeds and report per-ambiguity-category breakdown.
- Add a single-turn LIVESQLBENCH baseline row to Table 2 (not only Figure 4 dotted lines) so readers can decompose interaction-induced difficulty.
- Report per-ambiguity-category SR in the main paper, and surface LOC retrieval failure analysis.
- Bootstrap CIs on Table 3 correlations and add n≥15 system models if feasible; otherwise frame as suggestive.

## Evaluation Axes
- **Originality:** Moderate-to-high. The two-stage function-driven simulator with UNA guard is genuinely novel; the c/a dual-protocol framing is sensible; Memory Grafting is original as an analytical probe.
- **Importance:** Real. Existing multi-turn text-to-SQL benchmarks are static and SELECT-only; this directly addresses both.
- **Soundness of claims:** Mixed. The benchmark and simulator design are sound. The empirical narrative around mode-specific rankings and the communication-deficit causal claim is overstated for single-run evidence with thin margins, and the m_amb-in-budget leak undermines the stress-mode framing.
- **Experiments:** Solid in scope (7 frontier models, two protocols, ITS sweep, alignment study); thin in statistical hygiene (single runs, no CIs, no controls on grafting).
- **Clarity:** Good overall structure; a few definitional inconsistencies (0.7/0.2 vs 70/30) and the m_amb leak is not flagged.
- **Value to community:** High — the artifact (sandbox, simulator, 900 tasks, evaluation harness) is what the field needs; the benchmark will be used.

## Anchor Comparison
- τ-bench (6.5, accept) — closest analog: LLM-based user simulator, multi-turn agent–user interaction, dynamic state, real APIs. BIRD-INTERACT is broader (CRUD + dual protocols + 900 tasks) and adds the leakage-controlled simulator; its weaknesses are also similar in flavor (simulator validity, single-run rankings). Slightly above τ-bench in scope, comparable in execution.
- AgentBench (6.2), AgentQuest (6.25), WebArena (6.33), ActionReasoningBench (6.75), HAZARD (6.75) — comparable benchmark papers, all accepted; BIRD-INTERACT is in the same tier.
- PARTNR (7.0) — slightly stronger paper with cleaner methodology; BIRD-INTERACT does not quite reach this tier because of the m_amb leak and single-run thin-margin claims.
- MLE-Bench (8.0), Cybench (8.67), PhysBench (8.0), BigCodeBench (9.0) — clearly above BIRD-INTERACT; those are transformative artifacts with broader community impact and cleaner experimental hygiene.

The bracket from Round 1 was 5.5–7.0. Round 2 places BIRD-INTERACT at or slightly above τ-bench but below PARTNR — i.e., 6.0–6.5. The benchmark contribution is real and the simulator is a genuine engineering advance, but the overclaim around the central interaction-mode narrative and the m_amb leak prevent it from clearing the PARTNR bar.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>