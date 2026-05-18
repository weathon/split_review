Now I have a thorough understanding of the paper and can verify all claims. Let me compose my final consolidated review.

---

## Summary

This paper proposes FIRM (Focused In-distribution Representation Modeling), a multi-positive contrastive loss for anomaly detection. The key idea is to assign multiple positives for in-distribution (ID) samples (all ID samples in a minibatch are treated as positives for each other) to encourage compact ID clustering, while retaining a single-positive strategy for synthetic outliers to preserve their semantic diversity. This addresses the class-collision problem in vanilla contrastive learning for anomaly detection. Experiments on CIFAR-10, CIFAR-100, Fashion-MNIST, and Cats-vs-Dogs show consistent AUROC improvements over prior contrastive methods (CSI, DROC, NT-Xent, SupCon), and the method also performs well on unlabeled multiclass OOD detection.

## Strengths

1. **Well-motivated and novel contrastive objective tailored for anomaly detection.** FIRM's design (Equations 2–3) directly addresses the conflict between contrastive learning's pressure for uniform representations and anomaly detection's need for compact ID clusters. The asymmetric treatment — multiple positives for ID samples, single positives for synthetic outliers — is intuitive and clearly justified. The loss landscape visualizations in Figure 1 provide helpful intuition for why NT-Xent, SupCon, and FIRM behave differently.

2. **Consistent empirical gains across multiple benchmarks and scoring variants.** FIRM achieves a mean AUROC of 97.2% on CIFAR-10 with outlier exposure (OE), outperforming CSI (96.0% with \(s_{\mathrm{shift}}\)) and DROC (Table 1a). Similar improvements hold on CIFAR-100, Fashion-MNIST, and Cats-vs-Dogs (Tables 1b–1d). The gains are consistent across scoring functions (\(s_{\mathrm{con}}\), \(s_{\mathrm{shift}}\), \(s_{\mathrm{ens}}\)), showing the robustness of the learned representations.

3. **Ablation studies cleanly isolate the contribution of the loss function.** Table 4 directly compares NT-Xent, SupCon (binary and multiclass), and FIRM under otherwise identical conditions. FIRM yields higher AUROC and AULC across all four datasets (e.g., +2.5% AUROC on CIFAR-10 over NT-Xent), confirming that the multi-positive design — not augmentation tricks or ensembles — drives the improvement.

4. **Effective on unlabeled multiclass OOD detection.** Despite being designed for homogeneous ID settings, FIRM (w/ OE) achieves 96.2% AUROC on LSUN\* and 93.6% on ImageNet\* (Table 3), outperforming CSI (93.9% and 90.3%). This demonstrates the method transfers beyond strictly homogeneous ID scenarios.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **No quantitative results on MVTec-AD despite invoking defect detection framing.** The paper discusses CutPaste and NSA as synthetic outlier generation methods for defect anomaly detection (Section 2) and shows t-SNE visualizations on MVTec-AD (Figure 2), but reports no AUROC or similar metric on any defect detection benchmark. MVTec-AD is a standard benchmark in the anomaly detection literature; its absence from the evaluation creates an expectation gap. The paper's core claims are substantiated on semantic AD benchmarks, but the authors should either add quantitative results or explicitly scope the paper to semantic anomaly detection and remove or reframe the MVTec-AD reference.

2. **Missing quantitative comparison to UniCon-HA (Wang et al., 2023).** The Related Work section (line 142) discusses UniCon-HA as a closely related contrastive method that also uses a multi-positive strategy for anomaly detection, and distinguishes FIRM from it by noting that UniCon-HA relies on complex augmentations while FIRM focuses on the loss design. However, no experimental comparison is provided. Given the methodological proximity, a direct comparison under identical conditions would substantially strengthen the paper's claims.

3. **Unlabeled multiclass OOD detection results exhibit a conceptual tension not fully resolved.** The paper acknowledges (line 121) that FIRM's hyperparameters were tuned for homogeneous anomaly detection, and the method works well on unlabeled multiclass OOD despite the paper's framing that OOD detection requires inter-class variance. The brief acknowledgment is appreciated, but a more detailed explanation — e.g., why the k-NN based scoring function can still separate multimodal ID clusters despite the loss collapsing them — would strengthen the paper.

4. **No formal analysis connecting the loss to optimal anomaly detection behavior.** The paper argues intuitively (Section 2.1, Figure 1) that FIRM's loss landscape is better suited for anomaly detection than NT-Xent or SupCon, but does not provide a formal analytical argument. For example, a proof of why minimizing intra-class variance for ID samples while maximizing diversity among synthetic outliers is optimal under a distance-based scoring rule would be a valuable addition.

### Trivial
None.

## Nice-to-Haves

- An ablation comparing different synthetic outlier generation methods (e.g., rotations vs. CutPaste on CIFAR-10) under FIRM would strengthen the generality claims.
- Exploring sensitivity to backbone capacity (beyond ResNet-18 / 32×32 inputs) would improve understanding of the method's robustness.
- A quantitative measure of representation quality beyond AUROC (e.g., average intra-class ID distance vs. inter-outlier distance) would directly validate the loss's intended effect and complement the ablation in Table 4.

## Removed Points

- **"Unclear statistical significance / uncertainty"** (Harsh Critic's Critical Issue #3): The paper explicitly states "We report the mean and standard deviation of evaluation metrics over five runs" (line 103). The standard deviations are in the (image-format) tables that the parser could not extract; the paper does report them. The additional request for prose-level significance discussion exceeds standard practice for conference papers in this area.
- **"Hyperparameter details not visible in main text"**: The appendix (which contains these details) is stripped by the parser. The paper states it reports mean/std over five runs; hyperparameter details exist in the appendix of the original submission.
- **"The paper uses only ResNet-18 and 32×32 inputs"**: ResNet-18 is the standard backbone in this line of work (CSI, DROC, SSD all use it). This is not a weakness — it is the standard experimental setup for this subfield.
- **Strengths that are generic or conflict with verified weaknesses**: Some strengths from the Strength Finder are retained but adjusted; none were fully removed as they are all grounded in actual paper content.

## Novel Insights

The reviews surface one insight worth noting beyond the paper's own contributions: the asymmetric multi-positive strategy — treating ID samples as each other's positives while keeping synthetic outliers as singletons — is a clean resolution of a tension in prior work. CSI and DROC use single-positive contrastive objectives that still push ID samples apart; SupCon treats synthetic outliers as a class, collapsing their diversity. FIRM's design essentially says "the optimal representation for anomaly detection is one where normal samples occupy a tight cluster and every anomaly, synthetic or real, is isolated." This framing unifies several prior observations (the value of hard negatives, the danger of class collision, the utility of outlier exposure) into a single loss design. However, as noted in Weakness #4, this intuition lacks formal justification connecting it to optimal decision boundaries.

## Suggestions

1. **Add quantitative MVTec-AD results or explicitly scope the paper to semantic AD.** Either run the same evaluation protocol on MVTec-AD classes and report AUROC, or remove the MVTec-AD t-SNE plots and CutPaste/NSA discussion that imply an evaluation the paper does not deliver.
2. **Add a direct comparison to UniCon-HA** under the same evaluation protocol, since it is the most relevant concurrent method discussed in the paper.
3. **Provide a brief explanation** for why FIRM works on unlabeled multiclass OOD detection despite its design assumption of homogeneous ID, e.g., discussing how k-NN scoring can separate clusters even when the loss collapses them.
4. Ideally, add a **formal or analytical argument** connecting the multi-positive loss design to optimal anomaly detection, e.g., showing that the loss minimizes an upper bound on the probability of misclassifying an OOD sample.

## Score and Decision

The paper presents a clean, well-motivated modification of contrastive learning that yields consistent empirical improvements on standard semantic anomaly detection benchmarks. The weaknesses are real — the MVTec-AD expectation gap and the missing UniCon-HA comparison limit the completeness of the evaluation — but they do not invalidate the paper's core claim: FIRM outperforms NT-Xent, SupCon, CSI, and DROC on semantic anomaly detection. With modest revisions addressing the scope clarity and missing comparisons, this would be a solid contribution.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>