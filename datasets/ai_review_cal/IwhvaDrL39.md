- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 6, 5, 6
Now I have a thorough understanding of the paper. Let me synthesize the consolidated review.

---

## Summary

This paper proposes ResearchTown, a multi-agent LLM framework for simulating research communities. It introduces **agent-data graphs** where researchers are agent nodes (LLM functions) and papers are data nodes (text), and defines **TextGNN**, a text-based message-passing framework that models research activities (paper reading, paper writing, review writing) as GNN-style inference. The paper also presents **ResearchBench**, a benchmark with 2,737 paper-writing and 1,452 review-writing tasks, evaluated via masked node prediction. Results on a 100-paper subset show ResearchTown outperforming baselines (zero-shot, swarm, AI Scientist, paper-only), and an ablation reveals that using only first+last authors outperforms using all authors.

## Strengths

- **Novel agent-data graph abstraction with formal message-passing definitions.** Sections 3–4 formally define a heterogeneous graph where agent nodes carry LLM functions and data nodes carry text attributes, with distinct interaction types (agent–agent, agent–data, data–data). Equations (3)–(4) give explicit text-space message-passing formulas that unify diverse research activities under a single framework. This provides a principled formalism that goes beyond prior multi-agent LLM work, which lacks a clear graph-theoretic distinction between agents and data.

- **Masked node prediction provides a scalable, objective evaluation protocol for research simulation.** Section 6 defines evaluation as predicting the attributes of a masked paper/review node from its graph neighborhood, using embedding similarity to the ground truth. ResearchBench (Section 7.1) implements this at scale (2,737 paper-writing + 1,452 review-writing tasks). This avoids the cost and subjectivity of LLM-as-a-judge or human evaluation.

- **Consistent empirical advantage over baselines.** Table 1 reports ResearchTown achieving the highest similarity scores across all settings (e.g., 64.8 vs. 62.5 for swarm, 62.8 for paper-only, with text-embedding-3-large at k=1), providing evidence that the graph-structured multi-agent approach adds value over simpler alternatives.

- **Ablation reveals an interesting and non-obvious pattern about author contributions.** Table 2 shows that aggregating only the first+last author (64.8) outperforms using all authors (63.4), which the paper interprets as aligning with real-world unequal contribution distributions. This is a concrete insight emerged from the simulation framework itself.

- **Case study provides qualitative evidence of interdisciplinary idea generation.** Section 10 gives specific examples (e.g., a paper on robust evaluation techniques for ML models in drug discovery requiring both ML and drug-design expertise), supporting the claim that the framework can bridge domains.

## Weaknesses

### Fatal
None.

### Major

1. **Quantitative results are reported on only ~4% of the claimed benchmark, making conclusions preliminary.** The paper states ResearchBench contains 2,737 paper-writing tasks, but Section 7.2 explicitly says experiments were run on a subset of "100 papers in machine learning conferences" from ML-bench (3.6%) and 20 from Cross-bench. The authors acknowledge this is due to budget constraints and promise "a more comprehensive result... in the later version" (line 161). For a paper whose central empirical contribution is a new benchmark and framework, presenting results on such a small fraction is insufficient to support the claimed findings at the level a top venue requires. The differences in Table 1 (e.g., 64.8 vs. 62.5) may or may not hold at scale.

2. **No quantitative results are reported for review writing.** The paper describes review writing evaluation in Section 6 (Equation 11) and the benchmark includes 1,452 review-writing tasks, yet Table 1 only covers paper writing. No review similarity scores are presented. Since review writing is a core claimed contribution of the framework, this omission is a significant gap.

3. **No error bars, confidence intervals, or variance estimates on any quantitative result.** The entire empirical evaluation (Tables 1–2) reports point estimates without any measure of uncertainty. The ablation in Table 2 does not even state the number of data points used. Given the small sample (100 papers), the observed differences (e.g., 64.8 vs. 64.2 for the f_u/f_g ablation) may not be statistically meaningful.

### Minor

1. **The evaluation measures reconstruction fidelity (similarity to existing papers), which captures one aspect of simulation quality but not others like plausibility, coherence, or novelty.** The paper's primary quantitative metric is cosine similarity between generated and ground-truth paper summaries. This tests whether the framework can reconstruct a paper from its citation/authorship context — a reasonable proxy — but a simulation framework that generates *novel* but plausible ideas would be penalized by this metric. The paper acknowledges this tension in Section 10 ("some papers generated from ResearchTown differ from the ground truth [but] are still reasonable and valuable") but does not provide a quantitative evaluation on these other quality axes. This limits what can be concluded from the headline numbers alone.

2. **The "swarm" and "AI Scientist" baselines are described too vaguely to assess whether they are competitively implemented.** The paper says: "swarm where we build the multi-turn conversation between researchers with papers as retrieval sources" and "AI Scientist where we utilize similar prompts proposed in Lu et al. (2024) while switching the target format." Details such as number of agents, conversation turns, retrieval strategy, and prompt structure are absent, making it difficult to assess whether ResearchTown's advantage over these baselines reflects a genuine architectural benefit or differences in prompt engineering.

3. **The evaluation weight vector $\mathbf{w}_i$ in Equations (10)–(11) is never specified.** The paper defines the paper evaluation score as a weighted sum over five prompting questions but never states the values of $\mathbf{w}_i$ (e.g., equal weights? learned?). This affects the headline numbers and should be clearly documented.

4. **The TextGNN formalism is descriptive rather than computationally predictive.** Equations (3)–(4) are essentially wrappers around LLM calls with text concatenation (hidden states are in text space, message functions are LLM invocations, aggregation is concatenation + LLM call). While the GNN analogy provides a useful organizational framework, calling this a "GNN" is a stretch since there is no learned parameterization, no weight sharing across layers in the usual sense, and no gradient-based optimization — it is a prompting framework inspired by GNN structure. The paper would benefit from being explicit about this distinction. (Note: this is partially mitigated by the empirical comparison to non-graph baselines in Table 1, which does show a benefit from the graph-structured approach.)

### Trivial

- The paper references "Algorithm 1" (line 113) but the pseudocode is absent from the extracted text — likely a parser artifact, but the paper should ensure it is available.
- The claim that the first+last author result "aligns with real-world research communities" (Section 7) could also be explained by LLM training data bias (first and last authors are more prominent in paper metadata the LLM was trained on); this alternative explanation is not discussed.

## Nice-to-Haves

- Discussion of API cost and failure rate per generated paper (how many generations are incoherent or empty?) would aid practical adoption.
- A comparison to a version of ResearchTown that flattens the graph structure (e.g., concatenating all cited papers as a flat list without author agent profiles) would more cleanly isolate the benefit of the graph formalism.
- If results are reported on the full ResearchBench (even a random sample of 500–1000 papers) with confidence intervals, the empirical case would be substantially strengthened.

## Removed Points

The following points from the inputs were removed with justification:

1. **"The TextGNN framing is purely terminological and the paper does not demonstrate that the graph structure is exploited"** — REMOVED. This is factually incorrect: Table 1 directly compares ResearchTown (graph-structured) against swarm and paper-only (non-graph) baselines, and ResearchTown outperforms them, demonstrating the graph structure adds value. The equations in Sections 4–5 also provide a specific, non-trivial instantiation of message-passing for three distinct research activities.

2. **"Algorithm 1 is missing / the appendix is absent"** — REMOVED. These are parser artifacts. The original submission contains these; the extracted text is incomplete due to parsing.

3. **"Missing related works"** — REMOVED per instructions: I cannot verify existence of missing references without external sources.

4. **"Formatting nitpicks / typos / capitalization / broken characters"** — REMOVED. Parser errors, not author errors.

5. **"The distinction between f_u and f_g is unclear and not empirically justified"** — WEAKENED and merged into Minor point 4. The paper actually does ablate this (Section 7, showing a "light drop" from 64.8 to 64.2) and transparently notes the distinction can potentially be simplified, so this is not a hidden flaw.

6. **"Strengths about generic/superficial aspects"** — The strength about "sampling-based best@k results showing improvement" is generic (sampling more candidates and picking the best always improves scores). Moved to supporting context rather than a standalone strength.

## Novel Insights

The reviews surface two non-obvious observations about the paper beyond its own contributions. First, the finding that first+last-author-only aggregation outperforms full-author aggregation (Table 2) could be an artifact of LLM training data (first/last authors are disproportionately visible in paper metadata) rather than a genuine discovery about collaboration dynamics — the paper does not discuss this alternative. Second, the evaluation tension (reconstruction vs. simulation) reveals a broader methodological challenge for the field: evaluating generative multi-agent simulations requires metrics that go beyond fidelity to existing data, and ResearchTown's masked-node-prediction setup, while clever and scalable, is only one piece of what a full evaluation would require. These points suggest useful directions for future work on simulation evaluation frameworks.

## Suggestions

1. **Complete the benchmark evaluation** on at least a statistically meaningful subset of ResearchBench (500+ papers) with confidence intervals, or present results on the full benchmark. Without this, the current results are preliminary.

2. **Report quantitative review-writing results.** The benchmark includes 1,452 review tasks; report the review similarity scores (even on the same 100-paper subset).

3. **Augment the evaluation with a human or LLM-judge assessment** of generated papers on plausibility, novelty, and coherence, even on a small sample (20–50 papers). This would directly address the reconstruction-vs-simulation concern.

4. **Specify the weight vector $\mathbf{w}_i$** in the evaluation equations and state whether weights are equal or tuned.

5. **Provide a clearer ablation** that removes the graph structure entirely (e.g., a "flat" version that concatenates all neighbor text without agent roles) to more directly isolate the benefit of the graph formalism over the "paper-only" baseline.
