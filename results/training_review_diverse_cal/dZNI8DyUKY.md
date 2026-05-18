I now have a thorough understanding of the paper and all reviewer claims. Let me produce the final consolidated review.

---

## Summary

This paper introduces MAEP, the first masked-autoencoder-based adversarial purifier for test-time defense. Unlike diffusion-based purifiers (DiffPure, ScoreOpt) that suffer from high inference cost and poor cross-dataset transferability, MAEP uses a ViT-based MAE trained with a purification loss to remove adversarial perturbations. The core claims are: (1) MAEP is the first pure purifier based on MAE, (2) it achieves defense transferability across datasets (CIFAR10 → ImageNet) without additional data, (3) it delivers SOTA robust accuracy while being an order of magnitude faster than diffusion methods, and (4) it generalizes across attack types. The key evidence is that MAEP trained on CIFAR10 achieves ~74% robust accuracy on ImageNet under AutoAttack (ε=4/255), outperforming diffusion models trained on ImageNet, while requiring ~47ms per image vs. >7000ms for DiffPure.

## Strengths

- **First MAE-based adversarial purifier with a clearly differentiated paradigm.** The paper convincingly distinguishes its approach from related MAE-based works: DRAM (detection+repair, not a purifier) and NIM-MAE (adversarial training with noise injection). MAEP is genuinely the first to use a standard MAE reconstruction loss as a standalone test-time purifier, opening a new direction for ViT-based defenses.

- **Exceptional defense transferability demonstrated empirically.** Table 8 shows MAEP trained only on CIFAR10 achieves ≈74% robust accuracy on ImageNet under AutoAttack (ε=4/255), outperforming DiffPure (68.60%) and ScoreOpt (68.05%) that were trained *on ImageNet itself*. At ε=8/255, MAEP (62.42%) remains competitive with DISCO (62.56%), another transfer-capable method. This cross-dataset transfer — low-res to high-res without retraining — is a genuine advance over diffusion-based purifiers that degrade sharply when transferred (Tables 2, 3).

- **Significant efficiency advantage over diffusion-based purifiers.** Table 9 reports MAEP inference at 47.9 ms/image vs. DiffPure's >7000 ms/image on CIFAR10. Table 10 shows MAEP training at ~7 hours vs. DDPM's >10.6 hours on a TPU. This practical efficiency is a meaningful contribution — diffusion-based purification has been criticized as impractical for real-time settings.

- **Strong robust accuracy on challenging datasets.** On CIFAR100 (Table 7), MAEP achieves 74.31% robust accuracy (AutoAttack) and 70.04% clean accuracy, substantially exceeding DiffPure (60.80% / 62.50%) and DISCO (66.75% / 65.25%). Notably, MAEP's robust accuracy exceeds its own clean accuracy, consistent with the paper's design rationale.

- **Lightweight LoRA finetuning effectively addresses train-test discrepancy.** The masking ratio shift (r=0.5 during training vs. r=0 during inference) is a practical concern, and the paper shows that LoRA finetuning with minimal added parameters improves both clean and robust accuracy (Table 5), while keeping the approach parameter-efficient.

## Weaknesses

### Fatal
None.

### Major

1. **No evaluation against adaptive attacks that differentiate through the purifier.** This is the most significant gap. The paper evaluates only AutoAttack and PGD, which treat the purifier+classifier as a black box. Since MAEP uses a differentiable ViT-based MAE, a white-box adversary could backpropagate through the entire pipeline (purifier → classifier) using BPDA or a full gradient attack. In the adversarial purification literature, this is standard practice — many purification methods that appear robust under black-box attacks are broken by adaptive attacks that account for the purifier. Without this evaluation, the paper's robustness claims are not fully validated, and the comparison to baselines like DiffPure (which has been evaluated under adaptive attacks in prior work) is asymmetric. This gap is *major* because it directly affects the believability of the core robustness results.

2. **The theoretical justification in Section 4.2 is not sound and should be substantially revised or dropped.** The derivation attempts to argue that the purification loss ℓ₁(P(xₐ), x) can maintain clean accuracy, but the logic is flawed: Eq. (7) claims P(x) − x ≈ P(xₐ) − xₐ because x ≈ xₐ (bounded by ε in ℓ∞ norm). This does not follow — the purifier P is a nonlinear function, and bounded ℓ∞ input difference does not guarantee similar output differences, let alone similar purification *directions*. The verification in Table 4 does not rescue this: it pre-processes the training set by adding −δₐ (via PGD) and tests a non-defense classifier, which tests how a classifier behaves on negatively perturbed images, not whether the purifier P behaves as theorized. The paper acknowledges this is a "conjecture" and a "feasible but simple explanation," which is honest, but the framing as theoretical grounding is misleading. This weakness is real but not fatal — the paper's contributions are empirical, and removing or rewriting this section would not invalidate the experimental results.

### Minor

3. **Missing standard deviations despite reporting averages over 5 runs.** The paper states that "each result for clean or robust accuracy was obtained by averaging from 5 runs with varying random seeds" but does not report standard deviations or confidence intervals. Given that performance differences between methods are often a few percentage points (e.g., MAEP 62.42% vs. DISCO 62.56% at ε=8/255 on ImageNet transfer), the absence of variance information makes it impossible to assess whether differences are statistically significant. This is a routine experimental reporting standard.

4. **No ablation of the masking ratio.** The paper uses r=0.5 during training and r=0 during inference, but does not ablate this choice. Would r=0.25 or r=0.75 work better? Can the model be trained with r=0 and still achieve similar robustness? These ablations would help understand why the masking mechanism helps and whether the current choice is optimal. This is a missing ablation, not a fatal gap.

5. **The SOTA claim is overstated at higher perturbation budgets.** The abstract states that MAEP "achieves state-of-the-art performance even when tested directly on ImageNet, outperforming existing diffusion-based models trained specifically on ImageNet." This is clearly supported at ε=4/255 on ImageNet transfer. However, at ε=8/255 on ImageNet, the comparison is primarily against DISCO (not diffusion models), and the margin is within 0.14 percentage points. The claim should be qualified to reflect the setting where it holds most clearly.

6. **Inconsistent baseline coverage across tables.** Tables 2 and 6-7 include different sets of baselines, making cross-table comparisons difficult. For example, Table 2 includes only DiffPure, DISCO, and MAEP (not ScoreOpt), while Table 3 does include ScoreOpt. A consistent baseline set across all experimental settings would strengthen the evaluation.

7. **Model size and compute cost not reported.** The paper reports inference and training time but does not state the number of parameters for the MAEP model, nor the GPU hours or FLOPs. This makes it hard to calibrate the efficiency claims relative to baselines of potentially different sizes.

### Trivial

- Some section references are dangling ("will be shown in Sec." without completing the reference, in Section 4.3). These are likely LaTeX cross-reference artifacts and should be filled in.

## Nice-to-Haves

- Evaluate adaptive attacks (BPDA, full-gradient attack) through the purifier to validate robustness claims.
- Include MAEP trained on ImageNet as a same-dataset baseline for Table 8, to enable direct comparison with diffusion models trained on ImageNet.
- Report standard deviations for all accuracy numbers.
- Add ablations on the masking ratio (r ∈ {0, 0.25, 0.5, 0.75}) to motivate the choice.
- State model parameter counts and compute (GPU hours) for reproducibility.

## Removed Points

These points were flagged by reviewers but are removed or downgraded per the review guidelines:

- *"Core method never clearly defined in the main text; L_MAEP not defined; dangling references."* — **Removed.** The main text describes the two-stage training, purification loss (Eq. 2), MLM loss (Eq. 1), masking ratio shift, and LoRA finetuning. The final loss (Eq. 12) and several supporting equations are in the appendix, which was stripped by the parser. Per policy, missing appendix content is not a valid weakness.
- *"Tables 2, 3 do not include ScoreOpt."* — **Removed.** Table 3 explicitly includes ScoreOpt, as confirmed in the caption ("ScoreOpt, Diffpure, DISCO, and our MAEP"). Table 2 (CIFAR100→CIFAR10) does not include ScoreOpt, but there is no evidence this is an omission rather than unavailability of those results for that specific transfer direction.
- *"The paper does not systematically test across a broad set of attack algorithms (e.g., FAB, BPDA, SPSA)."* — **Downgraded.** AutoAttack (used in the paper) already includes FAB and Square attacks. The substantive gap is the lack of *adaptive* attacks (BPDA), which is kept as a Major weakness above. The generic "broad set" complaint is removed.
- *"The comparison to DISCO is repeated often, but DISCO uses additional data (EDSR trained on DIV2K)."* — **Removed.** The paper explicitly acknowledges this distinction (Section 2: DISCO "used EDSR trained on additional dataset... its performance will heavily depend on additional data"). This is a strength of MAEP, not a weakness, and the paper makes this clear.
- *"DRAM was not selected for comparison."* — **Removed.** The paper explains why DRAM is excluded (it involves detection+repair, a different paradigm). The reviewer's disagreement with this exclusion is a matter of taste, not a valid weakness.
- Various formatting/style nitpicks — **Removed** per policy.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the standard tension in adversarial purification: strong results under standard benchmarks (AutoAttack) must be validated against adaptive attacks, and the theoretical framing could be replaced with a cleaner empirical motivation. Neither insight is novel to this paper.

## Suggestions

1. **Add adaptive attack evaluation.** This is the single most impactful improvement. Evaluate MAEP under BPDA with a full-gradient approximation or a proxy that differentiates through the MAE. If the purifier introduces gradient masking due to the masking mechanism, design a workaround (e.g., averaging over multiple masks, or a differentiable approximation). Without this, the robustness claims are incomplete.
2. **Either drop or fundamentally rewrite Section 4.2.** Replace the flawed theoretical derivation with a clean empirical analysis: show that MAE reconstruction error is higher on adversarial images than on clean images across datasets, demonstrate that purified images lie closer to the clean manifold, or analyze the latent space separation. This would provide genuine insight without making unsupported mathematical claims.
3. **Report standard deviations** for all main results (Tables 6-8), since 5 runs are already performed.
4. **Add a masking ratio ablation** to justify the r=0.5 choice and understand the train-test discrepancy better.
5. **Qualify the SOTA claim** in the abstract to explicitly reference the ε=4/255 setting on ImageNet transfer, where the advantage is clearest.

## Score and Decision

The paper introduces a genuinely novel application of MAE to adversarial purification and demonstrates compelling results on cross-dataset transferability and efficiency — contributions that are both timely and practically relevant. However, the evaluation has a significant gap: the absence of adaptive attacks (BPDA) raises legitimate questions about whether the claimed robustness holds under stronger threat models. This gap prevents full acceptance in the current form. The paper would be substantially strengthened by addressing this concern.

**Score:** 5.5

**Decision:** Accept (borderline, contingent on addressing the adaptive attack gap in the final version)

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>