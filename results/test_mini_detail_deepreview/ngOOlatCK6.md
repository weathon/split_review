Now I have all the information needed. Let me write the consolidated review.

## Summary

This paper studies conditional interventions in causal bandits — where the agent chooses both which node to intervene on and a policy for setting its value based on observed context. The core contribution is characterizing the *minimal globally interventionally superior set* (mGISS): the smallest set of nodes guaranteed to contain the optimal intervention node. The paper proves this equals the LSCA closure of the parents of the target variable (Theorem 13), gives an elegant alternative characterization via Λ-structures (Theorem 12), and provides a linear-time algorithm (C4) to compute it (Theorem 16). Experiments on random and real-world causal graphs show the mGISS can prune over 90% of the ancestor set for large models, and integrating it into a UCB-based bandit algorithm reduces cumulative regret.

## Strengths

- **Novel theoretical characterization of the mGISS for conditional interventions.** The paper is the first to fully characterize the minimal search space for a causal bandit problem with non-hard interventions. Proposition 4 (equivalence of conditional-intervention superiority and deterministic atomic-intervention superiority) is a non-trivial technical bridge that enables the graphical analysis. The resulting characterization (mGISS = LSCA closure of Pa(Y)) is clean and well-motivated through the intuitive Λ-structure definition (Theorem 12, Figure 2a).

- **Linear-time C4 algorithm.** Algorithm 1 computes the mGISS in O(|V|+|E|) time through a single reverse-topological pass using the connector concept (Definition 14, Lemma 15). The connector mechanism is elegant — nodes are added to the closure when their children have multiple distinct connectors, which directly corresponds to Λ-structure membership. This makes the method practical as a pre-processing step for any conditional bandit algorithm.

- **Convincing search-space reduction on real-world graphs.** On the bnlearn repository graphs (asia, sachs, child, pathfinder, and others) plus a railway network graph, the mGISS prunes over 90% of the ancestor set for the largest models (Section 6, with full bar plot in Appendix H Figure 6). These are well-known, standard benchmark graphs, making the results easy to interpret and reproduce.

- **Thorough random-graph ablation across graph size and density.** Experiments on 1000 Erdős-Rényi graphs across 4 node counts (20–500) and 4 expected degree settings show that pruning effectiveness increases with graph size and sparsity — exactly the regime where the method is most needed. For 500-node graphs at expected degree 2, only 17% of ancestor nodes remain in the mGISS.

- **Clear problem framing and honest scope articulation.** The paper carefully defines conditional interventions with observable conditioning sets (Section 2), including the inclusion constraints An(X)\{X\} ⊆ Z_X ⊆ V\De(X) and the monotonicity condition. The limitations (no latent confounders, single-node interventions) are explicitly stated and scoped as future work, with a clear positioning relative to Lee & Bareinboim (2018; 2020).

## Weaknesses

### Major

None.

### Minor

- **The bandit experiment (Figure 3) is underspecified.** The paper states it uses bnlearn datasets and a custom CondIntUCB algorithm, but does not describe (i) how the SCM reward is simulated from the bnlearn CPTs, (ii) the domain sizes and how the per-context UCB instances were updated in practice, (iii) the reward scale, or (iv) how the total number of rounds was chosen ("as to observe near convergence" is vague). The datasets were selected "because both An(Y) and mGISS_Y(G) are sufficiently small" — but this only addresses feasibility for the node-selection UCB, not the per-context UCBs needed for the policy step. The supplementary code (mentioned in the reproducibility statement) likely fills some of these gaps, but the paper itself should provide enough detail for a reader to assess the experiment without running code. **That said**, this experiment is supplementary to the main contribution — the search-space reduction experiments already demonstrate practical utility independently.

- **The bandit experiment uses an estimated best arm ("the arm that most runs concluded to be the best at the end of training") to compute regret, which introduces circularity.** If the estimated best arm is derived from the same algorithm being evaluated, the regret comparison between mGISS and brute-force could be biased if one setting converges to a different "best" node. The paper should clarify whether the estimated best arm was computed independently (e.g., by exhaustive search in a fixed SCM).

### Trivial

None.

## Nice-to-Haves

- Include a brief proof sketch of Proposition 4 in the main text (2–3 sentences explaining why conditional-intervention superiority reduces to deterministic atomic-intervention superiority). The current paper defers entirely to the appendix; a sketch would increase reader confidence and self-containedness.
- Clarify the definition of the "observable conditioning set" formally (currently introduced only informally on page 3).

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Proposition 4 proof unverifiable from main text"** (Harsh Critic): Deferred proofs to appendices are standard practice at ICLR. The paper clearly states the proposition and provides the intuition that the equivalence is used to simplify the problem. This is not a weakness.

- **"Novelty may be overstated"** (Harsh Critic): The paper explicitly discusses Lee & Bareinboim (2018; 2020) and distinguishes its single-node conditional-intervention setting from multi-node hard interventions. The novelty claim is appropriately scoped.

- **"Formatting nitpick about \tilde{d}o notation"** (Harsh Critic): This is a parser artifact, not a paper flaw.

- **"The bandit experiment context enumeration is computationally infeasible for large ancestor sets"** (Harsh Critic): The paper explicitly states that datasets were selected because "both An(Y) and mGISS_Y(G) are sufficiently small to allow experimentation with our setup," directly addressing this concern.

- **Missing related works** (not included — I cannot confirm their existence without external sources).

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Expand the bandit experiment specification** in Section 6 to include: (a) how the bnlearn CPTs are used as SCM structural assignments, (b) a brief description of the per-context UCB update procedure with example context counts, (c) the reward scale and how the best arm is determined for regret computation, and (d) confidence intervals or standard errors on the regret curves (the figure shows standard deviations, which is good, but the method should be described in text). If the authors prefer to keep the paper compact, they could move this detail to the appendix and reference it clearly.

2. **Add a proof sketch** for Proposition 4 in the main text (1–2 paragraphs in Section 3 after the proposition statement). This would help the average reader understand why the equivalence holds without reading the full appendix.

3. **Reconsider the estimated-best-arm computation** for regret. If it is computed from the same algorithm's end-of-training results, this creates a potential feedback loop. An alternative is to run an oracle that exhaustively evaluates all candidate arms in the known SCM to find the true best arm, then compute regret against that.

## Score and Decision

### Calibration Report

**Round 1 (Bracketing):** Three queries on related topics across score bands.

*Low band (< 3.5):* Papers on causal discovery / structure learning (scores 3.0–3.25). Examples: "Sparse Causal Model" (3.0, Reject), "D^3PM: Diffusion for Causal Discovery" (3.25, Reject). These are substantially weaker — they lack the theoretical rigor and clear empirical validation of the current paper.

*Middle band (3.5–7.5):* Relevant causal bandit / causal intervention papers (scores 5.0–6.5). Key anchors: "Learning Good Interventions in Causal Contextual Bandits with Adaptive Context" (5.0, Reject — limited experiments, restrictive binary interventions), "Adversarial Causal Bayesian Optimization" (6.0, Accept — solid theory and experiments but framing concerns), "Causal Bayesian Optimization with Unknown Causal Graphs" (6.5, Reject — mixed scores, strong contribution but divisive).

*High band (> 7.5):* Papers scoring 8.0 (Accept) on causal discovery/intervention topics. These are highly polished papers with both strong theory and extensive experiments. The current paper's experimental section (particularly the bandit component) is not at this level.

**Round 1 Bracket:** 5.0–7.0.

**Round 2 (Narrowing within bracket):** Two queries targeting (4.5, 6.5) and (6.0, 7.5).

Anchors read in full:
- "Deriving Causal Order from Single-Variable Interventions" (7.0, Accept, scores 5/8/8/6/8): Strong theory and experiments but some reviewers questioned limited comparisons and restrictive assumptions. The current paper has cleaner theory but less thorough experiments — the theory carries more weight per page.
- "Robust Root Cause Diagnosis using In-Distribution Interventions" (6.5, Accept, scores 6/6/6/8): Strong experiments but the methodological contribution was questioned as incremental. The current paper has a more substantive theoretical contribution.
- "Learning Good Interventions in Causal Contextual Bandits" (5.0, Reject, scores 5/5/5/5): Restrictive assumptions (binary interventions), limited experiments, unclear novelty. The current paper is clearly stronger across all dimensions.

**Final Score Determination:** The paper is stronger than the 5.0 anchor (rejected with weak experiments and restrictive assumptions). It is comparable to the 6.0 anchor (ACBO, accepted) — both have novel theoretical contributions and solid experimental validation, with some polish issues in experiments. It is below the 7.0 anchor (DERIVE, accepted) in experimental thoroughness. The search-space reduction experiments are strong, but the bandit experiments need more detail. **Score: 6.0.**

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>