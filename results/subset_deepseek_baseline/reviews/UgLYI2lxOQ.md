## Summary

This paper identifies a fundamental limitation in intermediate layer distillation (ILD): the regressor used to align teacher-student feature map dimensions creates an indirect knowledge transfer bottleneck. The authors propose a regressor-free ILD method that prunes the teacher's target layer to match the student's dimensions, enabling direct feature distillation. Experiments on CIFAR-100 and TinyImageNet with ResNet, VGG, and ShuffleNetV2 architectures show consistent improvements over traditional regressor-based FitNet, with some configurations even exceeding teacher accuracy.

## Strengths

- **Clear problem identification with empirical evidence**: The probing experiments (Figure 2) convincingly demonstrate that the regressor-based approach leads to suboptimal knowledge transfer, with the post-regressor feature map containing less usable information than even the pre-regressor features. This provides strong motivation for the proposed method.

- **Theoretical grounding via mutual information**: The paper provides a clean theoretical argument using the data processing inequality to show that the proposed method's mutual information lower-bounds that of the regressor-based approach (Eq. 5-6), assuming negligible pruning loss γ. This connects the empirical findings to information-theoretic principles.

- **Consistent empirical gains across diverse settings**: The method outperforms FitNet in 16 out of 22 layer-architecture-dataset combinations, often by substantial margins (e.g., 77.50% vs 75.40% on ResNet/CIFAR-100 Layer4, 49.23% vs 45.08% on ResNet/TinyImageNet Layer4). The ablation studies (probing analysis, direct feature map distillation comparison) further support the core claims.

## Weaknesses

### Major

- **Limited scope of architectures and tasks**: The paper only evaluates CNN-based architectures (ResNet, VGG, ShuffleNetV2) on image classification. The authors acknowledge this limitation but it significantly restricts the generality of the findings. Modern deep learning heavily uses Transformers (ViT, BERT, GPT), and the claim that "the structure makes it difficult to prune only specific layers" for ViT families is not sufficiently justified—structured pruning of attention heads or MLP dimensions is well-established. Without demonstrating applicability to Transformers or other modalities (NLP, speech), the practical impact is substantially reduced.

- **The mutual information argument has a critical gap**: The proof relies on the assumption that γ (information loss from pruning) is "negligibly small." While the paper shows pruned teacher accuracy remains close to the original, mutual information and task accuracy are not equivalent. The pruning process could discard information that is irrelevant for the teacher's own task but valuable for distillation to a different student architecture. The inequality I(f_t; f_s) - I(f_tp; f_s) ≤ γ is asserted without formal justification or empirical measurement of mutual information. The data processing inequality application (Eq. 5) is correct, but the overall bound is only as strong as the unverified γ assumption.

- **No comparison with alternative dimension-matching strategies**: The paper frames the choice as "regressor vs. pruning" but ignores other approaches: (1) using 1x1 convolutions on the teacher side instead of the student side, (2) adaptive pooling to match spatial dimensions, (3) linear projections that are shared between teacher and student, or (4) attention-based alignment. Without ablating these alternatives, it's unclear whether the benefit comes from removing the regressor specifically or from any method that achieves direct alignment.

### Minor

- **The method's advantage over logit distillation from pruned teacher is inconsistent**: In several cases (e.g., VGG/CIFAR-100 Layer1, ShuffleNetV2/CIFAR-100 Layer4), logit distillation from the pruned teacher matches or exceeds the proposed ILD method. The paper claims the method is "versatile because it can be readily applied to other ILD frameworks," but the standalone benefit over simpler logit distillation is not always clear.

- **Retraining overhead is not adequately discussed**: The teacher pruning step requires retraining, which adds computational cost. The direct feature map distillation experiment (Section 4.3.2) shows that without retraining, performance drops significantly. The paper should provide a cost-benefit analysis comparing the retraining overhead against the performance gains.

### Trivial

- The paper states "we share our source code" but the URL is anonymized and cannot be verified during review.

## Nice-to-Haves

- An analysis of which specific channels are pruned (e.g., visualization of pruned filters) would provide intuition about what information is being discarded and why it doesn't hurt distillation.
- A comparison with state-of-the-art ILD methods (e.g., AT, SP, RKD, CRD) would strengthen the claim that the regressor issue is a general problem, not just specific to FitNet.
- Experiments on larger-scale datasets (e.g., ImageNet-1K) would increase confidence in the method's scalability.

## Novel Insights

The paper's key insight is that the regressor in ILD acts as an information bottleneck, not just a dimension-matching tool. The probing experiments reveal that the regressor-transformed features contain less task-relevant information than the raw student features, which is counterintuitive—one would expect the distillation target to enrich the representation. This suggests that the gradient flow through the regressor during training may be suboptimal, and that direct alignment (via teacher pruning) avoids this issue. The mutual information analysis formalizes this intuition, though the empirical verification of the γ term remains an open question. The finding that pruning the teacher can improve distillation even beyond the original teacher's performance (consistent with Park & No 2022) is an interesting phenomenon that deserves further theoretical investigation.

## Suggestions

- **Address the Transformer limitation**: Either provide experiments on ViT-based architectures (e.g., DeiT-Tiny distilled from DeiT-Small) with appropriate structured pruning of attention heads or MLP dimensions, or provide a more rigorous argument for why the method cannot be extended. If the method is truly CNN-specific, this should be clearly stated as a limitation rather than left as future work.

- **Strengthen the mutual information analysis**: Measure or estimate the actual mutual information values (or a proxy like the Hilbert-Schmidt Independence Criterion) for the pruned vs. original teacher features with respect to the student features, rather than relying solely on accuracy as a proxy for γ.

- **Add baselines for alternative alignment methods**: Compare against (a) teacher-side 1x1 convolution to reduce teacher dimensions, (b) adaptive pooling, and (c) a learnable linear projection that is applied to both teacher and student features before computing the distillation loss. This would isolate whether the benefit is from removing the regressor or from the specific pruning mechanism.

- **Report standard deviations**: The paper states experiments were conducted five times with averages reported, but no standard deviations are shown. Adding error bars or confidence intervals would help assess the statistical significance of the improvements.

## Score and Decision

The paper addresses a genuine and under-explored problem in knowledge distillation, provides clear empirical motivation, and demonstrates consistent improvements. However, the limited architectural scope (CNNs only), the gap in the theoretical argument, and the lack of comparison with alternative alignment methods prevent it from being a definitive contribution. The core idea is sound and the experiments are well-executed within their scope, but the paper would benefit from broader validation before acceptance at a top venue.

MY FINAL SCORE: <score>6</score>
MY FINAL DECISION: <decision>Accept</decision>