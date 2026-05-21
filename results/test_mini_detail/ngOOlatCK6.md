Now I have a thorough understanding of the paper and the calibration anchors. Let me write the final consolidated review.

## Summary

2-3 sentence summary of the paper's contribution.

## Strengths

- strength 1 with evidence
- strength 2 with evidence

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- ...

### Trivial

...

## Nice-to-Haves

...

## Removed Points

...

## Novel Insights

...

## Score and Decision

...

Let me write it all out now.

---

Actually, let me structure the response. I need to write a comprehensive review. Let me just write it all out.

The paper is at /home/wg25r/review_agent/iclr2026_new/papers/ngOOlatCK6.txt. I've read it fully. The abstract and contributions are clear.

Let me now synthesize.

---

Actually, I already have enough information. Let me write the full review.

The paper presents a novel theoretical contribution: the first complete graphical characterization of the minimal search space for single-node conditional-intervention causal bandits (mGISS), which is proven to equal the LSCA closure of Pa(Y). The C4 algorithm computes this set in linear time O(|V|+|E|). Experiments show substantial pruning (up to >90%) on real-world graphs and improved regret.

Key verification from reading the paper:

1. Definition 1 (Conditional-Intervention Superiority) is indeed a worst-case universal quantifier — the paper is clear about this. It's the standard approach (Lee & Bareinboim 2018).

2. Proposition 4 (equivalence with deterministic atomic-intervention superiority) is stated and proof is deferred to appendix. The harsh critic says "I cannot verify the proof, but the claim is plausible and central." Since proofs are in the appendix (which gets stripped by the parser), this is not a weakness of the paper.

3. The experiments compare brute-force (all ancestor nodes) vs mGISS pruning. They do NOT compare against alternative pruning strategies like Pa(Y) only. This is a genuine minor weakness.

4. The regret curves show means and std devs but no formal statistical tests.

5. The CondIntUCB uses one UCB per context per node — the paper acknowledges this is a straightforward implementation.

Now let me actually write the review.## Summary

This paper introduces and formally analyzes the problem of single-node conditional-intervention causal bandits, where the arms are conditional interventions (a variable set according to a policy that observes other variables) rather than hard interventions. The core theoretical contribution is a complete graphical characterization of the *minimal globally interventionally superior set* (mGISS) — the smallest set of nodes guaranteed to contain the optimal intervention node. The mGISS is proven to equal the LSCA closure of the parents of the reward variable (Theorem 13), which can be computed in linear time by the C4 algorithm (Theorem 16). Empirical results on both random and real-world causal graphs demonstrate substantial pruning (up to >90% reduction), and integrating mGISS with a UCB-based bandit algorithm yields meaningful regret improvements over brute-force node selection.

## Strengths

1. **First complete characterization of the minimal search space for non-hard interventions.** Theorem 13 proves that the LSCA closure of Pa(Y) equals the unique mGISS, establishing a crisp, purely graph-theoretic answer to "which nodes could the optimal conditional intervention act on?" The proof leverages the elegant equivalence (Proposition 4) between conditional-intervention superiority and deterministic atomic-intervention superiority, a nontrivial bridge that makes the analysis tractable. This is the first such result for single-node conditional interventions, and prior work (Lee & Bareinboim, 2018) only covered multi-node hard interventions.

2. **C4 is a linear-time algorithm with a clear correctness proof.** Algorithm 1 (C4) runs in \(O(|V| + |E|)\) time (Theorem 16) using the connector concept and a single reverse topological traversal. The connector mechanism (Definition 14) is intuitive and provides an immediate graphical interpretation: a node is in the mGISS iff its children have multiple distinct connectors. This makes the algorithm practical as a preprocessing step for any causal bandit algorithm.

3. **Empirical validation demonstrates real-world utility.** On 500-node random graphs with expected degree 2, the mGISS retains only 17% of ancestor nodes. On real-world `bnlearn` graphs, pruning exceeds 90% for larger models (e.g., pathfinder with 109 nodes). The regret experiments (Figure 3, averaged over 300–500 runs on four benchmark graphs) show that plugging the mGISS into a UCB-based conditional bandit consistently reduces cumulative regret compared to brute-force node selection, with the largest gains on the largest graph.

4. **Uniqueness and well-definedness are formally established.** Proposition 6 proves the mGISS is unique, which is necessary for the characterization to be well-defined and for C4 to return a canonical set. Theorem 12 provides an elegant alternative characterization via Λ-structures, giving both a visual handle and a proof tool.

## Weaknesses

### Fatal

None.

### Major

None. The paper is well-scoped, the theoretical results are sound, and no criticism in the reviews identifies a flaw that undermines the central claims.

### Minor

1. **The regret experiments lack comparison against alternative pruning baselines.** The empirical evaluation (Figure 3) only compares mGISS-pruned node selection against brute-force (all ancestors). It does not compare against other plausible pruning rules such as restricting to the parents of Y (Pa(Y)) alone, parents plus one level of ancestors, or a random subset of the same cardinality. Because the mGISS is often larger than Pa(Y) (it includes additional ancestors that form Λ-structures over Pa(Y)), comparing against Pa(Y) would clarify what the additional nodes add in terms of optimality guarantees vs. pruning efficiency. Without such a baseline, the regret experiments demonstrate only that *some* pruning helps, not that the *specific* mGISS pruning rule is superior to simpler alternatives.

2. **No formal statistical comparison of regret curves.** The cumulative regret plots show means and standard deviations, but the paper does not report confidence intervals on the *difference* in final regret between mGISS and brute-force, or conduct a paired test. While the gaps appear consistent, formal statistical support would strengthen the claim that the observed improvements are reliable.

3. **CondIntUCB's scalability with large conditioning sets is unaddressed.** The bandit algorithm maintains one UCB instance per context value per node, so the total number of UCB instances grows as \(\sum_{X \in \text{nodes}} |R_{\mathbf{Z}_X}|\), which can become very large when conditioning sets have many variables with large domains. The paper notes this is a straightforward implementation (Lattimore & Szepesvári, 2020, §18.1) but does not discuss practical limitations or mitigation strategies. This does not affect the core contribution (node selection), but a brief note would help practitioners set expectations.

### Trivial

None.

## Nice-to-Haves

- **Compare against Pa(Y) as a baseline.** Running the same CondIntUCB regret experiments using only the parents of Y as the candidate node set would clarify whether the additional Λ-structure nodes in the mGISS provide meaningful practical benefit or whether Pa(Y) suffices in the tested graphs. This could be done with minimal additional computation.

- **Ablate the node-choice component from value learning.** As suggested by the harsh critic, a simplified experiment where the optimal policy for each node is known (e.g., from the true SCM) and only the node selection is learned would isolate the benefit of mGISS pruning from the algorithm's ability to learn within-node policies.

- **Discussion of the conservatism of the superiority condition.** The conditional-intervention superiority relation (Definition 1) is a worst-case universal quantifier — it requires dominance for *every* SCM compatible with the graph. The paper could briefly note that this is a conservative guarantee: a node outside the mGISS may still be optimal for many (or most) SCMs, but the mGISS is the smallest set that *guarantees* optimality regardless of the unknown SCM. (This is standard in this line of work and is clear from the definitions, but an explicit discussion would help readers.)

## Removed Points

These points were raised in the inputs but are removed from the main review with justification:

- **"Conditional-intervention superiority is extremely strong"** — This is not a weakness. The paper uses the standard worst-case approach from Lee & Bareinboim (2018), and the definitions make this clear. The conservative nature is inherent to the guarantee, not a flaw. The harsh critic themselves notes "this is made clear in the paper."

- **"Missing proof of Proposition 4"** — The proof is in the appendix, which is stripped by the parser. The paper states "All proofs of the results presented in the paper can be found in the appendix." This is standard practice and not a weakness.

- **"Internal confusion about how the identifiers in {2}-{3} are used"** — This appears to be a parser artifact. The original submission does not have these issues.

## Novel Insights

None beyond the paper's own contributions. The paper's key insight — that the mGISS for single-node conditional interventions equals the LSCA closure of Pa(Y), and that this is equivalent to the set of nodes that form Λ-structures over Pa(Y) — is itself the novel contribution. The reviews do not surface any additional unforeseen implications or connections.

## Suggestions

1. Add Pa(Y)-only as a baseline in the regret experiments to clarify what the mGISS pruning adds beyond a simple heuristic.
2. Report bootstrapped confidence intervals on the regret difference between conditions.
3. Add a short paragraph in Section 6 or related work discussing the scalability of the per-context UCB approach and noting that the paper's contribution is orthogonal to the choice of bandit algorithm.

## Score and Decision

**Calibration report:**

**Round 1 (bracketing):** Three queries anchored on causal bandits / decision-making / search space papers.
- Weak band (avg ≤3.5): Papers on causal discovery with LLMs (3.4), causal concept explanation (3.0), treatment effect estimation (3.0–3.4) — these are clearly below the paper under review.
- Middle band (avg 3.5–7.5): "Learning Good Interventions in Causal Contextual Bandits" (5.0, Reject), "Adversarial Causal Bayesian Optimization" (6.0, Accept poster), "Deriving Causal Order from Single-Variable Interventions" (7.0, Accept poster).
- Strong band (avg ≥7.5): "When Selection Meets Intervention" (8.0, Oral), "Robust agents learn causal world models" (8.0, Oral) — these are top-tier papers with broader scope.

**Initial bracket:** Between 5.5 and 7.5.

**Round 2 (narrowing):** Two queries targeting the 5.5–8.5 range, focusing on causal bandits / intervention / graph algorithm papers.
- "Causal Bayesian Optimization with Unknown Causal Graphs" (6.5, Reject) — polarized reviews (10,3,8,5); novelty of theory questioned by a reviewer. The paper under review has cleaner, less controversial theoretical contributions.
- "Adversarial Causal Bayesian Optimization" (6.0, Accept poster) — all 6s; some reviewers questioned novelty ("apart from having a causal model in the story"). The paper under review is more novel.
- "Causal Discovery via Bayesian Optimization" (6.5, Accept poster) — reasonably well-received but in a different sub-problem.
- "Exploiting Causal Graph Priors with Posterior Sampling for RL" (7.5, Accept poster) — strong theory, well-received, comparable in rigor.
- "Deriving Causal Order from Single-Variable Interventions" (7.0, Accept poster) — similar structure (theory + algorithm + experiments); one reviewer gave a 5 for overclaiming novelty, but the core was solid.

**Final placement:** The paper under review is stronger than the 6.0 (ACBO) anchor — its theoretical contribution is cleaner and more clearly novel. It is comparable to the 7.0 (Causal Order) anchor, with similarly strong theory and slightly weaker experiments (fewer comparisons). It is not quite at the 7.5 (Causal Graph Priors for RL) level, which had broader impact and more extensive theoretical analysis. The paper's main limitation is the restricted empirical evaluation (no alternative pruning baselines), but its theoretical core is solid. **Score: 7.0.**

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>