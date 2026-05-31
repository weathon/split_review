## Summary

This paper introduces Distributional Input Projection Networks (DIPNet), a framework that improves neural network generalization by projecting inputs into learnable Gaussian distributions at each layer during both training and inference. The authors provide theoretical analysis showing DIPNet reduces the Lipschitz constant and smoothness of the learned function, and empirically validate the method across Vision Transformers, LLMs, ResNets, and MLPs on standard, adversarial, and OOD tasks, demonstrating consistent improvements over baselines.

## Strengths

- **Novel and well-motivated approach:** DIPNet's idea of projecting inputs into learnable distributions at each layer—not just at the input level, and applied during both training and inference—is a creative architectural contribution that goes beyond standard noise injection or data augmentation techniques. The variational inference derivation provides a principled motivation for the distributional projection framework.

- **Theoretical guarantees:** The paper provides formal theorems (Theorems 1-3) showing that DIPNet reduces the Lipschitz constant and smoothness of the network function under reasonable conditions. These theoretical results directly support the paper's core claims about improved generalization and are a concrete contribution beyond empirical observation.

- **Broad empirical validation:** The experiments span a diverse range of architectures (ViT-Tiny/Small/Base, Qwen2.5, Llama-3, Gemma-3, ResNets, MLPs) and tasks (standard classification, adversarial attacks, OOD generalization, LLM reasoning), showing consistent improvements. The evaluation on LLM reasoning (GSM8K) across six different models with up to 12B parameters is particularly impressive and demonstrates scalability.

## Weaknesses

### Fatal

None.

### Major

- **Unconvincing visual results and missing key experimental details:** Figure 2 is the primary evidence for the distillation vs. multi-sampling comparison, but the accuracy values shown in the figure are extremely low (~11-13%), which does not align with the main results in Table 1 (ViT-Tiny under Gaussian: 52.22%) or Table 2 (Llama-3.2-3B: 33.06%). This discrepancy suggests either different evaluation settings or a plotting error that undermines confidence in the distillation analysis. Additionally, the paper evaluates inference time but does not report training-time overhead, which is critical for practical adoption.

- **Limited evaluation of the stability penalty hyperparameter λ:** Table 3 shows that λ=0 achieves the best accuracy for ViT-Tiny under Gaussian attack across all (α,β) combinations, raising the question of whether the stability penalty is actually beneficial in this setting. The paper briefly mentions that λ>0 helps when training from scratch (Appendix D.6.2), but this key claim is not prominently presented or adequately analyzed. The empirical support for the stability penalty—a core component of the theoretical formulation—is weak.

- **Insufficient baseline comparisons:** The main experiments compare DIPNet against SAM, RS, Cutout, Mixup, CutMix, and AugMix, but several relevant methods are missing. Gaussian noise injection at the input level during training only (the standard data augmentation approach) is not included as a direct ablation to isolate the benefit of layerwise distributional projection. Similarly, recent smoothing-based methods or other architectural approaches for improving smoothness are not compared.

### Minor

- **Theoretical gap between analysis and practice:** The theoretical results (Theorems 1-3) analyze a single-layer smoothing of the form g(x) = ∫ h(x+η) μ(η) dη, but DIPNet applies distributional projection at every layer with learned Σ_l that are trained jointly with the network parameters. The gap between the analyzed function and the actual multi-layer, learned-Σ setting is not addressed.

- **Ablation on layerwise projection:** The paper does not include an ablation comparing DIPNet with distributional projection at *every* layer versus at only the input layer (or a subset of layers). This would help isolate whether the layerwise nature is essential to the performance gains.

- **Computational cost of training:** The training algorithm requires m samples per data point per epoch (Algorithm 1), which introduces substantial training overhead. The paper does not report training time or FLOPs compared to baselines.

### Trivial

- The paper uses "uning" instead of "tuning" in Remark 1 (page 4), but this appears to be a parser artifact.

## Nice-to-Haves

- An analysis of how learned Σ_l values look across layers and tasks—do certain layers learn higher variance than others? This could provide insight into where smoothness is most beneficial.
- A comparison against stochastic depth (Huang et al., 2016) or dropout variants, which also introduce stochasticity during training but with different motivations.
- Evaluation on additional OOD benchmarks beyond those mentioned, such as CIFAR-10-C or ImageNet-C.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Resolve the discrepancy between the low accuracy values in Figure 2 (~11-13%) and the main results in Tables 1 and 2. If Figure 2 uses a different evaluation setting (e.g., only the first 100 test samples, or a different attack), this should be clearly stated. If the values are incorrect, the figure should be corrected.

2. Include an ablation where λ=0 is compared to λ>0 more prominently, and clarify under what conditions the stability penalty helps. Consider providing training-from-scratch results in the main paper rather than only in the appendix.

3. Add a comparison to "input-only Gaussian noise" (Gaussian noise added only at the input layer during training, matching the standard data augmentation) to directly demonstrate the benefit of layerwise projection.

4. Report training time / FLOPs overhead for DIPNet compared to the standard baseline and other methods.

## Score and Decision

The paper presents a genuinely novel architectural framework with strong theoretical grounding and broad empirical validation across vision and language models. The main concerns are the questionable Figure 2 results, limited support for the stability penalty component, and missing ablations. These issues are addressable and do not invalidate the core contribution.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>