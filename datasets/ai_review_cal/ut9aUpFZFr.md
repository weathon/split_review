- Decision: Reject
- Avg Score: 4.67
- Scores: 5, 6, 3
Now I have a thorough understanding of the paper. Let me produce the consolidated review.

## Summary

COINs introduces a model-based method for accelerating link prediction and query answering on knowledge graphs by partitioning entities into communities and performing a two-step evaluation: first predict the target node's community, then search for the correct entity only within that community. The paper provides a complexity analysis (Proposition 1) showing that with optimal partitioning this yields a quadratic reduction in inference cost, along with empirical results across 4 embedding models and 3 datasets demonstrating 3–10× acceleration with moderate performance loss.

## Strengths

- **Clear complexity analysis with actionable bounds (Proposition 1).** The derivation in Section 2.3.2 precisely quantifies the number of embedding computations as Σ_k (K + |C_k|)|E_k^test|, establishes upper and lower bounds, and shows that optimal partitioning (K = O(√|V|) with equal-sized groups) yields a quadratic reduction in inference cost. This is the paper's strongest formal contribution and directly supports the acceleration claim.

- **Novel and well-motivated integration of community detection into KG inference.** Applying Leiden communities (with CPM modularity) to structure the prediction pipeline is a principled model-based alternative to distributed-system approaches (PyTorch-BigGraph, DistDGL). The paper's analysis of edge locality (Section 2.3.3) and the role of the resolution hyperparameter (Figure 2) provides useful guidance for practitioners deploying the method.

- **Multi-model, multi-dataset empirical validation with transparent discussion of failure cases.** Results span 4 embedding methods (TransE, DistMult, ComplEx, RotatE) on 3 datasets (FB15k-237, WN18RR, NELL-995), with acceleration factors of 3–10×. The paper acknowledges that performance degrades on dense graphs like FB15k-237 and that TransE/DistMult struggle with community prediction there (Table 3, Section 4.2). This transparency is commendable.

## Weaknesses

### Fatal
None.

### Major

- **Proposition 2's theoretical derivation is based on an inappropriate model of the evaluation procedure.** The paper models the number of edges evaluated before a correct hit (H_k) as a geometric random variable, but the COINs two-step procedure does not sequentially sample edges — it evaluates all candidates in the predicted community in a single pass and then ranks them. The geometric distribution does not match the rank-based evaluation procedure. The resulting inequality (ε < 1 − COINs_cost/baseline_cost) is conceptually intuitive but the derivation from the geometric assumption is not sound. Since the abstract claims "theoretically justified criteria for gauging the applicability of our approach," this gap undermines a stated contribution. The paper would be better served by either dropping Proposition 2 or replacing it with a valid expected-rank analysis.

- **The method suffers severe performance degradation on dense graphs, with no thorough analysis of when it should not be used.** On FB15k-237, TransE's Hits@10 drops from 47.2 to 13.2 (72% relative loss) and DistMult's from 33.6 to 17.8 (47% relative loss). The paper acknowledges poor community prediction as the cause but does not provide a practical diagnostic — e.g., a measure of community detection quality or cross-community edge density — that would let practitioners know upfront whether COINs is suitable for their graph. Without such guidance, the method's applicability is unclear beyond the three tested datasets.

### Minor

- **Training cost is not reported, yet the paper frames COINs for "low-resource settings."** The paper only reports evaluation-time acceleration. COINs introduces multiple sub-embedders (community-level, per-community intra, inter-community) with a more complex loss requiring backpropagation through all components, and memory increases by 1.5–2× (Table 2). Training time, convergence speed, and total (training + amortized inference) cost are never compared to baselines. For a method targeting resource-constrained scenarios, this is a meaningful gap — though the paper's stated focus is specifically on evaluation cost.

- **Architecture of sub-embedders and integration with base models is underspecified.** Algorithm 1 defines f_C, f_k, f_* as "sampled from ℱ" (the class of KG embedding models), but it is never concretely shown how e.g., TransE's scoring function is instantiated within each sub-embedder. The statement "equal hyperparameters" (Table 3 caption) is vague — it is unclear which hyperparameters are shared and whether COINs's different architecture might require different optimal settings. A concrete example (e.g., TransE-COINs equations) would significantly improve reproducibility.

- **No confidence intervals or significance tests for main results.** Many performance differences in Table 3 are small (e.g., RotatE on FB15k-237: MRR 29.2→29.6). Without error bars over random seeds or a significance test, it is impossible to assess whether these differences are meaningful or noise. The paper states results are from 5 random seeds but does not report variance.

- **The "convexity preserves training stability" claim is unsubstantiated.** Section 3.2 states that "the convexity of the final embedding refinement will preserve training stability," but the convex combination (Softmax weights applied to embedding vectors) is only convex in the mixing weights — the underlying sub-models (f_C, f_k, f_*) are non-convex neural embedding models. This claim about stability is not supported by any analysis or experiment.

### Trivial
None.

## Nice-to-Haves
- Replace Proposition 2 with a valid expected-rank analysis or drop it and let the empirical results speak for themselves.
- Report wall-clock training and total (training + inference) time, with a break-even analysis for when COINs becomes beneficial.
- Add confidence intervals or error bars to Table 3 results.
- Provide an ablation study isolating the effects of (a) community-level only, (b) intra-community only, (c) the full COINs architecture.
- Analyze sensitivity to the α (loss weight) hyperparameter.

## Removed Points
These points were flagged for removal; treat them with caution:

1. **"Proposition 2 is a tautology providing no actionable guidance"** — While the geometric model assumption is flawed, the resulting inequality ε < 1 − cost_ratio is not a tautology; it is a conceptually meaningful (if imprecisely derived) condition. The criticism overstates the problem. The point is retained in weakened form under Major weaknesses.

2. **"Oracle evaluation in Figure 3 bottom row is disingenuous / masks failures"** — The paper is transparent about this being an analysis that "removes the impact of the community prediction performance." This is a legitimate ablation to isolate the source of error. The paper does not claim the bottom row represents achievable performance. Removed as factually inaccurate criticism.

3. **"Several rows highlighted in Table 3 even when relative error >10%"** — The caption states "Highlighted values indicate the superiority of COINs **or** a relative error lower than 10%." Values showing improvement (superiority) are highlighted regardless of the 10% threshold. The critic misread the caption. Removed.

4. **"Baseline results from Sun et al. (2019) may have been optimized differently"** — Speculative and not anchored in any specific discrepancy in the paper. Removed.

5. **"No hyperparameter details (epochs, batch size, learning rate schedule)"** — The instructions require removing nitpicks about undisclosed hyperparameters. The paper does provide optimizer (Adam), regularization (ℓ2), and early stopping details. Removed.

6. **"The paper should have compared to random subsampling baselines"** — This is a suggestion for additional experiments, not a weakness of the existing evaluation. Moved to Nice-to-Haves.

7. **"Proposition 1's bounds are not surprising"** — A subjective value judgment, not a weakness. Removed.

8. **"No analysis of community detection quality (modularity, NMI)"** — The paper reports community-level Hits@1 as a quality measure (Table 3 footnote) and discusses edge locality. This is sufficient for its purpose. Removed.

## Novel Insights
None beyond the paper's own contributions. The reviewers raise no genuinely novel observation about the method or problem that the authors did not already articulate.

## Suggestions
1. **Replace Proposition 2** with a clean expected-rank analysis that directly relates community prediction accuracy, community size distribution, and node-level rank distribution to the expected number of candidate evaluations. Alternatively, remove Proposition 2 entirely and frame the paper's theoretical contribution as Proposition 1 alone (which is sound).
2. **Provide a concrete instantiation** — write out the equations for at least one base model (e.g., TransE-COINs) showing exactly how f_C, f_k, and f_* are parameterized and how the scoring functions compose.
3. **Report training wall-clock time** per epoch and total across all random seeds, alongside evaluation time, to give a complete resource picture.
4. **Add a practical applicability criterion** — e.g., a threshold on cross-community edge fraction or community prediction accuracy below which COINs is unlikely to be beneficial — to help practitioners decide whether the method suits their graph.
5. **Include error bars** on the Table 3 results (standard deviation across seeds) so readers can assess the significance of small differences.
