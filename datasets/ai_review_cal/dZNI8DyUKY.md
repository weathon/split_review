- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 3, 5, 3
Now I have a thorough understanding of the paper and can verify (or refute) each reviewer claim against the actual text. Let me produce the final consolidated review.

## Summary

The paper proposes MAEP (Masked AutoEncoder Purifier), which integrates a masked autoencoder into an adversarial purifier framework for test-time defense. The core claims are: (1) MAEP is the first MAE-based adversarial purifier, (2) it achieves defense transferability across datasets (including low-resolution CIFAR10 to high-resolution ImageNet) without requiring additional training data, and (3) it offers substantial computational advantages over diffusion-based purifiers. Empirically, MAEP trained on CIFAR10 is reported to outperform diffusion-based purifiers trained on ImageNet on the ImageNet test set.

## Strengths

- **Novel integration of MAE into adversarial purification**: The paper correctly identifies that prior work (DRAM, NIM-MAE) uses MAE for detection or adversarial training, not as a standalone purifier. MAEP's design — using the masking mechanism for reconstruction-based purification — is a genuine departure from the diffusion-model paradigm and is clearly distinguished from related approaches in Table 1 and Section 2.

- **Defense transferability is demonstrated across multiple dataset pairs**: Tables 2 (CIFAR100→CIFAR10) and 3 (CIFAR10→CIFAR100) show that MAEP consistently outperforms diffusion-based baselines (DiffPure, ScoreOpt) on cross-dataset transfer under AutoAttack (ε∞=8/255). This is not a single lucky result; the pattern holds across both directions of CIFAR10/CIFAR100 transfer and under the harder ImageNet transfer in Table 8.

- **Clean accuracy is much better preserved than diffusion baselines during transfer**: On the ImageNet transfer (Table 8), MAEP's clean accuracy drops only ~3% from the undefended classifier (80.85% → ~77.85%), whereas DiffPure and ScoreOpt drop ~10%. The paper correctly attributes this to the fact that diffusion models inject noise to remove perturbations, inherently degrading clean images, while MAEP's masking-based reconstruction does not.

- **Computational efficiency is substantially higher**: Tables 9 and 10 report that MAEP inference (0.58s/image) and training (4.3 hours) are orders of magnitude cheaper than diffusion-based alternatives (10.2s inference, 72 hours training). This supports the practical motivation of avoiding expensive diffusion training.

- **LoRA-based finetuning yields measurable gains**: Table 5 shows that LoRA finetuning improves both clean accuracy (73.84% → 83.30%) and robust accuracy (39.00% → 41.54%), validating the train-test discrepancy analysis in Section 4.4.

## Weaknesses

### Fatal
None.

### Major

- **The combined training objective is not fully specified in the main text**. The paper states that the purifier is "pre-trained from scratch with the loss in Eq. (12)" (Section 5.1) and that inference uses "purification loss LMAEP" (Section 5.1), but neither Eq. (12) nor the symbol LMAEP are defined in the main body. The paper defines the MAE reconstruction loss (Eq. 1) and the DISCO purification loss ℓ₁(𝒫(x_a), x) (Eq. 2), and the text says MAEP combines "the purification loss and MLM together" (Section 4.2), but the exact combined loss function — including any weighting coefficients — is absent from the main text. The reader also cannot tell from the main text whether the pre-training uses clean images, adversarial images, or both (the phrase "MAEP has purified the adversarial image (Eq. 12)" in Section 4.4 implies adversarial images are used, but this is never stated directly). This is a core methodological gap that impairs reproducibility and full understanding of the method. While the appendix likely contains the missing details, the main text should be self-contained on the central loss function.

- **The headline transferability claim (Table 8) rests on an uncontrolled comparison**. The caption of Table 8 states that results marked with an asterisk are "excerpted from the papers." The paper claims that MAEP (trained on CIFAR10) outperforms DiffPure and ScoreOpt (trained on ImageNet) on ImageNet — but the baseline numbers are taken from the original papers while MAEP's numbers are from the authors' own runs. This introduces uncontrolled confounds: different classifier checkpoints, different attack implementations, and different evaluation protocols. The paper does note this with asterisks and does state that for CIFAR10/100 (Tables 6, 7) it ran the official DiffPure code under the same setup. But for the ImageNet transfer specifically, the comparison is not apples-to-apples. The central contribution ("outperforming diffusion-based models trained on ImageNet") cannot be considered verified until all methods are evaluated under identical conditions. This is fixable but the paper as written overclaims.

### Minor

- **The derivation in Section 4.2 (purification loss vs. clean accuracy) is heuristic and the supporting experiment (Table 4) does not directly validate MAEP**. The paper itself calls this a "feasible but simple explanation." The derivation assumes the purifier is approximately Lipschitz and that 𝒫(x)-x ≈ 𝒫(x_a)-x_a, which is neither proven nor tested. Table 4 replaces the purifier with a one-step PGD perturbation applied to a *different* classifier (ResNet-18) than the one used in the main experiments (WRN-28-10), and it does not use MAEP at all. At best, Table 4 shows that adding -δ_a preserves reasonable accuracy on a ResNet-18; it says nothing about MAEP's actual behavior. This section does not strengthen the paper and could be removed without loss.

- **No error bars reported**. Though the paper states results are averaged over 5 runs (Section 5.1), no standard deviations or variances are reported for any table. Adversarial robustness results can vary with random seeds; providing variance would significantly strengthen confidence in the claims.

- **Robust accuracy exceeding clean accuracy (Table 7, CIFAR100) is noted but not adequately explained**. For both MAEP and DISCO, robust accuracy is higher than clean accuracy on CIFAR100. This is an unusual phenomenon that the paper dismisses in one sentence ("One possible explanation is that they primarily learn the mapping from the adversarial image to the clean image"). A more thorough analysis or ablation is warranted before advancing this explanation.

- **No evaluation against adaptive attacks**. The paper evaluates AutoAttack on the classifier *after* purification, which is standard, but does not evaluate attacks designed to be aware of the MAEP purification pipeline (e.g., BPDA with a straight-through estimator for the masking operation). This is a standard requirement for purification defenses (the DiffPure paper evaluates this). Its absence is a limitation.

### Trivial
None.

## Nice-to-Haves
- An explicit statement in the main text of whether adversarial examples are used during MAEP pre-training, and if so, which attack and budget.
- Reporting training cost comparisons (MAEP vs. diffusion models) directly rather than citing a separate paper's numbers for diffusion training time.
- An ablation showing the contribution of each loss term (reconstruction vs. purification) to the final performance, rather than deferring to Table 12 in the appendix.

## Removed Points

These points are flagged as removed from the main weaknesses — treat them with caution if referenced:

1. *"The clean accuracy of DiffPure is reported as 68.60%—exactly the same as its robust accuracy at ε∞=4/255. This is physically implausible."* — Removed because the table is an embedded image that cannot be verified from the extracted text. The text around Table 8 only states DiffPure's value (68.60%) in the context of the ε∞=4/255 condition without clarifying whether this is clean or robust accuracy. This specific numerical claim cannot be confirmed from the available evidence.

2. *"Missing appendix content (Eq. 12, Table 12, broken section references)"* — Removed. These are standard parser artifacts; the appendix exists in the original submission. The main text should ideally be self-contained, but referencing the appendix for extended results is standard practice.

3. *"The paper claims MAEP is the 'first study of adversarial purifier based on masked autoencoder' — this is defensible and appropriate"* from the Section-by-Section notes — Removed from strengths because it overlaps with the stated contribution and is generic positioning language rather than a concrete strength with evidence.

4. *"The paper correctly distinguishes MAEP from DRAM and NIM-MAE"* — Removed from strengths. This is adequate related-work coverage, expected in any submission, not a distinctive strength.

5. *"The empirical demonstration that DiffPure's robust accuracy drops from 89% to 69% when transferring CIFAR10→CIFAR100 is convincing"* — Removed from strengths. This is a problem statement, not a contribution of the paper.

## Novel Insights

None beyond the paper's own contributions. Both the harsh critic and strength finder largely recapitulate what the paper itself claims; no genuinely novel synthesis emerges from the reviews that isn't already in the paper.

## Suggestions

1. **Define the complete training loss in the main text.** State explicitly: the full combined loss (including both MAE reconstruction and purification terms with their coefficients), whether pre-training uses clean images only or adversarially perturbed images, and if the latter, which attack and budget.

2. **Re-run all ImageNet baselines (DiffPure, ScoreOpt) under identical conditions** for Table 8, or alternatively downgrade the claim to "competitive" with explicit caveats about comparison fairness.

3. **Add standard deviations** (over at least 3 seeds) to all main tables.

4. **Evaluate against an adaptive attack** designed to break the MAEP pipeline (e.g., BPDA with straight-through estimator for the binary mask operation), or explicitly discuss why this is not applicable.

5. **Either remove Section 4.2 or substantially rewrite it.** The current derivation is unconvincing and the supporting experiment (Table 4) does not involve MAEP. Replace it with an ablation showing that omitting the purification loss harms performance.
