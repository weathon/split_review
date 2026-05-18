Now I have all the information I need. Let me construct the final consolidated review.

## Summary

This paper proposes CONTROL, a contrastive learning framework for open-world semi-supervised learning (SSL) that adds three contrastive losses (supervised, nearest-neighbor, and unsupervised) to existing BCE-based methods such as ORCA and NACH. The authors claim theoretical justification that contrastive losses are more robust than BCE loss to misaligned nearest-neighbor pairs, and that uniformity in contrastive learning prevents representation collapse. Experiments on CIFAR-10, CIFAR-100, and ImageNet-100 show improvements over baseline methods, with the largest gains on unseen class accuracy (e.g., +6.4% on CIFAR-100 with NACH).

## Strengths

- **Consistent empirical gains across benchmarks.** CONTROL improves unseen class accuracy over NACH by 6.4% on CIFAR-100 and 4.0% on ImageNet-100 (Tables 1 and 2). All-class accuracy also improves by 2.1% and 1.2% respectively. These are non-trivial improvements that suggest the framework is doing something useful.

- **Quantitative analysis connecting the framework to the claimed mechanism.** Table 4 shows that CONTROL increases the ratio of unseen-unseen nearest-neighbor pairs by 2.35% and the ratio of unseen class predictions by 2.77% on CIFAR-100 with NACH. This directly supports the paper's narrative that feature-level alignment reduces the seen-unseen pair problem identified in Figure 2.

- **Plug-and-play compatibility with existing BCE-based methods.** CONTROL is tested with two distinct BCE-based baselines (ORCA and NACH) across three datasets and improves both in every configuration, demonstrating that the framework can be applied as an add-on module.

## Weaknesses

### Fatal

None.

### Major

- **The theoretical derivation in Section 4.1 is not rigorous and contains errors.** This is presented as a core contribution (item two in the contribution list), but the analysis has two substantive problems that prevent it from serving as valid theoretical support.

  *BCE analysis:* The paper claims that when $x$ and $v$ are independent, $g(\phi(x))^\top g(\phi(v)) = 0$ and consequently $M \to -\infty$. Neither step is justified. Independence of random variables does not imply their inner product is zero — this would require distributional assumptions (e.g., zero-mean or uniform on the hypersphere for features, plus a corresponding property for logits $g(\cdot)$) that are neither stated nor argued. Additionally, $-\log(0) = +\infty$, not $-\infty$, so the direction of the claimed blow-up is wrong. While the core intuition (noisy pairs create a large gap in BCE risk) may still be correct, the mathematical presentation is incorrect.

  *Contrastive analysis:* The paper simplifies $\mathbb{E}_{\mathrm{P}_{XV}^\eta}\mathcal{L}_\phi$ to $(1-\eta)\mathbb{E}_{\mathrm{P}_{XV}}\mathcal{L}_\phi + \eta\cdot\log(|\mathcal{N}(x)|)$ by claiming the cross-terms vanish because $\phi(x),\phi(v^+),\phi(v^-)$ are independent. This is insufficient. Independence alone does not imply $\mathbb{E}[-\phi(x)^\top\phi(v^+)/\tau] = 0$ (this requires features to be zero-mean or orthogonal in expectation), nor does it imply $\mathbb{E}[\log\sum\exp(\phi(x)^\top\phi(v^-)/\tau)] = \log(|\mathcal{N}(x)|)$ (this requires the dot products to all be zero, i.e., perfect uniformity on the hypersphere, which is neither guaranteed nor shown). Without these additional assumptions, the conclusion that the noisy and clean distributions yield the same optimal classifier is unsubstantiated.

  Because the theory is listed as a key contribution and motivates the framework, this is a significant weakness. The paper would be stronger if it either provided a correct derivation with explicit assumptions, or acknowledged the argument as heuristic and relied on empirical analysis instead.

- **Complete absence of error bars or measures of variability.** All tables report single means over three runs with no standard deviations, confidence intervals, or statistical significance tests. For improvements that are modest (e.g., +0.8% on seen classes for NACH+CIFAR-100, +0.2% on all classes for SupNN ablation), it is impossible to assess whether these gains are meaningful or within the noise of the runs. This is a basic reporting requirement for empirical ML papers and directly undermines the claim of "significant improvement."

### Minor

- **Ablation does not fully isolate each loss component.** Table 3 reports "(SupSeen + SimAll)" combined and SupNN alone, but never reports SupSeen alone, SimAll alone, or the other pairwise combinations. Without these, it is difficult to attribute the gains to specific components. This is partially mitigated because each component is shown to contribute positively in at least one configuration, but the attribution remains incomplete.

- **Hyperparameter values are not reported.** The framework has three weighting coefficients $\lambda_1,\lambda_2,\lambda_3$ and a temperature $\tau$, all of which are mentioned in the formulation but never given numerical values. The paper does not state how these were selected (grid search? heuristic?) or whether the results are sensitive to them. For a "simple and efficient" framework intended for broad use, this information is necessary for reproducibility.

- **Unclear whether the OpenCon comparison is controlled.** The paper compares against OpenCon but does not explicitly state whether OpenCon was re-implemented under the same backbone and training protocol or whether numbers are taken from its original paper. The statement "all experiments use the same backbone ResNet18" is given for the main comparisons but not specifically confirmed for OpenCon. If OpenCon uses a different backbone or augmentation strategy, the comparison may not be fair.

### Trivial

- The paper claims CONTROL is "compatible with a broad range of existing open-world semi-supervised learning algorithms" but only tests on two BCE-based methods (ORCA and NACH). Acknowledging this scope limitation more explicitly would strengthen the paper's claims.

## Nice-to-Haves

- Sensitivity analysis for the hyperparameters $\lambda_1,\lambda_2,\lambda_3$ and $\tau$ would help establish the framework's robustness.
- An experiment on a non-BCE-based method (such as OpenLDN or TRSSL) would strengthen the claimed generality, though this is not required given the paper's focus on BCE-based methods.
- Visual analysis of the learned feature representations (e.g., t-SNE plots or alignment/uniformity metrics) would provide empirical support for the claims about uniformity and collapse prevention, partially compensating for the flawed theoretical analysis.

## Removed Points

- **"Theoretical justification that contrastive loss is robust to noisy nearest-neighbor pairs while BCE loss is not"** (from Strength Finder). This strength directly conflicts with the verified weakness that the theoretical derivation is flawed. The strength is removed because the weakness wins.

- **"Ablation study isolating each loss component"** (from Strength Finder). This overstates what the paper actually does — the ablation combines SupSeen and SimAll without isolating them individually. The strength is removed as overly generous.

- **"The paper should also test non-BCE-based methods"** (from Harsh Critic's "Other Observations"). This demands breadth outside the paper's stated scope (BCE-based methods). Weakened to a minor scope note above rather than a standalone weakness; the core issue is that the claimed "broad compatibility" is not fully supported, which is already addressed in the Trivial section.

## Novel Insights

None beyond the paper's own contributions. The core idea — that feature-level contrastive losses can complement logit-level BCE alignment in open-world SSL — is a natural extension of existing work. The reviews do not surface any unexpected synthesis or cross-observation that the paper itself does not already articulate.

## Suggestions

1. **Either fix or remove the theoretical analysis.** If the derivation in Section 4.1 cannot be made rigorous with proper assumptions, the paper should honestly retreat from the theoretical claim and instead provide empirical support for why contrastive losses help (e.g., measuring feature alignment/uniformity, visualizing the embedding space, or analyzing gradient agreement). The current form is a liability.

2. **Report standard deviations for all experimental results.** This is the single most important addition. Without it, the empirical contribution cannot be evaluated.

3. **Disclose all hyperparameter values** ($\lambda_1,\lambda_2,\lambda_3,\tau$) and state how they were chosen. Include a sensitivity analysis for the weighting coefficients.

4. **Complete the ablation.** Report the contribution of each loss component individually (SupSeen alone, SimAll alone, SupNN alone) and each pairwise combination.

5. **Clarify the OpenCon comparison** — state whether it was re-implemented under the same conditions or cite the original paper's numbers, and if the latter, note any differences in protocol.

## Score and Decision

The paper addresses a real problem and the empirical pattern is promising, but the current form has two major issues: (1) the theoretical analysis, presented as a core contribution, is not mathematically sound; and (2) the empirical reporting lacks basic statistical rigor. These issues are addressable in revision but prevent the paper from making a convincing contribution in its current form.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>