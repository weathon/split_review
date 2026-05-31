Now I have all the information needed. Here is the consolidated final review.

---

## Summary

This paper proposes Multi-Expert Collaboration (MEC), a method for heterogeneous multi-teacher knowledge distillation (Knowledge Amalgamation). MEC replaces the conventional single-head student classifier with multiple expert-specific classifiers (multi-head design) and introduces an anchor-based Helmholtz Free Energy (HFE) self-normalization loss to align the outputs of these classifiers. The motivation is grounded in an analysis showing that logit misalignment between teacher and student degrades performance, and that a single shared classifier suffers from interference as the number of experts/classes increases. Experiments on CIFAR-100 and ImageNet-100 with disjoint-class expert splits report "over 10%" average accuracy improvement over existing methods.

## Strengths

- **Principled problem formulation with supporting analysis.** Section 3 provides a concrete gradient analysis (Eq. 1–2) showing how a misaligned teacher logit can incorrectly guide the student, and an empirical correlation between prediction accuracy and logit alignment rate (Figure 2b). The paper also defines explicit criteria (Criterion 1 and 2) for heterogeneous knowledge alignment: in-stage data should have higher confidence, and confidence should be consistent across classifiers. This analysis directly motivates the problem and the design choices.

- **Multi-head classifier architecture directly addresses the identified interference issue.** The paper replaces a single shared-output classifier with multiple expert-specific heads (Section 4.1.2), which is a clean architectural solution to the interference problem documented in Section 3 (Figure 3). The scalability experiment (Figure 5) shows that MEC maintains accuracy as the number of experts grows, while single-head baselines degrade sharply — a concrete demonstration that the design choice works.

- **Anchor-based HFE self-normalization is a novel alignment mechanism.** The idea of constraining each classifier's Helmholtz Free Energy to a fixed anchor Δ (Eq. 7) to achieve consistent energy levels across classifiers is a technically interesting contribution. The use of free energy from the OOD detection literature (Liu et al. 2020) as an alignment regularizer in multi-teacher distillation is, to the best of my knowledge, novel.

## Weaknesses

### Fatal
None.

### Major

- **Baseline methods are not named, making the central quantitative claim unverifiable.** The experiments section (Section 5.3, lines 218–222) states that MEC was compared with "existing heterogeneous multi-teacher knowledge distillation methods" and achieves "over 10% average accuracy improvement," but **no specific baseline method names appear anywhere in the paper**. Table 1 reports numbers but the column headers are image-based; the surrounding text never identifies which prior methods (e.g., which of Shen et al. 2019, Ye et al. 2020, Xu et al. 2022, etc.) were re-implemented or compared against. Without knowing the baselines, the reader cannot tell whether the improvement is over a weak strawman or the strongest prior work. The paper repeatedly contrasts "traditional methods" with MEC, but this is not a substitute for named, calibrated baselines. This is a structural evaluation flaw that undermines the paper's headline contribution.

- **The ablation study does not isolate the novel HFE component from the multi-head architecture.** The ablation (Table 3) compares "only MERL (single-head + representation learning)" vs. "MERL + CAL (multi-head + HFE loss)." CAL bundles together the multi-head classifier architecture and the HFE self-normalization loss. There is no variant with **multi-head classifiers but without the HFE loss** (i.e., just cross-entropy and KD on each head). Therefore, the accuracy gain attributed to CAL could be entirely due to the multi-head architecture, with the HFE alignment contributing nothing. Since the HFE self-normalization is claimed as a core contribution, this gap is significant. The paper's core methodological contribution is not properly evidenced.

- **Key hyperparameter Δ (the HFE anchor) is never specified.** Eq. 7 constrains each classifier's free energy to a fixed anchor Δ, but its value is never reported. Without knowing Δ, the results are not reproducible, and the sensitivity of performance to this choice is unexplored.

### Minor

- **Missing training details compromise reproducibility.** The paper does not report: the temperature T (used in Eq. 10), the loss weights λ₁ and λ₂ (Eq. 11), the number of training epochs, batch size, data augmentation strategy, whether the student backbone is also ResNet-18, or the number of independent runs with variance/confidence intervals. The learning rate is given as 10⁻⁴ (line 202). These omissions prevent reproduction and make it impossible to assess the statistical reliability of the reported improvements.

- **Limited heterogeneity in the experimental setup relative to the paper's motivating scope.** The problem framing (line 12) discusses teachers "trained based on different architectures, training data, and task objectives." However, all expert models in the experiments use the same architecture (ResNet-18, line 202) and are trained on disjoint subsets of the same dataset (CIFAR-100 or ImageNet-100). "Heterogeneity" reduces to different class sets within the same domain and architecture. Genuinely heterogeneous scenarios — e.g., ResNet vs. VGG vs. ViT teachers, or different source datasets/domains — are not tested. The paper's claims about handling "heterogeneous" teachers are therefore narrower than advertised.

- **Textual description of free energy and confidence is mathematically inconsistent.** The paper states that "in-stage data generally exhibits higher free energy (i.e., higher confidence scores)" (line 140). However, given the definition Fᵐ(x) = −log Σ_y exp(hᵐ(x)[y]) (Eq. 6), higher logits (higher confidence) produce more negative (i.e., lower) free energy. The inference rule in Eq. 10 correctly selects the classifier with the lowest free energy (m* = argmax(−Fᵐ(x))), so the method itself is consistent, but the textual claim at line 140 is backwards and will confuse readers.

### Trivial
None.

## Nice-to-Haves

- An ablation variant with multi-head classifiers but no HFE loss would cleanly isolate the contribution of the HFE mechanism.
- Experiments with genuinely heterogeneous teacher architectures (e.g., ResNet, VGG, ViT) would match the paper's motivating scope.
- Reporting Δ, T, λ₁, λ₂, and training epochs would improve reproducibility.
- A grid search or sensitivity analysis for the anchor Δ would strengthen confidence in the method's robustness.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Strength: "Substantial and consistent empirical gains" (Strength Finder Point 4).** This strength claims that MEC outperforms all baselines with "over 10% improvement." It conflicts with the verified weakness that baseline methods are not named — the quantitative claim cannot be evaluated without knowing what was compared. Removed per the rule that when a strength and a verified weakness disagree, the weakness wins.

- **Strength: "Per-expert task accuracy analysis" (Strength Finder Point 5).** Depends on the same baseline identification issue. Removed for the same reason.

- **Strength: "Ablation study isolating contributions" (Strength Finder Point 6).** This claims that the ablation shows "each module is necessary for the best performance." This directly conflicts with the verified weakness that the ablation bundles multi-head architecture with HFE, and does not isolate the HFE component. Removed.

- **Criticism: "The paper does not define independence or alignment precisely."** Section 3 defines Criterion 1 and 2, which serve as operational definitions. While these are not formal mathematical definitions, they are stated clearly enough to guide the method design.

- **Criticism: "Gradient analysis identifies a problem but the method doesn't directly address it."** The multi-head design does address this by isolating each expert's logits to its own classifier, preventing one expert's wrong logits from interfering with another expert's classes. The connection is present.

- **Criticism: "It is unclear why features are halved in size or why a reconstruction loss is needed."** These are design choices explained in the text (line 116–117). The lack of a dedicated ablation for the reconstruction loss is a reasonable suggestion, but not a core weakness.

- **Criticism: "The paper does not discuss how MEC differs from prior methods concretely."** The related work section cites relevant prior KA methods, and Section 3 identifies specific limitations (interference in shared classifiers, misaligned logits) that MEC addresses. The contrast is present at the level argued by the paper's framing.

## Novel Insights

None beyond the paper's own contributions. The reviews surface known failure modes in ML evaluation (unnamed baselines, incomplete ablation design) that apply broadly but do not add new insight about the paper's subject matter.

## Suggestions

1. **Name every baseline method explicitly** in the experimental section (e.g., "we compare against the following KA methods: Shen et al. 2019 (logit concatenation), Ye et al. 2020 (data-free KA), Xu et al. 2022 (model-heterogeneous training), and a single-head student with cross-entropy + KD baseline"). Table 1 legends should clarify what each column corresponds to.

2. **Add an ablation variant: multi-head classifiers without HFE loss.** Train the multi-head student using only cross-entropy and KD per head, without the ℒₐₗ energy constraint. This will isolate whether the HFE mechanism provides additional benefit beyond the architectural change.

3. **Report all missing hyperparameters:** Δ, T, λ₁, λ₂, epochs, batch size, data augmentation, and the student backbone architecture. Report results over at least 3 random seeds with mean and standard deviation.

4. **Correct the free-energy/confidence relationship** in the text (line 140). The statement should read something like: "in-stage data generally exhibits lower (more negative) free energy, corresponding to higher confidence scores."

5. **Add at least one experiment with genuinely heterogeneous teachers** (different architectures or different source datasets) to match the paper's motivating claims.

## Score and Decision

This paper identifies a real problem in multi-teacher knowledge distillation and proposes a reasonable architectural approach (multi-head classifiers + HFE alignment). The problem formulation, analysis of misalignment, and scalability motivation are strengths. However, the evaluation has two significant gaps: (1) the baseline methods are not named, rendering the headline "10% improvement" unverifiable; and (2) the ablation does not isolate the HFE component from the multi-head architecture, so the core methodological contribution is not demonstrated. Combined with missing hyperparameters and limited experimental scope, the evidence presented does not meet the bar for acceptance. The paper would require major revisions, particularly a complete evaluation with named baselines and a proper ablation, before its claims can be assessed.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>