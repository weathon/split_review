Now I have read the full paper. Let me write my review.

---

## Summary

This paper establishes the first distributional equivalence characterization for linear non-Gaussian (LiNG) causal models with *arbitrary* latent structure and cycles, filling a long-standing open problem in the causal discovery literature. The central contribution is a graphical criterion (Theorem 2) expressed in terms of "children bases" via edge matchings, analogous to how Markov equivalence is characterized by shared adjacencies and v-structures. The paper also introduces *edge rank constraints* — a local, edge-level tool dual to path rank constraints — and provides a transformational characterization of equivalence classes (Theorem 3, analogous to Meek's conjecture). Built on these results, the authors develop the glvLiNG algorithm, claimed as the first structural-assumption-free method for latent-variable causal discovery.

---

## Strengths

- **Foundational theoretical contribution with clean results.** The paper solves a well-recognized open problem: distributional equivalence for latent-variable models is notoriously complex (Verma & Pearl, 1991; Richardson et al., 2023 noted for cycles; Adams et al., 2021 for acyclic latent models without full characterization), and the prior landscape has only handled special cases (cycles alone or restricted latent structure). The final criterion (Theorem 2) is surprisingly clean given this complexity: it decomposes into per-vertex checks over "children bases," directly mirroring the classical result for causally sufficient models (Lacerda et al., 2008).

- **Edge rank duality is an independently valuable insight.** Theorem 1 establishes an elegant duality between path ranks (global, mixing-matrix-based, well-known in causal discovery) and edge ranks (local, adjacency-based, known in matroid theory but missing from the causal toolbox). The equation min(|Z|,|Y|) − ρ_G(Z,Y) = |V| − max(|Z|,|Y|) − r_G(V\Y, V\Z) is non-trivial. The observation that every d-separation and t-separation statement can be rephrased in edge-rank terms is a useful theoretical connection, and the claim that this piece was missing from the causal-discovery toolkit is well-justified.

- **Comprehensive analogy with classical equivalence theory.** The paper systematically provides counterparts of: (i) a graphical equivalence criterion (Theorem 2, analogous to "same adjacencies and v-structures"), (ii) a transformational characterization (Theorem 3, analogous to Meek's conjecture), (iii) a maximal representative of each equivalence class (Theorem 4, analogous to CPDAG). This is not just aesthetic — it shows the theory is complete and internally consistent, and the side-by-side comparison table (Table 2, Appendix C.5) is a valuable contribution.

- **Irreducibility analysis is thorough and principled.** The paper carefully rules out trivially unidentifiable cases (latent variables with fewer than 2 children outside the set) via an explicit reduction procedure (Proposition 2), with a clear graphical condition and worked examples. This level of care is necessary and well-executed.

- **Experimental evaluation covers multiple relevant dimensions.** The empirical section evaluates equivalence class sizes (Table 3), runtime comparisons vs. LP baseline (Table 4 showing dramatic speedups), behavior of existing methods under structural misspecification (Table 5), finite-sample performance under varying density and latent count, and a real-world stock return dataset. The diversity of evaluation angles is appropriate for a paper making both theoretical and algorithmic contributions.

---

## Weaknesses

### Fatal
None.

### Major

- **OICA dependence is a practical bottleneck that limits the algorithm's reach.** The glvLiNG pipeline's first step is over-complete ICA (OICA), which is notoriously hard in practice: it requires the number of sources to exceed the number of observations, and its sample complexity is unfavorable. The authors acknowledge this ("OICA's known inefficiency"), framing glvLiNG as a "proof of concept." However, the finite-sample experiments (Appendix D.4) must therefore be interpreted with care: glvLiNG's advantage over baselines in denser graphs may partly reflect that both methods are struggling, but baselines struggle in a different way. A quantitative assessment of OICA estimation error's propagation through the algorithm would have strengthened the empirical claims.

- **Faithfulness assumption in cyclic models is non-trivial.** The glvLiNG recovery guarantee relies on Assumption 1 (no coincidental low ranks in the mixing matrix). In acyclic models, faithfulness violations are known to be measure-zero generically; in cyclic models, rational functions in the adjacency weights can create structured cancellations that are harder to rule out generically. The paper does note (in §3.1) that the pathological locus where denominators vanish does not affect main results, but this is a different concern from coincidental rank deficiencies in non-degenerate parameter regimes. More discussion on the genericity of faithfulness in cyclic models would be appropriate.

### Minor

- **The reduction procedure (Proposition 2) is stated for arbitrary graphs, but its complexity is not analyzed.** For large graphs with many latent variables, the identification of "maximal redundant latents" (mrl in Eq. 7) could be expensive. A brief note on computational cost would be helpful.

- **The comparison to baselines in finite samples (Appendix D.4)** could more clearly separate the effect of OICA estimation error from the effect of structural misspecification. Currently, it is unclear whether glvLiNG's relative performance advantage comes from correct model class or simply from OICA using more data.

### Trivial
None worth mentioning.

---

## Nice-to-Haves

- An extension or discussion of how the edge rank duality might apply to linear Gaussian models (where the analogous result via characteristic functions would differ) would help readers understand the scope of this new tool.
- A worked example explicitly tracing glvLiNG step-by-step on a small graph, from OICA output through rank realization to equivalence class traversal, would significantly aid reproducibility without increasing paper length.
- The real-world application (stock returns, Appendix D.5) is interesting but brief. Even a partial ground-truth or domain-expert validation of the recovered latent structure would strengthen this section.

---

## Novel Insights

The introduction of edge ranks as a dual to path ranks is the most surprising insight in the paper. These two notions capture the same underlying graphical bottleneck from complementary angles: path ranks summarize bottleneck sizes along directed paths in the mixing matrix, while edge ranks count maximum matchings via the local adjacency. The duality theorem (Theorem 1) makes this precise and yields a powerful consequence: the globally intractable condition of "matching all path ranks under a permutation" (Lemma 3) becomes the locally decomposable condition "matching children bases per vertex" (Theorem 2), precisely because edge ranks — unlike path ranks — respect the local structure of individual edges. This local decomposition is the technical core that makes the criterion practical. Additionally, the realization that only a single cycle reversal is ever needed in the transformational characterization (Theorem 3) is a structural insight suggesting that cycles do not proliferate the complexity of the equivalence class in the way one might expect.

---

## Suggestions

- Provide a careful complexity analysis of the glvLiNG algorithm, including the traversal in Theorem 3 (e.g., worst-case number of admissible operations needed to reach from one graph in the class to another).
- Consider adding a discussion of *partial* identifiability results: when structural assumptions are partially available (e.g., some variables known to be pure measurements), how does the equivalence class shrink? This would help bridge the gap between the fully general setting and existing specialized methods.
- In the finite-sample experiments, include an ablation that measures sensitivity to OICA estimation quality, e.g., by varying sample size and reporting both OICA reconstruction error and final graph recovery accuracy separately.

---

## Score and Decision

The paper solves a fundamental open problem in causal discovery — distributional equivalence for the most general class of linear non-Gaussian models (arbitrary latent variables + cycles) — with theoretically clean results and a practically oriented algorithm. The edge rank duality theorem is a genuine intellectual contribution independent of the main result. The experimental section is broad and honest about limitations. The primary weakness (OICA dependence) is acknowledged and does not undermine the theoretical core. This is a strong contribution that advances foundational understanding of what is and is not identifiable in one of the most studied parametric settings.

MY FINAL SCORE: <score>8.0</score>
MY FINAL DECISION: <decision>Accept</decision>