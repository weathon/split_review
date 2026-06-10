**Final Review**

## Summary

This paper proposes Principled Masked Autoencoders (PMAE), a modified masking strategy for Masked Image Modeling that replaces the standard practice of masking random spatial patches with masking in PCA space. The idea is to project images onto principal components, randomly mask a subset of them (removing certain fractions of explained variance), then project back to pixel space and train a MAE-style encoder-decoder to reconstruct the masked variance. The paper reports consistent improvements over spatial masking on five small-scale datasets (CIFAR-10, TinyImageNet, three MedMNIST datasets) with a ViT-T/8 backbone, and demonstrates that a hyperparameter-free randomized variant (PMAE_rd) often matches or exceeds the optimally-tuned spatial masking baseline.

## Strengths

1. **Consistent empirical gains across diverse small-scale datasets** — The paper reports that PMAE_ocl improves over MAE_std by an average of +10 percentage points across five datasets spanning natural and medical images (Section 5). PMAE_rd (randomized ratio, no tuning) outperforms the optimally-tuned MAE_ocl in 9 of 10 evaluation configurations (Table 1). The consistency across datasets suggests a genuine advantage.

2. **Hyperparameter robustness is convincingly demonstrated** — PMAE achieves near-optimal performance across all five datasets with 10–20% of variance masked, whereas MAE's optimal ratio varies widely and is dataset-dependent (Fig. 5). The randomized variant requires zero hyperparameter tuning yet beats the tuned spatial baseline in almost all cases, which is practically significant.

3. **Faster convergence** — Fig. 6 (left) shows PMAE reaching MAE's 800-epoch performance in just 200 epochs on CIFAR-10, demonstrating a substantial efficiency advantage.

4. **Clear intuitive motivation** — The paper articulates a concrete failure mode of spatial masking (complete object removal, redundant information) and provides a principled rationale for why PC-space masking mitigates it, grounded in the latent-variable perspective of Kong et al. (2023). Fig. 7 visualizes the correspondence between principal components and spatial features.

5. **General framework formulation** — Eq. (3.1) casts masking generically as operating in any invertible transformed space, with PCA as one instantiation. This separation of the core idea from the specific transformation is well-framed and opens future directions (Fourier, wavelets, kernel PCA).

## Weaknesses

### Fatal

None.

### Major

1. **Structural confound: the encoder input differs fundamentally between MAE and PMAE.** In the standard MAE implementation (He et al., 2021), the encoder receives only *visible patches* — masked patches are removed entirely, so at r=0.75 the encoder processes roughly 25% of tokens. In PMAE, the encoder receives the *full image projected back from the visible principal components* (Eq. 3.1: $h(\mathbf{m}, \mathbf{x}) = t^{-1}(\mathbf{m} \odot t(\mathbf{x}))$): every patch is present, but each carries degraded information. The PMAE encoder thus processes 100% of patches. This conflates two variables: (i) the masking space (PC vs. pixel), and (ii) the number of tokens the encoder sees. Because Vision Transformers benefit from additional spatial context, the reported improvements may be partly or largely driven by this token-count difference rather than the PC masking strategy itself. The paper does not acknowledge or control for this confound. A controlled comparison would require either (a) a version of MAE where the encoder sees all patches (masked ones replaced with a learnable mask token, as in BEiT/SimMIM), or (b) a version of PMAE where the encoder sees only a subset of patches. Without this control, the core attribution claim is weakened. (Note: the confound's effect direction is not unambiguously pro-PMAE — more tokens but each is heavily degraded — but it is an uncontrolled variable that must be addressed.)

2. **Evaluation is limited to small-scale, low-resolution benchmarks.** The paper evaluates on CIFAR-10 (32×32, 10 classes), TinyImageNet (64×64, 200 classes), and MedMNIST (64×64) with a ViT-T/8 backbone. This is far below the standard evaluation protocol in the MIM literature (ImageNet-1K at 224×224 with ViT-B or larger). On 32×32 images, PCA operates on only 1024 dimensions and the ViT sees only 4×4=16 patches — qualitatively different from the standard MIM setting of 196 patches. The paper acknowledges PCA's cubic scaling cost (Section 8) but does not evaluate at scales where this is a practical concern (e.g., 224×224 images would require PCA on 50176 dimensions). The claims of general effectiveness are not supported by evidence at the scales and complexities that define the field's standard benchmarks.

3. **Only one architecture (ViT-T/8) is tested.** The paper does not evaluate with larger backbones (ViT-S, ViT-B) or alternative architectures. Architectural scaling is standard practice in MIM evaluations. The method's effectiveness with larger models — where PCA's quadratic memory and cubic time costs also become more burdensome — is unknown.

### Minor

1. **The faster convergence claim (200 epochs exceeds 800) is only shown for CIFAR-10** in Fig. 6 (left). The paper states additional figures exist in the appendix, but the main paper provides this striking efficiency evidence for only one dataset.

2. **PCA introduces dataset-level statistics into the masking strategy.** The eigenvectors are computed on the full training set, meaning the masking is informed by global dataset covariance structure. This differs qualitatively from per-sample random spatial masking and is not discussed. On small datasets, the covariance structure may be dominated by the specific training set rather than general properties of natural images.

3. **The PMAE encoder never receives a "clean" patch** — every patch is degraded by the removal of some PCs. The paper does not disentangle whether the benefit comes from PC masking specifically or from any global/non-spatial degradation strategy (e.g., Fourier-domain masking, additive noise in PC space). A comparison to other global masking strategies would strengthen attribution.

### Trivial

- On 32×32 images with 8×8 patches, the ViT processes only 4×4=16 patches — far from the standard MIM setting of 196 patches. This is useful context for interpreting the results.
- The "oracle" terminology for MAE_ocl/PMAE_ocl is slightly misleading since it only tunes one hyperparameter.

## Nice-to-Haves

- A controlled experiment comparing PMAE to a version of MAE where the encoder receives all patches (with mask tokens for masked ones) would directly address the token-count confound.
- Evaluation on at least one standard-scale benchmark (ImageNet-100 or ImageNet-1K at 224×224) would substantially strengthen the claims of general effectiveness.
- Comparison to other global/non-spatial masking strategies (Fourier masking, frequency filtering) would help isolate whether the benefit is specific to PCA or generalizes to any global masking approach.
- Reporting error bars or confidence intervals for the main results (Table 1) would improve rigor.

## Removed Points

- **"Inflated reporting (26% relative improvement may be misleading)"** — Removed: The paper reports both relative (26%) and absolute (+10pp) improvements, which is standard. The critic's speculation about baseline quality is unsupported by paper evidence.
- **"PMAE is not the first to leverage PCA"** — Removed: The paper's novelty claim is appropriately qualified ("To the best of our knowledge...") and is scoped to MIM specifically, not PCA in general. Cited alternatives target different settings (denoising autoencoders, VQVAE).
- **"Claim that MIM leads to suboptimal learning approach is stated as conclusion"** — Removed: The paper explicitly says "We conjecture that..." (line 46), clearly framing it as a hypothesis.
- **"No error bars for main results"** — Partially removed: The ablation study (Fig. 6 right) includes standard errors. Whether Table 1 includes error bars cannot be verified from the parsed text (table is an image). Moved to Nice-to-Haves.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Control for encoder token count.** This is the single most impactful experiment. Modify the MAE baseline to present all patches to the encoder (masked replaced with a learnable mask token, as in BEiT/SimMIM), and compare PMAE to this controlled version.
2. **Add at least one ImageNet-scale evaluation.** Even ImageNet-100 at 224×224 with ViT-S or ViT-B would substantially strengthen the evidence for general effectiveness.
3. **Include larger backbones** (ViT-S, ViT-B) to demonstrate scalability.
4. **Compare against other global masking strategies** (Fourier masking, random frequency filtering) to isolate whether the benefit is specific to PCA.
5. **Explicitly acknowledge and discuss the token-count confound** in the method section, even if a full control experiment is deferred.

## Score and Decision

The paper introduces a well-motivated idea and provides consistent evidence of improvement across small-scale benchmarks. However, the evaluation contains a structural confound (different encoder token counts between MAE and PMAE) that undermines attribution of the gains to PC masking, and the evaluation scale is far below the standard in the MIM literature. Given these issues, the current evidence does not convincingly support the paper's core claims at the level expected by ICLR.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>