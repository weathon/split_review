Now I have all the information I need. Let me compose the final consolidated review.

## Summary

RADAR addresses a significant gap in neural combinatorial optimization for vehicle routing: most neural solvers assume symmetric Euclidean distances, but real-world costs are often asymmetric. The paper proposes two clean, modular modifications to the encoder architecture — SVD-based node initialization to encode static (input-level) asymmetry, and Sinkhorn normalization (replacing softmax) in the attention mechanism to capture dynamic (learned, layer-dependent) asymmetry during representation learning. Extensive experiments on 17 synthetic and 3 real-world asymmetric VRP variants show consistent improvements over strong baselines, with particularly striking zero-shot generalization from size-100 training to size-500/1000 evaluation (e.g., 2.13% gap vs. the best neural baseline's 10.74% on ATSP500).

## Strengths

1. **Principled and modular architectural contributions.** The paper cleanly decomposes the problem into "static asymmetry" (captured by SVD-initialized node embeddings encoding inbound/outbound roles, Definition 1, Algorithm 1) and "dynamic asymmetry" (captured by Sinkhorn-normalized attention providing bidirectional neighborhood context, Algorithm 2). Each component is independently ablated in Table 6, and both contribute meaningfully.

2. **Exceptional zero-shot generalization to larger instances.** Trained only on size 100, RADAR achieves 1.01% gap on ATSP200, 2.13% on ATSP500, and 4.13% on ATSP1000 (Table 1). The best neural baseline (ELG) reaches 10.74% on ATSP500 and many baselines exceed 50% on ATSP1000. This is the single strongest piece of evidence for the method's effectiveness.

3. **Comprehensive experimental scope.** The paper evaluates on 17 synthetic VRP variants (ATSP, ACVRP, 16 RouteFinder variants), three real-world benchmarks (ATSP, ACVRP, ACVRPTW), multiple asymmetry levels, demand distributions, and multitask settings. RADAR consistently outperforms strong baselines across all settings.

4. **Clean, well-executed ablation study (Table 6).** The ablation cleanly separates the contributions of SVD initialization and Sinkhorn normalization, showing each component helps and the combination is best. This avoids the "kitchen sink" concern.

5. **Analysis of coordinates vs. distance structure (Table 4).** The paper shows RADAR without any coordinates (gap 1.49–2.00%) already outperforms RRNCO with coordinates and augmentation (gap 1.80–2.30%), demonstrating the SVD embeddings capture structural information more effectively than coordinate-based cues.

## Weaknesses

### Fatal
None.

### Major
None that threaten the paper's core claims. The following are substantive concerns but do not invalidate the contribution.

### Minor

1. **ELG baseline adaptation, though disclosed, could be presented more carefully.** The paper states: "Since ELG does not natively support asymmetry, we adapt it by replacing its encoder with MatNet using random embeddings and removing Euclidean-specific components." The adaptation is transparently described, and ELG still performs strongly (2nd best on ATSP). However, labeling this modified architecture simply as "ELG" in the table may lead readers to infer the original ELG method's strengths, when the actual comparison is to an asymmetric variant. A more precise label (e.g., "ELG-Adapted" or a footnote on every reference) would improve clarity. This does not inflate RADAR's advantage — if anything, the adaptation is a generous baseline — but it affects interpretability.

2. **The claimed connection between Sinkhorn normalization and "dynamic asymmetry" is intuitively motivated but not empirically analyzed.** The paper argues that Sinkhorn provides bidirectional normalization (rows and columns), making attention scores aware of both nodes' full neighborhoods. The ablation shows it helps (Table 6), and Appendix D.5 shows faster convergence. However, the paper does not directly analyze the resulting attention matrices (e.g., comparing A_{i,j} vs. A_{j,i} asymmetries under softmax vs. Sinkhorn, or attention heatmaps). Such an analysis would strengthen the mechanistic claim. This is a missed opportunity rather than a fatal flaw — the ablation already establishes the practical benefit.

3. **Absence of variability measures for main results.** The paper reports objective values and gaps over 1,000 test instances but does not provide standard deviations, confidence intervals, or interquartile ranges. While the large test set (1k instances) provides some robustness, some in-distribution improvements are modest (e.g., RADAR 0.72% gap vs. ReLD 1.64% on ATSP100), and variance estimates would strengthen the claim of consistent superiority. This is a standard practice gap common in the NCO routing literature.

4. **LKH-10k results are stated as omitted but not shown for context on ATSP.** The paper says "10k omitted for ATSP as performance saturates by 100." Showing even a footnote confirming LKH-1000 already matches LKH-100 on ATSP (or a small-scale verification) would put this reader question to rest. Currently the reader must take this on faith.

5. **The Efficiency Score (max(1 − Gap, 0)) used in Figure 3 is ad-hoc.** It is used only in one figure as a visualization device, so this is minor, but a more standard metric would improve clarity.

### Trivial
- The paper could more clearly separate the definition of static/dynamic asymmetry earlier in the abstract/first paragraph. Currently readers must reach paragraph 3 of the introduction for clear definitions.
- HGS negative gaps in Table 1 could include a more prominent visual indicator (e.g., daggers) that the solutions are infeasible, beyond the note at the bottom.

## Nice-to-Haves

- An attention-map visualization (softmax vs. Sinkhorn) for a small ATSP instance, showing how Sinkhorn spreads attention and whether A_{i,j} ≠ A_{j,i} patterns are learned.
- A sensitivity analysis of SVD truncation rank *k* w.r.t. routing performance (not just Frobenius norm reconstruction). The paper fixes k=10 based on 85% reconstruction quality, but the link to routing performance is not directly shown.
- Testing Sinkhorn *without* distance concatenation (as a complement to the existing ablation which tests Sinkhorn with distance scores) to further isolate its contribution.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"The Sinkhorn claim about Euclidean settings is misleading."** — Removed because the paper's claim is factually correct: in 2D Euclidean settings, distances are fully determined by coordinates, so the distance information is already embedded in node representations. The reviewer misread this section.

2. **"The introduction/abstract lacks precise definitions of static/dynamic asymmetry."** — Removed because the paper defines both terms explicitly (line 29: "Static asymmetry refers to directional discrepancies... Dynamic asymmetry refers to learned, layer-dependent interaction differences..."). The definitions are present.

3. **"HGS negative gaps are confusing."** — Removed because the paper clearly explains in the table note that HGS yields infeasible solutions and is not used for gap computation. The table correctly reports these values with an explanatory footnote.

4. **"SVD initialization's practical value is limited because the model can learn from any initialization."** — Removed because the paper explicitly frames this as an inductive bias (line 99: "the model is theoretically capturing static asymmetry"), not a mathematical guarantee. The ablation (Table 6) and comparison (Table 5) empirically validate its benefit.

5. **"Missing HGS comparison on real-world datasets."** — Removed because the paper explains these results are reused from RRNCO's paper due to incompatible settings. The comparison against RRNCO (which does include HGS in its own paper) is sufficient.

6. **"Gaussian noise may break triangle inequality, making the problem harder in ways unrelated to asymmetry."** — Removed because real-world asymmetric matrices commonly violate triangle inequality. This is a feature, not a bug, of the experimental design.

7. **Various minor formatting/style nitpicks about asterisks, table presentation, etc.** — Removed per hard rules about formatting.

## Novel Insights

The harsh critic raises an important cross-cutting observation that neither reviewer addresses directly: the paper's two proposed components (SVD init and Sinkhorn attention) both serve to embed *global* structural information — SVD via a low-rank decomposition of the full matrix, and Sinkhorn via bidirectional normalization that couples every row-column pair. This suggests a deeper principle: asymmetry-aware routing benefits from representations that encode global matrix structure rather than local neighborhoods. The paper's strongest result (OOD generalization from size 100 to size 1000) arises precisely because SVD captures the global singular vector structure, which is scale-invariant in a way that local k-NN or distance-sampling embeddings are not. This insight — that global decomposition beats local aggregation for asymmetric matrices — is arguably the paper's most important conceptual lesson, and it is worth elevating beyond the experimental sections.

## Suggestions

1. Add standard deviations or interquartile ranges to the main result tables (Tables 1, 3, 5, 6) for at least the in-distribution results, which are most directly comparable across methods.
2. Include a brief analysis of attention matrices (e.g., histogram of A_{i,j} vs. A_{j,i} asymmetry under softmax vs. Sinkhorn for one encoder layer on ATSP) to substantiate the "dynamic asymmetry" mechanism.
3. Rename the ELG baseline to "ELG-Adapted" or add a more prominent footnote in Table 1 to avoid confusion.
4. Consider adding a small experiment (or even a note) verifying that LKH-100 already matches LKH-1000 on ATSP, justifying the omission of LKH-10k.

## Score and Decision

**Calibration anchors:**

| Anchor | Path | Avg Score | Comparison to RADAR |
|--------|------|-----------|---------------------|
| RRNCO | /home/wg25r/review_agent/human_reviews_2026/sKvo9ZZfpe.md | 5.50 | Directly comparable work on asymmetric real-world routing. RADAR has cleaner modular contributions, substantially stronger OOD generalization (2.13% vs 10.74% gap at 5× scale), and broader experimental scope. Stronger paper. |
| UNE-GCN | /home/wg25r/review_agent/human_reviews_2026/UX6JWRJudg.md | 4.40 | GCN-based ATSP solver with limited novelty concerns and weaker empirical validation. RADAR is clearly stronger. |
| PENS | /home/wg25r/review_agent/human_reviews_2026/EQuoft7Yc7.md | 4.00 | Applies positional encodings to Euclidean TSP. Narrower scope and less clear contribution. RADAR is stronger. |
| FrontierCO | /home/wg25r/review_agent/human_reviews_2026/BVprkacwFY.md | 5.33 | Benchmark paper with different contribution type. Both accepted. |
| Efficient TSP (NAR) | /home/wg25r/review_agent/human_reviews_2026/VrXOym8iiA.md | 3.00 | Weaker results, limited evaluation. RADAR is substantially stronger. |

**Originality:** Good — decomposing asymmetry into static (SVD init) and dynamic (Sinkhorn attention) components is well-motivated and the individual techniques are applied in a novel combination for asymmetric VRPs.

**Importance:** High — real-world routing problems are fundamentally asymmetric, and the NCO field has mostly ignored this. The paper tackles a genuine bottleneck.

**Claims supported:** Yes — the core claims are supported by comprehensive experiments, though statistical variability measures would strengthen the evidence.

**Soundness:** 3.5/4 — Clean methodology, extensive baselines, good ablations. Minor concerns about ELG naming and missing variance estimates.

**Clarity:** Good overall, though the static/dynamic framing could be introduced more crisply earlier in the paper.

**Value to community:** High — the SVD-based embedding method for asymmetric matrices is a simple, reusable trick that could benefit other neural routing and graph problems.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>