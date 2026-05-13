## Summary
The paper studies action-robust RL under probabilistic policy execution uncertainty (PR-MDPs of Tessler et al. 2019). It proves existence of a deterministic optimal robust policy and an action-robust Bellman optimality equation, then introduces ARRLC (model-based, with policy certificates) and AR-UCBH (model-free Q-learning) with regret bounds $\widetilde{O}(\sqrt{SAH^3K})$ and $\widetilde{O}(\sqrt{SAH^5K})$ respectively. Tabular experiments on CliffWalking and InvertedPendulum compare against non-robust ORLC and the robust TD method of Klíma et al.

## Strengths
- **Variance handling under a stochastic ρ-mixture behavior policy is genuinely new.** In ORLC/UCBVI the behavior policy is deterministic, so the standard variance-summation argument applies cleanly. Here the behavior policy mixes $\overline{\pi}$ and $\underline{\pi}$, and Lemmas on $M_1$, $M_2$ (Sec. 6, l. 225–243) decompose the resulting variance contributions; this is the main technical contribution and it is executed cleanly.
- **Simultaneous optimistic/pessimistic estimates with the sandwich $\overline{V}\ge V^*\ge V^{\overline{\pi}}\ge \underline{V}$** (Lemma 2, l. 220–221) gives a principled way to extend the policy-certificate mechanism of Dann et al. (2019) to the robust min–max setting.
- **First $\widetilde{O}(\sqrt{SAH^3K})$ regret bound for PR-MDPs.** Even setting aside the "minimax optimal" framing, this is a quantitative improvement over what one would obtain by black-boxing Nash-VI or V-learning, which the paper itself notes are off by factors of $A$ or $H^2$ (l. 40).

## Weaknesses

### Fatal
None — the core upper-bound results appear sound.

### Major
- **"Minimax optimal" rests on a one-line $\rho=0$ reduction.** The matching lower bound argument (l. 188–189) is: "When $\rho=0$, the action robust MDPs is equivalent to the standard MDPs. Thus, the information-theoretic [lower bounds] should have same dependency on $S, A, H, K$ or $\epsilon$." This only establishes tightness at the single degenerate point $\rho=0$, which is precisely the standard-MDP case the paper is not really about. Nothing rules out that the true lower bound for $\rho\in(0,1)$ depends nontrivially on $\rho$ in a way the upper bound does not, and the paper's $\widetilde{O}(\sqrt{SAH^3K})$ has no $\rho$ dependence at all. The "minimax order optimal" claim in the introduction (l. 24) and Theorem 2 discussion should be either weakened to "matches the standard-MDP minimax rate" or accompanied by an actual lower bound argument for $\rho>0$.
- **The experiments do not test the paper's quantitative claim (sample efficiency vs. prior PR-MDP solvers).** The introduction and related work explicitly position the contribution against Nash-VI, V-learning, and PR-PI (Tessler et al. 2019), citing that those approaches are off by $A$ or $H^2$ factors (l. 40, l. 18). Yet the experiments compare only against ORLC (a non-robust algorithm) and Klíma et al.'s robust TD (which has no sample-complexity guarantee). Beating a non-robust algorithm under adversarial perturbation is essentially tautological and does not probe sample efficiency relative to the methods the paper claims to improve upon. At least PR-PI, which is the algorithmic predecessor on the same MDP model, is a natural baseline.

### Minor
- **Inverted Pendulum is run with a tabular algorithm on a continuous-state MuJoCo environment with no discretization specified.** ARRLC and AR-UCBH are analyzed for finite $\mathcal{S}, \mathcal{A}$ (l. 47), and Sec. 7 (l. 308–329) gives no description of how the continuous state and the continuous force action are discretized, nor what the resulting $S, A$ are. The results may well be valid for some discretization, but as written they cannot be connected to the theory. CliffWalking is fine.
- **Fixed adversary in Inverted Pendulum is a constant 0.5 N leftward force** (l. 329). This is a constant disturbance more than an adversarial policy; demonstrating robustness to such a perturbation is weaker evidence than testing against a learned worst-case adversary, which the algorithm specifically models.
- **No training-seed variability reported.** The text (l. 309) describes averaging "over 100 trajectories" but this refers to evaluation rollouts of a fixed learned policy, not multiple training seeds. Curves in Figs. 4–5 are presented without shaded variance regions.
- **Lower-order term $S^2AH^3\iota^2$ is worse than ORLC's.** Theorem 2 (l. 184) has a second-order term that exceeds the corresponding ORLC term, and the paper does not discuss whether this is intrinsic to the robust setting or an analytical artifact. Matters for small-$K$ regimes.
- **Theorem 1's novelty is partially redundant with Tessler et al. (2019).** The paper itself acknowledges (l. 121) that perfect duality / Markov-game equivalence was already established there; the contribution in Sec. 4 is a specialization to the action-robust Bellman optimality equation. Reasonable, but the introduction's first bullet (l. 23) overstates this as a standalone contribution.

### Trivial
- The model-free section establishes a result $H^2$ worse than the model-based result, but provides no discussion of when one would prefer it; the section feels orphaned.

## Nice-to-Haves
- A plot of $\overline{V}_1 - \underline{V}_1$ across episodes, showing certificate tightness in practice.
- A comparison or at least a discussion against PR-PI (Tessler et al. 2019), even on the tabular CliffWalking benchmark.
- Either a discretization analysis for the Inverted Pendulum experiment, or replacement with a genuinely tabular benchmark such as a larger gridworld.
- Even a partial lower bound that exhibits $\rho$-dependence, or an explicit acknowledgement that the optimality claim is restricted to the $\rho=0$ slice.

## Removed Points
*These points are flagged to be removed, treat them with caution.*
- Strength Finder's claim that "minimax optimality translates into practical robustness and efficiency" is conflated with the empirical comparison — it is generic praise that also conflicts with the verified weakness about the lower bound, so it is dropped.
- Strength Finder's "rigorous theoretical foundation" and "transparent proof sketch" are kept implicitly via the strengths above but their generic versions are removed as superficial.
- Harsh critic's framing of the abstract sentence "outperforms non-robust RL algorithms" as a misleading claim is a presentation nitpick rather than a substantive flaw; downgraded into the Major point about baselines.

## Novel Insights
None beyond the paper's own contributions. The most interesting technical observation — that the variance-summation argument needs to account for a non-deterministic behavior policy because the algorithm internally simulates the adversary — is already the paper's contribution.

## Suggestions
- Either prove a lower bound that retains a $\rho$ dependence, or rephrase the optimality claim as "matches the standard-MDP minimax rate; whether the rate is tight for $\rho>0$ is open."
- Add a tabular PR-PI baseline (and Nash-VI if feasible) on CliffWalking; this is the most direct test of the central claim.
- Specify (and justify) the discretization for Inverted Pendulum, or move that experiment to a genuinely tabular environment.
- Report multiple training seeds with confidence bands on Figures 4–5.
- Test against a learned worst-case adversary at evaluation, not just constant or uniform-random perturbation.

---

**Axis evaluation.** *Originality:* moderate — careful but incremental extension of ORLC and Dann et al.'s certificate machinery to the PR-MDP setting, with a genuine new variance analysis. *Importance:* PR-MDP action robustness is a recognized, narrow-but-real subproblem. *Support for claims:* upper bounds are well-supported; the headline "minimax optimal" label is only justified at $\rho=0$. *Soundness of experiments:* CliffWalking is reasonable; Inverted Pendulum is methodologically loose (no discretization, weak adversary, no training-seed variability), and the baselines do not probe the paper's main quantitative claim. *Clarity:* good; algorithm and proof sketch are well-organized. *Value to community:* a useful improvement on the regret rate for PR-MDPs that should be of interest to the robust-RL theory community, provided the framing is corrected.

## Score and Decision

The technical core (model-based regret bound and its variance analysis) is real and improves over the prior literature. The framing ("minimax optimal") overshoots what is proved, and the empirical section sidesteps the baselines that would actually test the sample-efficiency claim. These are correctable, not fatal — but they meaningfully reduce the contribution as presented.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>