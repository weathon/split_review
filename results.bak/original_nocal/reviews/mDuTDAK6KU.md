Now I have a thorough understanding of the paper. Let me produce the consolidated review.

---

## Summary

KOALA proposes an adversarial detector that flags an input as attacked when class predictions from two complementary metrics—KL divergence and a custom L₀-based similarity—disagree. The paper provides a theoretical guarantee (Theorem 1) stating that under bounded perturbations and sufficient inter-class prototype separation, no single perturbation can simultaneously flip both metric predictions, forcing disagreement and enabling detection. The method requires only lightweight fine-tuning on clean images and is evaluated on ResNet-18/CIFAR-10 and CLIP ViT-B/32/Tiny-ImageNet.

## Strengths

1. **Novel and well-motivated detection principle.** The idea of using two complementary metrics (KL for dense/low-amplitude shifts, L₀ for sparse/high-impact changes) that naturally fail in mutually exclusive ways under attack is intuitively appealing and genuinely under-explored in prior work. The paper provides clear motivation (Figure 1) for why these two metrics together cover a broader range of perturbation types than any single metric.

2. **Formal theoretical guarantee.** Theorem 1 provides a proof of correctness: under specified assumptions (normalized features, bounded perturbation, coordinate-wise bound, clean-example alignment), a sufficiently large coordinate gap between class prototypes guarantees that KL and L₀ predictions will disagree on attacked inputs. Although the conditions are restrictive (see weaknesses), having any formal detection guarantee is rare among reactive detectors, which are typically purely empirical.

3. **Lightweight, practical training.** The detector requires only fine-tuning the backbone encoder on clean images with a composite KL+L₀ loss (Section 3.3). No adversarial examples, architectural changes, or auxiliary detector heads are needed. This is demonstrated across two different architectures (ResNet-18, CLIP ViT-B/32) and is a genuine practical advantage over methods requiring adversarial retraining.

4. **Empirical validation of the theorem's sufficiency.** Experiment 1 (Table 1) shows that on the subset of test samples satisfying Theorem 1's conditions, detection is perfect (Accuracy=1.0, Precision=1.0, Recall=1.0, F1=1.0) across both architectures and two perturbation budgets. This is a non-trivial empirical check—it confirms that the conditions stated in the theorem are indeed sufficient for the claimed behavior.

5. **Ablation study supports metric complementarity.** Experiment 2 (Table 2) systematically compares KL+L₀ against alternative pairings (L₀+Cosine, KL+Cosine, KL+L₀+Cosine). On ResNet/CIFAR-10, KL+L₀ consistently outperforms all alternatives across Accuracy, Precision, Recall, and F1, providing direct evidence that the two chosen metrics capture distinct perturbation patterns. Experiment 3 (Tables 3-4) further shows that KL+L₀ fine-tuning yields substantially higher adversarial accuracy on ResNet (e.g., 57.32% vs. 45.5% baseline under PGD ℓ∞²/²⁵⁵) than any single-metric fine-tuning.

## Weaknesses

### Fatal
None.

### Major

1. **Non-standard evaluation metrics conflate detection with classification, impeding comparison with prior work.** The detection confusion matrix (Section 4.2) defines TP to include attacked samples that are *neither flagged (â=0) nor misclassified* — i.e., an attack that completely bypasses the detector is still counted as a "true positive" if the classifier happens to predict the correct label. Specifically, TP = [a=1] ∧ [(â,ŷ)=(1,⊥) ∨ (â,ŷ)=(0,y*)]. This means a detector that never flags anything (â=0 always) could still achieve arbitrarily high recall on attacked samples purely through classification accuracy. Standard detection benchmarks (AUROC, TPR at fixed FPR, or even a simple â-vs-a confusion matrix without classification outcome) are absent. While the metrics are internally consistent and capture a system-level notion of "attack containment," they differ from what the community expects from detection evaluation. The paper provides no conversion or auxiliary reporting of standard metrics, making it impossible to compare KOALA to any existing detector or assess whether the reported precision/recall values (e.g., 0.94/0.81 on ResNet/CIFAR-10) represent a meaningful advance.

2. **No comparison to any existing adversarial detection baseline.** The experiments compare only KOALA variants with different metric combinations. There are no baselines: no NIC, LID, Mahalanobis-based detection, feature squeezing, MagNet, CADet, or any other standard method from Sections 1-2 of the paper itself. The paper claims "effective adversarial detection" as a contribution, but without any comparative evaluation against prior methods on the same datasets and attacks, this claim is unsubstantiated. The relative performance of KOALA to existing approaches is entirely unknown.

3. **Theorem conditions apply to a small fraction of test data in the CLIP setting, and the practical relevance of the guarantee is unclear.** For CLIP/Tiny-ImageNet, only ~10% of samples (510/5000 for ℓ∞²/²⁵⁵) satisfy the theorem conditions (Table 1). On the remaining ~90% of "non-compliant" samples, detection performance drops substantially (e.g., recall 0.42–0.45 for ResNet/CIFAR-10 non-compliant; precision 0.62–0.63 for CLIP/Tiny-ImageNet non-compliant). The paper acknowledges this disparity ("the massive scale of CLIP's pre-training data... can lead to a more compact, less-separable embedding space") but does not attempt to characterize or improve the frequency of compliance. The guarantee is therefore practically meaningful only when the embedding space happens to satisfy the conditions — which is not guaranteed and, on CLIP, is rare.

4. **Theorem compliance criterion is not operationalized.** The paper partitions samples into "Theorem-Compliant" and "Non-Compliant" based on "sufficient inter-class prototype separation" but never specifies the exact algorithm or threshold used. Theorem 1 mentions a threshold Γᵢ(ε) without defining its form or showing how it is computed from data. Without this information, the experiment in Table 1 cannot be reproduced, and it is unclear whether the compliance determination uses a principled or ad-hoc criterion. The full proof in Appendix B (stripped by parser) may contain these details, but the main text should specify the operational test.

### Minor

1. **L₀ threshold τ=0.75 and training loss weights (ω_L₀=0.9, ω_KL=0.1) lack sensitivity analysis.** The paper states τ=0.75 without justification or ablation, and the loss weights are justified only with "as L̂₀ is harder to optimize." No experimental evidence is provided that detection performance is robust to these choices. Given that the proof sketch simultaneously discusses an adjustable τ (Proposition 4: "we can always find a threshold τ") while using a fixed τ=0.75 in practice, the relationship between the theoretical τ and the experimental τ merits clarification.

2. **Assumption A3 (|δᵢ| ≤ 3/2|pᵢ*|) is stated without justification for the specific constant.** The paper calls this "mild and practical" but provides no rationale for why 3/2 specifically (as opposed to, say, 2 or any other constant). The proof in Appendix B presumably derives this bound, but for readers of the main text, the choice appears arbitrary.

3. **The dismissive treatment of the KL+L₀+Cosine result on CLIP (Table 2) is unconvincing.** The paper notes that KL+L₀+Cosine achieves the best detection metrics on CLIP but dismisses this as an "artifact" where the model "breaks the underlying classification" (low adversarial accuracy in Table 6). This is a plausible explanation but lacks evidential support. Since detection (not classification robustness) is the paper's primary claim, a combination that achieves the best detection might be preferable, and the dismissal appears post hoc. The paper should either provide evidence for the "broken classification" claim or engage more seriously with this result.

### Trivial
None.

## Nice-to-Haves
- Report standard detection metrics (AUROC, TPR at 1%/5% FPR) alongside the paper's existing metrics to enable comparison with prior work.
- Compare against at least one baseline detection method (e.g., Mahalanobis or LID) on the same datasets and attacks.
- Conduct a sensitivity analysis for τ (e.g., τ ∈ {0.5, 0.6, 0.7, 0.8, 0.9}) to demonstrate robustness of the method.
- Visualize the embedding space (e.g., t-SNE) to illustrate the claimed mutual exclusivity of stability bands.

## Removed Points
These points were flagged by reviewers but are removed per the filtering rules. Treat them with caution.

- **Claim that Experiment 1 is "circular" / "tautological."** The experiment tests whether samples satisfying Theorem 1's conditions (independently defined by inter-class prototype separation) achieve perfect detection. This is a standard empirical validation of a sufficiency claim, not a circular argument. The conditions are defined by feature-space geometry, not by the detection outcome. The removed criticism also ignores that the paper reports performance on the non-compliant subset and uses it as a comparison baseline — clear evidence the experiment was designed as a meaningful test, not a tautology.

- **Claim that non-standard metrics "invalidate" Tables 1 and 2.** The metrics are non-standard but internally consistent and clearly defined. For Table 1 on the compliant subset, the theorem guarantees â=1 (detection) on attacked samples, so the TP definition's classification component is irrelevant — the perfect scores are valid. For Table 2, the relative ordering between KOALA variants under identical metrics remains informative even if absolute values differ from standard metrics. The criticism overstates the damage.

- **Criticism about the proof being unavailable (appendix not provided).** The appendix was stripped by the PDF parser; it exists in the original submission. Per policy, missing appendix content is not a valid weakness.

- **Criticism that the paper lacks confidence intervals / single-run evaluation.** Single-run evaluation is standard for large-scale adversarial robustness benchmarks, and demanding otherwise would impose non-standard practice.

- **Criticism about missing coverage of all possible attack types.** The paper evaluates PGD, CW, and AutoAttack across two budgets, which is a standard evaluation suite.

## Novel Insights
The two reviews primarily surface tensions already present in the paper: the theoretical guarantee is mathematically sound but practically limited by the restrictive conditions (especially for CLIP embeddings), and the evaluation metrics are unconventional. An interesting pattern that emerges is that KOALA's fundamental strength—grounding detection in a formal understanding of how different metrics fail under attack—is also its main liability: the guarantee applies only when the feature space has sufficient structure, and the paper's experiments are designed to showcase what happens when that structure is present (perfect detection) vs. absent (degraded performance). This two-sided presentation is actually more honest than many detection papers that claim universal effectiveness, but it leaves the reader asking: "how can we engineer the embedding space to satisfy the theorem conditions more frequently?" That question is not addressed.

## Suggestions

1. **Report standard detection metrics (AUROC, TPR@FPR) alongside the current metrics.** This would be the single highest-impact improvement. It costs nothing extra (the same raw predictions produce all metrics) and would allow readers to compare KOALA to prior work. It would also clarify which of the reported precision/recall values reflect genuine detection ability versus coincidental classification accuracy.

2. **Add at least one existing detection baseline.** Even a single comparison (e.g., Mahalanobis-based detection from Lee et al. 2018, or LID from Ma et al. 2018) on the same datasets and attacks would contextualize KOALA's performance. Without any baseline, the paper's evaluation cannot answer "is this better than what exists?"

3. **Operationalize the compliance criterion.** Provide the exact algorithmic test (or the formula for Γᵢ(ε)) used to partition samples into Theorem-Compliant and Non-Compliant. This is essential for reproducibility and for assessing how frequently the theorem's conditions hold in practice.

4. **Analyze how to increase the compliance rate.** Given that only ~10% of CLIP/Tiny-ImageNet samples satisfy Theorem 1, the practical value of the guarantee is limited. A natural extension would be to investigate whether stronger fine-tuning or architectural modifications can increase inter-class prototype separation. This would directly strengthen the paper's core contribution.

5. **Ablate the L₀ threshold τ and the loss weights ω_L₀/ω_KL.** Show that detection performance is not overly sensitive to these choices, or characterize the trade-offs involved.

## Score and Decision

The paper presents a genuinely novel detection principle with a formal guarantee—a rare combination. The experimental evaluation, however, has two major gaps: (1) non-standard metrics that conflate detection with classification, making comparison with prior work impossible, and (2) a complete absence of baseline comparisons. These gaps are addressable (they require re-running analysis on existing data, not new data collection), and the core idea remains interesting. The theoretical guarantee is also restricted by conditions that fail for most CLIP samples, but the paper is transparent about this. In its current form, the evidence is insufficient to demonstrate that KOALA advances the state of the art in adversarial detection. The paper should not be accepted without addressing the evaluation gaps.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>