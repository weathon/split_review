Below is the final synthesized review.

---

## Summary

This paper proposes Instance-dependent Early Stopping (IES), a method that identifies training instances whose loss values have stabilized (using second-order differences) and excludes them from backpropagation for the remainder of training. The key insight is that second-order differences provide a threshold-uniform criterion across instances with varying loss magnitudes, enabling simple implementation. Experiments on CIFAR-10/100 and ImageNet-1k show 10–50% reduction in backpropagation instances with maintained or slightly improved accuracy, and the paper provides mechanistic analysis linking the savings to larger gradient norms and faster sharpness reduction.

---

## Strengths

- **Second-order difference as a unified mastery criterion.** The paper identifies a genuine problem with using raw loss values for instance selection (varying optimal losses across instances due to sample complexity, noise, imbalance) and validates that second-order differences have lower and more consistent coefficient of variation across instances in later training stages (Figure 3). This enables a single threshold δ to work across all instances, a practical advantage over methods requiring per-instance thresholds.

- **Concrete computational savings across diverse settings.** Table 1 reports consistent backpropagation reductions of 10–50% across CIFAR-10/100 and ImageNet-1k with multiple architectures (ResNet, VGG, DenseNet) and optimizers (SGD variants, Adam, AdamW) while maintaining or slightly improving test accuracy. The δ robustness analysis (Figure 5, lower row) shows accuracy stays within ~2% of baseline across four orders of magnitude of δ, indicating the method is not brittle.

- **Mechanistic explanation beyond black-box efficiency.** Figure 4 provides evidence that IES increases average mini-batch gradient norms and reduces both the maximum Hessian eigenvalue and SAM value more rapidly than full-data training. This goes beyond a pure efficiency claim and offers insight into why removing mastered instances can improve the optimization trajectory.

- **Transfer learning benefit.** Models pretrained with IES on ImageNet-1k and fine-tuned on CIFAR and Caltech-101 show average improvements of 1.5% over standard pretraining (Section 4.1), an unexpected positive side-effect.

- **Extension beyond classification.** IES is demonstrated on object detection (Faster R-CNN) and semantic segmentation (DeepLab v3) on PASCAL VOC (Table 5), showing applicability to dense prediction tasks.

---

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Algorithm notation inconsistency.** Algorithm 1 line 5 (line 94) writes the mastery criterion as $|\Delta^2 L_i(w^{(t')})| < \delta$ with an undefined superscript $t'$. The intended reading is clearly $t$ (the current epoch), and the second-order difference formula is correctly defined in Equation (lines 72–73), so the method remains implementable. However, this is a concrete error in the algorithm specification that should be fixed. Additionally, the introduction mentions "over $k$ epochs" (line 21) but the formal criterion checks only the current second-order difference — these two descriptions should be reconciled.

- **Computational savings reported via proxy rather than measured time.** The paper translates "40% backpropagation reduction" into "nearly 30% savings in total computational cost" (line 106) without accounting for the forward passes still performed on all instances each epoch for the mastery check. The actual wall-clock savings depend on the forward/backward cost ratio of the architecture and batch size. Reporting measured training time or FLOPs on at least one primary setting (e.g., ResNet-50 on ImageNet-1k) would substantiate the practical speedup.

- **Limited evidence that permanently removing mastered instances is safe.** The claim that mastered instances can be permanently excluded without harm (a core assumption of the method) is supported by a single experiment on CIFAR-10 with ResNet-18 (Figure 2). While the end-task accuracy results across many settings indirectly suggest no catastrophic forgetting, the paper does not explicitly verify that excluded instances' losses remain low after removal (e.g., by measuring loss on excluded instances at the end of training) or study settings where forgetting is known to occur (e.g., noisy labels, class imbalance, long training horizons).

- **Transfer learning improvement not deeply analyzed.** The 1.5% average improvement in transfer learning (Section 4.1) is a potentially significant finding but receives only one sentence of explanation. The paper attributes it to "faster sharpness reduction" but provides no causal evidence. Alternative explanations (e.g., regularization from training on fewer examples) are not discussed.

- **2.0× speedup comparison calibration not explained.** In Section 4.3, the paper compares IES against several baselines at a target ~2.0× computational acceleration but does not describe how each method was calibrated to achieve exactly this speedup. For IES, δ controls the removal rate, but the protocol for selecting δ to match the target is unspecified. This makes it difficult to assess whether the comparison is apples-to-apples.

### Trivial

- The superscript $t'$ in Algorithm 1 is a typo (should be $t$). Fix for clarity.

---

## Nice-to-Haves

- Testing on an imbalanced dataset (e.g., CIFAR-100-LT, ImageNet-LT) would strengthen the argument that the second-order difference criterion does not disproportionately remove tail-class instances — a motivation the paper itself cites for not using raw loss values.
- Including a version where previously mastered instances can be re-admitted (e.g., if their loss spikes) and comparing it to the permanent-removal version would clarify whether the one-way design ever causes problems.
- A brief discussion of how the method would behave in non-stationary or continual learning settings would help scope the contribution.

---

## Removed Points
*These points appeared in the input reviews but were removed after cross-checking against the paper. They should be treated with caution.*

- *"Algorithm is structurally ambiguous and cannot be re-implemented"* — overblown. The formula for Δ²L is clearly defined (lines 72–73), and the algorithm is implementable despite the notation typo. The "over k epochs" vs. single-check inconsistency is real but minor (the second-order difference inherently spans 3 epochs).
- *"Framing as early stopping is misleading"* — scope creep. The paper explicitly positions itself as extending early stopping to the instance level; this is a reasonable framing choice.
- *"δ robustness analysis doesn't report exclusion rate"* — factually incorrect. The Figure 5 description explicitly states it shows "sample removal" alongside accuracy.
- *"One-way design is not adaptive enough"* — misunderstanding. Permanent removal is by design per the stated principle "once mastered, training on it should stop."
- *"Missing related works"* — rule prohibits this criticism.
- *"Table 1 embedded as image" / "Parser garbles numbers"* / "Missing appendix content" — parser artifacts.
- *"Missing theoretical justification for N=2"* — acknowledged in the limitations section (line 186); empirically justified by Figures 3 and 5.
- Generic strengths from Strength Finder ("addresses an important problem," "interesting question") — removed as superficial.

---

## Novel Insights

None beyond the paper's own contributions. The reviewers' analyses do not surface a perspective not already present in the paper.

---

## Suggestions

1. Fix the notation typo in Algorithm 1 (line 5: replace $t'$ with $t$) and reconcile the "over $k$ epochs" language in the introduction with the formal single-check criterion.
2. Report measured wall-clock time or actual training FLOPs on at least one primary setting to validate the claimed 30% computational savings.
3. Add an explicit verification that excluded instances' losses remain stable after removal (e.g., compute loss on the excluded set at the end of training), and ideally test on a class-imbalanced benchmark.
4. Describe the calibration protocol used to set δ (and each baseline's hyperparameters) to achieve the target 2.0× speedup in Section 4.3.
5. Expand the transfer learning analysis with ablations or a discussion of alternative mechanisms (regularization vs. sharpness reduction).

---

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>