Now I have a thorough understanding of the paper and can write the final synthesized review.

---

## Summary

KOALA (KL-L0 Adversarial detection via Label Agreement) is a reactive adversarial detector that flags adversarial inputs when two nearest-prototype classifiers — one using KL divergence (sensitive to dense, low-amplitude perturbations) and one using a custom L₀-based distance (sensitive to sparse, high-impact perturbations) — disagree on the predicted class. The paper provides a formal theorem guaranteeing detection when inter-class prototype separation is sufficient, and proposes a lightweight clean-image-only fine-tuning procedure for a backbone encoder. Experiments are conducted on ResNet/CIFAR-10 and CLIP/Tiny-ImageNet.

---

## Strengths

1. **Perfect detection on theorem-compliant subsets (Table 1):** On the subset of test inputs that satisfy Theorem 1's conditions, all detection metrics (accuracy, precision, recall, F1) are 1.0 across both architectures and both attack strengths. This directly and cleanly empirically validates the formal guarantee on the data where it applies.

2. **Formal characterization of detection conditions:** Theorem 1, backed by the proof sketch in Section 3.2, derives explicit sufficient conditions (inter-class prototype "coordinate gap") under which KL and L₀ stability bands are mutually exclusive. This is a qualitative step above purely empirical detection methods.

3. **Ablation over metric combinations confirms complementarity on CIFAR-10 (Table 2):** The KL+L₀ combination achieves the highest accuracy (0.88), precision (0.94), recall (0.81), and F1 (0.87) on ResNet/CIFAR-10, outperforming L₀+Cosine, KL+Cosine, and the three-metric combination, supporting the design choice.

4. **Adversarial accuracy improvement via clean-only fine-tuning (Table 3):** KL+L₀ fine-tuning improves adversarial accuracy substantially over the baseline on ResNet/CIFAR-10 (e.g., 57.32% vs. 45.5% under PGD ε=2/255), demonstrating that the training procedure has utility beyond detection.

5. **Honest reporting of CLIP/Tiny-ImageNet limitations:** The paper directly acknowledges in Section 4.3 that KL+L₀+Cosine's high CLIP detection rate results from "breaking the underlying classification" (very low adversarial accuracy in Table 6), not from the intended mechanism, and explains the distinction. This transparency is a strength.

---

## Weaknesses

### Fatal
None. The core idea is not invalidated, but several major empirical gaps prevent judging whether it works competitively.

### Major

1. **No comparison to any established adversarial detector.** The related work cites Feature Squeezing (Xu et al., 2018), LID (Ma et al., 2018), MagNet (Meng & Chen, 2017), Mahalanobis (Lee et al., 2018), NIC (Ma & Liu, 2019), and CADet (Guille-Escuret et al., 2023), yet none appear in the experimental tables. The ablation study (Table 2) compares only KOALA metric variants against each other. Reporting "precision 0.94 / recall 0.81" on ResNet/CIFAR-10 is uninterpretable without context from at least two or three of these baselines. Without this comparison, the central empirical claim — that KOALA "consistently and effectively detects adversarial examples" — is unsubstantiated.

2. **No evaluation against adaptive adversaries.** The paper tests only PGD, CW, and AutoAttack — all of which target the underlying classifier and are unaware of KOALA's detection logic. Since Carlini & Wagner (2017), adaptive adversary evaluation is the standard for detection papers. The obvious adaptive attack (crafting perturbations that minimize the probability of KL–L₀ disagreement while also fooling the classifier) is absent. Theorem 1 provides a theoretical safety argument, but it covers only 10–67% of inputs depending on setting (Table 1); the vast non-compliant fraction has no adaptive adversary analysis.

3. **Non-standard confusion matrix definition conflates detection with classification.** Section 4.2 defines TP as: an adversarial input is a true positive if *either* the detector correctly flags it **or** the model correctly classifies it anyway without flagging. The condition `(â, ŷ) = (0, y*)` (not detected, but correctly classified) contributing to TP means the metric counts successful misclassifications that happen to yield correct output as detection successes. This is non-standard and means the reported precision and recall are not directly comparable to detection metrics in any prior work, compounding the problem caused by the absence of baselines.

4. **KL+L₀ actively underperforms individual metrics on CLIP/Tiny-ImageNet (Table 4), directly contradicting the paper's core thesis.** On CLIP under CW at ε=2/255, L₀-only achieves 37.49% adversarial accuracy while KL+L₀ achieves only 11.91% — a near-fourfold degradation. KL-only achieves 25.69% vs. KL+L₀'s 11.91%. The paper's explanation (Section 4.4) — that CLIP's pretraining concentrates inter-class variation in few directions, making L₀-only especially effective — is entirely post-hoc and not empirically verified. Since the paper's thesis is that KL and L₀ are *complementary* and jointly beneficial, CLIP results showing the combination as actively harmful to adversarial robustness constitute a genuine challenge to the thesis, not a minor curiosity.

5. **Theorem coverage is severely limited on CLIP (Table 1).** On CLIP/Tiny-ImageNet, only 510 of ~5000 test samples (~10%) satisfy Theorem 1's conditions at ε=2/255, and 556 (~11%) at ε=4/255. The abstract states "Our extensive experiments confirm our theoretical claims" and Section 3.2 states "detection is not a probabilistic outcome but a mathematical certainty" — both without qualification. For ~90% of CLIP inputs, KOALA's guarantee is simply absent. The fine-tuning procedure is said to "encourage" the coordinate gap condition (Section 3.2, 3.3) but there is no measurement of whether it actually increases the compliant fraction before vs. after fine-tuning.

### Minor

1. **Assumption A3 is non-standard and unverified.** The coordinate-wise bound |δᵢ| ≤ (3/2)|pᵢ*| (Section 3.2, A3) is not a standard adversarial robustness assumption. In softmax-normalized high-dimensional embeddings where most coordinates are O(1/d), this can become extremely tight. The paper describes A3 as "mild and practical" but does not verify it holds in the experimental setup, and does not acknowledge that an adversary can violate it by concentrating energy on small-valued coordinates.

2. **Hyperparameters τ=0.75 and φ=0.5 are set without justification.** These appear in Section 4.1 without ablation or explanation of how they were selected. Since the test set is split from the development set, it is unclear whether these were tuned on held-out validation or on the reported test numbers.

### Trivial

- The abstract's phrase "formal proof of correctness" without qualification overstates the guarantee given its ~10% coverage on CLIP; a one-sentence qualifier would fix this.

---

## Nice-to-Haves

- **Quantify fine-tuning's effect on compliant fraction.** Reporting the percentage of theorem-compliant samples before and after fine-tuning would directly connect the training procedure to Theorem 1's conditions, which is the key missing link.
- **Characterize when the coordinate gap condition holds.** Is it a function of ε, encoder dimensionality, or dataset difficulty? An analysis of this would substantially deepen the theoretical contribution.
- **Standard AUROC/ROC curve reporting.** Alongside the authors' custom confusion matrix, providing AUROC or detection TPR at fixed FPR would facilitate comparison with the community.

---

## Removed Points

*These points were flagged for removal; treat with caution.*

- **Proof sketch's "dense perturbation path" incompleteness (Harsh Critic, Section 3.2 note):** The full proof is in Appendix B, which is stripped by the parser. Per the hard rules, we do not penalize for absent appendix content.
- **Section 4.3 "not drawing the necessary conclusion" about L₀+KL+Cosine:** The paper *does* draw the conclusion explicitly ("a high detection rate does not always equate to a truly robust model… by breaking the underlying classification") — this criticism is a strawman.
- **Strength: "Clear motivation and architecture exposition" (Strength Finder):** This is generic presentation praise, removed per filtering discipline.

---

## Novel Insights

The disagreement-between-complementary-metrics paradigm is an underexplored angle in adversarial detection. The paper's most concrete novel observation is that the KL and L₀ stability bands around class prototypes are geometrically mutually exclusive under the coordinate gap condition, making detection a consequence of prototype geometry rather than an empirical heuristic. The finding that this structure emerges naturally more on ResNet/CIFAR-10 than on CLIP/Tiny-ImageNet — due to differing pretraining regimes and their effect on embedding geometry — is a secondary but interesting empirical insight, even if currently underexplained.

---

## Suggestions

1. Add at least Feature Squeezing and Mahalanobis as baseline detectors; both operate on embeddings and require no adversarial retraining, making them natural comparisons.
2. Implement one adaptive attack: gradient-based optimization minimizing the margin between KL and L₀ predictions while fooling the base classifier. Even a single result would dramatically change the paper's credibility.
3. Revise the confusion matrix to separate detection success from incidental correct classification. Report standard AUROC alongside the custom metric so the community can situate results.
4. Report theorem-compliant fraction before and after fine-tuning to justify the training procedure's theoretical relevance.
5. Add an ablation over τ ∈ {0.5, 0.75, 1.0} and φ ∈ {0.25, 0.5, 1.0} to establish robustness of the hyperparameter choice.

---

## Score and Decision

**Originality:** The disagreement-based detection with complementary metrics has genuine novelty, and the formal theorem is a real contribution. Score: 3/5.
**Importance of research question:** Adversarial detection without adversarial training is genuinely important. Score: 4/5.
**Claims supported:** The central empirical claim ("consistently and effectively detects") is not supported without baselines; the theorem is only validated on 10–67% of inputs; CLIP results undermine the KL+L₀ thesis. Score: 2/5.
**Soundness of experiments:** The ablation is internally informative but the experimental design is missing critical pieces (baselines, adaptive adversary). The non-standard confusion matrix further compromises soundness. Score: 2/5.
**Clarity of writing:** The paper is clearly written and honest about limitations. Score: 4/5.
**Value to community:** Without baseline comparison or adaptive evaluation, the paper's value to practitioners is limited in current form. Score: 2/5.

The paper presents an interesting idea with genuine theoretical grounding but has critical empirical gaps standard in adversarial detection work: no baseline comparison whatsoever, no adaptive adversary evaluation, non-standard evaluation metrics that prevent direct comparison, and CLIP results that actively undermine the core thesis. These issues are not addressable through clarification — they require new experiments.

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>

<subscores>
<originality>3</originality>
<importance>4</importance>
<claims_supported>2</claims_supported>
<soundness>2</soundness>
<clarity>4</clarity>
<community_value>2</community_value>
</subscores>