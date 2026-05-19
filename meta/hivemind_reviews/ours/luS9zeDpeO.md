## Summary
This paper addresses decentralized safe multi-agent reinforcement learning (MARL) for homogeneous multi-agent systems with continuous action spaces. It formally characterizes homogeneous constrained Markov games, proves that policy sharing preserves optimality and safety (Theorem 1), proposes an on-policy decentralized primal-dual actor-critic algorithm with asymptotic convergence guarantees (Theorems 3–5), and develops a practical off-policy DRL variant. Experiments on three continuous multi-robot coordination tasks show the practical algorithm (DPDAC-ER) matches the safe centralized baseline (MASAC-Lag) while operating in a fully decentralized manner.

## Strengths
- **Theoretical justification of policy sharing for safe MARL (Theorem 1)**. The paper proves that in homogeneous constrained MGs, there exists an optimal observation-based joint policy with identical local policies that preserves both optimal reward and safety constraints. This is the first result justifying policy sharing in safe MARL, directly supporting the algorithmic design.

- **Asymptotic convergence analysis for the decentralized algorithm (Theorems 3–5)**. Using multi-timescale stochastic approximation under standard assumptions (Assumptions 1–7), the paper proves convergence of the critic parameters to MSPBE minimizers (Theorem 3), actor parameters to equilibria of the gradient ODE (Theorem 4), and dual variables to equilibria of the dual ODE (Theorem 5). Propositions 1–2 further relate the converged dual variable to constraint satisfaction. These results provide rigorous theoretical backing for the on-policy algorithm.

- **Novel decentralized dual variable update with consensus**. The algorithm introduces a consensus-based update for the Lagrangian multiplier (Eq. 8 and the off-policy loss in Eq. 15), where each agent computes a local gradient using initial-state samples and averages with neighbors. This design enables constraint enforcement without a central coordinator, addressing the challenge of a centralized (team-average) constraint in a decentralized setting.

- **Empirical validation on continuous safe MARL tasks**. Figure 1 shows DPDAC-ER achieving comparable reward and cost to the centralized safe baseline MASAC-Lag across three tasks while being fully decentralized, and outperforming it in the Formation task. The ablation comparing DPDAC (without entropy) demonstrates that the entropy regularization mechanism is crucial for safe policy learning in continuous spaces.

## Weaknesses
### Fatal
None.

### Major
None. The paper's core theoretical contributions are sound and well-supported. The empirical evaluation, while not exhaustive, demonstrates the algorithm's effectiveness on its own terms.

### Minor
- **No direct comparison with prior decentralized safe MARL methods adapted to continuous spaces.** The paper claims to improve upon Lu et al. (2021) and Ying et al. (2023b) by extending to continuous spaces, but the experiments include no version of those methods adapted for continuous action spaces. The paper compares instead with CT-based baselines (MASAC, MASAC-Lag) and an unsafe decentralized baseline (DAC-ER). While adapting these discrete-space methods is non-trivial, including even a reasonable adaptation (or explaining why it is infeasible) would strengthen the claim of advancing the state of the art in the decentralized safe MARL sub-area. As it stands, the paper demonstrates that DPDAC-ER *works in continuous spaces*, but not that it is *better* than what prior decentralized safe MARL methods could achieve with reasonable adaptation.

- **Experimental results lack quantitative summary statistics.** The results are presented only as smoothed learning curves (Fig. 1) without final-performance tables reporting mean ± standard deviation across the 5 trials. Quantitative comparison (e.g., mean reward and cost at convergence with confidence intervals) would make the empirical claims more rigorous and reproducible, especially the claim that DPDAC-ER outperforms MASAC-Lag in the Formation task.

- **Theory-practice gap is acknowledged but not discussed.** The paper notes that the convergence results (Theorems 3–5) are for the on-policy, linear-function-approximation algorithm, while the experiments use an off-policy DRL variant with neural networks (Section 5). This gap is standard in the literature, but the paper would benefit from a brief discussion of why the theoretical insights are expected to carry over (e.g., empirical consistency checks on a small-scale version, or references to bridging practices in related work).

### Trivial
- The ablation on local observation (Section 6) reports that the algorithm "can maintain its learning performance under the local observation setting" but provides only a textual claim; the supporting results appear to be in the appendix, which is stripped by the parser. Including a brief quantitative summary or referencing the specific appendix figure in the main text would improve transparency.

## Suggestions
- Add a final-performance table (mean ± std reward and cost at convergence) to the main experimental section, supporting the learning curves with quantitative evidence.
- Clarify in Section 6 what cost threshold \(b\) is used for each environment, and mention whether the ablation uses different \(b\) values explicitly.
- In the related work or experimental design, briefly state why direct adaptation of Lu et al. (2021) or Ying et al. (2023b) to continuous spaces is non-trivial, and whether any comparison was attempted.
- Discuss the theory-practice gap more explicitly in Section 5: note which components of the theoretical analysis are preserved in the off-policy DRL variant and which are heuristic, perhaps with a small-scale consistency check.

## Score and Decision

This paper makes meaningful theoretical contributions (Theorem 1 and the convergence analysis) that advance the state of the art for decentralized safe MARL. The practical algorithm is well-motivated and performs competitively against centralized safe baselines. The empirical evaluation could be strengthened with quantitative summary statistics and a more direct positioning against prior decentralized safe methods, but these are not fatal weaknesses. The paper is clearly written, the claims are generally well-supported, and the research question is important.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>

## Questions


## Decision
Accept
