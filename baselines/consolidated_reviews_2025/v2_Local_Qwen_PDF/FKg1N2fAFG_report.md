## Summary
# Final Review Report

## Summary
This paper addresses the critical issue of architecture overfitting in dataset distillation, where distilled data optimized for a shallow training network yields poor performance when evaluated on architecturally distinct deep test networks. The authors propose a unified training framework for test networks that integrates four key components: (1) a three-phase DropPath scheduler with improved shortcut connections to dynamically adjust effective depth and preserve feature quality, (2) small-to-large knowledge distillation using the shallow training network as a teacher, (3) periodical learning rate resets synchronized with architectural changes, and (4) stronger k-fold data augmentation. Extensive experiments across multiple distillation algorithms (FRePo, MTT), datasets (CIFAR-10/100, Tiny-ImageNet), and IPC settings demonstrate that the proposed methods significantly narrow the performance gap, enabling deep test networks to consistently outperform the original shallow training architectures. The methods also show transferability to training on limited real data.

## Strengths
1. **Clear Problem Formulation:** The paper correctly identifies architecture overfitting as a critical bottleneck in dataset distillation, where distilled data optimized for shallow networks fails to generalize to deeper test architectures. This is a highly relevant and practically important issue.
2. **Cohesive Methodological Framework:** The proposed combination of three-phase DropPath, improved shortcut connections, and small-to-large knowledge distillation is well-motivated. The mechanistic link between dynamic depth reduction (DropPath) and feature-space alignment with the shallow training network is insightful.
3. **Comprehensive Empirical Validation:** The experiments are extensive, covering multiple distillation algorithms (FRePo, MTT), datasets (CIFAR-10/100, Tiny-ImageNet), IPC settings (1, 10, 50), and diverse test architectures (ResNet, AlexNet, VGG). The ablation studies effectively validate the contribution of each component.
4. **Practical Transferability:** The demonstration that the proposed methods also improve performance on limited real data (e.g., 100 samples) highlights the broader utility of the framework beyond synthetic dataset distillation.

## Weaknesses
1. **Narrative and Motivation Clarity:** The introduction and abstract mix comparison targets, ambiguously referring to "existing methods" when discussing test-network performance. The motivation for using deeper test networks relies on generic "representation power" claims rather than explicitly addressing the feature-space mismatch caused by shallow training networks.
2. **Mechanistic Justification for Auxiliary Components:** Section 3.3 (Training and Data Augmentation) lists periodical LR, Lion optimizer, and k-fold augmentation with minimal mechanistic explanation. The connection between architectural changes (DropPath keep rate shifts) and learning rate resets is implicit, and the choice of Lion lacks a clear link to generalization on synthetic data.
3. **Related Work Positioning:** The related work dismisses factorization methods solely based on IPC requirements without discussing their underlying mechanism for improving transferability (e.g., feature disentanglement). This misses an opportunity to contrast the proposed test-time regularization approach with feature-space optimization approaches.
4. **Contribution Statement Specificity:** The contribution statements are too generic. Contribution 2 claims "extensive experiments" as a contribution, which is standard practice rather than a scientific advance. The specific technical innovations (e.g., three-phase DropPath, small-to-large KD) are not explicitly highlighted in the contribution list.

## Key Issues
1. **Feature-Space Mismatch Mechanism Underexplained:** The core reason deep networks fail on distilled data is that the data is optimized for the shallow training network's feature space. The manuscript mentions "architecture overfitting" but does not explicitly frame the problem as a feature-space or inductive bias mismatch. Clarifying this would strengthen the motivation for DropPath (dynamic depth alignment) and KD (manifold regularization).
2. **Synergy Between Components Needs Explicit Analysis:** While Table 2 shows that combining DropPath and KD yields the best results, the text only briefly states that KD is marginal without DropPath due to architectural differences. A deeper analysis of *why* they are synergistic (e.g., DropPath creates shallower pathways that KD can more effectively regularize) would significantly improve the paper's theoretical grounding.
3. **Generalization to Real Data Lacks Context:** Section 4.2 shows improvements on limited real data, but the connection to the distilled data setting is not fully explored. Is the improvement due to the same mechanisms (depth regularization, manifold alignment), or is it simply a strong low-data training recipe? Clarifying this distinction would help bound the claims appropriately.

## Actionable Suggestions
1. **Refine Abstract and Introduction Narrative:** Rewrite the abstract to explicitly state that the gains apply to *test networks* evaluated on distilled data, and add a representative quantitative highlight (e.g., maximum accuracy gain). In the introduction, replace the generic application list with a focused statement on architecture overfitting as the critical bottleneck, and explicitly frame the problem as a feature-space mismatch between shallow training and deep test networks.
2. **Strengthen Methodological Explanations:** In Section 3.1, clarify that DropPath dynamically reduces effective depth, forcing the deep network to learn representations compatible with shallower pathways. In Section 3.2, reframe knowledge distillation as "small-to-large distillation" and explain that the shallow teacher provides a stable target distribution for the synthetic data, regularizing the deep student against overfitting to noisy samples. In Section 3.3, briefly justify periodical LR resets (adapting to architectural changes), Lion (flatter minima for generalization), and k-fold augmentation (expanding effective data diversity).
3. **Improve Related Work Positioning:** Briefly discuss how factorization methods improve transferability via feature disentanglement, and contrast this with the proposed test-time regularization approach. This will better position the paper within the broader dataset distillation landscape.
4. **Sharpen Contribution Statements:** Replace the generic "extensive experiments" contribution with a statement about the unified framework or the observed phenomenon (e.g., deep networks surpassing shallow ones under the proposed scheme). Explicitly name the key methods (three-phase DropPath, small-to-large KD) in Contribution 1.

## Storyline Options + Writing Outlines
### Abstract Outline (Complete)
- **S1 (Problem & Domain):** Dataset distillation synthesizes compact training sets but suffers from architecture overfitting: distilled data optimized for a specific training network yields poor performance when evaluated on architecturally distinct test networks.
- **S2 (Significance/Challenge):** This transferability gap severely limits the practical deployment of distilled data, especially when deep test networks are required for downstream tasks.
- **S3 (Prior Gap):** Existing methods focus on improving the distillation objective but often neglect the training dynamics of the test network, leaving the feature-space mismatch between shallow training and deep test networks unaddressed.
- **S4 (Proposed Method):** We propose a unified training framework featuring a three-phase DropPath scheduler, improved shortcut connections, small-to-large knowledge distillation, and adaptive augmentation to bridge this mismatch.
- **S5 (Key Result & Implication):** Extensive experiments demonstrate that our approach enables deep test networks to consistently outperform the original shallow training architectures across multiple distillation algorithms and low-IPC regimes, significantly narrowing the cross-architecture performance gap.

### Introduction Outline (Complete)
- **P1 (Big Picture & Motivation):** Deep learning requires massive data, motivating dataset distillation to synthesize compact, highly informative training sets. While effective at data compression, current methods face a critical bottleneck: severe architecture overfitting.
- **P2 (Concrete Gap):** Distilled datasets are heavily biased toward the feature space of the (typically shallow) training network. When evaluated on deeper test networks, performance degrades significantly due to this feature-space mismatch, limiting practical utility.
- **P3 (Proposed Idea):** We argue that mitigating overfitting requires aligning the inductive bias of deep test networks with the shallow training architecture. We propose a unified framework that dynamically adjusts effective depth (DropPath), regularizes predictions via the shallow teacher (KD), and stabilizes training on synthetic data (adaptive LR/augmentation).
- **P4 (Evidence Preview):** Our methods synergistically bridge the architectural gap, enabling deep networks to surpass shallow baselines on distilled data. The framework also generalizes to training on extremely limited real data.
- **P5 (Contribution Summary):** (1) Unified framework with three-phase DropPath and small-to-large KD; (2) Demonstration that deep networks can outperform shallow training architectures under our scheme; (3) Generalization to low-data real-world training scenarios.

## Priority Revision Plan
| Priority | Action Item | Expected Impact | Effort |
|---|---|---|---|
| **P0** | Rewrite Abstract and Introduction to explicitly frame architecture overfitting as a feature-space mismatch and clarify comparison targets. | Improves narrative coherence and immediately communicates the core problem and solution. | Low |
| **P0** | Refine Contribution statements to explicitly name key methods (three-phase DropPath, small-to-large KD) and replace "extensive experiments" with a conceptual insight. | Strengthens the perceived scientific contribution and novelty. | Low |
| **P1** | Enhance Section 3.1-3.3 with mechanistic justifications: link DropPath to dynamic depth alignment, KD to manifold regularization, and auxiliary techniques to synthetic data challenges. | Provides deeper theoretical grounding and justifies engineering choices. | Medium |
| **P1** | Update Related Work to briefly contrast test-time regularization (proposed) with feature-space optimization (factorization methods). | Better positions the paper within the broader dataset distillation landscape. | Low |
| **P2** | Add a short analysis paragraph discussing the synergy between DropPath and KD (e.g., how DP creates pathways that KD can effectively regularize). | Strengthens the methodological narrative and explains ablation results. | Medium |
| **P2** | Polish Conclusion to summarize validated findings (deep networks surpassing shallow ones) and specify concrete future work directions. | Leaves a stronger final impression and guides future research. | Low |

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory
| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|---|---|---|---|---|---|---|
| E1 | Mitigate architecture overfitting on distilled data | FRePo/MTT, CIFAR-10/100, Tiny-ImageNet, IPC 1/10/50, ResNet/AlexNet/VGG | Test Accuracy | Deep networks surpass shallow training networks; gaps narrowed | C1, C2 | Variance reported only in appendix |
| E2 | Validate component synergy (Ablation) | CIFAR-10, FRePo, IPC=10, ResNet18 | Test Accuracy | Full method > w/o DP > w/o KD > Baseline | C1 | Lacks statistical significance tests |
| E3 | Improve performance on limited real data | CIFAR-10 subsets (0.002-0.1 fraction) | Test Accuracy | ResNet18/50 outperform 3-layer CNN at low fractions | C3 | Teacher performance saturates at higher fractions |
| E4 | Hyperparameter sensitivity | Keep rate, KD weight/temp, LR schedule | Test Accuracy | Method robust to hyperparameter choices | C1 | Limited to single dataset/architecture |

### Research-Theme Gap Diagnosis
The core claim of "mitigating architecture overfitting" is well-supported by E1 and E2. However, the causal mechanism (feature-space alignment via dynamic depth and manifold regularization) is inferred rather than directly measured. Additionally, the generalization to real data (C3) is demonstrated but not deeply analyzed in the context of the distilled data findings.

### Proposed Research Experiments
| Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Est. Cost | Expected Gain |
|---|---|---|---|---|---|---|---|
| C1 (Mechanism) | DropPath aligns test network depth with training network depth | Vary training network depth (3, 5, 7 layers) and measure gap reduction | Standard DD baselines | Accuracy gap | Gap reduction scales with training depth | Medium | Validates depth-alignment hypothesis |
| C1 (Synergy) | KD regularizes the shallow pathways created by DropPath | Analyze feature similarity (e.g., CKA) between teacher and student with/without DP | w/o DP, w/o KD | CKA score | Higher CKA with Full method | Low | Provides mechanistic evidence for synergy |
| C3 (Generalization) | Framework improves low-data generalization beyond CIFAR | Apply to ImageNet-100 or STL-10 with 100-500 samples | Standard low-data baselines | Test Accuracy | Consistent gains across datasets | High | Strengthens real-data generalization claim |

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score:** 6.5/10
**Post-Revision Target:** [7.5, 8.5]/10

**Rationale:** The paper addresses a highly relevant and practically important problem in dataset distillation (architecture overfitting) and proposes a cohesive, well-validated framework. The empirical results are strong, demonstrating that deep test networks can consistently outperform shallow training architectures. However, the current score is moderated by the generic narrative framing, underexplained mechanistic justifications for auxiliary components, and vague contribution statements. With the suggested revisions to clarify the feature-space mismatch motivation, strengthen the methodological explanations, and sharpen the contribution claims, the paper has strong potential to reach a higher score.