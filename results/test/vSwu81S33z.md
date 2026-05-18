Here is the consolidated review:

## Summary

This paper introduces Nonparametric Transfer Learning (NPTL), adapting the Bayesian nonparametric learning (NPL) framework to transfer learning. The key idea is to construct a Dirichlet Process prior whose base measure is built from a linear-probed model (pseudo-labels on downstream inputs), then sample from the posterior by solving weighted optimization problems with block-Dirichlet-sampled weights. The method is designed to handle distribution shifts between upstream and downstream data, where standard weight-space Gaussian priors may be misspecified. Experiments on vision (ResNet-20x4, ResNet-50, ViT-B/16) and language (RoBERTa-Base) tasks show that NPTL posterior samples yield competitive or superior BMA performance compared to SGHMC and ensemble baselines with L2SP/PTYL priors.

## Strengths

1. **Principled adaptation of NPL to transfer learning.** The paper identifies a natural connection: NPL's robustness to model misspecification (via its nonparametric DP prior) is directly relevant to transfer learning, where the upstream-trained model may be a poor fit for the downstream task. The construction — using a linear-probed model on downstream inputs to build the base measure and a DP posterior that combines actual and pseudo-data in a weighted manner — is a clean and well-motivated algorithmic adaptation (Sections 3.1–3.2).

2. **Empirically competitive BMA performance across diverse settings.** The method is evaluated on vision (3 architectures × 4–5 datasets each), language (RoBERTa-Base on 3 GLUE tasks), and robustness (CIFAR-10-C). NPTL achieves the best or second-best NLL in nearly all configurations, and consistently outperforms standard ensemble baselines on NLL — a metric that directly reflects posterior predictive quality. The CIFAR-10-C results show systematic improvement across all severity levels, supporting the claim that NPTL handles distribution shift.

3. **Practical design choices that enable scaling.** The block Dirichlet distribution reduces sampling from a $2n$-dimensional Dirichlet to $2L$ dimensions ($L \ll n$), making the method feasible for large $n$ (Section 3.2). Empirical Bayes selection of $\alpha$ on a held-out validation set provides a principled, data-driven way to set prior strength. The NPTL-Soup variant (weight averaging of posterior samples via Greedy Soup) yields a single-model approximation competitive with full BMA, addressing inference cost.

4. **Parallel sampling.** Unlike sequential MCMC methods (SGHMC), each NPTL posterior sample is obtained by independently solving a weighted optimization, making the $M$ samples embarrassingly parallel (Algorithm 1). This is a practical advantage for large-scale deep learning.

## Weaknesses

### Major

- **The prior base measure depends on the downstream data, and the implications for uncertainty quantification are not discussed.** The linear-probed head $\mathbf{W}^*$ is trained on the downstream labels (Section 3.1, lines 97–98), and the resulting pseudo-labels $f_{\text{probed}}(x_i)$ are evaluated on the same downstream inputs $x_i$ used in the likelihood. The paper explicitly acknowledges this is an empirical Bayes procedure (line 97). However, this creates a concretely non-standard form of empirical Bayes: the prior carries $n$ pseudo-observations whose "labels" are functions of the downstream training labels, meaning the same downstream data indirectly influences both the prior and the likelihood. The paper does not discuss how this double use of data might affect posterior calibration, coverage, or sharpness. Since the paper's central claim is improved BMA quality (which depends on faithful uncertainty), this limitation should at minimum be acknowledged and ideally analyzed (e.g., via comparison to a variant that constructs the base measure from a disjoint subset). Unlike textbook empirical Bayes (which estimates a small number of hyperparameters), here the entire pseudo-dataset is data-dependent, making the issue more salient.

### Minor

- **Statistical significance of improvements is unclear.** The reported standard deviations often overlap between NPTL and the best baselines (e.g., Table R20_bma: NPTL NLL 0.148±0.013 vs Ens+L2SP 0.163±0.015 — the ranges overlap within roughly 1 standard deviation). No statistical significance tests are reported. Given that NPTL has comparable computational cost to ensembles ($M$ independent optimizations), the practical advantage would be clearer with confidence intervals or paired comparisons.

- **Sensitivity analysis for key hyperparameter $\alpha$ is absent.** The hyperparameter $\alpha$, which controls prior strength, is selected by minimizing NLL on a 10% validation set. No analysis is provided showing how performance varies with $\alpha$ or whether the method is robust to its choice. Since $\alpha$ determines the balance between the prior pseudo-data and the observed data, this is a critical tuning knob whose sensitivity should be reported.

- **The weighted SGD implementation is underspecified.** The objective (Equation 5, lines 137–138) weights each training example individually via block-Dirichlet-sampled weights, but the paper does not describe how per-example weights are incorporated into minibatch SGD. Clarifying whether weights are used for importance sampling or loss re-weighting would aid reproducibility (this is a straightforward detail that can be addressed in a few sentences).

### Trivial

- The number of blocks $L$ in the block Dirichlet approximation is not discussed in the main paper; its effect on sampling quality versus computational cost is deferred entirely to the appendix.
- The reader must infer from context that "Ensemble" (a separate baseline) uses standard fine-tuning without L2SP/PTYL regularization — this could be stated more explicitly.

## Nice-to-Haves

- Comparison to SWAG and MC Dropout would strengthen the empirical positioning but is not essential given the existing baselines.
- Reporting wall-clock or FLOPs cost of NPTL relative to ensembles would help practitioners evaluate the practical trade-off.
- An analysis of the impact of the block Dirichlet approximation on the quality of posterior samples (comparing to exact sampling for small $n$) would strengthen confidence in the method.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Parallelization claim is overstated:** The reviewer argues this because ensembles are also parallelizable. However, the paper explicitly contrasts with *MCMC methods* (line 25: "such parallelization is not straightforward for stochastic gradient Markov Chain Monte Carlo (MCMC) methods"), not with ensembles. This criticism misreads the paper's claim. → **Removed as factually inaccurate.**

- **Missing baselines (simple deep ensembles, SWAG, MC Dropout):** The paper already includes Ensemble as a baseline (which is a standard deep ensemble — multiple fine-tunings from the pre-trained initialization). SWAG and MC Dropout would be informative additions but their absence does not constitute a structural flaw given the existing baselines (SGHMC, Ensemble, Ensemble+L2SP, Ensemble+PTYL). → **Downgraded; listed as Nice-to-Have.**

- **"Ensemble is ambiguous about whether it uses L2SP":** The paper clearly lists Ensemble as a separate method and then describes L2SP and PTYL as additional regularization approaches applied in the "baseline BMA procedure" (lines 168–170). The distinction is clear from context. → **Removed as a misreading.**

- **Block Dirichlet approximation diagnostics not in main paper:** Referencing the appendix for technical analysis is standard practice in page-limited conference submissions. → **Trivial; kept only as a minor note.**

- **Use of downstream training data to construct prior base measure (framed as fatal):** The paper explicitly acknowledges this as empirical Bayes (line 97). While the concern about calibration impact is valid and kept above, the framing as a fatal flaw is disproportionate. The pseudo-dataset uses predicted labels $f_{\text{probed}}(x_i)$, not the actual downstream labels $y_i$, and the linear probe is a highly constrained model (single linear layer on frozen features), limiting the degree of data reuse. → **Downgraded from Fatal to Major with more measured framing.**

## Novel Insights

The reviews surface a tension that the paper itself partially acknowledges but does not fully resolve: the NPL framework's theoretical guarantees (robustness to model misspecification) are developed for the setting where the prior base measure is legitimately prior (independent of the data). The paper's pragmatic adaptation — using the downstream data to build the base measure — gives up this independence. This is not fatal (empirical Bayes routinely trades off some theoretical purity for practical effectiveness), but it means the theoretical motivation for NPL's robustness does not automatically carry over to NPTL. A thoughtful analysis: under what conditions does using the downstream data to build the base measure actually *help* (vs. hurt) uncertainty quantification? The CIFAR-10-C results suggest it helps empirically, but a deeper understanding would strengthen the contribution.

## Suggestions

- Add a brief discussion of the double-use-of-data issue in the main paper, acknowledging the limitation and explaining why the empirical Bayes construction is reasonable despite it (e.g., the linear probe is a highly constrained model, and the pseudo-labels differ from the true labels).
- Report confidence intervals, error bars from multiple seeds, or simple paired statistical tests for the main results.
- Include a sensitivity plot (or table) for $\alpha$ across one or two datasets to demonstrate robustness.
- Clarify the SGD weighting scheme: state explicitly that each minibatch computes a weighted average of per-example losses using the assigned block weights.

## Score and Decision

The paper introduces a well-motivated adaptation of nonparametric learning to transfer learning, with extensive experiments and practical algorithmic contributions (block Dirichlet, NPTL-Soup). The core weakness is that the data-dependent construction of the prior base measure is acknowledged but its implications for uncertainty quantification are not discussed. This is a real limitation but not a fatal one — the empirical results stand as evidence that the method works. The paper would benefit from addressing this in revision and from tighter statistical reporting, but the contribution is solid and clearly presented.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>