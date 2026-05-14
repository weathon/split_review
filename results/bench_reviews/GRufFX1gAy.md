## Summary

This paper introduces **InnoGym**, a benchmark and evaluation framework for measuring the innovation potential of AI agents along two complementary axes: **performance gain** (improvement over best-known solutions) and **methodological novelty** (dissimilarity to prior approaches). The benchmark (iBench) comprises 18 carefully curated Improvable Tasks sourced from real-world competitions and classical problems, each standardized through multi-stage filtering, evaluator normalization, and solution collection. A companion execution environment (iGym) provides unified infrastructure for long-horizon agent evaluation. Experiments on three agent scaffolds (MLAB, CODEACT, AIDE) reveal that while agents can exhibit moderate novelty, they consistently fail to surpass human state-of-the-art performance, exposing a robustness–creativity gap that the benchmark is uniquely designed to measure.

---

## Strengths

- **Principled dual-metric framework**: The paper formalizes innovation through performance gain *G* and novelty *N* (Equations 2–3), grounded in a task quadruple (P, S, V, D) and a taxonomy of solved / improvable / exploratory problems (Section 2). This moves beyond correctness-only benchmarks in a well-motivated way, and Table 1 convincingly shows no prior benchmark evaluates both dimensions simultaneously.

- **Rigorous benchmark construction**: The 197 → 18 curation pipeline (Section 3, Appendix G) with resource filtering, evaluator normalization (Pearson ≥ 0.9, Kendall-τ ≥ 0.8 on ROADEF), validator construction, and solution collection is thorough and well-documented. Table 3 provides task metadata including reference solution counts and diversity scores, giving transparency into benchmark composition.

- **Empirical validation of the novelty metric**: Appendix F validates D_AGENT on 50 EquiBench code triplets (Table 8: superficial edits = 1.00 vs. algorithmic variants = 9.75), 8 human-annotated triplets (Spearman ρ = 0.87, 75% triplet agreement — Table 10), and 3 human-expert method triplets across three AI subfields (perfect agreement, Table 12). This demonstrates the metric can distinguish superficial from substantive methodological changes at both code and paradigm levels.

- **Meaningful empirical findings**: Table 2 shows that no agent achieves positive performance gain across 10 diverse tasks, and many task–agent pairs produce zero valid submissions (Table 6). The finding that agents can achieve moderate novelty (MLAB avg. 56.55) while failing on performance is a concrete, actionable insight about current agent limitations. The identification of a temperature "sweet spot" (0.5–0.75) balancing exploration–exploitation (Fig. 6c) offers practical guidance.

- **Statistical rigor in appendix**: Appendix E.2 provides bootstrap confidence intervals (Table 4) and paired significance tests (Table 5) with pessimistic imputation of failure cases, going beyond what many benchmark papers provide.

---

## Weaknesses

### Fatal

None.

### Major

- **Limited domain coverage in novelty metric validation**. The D_AGENT validation (EquiBench code triplets, 3 ML research method triplets) demonstrates the metric works for code-level edits and ML paradigm shifts. However, the 18 benchmark tasks span operations research (ROADEF), combinatorial optimization (CirclePacking, Graph Coloring, 2D Bin Packing), compiler optimization (CompilerGym), and mathematical modeling (GMCM) — domains whose solution structures differ substantially from the ML-centric validation triplets. The paper provides no direct evidence that the extraction and comparison prompts produce sensible dissimilarity scores for, e.g., a branch-and-cut solver vs. a genetic algorithm on ROADEF. Since every novelty result in Table 2 and all subsequent interpretations depend on this metric, the domain gap in validation introduces uncertainty that the authors should acknowledge and address. This does not invalidate the contribution — the validation that exists is principled — but it limits confidence in novelty scores for non-ML tasks and should be discussed as a limitation.

- **Variance not integrated into main claims**. The main results (Table 2) report only the best of 3 runs, and the paper draws conclusions about agent novelty and the robustness–creativity gap from these point estimates. While Appendix E.2 provides bootstrap confidence intervals and paired tests that partially address this (Table 4: macro-averaged CI for MLAB novelty is [22.08, 56.25]), these are not referenced in Section 4.2 where the main claims are made. The reader encounters strong claims about novelty without seeing the substantial uncertainty around them. Integrating the appendix analysis into the main text would strengthen the paper considerably.

### Minor

- **Performance gain scale interpretability**. While Appendix G.2 describes evaluator normalization and validates it via rank correlation, the main text never concretely states what *V* measures for each task (e.g., packing density for CirclePacking, classification accuracy for BETTL). The Gain/Ratio numbers in Table 2 are interpretable as "how far below the best known solution" but the reader cannot map them to task-intrinsic units without consulting the appendix or external competition documentation.

- **Analysis experiments limited to a single task**. The controlled experiments in Section 4.3 (temperature, base model comparison, temporal dynamics, prior knowledge) are all conducted on CirclePacking. While this task is representative of a hard optimization problem, the generality of insights about innovation dynamics across diverse task types remains unverified.

- **iGym features claimed but not evaluated**. Section 3.5 and Appendix C describe iGym's recovery mechanisms, concurrency support, and unified abstraction layer. These are presented as contributions but none are empirically validated (e.g., ablation showing recovery improves success rates, or concurrency speeds up evaluation). The runtime environment is better positioned as infrastructure rather than a separately evaluated contribution.

- **10/18 tasks used in main experiments**. This is acknowledged and pragmatically justified by resource constraints, but it leaves 8 tasks (including all 3 ROADEF challenges) unevaluated, narrowing the empirical scope.

### Trivial

- The paper could benefit from explicitly stating which concrete *V* metric underlies each task in the main text or a small table, rather than requiring readers to trace through the appendix.

---

## Nice-to-Haves

- Human evaluation of novelty on a sample of actual benchmark solutions (agent submissions vs. known solutions) would substantially strengthen confidence in the metric for the benchmark's specific task domains.
- A controlled experiment where a known methodological innovation is deliberately injected into a baseline solution to verify D_AGENT captures the intended change would provide stronger construct validity than the triplet tests alone.
- Qualitative case studies comparing high-novelty and low-novelty submissions for one or two tasks would help readers build intuition about what novelty scores mean in practice.

---

## Removed Points

*These points are flagged to be removed, treat them with caution.*

1. **"The term Improvable Tasks is defined but the paper never provides a concrete example of what constitutes the optimum V\*"** — The definition of Improvable Tasks (Section 2.3, Appendix D.1) is precisely that the optimum is *unknown*. This is the defining property of the category. The criticism misunderstands the taxonomy. **Removed.**

2. **"Known solutions S_known are not listed or characterized"** — Table 3 provides |S_known| counts and diversity scores (Div) for every task. Appendix G.1 details the multi-stage collection process. The solutions themselves are part of the open-source benchmark release. **Removed.**

3. **"12-hour time budget impact is not analyzed relative to the nature of the tasks"** — Section 4.3 and Figure 6(a) analyze temporal dynamics of innovation (G and N evolution over time) on CirclePacking. **Removed.**

4. **"The Gain column is entirely negative, meaning all agents underperform the best known; the values [are] unanchored"** — This is the paper's central empirical finding, not a weakness. The paper is transparent that agents fail to beat human baselines. The negative gains are precisely what make the robustness–creativity gap meaningful. **Removed.**

5. **"The abstract's assertion that 'some agents produce novel approaches' presupposes the validity of the novelty metric"** — Every paper's claims presuppose its methods are valid. The novelty metric has validation (Appendix F). This is not a separate weakness. **Removed.**

6. **"Comparison table lists multi-GPU, multi-node, and save-and-restore as important differentiators... yet no ablations are performed"** (from Strength Finder referencing InnovatorBench-style criticism) — This criticism appears to be about a different paper (InnovatorBench). InnoGym's Table 1 comparison focuses on reference solutions and evaluation dimensions, not infrastructure features. **Removed.**

7. **Generic strength about "addressing an important problem"** — Too generic, no specific citation or concrete evidence. **Removed from strengths.**

---

## Novel Insights

Beyond the paper's own contributions, a genuinely interesting observation emerges from the tension in the experimental results: agents can produce methodologically novel solutions (average novelty 46–57) that simultaneously fail catastrophically on performance (all gains negative). This suggests current agent scaffolds may be better at *divergent generation* of ideas than at *convergent refinement* of those ideas into working solutions — a pattern that mirrors known capability profiles of the underlying LLMs. The benchmark thus reveals that the bottleneck in AI-driven innovation is not ideation but execution robustness, which is a more nuanced and actionable diagnosis than simply "agents aren't creative enough."

---

## Suggestions

- Move the bootstrap analysis (Appendix E.2, Tables 4–5) into the main text or at minimum reference it directly in Section 4.2 when making claims about agent profiles, so readers see the uncertainty around novelty and gain estimates.
- Add a brief limitations paragraph in the main text acknowledging the domain gap between D_AGENT's validation settings (code-level edits, ML paradigms) and the full task diversity of iBench, particularly for operations research and combinatorial optimization tasks.
- For the camera-ready version, consider running at least one additional task from the 8 unevaluated ones (ideally a ROADEF challenge) to demonstrate cross-domain applicability, even if only with one agent scaffold.
- Add per-task descriptions of the raw performance metric *V* (e.g., a one-line note in Table 2 or a small supplement table) to improve interpretability.

---

## Score and Decision

### Calibration anchors used:

| Paper | Path | Avg Score | Comparison to current paper |
|---|---|---|---|
| Gaia2 | `9gw03JpKK4.md` | 8.00 | Stronger: more comprehensive evaluation, genuine infrastructure contribution (ARE), action-level verification. Our paper has a more novel conceptual framework but less thorough execution. |
| InnovatorBench | `w8rZ2Jd6Jo.md` | 5.33 | Weaker: similar concept (agent research/innovation benchmark) but fewer tasks, less rigorous curation, no metric validation, and no statistical analysis. Our paper is clearly stronger on all these axes. |
| EXP-Bench | `KjgyAm383Z.md` | 6.00 | Comparable quality: 461 tasks from 51 papers, strong curation. Our paper has a more distinctive contribution (dual-metric framework vs. correctness-only) but smaller scale. |
| FML-bench | `h6BT8RhrNc.md` | 4.50 | Weaker: contributed a benchmark but had arbitrary metric design and contrived conclusions. Our paper has better-justified metrics with validation. |
| C2-Eval | `ywMGBtTi4z.md` | 3.00 | Much weaker: creativity benchmark with ad-hoc metrics that had no expert validation. Our paper validates its novelty metric against human judgments. |
| TimeSeriesGym | `8gdfWRilR7.md` | 3.50 | Much weaker: domain-specific benchmark with critical evaluation flaws and floor effects. Our paper's benchmark construction and metric validation are more rigorous. |
| A2ASecBench | `LfdFnakqGJ.md` | 5.50 | Comparable quality: security benchmark with well-defined threat model. Our paper has broader ambition (measuring innovation) but similar level of execution rigor. |
| StockBench | `9tFRj7cmrS.md` | 2.50 | Much weaker: trading benchmark with significant methodological issues. Our paper is substantially stronger. |

This paper makes a genuine conceptual contribution — the dual-metric framework for evaluating innovation is novel and well-motivated. The benchmark construction (197→18 curation, evaluator normalization, solution collection) is rigorous by community standards. The novelty metric is validated against human judgments across two settings, which exceeds what many benchmark papers provide. The empirical findings (robustness–creativity gap) are meaningful and well-supported. The main weaknesses are the domain gap in novelty metric validation and the separation of variance analysis from main claims — both addressable in revision.

Compared to InnovatorBench (5.33, accepted), this paper is clearly stronger. Compared to Gaia2 (8.00, oral), it has less comprehensive evaluation and a less polished infrastructure contribution but a more conceptually distinctive benchmarking idea. I place it between these anchors, closer to the 6.0 mark.

**Overall assessment**: A solid benchmark paper with a distinctive conceptual contribution, reasonable validation, and meaningful findings. The weaknesses are real but not fatal and are largely addressable through revision. Accept.

---

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>