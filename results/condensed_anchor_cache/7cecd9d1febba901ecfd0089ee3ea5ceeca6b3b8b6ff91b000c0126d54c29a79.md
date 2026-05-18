- Decision: Reject
- Scores: 5, 8, 6, 5

## Merged Review

### Summary
This paper studies learning approximate Nash equilibria (NE) in two-player zero-sum imperfect-information extensive-form games (IIEFGs) under the bandit feedback setting. The proposed algorithm uses a negentropy regularizer weighted by a virtual transition over the information-set–action space. The authors prove that when both players follow the algorithm, their last-iterate strategies converge to the NE at a rate of \(\widetilde{O}(k^{-1/8})\) with high probability and \(O(k^{-1/6})\) in expectation. A lower bound of \(\Omega(k^{-1/2})\) is also established. The algorithm is fully uncoupled between the two players.

### Strengths
- **First finite-time last-iterate convergence under bandit feedback.** This is the first algorithm achieving polynomial-time last-iterate convergence for approximate NE in IIEFGs with bandit feedback (all reviewers).
- **Concrete theoretical guarantees.** The paper provides explicit rates: \(\widetilde{O}(k^{-1/8})\) high-probability and \(O(k^{-1/6})\) in expectation, along with a lower bound of \(\Omega(k^{-1/2})\) (Reviewers 2, 4).
- **Significance and rigor.** The theoretical results are of vital importance for the literature and serve as an important step toward improving last-iterate convergence guarantees. The proofs appear rigorous and well-structured (Reviewer 2).
- **Writing and exposition.** The paper is well-written, smoothly flowing, and provides a good introduction of background and motivation (Reviewers 2, 3).
- **Novelty of the virtual transition.** The introduction of the virtual transition technique adapts entropy regularization from normal-form games to extensive-form games in a novel way (Reviewers 1, 3).
- **Fully uncoupled property.** The algorithm does not require communication between players (Reviewer 2).

**Minority contrast:** Reviewer 2 is notably more positive, emphasizing the importance and rigor of the results; other reviewers are more reserved but still acknowledge these strengths.

### Weaknesses
- **Missing empirical validation.** No experiments are provided. The paper would benefit from simulations on example games (e.g., Kuhn Poker, Leduc Poker) to demonstrate convergence, runtime, and sensitivity to game parameters (Reviewers 2, 3, 4). Without experiments, it is difficult to assess practical relevance or compare with existing algorithms (Reviewer 3).
- **Unclear necessity and intuition of virtual transition.** The need for the virtual transition is not convincingly justified. It appears to stem from low-level proof difficulties rather than a high-level algorithmic requirement (Reviewer 1). The connection to the sequence-form representation (Eq. (5)) seems contradictory, and the justification via Pinsker’s inequality is not entirely persuasive (Reviewer 2). A more intuitive explanation is needed.
- **Dependence on prior knowledge of infoset structure.** The virtual transition requires knowledge of the game’s information-set structure, which is a limitation compared to methods that only use visited infosets (e.g., Kozuno et al.) (Reviewer 1).
- **Obscure analysis of previous regularizers.** The explanation of why a vanilla negentropy regularizer is difficult to use for controlling the NE gap is unclear. The claim that bounding the stability term of OMD with dilated negentropy critically relies on its closed-form update is confusing; Eq. (2) does not have a closed-form solution provided (Reviewer 4). Simple examples illustrating these limitations would help (Reviewer 4).
- **Benefits of the proposed regularizer are not clearly articulated.** It is unclear how the negentropy weighted by the virtual transition specifically contributes to the convergence results (Reviewer 4). Moreover, Eq. (2) only yields an approximate solution, yet the analysis appears to rely on exact solvability (Reviewer 4).
- **Arbitrary constraint choice.** The constraint \(\mu(a_h \mid x_h) \ge \frac{1}{A(k+1)}\) seems somewhat arbitrary. A precise explanation of how this bound affects the convergence rate (beyond a multiplicative constant) and why constraining the feasible set does not prevent convergence is needed (Reviewer 2).
- **Computational complexity not discussed.** The paper does not analyze the computational cost of solving Eq. (2) or the overall cost of Algorithms 1 and 2 (Reviewers 3, 4).
- **Straightforward extension from normal-form games.** The work is described as a largely straightforward extension of Cai et al. (2023) to the extensive-form setting, limiting the core technical novelty (Reviewer 1; this is a minority view).
- **No discussion of adaptive virtual transition.** The virtual transition is fixed a priori; whether it could be made adaptive using historical bandit feedback to further improve the convergence rate is not explored (Reviewer 2).
- **Minor typo.** Line 101 contains a doubled “to” (Reviewer 3).