Now I have a solid comparative picture. Let me finalize my assessment.

**Bracket:** Round 1 placed the paper in **5.5–7.5**. Round 2 anchors:
- pOoKI3ouv1 (5.75): accepted, purely theoretical, no experiments — our paper is stronger (has experiments, more actionable result)
- YcW8i9VCf5 (6.00): accepted, solid theory + experiments — comparable, our theory is more complete
- u63OVngeSp (7.00): accepted, strong theory + competitive experiments — our experiments are noticeably weaker

**Narrowing:** The paper sits clearly above pOoKI3ouv1 (better than pure theory, experiments exist) and clearly below u63OVngeSp (experiments are supplementary, not competitive). It is comparable to YcW8i9VCf5 in overall quality — slightly better theory, slightly weaker experiments. Score: **6.0**.

Now let me write the final review.

---

## Summary
This paper introduces the conditional causal bandit problem, where arms are single-node conditional interventions of the form do(X = g(Z_X)) on a known causal DAG. The core contribution is a complete graphical characterization of the minimal node set (mGISS) guaranteed to contain the optimal intervention target — it equals the LSCA closure of Pa(Y) — along with the C4 algorithm that computes this set in O(|V|+|E|) time via a novel connector-propagation scheme. Empirical results on random and real-world graphs show substantial search-space pruning and improved bandit convergence.

## Strengths
- **Proposition 4 (equivalence of superiority relations):** The proof that conditional-intervention superiority in probabilistic SCMs coincides with deterministic atomic-intervention superiority is a nontrivial reduction that elegantly simplifies the subsequent analysis. This is a genuinely surprising result that serves as the theoretical engine of the paper (Section 3, lines 102–122).
- **Theorem 13 (graphical characterization of mGISS):** The central result — that mGISS_Y(G) = L^∞(Pa(Y)) — is complete, rigorous, and purely graph-based. Given only the causal DAG, one can deterministically identify the minimal search space with a formal guarantee that the optimal intervention node is retained (Section 4, line 215).
- **C4 algorithm (Algorithm 1):** The connector-based linear-time algorithm for computing the LSCA closure is elegant. Lemma 15 formally ties connectors to the closure, and Theorem 16 proves correctness and O(|V|+|E|) complexity. The algorithm is remarkably simple — a single reverse-topological pass with a lightweight case analysis (Section 5, lines 229–257).
- **Theorem 12 (Λ-structure characterization):** The characterization of the LSCA closure via Λ-structures (two internally disjoint directed paths from a node to two nodes in the base set) provides an intuitive, non-recursive alternative understanding of the closure and is instrumental in the proofs (Section 4, lines 199–200).
- **Well-scoped problem formulation with concrete examples:** The paper grounds the conditional intervention framework in realistic scenarios (doctor adjusting treatments, traffic controller managing delays) that make the assumptions about observable conditioning sets feel natural. The differentiation from Lee & Bareinboim (2018, 2020) and contextual bandits is clear and precise (Sections 1–2, Section 7).
- **Systematic search-space reduction experiments:** The Erdős-Rényi experiments sweep both graph size (20–500 nodes) and expected degree (2–11), convincingly showing that the method is most effective for large, sparse graphs — precisely the regime of real-world causal models. The bnlearn graph experiments confirm over 90% pruning on some large models (Section 6, lines 263–279).

## Weaknesses

### Fatal
None.

### Major
- **Non-standard regret metric weakens the bandit experiments:** The cumulative regret in Section 6 is computed against the "estimated best arm" — defined as the arm most runs concluded to be best at the end of training (footnote 11) — rather than against the true optimal arm's mean reward. This metric conflates convergence speed with convergence quality: mGISS could in principle exclude the truly optimal node (contradicting the theoretical guarantee) yet still show lower regret if CondIntUCB converges faster to a suboptimal but adequate arm while brute-force continues to explore. Since the paper's key claim is that mGISS guarantees containment of the optimal intervention, computing regret against the true optimum (derivable from the known SCM) would be a direct test of this guarantee. As presented, the regret curves demonstrate faster convergence to *something*, not necessarily to the optimum.
- **SCM parameterization for bandit experiments is unspecified:** The bnlearn repository provides Bayesian networks with graphical structure and conditional probability tables, not structural causal models with functional assignments. To simulate interventions in a bandit setting, one needs explicit structural equations and noise distributions. The paper never states what functional forms and noise distributions were used with each bnlearn graph (asia, sachs, child, pathfinder). Without this specification, the bandit experiments are not reproducible as described, and it is impossible to assess whether the SCMs used respect the causal graph structure claimed.

### Minor
- **No empirical verification that mGISS contains the optimal intervention:** While Theorem 13 provides a theoretical guarantee, a direct empirical sanity check — e.g., computing the truly optimal conditional intervention for a few SCMs with known ground truth and confirming it lies in the mGISS — would close the loop between theory and experiment. This is not essential given the proof, but its absence leaves a gap in the experimental narrative.
- **No sensitivity analysis for target Y selection:** All experiments pick Y as the node with the most ancestors (and >1 parent). While this is a reasonable heuristic, results could vary for randomly chosen targets, and a brief investigation would strengthen the generality claim.
- **CondIntUCB context handling is not discussed:** For graphs with even modest numbers of ancestors, the number of possible context realizations (values of Z_X) can grow combinatorially. The paper does not address how sparse contextual data is managed — e.g., whether unseen contexts default to a prior or whether contexts are binned.

### Trivial
- The claim in the introduction that "restricting to single-node interventions in fact makes the problem more challenging" (line 37) is debatable and could be toned down, as the paper itself notes this is only true in the narrow sense that the minimal search space is not trivially Pa(Y). This does not affect the technical contribution.

## Nice-to-Haves
- A discussion of what happens when only a subset of ancestors is observed (relaxing the An(X)\{X} ⊆ Z_X assumption) would strengthen practical relevance.
- Wall-clock time or computational cost of CondIntUCB relative to brute-force could be reported.
- Multiple SCM parameterizations per graph would demonstrate robustness of the pruning benefit.

## Removed Points
These points are flagged to be removed; treat them with caution:
- Harsh Critic's concern about the appendix being stripped — this is a parser artifact, not an author error. The proofs and full reference list exist in the original submission.
- Harsh Critic's note about Proposition 4/Proposition 6 proofs being unverifiable — the critic acknowledged the appendix was stripped and that the claim structure was plausible. Not a paper weakness.
- Harsh Critic's comment that "the paper does not discuss what happens when Y has no parents" — the paper explicitly scopes to Y with at least one parent (Proposition 6 states "with at least one parent", Theorem 13 same), and the single-parent case is addressed in the intuition section (Figure 1c, line 153: "In the particular case where Y has a single parent A, that node is the only node worth intervening on").
- Harsh Critic's criticism of "more challenging" claim — this is a framing choice, not a substantive error. Moved to Trivial.
- Strength Finder's characterization of "Empirical regret reduction" as a core strength — kept as a strength but qualified given the non-standard regret metric.
- Harsh Critic's concern about regret being computed against estimated best arm raised to Fatal — actually this is Major, not Fatal. The theoretical guarantee ensures the optimal node is in mGISS; the metric issue means the experiments don't *directly* verify the guarantee, but they still demonstrate practical benefit.
- Harsh Critic's suggestion to relax the An(X)\{X} ⊆ Z_X assumption — this is scope creep. The paper explicitly sets this as a working assumption under no latent confounding and flags latent confounders as future work. Moved to Nice-to-Haves.

## Novel Insights
The paper's key insight goes beyond the specific LSCA closure result: it shows that the problem of comparing conditional interventions in probabilistic SCMs reduces exactly to comparing atomic interventions in deterministic SCMs (Proposition 4). This equivalence is surprising and has implications beyond this paper — it suggests that for problems involving "best single-node intervention" queries on causal graphs, one can work entirely in the simpler deterministic-atomic framework without loss of generality. The Λ-structure characterization then gives this a clean graph-theoretic interpretation that connects naturally to the connector-based algorithm. The paper essentially maps a probabilistic decision problem onto a purely structural graph property.

## Suggestions
- Replace the estimated-best-arm regret metric with regret computed against the true optimal arm (analytically derived from the known SCM). This directly tests the theoretical guarantee and removes the conflation between convergence speed and convergence quality.
- Specify the SCM parameterization used with each bnlearn graph (structural equations, noise distributions). Ideally, use multiple parameterizations per graph to demonstrate robustness.
- Add a brief empirical sanity check: for a few SCMs, compute the ground-truth optimal intervention and verify it lies in the mGISS.
- Include a brief discussion of how CondIntUCB handles unseen context realizations.

## Anchor Comparisons
- **IPayPEGwdE (5.00):** Causal contextual bandits with adaptive context — our paper has more complete theory (full characterization vs regret bounds) and more systematic experiments. Our paper is clearly stronger.
- **oVVLBxVmbZ (5.25):** Conditional intervention in algorithmic recourse — our paper has a rigorous theoretical characterization that this paper lacks. Our paper is stronger.
- **pOoKI3ouv1 (5.75):** Robust agents learn causal world models — purely theoretical, no experiments. Our paper is stronger due to having experiments and a directly actionable algorithm.
- **YcW8i9VCf5 (6.00):** Adversarial Causal Bayesian Optimization — comparable overall quality. Our theory is more complete (exact characterization), our experiments are somewhat weaker. Roughly comparable; our paper is slightly better theoretically.
- **u63OVngeSp (7.00):** Deriving Causal Order from Single-Variable Interventions — has strong theory and competitive experiments that outperform baselines. Our paper has comparable theory but weaker experiments. Our paper is clearly below this anchor.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>