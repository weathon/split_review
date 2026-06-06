Now I have a clear picture. Let me calibrate:

**Comparison with anchors:**

- **YcW8i9VCf5 (6.0):** The paper under review is clearly stronger. The 6.0 anchor had substantive concerns about novelty (one reviewer said "I don't see any fundamental difference between the studied model and a standard bandit"), naming confusion, and unclear motivation. Our paper has a crisp, well-motivated problem formulation and clearly novel theoretical machinery.

- **u63OVngeSp (7.0):** Comparable quality. Both have novel theoretical constructs, proven guarantees, and algorithms. The 7.0 anchor had one reviewer give a 5 citing limited comparison to prior work and restrictive assumptions; another reviewer noted lack of real-world data. Our paper has real-world graph experiments but has the minor non-standard regret metric issue. The paper under review seems slightly more complete but comparable in overall quality.

- **bjxuqI4KwU (7.5):** This is a more fundamental theoretical contribution (solving an identifiability gap for linear SCMs), with uniformly high reviewer scores (8,8,6,8). Our paper is well-executed but narrower in fundamental impact — it characterizes the search space for a specific problem class rather than solving a broad identifiability question.

**Final assessment:** 7.0 — a solid accept. The paper makes a clean, well-scoped theoretical contribution with supporting empirical evidence. Only minor, fixable issues remain.

---

## Summary

This paper addresses the problem of finding the minimal set of nodes in a causal graph guaranteed to contain the optimal single-node conditional intervention for maximizing a target variable Y. The core contributions are: (1) proof that conditional-intervention superiority reduces to deterministic atomic-intervention superiority (Proposition 4), (2) a graphical characterization of the minimal globally interventionally superior set (mGISS) as the LSCA closure of Y's parents, equivalently the set of nodes forming Λ-structures over those parents (Theorems 12, 13), and (3) the C4 algorithm that computes this set in O(|V|+|E|) time (Theorem 16). Empirical results on random and real-world graphs demonstrate substantial search-space reduction and improved bandit convergence when using the mGISS.

## Strengths

- **Elegant theoretical reduction (Proposition 4):** The equivalence between conditional-intervention superiority over probabilistic SCMs and deterministic atomic-intervention superiority is a non-trivial technical bridge. It allows the entire subsequent analysis to proceed in the simpler deterministic setting while guaranteeing the result holds for the more general conditional-intervention case.

- **Novel Λ-structure characterization (Theorem 12):** The result that the LSCA closure equals the set of nodes forming Λ-structures over pairs in the target set provides an elegant, purely graph-theoretic characterization. Λ-structures (Definition 11, Figure 2a) — pairs of internally disjoint directed paths from a common ancestor to two target nodes — capture the exact condition under which a node can simultaneously influence multiple targets. This is a genuinely novel graph-theoretic concept.

- **Linear-time C4 algorithm with correctness proof (Theorem 16, Algorithm 1):** The connector-based single-pass algorithm computes the mGISS in O(|V|+|E|) time, which is asymptotically optimal. The connector concept (Definition 14, Lemma 15) is clever: a node whose children all share the same connector is "covered" by that downstream node and can be pruned; a node whose children carry multiple distinct connectors must be retained. The algorithm is simple enough to be immediately usable.

- **Complete pipeline from graph to minimal intervention set (Theorem 13):** The main result synthesizes the definitions into a single theorem: the mGISS equals the LSCA closure of Pa(Y). The counterexamples in Figure 1 (especially 1d) convincingly demonstrate that simpler heuristics (LCAs) fail, justifying the more sophisticated LSCA machinery.

- **Substantial search-space reduction on real-world graphs:** On bnlearn benchmark graphs, the method achieves over 90% search-space reduction for several large models. The random-graph experiments show the method is most effective on sparse graphs, which real-world causal models tend to be.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Non-standard regret metric in bandit experiments:** The cumulative regret is computed against the "estimated best arm, defined as the arm that most runs concluded to be the best at the end of training" (footnote 11), rather than against the true optimal arm. If the brute-force and mGISS approaches converge to different arms in finite samples, their regrets are measured against different baselines, partially confounding the comparison. Since Theorem 13 already guarantees the mGISS contains the true optimal node, the direction of the results is plausible, but the empirical evidence for improved convergence is weaker than it appears. This is fixable by computing regret against the true optimal arm (available since the SCM is known in the experimental setup).

- **CondIntUCB algorithm is insufficiently specified:** The bandit algorithm used in Section 6 is described only narratively in two sentences — there is no pseudocode, and key parameters (UCB exploration constant, number of runs per context, convergence criteria) are not stated. This makes the bandit experiments difficult to reproduce without consulting the supplementary code.

- **Limited scale of bandit experiments:** Only 4 datasets with relatively small graphs (8–109 nodes) are used for the bandit experiments. While partly justified by the need to run brute-force comparisons, this limits the demonstration of scaling benefits that the linear-time C4 algorithm theoretically enables.

### Trivial

- **Algorithm 1 does not handle the |C| = 0 case explicitly:** The loop iterates over all V ∈ V\U in reverse topological order, but for nodes not in An(U), the set C will be empty and c[V] is never assigned. This is harmless in practice but makes the pseudocode slightly incomplete. An explicit else branch or restriction to An(U) would clarify the intended behavior.

## Nice-to-Haves

- **Minimality illustration:** While minimality is a theoretical claim and cannot be empirically "proven," including a concrete example where removing any single node from the mGISS causes a specific SCM to fail to find the optimal intervention would illustrate tightness for readers.
- **Compute regret against true optimal arm** to make the bandit results unambiguous.
- **Broader bandit evaluation** on larger graphs (even with approximate baselines) to better demonstrate scaling benefits.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The gap between the theoretical model and the bandit experiments is not fully bridged"** — The harsh critic noted that experiments don't validate the "minimal" part of the claim. This is inherent: minimality is a theoretical property that cannot be empirically validated by design. The paper already distinguishes between what the experiments demonstrate (search-space reduction + improved convergence) and what the theory guarantees (minimality). Not a weakness.

- **"The conditioning set assumption is strong — what happens when Z_X is a proper subset of ancestors?"** — The paper explicitly addresses this in footnote 3: "We are not claiming that all variables in An(X)\{X\} need to be in Z_X for the best decision to be made, or for our results to hold, but that we can always include them in Z_X under the assumptions of our problem." The paper states its assumptions clearly and acknowledges the no-latent-confounders limitation in the conclusion. Removed.

- **"Missing intuition before Proposition 4"** — This is a presentation preference, not a substantive weakness. The paper states the equivalence clearly and the formal proof is in the appendix.

- **"Non-strict common ancestor motivation unclear"** — Already discussed through examples in the paper.

- **"No comparison against alternative node selection approaches"** — The paper's contribution is the characterization itself; brute-force is the natural baseline. There are no existing alternative node-selection methods for this specific problem setting. Asking for comparison to non-existent methods is scope creep.

- **Formatting/style nitpicks** from the harsh critic — Removed per hard rules.

## Novel Insights

The most novel technical insight is the equivalence between conditional and deterministic atomic superiority (Proposition 4), which reduces a complex stochastic optimization problem over conditional interventions to a deterministic graph-theoretic one. Combined with the Λ-structure characterization, this reveals that the answer to "which nodes could possibly be optimal to intervene on" depends only on graph topology — specifically on the existence of internally disjoint directed paths from a common ancestor to pairs of Y's parents. The connector-based C4 algorithm then provides an elegant computational realization: a node is worth testing exactly when its children have different "connectors" to the target set, meaning the node can influence the target through multiple distinct channels.

## Suggestions

- Replace the estimated-best-arm regret metric with regret against the true optimal arm (computable offline since the SCM is known). This would make the bandit results unambiguously valid.
- Add a concrete minimality example (a graph + SCM where removing any node from the mGISS causes the optimal intervention to be missed) to illustrate the tightness of the characterization.
- Include pseudocode and parameter specification for CondIntUCB to improve reproducibility of the bandit experiments.

---

**Calibration summary (all anchors retrieved):**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| MVpvyeVeyI (Causal BO Unknown Graphs) | 3.40 | R1 | Much weaker — rejected paper with limited contributions |
| JzFLBOFMZ2 (CSL Supervised by LLM) | 3.20 | R1 | Much weaker — rejected |
| fSxiromxAq (Sparse Causal Model) | 3.00 | R1 | Much weaker — rejected |
| AvXrppAS2o (Outcome Prediction via CSL) | 3.00 | R1 | Much weaker — rejected |
| IPayPEGwdE (Causal Contextual Bandits Adaptive) | 5.00 | R1 | Weaker — rejected, limited experiments, restrictive assumptions |
| YcW8i9VCf5 (Adversarial CBO) | 6.00 | R1,R2 | Our paper is stronger — clearer contribution, fewer substantive weaknesses |
| BZYIEw4mcY (Causal Discovery Latent Variables) | 6.00 | R1,R2 | Different topic; similar quality band |
| pOoKI3ouv1 (Robust agents learn causal models) | 5.75 | R2 | Similar quality — interesting theory but less complete pipeline |
| mGmx41FTTy (Two Time-Slices Topological) | 6.33 | R2 | Similar quality band |
| jE6VXUhxq9 (Causal Discovery Deterministic) | 6.25 | R2 | Similar quality band |
| u63OVngeSp (Causal Order Single-Var Interventions) | 7.00 | R2 | Our paper is comparable — slightly more complete empirical validation |
| SKulT2VX9p (Interventional Fairness PDAG) | 6.67 | R2 | Our paper is slightly stronger |
| bjxuqI4KwU (Linear SCM Identification) | 7.50 | R2 | Our paper is weaker — the anchor solves a more fundamental identifiability problem |
| Bp0HBaMNRl (Differentiable Causal Discovery) | 6.75 | R2 | Our paper is comparable or slightly stronger |
| FhQSGhBlqv (Versatile Causal Discovery Hidden) | 7.50 | R2 | Our paper is weaker — the anchor has broader fundamental results |

**Round 1 bracket:** 5.5–7.5  
**Round 2 narrowed to:** 6.5–7.5, with the paper sitting closest to the u63OVngeSp (7.0) anchor.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>