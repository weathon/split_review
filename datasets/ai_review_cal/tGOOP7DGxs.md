- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5, 5
Now I have sufficient information to compose the final consolidated review.

## Summary

This paper proposes LARGE-GT, a graph transformer framework designed to scale to graphs with millions of nodes. It combines a local module that samples a fixed-size set of 1- and 2-hop neighbors (enriched with precomputed 1-hop and 2-hop context features) with a global module based on a trainable codebook (adapted from GOAT). The key claims are: (1) achieving a 4-hop effective receptive field through only 2-hop operations via the context features, (2) computational complexity independent of graph size, (3) a 3× training speedup on ogbn-products, (4) a 16.8% gain on snap-patents, and (5) a 5.9% gain on ogbn-papers100M over GOAT.

## Strengths

1. **Clear and practical design for scalability**: The framework's complexity is O((3K)² + B), depending only on tunable constants K (sampled neighbors) and B (codebook size), not on graph size N (Section 3.2, Complexity paragraph). This is a formal guarantee that the approach can be applied to graphs with billions of nodes without quadratic growth in computation, directly addressing the core scalability challenge.

2. **Strong empirical performance on snap-patents**: On the non-homophilic snap-patents dataset (2.9M nodes), LARGE-GT-full achieves 70.21% test accuracy, outperforming the best baseline (NAGphormer-constraint at 60.11%) by 16.8% (Table 1b). The large margin suggests the local-global architecture is genuinely beneficial for non-homophilic tasks where local-only information is insufficient.

3. **Demonstrated scalability to 111M nodes**: LARGE-GT-full achieves 64.73% on ogbn-papers100M, a 5.9% improvement over GOAT-full-constraint (61.12%) within a 48-hour computational budget (Table 1c). This demonstrates the framework can be applied to one of the largest publicly available single-graph benchmarks.

4. **Offline sampling design enables distributed training**: The LocalNodes and InputTokens algorithms (Algorithms 1-2) are designed to run independently per node on CPU prior to training, can be parallelized across cores/machines, and do not require the full adjacency matrix on a single machine (lines 123, 180). This is a principled design choice that avoids the memory bottlenecks of traditional GNN training.

5. **Transparent attribution of borrowed components**: The paper explicitly states the global module is "adapted from GOAT" (line 32, line 82) and discusses NAGphormer in related work. The contributions are clearly scoped around the novel tokenization and the combination of components.

## Weaknesses

### Fatal
None.

### Major

1. **Single baseline on ogbn-papers100M**: The flagship large-scale result (5.9% improvement over GOAT-full-constraint on 111M nodes, Table 1c) is compared against only one baseline. The paper states this is "due to computational constraints" (line 295), but without additional comparisons—even GraphSAGE-constraint or NAGphormer-constraint trained to a limited budget—it is difficult to interpret whether the gain reflects genuine superiority or is specific to the GOAT comparison. This weakens the paper's most impressive headline result.

2. **Missing comparison with decoupled/feature-precomputation GNNs**: Methods such as SIGN (frasca2020sign), SAGN, GBP, or SGC (wu2019simplifying) are the most natural competitors for a model that relies on precomputed neighborhood aggregations (C⁰ = ÃH, C¹ = Ã²H). The paper cites these in the related work (line 47) but does not include them as baselines. Since these methods also achieve multi-hop receptive fields through precomputed diffusions without any transformer machinery, their absence makes it unclear whether LARGE-GT's transformer provides meaningful benefits beyond the precomputed features.

3. **Insufficient ablation study**: The paper does not isolate the contribution of the context features (C⁰, C¹) — there is no comparison of LARGE-GT-local with vs. without these features, or using only raw node features of sampled neighbors. The global codebook size B is not reported or ablated. The K-parameter study (Figure 5) is useful but only examines one axis. Without these ablations, the individual contributions of the claimed innovations cannot be assessed.

### Minor

1. **"4-hop receptive field" framing requires clarification**: The mechanism (Algorithm 2) is correctly described: sampling 1- and 2-hop neighbors and retrieving their precomputed 1-hop and 2-hop context features does provide information from up to 4 hops away. However, the terminology "receptive field" could mislead readers into thinking this is a learned 4-hop propagation mechanism (like stacking 4 GNN layers). It is more precisely "access to multi-hop aggregated information via precomputed context features." The paper should clarify this distinction; it does not invalidate the contribution but the framing should be more precise (see lines 9, 31, 175).

2. **Speedup claim is slightly imprecise**: The abstract states "3× speedup" (line 12), and the text says "up to a maximum of 3× times" (line 322). The actual ratio from the figure (GOAT-full-constraint at ~15.2s/epoch vs. LARGE-GT-full at ~5.6s/epoch) is approximately 2.7×. This is a reasonable rounding but should be more precise in the abstract.

3. **Per-epoch time reported, not total training time to convergence**: Figure 4 shows per-epoch wall-clock time, but total training time (hours to reach best validation performance) is not reported. A model with faster per-epoch time but requiring more epochs could be slower overall. For a paper centered on scalability, total training cost is the more meaningful metric.

4. **High variance of LARGE-GT-local on snap-patents**: The local-only variant shows 68.19±3.11 standard deviation across 4 runs on snap-patents (Table 1b), which drops to 0.12 for the full model. The paper does not discuss this instability or whether the runs used different seeds or node subsets.

5. **Performance on ogbn-products is not state-of-the-art**: LARGE-GT-full (79.81%) ranks second behind GOAT-local-constraint (81.17%) and is statistically tied with GOAT-full-constraint (79.88%) (Table 1a). The paper honestly calls this "competitive," but on the homophilic benchmark, the proposed model does not outperform a purely local baseline. This limits the strength of the claim that the 4-hop context and global module are beneficial in all settings.

### Trivial
- The abstract phrasing "3× speedup and 16.8% performance gain on ogbn-products and snap-patents compared to their nearest baselines respectively" is ambiguous — the speedup applies to ogbn-products and the gain to snap-patents, but the sentence structure could mislead readers into thinking both metrics apply to both datasets.

## Nice-to-Haves
- Report the actual time/cost of the offline sampling step (Algorithm 1) and the storage cost of the precomputed context features C (for ogbn-papers100M, C would be N × 2 × D — at D=128 that is ~28 GB). The paper states the offline step's complexity is not a concern, but concrete numbers would be informative.
- Include a comparison showing original (non-constrained) performance of baselines for context, to quantify how much the 2-hop constraint degrades each method.
- Report total training time to convergence (hours) in addition to per-epoch time.
- Study the sensitivity of the codebook size B in the global module.

## Removed Points
The following points from the reviewers are removed (with justification):

1. **"Missing hyperparameters/details in main text"** (e.g., hidden dimension D, number of heads, codebook size B, positional encodings): The paper explicitly references "Section sec:hyperparameters" (line 222-223) for these details, which is in the appendix. Per instructions, the appendix was stripped by the parser and exists in the original submission. This criticism is removed.

2. **"Missing appendix content"**: Several criticisms reference missing proofs, tables, or details that are in the appendix. Per hard rules, these are removed.

3. **"Global module novelty questioned"**: The paper is transparent that the global module is "adapted from GOAT" (line 32). This is not a weakness — the paper clearly scopes its contribution as the combination + local module. The harsh critic's framing of this as a weakness is removed.

4. **"Related work gaps" (general)**: The harsh critic claimed the paper "does not discuss precomputed neighborhood aggregation methods (SIGN, SAGN, GBP, etc.)." In fact, the paper does cite these at line 47 ("Information propagation prior to or after the training stage (gasteiger2018predict, wu2019simplifying, frasca2020sign)"). The specific claim of omission is factually wrong. However, the related point about missing these as baselines in experiments is retained as a Major weakness.

5. **"The 4-hop receptive field conflates precomputed static aggregations with learned receptive field"** framed as a fatal flaw: The paper's claim is about the information accessible to the model, not about learned propagation. The mechanism (Algorithm 2) is mathematically sound — precomputed or not, the transformer attends to tokens carrying information from up to 4 hops away. This is a valid design choice, not a fundamental error. The milder framing (clarification needed) is retained in Minor weaknesses.

6. **"Weakness: NO distributed training experiments"**: The paper discusses distributed training as a design principle (D2, Section 3.1) and states the framework can be parallelized "in principle" (line 180, 319). It does not claim to have conducted distributed experiments. The lack of distributed experiments is outside the paper's stated scope.

7. **"Weakness: 2-hop limit not justified"**: The paper provides detailed justification at lines 80-81, explaining the O(dˡ) complexity of l-hop retrieval and citing prior work that adopts the 2-hop limit. The criticism that this is "self-imposed" and "not justified" ignores this explicit justification.

8. **Several generic/formulaic strengths from the Strength Finder** (e.g., "the paper addresses a genuinely difficult problem") are dropped as they are superficial and lack specific evidence.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. Add at least 2-3 additional baselines on ogbn-papers100M (e.g., GraphSAGE-constraint, NAGphormer-constraint) trained to a limited budget to strengthen the large-scale result.
2. Include decoupled GNN baselines (SIGN, SAGN) as they are the most natural competitors using precomputed aggregations.
3. Add an ablation comparing LARGE-GT-local with vs. without context features C⁰, C¹ to isolate their contribution.
4. Report the codebook size B used in experiments and study its sensitivity.
5. Clarify the "4-hop receptive field" terminology as "access to multi-hop aggregated features through precomputed context" to avoid confusion with learned multi-layer propagation.
6. Report total training time to convergence in addition to per-epoch time.
7. Make the speedup claim in the abstract more precise (e.g., "up to 2.7×" instead of "3×").
