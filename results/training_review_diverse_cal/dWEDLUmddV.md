Now I have all the evidence I need to verify each claim against the paper. Let me compose the final review.

---

## Summary

This paper identifies and quantifies negative correlations between trajectory segments in dataset distillation via trajectory matching (TM), showing that matching one segment can increase the matching loss of others. It frames this as a continual learning problem where naive sequential learning causes catastrophic forgetting, and proposes ConTra — a concurrent training method that matches multiple segments simultaneously using multi-task learning. The method achieves consistent improvements over prior TM-based methods on CIFAR-10, CIFAR-100, Tiny ImageNet, and ImageNet-1K (the latter in the appendix), and its concurrent training component generalizes as a plug-in module for existing methods like MTT and DATM.

## Strengths

1. **Systematic identification and quantification of negative correlations between trajectory segments.** The paper provides theoretical framing (Theorem 1 linking negative correlation to accumulated trajectory error) and extensive empirical evidence (PCC heatmaps in Figure 2 across different IPCs) demonstrating that matching one segment can increase the matching loss of others. This directly supports the paper's central claim that segmented matching overlooks harmful interactions. (Section 4.1, Section 4.2, Figure 2)

2. **Consistent state-of-the-art performance across multiple benchmarks and settings.** ConTra surpasses DATM on CIFAR-10 by 3.1%/1.5% at IPC 1/10, achieves lossless condensation at 20% IPC on CIFAR-10/100 and 10% IPC on Tiny ImageNet, and consistently outperforms baselines on CIFAR-100 and Tiny ImageNet (Table 1, 5 runs with standard deviations). (Table 1, Section 6.2)

3. **Demonstration that concurrent training is an effective plug-in module.** Simply replacing the sampling loss in MTT or DATM with the concurrent training loss (Equation 8) yields consistent improvements of 1.1–3.6% and 0.3–1.6% respectively, confirming generalizability beyond a single method. (Table 3, Section 6.4)

4. **Comprehensive ablation and analysis of key design choices.** The paper investigates the effect of the number of tasks K (Figure 4 left), the balance coefficient β (Figure 4 right), curriculum learning (Table 4 left), and training time vs. convergence speed (Table 4 right), providing insight into why and when concurrent training works best. (Section 6.4, Figure 4, Table 4)

5. **Validation of cross-architecture generalization.** ConTra distilled with ConvNet achieves the best test accuracy among TM-based methods on AlexNet, VGG11, ResNet18, and DenseNet121 at both IPC 10 and IPC 50, showing strong transferability of the distilled synthetic datasets. (Table 2, Section 6.3)

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

1. **Theorem 1 is a tautological decomposition rather than a substantive theoretical result.** Theorem 1 states that the accumulated error of the last segment is the sum of initialization errors and matching errors from all preceding segments. This follows directly from the definitions and does not provide bounds, conditions, or guarantees about when negative correlation leads to increased error. The paper's argument that "minimizing one δᵢ may increase other δⱼ" is intuitive and plausible, but the theorem adds no formal support beyond what is already described in prose. While this does not undermine the paper's empirical contributions, the abstract's claim of theoretical analysis is overstated. (Section 4.1)

2. **Direct evidence of catastrophic forgetting in the actual training procedure is missing.** The paper frames sequential segment matching as a continual learning problem but measures forgetting indirectly: the correlation heatmaps (Figure 2) show that matching a *fixed* segment causes other segments' losses to rise, which demonstrates interference. However, the actual training procedure samples segments randomly from a range each iteration (not sequentially in a fixed order), and the paper does not track the matching loss of a fixed reference segment over training iterations to show that standard TM actually "forgets" it. The existing evidence is reasonable but could be strengthened — e.g., by measuring whether the loss on a previously matched segment rises as the synthetic dataset is updated to match other segments. (Section 4.2, Section 5)

3. **Hyperparameter selection for K and β is empirical.** The number of concurrent tasks K and the balance coefficient β are ablated (Figure 4) but optimal values vary per dataset and IPC, and no principled guidance is provided for choosing them without tuning. This somewhat limits practical deployability. (Section 6.4, Figure 4)

### Trivial

- The curriculum learning component (Section 5, "Information capacity") is introduced briefly and used only at very low IPC (1 and 10). The paper acknowledges it is not a primary contribution. The ablation in Table 4 left clarifies its effect. This is fine but the presentation could better separate it from the main concurrent training contribution.

## Nice-to-Haves

- **Comparison with multi-objective optimization baselines:** The paper frames the problem as one of conflicting objectives but does not compare against methods that handle such conflicts explicitly (e.g., gradient surgery, weighted loss terms, or other multi-task balancing techniques). A brief discussion or comparison would strengthen positioning.
- **Segment-level forgetting measurement:** As noted in Weakness #2, tracking the matching loss of a fixed reference segment over actual training iterations would provide more direct evidence of forgetting in the random-sampling procedure.
- **Theoretical characterization of when negative correlation increases error:** Theorem 1 could be meaningfully extended by characterizing conditions under which negative correlation causes ε_{T-1} to increase (e.g., under Lipschitz conditions on gradient updates or by linking to Hessian spectral properties).

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Granularity mismatch between correlation analysis and matching procedure (Harsh Critic #1):** The critic argues that the correlation analysis uses epoch-level granularity while the method uses segment-level granularity. **Removed as factually wrong.** The paper explicitly states in Section 4.2: "a complete training trajectory comprises 40 epochs where each representing a segment with multiple checkpoints." The paper also refers to "the i-th segment (epoch)" (line 98), confirming that epochs ARE the segments used in the analysis. The granularity matches the method exactly. Furthermore, Figure 3 uses the same setup to show ConTra's effect, providing internal consistency.

- **ImageNet-1K results not in main paper (Harsh Critic #4):** The critic claims the abstract's ImageNet-1K claim is unverifiable. **Removed as a missing-appendix issue.** Section 6.6 states "We can scale up ConTra to ImageNet-1K using TESLA" and references appendix tables and figures. The parser strips appendix sections from all papers; these results exist in the original submission. Per hard rule: remove weaknesses about missing appendix content.

- **Missing proof of Theorem 1 (Harsh Critic "Missing Parts"):** The critic notes "The proof of Theorem 1 is omitted." **Removed as a missing-appendix issue.** The paper states "The proof of Theorem.1." — the proof is deferred to the appendix, which the parser strips.

## Novel Insights

The most insightful observation from the cross-examination of reviews is that the paper's central empirical finding — that *matching one segment increases the loss on other segments* — is itself a form of forgetting measurement, just at a coarser granularity than what one would ideally want. The correlation heatmaps (Figure 2) essentially measure cross-task interference in the space of segment-matching losses, which is precisely the quantity that matters for the continual learning analogy. The critic's request for "tracking a fixed reference segment over time" would add process-level confirmation, but the static correlation analysis already identifies the core problem. The key bridge the paper could build is to show that the PCC values in Figure 2 predict the magnitude of improvement from ConTra (i.e., datasets/IPCs with stronger negative correlations see larger gains), which would unify the analysis and the method into a single predictive framework.

## Suggestions

- Strengthen the continual learning framing by directly measuring whether, during standard TM training, the matching loss on a held-out reference segment increases over iterations (direct forgetting measurement).
- Consider extending Theorem 1 to characterize conditions (e.g., gradient Lipschitzness, Hessian properties) under which negative correlation provably increases accumulated error, rather than just stating a decomposition.
- Add a brief discussion or one baseline comparison with multi-objective optimization techniques (gradient surgery, loss weighting) to contextualize the simplicity of concurrent training.
- Provide heuristic guidance for choosing K and β across datasets (e.g., K proportional to number of epochs in the matching range) to improve practical deployability.

## Score and Decision

**Originality:** The paper identifies a genuinely overlooked issue (negative correlations between trajectory segments) — existing TM methods treated segment matching as independent, and the paper shows this is incorrect. The proposed fix (concurrent training) is simple but effective, and the plug-in demonstration shows it generalizes.

**Importance of research question:** Understanding interactions between segments in trajectory matching is directly relevant to improving dataset distillation, a growing field. The finding that negative correlation varies with IPC and can be mitigated by concurrent training is valuable.

**Claims supported:** The central claims are well supported by the experiments on CIFAR-10, CIFAR-100, and Tiny ImageNet. The ImageNet results are in the appendix. The theoretical claim (Theorem 1) is overstated — it is a notational decomposition, not a substantive theorem.

**Soundness:** The experimental methodology is sound — 5 runs with standard deviations, cross-architecture validation, plug-in ablations, ablation of key hyperparameters. No fatal flaws.

**Clarity:** The paper is clearly written and well-structured. The heatmap visualizations effectively communicate the key finding.

**Value to community:** The identification of negative correlations is likely to influence future TM-based methods, and the simple plug-in nature of ConTra makes it easy to adopt. The correlation analysis methodology may also be reused.

The paper has no fatal or major weaknesses. The two most significant issues — the tautological nature of Theorem 1 and the lack of direct forgetting measurement — are minor concerns that do not undermine the core empirical contribution. The paper's strengths (clear problem identification, consistent empirical gains, plug-in generalizability, thorough ablation) clearly outweigh these issues.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>