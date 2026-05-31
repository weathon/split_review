## Summary

This paper studies the stochastic bilevel optimization problem in the nonconvex-strongly-convex setting. The authors introduce a key reinterpretation: the F²SA method (Kwon et al., 2023) can be viewed as approximating the hyper-gradient via a forward finite difference on a parameterized lower-level optimal-value function $\ell_\nu(\mathbf{x})$. Building on this insight, they propose F²SA-$p$, a family of methods that use $p$th-order finite difference for hyper-gradient approximation, achieving an SFO complexity of $\tilde{\mathcal{O}}(p\kappa^{9+2/p}\epsilon^{-4-2/p})$ under a $p$th-order smoothness assumption in the lower-level variable $\mathbf{y}$. They further prove a matching $\Omega(\epsilon^{-4})$ lower bound via a clean separable construction, establishing near-optimality when $p = \Omega(\log\epsilon^{-1}/\log\log\epsilon^{-1})$.

## Strengths

- **Elegant and productive conceptual reframing.** Identifying F²SA's penalty reformulation as a forward finite difference applied to $\frac{\partial}{\partial\mathbf{x}}\ell_\nu(\mathbf{x})$ (via Eq. (8)-(9)) is a genuine insight. It immediately motivates a natural family of algorithms by substituting higher-order finite difference formulas, directly importing classical numerical analysis into bilevel optimization.

- **Monotone improvement in complexity.** The $\tilde{\mathcal{O}}(p\epsilon^{-4-2/p})$ bound interpolates smoothly from $\tilde{\mathcal{O}}(\epsilon^{-6})$ at $p=1$ to $\tilde{\mathcal{O}}(\epsilon^{-4})$ for logarithmically large $p$, matching the single-level SGD lower bound up to log factors. The family is thus genuinely Pareto-improving over F²SA under progressively stronger smoothness.

- **Strictly weaker assumption than competing work.** Unlike Huang et al. (2025), which assumes second-order smoothness jointly in $(\mathbf{x},\mathbf{y})$, Assumption 2.5 only requires high-order smoothness in $\mathbf{y}$. This is a meaningful relaxation; the paper gives concrete examples (data hyper-cleaning, learn-to-regularize with softmax/logistic-regression structure) that satisfy it.

- **Clean, novel lower bound construction.** Prior bilevel lower bound constructions (Dagru et al., 2024; Kwon et al., 2024a) had technical deficiencies under the intended assumptions. The fully separable construction used here ($f(\mathbf{x},\mathbf{y})\equiv f_U(\mathbf{x})$, $g(\mathbf{x},\mathbf{y})\equiv\mu y^2/2$) is unambiguously valid and cleanly reduces bilevel to single-level hardness (Arjevani et al., 2023).

- **Tighter intermediate bound for $p=2$ (Remark 3.2).** Lemma 3.2's approach via Faà di Bruno's formula avoids explicit computation of $\nabla^2\varphi(\mathbf{x})$ and yields a $\mathcal{O}(\kappa^5\bar{L})$ Lipschitz constant for $\frac{\partial^3}{\partial\nu\partial\mathbf{x}^2}\ell_\nu(\mathbf{x})$, improving the $\mathcal{O}(\kappa^6\bar{L})$ bound in Chen et al. (2025b)—a result that is useful independently.

## Weaknesses

### Fatal
None.

### Major

- **Normalized gradient descent without a full proof path for the standard step.** Algorithm 1 uses $x_{t+1} = x_t - \eta_x\Phi_t/\|\Phi_t\|$ (line 14), which is non-standard relative to F²SA. The paper acknowledges in Remark 3.1 that the standard gradient step "likely also works" but does not prove it. This is a notable omission because: (a) normalized gradient descent has different practical behavior and convergence properties; (b) the complexity comparison with F²SA in Table 1 is slightly misleading if the algorithms are not in the same algorithmic family; and (c) implementation details for practitioners change with this modification.

- **Gap remains for all fixed $p$.** The paper's near-optimality result requires $p$ to grow logarithmically with $\epsilon^{-1}$, meaning no fixed-$p$ instantiation of the algorithm is $\epsilon$-tight. In particular, the practically important cases $p=1$ and $p=2$ still show a $\tilde{\mathcal{O}}(\epsilon^{-6})$ and $\tilde{\mathcal{O}}(\epsilon^{-5})$ upper bound respectively, well above the $\Omega(\epsilon^{-4})$ lower bound. This is honestly discussed but limits the practical takeaway for the most common smoothness regimes.

### Minor

- **Experiments compare per outer-iteration performance, not SFO calls.** The theoretical contributions are phrased entirely in terms of SFO complexity, yet Figure 1 plots test loss/accuracy vs. number of outer-loop iterations $t$. Since HVP-based methods (stocBiO, MRBO, VRBO) have different per-iteration oracle costs than the fully first-order methods, this comparison does not map cleanly onto the paper's own theoretical metric. A plot in terms of total SFO calls or gradient evaluations would be more consistent.

- **Condition number gap.** The upper bound carries a $\kappa^{9+2/p}$ factor while the lower bound is $\Omega(\epsilon^{-4})$ with no condition number term. The paper notes the gap is $\Omega(\kappa^9)$ and mentions concurrent work bounding it, but the analysis is incomplete. Since $\kappa$ can be large in practical bilevel problems, this gap is substantive for non-constant $\kappa$.

### Trivial

- The main text only presents Algorithm 1 for even $p$; the odd-$p$ algorithm (Algorithm 2) is deferred to the appendix, leaving the treatment slightly asymmetric.

## Nice-to-Haves

- An empirical comparison using total SFO calls (accounting for parallel inner-loop work across $p+1$ sub-problems) would let the reader assess whether higher $p$ is actually worth the extra per-iteration cost.
- A brief discussion of how $p$ should be chosen in practice given only partial knowledge of the problem's smoothness order would be helpful.

## Novel Insights

The paper's most genuinely novel insight is that the penalty-based reformulation at the heart of F²SA can be exactly understood as a forward finite difference applied to $\nu \mapsto \nabla_\mathbf{x}\ell_\nu(\mathbf{x})$, where $\ell_\nu(\mathbf{x}) = \min_\mathbf{y} g_\nu(\mathbf{x},\mathbf{y})$ is a smoothly parameterized lower-level value function. This identification is non-obvious and conceptually unifying: it bridges the penalty approach in bilevel optimization with classical numerical differentiation theory (Lemma 3.1), allowing one to import a rich library of finite difference formulas with known error orders into the bilevel setting. The consequence—that higher-order smoothness in $\mathbf{y}$ translates directly into faster hyper-gradient approximation and hence faster convergence—is obtained with essentially no extra structural assumptions beyond what already appears in the literature. The separable lower-bound construction, while technically simple, also resolves the correctness issues present in prior bilevel lower bounds.

## Suggestions

- Prove (or provide a sketch) that Theorem 3.1 holds with standard gradient descent in place of normalized gradient descent, or provide a clear example showing where the analysis breaks down, so readers can assess the gap.
- Add an SFO-cost-normalized experiment where each method's horizontal axis accounts for the number of gradient evaluations (including inner-loop calls) to allow fair comparison with HVP-based baselines.
- Clarify whether the $p+1$ parallel lower-level sub-problems in each iteration of Algorithm 1 are genuinely parallelizable in the experiments, and if not, how the per-iteration wall-clock cost scales.

## Score and Decision

The paper delivers a clean theoretical contribution to the bilevel optimization literature: a natural algorithmic family motivated by a novel perspective, improved complexity under reasonable additional assumptions, and a valid matching lower bound. The finite difference reinterpretation is elegant and productive. The main limitations—the gap for fixed small $p$ and the unproven extension to standard gradient steps—are acknowledged honestly and do not invalidate the core results. The paper is technically sound and advances the field.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>