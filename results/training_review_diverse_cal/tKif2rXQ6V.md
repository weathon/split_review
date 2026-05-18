I have thoroughly analyzed the paper and all reviewer claims. Here is my consolidated review.

---

## Summary

This paper introduces SteBen, a large-scale benchmark dataset for the Steiner Tree Problem (STP) containing 1.28 million instances across four graph models (Erdős–Rényi, Watts–Strogatz, Random Regular, and Grid) with node sizes up to 1000. The authors also implement four NCO baselines spanning the autoregressive/non-autoregressive and supervised/reinforcement learning quadrants, and provide a comparison of these methods alongside classical solvers (SCIP-Jack and a 2-approximation heuristic). The paper claims that solvers trained on SteBen generalize to real-world instances without fine-tuning.

## Strengths

- **First large-scale, exact-solution dataset for STP.** SteBen provides 1.28M instances across four graph models and multiple sizes (10–1000 nodes), directly addressing the critical limitation of prior datasets like SteinLib (which offers only a few dozen instances per scenario). This is a genuine contribution that fills an important gap in the NCO literature (Section 4.1).

- **Systematic quadrant-based comparison of NCO paradigms on STP.** The paper is the first to compare autoregressive vs. non-autoregressive and supervised vs. reinforcement learning methods on STP, organizing them into four methodological quadrants. The qualitative discussion (Section 6) identifies that non-autoregressive models tend to outperform autoregressive ones on STP (attributed to a smoothing problem in partial-solution embeddings), providing actionable guidance for future work.

- **Training sample efficiency analysis.** The paper quantifies how supervised learning methods degrade with reduced training data (Figure 2, Section 6), showing DIFUSCO is more robust than PointerNet in low-sample regimes. This analysis leverages the dataset's size and provides practical guidance for resource-constrained settings.

- **Careful adaptation of diverse NCO architectures to STP.** The paper modifies PtrNet with level-order tree traversal and GNN embeddings for tree-structured outputs, adjusts DIFUSCO's edge feature initialization to encode cost and terminal information, and adapts DIMES with STP-specific decoding (Section 4.2). These adaptations are non-trivial and documented in sufficient detail for reproducibility.

## Weaknesses

### Fatal

None. The paper's primary contribution — the dataset itself — is presented with sufficient detail (graph types, sizes, generation procedure, terminal probabilities, edge cost distributions) to be evaluated and used. No single flaw invalidates the entire paper.

### Major

- **The real-world generalization claim is entirely unsubstantiated.** The abstract states that "solvers trained on our datasets generalize well to real-world instances without fine-tuning, proving its practical utility," and this is listed as a numbered contribution (bullet 3, Section 1). Yet the paper contains **no description whatsoever** of any real-world dataset, experiment, result, or evaluation supporting this claim. No real-world instances are named, no quantitative results are shown, and no comparison to baselines on such instances is presented. The Limitations section (line 182) even acknowledges that "our study focuses on the unconstrained version, leaving constrained versions for future work," which is inconsistent with the claimed demonstration. This is a central claim presented as a demonstrated result that has zero evidence in the paper body. The authors must either provide the experimental evidence or retract the claim.

- **The provenance of the "optimal solutions" is undocumented, undermining the dataset's core value proposition.** The paper repeatedly describes the dataset as containing "exact solutions" and "optimally solved samples" (abstract, lines 16, 108, 189), yet Algorithm 1 describes only graph generation — it says nothing about how the optimal Steiner tree was computed. Crucially: (a) no solver is specified (was SCIP-Jack used? A custom MILP? A different exact algorithm?), (b) no runtime limits are reported, (c) no optimality verification procedure is described, and (d) the paper itself notes (line 92) that "the STP is NP-hard, making it infeasible to find exact solutions for large instances" — which would include the test instances of 200, 500, and 1000 nodes. If the ground-truth labels for larger instances are only near-optimal, the supervised learning training targets and evaluation metrics are unreliable, and the Gap metric relative to these "optimal" solutions becomes uninterpretable. For a benchmark whose primary contribution is providing exact solutions, this documentation gap is serious.

- **The main quantitative comparison (Table 1) is absent from the provided text.** Section 5.2 ("RESULTS") contains a heading and no content — no tables, no figures, no numerical values. Section 6 (Discussion) repeatedly references "Table 1" and makes quantitative claims about relative performance (e.g., "non-autoregressive models outperform autoregressive models," performance degradation rates, SL vs. RL trade-offs), but the actual data supporting these claims is not present. While some of this may be a parser artifact (tables and figures are commonly lost in PDF-to-text extraction), the lack of any textual summary of the numerical results means the paper's central empirical findings cannot be verified from the available content.

### Minor

- **Only one method per quadrant limits the interpretability of the comparison.** The paper implements exactly one method per quadrant (PtrNet for AR-SL, Cherrypick/AM for AR-RL, DIFUSCO for NA-SL, DIMES for NA-RL). The paper acknowledges this limitation (Section 1: "we aimed to evaluate broad methodological categories rather than specific SOTA solvers"), but it means the observed differences could be driven by implementation idiosyncrasies rather than paradigm-level properties. A benchmark is most informative when it includes multiple methods per category to distinguish trends from implementation artifacts.

- **Baseline adaptations are described but not empirically validated.** The modifications to PtrNet (level-order tree traversal, node prioritization by distance to terminals, GNN feature embeddings) and DIFUSCO (custom edge feature initialization) are non-trivial design choices that could significantly affect performance. The paper does not ablate these choices (e.g., comparing alternative sequential representations for PtrNet, or using the original DIFUSCO edge features vs. the modified ones). For a benchmark paper, better empirical justification of these adaptations would strengthen confidence in the fairness of the comparison.

- **Grid graph instances have random edge costs despite 2D node coordinates.** The paper states that grid nodes have 2D location features "making them analogous to Euclidean-space combinatorial optimization problems like TSP and VRPs" (line 110), but edge costs are assigned as random integers from a truncated Gaussian (line 111), unrelated to the node coordinates. This weakens the Euclidean analogy — the grid provides structural topology, but edge weights are not distance-derived. This limits the practical relevance of the grid benchmark for Euclidean STP variants.

### Trivial

None.

## Nice-to-Haves

- Documenting the RL environment details (state space, action space, reward function, episode termination) for Cherrypick and AM would improve reproducibility.
- Reporting the computational cost of generating the optimal solutions (solver runtime, hardware) and wall-clock training times for each baseline would help researchers assess the practical feasibility of using SteBen.

## Removed Points

The following points from the reviewer inputs were assessed and removed or downgraded for the reasons noted:

1. *"Section 5.2 is empty — the paper is fundamentally incomplete."* — Moved from Fatal to Major and reframed. The parser is known to strip tables/figures; the qualitative results discussion in Section 6 provides some information even if the numerical table is missing. However, the absence of verifiable numerical results is still a Major concern.

2. *"Adaptation of baselines is superficial/lacks justification."* — Downgraded from its original framing. The adaptations are described textually; the concern is lack of empirical validation (ablation), which is a Minor issue, not a structural flaw.

3. *"Grid graph random edge costs make the benchmark less relevant."* — Kept as Minor but noted that this is a limitation of one of four graph models, not a systemic problem.

4. *Strength Finder's claimed strength about "demonstrated practical utility via zero-shot real-world generalization."* — Removed because it directly conflicts with the verified weakness that this claim has no evidence in the paper.

5. *"The paper should include multiple methods per quadrant."* — Kept as Minor rather than Major because the paper acknowledges this limitation, and one method per quadrant is acceptable for an initial benchmark.

## Novel Insights

The most interesting observation emerging from this review is a tension in the paper's structure: the dataset contribution (the paper's strongest asset) and the real-world generalization claim (the paper's weakest-supported assertion) appear to be in conflict. The paper would be **stronger** if it dropped the unsubstantiated real-world claim and instead devoted space to documenting the optimal solution provenance and presenting the ablation studies that would validate the baseline adaptations. This would transform the paper from one that overclaims into one whose primary contribution — a large-scale, well-documented benchmark — is fully credible.

## Suggestions

1. **Document the optimal solution computation in full.** Specify the exact solver used, runtime limits per instance size, optimality verification procedure, and any optimality gaps (especially for 200–1000 node instances). This is the single most important addition, as it directly affects the dataset's credibility.

2. **Either provide the real-world generalization experiment or remove the claim.** If the experiment exists, describe the real-world instances used, present quantitative results, and compare to baselines. If it does not, remove the claim from the abstract and contributions — the dataset is a valuable contribution on its own merits.

3. **Include the full results (Table 1, Figure 2) with statistical significance.** Ensure the Gap metric is clearly defined (gap to what reference solution?), report standard deviations or confidence intervals, and include both in-distribution and out-of-distribution results across all graph types and sizes.

4. **Add ablation studies for the key adaptation decisions.** At minimum: (a) compare PtrNet with and without GNN embeddings and with alternative sequential tree representations; (b) compare DIFUSCO with original vs. modified edge feature initialization; (c) show whether the Cherrypick decoding method is sensitive to the choice of baseline.

## Score and Decision

The paper addresses a clear gap — STP has been underserved by the NCO community, and a large-scale benchmark is genuinely needed. The dataset generation methodology is sound, the graph models and sizes are well-chosen, and the quadrant-based organization of baselines is sensible. However, the paper has two serious deficiencies that reduce confidence in its contributions: (1) the real-world generalization claim, presented as a key contribution, is entirely unsubstantiated; (2) the optimal solution provenance is undocumented, which undermines trust in the dataset's "exact solution" labels. Additionally, the main quantitative results table is not present in the provided text. These issues are resolvable with revisions, but in their current state they prevent full acceptance.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>