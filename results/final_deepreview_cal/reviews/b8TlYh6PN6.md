Now let me write the final consolidated review.

## Summary

This paper establishes the first graphical characterization of distributional equivalence for linear non-Gaussian causal models that simultaneously include both latent variables and cycles. The central theoretical contribution is a criterion (Theorem 2) reducing the global equivalence check to local checks on each singleton observed variable, plus a transformational characterization (Theorem 3) analogous to the Meek conjecture that enables traversal of the entire equivalence class. A new tool—edge rank constraints—is introduced as a local, graph-manipulable alternative to path ranks, with a duality theorem linking the two. The paper also presents glvLiNG, an algorithm that recovers models up to equivalence, though it is positioned primarily as a proof-of-concept given its reliance on over-complete ICA (OICA). The theoretical results are clean, novel, and well-motivated; the empirical evaluation, while limited in the main text, is supplemented in the appendix.

## Strengths

- **First distributional equivalence characterization with latent variables in linear non-Gaussian models without structural assumptions.** This is the paper's headline contribution and is genuinely novel. Previous work either assumes acyclicity (Lacerda et al., 2008), assumes specific graphical patterns (pure children, triangle-free, etc.), or handles only the latents or only the cycles separately. Unifying both under a single framework and proving an equivalence criterion is a significant theoretical step forward.

- **Introduction of edge rank constraints and the duality with path ranks (Theorem 1).** Edge ranks provide a local, edge-level perspective that complements the global path-rank perspective familiar from prior work. The duality theorem is elegantly stated and opens a new angle for analyzing rank constraints in causal discovery beyond this paper.

- **Theorem 2 provides a practical graphical criterion that reduces exponentially many subset checks to a per-singleton check.** The result that equivalence can be verified by checking children bases of L and each L ∪ {X_i} independently is a genuine simplification, analogous to how "same adjacencies and v-structures" simplifies "same d-separations" in the Markov equivalence setting. This is what makes the characterization operational.

- **Transformational characterization (Theorem 3) enabling equivalence class traversal.** The analogue of the Meek conjecture for this setting is a nice result. Together with Lemma 6 (admissible cycle reversals) and Lemma 7 (admissible edge additions/deletions), it provides a concrete mechanism to enumerate the equivalence class (e.g., via BFS/DFS). The online demo (equiv.cc) is a helpful complement.

- **Clear writing and careful positioning.** The paper is well-structured, definitions are precise, and the limitations (OICA reliance, glvLiNG as proof-of-concept) are acknowledged. The comparison to the CPDAG framework throughout helps readers from the causal discovery community grasp the results by analogy.

## Weaknesses

### Major

- **The practical evaluation in the main text is too thin to support the practical discovery claim headlined in the abstract.** The evaluation section (§5) describes five evaluation aspects but provides almost no numerical results in the main body. For the finite-sample experiments (aspect 4), the text says only that glvLiNG "performs particularly better than baselines on denser graphs" — no precision/recall, SHD, F1, confidence intervals, or statistical tests appear. For the oracle comparison (aspect 3), the claim that baselines "misidentify over half of the edges" is stated without tabular support. The paper references Tables 3–5 and Appendix D, which contain the actual numbers, but the main text alone does not enable a reader to assess the method's reliability, failure modes, or the fairness of comparisons. Given that the abstract and introduction prominently claim "the first structural-assumption-free discovery method," this gap between claim and presented evidence is significant. The paper's own final remarks acknowledge that glvLiNG "serves more as a proof of concept," which is honest but creates a mismatch with the stronger claims in the abstract.

- **The algorithmic claim is weakened by dependence on oracle OICA, and the practical implications are not discussed.** The glvLiNG pipeline assumes an oracle OICA that recovers the mixing matrix up to scaling and permutation (Assumption 1, deferred to Appendix A). Over-complete ICA (more sources than observations) is notoriously difficult — consistency results are delicate, sample-size requirements are high in practice, and the number of components may be estimated incorrectly. The paper does not analyze how glvLiNG would behave when OICA estimates are noisy, components are mis-specified, or the sources are not exactly independent/non-Gaussian. While the paper acknowledges this limitation in the conclusion, the practical feasibility of the algorithm as a "discovery method" remains unclear without a discussion of when OICA can be replaced by more robust rank estimation techniques or how estimation errors propagate.

### Minor

- **Computational complexity of the irreducibility check (Proposition 1) is not discussed.** The condition requires checking every non-empty subset l ⊆ L, which is exponential in |L|. The paper notes that for acyclic graphs it suffices to check each single L_i, but the general cyclic case is left unaddressed. Since irreducibility is a prerequisite for the equivalence characterization, this computational cost deserves at least a brief discussion.

- **Computational complexity of the edge-addition criterion (Lemma 7) is not characterized.** The criterion requires computing edge ranks for subsets whose size grows with |L|. The paper mentions acceleration via parallel traversal (Lemmas 9 and 12, in the appendix) but provides no algorithmic analysis or empirical evidence on tractability for moderate |L|.

- **Proof sketches for key theorems are absent from the main text.** Theorems 2 and 3 are stated without any proof intuition in the main body. A brief sketch (e.g., "Theorem 2 follows from Lemma 5 by a matroid intersection argument that reduces to checking singletons because the edge rank function is submodular") would increase reader trust and readability.

### Trivial

- The claim "first such result known to us in any parametric setting" (contributions) is broader than what the paper supports — the result is established for linear non-Gaussian models, which is one parametric setting. The phrase "in any parametric setting" should be scoped to "in the linear non-Gaussian setting."

## Nice-to-Haves

- An explicit verification that Theorem 2 reduces to known results when L = ∅ (the Lacerda et al., 2008 condition) or when cycles are absent would strengthen the paper's positioning relative to prior work. The paper hints at this connection (line 252: "Theorem 2 immediately reduces to the classical result") but could elaborate.
- The finite-sample experiments, while deferred to the appendix, would benefit from a summary table in the main text (e.g., mean SHD or precision/recall across settings) to give readers a concrete sense of performance without having to cross-reference the appendix.

## Removed Points

These points from the harsh critic or strength finder were evaluated and removed with justifications:

- **"Theorem 3 reliance on checking all subsets is exponential"** — The paper notes the procedure can be accelerated via parallel traversal across children (Lemmas 9, 12, deferred to appendix). Without the appendix content, this is unverifiable either way. Demoted from a structural concern to a minor note about missing complexity analysis.

- **"No hardware details, standard deviations, or baseline descriptions for runtime"** — The main text reports that glvLiNG solves n=10 vertices in under 5s vs. a linear programming baseline that takes hours beyond n=5. This is sufficient for an illustrative runtime comparison in a theory-focused paper; the full details are in the appendix.

- **"Missing related work"** — The paper does cite relevant prior work (Adams et al., Lacerda et al., Ghassami et al., Evans, etc.) and positions itself relative to them. The claim that it misses comparisons is not supported by the paper as read.

- **"The evaluation is not reproducible from the main text alone"** — Code is provided. The detailed results are in the appendix. Expecting full reproducibility from the main text alone is not a standard requirement for conference papers with page limits.

- **Strength Finder's "first structural-assumption-free method"** — This claim appears in the abstract but is tempered by the paper's own acknowledgment that glvLiNG is a proof-of-concept. The strength as stated is valid for the theoretical contribution but oversold for the algorithm; kept the strength in modified form as "first equivalence characterization."

- **Various generic strengths from the Strength Finder** — "Algorithm glvLiNG as the first structural-assumption-free method" is a duplicate of the core strength already listed. "Reduction to irreducible models" is a necessary step but not a standalone strength; merged into the summary.

## Novel Insights

The paper's most insightful contribution beyond its own results is drawing the explicit parallel between edge-rank-based equivalence and classical Markov equivalence — showing that distributional equivalence in the linear non-Gaussian latent-variable setting admits both a "same adjacencies and v-structures" analog (Theorem 2) and a "Meek conjecture" analog (Theorem 3). This framing bridges the gap between parametric latent-variable models and the well-understood nonparametric causal sufficiency setting, suggesting that the equivalence class structure in this harder setting is more tractable than previously believed.

## Suggestions

1. **Align the abstract and introduction claims with the actual contribution.** The phrase "first structural-assumption-free discovery method" should either be replaced with "first structural-assumption-free equivalence characterization" or be accompanied by a much stronger empirical evaluation. Currently, the abstract oversells the algorithmic contribution relative to what is demonstrated.

2. **Include at least one summary table of finite-sample results in the main text.** Even a small table showing SHD or F1 for a few representative settings (dense/sparse, small/large n) would transform the evaluation from "thin" to "informative enough to judge."

3. **Add proof sketches or intuition for Theorems 2 and 3 in the main body.** A paragraph of intuition would help readers gauge plausibility without diving into the appendix.

4. **Discuss the computational complexity of the irreducibility check and edge-addition criterion.** Even a brief note on whether these can be checked in polynomial time or whether |L| is typically small would address a clear reader concern.

5. **Clarify the scope of the "any parametric setting" claim.** This is established for linear non-Gaussian models; rephrase to avoid overclaiming.

## Score and Decision

### Calibration report

**Round 1 — Bracketing.** Three queries on topics similar to the paper (causal discovery with latent variables, linear non-Gaussian). Lower band (scores < 3.5): results showed papers at 3.00–3.25 with fundamental flaws. Middle band (3.5–7.5): anchors at 5.25, 6.00 (×2), 6.75. Upper band (> 7.5): anchors at 8.00 (×4) with very strong theory+experiments. **Initial bracket:** 5.5–7.5.

**Round 2 — Narrowing.** Queries targeting 4.5–7.0 and 5.5–7.5. Anchors read in full:
- "Recovery of Causal Graph Involving Latent Variables via Homologous Surrogates" (6.00, 4 reviews): Makes structural assumptions (homologous surrogates), strong presentation issues, narrower contribution. **This paper is stronger** — it solves a more general problem (no pure-child-type assumptions, allows cycles) with cleaner theory.
- "Efficient and Trustworthy Causal Discovery with Latent Variables" (6.00, 4 reviews): Makes pure-children-type assumptions, reviews note limited experiments and dense presentation. **This paper is stronger** — more general setting, more novel theory.
- "Differentiable Causal Discovery for Latent Hierarchical Causal Models" (6.75, 4 reviews): Strong theory with differentiable method, but limited experiments; one reviewer gave 5, another gave 8. **Comparable** — similar profile of strong theory + limited experiments, but this paper's theoretical contribution (first equivalence characterization) is more fundamental.
- "Structural Estimation of Partially Observed Linear Non-Gaussian Acyclic Model" (6.50, 4 reviews): Makes atomic-unit/pure-children assumptions, practical algorithm with good experiments. **This paper is slightly weaker on experiments but stronger on theoretical generality** — no acyclicity assumption, no pure-children assumption.

**Final score:** 6.5. The paper's theoretical contribution is genuinely novel and significant — it opens a new direction for latent-variable causal discovery. But the practical discovery claim is undersupported by the evaluation, and the gap between the abstract's "first structural-assumption-free discovery method" and the paper's own "proof of concept" acknowledgment pulls the score down from the 7+ range. The paper sits above the 6.00 papers (which make more restrictive assumptions and have narrower theoretical contributions) and is comparable to the 6.5–6.75 papers (strong theory, limited experiments).

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>