Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

---

## Summary

This paper introduces MetaDD, a plug-in component for dataset distillation (DD) that improves cross-architecture generalization. The key idea is to decompose distilled data features into *meta features* (common recognition patterns consistent across architectures) and *heterogeneous features* (architecture-specific biases), then regularize the distillation process to maximize meta features by minimizing the variance of CAMs across a set of pre-trained auxiliary networks. The method is evaluated on CIFAR-10, Tiny-ImageNet, and ILSVRC-2012 across four DD baselines (DC, DM, MTT/TesLa, Sre2L), consistently outperforming prior cross-architecture methods GLaD and ModelPool while adding substantially less GPU memory overhead.

## Strengths

- **Novel and well-motivated conceptual framework.** The paper identifies a root cause of the cross-architecture gap in DD — that distilled data over-expresses heterogeneous (architecture-specific) features while lacking meta (shared) features — and validates this diagnosis through CAM visualizations (Figure 1) and a controlled erasure experiment (Figure 3). The experiment shows that erasing meta features from Tiny-ImageNet degrades ViT accuracy substantially, while erasing heterogeneous features of other architectures causes minimal loss, directly supporting the paper's conceptual decomposition.

- **Consistent cross-architecture accuracy gains across diverse settings.** MetaDD outperforms GLaD and ModelPool on both seen and unseen architectures across 3 datasets and 4 DD baselines. For example, on Tiny-ImageNet with DC (IPC=50), MetaDD achieves 13.8% average accuracy vs. GLaD's 12.5% (Table 1); on ILSVRC-2012 with TesLa (IPC=10), MetaDD achieves 13.1% vs. GLaD's 12.1%. Gains hold on unseen architectures (e.g., Sre2L on ILSVRC-2012: 15.8% on Vgg19 and 15.9% on Swin-S, neither included in the auxiliary set).

- **Substantially lower memory overhead than the prior state of the art.** Table 4 shows MetaDD adds ~2.7 GB to the MTT baseline on CIFAR-10 (19.9→22.6 GB) compared to GLaD's +19.2 GB (19.9→39.1 GB). On ILSVRC-2012 with TesLa, MetaDD adds ~7.7 GB vs. GLaD's +50.4 GB. This advantage is achieved by keeping auxiliary networks frozen, avoiding the generator memory cost that GLaD incurs.

## Weaknesses

### Fatal

None.

### Major

1. **Same-architecture accuracy is not reported, obscuring a potential trade-off.** The entire paper focuses on cross-architecture generalization, but never reports how MetaDD affects accuracy when the *same* architecture used for distillation is trained on the resulting distilled set. Since MetaDD explicitly suppresses heterogeneous features (which are the architecture-specific discriminative patterns the backbone relies on), same-architecture accuracy could plausibly degrade. Without this number, readers cannot evaluate whether the cross-architecture gains come at a cost to the primary DD use case. The backbone architecture (ConvNet or ResNet18) does not even appear in the evaluation columns of the main tables.

2. **Ablation is incomplete: the combined effect of all three loss terms is missing.** Table 5 tests each loss component individually (baseline MTT: 52.1; +L_ai: 52.4; +L_pos: 52.3; +var: 52.9) but never the full combination of all three that the method actually uses. Since the individual gains are small (0.2–0.8 points), the combined result is critical to assess whether the components are additive, redundant, or interfering. Without it, the ablation only tells half the story.

3. **No sensitivity analysis for the CAM binarization threshold.** The 0.5 threshold (Eq. 1) that defines which CAM pixels count as "high-confidence" — and thus what constitutes a meta feature — is never varied. CAM values are noisy, and this threshold directly controls what fraction of pixels are treated as meta vs. heterogeneous. A stability analysis across thresholds (e.g., 0.3, 0.5, 0.7) would substantially increase confidence in the method's robustness.

4. **Pre-trained auxiliary networks create an unaddressed distribution mismatch.** The auxiliary networks are pre-trained on the full original dataset and frozen. However, the distilled dataset is used to train *randomly initialized* models from scratch. Features that are discriminative and "meta" for a pre-trained network (which has seen the full data distribution) may differ from what is learnable by a fresh model on a tiny distilled set. The paper neither discusses this limitation nor tests it with a control (e.g., auxiliaries pre-trained on a different dataset like ImageNet for CIFAR-10 distillation).

### Minor

1. **Contagious generalizability claim lacks quantitative support.** The claim that meta features "transfer" to unseen architectures is supported only by qualitative CAM visualizations (Figure 8). No metric is provided that quantifies the correlation between meta feature overlap on unseen architectures and the accuracy improvements shown in the main tables.

2. **No analysis of how performance scales with the number of auxiliary networks.** The method uses 4 auxiliaries by default. How does performance change with |M|=1, 2, 3, 4, 5? This is directly relevant to the memory claim, since more networks increase overhead.

3. **The erasure experiment operates on the original dataset, not distilled data.** The validation experiment (Figure 3) erases pixels from original Tiny-ImageNet, then trains ViT from scratch. This supports the conceptual distinction between meta and heterogeneous features, but does not directly validate that the CAM-based operation during *distillation* produces the same effect. The link between the conceptual validation and the actual method is looser than claimed.

### Trivial

1. **Naming inconsistency.** The method is called "MetaDD" in the title, abstract, and most text, but appears as "MetaCAM" in Table 2 (CIFAR-10), Table 4 (memory/time), figure captions (Figures 2, 4), and algorithm labels. Authors should settle on one name.

## Nice-to-Haves

- **Clarify the role of the KL divergence term in L_ai.** The paper states that the KL divergence "maximumly displays heterogeneous features antagonistic to the main NN," but the mechanism (matching the auxiliary's output distribution to the backbone's) seems more like *suppressing* disagreement. An experiment isolating the effect of the cross-entropy term alone vs. the full L_ai would be informative.
- **Test auxiliary networks pre-trained on a different dataset** (e.g., ImageNet-pretrained auxiliaries for CIFAR-10 distillation) to disentangle dataset-dependence from architecture-invariance.
- **Add a limitations section** explicitly acknowledging the reliance on CAM-based feature definition, the threshold hyperparameter, and the pre-trained auxiliary assumption.

## Removed Points

- **Memory claim is misleading (from Harsh Critic, Critical Issue 3):** The reviewer argues that calling MetaDD "low-memory" is imprecise because backprop through frozen networks still requires storing activations and gradients. However, Table 4 clearly shows MetaDD adds ~2.7–7.7 GB vs. GLaD's +19.2–50.4 GB. The claim is well-supported and relative. This is not a genuine weakness. *Removed because the paper's evidence supports the claim.*
- **The erasure experiment "does not prove" the CAM definition is correct:** The reviewer frames this as a fatal flaw. In reality, the experiment provides reasonable empirical support for the conceptual framework — erasing CAM-defined meta features hurts all architectures, which is exactly the predicted behavior. The criticism overstates the problem. *Kept in Minor as a tighter formulation.*
- **"CAMs do not capture all feature types (texture, frequency, etc.):"** This is a statement about what CAMs cannot do, not a weakness of the paper — the method defines "feature" as spatial saliency, which is a defensible choice for its purpose. A paper is not required to solve all problems simultaneously. *Removed as a scope-creep criticism.*

## Novel Insights

None beyond the paper's own contributions. The reviewers' observations (incomplete ablation, missing same-architecture analysis, pre-trained mismatch) identify gaps in thoroughness but do not produce new insights about the data or problem that the paper itself does not articulate.

## Suggestions

1. **Report same-architecture accuracy** for all main experiments. Without this, the trade-off is invisible. If accuracy is preserved, this strengthens the paper considerably; if it degrades, the paper should discuss the implications honestly.
2. **Add the full-combination row to the ablation table** (Table 5) — baseline, each component alone, and all three together — for both MTT and Sre2L.
3. **Run a threshold sensitivity analysis** on at least one dataset (e.g., Tiny-ImageNet with DC) showing cross-architecture accuracy at thresholds 0.3, 0.4, 0.5, 0.6, 0.7.
4. **Add an experiment varying |M|** (number of auxiliary networks) to show how performance and memory scale.
5. **Discuss the pre-trained auxiliary limitation** explicitly, or add a control experiment using cross-dataset pre-trained auxiliaries.

## Score and Decision

**Originality:** Good — the meta/heterogeneous feature decomposition is a novel framing for the cross-architecture DD problem.  
**Importance:** Good — cross-architecture generalization is a recognized limitation of DD with practical significance.  
**Claims support:** Moderate — the central empirical claim (MetaDD improves cross-architecture accuracy) is supported, but key validations (combined ablation, same-architecture trade-off, threshold sensitivity) are missing.  
**Soundness:** Moderate — the experimental design is reasonable but the gaps in the ablation and the missing same-architecture analysis weaken the overall picture.  
**Clarity:** Good — the paper is well-structured and the motivation is clearly explained, despite a minor naming inconsistency.  
**Value to community:** Good — the method is plug-and-play with low overhead, making it practically useful.

The paper addresses a genuine problem with a clean, novel idea and provides consistent empirical evidence across multiple settings. The main weaknesses are gaps in thoroughness (missing ablation row, missing same-architecture results, no threshold sensitivity) rather than fundamental flaws in the approach. These are fixable with additional experiments. On balance, the contribution is solid and the paper would benefit from a revision addressing the above points.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>