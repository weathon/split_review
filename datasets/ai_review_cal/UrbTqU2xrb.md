- Decision: Reject
- Avg Score: 5.75
- Scores: 5, 6, 6, 6
Now I have all the information needed. Here is my consolidated review.

---

## Summary

This paper proposes the first feed-forward pipeline for clothing-disentangled 3D character generation from a single image. The approach uses a two-stage strategy: (1) a multi-part diffusion model with cross-part attention to disentangle clothing components in 2D image space, and (2) a multi-view diffusion model with a combination attention mechanism to generate multi-view images of each part, followed by feed-forward 3D reconstruction (LGM). A new dataset of 10k+ anime characters with 11 clothing combinations each is contributed. Experiments on this dataset show that the proposed modules improve disentanglement and composition quality over a Wonder3D-based baseline.

## Strengths

- **Novel two-stage disentanglement pipeline demonstrates clear improvements over independent part generation.** Table 2 (ablation) shows that the multi-part attention module raises PSNR from 22.15 to 27.52 and SSIM from 0.962 to 0.987 for 2D part disentanglement, compared to generating each part independently. Figure 4 provides visual confirmation. This is a concrete and measurable contribution.

- **Large-scale clothing-disentangled dataset with more diversity than prior work.** Section 4.1 describes a dataset of "over 10,000 character models" each with "11 distinct clothing combinations," compared to prior datasets with "fewer than 1,000" subjects. This is a tangible resource for the community.

- **The combination attention mechanism improves multi-view part composition over naive conditioning.** Table 1 shows that the proposed method achieves PSNR 27.52 vs. the Wonder3D extended baseline's 22.15 on multi-view generation. The ablation in Table 2 confirms the special condition image design helps over the variant without it.

- **Qualitative demonstrations of downstream applications (cloth transfer, animation).** Figures 6 and 7 show that the disentangled 3D representation naturally supports clothing editing and animation, which is a desirable capability not trivial to achieve with holistic reconstruction methods.

## Weaknesses

### Fatal

None.

### Major

- **A core architectural component — the "special condition image" — is never defined.** Section 3.2 states: "we propose to introduce a special condition image specifically for part combination" and "the network learns multi-view generation from input part images and part combination from special condition images." The paper never specifies what this image is: the original input clothed character? A composite of the disentangled part images? A learned embedding? The entire combination mechanism (and the ablation that shows it helps vs. without it) rests on this undefined concept. This is a genuine reproducibility gap that prevents evaluation of the method's rationale and limits its utility to the community.

- **No quantitative evaluation of the output 3D models.** The paper claims to generate clothing-disentangled *3D* characters, but all quantitative metrics (PSNR, SSIM, LPIPS) are computed on rendered *2D multi-view images* of individual parts. There are no 3D geometric metrics (Chamfer distance, normal consistency, volumetric IoU) for the reconstructed 3D models of each part or the combined character. The 3D part model composition optimization (Section 3.3, Eq. 3) is only shown qualitatively in Figure 5 (right). Without 3D evaluation, it is unclear whether the multi-view→3D reconstruction step preserves the disentanglement quality and geometric accuracy that the 2D stage claims to provide.

- **The central efficiency claim ("hours to mere seconds") is unsubstantiated.** The paper repeatedly frames its contribution as being dramatically faster than optimization-based methods (lines 14, 27, 45), yet it reports zero runtime measurements for its own pipeline and provides no timing comparison against any prior method. The only concrete number is that LGM reconstructs each part "in 1 second" (line 87), but total pipeline time (2D disentanglement + multi-view generation for N parts + combination + reconstruction) is never given. A central claim lacks supporting evidence.

- **The baseline comparison is insufficient to support the paper's framing.** The only baseline is a single method (Wonder3D augmented with part-type conditioning). Since the paper positions itself against optimization-based approaches, some comparison (even qualitative or with limited scope) against a representative optimization-based clothing-disentanglement method would be needed to validate the claimed advantage. The current baseline only demonstrates that the proposed two-stage approach outperforms a naive single-stage conditional approach, which is a low bar.

### Minor

- **Missing ablation variants weaken the analysis of the combination attention module.** The ablation (Table 2) only compares with vs. without the special condition image. Two informative missing variants: (a) no combination attention at all (generate multi-views per part separately, reconstruct 3D parts, then combine in 3D), which would isolate the benefit of learning combination in diffusion space vs. post-hoc 3D alignment; (b) using the original input image instead of the undefined "special condition image" in the combination attention.

- **Only 4 views are rendered for the multi-view dataset (Section 4.1).** Many multi-view reconstruction methods use 6–8 views; no justification is given for this choice. This may limit reconstruction quality, especially for complex clothing geometries.

- **"Feed-forward" terminology is slightly imprecise.** The diffusion models in Stages 1 and 2 involve iterative denoising (50–100 steps), not a single forward pass. The paper's actual distinction from prior work is that it avoids per-scene (SDS-based) optimization. The claim would be better framed as "no per-scene optimization" rather than "feed-forward."

- **No standard deviations or significance tests reported** for the quantitative metrics in Tables 1 and 2.

- **Failure modes are not discussed.** The limitations section (4.6) acknowledges dataset size and lack of dynamic clothing but does not discuss cases where the method would be expected to struggle (e.g., complex poses, heavy occlusion, similar colors across parts, small accessories).

### Trivial

None.

## Nice-to-Haves

- Provide per-stage runtime breakdown (2D disentanglement, multi-view generation per part, combination, 3D reconstruction) and compare against at least one optimization-based method.
- Compute 3D metrics (Chamfer distance, F-score, volumetric IoU) on the test set against ground truth 3D models.
- Add an ablation that removes the combination attention entirely (post-hoc 3D assembly only).
- Clarify the "special condition image" and consider an ablation that replaces it with the original input image.
- Show failure cases (e.g., loose garments, occluded parts) to characterize the method's limitations.
- Report standard deviations for all quantitative results.

## Removed Points

- **Criticism that the paper should compare against GALA specifically** (from Harsh Critic, Critical Issue 1). GALA (Kim et al. 2024) takes a single-layer clothed 3D mesh as input, not a 2D image, so the input modalities are fundamentally different. The general point about missing comparison with optimization-based methods is retained in Major above. This specific suggestion is removed as not applicable to the paper's stated task.
- **Criticism about multi-part attention complexity scaling (Harsh Critic, Section-by-Section)**. The paper uses N=4 parts, so quadratic scaling in the attention key/value lengths is not a practical concern. This is a technical nitpick without consequence for the presented work.
- **Strength Finder: "First feed-forward method... seconds-level runtime."** This is the paper's own claim, not a verified strength, since no runtime data is provided. It is retained as context in the Summary but removed as a "strength" since it remains unsubstantiated.
- **Strength Finder: "Optional 3D optimization improves rendering quality."** Kept but downgraded — the evidence is purely qualitative (one visual example in Figure 5, right). It is referenced in Minor weaknesses as needing more validation.

## Novel Insights

None beyond the paper's own contributions. The harsh critic identifies genuine evaluation gaps but does not surface any methodological insight that the paper itself misses. The strength finder confirms the paper's stated contributions without adding new perspective.

## Suggestions

1. **Define the "special condition image" explicitly.** This is the single most important fix for reproducibility. State what it is (the original input? a masked composite? a learned token?) and include a figure or pseudocode showing how it enters the combination attention.
2. **Add 3D evaluation metrics** (Chamfer distance, normal consistency, or volumetric IoU) on the test set against ground truth 3D models, for each part and the combined character.
3. **Report total inference runtime** with a breakdown per stage, and include at least one timing comparison against an optimization-based method (even on a single example).
4. **Add the missing ablation variant** that removes the combination attention entirely and assembles parts directly in 3D via the optimization from Section 3.3, to quantify the contribution of image-space combination.
5. **Include failure case analysis** — at least 2–3 examples where the method performs poorly, with discussion of why.
