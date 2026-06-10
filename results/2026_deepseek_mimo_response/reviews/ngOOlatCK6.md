Now I have enough calibration data. Let me write the final review and score.

**Round 1 bracket**: Based on comparison with anchors scoring 5.0 (causal contextual bandits, rejected), 6.0 (adversarial CBO, accepted), and 7.0 (causal order derivation, accepted), the paper sits in the 5.5–7.0 range.

**Round 2 narrowing**: Compared to the 6.0 anchors (fGhr39bqZa: causal graph recovery via homologous surrogates; YcW8i9VCf5: adversarial CBO), the under-review paper has cleaner and more elegant theory (the Λ-structure characterization is particularly well-crafted). Compared to the 7.0 anchor (u63OVngeSp: deriving causal order from interventions), the under-review paper has comparable theoretical novelty but weaker empirical validation. This places it at ~6.5.

## Summary
This paper addresses conditional causal bandits, where arms are conditional interventions `do(X = g(Z_X))` rather than hard interventions. The core contribution is a graphical characterization of the minimal Globally Interventionally Superior Set (mGISS) — the smallest set of nodes guaranteed to contain the optimal node for a single-node conditional intervention to maximize a target variable Y. The paper proves this set equals the LSCA closure of Y's parents, characterized via novel Λ-structures, and provides a linear-time algorithm C4 (O(|V|+|E|)) to compute it.

## Strengths
- **Surprising equivalence result (Proposition 4)**: The proof that conditional-intervention superiority (≥^c_Y) and deterministic atomic-intervention superiority (≥^{det,a}_Y) are equivalent is non-obvious — conditional interventions involve arbitrary policies over conditioning sets while atomic interventions on deterministic SCMs are far simpler. This equivalence (line 120: "X ≥^c_Y W ⟺ X ≥^{det,a}_Y W") enables the entire analysis to proceed in the simpler deterministic setting.
- **Elegant main characterization via Λ-structures (Theorems 12–13)**: The Λ-structure concept (Definition 11) provides an intuitive graph-theoretic characterization. Theorem 12 establishes L^∞(U) = Λ(U, U), and Theorem 13 proves this equals the mGISS. The progressive examples in Figure 1a–d effectively motivate why standard LCA is insufficient and why the recursive LSCA closure is needed.
- **Optimal algorithm C4 with formal correctness (Theorem 16)**: The connector concept (Definition 14) reduces the problem to a single reverse-topological-order pass. Lemma 15 provides clear intuition: V ∈ L^∞(U) ⟺ c[V] = V. The O(|V|+|E|) complexity is optimal since the graph must be read.
- **Substantial empirical search space reduction**: For 500-node random graphs (expected degree 2), mGISS retains only 17% of ancestor nodes on average (line 277). Real-world bnlearn graphs show over 90% reduction for larger models (Figure 6, Appendix H).
- **Validated improvement in MAB convergence**: CondIntUCB experiments on four bnlearn datasets (asia, sachs, child, pathfinder) show consistently faster convergence and lower cumulative regret when the search space is pruned, averaged over 300–500 runs (Figure 3, line 275).

## Weaknesses

### Fatal
None.

### Major
- **Regret experiments lack SCM specification**: The paper uses bnlearn graph structures but does not describe the specific structural assignments F or noise distributions p_N that define the SCMs used in the regret experiments (Section 6). The mGISS result is guaranteed to contain the optimal node for any SCM, but the magnitude of regret improvement depends on the chosen SCM. While the code repository is provided (line 317), the paper alone does not allow the reader to assess whether the chosen SCMs are representative or particularly favorable. (Line 281 describes the bandit setup but not the underlying SCM.)
- **Regret experiment comparison is somewhat expected**: Since mGISS is theoretically guaranteed to contain the optimal node, comparing UCB over all ancestor nodes vs. UCB over mGISS nodes is a valid proof-of-concept but the result — fewer arms → faster UCB convergence — is largely predictable from the theory. The paper itself acknowledges the experiments are validation ("we present empirical evidence that restricting the node search space to the mGISS allows a straightforward UCB-based algorithm to converge more rapidly," line 281), but a stronger empirical case would involve comparison against non-causal bandit baselines or scaling experiments.

### Minor
- **Limited dataset selection for regret experiments**: Only 4 datasets with specific target selection criteria (node with most ancestors, more than one parent, tractable size). The criteria are disclosed (footnotes 8, 12) and justified (e.g., cancer dataset has trivial mGISS), but this limits generalizability.
- **No discussion of Z_X choice impact**: The experiments use the smallest observable conditioning set (Z_X = An(X) \ {X}, footnote 10), giving the bandit algorithm less context than possible. The paper does not discuss how Z_X choice affects results.

### Trivial
- Standard deviations are mentioned (line 275) but could be reported more systematically alongside final regret values.

## Nice-to-Haves
- A scaling experiment showing how the regret gap between mGISS and brute-force grows with graph size would strengthen the practical significance argument considerably.
- Reporting C4's actual computation time empirically would reinforce it is negligible as a preprocessing step.
- Brief discussion of mGISS sensitivity to approximate/learned causal graphs would be valuable for practitioners.

## Removed Points
These points are flagged to be removed, treat them with caution:
- **"Narrow scope bounding contribution"**: The harsh critic notes the restrictions (single-node interventions, no latent confounders, node selection only). However, the authors explicitly acknowledge each restriction and justify them as necessary steps toward the general case (lines 36–42). This is appropriate for a theory paper.
- **"Missing related works"**: Cannot verify external references exist, so not included.
- **Formatting/style nitpicks**: Parser artifacts, not paper problems.

## Novel Insights
The equivalence between conditional-intervention superiority and deterministic atomic-intervention superiority (Proposition 4) is genuinely surprising and novel. It means that the complex optimization over all possible policies g and conditioning sets Z_X collapses to the much simpler problem of finding the best fixed value x for a single variable X in a deterministic model (known n). This insight is what makes the graphical characterization tractable and is the paper's most intellectually distinctive contribution.

## Suggestions
- Specify the SCMs used in the regret experiments (at minimum, describe the functional forms and noise distributions), even if the code is available.
- Add a brief scaling experiment for regret across different graph sizes.
- Consider comparing C4 + CondIntUCB against a non-causal bandit baseline to strengthen the practical case.

## Reporting — Calibration Anchors

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| Causal Bayesian Optimization with Unknown Graphs | MVpvyeVeyI.md | 6.50 | 1 | CBO variant with unknown graphs; more applied but more scattered contributions |
| Causal Contextual Bandits with Adaptive Context | IPayPEGwdE.md | 5.00 | 1 | Causal contextual bandits; weaker theory, rejected |
| Adversarial Causal Bayesian Optimization | YcW8i9VCf5.md | 6.00 | 1 | CBO under adversarial external interventions; comparable quality, accepted |
| Root Cause Analysis via Observational Causal Discovery | 2pEqXce0um.md | 4.50 | 1 | Causal root cause analysis; weaker contribution |
| Contextual Bandits with Graph Feedback | fcl6WeMARK.md | 4.33 | 1 | Graph feedback bandits; different setting, weaker |
| Sparse Causal Model | fSxiromxAq.md | 3.00 | 1 | Causal discovery on sparse data; much weaker |
| Test-Time Learning of Causal Structure | ZXs3pkmrRG.md | 5.50 | 2 | Causal structure learning from interventional data; comparable novelty level |
| Causal Graph Recovery via Homologous Surrogates | fGhr39bqZa.md | 6.00 | 2 | Causal discovery with latent variables; similar quality level |
| Deriving Causal Order from Single-Variable Interventions | u63OVngeSp.md | 7.00 | 2 | Causal order derivation; stronger experiments, comparable theory |
| Efficient Causal Discovery with Latent Variables | BZYIEw4mcY.md | 6.00 | 2 | Causal discovery with complex latent relations; comparable |
| Robust Agents Learn Causal World Models | pOoKI3ouv1.md | 5.75 | 2 | Causal models for robust agents; different angle |
| Independent-Set Design for Network Interference | w50MQ9Vfty.md | 5.50 | 2 | Experimental design for causal inference; weaker contribution |

**Round 1 bracket**: 5.0–7.0, anchored by causal bandit papers at the low end and causal theory papers at the high end.
**Round 2 narrowing**: The paper has cleaner theory than the 6.0 anchors but weaker experiments than the 7.0 anchor. Final position: 6.5 — above the 6.0 anchors due to the elegance and completeness of the theoretical contribution, but below 7.0 due to limited empirical validation.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>