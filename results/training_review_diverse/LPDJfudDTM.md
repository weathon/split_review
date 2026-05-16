Now I have all the information needed to construct the final authoritative review.

Here is my consolidated meta-review:

## Summary

This paper proposes Multi-Expert Collaboration (MEC), a method for heterogeneous multi-teacher knowledge distillation (knowledge amalgamation). MEC replaces the conventional single-head student classifier with multiple expert-specific classifier heads (ensuring knowledge independence) and introduces an anchor-based Helmholtz Free Energy (HFE) self-normalization loss to align these heads at a consistent energy level. The method is evaluated on CIFAR-100 and ImageNet-100 under label-partitioned multi-expert settings, reporting average accuracy improvements over 10% compared to existing methods.

## Strengths

1. **Multi-head classifier architecture directly addresses the knowledge interference problem.** The paper identifies a genuine limitation of single-head classifiers in multi-teacher distillation—when heterogeneous knowledge is compressed into a shared output layer, conflicting decision boundaries degrade performance. Replacing the single head with expert-specific classifiers (initialized from teacher weights) is a clean architectural fix, and the ablation study (Table 3) shows that this design alone (CAL module) improves accuracy over the single-head baseline by ~4–6%, confirming the independence benefit.

2. **HFE-based alignment provides a principled calibration mechanism.** The paper identifies that alignment of heterogeneous knowledge requires both (a) each head to be confident on its own classes and (b) confidence levels to be comparable across heads. Anchoring each head's Helmholtz Free Energy to a common scalar Δ is a theoretically grounded way to achieve both, building on established energy-based OOD detection literature (Liu et al. 2020). The ablation confirms CAL (which includes L_al) contributes meaningful gains beyond MERL alone.

3. **Gradient analysis motivating misalignment.** Section 3 derives how misaligned teacher logits produce incorrect gradient signals during KD (Eq. 3), and Figure 2b shows a positive empirical correlation between alignment rate and prediction accuracy. This provides a principled motivation for why alignment matters in the heterogeneous setting.

4. **Ablation study validates both components.** Table 3 systematically ablates MERL and CAL: MERL alone (feature alignment with single head) yields ~72%, CAL alone (multi-head without representation learning) improves to ~76%, and the full model reaches ~78%, demonstrating independent contributions from each module.

## Weaknesses

### Fatal
None.

### Major

1. **Baselines in Table 1 are not identified by name, making the central empirical claim unverifiable.** The paper states "existing heterogeneous multi-teacher knowledge distillation methods" were compared and that MEC achieves "over 10%" improvement, but Section 5.2 (Baselines Setup) does not name a single specific prior method that was re-implemented or compared against. The related work section lists many KA methods (Shen 2019, Ye et al. 2019, Ye et al. 2020, Luo et al. 2020, Xu et al. 2022, Zhang et al. 2023, Gao et al. 2024, and others), but the experiments never specify which of these were used as baselines, how they were configured, or whether they were given the same data/architecture. The only described comparator is "traditional student models with shared output layers" — an underspecified baseline. For a new-method paper whose primary evidence is a >10% accuracy gain, this is a critical omission.

2. **Mismatch between the claimed "heterogeneous" setting and the experimental design.** The paper motivates the work with "teachers trained based on different architectures, training data, and task objectives" (line 12). However, all experiments use ResNet-18 feature extractors for every teacher, trained on disjoint label subsets of the *same* dataset (CIFAR-100 or ImageNet-100). The only source of heterogeneity is the label partition. The method may well be effective in this label-disjoint setting, but the paper's framing promises generalization to architecture-level heterogeneity (CNN vs. ViT, different training domains) and the experiments do not test this. This gap weakens the claimed scope of the contribution.

3. **Training data specification is ambiguous, affecting reproducibility.** The paper states "using only a small amount of data samples for training" (line 92) and describes selecting 20 samples per class via nearest class mean (Section 5.2). However, the overall loss function (Eq. 9) involves expectations over data distributions without clarifying whether the student is trained only on these 20 samples per class, on the full dataset, or on some combination. This ambiguity makes it impossible to determine the exact training protocol and undermines reproducibility. If the 20-sample selection is applied only to MEC and not to baselines, the comparison would be fundamentally unfair. This needs clarification.

4. **No variance/confidence intervals reported.** No results include standard deviations or error bars across multiple runs. Given the modest dataset sizes (CIFAR-100, ImageNet-100) and the centrality of the >10% improvement claim, it is impossible to assess statistical reliability.

### Minor

1. **Unclear which classifier head's output is used for L_ce during training.** The paper specifies that at inference, the head with highest HFE is selected for prediction (Eqs. 10–11). But during training, the cross-entropy loss L_ce(p^s, y) in Eq. 9 is not tied to a specific head. It is unclear whether L_ce is applied to all heads jointly, only the highest-HFE head, or the head corresponding to the ground-truth expert. This should be specified.

2. **No ablation or sensitivity analysis on the anchor value Δ.** The anchor-based self-normalization loss (L_al) uses a fixed scalar Δ, but the paper provides no analysis of how Δ is chosen, how sensitive results are to its value, or what range of Δ is reasonable. This is the central hyperparameter of the novel alignment mechanism and its lack of analysis weakens the methodological contribution.

3. **The "traditional method" in Figure 5 is not identified.** Figure 5 shows MEC maintaining accuracy as the number of experts grows while "traditional" methods degrade, but the specific traditional method used for this comparison is not named. Without knowing what "traditional" means, this figure is difficult to interpret.

4. **Introduction oversimplifies existing KA methods.** The claim that "current heterogeneous multi-teacher knowledge distillation only refines the student's knowledge by simply concatenating logits" (line 16) is an oversimplification. The related work section itself acknowledges that KA methods use both classification score learning and feature-level alignment (lines 48–49). The rhetorical framing diminishes the paper's positioning without being necessary to motivate the contribution.

### Trivial
None.

## Nice-to-Haves

- Testing on genuinely heterogeneous teachers (different architectures such as ResNet + ViT, different training datasets) would strengthen the claim of applicability to heterogeneous settings.
- Visualizing the learned feature space (e.g., t-SNE) to show that the shared backbone learns separable representations across all classes while classifier heads specialize.
- Reporting model size and training time overhead of the multi-head architecture.
- A discussion of limitations or failure cases (e.g., overlapping label sets, large number of experts) would strengthen the paper.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The paper does not cite or discuss [Ye et al. 2019, Xu et al. 2022]."** The related work section (lines 48–49) explicitly cites both Ye et al. (2019) and Xu et al. (2022). This criticism is factually incorrect and is removed.
- **"Eq. 8 is incorrect: it writes log(p_hat/T)/(p_t/T)."** The equation formatting appears garbled in the text extraction; the original PDF likely has proper KL divergence notation. Per the formatting-artifact rule, this criticism is removed.
- **"The tables are inserted as images that are unreadable in the extracted text."** This is a PDF parsing artifact. The table content exists in the original submission. The substantive criticism about unnamed baselines is retained in the Major section above.
- **Criticism about missing appendix sections.** The parser strips appendix content from all papers. Per the hard rule, this is removed.
- **"The HFE alignment says nothing about how a head responds to other classes."** The paper explicitly states the known property (from Liu et al. 2020) that "in-stage data generally exhibits higher free energy than out-stage data" (line 140). Constraining in-stage HFE to Δ therefore implicitly separates in-stage from out-stage via this established property. The criticism overstates the gap; the related concerns about missing ablation on Δ and lack of HFE distribution analysis are retained in the Minor section.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Name every baseline method in Table 1 explicitly** (which KA methods were re-implemented, with citations). Describe the configuration used for each baseline (architecture, optimizer, hyperparameters, data access). This is the single most important fix.
2. **Clarify the training data protocol:** Is the student trained on the full dataset or only the 20 selected samples per class? If the latter, ensure baselines receive the same data budget.
3. **Specify how L_ce is computed during training** (which head's output, how ground truth maps to heads).
4. **Add an ablation on the anchor value Δ** to demonstrate robustness and provide guidance for choosing it.
5. **Report standard deviations** over at least 3 runs.
6. **Add at least one experiment with genuinely heterogeneous teachers** (different architectures or different training datasets) to match the paper's motivational framing.
7. **Identify the "traditional" method in Figure 5** by name.

## Score and Decision

The paper identifies a real problem and proposes a reasonable architectural solution with a novel alignment mechanism. The multi-head classifier design and HFE-based calibration are legitimate contributions. However, the experimental evaluation has a critical hole: the baselines used to substantiate the central claim (the >10% improvement) are not named or described, making the primary result unverifiable. Combined with the mismatch between the claimed heterogeneous setting and the evaluated label-partitioned setting, and several methodological ambiguities, the paper in its current form does not meet the standard for acceptance. The core ideas are salvageable and potentially valuable, but the evaluation requires substantial revision.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>