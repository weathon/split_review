Now I have a clear picture. Let me finalize the review.

**Round 1 bracket:** 5.5–7.5

**Round 2 comparisons:**
- YcW8i9VCf5 (6.00, Accept): Adversarial CBO with regret bounds — has presentation issues, unclear relationship to prior work. Our paper is cleaner and more self-contained.
- u63OVngeSp (7.00, Accept): Causal order from interventions — strong theory + algorithm + extensive experiments. Comparable quality but more ambitious. Our paper is slightly narrower.
- pOoKI3ouv1 (5.75, Accept): Causal world models — more philosophical. Our paper is stronger.
- mGmx41FTTy (6.33, Reject): Topological ordering — comparable quality but different area.

**Final score: 6.5.** The paper has an elegant theoretical characterization, a clean linear-time algorithm, and solid empirical validation. Weaknesses (non-standard regret metric, no heuristic baselines, policy-selection gap) are minor and don't undermine the core contribution.

---

## Summary
This paper introduces the conditional causal bandit problem, where arms are single-node conditional interventions of the form do(X = g(Z_X)). The authors characterize the minimal set of nodes (the mGISS) guaranteed to contain the node whose optimal conditional intervention maximizes expected reward, and provide an O(|V|+|E|) algorithm (C4) to compute this set from the causal graph alone. Experiments on random and real-world bnlearn graphs demonstrate substantial search-space pruning (over 90% for large models) and improved cumulative regret when restricting the node search space to the mGISS.

## Strengths
- **Proposition 4 — Equivalence between conditional and deterministic atomic superiority (Section 3):** This non-obvious result proves that the complex conditional-intervention superiority relation (involving universally quantified policies, observable conditioning sets, and expectations over noise) is equivalent to the simpler deterministic atomic-intervention superiority. This reduction is the linchpin that makes the subsequent graphical analysis tractable, as the authors explicitly note on line 122: "Since deterministic atomic interventions are easier to reason about, we use them in formulating proposals for the minimal search space and in our proofs."
- **Theorem 13 — LSCA closure of Pa(Y) characterizes the mGISS (Section 4):** The paper builds up through well-motivated graph examples (Figure 1), introduces the stricter notion of lowest strict common ancestors (LSCA, Definitions 7–8), defines the iterative LSCA closure (Definition 9), provides an elegant equivalent characterization via Λ-structures (Theorem 12), and proves the main result. The pedagogical build-up through Figure 1 (illustrating why naive heuristics like LCAs fail) makes the result intuitive before formalization.
- **C4 algorithm — linear-time computation of the LSCA closure (Section 5, Algorithm 1):** The connector-based algorithm is genuinely clever, computing what would naively be an expensive iterative closure in a single reverse-topological pass in O(|V|+|E|) time. Lemma 15 provides the key semantic insight (the connector is the first LSCA-closure node on any path), and Theorem 16 ties the algorithmic logic directly to the graphical characterization.
- **Empirical validation on real-world graphs (Section 6):** Experiments on bnlearn graphs show search-space reductions exceeding 90% for some of the largest models, confirming practical value. Bandit experiments across four datasets (asia, sachs, child, pathfinder) demonstrate consistently lower cumulative regret when pruning to the mGISS compared to brute-force node selection (Figure 3).
- **Clear problem scoping and well-justified assumptions (Sections 1–2):** The paper carefully differentiates its contribution from Lee & Bareinboim (2018), clearly explaining why single-node conditional interventions are both harder and more realistic than multi-node hard interventions (lines 98–99). The assumptions on observable conditioning sets are motivated through concrete examples (train delays, medical treatment scheduling).

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
- **Non-standard regret metric (footnote 11, line 291):** The cumulative regret is computed against "the estimated best arm, defined as the arm that most runs concluded to be the best at the end of training" rather than against the true optimal arm. While the true optimal arm is genuinely unavailable in this setting, this choice should be discussed more explicitly, as it could create subtle issues if brute-force search occasionally finds arms the mGISS-restricted search cannot reach. Reporting mean rewards alongside regret would corroborate the finding.
- **No baseline comparison for node-selection heuristics:** The bandit experiments compare mGISS-restricted search only against full brute-force search. Simpler heuristics such as using only Pa(Y) or Pa(Y) plus one iteration of LSCA would help the reader assess how much value the full LSCA closure provides over cheaper alternatives, particularly for denser graphs where the closure can be substantially larger than Pa(Y).
- **Policy-selection gap bounds practical significance:** The paper solves the node-selection subproblem but does not address the policy-selection subproblem (finding the optimal g for a given node). The CondIntUCB algorithm uses naive per-context UCB, which does not scale to graphs with high-cardinality variables. The paper acknowledges this honestly (lines 96, 313: "no such algorithm currently exists"), but the practical contribution is narrower than the framing sometimes implies.

### Trivial
- **Experimental target choice is arbitrary:** Y is always chosen as "the node with the most ancestors" (with more than one parent). Results could vary with different target choices, and this sensitivity is not explored. This is a minor limitation given the systematic random-graph experiments already cover diverse graph structures.

## Nice-to-Haves
- Reporting mean rewards alongside regret in the bandit experiments would address the estimated-best-arm concern and give a clearer picture of arm quality.
- A brief discussion of how C4 could be combined with more sophisticated policy-search methods would calibrate reader expectations.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **Harsh Critic Point 1 (Proposition 4 proof not in main text):** REMOVED per hard rule — the complaint is that the proof is in the appendix, which the parser stripped. The original submission includes full proofs. The paper explicitly states "All proofs of the results presented in the paper can be found in the appendix" (line 60–61).
- **Harsh Critic note about Ch(V) ∩ An(U) complexity:** REMOVED — computing ancestors of a set is trivially O(|V|+|E|) with standard graph traversal, already within the stated complexity bound.
- **Harsh Critic note about topological order assumption:** REMOVED — computing a topological ordering of a DAG is O(|V|+|E|), a standard preprocessing step.
- **Harsh Critic note about "single-node interventions are harder" claim not being argued in detail:** REMOVED — the paper provides a clear argument on lines 98–99, and this is a framing claim, not a core result.
- **Harsh Critic note about Definition 3 being "weak form of set superiority":** REMOVED — this is a descriptive observation, not a substantive weakness, and the formulation is appropriate for the single-node setting.
- **Harsh Critic note about garbled Figure 2 caption:** REMOVED — this is a parser formatting artifact, not an author error.
- **Harsh Critic note about "missing analysis of graph misspecification":** REMOVED — the paper addresses this at lines 57–60: "if the true causal graph is unknown and instead a family of candidate graphs is available, the C4 algorithm can simply be applied to each candidate graph, and the results combined by taking the union of the resulting minimal search spaces." The paper does not claim robustness to misspecification as a contribution.

## Novel Insights
Beyond the paper's own contributions, the review process highlights an interesting structural observation: the paper's reduction of conditional-intervention superiority to deterministic atomic-intervention superiority (Proposition 4) is a rare example where adding realism (conditional policies, unknown noise, expectations) does not change the graphical characterization of which nodes matter for optimal intervention. This suggests that when the conditioning set Z_X contains all ancestors of X (as the paper assumes), the information carried by observed variables is sufficient to bridge the gap between deterministic per-unit optimization and probabilistic expected optimization — a philosophically interesting result about the power of ancestral information in causal systems.

## Suggestions
- Add a simple baseline comparison (e.g., Pa(Y) alone, or one-iteration LSCA) to the bandit experiments to quantify the marginal value of the full LSCA closure.
- Report mean final-arm rewards alongside cumulative regret to corroborate the regret findings.
- Discuss how the mGISS changes under different target node choices, even qualitatively, to give readers intuition about robustness.

## Score and Decision

**Anchor comparison summary:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| IPayPEGwdE (Causal Contextual Bandits) | 5.00 | R1 | Our paper has cleaner theory and better empirical grounding |
| MVpvyeVeyI (CBO Unknown Graphs) | 3.40 | R1 | Our paper is substantially stronger in rigor and presentation |
| 8muemqlnG3 (Causal Discovery via BO) | 6.50 | R1 | Comparable quality; our paper more theoretical, theirs more empirical |
| xByvdb3DCm (Selection meets Intervention) | 8.00 | R1 | Our paper is narrower in scope and theoretical ambition |
| YcW8i9VCf5 (Adversarial CBO) | 6.00 | R2 | Our paper has cleaner framing and fewer unresolved issues |
| pOoKI3ouv1 (Robust agents learn causal models) | 5.75 | R2 | Our paper has more concrete algorithmic and empirical contributions |
| mGmx41FTTy (Two Time-Slices) | 6.33 | R2 | Comparable quality; different problem domain |
| u63OVngeSp (Causal Order from Interventions) | 7.00 | R2 | Slightly stronger — more extensive evaluation, broader scope |

The paper's clean theoretical characterization, elegant linear-time algorithm, and solid empirical validation place it squarely in the accept range. Minor weaknesses around the regret metric, missing heuristic baselines, and the policy-selection gap are addressable and do not undermine the core contribution.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>