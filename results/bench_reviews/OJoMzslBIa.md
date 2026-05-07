Now I have good calibration anchors. Let me write the final consolidated review.

## Summary

ReweightOOD proposes a similarity-dependent reweighting mechanism for contrastive learning in distance-based OOD detection. The key idea is to multiply within-class and between-class cosine similarities by sigmoid-based reweighting factors inside a contrastive loss—prioritizing "hard" pairs (low within-class similarity, high between-class similarity) over "easy" ones—to produce more compact class clusters and greater inter-class dispersion. The paper reports substantial FPR improvements over baselines and prior methods on CIFAR-10/100 and ImageNet-100 benchmarks.

## Strengths

- **Addresses a meaningful problem**: Improving embedding geometry for distance-based OOD detection is a well-motivated goal, and the intuition that contrastive learning should prioritize hard pairs rather than treating all pairs equally is sound.

- **Strong empirical improvements**: ReweightOOD achieves a large improvement over the unweighted baseline (FPR 40.32 vs. 65.42 on CIFAR-100 with KNN) and outperforms existing contrastive methods like CIDER and KNN+ across both KNN and Mahalanobis postprocessors (Tables 3–4). The consistency of improvements across architectures (ResNet-18, WRN-40-2, DenseNet) and datasets (CIFAR-10/100, ImageNet-100) adds credibility.

- **Preserved classification accuracy**: Linear-probe accuracy of 75.54% on CIFAR-100 is comparable to the 74.96% cross-entropy baseline, confirming OOD gains don't trade off ID performance.

- **Joint evaluation with two postprocessors**: Testing both KNN and Mahalanobis distance scoring demonstrates the representation improvement transfers across postprocessing choices.

## Weaknesses

### Major

- **The "centroid dispersion" metric is defined and interpreted incorrectly, invalidating the claim about inter-class separation.** The paper defines centroid dispersion as $d_{ab} = \frac{\mu_a \cdot \mu_b}{\|\mu_a\|_2 \|\mu_b\|_2}$ with an upward arrow (↑), indicating higher is better. But this formula is cosine similarity: higher values mean centroids are *closer* in angle, not more dispersed. If the intent was angular distance (arccos of cosine similarity), the formula should be $\arccos(\cdot)$ and the direction would be correct. As written, claiming "higher dispersion" using cosine similarity is either a formula error or a directional error. This directly undermines the central explanatory claim that ReweightOOD increases inter-class dispersion, since Table 2's reported improvement in this metric actually shows increased angular similarity (i.e., less dispersion), not more.

- **The loss does not cleanly implement the claimed "reweighting" mechanism, and the paper does not address gradient interactions.** The proposed loss modifies the exponents as $\exp(\sigma(\mathcal{T}_B) \cdot s_b / \tau)$ rather than applying external importance weights. Unless the sigmoid factors are detached from the gradient graph (which the paper never states), the gradients flow through the reweighting factors, meaning the method is not simply up/downweighting pair contributions—it is transforming the effective similarity in potentially complex ways. With the reported hyperparameters $(m_w=2, c_w=1)$, for positive pairs the function $\phi_w(s) = \frac{s}{1+e^{2s+1}}$ is *not monotonically increasing* over $[-1,1]$, so well-aligned positive pairs can receive gradients that do not strictly increase their similarity. The paper's mechanistic story (hard positives get more weight, easy ones less) does not match what the loss actually optimizes, and no analysis of the resulting effective objective is provided.

- **Insufficient controlled ablation to attribute gains to the reweighting mechanism.** The paper compares ReweightOOD against the baseline (unweighted) contrastive formulation and other methods, but does not ablate individual components (positive-only vs. negative-only reweighting, detached vs. non-detached weights, alternative monotone weighting functions, or standard hard-negative mining). Since the method introduces 4 new hyperparameters tuned on Gaussian noise and modifies the loss form, attributing the ~25-point FPR reduction specifically to the similarity-dependent reweighting is not established.

### Minor

- **"MES radius" is mislabeled.** The formula $r_{cl} = \max_{\mathbf{h}_i \in \mathcal{H}_{cl}} \|\mathbf{h}_i - \mu_{cl}\|_2$ computes the maximum distance from the empirical centroid, not the true minimum enclosing sphere (which could have a different center with a smaller radius). It is a valid class compactness measure, but calling it "Minimum Enclosing Sphere" is technically incorrect. Renaming it to "maximum centroid distance" or "class radius" would be more precise.

- **Hyperparameter tuning on Gaussian noise contradicts the "no OOD needed" framing.** The paper emphasizes that "all experiments assume the unavailability of OOD/outliers during training" but tunes the four reweighting hyperparameters on Gaussian noise validation, which is an out-of-distribution signal. This is common practice in the field but creates tension with the stated setup. A transfer experiment (tuning on one dataset, applying unchanged to another) or ID-only validation would strengthen the claim.

- **FPR@95 is loosely described.** The paper states "lower FPR suggests a lower probability of ID samples getting misclassified as OOD" (line 122), but FPR@95 actually measures OOD samples incorrectly classified as ID at 95% ID TPR. This is a minor wording issue but could confuse readers.

- **No per-OOD-dataset breakdowns or variance across seeds** are reported in the main body for the primary CIFAR-100 experiment, making it hard to assess whether improvements are consistent or driven by particular OOD datasets.

### Trivial

- The $38\%$ improvement claim in the abstract is ambiguous about whether it is relative or absolute—the actual FPR drop from ~65 to ~40 is ~38% *relative* reduction, not absolute.

## Nice-to-Haves

- Controlled ablations of the loss components (positive-only, negative-only, detached weights, alternative weighting functions) would substantially strengthen the mechanistic claim.
- Analysis of the effective gradient landscape (plotting $\phi_w(s)$ and $\sigma(\mathcal{T}_B) \cdot s_b$ as functions of similarity for the reported hyperparameters) would clarify what the loss actually optimizes.
- Per-dataset results with confidence intervals across multiple seeds.
- Correcting the centroid dispersion metric to use angular distance would make the geometric story coherent.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Claim that the contrastive loss formulation (Section 3.2) is "not standard SupCon"**: The paper's formulation is a reasonable log-softmax-style contrastive objective. While not identical to the SupCon formulation in Khosla et al., this is not a weakness—it is a valid design choice. The paper compares against SupCon as a separate baseline, and the comparison is appropriate.

- **Concern about FPR@95 threshold set on "training data"**: The harsh critic misreads the relevant sentence. Line 32 says "The threshold $\lambda$ is often set for a 95% true positive rate on training data," which describes the standard convention. Whether they use training data or a held-out ID validation set for threshold setting is not a substantive flaw.

- **Demand for comparison with focal-style contrastive and hard-pair mining baselines**: While these would be nice-to-have comparisons, the paper's main contributions are in the OOD detection context, and the existing comparisons against SupCon, CIDER, KNN+, and posthoc methods are within the field's norms. This is a suggestion, not a substantive weakness.

- **Request to prove the loss optimizes MES or dispersion**: The paper makes intuitive claims about geometry, not formal optimization guarantees. The geometric claims should be evaluated on whether they hold empirically (which the centroid dispersion metric issue does affect), not on whether they have formal proofs.

- **Concern about the ImageNet-100 fine-tuning setup being a "different regime"**: The paper explicitly frames this as a compatibility experiment, and showing improvement under fine-tuning is a legitimate contribution. Criticizing it for not matching the from-scratch setup is scope creep.

- **Strength removed: "Direct quantitative evidence linking reweighting to improved embedding geometry"**: This claimed strength is invalid because the "centroid dispersion" metric is cosine similarity (not dispersion), so the purported evidence for increased inter-class separation is unreliable.

- **Strength removed: "Well-motivated and specific reweighting formulation"**: The formulation is conceptually motivated but the specific implementation does not cleanly implement reweighting (gradients flow through the sigmoid), so this is not a strength as stated.

- **Request for seed variance**: For CIFAR-scale OOD experiments with contrastive training, single-run evaluation is common in the field. This is a nice-to-have, not a substantive weakness.

- **Concern about UMAP visualization**: UMAP is presented as qualitative support only (alongside quantitative tables). This is standard practice and not a weakness.

- **Concern about notation reuse $\tau$ for temperature and transformation**: The paper uses $\tau$ for temperature and $\mathcal{T}$ for the transformation, which are distinct symbols. This appears to be a parser artifact, not a genuine notation issue.

## Novel Insights

The paper's most interesting observation is that within standard contrastive learning for OOD detection, the implicit assumption of equal pair importance creates redundancy—easy positive pairs that are already tightly clustered continue to receive gradient signal that provides diminishing returns for OOD separation, while hard pairs that matter most for the embedding geometry receive proportionally less attention. However, the current implementation does not cleanly separate the "reweighting" mechanism from the similarity transformation (since gradients flow through the weighting factors), and the geometric analysis uses an incorrectly oriented metric, leaving the mechanistic explanation of *why* the method works unclear despite promising empirical results.

## Suggestions

1. **Fix the centroid dispersion metric**: Replace $d_{ab} = \frac{\mu_a \cdot \mu_b}{\|\mu_a\|_2 \|\mu_b\|_2}$ with angular distance $\arccos\left(\frac{\mu_a \cdot \mu_b}{\|\mu_a\|_2 \|\mu_b\|_2}\right)$, and verify whether ReweightOOD actually increases inter-class angular separation or the current result is an artifact of the metric direction.

2. **Clarify whether sigmoid factors are detached**: Add a sentence stating whether the reweighting factors are treated as constants (detached) during backpropagation, and analyze/discuss the difference.

3. **Add ablation experiments**: At minimum, show the unweighted baseline vs. ReweightOOD with identical training settings and hyperparameter tuning protocols, and ideally positive-only and negative-only reweighting variants.

4. **Report per-OOD-dataset results** for the main CIFAR-100 table so readers can assess consistency.

## Score and Decision

**Calibration anchors:**

| Paper | Avg Score | Comparison |
|-------|-----------|------------|
| mUXdysoxEP (Neural Collapse OOD) | 6.75 | Stronger: formal NC grounding, cleaner geometry claims, similar results level |
| uNkKaD3MCs (PALM mixture-of-prototypes OOD) | 5.75 | Comparable: similar embedding-geometry-for-OOD motivation, reweighting mechanism |
| 83le3arfeA (Balanced Hyperbolic OOD) | 5.50 | Comparable: geometry-overclaim concerns, moderate results |
| am7BPV3Cwo (ImOOD reweighting for imbalanced OOD) | 5.75 | Comparable: reweighting-based approach for OOD, similar scope |
| jQnXDGxdDG (FIRM contrastive anomaly detection) | 3.80 | Weaker: limited novelty, narrow improvements |
| hlijRgXTDK (Pathologies of OOD detection) | 4.75 | Different type: position paper, not directly comparable |
| VAmVEghgoC (NC-OOD detection) | 4.50 | Comparable: questionable directional geometry claims, moderate experiments |
| HACk-OOD (hypercone OOD) | 5.00 | Comparable: geometry claims for OOD, similar experiment scale |

The paper sits in a similar methodological space to PALM (5.75) and ImOOD (5.75) but has a more serious technical issue with its central explanatory metric (the centroid "dispersion" is actually cosine similarity, with the wrong direction claimed). This is not just a naming issue—it means the paper's explanation for *why* the method works is unreliable. The contrastive loss also has a mismatch between the claimed reweighting mechanism and what the math actually implements. However, the empirical results are genuinely strong (25-point absolute FPR improvement over baseline), and the method works across architectures and postprocessors. The paper is comparable to VAmVEghgoC (4.50, also had questionable geometry claims) and somewhat stronger due to better empirical results, but weaker than the 5.5–5.75 range papers whose theoretical claims were more solid. 

**Assessment on axes:**
- Originality: Moderate—the difficulty-aware reweighting idea is intuitive and has parallels in metric learning, but its application to contrastive OOD detection is new
- Importance of research question: High
- Claims well supported: No—the geometric explanation is undermined by metric errors, and the mechanistic claim isn't verified by ablation
- Soundness of experiments: Moderate—strong results but insufficient ablation
- Clarity: Moderate—key definitions are wrong/misleading
- Value to community: Moderate—the empirical results are useful but the explanation for them is unreliable

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>