Now I have a thorough understanding of the paper, the critic claims, and the strength claims. Let me construct the final review.

## Summary

This paper proposes MAEP, the first adversarial purifier based on a Masked Autoencoder (MAE) architecture rather than the diffusion models dominating prior work. The central claims are: (1) MAEP achieves competitive or state-of-the-art adversarial robustness on CIFAR-10/100, (2) it exhibits superior **defense transferability** across datasets (notably, a purifier trained only on CIFAR-10 transfers to ImageNet with ~74% robust accuracy, outperforming diffusion-based models trained directly on ImageNet), and (3) it offers dramatic computational savings relative to diffusion-based purification (minutes vs. hours of training; milliseconds vs. seconds per image at inference).

## Strengths

- **Defense transferability across datasets is convincingly demonstrated.** Table 8 shows MAEP trained *only* on CIFAR-10 (32×32 images) achieves ~74% robust accuracy on ImageNet under AutoAttack (ε=4/255), outperforming DiffPure (68.60%) and ScoreOpt (68.05%) despite those baselines being trained directly on ImageNet. Tables 2–3 further show MAEP suffers much smaller accuracy drops than diffusion-based methods when transferring between CIFAR-10 and CIFAR-100. This is the paper's most distinctive and novel empirical contribution.

- **Competitive adversarial robustness on CIFAR-10/100 with higher clean accuracy.** Table 6 shows MAEP achieves the highest clean accuracy (93.36%) among compared purifiers on CIFAR-10, with robust accuracy (75.40%) comparable to ScoreOpt-O (74.19%) and well above DiffPure (67.30%). On CIFAR-100 (Table 7), MAEP robust accuracy (80.95%) substantially exceeds DISCO (75.33%) and DiffPure (51.91%). The combination of high clean accuracy and competitive robust accuracy is practically valuable.

- **First masked-autoencoder-based adversarial purifier.** As Table 1 summarizes, MAEP is genuinely distinct from prior uses of ViT/MAE in adversarial settings: Huang et al. studied only classifier robustness, DRAM is a detection+repair approach, and NIM-MAE is adversarial training rather than purification. The paper correctly identifies and fills this gap.

- **Dramatic computational efficiency.** Tables 9–10 report MAEP training time on CIFAR-10 as ~10 minutes (vs. 10+ hours for diffusion models) and inference time as ~0.008 seconds/image (vs. 0.20–6.55s for DiffPure/ScoreOpt). This is a genuine practical advantage that aligns with the motivation in the introduction.

- **Lightweight finetuning strategy is sensible.** The LoRA-based finetuning (Table 5) improves clean accuracy from 89.60%→93.36% and robust accuracy from 55.00%→75.40%, and the rationale (train-test discrepancy from different masking ratios during training vs. inference) is well-motivated.

## Weaknesses

### Major

- **The theoretical justification for clean accuracy preservation (Section 4.2) is unsound and should be de-emphasized or removed.** The derivation claims P(x) − x ≈ P(x_a) − x_a = −δ_a (Eq. 7), where δ_a is the one-step adversarial gradient. There is no justification for the claim that the purifier's residual on adversarial images equals the negative adversarial gradient, nor for the step that the residual on clean images approximates the residual on adversarial images. The subsequent "verification" (Table 4) does not test the actual purifier at all — it measures c(x − δ_a) on a *non-defense classifier* (ResNet-18), which sidesteps the purifier entirely. The paper would be stronger by dropping this derivation and empirically justifying the approach (e.g., "the purification loss alone suffices because...") rather than presenting mathematically shaky reasoning. This does *not* invalidate the empirical results, but presenting an incorrect explanation as a "derivation" weakens the paper's credibility.

- **The adaptive attack threat model is not explicitly specified, particularly for the ImageNet transfer experiments.** The paper never states whether AutoAttack evaluates the *full pipeline* (purifier + classifier) with gradients backpropagated through the purifier, or attacks the classifier alone with the purifier applied as a non-differentiable pre-processing step. For a purification defense, this distinction is critical — non-adaptive evaluation can massively overestimate robustness. For the CIFAR experiments (Tables 6–7), the use of RobustBench classifiers and official baseline code makes the adaptive protocol likely. But for **Table 8 (ImageNet transfer)** — the paper's headline result — the classifier is a standard PyTorch ResNet-50, and the paper provides no details on how AutoAttack is applied. Given that MAEP reports ~74% robust accuracy against a non-robust ResNet-50 on ImageNet (where the classifier alone has near-0% robust accuracy), this omission undermines the paper's strongest claim. The authors must explicitly clarify whether gradients flow through MAEP, and if not, the ImageNet results should be considered preliminary.

### Minor

- **No ablation isolating the contribution of the masking mechanism.** The paper claims the masking mechanism (MAE) is a core contribution, but provides no comparison to a non-masked ViT autoencoder trained with the same purification loss. It is therefore unclear whether the masking mechanism itself provides any benefit beyond the ViT architecture and the purification loss. The loss design comparisons (Table 12) are deferred to the appendix, but the question of "masked vs. unmasked" is a different and more fundamental ablation.

- **Standard deviations / confidence intervals are not reported.** The paper states results were averaged over 5 random seeds, but no table includes any variance information (not even ± notation). Given that some accuracy comparisons are close (e.g., MAEP 75.40% vs. ScoreOpt-O 74.19% on CIFAR-10 robust accuracy), knowing the variability is important for assessing significance.

- **The higher clean accuracy of MAEP vs. diffusion methods is presented as an unqualified advantage, but may partly reflect a different robustness-utility trade-off.** Diffusion-based purifiers apply noise that intentionally degrades inputs to remove perturbations — this can reduce clean accuracy by design. The paper should discuss whether the clean accuracy gap stems from a fundamental architectural advantage of MAE or simply from less aggressive purification.

- **No baseline reporting of the classifier's robustness without any purification.** For context, the paper should report what the WRN-28-10 (RobustBench) classifier's clean and robust accuracies are without MAEP (i.e., the defense-free baseline). This would clarify how much robustness is attributable to the purifier vs. the classifier itself.

### Trivial

- Table 8 caption contains a typo ("sterisk" instead of "asterisk").
- Figure 2 is referenced repeatedly in Section 4.2 but the paper does not include a displayed Figure 2 with labeled axes or quantitative content visible in the parsed text (images are embedded but their content cannot be verified from the text alone).

## Nice-to-Haves

- Qualitative examples (purified clean and adversarial images) would help build intuition for what MAEP actually does to the input.
- Evaluation on ℓ₂ attacks (currently deferred to appendix, Table 18) would be useful in the main text.
- The paper could benefit from applying adaptive attacks via BPDA or a fully differentiable pipeline to confirm the ImageNet transfer results under the correct threat model.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Incomplete and incoherent method description: Eqs. (9), (10), (12) never defined; Section 4.3 essentially empty."** The parser strips appendix sections from all papers. The referenced equations and loss formulations exist in the original submission's appendix. The garbled cross-reference "Please refer to Sec." is a parser artifact, not a missing section. This is not a valid weakness of the submission.

- **"No PGD-20/PGD-100 evaluation; limited to AutoAttack."** AutoAttack is the current standard for robustness evaluation in this community. The paper also mentions PGD-ℓ∞ in Section 5.1 and ℓ₂ results in the appendix. This is a scope/breadth preference, not a weakness.

- **"Limited scope — only ℓ∞ attacks."** The paper mentions ℓ₂ results in the appendix. Evaluating every attack norm is scope creep.

- **"Critical implementation details missing (model size, epochs, LR, batch size)."** The paper states "Details of model structure and parameter settings can be found in Sec." — these are in the appendix, which was stripped. Reproducibility details of this granularity are standard for appendices.

- **"The paper does not explain why diffusion models lose transferability."** The paper's contribution is proposing MAEP, not diagnosing diffusion models. This is scope creep.

- **"No discussion of whether finetuning could be applied to non-masked purifier."** Similarly scope creep — the paper focuses on its proposed method.

- **"DRAM's inferiority is claimed without citations/numbers."** The paper characterizes DRAM qualitatively, which is standard in related-work comparisons.

- **Strength Finder's "theoretical motivation with empirical verification."** This strength is misleading given the weakness of the derivation. The "verification" in Table 4 tests a different quantity (c(x−δ_a) on a non-defense classifier) than what the derivation claims (c(P(x)) properties). Removed as conflicting with a verified weakness.

## Novel Insights

None beyond the paper's own contributions. The reviews identify no unclaimed insight that the paper's results reveal beyond what the authors already state — the key novel finding is that an MAE-based purifier trained on low-resolution data can transfer effectively to high-resolution data, a result the authors prominently claim.

## Suggestions

1. **Explicitly describe the adaptive attack protocol.** State whether AutoAttack on ImageNet (Table 8) evaluates the full MAEP+ResNet-50 pipeline with gradients flowing through the purifier. If it does, this should be confirmed; if it does not, the evaluation should be redone or the claims should be tempered accordingly. This single clarification determines how seriously the paper's central result should be taken.

2. **Remove or significantly rewrite Section 4.2.** The current "derivation" is mathematically unsupported and its verification (Table 4) does not validate the claim. Replace it with an honest empirical observation: "We trained only on adversarial images and observed that clean accuracy remains high. Here is a plausible reason: the adversarial perturbation is small, so the purifier's residual on clean and adversarial images may be similar." Alternatively, drop the theoretical pretense entirely.

3. **Add an ablation comparing masked vs. unmasked ViT autoencoder** with the same purification loss. This directly tests whether the masking mechanism (the claimed novelty) provides any benefit beyond the ViT backbone.

4. **Report standard deviations** for the main accuracy numbers, particularly for comparisons where results are close (e.g., MAEP vs. ScoreOpt-O on CIFAR-10 robust accuracy).

## Score and Decision

The paper makes a genuine contribution: it introduces a new paradigm for adversarial purification based on masked autoencoders, demonstrates impressive defense transferability (particularly from CIFAR-10 to ImageNet), and offers substantial computational advantages over diffusion-based alternatives. The CIFAR-10/100 results are solid and reported with comparisons to standard baselines.

However, two issues prevent full confidence. First, the theoretical derivation in Section 4.2 is unsound and should not have been included in its current form. Second — and more critically — the paper's headline result (defense transferability to ImageNet) lacks explicit specification of whether the evaluation was conducted under a proper adaptive threat model (attack gradients through the full purifier+classifier pipeline). For a purification defense, this is not a minor oversight; it is the single most important experimental detail. Until this is clarified, the strongest claim in the paper rests on an ambiguous experimental foundation.

The paper's contributions are real and the direction is promising, but the current presentation and evaluation gaps prevent acceptance at the claimed level of rigor.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>