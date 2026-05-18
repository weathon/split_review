I've now thoroughly verified all claims against the paper. Here is my consolidated review.

---

## Summary

This paper proposes COEBL (Competitive Co-evolutionary Bandit Learning), an algorithm that integrates evolutionary algorithms (mutation + selection) into the bandit learning framework for two-player zero-sum matrix games with bandit feedback. The authors provide a regret analysis showing that COEBL achieves $\tilde{O}(\sqrt{m^2 T})$ sublinear regret (Theorem 2), matching the UCB bound of O'Donoghue et al. (2021), and present empirical results across RPS, DIAGONAL, and BIGGERNUMBER games where COEBL outperforms EXP3, UCB, and EXP3-IX baselines.

## Strengths

- **First regret analysis of an evolutionary bandit learning algorithm in matrix games.** The paper provides a rigorous sublinear regret bound ($\tilde{O}(\sqrt{m^2 T})$) for COEBL (Theorem 2), which is genuinely novel — no prior work has analysed evolutionary algorithms for regret in this bandit-game setting. The proof sketch (Section 3.2) and Lemma 1 provide a plausible path from the mutation operator's randomness to a bound on cumulative regret.

- **Consistent empirical outperformance across multiple game benchmarks with varying complexity.** In head-to-head comparisons (ALG 1-vs-ALG 2), COEBL achieves lower regret than EXP3, UCB, and EXP3-IX on the RPS game (Figure 2), DIAGONAL game for $n=2$ through $7$ (Figure 4), and BIGGERNUMBER game (Figure 6). On DIAGONAL, COEBL's regret remains beneath the theoretical bound of $0.1\sqrt{K^2 T}$ (Figure 3) while baselines show substantially larger regret. The empirical evaluation covers games with exponentially growing action spaces (up to $2^7 = 128$ pure strategies), and results are reported with 95% confidence intervals over 50 seeds.

- **Clear algorithmic design integrating evolutionary operators with the OFU principle.** The mutation operator (Eq. 2) scales its Gaussian perturbation inversely with visit counts, creating a form of randomised optimism. The selection mechanism (Fitness function = minimax value under the optimistic matrix) provides a principled way to accept or reject mutated policies. This design is well-motivated and clearly described.

- **Thorough evaluation with multiple metrics.** The paper evaluates both regret and convergence to Nash equilibrium (KL-divergence or total variation distance) across two scenarios (self-play and competitive), providing a well-rounded empirical picture.

## Weaknesses

### Fatal
None.

### Major

- **The paper's framing overstates the novelty of "randomised optimism" by implying it is an open question.** The abstract states: "it remains an open question whether randomised optimism can also exhibit sublinear regret." However, the paper's own related work (Section 1.4.1, line 51) acknowledges that O'Donoghue et al. (2021) "conducted a detailed regret analysis on the UCB algorithm, **Thompson Sampling**, and K-Learning" and "showed sublinear regret bounds for these existing bandit baselines in matrix games." Thompson Sampling is a *randomised* optimism method, so the claim that randomised optimism's sublinear regret was an open question is factually incorrect. The paper's genuine contribution — an *evolutionary* bandit algorithm — does not require this false dichotomy. This framing erodes trust and should be corrected to accurately position the work as the first analysis of *evolutionary* randomised optimism, not randomised optimism per se.

- **Thompson Sampling is acknowledged but omitted from empirical comparisons.** Given the paper's repeated emphasis on contrasting "deterministic optimism" with "randomised optimism via evolution," the omission of Thompson Sampling — the most natural randomised optimism baseline — from the empirical evaluation (Figures 1–6) undermines the claim that "COEBL outperforms existing methods." Without this comparison, the reader cannot tell whether COEBL offers any advantage over an existing randomised method with known theoretical guarantees, or whether the empirical gains are only relative to deterministic UCB and the EXP3 family. This does not invalidate the paper's core contribution but substantially weakens its empirical conclusions.

### Minor

- **Assumption (A) is referenced in Lemma 1 and Theorem 2 but never explicitly defined or labeled in the text.** The text preceding Lemma 1 (line 137) says "We follow the setting in O'Donoghue et al. (2021) and consider the case where there is 1-subGaussian noise when querying the payoff matrix." This appears to be Assumption (A), but it is never labeled as such (no "**Assumption (A)**" heading or callout). This makes Lemma 1 needlessly hard to parse. The authors should add an explicit "Assumption (A)" label.

- **The proof sketch in Section 3.2 is very brief (three sentences).** While the full proof is deferred to the appendix (which was stripped by the parser), the sketch could be more informative. For instance, it does not explain how the fitness comparison (Lines 7–10 of Algorithm 1) interacts with the optimism guarantee, or how the regret decomposition connects the mutation operator's randomness to the actual payoff sequence. Adding 2–3 sentences to bridge these gaps would make the theoretical claim more self-contained and credible in the main text.

- **Algorithm 1 omits the explicit action-selection step.** The algorithm updates policy $x_t$ but never explicitly states how actions $i_t$ (for the row player) are chosen in each round. By standard bandit convention, actions are sampled from the policy ($i_t \sim x_t$), and the regret definition (Definition 3) assumes the algorithm maps to a distribution over actions. However, explicitly adding "Sample $i_t \sim x_t$" to the pseudocode would improve clarity and prevent confusion.

- **The mutation formula's denominator notation is ambiguous.** The mean term contains $\sqrt{c\log(2T^2 m^2) / (1\vee n_{ij}^t+1)}$ — it is unclear whether this is $(1\vee n_{ij}^t)+1$ or $1\vee(n_{ij}^t+1)$. While standard operator precedence suggests the former, a clarifying parenthesis would help. The variance term scales as $1/(1\vee n_{ij}^t)^2$, so the mean and variance have different scaling with $n$, which warrants a brief justification.

### Trivial
None.

## Nice-to-Haves

- An ablation study on the mutation rate $c$ across multiple games would empirically validate the paper's theoretical threshold ($c \geq 8$) and the authors' conjecture that smaller $c$ values may also work.

- Adding Thompson Sampling as a baseline in the empirical evaluation (or at minimum, an explanation for its omission if a direct comparison is technically infeasible).

- Clarifying how $n_{ij}^t$ and $\bar{A}_{ij}^t$ are initialized when $n_{ij}^t = 0$ (presumably $\bar{A}_{ij}^t = 0$ or a prior), which is standard but should be stated explicitly.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"c=2 parameter choice for RPS is unexplained"** — The paper explicitly addresses this at lines 149 and 174: "The current results considers $c\geq8$ in the analysis due to current technical limitations. We conjecture that the regret bound can be improved by considering smaller $c$ values, and thus, in practical use, we suggest one may need hyperparameter tuning in various problems." The authors transparently note the gap between theory and practice; the criticism is factually incorrect.

- **"The regret analysis is not adequately presented because the proof is in the appendix which is stripped"** — Per instructions, appendix stripping is a parser artifact. The proof exists in the original submission. The sketch brevity concern is retained above as minor.

- **"Action selection missing is a critical/fatal flaw"** — The action selection step is standard convention in bandit learning (the algorithm outputs a policy, actions are sampled from it). The paper states in Section 2.1 that "the row player chooses $i_t\in[m]$" and Definition 3 defines the algorithm as mapping to a distribution over actions. The absence of an explicit sampling line in the pseudocode is a minor clarity issue, not a fatal flaw. Retained above as minor.

- **"The mutation operator's formula looks off" (as a substantive weakness)** — The reviewer acknowledges "this may be correct." The notation ambiguity is a minor clarification issue, retained above as minor.

## Novel Insights

None beyond the paper's own contributions. The reviews largely corroborate the paper's claims (first regret analysis of evolutionary bandit learning, strong empirical performance) while correctly identifying a framing inconsistency. The most useful diagnostic insight is that the paper's contribution — an evolutionary algorithm with a specific mutation operator — is stronger and more defensible than its own framing suggests, and the abstract should be rewritten to accurately claim "first evolutionary bandit algorithm with regret analysis" rather than overreaching on "randomised optimism."

## Suggestions

1. **Correct the framing in the abstract and introduction.** Replace "it remains an open question whether randomised optimism can also exhibit sublinear regret" with accurate language acknowledging that Thompson Sampling already provides sublinear regret for randomised methods in this setting, and reframe the contribution as the *first evolutionary* bandit learning algorithm with regret analysis.

2. **Add Thompson Sampling as an empirical baseline** or, if infeasible, provide a detailed discussion comparing COEBL's mechanism and expected behaviour against Thompson Sampling.

3. **Explicitly label Assumption (A)** in Section 2 or Section 3, and add a brief statement of what it entails.

4. **Add an explicit action-sampling step** to Algorithm 1 (e.g., "Sample $i_t \sim x_t$"), and clarify whose actions are used to update $n_{ij}^t$ in Line 12.

5. **Expand the proof sketch** in Section 3.2 to show how the fitness comparison (the selection mechanism) interacts with the optimism guarantee, and how the regret decomposition follows from the law of total probability and Lemma 1.

## Score and Decision

This paper presents a genuine contribution — the first regret analysis of an evolutionary bandit algorithm in matrix games — supported by a theoretical bound and convincing empirical results across games with varying complexity. The main weaknesses are a flawed framing that overclaims novelty about "randomised optimism" (contradicted by the paper's own related work section) and the omission of Thompson Sampling from the empirical comparisons. These are significant but addressable: they do not invalidate the core technical contribution. The paper is likely to become a solid publication after correcting the framing and adding the missing baseline.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>