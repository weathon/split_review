Now I have verified the key claims against the actual paper. Let me construct the final review.

---

## Summary

GraphArena is a benchmarking tool that evaluates LLMs on real-world graph computational problems. It collects subgraphs from five real-world sources (DBLP, Social Network, DBpedia, OpenFlights, PubChemQC) and defines 10 tasks — 4 polynomial-time and 6 NP-complete — each decomposed into basic and optimal requirements. A path-based evaluation protocol classifies LLM outputs as correct, suboptimal, hallucinatory, or missing, going beyond simple string-matching. Evaluation of 10 LLMs across 10,000 problems reveals that even top models struggle on NP-complete tasks (under 10% accuracy on large graphs) and exhibit hallucination that scales with graph size. The paper also explores CoT prompting, instruction tuning, code writing, and test-time compute scaling as improvement strategies.

---

## Strengths

1. **Realistic graph collection (Section 2.1):** Unlike prior benchmarks (NLGraph, GraphQA) that use synthetic graphs (e.g., Erdős–Rényi), GraphArena samples subgraphs from five real-world sources using a random walk with restart strategy that preserves local topology. This provides a more authentic and challenging evaluation environment.

2. **Comprehensive and demanding task selection (Section 2.2):** The benchmark includes four polynomial-time tasks (e.g., Shortest Distance) and six NP-complete tasks (e.g., TSP, Maximum Clique), each decomposed into basic and optimal requirements. This goes beyond the basic structural understanding tested in prior benchmarks, enabling assessment of both direct algorithmic reasoning and meta-algorithmic planning.

3. **Rigorous path-based evaluation framework (Section 2.3):** The three-step process (path extraction via regex, feasibility check, optimality verification) classifies responses into four categories. As shown in the clique example (Figure 1), this prevents pattern-based guessing that numerical-only evaluation would miss — GPT-4o finds a feasible but suboptimal clique while Llama3-8b's hallucinatory response would be marked "correct" by number matching.

4. **Revealing experimental insights (Section 3.1):** Evaluation of ten LLMs across 10,000 problems (Table 1) shows that even top models (GPT-4o, Claude-3.5) achieve under 10% accuracy on NP-complete tasks with large graphs, and hallucination increases monotonically with graph size (Figure 4). The comparison with graph algorithms (Figure 3) shows GPT-4o occasionally outperforms greedy heuristics on NP-complete tasks, highlighting LLMs' potential as alternative heuristics.

5. **Systematic exploration of improvement strategies (Section 3.2):** The paper goes beyond CoT prompting to investigate instruction tuning, code writing, and test-time compute scaling — each with quantitative results (Tables 2-3, Figure 7). Findings are nuanced and honestly reported: code writing reduces hallucination on large graphs (e.g., Deepseek-V2-Coder: 61.1% → 31.4% hallucination) while instruction tuning improves small polynomial tasks but not complex NP tasks.

---

## Weaknesses

### Fatal
None.

### Major

1. **Instruction tuning data split ambiguity (Section 3.2 vs. Section 2.2):** The problem generation section (Sec. 2.2) states that 10 tasks × 500 small + 500 large graphs = 10,000 graphs total for the entire GraphArena benchmark. The instruction tuning section (Sec. 3.2) then states: "we fine-tuned Llama3-8b and Qwen2-7b on an **additional** 10,000 GraphArena problems." If there are only 10,000 total problems, this "additional" set cannot exist without a separate generation process, but none is described. The paper does not specify whether the SFT data and evaluation data are disjoint. If they overlap, the reported SFT improvements (Table 2 — Llama3-8b-SFT reaching accuracy comparable to Llama3-70b) could be artifacts of data leakage rather than genuine reasoning gains. This ambiguity undercuts the most striking result in the improvement strategies section. The authors must clarify the train/test split, the source of the 10,000 fine-tuning problems, and confirm no overlap.

### Minor

2. **Single-run evaluation with no variance estimates (Section 3, experimental setup):** The paper states it conducted "a single run per model across the 10,000 problems" due to computational cost. While understandable, LLM outputs have inherent stochasticity even at low temperature (0.1). The absence of error bars or multiple runs makes it impossible to assess whether reported differences (e.g., between GPT-4o and Claude-3.5-sonnet, or between baseline and SFT models) are statistically significant.

3. **GraphWiz comparison is of limited value (Section 3.1):** GraphWiz is evaluated zero-shot on GraphArena tasks that differ from its training corpus; the paper itself notes the result is "primarily due to the lack of task overlap and differences in graph formats." While the paper is transparent about this, including GraphWiz in a head-to-head comparison table without retraining on GraphArena's tasks gives an uninformative result. The GraphToken comparison is fair and informative on its own; the GraphWiz inclusion adds little. The authors should either retrain GraphWiz or remove this comparison.

4. **GNN comparison lacks experimental detail (Section 3.1):** The comparison with GNNs (GIN, GAT, GraphSAGE) is described as "preliminary" and provides no detail on how these models were trained, what data they were trained on, or how performance was evaluated. The claim that "Claude-3.5-sonnet generally outperforms these GNNs when they lack task-specific architecture design" is hard to evaluate without knowing the GNN training setup. Given that GNNs and LLMs process graph information in fundamentally different ways, this comparison needs more careful framing.

5. **Graph size limitations not explicitly discussed as a limitation (Section 2.2):** The largest graphs contain 50 nodes (polynomial tasks) or 20 nodes (NP-complete tasks) — far below real-world problem scales where graphs may have millions of nodes. The paper notes "[problems] often result in problems containing up to 6,000 tokens, posing a long-context challenge," but does not explicitly acknowledge that this scale limitation is driven by LLM context window constraints and affects the generalizability of findings to real-world graph computation.

### Trivial

6. Regular expressions for path extraction are mentioned but not specified per task (Section 2.3). For tasks where the output is a set (e.g., Common Neighbor — identifying a set of nodes), it is unclear how the "path" is extracted and validated. This harms reproducibility.

7. "Missing related works" note: The harsh critic mentions the paper could position itself more clearly against CLRS-Text/MAGMA. This observation is kept but demoted to trivial — the paper does cite and briefly discuss these works.

---

## Nice-to-Haves

- Provide a finer-grained error analysis: manually inspect a sample of hallucinatory responses and categorize errors (e.g., graph extraction failure vs. reasoning failure vs. algorithm selection error). This would deepen the benchmark's diagnostic value.
- Include a stronger non-LLM baseline for NP-complete tasks (e.g., simulated annealing for TSP, randomized greedy for Max Clique) to better contextualize LLM performance.
- Add a human performance baseline, even if informally estimated on a small subset.
- Analyze how LLMs handle weighted vs. unweighted graphs more explicitly (only OpenFlights uses weights, and no comparative analysis is provided).

---

## Removed Points

- **"GraphWiz comparison is misleadingly pessimistic"** — The paper explicitly acknowledges the limitation of this comparison. The result is presented with a caveat, not hidden. This is not misleading; it's a transparent zero-shot evaluation. Kept as Minor #3 (limited value, not misleading).
- **"Real-world graphs are partially cosmetic"** — The harsh critic's point that tasks are standard graph problems despite using real-world graphs is not a genuine weakness. Using real-world graph topologies is the point. Removed as it misunderstands the contribution.
- **"CLRS-Text/MAGMA positioning is a minor omission"** — The paper does discuss these works in Section 4 (Related Work). This is adequately handled.
- **Miscellaneous formatting/style nitpicks** from the harsh critic's section notes — removed per filtering rules.
- **Generic suggest-variance-estimates and reproducibility criticisms** — Kept only the specific, verifiable version in Minor #2 rather than the more sweeping version in the "Missing Parts" section.
- **"Missing baseline (nearest neighbor for TSP, randomized greedy for Max Clique)"** — The paper already compares against random, greedy, and approximation algorithms. Requesting specific additional baselines is scope creep. Moved to Nice-to-Haves.

---

## Novel Insights

The reviews surface one insight not fully articulated by the paper itself: the path-based evaluation framework is structurally better aligned with NP-complete problems (where checking a solution is easy but finding one is hard) than with polynomial problems. The feasibility/optimality decomposition effectively mirrors the P vs. NP distinction — the basic requirement tests verification (easy for NP problems), while the optimal requirement tests search (hard). This means the framework may be measuring qualitatively different capabilities across task types, which could be made explicit. Additionally, the finding that code writing reduces hallucination but sometimes worsens small-graph accuracy (due to graph extraction errors from text) suggests an interesting trade-off: externalizing computation helps with scaling but creates new failure modes in information extraction.

---

## Suggestions

1. **Resolve the data split ambiguity:** In revisions, explicitly state how the 10,000 instruction tuning problems were generated, confirm they are disjoint from the 10,000 evaluation problems, and report the overlap status. This is the single most impactful fix.
2. **Either retrain GraphWiz or remove the comparison:** If GraphWiz cannot be retrained on GraphArena tasks, the zero-shot result adds no value and should be removed. Keep GraphToken as the primary hybrid model comparison.
3. **Add error bars or multiple runs:** Even 2-3 runs on a subset of tasks (e.g., one per task category) would allow basic confidence intervals and strengthen the reliability of the reported trends.
4. **Acknowledge graph scale limitations explicitly** in the conclusion or a dedicated limitations paragraph, noting that current results reflect LLM constraints rather than fundamental capability boundaries.
5. **Split or clarify the metric reporting for Table 2:** Show the SFT training data source and size explicitly in the table caption to prevent ambiguity.

---

## Score and Decision

The core benchmark contribution — realistic graph collection, comprehensive task selection, and rigorous path-based evaluation — is solid and addresses genuine gaps in LLM graph reasoning evaluation. The data split ambiguity for the instruction tuning experiment is the most significant issue, but it is a matter of clarification rather than a fundamental flaw (the problem generation methodology is described and can straightforwardly produce disjoint training/evaluation sets). None of the weaknesses undermine the primary benchmark contributions.

**MY FINAL SCORE:** <score>7.5</score>
**MY FINAL DECISION:** <decision>Accept</decision>