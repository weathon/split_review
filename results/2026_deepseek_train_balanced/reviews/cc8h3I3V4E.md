## Summary

The paper introduces the first loss function for approximate Nash equilibria in normal-form games (NFGs) that admits unbiased Monte Carlo estimation, by projecting gradients onto the *tangent space* of the simplex (a linear operation) and applying the double-sampling trick. It provides theoretical convergence guarantees via $\mathcal{X}$-armed bandits, analyzes the Hessian and polymatrix-isolatedness of equilibria, and presents empirical comparisons of SGD against FTRL, Regret Matching, and ADIDAS on four games. The core insight — that replacing the nonlinear simplex projection with the linear tangent-space projection enables unbiased estimation — is genuinely novel and well-articulated.

## Strengths

- **Tangent-space projection enables unbiased Monte Carlo estimation of a Nash-relevant loss.** The paper identifies that $\Pi_{T\Delta}$ (projection onto the simplex tangent space) is linear, unlike $\Pi_{\Delta}$ (projection onto the simplex itself). This allows $\mathcal{L}(\boldsymbol{x}) = \sum_k \eta_k \|\Pi_{T\Delta}(\nabla^k_{x_k})\|^2$ to be estimated without bias via $\mathbb{E}[Y^{(1)} Y^{(2)}] = \mathbb{E}[Y]^2$. Table 1 clearly contrasts this with prior losses (exploitability, Nikaido-Isoda, fully-differentiable exploitability, gradient-based NI) that all involve a nonlinear $\max$ or $\Pi_{\Delta}$ and are therefore biased under sampled play. This is the paper's central technical contribution.

- **Provable global convergence rates via $\mathcal{X}$-armed bandits.** The connection to $\mathcal{X}$-armed bandits yields PAC-style rates (Theorems 1 and 2) that map to approximate Nash equilibrium guarantees. While the rates depend on assumptions discussed below, the existence of any global convergence guarantee for general-sum $n$-player NFGs within a stochastic optimization framework is a genuine theoretical contribution beyond prior local-convergence or heuristic approaches.

- **Entropy regularization integrates cleanly.** Adding a Shannon entropy bonus $\tau S(x_k)$ makes all equilibria interior while the entropy gradient $-\tau(\ln(x_k) + \mathbf{1})$ is known deterministically and can be added to the gradient estimator without breaking unbiasedness. Lemma 7 provides the clean bound $\epsilon \le \tau \log(\prod_k m_k) + \sqrt{2n/\min_k \eta_k}\sqrt{\mathcal{L}^\tau(\boldsymbol{x})}$, linking minimizers of $\mathcal{L}^\tau$ to approximate NEs of the original game. The Chicken game visualization (Figure 1) provides compelling qualitative evidence of the practical consequence of unbiasedness.

- **Hessian analysis and polymatrix-isolated condition.** The closed-form Hessian (Lemma 9) and the matrix $M(\boldsymbol{x})$ (Eq. 16) give a concrete, checkable condition for when an equilibrium is locally isolated with positive-definite curvature. This goes beyond standard stationarity analysis and provides structural insight into the loss landscape. Verification on four classical games demonstrates the condition is not vacuous.

## Weaknesses

### Fatal

None.

### Major

- **Figure 4 (SGD comparison) does not specify axis labels in the caption or text.** The caption (line 284) describes the games but does not state what metric is plotted on the $y$-axis (exploitability? NashConv? projected-gradient norm?) or the $x$-axis (iterations? samples? wall time?). Line 300 states that SGD "is competitive" but the reader cannot independently verify what is being compared. Without this basic information, the paper's claim in the abstract that "stochastic gradient descent can outperform previous state-of-the-art approaches" cannot be properly evaluated.

- **No runtime or memory measurements despite scalability being the central motivation.** The introduction argues that existing methods cannot scale because they require reading the exponential $nm^n$ payoff tensor into memory (line 26). The paper presents scalability as a primary motivation (lines 24–29). Yet no experiment measures runtime, memory usage, or sample complexity (number of payoff queries vs. exploitability). The largest game tested (3 players, 286 actions) is well below the scale where the $nm^n$ memory bottleneck becomes prohibitive. Without measurements that directly validate the scalability thesis, the practical significance of the contribution is asserted but not demonstrated.

- **Bandit convergence guarantees depend on assumptions that are not validated and rates that degrade rapidly.** The polymatrix-isolated condition (Definition 1) is checked for only four small classical games (line 278). The zooming dimension $d_z = \frac{1}{2}n\bar{m}$ and zooming constant $C_z$ in Theorem 1 depend on quantities (the set $\mathcal{X}^*$ of near-optimal states, local strong-convexity parameters $r_\eta$, $\sigma_{-\infty}$) that cannot be computed without knowledge of the loss landscape — they are essentially existential. The stated rate $\tilde{\mathcal{O}}(T^{-1/(2(d_z+2))})$ becomes extremely slow in high-dimensional strategy spaces, and the StoSOO rate (Theorem 2) requires an exponential burn-in (line 337). These limitations are not discussed; the theorems are presented as positive results without acknowledging their practical restrictiveness.

### Minor

- **The $\tau$-approximation tradeoff is acknowledged qualitatively but not analyzed.** Lemma 7 shows $\epsilon \le \tau \log(\prod_k m_k) + \sqrt{2n/\min_k \eta_k}\sqrt{\mathcal{L}^\tau(\boldsymbol{x})}$, where the additive error grows linearly with $n$ and $\log m_k$. Meanwhile, the Lipschitz constant $\hat{L}$ scales with $1/(p\ln(1/p))$ where $\tau = 1/\ln(1/p)$ (line 323), meaning approximation error and optimization difficulty both increase with game size. The paper does not provide guidance on how to choose $\tau$ given a target exploitability and game size, nor does it analyze whether optimization at the required $\tau$ remains tractable.

- **The bandit experiment (Figure 5) is on a single artificial 7-player, 2-action game with no comparison to any baseline method.** While this figure primarily illustrates the bandit search concept, its evidentiary value is limited without a baseline.

### Trivial

None.

## Nice-to-Haves

- A variance analysis of the three estimators in Table 1 would strengthen the practical guidance on estimator choice, particularly since the "Sample All" estimator's bounds scale cubically in $m_k$ (as noted in Table 1).
- The SGD comparison would be more informative with error bars (multiple random seeds) and a clear statement of the metric and axis labels in the caption.

## Removed Points

These points from the inputs are flagged to be removed following the filtering rules; treat them with caution:

- **Reproducibility/reviewer nitpicks (hyperparameter tuning, code, pseudocode, learning rates, initialization, stopping criteria, hardware):** Removed per the rule against nitpicking reproducibility details that are standard to omit from a conference submission.
- **Gumbel-max trick suggestion:** The reviewer suggested discussing the Gumbel-max trick for unbiased estimation of $\max$, but this is a misunderstanding — the Gumbel-max trick is for sampling from a distribution, not for unbiasedly estimating the expectation of a $\max$ of random variables.
- **"Cherry-picking games" criticism:** The games are explicitly drawn from the prior work of Gemp et al. (2022), the benchmark used by the main comparator. This is appropriate experimental design, not cherry-picking.
- **"Gradient-based NI entry is unfair" framing:** The reviewer argued that the paper's own approach "only works because the loss is the norm of a projected gradient." This is not a weakness — the loss is *defined* as the norm of the projected gradient; the paper never claims otherwise.
- **Missing formal variance analysis:** Lemma var_bnd is referenced but stripped by the parser; the paper likely contains this analysis in its full version.
- **"Prior methods might work well despite bias" speculation:** This is a hypothetical concern with no evidence either way; the paper provides empirical evidence in Figure 1 that bias is harmful in at least one concrete case (Chicken game).
- **Generic area-of-concern-style speculations** (e.g., "could the metric be measuring a proxy") that lack specific anchors in the paper text.

## Novel Insights

The two review inputs largely converge on the same assessment: the theoretical core is novel and competent, while the experimental evaluation is insufficiently rigorous and does not adequately support the claimed practical significance. Neither reviewer identified a fatal flaw in the theory or a fundamental error in the paper's central contribution. The most informative signal from combining both reviews is that the paper suffers from a misalignment between its ambition (claimed practical superiority in scalable equilibrium computation) and its evidence (thin, poorly-documented experiments on small games). This is a framing and execution problem, not a conceptual one.

## Suggestions

1. **Specify the axes in Figure 4's caption** — what metric is plotted on the $y$-axis (exploitability, NashConv, or loss?) and what the $x$-axis represents (iterations, payoff queries, or wall time?).
2. **Add a runtime or sample-complexity comparison** that directly validates the scalability motivation: number of payoff tensor entries accessed vs. exploitability achieved, comparing SGD (with unbiased estimator) against baselines that must access the full tensor.
3. **Add an ablation study** comparing SGD on $\mathcal{L}$ vs. $\mathcal{L}^\tau$ on a game with pure equilibria to empirically demonstrate the entropy regularization's effect.
4. **Add practical guidance** for choosing $\tau$: given $(n, m_k)$ and a target exploitability, what $\tau$ is required, and what does that imply for the Lipschitz constant and expected convergence rate.
5. **Reframe the paper's claims** to match the evidence: if the experiments remain proof-of-concept, the abstract and introduction should not claim to "outperform previous state-of-the-art approaches" without substantial qualification.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>