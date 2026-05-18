Now I have all the information I need. Let me write the consolidated review.

---

## Summary

This paper proposes LRM (Large Reconstruction Model), a 500M-parameter transformer-based framework that predicts a triplane-NeRF 3D representation from a single input image in under 5 seconds. The model is trained end-to-end on approximately 1 million objects (synthetic from Objaverse and real from MVImgNet) using only image reconstruction losses (MSE + LPIPS). The key architectural innovation is an image-to-triplane transformer decoder that uses cross-attention from learnable triplane tokens to DINO image features, modulated by camera parameters. The paper demonstrates compelling qualitative results across diverse input types (real photos, rendered images, AI-generated images) and shows visible improvement over the concurrent One-2-3-45 method.

## Strengths

- **Ambitious scale and clean architecture**: The model trains on ~1M objects (730K Objaverse + 220K MVImgNet) with 500M parameters across 128 A100 GPUs — substantially larger than prior single-image-to-3D methods. The architecture is fully transformer-based and end-to-end differentiable, with no per-shape optimization or 3D-specific regularization needed (Sec. 3, Sec. 4.1-4.2).

- **Practical inference speed**: The feed-forward pipeline produces a complete 3D mesh in under 5 seconds on a single A100 GPU, with a clear time breakdown provided (1.14s image-to-triplane, 1.14s NeRF querying, 1.91s marching cubes; Sec. 1 footnote, Sec. 4.2). This makes the method genuinely practical for downstream applications.

- **Visually compelling results across diverse inputs**: Figure 2 shows high-fidelity reconstructions from real-world captures, rendered objects, and AI-generated images, none seen during training. The model reconstructs both complex geometry (flower, flagon) and fine textures (wood peafowl), and infers plausible occluded regions (giraffe, penguin). Figure 3 shows noticeably sharper textures and more consistent geometry than the concurrent One-2-3-45 on that method's own published examples, using those examples specifically to avoid cherry-picking (Sec. 4.3.1).

- **Well-motivated design choices**: The use of DINO (rather than CLIP) as the image encoder is justified by its retention of structural and texture information needed for 3D reconstruction (Sec. 3.1). The camera modulation via adaptive layer norm (Sec. 3.2) and camera normalization (Sec. 4.2) are sensible design choices that reduce the optimization space. The cross-attention design allows the model to learn 2D-to-3D correspondence without explicit spatial alignment (Sec. 3.2).

- **Simple, scalable training objective**: Training uses only pixel-wise MSE and LPIPS loss between rendered and ground-truth views (V=4 per object), avoiding complex 3D-aware regularizations, diffusion guidance, or adversarial losses that would hinder scalability (Eqn. 1, Sec. 4.2).

- **Well-written and clearly described**: The architecture, data pipeline, and training setup are presented with sufficient detail for understanding and approximate reproduction.

## Weaknesses

### Fatal

None.

### Major

- **Complete absence of quantitative evaluation**: The paper claims to produce "high-quality 3D reconstructions" and to be "highly generalizable," but provides zero quantitative metrics to support these claims. No 2D rendering metrics (PSNR, SSIM, LPIPS on held-out views), no 3D geometry metrics (Chamfer distance, IoU), and no systematic comparison against any baseline beyond a few hand-selected qualitative examples. This is particularly problematic because the paper explicitly states in Sec. 4.1 that they acquired 50 unseen shapes from Objaverse and 50 from MVImgNet "to numerically study the design choices" — yet no such numerical study appears anywhere in the manuscript. The qualitative results are compelling but do not substitute for quantitative evidence. This is the single most significant gap in the paper and prevents readers from assessing whether the claimed generalization and quality hold on average, beyond the curated examples shown.

- **No ablation studies to support the scaling thesis**: The paper's motivating question (Sec. 1) is whether scaling data and a simple transformer architecture yields a generic 3D prior. Yet no experiments vary model size, training data volume, triplane resolution, number of transformer layers, or the choice of image encoder. The reader cannot tell whether the observed visual quality is due to scale, architecture, or the DINO encoder alone — and cannot judge whether a smaller, cheaper model would perform similarly. For a paper whose central framing is about scaling, the absence of any scaling-curve analysis is a significant gap.

### Minor

- **Inference-time camera assumption is acknowledged but unquantified**: At inference, the method assigns a fixed normalized camera pose (from the Objaverse training distribution) to every input image. The paper acknowledges this can cause distortion (Sec. 4.3.2, Fig. 4) but provides no quantitative measurement of how severely this assumption degrades reconstruction quality when violated. A sensitivity analysis (e.g., measuring reconstruction error as a function of true-camera deviation from the assumed pose) would substantially strengthen the failure-case discussion. That said, the paper does honestly surface this as a limitation, so this does not rise to major.

- **Comparison limited to a single baseline**: The only comparison is against One-2-3-45 (Fig. 3). While the paper's effort to use that baseline's own published examples is commendable, a broader comparison against other relevant methods (e.g., a per-shape NeRF baseline, Zero-1-to-3 which is discussed in related work, or a smaller version of LRM) would better contextualize the results. The comparison is also purely qualitative.

- **Background removal artifacts unexamined**: The MVImgNet pipeline uses an off-the-shelf background remover (Rembg, Sec. 4.1). While the paper is transparent about this, any artifacts introduced by imperfect background removal are neither measured nor discussed.

### Trivial

None of substance.

## Nice-to-Haves

- Joint camera estimation or test-time camera adaptation would address the distortion problem noted in Sec. 4.3.2 and is suggested as future work, but a preliminary experiment in this paper would strengthen it.
- Visualizing or probing the learned triplane features could provide insight into whether the model learns a structured 3D representation.
- A systematic failure-mode gallery with a breakdown of cause (camera mismatch, occlusion, ambiguous geometry) would improve the limitations analysis.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"The paragraph on multimodal 3D feels tangential"**: The Multimodal 3D paragraph (Sec. 2, lines 51-56) situates the paper within broader trends of multimodal learning and mentions concurrent works. It is a reasonable related-work subsection, not a weakness. This is a stylistic preference, not a substantive flaw.

- **"The authors position themselves against concurrent works like Cap3D and 3D-LLM without needing to"**: The paper merely *mentions* these as related concurrent work in a single paragraph; it does not position against them. This is a misreading. Removed.

- **Demand for comparison against Zero-1-to-3 with metric depth, CO3D benchmarks, etc.**: The paper's stated scope is single-image-to-3D object reconstruction using a feed-forward model trained on Objaverse-scale data. While additional baselines would strengthen the paper, demanding specific benchmarks and comparisons that go beyond the paper's framing is scope creep. Weakened to the minor point above about limited comparison.

- **"The introduction... never answers that question empirically; it merely shows pictures"**: This is addressed substantively in the Major weakness about no quantitative evaluation and no scaling ablations. The framing is not independently a weakness — it's a symptom of the same underlying gap.

## Novel Insights

The paper's genuinely novel insight — which subsequent work has validated — is that a simple transformer decoder with cross-attention from triplane tokens to image features, combined with camera modulation and trained at massive scale on Objaverse, can learn a surprisingly effective 2D-to-3D mapping without any explicit geometric alignment, 3D supervision, or diffusion guidance. The idea that 3D can be treated as "just another modality" for cross-attention, and that the resulting model can produce usable 3D in a single feed-forward pass, was ahead of its time and has proven influential. The specific design choice of DINO over CLIP for structural detail preservation is also a non-obvious and consequential architectural decision.

## Suggestions

1. **Add quantitative evaluation** — this is the single most important improvement. Even a modest set of PSNR/SSIM/LPIPS numbers on the 50+50 held-out objects already collected would transform the paper's credibility. Include 3D metrics (Chamfer distance, IoU) on extracted meshes.
2. **Add scaling ablations** — train smaller variants (e.g., 125M, 250M parameters) and/or train on data subsets (10%, 50%) to directly test the scaling hypothesis posed in the introduction.
3. **Add a sensitivity analysis for the camera assumption** — measure how reconstruction quality degrades as the true camera deviates from the assumed canonical pose, to quantify the practical severity of this limitation.
4. **Include at least one additional baseline** beyond One-2-3-45, even a simple one such as per-shape triplane optimization or a reduced-capacity LRM variant.

## Score and Decision

### Anchor Comparison

| Anchor | Avg Score | Comparison to LRM |
|--------|-----------|-------------------|
| NeuralPlane (`/home/wg25r/split_review/datasets/deepreview_13k_calibration/5UKrnKuspb.md`) | 8.00 | Far stronger: thorough quantitative evaluation on multiple benchmarks, extensive ablations, clear SOTA claims. LRM is clearly below this tier. |
| PRM (`/home/wg25r/split_review/datasets/deepreview_13k_calibration/AkL2ID5rRV.md`) | 6.25 | Stronger: has quantitative evaluation and comparisons. LRM is below this level due to absence of metrics. |
| GTR (`/home/wg25r/split_review/datasets/deepreview_13k_calibration/Oxpkn0YLG1.md`) | 5.60 | Builds directly on LRM, adding quantitative evaluation and ablations. LRM itself — lacking those — should score somewhat lower. |
| Hi-Gaussian (`/home/wg25r/split_review/datasets/deepreview_13k_calibration/L3WnnnBRdu.md`) | 5.75 | Has evaluations but was still rejected. LRM's qualitative-only approach ranks below this. |
| Long-LRM (`/home/wg25r/split_review/datasets/deepreview_13k_calibration/meOELl7HRf.md`) | 5.33 | Similar LRM-based approach, also rejected. |
| SCoRF (`/home/wg25r/split_review/datasets/deepreview_13k_calibration/ESmvnmZ9fT.md`) | 4.33 | Limited evaluation scope. LRM has stronger vision/scale but similarly incomplete evaluation. |
| studentSplat (`/home/wg25r/split_review/datasets/deepreview_13k_calibration/fRXAQfHlmr.md`) | 4.25 | Has experiments but limited. LRM somewhat above this due to scale and vision. |
| GeoGS3D (`/home/wg25r/split_review/datasets/deepreview_13k_calibration/I86z54CL2y.md`) | 3.40 | LRM is clearly stronger — better architecture, scale, and qualitative evidence. |
| PointRecon (`/home/wg25r/split_review/datasets/deepreview_13k_calibration/3JfvvuPXsH.md`) | 3.50 | LRM is stronger in ambition and visual evidence. |
| Scaled Inverse Graphics (`/home/wg25r/split_review/datasets/deepreview_13k_calibration/GSckuQMzBG.md`) | 3.00 | LRM is much stronger — better framing, scale, and results. |

**Positioning**: LRM sits between the ~4.0-4.5 tier (papers with interesting ideas but incomplete evaluation) and the ~5.3-5.6 tier (LRM-based papers that added quantitative evaluation). The paper has a genuinely novel and influential architecture, impressive scale, and compelling qualitative results. However, the complete absence of quantitative evaluation — despite the paper explicitly collecting data for such a study — is a significant gap that prevents core claims from being scientifically verifiable. The paper reads more like a strong tech report / proof-of-concept than a fully evaluated scientific contribution.

This is not a fundamentally broken or worthless paper (the architectural contribution is real and proved influential), but the evaluation gap is substantial enough to place it below the acceptance threshold for venues that require rigorous empirical validation.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>