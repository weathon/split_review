Now I have enough evidence. Let me compose the final consolidated review.

## Summary

This paper systematically investigates the trade-off between diversity and consistency in LLM ensembles. It introduces a unified framework for ensembling strategies, an EigenDivergence metric for semantic filtering in Gated Mixture of Agents (GMoA), a mixture optimization algorithm, and—as its capstone contribution—a Dynamic Mixture of Agents (DMoA) that selects models at inference time based on query skills. The key empirical results include task-dependent effects of consistency filtering (Table 1), trade-offs revealed through mixture optimization (Fig. 3), and a reported SOTA result of 91.85% normalized accuracy on Big Bench Hard when using Claude 3.5 Sonnet as the aggregator in DMoA.

## Strengths

- **Systematic empirical characterization of diversity–consistency trade-offs**: The GMoA experiments (Table 1) provide controlled evidence across arithmetic reasoning, commonsense reasoning, and instruction following that neither maximizing consistency nor maximizing diversity is universally optimal. EigenDivergence filtering improves GSM8K (+0.36%) and MATH (+1.12%) but degrades AlpacaEval (−0.84%) and MT-Bench (−0.22%), directly supporting the paper's central hypothesis. Standard deviations are reported for these results, lending credibility.

- **Novel EigenDivergence metric grounded in information theory**: The metric operationalizes semantic consistency filtering as the change in differential entropy when removing an output from the ensemble (Eq. 8–10), with a clear connection to the EigenScore for hallucination detection. This is deployed as an active gating mechanism in GMoA, going beyond prior work that used similar scores only for detection.

- **Well-controlled ablation studies**: Section 4.3 cleanly disentangles the contributions of different processing functions (aggregation-and-synthesis outperforms both LLM-based ranking and universal self-consistency) and shows that maximizing semantic diversity degrades performance across all tasks, while filtering already-specialized ensembles harms their target performance.

- **Mixture optimization reveals cross-task trade-offs**: The optimization algorithm (Section 3.2) demonstrates a clear negative correlation between arithmetic reasoning performance and instruction following as mixture composition shifts (Fig. 3), providing empirical motivation for the dynamic, query-level approach.

## Weaknesses

### Major

- **DMoA framework is critically underspecified**. The paper's central claimed contribution—the Dynamic Mixture of Agents—is described only as a pair of functions $f_s(q_j;\theta)$ (skill identification) and $f_m(S;q_j,\theta)$ (model selection) with "optionally learnable parameters" $\theta$, referencing Insights 2 and 3 from Section 4.4 as justification (lines 125–131). The paper never specifies what these functions actually are: whether they are learned classifiers, retrieval-based systems, prompted LLMs, or hand-engineered rules; what input/output spaces they operate over; how skills are identified from a query; or how models are predicted to perform given those skills. Without this specification, the DMoA contribution is an architectural sketch rather than a concrete method. The DMoA results in Table 2 cannot be attributed to any specific design, and the paper's stated contribution of a "novel inference-time LLM ensembling strategy" is not supported in its current form.

- **SOTA claim on Big Bench Hard lacks a critical baseline**. The paper reports that "DMoA ... achieves a new state-of-the-art result" on BBH with 91.85% normalized accuracy using Claude 3.5 Sonnet as the final aggregator (lines 176, Table 2). The comparison is against Sonnet alone at 90.16% — a 1.69-point gain. However, the paper does **not** report a standard MoA (non-dynamic) using Claude 3.5 Sonnet as the aggregator with the same base models. Without this baseline, it is impossible to determine whether the improvement comes from the dynamic model selection mechanism or simply from using a stronger aggregator in a non-dynamic MoA. The paper does show DMoA with Qwen2-72B aggregator (83.63%) outperforming MoA with the same aggregator, which supports the value of dynamic selection for that configuration, but the SOTA claim specifically rests on the Sonnet configuration where the appropriate baseline is absent.

### Minor

- **Embedding function $e(\cdot)$ for EigenDivergence is unspecified**. The paper defines $Z = e(S)$ where $e(\cdot)$ is "an embedding function" (line 84) but never states which specific embedding model is used. Since EigenDivergence operates in sentence-embedding space, different embedding functions could produce qualitatively different rankings of output divergence. This is a straightforward specification gap that affects reproducibility of the GMoA experiments and the ablations that depend on it.

- **Mixture optimization results from a single optimization trajectory**. The optimization experiment (Section 4.2) shows results from what appears to be a single run per optimization target (Fig. 3). While the observed trade-off patterns are clear and consistent with the paper's thesis, the paper provides no analysis of whether different initial mixtures or multiple optimization seeds would yield the same conclusions. The paper itself acknowledges "it does not guarantee reaching a local optimum" (line 198) but does not investigate the stability of the observed patterns.

- **LLM-based ranking function $f_R(\cdot)$ in ablation is not described**. The ablation comparing aggregation-and-synthesis with "LLM-based ranking" (Fig. 4-left, line 164) references $f_R(\cdot)$ without specifying the ranking criterion used. This limits the interpretability of this comparison.

### Trivial

- None.

## Nice-to-Haves

- Reporting variance or error bars for the DMoA results in Table 2 and the ablation study results in Fig. 4 would ground the comparisons, especially where differences are small (<1 absolute point).
- A per-query diagnostic showing which models DMoA selects for which BBH tasks would substantially strengthen the case that skill-based selection is doing meaningful work.
- The "cross-validation bias" concept introduced in Section 4.4 (Insight 1) would benefit from a clearer definition and connection to standard cross-validation.

## Removed Points

These points from the automatic reviewers are flagged for removal; treat them with caution:

- *"The unified perspective is standard notation, not a contribution"* (Harsh Critic) — This is a matter of opinion about contribution framing, not a concrete weakness. The unified framework is explicitly presented as an expository tool to systematize ensembling strategies.
- *"Goodhart's law discussion does not derive from experiments"* (Harsh Critic) — This appears in the Discussion section as speculative interpretation (Section 6, line 196), not as an empirical claim. Speculative discussion of broader connections is standard practice and not a weakness.
- *"The paper should cover Y / additional tasks / domain Z"* — These demands exceed the paper's stated scope (arithmetic reasoning, commonsense reasoning, instruction following, and BBH).

## Novel Insights

The review process surfaces a genuine gap that the paper does not fully resolve: the paper provides strong empirical evidence *that* task-dependent diversity-consistency trade-offs exist and matter, but the DMoA's proposed solution to *exploit* these trade-offs is presented at a level of abstraction that masks the hardest engineering decisions (how to map queries to skills, and skills to model subsets). A revised version that concretizes these decisions—even with a simple classifier or retrieval-based approach—would substantially strengthen the paper. Conversely, if the paper were reframed to focus on the empirical characterization of trade-offs (which is solid) while positioning DMoA as an illustrative rather than fully specified system, it would also be viable.

## Suggestions

1. **Concretize the DMoA mechanism.** Specify what $f_s$ and $f_m$ are: e.g., a classifier trained on skill-labeled queries, a retrieval system that matches queries to similar examples from a held-out set, or a prompted LLM. Describe the skill taxonomy, the training data (if learned), and the selection criterion. Without this, Contribution 4 remains a sketch.
2. **Add the missing MoA+Sonnet baseline on BBH.** Run a standard MoA with Claude 3.5 Sonnet as the aggregator and the same base models as DMoA. If the improvement over this baseline is small or absent, revise the SOTA claim accordingly.
3. **Specify the embedding model** used for $e(\cdot)$ in the EigenDivergence computation.
4. **Report multiple runs or seeds** for the mixture optimization experiment, or at minimum acknowledge the limitation more explicitly than a brief note about not guaranteeing a local optimum.

## Score and Decision

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>