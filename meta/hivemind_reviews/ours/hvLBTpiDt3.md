## Summary
This paper proposes DPaI (Differentiable Pruning at Initialization), a method that converts the discrete Node-Path Balancing (NPB) principle into a differentiable formulation using Straight-Through Estimators and tanh-based activations. This enables gradient-based optimization of the pruning mask to jointly maximize effective paths, nodes, and kernels at initialization — something previous NPB, which required discrete layer-wise heuristics, could not do. The method is evaluated on CIFAR-10/100, Tiny-ImageNet, and ImageNet-1K across ResNet and VGG architectures.

## Strengths
- **First differentiable PaI method incorporating network topology (NPB principle)**. DPaI introduces a continuous relaxation of the discrete NPB optimization (Section 3.2, Equations 2–6) using Straight-Through Estimators and tanh-based node/kernel activations. This enables gradient-based joint optimization of effective paths, nodes, and kernels — a combination no prior PaI method achieves. The convergence analysis (Section 3.3) provides local guarantees: the update rule strictly increases effective paths and activates ineffective nodes under a single-edge-swap assumption, offering theoretical grounding absent in the heuristic discrete NPB solver.

- **Strong and consistent empirical performance across architectures and sparsity levels**. DPaI outperforms all baseline methods (Random, SNIP, SynFlow, Iter-SNIP, PHEW, NPB) on CIFAR-10, CIFAR-100, and Tiny-ImageNet across ResNet-18, ResNet-50, ResNet-20, and VGG19, with gains up to 4.6% at high sparsities (Figure 1). On ImageNet-1K at 95% sparsity (Table 1), DPaI achieves 69.26% top-1 accuracy vs. SynFlow's 67.95%. The discovered subnetworks consistently have higher effective node and path counts, directly validating the optimization objective.

- **Low and stable pruning time**. DPaI maintains consistently low wall-clock pruning time across all architectures and sparsity levels (Figure 3), unlike NPB and PHEW whose costs vary significantly with network size and target sparsity.

- **Hyperparameter robustness**. The ablation study (Figure 2) shows that even the worst hyperparameter choices of DPaI outperform most baselines (Random, SNIP, SynFlow, Iter-SNIP) across the majority of settings.

## Weaknesses
### Fatal

None.

### Major

- **ImageNet-1K comparison is limited to a single baseline**. Table 1 compares DPaI only to SynFlow on ImageNet. Several other baselines that were compared on smaller datasets (NPB, PHEW, Iter-SNIP, SNIP) are absent from the large-scale evaluation. This weakens the claim of "significantly outperforming current state-of-the-art PaI methods on various architectures" (abstract) for the large-scale setting. The conclusion may be correct, but the evidence provided does not fully support it at ImageNet scale.

- **No statistical significance or variance is reported**. Accuracy results are presented as single-point estimates with no standard deviations, confidence intervals, or multi-run statistics. Since score parameters are randomly initialized and the Top-k selection introduces stochasticity, the robustness of reported improvements cannot be assessed. This is a methodological gap that affects the credibility of all accuracy claims, particularly for the smaller CIFAR experiments where multi-run reporting is standard practice.

### Minor

- **The "data-agnostic" claim is overstated**. Section 4.2 states DPaI is "entirely data-agnostic and independent of initial weights," but the hyperparameters α and β are tuned via grid search on validation accuracy (Section 4.1), and Figure 2 shows these strongly affect performance. The mask optimization itself does not use data (which is a legitimate advantage), but the overall pipeline for obtaining a good mask depends on dataset-specific hyperparameter tuning. This should be clarified.

- **VGG19 underperformance at 99% sparsity is explained speculatively**. The paper attributes DPaI's underperformance versus NPB and PHEW on VGG19 at 99% sparsity to those methods "biasing their algorithms towards weight magnitudes." No ablation or analysis is provided to support this explanation.

- **The value of γ (tanh scaling constant) is not specified**. The paper states only that γ is "sufficiently large" (line 88). For large γ, tanh saturates and gradients vanish for active or inactive nodes, yet no concrete value or sensitivity analysis is provided for this parameter.

- **Figure 1 caption is unclear**. The caption says "The best accuracy of each setting was set in blue" without explaining the color-to-method mapping for non-best entries, making the figure hard to interpret independently.

- **Convergence analysis is local/heuristic**. The analysis in Section 3.3 assumes a single edge swap with all other parameters fixed. The practical stopping criterion (3000 steps or no change in objectives, line 180) is reasonable but the "convergence" claim is informal. This is typical for the area but should be labeled accordingly.

### Trivial

None.

## Suggestions
1. Add ImageNet results for NPB, PHEW, and Iter-SNIP to support the SOTA claim at large scale.
2. Report mean and standard deviation over at least 3-5 runs for key comparisons.
3. Clarify the data-agnostic claim: the mask computation itself is data-free, but α/β tuning uses validation accuracy.
4. Specify the γ value used in experiments and discuss its sensitivity.
5. Improve Figure 1 caption to clearly explain the color-to-method mapping.
6. Provide more evidence for the explanation of VGG19 underperformance at 99% sparsity, or remove the speculation.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>

## Questions


## Decision
Accept
