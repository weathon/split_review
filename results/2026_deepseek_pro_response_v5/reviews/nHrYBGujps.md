Now I have a clear picture. Let me finalize the review with the calibrated score.

**Calibration summary:**

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| R-KinetiQuery | 1.67 | R1 | Much weaker — fundamentally flawed sign-language-to-SQL paper |
| EDU-RAG | 2.33 | R1 | Much weaker — simple RAG benchmark with limited contribution |
| DB-GPT-Hub | 3.75 | R1 | Weaker — focuses only on fine-tuning evaluation, less novel |
| TrustSQL | 4.00 | R1 | Weaker — narrower scope, penalty-based scoring only |
| EvoSchema | 4.25 | R1 | Weaker — schema evolution robustness, narrower contribution |
| LAIA-SQL | 5.00 | R1 | Weaker — task decomposition method, not a benchmark |
| SQL-GEN | 5.67 | R1 | Weaker — synthetic data generation method, not benchmark-focused |
| CHASE-SQL | 6.25 | R2 | Weaker — text-to-SQL method, not a benchmark |
| τ-bench | 6.50 | R2 | Slightly weaker — similar user-agent interaction benchmark but simpler user simulator, smaller domain scope |
| DyVal | 6.50 | R1 | Different — dynamic evaluation for reasoning, not text-to-SQL |
| SOTOPIA | 6.67 | R2 | Different — social intelligence evaluation, less structured |
| MINT | 6.75 | R1/R2 | **Most comparable** — multi-turn interaction benchmark; BIRD-INTERACT has more principled simulator design and creative memory grafting, but MINT covers broader tasks (20 models vs 7) |
| LiveBench | 7.33 | R1 | Stronger — contamination-free, frequently updated, broader task coverage, more established |
| WildBench | 7.33 | R2 | Stronger — 1M+ real user conversations, larger scale, more real-world grounding |
| Spider 2.0 | 8.00 | R1 | Much stronger — real enterprise databases, 1000+ columns, complex workflows, gold standard |

**Round 1 bracket:** 6.0–7.5
**Round 2 narrowed:** BIRD-INTERACT lands between τ-bench (6.50) and MINT (6.75), slightly above MINT due to the principled function-driven simulator and creative memory grafting, but below WildBench (7.33).

**Final score: 7.0**

The paper's core contribution (benchmark + function-driven simulator) is solid, the USERSIM-GUARD evaluation is convincing, and the memory grafting experiment is genuinely novel. Minor methodological gaps (single-run evaluation, limited statistical power in human-alignment study, no empirical comparison to existing benchmarks, documentation gaps in memory grafting setup) prevent it from reaching the upper tier but do not undermine the core contribution. These are addressable in revision.

---

## Summary
BIRD-INTERACT introduces a dynamic multi-turn text-to-SQL benchmark with 900 tasks (600 FULL, 300 LITE) covering the full CRUD spectrum. It features a function-driven user simulator that maps model questions to constrained actions (AMB/LOC/UNA) to prevent ground-truth leakage, two evaluation settings (protocol-guided c-Interact and agentic a-Interact), and systematic ambiguity injection across superficial, knowledge, and environmental categories. Experiments across 7 frontier LLMs show models struggle dramatically (GPT-5 achieves only 8.67% end-to-end SR in c-Interact), and a memory grafting experiment cleanly isolates communication strategy from SQL generation capability.

## Strengths
- **Function-driven user simulator with validated reliability**: The two-stage design (semantic parser → controlled response, §3.3) reduces simulator failure rates on unanswerable questions from up to 67.4% (baselines) to as low as 2.7% on the USERSIM-GUARD dataset (Figure 6). This is a concrete, measured improvement over naive LLM simulators and directly supports unsupervised evaluation.
- **Mode-dependent model aptitude revealed by dual settings**: GPT-5 performs worst in c-Interact (14.50% SR) but best in a-Interact (29.17% SR), while other models show the opposite pattern (Table 2). This non-obvious finding validates the necessity of both evaluation settings and demonstrates that interaction mode is a decisive factor in real-world performance.
- **Memory grafting experiment cleanly isolates communication from generation**: §5.2 provides GPT-5 with clarification histories from better-performing models (Qwen-3-Coder, O3-Mini) and observes SR improvement from 13.8% to 20.5% (Figure 5). This demonstrates that GPT-5's SQL generation is intact but its interactive communication strategy is deficient — a finding with implications beyond this benchmark.
- **Systematic ambiguity injection taxonomy**: §3.2 defines structured ambiguity types (intent-level, implementation-level, one-shot knowledge, knowledge chain breaking, environmental), each paired with a clarification source from ground-truth SQL. The knowledge chain breaking mechanism (Figure 2), where intermediate DAG nodes are masked, is a novel technique.
- **State-dependent follow-up sub-tasks**: Unlike prior multi-turn benchmarks, follow-up sub-tasks require reasoning over database states modified by preceding queries (§3.2), capturing an authentic production challenge ignored by existing benchmarks.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
- **Single-run evaluation without variance estimates**: All experiments use a single run per model with temperature=0 (§5, line 163). While temperature=0 makes results mostly deterministic, the user simulator's LLM backbone introduces some non-determinism across calls. Model rankings and numerical comparisons in Table 2 are point estimates; the paper acknowledges the cost constraint but should explicitly discuss stability as a limitation and ideally provide a sensitivity analysis on a small subset.
- **Human-alignment study has limited statistical power**: Table 3 reports Pearson correlations between human and simulator SRs computed across only 7 data points (one per system model). With n=7, the reported p-values (0.02, 0.03) rest on an unstable foundation — a single outlier model could substantially shift the correlation. Reporting per-task agreement would substantially increase the sample size and strengthen this analysis.
- **Memory grafting experiment uses unspecified subset**: Figure 5 reports SRs (13.8%, 18.5%, 18.8%, 20.5%) that do not match any row in Table 2, indicating a different evaluation setup (likely the LITE set or a subsample). The paper should state which subset was used, as this affects the interpretability of the results.
- **No empirical comparison to existing multi-turn benchmarks**: The paper argues conceptually that COSQL and LEARN-TO-CLARIFY are inadequate due to static conversation transcripts (§1, §7), but never runs models on those benchmarks to demonstrate that BIRD-INTERACT surfaces different failure modes. A side-by-side comparison, even on a subset, would transform a plausible conceptual argument into an empirically supported one.

### Trivial
None.

## Nice-to-Haves
- Run 3–5 seeds on a subset (e.g., 50–100 LITE tasks) to estimate ranking stability, or provide an analytic bound on simulator-induced variance.
- Characterize the simulator's behavior on borderline LOC/UNA questions (e.g., 50–100 edge cases with human labels) to further validate the gray zone between reasonable clarification and information leakage.
- Analyze which specific ambiguity types (superficial, knowledge-chain, environmental) most challenge which models, making the benchmark more diagnostically useful.
- Explicitly document the human-automation split in the ambiguity injection process (§3.2): which steps were manual vs. automated.
- Give the single-turn idealized baseline (Figure 4, dotted line) more prominence — it is one of the most diagnostic comparisons in the paper.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **Harsh Critic: "budget formula means the model doesn't know how many ambiguities there are"** — This is speculative; the paper describes the budget constraint mechanism clearly, and operating under uncertainty about remaining budget is a feature of the stress-testing design, not a flaw.
- **Harsh Critic: "ITS Law claim should be qualified to note this is model-dependent"** — The paper already does this: "Claude-3.7-Sonnet exhibits clear scaling behavior" while other models show flatter curves (line 203-205). The paper does not claim all models satisfy the ITS Law; it defines the law as a criterion and notes only Claude satisfies it.
- **Harsh Critic: "DM tasks may be easier for simpler reasons than stated"** — The paper's claim that DM tasks "follow standardized, predictable patterns" (line 175) is a reasonable interpretation. The Harsh Critic's alternative hypothesis is speculative. A paper is not required to disprove every alternative explanation.
- **Harsh Critic: "Related work is inadequate / doesn't engage with LLM-based user simulators or agent-based text-to-SQL"** — The paper does discuss MINT (Wang et al., 2024) as a dynamic interaction benchmark and MAC-SQL (Wang et al., 2025) as an agent-based framework (§7). The related work section covers the relevant literature adequately for the paper's scope.
- **Strength Finder: generic strengths about "addressing an important problem" or "targeting an interesting question"** — These are superficial and lack concrete evidence or specific citations.
- **Harsh Critic: "the abstract claim of 11,796 dynamic interactions is opaque"** — This is a minor presentation preference, not a substantive weakness. The paper clarifies this in the body text as the total across all tasks.
- **Harsh Critic: "no explicit limitations section"** — The paper includes a Future Work section (§8) that discusses limitations honestly. A separate limitations section would be a formatting preference, not a substantive weakness.
- **Harsh Critic: "the single-turn idealized baseline is under-discussed"** — This is a presentation suggestion, moved to Nice-to-Haves.

## Novel Insights
The memory grafting experiment (§5.2) is genuinely novel in its design: rather than just showing that interaction matters, it cleanly factorizes performance into (a) SQL generation capability and (b) communication strategy by transplanting interaction histories between models. This technique could be applied in other interactive evaluation settings beyond text-to-SQL. The action distribution finding — that models concentrate 60.87% of actions on *submit* and *ask* while underutilizing cheaper systematic exploration — is also a concrete, data-backed insight with implications for agent design.

## Suggestions
- The budget-constrained design is thoughtful, but a "free-mode" baseline (mentioned in future work, §8) where models have unlimited interactions would help contextualize the stress-testing results and reveal whether models naturally converge or diverge when unconstrained.
- Consider adding a dedicated limitations paragraph (distinct from future work) that transparently discusses the single-run evaluation, the simulator's retained ground-truth access, and the benchmark's derivation from LIVESQLBENCH rather than construction from scratch.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>