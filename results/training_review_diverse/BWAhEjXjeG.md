Now I have a thorough understanding of the paper. Let me synthesize the final consolidated review.

## Summary

This paper addresses robust conformal prediction — generating prediction sets with guaranteed coverage even under adversarial perturbations. It identifies a flaw in the prior RSCP method (its robustness guarantee relies on an intractable expectation approximated by Monte Carlo without bounding the error) and proposes **RSCP+**, which uses the Monte Carlo estimator directly as the conformity score and provides a certified guarantee via concentration inequalities. To combat the conservativeness that makes robust conformal prediction produce trivial (full-label-set) prediction sets, the paper introduces **Post-Training Transformation (PTT)**, a training-free score transformation, and **Robust Conformal Training (RCT)**, a training framework that incorporates the robust conformal pipeline into the learning objective. Experiments on CIFAR10, CIFAR100, and ImageNet show that the baseline (RSCP+) yields trivial sets, while PTT and RCT dramatically reduce set sizes (up to 16.9× on ImageNet).

## Strengths

1. **Identifies a genuine flaw in RSCP and provides a principled fix.** The paper clearly shows that RSCP's robustness guarantee is invalid in practice because it applies Lipschitz continuity to the intractable smoothed score \(\mathbb{E}[S(x+\delta,y)]\) while using a Monte Carlo estimator without bounding the error (Section 3). RSCP+ avoids this gap by using the Monte Carlo estimator \(\hat{S}_{\text{RS}}\) directly as the score, maintaining the i.i.d. property required for conformal prediction and providing a *certified* guarantee via Hoeffding's inequality. This is a clean, well-motivated theoretical contribution.

2. **PTT and RCT produce large, practically meaningful efficiency gains.** Baseline RSCP+ yields trivial predictions (set size = number of classes) on all three datasets. The paper's PTT and RCT reduce set sizes dramatically — e.g., on CIFAR10 with APS, from 10 to 1.90 (PTT) and 1.72 (RCT). On ImageNet, the efficiency boost reaches 16.9×. These results demonstrate that the methods make robust conformal prediction practically usable rather than degenerate.

3. **PTT is training-free and scalable.** The ranking+sigmoid transformation operates on scores post-hoc using a holdout set of only 500 samples, requiring negligible computation. This is a practical advantage that lowers the barrier to adoption.

4. **Comprehensive evaluation across multiple datasets and score functions.** Experiments cover CIFAR10, CIFAR100, and ImageNet with both HPS and APS scores, using ResNet-110 and ResNet-50, with consistent trends. The analysis of Monte Carlo sample count (Fig. SizeVsNmc) provides useful practical guidance on the computation-efficiency trade-off.

5. **Acknowledges limitations.** The paper explicitly discusses a potential failure mode for PTT (Appendix) and notes that PTT's improvement is not guaranteed in all cases, showing balanced scientific reporting.

## Weaknesses

### Fatal
None.

### Major

1. **Empirical coverage verification is absent, especially for PTT and RCT.** The paper reports only average set sizes — never the empirical coverage on either clean or adversarially perturbed data. While RSCP+'s coverage guarantee is theoretical (certified), PTT uses a heuristic linear approximation (Eq. linearApprox) that is not rigorously bounded, and RCT modifies the training objective. The paper argues PTT and RCT are "orthogonal" to the robustness fix, but this claim would be substantially strengthened by showing that empirical coverage actually meets the \(1-\alpha\) target (within error bars) for all methods. Without this, the reader cannot fully verify that the efficiency gains do not come at the cost of coverage violation.

2. **The efficiency comparison does not isolate the cost of the Monte Carlo fix.** The baseline is described as "the vanilla method from Gendler et al. directly equipped with our \algoname" — i.e., RSCP+ without PTT/RCT. The paper does not report the set sizes of *original RSCP* (without the fix). This makes it impossible to determine whether the trivial predictions are inherent to the robust conformal formulation itself, or are substantially worsened by the additional margin from RSCP+'s Monte Carlo correction (\(\epsilon/\sigma + \text{MC error bound}\)). A three-way comparison (vanilla CP → original RSCP → RSCP+) would clarify the source of conservativeness and better calibrate expectations about what PTT/RCT are overcoming.

### Minor

3. **PTT's theoretical justification relies on a heuristic linear approximation with limited validation in the main paper.** The coverage gap analysis uses a first-order Taylor expansion of \(\Phi_{\text{RS}}(\tau + M_\epsilon) - \Phi_{\text{RS}}(\tau) \approx \Phi'_{\text{RS}}(\tau) \cdot M_\epsilon\). The paper acknowledges this is an approximation and provides a synthetic analysis in the appendix, but the main text would benefit from summarizing the conditions under which the approximation is reliable (e.g., Lipschitz constant of the CDF). Additionally, the connection between reducing the slope of \(\Phi_S\) (the base score CDF) and reducing the slope of \(\Phi_{\text{RS}}\) (the smoothed score CDF) is stated as an "approximation" without formal characterization. A figure in the main text showing the empirical CDF before and after PTT, and how the slope at the threshold changes, would substantially strengthen the presentation.

4. **RCT's benefit over the baseline may be partially attributable to additional training, not just the objective.** The RCT experiments start from pre-trained models and then fine-tune with the RCT objective. The baseline uses the same pre-trained model without fine-tuning. While this is a valid comparison, it conflates "training with the RCT objective" with "additional training in general." A controlled ablation where the same architecture is fine-tuned for the same number of steps with a standard cross-entropy objective (or conformal training without the robustness modifications) would isolate the effect of the RCT-specific components. This is not a fatal gap, as the paper's main efficiency contribution is PTT (training-free), but it weakens the standalone standing of RCT.

### Trivial

5. **Notation is overloaded and sometimes confusing.** The paper introduces multiple score notations (\(S\), \(\text{RS}\), \(\hat{S}_{\text{RS}}\), \(\text{SCORE}_{\text{trans}}\), \(\text{SCORE}_{\text{RS}}\)) with inconsistent subscripts. A summary table mapping each score to its definition and role would improve readability.

## Nice-to-Haves

- **Separate ablation of PTT's ranking and sigmoid components.** The paper presents PTT as a two-step transformation (ranking + sigmoid) but only reports the combined result. Showing the contribution of each step (ranking alone, sigmoid alone on uniform scores) would help understand where the efficiency gains come from.
- **Runtime or wall-clock time.** Given that RSCP+ uses 256 Monte Carlo samples per test point, reporting inference cost per sample would help practitioners assess the practical trade-offs.
- **From-scratch training baseline for RCT** (as discussed in Minor weakness 4 above) would strengthen the claim that RCT is a method in its own right.
- **Comparison to original RSCP set sizes** (as discussed in Major weakness 2 above) would help the community understand the full picture.

## Removed Points

- **Criticism about "no empirical verification that coverage guarantee holds" as a fatal flaw.** The paper provides a *certified* (theoretical) robustness guarantee, which is standard in the certified defense literature. Empirical coverage on adversarial examples is not required to validate a theoretical guarantee. However, the concern is retained in Major weakness 1 because PTT uses a heuristic approximation, making empirical validation more relevant for that component.
- **Criticism about strict hyperparameter disclosure or missing code.** These are either addressed by the paper (hyperparameters stated in Section 5) or are standard practical limitations not affecting the validity.
- **Criticism about missing related work.** Not included per instructions since I cannot independently verify existence of missing references.

## Novel Insights

None beyond the paper's own contributions. The reviewer observations mostly echo the paper's self-identified limitations (conservativeness, heuristic approximation) rather than adding new analytical insights.

## Suggestions

1. **Add an empirical coverage table** showing (a) coverage on clean test data and (b) coverage under adversarial perturbation (using the same \(\epsilon\) as the certified setting) for all methods (baseline, PTT, RCT), with standard errors over multiple calibration splits. This directly addresses the most significant gap.
2. **Include original RSCP (without the fix) in the efficiency comparison.** Report set sizes for vanilla CP, original RSCP, RSCP+, RSCP++PTT, and RSCP++RCT. This would disentangle the sources of conservativeness.
3. **Add a figure in the main text** showing the empirical CDF of the base scores before and after PTT, with the threshold \(\tau\) and \(\tau+M_\epsilon\) marked, to visually demonstrate the slope-reduction intuition.
4. **Characterize the linear approximation error** more explicitly — e.g., bound the gap between \(\Phi_{\text{RS}}(\tau+M_\epsilon)-\Phi_{\text{RS}}(\tau)\) and \(\Phi'_{\text{RS}}(\tau)\cdot M_\epsilon\) under a Lipschitz or smoothness assumption on the CDF.
5. **Add a simple ablation** of PTT's two components (ranking only, sigmoid only on ranked scores) to the appendix.

## Score and Decision

The paper identifies a real flaw in an existing method, proposes a clean theoretical fix, and introduces two practical methods that produce large, meaningful efficiency gains on standard benchmarks. The core contribution (RSCP+) is theoretically sound, and the efficiency results are striking. The main weaknesses are in the empirical validation (missing coverage verification, incomplete baselines) and in the heuristic nature of PTT's justification. These are addressable and do not undermine the paper's central claims.

The paper is a solid contribution to the area of trustworthy ML / conformal prediction. With the suggested additions, it would be a strong paper. In its current form, the empirical gaps prevent unconditional acceptance, but the core ideas are clearly valuable.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>