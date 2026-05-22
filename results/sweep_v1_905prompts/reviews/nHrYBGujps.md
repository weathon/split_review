Now I have sufficient calibration. Let me synthesize my final review.

**Round 1 bracket**: I initially bracketed this paper between 4.5 and 7.0 based on the first round of anchors. The low band (1.67–3.4) contained clearly weaker papers (e.g., DataSciBench 3.2, RuY1r1PDdQ 3.0). The mid band (3.75–6.25) contained TrustSQL (4.0, Reject) and CHASE-SQL (6.25, Accept). The high band (8.0+) contained MMQA and Spider 2.0. BIRD-INTERACT was clearly above TrustSQL but not at the level of Spider 2.0.

**Round 2 narrowing**: I compared against MINT (6.75, Accept) and τ-bench (6.50, Accept) — both interactive benchmarks with simulated users. BIRD-INTERACT is structurally similar but slightly behind on presentation polish and claims calibration. The **ITS law overclaiming** and clarity issues pull it down relative to these anchors. I place it at **6.0** — an Accept-level contribution with real strengths and addressable weaknesses.

**Anchor list**:
- Avg6hmtgHE (3.40, Reject) — QA paper, much weaker
- RuY1r1PDdQ (3.00, Reject) — hallucination benchmark, much weaker
- BltaWJZMeR (3.20, Reject) — data science benchmark, much weaker
- lMW9d1AqC9 (1.67, Reject) — unrelated, weaker
- NmILZXKcOi (3.75, Reject) — DB-GPT-Hub, weaker integration paper
- CvGqMD5OtX (6.25, Accept) — CHASE-SQL, method paper, comparable quality
- BAglD6NGy0 (6.25, Accept) — ROUTE, method paper
- 7ZeoPg3eTA (4.00, Reject) — TrustSQL, weaker benchmark
- GGlpykXDCa (8.00, Accept) — MMQA, stronger benchmark
- XmProj9cPs (8.00, Accept) — Spider 2.0, stronger benchmark
- YrycTjllL0 (9.00, Accept) — BigCodeBench, stronger benchmark
- jOmk0uS1hl (8.00, Accept) — unrelated
- WYdpjwKQma (5.00, Reject) — LAIA-SQL, method paper
- iSTMsye6SD (5.25, Reject) — reasoning benchmark
- JffVqPWQgg (5.00, Reject) — schema linking method
- Dojny642Dy (4.67, Reject) — video retrieval benchmark
- jp3gWrMuIZ (6.75, Accept) — MINT, very similar interactive benchmark
- roNSXZpUDN (6.50, Accept) — τ-bench, very similar interactive benchmark
- Dpqw0namg3 (6.00, Reject) — LAM Simulator

Now let me write the final review.

For the "AMG" acronym — looking at the paper more carefully, in Figure 6 caption it says "Baseline (AMG)" — this could refer to Google's Gemini models (A**M**G could be related to Anthropic **M**odel **G**??? Actually I don't know, and the paper doesn't expand it). This is a minor clarity issue.

Actually wait, let me check if "AMG" appears anywhere else in the paper beyond the figure caption... I already grepped and it only appears in the figure caption text. It's likely "Anthropic Model" something or "Another Model" something. This is a minor presentation issue.

Let me now write the review.## Summary

BIRD-INTERACT introduces a benchmark for evaluating text-to-SQL systems through dynamic multi-turn interactions, going beyond static-transcript evaluation. It provides (1) 900 tasks spanning CRUD operations with injected ambiguities and follow-up sub-tasks, (2) a function-driven user simulator that prevents ground-truth leakage (reducing unanswerable-question failure from ~67% to ~3%), and (3) two evaluation settings (*c*-Interact for protocol-guided conversation and *a*-Interact for autonomous agentic planning). Evaluations of 7 frontier models show that even the strongest models achieve only 8.67–17.00% success on the full set, revealing a large gap between SQL generation capability and interactive communication skill.

## Strengths

- **Function-driven user simulator with strong empirical validation.** The two-stage strategy (Section 3.3) maps system queries to constrained actions (AMB/LOC/UNA) before generating responses. Figure 6 shows this reduces failure on Unanswerable questions from 67.4% (baseline) to 2.7%, and Table 3 shows it achieves 0.84 Pearson correlation with human users (vs. 0.61 baseline). This is a technically rigorous solution to a known problem with LLM-based simulators, and the human-alignment evaluation is a strength rarely seen in benchmark papers.

- **Two evaluation settings that reveal differential model capabilities.** Section 4's *c*-Interact and *a*-Interact settings capture fundamentally different interaction modes. Table 2 shows GPT-5 is worst in *c*-Interact (14.50% SR) but best in *a*-Interact (29.17% SR), while Gemini-2.5-Pro shows the opposite pattern. This demonstrates the benchmark captures meaningful differences in interaction strategy, not just single-turn accuracy.

- **CRUD coverage and state-dependent follow-up sub-tasks.** The task suite covers the full CRUD spectrum (BI and DM operations), with follow-up sub-tasks that depend on intermediate database states from prior queries (Section 3.2). This goes beyond SELECT-only benchmarks like Spider and COSQL, reflecting realistic database assistant scenarios.

- **Memory grafting diagnostic.** Section 5.2 (Figure 5) shows that providing GPT-5 with interaction histories from better models raises its success rate from 13.8% to 20.5%, cleanly isolating that GPT-5's weakness in *c*-Interact is communication skill rather than SQL generation ability. This diagnostic capability is absent in static-transcript benchmarks.

## Weaknesses

### Major

- **None.** No verified weakness fundamentally undermines the paper's core claims or invalidates its results.

### Minor

- **The "ITS law" framing is overclaimed.** The paper defines "ITS Law" as: "A model satisfies this law if, given enough interactive turns, its performance can match or even surpass that of the idealized single-turn task." In Figure 4, only Claude-3.7-Sonnet in *c*-Interact approaches the idealized line; no model surpasses it, and most remain well below. The observation that performance improves (sometimes monotonically, sometimes not) with interaction turns is useful, but calling it a "law" with a claim about matching/surpassing the idealized baseline is not supported by the evidence. This is a presentation issue — the underlying empirical finding (performance can scale with interaction opportunities) is still interesting. The authors should either reframe this as a qualitative observation or provide stronger quantitative evidence.

- **Clarity issues that should be fixed.** (a) The acronym "AMG" in Figure 6 is never expanded in the paper. (b) The inter-agreement metric in Table 1 (93.33%, 93.50%) is reported without specifying whether this is percentage agreement, Cohen's κ, or another metric, nor what was being agreed upon. (c) The default patience parameter λ_pat = 3 is stated but not justified — since Figure 4 shows strong effects of patience on performance, the paper would benefit from a brief rationale for this choice. (d) The reward weighting (70% primary sub-task, 30% follow-up) is mentioned only in Section 5.1 and Figure 3, but should also appear in the problem definition (Section 2).

- **User simulator action space coverage could be better characterized.** The simulator maps queries to three actions (AMB/LOC/UNA). The evaluation on USERSIM-GUARD (2,100 questions) tests classification accuracy within this taxonomy, but the paper does not characterize whether the taxonomy itself is sufficient for the range of clarification requests that arise in practice. A human-annotation study showing what fraction of naturally-occurring clarification requests fall outside the three-action taxonomy would strengthen the validation.

### Trivial

- The cost explanation in Table 2's caption ("Avg. Cost is the cost for one task on average in USD. Our user simulator has an avg. cost of 0.03 USD.") could clarify whether the simulator cost is included in the reported model costs or listed separately.

## Nice-to-Haves

- A sensitivity analysis showing whether model rankings change under different λ_pat values for the FULL set (or a representative subset).
- A more direct comparison where the same tasks are tested with and without ambiguity injection to attribute the performance gap specifically to interaction skill vs. SQL generation difficulty.
- Reporting the fraction of runs that hit the budget limit in both evaluation settings.

## Removed Points

These points are flagged to be removed, treat them with caution:

- Harsh critic's point 2 about memory grafting (unclear baseline): The paper's Figure 5 and text make it reasonably clear — "Without Memory Grafting" for GPT-5 conditions is GPT-5 alone (13.8%). The critic's suggestion to also test GPT-5 with its *own* successful history is a nice-to-have, not a flaw in the current experiment's validity.
- Harsh critic's point about "duplicated figure caption on page 1": This is a PDF-parser artifact, not a paper flaw.
- Harsh critic's point about missing limitations section / appendix: The paper states "Rest of paper (reference and Appendix) is removed" — these were stripped by the parser, not absent from the original submission.
- Strength Finder's claim about "rigorous annotation process with high inter-annotator agreement" — this is valid but softened by the missing metric-type specification noted under weaknesses.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Reframe the ITS claim.** Replace "ITS Law" with "Interaction Test-time Scaling (ITS) Phenomenon" and clarify that it describes observed monotonic improvement under some conditions, not a law with proven convergence to idealized performance.
2. **Expand the AMG acronym** (Figure 6) and **specify the inter-agreement metric** (Table 1).
3. **Move the reward weighting (70/30) to Section 2** (Problem Definition) for reproducibility.
4. Add a brief justification for λ_pat = 3 — even a one-sentence reference to pilot studies or human-annotation statistics would suffice.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>