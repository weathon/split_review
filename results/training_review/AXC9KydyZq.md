Now I'll produce the consolidated final review.

## Summary

This paper addresses mixture graph matching and clustering (MGMC), a scenario where graphs from multiple categories must be jointly matched and clustered. It introduces M3C, a learning-free solver using a Minorize-Maximization framework with a relaxed cluster indicator, and UM3C, an unsupervised extension with edge-wise affinity learning and pseudo-label selection. The paper is motivated by a practical and underexplored problem, and the proposed methods show clear improvements over prior unsupervised MGMC work (GANN) on both accuracy and runtime.

## Strengths

- **First MM-based alternating framework for MGMC with a principled optimization structure.** The paper constructs a Minorize-Maximization alternation between matching and clustering (Section 4.1), providing a clear optimization framework where prior works (DPMC, GANN) lacked convergence analysis. The MM surrogate construction is a nontrivial adaptation to the MGMC setting.

- **Relaxed cluster indicator yields measurable improvements over hard clustering.** Proposition 1 correctly identifies that hard clustering fixes the optimization space prematurely. Empirically, M3C (with relaxed indicator) outperforms M3C-hard by 4.6% MA and 5.6% CA on Willow ObjectClass (3×8, 0 outliers), and the gap widens to 7.7% CA with 2 outliers (Table 1). This cleanly demonstrates the benefit of the relaxation.

- **UM3C convincingly outperforms the only peer unsupervised method GANN by large margins.** On Willow ObjectClass with 0 outliers, UM3C achieves MA 0.955 vs. GANN 0.896 (+5.9%); with 2 outliers, MA 0.858 vs. GANN 0.610 (+24.8%). On Pascal VOC, UM3C is 1.8–2.0× better in MA and 5–6× faster. These are substantial, reproducible gains that clearly establish UM3C as the new state-of-the-art for unsupervised MGMC.

- **Edge-wise affinity learning plus pseudo-label selection provides a sound unsupervised pipeline.** The affinity loss (Eq. 7) decouples learning from the solver, avoiding the conflation problem in prior work. The ablation (Fig. 2) shows that pseudo-label selection yields ~5% improvement in early training accuracy, and edge-wise affinity learning adds further gains. The pipeline is modular and conceptually clear.

- **Significant efficiency advantage.** UM3C is 2.5–6× faster than GANN on Willow (e.g., 3.3s vs. 20.6s with 2 outliers) and over 6× faster on Pascal VOC. Combined with its accuracy advantage, this makes the method practically appealing.

## Weaknesses

### Fatal

None. The paper makes a real contribution to an underexplored problem; the issues below are serious but addressable.

### Major

- **Overclaim in the contribution list and conclusion, contradicted by the paper's own results.** The contribution list states: "*namenn* even outperforms supervised models such as BBGM and NGM, establishing itself as the top-performing method for MGMC on the utilized public benchmarks." This is false for Pascal VOC, where supervised BBGM/NGMv2 achieve MA 0.79–0.81 while UM3C achieves only 0.49–0.50 (Table 2). The conclusion similarly states "outperform all state-of-the-art methods." These claims are unsupported by the full set of results presented in the paper. The claim is true for Willow ObjectClass, but the phrasing "the utilized public benchmarks" (plural) is misleading. The abstract is more measured ("outperforms state-of-the-art graph matching and mixture graph matching and clustering approaches") but still ambiguous since "state-of-the-art" could be read as including supervised methods.

- **Convergence guarantee as stated in Section 4.1 applies to the hard clustering variant, while the actual M3C algorithm (Section 4.3) uses the relaxed indicator.** The MM framework and the monotonic increase guarantee (Eq. 4) are derived for $f(\mathbf{x}) = \mathcal{F}(\mathbf{x}, h(\mathbf{x}))$ where $h$ finds the optimal hard cluster division satisfying the strict transitive constraints of Eq. 1. The M3C algorithm replaces $h$ with $\hat{h}$ (ranking-based selection via the relaxed indicator). The paper does not explicitly prove in the main text that the relaxed version inherits the same monotonic convergence property, nor does it explain how the relaxation affects the minorization condition. The claim "first theoretically convergent algorithm for MGMC" conflates the formulation for which convergence is proved (hard clustering MM) with the formulation actually used (relaxed indicator). The appendix (stripped from the review copy) may contain additional justification, but the main text should at minimum clarify the precise scope of the guarantee.

### Minor

- **No explicit definition of what "outliers" means in the outlier experiments.** The paper tests with "2 outliers" and "4 outliers" on Willow ObjectClass (Table 1) but never specifies whether outliers are graphs from unseen categories, graphs with perturbed features, or pure noise graphs. This makes the experiment difficult to reproduce or interpret. (The setting follows prior work by Wang et al. [GANN, 2020], but a brief definition is still needed.)

- **No explanation of how clustering metrics (CA, CP, RI) are derived for methods that do not natively perform clustering (RRWM, MatchLift, CAO-C, MGM-Floyd, DPMC).** These methods produce pairwise matchings but no explicit cluster assignment. The paper should state what post-processing (e.g., spectral clustering on the affinity matrix) is used to obtain cluster divisions from these methods, as the clustering results depend on that choice.

- **The outlier comparison against supervised BBGM/NGMv2 is not controlled for training distribution.** Supervised methods were presumably trained on clean data without outliers, so their degraded performance in the outlier setting is expected and does not constitute evidence that UM3C is "more robust" than supervised learning *per se* — only that it is more robust than supervised models trained without outlier augmentation. The paper should acknowledge this caveat. (The core comparison against GANN — the only other unsupervised MGMC method — is clean and remains strong.)

- **No discussion connecting relaxed-indicator solutions back to the original hard MGMC problem.** The relaxation replaces transitive closure constraints ($c_{ik}c_{kj} \leq c_{ij}$, SCC(C)=N_c) with simple cardinality constraints on selected pairs. The paper does not discuss whether (or how) the relaxed solution can be post-processed into a valid hard clustering of the original problem, or whether the solutions to the relaxed problem empirically correspond to meaningful clusterings.

### Trivial

- The "Additional Experiments" section (Section 6.3, line 331) is a placeholder referencing subsections that appear in the (missing) appendix. These should either be briefly summarized in the main text or properly structured.

## Nice-to-Haves

- A direct comparison of M3C (learning-free, hand-crafted K) vs. UM3C (with learned K) as a standalone ablation to quantify the benefit of edge-wise affinity learning separately from the solver change. (Table 1 provides this comparison indirectly: M3C MA=0.884, UM3C MA=0.955 → +7.1%, but this is not explicitly discussed as an ablation.)

- Sensitivity analysis of the hyperparameter $r$ (relaxation ratio) on matching accuracy and clustering quality across datasets, to help practitioners choose this value.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Convergence guarantee is for a different problem" — the part claiming this is a "fatal" flaw and that the convergence guarantee is "trivial."** The critic overstates severity: the MM framework structure is sound, the relaxed algorithm follows the same alternating optimization pattern, and the appendix (stripped from the review copy) likely contains the relevant proof. The issue is a clarity/rigor gap in the main text, not a fatal flaw. Downgraded to Major.

- **"Affinity loss is O(n^4) per graph pair, computationally prohibitive (160k×160k for 20 nodes)."** The critic's math is incorrect. $\text{vec}(\mathbf{X})$ has size $n_1 n_2$, so for $n_1=n_2=20$ the outer product is $400 \times 400 = 160{,}000$ entries — entirely manageable. O(n^4) scaling is correct in the abstract sense, but for the graph sizes used in the paper (~10–20 nodes) the computation is not prohibitive. Removed as factually wrong.

- **"Ablation does not separate M3C solver from learning components."** The baseline in the ablation uses M3C as solver with hand-crafted features, and components are added incrementally. The M3C-vs-UM3C comparison is available from Table 1 (M3C MA=0.884, UM3C MA=0.955). The ablation isolates the learning components correctly. Removed.

- **"Low CA/CP for supervised methods indicate failure."** The paper includes these metrics for completeness; the critic acknowledges these methods are not designed for mixture data. Low clustering scores are expected and the paper does not claim otherwise. This is not a genuine weakness. Removed.

- **Various minor presentational/formatting nitpicks.** Removed per instructions.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Revise overclaims.** Remove or carefully qualify the statement that UM3C is the "top-performing method for MGMC on the utilized public benchmarks." The claim should be scoped to (a) unsupervised methods, or (b) Willow ObjectClass specifically, or (c) prefaced with "on Willow ObjectClass, UM3C even outperforms supervised methods." Similarly ensure the abstract and conclusion accurately reflect that on Pascal VOC, supervised methods substantially outperform UM3C in matching accuracy.

2. **Clarify the scope of the convergence guarantee.** Explicitly state that the convergence proof in Section 4.1 applies to the hard-clustering MM framework, and separately either (a) prove that the relaxed algorithm inherits the same guarantee, or (b) state the guarantee precisely for the relaxed formulation. The phrase "first theoretically convergent algorithm for MGMC" should specify which formulation's convergence is proved.

3. **Define outliers** in the experimental setup (Section 6.1) and **explain how clustering is extracted** from non-clustering baselines (RRWM, MatchLift, etc.).

4. **Add a brief discussion** (even a paragraph) connecting relaxed-indicator solutions to hard clustering — e.g., show empirically that the top-ranked pairs selected by the relaxed indicator correspond to within-cluster pairs, or describe a post-processing step.

## Score and Decision

The paper tackles an important and underexplored problem with a principled framework and strong empirical results against relevant baselines (especially GANN). The unsupervised pipeline with edge-wise affinity learning is novel and the results are compelling. However, the overclaim about surpassing supervised methods on "the utilized public benchmarks" (contradicted by the Pascal VOC results) and the gap between the convergence claim and what is explicitly proved in the main text are significant issues that undermine the paper's credibility. These are fixable with careful revision, but in their current form they misrepresent the paper's achievements.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>