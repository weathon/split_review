Now I have all the information I need. Let me write the final review.

## Summary
This paper studies the problem of identifying the minimal set of nodes worth intervening on in a single-node conditional-intervention causal bandit. The authors define the "minimal globally interventionally superior set" (mGISS) and prove it equals the LSCA (Lowest Strict Common Ancestor) closure of the parents of the reward variable Y (Theorem 13). They also propose the C4 algorithm that computes this set in O(|V|+|E|) time (Theorem 16) and provide supporting experiments on random and real-world causal graphs.

## Strengths

1. **Proposition 4 (equivalence of superiority relations).** The paper proves that conditional-intervention superiority (Definition 1) coincides with deterministic atomic-intervention superiority (Definition 2). This is a non-trivial theoretical bridge — it allows the entire analysis to be carried out in the simpler deterministic atomic setting while the results apply to the more complex conditional-intervention setting (lines 118–120).

2. **Theorem 12 (Λ-structure characterization).** The characterization of the LSCA closure via Λ-structures (lines 199–200) gives a clean, checkable graphical criterion. This is a genuinely novel graphical concept that goes beyond the standard LCA notion used in prior work (Lee & Bareinboim, 2018), and the paper's own Figure 1d demonstrates why standard LCA fails and LSCA is necessary.

3. **Theorem 13 (LSCA closure = mGISS).** The main theoretical result — that the LSCA closure of Pa(Y) is the minimal set guaranteed to contain the optimal node for a single-node conditional intervention (lines 214–217). The uniqueness of the mGISS is also established (Proposition 6). This is a clean, provably minimal characterization.

4. **C4 algorithm with O(|V|+|E|) time complexity (Algorithm 1, Theorem 16).** The connector-based algorithm is elegant and practically useful — it can be used as a preprocessing step for any conditional causal bandit algorithm. The connector concept (Lemma 15) provides a nice intuition: a node whose children have multiple distinct connectors is a worthwhile intervention candidate.

5. **Search-space-reduction evidence.** The experiments on 1000 random graphs with varying sizes and degrees, combined with evaluations on most graphs from the bnlearn repository, convincingly show that mGISS is often substantially smaller than the full ancestor set, particularly for sparse graphs (lines 263–279). For the pathfinder model, the reduction exceeds 90%.

## Weaknesses

### Fatal
None.

### Major

1. **Regret computation uses a data-dependent oracle.** Footnote 11 (line 291) states: "For the computation of regret, we use the estimated best arm, defined as the arm that most runs concluded to be the best at the end of training." This is circular — the same experimental runs that determine which arm is "best" also determine the regret. Since the paper simulates from bnlearn models with known conditional probability tables, the true optimal conditional intervention could in principle be computed (for discrete variables, the optimal policy for each node is computable from the CPDs). The regret curves in Figure 3 therefore show that mGISS converges faster to a *consensus* about which node is best, but do not rigorously demonstrate convergence to the *truly optimal* node. This weakens the paper's claim in the abstract of "substantially accelerat[ing] convergence rates."

### Minor

2. **No comparison against other node-selection heuristics.** The bandit experiment compares mGISS only against brute-force (all nodes). The search-space-reduction experiments compare mGISS only against the full ancestor set. Natural baselines such as parents-only, ancestors-only, or an LCA-based selection adapted from Lee & Bareinboim (2018) are not included. While mGISS is provably minimal, quantifying how much tighter it is than other reasonable sets on real graphs would strengthen the empirical contribution.

3. **Bandit experiment limited in scope.** Only 4 graphs are used (8, 11, 20, 109 nodes), and the paper explicitly selects graphs where both mGISS and ancestor sets are "sufficiently small to allow experimentation" (line 281). This limits the generality of the regret results. The larger real-world graphs where mGISS achieves >90% reduction (mentioned in the search-space-reduction section) are not tested in the bandit setting.

4. **Lack of clarity on SCM reward generation.** The paper does not explain how rewards are generated from bnlearn models. Since bnlearn provides conditional probability tables for Bayesian networks, it is unclear whether these CPDs are used directly as the structural equations, and if so, whether the true optimal arm could have been computed analytically instead of relying on the data-dependent oracle (related to weakness 1).

### Trivial

5. Minor presentation ambiguity in Algorithm 1: `c[V]` is used both as an array name and as a value reference (`c[V] ← X` on line 8). This is slightly confusing on first reading but does not affect the algorithm's clarity.

## Nice-to-Haves
- A clean computational verification of Theorem 13 (e.g., for randomly generated SCMs, enumerate all possible conditional interventions over all nodes, identify the truly optimal node, and verify it lies in the mGISS) would directly demonstrate the practical relevance of the characterization.
- Comparison of mGISS size against heuristic node sets (parents, ancestors, LCA-closure) on the real-world bnlearn graphs would help quantify the tightness of the characterization beyond what the paper's examples show.
- Discussion of edge cases: what happens when Y has zero parents (Y is a root node) or exactly one parent (briefly mentioned in the intuition on line 153 but not formally covered).

## Removed Points
These points from the inputs were removed with brief justification:

- **Criticism that Definition 1 (conditional-intervention superiority) is too strong because it quantifies over all conditioning sets.** REMOVED. The universal quantification makes the guarantee *stronger*, not weaker — it is a worst-case bound that ensures the mGISS is valid for any valid choice of conditioning sets. This is a feature of the theoretical framing, not a flaw.
- **Criticism that experiments don't "test" the core theoretical guarantee.** REMOVED with partial absorption into nice-to-haves. Theorem 13 is a mathematical theorem; experiments cannot test it. The experiments demonstrate the practical consequences of the characterization. The suggestion to computationally verify the guarantee on random SCMs is a constructive idea but not a weakness.
- **Formatting/style nitpicks and concerns about missing appendix content.** REMOVED per hard rules (parser strips appendices from all papers; formatting artifacts are parser errors).
- **Concerns about code or model availability.** REMOVED per hard rules (the paper states code is in supplementary material).

## Novel Insights
None beyond the paper's own contributions. The most notable aspect is how Proposition 4 sidesteps the complexity of conditional interventions entirely, reducing the problem to deterministic atomic interventions. This is elegant but also means the mGISS characterization does not leverage any property unique to conditional interventions beyond the graph structure.

## Suggestions
1. **Fix the regret computation.** Since the bnlearn models (with known CPDs) are used for simulation, compute the true optimal expected reward for each node's conditional intervention. For discrete variables, this requires finding the best policy g: R_{Z_X} → R_X for each X, which is computable from the CPDs. Regret should be computed against this true optimal.
2. **Add heuristic baselines.** Compare mGISS size against parents-only and ancestors-only on the same random and real graphs, so the reader can see how much tighter the mGISS characterization is.
3. **Clarify reward generation.** Explain how the bnlearn CPDs (or structural equations) are used to generate rewards in the bandit simulation.
4. **Expand the bandit experiment.** Test on a few more real-world graphs, especially those where mGISS gives >90% reduction, to strengthen the claim about convergence acceleration.

---

## Score and Decision

**Calibration summary:**

All calibration anchors below are from `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/`.

| Paper (path prefix) | Avg Score | Round | Comparison to current paper |
|---|---|---|---|
| `p1b96KC6rj` | 2.17 | R1 | Not topically similar (CADR estimation); irrelevant for calibration |
| `y2ch7iQSJu` | 2.00 | R1 | Not topically similar (survival analysis) |
| `MVpvyeVeyI` | 3.40 | R1 | Causal BO with unknown graphs; mixed reviews (3,5,8,10); our theory is more self-contained |
| `aUeQPyRMeJ` | 3.80 | R1 | LLMs for causal discovery; not directly comparable |
| `nsvgVuaWXK` | 4.25 | R1 | Partially observable contextual bandit; less topically similar |
| `IPayPEGwdE` | 5.00 | R1,R2 | **Most topically similar.** Causal contextual bandits with theory+experiments. Our paper has a cleaner theoretical contribution but similar experimental weaknesses. Our paper is clearly stronger. |
| `ZXs3pkmrRG` | 5.50 | R2 | Test-time causal structure learning; limited topical overlap |
| `pOoKI3ouv1` | 5.75 | R2 | Purely theoretical causal learning paper; accepted despite no experiments. Our paper has theory + experiments (with flaws); comparable theoretical depth |
| `w50MQ9Vfty` | 5.50 | R2 | Causal inference under interference; limited topical overlap |
| `YcW8i9VCf5` | 6.00 | R1,R2 | **Adversarial Causal BO.** Theory+experiments, accepted with consensus 6s. Stronger empirical validation than our paper. |
| `9UGAUQjibp` | 5.80 | R2 | Causal dynamics in RL; limited topical overlap |
| `qac43AwuL9` | 6.00 | R2 | Causal Information Bottleneck; limited topical overlap |
| `mGmx41FTTy` | 6.33 | R1 | Topological ordering for DAGs; more methodologically different |
| `8muemqlnG3` | 6.50 | R1 | Causal discovery via BO; less topically similar |
| `u63OVngeSp` | 7.00 | R1 | Deriving causal order; stronger theory paper |
| `xByvdb3DCm` | 8.00 | R1 | Selection bias in causal discovery; clearly stronger paper |
| `3cuJwmPxXj` | 8.00 | R1 | Causal representation learning; clearly stronger paper |
| `A3YUPeJTNR` | 8.00 | R1 | Prediction timing; not topically similar |

**Round 1 bracket:** [5.0, 6.5]. The paper is clearly above the 2.5-4.5 band (reject-level papers) due to its clean theoretical contribution. It sits between the 5.00 topically similar causal bandits paper and the 6.00-7.00 upper-middle band.

**Round 2 narrowing:** Comparing within [4.5, 6.5], the paper is **stronger** than the 5.00 causal bandits paper (cleaner theory, more fundamental contribution) but **weaker** than the 6.00 adversarial CBO paper (which has more rigorous experiments). It is comparable in theoretical depth to the 5.75 purely theoretical paper.

**Final calibrated score: 5.5.** This reflects a paper with genuinely novel and clean theoretical contributions whose overall impact is diminished by a methodological flaw in the regret computation experiments. The theory alone (Proposition 4, Theorems 12-13, C4 algorithm) is publishable, but the empirical claims in the abstract about "substantially accelerating convergence rates" are not fully supported as written.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>