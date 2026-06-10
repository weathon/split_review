## Summary

This paper proposes UNI, a method that replaces static baselines (black, blurred, noised) in path-based attribution with an **adaptively learned baseline** obtained by perturbing the input toward an "unlearning direction" — matching the activations of an unlearned model. The key idea is to operationalize "absence of signal" in a task-, model-, and input-specific way rather than relying on hand-picked reference inputs. Experiments on ImageNet show UNI consistently outperforming baselines on monotonicity, faithfulness (MuFidelity), and robustness (FGSM) across six architectures.

## Strengths

1. **Original connection between machine unlearning and baseline definition for path attribution**: The paper is the first to operationalize "absence of signal" via an unlearning direction — perturbing the input to match activations of an unlearned model (Algorithm 1). This departs entirely from the prior focus on static baselines or averaging over them, providing an adaptive per-(task, model, input) baseline that is "specific and featureless" (Section 4.1).

2. **Formal error bound connecting path curvature to Riemann approximation quality**: Equation (11) gives a clean Taylor-Lagrange bound showing that the Riemann sum error scales as \(M\|x-x'\|^2 / (2B)\), where \(M\) is the maximum second derivative along the path. This formally motivates why low-curvature paths yield more accurate attributions with fewer integration steps — a justification that prior work on baseline choice does not provide.

3. **Systematic demonstration of post-hoc biases from static baselines**: Section 3.2 and the accompanying figures show that each static baseline family (black, blurred, noised) imposes its own extraneous bias — color, texture, and frequency respectively — and verifies this on ImageNet-C corruptions. This provides a concrete diagnosis of why static baselines fail, rather than just an empirical comparison.

4. **Consistent empirical superiority across architectures**: UNI achieves the best monotonicity scores (0.89–0.99 Spearman across 6 architectures vs. 0.27–0.88 for baselines, Table 1), best MuFidelity in 5/6 architectures (Table 2), and best robustness under FGSM attacks on both Spearman correlation and top-1000 pixel intersection (Tables rSC, rTK). Gains hold across CNN (ResNet, EfficientNet, ConvNeXt, VGG) and transformer (ViT, Swin) backbones.

## Weaknesses

### Major

1. **Core algorithm uses undefined quantities, preventing full understanding and reproducibility.** Algorithm 1 (line 58) computes \(\mathcal{C} = \infdiv{F(x; \hat{\theta})}{F(x + \delta^t; \theta)}\) using two symbols never defined in the paper: **(a)** \(\infdiv\) — the divergence function is never specified (KL? JS? cross-entropy?); **(b)** \(\hat{\theta}\) — the "unlearned" model. The paper mentions "unlearning in the model space \(\theta \longmapsto \hat{\theta}\)" (Figure 1 caption) and "first, unlearn predictive information in the model space" (Section 4.1), but provides no algorithm, loss function, or update rule. The hyperparameter "unlearning step size \(\eta = 1\)" (line 150) is listed, yet \(\eta\) never appears in Algorithm 1 — suggesting it applies to an unlearning procedure that is never described. These are not implementation details; they are the central mechanism of the method.

2. **Absolute faithfulness scores are very low and the paper overclaims.** MuFidelity values range from 0.05–0.18 across all methods (Table 2), with standard deviations comparable to or exceeding the mean (e.g., UNI on ResNet-18: \(0.12 \pm 0.124\)). A correlation of 0.12 means the attribution explains ~1.4% of the variance in actual feature effect. Calling this "high faithfulness" (abstract, line 155) is misleading. UNI wins most comparisons, but the absolute magnitudes suggest that *none* of these methods — including UNI — produce attributions that reliably correspond to the model's actual feature dependence. This should be acknowledged and discussed.

### Minor

3. **No computational cost analysis despite claiming efficiency.** The abstract calls UNI "efficient" and criticizes competing methods as "computationally costly" (Section 1), but the paper provides zero runtime or FLOP comparisons. UNI requires (a) obtaining \(\hat{\theta}\) (cost unknown), (b) \(T=10\) gradient-based optimization steps for \(\delta\) (each requiring forward+backward passes), and (c) \(B=15\) Riemann-sum gradient computations. This is substantially more expensive than standard IG. The efficiency claim is unsupported without measurements.

4. **Limited robustness evaluation.** Only FGSM (a weak single-step attack) is tested. Stronger iterative attacks (PGD, CW) could erode UNI's advantage, and the post-attack Spearman values of 0.27–0.32, while better than baselines, are still low in absolute terms.

5. **Curvature reduction claim is asserted but not directly measured.** The paper claims "unlearning reduces the curvature of decision boundaries" (line 28) and states "We empirically verify this local smoothing effect by measuring the normal curvature" (line 24), yet the experiments section contains no direct curvature measurement. The monotonicity table is offered as indirect evidence, but monotonicity and curvature are distinct properties. Direct measurement (e.g., Hessian spectral norm along the path) is needed to support this claim.

6. **Only one faithfulness metric (MuFidelity).** Standard complementary metrics such as insertion/deletion scores, ROAR, or the pointing game are absent. Including at least one additional metric would substantially strengthen the evaluation.

### Trivial

7. Typo: "we the following hyperparameters" (line 150) — missing verb ("use").

## Nice-to-Haves

- Ablation study: how does the choice of divergence (\(\infdiv\)) affect results?
- Statistical significance testing (confidence intervals or paired tests) for MuFidelity comparisons, given overlapping standard deviations.
- Analysis of failure cases — does UNI ever converge to trivial solutions (\(\delta=0\)) or erase wrong features?
- Explicit discussion of the computational trade-off between improved attribution quality and added cost.

## Removed Points

These points were surfaced by the reviewers but removed per the filtering rules:

- **Post-hoc bias "conflation" (Harsh Critic #3)**: The critic argued the bias evidence is "equally consistent with the model genuinely depending less on features similar to the baseline." This is not a valid contradiction — the paper demonstrates that different baseline types produce systematically different attribution patterns aligned with the baseline's properties (color, texture, frequency) and verifies this on ImageNet-C. The critic's "alternative explanation" would need independent evidence to constitute a confound. Removed as a strawman.
- **"Thin evaluation" as an umbrella critique**: General framing without a specific anchor. The concrete sub-points (only one faithfulness metric, only FGSM) are already listed as individual Minor weaknesses above.
- **No statistical significance testing / code release**: Per hard rules, removed from main weaknesses.
- **Monotonicity table not specifying the quantities**: The caption ("Path monotonicity scores with Spearman correlation coefficient") and surrounding text (line 144: "predictive confidence should be non-decreasing") make clear the correlation is between path position and output confidence. Removed.
- **Strength: "principled desiderata"**: Listing desirable properties is standard methodology practice; this strength is generic and dropped.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a genuinely novel synthesis that the paper itself does not provide.

## Suggestions

1. **Define \(\infdiv\) explicitly** in the main text — this single fix resolves the most critical reproducibility gap.
2. **Describe the unlearning procedure** for obtaining \(\hat{\theta}\) with at minimum the loss function and update rule. The paper already hints at "first-order approximate unlearning" (conclusion, line 254) — this needs to be concrete in the main paper.
3. **Add at least one additional faithfulness metric** (insertion/deletion scores are the standard choice) and **discuss the low absolute MuFidelity values** rather than calling them "high faithfulness."
4. **Provide runtime comparisons** to substantiate the efficiency claim, or remove the claim from the abstract.
5. **Test robustness under stronger attacks** (e.g., PGD-20) and include direct curvature measurements (Hessian spectral norm) to support the curvature reduction claim.
6. **Clarify the relationship to established unlearning literature**: is this actual gradient-based unlearning, or simply gradient ascent on the loss at \(x\)? The distinction matters for situating the contribution.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>