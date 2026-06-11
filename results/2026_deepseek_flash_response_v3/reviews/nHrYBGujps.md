Now let me write my final consolidated review.

## Summary

BIRD-INTERACT is a benchmark for evaluating LLMs on dynamic, multi-turn interactive text-to-SQL. It builds on LIVESQLBENCH to create 900 tasks (600 FULL + 300 LITE) spanning CRUD operations with injected ambiguities, state-dependent follow-up sub-tasks, and two evaluation settings: protocol-guided *c*-Interact and open-ended *a*-Interact. A key technical contribution is a two-stage function-driven user simulator that prevents ground-truth leakage. Experiments on 7 frontier LLMs show very low success rates (best = 17.00% end-to-end in *a*-Interact), a non-obvious rank inversion between settings (GPT-5 is worst in *c*-Interact but best in *a*-Interact), and a memory grafting experiment providing causal evidence that interaction skill is separable from SQL generation ability.

## Strengths

- **Function-driven user simulator with strong quantitative validation.** The two-stage design (Section 3.3) constrains simulator responses to three symbolic actions (AMB/LOC/UNA), reducing inappropriate responses on unanswerable queries from 67.4% to 2.7% (Figure 6) and achieving Pearson r=0.84 (p=0.02) alignment with human users versus 0.61 (p=0.14) for the baseline (Table 3). This directly addresses a known problem in LLM-based evaluation (ground-truth leakage).

- **Memory grafting experiment provides causal evidence for skill decomposition.** By grafting interaction histories from Qwen-3-Coder and O3-mini onto GPT-5 while keeping only the final SQL generation, GPT-5's success rate jumps from 13.8% to 18.8% and 20.5% respectively (Figure 5). This controlled intervention causally separates communication effectiveness from SQL ability — a genuinely novel finding that directly validates the paper's central thesis.

- **Dual evaluation settings reveal non-obvious model-specific tradeoffs.** The *c*-Interact vs. *a*-Interact settings produce divergent rankings: GPT-5 is the worst model in *c*-Interact (14.50% SR) but best in *a*-Interact (29.17% SR), while Qwen-3-Coder-480B shows the opposite pattern (Table 2). This granular characterization demonstrates mode-dependent interaction skill differences beyond aggregate accuracy.

- **Principled ambiguity injection via knowledge chain breaking.** Section 3.2 introduces a grounded mechanism where intermediate nodes in hierarchical knowledge DAGs are masked (Figure 2), creating tasks that are provably unsolvable without interaction and reconstructable after clarification. This is more principled than ad-hoc ambiguity injection.

- **CRUD coverage with state-dependent follow-up sub-tasks.** The benchmark covers INSERT/UPDATE/DELETE/DDL alongside SELECT (190 DM + 410 BI tasks in FULL), and follow-up sub-tasks depend on modified database states from preceding queries — a structural departure from COSQL and SParC where sub-tasks are largely independent.

## Weaknesses

### Major

- **Memory grafting numbers are inconsistent with Table 2 and the experimental setup is underspecified.** Figure 5 reports Qwen-3-Coder at 18.5% and O3-Mini at 18.5% (baseline), but Table 2 shows their *c*-Interact Priority SR as 22.00% and 24.00% respectively. GPT-5's baseline is 13.8% in Figure 5 but 14.50% in Table 2. The paper does not state whether Figure 5 reports on FULL or LITE, or which metric (Priority SR, Follow-up SR, or some hybrid). Since the memory grafting experiment is one of the paper's most important analyses, this ambiguity undermines its interpretability. The authors must clarify the experimental setup and reconcile the discrepancy.

- **"ITS Law" naming is inflated relative to the evidence.** Section 5.2 defines an "ITS Law" as a model satisfying that "given enough interactive turns, its performance can match or even surpass that of the idealized single-turn task." The evidence (Figure 4) shows this behavior clearly for Claude-3.7-Sonnet only, while other models plateau or decline. Labeling a single-model observation as a "law" overstates what the data supports. The observation itself (that some models benefit from more interaction turns) is genuinely interesting and needs no inflated label.

### Minor

- **No empirical comparison demonstrating that BIRD-INTERACT captures distinct capabilities from existing benchmarks.** The paper criticizes existing multi-turn benchmarks (CoSQL, SParC) for static transcripts and narrow scope, but never empirically tests whether model rankings on BIRD-INTERACT diverge from rankings on those benchmarks. The paper does provide *indirect* evidence (the rank inversion between settings, the memory grafting result), but the claim that the benchmark measures fundamentally different skills would be substantially stronger with a direct correlation or rank-ordering comparison. This does not invalidate the paper's contributions — many strong benchmark papers do not run such comparisons — but it is a notable gap given how heavily the paper's motivation relies on the inadequacy of existing benchmarks.

- **Inter-annotator agreement metric is underspecified.** Table 1 reports "Inter-Agreement" of 93.33% and 93.50%, but the paper does not state what this agreement was measured *on* — ambiguity labels, follow-up sub-task correctness query classification, or something else. Without context, the number cannot be interpreted.

- **Action distribution analysis is descriptive, not diagnostic.** Section 5.2 reports that 60.87% of actions are *submit* and *ask*, but does not correlate these patterns with task success. Does exploration behavior (knowledge/schema retrieval) predict higher success? This would directly test the hypothesis about pre-training biases and is a natural next step from the data already collected.

- **BI vs. DM difficulty comparison does not control for confounders.** The paper observes that BI queries are harder than DM queries (Section 5.1) but does not control for differences in ambiguity count, SQL complexity, or task distribution across the two categories. The observed gap could be an artifact of domain properties rather than a fundamental difference.

- **No verification that ambiguous queries are indeed unsolvable without clarification.** The paper asserts this (Section 3.2) and references Appendix H, but no empirical sanity check (e.g., running the ambiguous query through a strong model without clarification and confirming failure) appears in the main text.

### Trivial

- **Reward weighting rationale.** The 0.7/0.3 split between primary and follow-up sub-tasks is stated without justification.

## Nice-to-Haves

- An ablation comparing model rankings under the function-driven simulator vs. a standard LLM-based simulator would directly demonstrate whether the simulator improvement affects evaluation conclusions.
- Variance estimates across seeds (even 2–3 runs) would strengthen the benchmark as a reference suite, though temperature=0 makes this less pressing than the Harsh Critic claimed.

## Removed Points

These points were considered during review but excluded from the main weaknesses after verification against the paper:

- **"Single-run evaluation with no variance reporting"** — Removed because the paper uses temperature=0 across all models and a deterministic simulator, making the evaluation deterministic. The reviewer's claim that "interaction trajectories are not fixed" is incorrect under these conditions. Single deterministic runs are standard practice for cost-constrained LLM evaluations.
- **"Avg. Cost unclear"** — The table caption explicitly defines "Avg. Cost is the cost for one task on average in USD" and notes the simulator costs $0.03. This is sufficiently clear.
- **"Stress-mode limitation"** — The paper explicitly acknowledges this limitation in Section 8 (Future Work) and plans free-mode experiments. No redundancy needed.
- **"Speculative explanation for GPT-5 rank inversion"** — The paper offers a hypothesis ("differences in training data distributions and architectural inductive biases") with appropriate hedging ("we hypothesize"). Speculation about causes of observed phenomena is normal and not a weakness.
- **Harsh Critic's point about missing confidence intervals and sample size for human alignment** — Partially addressed by the reported p-values (p=0.02 for the function-driven simulator). The small sample concern is valid but minor and does not undermine the clear directional improvement.

## Novel Insights

The most striking finding across the reviews is the rank inversion between *c*-Interact and *a*-Interact settings (GPT-5 goes from worst to best), which, combined with the memory grafting experiment, suggests that current LLM evaluation in text-to-SQL conflates at least two distinct capabilities: structured conversational skill (following a predefined protocol) vs. autonomous exploration ability (planning and deciding when to act). The memory grafting result is particularly novel because it provides causal (not just correlational) evidence for this separation — by controlling for SQL generation ability and varying only the interaction history, the experiment isolates the interaction skill component. This is the kind of finding that can reframe how the community thinks about LLM capabilities in database tasks.

## Suggestions

1. **Resolve the memory grafting inconsistency.** Clearly state whether Figure 5 reports on FULL or LITE, which metric (Priority SR or combined), and reconcile the numerical discrepancies with Table 2.
2. **Replace "ITS Law" with measured language** such as "observed interaction test-time scaling" or "interaction scaling behavior in some models."
3. **Define the inter-annotator agreement metric explicitly** — what was measured, on what annotation task, and using what formula.
4. **Add a small-scale empirical check** that ambiguous queries fail without clarification (e.g., run them through a strong model in a zero-clarification setting).
5. **Consider adding a correlation/ranking comparison** against at least one existing multi-turn benchmark (CoSQL or SParC) to strengthen the claim that the benchmark captures distinct capabilities.

## Score and Decision

**Round 1 — Bracketing:** I queried for papers in five score bands with the query "text-to-SQL benchmark evaluation interactive multi-turn." Strong reject anchors averaged 1.67–2.33 (e.g., a pose-driven SQL paper at 1.67, an RAG benchmark at 2.33); medium-low anchors 3.75–4.25 (TrustSQL at 4.00, EvoSchema at 4.25); middle anchors 4.67–5.67 (SQL-GEN at 5.67); medium-high anchors 6.25–6.50 (τ-bench at 6.50, CHASE-SQL at 6.25); and strong anchors 8.00 (Spider 2.0, MMQA). BIRD-INTERACT is clearly above strong-reject papers and above TrustSQL/DynaEval (4.00–4.25), but below τ-bench (6.50) and Spider 2.0 (8.00). Initial bracket: [4.5, 6.0].

**Round 2 — Narrowing:** I queried bands (3.5, 5.0) and (5.0, 6.5) with a broader query "interactive benchmark LLM evaluation user simulator dynamic multi-turn." In the lower band: DynaEval (4.25), TurtleBench (3.80), WILT (4.25), FB-Bench (4.00). In the upper band: a real-time conversation paper (5.25), LAM Simulator (6.00), MTU-Bench (5.75, Accept), Talking Turns (5.80, Accept). Reading MTU-Bench (5.75) in full showed it has different weaknesses (incremental contribution, synthetic data concerns) but similar overall quality. BIRD-INTERACT has stronger individual findings (memory grafting, rank inversion) but also sharper presentation issues (memory grafting inconsistency, ITS Law overclaim) that MTU-Bench does not. Reading τ-bench (6.50) showed a cleaner, more polished benchmark with a novel metric and comprehensive analysis — BIRD-INTERACT is clearly below this standard.

**Final score:** 5.0. The paper makes solid contributions — the function-driven simulator, the dual settings revealing rank inversion, and the memory grafting experiment are genuine advances. But the memory grafting inconsistency and the "ITS Law" overclaim are real presentation issues that need fixing, and the lack of comparison to existing benchmarks is a notable gap for a paper whose motivation rests on the shortcomings of those benchmarks. The paper is above TrustSQL (4.00) and DynaEval (4.25), comparable to some aspects of MTU-Bench (5.75) but with more significant unresolved issues, and clearly below τ-bench (6.50).

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>