I now have a complete understanding of the paper. Let me write the consolidated review.

## Summary

The paper introduces a method for camera-controlled novel view synthesis from a single image that combines a 3D-free inference-time optimization (HawkI-style) with weak 3D priors from a pretrained NVS model (Zero123++). The approach does not require training on 3D datasets. A regularization term aligns the optimized CLIP embedding with a text embedding encoding target elevation/azimuth angles, and the method is evaluated on synthetic and real complex scenes across four viewpoints.

## Strengths

- **Effective integration of 3D priors into 3D-free optimization for camera control**: The method demonstrably achieves viewpoint transformations at specified azimuth/elevation angles on complex, in-the-wild scenes (e.g., Eiffel Tower with Seine River background, pyramid with shadows) that both pure 3D-free methods (HawkI) and pure 3D-based methods (Zero123++, Stable Zero123) struggle with. This is evidenced by consistent qualitative improvements in Figures 5–6 where competitive methods fail to capture correct viewpoints or background details.

- **Quantitative superiority over both 3D-based and 3D-free baselines**: In Table 1, the proposed method achieves the best LPIPS, CLIP score, DINO, CLIP-I, PSNR, and SSIM across the vast majority of metric–dataset–angle combinations. For instance, on HawkI-Real (30°,270°) the method improves LPIPS by 0.0347 over HawkI (the next best) and CLIP score by 1.50.

- **Regularization loss consistently improves most metrics in ablation**: Table 2 shows that adding \(L_{reg} = \|e_{view} - e_{target}\|^2\) improves performance on 51 out of 56 metric–dataset–angle combinations (across all 8 viewpoint/dataset settings × 7 metrics). While improvements are modest in magnitude, the direction is highly consistent, supporting the claimed benefit of the regularization term.

- **Data efficiency via inference-time optimization**: The method requires no additional 3D data, multi-view data, or fine-tuning; it operates purely with off-the-shelf pretrained components (Stable Diffusion 2.1, Zero123++) and a lightweight inference-time optimization, contrasting with fully-supervised NVS methods that require large-scale 3D training datasets.

## Weaknesses

### Fatal

None.

### Major

- **No metric that directly measures camera-angle correctness**: The paper's primary claim is camera-controlled novel view synthesis at specified angles, yet none of the seven reported metrics (LPIPS, CLIP score, DINO, SSCD, CLIP-I, PSNR, SSIM) directly evaluate whether the generated image corresponds to the commanded camera angle. They compare against a ground-truth image at the target angle, which provides an *indirect* signal — but a model that produces a blurry or incorrect viewpoint could still obtain non-trivial scores. Critically, the **View-CLIP Score** is mentioned in the text (line 177) as a metric that "focuses specifically on the viewpoint," but it is never reported in any table. This is the most significant gap in the evaluation. Without a direct measure of angular accuracy (e.g., pose estimation error, angular classification accuracy, or at minimum the View-CLIP Score promised in the paper), the central claim is not fully substantiated by the quantitative evidence.

### Minor

- **The regularization loss mechanism is not analyzed**: The paper assumes that minimizing \(\|e_{view} - e_{target}\|^2\) meaningfully injects angle information into the diffusion process, but it provides no analysis of whether (a) \(e_{target}\) for different angles is discriminable in CLIP space, (b) the optimized \(e_{view}\) actually moves toward angle-specific regions of the embedding space, or (c) the improvement arises from the specific angle content versus generic embedding regularization. The ablation shows the loss helps, but the *why* is unexplained. A simple control experiment (e.g., replacing \(e_{target}\) with a random unrelated text embedding) would help clarify the specificity of the effect.

- **Improvements in ablation are modest and occasionally inconsistent**: While the regularization term improves most metrics, the gains are small (e.g., LPIPS from 0.5867→0.5661 on HawkI-Syn (30°,30°), which is a ~3.5% relative improvement). Moreover, in 5 out of 56 metric–angle combinations, the unregularized version performs better (e.g., DINO on HawkI-Real (-20°,210°): 0.3817 vs. 0.3610 with regularization). The paper does not discuss or explain these regressions.

- **The analysis of CLIP's 3D understanding (Section 3) is basic**: The two experiments show expected results (CLIP without guidance fails; incorrect guidance dominates output). These observations motivate the method but do not constitute a deep analysis. The paper would benefit from more rigorous probing of what angle information CLIP embeddings actually encode.

- **Mutual information guidance is cited but not explained**: The inference step uses "mutual information guidance" borrowed from HawkI (line 127), but the paper does not describe what this entails. Since this component likely contributes to the final results, the reader cannot fully assess where the performance gains come from.

### Trivial

- The paper describes "evaluate our method using six metrics" on line 177 but then enumerates eight metric names (LPIPS, CLIP-Score, View-CLIP Score, DINO, SSCD, CLIP-I, PSNR, SSIM), and View-CLIP Score is never reported. This is inconsistent.

## Nice-to-Haves

- **Runtime/efficiency reporting**: The optimization requires ~1,750 iterations per viewpoint (1,000 for text embedding on input + 500 for UNet on input + 500 for text embedding on view + 250 for UNet on view, plus 50 inference steps). A runtime comparison against baselines would help contextualize the practical trade-offs. The paper acknowledges this limitation (line 271) but provides no quantification.

- **Testing on standard NVS benchmarks** (e.g., RealEstate10K, LLFF) would strengthen claims of generalizability beyond the HawkI-derived datasets.

## Removed Points

These points were flagged by reviewers but are removed after cross-checking against the paper:

1. **"The baseline comparison with HawkI is unfair because HawkI is designed for aerial views"** — The paper explicitly states that HawkI is a 3D-free method that "struggles with controlling camera angles" (line 41). Evaluating HawkI on non-aerial camera control tasks is a direct comparison on the paper's own problem setting. This is not unfair; it demonstrates a known limitation of existing 3D-free methods that the proposed approach aims to address.

2. **"Calling the approach '3D-free' is imprecise"** — The title is "3D-free meets 3D priors." The paper is transparent that it uses a pretrained 3D NVS model for weak guidance while the optimization framework itself requires no 3D training data. This framing is accurate, not misleading.

3. **"No details about number of scenes or view diversity in datasets"** — The datasets (HawkI-Syn, HawkI-Real) are cited from prior work. Providing full dataset statistics in the paper is not standard practice when datasets are established and published.

4. **"The analysis in Section 3 is not comprehensive"** — The two controlled experiments serve their stated purpose: motivating the need for accurate 3D guidance. Their simplicity does not invalidate their usefulness for the paper's argument.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Report the View-CLIP Score** — The paper already mentions this metric and defines it as focusing on viewpoint alignment. Adding it to Table 1 would directly address the most critical evaluation gap.

2. **Add a direct angle-accuracy metric** — Even a simple evaluation using an off-the-shelf pose estimator (e.g., COLMAP or a learned relative pose regression model) to compute angular error between generated and ground-truth views would strengthen the central claim substantially.

3. **Include a control experiment for the regularization** — Replace the angle-specific text embedding \(e_{target}\) with a non-angle text embedding (e.g., "a photo") to test whether the benefit of \(L_{reg}\) is specific to angle information or is just a generic embedding regularizer.

4. **Analyze the discriminability of angle text embeddings** — Measure whether CLIP text embeddings for different angle descriptions (e.g., "+30 degrees" vs "+45 degrees") are distinguishable, and whether \(e_{view}\) moves toward the correct one during optimization.

## Score and Decision

The paper presents a well-motivated approach that combines the complementary strengths of 3D-free and 3D-based methods for camera-controlled NVS. The qualitative results are compelling, and the quantitative results show consistent improvements over strong baselines across nearly all reported metrics. The main weakness is the absence of a direct camera-angle accuracy metric in the evaluation — the View-CLIP Score is mentioned but never reported. This gap is addressable but non-trivial, as it leaves the paper's central claim supported only by indirect evidence. The method itself is sound and the contribution is clear.

Based on the paper's originality (integration of 3D priors into 3D-free optimization), importance (data-efficient camera control without 3D training data), experimental support (strong but missing a direct angle metric), and clarity (well-structured, though the mechanism analysis is shallow), the paper merits acceptance after addressing the evaluation gap.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>