Now I have a full picture of the paper. Let me write my review.

---

## Summary

This paper studies *conditional causal bandits*, a variant of the multi-armed bandit problem where each arm is a single-node conditional intervention do(X = g(Z_X)) in a Structural Causal Model, and the agent knows the causal graph but not the structural assignments or noise distribution. The central contribution is a graphical characterization of the **minimal Globally Interventionally Superior Set (mGISS)** — the smallest set of nodes guaranteed to contain the node yielding the optimal conditional intervention — proven to equal the LSCA closure L^∞(Pa(Y)) of the parents of the reward node Y. A linear-time algorithm, C4, computes this set in O(|V| + |E|). Experiments on both synthetic and real-world Bayesian network graphs confirm substantial search space reduction, with an integrated UCB-based algorithm showing faster regret convergence.

---

## Strengths

- **Proposition 4 (conditional ↔ deterministic atomic superiority) is a non-obvious and elegant result.** The equivalence between conditional-intervention superiority and deterministic atomic-intervention superiority cleanly reduces a complex stochastic problem to reasoning about deterministic SCMs, considerably simplifying the analysis in the rest of the paper.

- **Theorem 13 provides a principled, complete graphical characterization.** The mGISS = L^∞(Pa(Y)) = Λ(Pa(Y), Pa(Y)) result is both tight (minimal) and elegantly expressed via Λ-structures. The LSCA closure and its Λ-structure characterization (Theorem 12) give a clear geometric intuition that is illustrated convincingly by Figures 1 and 2.

- **The C4 algorithm is practical and provably efficient.** Computing the connector for every ancestor node in reverse topological order achieves O(|V| + |E|) time — linear in graph size — making the pre-processing step negligible relative to any downstream bandit algorithm. The algorithm's correctness proof is grounded in Lemma 15, which characterizes connectors precisely.

- **Experiments consistently support the claims.** On real-world `bnlearn` networks the mGISS can eliminate over 90% of candidate nodes in larger sparse models; regret curves for four distinct networks uniformly show faster convergence when C4 is used as a pre-processing step, with the improvement scaling with graph size.

- **Problem novelty is well-established.** The paper is explicit about how its setting differs from prior work: Lee & Bareinboim (2018) studied multi-node hard interventions; contextual bandits do not exploit causal graph structure; Subramanian & Ravindran (2022, 2024) pre-specify the node. This is genuinely the first complete characterization of the minimal search space for single-node conditional interventions.

---

## Weaknesses

### Fatal
None.

### Major

- **No regret bounds for CondIntUCB.** The paper positions itself in the MAB literature, yet provides no theoretical regret guarantees for the proposed CondIntUCB algorithm (or for the mGISS-pruned variant in particular). A reader wanting to understand the statistical savings — not just the graph-structural savings — from reducing from |An(Y)| to |mGISS_Y(G)| arms is left without a quantitative answer. The paper cites Lattimore & Szepesvári (2020, §18.1) for the contextual UCB construction; it would be feasible at least to state how standard contextual bandit regret bounds scale with the number of nodes/contexts and how mGISS reduction modifies that scaling.

- **Single-node, no-latent-confounders assumptions are significant joint restrictions.** The paper clearly acknowledges these limitations, but the combination is strong: multi-node interventions are already well studied (Lee & Bareinboim 2018, 2019) and confounders are ubiquitous in practice. The paper argues that single-node is harder than multi-node for the *search-space reduction problem* (which is true), but it does not discuss whether the mGISS construction has any reasonable extension or partial validity under hidden-variable SCMs — even a negative example showing it breaks would be informative.

### Minor

- **Conditioning set Z_X is pre-specified and maximally large.** The paper assumes An(X)\{X} ⊆ Z_X ⊆ V\De(X), and the experiments default to Z_X = An(X)\{X}. This is a strong assumption in high-dimensional settings where not all ancestors are observable or the policy class must be restricted. A brief discussion of how different (smaller) conditioning sets affect the mGISS would strengthen the practical relevance.

- **Experimental comparison is limited to brute-force.** The CondIntUCB experiments compare only mGISS-pruned vs. full-ancestor-set UCB. There is no comparison against other causal MAB algorithms (e.g., those exploiting the causal structure within the arms), making it hard to judge whether the node-selection reduction translates to end-to-end competitive performance.

### Trivial
None.

---

## Nice-to-Haves

- A theorem or corollary bounding regret savings as a function of |mGISS| vs |An(Y)| would substantially strengthen the bridge between the structural result and the bandit literature.
- An analysis or example of the mGISS behavior when a partial causal graph is known (e.g., Markov equivalence class) would be useful for practitioners without complete graph knowledge (the current suggestion of taking the union over candidate graphs is correct but not analyzed).
- Reporting statistical uncertainty (confidence intervals) on the search-space reduction fraction in the random-graph experiments would be more rigorous than reporting means alone.

---

## Novel Insights

The most genuinely novel insight in this paper is that the problem of choosing which single node to intervene upon conditionally is, in terms of worst-case optimality, *equivalent* to choosing which node to intervene upon atomically in a deterministic SCM (Proposition 4). This equivalence is surprising because conditional interventions are strictly more expressive than atomic ones, yet the problem of selecting the *node* is equally hard under both. This allows the rich structure of deterministic interventions to be leveraged in proofs without loss of generality. The Λ-structure characterization of the LSCA closure (Theorem 12) is also a clean structural insight: a node V belongs to the minimal search space if and only if it lies at the apex of two node-disjoint directed paths to distinct members of Pa(Y), a condition that is both intuitive and computationally tractable.

---

## Suggestions

- Prove or conjecture a regret bound for CondIntUCB (pruned with C4) to quantify the statistical benefit of the mGISS reduction, even in a simplified setting.
- Provide at least one example showing how the mGISS changes or becomes undefined/incorrect in the presence of a latent confounder, to help readers understand why extending to hidden variables is non-trivial.
- In the random-graph experiments, report standard deviations or confidence intervals alongside means.

---

## Score and Decision

The paper delivers a clean, rigorous theoretical foundation for a new and natural variant of causal bandits. The key results — Proposition 4, Theorems 12 and 13, and the C4 algorithm — are all novel, well-motivated, and supported by proofs. The empirical validation is consistent with the theoretical claims. The primary shortcoming is the absence of regret-theoretic analysis; the paper is essentially a structural/graphical paper grafted onto a bandit motivation, and the bandit half is under-developed theoretically. The scope limitation (single-node, no confounders) is acknowledged but genuine. Taken together, this is a sound, useful contribution that advances a well-posed open problem, suitable for acceptance at a venue valuing theoretical rigour.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>