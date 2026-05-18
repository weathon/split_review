Now I have all the information I need. Let me produce the final consolidated review.

---

## Summary

This paper proposes a mixture-of-experts (MoE) framework for dataset distillation that splits the distillation budget among multiple expert models, each distilling a disjoint subset of the original data. A distance correlation minimization loss encourages inter-expert diversity, and a cross-expert mixup-based fusion strategy is applied during downstream training. The goal is to improve cross-architecture generalization of distilled datasets, a known limitation of existing DD methods. The framework is evaluated by integrating it with three representative DD methods (IDC, IDM, MTT) on CIFAR-10/100 and higher-resolution datasets.

## Strengths

- **Novel and well-motivated idea.** Applying an MoE structure to dataset distillation to promote diversity and mitigate cross-architecture degradation is a genuine contribution. The approach of having multiple experts each distill a disjoint subset and using distance correlation to enforce distinctiveness is creative.

- **Consistent cross-architecture improvement across three DD paradigms.** Table 1 shows that for IDC on CIFAR-10/100, the multi-expert setup (NoE=2) outperforms the single-expert baseline on all four target architectures (ConvNet-3, VGG11, ResNet18, AlexNet) at both IPC=10 and IPC=20. Similar trends hold for most IDM and MTT results, suggesting the framework generalizes across distillation objectives.

- **Ablation validates individual components.** Table 2 shows that adding distance correlation alone improves performance across IDM, IDC, and MTT, and adding mixup fusion on top yields further gains. The full combination obtains the best results in nearly every configuration, confirming both components are complementary and individually beneficial.

- **Ablation isolating cross-expert mixup.** Table 3 compares cross-expert mixup (proposed), vanilla mixup, and no mixup. The proposed strategy outperforms both baselines on all target architectures, confirming that mixing across experts (rather than within the same expert) leverages complementary information.

- **Broader utility beyond standard classification.** Table 5 shows that the multi-expert distilled dataset (IDM, ImageNette) improves supervised contrastive learning accuracy (34.57% → 46.62%) and transfer performance to ImageWoof and STL-10.

## Weaknesses

### Major

1. **Confounded comparison due to real-data subset selection.** The paper states (Implementation Details) that for IDC and IDM, each expert's synthetic images are initialized from easy real samples (top 10%–30% lowest-loss samples). For the single-expert (NoE=1) baseline, it is not specified whether the same easy-sample selection is applied or whether the full real dataset (including hard samples) is used. If the single-expert uses the full dataset while multi-expert uses only easy samples, the comparison in Table 1 is confounded: the multi-expert improvement could stem from distilling easier data rather than from the MoE structure or diversity-promoting losses. The ablation study in Table 2 (which compares variants within the multi-expert setup) is not affected by this confound, but the headline comparison between NoE=1 and NoE=2 in Table 1 is. A controlled experiment is needed: compare single-expert (using easy-only samples) vs. multi-expert (each using disjoint easy subsets), and single-expert (full data) vs. multi-expert (random disjoint subsets). Without this, the paper's core claim rests on shaky ground.

2. **Under-specified distance correlation computation.** The loss is ℒ_Corr = dCor²(φ(Sᵢ), φ(Sⱼ)), but the paper does not explain how the pairing between the two sets of feature vectors is performed for distance correlation, which is defined for paired samples. While index-based pairing of same-size sets is the natural approach, it should be stated explicitly. The update frequency ("once every few iterations") is left vague. The reference to (Zhen et al., 2022) and (Székely et al., 2007) provides the mathematical definition but not the operational choice for this specific setting. This affects reproducibility and the reliability of the claimed diversity benefit.

### Minor

1. **MTT real-data subset selection not specified.** The easy-sample selection is mentioned only for IDC and IDM. For MTT, which requires training trajectories on real data, it is unclear whether different experts see different real-data subsets, different trajectories, both, or neither. This is a nontrivial detail since the trajectory-matching objective depends on which real data is used.

2. **Several hyperparameters not reported.** Specific values for the SGD learning rate and momentum applied to synthetic image optimization are not given (the paper only says "fixed learning rate and a momentum, following prior works"). For MTT, the inner-loop length N (number of synthetic-data training steps) is not stated. While deferring to prior work is common, the paper should at minimum state whether the same values as the original methods were used.

3. **Mixup label handling not clarified.** The paper specifies Beta(0.5) for image interpolation but does not state whether labels are also interpolated (canonical mixup) and, if so, how labels from different experts are combined. This is needed to reproduce the evaluation procedure.

4. **Figure 1 vs. implementation inconsistency in initialization.** Figure 1's caption states "each expert initializes its synthetic data from the original full dataset," while the Implementation Details section says initialization uses only easy samples (top 10–30%). The paper should reconcile these statements.

### Trivial

- None that survive filtering.

## Nice-to-Haves

- **Additional architectures (e.g., ViT).** The cross-architecture claim is tested on three non-architectures beyond ConvNet-3. While VGG11, ResNet18, and AlexNet are reasonable and standard, adding a ViT or deeper ConvNet would strengthen the generalizability claim.

- **Analysis of diminishing returns with more experts.** Table 4 shows mixed results when going from 2 to 3 experts. The paper attributes this to "diminishing returns" but provides no analysis of why (e.g., does the distance correlation loss saturate? Do subsets become too small?).

- **Training time / compute cost analysis.** The paper runs multiple distillation processes in parallel (or sequentially) and adds a distance correlation loss. Reporting overhead would be useful for practitioners.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Fusion strategy not properly scoped"** — The paper clearly presents fusion as part of the proposed framework (Section 3.3). Table 3 reports performance without fusion. This is proper scoping for a method paper. REMOVED: the reviewer's concern reflects a misunderstanding of standard method paper practice.

- **"Same φ for dCor and distillation loss could introduce trivial correlation"** — Using the same pretrained feature extractor for both the distillation loss and the diversity loss is standard and expected. There is no confound here; the two losses operate on different terms in the objective. REMOVED: not a genuine weakness.

- **"Only 4 architectures tested is a limitation"** — Four architectures spanning different design families (VGG, ResNet, AlexNet) is standard in DD research. This is a nice-to-have, not a weakness. DOWNGRADED to Nice-to-Haves.

- **"Baseline methods used without their full original pipeline"** — The paper explicitly states which components are omitted and why (e.g., "omitting the multi-formation aspect," "excluded the model queue technique"). This is transparent and reasonable for integrating methods into a new framework. REMOVED.

- **"Paper lacks a clear description of how many real images each expert receives"** — The paper states "top 10% to 30% of samples," which provides the range. REMOVED: the description is sufficient.

- **"The 'decoupling' of synthetic data and model parameters for IDC is mentioned but not explained"** — This is a detail from the original IDC paper; readers can refer there. REMOVED: standard practice to reference original methods.

- **"How is the gradient of distance correlation w.r.t. synthetic images computed?"** — Distance correlation is composed of differentiable operations (Euclidean distances, means); gradients are handled by standard auto-diff frameworks. REMOVED: the reviewer is asking about standard automatic differentiation.

## Novel Insights

The most interesting observation across the reviews is that the distance correlation component and the mixup fusion component both show independent value in the ablation (Table 2), but their relative contributions vary noticeably across distillation methods. For IDM, distance correlation contributes more than fusion in some settings; for MTT, fusion contributes more. This suggests that the two components address different failure modes (representation diversity vs. feature integration) and that the optimal balance is method-dependent — an observation worth exploring further. None beyond the paper's own contributions.

## Suggestions

1. **Run a controlled experiment** that isolates the easy-sample confound: compare (a) single-expert with easy-only data vs. multi-expert with disjoint easy subsets, and (b) single-expert with full data vs. multi-expert with random (not easy-only) disjoint subsets. This will cleanly separate the effect of the MoE framework from the effect of easier distillation data.
2. **Specify how pairing works for distance correlation** between two synthetic subsets (index-based pairing, assuming equal sizes). State the update frequency for the dCor loss (e.g., every K iterations) and confirm that the gradient is computed via standard auto-differentiation.
3. **Report fusion-free performance in the main table** (or at least note the gap), since the distilled dataset alone underperforms without the prescribed mixup training procedure.
4. **Clarify MTT real-data usage** — state whether each expert receives different trajectories, different real subsets, or both.
5. **State specific hyperparameter values** (learning rate, momentum, MTT inner-loop length) or confirm they match the original papers exactly. Clarify label handling in mixup fusion.
6. **Reconcile Figure 1** (which says initialization from "original full dataset") with the Implementation Details (which say easy-sample initialization).

## Score and Decision

The paper introduces a genuinely novel and well-motivated idea, and the non-confounded ablation studies provide evidence that the individual components (distance correlation, cross-expert mixup) are effective. However, the main experimental comparison (Table 1) has a significant confounding factor: the single-expert baseline likely uses a different real-data selection than the multi-expert setup. This undermines confidence in the headline claim that the MoE structure itself is responsible for the improvement. The issue is fixable with additional controlled experiments, and the approach is worth pursuing, but in its current form the evidence is not clean enough to support acceptance.

MY FINAL SCORE: <pineapple>4.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>