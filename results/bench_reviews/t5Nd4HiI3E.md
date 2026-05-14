Now I have all the evidence needed. Let me write the review.

## Summary

This paper studies preference optimization for Large Reasoning Models (LRMs) and identifies a key challenge: the intractable marginal preference objective over reasoning traces is replaced by a single-sample trace-based gradient, which introduces high variance. The authors propose BVPO, which mixes the noisy trace-based gradient $g_t$ with a low-variance empty-trace gradient $g_e$ (obtained by suppressing reasoning trace generation) via convex combination $g_c = \alpha g_t + (1-\alpha)g_e$. The paper provides theoretical results on variance reduction, MSE-optimal mixing, and SGD convergence, and demonstrates consistent empirical gains across three LRMs (1.5B–8B) on AlpacaEval 2 and Arena-Hard, while also reporting improvements on math reasoning benchmarks.

## Strengths

- **Well-motivated problem with practical importance.** The paper identifies a genuine gap: existing preference optimization methods (DPO, SimPO, etc.) were developed for conventional LLMs and ignore the unique challenge of trace-induced gradient variance when applied to LRMs. The formalization of the marginal vs. trace-based objective (Section 3.2) clearly articulates why this matters.

- **Consistent and substantial empirical gains across multiple settings.** Table 1 shows BVPO outperforms the best baseline (DPO or SimPO) by up to 7.8 points on AlpacaEval 2 Win Rate and 6.8 points on Arena-Hard, across three LRMs (1.5B, 7B, 8B) and both Thinking/NoThinking modes. The gains are systematic — BVPO wins on all 18 reported cells (6 metrics × 3 models).

- **Clean theoretical connection between MSE and SGD convergence.** Theorems 3 and 4 formally link the MSE of the gradient estimator to the convergence bound of SGD, providing a principled rationale for MSE minimization. This bridges statistical estimator quality and algorithmic optimization behavior.

- **Simple, practical, drop-in design.** BVPO requires only adding an empty-trace loss term alongside the standard trace-based loss. It is agnostic to the underlying preference optimization algorithm (instantiated with DPO in experiments) and does not require additional data collection, making adoption straightforward.

- **Surprising but reported reasoning improvement.** Table 2 shows that BVPO, trained only on general conversational data, improves average math reasoning performance by up to 4.0 points — an interesting observation that, while mechanistically unexplained, is honestly reported.

## Weaknesses

### Fatal
None.

### Major

- **Missing α ablation — the core mechanism is unvalidated.** The paper claims BVPO works by optimally balancing bias and variance through the mixing coefficient $\alpha$. However, no ablation study varying $\alpha$ is reported — the paper never shows what $\alpha$ was used, how sensitive performance is to this hyperparameter, or whether intermediate $\alpha$ values outperform the extremes ($\alpha=0$ or $\alpha=1$). Without this, the empirical results cannot distinguish between the claimed bias-variance trade-off mechanism and alternative explanations (e.g., the empty-trace loss acts as a regularizer, or simply having more gradient signal helps). This is the single most important piece of missing evidence for the paper's central claim.

- **No direct measurement of gradient variance during training.** The paper attributes BVPO's success to variance reduction from trace sampling, but never measures gradient variance (or a proxy) for any method during training. Appendix B reportedly measures variance of log-probabilities and response lengths, but this does not directly measure gradient variance, which depends additionally on the loss landscape and model parameters. Without variance measurements, the claimed mechanism is untestable from the presented experiments.

- **Missing comparison to alternative variance reduction techniques.** Standard approaches such as larger batch sizes, gradient accumulation, or Polyak averaging would also reduce gradient variance. Without comparing against these, it is unclear whether BVPO's specific mechanism matters or whether any method that increases the effective gradient signal would perform similarly.

### Minor

- **Optimal $\alpha^*$ is a theoretical reference, not a practical prescription.** Theorem 2 derives a closed-form MSE-optimal mixing coefficient, but it depends on unknown quantities ($\mu$, biases, covariances). The paper never explains how $\alpha$ is actually chosen in experiments, creating a gap between the theory and the empirical implementation. This is standard in bias-variance trade-off work but should be discussed.

- **Theorem 4's optimality claim requires $\eta L = 1$.** The equivalence between MSE-minimization and convergence-error-minimization holds only in this specific condition. The paper acknowledges this but the restriction limits the generality of the "algorithmic optimality" claim. In practice, $\eta L = 1$ is a known condition in the theory but is not verified in the experiments.

- **Statistical significance on small test sets.** Several math reasoning benchmarks (AIME 2024, AIME 2025) have only 30 problems. While avg@32 evaluation is used, no confidence intervals or significance tests are reported, making it difficult to assess whether improvements (e.g., 2–3 point gains on AIME 2025) are reliable.

- **The reasoning improvement from non-math data is unexplained.** The paper reports that training only on general conversational data improves math reasoning, but offers no analysis of why this happens or whether it is a BVPO-specific effect or a general phenomenon (e.g., the base model benefits from any additional fine-tuning). This does not undermine the alignment results but leaves an important empirical finding unexamined.

### Trivial

- **The term "estimator" for $g_e$ is used loosely.** $g_e$ is the gradient of the empty-trace loss, not a sampling-based estimator of the marginal gradient $\mu$ in the traditional Monte Carlo sense. The paper defines its bias explicitly relative to $\mu$, so the MSE analysis is mathematically valid, but the terminology could mislead readers. Clarifying this would help.

## Nice-to-Haves

- An ablation of $\alpha$ on at least one model/benchmark pair to validate the bias-variance trade-off mechanism.
- Gradient variance measurements (or a proxy like per-step gradient norm variance) for DPO, SimPO, and BVPO during training.
- Comparison to DPO with larger batch sizes or gradient accumulation as a control for the "more gradient signal" alternative.
- Confidence intervals for small-test-set benchmarks.

## Removed Points

The following criticisms from the harsh reviewer are removed or weakened after verification against the paper:

1. **"$g_e$ is not a valid estimator; the entire theoretical framework collapses."** — Removed. The paper explicitly defines bias vectors $b_t, b_e$ relative to $\mu$ and acknowledges $g_e$ has "potentially higher bias." The MSE framework is mathematically valid for any pair of gradient vectors with defined first/second moments. The bias is a feature of the trade-off, not a flaw in the theory. The critic's claim of "structural collapse" is an overstatement.

2. **"Theorem 1 is trivial/vacuous."** — Removed. The result that $\text{Var}(g_c) = \alpha^2 \text{Var}(g_t)$ is mathematically simple but not vacuous — it establishes that $g_e$ being deterministic w.r.t. trace sampling creates a guaranteed variance reduction. This is a real property that depends on the specific construction of $g_e$.

3. **"Contradiction: training on general data improves math reasoning contradicts the theory."** — Removed. The paper reports this as an empirical observation, not a theoretical prediction. There is no contradiction; the paper does not claim the theory predicts this outcome.

4. **"Appending 'thinking response' is not an empty reasoning trace."** — Removed. In DeepSeek R1 models, the `