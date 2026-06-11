## Final Review

## Summary
BIRD-INTERACT introduces a dynamic interactive text-to-SQL benchmark that replaces the static conversation transcripts of prior benchmarks (SParC, CoSQL) with a function-driven user simulator, enabling evaluation where each model's own interaction choices determine its trajectory. The benchmark comprises 900 tasks (600 FULL + 300 LITE) covering the full CRUD spectrum, with each task featuring ambiguous initial sub-tasks requiring clarification and state-dependent follow-up sub-tasks. Two evaluation settings are provided: c-Interact (protocol-guided conversation) and a-Interact (agentic REACT-style tool use). The function-driven simulator uses a two-stage design (classify-then-respond) validated via USERSIM-GUARD (2,100 labeled questions), reducing unanswerable-query failures from 67.4% to 2.7%. Even the strongest model (GPT-5) solves only 17% of tasks end-to-end, establishing that BIRD-INTERACT measures capabilities distinct from single-turn SQL generation.

## Strengths
- **Function-driven user simulator with robust validation:** The two-stage simulator (classify question → constrained response) shows a 25× improvement over baselines on USERSIM-GUARD (Figure 6): baseline simulators fail on 67.4% of unanswerable queries while the proposed approach drops to 2.7%. This is a genuine methodological contribution that directly addresses a known weakness of LLM-based simulators — ground-truth leakage — with a principled, controllable alternative.
- **Dynamic evaluation that discriminates interaction strategies:** Table 2 shows GPT-5 achieves only 14.50% SR in c-Interact (worst among all models) but 29.17% in a-Interact (best), demonstrating the benchmark meaningfully distinguishes interaction-specific capabilities beyond raw SQL generation ability. This validates the paper's core claim that interaction mode is a decisive factor.
- **Memory grafting experiment cleanly disentangles communication from generation:** When GPT-5 inherits clarification histories from O3-mini, its SR jumps from 13.8% to 20.5% (Figure 5), nearly matching O3-mini's 18.5%. This causal intervention directly supports the paper's claim that interaction quality, not SQL generation capability, determines task success — a finding with implications beyond text-to-SQL.
- **State-dependent follow-up sub-tasks:** Follow-up queries must reason over database states modified by the priority sub-task — a novel requirement absent from SParC and CoSQL that better reflects real-world database interaction patterns (Section 3.2).
- **Controlled ambiguity taxonomy with knowledge chain breaking:** The three-category taxonomy (superficial, knowledge, environmental) with the knowledge chain breaking mechanism (Figure 2) enables reproducible and controllable evaluation of clarification-seeking behavior, pairing each ambiguity with a pre-annotated SQL snippet as a clarification source.
- **Scale and annotation rigor:** 900 tasks, 12 expert annotators with multi-stage selection, 93%+ inter-annotator agreement, executable test cases verifying functional equivalence, and up to 11,796 dynamic interactions — among the largest interactive text-to-SQL benchmarks constructed.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
- **Human-simulator correlation study is underpowered for the conclusions drawn (Table 3):** The paper computes Pearson correlation between human and simulator SR across only 7 system models (n=7). While the p-values are statistically significant (0.02, 0.03), ranking correlation across models does not measure task-level agreement — a simulator that systematically overestimates all models by 20 points could still achieve r=1.0. For validating the simulator as an evaluation proxy, task-level agreement metrics (e.g., Cohen's kappa on per-task pass/fail judgments) would be more informative. USERSIM-GUARD provides strong independent validation, but this study's limitations should be acknowledged.
- **Single-run evaluation limits confidence in fine-grained model comparisons (line 163):** Results in Table 2 are based on a single run per model. While temperature=0 is standard practice and the paper transparently acknowledges this limitation is due to cost, differences between adjacent models (often 1–4 percentage points) are reported to two decimal places without any variance estimate. Even a limited multi-run subset would strengthen the empirical analysis.
- **CRUD coverage claim not quantitatively substantiated:** The paper repeatedly states the benchmark covers the "full CRUD spectrum" and "full spectrum of SQL operations, including DML and DDL" (line 56), but no breakdown by operation type (SELECT vs. INSERT vs. UPDATE vs. DELETE vs. DDL) is provided in the main text. The BI/DM split in Table 1 is a proxy but does not let a reader assess the actual distribution of operation types.
- **"ITS Law" is demonstrated for only one model (line 207):** Figure 4 shows Claude-3.7-Sonnet exhibiting the defined ITS Law behavior (monotonically approaching idealized single-turn performance with more interaction turns), but other models (O3-Mini, GPT-4o, Qwen-3) show flat or irregular scaling. Presenting this as a named "law" overstates the current evidence.
- **Simulator leakage-prevention framing could be more precise:** The USERSIM-GUARD results (Figure 6) show the proposed and baseline approaches perform similarly on AMB (~90%) and LOC (~90%) questions, diverging sharply only on UNA (67.4% vs. 2.7%). The primary improvement is in refusing to answer inappropriate questions via the UNA() gate, which is valuable but narrower than the broad "prevents ground-truth leakage" framing. More precisely distinguishing what the mechanism prevents (UNA gate) from what it controls (AMB/LOC via pre-annotated snippets) would strengthen the paper.

### Trivial
- The memory grafting experiment (Figure 5) shows GPT-5 with grafted memory achieves 20.5% SR, a ~7-point gain but still only one-fifth of tasks solved. The paper's phrasing that this shows GPT-5 "possesses robust SQL generation capabilities" (line 191) should be tempered — even with perfect interaction history, overall performance remains low, and the claim should reflect what the experiment actually demonstrates (that communication is the bottleneck, not that generation is "robust" in absolute terms).

## Nice-to-Haves
- A discussion of potential training data contamination given that LIVESQLBENCH was publicly released before the evaluated models were trained would strengthen the paper, even if only to acknowledge the question.
- A qualitative example of a failed interaction (to complement the successful example in Figure 1) would make the benchmark's difficulty more concrete to readers.
- Task-level agreement metrics (e.g., Cohen's kappa) in the human correlation study would strengthen the simulator validation.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **Harsh Critic: "The function-driven simulator's leakage-prevention mechanism is underspecified in a way that affects the paper's central technical contribution"** — The paper describes the mechanism clearly in Section 3.3: Stage 1 classifies questions into AMB(), LOC(), or UNA(); Stage 2 generates responses based on the chosen action and annotated GT SQL. The UNA() gate explicitly rejects inappropriate requests. The mechanism is specified; the remaining concern (framing precision) is retained above as a minor weakness.
- **Harsh Critic: "Action costs for a-Interact are only mentioned as existing in a figure and deferred to Appendix J"** — The appendix is stripped by the parser; the original submission includes these details. This is a parser artifact, not an author error.
- **Harsh Critic: "The paper does not discuss whether LIVESQLBENCH data might appear in LLM training corpora"** — This is speculative and there is no evidence of contamination. Moved to Nice-to-Haves as a suggestion.
- **Harsh Critic: Assertion that run-to-run variance "could easily be several points"** — This is speculative. Temperature=0 with greedy decoding produces largely deterministic outputs from API models; the magnitude of any residual nondeterminism is unmeasured and the critic's estimate is conjecture. The single-run limitation is retained as a minor weakness but the speculation about effect size is removed.
- **Strength Finder: "ITS Law reveals lawful behavior" listed as an independent strength** — This is demonstrated convincingly for only one model (Claude-3.7-Sonnet) out of four tested. It is insufficient evidence to present as a core strength and is instead included as a qualified minor weakness above.

## Novel Insights
The memory grafting experiment (Section 5.2, Figure 5) provides a novel methodological template for disentangling interaction skill from core generation capability in LLM evaluation. By treating clarification histories as a transferable resource that can be "grafted" between models, the paper offers a clean causal intervention design that could generalize to other interactive evaluation settings beyond text-to-SQL. The finding that a model can nearly match another's performance purely by inheriting its interaction history — without any change to its own generation procedure — is a crisp demonstration that interaction strategy and SQL generation are separable, independently measurable capabilities. This experimental design is the paper's most original analytical contribution.

## Suggestions
- Run even 3 repeats on a subset (e.g., 100 tasks for the top and bottom 2 models) and report means with standard deviations to strengthen the empirical comparisons.
- Add a CRUD operation-type breakdown table showing the distribution of SELECT, INSERT, UPDATE, DELETE, and DDL operations across tasks.
- Soften the "ITS Law" framing to "ITS behavior" or "ITS pattern" unless additional models demonstrate the same monotonic scaling.
- Include a per-task agreement metric (Cohen's kappa) between human and simulator pass/fail judgments in the human correlation study.

## Calibration Summary

**Round 1 — Bracketing:** Queried across five score bands. Most relevant anchors: MINT (6.75, multi-turn interaction benchmark), τ-bench (6.50, tool-agent-user interaction), WildBench (7.33, real-world user queries), Spider 2.0 (8.00, enterprise text-to-SQL). BIRD-INTERACT sits clearly above τ-bench (stronger simulator, richer analysis), comparable-to-slightly-better than MINT, and slightly below WildBench. **Initial bracket: 6.5–7.0.**

**Round 2 — Narrowing:** Additional queries inside the bracket confirmed τ-bench (6.50) as the lower bound and MINT (6.75) as the closest comparator. BIRD-INTERACT's function-driven simulator directly addresses the core weakness of both (leakage-prone LLM-simulated users) and provides deeper behavioral analysis through memory grafting and ITS. Accounting for reviewer under-estimation bias on strong papers: **final score 7.0.**

**All anchors retrieved (26 total across both rounds), with the most relevant comparisons highlighted above.**

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>