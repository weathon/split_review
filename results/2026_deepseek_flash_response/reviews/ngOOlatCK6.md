Now I'll write the final consolidated review.

## Final Merged Review

## Summary

This paper studies conditional causal bandits (single-node conditional interventions with known causal graph but unknown mechanisms) and provides a complete graphical characterization of the minimal set of nodes (mGISS) guaranteed to contain the optimal intervention target. The main theoretical result (Theorem 13) proves the mGISS equals the LSCA closure of the parents of Y, and the paper provides the C4 algorithm that computes this set in O(|V|+|E|) time. Experiments on random and real-world graphs demonstrate substantial search-space reduction, and bandit simulations show that pruning to the mGISS accelerates convergence.

## Strengths

- **Proposition 4 (equivalence of superiority relations).** The paper proves that conditional-intervention superiority (Definition 1) is equivalent to deterministic atomic-intervention superiority (Definition 2). This is a non-trivial theoretical bridge: it lets the authors reason in the simpler deterministic-atomic setting and carry results back to the more complex conditional-intervention setting. Prior work (Lee & Bareinboim 2018) dealt only with hard interventions and did not establish any such equivalence.

- **Theorem 13 + Theorem 12 (full graphical characterization of the mGISS).** Theorem 13 identifies the minimal set of nodes that must be tested as the LSCA closure of the parents of Y, and Theorem 12 gives an elegant alternative characterization via Λ-structures. For the single-node conditional-intervention case, the characterization is a non-trivial recursive closure — going substantially beyond Lee & Bareinboim (2018) where for multi-node hard interventions the parents themselves form the minimal set.

- **C4 algorithm with O(|V|+|E|) time complexity (Theorem 16, Algorithm 1).** The connector-based procedure computes the mGISS in a single reverse-topological pass. The connector concept (Definition 14) is clean: if all children of V share the same connector, V is redundant; otherwise V enters the closure. No prior work on minimal search spaces for causal bandits provides an explicit linear-time algorithm.

- **Large search-space reduction on real graphs.** The paper reports over 90% pruning on some of the largest bnlearn models (line 279). This is concrete evidence that the theoretical characterization yields practical savings in realistic sparse graphs.

- **Clearly articulated problem difficulty.** The paper explicitly explains why the single-node conditional-intervention setting is more challenging than the multi-node hard-intervention setting (lines 32–38, 98): with multi-node interventions one can intervene on all parents of Y simultaneously, but with single-node interventions the optimal node may be a distant common ancestor, motivating the LSCA closure machinery.

## Weaknesses

### Fatal
None.

### Major
None. The theoretical core is sound and well-presented; the weaknesses below are addressable but do not threaten the paper's central claims.

### Minor

- **Regret computation uses an empirically estimated best arm as the oracle.** Footnote 11 (line 291) states that regret is computed using "the estimated best arm, defined as the arm that most runs concluded to be the best at the end of training." This means the oracle against which regret is measured is itself a statistical estimate derived from the algorithm being evaluated. If the algorithm systematically converges to a suboptimal arm in many runs (which can happen when the number of contexts per node is large relative to sample size), the reported regret would be artificially deflated. Since the bnlearn models have known conditional probability tables, the optimal arm per node could be computed independently, providing a cleaner ground truth. This issue should be addressed in a revised version.

- **The bandit experiments compare a superset (all ancestors) against a subset (mGISS), so faster convergence from fewer arms is partially predetermined.** Since the mGISS is by construction a subset of the ancestor set, it is well known that any bandit algorithm converges faster with fewer arms under otherwise identical conditions. The experiments therefore illustrate a trivial consequence of arm-count reduction rather than testing the paper's central theoretical guarantee (that the mGISS contains the optimal node). A stronger experimental design would use synthetic SCMs where the ground-truth optimal node is known by construction, and verify that it always falls within the mGISS. This would directly demonstrate the paper's main value proposition rather than merely showing that pruning helps — which is expected regardless of whether the pruning criterion is correct.

- **Target Y is always the node with the most ancestors.** This choice (lines 263, 279) systematically biases the results toward graphs with large ancestor sets, making the pruning appear more dramatic. A robustness check using randomly selected Y nodes (subject to having multiple parents) would strengthen the analysis.

- **No comparison with simpler heuristic baselines for node selection.** The paper compares "all ancestors" against "mGISS." A natural baseline would be the LCA-based heuristic discussed in the intuition section (parents of Y plus their lowest common ancestors). The paper argues that LCA fails for graphs like Figure 1d, but quantifying how often this matters in real graphs would be informative. This is more of a missed opportunity than a critical flaw.

### Trivial
None.

## Nice-to-Haves
- Redesign the bandit experiments to use synthetic SCMs where the optimal intervention is known, directly testing whether the mGISS always contains the optimal node.
- Add a baseline comparison with the LCA-based heuristic on real graphs.
- Report the range of pruning fractions and specific model names for the >90% reduction claim in the main text (currently these details are in the appendix).
- Include a brief "Scope and Limitations" paragraph after Theorem 13 making explicit what the characterization does not cover.

## Removed Points
*These points were flagged by the reviewers but are removed here with justification.*

- **"Proposition 4 is stated without proof (deferred to appendix)."** The paper explicitly states (line 60–61) that all proofs are in the appendix. The parser strips appendix content from all papers. This is not a weakness of the paper as submitted.
- **"Results for real-world graph search space reduction are in the appendix."** Same reason — appendix content is stripped by the parser.
- **"The assumption that An(X)\{X} ⊆ Z_X is a substantive restriction."** The paper already acknowledges this and discusses its implications with concrete examples.
- **"The comparison with Lee & Bareinboim is handled fairly but..."** This is a positive observation, not a weakness.
- **"The paper does not test whether the mGISS throws away the optimal node."** This is actually a theoretical guarantee (Theorem 13); the experiments are illustrations of practical impact, not proofs. The point about stronger experimental design is kept as a minor weakness above.
- **Strength Finder's generic strengths** (e.g., "addressed an important problem") are removed as they are not specific or evidence-grounded.

## Novel Insights

The harsh critic's most valuable observation is that the bandit experiments test a trivial consequence of pruning (fewer arms → faster convergence) rather than the paper's central theoretical claim. This is a genuine insight into how the empirical evaluation could be substantially strengthened: by using synthetic SCMs with known ground-truth optimal interventions, the authors could directly verify that the mGISS indeed retains the optimal node. The finding that real-world graphs achieve >90% pruning is also interesting and deserves more prominent presentation.

## Suggestions
1. In the bandit experiments, replace the estimated-best-arm regret computation with the known optimal intervention derived from the bnlearn CPTs, or use synthetic SCMs where the optimal intervention is known by construction.
2. Add a robustness check using randomly selected Y nodes (with multiple parents) in the graph pruning experiments.
3. Consider including the LCA-based heuristic as a baseline to quantify the frequency of graphs where the stricter LSCA notion makes a difference.
4. Report the specific graph names and pruning fractions for the >90% reduction claim in the main text.
5. Add a brief "Scope and Limitations" paragraph after Theorem 13 to explicitly state what the mGISS characterization does not cover (e.g., simultaneous multi-node interventions, latent confounding, optimal policy selection for a given node).

## Score and Decision

### Calibration Anchors

**Round 1 — Bracketing:**
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|-----------|
| `IPayPEGwdE.md` (Causal Contextual Bandits) | 5.00 | R1 | Weaker: restricts to binary interventions, simple chain graphs, while current paper handles general graphs and richer interventions |
| `YcW8i9VCf5.md` (Adversarial CBO) | 6.00 | R1 | Comparable: similar theoretical depth, but current paper has cleaner theory while ACBO has stronger experiments |
| `M0xK8nPGvt.md` (Causal Priors for RL) | 7.50 | R1 | Stronger: broader scope with both theory and experiments; current paper is narrower and more specialized |
| `xByvdb3DCm.md` (Causal Discovery Selection) | 8.00 | R1 | Stronger: more comprehensive contribution with both theoretical and experimental depth |

**Bracket from Round 1:** The paper sits between the 5.0 anchor (clearly weaker) and the 7.5–8.0 anchors (clearly stronger), with the 6.0 anchor being the closest comparator.

**Round 2 — Narrowing:**
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|-----------|
| `ZXs3pkmrRG.md` (Test-Time Causal Learning) | 5.50 | R2 | Weaker: more applied, with higher variance in reviewer scores; current paper is more theoretically solid |
| `pOoKI3ouv1.md` (Robust Causal World Models) | 5.75 | R2 | Comparable: both are theory-heavy, but current paper has cleaner self-contained results while the anchor has higher variance (8,1,6,8) |
| `2pEqXce0um.md` (Root Cause Analysis) | 4.50 | R2 | Weaker: more applied, less novel theoretically |
| `8muemqlnG3.md` (Causal Discovery via BO) | 6.50 | R2 | Comparable but stronger experiments and broader empirical validation |

**Final Score:** The paper is closest to the 6.0 anchor (Adversarial CBO, Accepted) in overall quality. Its theoretical contribution is cleaner and more self-contained, but its empirical evaluation is weaker. After comparing against all anchors, the paper merits a score of **6.0** — marginally above the acceptance threshold. The theoretical results are original, non-trivial, and clearly presented; the experiments serve their illustrative purpose despite the methodological concerns noted above.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>