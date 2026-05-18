Now I have all the information I need. Let me produce the authoritative consolidated review.

## Summary

This paper proposes Patch-DM, a patch-based denoising diffusion model for high-resolution image synthesis. The core technical contribution is a **feature collage** strategy: instead of generating independent patches or collaging in pixel space, the method operates on U-Net feature maps by splitting and recombining partial features from four neighboring patches before passing them to the decoder. This enables seamless high-resolution generation (tested up to 1024×512) using a model trained only on 64×64 patches, with significantly fewer parameters (154M full model vs. 552M for ADM). The method achieves state-of-the-art FID among patch-based methods on FFHQ (10.02), LSUN-Bedroom (6.04), LSUN-Church (5.49), and a newly collected 1024×512 nature dataset (20.37).

## Strengths

- **Feature collage demonstrably eliminates boundary artifacts.** The ablation (Table 4, Figure 6) provides clear evidence: the full feature-collage model achieves FID 37.99 (1k images) on FFHQ, substantially better than pixel-space fixed shift (49.80), pixel-space random shift (52.11), no global conditions (79.33), and no position embeddings (48.82). All ablations use the same evaluation protocol, so the relative ordering is credible.

- **State-of-the-art among patch-based methods on all four datasets.** On the nature 1024×512 dataset (Table 1), Patch-DM (FID 20.37) more than doubles Anyres-GAN (44.17). On the three 256×256 benchmarks (Table 2), it consistently beats all prior patch-based methods (COCO-GAN, InfinityGAN, Anyres-GAN) by large margins. The table transparently separates non-patch and patch-based methods using midrules and different bold/underline formatting, making the scope of the claim clear.

- **Significantly reduced model size.** The full Patch-DM uses 154M parameters vs. ADM (552M), LDM-4 (274M), and DiffAE (232M) for 256×256 generation (Table 3). The 70M variant (without semantic encoder and latent DPM) is the most compact. This directly supports the claimed memory-complexity advantage over classic diffusion models.

- **Flexible zero-shot applications.** Patch-DM performs outpainting and inpainting without any fine-tuning (Figures 7–9), and can generate beyond-training-resolution images (e.g., 2048×1024 from a 1024×512-trained model, Figure 5; 384×384 from a 256×256 model, Figure 7). These demonstrate practical flexibility beyond standard generation.

- **New high-resolution benchmark dataset.** The authors collect and release 21,443 nature images at 1024×512 resolution, providing a standardized testbed for evaluating direct high-resolution patch-based generation that was previously lacking.

## Weaknesses

### Fatal
None.

### Major

- **No diffusion baseline on the 1024×512 dataset.** The central claim is enabling direct high-resolution synthesis with patch-based diffusion, yet the only quantitative comparison on the newly collected nature dataset is against three patch-based GANs (COCO-GAN, InfinityGAN, Anyres-GAN). There is no comparison to any diffusion model operating at this resolution — not a latent diffusion model (e.g., LDM) adapted to 1024×512, nor a hierarchical approach (e.g., a base 256×256 model + super-resolution pipeline), nor even a standard U-Net diffusion model of comparable parameter count trained on downsampled versions. Without this baseline, the reader cannot assess whether Patch-DM's patch-based approach is genuinely beneficial for high-resolution synthesis or whether a standard (non-patch) diffusion model of similar size would perform comparably. This gap weakens the paper's primary contribution claim.

### Minor

- **Ablation FID uses a different evaluation protocol than main results without explanation.** The ablation (Table 5) computes FID on 1,000 images (yielding 37.99 for the full model on FFHQ), while the main results (Table 2) use 50,000 images (yielding 10.02 on FFHQ). These differ by nearly 4×, which is consistent with known FID behavior under small sample sizes, but the paper never acknowledges this discrepancy or explains why a 1,000-image protocol was used for ablations. While the internal validity of the ablation (all variants use the same 1k protocol) is preserved, the lack of comment is confusing and prevents readers from connecting the ablation numbers to the main results.

- **Feature collage split fractions are underspecified.** Equation (4) describes collaging via functions \(P_1, P_2, P_3, P_4\) that are "split functions as shown in Figure 1(c)," but the exact cropping mechanism (e.g., what fraction of each feature map is taken in each spatial dimension, how feature maps are spatially aligned, how border patches are padded) is never stated numerically. The inference description (Figure 2 caption) gives the high-level idea — "four adjacent obtained feature maps after encoding are concatenated, and a new patch in the middle with red borders is extracted" — but without dimensioned examples or pseudo-code, a practitioner cannot reproduce or adapt the core claimed contribution. This is the paper's most novel operation and it deserves explicit specification.

- **No reported memory or runtime measurements.** The paper claims reduced memory complexity compared to classic diffusion models but provides only parameter counts. Actual peak GPU memory usage and per-sample inference time (for both patch-level denoising and the full pipeline including the latent DPM) are never reported. Since Patch-DM's inference requires running multiple patches through the encoder and performing the feature collage, the practical memory savings relative to a standard U-Net operating on the full image are not empirically validated.

- **Classifier-free guidance scale not reported.** The paper reports dropout rates (0.1 for global conditions, 0.5 for position embeddings) but never states the classifier-free guidance scale (weight) used during sampling. This is a well-known hyperparameter that significantly affects the FID-diversity trade-off and should be reported for reproducibility.

- **Applications are qualitative only.** The beyond-patch-generation (2× resolution), outpainting, and inpainting sections (Figures 5, 7–9) show only qualitative results. While these are intended as demonstrations rather than core contributions, adding even a simple quantitative measure (e.g., FID on outpainted regions, or comparison to a trivial baseline) would strengthen the paper's claims about the versatility of feature collage.

### Trivial

- The ablation caption (Table 5) could more explicitly note that the FID values are computed on 1,000 images and are not directly comparable to the main Table 2 figures.

## Nice-to-Haves

- **Add a diffusion baseline on the 1024×512 dataset.** The single most valuable addition would be to adapt a latent diffusion model (e.g., LDM-4) to the nature dataset (perhaps with a VAE providing sufficient compression for 1024×512 images, or by using a super-resolution pipeline) and report FID. This would directly test the central hypothesis that patch-based training is beneficial at high resolutions.

- **Report guidance scale values** used for classifier-free guidance on global conditions and position embeddings.

- **Provide peak GPU memory and per-sample inference time** for Patch-DM vs. a standard U-Net diffusion model at both 256×256 and 1024×512 resolutions.

- **Include dimensioned examples or pseudo-code** for the feature collage operation to improve reproducibility.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism #1 (abstract overclaims SOTA):** The reviewer claims the abstract asserts SOTA against *all* methods, but the abstract states: "We compare our method with **previous patch-based generation methods** and achieve state-of-the-art FID scores on all four datasets." The qualifier is explicit. Table 2 confirms Patch-DM achieves best FID among all patch-based methods on all three 256×256 datasets, and Table 1 confirms it beats all compared (patch-based) methods on the nature dataset. The claim is accurate within its stated scope. **Removed** — stems from misreading the paper's scoping.

- **Criticism about "two-stage pipeline adds complexity undercutting the lightweight claim":** The full model is 154M vs. ADM (552M), LDM-4 (274M), and DiffAE (232M) — a genuine reduction. The 70M variant without latent DPM and semantic encoder is substantially smaller. The paper is transparent about the two-stage design (denoising U-Net + latent DPM) and the conditional generation capability without the latent DPM. The reduced parameter count *is* the evidence for reduced memory complexity, and the claim is well-supported. **Removed** — the reviewer's "not dramatically smaller" claim is contradicted by the data (154M is 44% smaller than LDM-4 at 274M).

- **Criticism about DDIM 50 vs. 1000 steps:** The paper explicitly notes: "For a fair comparison, results are reproduced in the same sampling steps as ours, using provided pretrained checkpoints of other diffusion models." The table labels each method's step count (s=N). This is standard practice and not a weakness. **Removed.**

- **Criticism about "optimizing the pre-obtained image features" being "unusual":** The paper clearly explains that CLIP embeddings are extracted and then treated as learnable parameters — this is a standard practice called embedding optimization (used in e.g., DreamBooth, textual inversion, and many GAN inversion methods). It is neither unusual nor unclear. **Removed.**

- **Strength Finder claim about feature collage being the "single most important piece of evidence" with FID 37.99:** This absolute value (37.99) uses the 1k-image protocol and is not comparable to the main results. While the relative comparison among ablations is valid, presenting this number as the primary evidence without caveat about the protocol is misleading. I preserve the relative comparison as a genuine strength but add context.

## Novel Insights

None beyond the paper's own contributions. The central insight — that applying a shifted-window collage operation in the *feature space* of a U-Net (rather than in pixel space) eliminates boundary artifacts in patch-based diffusion — is the paper's own contribution. The reviews do not reveal a deeper or alternative insight.

## Suggestions

1. **Add a diffusion baseline at 1024×512 resolution.** Even a simple latent diffusion model trained on downsampled images with a super-resolution upsampler would provide the missing comparison point for the paper's central claim.
2. **Recompute the ablation FID using the same 50K-image protocol as the main results**, or explicitly explain why the 1K-image protocol was chosen and note that the absolute values are not comparable to Table 2.
3. **Specify the exact split fractions for the feature collage.** In particular: what fraction of each feature map is taken from each of the four neighboring patches? How is padding handled for border patches? A dimensioned example or pseudo-code would suffice.
4. **Report peak GPU memory** for Patch-DM vs. a standard U-Net at both 256×256 and 1024×512 resolutions to substantiate the memory-complexity claim.
5. **Report the classifier-free guidance scale** used for both global conditions and position embeddings.
6. **Consider a simple quantitative evaluation for the outpainting/beyond-generation demos** (e.g., FID on the extended region, or comparison to a naive baseline) to strengthen the claims about flexibility.

## Score and Decision

**Originality:** The feature collage idea — applying a shifted-window mechanism in the feature space rather than pixel space for patch-based diffusion — is novel and well-motivated. **Importance:** High-resolution synthesis with compact models is an important problem. **Claims support:** The core claims (feature collage eliminates boundary artifacts, SOTA among patch-based methods, reduced model size) are supported by evidence. However, the central claim about high-resolution benefits would be substantially stronger with a diffusion baseline at 1024×512. **Soundness:** The methodology is sound; the ablations are properly controlled internally. The FID protocol inconsistency is confusing but not invalidating. **Clarity:** The feature collage description lacks precision needed for reproducibility, and the FID discrepancy is not explained. **Value:** The paper makes a useful contribution but falls short of the strongest possible form due to the missing high-resolution diffusion comparison.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>