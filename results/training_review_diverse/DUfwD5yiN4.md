Now I have a thorough understanding of the paper and all the review inputs. Let me produce the consolidated review.

---

## Summary

This paper proposes an exact distributed structure-learning algorithm for Bayesian networks. The key idea is to partition variables into overlapping subsets (a "conditional P-map reduction") such that each subset can be learned independently using a standard P-map learner, then concatenated and refined via boundary-node processing. The paper defines conditional P-map and conditional P-map reduction, outlines a three-step algorithm (cover-finding, local learning, boundary correction), and reports experiments on seven benchmark networks comparing against the centralized PC algorithm.

## Strengths

- **Low-order conditioning bound.** The algorithm bounds the separator size by a user-specified parameter \(W\) (e.g., \(W=1\) in experiments), avoiding the high-order conditional independence tests required by prior exact distributed methods (Xie et al., 2006; Liu et al., 2017). This is a genuine architectural design choice that could make distributed structure learning more practical in settings where high-order CI tests are infeasible.
- **Conceptually clean formulation.** The formalization of conditional P-map (Definition 3.2) and conditional P-map reduction (Definition 3.3) provides a principled vocabulary for thinking about distributed structure learning, and the paper correctly identifies the key issue (finding a cover that decomposes the learning problem while preserving exactness).

## Weaknesses

### Major

- **Theoretical gap in the local learning step (undermines the central exactness claim).**  
  Definition 3.3 requires that \(\mathcal{G}[\mathcal{X}_i]\) be a *conditional* P-map for \(P[\mathcal{X}_i]\) given \(\mathrm{bd}(\mathcal{X}_i)\). Under this definition, a d-separation in \(\mathcal{G}[\mathcal{X}_i]\) may only appear as a conditional independence in \(P[\mathcal{X}_i]\) when *additional* boundary variables are conditioned on (Condition (ii) of Definition 3.2). However, Algorithm 1 (line 3) calls a standard P-map learner (e.g., PC) on the marginal \(P[\mathcal{X}_i]\) alone, without conditioning on boundary nodes. When a d-separation requires boundary conditioning to be detectable, PC will fail to detect the corresponding conditional independence and will incorrectly retain an edge. The paper asserts that "PC can correctly identify the edges that do not exist between two interior nodes or an interior node and a boundary node" (Section 3.1), but provides no argument for why such "hard-to-detect" d-separations do not affect interior-relevant edges. The reference to Remark A (in the appendix, stripped by the parser) does not fill this gap in the main text. **This is a structural problem: if the reasoning cannot be repaired, the central claim of exactness is unsupported.**

- **Cover-finding algorithms are underspecified.**  
  Algorithms 2 and 3 — which solve the critical problem of partitioning variables — are described only in prose. Algorithm 2 mentions checking subsets from the power set of a component, which in the worst case is exponential, but no analysis of tractability, termination criteria, or computational complexity is provided. Algorithm 3 is name-dropped in the experiments but never described. The dependency matrix approach is mentioned but not connected to the algorithmic search. Without a concrete specification (pseudo-code), neither correctness nor runtime guarantees can be evaluated. This undermines reproducibility.

- **Weak experimental evaluation relative to the claims.**  
  The experiments suffer from three interrelated problems:  
  (1) **No ground-truth comparison.** Structural Hamming distance is reported only between Algorithm 1 and PC, not against the true DAG. Low SHD to PC could mean both make the same errors, which does not demonstrate exactness.  
  (2) **Marginal speedup.** The reported speedup is up to 2× using 30 CPUs on networks with at most 70 variables. The paper claims applicability to a "giant" number of variables but provides no evidence of scaling beyond tiny benchmarks.  
  (3) **Unjustified parameters.** The choices \(d = 0.75n\) (so subsets are still 75% of total variables) and \(W = 1\) are fixed without sensitivity analysis. With \(d\) set so high, the distributed advantage is severely limited. No ablation isolates the contribution of cover-finding vs. local learning vs. boundary correction.

### Minor

- **Ambiguous experimental setup for the PC baseline.** The paper states "the number of CPUs was set to 30 for all datasets" in the context of reporting runtime for both Algorithm 1 and PC, but PC is not a parallel algorithm. It is unclear whether PC was given the same 30-CPU resource pool or used a single CPU, making the runtime comparison potentially misleading. The paper also does not compare against a parallelized version of PC or against any prior distributed method (e.g., Gu & Zhou 2020) — even as an approximate baseline.

- **No complexity analysis.** The paper provides no worst-case bounds for Algorithms 2 and 3 in terms of \(n\), \(d\), and \(W\). Even the claim that "connected-components decomposition takes \(O(n^2)\)" assumes the dependency matrix is already built, which requires \(O(n^2)\) CI tests — a significant cost unaccounted for in scalability claims.

- **No limitations or failure-case discussion.** The paper acknowledges (via Figure 2) that not all DAGs admit a P-map reduction, but does not formally characterize when a conditional P-map reduction exists, when the method fails, or what the separator size \(W\) implies about graph topology. Densely connected graphs that require large \(W\) are likely to negate the advantage of the approach, but this is not discussed.

### Trivial

- None.

## Nice-to-Haves

- A sensitivity analysis varying \(d\) and \(W\) to show how these parameters affect cover size, number of components, and overall runtime.
- A comparison against ground-truth structures on benchmark networks (where the true DAG is known) to directly test the exactness claim.
- A comparison against a parallelized CI-test baseline (e.g., running PC with parallel CI tests) to distinguish gains from problem decomposition from gains due to parallelism.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Strength Finder's "Exact output guarantee" strength.** Removed because it conflicts with the verified weakness that the theoretical justification for exactness is incomplete (the local learning step has a logical gap). A claimed contribution is not a verified strength when its support is questionable.
- **Strength Finder's "Empirical validation on standard benchmarks" strength.** Removed because it conflicts with the verified weaknesses about experimental design (no ground-truth comparison, marginal speedup, lack of parameter sensitivity). The evidence is too thin to qualify as a strength supporting the paper's core claims.
- **"The introduction twice calls the approach 'exact' without qualifying that exactness depends on perfect CI tests."** This is a presentation nitpick. All constraint-based methods assume perfect CI tests; the community standard does not require restating this caveat on every occurrence.
- **"Definition 3.2/3.3 ambiguity about marginal vs. full distribution."** The text is actually explicit: Definition 3.3 states "conditional P-map for \(P[\mathcal{X}_i]\) given \(\mathrm{bd}(\mathcal{X}_i)\)", which correctly applies the definition to the marginal distribution.
- **Criticisms about missing appendix content or proofs deferred to the appendix.** The parser strips appendix content from all papers.

## Novel Insights

None beyond the paper's own contributions. The core insight — that one can partition variables using conditional independence such that local learning is exact — is the paper's own. The reviews do not surface additional novel observations.

## Suggestions

1. **Fix the theoretical gap.** Either prove that for conditional P-map reductions, all d-separations involving interior nodes (or interior-boundary pairs) are detectable without conditioning on boundary variables, or modify the local learning step to explicitly condition on boundary nodes during CI testing.
2. **Provide pseudo-code for Algorithms 2 and 3**, including termination criteria, the role of the dependency matrix, complexity analysis, and how the search over separators is bounded (e.g., by \(W\)).
3. **Re-run experiments against ground-truth DAGs** on benchmark networks where the true structure is known. Report SHD to the ground truth for both Algorithm 1 and PC. Show error bars (or multiple random seeds).
4. **Demonstrate scalability** on larger networks (hundreds or thousands of variables), or at least provide complexity analysis that would support the scalability claims.
5. **Include a sensitivity study** varying \(d\) and \(W\) to show how these parameters affect cover decomposition and runtime.
6. **Add a limitation section** discussing when the method may fail (graphs with no conditional P-map reduction, dense graphs requiring large \(W\), etc.).

## Score and Decision

The paper proposes a conceptually appealing idea — exact distributed structure learning via conditional P-map reductions — which is a relevant and timely problem. However, the current manuscript has three serious issues that collectively undermine the central contribution: (1) a logical gap in the theoretical justification for why local learning is exact, (2) cover-finding algorithms specified too vaguely to evaluate or reproduce, and (3) experiments that do not demonstrate exactness and show only marginal scalability on small benchmarks. These are not minor presentation issues they are structural flaws that prevent the paper from being accepted in its present form. The core idea may be salvageable with substantial revision, but the submission as-is does not meet the bar for publication.

**Score:** 4.0 (weak reject — interesting idea but major theoretical and evidential gaps)

MY FINAL SCORE: <pineapple>4.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>