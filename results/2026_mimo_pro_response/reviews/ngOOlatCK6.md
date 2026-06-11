Now I have enough information to finalize the review. Let me synthesize everything.

**Round 1 bracket:** Based on the anchors, the paper sits between 5.5 and 8.0. It's clearly above the rejected causal bandits papers (IPayPEGwdE at 5.00) and comparable to accepted papers in the 6.0-7.5 range (YcW8i9VCf5 at 6.0, u63OVngeSp at 7.0). It doesn't reach the level of the strongest anchors (xByvdb3DCm at 8.0).

**Round 2 narrowing:** Comparing directly to u63OVngeSp (7.00, "Deriving Causal Order from Single-Variable Interventions"), our paper has a more complete theoretical characterization (full mGISS vs. approximation guarantees), a proven linear-time algorithm, comparable experiments, and one notable weakness (missing random-pruning ablation). These factors roughly balance out.

**Final score: 7.0** — A solid theoretical contribution with a clean, complete characterization, practical algorithm, and good (if not comprehensive) empirical validation. The missing ablation weakness is real but doesn't undermine the core theoretical contribution.

---

## Summary
This paper provides the first complete graphical characterization of the minimal globally interventionally superior set (mGISS) — the smallest set of nodes guaranteed to contain the optimal single-node conditional intervention in a causal graph. The central result (Theorem 13) proves the mGISS equals the LSCA closure of Pa(Y), computable in O(|V|+|E|) time via the C4 algorithm. Experiments on random and real-world graphs demonstrate substantial search space reduction (90%+ for large models), and integration with a UCB-based bandit algorithm shows improved convergence.

## Strengths
- **First complete characterization of mGISS for non-hard interventions**: Theorem 13 proves the LSCA closure of Pa(Y) equals the mGISS, filling a genuine gap — prior work (Lee & Bareinboim 2018) only addressed multi-node hard interventions. The result is novel for both conditional interventions and single-node interventions of any kind, as explicitly claimed and substantiated in Section 1.
- **Surprising theoretical equivalence (Proposition 4)**: The equivalence between conditional-intervention superiority and deterministic atomic-intervention superiority is non-obvious and powerful — it allows all proofs to use the simpler deterministic atomic framework while obtaining guarantees for the general conditional case. This is the key enabling result.
- **Linear-time algorithm with provable correctness**: The C4 algorithm (Algorithm 1, Theorem 16) computes the mGISS in O(|V|+|E|) time using the novel "connector" concept (Definition 14, Lemma 15). This is optimal since it requires reading the graph at least once.
- **Substantial empirical search space reduction**: Random graph experiments (Section 6) show 17% retention for 500-node graphs with expected degree 2; real-world bnlearn graphs show 90%+ reduction for large models. Results are systematically reported across multiple graph sizes and densities.
- **Clean modular design**: C4 is a pure preprocessing step agnostic to the downstream bandit algorithm (Section 7, lines 309-313), making it broadly applicable as a component for any future conditional bandit algorithm.

## Weaknesses

### Fatal
None

### Major
- **Missing random-pruning ablation in bandit experiment**: The bandit experiment (Section 6, Figure 3) compares CondIntUCB using all ancestor nodes (brute-force) vs. only mGISS nodes. Since UCB with fewer arms naturally converges faster, this comparison cannot distinguish "mGISS is smart pruning" from "any pruning helps UCB." The meaningful comparison is mGISS vs. random subsets of the same cardinality from An(Y). Without this baseline, the claim that mGISS specifically (rather than any reduction) improves convergence is not fully supported. The theoretical contribution stands regardless — the mGISS is provably optimal — but this weakens the empirical narrative.

### Minor
- **Limited scope of bandit experiment**: Only 4 small bnlearn datasets (8–109 nodes) and a single MAB algorithm (CondIntUCB) are used. The paper explains dataset selection (footnotes 8, 12), but testing with a second bandit algorithm would demonstrate algorithm-agnosticism, and broader datasets would strengthen generalizability.
- **Non-standard regret definition**: Footnote 11 defines cumulative regret using "the estimated best arm" rather than the standard definition using the true optimal arm. This pragmatic choice is acknowledged but not justified — a brief discussion of why standard regret was not used would improve clarity.

### Trivial
None

## Nice-to-Haves
- Reporting wall-clock computation times on real-world graphs would give practitioners a concrete sense of C4's overhead.
- A brief discussion of how mGISS size varies with different target node Y choices (not just the node with most ancestors) would strengthen generality.

## Removed Points
These points are flagged to be removed, treat them with caution.
- None removed — all reviewer criticisms were either kept or already addressed by the paper.

## Novel Insights
The paper's most novel insight is the equivalence between conditional-intervention superiority and deterministic atomic-intervention superiority (Proposition 4). This is surprising because conditional interventions involve policies over conditioning sets while deterministic atomic interventions operate on fixed noise realizations — the two frameworks seem fundamentally different, yet they yield identical superiority orderings. This equivalence is the key enabling result that makes the entire graphical characterization tractable.

## Suggestions
- Add a random-pruning ablation: run CondIntUCB with random subsets of An(Y) of the same cardinality as the mGISS, averaged over many random subsets, to decompose convergence improvement into "fewer arms" vs. "smart pruning" effects.
- Briefly acknowledge the "fewer arms" effect in the bandit experiment discussion, positioning the mGISS contribution as guaranteeing the optimal arm survives (a safety property) in addition to any convergence benefit.

## Calibration Anchors Retrieved

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| Uj0h13lVrR | 1.00 | 1 | GFlowNet paper, completely different, score not comparable |
| bEgDEyy2Yk | 1.00 | 1 | Implementation paper, irrelevant |
| MVpvyeVeyI | 3.40 | 1 | Causal BO with unknown graphs — rejected, our paper has cleaner theory |
| fSxiromxAq | 3.00 | 1 | Sparse causal model — rejected, our paper is much stronger |
| IPayPEGwdE | 5.00 | 1 | Causal contextual bandits — rejected, comparable topic but weaker theory, all 5s |
| YcW8i9VCf5 | 6.00 | 1 | Adversarial CBO — accepted, all 6s, comparable but our theory is more complete |
| xByvdb3DCm | 8.00 | 1 | Selection meets intervention — accepted, all 8s, stronger novelty |
| u63OVngeSp | 7.00 | 2 | Causal order from interventions — accepted, 5/8/8/6/8, most comparable anchor |
| BZYIEw4mcY | 6.00 | 2 | Causal discovery with latent vars — accepted, all 6s |
| l11DZY5Nxu | 6.50 | 2 | Robust root cause diagnosis — accepted, 6/6/6/8 |

**Round 1 bracket:** 5.5–8.0. Our paper is clearly above the rejected causal bandits papers (5.0) and comparable to accepted papers in the 6.0–7.5 range.

**Round 2 narrowing:** Direct comparison to u63OVngeSp (7.00) — our paper has cleaner, more complete theory and a proven linear-time algorithm, but has the missing ablation weakness. Net: comparable to 7.0.

**Final score: 7.0** — Solid theoretical contribution with clean characterization, practical algorithm, and adequate empirical validation. The missing ablation weakness is notable but fixable and does not undermine the core contribution.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>