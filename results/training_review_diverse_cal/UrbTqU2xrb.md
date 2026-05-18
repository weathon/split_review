Now I have all the evidence needed. Let me synthesize the review.

---

## Summary

This paper proposes the first feed-forward method for clothing-disentangled 3D character generation from a single image. It introduces a two-stage pipeline: a multi-part diffusion model for 2D component disentanglement with cross-part attention, followed by a multi-view diffusion model with a novel combination attention mechanism to generate multi-view images for each part. Off-the-shelf feed-forward reconstruction (LGM) converts these to 3D Gaussians, with an optional alignment step. The authors also contribute a large dataset of >10,000 disentangled anime characters. The 2D multi-view image results (PSNR/SSIM/LPIPS) show clear improvement over an adapted Wonder3D baseline.

## Strengths

1. **First feed-forward framework for clothing-disentangled 3D generation.** The paper demonstrates a genuine paradigm shift from optimization-based methods (hours per character) to a pipeline that can operate in seconds, as substantiated by the abstract, introduction, and the use of LGM for reconstruction. The approach is well-motivated and addresses a real bottleneck in the area.

2. **Multi-part attention mechanism for 2D component disentanglement.** The cross-part attention module that enables information exchange among clothing components is a technically sound contribution. Table 2 provides direct quantitative evidence: without multi-part attention, PSNR for the body drops from 24.63 to 22.67, and SSIM drops from 0.9711 to 0.9603. Figure 4 confirms qualitatively that the module produces cleaner, more complete part images with fewer artifacts.

3. **Combination attention mechanism with special condition image.** Incorporating part composition directly into the multi-view diffusion model (rather than using a separate combination network) is an elegant design that reduces pipeline complexity. Table 1 shows the proposed approach outperforming the adapted Wonder3D baseline across all metrics (e.g., PSNR 25.81 vs 24.49 for body, LPIPS 0.039 vs 0.096 for body). The ablation confirms the special condition image is key to the improvement.

4. **Large-scale clothing-disentangled dataset.** The dataset of >10,000 anime characters (with 11 clothing combinations each, totaling >110,000 unique configurations) is a significant resource that far exceeds existing alternatives (<1,000 subjects). This enables training data-hungry diffusion models and will be valuable to the community.

## Weaknesses

### Major

1. **No quantitative evaluation of the final 3D output.** The paper's title and core claim concern "3D character generation," yet every quantitative metric (PSNR, SSIM, LPIPS in Tables 1, 2) evaluates only the intermediate multi-view 2D images. No 3D metric—Chamfer distance, volumetric IoU, FID of rendered novel views from reconstructed 3D models, or any disentanglement-specific 3D measure—is reported for the reconstructed 3D Gaussians. The dataset contains ground-truth 3D meshes, so this evaluation is feasible. Without it, the reader cannot judge whether the method actually produces usable, geometrically accurate, and properly separated 3D models, or whether reconstruction errors, interpenetration, or missing geometry undermine the claimed 3D contribution. The qualitative 3D results (Figures 5–7) are helpful but insufficient to close this gap.

2. **Insufficient baseline comparison.** The only baseline is Wonder3D adapted with a part-type condition. While this shows the proposed components improve over a direct extension of an existing method, it does not contextualize the claimed speed/quality trade-off against the optimization-based approaches the paper positions itself against (e.g., SDS-based multi-layer avatar models like GALA). The abstract claims "reducing the process from several hours to mere seconds," but no optimization-based method is included in any comparison—qualitative or quantitative. A reader cannot tell whether the feed-forward advantage comes at a severe quality cost. Additionally, a stronger feed-forward baseline (e.g., SAM+part-classifier segmentation followed by independent multi-view generation) would better isolate the value of the multi-part attention and two-stage design.

3. **Runtime not reported for the full pipeline.** The paper claims "seconds" (abstract, Section 3) and mentions LGM runs "in 1 second," but no end-to-end timing breakdown is provided: time for 2D disentanglement, multi-view generation (for all parts), reconstruction, and the optional alignment optimization. Given that efficiency is a central selling point, this omission weakens the paper's empirical support for its speed claims.

### Minor

1. **The "optional" 3D alignment optimization lacks runtime and impact analysis.** Section 3.3 introduces a per-instance optimization to align part 3D models (solving for rotation, translation, scale via rendering consistency). While labeled optional and compared against in Figure 5 (right), the paper does not report how long this optimization takes or systematically ablate how much it contributes to final 3D quality. The qualitative comparison shows improvement, but without quantitative 3D metrics, the necessity of this step for acceptable results remains unclear.

2. **Ablation of the two-stage design is missing.** The paper proposes a two-stage pipeline (2D disentanglement first, then multi-view generation). A valuable ablation would compare generating disentangled multi-view images directly (without the separate 2D stage) versus the proposed approach, to validate the key architectural choice.

### Trivial

- None.

## Nice-to-Haves

- A comparison with at least one optimization-based disentanglement method (e.g., GALA or a text-driven multi-layer SDS baseline adapted to image input) in terms of quality vs. runtime would substantially strengthen the paper.
- An ablation using a separately trained combination network (as in prior 2D composition work) versus the proposed combination attention would better justify the "reduced complexity" claim.
- Evaluating the method on real-world (non-anime) images, even as a small qualitative study, would clarify the generality of the approach beyond the anime domain.

## Removed Points

These points were identified in the inputs but are removed or downgraded after verification against the paper:

- **"The feed-forward claim is undermined by the optional 3D optimization"** — The paper explicitly labels this optimization "optional" (Sections 3, 3.3) and shows results both with and without it (Figure 5, "Single GS" vs. optimized). The optimization only adjusts rotation/translation/scale (6+3 parameters per part), not full geometry, and is presented as a refinement, not a necessity. The core feed-forward claim (generating per-part 3D models in seconds without per-scene optimization) holds without this step. Downgraded from Major to Minor (covered above as Minor #1).
- **"Domain restriction not indicated in title/abstract"** — The abstract states the dataset "focusing on anime characters." The paper is transparent about this scope. A title-level domain specification would be nice but is not a weakness.
- **"Missing related works"** — The paper has an extensive related work section covering clothed human modeling and diffusion-based 3D generation. No substantive gaps were identified.
- **"Weakness about missing appendix/references/proofs"** — Parser artifacts; these exist in the original submission.

## Novel Insights

The harsh critic raises two structural issues that, together, point to a deeper pattern: the paper evaluates what it is easiest to evaluate (2D image metrics) rather than what it claims to contribute (3D disentangled models). The 2D metrics demonstrate that the multi-part attention and combination attention modules work as designed for the intermediate representations, but because 3D evaluation is absent, the paper's most important claim—that this pipeline actually produces high-quality clothing-disentangled 3D characters—rests entirely on a few qualitative figures. Meanwhile, the runtime claim ("seconds") is similarly asserted without the systematic breakdown that a reader would expect for an efficiency-focused method. These are not fatal flaws—the 2D metrics are informative, the method is well-motivated, and the qualitative results look promising—but together they create a gap between what the paper promises and what it proves. The dataset contribution is substantial and stands on its own regardless.

## Suggestions

1. Add quantitative 3D evaluation: Chamfer distance between reconstructed 3D Gaussians and ground-truth meshes (per-part and combined), and/or FID on novel-view renderings. This is the single highest-impact addition.
2. Report end-to-end runtime: 2D disentanglement time, multi-view generation time (all parts), LGM reconstruction time, and optional optimization time.
3. Compare with at least one optimization-based method (qualitatively or quantitatively) to substantiate the speed-vs-quality positioning.
4. Ablate the two-stage design: compare direct generation of disentangled multi-view images vs. the proposed 2D-first approach.

## Score and Decision

The paper tackles an important and well-motivated problem, introduces several technically sound components (multi-part attention, combination attention), and contributes a valuable dataset. However, the evaluation has significant gaps: the 3D output is not quantitatively evaluated despite being the paper's central claim, the baseline comparison is too narrow to contextualize the contribution, and runtime is not reported despite efficiency being a key selling point. These gaps are addressable but prevent the paper from fully supporting its claims in its current form.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>