Now I have a solid calibration picture. Let me synthesize the final review.

**Round 1 bracket:** The paper sits between 6.5 and 8.0 based on the round-1 anchors.

**Round 2 narrowing:** Comparing against round-2 anchors:
- **MVpvyeVeyI (6.50, Reject)**: Our paper is stronger — cleaner theory, more thorough experiments, no fundamental novelty concerns.
- **SKulT2VX9p (6.67, Accept)**: Our paper is stronger — the theory is more self-contained and the experiments more systematic.
- **u63OVngeSp (7.00, Accept)**: Comparable profile. Both have clean theory + algorithm + empirical validation with minor weaknesses. Our paper arguably has a more complete characterization (exact rather than approximate algorithm) and more extensive experiments.
- **M0xK8nPGvt (7.50, Accept)**: This paper had a novel hierarchical Bayesian procedure with regret analysis; our paper's contribution is comparably solid but the bandit regret experiment lacks theoretical analysis.
- **xByvdb3DCm (8.00, Accept)**: Clearly above — addresses a more novel/complex problem with broader implications.

**Final score: 7.0**. The paper is a strong accept with clean, non-trivial theoretical contributions and solid empirical validation. Minor weaknesses exist but do not threaten the core contribution.

---

## Summary
This paper addresses the problem of identifying the minimal set of nodes that must be examined to find the optimal single-node conditional intervention in a causal bandit, given a known causal DAG. The authors prove that conditional-intervention superiority is equivalent to deterministic atomic-intervention superiority (Proposition 4), characterize the minimal globally interventionally superior set (mGISS) as the LSCA closure of the parents of the target variable Y (Theorem 13), and provide the C4 algorithm that computes this set in linear time O(|V|+|E|). Empirical results on random and real-world graphs demonstrate substantial search-space pruning (often >90%), and bandit regret experiments confirm that restricting action space to the mGISS accelerates convergence.

## Strengths
- **Elegant reduction (Proposition 4):** The equivalence between conditional-intervention superiority and deterministic atomic-intervention superiority is non-obvious and substantially simplifies the theoretical analysis, allowing reasoning about hard interventions in deterministic SCMs without loss of generality.
- **Complete graphical characterization (Theorems 12 and 13):** The characterization of the mGISS as the Λ-structure closure of Pa(Y) — equivalently, the LSCA closure — is a clean, recursive, purely graph-theoretic result. Theorem 12 (Λ-structures characterize the LSCA closure) and Theorem 13 (LSCA closure of Pa(Y) equals the unique mGISS) together form the paper's central contribution and appear correct.
- **Practical algorithm (C4, Theorem 16):** The C4 algorithm computes the mGISS in a single reverse-topological pass with O(|V|+|E|) time. The connector-based computation (Definition 14, Lemma 15) is clever, and the correctness proof ties cleanly to the Λ-structure characterization.
- **Thorough empirical validation:** The random-graph pruning experiment systematically explores graph size (20–500 nodes) × expected degree (2–11), and the real-world bnlearn evaluation covers most graphs in the repository, showing >90% pruning on large sparse graphs (Figures 5–6). The bandit regret experiment (CondIntUCB, Figure 3) on four benchmark Bayesian networks (asia, sachs, child, pathfinder) demonstrates that mGISS pruning translates to visibly lower cumulative regret.
- **Clear exposition:** Figure 1 provides effective pedagogical motivation for the LSCA heuristic, and the stepwise definitions (Λ-structures, LSCA closure, connectors) build intuition before the formal results.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
- **Bandit experiment compares only against all-ancestors baseline (not intermediate heuristics):** The regret experiment (Section 6, Figure 3) contrasts mGISS against the full ancestor set but does not compare against natural superset heuristics (e.g., parents of Y only, or parents ∪ grandparents). Showing that mGISS outperforms coarser prunings would more directly demonstrate that *minimality* matters in practice, beyond the obvious benefit of a smaller action space. The core claim about search-space reduction is adequately supported by the pruning experiments, so this is an evidential gap rather than a flaw.
- **Target Y selection may bias pruning ratios:** In both the random-graph and real-world experiments, Y is consistently chosen as the node with the most ancestors (among those with >1 parent). While this choice is reasonable (it ensures non-trivial mGISS cases), it may inflate reported pruning ratios relative to what a random practitioner would encounter. The paper acknowledges the selection criteria but could strengthen conclusions with sensitivity analysis over different Y choices.

### Trivial
- The claim that mGISS pruning "substantially accelerates convergence rates" (abstract) could be slightly tempered. The observed acceleration follows naturally from a smaller action set; the more fundamental message is that the mGISS is provably sufficient while being dramatically smaller.

## Nice-to-Haves
- Provide a concrete SCM counterexample where a node outside the mGISS is provably suboptimal, to vividly demonstrate set minimality.
- Discuss the practical feasibility of the full pipeline when the conditioning set Z_X = An(X)\{X} leads to exponentially many contexts in large graphs.
- Extend the bandit regret experiment with a superset baseline (e.g., Pa(Y) or a superset of the mGISS) to isolate the benefit of minimality.

## Removed Points
These points are flagged to be removed, treat them with caution:

- *"The paper would benefit from a short informal walk-through of why a node outside the Λ-closure is indeed inferior"* — The paper already provides this through Figure 1 and the surrounding intuition in Section 4. Not a real weakness.
- *"The paper does not analyze the bandit regret theoretically"* — Out of scope. The paper's contribution is the graphical characterization and algorithm, not bandit regret analysis. Requiring a regret bound is scope creep.
- *"The assumption that all ancestors of X are observed and available for conditioning is stated but not discussed with respect to feasibility in large graphs"* — The paper already acknowledges this limitation explicitly in the conclusion (Section 7) and the assumption is clearly stated in Section 2 with motivation. The concern about exponential context space is inherent to the problem setting, not a paper flaw.
- *"Repeating the experiment with randomly chosen Y would make the conclusions more robust"* — This is partially valid and merged into the minor weakness about Y selection, but the full robustness study is a nice-to-have, not a requirement.

## Novel Insights
The paper's most striking insight is that the minimal set of nodes worth testing for single-node conditional interventions is exactly the Λ-structure closure of Pa(Y) — a purely graph-theoretic characterization that holds for *all* SCMs over the given DAG, not just a subclass. The equivalence in Proposition 4 (conditional ↔ deterministic atomic superiority) is a clever reduction that may be independently useful for future work on conditional intervention problems. The connector-based C4 algorithm is also a nice algorithmic contribution: it shows that a concept (Λ-structures) defined in terms of pairwise path-intersection properties can be computed in a single reverse-topological sweep, making the result genuinely practical.

## Suggestions
- In the rebuttal, address the minor point about comparing mGISS against superset heuristics in the bandit experiment. Even a brief discussion of why the observed regret improvement cannot be matched by simpler pruning rules would strengthen the paper.
- Consider adding a remark on the relationship between sparsity (low average degree) and mGISS size — the empirical results already show this pattern, and formalizing it with even a simple bound would elevate the contribution.

## Score and Decision

**Anchor comparison:**
| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| IPayPEGwdE (causal contextual bandits, adaptive context) | 5.00 | R1 | Our paper is clearly stronger — cleaner theory, more thorough experiments |
| MVpvyeVeyI (CBO with unknown graphs) | 6.50 | R1/R2 | Our paper is stronger — self-contained theory, no fundamental concerns |
| SKulT2VX9p (interventional fairness, partial graphs) | 6.67 | R2 | Our paper is stronger — more complete theoretical characterization |
| u63OVngeSp (causal order from interventions) | 7.00 | R1/R2 | Comparable — both have clean theory + algorithm + validation with minor weaknesses |
| M0xK8nPGvt (causal graph priors for RL) | 7.50 | R2 | Slightly above our paper — has regret analysis in addition to novel method |
| xByvdb3DCm (selection meets intervention) | 8.00 | R1/R2 | Above our paper — addresses a broader, more novel problem with deeper implications |

**Round 1 bracket:** 6.5–8.0
**Round 2 narrowing:** The paper sits closest to u63OVngeSp (7.00) — a strong accept with clean theory, practical algorithm, and solid empirical support. It is slightly below M0xK8nPGvt (7.50) which offered theoretical regret analysis alongside its novel method.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>