Now I have all the evidence I need. Let me write the consolidated review.

## Summary

BIRD-INTERACT converts the single-turn LIVESQLBENCH into a dynamic multi-turn interactive text-to-SQL benchmark. It introduces a function-driven user simulator that avoids ground-truth leakage (reducing failure on unanswerable questions from 67.4% to 2.7%), two evaluation settings (c-Interact for protocol-guided conversation and a-Interact for autonomous agentic planning), and 900 tasks spanning the full CRUD spectrum. Key findings show that even GPT-5 achieves only 8.67% success in c-Interact and 17% in a-Interact, with memory grafting experiments suggesting communication strategy deficits rather than SQL generation deficits.

## Strengths

- **Function-driven user simulator with strong evidence of improvement.** The two-stage architecture (semantic parser → constrained response generator) demonstrably prevents ground-truth leakage: failure rate on unanswerable (UNA) questions drops from up to 67.4% (baseline) to 2.7% (Figure 6). Human alignment rises from Pearson r=0.61 (p=0.14) to r=0.84 (p=0.02) (Table 3). This is a concrete, verified improvement over prior LLM-based user simulators.

- **Two evaluation settings that reveal model-specific interaction modes.** c-Interact (protocol-guided) and a-Interact (autonomous) produce markedly different model rankings (Table 2). GPT-5 is worst in c-Interact (14.50% SR) but best in a-Interact (29.17% SR), while Claude-Sonnet-4 shows the reverse pattern. This demonstrates that the two settings capture genuinely distinct dimensions of interaction capability, not just a single difficulty axis.

- **Challenging task suite that exposes a wide performance gap across models and domains.** Top models achieve only 17–25% normalized reward across settings (Table 2). BI tasks are consistently harder than DM tasks (e.g., GPT-5: 15.61% BI vs. 58.42% DM in a-Interact). These low absolute numbers confirm the benchmark's difficulty and reveal distinct failure modes across query types.

- **Interaction Test-time Scaling (ITS) and memory grafting go beyond simple score reporting.** Figure 4 shows that several models improve monotonically with more interaction turns, and Claude-3.7-Sonnet nearly catches its single-turn idealized performance. The memory grafting experiment (Figure 5) provides causal evidence that GPT-5's c-Interact weakness stems from communication strategy, not SQL ability — a stronger finding than correlational analysis alone.

- **Action distribution analysis quantifies model behavior.** The finding that 60.87% of a-Interact actions are *submit* or *ask* (trial-and-error) while knowledge and schema retrieval are underused (Section 5.2) provides a concrete target for future work on tool-utilization incentives.

## Weaknesses

### Fatal
None.

### Major

- **Single-turn baselines are missing on the full set, making it difficult to attribute the low success rates to interaction difficulty vs. base SQL difficulty.** Figure 4 reports "Idealized Performance" (single-turn, ambiguity-free) only for the lite set, which the paper describes as having "simplified databases" — performance there may not generalize to the full set. Without knowing how models perform on the same full-set tasks when all ambiguities are resolved, the claim that the benchmark measures *interaction* capability is partially uncalibrated. The authors should report single-turn results on the full set (or at least a representative subset) to establish the baseline the benchmark is designed to exceed. (Verified: the paper states the lite set has "simplified databases" and the full set results in Table 2 have no single-turn baseline.)

### Minor

- **The ambiguity injection is synthetic and the benchmark's ecological validity is not directly validated.** The paper explicitly frames this as a design choice for controllability ("To make annotation and evaluation controllable, we design methods to inject ambiguities"), and this is a reasonable trade-off. However, the benchmark measures how well models handle *annotator-designed* ambiguities with known clarification sources rather than naturally-occurring ones. A small user study validating whether the injected ambiguities resemble real user ambiguities (or even a qualitative comparison) would strengthen the claim of realism. This is not a flaw, but an acknowledged limitation worth more candid discussion.

- **The simulator's human alignment evaluation is based on 100 tasks using a single metric (success rate correlation).** While the reported Pearson r=0.84 (p=0.02) is strong, this is a narrow validation. The paper does not evaluate whether the simulator produces similar interaction trajectories, clarification questions, or turn counts as human users. Given that the simulator is a core component of the benchmark, broader behavioral validation would increase confidence (Verified: Section 6 reports "100 randomly sampled tasks" and only SR correlation).

- **The memory grafting experiment lacks variance reporting.** The paper reports point estimates (13.8% → 20.5%) from what appears to be a single run, with no indication of the number of tasks or statistical significance. While the ~48% relative improvement is substantial, the lack of confidence intervals weakens the strength of the conclusion (Verified: Section 5.2 describes the experiment but no variance is reported; the method section says "single runs due to cost").

### Trivial

- **No confidence intervals or variance estimates for main results.** Table 2 reports single runs for each model. While this is common in LLM evaluation papers due to cost, reporting variance for at least a subset of models would improve reliability assessment.

## Nice-to-Haves

- Run single-turn baselines on the full set (or a representative subset) to calibrate interaction difficulty vs. SQL difficulty.
- Broaden the user simulator validation beyond success rate correlation: compare interaction trajectories, turn counts, and clarification question similarity against human users.
- Report variance or confidence intervals for at least a subset of main results.
- Analyze whether successful task completion correlates with a different action distribution in a-Interact (e.g., do successful agents use more knowledge retrieval?).

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **"The artificial ambiguity injection undermines ecological validity" (Harsh Critic - full version)** — The original framing treated this as a major weakness suggesting the benchmark may not reflect real-world scenarios. However, the paper explicitly states the ambiguity injection is a deliberate design choice for controllability. This is a scope limitation the paper acknowledges, not a methodological error. Kept as a Minor weakness in the main review with softened framing.

2. **"Memory grafting does not control for different questions asked" (Harsh Critic)** — This misunderstands the experiment: the different interaction histories from different models *are* the experimental manipulation. The point is precisely that GPT-5's own history leads to worse outcomes than histories from other models, supporting the claim that its interaction strategy is the bottleneck. Removed as a misunderstanding.

3. **"User simulator shows only moderate alignment" (Harsh Critic)** — The framing of 0.84 Pearson as "moderate" is inaccurate (R²=0.71, substantial for behavioral alignment; p=0.02, significant). Removed; replaced with a more accurate characterization in the Minor section above.

4. **"Missing related works" (Harsh Critic)** — The paper has an adequate related work section covering text-to-SQL and multi-turn benchmarks. Removed per protocol (I cannot independently verify missing references).

5. **"Reproducibility concern about public release" (Harsh Critic)** — The paper provides a GitHub link and project website. Removed as the benchmark is stated to be available.

6. **Strength Finder claims about generic importance** — Some overclaimed phrasing softened (e.g., "important research question" type statements removed; concrete evidence-backed strengths retained).

## Novel Insights

The reviews surface one genuinely novel observation beyond the paper's own contributions: the design choice of *two evaluation settings* (c-Interact vs a-Interact) creates an interesting methodological precedent for interactive text-to-SQL benchmarks. The finding that GPT-5 flips from worst in c-Interact to best in a-Interact (while Claude-Sonnet-4 does the opposite) suggests that interaction-mode compatibility with model training biases is a non-trivial factor — not just a matter of "better models are better at interaction." This insight, which the paper surfaces but does not fully explore, points toward a research direction: rather than building one interaction benchmark, the community may need to characterize which models are suited to which interaction paradigm. The memory grafting experiment concretely supports this by attributing the discrepancy to communication strategy differences rather than SQL competence.

## Suggestions

1. **Add single-turn baselines on the full set** — Run the same models on BIRD-INTERACT-FULL with all ambiguities resolved (the original LIVESQLBENCH tasks). This single addition would calibrate the benchmark's difficulty and make the core claims much stronger. This is the single most impactful improvement.

2. **Report the number of tasks used in the memory grafting experiment and indicate stability** — Even a brief statement like "the memory grafting results are stable over X randomly sampled tasks" would significantly strengthen the conclusion.

3. **Include a brief qualitative discussion of how the injected ambiguities compare to natural user ambiguities** — Even a few examples comparing injected vs. naturally-occurring ambiguities would help readers assess ecological validity.

4. **Provide interaction trajectory-level analysis** — Beyond success rate, compare action distributions, turn counts, and clarification patterns for successful vs. unsuccessful tasks. This would deepen the analysis beyond what is already presented.

## Score and Decision

**Round 1 Bracketing (initial calibration):** Searched for topically similar papers across three score bands:
- Weak (<3.5): Papers scoring 1.67–3.40 (e.g., DataSciBench at 3.20, pose-driven query synthesis at 1.67)
- Middle (3.5–7.5): Papers scoring 3.75–6.25 (e.g., DB-GPT-Hub at 3.75, TrustSQL at 4.00, CHASE-SQL at 6.25)
- Strong (>7.5): Papers scoring 8.00 (Spider 2.0, MMQA)

BIRD-INTERACT is clearly above the weak band and below Spider 2.0 (8.00). Initial bracket: **5.5–7.5**.

**Round 2 Narrowing:** Searched for more granular anchors, particularly τ-bench (avg 6.50, scores 6/6/6/8), AgentBench (avg 6.20, scores 3/8/6/8/6), and HAZARD (avg 6.75, scores 5/6/8/8).

- **τ-bench (6.50):** A benchmark for tool-agent-user interaction using LLM-simulated users. BIRD-INTERACT is arguably **stronger** on the user simulator dimension — it provides rigorous USERSIM-GUARD evaluation (2,100 labeled questions) and human correlation analysis (0.84 Pearson), whereas τ-bench does not evaluate its user simulator with comparable rigor. BIRD-INTERACT's technical depth on the simulator is greater.
- **AgentBench (6.20):** A multi-environment LLM-agent benchmark. AgentBench is broader (8 environments) but shallower in each. BIRD-INTERACT is more focused and technically deeper. One AgentBench reviewer scored it 3 for limited novelty. BIRD-INTERACT's benchmark construction (ambiguity injection methodology, user simulator innovation) has more novel content.
- **Spider 2.0 (8.00):** A real-world enterprise text-to-SQL benchmark. Spider 2.0 had essentially no major weaknesses identified by any reviewer — it received all 8s. BIRD-INTERACT's weaknesses (missing single-turn baselines on full set, limited human eval scope, lack of variance reporting) are more noticeable, preventing it from reaching this tier.

Comparing against these anchors, BIRD-INTERACT sits above τ-bench and AgentBench but below Spider 2.0. The paper's main contributions (function-driven simulator, dual evaluation settings, challenging CRUD suite) are well-executed and empirically supported. The weaknesses are real but addressable and do not threaten the core claims.

**Final score: 6.5**

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>