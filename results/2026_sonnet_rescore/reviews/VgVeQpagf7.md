## Summary

SPS and SPS+ are differentially private dataset distillation algorithms that adapt the D3S framework to the private setting by replacing the privately-trained model with a public pretrained model, collecting class-conditional and global activation statistics, privatizing them via the Gaussian mechanism, and optimizing a KL-divergence objective to produce a synthetic dataset. SPS+ adds multistage clipping and grouped pseudo-classes to substantially close the performance gap on multiclass tasks under tight privacy budgets. The key practical advantage is that a synthetic dataset can be freely post-processed—enabling model ensembling, federated aggregation, and continual learning without additional privacy cost—capabilities that composition limits render infeasible under standard DP-SGD.

---

## Strengths

- **State-of-the-art DP image classification via ensembling.** Table 1 shows SPS+ WRN34-10 ensemble achieves 96.2% / 76.6% on CIFAR-10/100 at ε=1, surpassing the prior best DP-SGD result (94.8% / 70.3%) by a clear margin, making this the first generation-based approach to reach parity with gradient-based private training.

- **SPS+ technical contributions are demonstrably effective.** The transition from SPS to SPS+ on CIFAR-100 at ε=1 (Table 1: 48.9% → 71.0% for WRN28-10) confirms that grouped pseudo-classes and multistage clipping solve a genuine and previously blocking challenge.

- **Free flexibility advantages are concretely demonstrated.** The paper documents ensembling without extra privacy cost (Table 1), federated learning outperforming FedLAP-DP/FedDM (Fig. 5d-e, reaching 89.5% at ε=1 with 5 parties), and continual learning (Fig. 5c, 68.1% vs 76.9% non-continual at ε=4). These are real practical capabilities absent from DP-SGD.

- **Effective dimensionality reduction.** Section 3.2.2 explains that projecting activations to lower-dimensional statistics reduces the privatized vector dimensionality from ~10⁷ (DP-SGD gradients) to ~10⁵, materially improving SNR under the same privacy budget.

- **Robustness to domain shift.** Table 2 shows SPS achieves 92.6% on CAMELYON17 at ε=8, outperforming DP-Diffusion (91.1% at ε=10) and DP-SGD (90.5% at ε=10) despite a significant mismatch between the ImageNet pretraining distribution and the histopathology domain.

---

## Weaknesses

### Fatal
None.

### Major

- **The "every setting" claim in Section 5.1 is factually wrong for single-model CIFAR-100 at ε≥2.** The paper states: "SPS+ matches or exceeds DP-SGD in every setting." Table 1 directly contradicts this. For SPS+ WRN28-10 vs. DP-SGD WRN28-10 on CIFAR-100: ε=2: 74.3 vs 74.7 (−0.4), ε=4: 76.2 vs 79.2 (−3.0), ε=8: 77.5 vs 81.8 (−4.3). Even SPS+ WRN34-10 trails DP-SGD at ε=4 (77.2 vs 79.2) and ε=8 (78.4 vs 81.8). The single-model advantage on CIFAR-100 exists only at ε=1 and is marginal (+0.7%). This is a directly verifiable factual error in the paper's core empirical claim, not a framing choice. The claim should be scoped to (a) CIFAR-10 single models, and (b) ensembles across all settings.

- **Abstract's headline comparison does not disclose that 96.2%/76.6% are ensemble results while the DP-SGD baseline (94.8%/70.3%) is a single model.** The abstract reads: "SPS+ achieves 96.2/76.6% top-1 accuracy, outperforming state-of-the-art (SOTA) DP-SGD results (94.8/70.3%)." The SPS+ numbers correspond to WRN34-10 ensembles (E=5) per Table 1. The free-ensemble argument is technically sound and presented in the body, but the abstract presents an asymmetric comparison as a straightforward accuracy win without qualification. This overstates the headline result and should be corrected.

### Minor

- **M is not stated in Table 1.** The caption for Table 1 says error bars are for n=5 runs and specifies "ensembles use 5 models," but does not state which M was used for the SPS+ rows. Section 5.1 only says M is varied. Figure 2 demonstrates that M has a large effect (e.g., 5+ percentage points on CIFAR-100 at ε=1). Without knowing the M used in Table 1, the reader cannot reproduce the numbers or understand the per-stage privacy budget allocation. M should be stated in the table caption.

- **Performance plateau of SPS+ on CIFAR-100 with ε is unexplained.** At ε=8, single-model SPS+ WRN28-10 on CIFAR-100 reaches 77.5%, while DP-SGD reaches 81.8%. The gap grows as ε increases (from ~+0.7 at ε=1 to −4.3 at ε=8), but the paper offers no analysis of why the statistics-matching approach converges to a lower ceiling at more favorable budgets. This matters for positioning: if SPS+'s single-model advantage is genuinely concentrated at tight budgets, that scope should be stated and motivated. An analysis here—whether the bottleneck is dimensionality of the projected statistics or the Gaussian assumption—would transform this gap into a genuine contribution.

- **Symbol collision in Theorem 4.1.** The theorem writes ε = Mα/(2δ²), where δ denotes the noise multiplier b₀. Throughout the rest of the paper, δ refers to the standard (ε, δ)-DP failure probability (fixed at 10⁻⁵). Using the same symbol for two distinct quantities in a differential privacy paper is a meaningful source of confusion. One of the two should be renamed (e.g., replace b₀'s δ with b₀ or σ_0 in the theorem statement).

- **No GSAM ablation in the main body.** Section 3.2.5 introduces GSAM as part of the downstream training pipeline. Since GSAM is used during fine-tuning on the synthetic data but is unavailable to standard DP-SGD pipelines (where it would require composition), the reported accuracy comparisons include any GSAM benefit. An ablation reporting SPS+ accuracy with and without GSAM would properly attribute the contribution of the optimizer choice vs. the synthetic data quality.

### Trivial
None.

---

## Nice-to-Haves

- A brief characterization of generation cost in the main text would help readers evaluate the practical compute trade-off. Section 6 acknowledges "the cost of generating these images is relatively heavy" and defers to the appendix; a single sentence (e.g., "generation takes approximately X GPU-hours, vs Y for DP-SGD") in the main text would suffice.
- The distinction between CAMELYON17 using SPS (not SPS+) is stated in Section 5.2 but Table 2 labels the result only as "Ours"; noting "SPS" in the table row would prevent confusion.
- The noise redistribution scaling √S (Section 3.2.4) relies on the definition S = LD_G^layer / (|L_C|D_C^layer), which makes the simplification to √2LD_G^layer a tautology. Clarifying this briefly would prevent readers from thinking it is an assumption.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh critic: "missing soft-label information requires unreasonable assumptions"** — Removed as a strawman. The paper directly and explicitly addresses the missing soft-label problem in Section 3.2.1 by using class-conditional statistics and hard labels, and validates this in ablation (Appendix B.1 cited in text).

- **Harsh critic: "CAMELYON17 SPS vs SPS+ not clearly flagged"** — Removed as inaccurate. Section 5.2 explicitly states: "We use SPS in this setting as in the binary classification case, the pseudo-class method does not apply." The concern is partially valid for Table 2's row label (kept as a trivial nice-to-have above).

- **Harsh critic: "computation cost limitation not addressed"** — Demoted. The limitation is acknowledged in Section 6 with a pointer to the appendix, which is reasonable for a method paper.

- **Strength Finder: "privacy guarantee is clearly stated"** — Removed as generic. The existence of Theorem 4.1 is expected; keeping a strength that amounts to "the theorem is present" is not a meaningful commendation.

- **Strength Finder: "robustness to domain shift demonstrates method is not limited to in-domain scenarios"** — Partially retained; the specific CAMELYON17 result is kept because it has concrete numerical evidence. Removed the generic framing.

---

## Novel Insights

The paper's most genuinely novel observation—buried in the experimental results but not explicitly analyzed—is that SPS+'s single-model accuracy gain over DP-SGD appears to be concentrated in the high-privacy (small ε) regime, while at more permissive budgets DP-SGD's gradient-based training retakes the lead for harder multiclass tasks. This suggests an intrinsic interaction between the dimensionality of the projected activation statistics, the noise level, and the amount of class-discriminative information that can be preserved under privatization. Exploring this interaction—whether the plateau is due to the Gaussian approximation of activation distributions or the effective information ceiling of the chosen D_G/D_C dimensions—would constitute a meaningful theoretical contribution beyond the empirical results already presented.

---

## Suggestions

1. Correct Section 5.1 to scope "SPS+ matches or exceeds DP-SGD in every setting" to either ensembles or to CIFAR-10 single models; qualify single-model CIFAR-100 performance explicitly.
2. Update the abstract to clarify that 96.2%/76.6% is from a 5-model ensemble, and explain why ensemble comparison is nonetheless fair (free post-processing).
3. Add M to Table 1 caption (or footnote).
4. Add a one-sentence GSAM ablation in Section 3.2.5 or Section 5.1.
5. Rename δ in Theorem 4.1 (noise multiplier) to avoid collision with the δ in (ε, δ)-DP.
6. Add brief analysis in Section 5.1 or 6 discussing why single-model SPS+ diverges from DP-SGD performance as ε grows on CIFAR-100.

---

## Score and Decision

**Originality:** The design (replacing privately-trained model with a public pretrained model; privatizing activation statistics; grouped pseudo-classes) is technically novel and well-executed. 4/5.

**Importance:** Closing the long-standing accuracy gap between generation-based and gradient-based private learning in images is a genuinely important milestone; the practical flexibility benefits (federated learning, continual learning, ensembling) add real value. 4/5.

**Claims supported:** The ensemble results are solidly supported; the "every setting" single-model claim is directly contradicted by Table 1 for CIFAR-100 at ε≥2. This is a concrete factual error, though correctable. 3/5.

**Soundness:** The privacy analysis is correct; the method is technically sound; the experimental comparisons are fair. The main methodological gap is the absent GSAM ablation. 4/5.

**Clarity:** Well-written overall; the M-specification gap in Table 1, the symbol collision in Theorem 4.1, and the overstated claim in Section 5.1 are the main clarity failures. 3/5.

**Community value:** High — provides a concrete, reproducible, state-of-the-art alternative to DP-SGD with demonstrated additional capabilities. 4/5.

The paper is a solid contribution with two correctable but meaningful presentation/framing problems (the "every setting" factual error and the abstract's asymmetric comparison). Neither undermines the method itself. Both should be fixed in revision.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>4</soundness>
<clarity>3</clarity>
<community_value>4</community_value>
</subscores>