Now let me write the final consolidated review.

---

## Summary

This paper introduces the *conditional causal bandit* problem, where each arm is a conditional intervention (a policy that sets a node based on observed context). The main contribution is a complete graphical characterization of the *minimal globally interventionally superior set* (mGISS) — the smallest set of nodes guaranteed to contain the optimal node to intervene on. The authors prove that the mGISS equals the LSCA (lowest strict common ancestor) closure of the parents of the target variable Y (Theorem 13), a clean structural criterion. They then provide the C4 algorithm, which computes this set in linear time O(|V|+|E|), and demonstrate substantial search space pruning on both random and real-world causal graphs, with a modest bandit experiment showing accelerated convergence.

## Strengths

- **First complete graphical characterization of the minimal search space for conditional-intervention causal bandits.** Theorem 13 establishes that the LSCA closure of the parents of the target variable is exactly the mGISS. This is the first result of its kind for non-hard, single-node interventions, and is a genuine theoretical advance over prior work (Lee & Bareinboim 2018, which addressed multi-node hard interventions). The Λ-structure characterization (Theorem 12) provides an intuitive, visualizable criterion.

- **Efficient, well-motivated linear-time algorithm.** Algorithm 1 (C4) computes the mGISS in O(|V|+|E|) time (Theorem 16). The connector concept (Definition 14) and Lemma 15 provide a clean, provably correct basis for the algorithm. The linear-time complexity is a direct practical advantage for deployment as a pre-processing step.

- **Empirical evidence of substantial search space reduction.** Experiments on random graphs (up to 500 nodes) and realistic graphs from the `bnlearn` repository show that mGISS can prune over 90% of the search space in large, sparse graphs. The real-world graph experiments ground the theory in practical structures (train delays, medical networks). The bandit regret curves (Figure 3) confirm that pruning via mGISS does not sacrifice optimality and accelerates convergence, albeit on a simple baseline.

## Weaknesses

### Major

1. **The equivalence in Proposition 4 is presented without even a proof sketch in the main text, leaving a natural uniformity concern unaddressed.** Proposition 4 claims that conditional-intervention superiority (∃ a single policy g that works for all conditioning sets and all alternative policies) is equivalent to deterministic atomic-intervention superiority (for each unit n, ∃ an atomic value x that beats any atomic value for W). The latter allows x to depend on the full unit n, while the former requires a single function g mapping the observed Z_X to values. The paper's main theoretical result hinges on this equivalence, yet the main text provides no reasoning to bridge this gap. The proof is deferred entirely to the appendix. While the proof may well be correct, the absence of any sketch or intuition in the main text makes it difficult for a reader to assess the soundness of the paper's central reduction. This is the paper's most significant vulnerability.

2. **The bandit experiment is too weak to meaningfully support the paper's applied claims.** The experiment compares CondIntUCB (an ad-hoc UCB contextual bandit with no theoretical guarantees) with and without mGISS pruning. The improvement is nearly tautological — fewer arms means faster identification of a good arm — and the experiment does not compare against a natural heuristic baseline (e.g., using just Pa(Y), or a random subset of nodes of comparable size). The theoretical guarantee that pruning does not hurt optimality is already established, so the experiment primarily validates that the pruning is empirically non-vacuous (which the graph-level experiments already demonstrate). A more informative baseline would strengthen the applied narrative.

### Minor

3. **Strong assumptions on conditioning sets are identified but their practical limitations are not discussed.** The paper assumes (a) no latent confounders, (b) all ancestors of X are observed and included in Z_X, and (c) the "observable conditioning set" property (W ∈ An(X) ⇒ Z_W ⊆ Z_X). While these are stated clearly, the paper does not discuss how results degrade when these assumptions are violated or whether weaker conditions suffice. For practitioners whose graphs have unobserved ancestors or whose domain restricts Z_X, it is unclear whether the mGISS characterization still holds, or whether it provides any approximate guidance. This limits the paper's practical scope beyond what the limitations section currently conveys.

4. **Random graph experiments use only Erdős-Rényi graphs with a single topological order.** While the real-world graphs provide useful complementary evidence, the random-graph results may not generalize to other random graph families (e.g., scale-free, small-world). A brief discussion or experiment with an alternative generative model would strengthen the generality claims.

### Trivial

5. The paper does not explicitly state the complexity of computing An(U) as a pre-processing step for the C4 algorithm, though it is standard (BFS, O(|V|+|E|)).
6. The experimental setup always selects Y as the node with the most ancestors; a brief note on whether or how much this choice matters would be helpful.

## Nice-to-Haves

- A proof sketch for Proposition 4 in the main text (even a paragraph) would greatly enhance reader trust in the central reduction.
- A discussion of what happens when Z_X does not contain all ancestors of X (i.e., when the "we can always include them" assumption is violated) would clarify the boundaries of the result.
- An experiment comparing mGISS-based selection against a natural heuristic baseline (e.g., Pa(Y) only, or random subsets) would make the bandit experiment more informative.

## Removed Points

The following points from the input reviews were removed as they do not meet the inclusion criteria:

- **"Uniqueness of the mGISS (Proposition 6) is asserted without a clear argument"** — The proof is in the appendix; main-text proofs of uniqueness claims are not standard for this type of paper. Speculative extension ("if Proposition 4 were weakened, uniqueness might no longer hold") is not a weakness of the paper as written. **Reason: REMOVED (speculative, not grounded in paper content).**

- **"observable conditioning set' is introduced without a formal definition"** — The paper explicitly gives the definition: *W ∈ An(X) ⇒ Z_W ⊆ Z_X*. The critic's claim is factually incorrect. **Reason: REMOVED (factually wrong).**

- **"Introduction claim that single-node is harder is not argued"** — The paper does argue this (lines 67-77, Section 2): in multi-node, intervening on Pa(Y) is trivially sufficient; in single-node this is impossible when |Pa(Y)| > 1. The critic overlooked this. **Reason: REMOVED (strawman).**

- **"Footnote 3 assumption should be stated as part of the problem definition"** — The paper explicitly states this as part of the problem definition (Section 2, paragraph on conditional interventions). **Reason: REMOVED (strawman).**

- **"The quantification over all conditioning sets in Definition 1 seems excessive"** — This is an observation about the definition's strength, not a weakness. The paper's results are conditional on this definition. **Reason: REMOVED (not a weakness).**

- **Strength Finder's generic strengths** (e.g., "Proposition 4 bridges conditional and deterministic atomic superiority... This is a non-obvious equivalence") — These are kept as they are specific to the paper's content; similar for "Λ-structure characterization" and "reproducibility." However, the Strength Finder's claim about Proposition 4 being a strength is somewhat in tension with it being the paper's most significant vulnerability. I note this in the review.

- **"Missing related works"** concerns — Removed per hard rules (cannot verify existence of missing references).

## Novel Insights

None beyond the paper's own contributions. The paper's core insight — that the mGISS equals the LSCA closure of Pa(Y) and can be computed in linear time via connectors — is itself the novel contribution.

## Suggestions

1. **Add a proof sketch for Proposition 4 in the main text.** A brief argument (2–3 sentences) explaining how the assumptions on Z_X (An(X)\{X} ⊆ Z_X and the observable conditioning set property) bridge the uniformity gap between per-unit x and the function g would address the most natural concern a reader has with the paper.

2. **Strengthen the bandit experiment** by adding a simple baseline: e.g., pruning to the parents of Y only, or pruning to a randomly selected subset of the same size as the mGISS. This would clarify whether the mGISS provides benefits beyond the trivial effect of arm count reduction.

3. **Discuss the practical impact of violated assumptions.** A brief paragraph in Section 7 on what happens when ancestors of X are not fully observable, or when the conditioning sets do not satisfy the nesting property, would help practitioners assess the method's applicability.

4. **Report which real-world graphs were used** in the main text (they are currently in Appendix H), and include brief summary statistics (|V|, |E|, average degree) to support the claim that real graphs tend to be sparse.

## Score and Decision

**Round-1 bracket**: 5.0 – 6.5

Anchors retrieved (all rounds):

| Anchor ID | Avg Score | Round | Comparison to this paper |
|-----------|-----------|-------|------------------------|
| EzHPHhSQMD | 2.00 | R1 (low) | Unrelated topic, clearly weaker |
| MHy7PnRcRO | 3.00 | R1 (low) | Not causal bandits, clearly weaker |
| ScQ7irexRS | 3.00 | R1 (low) | Not causal bandits, clearly weaker |
| p0kabcRgJZ | 3.00 | R1 (low) | Not causal bandits, clearly weaker |
| gjvTNxVd2f | 5.50 | R1 (mid), R2 | Counterfactual SCB — most topically similar; both are SCB extensions with clean theory; this paper has cleaner self-contained theory but thinner experiments |
| QW0PchhVaD | 4.50 | R1 (mid) | Contextual Causal BO; this paper is stronger (tighter theory, algorithm with proof) |
| UNnHm7Lm4T | 4.00 | R1 (mid) | Confounded POMDPs, unrelated |
| uGLGPCatwh | 4.00 | R1 (mid) | Causal Meta-RL, unrelated |
| rxZdaKhu2I | 6.00 | R2 | CATE allocation; similar score range but different subfield |
| CWpQsAubxy | 6.50 | R2 | Active causal quantity estimation; different subfield |
| 040ClRXMf3 | 6.00 | R2 | Explainable NAMs, unrelated |

**Round-2 narrowing**: The Counterfactual SCB anchor (5.50) is the closest topical match. That paper was accepted as a poster with a reviewer consensus that the theory was sound but the significance was questioned by some. The current paper has cleaner, more self-contained theory (complete graphical characterization + linear-time algorithm) but thinner experiments and stronger assumptions. I rate it as comparable — slightly better on theoretical cleanness, slightly weaker on empirical evaluation.

**Final score: 5.5** — Solid theoretical contribution. The paper makes a genuine advance on a well-motivated problem. The main theoretical claim is clean and the algorithm is elegant. However, the bandit experiments are thin, the assumptions are strong without adequate discussion of their implications, and Proposition 4 (the linchpin of the theory) is presented without even a sketch in the main text, leaving a natural concern unaddressed. These factors keep the paper in the solid-but-not-strong range.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>