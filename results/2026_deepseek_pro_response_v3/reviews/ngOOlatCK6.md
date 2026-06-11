Now I have enough calibration data to finalize. Let me synthesize everything.

**Round 1 Bracket:** Between 5.5 and 7.5.

**Round 2 Anchors vs. This Paper:**

- **M0xK8nPGvt (7.50):** Stronger — has more polished theoretical analysis (Bayesian regret tied to prior knowledge), better experimental validation. Our paper has a more elegant graph-theoretic characterization but weaker experiments.
- **u63OVngeSp (7.00):** Slightly stronger — similar elegant theoretical contribution but more comprehensive evaluation with multiple baselines. Our paper's experimental validation is notably weaker.
- **YcW8i9VCf5 (6.00):** Comparable — both have solid theory with some experimental/positioning issues. Our paper contributes a more novel theoretical characterization.
- **IPayPEGwdE (5.00):** Our paper is stronger — more novel theory, cleaner contribution.

**Final Score:** The paper sits above 5.00 (IPayPEGwdE) and is roughly comparable to 6.00 (YcW8i9VCf5) with a slightly stronger theoretical contribution but weaker experimental validation. I place it at **6.0**.

---

## Summary
This paper introduces the conditional causal bandit problem and characterizes the minimal set of nodes (mGISS) guaranteed to contain the optimal single-node conditional intervention. The key theoretical insight is that the mGISS equals the LSCA closure of the parents of the reward variable Y, which is elegantly characterized via Λ-structures and computable in O(|V|+|E|) time via the C4 algorithm. The paper demonstrates significant search-space reduction on both random and real-world graphs.

## Strengths
- **Elegant Λ-structure characterization (Theorem 12):** The insight that the recursive LSCA closure has a simple one-shot characterization — a node V belongs iff it forms a Λ-structure over (U,U) (two internally-disjoint paths from V to nodes in U) — is theoretically clean and enables the efficient algorithm. This reformulation eliminates iterative computation and directly connects graph topology to interventional necessity.
- **Linear-time C4 algorithm (Theorem 16, Lemma 15):** The connector-based Algorithm 1 is simple, well-specified, and provably correct. The connector concept — tracking which closure node a node's influence funnels through — provides genuine algorithmic insight (a node is in the closure iff it is its own connector). The O(|V|+|E|) complexity makes it practical as preprocessing for any causal MAB method.
- **Clear problem formalization:** The paper carefully defines observable conditioning sets Z_X (lines 86-87), the conditional-intervention superiority preorder (Definition 1), and explicitly contrasts with Lee & Bareinboim (2018, 2020). The motivation through concrete examples (train delay control, medical treatment scheduling) is effective, and the paper is honest about its scope (no latent confounders, single-node interventions).
- **Substantial search-space reduction on real-world graphs:** Evaluation on the bnlearn repository shows over 90% search space reduction for the largest models, and the analysis correctly identifies that real-world causal graphs have low average degree (< 4.0), making them amenable to pruning by C4.

## Weaknesses

### Major
- **Regret metric is defined relative to an estimated best arm rather than ground-truth optimum (footnote 11):** Regret is computed "using the estimated best arm, defined as the arm that most runs concluded to be the best at the end of training." This is circular: it measures convergence to whatever each method discovers rather than to the true optimal intervention. If the mGISS accidentally excluded the genuinely optimal node, mGISS-restricted regret would still appear favorable because the "best arm" reference would shift to the best within the restricted set. Since bnlearn datasets have known CPTs from which ground-truth optimal interventions could be computed, this is an avoidable gap that undermines the regret evidence.
- **Bandit experiments lack baselines that would validate the specific mGISS characterization:** The regret experiments compare mGISS-restricted search against brute-force search over all ancestors of Y. While this demonstrates that pruning helps convergence, it does not test whether the mGISS is the *correct* minimal set. No comparison is made against simpler pruning strategies (e.g., "parents of Y only," "common ancestors of Pa(Y)," or the non-recursive LSCA), which would contextualize whether the sophisticated Λ-structure characterization yields benefits beyond obvious pruning heuristics.

### Minor
- **The CondIntUCB bandit algorithm is underspecified:** The description of how node-level and context-level UCB instances interact, how unseen contexts are handled, and how exploration is managed across the two levels is brief (lines 281-282). More detail would aid reproducibility, particularly given the novelty of the conditional-intervention bandit setting.
- **Scalability of the conditional-policy learning step is not addressed:** The CondIntUCB approach maintains a separate UCB instance for each unique context, which becomes impractical when Z_X has a large state space. While footnote 12 acknowledges datasets were chosen for being "sufficiently small," this limits the strength of practical applicability claims.

## Nice-to-Haves
- Empirically verify that the true optimal conditional intervention lies in the mGISS for the tested bnlearn datasets (since the true SCM is known from CPTs, this could be done via exhaustive enumeration over all single-node conditional interventions).
- Add baselines comparing mGISS against simpler pruning strategies (parents of Y, LCA of Pa(Y) without full closure) to demonstrate the value of the full LSCA closure characterization.
- Use ground-truth optimal arm for regret computation rather than the consensus best arm across runs.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **Harsh Critic Point about Proposition 4 equivalence:** The critic argued Proposition 4 is "not obviously true" and raised a mathematical concern about whether deterministic atomic superiority (pointwise per-unit optimality) implies conditional-intervention superiority (requiring a single policy that only sees Z_X). The critic stated "without access to the appendix I cannot verify whether the proof resolves the tension." Per review guidelines, criticisms about inability to verify proofs in the stripped appendix must be removed — the proofs exist in the original submission. The underlying mathematical observation about the tension between pointwise optimality and policy restrictions is noted but does not constitute a verified weakness since the paper claims the equivalence as proven and the proof is in the full submission.

## Novel Insights
The connector concept (Definition 14) provides a genuinely novel algorithmic insight: a node V is in the LSCA closure iff it is its own connector, meaning its children connect to multiple distinct closure nodes. This transforms the recursive LSCA definition into a single-pass reverse-topological computation with an intuitive "funneling" interpretation of causal influence in DAGs — a technique that may have applications beyond this paper in causal graph analysis.

## Suggestions
- Compute ground-truth regret against the true optimal arm for the bnlearn datasets (available from known CPTs) to directly validate that the mGISS contains the optimal conditional intervention.
- Add at least one comparison against a simpler pruning baseline (e.g., parents of Y or non-recursive LSCA) to demonstrate that the full Λ-structure characterization matters beyond naive pruning.
- Provide a full algorithm block for CondIntUCB to improve reproducibility.

## Score and Decision

**Calibration anchors considered:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| IPayPEGwdE (Causal Contextual Bandits, Adaptive Context) | 5.00 | R1 | Our paper is stronger — more novel theoretical characterization |
| YcW8i9VCf5 (Adversarial CBO) | 6.00 | R1 | Roughly comparable — our theory more elegant, their experiments stronger |
| oVVLBxVmbZ (Conditional Intervention Algorithmic Recourse) | 5.25 | R1 | Our paper is stronger — more fundamental contribution |
| ZXs3pkmrRG (Test-Time Causal Structure Learning) | 5.50 | R2 | Our paper is stronger — cleaner theory and algorithm |
| M0xK8nPGvt (Causal Graph Priors for PSRL) | 7.50 | R2 | That paper is stronger — more polished theory and experiments |
| u63OVngeSp (Causal Order from Single-Variable Interventions) | 7.00 | R2 | That paper is slightly stronger — more comprehensive empirical validation |

The paper makes a clean, novel theoretical contribution — the mGISS characterization and C4 algorithm — that is elegant and practical. However, the experimental validation has notable gaps: the circular regret metric undermines the bandit experiments, and the lack of comparison baselines means the experiments demonstrate only that pruning helps, not that the *specific* mGISS characterization is correct or necessary. These issues prevent the paper from reaching the 7.0+ tier but do not invalidate the core theoretical contribution, which stands on its own.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>