Now I'll write the final consolidated review.

## Summary

This paper studies the minimal search space for single-node conditional-intervention causal bandits. It defines the minimal globally interventionally superior set (mGISS) — the smallest set of nodes guaranteed to contain the optimal conditional intervention — and characterizes it as the LSCA (Lowest Strict Common Ancestor) closure of Pa(Y). The paper provides the C4 algorithm that computes this set in O(|V|+|E|) time, and presents empirical results on random and real-world graphs showing substantial pruning of the search space, as well as bandit experiments showing improved cumulative regret.

## Strengths

1. **Rigorous graphical characterization of the minimal search space (Theorems 12 and 13):** The paper provides a complete, provably correct characterization of the mGISS as the LSCA closure of Pa(Y). This is a non-trivial extension beyond the hard-intervention setting of Lee & Bareinboim (2018), where the answer is simply Pa(Y). The Λ-structure characterization (Theorem 12) is elegant and provides geometric intuition for the closure. The proof that the mGISS is unique (Proposition 6) and the proof that the LSCA closure equals the mGISS (Theorem 13) form a tight theoretical package.

2. **C4 algorithm with O(|V|+|E|) complexity (Theorem 16):** The connector concept (Definition 14, Lemma 15) is clean and intuitive — a node is in the LSCA closure iff its connector is itself. The algorithm makes a single reverse-topological pass, giving linear time. This makes the method practical as a pre-processing step for any downstream bandit algorithm.

3. **Proposition 4 (equivalence of conditional and deterministic atomic superiority):** This theoretical bridge is what enables the analysis to be carried out in the simpler deterministic setting, where reasoning about atomic interventions is more tractable than reasoning about general policies over conditioning sets.

4. **Empirical demonstration of practical pruning on diverse graphs:** The search-space reduction experiments cover both random Erdős–Rényi graphs (e.g., 500-node with expected degree 2 retaining only 17% of ancestors) and a broad set of real-world bnlearn graphs (over 90% reduction for some large models). These results provide concrete evidence that the theoretical pruning translates to practice, especially on sparse graphs typical of real systems.

## Weaknesses

### Fatal
None.

### Major
- **Non-standard regret computation (Footnote 11).** The regret is computed using "the estimated best arm, defined as the arm that most runs concluded to be the best at the end of training." This is not standard: regret should be measured against the *true* optimal arm. In this setting, reward samples are generated from known SCMs/CPTs (as the experiments use bnlearn models), so the true optimal intervention could be pre-computed. Using a consensus of the algorithm's own outputs as the reference creates a circularity that weakens the quantitative claims about regret improvement. If the mGISS and brute-force algorithms converge to different nodes, the "most runs" criterion arbitrarily selects one as the "best," and the algorithm that includes that node will mechanically appear to have lower regret. This does not invalidate the paper's theoretical contributions, but it undermines the empirical claim that mGISS "improves" bandit performance in a quantitatively meaningfully way.

### Minor
- **Bandit experiments lack comparison against alternative pruning strategies of the same cardinality.** The experiments compare mGISS pruning against brute-force (all nodes). This only shows that having fewer arms helps convergence — it does not test whether the *specific* pruning induced by mGISS is better than any random subset of the same size. Since the theoretical result already guarantees mGISS retains the optimal node (which random pruning cannot guarantee), this comparison is not necessary for correctness, but would strengthen the empirical case that mGISS is specifically beneficial.

- **Search-space reduction results on random graphs reported without variance in the main text.** The paper reports single averages over 1000 random graphs (e.g., "17%, 29%, 62% and 77%") without standard deviations or confidence intervals, making it difficult to assess stability. Full results are in Appendix H (not viewable in the main text).

- **No proof sketch for Proposition 4 in the main text.** Proposition 4 is the linchpin equating conditional-intervention superiority to deterministic atomic-intervention superiority. These have different quantifier structures (∃g ∀h vs. ∀n ∃x), and the equivalence is non-trivial. Providing a brief intuitive justification or noting the key technical steps would help readers assess the central theoretical move without needing to access the appendix.

### Trivial
None.

## Nice-to-Haves
- A direct validation on synthetic SCMs with known ground truth, verifying that the optimal node always lies within the mGISS and measuring how often nodes outside the mGISS are suboptimal.
- Characterizing graph structures where the mGISS is much smaller than An(Y) versus those where it nearly equals An(Y).
- A worked example comparing mGISS against Lee & Bareinboim (2018)'s Pa(Y) result on the same graph to illustrate concretely why the single-node conditional setting generates a different (more complex) minimal set.

## Removed Points
These points were flagged by the reviewers but are removed after filtering:

- **"Bandit experiments do not validate the theoretical claim"** — The theoretical claim (Theorem 13) is a mathematical proof. The bandit experiments validate the *practical benefit* of pruning, not the theory itself. The harsh critic's framing that the experiments are "equally consistent with the hypothesis that any fixed-size subset would produce similar regret curves" is a valid concern about experimental design — moved to Minor weakness (lack of alternative pruning baseline).
- **"No error bars for bandit experiments"** — The paper explicitly states it reports standard deviations (line 291: "plot the two average cumulative regret curves along with their standard deviations").
- **"Paper does not specify how reward samples are simulated"** — The reproducibility statement (line 317) and submitted code repository address this.
- **"No comparison against closest prior work"** — The paper clearly explains the settings are non-comparable (lines 33-40). A comparison would be a nice-to-have, not a weakness.
- **Missing related works** — Cannot be externally verified.
- **Formatting/typo nitpicks** — Parser artifacts.
- **Generic strengths from Strength Finder** — e.g., "addressed an important problem" — removed as non-specific.

## Novel Insights
None beyond the paper's own contributions. The reviews converge on the same assessment: the theory (LSCA closure, C4 algorithm, Proposition 4) is the paper's genuine contribution and is solid, while the experiments have methodological weaknesses that need addressing. The most useful insight from the meta-review is identifying the non-standard regret computation as the most actionable concrete flaw.

## Suggestions
1. Replace the "estimated best arm" regret computation with regret computed against the *true* optimal arm. Since reward samples are generated from known bnlearn models, the true optimal conditional intervention can be pre-computed (or closely approximated) and used as the reference.
2. Add a bandit experiment comparing mGISS against random subsets of the same cardinality to show that mGISS's specific pruning is beneficial beyond mere arm-count reduction.
3. Report standard deviations or confidence intervals for the search-space-reduction percentages on random graphs in the main text.
4. Add a short intuitive justification for Proposition 4 in the main text — even 2-3 sentences explaining why the quantifier reversal is valid would help readers.

### Calibration Anchors

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| IPayPEGwdE.md (causal contextual bandits) | 5.0 | 1, 2 | Weaker theory, comparable experiments → our paper is stronger |
| MVpvyeVeyI.md (CBO unknown graphs) | 6.5 | 1 | Polarized reviews (3,5,8,10), our paper is more consistent |
| YcW8i9VCf5.md (adversarial CBO) | 6.0 | 2 | Most comparable: clean theory, experimental concerns, similar quality |
| pOoKI3ouv1.md (robust agents causal) | 5.75 | 2 | Purely theoretical, mixed reviews (1,6,8,8), our paper has experiments |
| w50MQ9Vfty.md (independent-set DOE) | 5.5 | 2 | More applied causal inference, our theory is cleaner |
| xByvdb3DCm.md (selection+intervention) | 8.0 | 1 | Stronger paper in all dimensions — our paper is clearly below this |

**Round 1 bracket**: 5.0–7.0  
**Round 2 narrowing**: Anchored near the Adversarial CBO paper (6.0) and CBO unknown graphs (6.5). Our paper's theory is cleaner than the former, but the regret computation issue holds it back.  
**Final score**: 6.0 — marginally above the acceptance threshold. The theoretical contribution (mGISS characterization, C4 algorithm) is strong and well-executed. The empirical evaluation has a genuine methodological flaw (non-standard regret computation) that prevents a higher score, but the search-space reduction results and the theoretical contributions justify acceptance pending reasonable revision.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>