## Summary

The paper argues that diffusion models in high-dimensional settings do not actually learn the statistical quantities (posterior distributions, score functions, velocity fields) prescribed by their theoretical foundations. It formalizes a "weighted sum degradation" phenomenon: when the true data distribution is treated as an empirical mixture of Dirac deltas, the posterior $p(x_0|x_t)$ collapses to a point mass at the nearest training sample in high-dimensional spaces. Empirical evidence is provided on ImageNet-256 and ImageNet-512. Building on this, the paper proposes a "Natural Inference" framework that re-interprets and unifies existing inference algorithms (DDPM, DDIM, Euler, DPM-Solver, DPM-Solver++, DEIS) as autoregressive linear combinations of $x_0$ predictions, without invoking any statistical concepts.

---

## Strengths

- **Concrete formalization of a genuine phenomenon.** The derivation of $p(x_0|x_t)$ under the empirical data distribution (Section 3.1–3.2) is technically sound and the empirical verification on ImageNet (Tables 1–2) is compelling. The degradation rates are dramatic: for VP at $t<600$, nearly 100% of samples show full degradation on both datasets.

- **Broad unification of inference algorithms.** Section 4 systematically shows that DDPM ancestral sampling, DDIM, Euler ODE/SDE, DPM-Solver, DPM-Solver++, and DEIS all fit within the Natural Inference framework as linear combinations of $x_0$ predictions. This is a useful synthesis rarely presented in a single framework.

- **Intuitive, accessible re-framing.** The frequency-spectrum interpretation (Section 3.3) — connecting the training objective to "predict filtered high-frequency components" — is an independently appealing perspective that connects to Dieleman (2024). The analogy between Self Guidance and unsharp masking is also instructive.

---

## Weaknesses

### Fatal
None that fully invalidate the core observations; however, the primary inferential leap is severely overstated (see Major).

### Major

1. **Central claim overreaches the evidence.** The paper's key conclusion — "diffusion models do not learn statistical quantities" — does not follow rigorously from the weighted sum degradation observation. The argument conflates the degraded *training signal at a specific $(x_0, x_t)$ pair* with the *learned model function over all of input space*. Even when each individual training target is dominated by a single sample, the model fits a smooth function across millions of distinct $(x_0, x_t)$ pairs. This is precisely how empirical risk minimization works: neural networks generalize well beyond individual training data points. The paper provides no evidence that the model's actual outputs are "nearest-neighbor lookups" rather than approximations of the true posterior mean.

2. **No direct experimental verification of the alternative hypothesis.** The paper claims the model works "via a different mechanism," but never directly tests this. A compelling test would be: at a given $x_t$, compare the model's predicted $x_0$ to the nearest training sample and to the true posterior mean (computable for controlled, small-dimensional settings). Without this, the paper demonstrates that the *training target* is degenerate but does not show that the *model output* is degenerate.

3. **Limited novelty of the Natural Inference framework.** The core observation that all inference steps can be written as linear combinations of $x_0$ predictions and independent noise vectors is well known in the community — it is essentially the "predict-$x_0$" parameterization already standard in the literature (e.g., used in DDIM's analysis). The "autoregressive" structure is a direct consequence of the iterative update rules, not a discovery. The framework unifies methods elegantly but does not enable any new algorithms or new theoretical results.

4. **Degradation threshold is arbitrary and not ablated.** The 90% threshold ($p(x_0 = X_0') > 0.9$) that defines "degradation" is stated without justification. Sensitivity to this threshold — and how the probability is actually computed over a finite but very large training set — is not analyzed.

### Minor

- The claim "the actual degradation ratio should be higher than the statistics show" (due to limited sampling) contradicts the empirical setup: degradation was measured directly by computing the discrete posterior over the training set. More training samples would *reduce* degradation by providing more candidates that may be nearby. This argument is inverted.

- The Self Guidance formulation (Section 4.1) is described as new, but the operation of extrapolating/interpolating between consecutive $x_0$ predictions at different noise levels is implicit in DDIM and related analyses. The CFG analogy is loose: CFG contrasts two different conditioning signals, while Self Guidance contrasts the same model at different noise levels.

### Trivial

- Figures 7–14 are described but located in the appendix that was stripped by the parser; the paper's core claims in Section 4.3 rely on them for quantitative support.

---

## Nice-to-Haves

- A controlled experiment in a moderate-dimensional regime (e.g., CIFAR-10 latents or toy Gaussian mixtures) comparing model outputs to true posterior means and to nearest-neighbor outputs would directly validate or refute the core claim.
- An analysis of how generalization (training on many distinct $(x_0, x_t)$ pairs) might still allow the model to implicitly learn statistical quantities despite the per-sample degradation.
- Demonstrating a practical benefit of the Natural Inference framework — e.g., a new sampling schedule derived from it that achieves better FID — would substantially strengthen the contribution.

---

## Novel Insights

The paper's most genuinely novel contribution is the precise quantification of weighted sum degradation on real datasets: it shows that for VP noise schedules on ImageNet, at $t < 500$, virtually every training sample $(x_0, x_t)$ has a posterior dominated (>90%) by the single nearest training example. This is a concrete empirical fact about the training regime of large-scale diffusion models that has not been systematically measured before. The frequency-spectrum interpretation builds on Dieleman (2024) but provides a useful, self-contained synthesis connecting training objective to inference behavior.

---

## Suggestions

- Clearly separate "the empirical training target is degenerate" from "the model cannot learn statistical quantities." The former is demonstrated; the latter requires additional experimental evidence.
- Derive at least one new, practically usable sampling strategy from the Natural Inference framework and evaluate it against baselines on FID or other metrics.
- Analyze the approximation error in representing existing samplers as Natural Inference for the common practical regime of 20–50 steps (not just asymptotically many steps).

---

## Score and Decision

The paper raises a legitimate and under-examined question about how high-dimensional diffusion models actually function. The weighted sum degradation analysis is rigorous and the empirical verification is compelling. However, the main inferential leap — from "training targets are degenerate" to "the model cannot learn statistical quantities" — is not supported by direct evidence, conflates the training signal with the learned function, and bypasses the standard understanding of generalization. The Natural Inference unification, while a clean presentation, does not offer new algorithmic or theoretical results. As a result, the paper is an intellectually stimulating perspective piece with a significant logical gap at its center and limited practical impact.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>