## Summary

This paper develops a high-dimensional SDE approximation for clipped SGD (C-SGD) in streaming least-squares problems, leading to a deterministic ODE description of risk evolution. The key contributions are two reduction factors, $\H_c$ and $\G_c$, that capture how clipping affects the descent and variance terms, yielding precise criteria: the Clipped-Stability-Criterion (CSC, $\H_c/\G_c>1$) and the Clipping-Comparison-Criterion (CCC, $\H_c^2/\G_c>1$) determine when clipping improves stability or optimization speed. A provably optimal max-CCC schedule with compensated learning rate is shown to never underperform unclipped SGD, and a practical single-parameter heuristic schedule is derived. The theory is validated on synthetic, CIFAR10, and Wikitext2 data using random-feature linear models.

## Strengths

- **Non-asymptotic bound on the C-SGD / C-HSGD approximation error**: Theorem 1 provides an explicit $O(\log(d)\,d^{-1/2})$ bound on the difference between the risk curves of clipped SGD and the homogenized SDE, with probability $1-e^{-u}$. This is stronger than the asymptotic guarantees common in the SDE-approximation literature, establishing that the approximation holds over finite time horizons in high dimensions.

- **Clean, interpretable criteria for clipping's effects**: The paper identifies two exact unitless conditions — CSC ($\H_c/\G_c>1$) and CCC ($\H_c^2/\G_c>1$) — that govern whether clipping helps stability or optimization speed. These go beyond qualitative "heavy-tailed noise" claims, giving computable rules expressed in terms of the reduction factors. The Gaussian form $\H_c = P(|w_x|\leq c)$ (via Stein's Lemma) is particularly elegant and interpretable.

- **Provably optimal schedule and converse**: Theorem 3 proves that the max-CCC schedule with compensated learning rate guarantees $\Rcl_T \leq \Runc_T$ for *any* unclipped learning rate schedule, with strict improvement when the CCC holds. The converse is also proved: if CCC $\leq 1$ everywhere, no clipping schedule can outperform SGD. This is a strong mathematical guarantee not present in prior clipping analyses.

- **Crisp negative result for Gaussian noise**: Theorem 4 proves that with Gaussian data and Gaussian noise, $\H_c^2(R)/\G_c(R) \leq 1$ for all $R,c>0$, so clipping never improves optimization speed. This gives practitioners a clear boundary — if gradient noise is near-Gaussian, clipping should not be expected to accelerate convergence.

- **Practical heuristic reducing to a single scalar**: The heuristic schedule $c^a(t) = \kappa\sqrt{2R_t + \sigma^2}$ (Eq. 496) reduces clipping threshold scheduling to tuning one parameter $\kappa$, and Figure 6 shows it matches the numerically optimized max-CCC schedule nearly identically in the tested setting.

- **Validation on real data distributions**: The theory is tested on CIFAR10 and Wikitext2 data (via random-feature linear models), showing that the deterministic ODE captures C-SGD dynamics even when data is non-Gaussian, demonstrating robustness beyond the synthetic Gaussian setting.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Framing oversells practical relevance to neural networks**. The introduction motivates clipping through GPT-3, MLP-Mixer, ViT, and differential privacy, creating an expectation that the analysis speaks to neural network training. However, every experiment — including CIFAR10 and Wikitext2 — uses *linear models on random features*, not neural networks. The paper is technically transparent about this (Section 2 explicitly states linear regression), but the gap between motivational framing (deep learning) and evidence (linear models) is significant. The Conclusion's discussion of neural network links remains entirely speculative with no measurements on actual networks. This does not invalidate the theory but means the claims about practical relevance are unsupported.

2. **The "never underperforms" guarantee applies to the optimal schedule, not the heuristic.** Theorem 3's guarantee is proven for the exact max-CCC schedule (Eq. 423—428), which requires computing $\argmax_c \H_c^2/\G_c$ at every step. The heuristic (Eq. 496—497) replaces this with a closed-form approximation derived from loose bounds (Eq. 175—178) involving uncharacterized constants $\kappa_l,\kappa_u$. The heuristic is only tested in one synthetic setting (Figure 6). The paper acknowledges "thorough exploration and validation is left for future work," but the abstract ("propose a simple heuristic… which we prove *never* underperforms unclipped SGD") could mislead readers into conflating the heuristic with the provable schedule.

3. **Theorem 1's bound contains exponential factors that may dominate in practice.** The constant $\mathcal{C}$ includes a factor $\exp(C\max\{\overline{\lr},\overline{\lr}^2\}(n/d))$ and the stochastic process $\mathcal{E}(t)$ involves exponential growth in an integral of $\lr(s)^2$. The bound is stated as "provided the right hand side is less than 1," but no guidance is given on the range of $n/d$ and learning rates for which the bound is non-vacuous. While common in SDE approximation bounds, this limits practical interpretability.

4. **The constants $\kappa_l,\kappa_u$ in the reduction factor bounds (Eq. 175—178) are never characterized.** The bounds are used to derive the heuristic schedule, but the paper provides no estimate of $\kappa_l,\kappa_u$ for any data distribution or discussion of how they depend on problem parameters. The reader cannot assess the tightness of these bounds or the reliability of the heuristic derived from them.

5. **Real-data experiments use very small intrinsic dimensions ($d\approx 4\text{--}5$), providing a weak test of large-$d$ asymptotic predictions.** The CIFAR10 experiment uses $d=4.578$ and Wikitext2 uses $d=3.237$. The theory is about the large-$d$ limit; validating on $d\approx 4$ is a very modest test of the asymptotic claims. The synthetic experiments use larger $d$ (e.g., $d=179$), but the real-data validation — the paper's primary evidence for practical relevance — operates in a regime far from the theoretical assumptions.

6. **Unsupported claim about SGD performance.** The statement "with sufficient hyper-parameter tuning, SGD often outperforms other more complex methods" (line 15) is a contested claim presented without citation.

### Trivial
- Figure 1 captions for the CIFAR10 and Wikitext2 panels do not explicitly state the number of runs or confidence intervals (though filenames suggest 50 runs were used, other figure captions do report these details).

## Nice-to-Haves
- **Empirical validation of the stability criterion (CSC)** would strengthen the paper. Section 4 derives the CSC theoretically and plots it (Figure 2), but there are no experiments showing that violating/preserving the CSC changes convergence behavior. This would be a natural validation of the theory.
- **Discussion of when the compensated learning rate violates practical constraints**: The compensated learning rate $\tilde{\eta}(t,c) = \eta(t)/\H_c(R_t)$ could exceed 1 or violate stability constraints. The paper does not discuss this limitation.
- **Testing the heuristic schedule on the CIFAR10/Wikitext2 settings**: The heuristic is only tested on synthetic data (Figure 6); applying it to the real-data settings used in Figure 1 would broaden its empirical support.

## Removed Points
- The harsh critic raised concerns about "the bound contains exponential factors that could vitiate the asymptotic guarantee in practice" — kept as Minor #3 (it is a verifiable fact about the bound's structure).
- The harsh critic's point about "No empirical evaluation of the stability criterion" — moved to Nice-to-Haves; the paper does not claim to validate CSC experimentally.
- The harsh critic's point about "compensated learning rate may violate constraints" — moved to Nice-to-Haves; this is a speculation about a potential practical issue.

## Novel Insights
None beyond the paper's own contributions. The review process did not surface an insight about the work that is not already present in the paper itself.

## Suggestions
1. **Reconcile framing with evidence**: Rephrase the abstract and introduction to clearly signal that the theory applies to high-dimensional least-squares problems (with linear models), and that the connection to neural network training is speculative future work. This would strengthen rather than weaken the paper by setting appropriate reader expectations.
2. **Characterize the heuristic's empirical scope**: Test the heuristic schedule on the CIFAR10 and Wikitext2 random-feature settings used in Figure 1, or at minimum, add a discussion of the regimes where the heuristic is expected to work.
3. **Provide guidance on when the Theorem 1 bound is non-vacuous**: Even a brief discussion or a plot showing the bound as a function of $n/d$ for representative parameter values would help readers understand the regime in which the theory applies.
4. **Add an explicit statement distinguishing the heuristic from the max-CCC schedule's guarantee** in the abstract or near the heuristic's description, e.g., "the heuristic has no proven guarantee but closely matches the provably optimal schedule in our experiments."

## Score and Decision

MY FINAL SCORE: <score>7</score>
MY FINAL DECISION: <decision>Accept</decision>