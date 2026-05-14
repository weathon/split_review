## Summary

This paper provides the first graphical characterization of distributional equivalence for linear non-Gaussian latent-variable models with arbitrary latent structure and cycles — crucially, without any structural assumptions on how latents are indicated or how they interact with observed variables. The authors introduce *edge ranks* as a new theoretical tool, prove their duality with the classical path ranks (Theorem 1), and use them to derive both a local graphical criterion (Theorem 2) and a transformational characterization (Theorem 3) for equivalence. A proof-of-concept algorithm, glvLiNG, recovers models from data up to this equivalence class. This is the first structural-assumption-free method for latent-variable causal discovery in any parametric setting.

## Strengths

- **First general distributional equivalence characterization for LiNG models without structural assumptions.** Theorem 2 reduces an exponential number of subset checks to a local, efficiently checkable condition involving "children bases." Theorem 3 shows equivalence classes are connected via admissible cycle reversals (Lemma 6) and edge additions/deletions (Lemma 7), with at most one cycle reversal. These are genuinely novel and foundational results.

- **Edge ranks and their duality with path ranks (Theorem 1).** The introduction of edge ranks — a local, edge-level constraint defined via maximum bipartite matching — fills a missing piece in the rank-based causal discovery toolbox. The duality theorem reveals that path ranks and edge ranks offer complementary perspectives on bottlenecks in digraphs. This tool is likely to find uses beyond the paper's specific setting (as the authors sketch for Gaussian and discrete settings in Appendix C.5).

- **Transformational characterization enabling class traversal.** Theorem 3 provides an analogue of Meek's conjecture for this setting, yielding a natural BFS/DFS procedure for enumerating all equivalent digraphs. The interactive demo at https://equiv.cc makes this tangible and is a valuable contribution in itself.

- **Reasonable multi-angle evaluation for a theory paper.** The paper quantifies equivalence class sizes exhaustively for small digraphs (Table 3), benchmarks structurally misspecified baselines under oracle conditions (Table 5), runs finite-sample simulations (Figure 7), and applies glvLiNG to real stock-market data recovering interpretable patterns (Appendix D.5). The authors are transparent that glvLiNG is a proof-of-concept and that OICA is a practical bottleneck.

## Weaknesses

### Fatal

None.

### Major

None. The theoretical contributions are rigorous and well-supported. The algorithmic limitations are explicitly scoped as proof-of-concept.

### Minor

- **No sensitivity analysis for the rank-thresholding parameters (α=25, ε=0.02) used in glvLiNG.** In Appendix D.4 (lines 3767-3773), the paper mentions a sigmoid-based confidence score with fixed α and ε, and briefly states robustness was verified under synthetic noisy ranks (N(0.75, 0.2) vs N(0.25, 0.2)). However, no systematic sweep over α/ε values is presented, nor is there analysis of how misclassification of ranks propagates to graph errors. Given glvLiNG is presented as a proof-of-concept, this is minor, but it would strengthen the empirical case for the algorithm's practical viability.

- **No evaluation of equivalence-class coverage.** The simulation experiments only report SHD to the closest equivalent graph (Appendix D.4, line 3781). Since Theorem 3 enables traversal of the entire estimated equivalence class, one could measure recall of true equivalent graphs on small instances where exhaustive enumeration is feasible. The absence of this experiment leaves open whether the algorithm systematically over- or under-estimates the class. The authors acknowledge the algorithm is proof-of-concept, so this is a missed opportunity rather than a fatal gap.

### Trivial

- **The 19,008-graph equivalence class in the stock-market analysis is presented without critical discussion of its practical informativeness.** Reporting that the class contains 20 solid and 14 dashed edges (Figure 8) is useful, but could be enriched by discussing what fraction of edges are invariant and what structural questions remain unresolved.

## Nice-to-Haves

- A comparison with Salehkaleybar et al. (2020), which also uses OICA but assumes acyclicity, would help contextualize the practical benefit of being assumption-free versus trading some structural flexibility for potentially more robust estimation.
- A discussion of how OICA estimation errors (mis-estimation of latent count, inaccurate column scaling) affect the recovered equivalence class would ground practical expectations.

## Removed Points

These points are flagged to be removed — treat them with caution.

- **"Reduction requires knowledge of the true graph; the paper does not discuss whether the same reduction can be soundly applied to an estimated graph."** Removed because the reduction (Proposition 2) is a theoretical canonicalization to rule out trivial equivalence cases, not an algorithmic step applied to data. The paper is explicit that this lets us "restrict attention to irreducible models for the remainder" (line 268).

- **"Runtime comparison against MILP is of limited value — MILP is an obviously inefficient baseline."** Removed. The paper uses MILP as a brute-force satisfiability baseline precisely to demonstrate the speedup from its constraint-based approach. This is standard practice, and the paper does not oversell the comparison. The real story is in the absolute runtime: glvLiNG solves n=10 in under 5 seconds.

- **"Missing baseline: Salehkaleybar et al. 2020."** Moved to Nice-to-Haves. The chosen baselines (LaHiCaSl, PO-LiNGAM) are structurally misspecified by design — they serve the paper's purpose of showing what goes wrong when structural assumptions are violated. Adding an OICA-based acyclic method would be informative but is not essential to the paper's core claim.

- **Formatting/typo/style criticisms from the harsh critic.** Removed — these are parser artifacts, not author errors.

## Novel Insights

None beyond the paper's own contributions. The paper's introduction of edge ranks as a dual perspective to path ranks, and the demonstration that this duality enables a clean decomposition from global rank constraints to local singleton checks, is genuinely novel and may influence how the broader community approaches rank-based causal discovery.

## Suggestions

- Add a sensitivity analysis varying α and ε by at least an order of magnitude, showing SHD as a function of threshold choice, to support the claim of robustness.
- On small graphs (n ≤ 6) where exhaustive enumeration of true equivalence classes is feasible, report recall of true equivalent graphs within the estimated class to validate that Theorem 3 traversal operates correctly on estimated inputs.
- Discuss the stock-market results more critically — quantify what fraction of edges are invariant (solid) vs. uncertain (dashed), and what domain-level claims can or cannot be made given the ~19k ambiguity.

---

**Anchor comparison:**

| Anchor | Avg Score | Comparison |
|--------|-----------|------------|
| `/home/wg25r/review_agent/human_reviews_2026/BNHplerBYE.md` | 5.33 (Accept Poster) | Same domain (latent-variable causal discovery). That paper proposes a score-based greedy search algorithm; this paper is more theoretically original with a first-of-its-kind equivalence characterization. The theory here is stronger; experiments are comparable. |
| `/home/wg25r/review_agent/human_reviews_2026/ssYeoL4ksl.md` | 5.50 (Reject) | Also handles cycles + latent variables in linear non-Gaussian models, but limited to bivariate case. This paper is substantially more comprehensive (arbitrary latent structure, full graph characterization). |
| `/home/wg25r/review_agent/human_reviews_2026/Uc1EAICxTD.md` | 4.50 (Accept Poster) | Independence test for LiNG data. Narrower contribution with comparable experimental depth. This paper's theoretical contribution is broader and more foundational. |
| `/home/wg25r/review_agent/human_reviews_2026/V7pT2ZRoTB.md` | 4.50 (Accept Poster) | Pure theory paper for causal discovery on random graphs. Narrow scope, experimental evaluation limited to simulations on graph models. This paper has broader scope and includes real-data evaluation. |
| `/home/wg25r/review_agent/human_reviews_2026/qLbTww6vv2.md` | 4.00 (Reject) | Latent additive noise models. Less rigorous theory, weaker experiments. This paper is clearly stronger on both axes. |
| `/home/wg25r/review_agent/human_reviews_2026/mA78uXqcnl.md` | 7.00 (Accept Oral) | Hawkes processes with latent confounders. Strong theory + strong experiments. This paper has comparable theoretical depth but weaker experimental validation (explicitly proof-of-concept). |

**Calibration reasoning:** This paper's theoretical contribution is foundational — the first equivalence characterization in its setting — and is more original than the 4.50-5.50 anchors. It falls below the 7.00 oral anchor (mA78uXqcnl) primarily because the algorithm and experiments are explicitly proof-of-concept while that paper delivers a more complete practical package. The score lands at 6.5: strong theoretical paper with acknowledged experimental limitations, clearly above borderline-accept territory but not at the oral level.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>