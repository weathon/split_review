Now I have a thorough understanding of the paper and all reviewer claims. Let me compose my final consolidated review.

## Summary

This paper introduces GraphGT, a Graph Transformer framework designed for single large graphs with millions to hundreds of millions of nodes. The core contributions are: (1) an offline 2-hop neighbor sampling strategy combined with precomputed 1-hop and 2-hop context features (matrices C⁰ and C¹) that give an effective 4-hop receptive field through attention on the sampled tokens; and (2) a global module using a trainable codebook (adapted from GOAT) for approximate all-graph context. The framework is evaluated on ogbn-products, snap-patents, and ogbn-papers100M, reporting a 3× training speedup over the closest architectural baseline on ogbn-products, a 16.8% improvement over the best baseline on snap-patents, and a 5.9% improvement on ogbn-papers100M.

## Strengths

- **Novel tokenization achieves a 4-hop receptive field with only 2-hop operations.** The `InputTokens` algorithm (Algorithm 2) constructs each sampled neighbor's token from its own 1-hop and 2-hop context features (C⁰, C¹). As explained in Section 3.2, this gives the central node access to information up to 4 hops away while requiring only 2-hop neighbor retrieval, cleanly addressing the scalability constraint (D2) while boosting local representation capacity.

- **Strong empirical gains on two of three large benchmarks.** Table 1 shows that GraphGT-full outperforms the best scalable baseline by **16.8%** on snap-patents (70.21 vs. 60.11) and by **5.9%** on ogbn-papers100M (64.73 vs. 61.12). These results demonstrate that the framework delivers on its core claim of scaling GTs to massive graphs without sacrificing accuracy on non-homophilic and homophilic tasks alike.

- **Demonstrated training speedup over comparable architectures.** Figure 2 shows GraphGT-full trains faster per epoch than GOAT-full-constraint (e.g., ~70s vs. ~205s on ogbn-products). The paper attributes this to the 2-hop constraint and the O((3K)²) local module complexity, which is independent of graph size. This supports the scalability design goal (D2).

- **Controlled comparison validates the local+global design.** GraphGT-full consistently beats GraphGT-local (e.g., +1% on ogbn-products, +2% on snap-patents in Table 1), confirming the value of the global module (D1).

## Weaknesses

### Fatal

None.

### Major

None. The identified weaknesses are addressable or partial; none invalidate the paper's core contributions.

### Minor

- **The claimed 4-hop receptive field benefit is not isolated via ablation.** The paper attributes performance gains partly to the 4-hop receptive field enabled by context features (C⁰, C¹). However, no ablation compares GraphGT-local with vs. without these context features while keeping sampling and attention identical. The existing comparisons (GraphGT-local vs. GOAT-local-constraint) differ in both sampling strategy and tokenization, making it impossible to attribute improvements specifically to the increased receptive field. Without this ablation, it is unclear whether gains come from the broader field, from the additional feature dimensions, or from the different sampling. (Note: this is a gap but not fatal—the overall framework still works and the 4-hop mechanism is a principled design choice.)

- **Offline preprocessing cost is not concretely documented, leaving the full scalability picture incomplete.** The framework depends on two offline steps: (i) enumerating 1-hop and 2-hop neighbors for all nodes (Algorithm 1), and (ii) computing context matrices C⁰ = ÃH and C¹ = Ã²H. For ogbn-papers100M (111M nodes, 1.6B edges), these are nontrivial operations. The paper states these steps "can be parallelized" and the graph "can be distributed," but reports no actual runtime, peak memory, or hardware specifications. While the fact that results were obtained on ogbn-papers100M implies the preprocessing was feasible, omitting these resource numbers makes the scalability argument less sharp than it could be.

- **Selectively framed claims in the abstract and introduction.** The abstract claims "3× speedup and 16.8% performance gain on ogbn-products and snap-patents compared to their nearest baselines respectively." The 3× speedup on ogbn-products compares GraphGT-full to GOAT-full-constraint (both ~79.8% accuracy), but the *best-performing* baseline on ogbn-products is GOAT-local-constraint (81.17%), against which GraphGT-full is slower and less accurate. The paper's own discussion (Section 4.2) presents the full picture honestly, but the front-matter phrasing could mislead a reader into thinking the 3× speedup comes at no accuracy cost on this dataset.

- **High variance of GraphGT-local on snap-patents (68.19±3.11).** The standard deviation of 3.11 across 4 runs is much larger than for the full model (0.12) and larger than all baselines. This suggests sensitivity to initialization or sampling stochasticity in the local-only configuration, which merits discussion.

- **Global module description is underspecified in the main text.** The GlobalModule is described as "adapted from [GOAT]" with no details on codebook size, training procedure, or how its output combines with the local module (beyond concatenation shown in Eqns. 5–6). While these details may appear in the (parser-stripped) appendix, the main text should at minimum state the codebook size and combination mechanism for self-contained readability.

### Trivial

- The complexity analysis states O((3K)²) without specifying single-head vs. multi-head attention. Clarifying would prevent ambiguity.
- Algorithm 1's Step 3 ("1 and 2 hop neighbors of node i") does not specify whether the full 2-hop set is materialized or sampled on-the-fly for high-degree nodes, which matters for implementation.

## Nice-to-Haves

- Report concrete resource usage (time, peak memory, number of CPUs/GPUs) for the offline preprocessing steps on ogbn-papers100M, to fully substantiate the scalability claim.
- Include a few more baselines on ogbn-papers100M (e.g., GraphSAGE-constraint) if computational budget allows, to strengthen the comparison on the largest dataset. (The current single-baseline comparison is acknowledged due to constraints but limits the strength of the evidence.)
- A brief paragraph discussing the limitations of the offline steps (e.g., memory for C⁰ and C¹ on terabyte-scale graphs) would improve the paper's tone.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Key full (unconstrained) results are omitted"** — The paper's experimental design explicitly constrains all baselines to 2 hops (D2). Requesting unconstrained results contradicts the paper's scope, which is evaluating under a specific scalability constraint. This is scope creep.
- **"Table 1 caption mentions colors for ranking, but the table is in black and white"** — A pure formatting/display artifact of the text extraction, not an author error.
- **"Missing evaluation on ogbn-papers100M for more baselines... The 'computational constraints' argument is weak"** — The paper acknowledges the computational budget (48h) and selects the strongest baseline. Demanding more baselines is a wishlist item, not a structural flaw.
- **"GlobalModule codebook size, attention heads not specified"** — These details were likely in the (parser-stripped) appendix (Section \ref{sec:hyperparameters}). The rule against penalizing missing appendix content applies here.
- **"The authors should add X" style suggestions throughout** — Most are reasonable suggestions for strengthening but do not constitute weaknesses.

## Novel Insights

The most striking finding is the performance asymmetry across datasets: GraphGT-local (68.19%) outperforms GOAT-local-constraint (40.95%) by 27 absolute points on snap-patents (non-homophilic), yet underperforms GOAT-local-constraint on ogbn-products (78.95% vs. 81.17%, homophilic). This suggests the context-feature-based tokenization disproportionately helps on non-homophilic tasks where local-only aggregation fails, while on homophilic tasks the extra context may dilute the signal from immediate neighbors. The high variance of GraphGT-local on snap-patents (±3.11) further hints that the local module's benefit is sensitive to the sampled neighborhoods on this dataset. These observations could guide more nuanced designs that adaptively weight context features based on graph homophily.

## Suggestions

1. Add an ablation comparing GraphGT-local with and without the context features (C⁰, C¹) while keeping sampling and architecture identical. This would directly isolate the 4-hop receptive field's contribution.
2. Report the hardware configuration and wall-clock time for the offline preprocessing steps (Algorithm 1 + context matrix computation) on at least one dataset. Even a brief statement ("10 minutes on 64 CPU cores for ogbn-products") would substantially strengthen the scalability narrative.
3. Tighten the language in the abstract: instead of "3× speedup ... on ogbn-products compared to their nearest baselines," specify "3× speedup over GOAT-full-constraint on ogbn-products" to avoid misleading readers about which baseline is being compared.
4. Discuss the high variance of GraphGT-local on snap-patents and whether it stems from the sampling randomness or the model's sensitivity to token order.

## Score and Decision

The paper makes a genuine contribution: a principled framework for scaling Graph Transformers to very large graphs, with strong results on snap-patents and ogbn-papers100M. The weaknesses are real but neither fatal nor structural. The missing ablation and incomplete preprocessing documentation are addressable gaps rather than flaws in the method itself. The selective framing in the abstract is a presentational issue that can be fixed with rewording. Overall, the paper has clear value to the community working on large-scale graph learning.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>