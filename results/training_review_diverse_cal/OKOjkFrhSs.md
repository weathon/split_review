Now I have all the information needed. Let me write the consolidated review.

## Summary

This paper proposes a Prompt-Guided Dynamic Network (PDN) for single image super-resolution that introduces multi-modal prompts (text or image) via a Dynamic Correlation Module (DCM). The DCM consists of two components: a Spatially Multi-Modal Attention Module that highlights prompt-relevant spatial regions, and a Prompt-Guided Dynamic Convolution Module that generates convolution kernels conditioned on prompt embeddings from CLIP. The module is designed as a plug-and-play component and is integrated into EDSR, RDN, and RCAN, achieving PSNR gains of up to 0.51 dB.

## Strengths

- **Novel mechanism for incorporating multi-modal prompts into SR**: The paper is the first to use prompt embeddings (from CLIP) to guide dynamic convolutional kernel estimation for SR. This goes beyond prior guided-SR methods (e.g., TGSR) by conditioning the kernel weights themselves on the prompt, rather than only using attention. The idea is validated by ablation results showing that removing either sub-module degrades performance (Table 4: EDSR+ w/o att drops from 25.76 to 25.56 PSNR on Urban100; EDSR+ w/o dy drops to 25.69).

- **Consistent quantitative gains across three SR architectures**: When integrated into EDSR, RDN, and RCAN, DCM improves PSNR by 0.11–0.51 dB and SSIM by 0.009–0.02 across all tested datasets (Table 3). The improvements are consistent, not cherry-picked from a single architecture.

- **Ablation studies confirm both sub-modules contribute**: Table 4 shows that removing either the attention module or the dynamic convolution module hurts performance on both Urban100 and CelebA-HQ, supporting the design rationale that both components are necessary. The attention visualizations (Figures 4 and 5) further show qualitative alignment between prompt semantics and highlighted regions.

- **Generality demonstrated**: The method is evaluated with both text prompts (on COCO) and image prompts (on FFHQ and non-annotated benchmarks), showing that DCM can work with either modality coming from CLIP's shared embedding space.

## Weaknesses

### Fatal

None.

### Major

1. **No control for added capacity — gains cannot be cleanly attributed to prompt information.** The DCM adds parameters and additional operations. The baselines (EDSR, RDN, RCAN) do not match this added capacity. The ablation in Table 4 removes sub-modules but still uses the prompt embedding, and the replacement for "w/o dy" is standard convolution (fewer parameters). Without a control that adds equal parameters *without* prompt conditioning (e.g., an equally sized feed-forward block, or a standard dynamic convolution conditioned on image features), the observed gains could partly or wholly reflect extra model capacity rather than semantic information from the prompt. This gap undermines the paper's central claim that *multi-modal prompts* drive the improvement.

2. **The dynamic convolution advantage is asserted without supporting evidence.** The paper claims that conventional dynamic convolution in SR produces "averaged" kernels with little diversity across samples (citing Chen et al., 2021), and that prompt-derived weights prevent this collapse due to higher variance. This claim is central to the motivation for prompt-guided dynamic convolution, but the paper provides no empirical analysis — no kernel similarity measurements, no effective rank or variance of combined kernels, and no direct comparison to a dynamic convolution conditioned on image features. The Remark in Section 3.3 asserts this as a motivation but validates it only via end-task metrics, which conflate multiple factors.

3. **Domain shift between training and evaluation prompt modalities is unaddressed.** The model is trained on COCO with text prompts but evaluated on Set5, Set14, Urban100, and CelebA-HQ using image prompts (horizontal flips of the LR input). Table 3 reports these results without discussing whether CLIP text and image embeddings have different statistical properties, how the DCM behaves under this mismatch, or whether the gains on these benchmarks might differ if text prompts were used. While CLIP projects both modalities into a shared space, the distributional difference is non-trivial and should be analyzed.

### Minor

1. **No complexity analysis despite claiming the module is "lightweight."** The paper states DCM is "lightweight" (Section 3.3) but provides no FLOPs, parameter counts, or runtime comparison with the baselines. For a plug-and-play module targeting practical use, this is a meaningful omission.

2. **Trade-off with per-word approaches not acknowledged.** The paper criticizes TGSR for using per-word embeddings that "neglect the relationship between words," but the proposed Spatially Multi-Modal Attention Module uses a single global prompt embedding, which loses word-level detail. Neither approach is clearly superior, and the paper does not acknowledge this trade-off.

3. **The paper does not discuss how text vs. image prompts are handled at test time.** Are the same DCM parameters and temperature/scaling factors used for both modalities? Given that CLIP text and image embeddings have different statistical distributions, this should be clarified.

### Trivial

- Citation error: Section 4.2 says "From Figure 1, we see…" when discussing visual comparison results, but Figure 1 is the network diagram; the reference should be to Figure 3 (the visual comparison).

## Nice-to-Haves

- Replace the prompt embedding with a random vector or learned constant embedding to quantify how much of the gain comes from semantic information vs. a fixed conditioning signal.
- Compare prompt-guided dynamic convolution against a standard dynamic convolution conditioned on image features (rather than prompt), to validate the claimed advantage of prompt-derived kernel diversity.
- Report standard deviations or confidence intervals for the main results, especially given that gains are sometimes as small as 0.11 dB.
- Provide kernel similarity analysis (e.g., effective rank, variance across samples) to support the claim that prompt embeddings prevent kernel collapse in conventional dynamic convolution.

## Removed Points

- **Point about unfair comparison with other methods**: The harsh critic's concern about unfair comparison was checked; the asymmetry favors baselines (no extra parameters), so this is not a weakness. Removed.
- **Point questioning whether the approach is "multi-modal" because most benchmarks use image prompts**: This mischaracterizes the paper — the method does use both text (COCO) and image (FFHQ/benchmarks) prompts, which is genuinely multi-modal. The underlying concern about domain shift is kept in Major above, but the framing that this "is not multi-modal" is factually incorrect and removed.
- **Suggestions that are practically infeasible**: None identified from the reviewer's suggestions — all suggested experiments are feasible for an academic team.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a standard but important methodological gap (capacity confounding) and an unsubstantiated claim (kernel diversity from prompts), but do not add a fundamentally new perspective that the paper itself lacks.

## Suggestions

1. Add a controlled experiment matching the DCM's added parameters with a non-prompt-conditioned module (e.g., an extra residual block or a standard dynamic convolution conditioned on image features). This is the single most important experiment needed to validate the paper's central claim.
2. Provide empirical evidence for the claimed kernel diversity advantage — measure effective rank or variance of combined kernels from prompt-guided vs. image-guided dynamic convolution.
3. Separate results by prompt modality on the same benchmark (e.g., COCO val with text prompts vs. image prompts) to isolate the effect of text guidance.
4. Report FLOPs and parameter counts for DCM and each upgraded network.
5. Fix the Figure 1→Figure 3 citation error.

## Score and Decision

The paper introduces a genuinely novel architectural idea and shows consistent positive results. However, the central claim — that multi-modal prompts drive the improvements — is not adequately supported because no equal-capacity baseline without prompt conditioning is tested, and the dynamic convolution motivation is asserted without direct evidence. These are substantive gaps that prevent clean attribution of the gains. The paper would benefit from major revisions to address these issues. In its current form, I cannot recommend acceptance.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>