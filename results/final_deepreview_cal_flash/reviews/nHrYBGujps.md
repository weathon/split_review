Now let me write the final consolidated review.

## Summary

BIRD-INTERACT presents a benchmark for evaluating text-to-SQL systems in a dynamic, multi-turn interactive setting. The benchmark includes (1) a function-driven user simulator that constrains LLM responses to three symbolic actions (AMB, LOC, UNA) to prevent ground-truth leakage, (2) two evaluation settings — c-Interact (conversational protocol) and a-Interact (autonomous agentic), and (3) 900 tasks covering the full CRUD spectrum with injected ambiguities and state-dependent follow-ups. The authors benchmark seven LLMs and report low success rates (best model GPT-5 achieves only 8.67% on c-Interact and 17.00% on a-Interact FULL), illustrating the difficulty of dynamic interaction compared to static benchmarks.

## Strengths

- **Function-driven simulator provides a principled solution to information leakage.** The two-stage design (semantic parser → constrained response) reduces the failure rate on unanswerable (UNA) questions from 67.4% (baseline) to 2.7% (Figure 6). This is a concrete, well-engineered improvement over naive LLM-as-simulator approaches and directly addresses a recognized problem in interactive evaluation.

- **Comprehensive task suite spans CRUD operations with state-dependent follow-ups.** Unlike prior multi-turn text-to-SQL benchmarks (CoSQL, SParC) that are limited to SELECT-only queries with static conversation transcripts, BIRD-INTERACT covers 410 BI tasks and 190 DM tasks with INSERT/UPDATE/DELETE operations and sub-tasks that depend on modified database states. This is architecturally novel for the text-to-SQL evaluation space.

- **Dual evaluation settings reveal complementary model capabilities.** The c-Interact and a-Interact modes produce divergent model rankings (e.g., GPT-5 ranks worst in c-Interact but best in a-Interact, Table 2), demonstrating the benchmark's ability to probe different interaction paradigms — structured dialogue vs. autonomous planning — and showing that the two settings measure distinct skills.

- **Experimental results confirm the benchmark's difficulty and diagnostic value.** The memory grafting experiment (Figure 5) shows that GPT-5's c-Interact performance jumps when it is provided with interaction histories from better-interacting models, suggesting the benchmark isolates interactive communication ability as a distinct capability separate from SQL generation proficiency.

## Weaknesses

### Major

- **Simulator human alignment study is insufficiently described and potentially methodologically problematic.** The alignment study (Section 6) uses only 100 tasks and reports Pearson correlations between human and simulator success rates, but the paper does not specify the unit of analysis. If correlations are computed over binary task-level success/failure, Pearson is inappropriate. If aggregated per system model (n=7), the sample is too small for stable estimation. The p-values (0.02, 0.03) are borderline, and no confidence intervals are reported. Since the benchmark's validity as a proxy for human interaction depends on this simulator, this gap is significant. The USERSIM-GUARD evaluation (preventing leakage) is solid, but that is a different claim from "simulates real user behavior."

- **Several analytical claims overreach the available evidence.**
  - The "ITS Law" is stated as a predictive principle ("given enough interactive turns, its performance can match or even surpass the idealized single-turn task"), but Figure 4 shows performance still substantially below the idealized line with no saturation trend. The data supports a "scaling trend" observation, not a law.
  - The claim that "Interaction Mode Emerged as the Decisive Factor" is contradicted by the paper's own data: GPT-5 excels in a-Interact (29.17%) but is worst in c-Interact (14.50%), while Qwen-3-Coder shows the opposite pattern (13.33% vs. 10.83%). The effect is model-specific, not a general property of modes.
  - The memory grafting experiment does not control for the amount of contextual information provided — the improvement may partly reflect having more (noiseless) information rather than specifically interactive communication skill. The paper states "hypothesize" which is appropriate, but the surrounding framing ("validates the importance of effective interaction") is stronger than the evidence supports.

### Minor

- **No uncertainty quantification for main results.** The paper acknowledges single-run evaluation at temperature=0, but still makes comparative claims (e.g., "GPT-5 performs poorly in c-Interact but excels in a-Interact") without confidence intervals or statistical tests. Given the modest task counts (600 or 300), success rate estimates have non-trivial variance, and some observed differences could reverse with additional runs.

- **Ambiguity injection lacks quantitative characterization.** The paper describes three ambiguity types (superficial, knowledge, environmental) and reports high inter-annotator agreement (93.3–93.5%), but provides no breakdown of their distribution across the 900 tasks, no examples of original vs. converted tasks for comparison, and no analysis validating that the ambiguities are representative of real user uncertainties.

- **Only two sub-tasks per session limit the horizon for evaluating state tracking.** Every task has exactly n=2 sub-tasks (priority + follow-up). Real interactive sessions often involve longer chains. The paper notes this as future work, but it constrains the benchmark's ability to stress-test long-range state tracking.

- **The "without memory grafting" baseline in Figure 5 (13.8% for GPT-5) is on the LITE set, but the paper does not explicitly state this.** While not a discrepancy (different test set from Table 2's 14.50% on FULL), the lack of clear labeling makes the figure harder to interpret without cross-referencing appendix Table 10.

### Trivial

None.

## Nice-to-Haves

- Include task complexity breakdowns: distribution of SQL operation types (SELECT vs. INSERT/UPDATE/DELETE), ambiguity type proportions, and difficulty tiers.
- Report action costs in the main text (e.g., "Execute SQL costs 100 units, Ask costs 5") to make the action distribution analysis interpretable without consulting the appendix.
- Show one or two complete task trajectories (original query → ambiguous version → clarification → successful sub-task completion) as concrete examples in the main paper.
- Add an ablation comparing performance on ambiguous tasks vs. their non-ambiguous counterparts to quantify the contribution of the ambiguity design.
- Consider including a specialized text-to-SQL agent (e.g., MAC-SQL or similar) as a baseline to calibrate benchmark difficulty against existing methods.

## Removed Points

These points were flagged during review synthesis but removed with justification:

- **Claimed discrepancy between memory grafting baseline (13.8%) and Table 2 (14.50%):** Removed. The memory grafting experiment was conducted on BIRD-INTERACT-LITE while Table 2 reports BIRD-INTERACT-FULL results. Different test sets yield different numbers; no discrepancy exists.
- **Pearson correlation on binary data criticism (original framing):** Demoted from "fatal methodology error" to "Major" (methodology unclear). The correlation could be computed over per-task success rate proportions (0–100%, which are continuous), not binary values. The criticism that Pearson is always inappropriate for this setting is factually incorrect — the real issue is lack of clarity about what was correlated.
- **Baseline simulator comparison is a strawman:** Weakened. The baselines are conventional LLM simulators (GPT-4o, Gemini-2.0-Flash) without explicit guard prompting. While a prompted baseline would strengthen the comparison, the improvement (67.4% → 2.7% failure) is so large that it is clearly meaningful regardless.
- **Missing related works:** Removed per instructions — I cannot independently verify missing citations.
- **Missing appendix content / proofs / hyperparameters:** Removed. The parser strips these sections; they exist in the original submission.
- **Reproducibility concerns about unreleased artifacts:** Removed per hard rules — the paper cites a GitHub link and website; I must assume they exist.
- **Pure formatting/style nitpicks:** Removed per instructions.

## Novel Insights

None beyond the paper's own contributions. The reviews surfaced a useful perspective that the paper's analytical contribution (ITS law, interaction mode analysis) is weaker than its engineering contribution (simulator construction, task design). This distinction — strong engineering contribution paired with overreaching analysis — is common in benchmark papers and worth noting, but is not itself a novel observation.

## Suggestions

1. **Clarify and strengthen the simulator human-alignment study.** Specify the unit of analysis for the Pearson correlation, report appropriate agreement metrics (e.g., Cohen's κ or accuracy), provide confidence intervals, and ideally expand the study to more tasks.
2. **Temper the analytical claims.** Re-label "ITS Law" as "ITS Scaling Trend" or "Preliminary Scaling Observations." Qualify the "interaction mode as decisive factor" claim to acknowledge model-specific variation. Add a clear statement that these are initial observations warranting further study.
3. **Add uncertainty estimates.** Compute bootstrap confidence intervals for the main success rates, or at minimum acknowledge the variance explicitly when comparing models.
4. **Provide ambiguity type distributions** in the main text or a dedicated statistics table.
5. **Add concrete examples** of task trajectories to give readers an intuitive understanding of the benchmark's difficulty.

## Score and Decision

### Calibration Report

**Round 1 — Bracketing:**
- Weak anchors (<3.5): Retrieved papers at 1.67–3.40 (e.g., pose-driven query synthesis, multi-entity QA, ToM benchmarks). BIRD-INTERACT is clearly stronger than these.
- Middle anchors (3.5–7.5): Retrieved MINT (6.75), CHASE-SQL (6.25), ROUTE (6.25), TrustSQL (4.00), LAIA-SQL (5.00), HoloBench (6.25).
- Strong anchors (>7.5): Retrieved Spider 2.0 (8.00), MMQA (8.00).

**Round 1 bracket:** 4.0–7.0. BIRD-INTERACT is weaker than Spider 2.0 (8.00) and MINT (6.75) due to validation gaps; stronger than TrustSQL (4.00) and DB-GPT-Hub (3.75).

**Round 2 — Narrowing (4.5–8.0):**
Queried for anchors in (4.5, 6.5) and (6.5, 8.0). Retrieved:
- MINT (6.75, Accept) — interactive benchmark with simulator. MINT has broader task scope and stronger human validation of its simulator. BIRD-INTERACT's function-driven simulator is more principled (prevents leakage) but its human alignment evidence is thinner. **BIRD-INTERACT is weaker than MINT.**
- CHASE-SQL (6.25, Accept) — text-to-SQL method, not directly comparable as a benchmark.
- ROUTE (6.25, Accept) — text-to-SQL method.
- HoloBench (6.25, Accept) — text-to-SQL derived benchmark with evaluation limitations. **Comparable but HoloBench had more severe size/diversity concerns.**
- TrustSQL (4.00, Reject) — had dataset construction concerns. **BIRD-INTERACT is clearly stronger.**

**Final calibration:** The paper sits between MINT (6.75) and TrustSQL (4.00). The core benchmark contribution is solid and well-motivated, and the simulator demonstrates clear engineering value (preventing leakage). However, the human alignment evidence for the simulator is insufficiently documented, and several analytical claims (ITS law, interaction mode as decisive) outrun the data. This places it below MINT but above the reject-range text-to-SQL benchmarks. Score anchored at 5.5.

**All anchors retrieved:**
| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| Avg6hmtgHE (multi-entity QA) | 3.40 | R1 | Much weaker; unrelated topic |
| lMW9d1AqC9 (pose-driven query) | 1.67 | R1 | Much weaker; unrelated topic |
| NmILZXKcOi (DB-GPT-Hub) | 3.75 | R1 | Weaker; framework paper with limited novelty |
| 7ZeoPg3eTA (TrustSQL) | 4.00 | R1 | Weaker; dataset construction was questioned |
| WYdpjwKQma (LAIA-SQL) | 5.00 | R1 | Comparable in some dimensions but method paper |
| CvGqMD5OtX (CHASE-SQL) | 6.25 | R1/R2 | Stronger; well-executed method paper |
| BAglD6NGy0 (ROUTE) | 6.25 | R1 | Stronger; well-executed method paper |
| 5LXcoDtNyq (HoloBench) | 6.25 | R2 | Stronger benchmark but had size concerns |
| jp3gWrMuIZ (MINT) | 6.75 | R2 | **Most comparable.** Stronger interactive benchmark. |
| sKYHBTAxVa (LiveBench) | 7.33 | R2 | Stronger; contamination-free design |
| XmProj9cPs (Spider 2.0) | 8.00 | R1 | Stronger; enterprise benchmark, well-received |

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>