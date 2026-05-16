I now have a thorough understanding of the paper and all the reviewer inputs. Let me write the final consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses
### Fatal
### Major
- weakness 1 — why it matters
### Minor
- weakness 1 — why it matters
### Trivial

## Nice-to-Haves

## Removed Points

## Novel Insights

## Suggestions

## Score and Decision

Now let me write the full review.

---

Here is my analysis of the key claims:

The harsh critic claims that "Table 2 shows Claude 3.5 Sonnet alone achieving 91.85% normalized accuracy on BBH, and DMoA/Sonnet also achieving 91.85%." However, the paper's text (line 176) says DMoA (with Qwen aggregator) gets 83.63%, which is "92.7% of the performance of Claude 3.5 Sonnet," implying Sonnet alone ≈ 90.19%. DMoA/Sonnet achieves 91.85%. The critic's specific numerical claim is factually inconsistent with the paper's text. The SOTA claim appears internally consistent: DMoA/Sonnet (91.85%) > Sonnet alone (~90.19%). I will REMOVE this criticism.

The DMoA underspecification (Critical Issue 1) is genuine — f_s and f_m are not concretely defined. This is kept as a MAJOR weakness.

The mixture optimization criticism (Critical Issue 3) — the paper explicitly acknowledges the algorithm converges to a self-ensemble (line 151: "the optimized mixture is a self-ensemble"), and the value is in the observed trade-off, not the algorithm's sophistication. The critic's characterization as "trivial" is somewhat harsh but the point that the findings are not deeply surprising has some merit. I'll DOWNGRADE this to Minor.

Let me finalize.## Summary

This paper systematically investigates the trade-off between diversity and consistency in LLM ensembles. It proposes a unified framework subsuming existing ensembling approaches (self-consistency, MoA, FrugalGPT, self-ensembling), introduces an EigenDivergence metric for measuring semantic consistency within heterogeneous mixtures, develops a mixture optimization algorithm for studying trade-offs at the model-composition level, and proposes Dynamic Mixture of Agents (DMoA) as an inference-time ensembling strategy. Experiments across arithmetic reasoning, commonsense reasoning, and instruction-following benchmarks provide empirical evidence that the optimal diversity-consistency balance is task-dependent, and DMoA achieves state-of-the-art normalized accuracy (91.85%) on Big Bench Hard when using Claude 3.5 Sonnet as the final aggregator.

## Strengths

- **Unified ensembling framework (Section 2):** The paper formalizes diverse ensembling strategies (self-consistency, FrugalGPT, MoA, self-ensembling) under a common set of equations (Eqs. 1–4), enabling clear comparison and hypothesis generation. This systematization is a useful conceptual contribution for the field.

- **EigenDivergence metric with information-theoretic grounding (Section 3.1):** Adapting the EigenScore from hallucination detection to the ensembling setting is novel. The metric is connected to differential entropy (Eqs. 7–9), and the experiments (Table 1) show meaningful task-dependent effects: filtering divergent outputs improves arithmetic reasoning (MATH: +1.12%) but degrades instruction following (AlpacaEval 2.0: –0.84%), providing direct evidence for the paper's central thesis.

- **Mixture optimization experiments demonstrate concrete trade-offs (Section 3.2, Section 4.2):** The algorithm systematically adjusts model composition, and the results (Figure 3) quantitatively show that optimizing for GSM8K (93.48% → 96.21%) causes AlpacaEval 2.0 performance to drop (59.59% → 55.87%), while optimization for instruction following degrades arithmetic reasoning (GSM8K: 93.48% → 91.36%). These concrete trade-off measurements are a solid empirical contribution.

- **Comprehensive ablation studies (Section 4.3):** Three ablations validate key design choices: (1) aggregation-and-synthesis outperforms ranking and self-consistency across tasks, (2) higher semantic diversity degrades performance across all tasks, and (3) filtering specialized ensembles harms their target performance. These results support the architectural decisions behind DMoA.

- **DMoA achieves strong performance on BBH (Section 4.4, Table 2):** DMoA with Claude 3.5 Sonnet as final aggregator achieves 91.85% normalized accuracy on Big Bench Hard, surpassing Sonnet alone (~90.19%, inferred from the reported "92.7% of the performance" relation). The DMoA with Qwen2-72B-Instruct as aggregator (83.63%) also outperforms the base MoA, indicating that the dynamic selection mechanism itself contributes, not just the stronger aggregator.

## Weaknesses

### Fatal
None.

### Major

- **DMoA is specified only at a conceptual level (Section 3.3).** The paper defines f_s (skill identification: "identify the required skills S = f_s(q_j; θ)") and f_m (model selection: "select a subset of models M_S = f_m(S; q_j; θ) ⊆ M") but never concretely specifies how either function works. It refers to Section 4.4 Insights 2–3, but these are high-level empirical observations ("task-specific skills reside in different subspaces," "task-dependent LLM expertise is crucial"), not implementations. Without knowing how skills are extracted from a query or how models are mapped to skills, the core algorithmic contribution of the paper is not reproducible. The paper also does not specify the full model pool M used in the DMoA experiments on BBH — only the final aggregator is named — nor which subset of models is selected for which query types. This is a structural gap, not a missing ablation.

- **No comparison to existing adaptive/router-based ensemble methods.** The paper cites router-based approaches (Lu et al. 2023, Shnitzer et al. 2023, Liu et al. 2023) and notes that DMoA differs by selecting an ensemble rather than a single model, but it does not compare DMoA against any of these methods on BBH or other benchmarks. Since DMoA is functionally an adaptive ensemble selector, evaluating against existing routing/selection baselines is necessary to establish that the dynamic ensemble selection offers advantages over simpler routing strategies.

### Minor

- **No variance or confidence intervals reported for the main BBH results (Table 2).** While the earlier experiments (Table 1) report standard deviations across three runs, the central BBH results have no indication of variability. Given the modest performance differences (e.g., DMoA/Sonnet 91.85% vs. inferred Sonnet alone ~90.19%), the reader cannot assess whether the improvement is statistically reliable.

- **Sentence embedding model e(·) for EigenDivergence is not specified (Section 3.1).** The paper says "we project LLM outputs into a sentence-embedding space as Z = e(S)" but never identifies which embedding model is used. This harms reproducibility of the EigenDivergence metric.

- **"Cross-validation bias" (Insight 1) is used without precise definition.** The term is borrowed from supervised learning but never formally defined in the LLM ensembling context. While the intuition ("reasoning traces validated by multiple hypotheses are more likely to be correct") is clear enough, the connection to standard cross-validation is vague.

- **Sampling parameters (temperature, number of samples) are not reported.** The paper mentions "the same sampling scheme as in Sec. 4.4" (which itself lacks sampling details) but never states the temperature, number of samples per model, or decoding strategy used. These are standard requirements for reproducibility.

### Trivial
None.

## Nice-to-Haves

- A comparison between DMoA's per-query model selection and a simple oracle that always selects the best model for each BBH subtask would help isolate the value of dynamic selection from the value of the aggregator model.
- An analysis showing which models are selected for which query types by the DMoA would make the "skill identification" concept more concrete and provide insight into the routing behavior.
- The mixture optimization algorithm's convergence behavior could be analyzed more formally; the paper already acknowledges it does not guarantee a local optimum.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh Critic's claim that "the SOTA claim on BBH is unsupported and likely false" (Critical Issue 2).** The critic states that "Claude 3.5 Sonnet alone achieving 91.85% normalized accuracy on BBH, and DMoA/Sonnet also achieving 91.85%." This is factually inconsistent with the paper's text, which states DMoA (with Qwen aggregator) achieves 83.63% — "92.7% of the performance of Claude 3.5 Sonnet" — implying Sonnet alone ≈ 90.19%. DMoA/Sonnet achieves 91.85%, which is an improvement. The SOTA claim is internally consistent from the textual evidence. The critic's claim that DMoA without Sonnet (83.63%) is "far below Claude alone" is irrelevant because the paper never claims the Qwen-based DMoA is SOTA; the SOTA claim is specifically for DMoA/Sonnet.

- **Harsh Critic's claim that the mixture optimization algorithm yields "trivial findings" that are "over-interpreted."** The paper explicitly acknowledges that the optimized mixture "is a self-ensemble" (line 151) and frames the algorithm as a tool for investigating trade-offs, not as a sophisticated optimization method. The finding that optimizing for one task hurts another, while intuitive, is empirically demonstrated with concrete numbers across multiple task pairings, which is a valid contribution. This criticism undervalues the empirical demonstration.

- **Harsh Critic's characterization of the ablation results as "well-known" and "not adding surprising new knowledge."** Whether results are "surprising" is subjective; the ablations systematically validate design choices that inform the DMoA architecture and serve a useful purpose within the paper's narrative.

- **Strength Finder's claim about DMoA "outperforming both the base MoA (78.93%) and Sonnet alone (90.19%)"** — these specific numbers cannot be verified from the text alone (the table is an image stripped by the parser), but the textual description is consistent with DMoA/Sonnet (91.85%) outperforming both.

## Novel Insights

The most interesting insight from the cross-referencing of reviews is that the paper's claimed SOTA result (DMoA/Sonnet at 91.85%) appears legitimate based on the paper's consistent internal arithmetic (83.63 is 92.7% of ~90.19). The harsh critic's numerical objection is simply a misreading. However, the DMoA's underspecification is the genuine blocking issue: the paper promises a concrete method but delivers only a conceptual sketch. This suggests the paper would be stronger if it rebranded itself more clearly as an empirical analysis paper (with the DMoA as a proof-of-concept illustration) rather than as a methods paper with an underspecified algorithm. The mixture optimization experiments and the EigenDivergence findings are the paper's strongest empirical contributions regardless of DMoA's specification status.

## Suggestions

1. **Specify f_s and f_m concretely.** The most critical revision: define how skills are extracted (e.g., using a lightweight classifier over task categories, keyword matching, or a learned embedding similarity) and how models are mapped to skills (e.g., based on per-task historical accuracy, or a learned routing function). Without this, the DMoA contribution is not reproducible.

2. **Add router-based baselines to the BBH evaluation.** Compare DMoA against existing LLM routing methods (Lu et al. 2023, Shnitzer et al. 2023) where a single model is selected per query, to demonstrate that ensemble selection adds value over single-model routing.

3. **Report variance or confidence intervals for Table 2.** Even a single additional run or bootstrap estimate would help assess the reliability of the claimed improvement over the baseline models.

4. **Specify the sentence embedding model** used for EigenDivergence and the sampling parameters (temperature, number of samples) for all experiments.

## Score and Decision

The paper makes genuine contributions: a useful unified ensembling framework, a novel diversity metric with clear empirical support for task-dependent trade-offs, and concrete quantitative demonstrations that optimizing for one reasoning type degrades another. The experiments are thoughtfully designed and the ablations are thorough. However, the central weakness is significant: the DMoA — the capstone contribution — is specified only at a conceptual level, with its core functions f_s and f_m left undefined. Combined with the missing comparison to existing routing baselines and the lack of variance estimates for the BBH results, this prevents the paper from being fully acceptable in its current form. The empirical analysis contributions alone (EigenDivergence experiments, mixture optimization, ablations) are valuable enough that the paper is close to the acceptance threshold, but the DMoA underspecification is a structural gap that a rebuttal cannot fully close without specifying the missing functions.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>