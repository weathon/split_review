Now I have all the information I need. Let me synthesize the final review.

## Summary

The paper introduces the conditional causal bandit problem, where arms are single-node conditional interventions on a known causal graph. It provides a graphical characterization of the minimal set of nodes (mGISS) guaranteed to contain the optimal intervention node, proving that it equals the LSCA closure of the reward variable's parents (Theorem 13). The paper further presents the C4 algorithm that computes this set in linear time O(|V|+|E|), and provides experiments showing substantial search-space reduction on random and real-world graphs.

## Strengths

- **Elegant graphical characterization (Theorem 13, Theorem 12).** The paper proves that the mGISS equals the LSCA closure of Pa(Y), and provides an alternative characterization via Λ-structures (Theorem 12) that is both clean and intuitive. This gives a directly checkable graphical condition for which nodes to consider, which is the paper's core theoretical contribution.

- **Linear-time C4 algorithm (Algorithm 1, Theorem 16).** The connector-propagation scheme is clever: by tracking whether a node's children connect to multiple distinct LSCA-closure nodes, the algorithm determines membership in O(|V|+|E|) time. The connector lemma (Lemma 15) provides a nice intuition for why the algorithm works.

- **Clear and appropriate scoping.** The paper carefully delineates its setting (single-node conditional interventions, no latent confounders) from prior work on multi-node hard interventions (Lee & Bareinboim, 2018), and is explicit about the limitation that latent confounders are left to future work.

- **Demonstrated search-space reduction.** The random-graph experiments (Figure 5, Appendix H) and real-world bnlearn experiments (Figure 6) convincingly show that the mGISS can be substantially smaller than the ancestor set — retaining as little as 17% of ancestor nodes for sparse 500-node graphs. This evidence directly supports the practical utility claim.

- **Rigorous theoretical scaffolding.** The paper proves uniqueness of the mGISS (Proposition 6), provides supporting lemmas (Lemma 15 on connectors), and the Λ-structure characterization which simplifies proofs.

## Weaknesses

### Major

- **Central equivalence (Proposition 4) lacks intuition or proof sketch.** The paper claims that conditional-intervention superiority (Definition 1) is equivalent to deterministic atomic-intervention superiority (Definition 2), and uses this to ground the entire graphical characterization. The two definitions look quite different — Definition 1 quantifies over all SCMs, all conditioning sets, and all policies, while Definition 2 is a per-unit condition with no policies. The paper states the equivalence (line 124) and says "All proofs of the results presented in the paper can be found in the appendix" (line 63), but provides **no intuition whatsoever** for why this non-trivial equivalence holds. A reader cannot begin to assess whether the proof avoids hidden assumptions (e.g., about the richness of the SCM class, closure under composition of policies). Since Theorem 13's applicability to conditional interventions depends on this result, the paper would benefit substantially from even a brief proof sketch or intuitive argument.

- **Regret experiments are underspecified, weakening empirical support.** The description of the regret-study setup omits critical details:
  - The paper uses bnlearn graphs but does not specify what SCM (structural equations, noise distributions, reward generation mechanism) is used to produce reward samples. Without this, it is unclear what bandit problem is actually being solved.
  - The regret computation uses "the estimated best arm, defined as the arm that most runs concluded to be the best at the end of training" (footnote 11). This definition is circular — the "best arm" is derived from the algorithm's own behavior, which introduces bias and conflates the evaluation of the pruning method with the algorithm's convergence properties.
  - The only baseline is brute-force over all nodes. Without comparisons against other natural subsets (e.g., parents only, random subsets of matching size), it is unclear whether the regret improvement is due to the specific mGISS set or merely to having fewer arms.

### Minor

- **No discussion of whether the superiority relation could be empty.** Definition 1 requires a single policy g to work for *all* observable conditioning sets Z_X and *all* policies h for W, *for every* SCM compatible with the graph. This is a very strong condition. If for some graph this relation is empty (no node is superior to any other), the mGISS would include all nodes, rendering the characterization vacuous for that graph. The paper does not discuss this possibility or characterize when the relation is non-trivial.

- **Only one baseline in regret experiments.** The regret study compares mGISS-pruned search vs. brute-force over all nodes. Adding comparisons against Pa(Y), Pa(Y) ∪ LSCA(Pa(Y)) \ Pa(Y), and random subsets of size |mGISS| would strengthen the claim that the improvement is due to the *specific* mGISS set rather than arm-count reduction alone.

### Trivial

- **An(U) precomputation not noted.** The C4 algorithm uses `Ch(V) ∩ An(U)` on line 6, but does not explicitly mention that a separate reachability pass is needed to compute `An(U)`. This is a minor expositional point — the linear-time claim still holds since ancestor computation is O(|V|+|E|).

## Nice-to-Haves

- A concrete example (small graph, known SCM) where the optimal intervention node is not in Pa(Y) but is in the LSCA closure would make the practical necessity of the LSCA closure more tangible.
- A discussion of how unobserved confounders might break the LSCA closure characterization would strengthen the paper, even if a full solution is left to future work.
- Regret curves with per-node selection counts over time would help illustrate *how* the mGISS guides the algorithm (e.g., by focusing exploration on fewer nodes vs. finding better nodes).

## Removed Points

- **Claim that "single-node interventions are more challenging" is unargued.** The paper does argue this on line 102: with multi-node interventions one "simply needs to intervene on all the parents Pa(Y)," which is not possible with single-node interventions when |Pa(Y)| > 1. The critic's claim that it's "merely stated" is incorrect. **Removed** as factually wrong.

- **Claim that CondIntUCB is underspecified.** The paper describes choice (i) as "UCB over nodes" and choice (ii) as "a UCB instance specific to the conditioning set value," and explicitly references Lattimore & Szepesvári (2020, §18.1) for contextual bandits with one bandit per context. This is a standard setup and adequate for a paper whose main contribution is the graph pruning, not the bandit algorithm. **Removed** as overly demanding about details outside the paper's main scope.

- **Criticism that Section 4 doesn't connect LSCA closure to superiority convincingly without appendix.** The paper states all proofs are in the appendix. The parser strips the appendix. The paper's main text provides the definitions, theorem statements, and algorithm description needed to understand the results. **Removed** per rule about missing appendix content.

- **Criticism about reproducibility statement being insufficient.** The paper provides code and states "All experiments and results described in Section 6 can be reproduced using the code in the repository." **Removed** per rule about not nitpicking reproducibility.

- **Criticism that the paper does not admit limitations in the Related Work section.** The paper repeatedly acknowledges the no-latent-confounders assumption as a limitation (lines 67, 102, and explicitly in future work on line 384). **Removed** as factually wrong.

- **Strength Finder items that are generic or conflict with weaknesses.** Several Strength Finder entries (e.g., "Uniqueness of the minimal GISS (Proposition 6)" as a standalone strength, "Connector-based characterization of LSCA closure (Lemma 15)") are kept but merged into the broader strengths above; the "Empirical evidence of search-space reduction" is kept as it is specific and grounded. The Strength Finder's framing of Proposition 4 as a core strength is retained but note the weakness about lack of intuition.

## Novel Insights

The harsh review's observation that the equivalence (Proposition 4) is far from obvious and insufficiently motivated is the most penetrating insight. However, no genuinely novel observation emerges beyond what the paper and the surface-level reading of its claims provide — the reviews largely consist of standard evaluation criteria applied to the stated contributions.

## Suggestions

1. **Add a proof sketch or intuition for Proposition 4 in the main text.** Even a brief paragraph explaining, e.g., why considering all units n separately suffices to handle all SCMs and all policies, or why the conditioning sets Z_X can be absorbed into the policy, would allow readers to assess the central theoretical claim without diving into the appendix.

2. **Fully specify the regret experiment setup.** State the structural equations, noise distributions, and reward generation mechanism used. Clarify how the "best arm" is determined (ideally using ground-truth knowledge of the SCM, not the algorithm's own estimates).

3. **Add baselines to the regret study.** At minimum, compare against Pa(Y) and a random subset of size |mGISS| to isolate whether the improvement is from the specific set composition or just arm-count reduction.

4. **Discuss when the superiority relation may be non-trivial.** Address whether there exist graphs for which the relation is empty (making mGISS equal to all nodes), and characterize when the pruning is guaranteed to be non-trivial.

## Score and Decision

The paper makes a genuine theoretical contribution: an elegant graphical characterization of the minimal search space for single-node conditional causal bandits, together with a linear-time algorithm. The theoretical scaffolding is well-structured and the search-space reduction experiments are convincing. However, the paper's main empirical demonstration (regret improvement) is weakened by underspecified experimental design, and the central theoretical bridge (Proposition 4) is presented without intuition, making it difficult to evaluate the link between the conditional-intervention problem and the deterministic atomic case used in the characterization. These are fixable issues but diminish the current form's completeness.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>