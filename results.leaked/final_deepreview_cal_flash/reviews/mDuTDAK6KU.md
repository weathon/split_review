Now let me write the final review and present the score.

## Summary

KOALA proposes an adversarial detection approach using the disagreement between two complementary nearest-prototype classifiers: one based on KL divergence (sensitive to dense, low-amplitude perturbations) and one based on an L₀-based metric (sensitive to sparse, high-impact changes). The paper provides a formal theorem proving that under bounded perturbations and sufficient inter-class prototype separation, no adversarial perturbation can simultaneously satisfy both metrics, forcing a disagreement and guaranteeing detection. The method requires only lightweight fine-tuning on clean images. Experiments are conducted on ResNet-18/CIFAR-10 and CLIP/Tiny-ImageNet under PGD, CW, and AutoAttack.

## Strengths

1. **Novel dual-metric detection mechanism.** The idea of detecting attacks via disagreement between KL-divergence and L₀-based nearest-prototype classifiers is conceptually well-motivated (Section 3.1, Figure 1). The two metrics are designed to be complementary for dense/low-amplitude and sparse/high-impact perturbation regimes, which is a clean conceptual contribution.

2. **Formal theorem with explicit, verifiable conditions.** Theorem 1 (Section 3.2) proves that under Assumptions A1–A4, no bounded perturbation can simultaneously flip both the KL and L₀ predictions, forcing disagreement and detection. Experiment 1 (Table 1) directly validates this: on the subset of test samples that satisfy the theorem's conditions, KOALA achieves **perfect detection (Acc=Prec=Rec=F1=1.0)** across both architectures and perturbation budgets. This direct empirical verification of a formal guarantee is a genuine strength.

3. **Lightweight, adversary-free training.** The fine-tuning procedure (Section 3.3) uses only clean images with a composite BCE loss. Tables 3 and 4 explicitly note that all finetuning is done on clean images. No adversarial examples, architectural changes, or expensive retraining are required, making the approach practical as a plug-and-play component.

4. **Comprehensive ablation over metric combinations.** Experiment 2 (Table 2) compares KL+L₀ against L₀+Cosine, KL+Cosine, and all three combined across both architectures. The KL+L₀ combination yields the best detection metrics on ResNet/CIFAR-10, experimentally justifying the core design choice.

5. **Substantial adversarial accuracy gains on ResNet/CIFAR-10.** Table 3 shows that KL+L₀ fine-tuning improves adversarial accuracy substantially over the baseline (e.g., 57.32% vs. 45.5% for PGD ε=2/255, 54.60% vs. 33.11% for ε=4/255) while maintaining clean accuracy near 95%. This demonstrates that the detector's training also strengthens the classifier.

## Weaknesses

### Fatal
None.

### Major

1. **Non-standard evaluation metric conflates detection with classification.** The confusion matrix in Section 4.2 defines:
   - TP := attacked AND [detected OR (not detected but correctly classified)]
   
   This means an undetected attack (â=0) counts as a True Positive whenever the classifier happens to predict the correct class. Under standard detection definitions, a TP requires â=1. The reported precision, recall, and F1 scores in Tables 1 and 2 are therefore inflated relative to standard detection metrics and cannot be compared to prior detection literature. A detector that never flags an attack but sits behind a robust classifier would achieve high scores under this definition. The adversarial accuracy experiments (Tables 3, 4) use standard metrics and are unaffected, but the paper's headline detection claims (abstract: "precision of 0.94 and recall of 0.81") are supported by a non-standard metric. The authors should re-evaluate with AUROC or a standard binary confusion matrix where TP requires â=1.

2. **No comparison against existing detection baselines.** Section 2 surveys a wide range of methods — Mahalanobis (Lee et al., 2018), LID (Ma et al., 2018), NIC (Ma & Liu, 2019), MagNet (Meng & Chen, 2017), CADet (Guille-Escuret et al., 2023), feature squeezing (Xu et al., 2018), and others — yet none are used as experimental baselines. The only comparisons are internal ablations over loss functions for the KOALA head. Without situating KOALA's performance relative to existing methods, it is impossible to assess whether the approach represents a practical advance. At minimum, a Mahalanobis-based detector (natural given the nearest-prototype framing) should be compared.

3. **Limited practical coverage of the theoretical guarantee.** Only ~50% of ResNet/CIFAR-10 samples (3345/5000 and 2967/5000) and ~10% of CLIP/Tiny-ImageNet samples (510/5000 and 556/5000) satisfy Theorem 1's conditions. On the remaining majority (non-compliant subset), detection F1 drops to 0.53–0.57 for ResNet and 0.70–0.72 for CLIP (Table 1). The abstract and introduction frame the "formal proof of correctness" as a general attribute without prominently caveating these coverage limitations, which is misleading. The theory is valid under its stated assumptions but applies to a minority of test cases in practice.

### Minor

4. **Assumption A3 is non-standard and lacks justification.** The coordinate-wise bound |δᵢ| ≤ ³⁄₂|pᵢ*| is not a standard constraint in adversarial robustness (attacks are typically bounded in ℓ₂ or ℓ∞ in pixel space, with no natural per-coordinate relative bound in feature space). The constant ³⁄₂ appears to arise from the proof structure rather than empirical properties of perturbations. The paper calls this "mild and practical" but provides no empirical evidence beyond the theorem-compliant counts.

5. **Method behavior is model- and dataset-dependent.** On ResNet/CIFAR-10, KL+L₀ is clearly best. On CLIP/Tiny-ImageNet, different metric combinations win (L₀+KL+Cosine for detection, L₀-only for adversarial accuracy). The explanations (Section 4.4) are post-hoc speculation about training histories and embedding structures, limiting confidence in the method's generality.

### Trivial
None.

## Nice-to-Haves

- **Standard detection metrics:** Report AUROC or standard binary confusion matrix (TP requires â=1) to make results comparable to prior work.
- **Detection baselines:** Include at least Mahalanobis-based detection and one adversarially-trained detector head.
- **Adaptive attacks:** Design an attack that explicitly targets the KL/L₀ disagreement mechanism to stress-test the theoretical guarantee.
- **Report non-compliant subset behavior in more detail:** Break down by attack type, show standard detection metrics, and analyze why the theorem's conditions fail.

## Removed Points

These points were raised by the original reviewers but are excluded from the main weaknesses for the reasons noted:

- *"The evaluation issue is fatal and invalidates all claims."* — Downgraded from Fatal to Major. The metric issue is real, but the relative ablations remain valid, the theorem-compliant results (perfect detection) are unaffected, and the adversarial accuracy results (Tables 3, 4) use standard metrics. The paper's core contributions are not invalidated, though the detection numbers need re-evaluation.
- *Criticisms about missing appendix/proof.* — The parser strips appendix content; the original submission contains the full proof (referenced as Appendix B). Per hard rules, this is not a valid criticism.
- *"The theory is overstated / framing exaggerates significance."* — The substance (limited practical coverage) is kept as Weakness 3. The tone judgment is softened.
- *Formatting/style nitpicks, reproducibility complaints about trivial hyperparameters, and requests for complete training logs.* — Removed per hard rules (parser artifacts and standard community practices).
- *Strength Finder's generic strengths* (e.g., "this paper addresses an important problem"). — Removed as lacking specific evidence anchoring. Only concrete, evidence-backed strengths are retained.

## Novel Insights

None beyond the paper's own contributions. The core insight — that complementary metrics (KL divergence and L₀) can be paired such that their disagreement serves as an adversarial signal, with a formal guarantee when class prototypes are sufficiently separated — is already the paper's claimed contribution.

## Suggestions

1. **Replace the evaluation metric** in Tables 1 and 2 with standard detection metrics (AUROC, or at minimum a standard binary confusion matrix where TP requires â=1). This is the single most impactful change.
2. **Add at least 2–3 detection baselines** from the methods surveyed in Section 2 (e.g., Mahalanobis distance-based detection, an LID-based detector).
3. **Caveat the theory's practical coverage** prominently in the abstract and introduction (e.g., "our guarantee applies when inter-class prototype separation is sufficiently large, which holds for ~50% of ResNet/CIFAR-10 test samples").
4. **Provide empirical evidence for Assumption A3** by measuring max |δᵢ|/|pᵢ*| for embeddings under standard attacks.
5. **Report standard detection metrics for the non-compliant subset** to better characterize where and why performance degrades.

## Calibration Summary

**Round 1 (Bracketing):** Three queries across score bands:
- Low (<3.5): anchors at 2.00–3.00 — substantially weaker papers; KOALA is stronger.
- Middle (3.5–7.5): anchors at 5.33–6.20 — KEY COMPARISONS. SPADE (5.50, Accept) has theory + weak evaluation. DDAD (6.20, Reject) has baselines but batch limitation. Randomized Feature Squeezing (4.75, Reject) has gradient obfuscation issues.
- High (>7.5): anchors at 8.00 — substantially stronger papers with rigorous evaluation.

**Bracket: 4.5–6.5.**

**Round 2 (Narrowing):** Two queries inside the bracket:
- Topical (detection + prototypes): anchors at 4.60–6.20.
- Lightweight detection: anchors at 4.75–5.75.

**Final position:** KOALA is stronger than the 4.5–4.8 papers (which have fundamental flaws) but notably weaker than DDAD (6.20) which includes baseline comparisons. SPADE (5.50) is the closest comparable — both have theory-plus-evaluation-concern patterns, but SPADE at least compares against MSP, KNN, etc. baselines. KOALA provides zero external baselines. **Score: 5.0.**

**Anchors consulted:**
| Path | Avg Score | Round | Comparison to KOALA |
|------|-----------|-------|---------------------|
| KAWlH5pfQu | 3.00 | R1 | Much weaker — incoherent method |
| kz78RIVL7G | 2.60 | R1 | Much weaker — vague approach |
| lEsNGN1SjG | 2.00 | R1 | Much weaker — flawed theory |
| 85Eej2kUHQ | 2.33 | R1 | Much weaker — limited evaluation |
| RzdtpxL0H5 (DDAD) | 6.20 | R1 | Stronger — has baselines, similar theory quality |
| YmQyEdLIkU | 5.50 | R1 | Similar — kernel theory paper, comparable |
| kwCHcaeHrf (SPADE) | 5.50 | R1 | Similar — theory + weak evaluation, but has baselines |
| IGzaH538fz | 8.00 | R1 | Much stronger — rigorous certification |
| rlsWIBDWhW | 5.50 | R2 | Similar — contrastive robustness |
| 7GCRhebJEr | 5.00 | R2 | Similar — Bregman divergence, mixed reviews |
| J2we1sVd9m | 4.60 | R2 | Slightly weaker — impractical OT requirement |
| sBpYRQOrMn | 5.75 | R2 | Slightly stronger — better evaluation |
| GNOMC90vbl | 4.80 | R2 | Weaker — Lipschitz approach, limited results |
| kfYM5lBzB6 | 4.75 | R2 | Weaker — gradient obfuscation concerns |
| adhxppqQAn | 3.75 | R3 | Weaker — multitask consistency detection |
| R1crLHQ4kf | 5.00 | R3 | Similar — output distribution detection |

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>