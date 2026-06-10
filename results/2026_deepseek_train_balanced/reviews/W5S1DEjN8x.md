## Summary

This paper proposes PETS (Practical ε-Exploring Thompson Sampling), an exploration strategy for continuous-control RL that combines Thompson Sampling with Langevin Monte Carlo for posterior sampling, parallel Markov chains to mitigate sample correlation, and gradient-based/gradient-free optimization to approximate the optimal action in continuous spaces. The authors integrate PETS into POMP, MBPO, and SAC and report improved performance on MuJoCo benchmarks, alongside a regret analysis under the linear MDP setting that matches the best-known discrete-action bound.

## Strengths

- **Theorem 3.1 extends the discrete-action TS regret bound to continuous controls under its stated assumptions.** The analysis shows that TS with gradient-based optimization can achieve $\tilde{O}(d^{3/2}H^{3/2}\sqrt{T})$ regret under linear MDPs, linear function approximation, L-smoothness, and the PL condition. While the assumptions are restrictive, this is a non-trivial extension of Ishfaq et al. (2024) from discrete to continuous action spaces.

- **Parallel chains ablation (Figure 5) provides controlled evidence that the proposed solution to LMC sample correlation is effective.** Figure 5a shows increasing $n$ monotonically improves returns; Figure 5b shows $n$ parallel chains outperform a single chain with $n$-step burn-in. This directly supports the paper's central algorithmic choice.

- **Generality across three different RL algorithms without modifying their hyperparameters.** PETS improves performance when plugged into POMP, MBPO, and SAC, suggesting it works as a general exploration module rather than being tied to a specific base algorithm.

- **Quantified improvements on challenging tasks.** The paper reports 38%, 29%, and 11% improvement over POMP on Walker2d, Ant, and Humanoid respectively (Figure 3, 8 seeds).

## Weaknesses

### Major

- **No numerical tables of final performance.** The paper relies entirely on learning-curve figures with no tables of mean/standard deviation returns at convergence. This makes it impossible to quantitatively compare against published numbers from other papers or to precisely assess the claimed improvements beyond the three percentages given. Learning curves are useful but should be accompanied by tabular results, which is standard practice for MuJoCo benchmarks.

- **PETS-specific hyperparameter values are not disclosed.** Algorithm 1 lists hyperparameters ($\epsilon$, $n_{\text{samples}}$, $\eta$, $\eta'$, $\beta$, $\lambda$, $n_{\text{grad\_steps}}$), but the main text provides **none of their actual values**. The paper states that base algorithm hyperparameters are kept the same, but the PETS-specific values (including how $\epsilon$ is set or whether it is annealed) are essential for reproducibility and for assessing whether results might depend on careful tuning.

- **The ablation does not isolate whether LMC drives the improvement or whether it is simply ensemble diversity.** The parallel-chains approach (n chains with SGLD noise) is compared only against a single chain with longer burn-in. The natural baseline is an ensemble of n independently trained Q-networks with standard SGD (no LMC noise term), with one selected uniformly at random at each step. Without this comparison, it is unclear whether the benefit comes from the LMC-specific stochastic gradient dynamics or simply from having multiple diverse Q-functions, which is a well-known technique.

- **Gap between the theoretical analysis and the experimental setting.** The regret analysis (Theorem 3.1) assumes linear MDPs, linear function approximation, the PL inequality, and L-smoothness. The experiments use neural-network Q-functions on MuJoCo environments that are not linear MDPs and for which the PL condition is not guaranteed during RL training. The paper is transparent about the theoretical setting (line 174: "as is standard in the literature"), but the analysis is presented as justification for gradient-based optimization in the actual method, creating a disconnect that is not addressed. The probability range $\delta \in (1/(2\sqrt{2e\pi}), 1) \approx (0.12, 1)$ is also unusual and does not allow standard high-probability guarantees without additional costs (Theorem C.11).

### Minor

- **Ablation experiments use only 3 seeds.** Figure 5 reports results averaged over 3 trials. For MuJoCo tasks, which have high variance (especially on Humanoid-level environments), 3 seeds provide limited statistical reliability.

- **Action diversity analysis is limited to a single task and a coarse metric.** The exploration effectiveness analysis (Figure 4) measures the standard deviation of hopper height on only the Hopper environment. This is a one-dimensional proxy for exploration quality and does not demonstrate that the pattern generalizes to other tasks.

- **Limited comparison against alternative exploration strategies applied to the same base algorithms.** The paper compares PETS-integrated versions against their base algorithms, but not against other exploration techniques applied to the same base (e.g., noisy networks, bootstrapped Q-ensembles, or count-based bonuses). This makes it difficult to attribute gains specifically to TS-based exploration rather than to the general effect of added stochasticity.

- **Conceptual gap in the parallel chains' posterior interpretation.** The paper argues that parallel chains provide diverse posterior samples, but each chain trains on different mini-batches from the same replay buffer, so they are not sampling from the same posterior in a strict Bayesian sense. The paper would benefit from acknowledging this and clarifying whether the benefit is Bayesian posterior sampling or simply ensemble diversity.

### Trivial

None.

## Nice-to-Haves

- A comparison of parallel chains against an independently trained Q-function ensemble (without LMC noise) would isolate whether LMC specifically drives the improvement.
- Reporting wall-clock time and compute overhead of maintaining $n$ parallel chains would aid practical adoption.
- A discussion of how PETS's $\epsilon$-greedy switching interacts with the base algorithm's own exploration (e.g., SAC's entropy-based exploration during $1-\epsilon$ steps) would clarify whether the mechanisms are additive or redundant.

## Removed Points

These claims from the reviewers are removed with justification:

- *"The DBAS description is incomplete — presumably in the appendix"* — Removed because the appendix is stripped by the parser. The paper states pseudocode and details are in the appendix, which existed in the original submission.
- *"Fatal theory-practice gap that invalidates the paper"* — Downgraded from Fatal to Major. The paper transparently states its theory is under the linear MDP setting "as is standard in the literature" (line 174). The gap is real but explicitly acknowledged, not concealed.
- *"Hyperparameter cherry-picking"* — Removed as a speculative accusation not grounded in the paper text.
- *"No statistical significance tests"* — Weakened. Formal significance tests are not standard practice for MuJoCo benchmarks; learning curves with error bars are the norm.
- *"Pure formatting/style nitpicks"* and *"typos/spelling/grammar"* — Removed per instructions (parser artifacts, not author errors).
- Strength Finder's generic strengths (e.g., "the paper addresses an important problem") — Removed as lacking concrete evidence specific to this paper.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add a table reporting mean and standard deviation of final returns for all methods and tasks, following standard MuJoCo reporting practice.
2. Disclose all PETS-specific hyperparameter values ($\epsilon$, $n_{\text{samples}}$, $\eta$, $\eta'$, $\beta$, $\lambda$, $n_{\text{grad\_steps}}$) and include a sensitivity analysis for the most critical ones.
3. Add an ablation comparing parallel SGLD chains against an ensemble of independently SGD-trained Q-networks (without LMC noise) to isolate LMC's role.
4. Qualify the theory more explicitly in the abstract/introduction: state that Theorem 3.1 holds under the linear MDP setting with linear function approximation and PL-smoothness, which differs from the neural-network regime in experiments.
5. Increase the number of seeds for ablation experiments (at least 5).

## Score and Decision

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>