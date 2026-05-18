Now I have all the information I need. Let me produce the consolidated review.

## Summary

AdaFisher proposes replacing Adam's second-moment estimate with a diagonalized, Kronecker-factored approximation of the Fisher Information Matrix (FIM). The method takes K-FAC's block-diagonal Kronecker factors, retains only their diagonals (justified via Gersgorin circle analysis), applies a Min-Max normalization, and plugs the resulting preconditioner into Adam's update rule in place of the usual $v_t$. Experiments span CIFAR-10/100 (8 architectures), ImageNet, transfer learning, and language modeling (WikiText-2, PTB). AdaFisher consistently achieves higher accuracy than Adam, K-FAC, AdaHessian, and Shampoo across most settings, and shows greater robustness to learning rate and batch-size variation.

## Strengths

- **Consistent accuracy improvements across a broad architectural zoo.** On CIFAR-10/100, AdaFisher achieves the highest accuracy among Adam, AdaHessian, K-FAC, and Shampoo across all 8 tested architectures (ResNet-18/50/101, DenseNet-121, MobileNetV3, Tiny Swin, FocalNet, CCT), with most gains outside the margin of error (e.g., on CIFAR-100: MobileNetV3 77.56 vs next-best 73.75, Tiny Swin 66.05 vs next-best 60.21). On ImageNet with ResNet-50 (batch 256, single-GPU), AdaFisher reaches 76.95% top-1 accuracy vs Adam 67.78%, K-FAC 70.96%, and Shampoo 72.82%.

- **Robustness to hyperparameter variation.** The stability analysis (Figure 4) shows that AdaFisher maintains high test accuracy across a wide range of learning rates (roughly 1e-4 to 1e-2) and batch sizes (64–1024) on CIFAR-100, whereas K-FAC and Adam degrade sharply at non-optimal settings.

- **Novel derivation of Kronecker factors for normalization layers.** Proposition (prop:proposition_normalization) provides explicit formulas for $\mathcal{H}_i$ and $\mathcal{S}_i$ for BatchNorm and LayerNorm layers, extending the diagonal block-Kronecker FIM approximation to normalization layers standard in modern architectures — a contribution missing from prior K-FAC work.

- **Computationally lightweight curvature approximation.** By discarding off-diagonal entries of Kronecker factors and using a simple diagonal Kronecker product, the method avoids the expensive full-matrix operations of K-FAC while reporting competitive epoch times (Figure 4, Panel D).

## Weaknesses

### Fatal

None.

### Major

- **Missing ablation studies that are explicitly promised.** Section 4.4 (line 295) states: "We further conduct extensive ablation studies on additional components of AdaFisher, including the convergence efficiency, our novel approximation of the FIM, the significance of EMA for Kronecker factors, the impact of the square root, the stability across learning rate schedulers and the updated computation of the FIM for normalization layers." No such results appear anywhere in the paper — the section transitions directly to Figure 4 (stability plots for batch size and learning rate). Without ablations that isolate the diagonal Kronecker structure, the Min-Max normalization, the removal of the square root, and the two-parameter EMA, it is impossible to attribute the reported gains to any specific component of the method. This omission is severe because the core algorithmic novelty (e.g., why use a Kronecker-factored diagonal instead of a simpler pixel-wise diagonal Fisher?) remains unvalidated.

- **Unclear and potentially unfair training protocol (WCT / epoch description).** The paper states: "We employ the Wall-Clock-Time (WCT) method with a cutoff of 200 epochs for AdaFisher's training, except for ImageNet, where we use a 90-epoch WCT for Adam" (line 189). The CIFAR table caption reads "with a 200-epoch AdaFisher training cutoff" (line 172), and for language modeling, "we apply the WCT method with 50 epochs training time of AdaFisher as the cutoff period" (line 286). This description is internally contradictory: "WCT" should mean all optimizers stop after a fixed wall-clock duration, yet the cutoff is defined in terms of one optimizer's epoch count. If baselines were run for fewer epochs because AdaFisher is slower per epoch and total time was fixed, then AdaFisher sees more data — making accuracy comparisons misleading. If all methods ran for the same number of epochs (200 for CIFAR, 90 for ImageNet), the "WCT" framing is unnecessary and confusing. The paper must clarify the exact protocol and confirm that all comparisons involve equal data exposure.

- **Non-competitive language modeling baselines undermine the NLP experiment.** On WikiText-2, Shampoo reports a perplexity of 1727.75 and AdaHessian reports 407.69, with the paper acknowledging that "Shampoo did not achieve convergence despite using optimal hyperparameters, and the K-FAC was unable to train effectively" (line 286). Values of 1727 indicate effectively random prediction and strongly suggest buggy or severely undertuned baselines. While the AdamW comparison (175.06 vs AdaFisherW 152.72) is more reasonable, the inclusion of failed baselines in the main table without clear visual or textual separation weakens the credibility of the language modeling evaluation. The paper should either report only well-tuned baselines for this task or explain why these methods are fundamentally unsuited to the architecture.

- **ImageNet: implausibly large gaps over K-FAC and Shampoo.** AdaFisher achieves 76.95% top-1 on ResNet-50 (batch 256), compared to K-FAC 70.96% and Shampoo 72.82%. A 6-point gap over K-FAC is unusually large for ImageNet ResNet-50 training; K-FAC is typically competitive with or better than Adam on CNNs. This discrepancy, combined with the K-FAC result being well below typical published K-FAC numbers, raises the question of whether the K-FAC baseline was properly tuned or given sufficient epochs. Since hyperparameters for all baselines are not disclosed, the reader cannot rule out suboptimal configuration.

- **"One additional hyperparameter" claim is imprecise.** The introduction states AdaFisher introduces "one additional hyperparameter compared to Adam" (line 20). However, Algorithm 1 lists $\gamma_1$, $\gamma_2$, and $\lambda$ as new hyperparameters compared to Adam (which itself has $\beta_1$, $\beta_2$, $\epsilon$). Even conservatively, this is at least two (the two-parameter EMA and the damping), and likely three. This claim should be corrected.

### Minor

- **Diagonal dominance evidence is limited in scope.** The Gersgorin circle analysis (Section 3.1) examines only one convolutional layer (Conv37 of ResNet-18) at two training steps. No quantitative measure (e.g., fraction of Frobenius norm on diagonal, ratio of diagonal to off-diagonal energy) is reported, and no results are shown for other layers, architectures, or training stages. While the analysis is suggestive, it is insufficient to support the broad claim that "Kronecker factors' energy is predominantly diagonal."

- **EMA equation (Eq. 4) and Algorithm 1 use confusing notation.** The update is written as $\mathcal{H}_i \leftarrow \gamma_1 \mathcal{H}_{i-1} + (1 - \gamma_2) \mathcal{H}_i$, using the same variable name $\mathcal{H}_i$ on both sides for different quantities (the updated EMA and the current batch estimate). The use of two different decay factors $\gamma_1$ and $\gamma_2$ in a single EMA is non-standard and should be justified. The subscripts conflate layer index and time step.

- **Min-Max normalization of Kronecker factors (Proposition 1) is not explained.** The paper applies Min-Max normalization to $\mathcal{H}_{D_i}$ and $\mathcal{S}_{D_i}$ before the Kronecker product but provides no rationale or ablation studying its effect. It is unclear whether this normalization is necessary for stability, whether it interacts with the damping parameter $\lambda$, or whether it could discard meaningful scale information.

- **Theoretical convergence bound does not leverage the Fisher approximation.** Proposition 2 provides a standard $O(\log T / \sqrt{T})$ non-convex convergence bound for generalized Adam-type methods, adapted from Chen et al. (2018). The bound does not depend on the specific diagonal Kronecker structure and offers no insight into why AdaFisher might converge to better minima than Adam. The theoretical contribution is essentially a sanity-check.

- **Baseline hyperparameter settings are not reported.** For AdaHessian, K-FAC, and Shampoo on each architecture (learning rate schedule, weight decay, damping, etc.), no hyperparameter details are given, making it difficult for the community to reproduce or assess the fairness of comparisons.

### Trivial

None.

## Nice-to-Haves

- Provide per-layer diagonal-dominance metrics (e.g., fraction of Frobenius norm on the diagonal) for all layers of ResNet-18/50 at multiple training stages.
- Include statistical significance tests (e.g., confidence intervals) for the CIFAR results where differences are small relative to standard deviations.
- Label Figure 1 (optimization path visualization) as either a real trajectory on a real loss surface or a toy illustration.
- Clarify the indexing in Algorithm 1 lines 10–11: distinguish between EMA at the previous time step and current batch estimate.

## Removed Points

*These points were flagged for removal; treat them with caution.*

- **Criticism about missing code release / reproducibility artifacts.** The harsh critic notes the paper does not mention code release. This is a standard expectation but not a valid criticism of the paper's technical content; many papers do not release code during the review process.
- **Criticism about the paper not reporting per-layer diagonal analysis in a table.** The Gersgorin analysis in Section 3.1 is a valid qualitative illustration; the request for a full per-layer table is reasonable but elevates a nice-to-have to a weakness.
- **Criticism about statistical significance for transfer learning.** The differences in Table 2 are generally outside 1σ (e.g., ResNet50 CIFAR10: AdaFisher 97.13±0.20 vs Adam 96.45±0.18 — a ~3.4σ difference), so the claim that differences are "within 1σ" is not accurate.
- **"Missing" related work / appendix / proofs.** These sections may be stripped by the parser; their absence in the extracted text is not evidence they are missing from the submission.
- **Criticism of the Gersgorin analysis being "not quantitatively assessed."** The paper does use Gersgorin's Circle Theorem and eigenvalue perturbation, which are quantitative tools; the scope (one layer) is limited but the analysis itself is valid.
- **Strength Finder strength about convergence guarantee.** This was removed due to conflict with the verified weakness that the theoretical bound is standard and does not depend on the proposed method.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the tension between the paper's strong and broad empirical results (8 architectures, multiple tasks) and the incomplete experimental presentation (missing ablations, unclear protocol). The diagonal approximation of Kronecker factors with Min-Max normalization is an interesting design choice whose rationale remains underexplored.

## Suggestions

1. **Provide the missing ablation studies.** For at least one dataset (e.g., CIFAR-100 with ResNet-50), ablate: (a) full Kronecker factors vs diagonal-only, (b) with and without Min-Max normalization, (c) with and without the square-root removal, (d) single vs two-parameter EMA. This is the single highest-priority addition.

2. **Clarify the training protocol explicitly.** State: "All optimizers were trained for T epochs on CIFAR (T=200), S epochs on ImageNet (S=90), and U epochs on language modeling (U=50). Wall-clock time was recorded but not used as the stopping criterion." Or if WCT was actually used, specify the wall-clock duration in hours/minutes and report the number of epochs each optimizer completed.

3. **Replace or remove failed language modeling baselines.** Present only the AdamW comparison (which shows a valid ~13% perplexity improvement) and either tune K-FAC/Shampoo properly or exclude them with a clear explanation.

4. **Report hyperparameter details for all baselines** in a supplementary table, including learning rate schedules, weight decay, damping, and the search procedure used.

5. **Correct the hyperparameter count claim** and clarify which hyperparameters the method actually adds relative to Adam.

6. **Quantify the diagonal dominance** across layers using Frobenius-norm-based metrics (e.g., $\| \text{diag}(A) \|_F / \| A \|_F$) for ResNet-18/50 at multiple training stages.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>