Now I'll produce the final consolidated review with the calibrated score.

## Summary

This paper studies single-node conditional-intervention causal bandits, where arms are conditional interventions (do(X = g(Z_X))) on a known causal graph G, and the goal is to maximize expected reward Y. The core contribution is a complete graphical characterization of the minimal set of nodes (mGISS) guaranteed to contain the optimal intervention node. Theorem 13 proves that mGISS_Y(G) = ℒ^∞(Pa(Y)) — the LSCA (lowest strict common ancestor) closure of the parents of Y. The paper also provides a linear-time O(|V|+|E|) algorithm (C4) to compute this set, and experiments showing substantial pruning on real-world graphs and improved regret in a UCB-based bandit.

## Strengths

- **Proposition 4 — equivalence between conditional-intervention and deterministic atomic-intervention superiority (Section 3):** The paper proves that X ⪰_Y^c W ⇔ X ⪰_Y^{det,a} W, establishing that the complex problem of conditional interventions in probabilistic SCMs reduces to the simpler problem of atomic interventions in deterministic SCMs. This non-obvious theoretical bridge makes the entire graphical characterization tractable and cleanly separates the paper from prior work (Lee & Bareinboim 2018, which studied multi-node hard interventions).

- **Theorem 13 — crisp characterization of mGISS as LSCA closure of Pa(Y) (Section 4):** The paper proves that mGISS_Y(G) = ℒ^∞(Pa(Y)), with an elegant equivalent characterization via Λ-structures (Theorem 12). This is a crisp, verifiable, and actionable result: given any DAG, one can immediately read off which nodes must be considered for intervention.

- **C4 algorithm with O(|V|+|E|) time complexity (Algorithm 1, Theorem 16, Section 5):** The algorithm computes ℒ^∞(U) in time linear in |V| and |E|, which is optimal since the input graph must be read. The connector data structure (Definition 14) and the lemma that c[V]=V ⇔ V∈ℒ^∞(U) are clean and ensure correctness. The pseudocode is simple enough to implement directly.

- **Provably unique mGISS (Proposition 6, Section 4):** The paper establishes uniqueness of the minimal globally interventionally superior set, confirming the characterization is well-defined and not ambiguous.

- **Search-space reduction of >90% on large real-world graphs (Section 6):** On several bnlearn benchmark models and a railway delay graph, C4 prunes over 90% of ancestor nodes. The paper honestly contextualizes this by noting real-world graphs have low average degree (all tested below 4.0), which is precisely the favorable regime — consistent with the random-graph experiments (e.g., 17% retention at degree 2 for 500-node graphs).

## Weaknesses

### Major

None that threaten the paper's core theoretical contribution.

### Minor

- **Regret experiment uses estimated best arm rather than true optimal arm (Footnote 11, Section 6):** The paper states: "For the computation of regret, we use the estimated best arm, defined as the arm that most runs concluded to be the best at the end of training." Since the bnlearn datasets have known conditional probability tables, the true optimal intervention could have been computed. The current approach conflates the bandit algorithm's convergence behavior with the actual quality of the mGISS — if brute-force converges to a worse arm, its regret is underestimated. The qualitative trend (mGISS converges faster) is almost certainly real, but the precise regret numbers and the framing of "significant improvement" are less cleanly interpretable than ground-truth-based evaluation would be. This is the paper's most significant methodological weakness.

- **Bandit experiment compares mGISS only against "all ancestors of Y" baseline (Section 6):** This comparison is primarily a sanity check that pruning doesn't hurt (already guaranteed by Theorem 13). Comparing against alternative reasonable pruning strategies (e.g., Pa(Y) only, LCA(Pa(Y))) would demonstrate that the LSCA closure captures structure that simpler heuristics miss, providing more informative evidence for the value of the specific characterization.

- **Regret experiment uses only 4 graphs, all relatively small (Section 6):** The largest graph (pathfinder, 109 nodes) has only ~50 nodes in An(Y). The results demonstrate the method works on these specific graphs but provide limited evidence of generality at larger scales.

- **Random-graph experiments report only average retention fraction (Section 6):** Reporting the proportion of graphs where mGISS is strictly smaller than the full ancestor set (not just the average) would give a clearer picture of when the method is useful versus when it retains all nodes.

### Trivial

None significant.

## Nice-to-Haves

- Worst-case analysis of mGISS size for dense graphs (e.g., complete DAGs) would help practitioners know when the pruning will not help.
- Sensitivity analysis to graph misspecification (missing/extra edges) would strengthen practical applicability claims.
- Discussion of the computational cost of CondIntUCB's per-context UCB approach, which could explode combinatorially for nodes with many ancestors.

## Removed Points

The following points from the inputs were removed in accordance with the filtering guidelines:

- **Proposition 4 proof "relegated to the appendix":** Removed per hard rules — the parser strips appendices from all papers; the proof exists in the original submission. The structural concern about Proposition 4's centrality is retained as a minor note but softened.
- **"Missing appendix" or "missing proofs":** Removed per hard rules.
- **Speculative "if the proof fails" fatal scenarios:** The harsh critic acknowledged the claim is "likely correct"; a fatal flaw must be unambiguous from what is on the page. The concern is present but softened to a minor structural note.
- **Generic "evaluation lacks rigor" / "baselines may not be fair" framings without concrete anchors:** Removed.
- **Criticisms about reproducibility (hyperparameters, complete training logs):** Removed per hard rules.
- **Strength about "empirical demonstration that pruning reduces regret":** The qualitative trend is valid, but the weakness about estimated-best-arm computation means the precise quantitative claim is weakened. The strength is retained with the caveat noted above.

## Novel Insights

None beyond the paper's own contributions. The reviewer inputs did not surface an insight about the paper that the paper itself does not already communicate.

## Suggestions

1. **Compute regret against the true optimal arm** using the known CPTs of the bnlearn models. This would convert the regret curves from a qualitative demonstration to quantitative evidence and cleanly address the most significant methodological concern.
2. **Add comparisons against simpler pruning baselines** (Pa(Y) only, LCA(Pa(Y))) in the bandit experiment to demonstrate that the LSCA closure captures structure that simpler heuristics miss.
3. **Report the proportion of random graphs** where mGISS is strictly smaller than the full ancestor set, not just the average retention fraction.
4. **Include a brief intuitive sketch of why Proposition 4 holds** in the main text, so readers can assess the claim without consulting the appendix.

## Score and Decision

**Calibration Anchors (all rounds):**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| MVpvyeVeyI — Causal Bayesian Optimization with Unknown Graphs | 6.50 (but high variance: 5,8,3,10) | R1 | Different topic (CBO without known graph); received split reviews |
| fSxiromxAq — Sparse Causal Model | 3.00 | R1 | Clearly weaker; poorly executed |
| AvXrppAS2o — Improved outcome prediction using causal structure learning | 3.00 | R1 | Clearly weaker |
| TRHyAnInUC — D³PM Diffusion Causal Discovery | 3.25 | R1 | Clearly weaker |
| IPayPEGwdE — Learning Good Interventions in Causal Contextual Bandits | 5.00 | R1, R2 | Most similar topic; rejected due to restrictive assumptions and weak experiments. Our paper is stronger — cleaner theory, better experiments, more general setting. |
| YcW8i9VCf5 — Adversarial Causal Bayesian Optimization | 6.00 | R1, R2 | Accepted; comparable quality. Both have clear theory + experiments, though in different sub-areas. |
| ZXs3pkmrRG — Test-Time Learning of Causal Structure | 5.50 | R2 | Less topically related; moderate scores |
| pOoKI3ouv1 — Robust agents learn causal world models | 5.75 | R2 | Different topic (theory of causal learning for robustness); accepted but split reviews |
| u63OVngeSp — Deriving Causal Order from Single-Variable Interventions | 7.00 | R2 | Higher-scoring; broader implications but also more restrictive assumptions. Our paper has cleaner characterization. |
| mGmx41FTTy — Two Time-Slices Help Topological Ordering | 6.33 | R2 | Less topically related |
| 8muemqlnG3 — Causal Discovery via Bayesian Optimization | 6.50 | R2 | Different methodology |
| M0xK8nPGvt — Exploiting Causal Graph Priors with Posterior Sampling for RL | 7.50 | R2 | Stronger paper with broader scope, more thorough evaluation |

**Round 1 bracket:** [5.0, 7.0] — clearly above the 3.0-3.5 weak band, comparable to the 5.0-6.0 middle band.

**Round 2 narrowing:** The paper is meaningfully stronger than the 5.0 anchor (same sub-area, rejected) and comparable to the 6.0 anchor (accepted). It is cleaner theoretically than the 5.75 anchor but has weaker experiments than the 7.0-7.5 anchors. The primary limitation is the estimated-best-arm issue in the regret experiment, which reduces the strength of the empirical evidence but does not threaten the theory.

**Final score:** 6.0 — marginally above the acceptance threshold. The paper makes a genuine, well-executed theoretical contribution (Proposition 4 + Theorem 13 + Theorem 16) that is clearly motivated, rigorously defined, and honestly scoped. The C4 algorithm is elegant and practically usable. The experiments demonstrate the method works, though the regret evaluation has a methodological weakness that should be addressed in revision. The paper is above the quality of rejected causal-bandits papers (score 5.0) and comparable to accepted middle-band papers (score 6.0).

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>