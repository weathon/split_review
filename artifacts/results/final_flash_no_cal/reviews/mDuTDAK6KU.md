I now have a thorough understanding of the paper. Let me compile the final review.

## Summary

KOALA is an adversarial detector that flags inputs as attacks when nearest-prototype classifiers using KL divergence and an L0-based metric disagree on the predicted class. The paper provides a formal theorem stating conditions under which this disagreement (and thus detection) is guaranteed, and a lightweight fine-tuning procedure that only requires clean images to shape embeddings. Experiments on ResNet/CIFAR-10 and CLIP/Tiny-ImageNet show that when the theorem's conditions are satisfied, detection is perfect, and on the full test sets KOALA achieves moderate detection performance.

## Strengths

- **Empirical verification of the theoretical guarantee**: Table 1 shows that on Theorem-compliant samples, KOALA achieves accuracy=precision=recall=F1=1.0 across both model/dataset combinations. This directly confirms that the theorem's sufficient conditions lead to guaranteed detection as claimed.

- **Clean-image-only training is a practical advantage**: The detector requires fine-tuning a pre-trained encoder only on clean images (Section 3.3, Eq. 5-6; Tables 3-4 notes), with no adversarial examples, architectural changes, or adversarial retraining. Despite this lightweight requirement, KOALA achieves meaningful detection (e.g., precision 0.94, recall 0.81 on ResNet/CIFAR-10 full set, Table 2).

- **Complementary metrics validated via careful ablation**: Table 2 systematically compares KL+L0 against L0+Cosine, KL+Cosine, and KL+L0+Cosine. On ResNet/CIFAR-10, KL+L0 consistently outperforms all alternatives across accuracy, precision, recall, and F1, supporting the paper's core motivation (Figure 1, Section 3.1) that KL captures dense low-amplitude shifts while L0 captures sparse high-impact changes.

- **Formal proof of correctness**: Theorem 1 (Section 3.2) provides provable conditions under which detection is guaranteed, which is a genuine rarity in the adversarial detection literature and goes beyond purely empirical approaches.

- **Preserves clean accuracy**: Table 3 shows that KL+L0 fine-tuned ResNet-18 maintains clean accuracy within 0.4% of the baseline (94.78% vs. 95.16%), demonstrating that the detector does not degrade standard classification performance.

## Weaknesses

### Fatal
None.

### Major

1. **Non-standard confusion matrix definitions conflate detection with classification robustness, inflating reported detection metrics.** The paper defines (Section 4.2):
   
   TP := [a=1] ∧ [(â,ŷ)=(1,⟂) ∨ (â,ŷ)=(0,y*)]
   
   This counts an attacked input that the detector fails to flag (â=0) as a true positive, as long as the classifier happens to predict the correct class. Under standard detection evaluation, this would be a false negative (missed detection). The definition means the reported precision (0.94), recall (0.81), and F1 (0.87) on the full ResNet/CIFAR-10 set (Table 2) intermingle the detector's ability to flag attacks with the classifier's robustness. A reader interpreting these numbers as standard detection metrics would overestimate KOALA's detection capability. The paper nowhere justifies or even acknowledges that this definition differs from the conventions used in the detection literature it cites (NIC, LID, MagNet, etc.), making results not directly comparable.

2. **No evaluation against adaptive attacks designed to bypass the detection rule.** The paper uses PGD, CW, and AutoAttack as off-the-shelf attacks (Section 4.1). However, the detection mechanism is transparent: an adversary aware of the detector would optimize a perturbation that forces ŷ_KL = ŷ_L0 = wrong_class (satisfying agreement on an incorrect label), which would evade detection entirely. The paper's Theorem 1 guarantees this is impossible under certain conditions, but those conditions hold for only ~67% of ResNet/CIFAR-10 samples and ~10% of CLIP/Tiny-ImageNet samples (Table 1). On the remaining substantial fraction of non-compliant samples, adaptive attacks could be highly effective. Without evaluating against such attacks, the practical security of the detection mechanism is unquantified.

3. **No quantitative comparison with any prior detection method.** The Related Work section (Section 2) discusses numerous prior detectors (NIC, Feature Squeezing, LID, MagNet, Mahalanobis, CADet, etc.), yet the experiments contain no comparison against any of them. The paper therefore provides no evidence that KOALA improves upon or is competitive with existing approaches, making it difficult to assess the practical contribution. This is particularly problematic because the non-standard evaluation metrics (Weakness #1) preclude meaningful indirect comparison with published numbers from prior work.

4. **Theorem's conditions hold for only ~10% of CLIP/Tiny-ImageNet samples, severely limiting the practical scope of the theoretical guarantee on that setup.** Table 1 shows that on CLIP/Tiny-ImageNet, only 510/5000 (~10%) of samples are Theorem-compliant for ℓ∞^{2/255} PGD, versus 3345/5000 (~67%) for ResNet/CIFAR-10. The paper acknowledges this but the implication is that for the CLIP model — a widely used architecture — the central theoretical guarantee applies to a small minority of cases. The non-compliant majority exhibits substantially weaker detection (e.g., accuracy 0.67, recall 0.84 on CLIP at ℓ∞^{2/255}), raising questions about how broadly the theorem's conditions can be expected to hold in practice.

5. **Table 4 caption contains a factual error that contradicts the reported data.** The caption states "The KL+L0 objective demonstrates superior adversarial accuracy, highlighting the complementary nature of these two metrics." However, the table shows KL+L0 performing substantially worse than individual KL or L0 on CLIP/Tiny-ImageNet across all attack types (e.g., PGD ℓ∞^{2/255}: KL=60.02%, L0=53.31%, KL+L0=26.50%). This appears to be a copy-paste error from Table 3 (where KL+L0 genuinely is best), but it means the paper incorrectly claims superiority for its proposed method on one of its two experimental setups. The paper's own discussion in the CLIP results section acknowledges that "L0-only fine-tuning objective yields the highest adversarial robustness," but the table caption still contradicts this.

### Minor

6. **KL+L0 is not the best detection combination on CLIP/Tiny-ImageNet.** Table 2 shows KL+L0+Cosine achieving the highest detection accuracy (0.75 vs. 0.71), precision (0.68 vs. 0.66), recall (0.94 vs. 0.85), and F1 (0.79 vs. 0.74) compared to the proposed KL+L0. The paper's explanation — that KL+L0+Cosine works by "breaking the underlying classification" — implies that KL+L0 is still preferable for "a more balanced approach to robust classification and detection." However, the detection metrics in Table 2 are the primary measure of detection performance, and on this measure KL+L0 is not the winner on one of the two evaluated setups. This undercuts the generality of the claim that the KL+L0 combination is the optimal choice.

7. **No ablation or sensitivity analysis of the L0 threshold hyperparameter τ (set to 0.75).** The L0 metric (Eq. 2) and the training surrogate both depend on τ, which controls what counts as a "perturbed" dimension. The paper does not study how detection performance varies with τ, nor gives guidance on how to set it for new models/datasets.

8. **Training uses a smooth surrogate for L0 but inference uses the hard L0, with no analysis of the discrepancy.** The surrogate L0 (Section 3.3) uses a sigmoid to make the loss differentiable, but at inference the hard L0 (Eq. 2) is used. The paper does not analyze whether this mismatch causes systematic differences between the training objective and the inference detection behavior.

### Trivial
None.

## Nice-to-Haves

- An analysis of how the threshold parameter τ affects detection performance would strengthen the practical guidance for deploying KOALA on new models.
- The paper could benefit from reporting standard detection metrics (TP = â=1 on attacked inputs) alongside the proposed system-level metrics, enabling direct comparison with the literature.
- Evaluating on additional attack norms (e.g., ℓ₂) would broaden the empirical scope.

## Removed Points

No Harsh Critic weaknesses were provided to filter. The Strength Finder's strengths were all concrete and evidence-based; none were removed as generic or superficial.

## Novel Insights

Beyond the paper's own contributions, the review surfaces a tension inherent in the work: the paper simultaneously presents a formal detection guarantee (Theorem 1) and a practical detection system (KOALA), but the guarantee applies to a limited and dataset-dependent fraction of inputs. This raises a broader question for the field — whether provable detection conditions can be designed to hold more universally, or whether the best one can hope for is a guarantee that applies after a data-dependent filtering stage. The paper's own data (Table 1) illustrates this sharply: the guarantee covers 67% of ResNet/CIFAR-10 cases but only 10% of CLIP/Tiny-ImageNet cases, suggesting that the practical reach of such theoretical conditions may be highly architecture- and data-dependent.

## Suggestions

1. Revise the confusion matrix definitions to separate detection performance (can the detector tell clean from attacked inputs?) from overall system robustness (does the system produce a correct outcome?). Report both sets of metrics, or at minimum justify and clearly label the non-standard definition.
2. Evaluate against adaptive attacks that specifically optimize for ŷ_KL = ŷ_L0 = wrong_class, especially on the non-compliant samples where the theorem does not guarantee detection.
3. Include quantitative comparisons with at least a few representative prior detection methods (e.g., Mahalanobis detector, LID, Feature Squeezing) under a shared evaluation protocol.
4. Correct the Table 4 caption error, and discuss the CLIP results more candidly: the proposed KL+L0 combination does not universally outperform alternatives.
5. Study the sensitivity of detection performance to the L0 threshold τ, and provide guidance for setting it.
6. Analyze whether the smooth-to-hard L0 mismatch during training versus inference materially affects performance.

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>