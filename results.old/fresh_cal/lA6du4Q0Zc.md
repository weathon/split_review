Now I have a thorough understanding of the paper. Let me compose the final consolidated review.

## Summary

The paper proposes NSMP, a neural-symbolic message passing framework for Complex Query Answering (CQA) over Knowledge Graphs. It integrates a frozen pre-trained neural link predictor (ComplEx-N3) with symbolic fuzzy logic inference to answer existential first-order logic queries without training on complex query datasets. The key innovations are: (1) a neural-symbolic message encoding function that combines neural embeddings with symbolic adjacency-matrix-based inference to produce fuzzy-set representations, (2) a dynamic pruning strategy that filters noisy messages from unupdated variable nodes during message passing, and (3) an efficiency advantage over step-by-step neural-symbolic methods, especially on cyclic queries. Empirical results show competitive MRR on benchmark datasets (FB15k-237, NELL995) and substantial speedups (69×–150×) over the FIT baseline on cyclic queries.

## Strengths

1. **Dynamic pruning strategy is novel and validated.** The paper identifies a genuine limitation of prior message-passing CQA models — that initial messages from unupdated variable nodes constitute noise — and proposes a simple, principled solution (only pass messages from updated variable nodes). The ablation study (Table 4) confirms consistent MRR improvements with dynamic pruning across both positive and negative query sets on FB15k-237 and NELL995. This is a clean, well-motivated design that directly addresses an unexplored issue.

2. **Large and well-documented efficiency advantage on cyclic queries.** The complexity analysis (Section 4.3) correctly identifies that step-by-step methods like FIT scale as O(|V|ⁿ) with the number of variables on cyclic queries, while NSMP's message-passing approach avoids this exponential blowup. Figure 3 provides compelling empirical validation with speedups of 69×, 125×, and 157× on "3c" and "3cm" query types. For acyclic queries, the speedup is at least 10×. This is a concrete, practically relevant advantage over the prior SOTA neural-symbolic method.

3. **Strong performance on negative queries among message-passing models.** Table 1 shows NSMP achieves an average MRR of 27.2 on negative queries (BetaE datasets), outperforming LMPNN (24.6) and CLMPT (24.9) by clear margins. This is attributed to the fuzzy-logic-based handling of negation (Section 4.1, Equations 11–12), which prior message-passing approaches handled less effectively.

4. **No training on complex query data required.** NSMP uses a frozen pre-trained neural link predictor and has no trainable parameters (Section 4.2.3). This is a genuine practical advantage over most neural CQA models that require large, resource-intensive complex query training datasets, a point explicitly contrasted in the Introduction.

5. **Clean theoretical framing.** The method is grounded in well-defined formalisms (EFO₁ queries, query graphs, TensorLog-style symbolic inference, fuzzy logic theory) with clear equations for each component. The paper is generally well-structured and the contributions are clearly stated.

## Weaknesses

### Fatal

None.

### Major

1. **Interpretability is claimed repeatedly but never demonstrated.** The abstract, introduction, and conclusion all state that NSMP "provides interpretable answers" and "offers interpretability through fuzzy sets." However, the paper provides zero empirical evidence for this claim: no qualitative examples, no visualizations of fuzzy vectors for variable nodes, no case study tracing how the fuzzy sets correspond to logical reasoning steps. Since interpretability is presented as a key advantage over purely neural models, the complete absence of any demonstration or analysis is a significant gap. At minimum, the paper should show fuzzy-set distributions for variables in representative queries (e.g., a negative query) and explain how they enable a user to understand the model's reasoning.

### Minor

2. **Baseline comparisons do not control for the underlying KG embedding backbone.** The paper reports numbers for a wide set of baselines (BetaE, LogicE, ConE, FuzzQE, GNN-QE, ENeSy, QTO, FIT, etc.) taken directly from original publications, without controlling for whether they use the same pre-trained neural link predictor as NSMP (ComplEx-N3). Some baselines train their own embeddings from scratch; others may use different checkpoints or architectures. This means the reported comparisons conflate the quality of the backbone with the proposed framework. The core comparisons to LMPNN, CLMPT, and FIT — which share the same neural link predictor paradigm — are fairer, but the broader claims of "outperforming most neural and neural-symbolic CQA models" are weakened by this confound. This is a common limitation in the field, but the paper should at minimum acknowledge it explicitly.

3. **Key hyperparameters λ and α are not ablated or justified.** λ (Eq. 19) balances neural and symbolic contributions in the final answer; α (Eq. 9–10) sets the baseline strength for symbolic negation. Neither is subjected to a sensitivity analysis, and their chosen values are not reported. These choices could affect results, and the paper would benefit from simple line plots showing MRR vs. each parameter for representative query types.

4. **Design choices for neural-symbolic fusion and fuzzy logic aggregation are not justified.** The neural-symbolic encoding function ϱ (Eq. 13–14) uses simple addition to fuse the neural fuzzy vector f(ρ) with the symbolic fuzzy vector μ. The node update (Eq. 17) uses product fuzzy logic (Hadamard product) for conjunction. The paper does not discuss why addition is chosen over learned weighting, min, or other fusion strategies, nor why product is chosen over other t-norms (e.g., Gödel, Lukasiewicz). These choices affect how conflicting signals interact. A small ablation comparing fusion/aggregation alternatives would strengthen the paper.

5. **Complexity analysis focus on the dense bound is somewhat misleading.** The paper presents the theoretical complexity as O(|V|²) while acknowledging in one sentence that "both NSMP and FIT can utilize sparse techniques for efficient inference" but then setting that aside "for simplicity." Since the reported speedups (Figure 3) necessarily come from a sparse implementation, presenting only the dense bound as the method's complexity gives an incomplete picture. The paper should either present the sparse complexity (O(|E|·d) or O(nnz(M_r))) as the primary analysis, or at minimum clearly distinguish worst-case from practical complexity.

### Trivial

6. **Ablation results (Table 4) are reported only as averages over query groups, not per query type.** Per-query-type breakdowns would strengthen the claim that dynamic pruning helps across diverse structures. Similarly, Figure 3 reports relative speedup but not absolute wall-clock inference times, which would improve transparency.

## Nice-to-Haves

- A per-query-type breakdown for the dynamic pruning ablation (Table 4).
- Reporting absolute inference wall-clock times in addition to relative speedups (Figure 3).
- A discussion of failure cases — e.g., query types where NSMP underperforms FIT (such as "2in" on NELL995: FIT 0.133 vs NSMP 0.093) with hypothesized explanations.
- Clarification of the sparse implementation details (e.g., CSR/COO storage, sparse matrix-vector products) to bridge the gap between the theoretical complexity analysis and the practical speedups.

## Removed Points

These points from the input reviews were identified and removed with justification:

1. **"The specific similarity function S is not stated" (Harsh Critic).** *Removed because factually wrong.* The paper explicitly states (line 169): "Depending on the selected pre-trained neural link predictor, S can either be an inner-product-based or a distance-based scoring function."

2. **"The 'for the first time' claim about neural-symbolic integration is questionable" (Harsh Critic).** *Removed because the claim is properly qualified.* The paper says "for the first time, integrates neural and symbolic reasoning **within a message passing CQA model**" (emphasis added). FIT and ENeSy are not message-passing-based, so the claim is defensible within its scope.

3. **Strength Finder's claim about "interpretable fuzzy-set representation" as a demonstrated strength.** *Moved here because the weakness (interpretability not demonstrated) overrides the claimed strength.* The paper's *design* supports interpretability in principle, but no evidence is provided, so it cannot be counted as a demonstrated strength.

4. **Generic strengths about the problem being important or the paper addressing an important question.** *Removed as generic/superficial per filtering rules.*

## Novel Insights

The harsh critic's observation that different baselines use different underlying KG embeddings — and that this confounds the comparison — is the most notable insight from the cross-review, though it is a well-known general concern in the CQA literature rather than specific to this paper. More interestingly, the tension between the strength finder's identification of interpretability as a core strength and the critic's correct note that it receives zero empirical validation reveals a pattern: the paper makes structural design choices that support interpretability in principle (fuzzy vectors, explicit symbolic inference), but treats interpretability as an inherent property of the representation rather than something that must be empirically validated through examples or user studies. This is a missed opportunity — the fuzzy-set representations are a genuine differentiator from purely neural methods, and a simple qualitative analysis would substantially strengthen the paper.

## Suggestions

1. **Add an interpretability case study.** Pick one test query (e.g., a negated query like "inp") and show the fuzzy vector for each variable node at different message-passing layers. Visualize entity probabilities in the fuzzy set and explain how the fuzzy logic operators (negation via 1−p, conjunction via product, aggregation via normalization) produce the final ranking. This turns a claim into evidence.

2. **Acknowledge the baseline confound explicitly.** Add a sentence to the experimental section noting that different baselines use different backbone embeddings (or different checkpoints of the same model) and that this should be considered when interpreting comparisons. Better yet, rerun the key baselines that can use ComplEx-N3 (LMPNN, CLMPT, CQD, FIT) with the same checkpoint used for NSMP.

3. **Add ablation or sensitivity analyses for λ and α.** A simple plot showing MRR over a range of λ (e.g., [0, 0.25, 0.5, 0.75, 1.0]) for a few query types would demonstrate robustness. Similarly, report the chosen α value and justify it, or ablate over a few values.

4. **Correct the complexity presentation.** Present the sparse complexity as primary (O(|E|·d) or proportional to the number of nonzeros in the adjacency matrix) and note the dense bound as a worst-case theoretical limit.

5. **Justify or ablate the fusion and aggregation choices.** A small experiment comparing addition vs. weighted average vs. learned gating for neural-symbolic fusion, and product vs. min vs. Lukasiewicz t-norm for conjunction, would directly validate the design decisions.

## Score and Decision

The paper makes a genuine methodological contribution — the neural-symbolic message passing framework with dynamic pruning is novel, well-motivated, and empirically supported by competitive results and substantial efficiency gains on cyclic queries. The weaknesses are real but addressable: the interpretability claim needs empirical backing, several design choices lack justification, and the baseline comparison has a common-but-unacknowledged confound. None of these threaten the core claims; the method is sound and the results (especially the efficiency advantage and negative-query performance) are solid. The paper should be accepted with a major revision to address the above gaps.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>