## Summary

This paper identifies a fundamental limitation in intermediate layer knowledge distillation (ILD): the regressor layer commonly used to align teacher-student feature map dimensions creates an indirect knowledge transfer bottleneck. The authors propose a novel approach that prunes the teacher's target layer to match the student's dimensions, enabling direct distillation without a regressor. Through extensive experiments on CIFAR-100 and TinyImageNet with ResNet, VGG, and ShuffleNetV2 architectures, they demonstrate consistent improvements over traditional regressor-based ILD, with some configurations even exceeding teacher accuracy.

## Strengths

- **Clear problem identification with empirical evidence**: The probing experiments (Figure 2) convincingly demonstrate that the regressor-based approach is suboptimal—the post-regressor feature map, which directly receives teacher information through distillation, actually contains less useful information than the pre-regressor feature map. This is a non-obvious finding that justifies the core motivation.

- **Principled theoretical justification**: The mutual information analysis (Section 3.3) provides a clean theoretical framework showing that the proposed method's information transfer is lower-bounded by the traditional approach, up to a negligible pruning loss term γ. The data processing inequality argument (Eq. 5) elegantly captures why the regressor cannot increase mutual information.

- **Comprehensive experimental validation**: The paper evaluates across 3 architectures, 2 datasets, and multiple target layers (5 layers for VGG, 4 for ResNet/ShuffleNetV2), with 5 runs each. The ablation studies (probing with different depths, direct feature map distillation without pruning) provide additional insight into why the method works.

- **Remarkable results in certain configurations**: The method achieves 77.50% on CIFAR-100 and 49.23% on TinyImageNet with ResNet when distilling at Layer 4, exceeding the teacher's performance. This is a strong empirical result that validates the approach.

## Weaknesses

### Fatal
None.

### Major

- **Limited scope of comparison**: The paper only compares against FitNet (Romero et al., 2014) as the ILD baseline. While the authors acknowledge they are not seeking SOTA, the paper would be significantly stronger by comparing against at least 2-3 additional ILD methods (e.g., AT (Heo et al., 2019), SP (Tung & Mori, 2019), or CRD (Tian et al., 2019)) to demonstrate that the regressor problem is general and that teacher pruning can be combined with these methods. The claim that "our method can be combined with other ILD techniques using a regressor to obtain performance improvements" (Section 4.1.3) is not experimentally validated.

- **Inconsistent improvements across layers**: The method underperforms compared to LD or FitNet in several configurations (e.g., ResNet Layer1 on CIFAR-100: Ours 74.64 vs LD 75.69; ResNet Layer2 on TinyImageNet: Ours 44.63 vs LD 45.68; VGG Layer1 on TinyImageNet: Ours 39.94 vs LD 40.67). The paper does not adequately discuss why the method fails in these cases or provide guidance on when to use which layer for distillation.

- **Pruning overhead not fully addressed**: The method requires retraining the pruned teacher, which adds computational cost. While the paper mentions this, there is no quantitative analysis of the additional training time or computational resources required. For practitioners, this overhead might outweigh the benefits in some scenarios.

### Minor

- **The probing analysis could be more rigorous**: The probing results in Figure 3 show that the traditional ILD student performs worse than the original student in 1-layer probing but better in 5-layer probing. The interpretation that "traditional method primarily conveys implicit information" is speculative and not directly supported by the experimental design.

- **The mutual information analysis assumes independence**: The derivation treats feature maps as random variables without discussing the validity of this assumption or the practical challenges of estimating mutual information in high-dimensional spaces.

### Trivial

- The paper uses "regressor" throughout but the original FitNet paper uses "regressor" to refer to the layer that maps student features to teacher dimensions. This is a minor terminology preference.

## Nice-to-Haves

- An analysis of how the pruning ratio (γ in Eq. 4) varies with different pruning criteria beyond L1-norm would strengthen the claim that the information loss is negligible.
- A discussion of how to select the optimal target layer for distillation without exhaustive search would increase practical utility.
- An experiment showing the method applied to a non-CNN architecture (even a small ViT) would address the acknowledged limitation.

## Novel Insights

The paper's key insight is that the regressor in ILD is not merely a technical necessity but an active hindrance to knowledge transfer. This is supported by the probing experiments showing that the post-regressor feature map contains less information than the pre-regressor one—a counterintuitive finding since the post-regressor features are the ones directly supervised by the teacher. The mutual information analysis provides a theoretical lens: the data processing inequality guarantees that the regressor cannot increase information, and the pruning approach bypasses this bottleneck entirely. This reframes the dimensional mismatch problem from "how to align dimensions" to "how to avoid the need for alignment altogether."

## Suggestions

- Add comparisons with at least 2-3 additional ILD methods (e.g., AT, SP, CRD) to demonstrate the generality of the regressor problem and show that teacher pruning can be combined with these approaches.
- Provide a quantitative analysis of the computational overhead of teacher pruning and retraining, including wall-clock time and FLOPs.
- Discuss the failure cases where the method underperforms baselines and provide guidance on layer selection.

## Score and Decision

The paper makes a clear, well-motivated contribution by identifying and addressing a genuine limitation in ILD. The experimental validation is thorough across multiple architectures and datasets, and the theoretical justification is sound. However, the limited comparison against only one ILD baseline and the inconsistent improvements across layers prevent this from being a strong accept. The core idea is novel and practically useful, warranting acceptance.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>