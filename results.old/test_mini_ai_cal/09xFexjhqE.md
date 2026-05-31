I have all the calibration data I need. Here is the final consolidated review.

---

## Summary

This paper identifies that robust fine-tuning (RFT) methods like vanilla RFT and TWINS suffer from divergent gradient directions between natural and adversarial objectives when both are optimized through the feature extractor (FE). To address this, the paper proposes AutoLoRa, which introduces a low-rank (LoRA) branch to disentangle the two objectives: the natural objective is optimized through the LoRA branch while the adversarial objective is optimized through the FE. The paper additionally proposes heuristic automated schedulers for the learning rate and loss-term scalars (λ₁, λ₂). Experiments on six datasets with ResNet-18, ResNet-50, ViT, and DeiT backbones show consistent improvements in adversarial robustness over vanilla RFT and TWINS, with statistical significance validated via t-tests.

---

## Strengths

1. **Clear identification and quantification of gradient divergence in existing RFT methods (Section 3.2, Figures 1a–1b)**: The paper introduces gradient similarity (GS) as a diagnostic and shows empirically that vanilla RFT and TWINS produce near-zero cosine similarity between natural and adversarial gradients, and that lower GS correlates with lower robust accuracy. This provides a well-motivated diagnostic for the problem being addressed.

2. **Consistent and statistically significant gains across diverse settings (Tables 1–3)**: AutoLoRa outperforms vanilla RFT and TWINS on all six datasets (CIFAR-10/100, DTD-57, DOG-120, CUB-200, Caltech-256) with both ResNet-18 and ResNet-50, and also shows gains with ViT and DeiT backbones. The paper reports t-tests validating significance (Table 7). Representative gains include +2.03% PGD-10 on CIFAR-100 (ResNet-18) and +3.03% on DOG-120 (ResNet-50).

3. **Parameter-efficient design with no inference overhead (Section 4.1, Table 4)**: The LoRA branch adds <5% extra parameters (at rank ≤8) and is removed during inference, so there is no inference latency penalty. This makes the method practical for deployment.

4. **Multiple informative ablations (Tables 4, 8, 9, 10)**: The paper systematically ablates rank (showing higher rank yields better robustness, consistent with the distillation hypothesis), pre-training budget (showing robustness gains hold across different ε_pt values), LR scheduler (showing automated LR matches tuned TWINS), and sharpening parameter α.

5. **Robustness across backbones and pre-training budgets (Tables 3, 8)**: AutoLoRa works with CNNs and vision transformers, and maintains its advantage across FEs pre-trained with varying adversarial budgets (ε_pt from 0 to 8/255).

---

## Weaknesses

### Fatal
None.

### Major

1. **The effect of disentanglement is not isolated from the effect of added capacity (missing ablation)**: The proposed method differs from vanilla RFT in at least three ways: (a) a LoRA branch adds extra capacity, (b) the natural CE loss does not update the FE (disentanglement), (c) a KL distillation loss transfers knowledge from LoRA to FE, and (d) hyperparameters are automatically scheduled. To attribute gains to disentanglement specifically, the paper needs a controlled ablation where the LoRA branch is present but the natural CE loss *also* updates the FE (i.e., removing the disentanglement while keeping the extra capacity and KL loss). Without this, it is unclear whether the improvement stems from disentangling gradient paths or simply from the added representational capacity of the LoRA branch. The rank ablation (Table 4) provides partial evidence (higher rank → better results, consistent with the distillation hypothesis), but does not directly address whether disentanglement itself is the mechanism. **Why this matters**: The paper's core conceptual claim is that disentangling gradients improves robustness. This claim requires that disentanglement, not capacity, drives the observed gains.

### Minor

2. **The automated scalar schedule (λ₁, λ₂) is not directly validated**: The paper proposes heuristic schedules for λ₁ and λ₂ based on graduated optimization (Eqs. 7–9), but provides no ablation comparing AutoLoRa with automated scalars against AutoLoRa with fixed, tuned scalars. The only scheduler ablation (Table 9) validates the automated *LR* scheduler on TWINS, not the λ₁/λ₂ scheduler on AutoLoRa itself. While the full method works well, the contribution of this specific component remains unsubstantiated.

3. **Standard deviations are absent from main result tables (Tables 1–2)**: While the paper reports p-values from t-tests (Table 7), this only communicates statistical significance, not effect size or variance. Reporting standard deviations (or confidence intervals) alongside mean accuracy would allow readers to assess result stability directly.

4. **Only two baselines are compared**: The paper compares only to vanilla RFT and TWINS. While TWINS is the most directly relevant SOTA method, claiming "state-of-the-art" based on two baselines is an overstatement. The claim should be bounded (e.g., "best among methods in the RFT-without-extra-data family") to avoid overclaiming.

### Trivial

5. **"FE parameters are updated only by the adversarial objective" is imprecise (Section 4.1, Eq. 5)**: The KL loss in the adversarial objective involves natural soft labels from the LoRA branch; its gradient w.r.t. θ₁ is nonzero, so the FE is indirectly influenced by natural data through distillation. The paper acknowledges this as "knowledge distillation," but the phrasing "only by the adversarial objective" is technically correct (the KL is part of the adversarial objective) yet could mislead readers about the degree of separation.

6. **The LR scheduler description is vague (Section 4.2)**: The paper states it "employ[s] the automatic step size scheduler in AutoAttack," but does not specify which scheduler variant or how it is adapted for learning rate scheduling. The exact schedule should be described in the main text or appendix.

---

## Nice-to-Haves

- **Controlled disentanglement ablation** as described in Major weakness 1.
- **Validate the automated λ₁/λ₂ scheduler** by comparing AutoLoRa with automated scalars vs. AutoLoRa with grid-searched fixed scalars.
- **Report standard deviations** in Tables 1 and 2.
- **Compute and report GS for AutoLoRa** to directly show that gradient conflict is reduced.
- **Broaden the baseline set** to include at least one more recent RFT variant if available.

---

## Removed Points

These points were raised by reviewers but are removed per the filtering rules; treat them with caution:

- *"The causal link between gradient divergence and poor robustness is not established"* — The paper uses correlational language ("indicates," "could prevent") and presents it as motivation, not proof. Most method-motivation papers in ML use correlational evidence to motivate a design. Requiring causal proof (e.g., artificially increasing GS) is an unrealistically high bar for a method-motivation section. The paper does not claim to have proven a causal mechanism — it claims GS is correlated with poor robustness, which the figures support.
- *"The KL loss creates gradient conflict with the adversarial CE loss"* — This is speculative. The paper's design means the natural CE loss's gradient never reaches the FE (it only flows through BA). The KL loss is part of the adversarial objective and involves adversarial data. While the KL loss does create an indirect natural-data influence (via the soft labels), this is fundamentally different from the vanilla RFT case where the natural CE and adversarial KL gradients directly compete on the FE. The paper acknowledges this as distillation.
- *"The α ablation is a simple parameter sweep"* — That is the purpose of an ablation: to test sensitivity to a hyperparameter. Calling it a weakness misconstrues the purpose of the experiment.
- *"SOTA claim is overblown"* — Already captured as a Minor weakness (point 4 above) with a recommendation to bound the claim. The harsh critic's framing as a "critical weakness" is disproportionate.
- *"Figure 2a is not in the main text"* — Parser artifact; figure exists in original submission. Additionally, the main paper already shows Figure 1a (DTD-57) and references Figure 2a for extensive datasets.
- *"Missing related works"* — Per instructions, I cannot verify the existence of unmentioned works.
- *"Selection of best checkpoint based on validation PGD-10 could introduce optimism"* — This is standard practice in adversarial robustness evaluation. The paper mitigates this with 3 repeated experiments and t-tests.
- *"Testing set size of Caltech-256 is unclear"* — The paper states the split (38,550 train, 3,549 test) clearly in Section 5.

---

## Novel Insights

The reviews surface an observation not fully articulated in the paper: the paper's disentanglement architecture (natural→LoRA, adversarial→FE) does not prevent *all* forms of gradient conflict — it only prevents the natural CE gradient from directly competing with the adversarial CE gradient on the FE. The KL distillation term creates a secondary gradient path on θ₁ that depends on the LoRA branch's natural soft labels. This means the "disentanglement" is partial: the FE is protected from the natural CE signal but still indirectly shaped by natural data through distillation. Whether this partial disentanglement is sufficient, or whether a more complete separation (e.g., training FE on adversarial data only, with no KL term) would work even better, is an open question the paper does not address. The paper's rank ablation (Table 4) partially speaks to this — higher rank yields better results, consistent with better soft labels reducing the conflict from the distillation path.

---

## Suggestions

1. **Add the disentanglement isolation ablation** (Major weakness 1): compare AutoLoRa against a variant where LoRA is present but the natural CE loss also updates the FE. This is the single most important addition to substantiate the paper's core claim.

2. **Validate the λ₁/λ₂ automated scheduler**: compare AutoLoRa with automated scalars against AutoLoRa with the best fixed scalars found via grid search.

3. **Add standard deviations to Tables 1 and 2** to complement the t-test p-values already in the appendix.

4. **Compute and report GS for AutoLoRa**, or explain why it is not applicable (e.g., because the natural gradient does not flow to the FE). Showing that AutoLoRa resolves the gradient conflict would directly support the motivation.

5. **Bounded SOTA claim**: replace "state-of-the-art" with a more precise description, e.g., "best among RFT methods that do not require additional data or architectural modifications."

---

## Score and Decision

**Round 1 (Bracketing, 3 queries)**: Weak anchors scored ~3.0 (papers with fundamental flaws — clearly below AutoLoRa). Strong anchors scored ~8.0 (near-flawless execution and SOTA results — clearly above AutoLoRa). Initial bracket: 3.5–7.5.

**Round 2 (Narrowing, 2 queries + full reads)**: Read 5 anchors inside the bracket. CURE (5.50, Accept) — adversarial training paper with similar missing-ablation gap but less comprehensive evaluation than AutoLoRa. LoRA-FA (5.33, Reject) — LoRA efficiency paper with fewer experiments. FDT (5.75, Accept) — ensemble adversarial training with a fundamental ε issue; AutoLoRa compares favorably. TATR (5.75, Reject) — clean model-merging theory with modest gains. Fast-LS-l0 (6.00, Reject) — thorough ablation study with minimal weaknesses; AutoLoRa's missing ablation is a more significant gap.

**Final judgment**: AutoLoRa is comparable to FDT (5.75) and TATR (5.75), above CURE (5.50), and below Fast-LS-l0 (6.00). The paper has a real and addressable gap (the disentanglement isolation ablation) but otherwise presents comprehensive experiments with consistent, statistically significant gains. The contribution is solid and the method is practical.

**All anchors retrieved**:

| Paper | Path | Round | Avg Score | Comparison |
|-------|------|-------|-----------|------------|
| Duet (certified robustness) | EIfcSw6MW0.md | R1 Low | 3.00 | Below — fundamental method issues |
| Effective Dimensionality | dIK7GpOwNY.md | R1 Low | 3.00 | Below — correlational study with weaker experiments |
| DABF backdoors | S5JCqTJyKj.md | R1 Low | 3.00 | Below — different subfield, weaker claims |
| Counterfactual adversarial ex. | gaa7gWPZBz.md | R1 Low | 3.00 | Below — limited to MNIST |
| LoRA-FA | RbKThNNFxr.md | R1 Mid | 5.33 | Below — fewer experiments, missing variance |
| CALoR | ysZvK6b60c.md | R1 Mid | 4.50 | Below — different task, less comprehensive |
| Fast-LS-l0 | NlEt8LYAxC.md | R1 Mid | 6.00 | Above — more thorough ablations |
| ROAD | 43flsheS4s.md | R1 Mid | 4.75 | Below — limited to CIFAR, no variance |
| Booster (alignment) | tTPHgb0EtV.md | R1 High | 8.00 | Above — near-flawless execution |
| RDC (diffusion classifier) | I5lcjmFmlc.md | R1 High | 8.00 | Above — SOTA with thorough evaluation |
| Context-parametric inversion | SPS6HzVzyt.md | R1 High | 8.00 | Above — clean controlled experiments |
| DUCI (data provenance) | EUSkm2sVJ6.md | R1 High | 7.60 | Above — well-executed with strong results |
| CURE (adversarial training) | 6IjN7oxjXt.md | R2 Low | 5.50 | Below — missing ablation, undefined metric |
| Reverse alignment | NIouO0C0ex.md | R2 Low | 5.67 | Comparable — different subfield |
| FDT (ensemble AT) | KW8yzAOIZr.md | R2 Low | 5.75 | Comparable — different weaknesses |
| TATR (model merging) | q3ztjJRQuJ.md | R2 High | 5.75 | Comparable — similar overall quality |

MY FINAL SCORE: <score>5.75</score>
MY FINAL DECISION: <decision>Accept</decision>