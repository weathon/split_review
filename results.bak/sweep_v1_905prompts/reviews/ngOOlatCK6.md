Now I have thoroughly verified the paper's content against all reviewer claims. Let me produce the final consolidated review.

## Summary

This paper studies a new variant of causal bandits where the arms are single-node *conditional interventions* (the value of the intervened variable depends on observed context) rather than the hard interventions studied in prior work. The core contribution is a graphical characterization of the *minimal* set of nodes (the mGISS) guaranteed to contain the optimal conditional intervention node. The paper proves this mGISS equals the LSCA closure of the parents of the target variable, provides an elegant $\Lambda$-structure characterization, and gives a linear-time algorithm (C4) to compute it. Empirical results on random and real-world graphs show that C4 prunes the search space substantially, and integrating mGISS pruning with a UCB-based bandit algorithm reduces cumulative regret.

## Strengths

- **First complete graphical characterization of the minimal search space for conditional causal bandits.** Theorem 13 proves that the LSCA closure $\mathcal{L}^\infty(\text{Pa}(Y))$ equals the mGISS. This is a novel result: prior work on search-space reduction for causal bandits (Lee & Bareinboim 2018) addressed multi-node hard interventions under latent confounders, which is a fundamentally different problem. The characterization via $\Lambda$-structures (Theorem 12) is clean and provides actionable intuition about which nodes matter.

- **Linear-time algorithm with a clear correctness argument.** The C4 algorithm (Algorithm 1) runs in $O(|V|+|E|)$ using a connector-based propagation scheme. The connector concept is well-motivated (Lemma 15), and the algorithm's correctness proof (Theorem 16) ties directly to the graphical characterization. This makes the theoretical contribution directly usable as a preprocessing step.

- **Equivalence reduction that simplifies the problem while being non-trivial.** Proposition 4 shows that conditional-intervention superiority (Definition 1, over all SCMs and all policies) is equivalent to deterministic atomic-intervention superiority (Definition 2). This is not obvious — conditional interventions allow arbitrary context-dependent policies while atomic interventions fix a single value — and the equivalence enables all subsequent analysis to be carried out in the simpler deterministic setting. This technique can benefit future work on conditional interventions.

- **Clear problem formulation and careful differentiation from prior work.** The paper precisely defines the conditional causal bandit problem, motivates the conditioning-set assumptions with concrete examples (traffic control, medical treatment), and explicitly contrasts the setting with contextual bandits and prior causal bandit formulations (Sections 2, 7). The scope and limitations (no latent confounders, observable ancestors) are stated transparently.

## Weaknesses

### Major

None.

### Minor

- **The bandit experiments compare mGISS only against brute-force (all ancestors), not against a random subset of the same size.** The results show that pruning reduces regret — but this is partly guaranteed by having fewer arms. A comparison against a random subset of nodes of size $|\text{mGISS}|$ would isolate whether the *specific* nodes in the mGISS carry the useful structure, as opposed to any small set. Without this, the regret experiment primarily validates that fewer arms reduce regret, not that the mGISS is the *right* set of arms. The paper's claims are about search-space reduction, so this does not threaten the core contribution, but it weakens the empirical demonstration.

- **The random-graph experiment selects $Y$ as the node with the most ancestors.** This choice biases the results toward larger ancestral sets and potentially inflates the pruning fraction, since nodes with many ancestors tend to sit deeper in the graph where more ancestors are subsumed. Reporting results averaged over all possible choices of $Y$ (or over multiple random $Y$ per graph) would give a more representative picture. The existing numbers are still informative, but the reported pruning rates should be interpreted as upper-end estimates.

- **Proofs of all key results (Proposition 4, Proposition 6, Theorem 13) are deferred entirely to the appendix.** This is standard practice in ML/AI conferences, and the paper clearly states that proofs are in the appendix. However, the core equivalence (Proposition 4) is the entire bridge between the bandit problem and the graph-theoretic analysis. Even a one-paragraph proof sketch in the main text — explaining *why* the universal quantifier over SCMs allows the reduction to deterministic atomic interventions — would significantly improve reader trust and reduce the paper's dependence on the appendix.

- **The assumption that all ancestors of $X$ are observed and included in $\mathbf{Z}_X$ limits applicability.** The paper acknowledges this and provides motivating examples where it holds. Nevertheless, in many real-world settings some ancestors may be unobserved, and the characterization's reliance on this assumption means the mGISS may not be a valid guarantee when it is violated. This is noted as a direction for future work, but deserves explicit mention as a limitation in the main-text conclusion.

### Trivial

- Figure 1's caption is rendered as repeated text ("Figure 1: Four causal graphs... appears twice). The paper should ensure a single clean caption in the camera-ready version.

## Nice-to-Haves

- Include a proof sketch of Proposition 4 in the main body (one paragraph).
- For the bandit experiment, add a random-subset baseline of size $|\text{mGISS}|$ to verify that the specific node selection matters.
- For the random-graph experiment, report results averaged over multiple choices of $Y$ per graph, not only the node with the most ancestors.
- Discuss when the mGISS is large (e.g., dense graphs) to give practitioners a clearer sense of when the method provides the most benefit.

## Removed Points

- *Criticism that Definition 1 uses $\tilde{d}o$ as a formatting artifact* — This is a parser issue, not an author error. Removed per formatting-artifact rule.
- *Criticism that computing $\text{An}(\mathbf{U})$ in C4 line 6 is not accounted for in complexity analysis* — Computing ancestor sets via reachability is a standard $O(|V|+|E|)$ operation and is within the stated bound. Removed per strawman rule.
- *Criticism that Proposition 4 and Proposition 6 lack any justification in the main text* — The paper explicitly states "All proofs of the results presented in the paper can be found in the appendix" (line 90–91). Deferring proofs to the appendix is standard. The point is demoted to Minor (as a presentation suggestion) rather than treated as a structural flaw.
- *Several generic strengths from the Strength Finder* ("this paper addressed an important problem", "this paper targeted an interesting question") — Removed as generic/superficial.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add a 3–5 sentence proof sketch of Proposition 4 in Section 3 to let the reader assess the core equivalence without consulting the appendix.
2. Strengthen the bandit experiment with a random-baseline comparison of size $|\text{mGISS}|$ nodes, and report results for multiple target-node choices in the random-graph experiment.
3. Explicitly state in the conclusion (Section 7) that the mGISS guarantee assumes no latent confounders and observable ancestors, and note that these are directions for future work (the paper already does this for latent confounders; doing so for the ancestor-observability assumption would be symmetric).

## Score and Decision

**Calibration Report**

Round 1 — Bracketing: Queries on "causal bandits minimal intervention set graphical characterization" returned weak anchors at 3.00–3.25 (various causal structure learning papers, rejected); middle anchors at 5.00–6.50 (causal bandits and causal Bayesian optimization papers with mixed accept/reject decisions); strong anchors at 8.00 (causal discovery / representation learning, accepted). The paper clearly sits in the middle band. **Round 1 bracket: [5.5, 7.5]**.

Round 2 — Narrowing: Queries at (5.0, 7.0) and (6.0, 8.0) returned anchors:
- **YcW8i9VCf5** (avg 6.0, accepted): Adversarial CBO paper. Comparable quality; the current paper has a cleaner theoretical contribution but weaker empirical baselines.
- **u63OVngeSp** (avg 7.0, accepted): Causal order from interventions. Stronger experiments; the current paper is slightly below this in empirical validation.
- **MVpvyeVeyI** (avg 6.5, rejected): CBO with Unknown Graphs. Mixed reviews (5,8,3,10); the current paper has more cohesive review profile.
- **BZYIEw4mcY** (avg 6.0, accepted): Causal discovery with latent variables. Clean contribution, accepted uniformly.
- **8muemqlnG3** (avg 6.5, accepted): Causal discovery via BO. Solid theoretical+empirical work.

The paper is comparable to **YcW8i9VCf5** (avg 6.0, accepted) and **BZYIEw4mcY** (avg 6.0, accepted) — it has a clear, novel theoretical contribution, an elegant algorithm, and adequate empirical support. It is weaker than **u63OVngeSp** (avg 7.0) in terms of experimental depth and weaker than **M0xK8nPGvt** (avg 7.5) overall. **Final score: 6.0**.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>