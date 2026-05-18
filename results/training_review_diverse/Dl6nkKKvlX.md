Now I have all the information I need. Let me compose the consolidated review.

## Summary

This paper empirically investigates the trade-off between diversity and consistency in LLM ensembles. The authors propose (1) a unified taxonomic framework for LLM ensembling, (2) an EigenDivergence metric derived from hallucination-detection literature to gate outputs by semantic consistency (Gated MoA), (3) a simple mixture optimization algorithm to study composition-level trade-offs, and (4) the Dynamic Mixture of Agents (DMoA), an inference-time ensembling strategy that selects model subsets based on task-specific skills. Experiments across arithmetic reasoning, commonsense reasoning, and instruction-following benchmarks provide evidence that task-dependent diversity-consistency trade-offs exist, and DMoA achieves a new SOTA on Big Bench Hard (91.85% with Claude 3.5 Sonnet as aggregator).

## Strengths

- **Novel EigenDivergence metric for semantic consistency in heterogeneous ensembles.** The paper adapts the EigenScore from hallucination detection to quantify each individual output's contribution to overall ensemble coherence (Eq. 8, §3.1). This is a principled, information-theoretic adaptation that is evaluated across multiple benchmarks (Table 1) and yields non-trivial findings (e.g., filtering divergent outputs helps MATH/CSQA but hurts AlpacaEval).

- **Systematic empirical documentation of task-dependent diversity-consistency trade-offs.** The EigenDivergence filtering experiment (§4.1) and mixture optimization (§4.2) together provide concrete evidence that the optimal balance varies by task type. For instance, optimizing for GSM8K improves arithmetic reasoning (+2.73%) but degrades AlpacaEval 2.0 (-3.72%), and optimizing for instruction following reduces GSM8K performance. These results are clearly shown in Fig. 3 and Table 1.

- **DMoA achieves competitive results on Big Bench Hard.** DMoA with Qwen2-72B-Instruct aggregator reaches 83.63% normalized accuracy (vs. MoA's 82.33%), and DMoA with Claude 3.5 Sonnet reaches 91.85% — improving over Sonnet alone (90.1%). This demonstrates that the dynamic selection mechanism adds value beyond the aggregator's individual capability.

- **Useful ablation studies characterizing processing functions and semantic diversity.** Figure 4 systematically compares aggregation-and-synthesis, LLM-based ranking, and universal self-consistency, showing that AS outperforms alternatives across tasks. The ablation also confirms that maximizing semantic diversity degrades performance and that filtering specialized ensembles is harmful — findings that directly support the paper's design choices.

## Weaknesses

### Fatal
None.

### Major

- **DMoA selection mechanism is underspecified.** The core of the claimed contribution — how skills are identified ($f_s$) and how models are matched to those skills ($f_m$) — is described only at a high level in §3.3: "identify the required skills $S = f_s(q_j; \theta)$" and "select a subset of models $\mathcal{M}_S = f_m(S; q_j, \theta) \subseteq \mathcal{M}$ predicted to perform well given these skills." Both functions defer to qualitative insights from §4.4 (Insight 2: "task-dependent LLM expertise is crucial"; Insight 3: "task-specific skills reside in different subspaces"). There is no concrete algorithm, no learnable parameter specification, no feature representation, and no evaluation of the selection component in isolation. Without specifying how routing decisions are made for arbitrary queries (outside pre-defined benchmark categories), the method is not reproducible as described.

### Minor

- **The mixture optimization algorithm uses a crude attribution assumption.** Equation 12 attributes each model's impact proportionally to its usage change, ignoring interactions between models, order effects in aggregation, and sampling noise. The algorithm replaces the lowest-delta model with a clone of the highest-delta model, which can (and does) collapse the mixture to a self-ensemble. The paper acknowledges it "does not guarantee reaching a local optimum" (§6), and the broad trade-off conclusion is likely robust, but the individual model attributions are unreliable for finer-grained analysis.

- **EigenDivergence analysis is purely correlational.** The paper removes divergent outputs and measures aggregate performance changes, but does not verify whether the removed outputs were actually incorrect or low-quality (vs. correct but creatively different). This leaves alternative explanations viable — e.g., for closed-ended reasoning tasks, filtering removes incorrect outliers, while for open-ended generation, filtering removes valid creative responses that evaluators reward. The paper's framing as a "diversity-consistency trade-off" is consistent with the data but not uniquely supported.

- **No ablation of the DMoA selection mechanism.** The paper compares DMoA to standard MoA, but does not include a baseline that randomly selects subsets of the same size. Without this, it is unclear whether DMoA's improvement over MoA comes from smarter model selection or simply from ensemble size reduction / stochastic variation.

- **The claim about "cross-validation bias contingent on model expertise" is not tested.** The abstract states the finding "contingent on the expertise of the constituent models," but all experiments use capable, state-of-the-art models. Model quality is never systematically varied, so this contingency is asserted rather than demonstrated.

- **Computational cost is not reported.** DMoA's dynamic selection could reduce inference queries, but no latency, query count, or total cost figures are provided. Since this is a potential advantage of the method, its omission is noticeable.

### Trivial

- "Cross-validation bias" is used to describe the phenomenon that ensembles outperform individuals. This is non-standard terminology — "cross-validation bias" normally refers to overfitting in model selection — and may confuse readers. "Ensemble averaging effect" or "multi-hypothesis validation" would be clearer.

## Nice-to-Haves

- A concrete specification of $f_s$ and $f_m$ (e.g., a lightweight classifier trained on task categories, or a retrieval-based approach using benchmark metadata).
- A random-selection baseline for DMoA to isolate the benefit of routing from ensemble size reduction.
- An analysis of the quality of EigenDivergence-removed outputs (were they incorrect, hallucinated, or just diverse but correct?).
- Reporting of inference cost (queries per example, latency) for all compared methods.

## Removed Points

- *"The unified perspective does not generate new insights or predictions."* — The paper presents it as a systematization/taxonomy (§2: "To enable clearer conceptualization and hypothesis generation"), not as a generative theory. Taxonomies are a legitimate contribution type, and this criticism holds the framework to an inappropriate standard.
- *"The SOTA claim is entirely attributable to the aggregator model."* — DMoA+Sonnet (91.85%) outperforms Sonnet alone (90.1%, reported as the previous SOTA), so the DMoA mechanism contributes measurable gains. The paper also reports DMoA without Sonnet (83.63%) vs. MoA (82.33%). The reviewer overstated this point.
- *"The mixture optimization algorithm produces results that are too brittle to support the conclusions."* — The trade-off conclusion (optimizing one task hurts another) is robustly observed across multiple task pairs (Fig. 3) and is not undermined by the algorithm's simplicity. The algorithm is crude but the observed trend is clear.
- *"Enforcing higher semantic diversity degrades performance — the paper's framing as a trade-off is too vague."* — The paper's interpretation is consistent with the data, and the alternative explanation (filtering removes incorrect answers for closed tasks) is complementary, not contradictory. The reviewer's characterization overstates the issue.

## Novel Insights

Beyond the paper's own contributions, one observation emerges from the reviews: the paper's results suggest that ensemble optimization for LLMs may face a fundamental limitation that parallels the Goodhart's law connection the authors themselves note in §6 — the more you optimize an ensemble for a narrow proxy (e.g., instruction-following ratings), the more you risk washing out the diversity that actually helps on other tasks. This is more than the usual diversity-consistency framing; it implies that for LLM ensembles, diversity is not just a helpful signal but an active resource that can be depleted by optimization, making any single-task optimization strategy inherently myopic.

## Suggestions

1. Specify the DMoA selection mechanism concretely. Even a simple classifier trained on query embeddings to predict which models perform best on which task categories would significantly improve reproducibility and allow proper ablation.
2. Add a random-subset selection baseline for DMoA (same ensemble size as DMoA selects, but models drawn uniformly). This would isolate the benefit of smart routing.
3. Analyze the quality of EigenDivergence-filtered outputs (e.g., by checking whether removed outputs were correct/incorrect) to strengthen the causal interpretation of the trade-off.
4. Report inference cost (queries per example and total API calls) for all methods — this is standard practice for ensembling papers and would highlight DMoA's efficiency advantage.

## Score and Decision

The paper makes a genuine empirical contribution by systematically documenting task-dependent diversity-consistency trade-offs in LLM ensembles and introducing the EigenDivergence metric as a principled tool for studying these trade-offs. The DMoA results on BBH are promising.

However, the DMoA — listed as a core contribution and highlighted in the title/abstract — is seriously underspecified. The selection mechanism ($f_s$, $f_m$) is described only by reference to qualitative insights, with no concrete algorithm, making the method unreproducible. This is a significant weakness for a claimed methodological contribution. Combined with the correlational nature of the EigenDivergence analysis and the lack of a random-selection ablation, the paper falls short of the bar for acceptance at a top venue in its current form. The empirical analysis of trade-offs is valuable, but the paper's central method needs substantial revision.

**Score: 5.0** — Borderline; the analysis contributions are solid but the main method contribution is insufficiently specified.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>