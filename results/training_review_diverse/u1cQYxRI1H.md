Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

The paper proposes IC-Light (Imposing Consistent Light transport), a training methodology that enforces a light transport consistency loss to enable scaling diffusion-based illumination editing models to over 10 million images across diverse data sources (in-the-wild augmentations, 3D renders, light stage captures). The method supports multiple backbones (SD1.5, SDXL, Flux) and demonstrates applications including background-conditioned relighting and normal map extraction. The key claim is that the consistency loss prevents the model from becoming a "structure-guided random generator" by physically constraining it to modify only illumination while preserving intrinsic properties.

## Strengths

- **Large-scale, diverse dataset construction (10M+ images across three data sources).** The paper unifies data from in-the-wild augmented images (~6M), 3D renders (~4M), and real light stage captures into a common format. This is a non-trivial engineering effort that enables training at a scale beyond prior illumination editing work, which typically relies on smaller/structured datasets. The quantitative results (Table 1) show the full method achieves best LPIPS (0.21), and visual comparisons (Fig. 6) demonstrate advantages over Relightful Harmonization.

- **Multi-backbone support and downstream applications.** The method is demonstrated with SD1.5, SDXL, and Flux, showing it is architecture-agnostic. The normal map extraction via multiple consistent inferences (Section 4.3, Eqs. 7–9) is a clever zero-shot application that exploits the model's ability to produce consistent appearances under varying illumination.

- **Quantitative ablation study with multiple components.** Table 1 systematically ablates light transport consistency, augmentation data, 3D data, and light stage data, showing contributions from each component. This provides evidence that the design choices matter.

## Weaknesses

### Major

- **The theoretical derivation of the consistency loss is mathematically unsound.** The paper claims (Section 3.2) that applying light transport linearity $\hat{I}_{L_1+L_2} = \hat{I}_{L_1} + \hat{I}_{L_2}$ to the diffusion denoising formula $\hat{I}_L = (I_{\sigma_t} - \epsilon_L)/\sigma_t$ yields $\epsilon_{L_1+L_2} = \epsilon_{L_1} + \epsilon_{L_2}$. This is incorrect. Using the paper's own formulation with the same noisy latent $I_{\sigma_t}$ across branches:

  $(I_{\sigma_t} - \epsilon_{L_1+L_2})/\sigma_t = (I_{\sigma_t} - \epsilon_{L_1})/\sigma_t + (I_{\sigma_t} - \epsilon_{L_2})/\sigma_t$
  
  Simplifying: $\epsilon_{L_1+L_2} = \epsilon_{L_1} + \epsilon_{L_2} - I_{\sigma_t}$

  The extra $-I_{\sigma_t}$ term does not vanish. Furthermore, in practice the three branches use *different* noisy latents (since the clean targets $I_{L_1}, I_{L_2}, I_{L_1+L_2}$ differ), which introduces additional terms. The paper introduces a learnable MLP $\phi$ to "adapt among potential data domains," implicitly acknowledging the mismatch, but does not explain how $\phi$ resolves the derivation error. While the loss as implemented ($\|M\odot(\epsilon_{L_1+L_2} - \phi(\epsilon_{L_1},\epsilon_{L_2}))\|_2^2$) may still provide useful regularization empirically, the paper's central theoretical claim — that the loss*