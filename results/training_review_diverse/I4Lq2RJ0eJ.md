Now I have all the information I need. Let me construct the final consolidated review.

## Summary

This paper investigates whether existing unlearnable examples (UEs) are truly unlearnable across different tasks. It finds that UEs fail to maintain unlearnability in multi-task settings (Taskonomy). To explain this, the paper analyzes the loss landscape of poisoned vs. clean training and proposes Sharpness-Aware Learnability (SAL), a per-parameter metric quantifying how much a parameter's perturbation changes the loss. Based on SAL, it further introduces Unlearnable Distance (UD), a task-agnostic metric defined as the ratio of learnable parameters in poisoned vs. clean models. Finally, it benchmarks 6 unlearnable methods across multiple datasets, architectures, and defenses using UD.

## Strengths

1. **Novel perspective on unlearnability through loss-landscape and parameter-level analysis.** The paper moves beyond test-accuracy-based evaluation and instead analyzes the training dynamics directly. Definition 1 (SAL) connects unlearnability to the sharpness of the loss landscape around parameters, and Figure 4 shows that UEs systematically reduce SAL. This framing is a genuine departure from prior work focused on linear separability of perturbations or peak accuracy behavior.

2. **Introduction of Unlearnable Distance (UD) as a task-agnostic metric.** UD (Equation 5) provides a single scalar that quantifies data unlearnability without depending on a specific downstream task metric. This is useful for comparing methods across different training regimes. The benchmarking in Tables 1–3 covers 6 unlearnable methods (EM, REM, DC, TAP, LSP, OPS), 4 architectures (ResNet‑18/50, SENet‑18, ViT), 3 datasets (CIFAR‑10/100, ImageNet‑100 subset), and 5 defenses, providing a reasonably broad reference.

3. **Principled distinction between true UEs and adversarial availability attacks.** SAL and UD correctly identify TAP (error-maximizing noise) as qualitatively different: TAP yields UD > 1 and high SAL (Tables 1, 3; Figure 6), because adversarial examples derail optimization direction rather than suppressing learning. This offers a conceptual tool for separating two classes of training-time threats that prior accuracy-based metrics conflate.

4. **First documented failure of UEs under multi-task training.** While the evidence is preliminary (discussed below), the observation that UEs generated for classification do not degrade performance in semantic segmentation, depth estimation, or keypoint prediction on Taskonomy (Figure 1) is the first demonstration of this limitation and motivates a worthwhile research direction.

## Weaknesses

### Fatal
None.

### Major

1. **UD validity is asserted without direct quantitative comparison to test accuracy.** The paper claims UD is "consistent with test accuracy" (Section 5.1) but provides no side-by-side table or correlation analysis. Table 1 reports only UD; the corresponding test accuracies are never shown. Without knowing whether UD actually tracks the phenomenon it claims to measure, the metric remains an untested proxy. The defense experiments (Table 2) show that defenses increase UD, which is consistent with expectations, but this is indirect validation — the core test is whether UD correlates with actual task performance across methods and datasets. The OPS case on CIFAR‑10 (lowest UD yet "test accuracy is not the lowest") is acknowledged but not reconciled, further underscoring the need for a systematic comparison. This weakness directly affects the paper's central claimed contribution (the UD metric).

2. **The multi-task experiment motivating the paper is under-reported.** Figure 1 is the key evidence for the claim "existing UEs fail to maintain unlearnability in multi-task models" (the first bulleted contribution), but it lacks numerical values, error bars, and statistical tests. The paper mentions only three generation methods (EM, OPS, AR) in the text while the figure caption references "4 selected UEs" — a discrepancy. The experiment uses one dataset (Taskonomy tiny split), one backbone (ResNet with ModSquad), and one training configuration. For a claim positioned as a first contribution, this evidence is too thin to be fully convincing. Numerical task metrics (classification accuracy, keypoint error, depth error, segmentation IoU) for each method should be reported, and testing additional methods would strengthen the claim that the failure is widespread.

### Minor

3. **Algorithm 1 is incomplete.** The pseudocode shows `θ^c(t+1) ← θ^c(t)` and `θ^p(t+1) ← θ^p(t)` (lines 3, 11) — parameter values are copied without any gradient-based update. The actual training step is missing. While the intent (compute SAL during or after training) is understandable from context, the algorithm as written is not reproducible as-is and should separate the training loop from the SAL computation.

4. **The relationship between SAL-based "flatness" and beneficial flatness (SAM literature) is not discussed.** The paper borrows the concept of sharpness from the generalization literature, where flat minima are associated with good generalization (Foret et al., 2020). The paper argues that flatness in UE-trained models indicates *unlearnability*. This tension is acknowledged only implicitly via a related-work citation; the paper should explain why the same geometric property signals opposite conclusions in the two settings.

5. **The K‑means threshold β is not justified or ablated.** The threshold for separating learnable from unlearnable parameters is determined by 2-cluster K‑means on the clean model's SAL values (Definition 2). The choice of two clusters is not justified, and no sensitivity analysis is provided (e.g., varying the number of clusters, testing other binarization methods). This introduces a source of variability whose impact on UD values is unknown.

6. **The "few key parameters" claim is extrapolated from a toy model.** Section 3.1 visualizes optimization trajectories for a 120-parameter linear classifier and concludes that "only a few key parameters in DNNs undergo normal learning." The paper acknowledges this limitation but does not attempt to verify the claim on a realistic architecture. The leap from a 120-parameter model to million-parameter DNNs is substantial and unsupported.

7. **OPS on ImageNet‑100 shows an anomalous trend left unexplained.** The paper notes that OPS exhibits the "largest UD on ImageNet‑100, accompanied by an increasing #LP as epochs grow, showing a weirdly opposite trend to the CIFAR dataset," and defers this to "future discussions." While this honesty is commendable, it undermines confidence in the metric's generality when a central method behaves in an unexplained way on a key dataset.

### Trivial
- The colorbar/scale in Figure 4 is not clearly explained in the caption or text, making the quantitative meaning of the visualization difficult to interpret.
- The paper does not explicitly state whether Tᶜ and Tᵖ are equal, though 100 epochs is the default for both from context.

## Nice-to-Haves
- A scatter plot or Spearman correlation between UD and test accuracy across methods/datasets would greatly strengthen the UD validation.
- A sensitivity analysis for the K‑means threshold (e.g., varying the number of clusters, using percentile-based thresholds) would show whether UD is robust.
- Reporting the computational overhead of SAL computation would help practitioners assess its practicality.

## Removed Points
- **Criticism that Algorithm 1 "cannot be reproduced":** The training update step is missing from the pseudocode (kept as Minor weakness 3), but the overall algorithm purpose is clear from context. Calling it structurally flawed or irreproducible overstates the issue.
- **Criticism about Section 3.1 being "speculation rather than evidence":** The paper acknowledges the toy-model limitation. The section is clearly framed as exploratory analysis providing intuition, not as proof.
- **Complaint that the paper doesn't compare UD to existing metrics (Yu et al. 2022, Sandoval-Segura et al.):** The paper's contribution is a *new* metric; comparison to existing metrics would be valuable but is not required for the paper's validity.
- **Criticism that Tᶜ and Tᵖ are not stated as equal:** Implicit from the experimental setup ("almost identical to Section 3.3").

## Novel Insights
The reviews surface an important tension that the paper does not fully resolve: SAL defines flatness as unlearnability, yet the SAM literature defines flatness as beneficial for generalization. Neither the paper nor the reviews offer a resolution — this is a conceptual gap worth addressing. Additionally, the reviews correctly identify that the paper's two main contributions (multi-task UE failure and the UD metric) are both promising but insufficiently evidenced, creating a cumulative weakness: each major claim partly depends on the other (the multi-task finding motivates UD; UD is used to analyze multi-task behavior), yet neither is independently airtight.

## Suggestions
1. **Add a table with UD alongside test accuracy** for every method/dataset pair in Tables 1–3, and report Spearman's rank correlation. This single addition would address the most serious weakness.
2. **Flesh out the multi-task experiment:** report actual task metrics numerically, add error bars, test at least two more methods (e.g., DC, REM), and reconcile the discrepancy between "3 methods" in text and "4 selected UEs" in Figure 1.
3. **Fix Algorithm 1:** explicitly show the gradient descent update (or reference it as a standard training step) and separate the SAL computation loop from the training loop.
4. **Address the SAM tension:** add a paragraph distinguishing SAL-style flatness (model cannot escape a poor minimum) from SAM-style flatness (model finds a wide, generalizable minimum).
5. **Ablate the K‑means threshold:** show UD values under different cluster counts or percentile thresholds.

## Score and Decision

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>