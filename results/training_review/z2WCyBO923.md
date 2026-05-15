Now I have a thorough understanding of the paper. Let me compose the final consolidated review.

---

## Summary

This paper proposes a Mixture-of-Experts (MoE) framework for dataset distillation to address cross-architecture performance degradation. The key ideas are: (1) splitting the real dataset into disjoint subsets assigned to different expert distillation models, (2) minimizing distance correlation between expert feature representations to encourage diversity, and (3) mixing synthetic images from different experts during evaluation via a mixup-based fusion strategy. Experiments across three DD methods (IDC, IDM, MTT) on CIFAR-10/100 show that multi-expert distillation generally outperforms single-expert baselines at the same storage budget, and the framework also improves supervised contrastive learning performance.

## Strengths

- **Consistent improvement across three distillation paradigms**: Table 1 shows that for IDC, IDM, and MTT on CIFAR-10/100, the multi-expert setup (NoE=2) outperforms the single-expert baseline on most target architectures (ConvNet-3, VGG11, ResNet18, AlexNet) at the same total IPC budget, supporting the claim that the framework helps mitigate cross-architecture degradation.

- **Component-level ablation validates contributions**: Table 2 isolates the effects of distance correlation minimization and mixup-based fusion. The progression from "w/o DC" → "w/ DC" → "w/ DC+Fusion" shows each component adds value across all three DD methods, providing causal evidence for the proposed techniques.

- **Expert-aware mixup versus vanilla mixup**: Table 3 shows that mixing images across different experts consistently outperforms both vanilla mixup (mixing without expert constraints) and no-mixup, confirming that the complementary information captured by different experts is the source of the benefit.

- **Generalization to contrastive learning**: Table 5 shows that MoE-distilled ImageNette achieves 46.62% SupCon accuracy versus 34.57% for single-expert IDM, and also improves transfer to ImageWoof and STL-10, demonstrating applicability beyond standard classification.

- **Method-agnostic design**: The framework is evaluated with three fundamentally different DD objectives (gradient matching via IDC, trajectory matching via MTT, distribution matching via IDM), showing broad applicability.

## Weaknesses

### Fatal
None.

### Major

- **The improvement is partially confounded with real-data subset size.** The paper compares a single expert (NoE=1, IPC=10/20) that distills using **all** real data against multiple experts (NoE=2, IPC=5×2 or 10×2) where each expert uses a **disjoint subset** of real data. The single expert sees the full real dataset; each multi-expert sees only a fraction. The paper does not include a control where a single expert is trained on the same reduced real-data subset as each multi-expert (e.g., a single expert with IPC=10 trained on only half the real data). Without this, the observed improvement could partially arise from reduced overfitting to the distillation architecture due to less training data per expert, rather than from the MoE structure itself. The ablations (Table 2) partially mitigate this by showing that MoE-specific components (DC, fusion) further improve over the base multi-expert, but the base comparison itself remains confounded.

### Minor

- **Some configurations underperform with multi-expert, without adequate analysis.** In Table 1, MTT on CIFAR-100 with IPC=10 shows multi-expert underperforming single-expert on several architectures (the paper notes "most" results improve but does not investigate these counterexamples). Understanding why the method fails on certain dataset/method/architecture combinations is important for assessing its general applicability, and the paper provides no analysis of these failure cases.

- **Cross-architecture evaluation is limited to CIFAR-10/100.** The higher-resolution datasets (ImageNette, STL-10) are used only in the SupCon experiment, where only ConvNet-4 is tested. The paper's primary claim about cross-architecture generalization thus rests entirely on two low-resolution datasets (32×32). Validation on higher-resolution datasets with multiple target architectures would strengthen the claim.

- **Selection of "easy samples" for expert initialization is not justified or ablated.** The paper initializes synthetic subsets using the top 10–30% of samples with lowest classification loss, which biases each expert toward easy examples. This design choice could limit the diversity the method claims to promote, yet no ablation studies its impact or compares it against random subset selection.

- **Distance correlation implementation details are underspecified.** The paper states that pairs of expert subsets are randomly selected "once every few iterations" for dCor computation, but does not specify how frequently, which feature layers are used, or whether the same pretrained model φ is used for all pairs. While these are not fatal, they affect reproducibility.

### Trivial
- The mixup-based fusion formulation (Eq. 6) states the image mixing equation but does not specify how labels are handled. In standard mixup, labels are mixed proportionally — the paper should be explicit about this for clarity.

## Nice-to-Haves
- A control experiment where a single expert uses the same amount of real data as each multi-expert (as discussed in Major weaknesses) would sharpen the paper's claims.
- Visual comparisons of synthetic images from different experts versus a single expert would help illustrate whether the MoE framework produces qualitatively different per-class synthetic data.
- A comparison against alternative diversity-promoting baselines (e.g., ensemble distillation with random seeds, or the model pool technique from IDM, which the paper excluded) would better isolate the specific benefit of the MoE structure.

## Removed Points

These points are flagged to be removed, treat them with caution:

- *Criticism that Table 2 is "incomplete and does not isolate contributions"* (Harsh Critic Point 2): The table clearly compares "w/o DC" (base multi-expert), "w/ DC" (adds distance correlation), and "w/ DC+Fusion" (adds both). The naming is standard and the progression isolates each component's contribution. The single-expert baseline is already provided in Table 1. This criticism misreads the table's purpose.

- *Criticism that the distance correlation objective is "unnecessary or even detrimental"* (Harsh Critic Point 3): The ablations (Table 2) show that adding dCor consistently improves over the base multi-expert without dCor. The data splitting and dCor serve complementary roles — splitting ensures different data inputs, while dCor prevents convergent representations. The criticism is speculative and contradicted by the evidence.

- *Criticism that claims are "overstated given inconsistent results"* (Harsh Critic Point 4): The paper uses measured language ("most of the multi-expert results built by IDM and MTT outperformed"). The critic presents this as an absolute claim, which the paper never makes.

- *Criticism about missing theoretical explanation* (Section 1 note): The paper provides an intuitive explanation (diversity helps cross-architecture generalization), which is standard for an empirical systems paper. Demanding formal theory is scope creep beyond community norms for this type of work.

- *Criticism about modified baselines*: The paper is transparent about modifications to IDC and IDM. This is standard practice in DD research and does not constitute unfair comparison since the modifications are documented.

- *Criticism about mixup labels being undefined*: Label mixing is standard practice from the original mixup paper and does not need re-derivation.

- *Criticism about SupCon only testing ConvNet-4*: The SupCon experiment is a separate analysis of representation learning quality, not a cross-architecture test. The scope of this experiment is appropriately scoped.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add the critical control experiment**: Compare a single expert trained on a reduced real-data subset (matching the amount seen by each multi-expert) against the full multi-expert framework. This would cleanly separate the benefit of data splitting from the benefit of MoE-specific components (dCor and fusion).

2. **Analyze and explain failure cases**: Investigate why MTT on CIFAR-100 at IPC=10 shows multi-expert underperforming single-expert for several architectures. This analysis would clarify whether the method is sensitive to dataset complexity or the base DD algorithm.

3. **Extend cross-architecture evaluation to higher-resolution datasets**: Even one experiment on ImageNette or STL-10 with multiple target architectures would significantly strengthen the paper's primary claim about cross-architecture generalization.

4. **Ablate the easy-sample selection**: Compare random subset assignment versus loss-based selection for expert initialization to show whether the current choice helps or hinders diversity.

5. **Add a reproducibility paragraph** specifying the exact frequency of dCor computation (every N iterations) and which feature layers are used.

## Score and Decision

This paper addresses a real problem (cross-architecture degradation in DD) with a simple, modular, and intuitively appealing framework. The experiments span three DD methods, multiple architectures, and include ablation studies that verify each component's contribution. The SupCon results provide additional evidence beyond standard classification.

However, the core comparison between single-expert and multi-expert is confounded by unequal real-data subset sizes — the single expert uses all real data while each multi-expert uses only a fraction. The absence of a control experiment for this confound weakens the central claim. Additionally, some configurations underperform without analysis, and cross-architecture evaluation is limited to CIFAR resolution.

These are addressable weaknesses, and the paper's contributions (dCor-based diversification, expert-aware mixup fusion, method-agnostic integration) are genuine. The paper would benefit from the suggested control experiment and failure analysis before it can fully support its claims.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>