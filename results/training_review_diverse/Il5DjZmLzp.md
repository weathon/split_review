Now I have all the information I need. Let me synthesize the final consolidated review.

## Summary

The paper proposes Foundation Model Canonicalization (FMC), a training-free method that uses energy functions from pre-trained vision foundation models (CLIP, Stable Diffusion, SAM) to canonicalize images under nuisance transformations such as rotation, color shifts, and 3D viewpoint changes. The core idea is that minimizing a combined energy function over transformed versions of an image recovers the canonical form because foundation-model priors encode the natural image distribution. FMC outperforms PRLC (a prior method requiring dataset- and model-specific training) on rotated classification accuracy across CIFAR10, CIFAR100, and STL10 when compared on PRLC's own benchmarks.

## Strengths

1. **Training-free canonicalization that generalizes across models, datasets, and transformations**: FMC demonstrates that a single method — requiring no re-training or fine-tuning — works for CLIP, SAM, ViT, and ResNet across CIFAR10, CIFAR100, STL10, and ImageNet, and extends to color chrominance shifts and 3D viewpoint ranking (Sections 4.1–4.3). This directly supports the claim of training-free invariance that generalizes.

2. **Outperforms trained dataset-specific canonicalizers on their own benchmarks**: FMC beats PRLC (Mondal et al., 2023) on rotated accuracy and pose estimation across the datasets where PRLC has trained specialists (CIFAR10, CIFAR100, STL10). On CLIP, FMC achieves at least 16% higher C8 pose accuracy (Figure 4) and 7.4%/9.6%/2.1% higher rotated accuracy on CIFAR10/CIFAR100/STL10 respectively (Table 1). This is strong evidence that a training-free approach can outperform a trained specialist.

3. **Principled combination of complementary energy functions from multiple foundation models**: The paper derives three energy functions — from CLIP (via joint energy models), Stable Diffusion (via diffusion model free energy), and SAM (via segmentation eIoU) — and combines them linearly (Section 3.2). This provides a systematic way to extract and compose priors for canonicalization without additional training.

4. **Bayesian Optimization for continuous transformation spaces**: To handle continuous groups where exhaustive search is infeasible and gradient-based optimization is memory-prohibitive, the paper employs Gaussian Process optimization with expected improvement (Section 3.3). This enables FMC to work beyond discrete rotations (e.g., color shifts, 3D viewpoints where Zero123 generates candidates).

5. **Thorough experimental comparison against a strong baseline**: The paper provides extensive results across multiple datasets (CIFAR10, CIFAR100, STL10, ImageNet), multiple foundation models (CLIP, SAM), multiple downstream models (ViT, ResNet), and multiple metrics (accuracy, pose accuracy, pose error), with an additional ImageNet extension demonstrating cross-dataset generalization.

## Weaknesses

### Fatal
None.

### Major
None that threaten the core claims. The results on CIFAR10, CIFAR100, and STL10 (where PRLC has trained specialists) are solid and uncontested by the reviewer's criticisms.

### Minor

1. **ImageNet comparison framing could mislead**: The paper states "we outperform PRLC by 4.4% on ImageNet" (line 25) lumped together with datasets where PRLC has specialists. In reality, PRLC has no ImageNet-trained canonicalizer; the comparison uses PRLC's STL10-trained canonicalizer transferred to ImageNet (line 185: "We take the best-performing PRLC aligner (STL10)"). The paper is transparent about this, and the framing as cross-dataset generalization is valid — it *is* a fair test of generalization ability, and FMC genuinely wins. However, the presentation in the abstract lumps ImageNet with the other datasets without clarifying this distinction, which could mislead readers into thinking PRLC has an ImageNet specialist that FMC beats. This should be clarified.

2. **Hyperparameter values and selection protocol not disclosed**: The combined energy function has five hyperparameters (α, β, γ₁, γ₂, γ₃). While they are formally defined (lines 131, 153), the paper does not report their values, state whether they were fixed across all experiments or tuned per dataset, or describe the validation procedure used. The Discussion mentions "hyperparameter selection via Bayesian Optimization" (line 281) but this is not operationalized in the experiments section. This makes it difficult for readers to assess sensitivity or reproduce results.

3. **No ablation of the three energy components**: The paper claims to combine three energy functions but never evaluates their individual contributions. Without ablations, it is unclear whether all three are necessary, whether any single energy (e.g., CLIP alone) already achieves the reported results, or whether components interfere. This limits understanding of the method's essential ingredients.

4. **PRLC adaptation to SAM not described**: The paper compares against PRLC on SAM for segmentation (Section 4.2) but does not explain how PRLC — originally designed for classifiers — was adapted to the segmentation task. This makes the SAM comparison opaque and harder to reproduce.

5. **3D viewpoint section uses a different paradigm than canonicalization**: The 3D experiments use Zero123 to generate multiple views and then select the view with minimum FMC energy. This is viewpoint selection from generated candidates rather than "canonicalization" in the strict sense of undoing a known transformation. The paper should more clearly distinguish this as an application of energy ranking rather than canonicalization.

### Trivial

1. **Color baseline comparison is qualitative**: When comparing against Barron & Tsai (2017) and Hernandez-Juarez et al. (2020) for color correction, the paper states "not competitive" without providing quantitative comparisons. Adding numbers would strengthen the presentation.

2. **Inference cost not quantified**: The Limitations section mentions FMC is "slow at inference time" but provides no rough FLOP or timing comparison against PRLC. Even a rough estimate would help readers assess practical feasibility.

## Nice-to-Haves

- Provide a sensitivity analysis for the hyperparameters (α, β, γ₁, γ₂, γ₃) showing how performance varies over a reasonable range.
- Ablate the number of Bayesian optimization steps and its effect on canonicalization quality.
- Discuss failure modes — categories of images (e.g., symmetric objects) where the energy landscape might not be well-behaved.
- Test on additional foundation models (e.g., DINO, MAE) to further substantiate the claim of model-agnostic generalization.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Energy functions lack empirical validation"** — The reviewer claims "no direct evidence that these energies are actually minimized at the true canonical transformation." This is factually wrong: Figure 4 directly reports C8 pose accuracy and pose error, which measure exactly whether the predicted transformation matches ground truth. On CIFAR10, FMC achieves ~80%+ C8 pose accuracy — this IS the requested validation. *Removed: factually incorrect.*

- **"Diffusion equation has undefined variable η"** — The paper defines η as "the noise" (line 86). *Removed: factually incorrect; the variable is defined.*

- **"ImageNet comparison invalidates central claim"** — The reviewer claims this is "structural" and "invalidates the central claim of Table 1." This is an overstatement. Table 1 includes CIFAR10/100/STL10 where PRLC has specialists and FMC wins fairly. The ImageNet row is a cross-dataset generalization test disclosed in the text. *Downgraded from "fatal/structural" to minor presentation issue.*

- **"PRLC column format confusing"** — Formatting/style nitpick about Table 1. *Removed: pure formatting nitpick.*

- **"SAM results don't show invariance"** — The claim "FMC can make models like CLIP and SAM invariant" is supported by 26.2% pose accuracy improvement and 3.4% mAP gain. The reviewer's characterization that only 3.4% is shown ignores the pose accuracy result. *Removed: mischaracterizes the evidence.*

- **"Strength: outperforms trained canonicalizers on their own benchmarks"** — This strength from the Strength Finder is valid and retained in Strengths above.

- **"Strength: thorough experimental comparison"** — Valid and retained.

## Novel Insights

The key insight beyond the paper's own contributions is that the reviews reveal a tension between novelty and rigor. The paper's core idea — using foundation model energy functions as training-free canonicalizers — is genuinely novel and well-motivated. However, the reviews surface a pattern where the paper makes strong comparative claims (e.g., "outperforms PRLC specialists" on ImageNet) that outrun the precision of its experimental design. Missing ablations and undisclosed hyperparameters prevent the reader from understanding why the method works and which components are essential. The paper would be substantially stronger if it tightened its comparative claims to match its experimental setup and added the ablations that the reviewers independently identified as missing.

## Suggestions

1. Clarify in the abstract/Table 1 caption that the ImageNet comparison uses PRLC's STL10 canonicalizer transferred to ImageNet (i.e., a test of cross-dataset generalization), to avoid misleading readers into thinking PRLC has an ImageNet-trained specialist.
2. Report the hyperparameter values (α, β, γ₁, γ₂, γ₃) used in all experiments, ideally fixed across all settings, and describe the selection procedure.
3. Add an ablation study decomposing the three energy terms — at minimum show accuracy with each term alone and all combinations — to justify the design and reveal which components are essential.
4. Describe how PRLC was adapted to SAM for the segmentation experiments.
5. Clarify in Section 4.3 that the 3D experiments are an application of energy-based viewpoint selection, distinct from canonicalization of a known transformation.

## Score and Decision

The paper proposes a genuinely novel approach to a well-motivated problem (training-free canonicalization). The core claims are supported for the main experimental settings (CIFAR10, CIFAR100, STL10) where PRLC has specialists. The weaknesses are addressable — missing hyperparameter details, absent ablations, and imprecise framing of the ImageNet comparison — and none rise to the level of invalidating the central contribution. The paper represents a solid contribution to the literature on invariance and canonicalization.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>