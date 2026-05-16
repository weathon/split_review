Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

This paper empirically studies the double descent phenomenon in deep learning by analyzing the learned feature space. It proposes that over-parameterized models "isolate" noisy training samples by embedding them among clean samples of the same original class in the penultimate-layer feature space, and measures this via a k-NN accuracy metric \(P\) (whether a noisy sample's nearest clean neighbors share its original class). The paper replicates double descent across FCNN/MNIST, CNN/CIFAR-10, and ResNet18/CIFAR-10 at three noise levels.

## Strengths

- **Novel perspective on double descent through feature-space analysis**: The paper proposes a concrete, testable hypothesis — that over-parameterized models interpolate correct samples around noisy ones — and introduces a quantitative metric \(P\) to probe it. This lens (feature-space geometry of noisy vs. clean training points) is clearly distinct from prior explanations based on bias-variance decomposition, decision boundary fragmentation, or interpolation sharpness.

- **Honest reporting of a contradictory finding**: The ResNet18 result (lines 171–173) shows \(P\) dropping to zero at the interpolation threshold, directly contradicting the "isolation" hypothesis. Rather than suppressing this, the paper acknowledges the contradiction and discusses it, including the observation that over-parameterized CNNs eventually surpass ResNets in test accuracy. This transparency strengthens the credibility of the analysis.

- **Systematic multi-architecture, multi-dataset design**: The paper replicates experiments across three architectures (FCNN, CNN, ResNet18) and two datasets (MNIST, CIFAR-10) at three noise levels (0%, 10%, 20%) under consistent training settings (Section 3.1). This breadth rules out simple dataset- or architecture-specific artifacts.

- **Training-only signal for generalization**: The metric \(P\) is computed solely from training-set representations (line 115), providing an interpretable, in-distribution signal that correlates with test accuracy trends — an interesting property for a mechanistic account of double descent.

## Weaknesses

### Fatal
None.

### Major

1. **The ResNet18 result directly contradicts the paper's central "isolation" claim, and the explanations offered are post-hoc and unconvincing.** For ResNet18 on CIFAR-10, \(P\) (k-NN prediction accuracy on clean labels) drops to zero at the interpolation threshold and remains zero — every noisy sample's k-NN neighbors share its *assigned noisy* label, not its original class (lines 171–172). The paper's response (line 173) — that over-parameterized CNNs eventually surpass ResNets in test accuracy — does not resolve why the "isolation" mechanism would reverse direction across architectures. If the central claim is that over-parameterized models "isolate noise by interpolating correct samples around noisy ones," this architecture produces the opposite pattern, and the paper's attempted explanations (superior feature extraction, CNNs surpassing ResNets) do not constitute a mechanistic account of the discrepancy. This undermines the generality of the claimed phenomenon.

2. **Conceptual tension between the k-NN analysis and the classifier's behavior is unaddressed.** For FCNN and CNN where \(P > 0\) in the over-parameterized regime, the k-NN on penultimate-layer representations predicts the *clean* label for noisy samples. Yet the trained classifier (operating on the same representations) predicts the *noisy* label with zero training error. The paper never explains how these two facts can coexist — if a noisy point is embedded among clean samples of its original class in the penultimate space, the final linear classifier must learn narrow decision boundaries to assign it a different label. The paper provides no analysis or ablation to show that this is happening or why it constitutes meaningful "isolation." This gap leaves the interpretation of \(P\) ambiguous.

### Minor

1. **The k value for k-NN is never stated.** Equation (1) defines \(P\) with a free parameter \(k\), and the paper refers to "the closest k neighbours" (line 76), but no specific value is given for any experiment. All empirical conclusions rest on this metric, yet the reader cannot assess whether the results are robust to the choice of \(k\) or even what \(k\) was used. This is a basic reproducibility gap.

2. **No quantitative measure of alignment between \(P\) and test accuracy.** The paper repeatedly states that \(P\) "aligns" with or "correlates" with test accuracy (lines 115–116, 146), but provides no numerical measure (Spearman correlation, rank agreement, or similar). The visual alignment is clear for FCNN/MNIST but substantially weaker for CNN/CIFAR-10 (where \(P\) plateaus at ~60%), making qualitative claims insufficient.

3. **No variance or error bars.** The paper states experiments are replicated and averaged (line 67), but no error bars or confidence intervals are shown in any figure. Given that the k-NN analysis involves counting neighbors in high-dimensional space, variance bars would help assess whether observed trends are robust.

4. **The "perfect learner" model in the conclusion is speculative and untested.** Section 5 (lines 190–196) contrasts "imperfect learners" (which show double descent) with "perfect learners" (which should not) and includes Figure 5 as a diagram. This conceptual model is presented as a key insight but is never instantiated or tested through any experiment (e.g., varying regularization strength). It belongs in future work, not as a claimed contribution.

5. **No sensitivity analysis for key methodological choices.** The k-NN analysis uses cosine similarity on penultimate-layer representations without justification, and no experiments vary the distance metric, layer choice, or \(k\) to test robustness. The paper acknowledges this limitation (lines 147–148) but does not address it.

6. **Figure 3 caption contains a confusing description.** The caption states: "The k-NN prediction accuracy \(P\) on the clean labels first increases and then decreases to 0 at the interpolation threshold. One additional purple line on predicting the noisy labels is introduced showcasing that the k-NN predicts all noisy data with their clean labels." The second sentence appears to describe the complementary noisy-label prediction accuracy but is worded in a way that seems to contradict the first.

### Trivial
- The variable name \(k\) is used for both network width and the k-NN neighbor count (Equation 1 vs. Section 3.1), creating potential confusion.

## Nice-to-Haves
- A control experiment computing \(P\) on an equally noisy subset of the training set for a model trained *without* noise would isolate the effect of in-distribution noise memorization.
- Testing the "perfect learner" argument by training with varying regularization (weight decay, label smoothing) to see if the double descent peak diminishes.
- Computing average distances from noisy samples to the nearest clean sample of the original class versus other classes as a more direct measure of "isolation."

## Removed Points

These points were removed from the main review with justification:

- **"The paper does not compare its findings to Gamba et al. (2022)"** — Factually incorrect. The paper explicitly contrasts with Gamba et al. (2022) on lines 38–39, distinguishing the k-NN approach from their smoothness measure. Removed.
- **Various formatting/style nitpicks** — None present; not applicable.
- **Clean-label-only control framing as a major gap** — The paper includes \(p=0\) plots. The specific control suggested is reasonable but belongs in Nice-to-Haves, not weaknesses.

## Novel Insights

The reviews surface a genuinely novel observation that goes beyond the paper's own contributions: the ResNet18 result reveals that the "isolation" phenomenon is architecture-dependent in a way that the paper's framework cannot explain. This suggests the mechanism is not a universal property of over-parameterization but interacts with architectural inductive biases (e.g., residual connections, depth). A more productive framing might be: *which* architectures exhibit noise isolation, and what structural features enable it? The contrast between ResNet18 (where k-NN predicts noisy labels) and CNN (where k-NN partially predicts clean labels) is itself an interesting empirical finding that the paper treats as a nuisance rather than a discovery.

## Suggestions

1. **Specify the k value** used for k-NN in all experiments and include a sensitivity analysis across a range of \(k\) values.
2. **Quantify the alignment** between \(P\) and test accuracy (e.g., Spearman rank correlation) across model widths for each architecture.
3. **Address the conceptual tension** between k-NN predictions (clean labels) and classifier predictions (noisy labels) when \(P > 0\). Analyze whether the final linear layer learns to separate nearby points with different labels, and whether this constitutes "isolation" or merely memorization.
4. **Either experimentally test the "perfect learner" model** or clearly relegate it to future work rather than presenting it as a contribution.
5. **Frame the ResNet18 result** as a finding in its own right rather than attempting to explain it away — the architecture-dependence of the P-accuracy relationship is itself informative.

## Score and Decision

This paper tackles an important question and brings a refreshing perspective through feature-space analysis. The experiments are systematic and honestly reported. However, the central claim is not uniformly supported: the ResNet18 result directly contradicts the "noise isolation" hypothesis, and the paper lacks a coherent explanation for why different architectures produce opposite patterns. The conceptual tension between k-NN and classifier predictions is never resolved, and the core methodology is under-specified (missing k value). These are structural issues that prevent the paper from establishing its claimed mechanism, and they cannot be fully resolved in a rebuttal. The paper is better framed as reporting an interesting but incomplete empirical observation rather than a validated mechanism.

**Score: 5.0**

**Decision: Reject**

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>