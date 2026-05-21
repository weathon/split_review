Now I have all the evidence I need. Let me compose the final consolidated review.

---

## Summary

KOALA proposes a novel adversarial detector that flags inputs as attacked when a KL-divergence-based classifier and an L0-based classifier produce conflicting predictions. The motivation is that KL divergence is sensitive to dense, low-amplitude perturbations while the L0 metric captures sparse, high-impact changes, making them complementary. The paper provides a theoretical guarantee (Theorem 1) that under sufficient inter-class prototype separation, no single perturbation can simultaneously fool both metrics, forcing disagreement and thus detection. KOALA requires only fine-tuning on clean images. Experiments on ResNet/CIFAR-10 and CLIP/Tiny-ImageNet validate the theory on theorem-compliant subsets and compare metric combinations.

## Strengths

- **Genuinely novel detection principle with theoretical grounding**: The idea of using forced disagreement between two complementary similarity metrics (KL and L0) to detect adversarial examples is creative and well-motivated. The observation that energy-bounded perturbations manifest as either dense/low-amplitude or sparse/high-impact shifts (Figure 1) provides clear intuition for the metric choice. Theorem 1 offers a formal condition under which detection is guaranteed — a rarity in the adversarial detection literature.

- **Strong empirical validation of the theory on compliant subsets**: Experiment 1 (Table 1) shows perfect recall and precision (1.0) on Theorem-compliant samples across all tested attacks and both datasets. This cleanly confirms that when the theorem's conditions hold, the disagreement mechanism works exactly as predicted, providing credible evidence for the theoretical framework.

- **Convincing ablation on metric complementarity**: Table 2 demonstrates that KL+L0 outperforms other metric combinations (L0+Cosine, KL+Cosine, KL+L0+Cosine) on ResNet/CIFAR-10 across all detection metrics, supporting the claim that these two metrics are genuinely complementary in practice, not just in theory.

## Weaknesses

### Fatal

None.

### Major

- **Non-standard detection metric definition inflates reported performance**: The paper defines a true positive (Eq. in Section 4.2) as an attacked input where the detector either flags it OR the model correctly classifies it despite not flagging. This means an adversarial example that fails to alter the model's prediction is counted as a "detection success" even though the detector never fired. While capturing a safety-relevant outcome, this metric does not measure the detector's standalone ability to identify adversarial inputs. The headline numbers (e.g., precision 0.94, recall 0.81 on ResNet) therefore cannot be interpreted as standard detection performance and are not comparable with detection metrics in the literature. Standard detection metrics (TPR when the attack succeeds, FPR on clean data) should be reported alongside or instead of this custom metric.

- **No comparison against any existing adversarial detector**: The paper positions KOALA in the reactive detection paradigm and discusses numerous prior detectors (LID, Mahalanobis, feature squeezing, MagNet, NIC, etc.) in the related work (Section 2), yet the experiments compare only variants of KOALA itself (different metric combinations). Without comparison to established detectors under the same attack setup, it is impossible to assess whether KOALA's detection behavior offers practical advantages over existing methods, or whether its theoretical guarantee translates into empirical improvement.

- **Adversarial accuracy comparison in Experiment 3 is confounded by different evaluation populations**: Experiment 3 reports "adversarial accuracy (performance on successfully attacked images that were not detected)." For KOALA models, this is evaluated only on the subset of adversarial examples that evaded detection. For the baseline model (which has no detector), all adversarial examples are evaluated. These are fundamentally different evaluation populations, making the claim that "KL+L0 objective demonstrates superior adversarial accuracy" (Tables 3–4) unsupported by a fair comparison. Additionally, the Table 4 caption is factually misleading for CLIP — KL-only and L0-only objectives outperform KL+L0 on most attacks in that table, contradicting the caption's claim.

### Minor

- **Limited practical coverage of the theoretical guarantee**: On CLIP/Tiny-ImageNet, only ~10% of test examples satisfy Theorem 1's conditions (510–556 out of 5000), and on the non-compliant majority, detection performance drops substantially (precision 0.62–0.63). While the paper acknowledges this split in Experiment 1, it does not discuss the implications for practical deployment, particularly for CLIP-based systems where the guarantee's reach is narrow. The paper would benefit from analyzing whether the compliant fraction can be increased through different training strategies or prototype design.

- **Under-specified normalization pipeline**: Assumption A1 requires feature embeddings to be non-negative and sum to 1 (probability vectors), satisfied "by using a softmax or similar normalization." However, the exact normalization step — where it is applied, whether it operates per-instance, how it interacts with prototype computation — is not specified in the main text. This matters because the KL divergence and L0 metric formulas assume probability-vector inputs, and the theoretical analysis depends on this normalization. Clarifying this step is important for reproducibility and for assessing the theory-practice link.

- **No sensitivity analysis for key hyperparameters**: The L0 threshold τ is set to 0.75 and the loss weights are ω_L0=0.9, ω_KL=0.1 for all experiments. No ablation or sensitivity analysis is provided for these choices, yet the theoretical guarantee depends on τ (through Γ_i(ε)). The paper would be strengthened by showing how detection performance varies with these parameters.

- **Compliance criterion not described in the main text**: How "Theorem-Compliant" vs. "Non-Compliant" samples are identified (the exact gap computation and threshold) is not described, making Experiment 1's partitioning procedure opaque.

### Trivial

- Table 4 caption claims "KL+L0 objective demonstrates superior adversarial accuracy" for CLIP, but the table itself shows KL-only and L0-only objectives outperforming KL+L0 on most attacks. The caption should be corrected or qualified.

## Nice-to-Haves

- Confidence intervals or standard deviations across multiple runs would strengthen the reported metrics.
- A discussion of inference-time computational cost (computing KL and L0 to all prototypes) would help assess the "lightweight" claim.
- Adaptive attack evaluation (where the attacker is aware of KOALA's detection mechanism) would test whether the detector can be circumvented by an informed adversary.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"The fine-tuning step does alter the backbone weights; calling the method plug-and-play overstates its ease of deployment"** — REMOVED. The paper is clear that fine-tuning is required and describes it as "lightweight" using only clean images. In the context of adversarial defenses (which typically require costly adversarial training), this is a reasonable characterization. The claim is not misleading.

- **"The mapping from perturbations in the image domain to bounded L2-norm in the softmax-normalized embedding space is only hand-waved via Lipschitz continuity"** — REMOVED as framed but partially captured in Minor weakness about normalization. The Lipschitz continuity argument (bounded input perturbation → bounded feature perturbation) is a standard and valid reasoning chain, not hand-waving. The remaining concern is about the softmax normalization step, which is now a separate minor point.

- **"The proof sketch mentions a coordinate gap that must exceed a derived threshold Γ_i(ε), but neither the sketch nor the main paper gives any expression for this threshold"** — REMOVED. The paper states the full proof is in Appendix B, which is stripped by the parser. Per review instructions, criticism about missing appendix content cannot be levied.

- **"Standard deviations, confidence intervals, or multiple runs are absent throughout all results"** — MOVED to Nice-to-Haves. Single-run evaluation is the norm for adversarial detection benchmarking at this scale; demanding multi-run statistics would be atypical for this subfield.

- **"Inference cost and training overhead are never discussed"** — MOVED to Nice-to-Haves. While relevant, this is not a core evaluative criterion for a detection methods paper.

- **Strength Finder's 'Plug-and-play design without adversarial retraining'** — RETAINED but qualified. The method does require fine-tuning, which modifies the backbone, so "plug-and-play" is an overstatement. However, the fine-tuning is indeed lightweight (clean images only, no architectural changes), which is a genuine practical advantage over adversarial training approaches.

- **Strength Finder's 'Semantics-free operation'** — RETAINED as a supporting strength. The method operates on embedding geometry without domain-specific priors, which is a valid design property though not a major differentiator.

## Novel Insights

Beyond the paper's own contributions, the reviewers' analysis reveals an interesting tension in detection evaluation: the paper's non-standard metric captures a genuine safety property (did the system ultimately handle the adversarial input correctly?) but at the cost of conflating detector quality with classifier robustness. This highlights a broader gap in the adversarial detection literature — there is no widely accepted evaluation protocol that cleanly separates "did the detector work?" from "was the system safe?" For reactive detection methods that abstain on flagged inputs, both questions matter, and the field would benefit from standardized reporting that addresses both dimensions separately.

## Suggestions

1. Separate detection evaluation from safety evaluation. Report standard detection metrics (TPR on successful attacks, FPR on clean data, AUROC) as the primary detection results, and report the safety-oriented metric (which combines detection with correct classification) as a secondary, clearly distinguished measure.

2. Include head-to-head comparisons against at least 2–3 established detectors (e.g., LID, Mahalanobis-based, feature squeezing) under the same attack setup. This is the single most important addition for establishing practical value.

3. Clarify the adversarial accuracy comparison in Experiment 3: either evaluate all models on the same set of adversarial examples (by forcing the detector to always classify, not abstain), or explicitly note that the comparison is across different evaluation populations and interpret accordingly.

4. Describe the exact normalization procedure (when and how softmax is applied) in the main text.

5. Discuss strategies for increasing the theorem-compliant fraction, particularly for CLIP, and acknowledge this as a limitation when coverage is low.

---

Now, let me provide the final score and decision. Based on my calibration, the paper sits around 4.5. The novel idea and theoretical grounding are genuine contributions, but the evaluation has significant methodological issues (non-standard metrics, no baselines) that prevent acceptance in current form.

**Anchor comparison summary:**
- `KAWlH5pfQu` (3.00, Round 1): Detection paper with wrong proofs, weak baselines — our paper is substantially stronger.
- `4BYzyGKIcb` (4.00, Round 2): OOD detection with limited novelty, questionable setting — our paper has stronger theoretical motivation and clearer problem framing.
- `J2we1sVd9m` (4.60, Round 1): Prototype-based OOD detection, reasonable but incremental — comparable quality but our paper has more significant evaluation issues.
- `7GCRhebJEr` (5.00, Round 2): Bregman divergence for robustness, elegant but limited experiments — our paper is slightly below this due to more fundamental evaluation validity concerns.
- `RzdtpxL0H5` (6.20, Round 1): DDAD with strong baselines and cleaner evaluation — our paper is clearly below this.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>