- Decision: Reject
- Avg Score: 4.50
- Scores: 3, 6, 6, 3
I now have a thorough understanding of the paper and all the reviewer claims. Let me write the final consolidated review.

---

## Summary

This paper proposes Foundation Model Canonicalization (FMC), a training-free method that uses energy functions derived from pre-trained foundation models (CLIP, Stable Diffusion, SAM) to canonicalize images under nuisance transformations (rotation, color shift, 3D viewpoint). The key insight is that these models encode priors about the natural image distribution that can be exploited to find the "canonical" version of an image. FMC combines three energy terms from these models and minimizes them over transformation parameters, using Bayesian optimization for continuous transforms. The paper evaluates FMC on rotated-image classification (CIFAR10/100, STL10, ImageNet), segmentation with SAM (COCO), color chrominance correction, and 3D viewpoint selection.

## Strengths

- **Training-free canonicalization across models and tasks is a novel and useful idea.** The paper demonstrates that FMC, without any training, can be applied to CLIP (classification) and SAM (segmentation), improving their robustness to rotations. The SAM segmentation experiment (Table 2) shows a clean comparison where FMC improves PRLC's C4 pose accuracy by 26.2% and mAP by 3.4%, both using SAM as the downstream model, providing the fairest evidence that the method adds value.

- **Extension to continuous transformations beyond discrete rotations.** Section 4.3 shows FMC working on color chrominance shifts (+9.9% accuracy on CIFAR100 with CLIP) and 3D viewpoint selection (up to 11.4% improvement on poor viewpoints). These go beyond what PRLC's discrete-grid approach can handle and demonstrate the generality of the energy-based framework.

- **The modular energy design is principled in concept.** Deriving energy functions from a classifier (CLIP via JEM), a diffusion model (Stable Diffusion), and a segmentation model (SAM) and combining them linearly follows the established EBM composition literature (Du et al., 2023; Liu et al., 2022). The paper correctly identifies that foundation models trained on large-scale natural data can serve as effective priors for the "upright assumption" that the canonical image is the most likely one.

## Weaknesses

### Major

- **Asymmetric comparison with PRLC undermines the headline claims.** The central claim that FMC "beats PRLC on their own settings" is based on comparisons where the downstream models differ. Table 1 compares FMC (using CLIP ViT-H-14, trained on 400M image-text pairs) against PRLC's canonicalizers paired with ResNet50/ViT classifiers trained only on CIFAR10/100/STL10. The accuracy gap (e.g., +7.4% on CIFAR10) could substantially reflect CLIP's superior representations rather than FMC's canonicalization. For the "PRLC on CLIP" comparisons, PRLC's canonicalizer was trained for ResNet50 and merely transferred to CLIP — it was never optimized for CLIP's embedding space. The strongest fair comparison is the SAM experiment (Table 2), where both methods use the same downstream model (SAM-ViT-H) — and FMC does win there, but this cleaner result is not the one emphasized in the paper's headline claims. The paper should either (a) compare both methods with the same downstream backbone, or (b) explicitly acknowledge this asymmetry and frame the results as "FMC+CLIP vs. PRLC+ResNet50" rather than "FMC beats PRLC."

- **No ablation of the three energy components.** The paper combines three energy functions (from CLIP, Stable Diffusion, SAM) with five hyperparameters (α, β, γ₁, γ₂, γ₃) but never ablates them. The reader cannot tell whether all three models are necessary, whether CLIP's energy alone suffices, or whether the more expensive models (Stable Diffusion, SAM) add meaningful signal. Relatedly, the hyperparameter values are not reported — the paper mentions they can be tuned via Bayesian optimization but does not state what values were actually used or whether they were tuned per dataset/transform, which is essential for reproducibility.

- **Missing key baselines.** The paper compares only to PRLC and "No Canon." A natural and important baseline is to use CLIP's own classifier logits directly as an energy function: rotate the image, compute the max or logsumexp over class logits, and pick the rotation with the highest value. This is approximately a special case of E_uncond (with β=1, α=0) and would test whether the additional complexity (Stable Diffusion, SAM, Bayesian optimization) is actually needed. For color shifts, no baseline (not even a simple gray-world assumption) is compared despite the paper noting FMC is "not competitive against SOTA supervised approaches." Without these baselines, the reader cannot assess whether FMC's energy assembly adds value over simpler alternatives.

- **No reporting of the 5 hyperparameter values.** The five hyperparameters (α, β, γ₁, γ₂, γ₃) are never disclosed. This is not a trivial omission — these weights control the balance between the three foundation models and the two terms within E_uncond. Without them, the experiments cannot be independently reproduced.

### Minor

- **Computational cost acknowledged but not quantified.** The paper notes "our technique is slow at inference time due to repeated evaluations of large models" but does not report any runtime, number of Bayesian optimization iterations, or approximate FLOP count per image. For C8 rotations (8 evaluations × 3 models), the cost is already substantial; for continuous transforms (Bayesian optimization with dozens of iterations) it is far higher. Quantifying this would help readers assess practical viability.

- **No analysis of failure cases or statistical significance.** The paper does not examine when FMC selects the wrong transformation — e.g., whether it has systematic biases toward certain textures or classes. Accuracy differences of a few percent are reported without confidence intervals or error bars, making it difficult to assess whether gains are stable or due to noise.

- **The diffusion energy formulation relies on unstated design choices.** The paper uses only time steps 500–1000 of Stable Diffusion's 1000-step schedule and a single noise sample per time step, but provides no analysis justifying these choices or showing sensitivity to them. While the general approach (using diffusion loss as an energy) is grounded in prior work, these specific design decisions are not validated.

### Trivial

- The paper states it "replaced LSE(.) with max(.) for simplicity" (line 78), but the actual E_uncond equation (line 124) uses a linear combination of *both* mean and max — this is a different function than described. The text and equation should be reconciled.

## Nice-to-Haves

- An experiment that validates each energy function individually (e.g., plotting E_uncond, E_diff, E_seg vs. rotation angle for a sample of images) would provide intuition about whether each term indeed has a minimum at the canonical orientation.
- The 3D viewpoint experiment could be strengthened by comparing against a simple baseline like "pick the Zero123 view with the highest CLIP class logit."
- Since the paper targets training-free canonicalization, a discussion of whether lighter-weight models (e.g., CLIP ViT-B vs. ViT-H or distilled Stable Diffusion) could provide a practical speed-accuracy trade-off would be useful.

## Removed Points

These points were flagged by reviewers but are removed after verification against the paper:

- **Criticism that E_diff "is not a principled energy" because it uses one fixed noise realization per time step.** The paper's equation uses independently sampled noise at each time step, which is a standard Monte Carlo estimate of the expected diffusion loss (Graikos et al., 2022). While it is an approximation (not an exact log-likelihood), it is a well-established approach in the literature, not an ad-hoc choice.
- **"No evidence that FMC works for lighting, occlusion, scale"** — The paper explicitly defines its scope as rotation, color shift, and 3D viewpoint. Demanding coverage of all possible transformations is scope creep.
- **"PRLC's SAM canonicalizer training data not described"** — The paper follows PRLC's published setup; the training distribution is PRLC's own, not the authors' to disclose. Speculating about unfairness without evidence is not a valid criticism.
- **"No theoretical proof that foundation model energies satisfy the required ordering"** — This is an empirical systems paper. Requesting formal proofs is beyond the standard for work in this area. A demonstration that the approach works empirically on multiple transforms is the expected form of evidence.
- **Missing related works** (a comment from the harsh critic not explicitly listed but implied) — I have no external source to confirm the existence of omitted works.

## Novel Insights

The two reviews essentially converge on the same picture: the paper has a genuinely interesting idea (harnessing foundation model priors for training-free canonicalization) and some promising results (most cleanly the SAM segmentation experiment), but the evaluation is weakened by asymmetric comparisons that inflate the apparent advantage over PRLC, and by a lack of ablation/baselines that would validate the specific design choices. The strongest insight from synthesizing the reviews is that the paper's core contribution — using foundation models as energy functions for canonicalization — is plausible and worth pursuing, but the current experimental framing makes stronger claims than the evidence supports. A revised version with controlled comparisons and proper ablations could be quite strong.

## Suggestions

1. **Re-frame the main comparisons.** Acknowledge that FMC leverages larger pre-trained models (CLIP) and that the primary comparison of scientific interest is canonicalization quality given the same downstream model. Emphasize the SAM experiment (Table 2) as the cleanest evidence, and for CLIP experiments, include a baseline where CLIP's own logits serve as a rotation-energy function.
2. **Ablate the energy components.** Show classification accuracy with each energy term individually (E_uncond only, E_diff only, E_seg only), with pairs, and with all three. Report the hyperparameter values used and whether they were tuned per dataset or held constant.
3. **Add the rotate-and-max baseline.** Using CLIP's max logit as the canonicalization signal is the most direct baseline and would clarify whether the multi-model assembly is necessary.
4. **Quantify computational cost.** Report average inference time per image (or per-pixel for segmentation) and the number of function evaluations used by Bayesian optimization.
5. **Report hyperparameter values.** Explicitly state the α, β, γ₁, γ₂, γ₃ values used in each experiment.
