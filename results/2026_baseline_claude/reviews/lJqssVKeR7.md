Now I have read the full available content of the paper. Let me write my review.

---

## Summary

The paper proposes **HiSo** (Hessian-informed Scalar-only communication), a federated learning algorithm that integrates diagonal Hessian approximations into zeroth-order (ZO) optimization while preserving scalar-only (dimension-free) communication. The central insight is that the aggregated global gradient scalars already communicated for model reconstruction in the ZO-FL framework can be reused to estimate a diagonal Hessian preconditioner at zero additional communication cost. The paper presents formal convergence results showing dimension- and Lipschitz-constant-independent rates under low-effective-rank/whitening assumptions, and reports 1.4–5.4× speedups over the DeComFL baseline across OPT models (125M–2.7B) on SST-2, QQP, and SQuAD.

---

## Strengths

- **Elegant "free Hessian" insight**: The key observation that the diagonal Hessian approximation can be reconstructed locally at both server and clients using previously communicated scalar values (gradient scalars and seeds) is non-trivial and elegantly resolves the apparent tension between Hessian preconditioning and scalar-only communication. No extra transmission is required because $\Delta x_{r,0}$ is already shared for model reconstruction.

- **Generalized framework with genuine conceptual contribution**: Algorithm 1 cleanly decouples the scalar-only communication mechanism from the specific ZO update rule. This generalization is a legitimate contribution beyond the HiSo method itself and could inspire future work on other optimization algorithms within the same communication paradigm.

- **Novel theoretical analysis**: The introduction of "low whitening rank" $\zeta = \text{Tr}(H^{-1/2}\Sigma H^{-1/2})$ as a variance quantity, and its use to derive a convergence rate independent of $d$ and $L$, is new to the ZO-FL literature. Corollary 3 further extends DeComFL's theory to the multiple-local-update ($\tau > 1$) setting, which DeComFL's original analysis could not handle, and shows that HiSo's advantage over DeComFL widens when $\tau > 1$.

- **Comprehensive empirical evaluation**: Experiments span four OPT model sizes (125M–2.7B), three NLP tasks, and multiple baselines including first-order adaptive FL methods (FedAdam, FedYogi, FedAdagrad) and ZO baselines (FedZO, DeComFL). Ablation on the smoothing parameter $\nu$ shows HiSo is robust to this hyperparameter. The MNIST experiment provides interpretable visualization of the learned Hessian structure and its long-tail distribution, supporting the theoretical assumptions.

---

## Weaknesses

### Fatal
None identified.

### Major

1. **Memory cost is not addressed in the main paper**: The diagonal Hessian $H_r \in \mathbb{R}^d$ requires $O(d)$ memory. For OPT-2.7B, this is approximately 2.7B floats (\~10 GB in float32, \~5.4 GB in float16). ZO methods are already justified partly by avoiding backward-pass memory, yet the diagonal Hessian may roughly double total client memory. While the paper refers readers to Appendix E for memory analysis, this cost is significant enough in the LLM fine-tuning context to warrant quantitative discussion in the main paper, especially for resource-constrained federated clients.

2. **"Well-approximated condition" is assumed rather than validated for LLMs**: The dimension-independent convergence rates (Corollaries 1 and 3) depend critically on the "well-approximated condition" $\text{Tr}(H^{-1/2}\Sigma H^{-1/2}) \leq \zeta \ll d$, which essentially assumes the diagonal Hessian approximation is already effective. The only validation is a log-normal simulation (Fig. 4); there is no empirical check that this condition approximately holds during actual LLM fine-tuning. Since this condition is both the primary assumption behind the accelerated rate and the primary justification for the algorithm, its empirical grounding in the main setting is thin.

3. **Asymmetric speedup measurement in Table 2**: HiSo's "speedup" is measured as the rounds to reach DeComFL's best accuracy, not HiSo's own convergence. Since HiSo consistently achieves higher final accuracy (Table 3), the true cost to reach HiSo's own convergence point is not reported. Convergence curves would be more informative than this one-directional comparison.

### Minor

1. **OPT-1.3B + QQP anomaly**: HiSo's communication cost on this setting (96.67 KB) is more than double DeComFL's (43.95 KB), with only a minor accuracy gain (+0.95%). This is not explained beyond a brief parenthetical acknowledgment. Understanding what causes this outlier—whether it is slow convergence in that particular configuration or a hyperparameter sensitivity issue—would strengthen confidence in the method's general reliability.

2. **Small FL scale**: All experiments use 6 clients ($M=6$, $m=2$ sampled per round). Real federated fine-tuning scenarios often involve orders of magnitude more clients. The impact of scale on both the Hessian approximation quality and convergence behavior is unexamined.

3. **Learning rate restriction for $\tau > 1$**: Theorem 1 requires $\eta \leq \frac{\beta_\ell}{4(\tau-1)}$, which becomes very restrictive as $\tau$ grows. The paper does not discuss whether this restriction is ever binding in practice or how it interacts with the convergence tradeoff in Corollary 3 ($\sqrt{\zeta/\tau mR}$ improves with $\tau$ but the drift term $\sqrt{\tau\kappa/mR}$ worsens).

### Trivial
None.

---

## Nice-to-Haves

- A convergence curve figure for LLM tasks (HiSo vs DeComFL vs first-order baselines) would substantially strengthen the empirical narrative.
- An ablation varying the number of clients and heterogeneity level $\alpha$ to understand scalability.
- A brief empirical estimate of how well the "well-approximated condition" holds during actual LLM fine-tuning, e.g., by computing $\text{Tr}(H^{-1/2}\Sigma H^{-1/2})$ at a few checkpoints.

---

## Novel Insights

The most genuinely novel insight in this paper is the observation that the global aggregated gradient scalars $\Delta x_r$—already transmitted for model reconstruction in the DeComFL paradigm—can be recycled to compute a running diagonal Hessian approximation at literally zero additional communication overhead. This "free Hessian" observation is the engine of the entire paper, and it is not obvious from prior work. Complementing this, the paper introduces "low whitening rank" $\zeta = \text{Tr}(H^{-1/2}\Sigma H^{-1/2})$ as a theoretically meaningful quantity that unifies and sharpens the variance analysis of ZO methods under Hessian preconditioning, yielding the first dimension-independent convergence rate for multi-step ZO-FL. Together, these contributions draw a meaningful conceptual bridge between adaptive/Newton-style optimization and zeroth-order federated learning.

---

## Suggestions

- Include a quantitative memory cost table in the main paper for the model sizes tested, clearly comparing ZO methods (HiSo vs. DeComFL) and first-order methods.
- Report convergence curves in the main paper for at least one LLM task to give readers a richer picture of convergence dynamics.
- Add a focused discussion or experiment on the OPT-1.3B + QQP case where HiSo's communication cost exceeds DeComFL's.
- Discuss the optimal $\tau$ tradeoff (from Corollary 3) and provide an experiment validating the predicted optimal range.
- Consider strengthening the "well-approximated condition" with at least one empirical measurement on an actual LLM checkpoint.

---

## Score and Decision

HiSo addresses a genuine bottleneck in federated LLM fine-tuning with a conceptually elegant solution: reusing already-communicated scalars to build a Hessian preconditioner at zero communication cost. The theoretical analysis is rigorous and novel (especially the multi-step extension), and the empirical results convincingly demonstrate 1.4–5.4× acceleration across diverse settings. The main concerns—unaddressed memory cost in the main paper, the thin empirical grounding for the core "well-approximated" assumption, and a small experimental FL scale—are worth attention but do not undermine the paper's central claims. This is a solid contribution to communication-efficient federated optimization.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>