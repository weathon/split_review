## Summary

KOALA (KL-L0 Adversarial detection via Label Agreement) is a plug-in adversarial detector that replaces the classifier head with a nearest-prototype classifier using two complementary distance metrics—KL divergence (sensitive to dense, low-amplitude perturbations) and an L0-based score (sensitive to sparse, high-impact perturbations). An input is flagged as adversarial when the two metrics disagree on the predicted class. The paper provides a formal proof of correctness (Theorem 1) under explicit conditions, and requires only lightweight fine-tuning on clean images. Experiments are conducted on ResNet/CIFAR-10 and CLIP/Tiny-ImageNet.

---

## Strengths

- **Principled theoretical framing.** The observation that energy-bounded perturbations exhibit either dense-low-amplitude or sparse-high-impact structure, and that these are separable by complementary metrics, is a clean and intuitive insight. Theorem 1 formalises when detection is guaranteed, and the proof sketch maps clearly onto three propositions with explicit, checkable conditions—not vague asymptotic claims.

- **Theorem validation experiment.** Partitioning the test set into theorem-compliant and non-compliant subsets (Table 1) is a principled design choice. The compliant subsets consistently achieve precision=recall=1.0 across all attack budgets and both models, directly corroborating the theory.

- **Lightweight and modality-agnostic.** No adversarial examples are required for training, no architecture change is needed, and the method is applied to both a convolutional network (ResNet-18) and a large vision-language model (CLIP). This breadth supports the plug-and-play claim.

- **Clean ablation study.** Experiment 2 compares metric combinations (KL-only, L0-only, KL+L0, KL+L0+Cosine) and confirms that the complementary pairing KL+L0 accounts for the performance, not either metric alone.

---

## Weaknesses

### Fatal
None.

### Major

1. **No comparison with baseline adversarial detectors.** The related work names a substantial number of prior detectors—Feature Squeezing (Xu et al., 2018), LID (Ma et al., 2018), MagNet (Meng & Chen, 2017), Mahalanobis (Lee et al., 2018), CADet (Guille-Escuret et al., 2023), NIC (Ma & Liu, 2019), and others. None of these baselines appear in Tables 2–4. Without a direct numerical comparison, there is no evidence that KOALA offers competitive or superior detection performance relative to existing work. This is a critical gap for any detection paper.

2. **No adaptive attack evaluation.** For a detection mechanism with an explicit, published decision rule (disagree between KL and L0 predictions), an adaptive adversary with white-box access to the detector can craft perturbations specifically designed to keep predictions in agreement under both metrics—without triggering detection. The paper does not evaluate any such adaptive attack. Given that the theorem's conditions are explicit (coordinate gap Γ_i(ε)), an adversary can directly target them. This omission substantially weakens the security claim.

3. **Very low theorem-compliant coverage for CLIP/Tiny-ImageNet.** On CLIP/Tiny-ImageNet, only ~510 out of 5000 samples (~10%) satisfy the theorem's conditions. This means the formal guarantees apply to a small minority of inputs in practice. The practical relevance of Theorem 1 depends heavily on the proportion of compliant inputs; 10% coverage is a significant limitation and should be analysed and discussed.

4. **Low precision on CLIP/Tiny-ImageNet (0.66 overall).** A 34% false-positive rate is problematic for security-critical deployment. The paper does not discuss whether this is due to the CLIP embedding structure, the prototype alignment training, or an inherent limitation of the KL+L0 pairing for larger-class problems. The cause and any mitigation are not addressed.

### Minor

1. **Threshold τ selection not principled.** The proof of Theorem 1 relies on the existence of an appropriate τ for the L0 metric, but the proof shows existence rather than providing a construction. In practice, τ=0.75 is set as a hyperparameter. The paper does not discuss how sensitive performance is to τ, nor how it should be chosen for a new dataset.

2. **Pair construction P in the training objective is not specified.** The KL and L0 losses are defined over pairs (i,j) ∈ P, but P—whether it is all class combinations, random negatives, or something else—is not defined in the main text, hampering reproducibility.

3. **Adversarial accuracy on CLIP/Tiny-ImageNet is not reported** in the same structured way as ResNet results (Table 3 vs. Table 4 interpretation). The relationship between adversarial accuracy and detection metrics is left implicit for CLIP.

### Trivial
None warranting mention.

---

## Nice-to-Haves

- A comparison with at least two off-the-shelf detectors (e.g., Feature Squeezing, Mahalanobis) on the same attack suite would substantially strengthen the paper.
- An analysis of the relationship between the magnitude of the coordinate gap Γ_i(ε) and the probability of theorem compliance across datasets would clarify practical scope.

---

## Novel Insights

The central insight—that energy-bounded adversarial perturbations must commit to one of two qualitatively distinct regimes (dense-smooth or sparse-impulsive) and that this regime commit-ment can be exploited by a two-metric disagreement criterion—is a genuine conceptual contribution. The formalisation that these two regimes produce mutually exclusive "stability bands" whose exclusivity can be guaranteed by a coordinate gap condition provides an unusually explicit correctness criterion for a detection method. Most prior detectors rely on empirical separation of clean and adversarial distributional statistics; KOALA instead derives its detection criterion from the geometry of the perturbation space itself. The formal linkage between perturbation geometry and metric disagreement is the most novel element of the work.

---

## Suggestions

- Include at least two baseline detectors in the experimental tables. Even a single row for Feature Squeezing or Mahalanobis on the same datasets and attack budgets would provide essential context.
- Evaluate an adaptive attack (e.g., a PGD variant with an auxiliary loss term that minimises the KL–L0 disagreement) to empirically probe the practical limits of the theoretical guarantee.
- Report and discuss what fraction of real-world samples is theorem-compliant for each setting, and whether the gap Γ_i(ε) has a practical interpretation that can be tuned.
- Provide a sensitivity analysis or ablation on τ, since both performance and theorem applicability depend on it.
- Clarify the construction of pairs P in the training objective.

---

## Score and Decision

The paper presents a genuinely novel theoretical contribution and a clean, well-motivated detection idea. However, the complete absence of comparisons with existing detectors and the lack of any adaptive attack evaluation are serious omissions that prevent confident assessment of practical utility. The narrow theorem-compliant coverage (~10%) on CLIP/Tiny-ImageNet and the 34% false-positive rate further limit the strength of the empirical case. These are not minor polish issues; they are the standard requirements for adversarial detection papers at ICLR.

MY FINAL SCORE: <score>4</score>
MY FINAL DECISION: <decision>Reject</decision>