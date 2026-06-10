Here is the final consolidated review.

---

## Summary

The paper proposes D-SPEC, a distribution-based spectral clustering algorithm that constructs an n×k bipartite graph between n data points and k learned cluster distributions, then applies a transfer cut to reduce the eigendecomposition to a k×k matrix — the theoretical minimum given k clusters. The method is evaluated on 15 benchmarks and 5 large-scale datasets (up to 20M points), showing competitive or superior performance against existing accelerated spectral clustering methods.

## Strengths

- **Achieves k×k eigendecomposition — a genuine advance.** Table 2 confirms O(k³) eigendecomposition time versus O(p³) for landmark methods where p >> k. This directly answers the paper's motivating question and is a qualitative improvement over prior work, not an incremental one.

- **Strong empirical performance across many datasets and scales.** D-SPEC achieves the best NMI on most of 15 benchmark datasets and on all 5 large-scale datasets (1M–20M points), while many competitors fail due to memory/time limits. The large-scale experiments (Figure 4) are the paper's strongest evidence, showing the method scales without sacrificing quality.

- **Demonstrates a qualitative capability on fundamental spectral clustering limitations.** On the Nadler & Galun (2006) challenging cases (8:1:1 imbalanced clusters, Gaussian vs. uniform distribution), D-SPEC maintains NMI > 0.8 while most comparison methods drop below 0.6–0.8. This suggests the distributional representation captures structural information that point-based methods miss.

- **Ensemble analysis indirectly validates base quality.** D-SPEC's ensemble version (D-SENC) shows negligible improvement over the base method, while U-SPEC's ensemble version substantially boosts U-SPEC. This honestly reported finding supports the claim that D-SPEC's base clustering is already near ceiling.

## Weaknesses

### Major

- **The bounded graph construction is underspecified, yet it determines the method's success.** The entire D-SPEC pipeline depends on obtaining good initial cluster approximations from the bounded graph (Step 2, Algorithm 1). The paper provides no concrete algorithm: how is the RKHS mapping chosen (which kernel?), how is the threshold τ selected, how are the "largest k subgraphs" identified from the bounded graph, and critically, **why does sampling p points make Assumption 3.1 hold?** The paper acknowledges Assumption 3.1 "is difficult to satisfy" for real data, then asserts that sampling p points fixes it, but provides no reasoning or analysis. Without this specification, the method's core step is a black box.

- **No ablation isolating the spectral refinement from the initial clustering.** If the bounded graph already separates data into k near-perfect connected components, the subsequent spectral embedding and k-means may add nothing. Conversely, if the bounded graph is corrupted, the entire method fails. The paper provides no experiment comparing: (i) bounded-graph clustering alone (no spectral step), (ii) spectral clustering on the bipartite graph without bounded-graph denoising, and (iii) full D-SPEC. This makes it impossible to attribute the results to the distribution-based spectral contribution versus the preprocessing.

- **Theoretical results are weak relative to the claims they are asked to support.** Theorem 3.2 assumes k completely disconnected subgraphs — the limiting case where clustering is already solved and any reasonable spectral method would produce perfect results. Theorems 3.3 and 3.4 state noise-robustness bounds (e.g., sup_i|λ_{di}¹ − λ_{di}⁰| ≤ sup_i|λ_i¹ − λ_i⁰|) but compare eigenvalues across different operators with no proof in the main text and no connection to clustering quality (NMI, ARI). A more meaningful theoretical statement would analyze a realistic setting (e.g., stochastic block model) rather than the idealized disconnected-subgraph case.

- **Critical hyperparameters τ and p lack principled selection or sensitivity analysis.** The method uses a threshold τ to construct the bounded graph and a sample size p for the initial subgraph. Neither has a documented selection method. The paper reports results on 15 datasets without specifying how τ and p were chosen, whether they were tuned per dataset, or how sensitive the results are to their values. If tuned per dataset, the comparison against baselines may be unfair. The absence of any sensitivity analysis is a major methodological gap.

### Minor

- **IDK kernel parameters not reported.** The paper relies on Isolation Distribution Kernel (IDK) for computing kernel mean embeddings (Equation 1) but does not specify the number of isolation trees, subsampling size, or any IDK parameters. These choices could affect results.

- **No standard deviations for individual benchmark results.** Table 1 reports average NMI over 10 runs but no standard deviations, making it impossible to assess result stability.

- **Nemenyi significance test at 0.1 level is lenient.** A 0.05 significance level is standard; the weaker threshold weakens the claim that "only D-SPEC is significantly better than SC."

- **Running times reported only as ratios, not absolute seconds.** The scale-up test (Figure 4, right) reports time ratios relative to a 1K-point run. Absolute wall-clock times would let readers assess practical efficiency.

### Trivial

None.

## Nice-to-Haves

- Adding standard deviations to Table 1.
- Reporting absolute running times in addition to ratios.
- A controlled experiment under a stochastic block model to support the theoretical claims.

## Removed Points

The following points from the inputs were removed with justification:

- **"Circular dependency" claim (Harsh Critic item 1, framed as "fatal"):** The reviewer asserts the method must know final clusters to compute distributions. The paper clearly describes a two-stage process: (1) obtain *approximate* clusters via thresholding on a *sampled subgraph*, (2) compute distributions from those approximations, then (3) refine via spectral embedding on the full data. This is a standard initialization-then-refinement pattern, not circular. The underlying concern about the bounded graph being underspecified is valid and preserved as a major weakness, but the "circular dependency" framing is a misreading of the paper and removed.

- **"Bounded graph does the real clustering work" (Harsh Critic item 2):** This concern is preserved and strengthened above as an ablation gap. The critic's framing that the spectral step "would then be redundant or marginal" is plausible but unsubstantiated — and that is exactly why an ablation is needed. Kept as a major weakness but reframed as a call for evidence.

- **"Missing related works" suggestions:** Removed per hard rule; I cannot verify the existence of missing citations.

- **"Transfer cut correctness not verified" criticism:** The transfer cut is cited to prior published work (Li et al., 2012; Huang et al., 2019; Li et al., 2022). The paper is not required to re-derive existing methods. Removed.

- **"No discussion of failure cases":** Generic criticism that does not identify a specific problem in the paper as written. Removed.

- **Formatting/style nitpicks** about undefined notation: Removed per hard rules on parser artifacts.

- **Strength Finder's "provably tighter noise-robustness bounds":** Downgraded — the bounds are stated without proof in the main text and the connection to clustering quality is not established. The theoretical contribution is better described as "stated bounds" than "proven robustness."

- **Strength Finder's claim that the central claim is "concretely demonstrated":** While the k×k eigendecomposition is indeed demonstrated (Table 2), the method's overall contribution depends on the bounded graph step which is underspecified. The strength finder overstates the completeness of the demonstration.

## Novel Insights

The key novelty — representing clusters as distributions rather than landmark points to enable k×k eigendecomposition — is an interesting conceptual shift. The empirical finding that this approach handles Nadler & Galun's fundamental spectral clustering limitations better than existing methods is noteworthy and suggests the distributional representation captures structural information that point-based methods miss. However, the extent to which this stems from the spectral refinement versus the initial bounded-graph denoising cannot be determined from the presented experiments.

## Suggestions

1. **Specify the bounded graph construction precisely.** Provide the exact algorithm: which kernel is used for the RKHS mapping, how τ is selected (cross-validation? quantile-based heuristic?), how connected components are identified, and why/how sampling p points mitigates violations of Assumption 3.1.
2. **Add a three-way ablation** comparing (a) bounded-graph clustering only → k-means, (b) spectral clustering on the bipartite graph without bounded-graph denoising, and (c) full D-SPEC.
3. **Report parameter sensitivity** for τ and p on at least 2–3 datasets, showing NMI across a range of values.
4. **Strengthen the theoretical analysis** by analyzing a realistic model (e.g., stochastic block model) where eigenvalue bounds can be linked to clustering recovery guarantees.
5. **Report IDK parameters** and test sensitivity to them.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>