Now I have a thorough understanding of the paper and all claims. Let me produce the final consolidated review.

## Summary

This paper proposes MAEP (Masked AutoEncoder Purifier), the first integration of a masked autoencoder into an adversarial purification framework. The key claimed contribution is **defense transferability**: MAEP trained on a low-resolution dataset (CIFAR10) achieves strong robustness on a high-resolution dataset (ImageNet) without needing target-domain training data, outperforming diffusion-based defenses (DiffPure, ScoreOpt) that were trained directly on ImageNet. The paper also reports substantially faster inference (0.03s vs. 5.60s per image vs. DiffPure) and training time.

## Strengths

- **Novel integration of MAE as an adversarial purifier.** The paper provides a clear comparison (Table 1) distinguishing MAEP from prior uses of MAE for robustness (DRAM for detection+repair, NIM-MAE for adversarial training, Huang et al. for classifier robustness). This architectural choice — using the ViT-based masking mechanism for purification — is genuinely different from the EDSR-based DISCO and the diffusion-based approaches.

- **Impressive cross-dataset defense transferability demonstrated empirically.** MAEP trained on CIFAR10 achieves ~74% robust accuracy on ImageNet under AutoAttack ε=4/255, outperforming DiffPure (68.60%) and ScoreOpt (68.05%) that were trained directly on ImageNet (Table 8). Additional transfer experiments between CIFAR10 and CIFAR100 (Tables 2, 3) consistently show MAEP outperforming baselines. This result is surprising and, if verified, practically valuable.

- **Significant efficiency gains over diffusion-based defenses.** Inference time is 0.03s per image on CIFAR10 versus DiffPure (5.60s) and ScoreOpt (0.30s) (Table 9). Training time is 8 hours versus 14.5 hours for ScoreOpt (Table 10). These efficiency numbers are concrete and meaningful for deployment.

- **Lightweight finetuning strategy (LoRA) to address train-test discrepancy.** The identification that masking ratio differs between training (r=0.5) and inference (r=0) creates a distribution shift, and the application of LoRA finetuning to mitigate this (Table 5), is a practical contribution that improves both clean and robust accuracy.

## Weaknesses

### Fatal
None.

### Major

- **No evaluation against adaptive attacks.** For any test-time purification method, robustness claims are incomplete without evaluating attacks that are aware of the purification mechanism (e.g., BPDA that differentiates through the purifier, or full white-box attacks on the combined purifier+classifier). The paper mentions BPDA in Related Work (line 133, noting DISCO was tested against it) but never evaluates MAEP against any adaptive attack. AutoAttack alone does not necessarily backpropagate through the MAE reconstruction if gradients are blocked or if the purifier is treated as a non-differentiable pre-processing step — the paper does not clarify this. Without adaptive attack evaluation, the claimed "state-of-the-art" robustness (especially on the source CIFAR-10/CIFAR-100 datasets) is not fully substantiated. This is a standard expectation for purification papers (DiffPure, ScoreOpt, DISCO all provide adaptive evaluations).

### Minor

- **Theoretical justification for clean accuracy is weakly supported.** Section 4.2 attempts to justify why training only with the ℓ₁ purification loss (on adversarial images) preserves clean accuracy by assuming the purifier behaves approximately linearly: P(x) − x ≈ P(x_a) − x_a (Eq. 7). This is a strong assumption with limited evidence. The verification in Table 4 replaces the learned purifier with a hand-crafted operation (subtracting a PGD perturbation from clean images), which does not test whether a learned MAEP purifier actually satisfies this property. The paper's empirical results stand on their own, but the theoretical framing does not add meaningful support and should either be strengthened or softened.

- **Finetuning dataset is underspecified.** The paper claims "defense transferability without relying on using additional data" (abstract, line 7) and uses LoRA finetuning to address train-test discrepancy. However, it never explicitly states what dataset is used for LoRA finetuning — particularly in the cross-dataset experiments (e.g., CIFAR10 → ImageNet, Table 8). The text (line 184) says "we train an MAEP with masked images and then use LoRA to only finetune the decoder with masking ratio r=0" without specifying which dataset. If finetuning uses target-domain data (e.g., ImageNet images), the "no additional data" claim is substantially weakened. This must be clarified.

### Trivial

- The paper has placeholder citations ("Sec.," "Table 12 of Sec.") throughout Section 4.3 and elsewhere. While these appear to reference appendix content stripped by the parser, the main-text exposition of the objective function design (Section 4.3) reads as incomplete — Section 4.3.1 begins describing the loss and cuts off. The core training loss (referenced as Eq. 12) should be stated explicitly in the main body for completeness.

## Nice-to-Haves

- **Ablation of masking ratio r.** The paper fixes r=0.5 without ablating this choice. Since the masking ratio is a key hyperparameter that affects both the reconstruction quality and the train-test discrepancy, an ablation would strengthen the understanding.
- **Reporting variance.** The text states results are averaged over 5 runs (line 206) but no standard deviations are reported anywhere.
- **Clarify whether the "no additional data" claim holds for the finetuning step** as discussed in the Minor weaknesses section above; this directly affects how the main contribution is interpreted.

## Removed Points

1. **"Core method not specified in the main paper / Eqs. (9), (10), (12), LMAEP never defined"** — Removed per hard rules: the parser strips appendix and referenced sections from all papers. The equations and tables referenced (Table 12, 13, 18) were present in the original submission and are absent only due to parsing. The main body does define the MAE reconstruction loss (Eq. 1) and the DISCO purification loss (Eq. 2) which form the basis; the combined loss (Eq. 12) was in stripped content.

2. **"DiffPure 0.09% robust accuracy suggests improper hyperparameter tuning"** — Removed: this is speculation. The paper reports legitimate experimental data, and the reviewer provides no evidence of improper tuning.

3. **"Novelty is incremental relative to DISCO"** — Removed: the paper's contribution (MAE + masking mechanism for purification, LoRA finetuning for train-test discrepancy) is architecturally distinct from DISCO (EDSR + LIIF). The masking mechanism is a fundamentally different reconstruction paradigm from super-resolution networks.

4. **Formatting and grammatical nitpicks** — Removed per hard rules: these are parser artifacts, not author errors.

5. **Strength: "Theoretical and empirical justification that purification loss alone preserves clean accuracy"** — Removed per instructions: this strength conflicts with a verified weakness (the theoretical justification is weak). The weakness wins.

## Novel Insights

The most genuinely novel observation emerging from these reviews is the **tension between the paper's strongest asset and its biggest gap**: the cross-dataset transfer result (CIFAR10 → ImageNet outperforming ImageNet-trained diffusion models) is the kind of surprising empirical finding that can drive a field forward even if the theoretical framing is imperfect. However, the absence of adaptive attacks is particularly problematic precisely because the mechanism behind MAEP's transferability is not well understood — without adaptive attacks, it is unclear whether the robustness generalizes to an informed adversary, which is the whole point of claiming it as a "defense." This interplay between the paper's most exciting result and its most serious evaluation gap is worth the authors' direct attention.

## Suggestions

1. **Conduct and report adaptive attacks (BPDA, full white-box against the combined purifier+classifier).** This is the single most important addition for credibility. The paper's reported robustness numbers cannot be fully trusted without this evaluation, which is standard in the purification literature.

2. **Explicitly state the dataset used for LoRA finetuning in each experiment.** If finetuning uses only the source dataset (e.g., CIFAR10 even when transferring to ImageNet), state this clearly. If it uses target-domain data, acknowledge this and discuss how it impacts the "no additional data" claim.

3. **Either strengthen the theoretical motivation (Section 4.2) with direct empirical tests on the learned purifier, or remove it and frame the architecture choice as empirical discovery.** The current derivation does not meaningfully support the method design and may mislead readers about the level of theoretical grounding.

4. **State the MAEP training loss explicitly in the main paper.** Even if Eq. (12) was in the appendix, the main body of Section 4.3 should define the complete objective function that combines MLM reconstruction and purification loss, so the method is self-contained.

## Score and Decision

**Originality:** Good — first MAE-based purifier, the masking mechanism is a novel architectural choice for this task. **Importance of question:** High — defense transferability is practically relevant and underexplored. **Claims support:** Moderate — the impressive transferability results are well-supported, but the robustness claims are undermined by the lack of adaptive attack evaluation. **Soundness of experiments:** Moderate — strong on the transferability front, incomplete on adaptive attack evaluation. **Clarity of writing:** Below average — placeholder references and incomplete sections, though partly attributable to parsing. **Value to community:** Moderate to high, provided the main claims hold up under adaptive attacks.

The paper presents a genuinely interesting empirical finding (cross-dataset defense transfer with an MAE-based purifier) and demonstrates clear practical advantages (speed, efficiency). However, the lack of adaptive attack evaluation is a significant gap for a purification paper, and the underspecified finetuning data leaves ambiguity in the core "no additional data" claim. These are addressable but real concerns.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>