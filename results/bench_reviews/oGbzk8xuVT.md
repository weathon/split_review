Now I have sufficient information. Let me produce the final consolidated review.

## Final Review

**Paper:** BuilderBench – A Benchmark for Generalist Agents

---

## Summary

BuilderBench introduces a benchmark for open-ended exploration and generalization in embodied agents, centered on block-building with a simulated robotic hand. The benchmark provides (1) a hardware-accelerated MuJoCo/JAX simulator, (2) a curated task suite of 42 target structures designed to test diverse reasoning abilities (geometry, physics, planning, scaffolding), (3) a self-supervised training protocol for measuring open-ended exploration, and (4) a supervised "training wheels" protocol for debugging. Benchmarking results show that current RL algorithms (SFL, MEGA, PPO, SAC, etc.) succeed only on the simplest 1–2 cube tasks, with performance collapsing on ≥3 cubes — establishing that the benchmark is genuinely challenging for existing methods.

---

## Strengths

1. **Rich, well-motivated task design.** The five case-study tasks (T-Block, Four Cube Packing, Hexagonal Portal, Leaning Tower, Maximum Overhang) are carefully chosen to require genuinely distinct reasoning abilities — geometric reasoning, counterweight placement, temporary scaffolding, simultaneous placement, and maximum-overhang physics. This is the paper's strongest contribution, demonstrating the potential of block-building as a domain for evaluating complex embodied reasoning. (Section 5.1)

2. **Two complementary evaluation protocols.** The paper explicitly provides both a self-supervised protocol (matching the core motivation of open-ended exploration) and a supervised "debug" protocol. This dual design is pragmatic: the self-supervised protocol sets the long-term challenge, while the supervised protocol allows researchers to make incremental progress on representation learning, reward design, and architecture choices without solving the full exploration problem first. (Section 6)

3. **Hardware-accelerated simulator.** Building the simulator on MuJoCo + JAX is a sensible engineering choice that enables faster training than CPU-bound environments. The paper claims 10–100× speedup over Crafter/Minecraft/NetHack (Appendix B), which if validated would lower the barrier to entry for academic research. The commitment to open-sourcing the code and providing single-file algorithm implementations further supports reproducibility. (Section 1, contributions list)

4. **Honest characterization of limitations.** The benchmarking results are presented transparently: the paper does not claim strong performance from existing methods. It clearly shows which tasks are solvable (1–2 cubes) and which are not (≥3 cubes), and it acknowledges the limitations of its evaluation scope. This honesty is valuable for a benchmark paper.

---

## Weaknesses

### Fatal
None. The paper has significant weaknesses but none that invalidate its core claims or results.

### Major

1. **Supervised protocol trains on test tasks, creating a tension with the core motivation.** The paper's central narrative is about open-ended exploration where "agents have to explore and learn general principles about the environment without any external supervision." Yet the supervised protocol — which provides the bulk of the quantitative results (8 subplots in Figure 7 vs. 3 in Figure 6) — trains agents directly on the test tasks with task-specific rewards. The paper acknowledges this as a "debug" mode, but the heavy reliance on it leaves a gap between the benchmark's stated purpose and its demonstrated use. While the self-supervised results exist, they are limited to 12 tasks and show near-zero performance on ≥3 cubes. The paper would benefit from either reducing the prominence of the supervised results or more clearly delineating them as a separate contribution rather than primary evidence for the open-ended exploration thesis.

2. **Complex case-study tasks are never benchmarked.** The paper's richest qualitative contribution is the five case-study tasks requiring scaffolding, counterweights, simultaneous placement, and maximum-overhang reasoning (Section 5.1). Yet none of these tasks appear in the benchmarking experiments — the self-supervised evaluation covers only 12 "lowest complexity" tasks (1–3 cube variations), and the supervised evaluation covers 17 tasks (cube-1 through cube-4). The Hexagonal Portal, Leaning Tower, and Maximum Overhang tasks — the very tasks that best illustrate the benchmark's claimed advantages — are not benchmarked at all. This means the paper provides no evidence that the benchmark can actually evaluate the high-level reasoning abilities it describes so compellingly. Even reporting "zero success" on these tasks would be informative.

3. **Insufficient analysis of why algorithms fail.** The paper reports that SFL/MEGA achieve trivial performance on 3-cube self-supervised tasks and that only PPO succeeds in the supervised setting, but it offers almost no analysis of why. Are algorithms failing due to reward sparsity, insufficient exploration, representation limitations, or the inherent difficulty of long-horizon credit assignment? The paper states "these results indicate that the tested algorithms are not directly scalable to complex tasks" but provides no ablation studies, failure-mode analysis, or diagnostic experiments that would help researchers identify the specific bottlenecks. This limits the benchmark's utility as a feedback signal.

### Minor

1. **LLM evaluation is too weak to support its conclusion.** The paper asks ChatGPT-5 and Gemini 2.5 Pro to produce high-level open-loop plans from text descriptions of five tasks, reports that both fail, and concludes "solving our tasks requires non-obvious steps of reasoning that are beyond what current models can achieve through scaling alone." The experiment tests whether LLMs can generate correct manipulation plans from text alone — with no feedback, no grounding, and no execution — which is a contrived setting that any current model would be expected to fail. The paper itself calls this "not meant to be an extensive evaluation," but the conclusion drawn is stronger than the evidence supports. This section should either be redesigned (e.g., allowing LLMs to query the simulator) or repositioned as a preliminary observation rather than formal evidence.

2. **Key environmental parameters are underspecified.** The paper mentions a maximum episode length H but never states its value. The task specification dimension (ℝ³⁴) is introduced without explanation of what occupies its 34 dimensions. The state space does not mention whether color is included. The relationship between environments (defined by cube count n) and which tasks from the 42-task suite are associated with each environment is described only by reference to an appendix. These omissions affect reproducibility.

3. **The 10–100× speed claim lacks summary evidence in the main text.** The abstract and contributions claim the simulator enables 10–100× faster training than CPU-based benchmarks, but the main text provides no numbers, no comparison table, and no hardware description — only a reference to Appendix B (which is stripped by the parser). A benchmark paper should include at least a summary table in the main body to support such a central claim.

4. **Normalized return definition is unclear for self-supervised results.** The paper reports "normalized return" in Figure 6 but does not define what the normalization is relative to (maximum possible? random baseline?) and the y-axis is unlabeled in the figure caption. The supervised results also lack confidence intervals beyond shaded standard deviation across three seeds, which is standard practice but should be explicitly stated.

5. **The "solutions unknown even to the authors" claim is stated but not followed up.** Section 5.2 lists this as a design principle, but no such tasks are identified in the paper, and it is unclear whether any tasks used in benchmarking fall into this category. This reads as an unsubstantiated claim.

### Trivial
- The final sentence of the abstract ("Can AI models build a world which today's generative models can only dream of?") is evocative but vague and not supported by the paper's content.
- Figure 1's font size is small and the three protocols are not clearly visually distinguished.

---

## Nice-to-Haves

- Include a human performance baseline (success rate, steps to solve) using the same action space, to calibrate task difficulty. The paper mentions "we manually solved most tasks" but provides no quantitative metrics.
- Benchmark at least one complex case-study task (e.g., T-Block or Four Cube Packing) in the self-supervised or supervised protocol to demonstrate that the benchmark's claimed reasoning abilities are actually testable.
- Provide a diagnostic ablation (e.g., curriculum learning, reward shaping variants) to show that the benchmark can produce incremental learning signals even if end-to-end RL fails.
- Add a difficulty map showing how many of the 42 tasks are solvable at each cube count by current methods.

---

## Removed Points

- **Criticism: "Benchmark appears too hard for any current method, making it unclear it can serve as a useful feedback signal"** — While partially valid (the benchmark is hard), this critique is weakened by the fact that (a) 1-cube and 2-cube tasks ARE partially solvable, showing a difficulty gradient, and (b) the paper explicitly acknowledges the harshness and provides the supervised protocol as a stepping stone. The critic's claim of a "binary cliff" rather than a gradient is an overstatement — the evidence shows decreasing performance from 1-cube (solved) → 2-cube (partial) → 3-cube (near-zero), which IS a gradient. However, I have kept the related concern about insufficient analysis of failure modes (Major #3) and the unbenchmarked complex tasks (Major #2).

- **Criticism: "The claim of 10–100× speedup over Crafter/Minecraft/NetHack is not substantiated in the main text"** — The original submission includes Appendix B with the speed test; the parser stripped it. The claim is referenced in the main text. I have weakened this to a Minor point recommending a summary table in the main text.

- **Criticism about missing related works** — Removed per instructions (cannot confirm from external sources).

- **Criticism about ARC-AGI comparison inconsistency** — The paper's distinction (ARC-AGI provides priors through examples; BuilderBench requires discovering priors through interaction) is actually consistent. The critic conflated the supervised protocol with this comparison, but the paper's framing is sound.

- **Strength Finder's claimed strength about "Evaluation of frontier language models"** — This is weakened by the experimental design limitations (see Minor #1). Kept as a partial observation but deemphasized.

- **"Does not report statistical significance (confidence intervals)"** — Three seeds with standard deviation shading is the standard practice in this field. Single-run large-scale benchmarks rarely report formal confidence intervals.

---

## Novel Insights

The reviews surface a genuine tension that is not explicitly discussed in the paper: the benchmark's very strength (its difficulty and the richness of its tasks) creates an evaluation paradox. The tasks that best demonstrate the benchmark's conceptual value (Hexagonal Portal, Leaning Tower) are the ones least amenable to current evaluation methods, while the tasks that are actually benchmarkable (cube-count variants) are the least conceptually distinctive. This tension is not unique to BuilderBench — it appears in many benchmark papers where task design and empirical tractability are in conflict — but it is unusually sharp here. A potential resolution would be to explicitly stratify the task suite into difficulty tiers and provide different evaluation protocols for each tier, rather than treating the supervised protocol as merely a "debug" mode.

---

## Suggestions

1. **Benchmark at least 1–2 case-study tasks** (e.g., T-Block, Four Cube Packing) using the supervised protocol. Even reporting zero success is informative — it quantifies the gap for the community.
2. **Provide a difficulty calibration** — a simple table showing, for each of the 42 tasks, how many cubes, what reasoning skills are required, and whether current best methods (human or algorithmic) can solve it.
3. **Add a simple curriculum or decomposition-based baseline** — show that decomposing a 3-cube task into sub-skills produces measurable progress. This would prove the benchmark provides a useful gradient.
4. **Move the LLM evaluation to an appendix or redesign it** — allow the LLM to query the simulator or produce executable code, making the test less trivial to fail.
5. **Include a summary of the speed benchmark in the main text** — a single table with environment steps/second on comparable hardware would suffice.
6. **Specify all missing environmental parameters** (episode length H, contents of the ℝ³⁴ task specification, how tasks map to environments) either in the main text or a clearly referenced appendix table.

---

## Score and Decision

**Calibration anchors (all from ICLR 2026 human reviews):**

| Anchor | Avg Score | Comparison to this paper |
|---|---|---|
| Gaia2 (9gw03JpKK4.md) | 8.00 (Oral) | Significantly stronger — comprehensive agent evaluation across frontier models, well-validated verifier, clear empirical support for claims. BuilderBench has richer task design but much weaker validation. |
| MIKASA (9cLPurIZMj.md) | 6.50 (Poster) | Stronger — systematic memory task categorization, more models benchmarked, clearer evidence of utility. BuilderBench has more creative task design but less thorough empirical grounding. |
| ACPBench Hard (WIXohR7mEo.md) | 6.00 (Poster) | Stronger — clean symbolic validators, comprehensive model evaluation, clear failure analysis. BuilderBench has a more interesting physical domain but weaker validation. |
| Octax (BdeUsYlyIf.md) | 5.50 (Poster) | Comparable — both provide hardware-accelerated simulators with speed advantages and benchmark existing methods. BuilderBench tasks are richer; Octax is more thoroughly validated. |
| CubeBench (MCmQyZ9Gxa.md) | 5.20 (Poster) | Comparable — both are "too hard for current methods" benchmarks with 0% on hardest tasks. CubeBench has cleaner evaluation; BuilderBench has richer task design. |
| COGITAO (4XBaqkreEP.md) | 4.00 (Reject) | Slightly weaker — procedurally generated composition tasks with incomplete empirical support. BuilderBench has better motivation and more grounded task design. |
| ERNav (Y4mSVCYEq8.md) | 4.00 (Reject) | Weaker — unclear novelty vs. existing navigation benchmarks. BuilderBench has clearer differentiation from prior work. |
| COIN (xU8DPbrglA.md) | 2.50 (Withdrawn) | Significantly weaker — poor presentation, unclear contributions. BuilderBench is far better written and motivated. |

**Score rationale:** Relative to these anchors, BuilderBench sits in the 5.0 range. It has genuine strengths (creative task design, clear motivation, open-source commitment) that place it above the COGITAO/ERNav reject tier. However, it falls short of the MIKASA/ACPBench Hard tier due to (a) heavy reliance on a supervised protocol that contradicts the core motivation, (b) failure to benchmark any of the case-study tasks that best illustrate its claimed advantages, (c) insufficient analysis of why algorithms fail, and (d) a scientifically weak LLM evaluation. The paper is positioned similarly to CubeBench (5.20, Poster accepted): both introduce clever domains where current methods fail, both have strong motivation but limited empirical validation of the hardest tasks, and both would benefit from deeper diagnostic analysis. BuilderBench's task design is arguably richer, but CubeBench's evaluation framework is cleaner. Overall, the paper presents a promising benchmark concept with creative task design, but the empirical case for its utility is not yet fully made.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>