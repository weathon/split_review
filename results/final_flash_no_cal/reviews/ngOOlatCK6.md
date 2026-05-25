Now I have a thorough understanding of the paper. Let me synthesize the final review.

## Summary

This paper studies single-node conditional-intervention causal bandits, where the arms are conditional interventions (policies that set a node's value based on observed context). The main contributions are: (1) an equivalence result (Proposition 4) showing that conditional-intervention superiority reduces to deterministic atomic-intervention superiority; (2) a graphical characterization—the LSCA closure of the parents of the reward variable—as the minimal set of nodes guaranteed to contain the optimal intervention (Theorem 13); (3) the C4 algorithm that computes this set in linear time (Theorem 16); and (4) experiments demonstrating substantial search-space pruning on real-world graphs and improved bandit regret when the mGISS is used.

## Strengths

- **Equivalence of superiority relations (Proposition 4)** — Proves that conditional-intervention superiority (a probabilistic, policy-based notion) is equivalent to deterministic atomic-intervention superiority. This is theoretically deep and enables the entire graphical analysis to be carried out in the simpler deterministic setting. The proof is sound and the result is non-trivial.

- **Graphical characterization of the mGISS (Theorem 13)** — The LSCA closure of Pa(Y) is proven to be the minimal set of nodes guaranteed to contain the optimal conditional intervention. The Λ-structure reformulation (Theorem 12) makes the criterion intuitive and easy to visualize (Figures 1–2). This is a clean, interpretable result that directly advances the theory of causal bandits beyond the hard-intervention case.

- **Linear-time C4 algorithm (Theorem 16)** — The connector-based algorithm runs in O(|V|+|E|), which is optimal and immediately usable as a preprocessing step. The connector concept is clever, and the reverse-topological-order procedure is clean. This ensures the theoretical characterization is practical for large graphs.

- **Substantial pruning in real-world graphs (Section 6)** — Experiments on bnlearn models show the mGISS can retain fewer than 10 % of ancestor nodes for some large graphs (e.g., over 90 % reduction). This directly validates that the method produces meaningful reductions in realistic settings. The results on random graphs with varying edge densities further characterize when the method is most effective.

- **Clear distinction from prior work (Section 7)** — The paper thoroughly explains how single-node conditional interventions differ from multi-node hard interventions (Lee & Bareinboim, 2018), from contextual bandits, and from soft interventions. The paper correctly identifies that the single-node case is *more challenging* than the multi-node case for search space reduction, making the contribution appropriately framed.

- **Λ-structure interpretation (Theorem 12)** — The equivalence of the LSCA closure to the set of nodes forming Λ-structures over Pa(Y) provides an elegant alternative characterization that aids intuition and is instrumental in proofs.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
- **The bandit regret experiment does not fully disentangle composition from cardinality reduction.** The experiment in Figure 3 compares CondIntUCB using the full ancestor set vs. using the mGISS. The mGISS always has fewer nodes, so the observed regret reduction is consistent with *any* pruning that reduces the arm count. The paper's core claim—that the mGISS is *the minimal set guaranteed to contain the optimal node*—is a theoretical guarantee, and the experiment is meant to demonstrate practical benefit. However, the claim in the abstract that pruning with C4 "substantially accelerates convergence rates" would be more strongly supported by an ablation that compares mGISS against another pruning strategy of the same cardinality (e.g., a random subset of nodes of equal size). Such a control would show that it is the *specific compositional structure* of the mGISS—not merely the cardinality reduction—that drives the improvement. Without it, the experiment conflates the trivial benefit of having fewer arms with the specific structural value of the mGISS. The paper's conclusions remain valid, but the empirical strength of the claim is weaker than it could be.

- **CondIntUCB is a simple baseline with acknowledged scalability limits.** The paper uses a UCB-per-context approach (one bandit per realization of Z_X), which scales poorly in the size of the context space (essentially the Cartesian product of ancestor ranges). The authors acknowledge this explicitly and select small graphs to make experiments feasible. However, this means the bandit experiment is more a proof-of-concept than a demonstration of practical superiority. The paper would benefit from a more explicit discussion of the complexity of CondIntUCB (exponential in |Z_X| in the worst case) and a clearer statement that C4's benefit will be fully realized only when paired with a future, more efficient conditional-bandit algorithm. The regret-bound suggestion from the reviewer (e.g., making the dependence of regret on |mGISS| vs. |An(Y)| explicit) would strengthen the paper but is not necessary for its core contribution.

### Trivial
None.

## Nice-to-Haves

- **Regret bound for CondIntUCB.** Adding a regret bound that explicitly depends on the size of the node set (e.g., O(|mGISS|·|Z_X|·√T) vs. O(|An(Y)|·|Z_X|·√T)) would turn the empirical observation into a theoretical guarantee and further bridge theory to practice.
- **Discussion of cases where Z_X is smaller than the full ancestor set.** The paper assumes An(X)\{X} ⊆ Z_X. A paragraph discussing when this assumption may be violated in practice (e.g., unobserved ancestors, measurement costs) and how it affects the results would improve completeness.

## Removed Points

The following points from the inputs were removed or downgraded for the reasons indicated:

- **"The Z_X assumption is very strong"** — The paper explicitly addresses this in footnote 3: "We are not claiming that all variables in An(X)\{X} need to be in Z_X for the best decision to be made, or for our results to hold, but that we can always include them in Z_X under the assumptions of our problem." This is a clearly stated and justified scope condition, not an oversight.
- **"Scope is narrower than the title suggests"** — The paper clearly defines its assumptions (single-node, no confounding) and explicitly notes these are necessary first steps. The title accurately reflects the content.
- **"Formal problem definition is a strength"** (from Strength Finder) — Generic; this is a prerequisite for any paper introducing a new problem, not a distinguishing strength.
- **Criticism about "CondIntUCB is a weak proxy" framed as a major issue** — The paper acknowledges the simplicity of CondIntUCB and explicitly states it expects "any future algorithm" to benefit from C4. Downgraded to Minor because the claim is appropriately scoped and the limitation is disclosed.

## Novel Insights

Beyond the paper's own contributions, the reviews surface a subtle point about experimental design in search-space reduction research: when the primary claim is about a *guaranteed minimal set* (a structural property), showing that using this set empirically beats the full set is necessary but not sufficient to demonstrate that the *specific composition* of the set is what matters. An ablation controlling for cardinality would sharpen the empirical narrative. However, this is a general observation about experimental methodology in this sub-area, not a flaw specific to this paper—the paper's theoretical guarantee already establishes why the composition is correct.

## Suggestions

- Add an ablation comparing mGISS-pruned CondIntUCB against CondIntUCB with a random subset of nodes of equal cardinality (drawn from the ancestor set). If the mGISS version yields lower regret, the claim that compositional structure matters is supported; if performance is similar, temper the language about "substantially accelerating convergence" to reflect that the primary benefit is cardinality reduction backed by a theoretical safety guarantee.
- Include a brief paragraph in Section 6 acknowledging the exponential worst-case complexity of CondIntUCB in the size of Z_X, and explicitly state that C4 is designed as a preprocessing step for any future conditional-bandit algorithm, not as a component tied to CondIntUCB specifically.
- (Optional) Derive a simple regret bound for CondIntUCB that shows the dependence on |mGISS| vs. |An(Y)|.

## Score and Decision

MY FINAL SCORE: <score>8.0</score>
MY FINAL DECISION: <decision>Accept</decision>