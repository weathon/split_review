Now I have a thorough understanding of the paper and all reviewer claims. Let me write the final consolidated review.

---

## Summary

This paper studies conditional causal bandits where arms are single-node conditional interventions, and provides a graphical characterization of the minimal set of nodes guaranteed to contain the optimal intervention. The core theoretical result (Theorem 13) identifies this minimal set as the LSCA closure of the parents of the reward variable Y. The paper also proposes the C4 algorithm, which computes this closure in O(|V|+|E|) time, and validates the approach empirically on both random and real-world graphs, demonstrating substantial search-space pruning and improved bandit regret.

## Strengths

- **Novel graphical characterization via Λ-structures**: Theorem 12 provides an elegant reformulation of the iterative LSCA closure in terms of Λ-structures — nodes that lie at the apex of two internally-disjoint paths to the target set. This is a genuinely non-trivial graph-theoretic insight that simplifies both proofs and algorithm design.

- **Linear-time C4 algorithm with clean correctness proof**: The connector-based algorithm (Algorithm 1) and its analysis via Lemma 15 and Theorem 16 are correct and well-structured. The connector concept provides an intuitive, implementable rule: a node belongs to the closure iff its children in the ancestor subgraph have distinct connectors. This is a solid algorithmic contribution independent of the conditional-intervention framework.

- **Substantial empirical pruning**: On sparse random graphs (500 nodes, degree 2), the mGISS retains only 17% of ancestors (Figure 5). On real bnlearn graphs like pathfinder, over 90% of the search space is pruned (Figure 6). These results convincingly demonstrate the practical value of the graphical characterization for reducing search space.

- **Bandit regret improvement**: Using the mGISS with a UCB-based conditional bandit (CondIntUCB) yields clearly lower cumulative regret and faster convergence across four real-world datasets (Figure 3), directly illustrating the downstream benefit of node-space pruning.

- **Well-motivated and well-positioned problem**: The paper clearly distinguishes its setting (single-node conditional interventions, no latent confounders) from Lee & Bareinboim (2018, 2020) and contextual bandits, making the novelty and scope explicit.

## Weaknesses

### Major

- **The proof of Proposition 4 (⇐) contains a well-definedness gap.** The construction on line 1226 defines the policy as `g*(f̄_{Z_X}(n)) = f̄_X[W](h*(f̄_{Z_W}(n)), n)`. The right-hand side depends on the full noise vector **n**, but the policy must be a function of the observed variables Z_X alone. Specifically, N_X (the noise variable of X) is not determined by f̄_{Z_X}(n) since X ∉ Z_X, yet N_X affects f̄_X[W](w, n) through X's structural equation. Two noise settings n₁, n₂ with identical Z_X values may produce different values of f̄_X[W](h*(f̄_{Z_W}(n)), n), rendering g* ill-defined. This gap is not a minor oversight — Proposition 4 is the bridge connecting the deterministic atomic framework (in which Theorem 13 is proved) to the conditional bandit setting (which is the paper's main motivation). Without a correct proof of the (⇐) direction, Theorem 13 is only established for deterministic atomic interventions, not for the conditional interventions the paper claims to solve. The paper's core claim about applicability to conditional causal bandits is therefore unsubstantiated. (The (⇒) direction and the independent algorithmic/graphical contributions are unaffected.)

### Minor

- **Bandit experiment description is high-level.** The CondIntUCB algorithm is sketched rather than fully specified: the UCB exploration parameter, the mechanism for coordinating node-level and per-context UCB instances, and the precise regret computation are described by reference to Lattimore & Szepesvári (2020, §18.1) but not spelled out. While the approach is standard, more explicit detail would strengthen replicability. The regret curves include standard-deviation bands but no formal statistical tests; however, the visual separation between mGISS and brute-force curves is sufficiently clear that this does not weaken the empirical argument.

### Trivial

- The claim in the introduction that single-node interventions are "more challenging" than multi-node interventions is stated without substantial justification in that paragraph, though the reasoning is provided later (lines 209–211). A brief forward reference would help.

## Nice-to-Haves

- Comparing the mGISS against other natural node-selection heuristics (e.g., LCA closure of parents, or simply all parents of Y) in the bandit experiments would strengthen the empirical case that the mGISS is not merely smaller but optimally so. The current comparison against brute-force establishes that pruning helps but not that the mGISS is the best possible pruning.

## Removed Points

These points are flagged to be removed — treat them with caution:

- **Harsh Critic: "The bandit experiments lack statistical rigor (no confidence bands or tests)."** → *Weakened to Minor.* The paper reports standard deviation bands, which is standard practice in the bandit literature for regret curves. Formal hypothesis testing is not the norm for this type of empirical evaluation.

- **Harsh Critic: "The claim that single-node interventions make the problem more challenging is stated rather than argued."** → *Removed.* The paper does provide the argument (lines 209–211): with multi-node interventions, simply intervening on all parents of Y always works; with single-node interventions, this is impossible when |Pa(Y)| > 1, making the search space non-trivial. This is brief but sufficient for an introduction.

- **Harsh Critic: Missing baselines in regret experiments.** → *Moved to Nice-to-Haves.* The core claim is about preserving optimality while pruning, so comparison against the full set is the right benchmark. Comparison against other heuristics would be a bonus.

- **Harsh Critic: "The proof of Proposition 4 (⇐) is incorrect, and this invalidates the main claim."** → *Kept as Major.* Verified against the paper. The concern is genuine: the policy construction is not obviously well-defined as a function of Z_X alone. However, the (⇒) direction, the Λ-structure characterization (Theorem 12), the C4 algorithm, and Theorem 13 within the deterministic atomic framework are unaffected.

- **Strength Finder: "Equivalence of conditional and deterministic atomic superiority (Proposition 4) is surprising and essential."** → *Qualified.* The claim is important, but the proof gap means this strength cannot be taken at full face value. The insight remains interesting and may well be correct, but the current proof is incomplete.

## Novel Insights

The Λ-structure characterization (Theorem 12) — that the LSCA closure of a set U equals exactly the set of nodes forming Λ-structures over (U, U) — is a genuinely novel graph-theoretic observation. It transforms a recursive, algorithmic definition into a clean, static structural condition that simultaneously simplifies the proof of correctness for the mGISS characterization and motivates the connector-based C4 algorithm. This connection between recursive common-ancestor closure and the Λ-structure pattern appears to be original and may have applications beyond causal bandits in graph algorithm design.

## Suggestions

- The authors should either (a) provide a corrected proof of Proposition 4 (⇐) that properly handles the well-definedness of the constructed policy, or (b) restrict the scope of Theorem 13's applicability claim to the deterministic atomic setting and clearly separate which results are proven for which setting. The gap is real but likely fixable — one possible route is to construct g* using the SCM's structural equations evaluated at the observed Z_X rather than the full noise vector, and prove that this achieves the required inequality in expectation.

- Provide a more complete specification of the CondIntUCB algorithm, including the UCB formula and exploration parameter, either in the main text or a dedicated appendix section, to improve reproducibility.

## Anchor Comparison and Score

| Anchor Paper | Path | Avg Score | Comparison |
|---|---|---|---|
| Counterfactual Structural Causal Bandits | gjvTNxVd2f | 5.50 | Similar domain; accepted with mixed reviews. Stronger than our paper: its theoretical results are sound without significant proof gaps. |
| Contextual Causal Bayesian Optimisation | QW0PchhVaD | 4.50 | Accepted with clarity issues but sound theory. Our paper has a more serious theoretical gap but arguably more novel graph-theoretic machinery. |
| On Transportability for Structural Causal Bandits | R2mMw1lesm | 3.50 | Rejected; limited novelty, straightforward extension. Our paper has substantially more novel characterization and algorithm. |
| Competition is the key | EzHPHhSQMD | 2.00 | Rejected; fundamental issues with claims and soundness. Our paper is clearly stronger. |
| Theoretical Guarantees for Causal Discovery | V7pT2ZRoTB | 4.50 | Accepted; theoretical paper with sound proofs. Our paper's graphical characterization is similarly deep, but the proof gap is a liability. |
| On Measuring Influence | VHdF91MvJq | 5.00 | Accepted; novel measure with theoretical backing. Our paper has a clearer practical application but a more significant proof issue. |

The paper under review has substantial strengths: a novel graphical characterization, a clean linear-time algorithm, and convincing empirical results. However, the proof gap in Proposition 4 (⇐) directly undermines the paper's central claim about applicability to conditional bandits — the very setting the paper is marketed for. Without this bridge, the paper only solves the deterministic atomic case. This is a significant but potentially fixable issue. Relative to the anchors, the paper sits between the Transportability SCB (3.50, rejected for limited novelty) and the Contextual Causal BO (4.50, accepted despite clarity issues). The proof gap here is more serious than mere clarity issues but the remaining contributions are more novel than a straightforward framework extension.

**Score: 4.0 — The paper has real contributions but a significant theoretical gap in a key proof; acceptable with major revisions to fix or circumscribe this gap.**

MY FINAL SCORE: <pineapple>4.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>