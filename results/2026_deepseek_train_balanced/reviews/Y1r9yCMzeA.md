## Summary

GraphArena is a benchmark for evaluating LLMs on graph computational problems, spanning 4 polynomial-time tasks (Common Neighbor, Shortest Distance, Connected Component, Graph Diameter) and 6 NP-complete tasks (MCP, MIS, MVC, MCS, GED, TSP). Subgraphs are sampled from five real-world network sources (DBLP, Social Network, DBpedia, OpenFlights, PubChemQC). The benchmark's core methodological contribution is a three-step path-based evaluation protocol (path extraction → feasibility check → optimality verification) that classifies outputs as *correct*, *suboptimal*, *hallucinatory*, or *missing* — catching failures that answer-string matching in prior benchmarks misses. The paper evaluates 10 LLMs across 10,000 problems and explores four improvement strategies (CoT, instruction tuning, code writing, test-time compute scaling).

## Strengths

- **Path-based evaluation catches failures that answer-only metrics miss.** Section 2.3 provides a concrete, verified example: Llama3-8b outputs the correct numerical clique size "4" using nodes that do not actually form a clique. Prior benchmarks (NLGraph, GraphQA) relying on string matching would count this as correct; GraphArena's protocol correctly flags it as hallucinatory. This is direct evidence that the evaluation framework is more informative than existing practice.

- **Inclusion of six NP-complete tasks that prior graph-reasoning benchmarks did not cover.** Table 1 confirms that all 10 LLMs achieve <10% accuracy on large NP-complete graphs — a steep drop from polynomial tasks — demonstrating that these tasks probe a difficulty regime beyond what earlier benchmarks (NLGraph, GraphQA) captured. This is the strongest evidence supporting the paper's claim that GraphArena tests higher-order reasoning.

- **Head-to-head comparison with classical graph algorithms (random, greedy, approximation).** Figure 3 quantifies win/tie/loss percentages for GPT-4o against these algorithms on four NP-complete tasks. The finding that GPT-4o occasionally ties or beats problem-specific approximation algorithms (e.g., Christofides for TSP) substantiates the paper's claim about LLMs' "potential as alternative heuristics for NP tasks" — a claim no prior graph benchmark has backed with algorithmic comparisons.

- **Honest and thorough documentation of negative results.** The paper reports that CoT produces only marginal improvements (Section 3.2, Figure 6), instruction tuning fails on large NP problems (Section 3.2), and test-time compute scaling helps only simpler tasks like Connected Component (Figure 7). In a benchmarking paper, rigorously reporting what does *not* work is a strength — it prevents the community from chasing dead ends.

- **Large-scale, multi-model evaluation with useful scaling comparisons.** The evaluation spans 10 models (closed-source, open-source, MoE architectures) across 10,000 problems. The paper shows that performance gaps between model sizes are wider on GraphArena than on GSM8K/GPQA (e.g., Llama3-70b vs. 8b: 61.2% vs. 28.6% on small graphs), providing evidence that graph computation is a differentiating dimension for model capability.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Five of six NP-complete tasks lack operational definitions in the main text.** Only MCP receives a proper description (lines 54–55). MIS, MVC, MCS, GED, and TSP appear only as acronyms in the problem size specification (lines 60–62). While these are well-known problems, a benchmark paper should specify how each is operationalized — e.g., which edit operations and costs for GED, whether MCS is the induced or general common subgraph, whether TSP is a decision or optimization variant, and what the evaluation criteria are per task. This omission prevents the reader from assessing the benchmark's design validity for half its content.

- **The paper claims subgraph sampling "preserves the original graph topology" (line 38) but provides no supporting analysis.** No degree distributions, clustering coefficients, community structure comparisons, or any other topological characterization is given to substantiate that the sampled 4–50 node subgraphs differ meaningfully from random graphs of the same size. This weakens one of the paper's three stated core improvements ("Realistic Graph Collection") because the reader cannot evaluate whether the real-world sourcing actually matters at these subgraph scales. The paper's own acknowledgment (line 69: "While the graphs in each problem may not appear large") raises the question but does not resolve it.

- **CoT prompting experiment is limited to 2 of 10 tasks, both polynomial-time (Diameter and Connected Component).** The paper concludes that CoT "remains insufficient to resolve hallucinations" but this claim is extrapolated from a narrow basis. The finding is valid for the tested tasks, but generalization to NP-complete tasks and other polynomial tasks is not supported by the presented evidence.

- **Single-run evaluation (line 86) without variance reporting.** At temperature 0.1, LLM outputs have some stochasticity. While single-run evaluation across 10,000 problems is the norm for large-scale LLM benchmarks and the law of large numbers mitigates noise, the paper draws fine-grained conclusions about relative model rankings (Table 1) and performance gaps that would benefit from at least a small-scale multiple-run analysis (e.g., 3 runs on a held-out subset) to establish the stability of the reported differences.

- **Code-writing results text misreferences Table 2 when Figure/Table 3 is the correct table (line 205).** A minor but correctable inconsistency.

### Trivial

- Typographical: "Superisingly" → "Surprisingly" (introduction, paragraph 4).
- "develope" → "develop" (Section 2.3, line 73).
- "excute" → "execute" (Section 2.2).

## Nice-to-Haves

- Providing a small-scale variance analysis (e.g., 3–5 runs on a 500-problem subset) would strengthen confidence in the reported rankings.
- Characterizing the topological properties of sampled subgraphs (degree distribution, clustering coefficient, community structure) versus the original graphs would substantiate the "real-world diversity" claim.
- Including a limitations section (as is now standard practice) would improve the paper's completeness.

## Removed Points

The following points from the reviews were removed after verification:

1. **"Hallucination framing conflates distinct failures"** — Removed because the paper defines "hallucinatory" clearly and operationally as "properly formatted but infeasible" (abstract, Section 2.3). This is a self-consistent definition; calling the model's output a "hallucination" when it fabricates a non-existent feasible solution is a defensible usage. The criticism is a terminological preference, not a substantive flaw.

2. **"Real-world graph claim is undermined by tiny subgraph sizes (structural)"** — Partially removed. The criticism that the paper provides no topological analysis to support the sampling claim is retained (see Minor weakness 2). However, the stronger claim that the subgraphs are "not meaningfully distinguishable from randomly generated small graphs" is speculation, not a verified fact about this paper. The paper does use real graph sources (DBLP, Social Network, DBpedia, etc.), which is a genuine differentiator from prior work's Erdős–Rényi synthetic graphs irrespective of subgraph size. The weakness is about insufficient evidence, not about the claim being false.

3. **"Comparison against approximation algorithms on 10–30 node graphs is a strange design choice"** — Removed. The paper computes exact solutions for all problems (line 62: "ground truth of each problem is generated by corresponding exact algorithms"). The comparison with approximation algorithms is a separate analysis to contextualize LLM performance, not a substitute for exact ground truth. The small graph sizes make exact computation tractable, which is an asset, not a flaw.

4. **"GNN comparison is preliminary and results not shown in a numbered table"** — Removed. The paper explicitly states the comparison is "preliminary" (line 127). Being transparent about the limitations of a comparison is appropriate, not a weakness.

5. **"No limitations section"** — Removed as a formatting preference; many strong papers do not have explicit limitations sections.

6. **"Instruction tuning is closed-loop"** — Removed. The paper presents instruction tuning as "more extensive data exposure," which is a valid framing for evaluating how much can be gained from within-distribution training. The paper does not claim out-of-distribution generalization for this experiment.

7. **"Missing related works"** — Removed per hard rules (cannot verify external sources).

8. **"Code writing missing detail on execution environment"** — Removed as a minor reproducibility nitpick that can be addressed in the code release.

9. **Strength Finder strength 2 ("real-world graphs making the benchmark harder to game via memorization")** — Removed because the paper does not demonstrate that the real-world sourcing prevents memorization.

10. **Strength Finder strength about "concrete differentiator"** — Partially removed the overclaim about memorization, retaining the fact that real-world graph sources are used (acknowledged in Strengths above).

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

- Add operational definitions for the five undefined NP-complete tasks (MIS, MVC, MCS, GED, TSP) — at minimum specifying the problem variant, encoding format, and evaluation criteria per task. This is essential for a benchmark paper.
- Include a brief topological analysis of the sampled subgraphs (e.g., degree distributions compared to the original graphs) to support the claim that real-world diversity is preserved.
- Clarify that the CoT experiment's findings are specific to the two tested polynomial-time tasks rather than generalized to all 10 tasks.
- Fix the table cross-reference on line 205 (should refer to Table 3, not Table 2).

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>