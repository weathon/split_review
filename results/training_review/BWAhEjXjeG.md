I now have a thorough understanding of the paper and all reviewer claims. Let me compose the final consolidated review.

---

## Summary

This paper addresses two limitations of Randomized Smoothed Conformal Prediction (RSCP): (1) its robustness guarantee is invalid when Monte Carlo sampling is used (because the estimation error is unbounded), and (2) RSCP produces overly large (sometimes trivial) prediction sets. The authors propose RSCP+, which uses the Monte Carlo estimator directly as the conformity score and bounds its error via Hoeffding's inequality, providing a provable robustness guarantee. They further propose two methods — Post-Training Transformation (PTT) and Robust Conformal Training (RCT) — that dramatically reduce prediction set size while preserving the guarantee. Experiments on CIFAR10, CIFAR100, and ImageNet show that the baseline yields trivial prediction sets (all classes), while PTT/RCT boost efficiency by up to 16.9×.

## Strengths

- **Identifies and fixes a genuine flaw in RSCP's robustness certification.** The paper correctly points out (Section 3) that RSCP's guarantee is invalid when Monte Carlo estimation replaces the intractable expectation without bounding the estimation error. RSCP+ resolves this by incorporating the Monte Carlo estimator directly as the conformity score and providing a rigorous bound via Hoeffding's inequality (Theorem 1). This is a clean, well-motivated fix to a real gap in the literature.

- **Proposes two methods (PTT and RCT) that dramatically improve efficiency.** The experiments show that without PTT/RCT, the RSCP+ baseline yields trivial prediction sets (all classes). PTT and RCT reduce set size by up to 4.36×, 5.46×, and 16.9× on CIFAR10, CIFAR100, and ImageNet respectively — transforming the method from unusable to informative. These are large, practically meaningful improvements.

- **Provides a principled theoretical motivation for PTT.** The linear approximation of the coverage gap (Eq. 8: $\covgap \approx \Phi_S'(\tau) \cdot M_\epsilon$) directly motivates reducing the slope of the score CDF near the threshold. The ranking+sigmoid transformation is a clean instantiation of this idea. The paper also explicitly acknowledges a case where PTT may not help (Appendix) and shows it consistently works in practice.

- **Demonstrates orthogonality of PTT/RCT to the robustness framework.** The remark (end of Section 3.2) correctly notes that PTT and RCT apply to both RSCP+ and the original RSCP, increasing the impact of the efficiency methods beyond the authors' own framework. Results on RSCP+PTT/RCT are provided in the appendix.

- **Extends conformal training to the robust adversarial setting.** RCT adapts the differentiable conformal training pipeline from Stutz et al. to include randomized smoothing and threshold adjustment, making the framework trainable for robust conformal prediction.

## Weaknesses

### Fatal

None.

### Major

- **Missing empirical coverage verification.** The paper reports only average set size, not empirical coverage on clean or adversarially perturbed test sets. The authors state (Section 5) that coverage is "guaranteed by our theoretical results," and while the theory appears sound, this is a significant omission for a conformal prediction paper. Empirical coverage verification serves as a crucial sanity check against implementation bugs or unaccounted randomness. Without it, the efficiency numbers (set sizes) could be misleading if coverage is accidentally violated. Reporting coverage with error bars for each method and dataset is standard practice and should be included.

- **Baseline comparison conflates two sources of conservativeness.** The baseline applies the original RSCP (HPS/APS) scores *within the RSCP+ framework*, which adds a concentration term (~0.122 for the chosen parameters) to the threshold on top of the standard RSCP adjustment $\epsilon/\sigma$. This additional term likely contributes substantially to the baseline's triviality. The paper does not include a direct comparison to the *original RSCP* (without the concentration term) in the main results. Without this comparison, it is unclear whether the triviality is inherent to the robust framework or primarily caused by the concentration term added by RSCP+. A table showing (a) original RSCP set size/coverage, (b) RSCP+ baseline set size/coverage, and (c) RSCP+PTT/RCT would clarify the source of conservativeness and strengthen the paper's claims.

### Minor

- **Probabilistic composition of guarantees is not explained in main text.** The coverage guarantee involves two probabilistic statements: the conformal prediction's marginal guarantee (over calibration+test randomness) and the high-probability bound on the Monte Carlo error (with probability $1-\beta$). The main text does not explain how these compose — e.g., whether the final guarantee is $1-\alpha$ or $1-\alpha-\beta$. While the practical impact is tiny ($\beta=0.001$), the paper should state this clearly to avoid any theoretical ambiguity.

- **Linear approximation in coverage gap analysis is acknowledged but not rigorously justified.** Eq. (8) uses $\covgap \approx \Phi_S'(\tau) \cdot M_\epsilon$, which assumes linearity over an interval of size $M_\epsilon$. The paper calls this an "approximation," and the appendix provides additional analysis on synthetic data. However, for large $\epsilon/\sigma$ ratios (especially on ImageNet with $\epsilon=0.25$), the linearity assumption may break down. The scope of this concern is limited because the approximation is used only for motivation, not as a proof step, but a more precise discussion would help.

- **Sensitivity of PTT hyperparameters ($b$, $T$) is not explored in the main text.** The sigmoid temperature $T=1/400$ is very small, making the transformed scores nearly binary (close to 0 or 1), which could cause numerical issues in the subsequent randomized smoothing. A brief ablation or sensitivity analysis (e.g., set size as a function of $T$ and $b$) in the main text would strengthen confidence in the method's robustness to hyperparameter choice.

- **The concentration term's contribution to threshold inflation is not discussed.** For $\beta=0.001$, $N_{\text{MC}}=256$, the concentration term is $\sqrt{\log(2/\beta)/(2N_{\text{MC}})} \approx 0.122$. Relative to $\epsilon/\sigma$ (e.g., $\epsilon/\sigma=0.5$), this is a ~24% increase, which is non-negligible. Discussing this trade-off and how $\beta$ and $N_{\text{MC}}$ were chosen would help readers understand the cost of the provable guarantee.

### Trivial

None.

## Nice-to-Haves

- Compare to adversarially trained classifiers as a stronger underlying model for the RSCP baseline.
- Show histograms of score distributions before and after PTT to illustrate how the transformation reduces the slope near the threshold.
- Include example prediction sets (e.g., CIFAR-10 images) to provide intuitive visualization of the improvement.
- Vary $\epsilon$ and $\sigma$ to demonstrate the robustness-utility trade-off across a range of perturbation budgets.

## Removed Points

The following criticisms from the reviews were removed with justification:

1. **Criticism about Lipschitz continuity derivation being incorrect** (Harsh Critic, Section 2.2). The claim that $\Phi^{-1}$ is not globally Lipschitz and that the Lipschitz constant is not $1/\sigma$ is incorrect. The $1/\sigma$ Lipschitz constant for the composed function $g(x)=\Phi^{-1}(\mathbb{E}_\delta[f(x+\delta)])$ is a standard, proven result from Cohen et al. (2019, Proposition 1). The critic's objection misunderstands how the composition yields this constant.

2. **Criticism about lacking empirical demonstration that RSCP actually fails** (Harsh Critic, Section 3). The paper's contribution is *theoretical* — identifying a flaw in the mathematical guarantee. The paper explicitly states RSCP works "empirically working well" (line 29). Demanding empirical failure demonstration misunderstands the nature of the contribution.

3. **Criticism about "introduction/abstract phrasing is misleading"** (Harsh Critic). The paper clearly states the baseline is original RSCP scores applied within the RSCP+ framework. The phrasing about trivial predictions is in reference to this baseline, which is clearly described.

## Novel Insights

The most insightful observation across the reviews is that the paper's primary experimental challenge — trivial prediction sets — may be partly self-inflicted by the concentration term that RSCP+ adds to the threshold. This creates an interesting tension: the very term that provides the provable guarantee also destroys usability, and the paper's main contribution (PTT/RCT) is to undo this damage. This dynamic means that the magnitude of the efficiency improvement depends directly on the size of the concentration term, which is a function of $\beta$ and $N_{\text{MC}}$. A more thorough analysis separating the conservativeness of RSCP from the conservativeness of the concentration term would sharpen the paper's narrative.

## Suggestions

- **Add empirical coverage results.** Report empirical coverage (with error bars) on both clean and $\ell_2$-adversarially perturbed test sets for all methods (baseline, +PTT, +RCT, +PTT+RCT) on all three datasets. This is the single most important addition.

- **Include a direct comparison to original RSCP.** Add a row showing original RSCP (threshold adjusted only by $\epsilon/\sigma$, without concentration term) to the main efficiency tables. This separates the conservativeness inherent to the robust framework from the conservativeness added by the concentration bound.

- **Clarify the probabilistic composition of guarantees.** State explicitly whether the overall coverage guarantee is $1-\alpha$ or $1-\alpha-\beta$ (or similar), and explain how the high-probability bound interacts with the conformal prediction guarantee.

- **Add a brief hyperparameter analysis.** Show how set size varies with $T$ (e.g., 1/100, 1/200, 1/400, 1/800) and $b$ (e.g., 0.85, 0.90, 0.95) on a validation set to justify the chosen values and demonstrate stability.

## Score and Decision

This paper makes genuine contributions: it identifies a real gap in RSCP's theoretical guarantee, provides a clean fix (RSCP+), and proposes two effective methods (PTT and RCT) that dramatically improve efficiency. The theoretical contribution is sound and the efficiency gains are large and practically meaningful. However, the paper is weakened by the absence of empirical coverage verification — a standard experimental component in conformal prediction work — and by a baseline comparison that conflates two sources of conservativeness without disentangling them. These issues are addressable but non-trivial. The paper is acceptable with these revisions, but the gaps prevent it from being a **strong** accept in its current form.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>