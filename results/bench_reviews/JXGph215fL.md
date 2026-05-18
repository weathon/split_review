Here is my final consolidated review.

---

## Summary

This paper introduces the "update-equivalence framework" for decision-time planning (DTP) in imperfect-information games, wherein DTP algorithms are viewed as replicating the updates of last-iterate learning algorithms rather than solving subgames. From this framework, the authors derive Mirror Descent Search (MDS) for cooperative games—proving a monotonic improvement guarantee under mirror descent—and Magnetic Mirror Descent Search (MMDS) for adversarial games. Empirically, MDS matches or exceeds PBS-based methods in Hanabi while using significantly less search time, and MMDS reduces exploitability in small 2p0s games with minimal public information.

## Strengths

- **Novel conceptual framework.** The update-equivalence perspective cleanly unifies existing DTP methods (Monte Carlo search, piKL, policy gradient search) under a single lens and provides a principled recipe for deriving new algorithms from last-iterate methods. This is a genuinely useful abstraction that shifts thinking away from the complexity of public-belief-state subgame solving.

- **Strong empirical result in 7-card Hanabi.** MDS achieves 24.28 ± 0.02 in the harder 7-card variant, outperforming the best PBS-based methods (multi-agent RLSearch with BFT at 24.18 ± 0.03) despite using only approximate beliefs (Seq2Seq) and no validation checks. This is the first demonstrated case of a non-PBS-based method outperforming PBS methods in a domain they have historically dominated. The performance gap widens with more non-public information, consistent with the paper's scalability motivation.

- **Controlled comparison with same blueprint.** In the 5-card Hanabi setting, MDS (PPO blueprint, 24.62 ± 0.02) is compared against single-agent SPARTA with the same PPO blueprint and Seq2Seq belief model (24.52 ± 0.02), providing a cleaner algorithmic comparison that partially mitigates confounding from blueprint differences.

- **Algorithmic simplicity.** MDS and MMDS are straightforward to implement: basic rollouts + a multiplicative weight (hedge) update, with no expensive validation checks needed. This contrasts favorably with the complexity of PBS subgame solving.

## Weaknesses

### Fatal
None.

### Major

- **The improvement guarantee (Theorem 1) is proven for simultaneous updates at *all* decision points, but MDS only updates a *single* decision point (the current one).** Theorem 1 states that if mirror descent is applied at *every* decision point simultaneously, the joint policy improves. MDS, however, applies Algorithm 1 at only the current decision point, keeping all other decision points' policies fixed. The paper asserts (line 168) that MDS "inherits the improvement property of Theorem 1" via Proposition 1, but Proposition 1 only establishes that the empirical action-value estimates converge to the true mirror descent update locally. No theorem or argument bridges the gap between local (one-decision-point) mirror descent and global joint-policy improvement. This is a real disconnect between the theoretical apparatus and the implemented algorithm. The central claim of a "provably sound search algorithm" is overstated relative to what is actually proven.

- **MMDS experiments do not demonstrate scalability to regimes where PBS methods fail.** The paper motivates the framework by arguing that PBS methods are "ineffective in settings with large amounts of non-public information." However, MMDS is only tested on 3x3 Abrupt Dark Hex and Phantom Tic-Tac-Toe — games with tiny state spaces where PBS methods would be easily applicable. The paper provides no experiment on larger boards, richer private information, or any setting where PBS methods are computationally prohibitive. The scalability claim for MMDS remains an untested hypothesis.

### Minor

- **The "two orders of magnitude" speed comparison is selective.** The claim is factually accurate when comparing against multi-agent PBS methods (2s vs 180–450s). However, single-agent SPARTA (1s) and single-agent RLSearch (35s) are substantially closer in runtime. The paper's framing ("two orders of magnitude less search time") is repeatedly stated without qualification in the abstract and introduction, potentially misleading readers about the comparison class.

- **Argmax implementation breaks update-equivalence.** The Hanabi implementation plays the argmax of the mirror descent update rather than sampling from it (acknowledged in footnote, line 219). The theoretical improvement guarantee is for the sampled distribution; playing the argmax breaks the update-equivalence link. The paper notes this discrepancy but does not discuss its implications for the theory.

- **MMDS has no formal safety guarantee.** For adversarial games, the paper states (line 180) that "if the observation of MMD's reliable last-iterate convergence to equilibrium holds, then MMDS leads to expected improvement." This is conditional on an empirical observation from a different setting (simultaneous-move matrix games), and there is no argument that local DTP updates cannot increase exploitability. The paper should more clearly acknowledge this gap relative to PBS methods which have formal safety guarantees.

### Trivial
None.

## Nice-to-Haves

- Adding a scalability experiment for MMDS on a larger game (e.g., a more complex variant of Dark Hex or a game where PBS methods are known to be costly) would substantially strengthen the empirical case.
- A discussion of the relationship between the local mirror descent update and global improvement (or a corrected theorem that addresses the gap) would resolve the central theoretical concern.

## Removed Points

These points are flagged to be removed; treat them with caution:
- The harsh critic's claim that "the Hanabi comparison is confounded by different blueprints" when there is no controlled comparison: the paper *does* include a controlled comparison (MDS vs SPARTA with the same PPO blueprint and Seq2Seq belief model in Table 1). This removes the edge of the criticism.
- The harsh critic's claim that "the argmax discrepancy is not discussed": the paper explicitly notes this difference with a footnote (line 219). However, the *implications* are not discussed, which is a valid minor point retained above.
- The harsh critic's claim that "the paper does not provide any experiment in a regime where PBS methods actually fail": this overreaches — the 7-card Hanabi variant *is* a regime where multi-agent SPARTA is inapplicable and PBS methods rely on approximate beliefs. The retained criticism is about MMDS specifically, not MDS.
- The Strength Finder's claim #2 that MDS has a "provable monotonic improvement guarantee" that directly applies — this conflicts with the verified weakness about the theory gap and is weakened accordingly in the strengths section above.

## Novel Insights

Beyond the paper's own contributions, the most striking takeaway from the reviews is that the update-equivalence framework reveals a fundamental tension in DTP theory: proving global improvement from *local* search-time updates is nontrivial even for simple algorithms like mirror descent. This suggests that the field may need to develop new analytical tools — perhaps leveraging the performance difference lemma with careful handling of occupancy-measure shifts — before the theory can fully catch up with empirically successful DTP methods. The paper's honest reporting of this gap (even if unintentionally, via the mismatch between Theorem 1's premise and Algorithm 1's operation) highlights an important open problem.

## Suggestions

1. **Fix the theoretical gap.** Either (a) prove that a single-decision-point mirror descent update improves the joint policy in common-payoff games (possibly using the performance difference lemma), or (b) honestly reframe the contribution as an empirical demonstration without claiming provable soundness. Option (a) is strongly preferred if feasible.
2. **Emphasize the controlled comparison more.** The MDS vs SPARTA comparison with the same PPO blueprint and Seq2Seq belief model (Table 1, right columns) is the fairest algorithmic comparison; give it more prominence in the narrative.
3. **Add a larger-scale MMDS experiment.** Even a modest step up in game size (e.g., 5x5 Dark Hex) would significantly strengthen the scalability claim.
4. **Discuss the argmax implication.** Explain whether the improvement guarantee extends to the argmax-played version or whether this is a heuristic departure from theory.

## Score and Decision

**Score calibration against anchors (retrieved from `/home/wg25r/split_review/datasets/deepreview_13k_calibration`):**

| Anchor | Avg Score | Comparison |
|--------|-----------|------------|
| `6PbvbLyqT6` (DDCFR) | 8.0 | Stronger theory, well-matched to algorithm; the current paper has a clearer conceptual contribution but weaker theory. |
| `stUKwWBuBm` (Tractable MARL) | 8.0 | Strong theory with limited toy experiments; the current paper has stronger empirical results but weaker theory. |
| `5qg1sAXhoh` (Tree Search SM Games) | 4.75 | Unclear algorithm description and missing baselines; the current paper is better-written and has clearer contributions. |
| `85Ik12q2hP` (ReAct Critique) | 4.0 | Primarily a negative result with limited novelty; the current paper has more positive contributions. |
| `w5pErXbwQl` (Noise-Robust Preference Losses) | 3.0 | Limited relevance; the current paper is substantially stronger. |

Relative to these anchors, the paper sits above papers scoring 3-5 but below papers scoring 7-8 due to a genuine theoretical gap and limited MMDS evaluation. It has a novel framework and strong Hanabi results, but the central theoretical claim is not fully supported.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>