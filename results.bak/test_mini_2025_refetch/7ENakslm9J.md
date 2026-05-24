## Summary

This paper studies bandit learning in two-sided matching markets where participants may have indifferent (tied) preferences — a relaxation of the strict-preference assumption that all prior work relies on. The authors propose the AE-AGS algorithm, which uses an arm-guided Gale-Shapley subroutine with adaptive exploration, and prove an \(O(NK \log T / \Delta^2)\) stable regret bound in both centralized and decentralized settings. The key design insight — letting players only explore arms that propose to them, eliminating suboptimal arms via confidence bounds without ever needing an explicit explore-versus-exploit decision — cleanly sidesteps the infinite-exploration deadlock that prior explore-then-exploit methods encounter under indifference.

## Strengths

- **First polynomial-regret guarantee for matching markets with indifferent preferences.** All prior work assumes strict preference rankings. The paper identifies the exact lemmas in six prior proofs (Table 1) that break under indifference, and shows that only AE-AGS achieves polynomial regret without requiring knowledge of the minimum gap \(\Delta\) or suffering exponential regret.

- **Clean algorithmic principle that avoids the explore-then-exploit dilemma.** By having players explore only among arms that propose to them, and using natural confidence-based elimination (Algorithm 3, Line 4), the algorithm never needs to decide "when to stop exploring." This is a genuine insight — under indifference, the state-of-the-art explore-then-GS methods (Zhang et al. 2022, Kong & Li 2023) would explore forever and incur linear regret.

- **The regret bound \(O(NK\log T / \Delta^2)\) matches the best known bound for the strict-preference case.** The table of comparisons (Table 1) clearly shows this, along with detailed annotations of exactly which lemmas fail under indifference for each prior work. This transparent failure analysis is valuable to the community.

- **Unified treatment of centralized and decentralized settings.** Both achieve the same regret order. The decentralized version introduces an index-estimation phase and a communication protocol whose cost is independent of \(T\).

- **Zero-regret guarantee when \(\Delta = 0\) in the centralized setting** (Theorem 4.1). This is a natural but non-trivial consequence of the algorithm design that no prior work provides.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Claim that communication costs "only a constant number of time slots" is imprecise.** Line 307 states this, but the communication protocol (Algorithm 5) can require up to \(O(NK^2)\) rounds in the worst case (each of the \(N\) players transmitting up to \(O(K^2)\) preference comparisons). While this cost is independent of \(T\) and therefore does not affect the leading regret term, it is not a literal constant — it scales with problem size. The paper should characterize the overhead as \(O(NK^2)\) or simply state that it does not affect the regret order rather than calling it constant.

2. **No proof sketch in the main text.** Theorem 4.1 states the regret bound, and the reader is told "the detailed proof is deferred to Appendix B" (line 202), but the main body offers no high-level intuition for why the arm-guided GS avoids the \(O(T)\) regret pitfall or how the elimination argument works. A short proof sketch would significantly improve accessibility.

3. **Experiments are entirely deferred to Appendix E** (line 204). The abstract claims "Extensive experiments demonstrate the algorithm's effectiveness," but the main text contains zero experimental results — not even a summary figure or table. While the theoretical contribution stands on its own, this disconnect between the empirical claim in the abstract and the content of the main text should be resolved by either including a brief summary in the main body or tempering the language.

### Trivial
None.

## Nice-to-Haves

- A concrete bound on communication regret in the main text (e.g., "total communication cost across all phases is at most \(O(NK^2)\) time slots") would make the \(O(NK\log T / \Delta^2)\) claim more precise.
- The decentralized algorithm could benefit from a short example illustrating one communication round (as currently Algorithm 5 is complex to parse).
- A brief justification of the \(\Delta = 0\) claim (centralized setting) would help avoid reader confusion.

## Removed Points
- **Experimental validation absent and cannot be assessed** (Harsh Critic, Critical Issue 1): This is a fair point in spirit, but the experiments exist in the original submission (Appendix E) and were stripped by the parser. The paper's core contribution is theoretical; the lack of experimental figures in the main text is a presentation flaw, not a scientific flaw. Moved to Minor weakness 3 with appropriate framing.
- **The critic's claim that communication overhead could be O(N²K²)**: This is factually wrong. In Algorithm 5, players transmit sequentially — each updating player takes 2·|Update_Pairs_i| + 1 rounds, so total overhead is O(NK²), not O(N²K²). The underlying point about imprecise wording is retained as Minor weakness 1.
- **Criticism about missing proof details (appendix)**: The paper explicitly defers proofs to appendices B and C due to space limits. This is standard for NeurIPS. The lack of a proof *sketch* in the main text is a separate point, retained as Minor weakness 2.
- **Strength Finder's generic strengths** ("this paper addresses an important problem," "this paper targets an interesting question"): These are too generic to be informative and have been removed.

## Novel Insights

The reviews do not surface any genuinely novel observation beyond the paper's own contributions. The harsh critic's identification that the communication-cost claim is imprecise is a useful editing note but not a scientific insight. The core value of the paper — that adaptive exploration via arm-guided GS naturally handles indifference without prior knowledge of \(\Delta\) — is already articulated clearly by the authors.

## Suggestions

1. Replace the phrase "only costs a constant number of time slots" (line 307) with a bound such as "costs at most \(O(NK^2)\) time slots, which does not affect the leading regret term."
2. Add a brief proof-sketch paragraph after Theorem 4.1 explaining the two key ideas: (a) why the arm-guided GS ensures that exploring among proposing arms never incurs regret for ties, and (b) how the confidence-based elimination argument yields the \(\log T / \Delta^2\) factor.
3. Either include a small experimental summary figure in the main text (even if full details remain in the appendix) or qualify the abstract's "extensive experiments" claim.

## Score and Decision

### Calibration Anchors

**Round 1 (bracketing):**
| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| `iKLSISIPH7` (Stochastic Matching Bandits) | 4.80 | R1 | Clearly weaker — criticized as "trivial extension," low novelty. Current paper solves a harder problem with a more novel algorithm. |
| `liSixK3eY4` (Combinatorial Online Prediction) | 4.75 | R1 | Weaker — mixed reviews, mediocre regret. Current paper is stronger in both problem framing and results. |
| `lsxeNvYqCj` (Strategic Click-Bandit) | 7.00 | R1 | Comparable — accepted as spotlight. Both papers have clear motivation, novel formulation, and solid theory. Current paper is slightly weaker in presentation polish. |
| `zDJNUDprhW` (Monotone Games) | 4.25 | R1 | Weaker — mediocre reception. Current paper is significantly stronger. |
| `cc8h3I3V4E` (Nash Equilibrium via Optimization) | 8.00 | R1 | Stronger — oral-level paper with very clean theory. Current paper is not at this level. |
| `7XXineVQeU` (MIPS via Bandits) | 2.00 | R1 | Much weaker. |

**Round 2 (narrowing within bracket [4.5, 7.5]):**
| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| `iKLSISIPH7` (Stochastic Matching Bandits) | 4.80 | R2 | See above. Paper under review is clearly stronger. |
| `liSixK3eY4` (Combinatorial Online Prediction) | 4.75 | R2 | See above. |
| `p1HeFnn2AA` (Deep Learning for 2-Sided Matching) | 7.33 | R2 | Rejected despite high scores (6,8,8) due to scalability and data concerns. Different area; hard to compare directly. |
| `oQKKlzxV1o` (Online Info Acquisition) | 6.75 | R2 | Comparable quality — both accepted-poster-level with solid theory and clear gap identification. |
| `iOAcVOHvEN` (Imperfect Info Games) | 6.00 | R2 | Slightly weaker — mixed reception (5,6,8,5), rejected. Current paper is more coherent. |

**Bracket**: After Round 1, the paper clearly sits in the [4.5, 7.5] range.

**Narrowing**: After Round 2, comparing against the matching bandits paper (4.80), the current paper is notably stronger (more novel problem, cleaner solution). Comparing against the info acquisition paper (6.75) and the strategic click-bandit paper (7.00), the current paper is comparable in contribution quality but slightly less polished in presentation (experiments in appendix only, imprecise communication cost claim). Hence it sits between these anchors.

**Final score**: 6.5 — a solid paper with a well-motivated contribution, clean theoretical results, and no fatal flaws. The presentation issues (imprecise wording on communication cost, no proof sketch, experiments not in main text) are real but minor relative to the strength of the theoretical contribution.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>