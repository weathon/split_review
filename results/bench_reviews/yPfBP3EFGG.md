## Summary

This paper proposes STNAdam, a stochastic variant of Adam for "nonconvex + weakly-convex" composite optimization that maintains two coupled iteration trajectories — an extrapolation track and a regular update track — governed by Nesterov momentum and adaptive conditioning. The algorithm is designed to accommodate arbitrary variance-reduced gradient estimators (SVRG, SAGA, SARAH), and the authors provide a convergence analysis under the Kurdyka-Łojasiewicz property proving almost-sure convergence to a stationary point with explicit rates. Empirical results on low-light image enhancement (LIE) using the LOL dataset show that STNAdam-SARAH achieves PSNR 22.26, SSIM 0.906, and LPIPS 0.050, outperforming several baselines including SGD, Adam, SNAdam, and specialized LIE algorithms.

## Strengths

- **Novel two-track coupled iteration framework.** The idea of maintaining separate extrapolation and regular update trajectories that interactively inform each other (Algorithm 1, Figure 1) goes beyond existing single-track methods like NAdam and SNAdam. This design is conceptually interesting and could be a genuine algorithmic contribution if validated.

- **General convergence analysis with flexible gradient estimators.** Theorem 1 establishes almost-sure convergence of the sequence $\{\bar{x}^k\}$ to a stationary point under the KL property, and Theorem 2 provides explicit convergence rates for $\{\tilde{x}^k\}$ that depend on the KL exponent. The analysis is designed to accommodate *any* variance-reduced gradient estimator satisfying the MSE bound and geometric decay conditions in Lemma 1 (SVRG, SAGA, SARAH, SPIDER), which is more general than existing stochastic Adam analyses that typically target a single estimator.

- **Strong empirical numbers on the LOL dataset.** STNAdam-SARAH achieves PSNR 22.26, SSIM 0.906, and LPIPS 0.050, substantially outperforming both generic optimizers (e.g., SNAdam at 17.14 PSNR) and specialized LIE methods (e.g., Retinex-Net at 18.44 PSNR). Visual results in Figure 2 show noticeably sharper detail preservation.

## Weaknesses

### Fatal
None.

### Major

- **Experimental evaluation is far too thin to support the claimed superiority.** Only one dataset (LOL) is used. No error bars, confidence intervals, or statistical significance tests are reported. No ablation studies isolate the effect of the two-track mechanism — the core algorithmic novelty — from other design choices (e.g., variance reduction, adaptive step sizes). The timing values (e.g., $2.64\times10^{-5}$ seconds for STNAdam-SARAH) are reported without specifying whether they are per-iteration, per-image, or total, and without describing image sizes or batch details. Without these controls, the headline numerical advantages cannot be reliably attributed to the two-track framework rather than to hyperparameter choices or dataset-specific overfitting.

- **Citation error:** The paper's experiments section states "SAdam (Kingma & Ba, 2014)" (line 285). Kingma & Ba proposed *Adam*, not SAdam. The introduction correctly cites Le-Duc et al. (2024) for SAdam, so this appears to be a careless mistake that nonetheless undermines confidence in the experimental setup.

- **The claim about "removing hand-tuning" via dynamic parameter scheduling is not supported.** The parameter intervals in (6)–(8) depend on unknown constants: $V_1, V_\Upsilon, \rho$ from Lemma 1 (which are properties of the gradient estimator and not specified for any concrete estimator), the Lipschitz modulus $L$, the weak-convexity constant $\tau$, and the energy-function parameters $M$ and $s$. The paper does not explain how a practitioner would determine these quantities for a given problem. Moreover, the interval for $\lambda_{k+1}$ in (7) requires $\delta < 0.6$ (so that $6 - 10\delta > 0$), where $\delta$ depends on $\hat{\pi}_{k+1}$, which is stochastic and iterate-dependent — establishing that this condition holds for all $k$ requires global bounds on $\hat{\pi}_{k+1}$ that are not provided. The phrase "removing hand-tuning" is therefore misleading; these intervals are a theoretical existence result rather than a practical recipe.

### Minor

- **Limited scrutiny of the core theoretical machinery.** The convergence analysis depends on an energy function (9) with auxiliary parameters ($M, H, Z, D$) whose existence is asserted but not explicitly constructed, and on eight positive coefficients $A_i$ in Lemma 2 whose existence is relegated to the appendix (which was stripped). While this structure is common in optimization proofs, the coupling between $M$ (used to define the energy function) and $\underline{\gamma}$ (which depends on $M$ via (6)) creates a dependency chain that requires careful verification that the intervals are non-empty and the $A_i$ are positive simultaneously. Without the appendix, these claims cannot be fully evaluated.

- **Half-norm regularization is non-standard and unexplained.** The LIE model (14) includes the term $\|\nabla L\|_{1/2}^{1/2}$, which is an unusual regularizer whose proximal operator is not standard and is not discussed.

### Trivial
None.

## Nice-to-Haves
- An ablation comparing STNAdam against a version using only one track (e.g., removing the extrapolation track) would directly validate the core claim.
- Convergence curves (loss vs. iteration) for all methods would clarify whether STNAdam converges faster or to a better value.
- Additional LIE benchmarks (e.g., MIT-Adobe FiveK, SCIE) would strengthen the experimental support.
- A comparison to NAdam (Dozat, 2016) would help isolate the effect of the two-track mechanism from Nesterov acceleration.

## Removed Points
Points flagged for removal (treated with caution):

- **Circular dependency claim.** The harsh critic's claim that $M$ in (6) and (9) creates a "circular dependency" is overstated. This pattern — define an energy function with free parameters, then show that algorithm parameters can be chosen to make it decrease — is standard in optimization theory. The practical concern about unknown constants (kept above) is the real issue.

- **Algorithm description confusion.** The critic's complaint that "the relationship between these sequences and the final output is never resolved" is inaccurate. Algorithm 1 clearly defines three variables ($x^{k+1}$, $\bar{x}^{k+1}$, $\tilde{x}^{k+1}$) with distinct roles, Theorem 1 proves convergence of $\{\bar{x}^k\}$, and Theorem 2 proves convergence rates for $\{\tilde{x}^k\}$. The description is adequate.

- **Generic strengths.** The Strength Finder's "explicit adaptive update rules for parameters" conflicts with the verified weakness about practical computability and is removed. "Compatibility with multiple variance-reduced gradient estimators" is genuine but already reflected in the Strengths section.

- **Speculative claims about proof errors.** The critic's assertion that "it is highly likely that the analysis contains gaps that cannot be fixed by minor revisions" is speculation without evidence. Without the appendix, this cannot be verified, and the main body's proof structure is standard for KL-based convergence analyses.

- **Pure formatting/style nitpicks** and missing-appendix complaints.

## Novel Insights

The two-track iteration framework is the paper's most distinctive idea. By decoupling the point used for gradient evaluation ($x^k$) from the point used for extrapolation ($\bar{x}^k$) and from the output ($\tilde{x}^k$), STNAdam attempts to combine the benefits of Nesterov-style lookahead with Adam-style adaptive conditioning while mitigating instability from stochastic gradients. This three-variable architecture goes beyond the standard NAdam approach of a single interpolated gradient direction and provides a template that could be applied to other adaptive optimizers beyond Adam (e.g., RMSprop, AdaBelief). The parallel analysis of $\{\bar{x}^k\}$ and $\{\tilde{x}^k\}$ using two different convergence metrics is also a reasonable formal framework for this design. However, these conceptual contributions remain incompletely validated by the current experimental evidence.

## Suggestions

1. **Fix the citation error** — SAdam should not be attributed to Kingma & Ba (2014). Correct this in the experiments section.

2. **Substantially expand the experiments.** Add at least 2–3 more LIE datasets (e.g., MIT-Adobe FiveK, SCIE). Report all metrics with error bars over multiple runs. Include convergence curves (loss vs. iteration) for all compared methods.

3. **Add an ablation study** comparing full STNAdam against single-track variants (e.g., remove the $\bar{x}^{k+1}$ extrapolation or replace it with $\bar{x}^{k+1} = x^k$). This is essential to validate the paper's central claim.

4. **Address the practical computability of the parameter intervals.** Either provide concrete procedures to estimate $L$, $\tau$, $V_1$, $V_\Upsilon$, $\rho$ for SAGA/SARAH on the LIE model, or tone down the "removing hand-tuning" claim to clearly state that the intervals are a theoretical existence result.

5. **Clarify the timing metrics.** Specify what "Time(s)" measures (per-iteration? per-image? per-dataset?), report image sizes and batch sizes, and explain how $2.64\times10^{-5}$ seconds is achievable.

## Score and Decision

**Calibration anchors** (all from ICLR 2026 human reviews):

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `/home/wg25r/review_agent/human_reviews_2026/0YDUJznwtX.md` (Simple Adam Proof) | 2.00 | Fundamentally flawed assumptions; STNAdam is substantially stronger in both novelty and theoretical depth. |
| `/home/wg25r/review_agent/human_reviews_2026/jzYUJ24Yis.md` (Role of Stochastic Env) | 3.50 | Similar-level theoretical ambition, but STNAdam has a more novel algorithmic contribution. |
| `/home/wg25r/review_agent/human_reviews_2026/dHxM51W120.md` (Parameter-Free Adaptive) | 4.00 | Comparable: both have clean theory but modest experiments. |
| `/home/wg25r/review_agent/human_reviews_2026/kW5hSRG5wq.md` (Curious Case of AdamW) | 4.50 | Comparable: interesting analysis with limited direct practical validation. |
| `/home/wg25r/review_agent/human_reviews_2026/NI42ANbHBk.md` (Adam vs Gauss-Newton) | 5.00 | Comparable: interesting theoretical insights, somewhat limited experiments. |
| `/home/wg25r/review_agent/human_reviews_2026/awXCOmF6ia.md` (Zeroth-Order) | 5.33 | Slightly stronger: more rigorous theory despite incremental novelty. |
| `/home/wg25r/review_agent/human_reviews_2026/9asuGOncOi.md` (Fast Frank-Wolfe) | 6.00 | Accept-level: clean theory, well-executed experiments, clear contributions. STNAdam is weaker. |
| `/home/wg25r/review_agent/human_reviews_2026/Snfqe4lU3G.md` (Derandomized O2NC) | 6.00 | Accept-level: strong novel theory with decent experiments on CIFAR-10. STNAdam is weaker. |

The paper has a genuinely novel algorithmic idea (two-track framework) and an ambitious theoretical analysis, but the experimental evaluation is too thin to substantiate the claimed advantages, the practical implementability of the parameter scheduling is unaddressed, and there is a citation error. Relative to the anchors, this paper falls below the typical acceptance threshold.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>