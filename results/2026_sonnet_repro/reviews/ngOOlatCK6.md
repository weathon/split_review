Now let me perform calibration searches to score this paper.My initial bracket is **6.0–7.5**. The paper under review is stronger than the rejected causal contextual bandits paper (5.0) due to its complete theoretical characterization, but may sit below the exceptional 8.0 papers. Let me narrow within this bracket.Now I have enough to write the final review. Let me compile all findings.

---

## Summary

This paper introduces the *conditional causal bandit* problem, where a learner must choose which single variable to intervene on using conditional interventions in a known causal graph (without knowledge of structural assignments) to maximize a reward variable $Y$. The central contributions are: (1) a rigorous graphical characterization showing that the minimal globally interventionally superior set (mGISS) equals the LSCA closure of Pa(Y) (Theorem 13), proven through the key equivalence between conditional-intervention superiority and deterministic atomic-intervention superiority (Proposition 4); (2) the C4 algorithm that computes this set in provably correct O(|V|+|E|) time via a novel connector mechanism (Theorem 16); and (3) empirical demonstrations on random and real-world graphs showing substantial search-space reductions and improved bandit regret.

---

## Strengths

- **Complete graphical characterization of the mGISS (Theorem 13)**: The result that mGISS_Y(G) = L^∞(Pa(Y)), the LSCA closure of Y's parents, is both necessary and sufficient. This is not just a sufficient condition but a full characterization, proved rigorously. The Λ-structure reformulation (Theorem 12) provides an elegant and operationally useful equivalent description.

- **Non-trivial theoretical simplification via Proposition 4**: The equivalence between conditional-intervention superiority (over all SCMs and probabilistic policies) and deterministic atomic-intervention superiority is genuinely surprising and serves as the conceptual backbone of all subsequent proofs. This reduces a complex stochastic optimization problem to a cleaner combinatorial one.

- **Provably correct, linear-time algorithm (C4, Theorem 16)**: The connector mechanism (Definition 14, Lemma 15) is a clean graph-theoretic device that enables both proof of correctness and linear-time execution. The algorithm is immediately deployable as a preprocessing step for any future causal bandit algorithm.

- **Empirically demonstrated utility**: Section 6 shows >90% search-space reduction on large bnlearn models, and Figure 3 demonstrates faster UCB convergence and lower regret across four real-world graphs (asia, sachs, child, pathfinder), with pathfinder showing dramatic improvement. The bnlearn experiments are grounded in standard Bayesian network benchmarks.

- **Uniqueness of the mGISS (Proposition 6)**: The paper establishes that the mGISS is well-defined (unique), a non-trivial result that makes the characterization operationally meaningful.

---

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Non-standard regret proxy in empirical evaluation**: Footnote 11 states "we use the estimated best arm, defined as the arm that most runs concluded to be the best at the end of training." This diverges from the standard definition of cumulative regret, which is computed against the *true* best arm. When the mGISS and brute-force conditions may converge to different consensus estimates of the best node, the two regret curves are being measured against potentially different baselines, making the comparison internally inconsistent. Since the SCMs come from bnlearn (with known conditional probability tables), the true optimal node reward can be approximated by Monte Carlo sampling directly from the model — this would remove the ambiguity. The theoretical contribution of Theorem 13 is not affected, but this weakens the evidential strength of Figure 3.

- **Target-node selection creates optimistic pruning statistics**: Both the random and real-world graph experiments set Y to the node with the *most ancestors* (Footnote 8). Since pruning effectiveness is monotone in the number of ancestors (more ancestors → more opportunities for Λ-structures not involving Pa(Y)), the reported search-space reduction figures are likely upper bounds on what a practitioner would observe for an arbitrary target node. Showing the distribution across all possible target nodes on a few representative graphs (as median/worst-case), rather than just the best case, would better calibrate reader expectations.

### Trivial

- **Union approach under unknown graph not analyzed**: The introduction states that when the true causal graph is unknown, one can apply C4 to each candidate graph and take the union. This claim is stated but not formally analyzed — specifically, how the union size scales with the number of candidate graphs, and whether the union remains guaranteed to contain the optimal node under model uncertainty. A brief formal statement (even proof-sketch) would strengthen this claim, though it lies outside the paper's main scope.

---

## Nice-to-Haves

- A worked end-to-end example tracing C4's execution on a non-trivial graph (beyond Figure 2b), showing how connectors propagate step-by-step, would aid readers' intuition and help verify algorithm understanding without requiring appendix access.
- The ancestor-inclusion assumption (An(X) \ {X} ⊆ Z_X) is well-motivated in Section 2 and footnote 3, but a brief separate paragraph noting it as a *distinct* practical restriction (beyond simply "no latent confounders") would help practitioners assess applicability in settings where some ancestor variables are unmeasured.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

1. **[Harsh Critic, Ancestor-Inclusion as "substantively stronger" limitation]**: The critic argues this assumption should be "flagged clearly as a distinct assumption, not subsumed under 'no latent confounders.'" However, the paper explicitly addresses this in Section 2 ("all ancestors of X are observed") and Footnote 3 ("we are not claiming that all variables in An(X)\{X} need to be in Z_X for the best decision to be made… but that we can always include them"). The paper's treatment is reasonable. Moved to Nice-to-Have level only.

2. **[Harsh Critic, Erdős-Rényi produces trees at low density]**: The critic notes that at low edge density, mGISS reduction is "mathematically guaranteed to be large," implying the random graph experiments are cherry-picked. However, the paper's *stated use case* is exactly this scenario — realistic models have low average degrees (all bnlearn models have average degree < 4.0), and the paper explicitly makes this argument. Experiments in this regime validate the paper's own practical claim, not an artificially favorable one.

3. **[Harsh Critic, selection of 4 bnlearn datasets is narrow]**: The critic notes that the 4 datasets are selected for having "non-trivial graphical structures" and "sufficiently small" ancestor sets. Footnote 12 provides explicit justification (e.g., the `cancer` dataset is trivial). This is a reasonable computational constraint, not a methodological flaw.

---

## Novel Insights

The central insight — that the problem of choosing the best node for a conditional (probabilistic, policy-based) intervention reduces to the problem of choosing the best node for a deterministic atomic intervention (Proposition 4) — is genuinely surprising. It allows the authors to sidestep the complexity of reasoning over all possible stochastic policies and conditioning sets, collapsing a seemingly intractable problem into a clean graph-theoretic one. The resulting mGISS characterization as a Λ-structure closure (reachability by two disjoint paths to distinct ancestors of Y) is both elegant and practically useful, and the connector concept provides a new graphical object that may find applications in related problems in causal inference.

---

## Suggestions

1. Fix regret computation to use the true optimal node (estimated via Monte Carlo from the bnlearn CPTs), making Figure 3 unambiguous and definitive rather than consensus-based.
2. Add a supplementary figure showing mGISS size distribution across *all* possible target nodes (not just the max-ancestor node) for 1–2 representative real-world graphs, to give a more honest picture of expected pruning in practice.
3. Add at least a brief formal statement (or appendix result) about the union-of-mGISS approach under unknown causal graphs, even if only in terms of guaranteed containment of the optimal node.

---

## Score and Decision

**Calibration anchors:**

| Path | Avg Human Score | Round | Comparison to paper |
|---|---|---|---|
| IPayPEGwdE.md (Causal Contextual Bandits with Adaptive Context) | 5.0 | R1 | Rejected; less complete theory, more experimental weaknesses — paper under review is clearly stronger |
| YcW8i9VCf5.md (Adversarial CBO) | 6.0 | R1/R2 | Accepted; similar type but has significant problem-framing issues and weaker theoretical completeness — paper under review is cleaner and more complete |
| ZXs3pkmrRG.md (Test-Time Learning of Causal Structure) | 5.5 | R1 | Rejected; different problem but comparable scope — paper under review stronger |
| 2pEqXce0um.md (Root Cause Analysis) | 4.5 | R1 | Rejected; weaker |
| mGmx41FTTy.md (Two Time-Slices DAG learning) | 6.33 | R2 | Borderline reject/accept; comparable level of contribution — paper under review is more complete |
| BZYIEw4mcY.md (Causal Discovery with Latent Variables) | 6.0 | R2 | Accepted; comparable scope, paper under review is similarly strong |
| u63OVngeSp.md (Deriving Causal Order from Single-Variable Interventions) | 7.0 | R2 | Accepted; similar structure (theory+algorithm for single-variable causal interventions), but algorithm there has *no* theoretical guarantee of optimality while C4 is proven correct — paper under review is comparably strong |
| FhQSGhBlqv.md (Versatile Causal Discovery Framework) | 7.5 | R2 | Accepted; handles harder problem (latent confounders) with polynomial-time algorithm — modestly stronger |
| xByvdb3DCm.md (Selection meets Intervention) | 8.0 | R1 | Accepted; stronger empirical scope, broader theoretical reach — significantly stronger |
| 3cuJwmPxXj.md (Identifying Representations for Intervention Extrapolation) | 8.0 | R1 | Accepted; broader theoretical reach — stronger |

**Round 1 bracket:** 5.5–8.0

**Round 2 narrowing:** After reading the 7.0 anchor (u63OVngeSp) in full, the paper under review is comparable — both offer theory + proven algorithm for single-variable causal intervention questions, and C4 is arguably *more* complete (proven correct, linear time) than INTERSORT (which is a heuristic without optimality guarantees). The paper under review sits firmly near the 6.5–7.0 range. Key differentiators: the paper's scope is intentionally limited (single-node, no latent confounders) and its empirical section has a minor methodological issue (regret proxy), while its theoretical core is clean and complete.

**Final score: 6.5** — The paper is a well-executed theory+algorithm paper for a new and well-motivated variant of causal bandits. The theoretical contributions (Proposition 4, Theorem 13, Theorem 16) are genuine, non-trivial, and rigorously proved. The empirical section supports the main claims despite minor methodological imperfections. The scope is deliberately limited and transparently acknowledged. This places it above the 6.0 accepts (which have more significant framing or comparison issues) but below the 7.5+ papers that handle harder, more general problems.

**Axes summary:**
- *Originality*: High — first complete characterization of minimal search space for conditional causal bandits; novel Λ-structure + connector machinery.
- *Importance of research question*: Moderate-high — conditional interventions are practically motivated; single-node case is explicitly a necessary step toward the general setting.
- *Claims supported by evidence*: Yes — all theoretical claims proved; empirical claims supported despite minor proxy issue.
- *Soundness of experiments*: Mostly sound; the regret proxy issue and optimistic target-node selection are noted limitations.
- *Clarity of writing*: Good — problem, definitions, and results are cleanly organized.
- *Value to community*: Solid — provides a practically applicable preprocessing tool and theoretical foundation for future work on causal bandits with conditional interventions.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>