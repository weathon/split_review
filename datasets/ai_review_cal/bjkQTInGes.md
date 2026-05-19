- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5, 5
Here is my consolidated final review:

---

## Summary

Ouroboros3D introduces a unified framework for single-image-to-3D generation that jointly trains a multi-view video diffusion model and a feed-forward 3D reconstruction model within a recursive denoising loop. During denoising, the diffusion model conditions on rendered RGB images and canonical coordinate maps (CCM) produced by the reconstruction module from the previous step's denoised estimate, creating a closed loop that mitigates the "data bias" between independently trained stages. Experiments on the GSO benchmark show consistent improvements over two-stage pipelines (LGM, InstantMesh) and inference-only hybrids (VideoMV), and the ablation study supports the contribution of each design component.

## Strengths

1. **Joint training with 3D-aware self-conditioning demonstrably outperforms inference-only integration.** Table 1 shows Ouroboros3D achieves PSNR 21.770 (multiview) and 21.761 (3D), substantially beating VideoMV (18.605/18.764) which combines stages only at inference. This directly supports the core claim that joint training reduces data bias.

2. **The ablation study cleanly quantifies the contribution of each component.** Table 2 shows stepwise improvements from the base (no joint training, PSNR 20.012) to joint training alone (20.549), to adding CCM feedback (21.325), to full CCM+RGB feedback (21.761). The ΔPSNR between multiview images and 3D rendered views drops from 1.067 to 0.009, directly demonstrating that the recursive framework aligns the two stages.

3. **Canonical coordinate maps (CCM) provide a principled geometric signal.** Section 3.3 motivates CCM over view-dependent depth/normal maps because CCM encodes global vertex coordinates and enables cross-view alignment. Table 2 confirms CCM alone lifts PSNR by 0.776 over joint training alone, validating this design choice.

4. **Probabilistic self-conditioning (50% dropout) prevents over-reliance on the reconstruction module.** Algorithm 1 shows this design choice explicitly (line 144: `if self_cond and random_uniform(0, 1) > 0.5`). The strong final results validate that this prevents the reconstruction feedback from dominating training.

5. **Gap metrics (ΔPSNR, ΔSSIM, ΔLPIPS) directly measure bias reduction.** Table 2 reports the difference between multiview-image quality and rendered-3D quality. The full model reduces ΔPSNR from 1.067 to 0.009, providing direct evidence that the recursive framework brings the two stages into alignment.

## Weaknesses

### Fatal
None.

### Major

1. **Resolution mismatch confounds the quantitative comparison (Table 1).** In the image-to-multiview block, SyncDreamer (256×256), SV3D (576×576), and VideoMV (256×256) are evaluated at different resolutions from Ouroboros3D (512×512). PSNR and LPIPS are resolution-dependent, so part of the reported gap could stem from resolution differences rather than the framework itself. The gap is large enough that it likely survives normalization, but the paper should either evaluate all methods at a common resolution (e.g., rescale to 512×512 or report Ouroboros3D at 256×256) or acknowledge this confound explicitly. In the image-to-3D block, LGM (512×512) and InstantMesh (512×512) match Ouroboros3D's resolution, so the concern primarily affects TripoSR (256×256) and VideoMV(GS) (256×256) in that block, but the multiview comparison remains weakened.

2. **Key training details are underspecified, hindering reproducibility and verification.**
   - **Algorithm 1 calls `recon_model(pred_x, c_noise)` directly on a reparameterized latent estimate**, but the text (lines 73, 90, 95) clarifies that `pred_x` must first be *decoded* to images before being fed to the reconstruction model. The decode step is absent from the pseudo-code, making the algorithm ambiguous about what `recon_model` actually receives.
   - **The reconstruction loss `recon_loss_fn(self_cond, x)` on line 149 is not defined.** The paper gives the LGM fine-tuning loss (Eq. 2) separately, but it is unclear how `self_cond` (rendered maps) is compared to the ground-truth `x`, what rendering process is used (differentiable? fixed? from which viewpoints?), and whether both color maps and CCM are supervised.
   - **The encoder architecture for color/coordinate map conditioning** is described only as "four feature extraction blocks and three downsample blocks" with no channel sizes, kernel sizes, or output resolutions (line 116). Combined with the absence of details on how the time embedding is integrated into LGM's U-Net (only mentioned in one sentence, line 97), this makes the method difficult to reproduce.

### Minor

1. **No error bars or confidence intervals** are reported for any quantitative result (Tables 1 and 2), despite a small test set of 100 GSO objects. While single-run evaluation is common in this area, reporting standard deviations would strengthen the reliability claims.

2. **No computational cost comparison** is given. The recursive loop with two forward passes (diffusion network + reconstruction) is more expensive than two-stage pipelines, but the paper only reports generation time (20 seconds) without comparing GPU-hours for training or inference against baselines.

3. **Failure cases and limitations are underexplored.** The limitation section (lines 301–304) only discusses mesh vs. 3DGS representation. It does not discuss failure modes such as textureless objects, objects with large concavities, cases where early denoising steps produce poor reconstructions that misguide later steps, or dependency on the quality of the input image.

4. **The "self-conditioning" nomenclature could cause confusion.** The method conditions on the *reconstruction module's output*, not the diffusion network's own previous prediction as in standard self-conditioning (Chen et al. 2022). The paper adapts the term (Section 3.3: "3D-aware self-conditioning") but should clarify the distinction to avoid misleading readers.

### Trivial
None.

## Nice-to-Haves

- **SV3D + LGM baseline**: Adding a baseline that uses SV3D as the multi-view generator and LGM as the reconstruction module (with or without re-sampling) would help isolate whether the improvement comes from joint training or from using better components.
- **Ablation with joint training + RGB-only feedback (no CCM)**: The current ablation jumps from "joint training alone" to "joint training + CCM" to "joint training + CCM + RGB." Adding a "joint training + RGB only" cell would isolate the contribution of geometric (CCM) vs. appearance (RGB) feedback.
- **Resolution-controlled evaluation**: Reporting results after downsampling Ouroboros3D output to 256×256, or upsampling baselines to 512×512, would cleanly address the resolution confound.
- **Quantitative out-of-distribution examples**: The generalizability results (Figure 5) are only qualitative. A few quantitative OOD evaluations would strengthen the claim.

## Removed Points

These points from the inputs were removed for the following reasons:

- **"The second forward pass through the diffusion network is computationally non-trivial and should be explicitly stated"** — This is visible in Algorithm 1 (lines 138 and 144–145) where the two `net()` calls appear when self-conditioning is active. The computational cost is implicit and standard for dual-forward methods. Moved to Minor (computational cost comparison is covered in Weakness #2).
- **"Missing baseline: SV3D + LGM with re-sampling would help isolate the value of joint training"** — VideoMV already implements inference-time re-sampling and is the direct ablated baseline for joint training. The SV3D+LGM combination is a reasonable extension but not a missing core baseline. Moved to Nice-to-Haves.
- **"The paper does not discuss how the improvement over VideoMV compares to simply using a better multi-view generator"** — The paper already compares against SV3D (multi-view) and VideoMV (re-sampling), which directly addresses this question. The improvement over VideoMV is specifically attributable to joint training since both use similar base architectures.
- **"The ablation study shows 'Jointly Training' alone improves PSNR from 20.012 to 20.549 — this is a moderate gain"** — This is a factual statement about the result, not a weakness. The full gain to 21.761 is substantial.
- **"Training convergence"** mentioned as missing — Not a standard expectation for a conference paper; moved to general suggestion.
- **Various formatting/style nitpicks** — Parser artifacts, not author errors.
- **Strength Finder's generic strengths** (e.g., "addressed an important problem") — Removed as generic/superficial; only specific, evidence-grounded strengths were retained.

## Novel Insights

None beyond the paper's own contributions. The key insight — closing the loop between generation and reconstruction via joint training with rendered 3D-aware feedback — is the paper's own novel contribution; the reviews do not surface any additional insight beyond what the authors present.

## Suggestions

1. **In Algorithm 1, add the explicit decode step** between `pred_x` and `recon_model` to clarify the data flow. Define `recon_loss_fn` precisely, specifying what rendered outputs are compared to ground truth and how rendering is performed.
2. **Evaluate all methods at a common resolution** (e.g., rescale to 512×512 or include Ouroboros3D at 256×256 as an additional row in Table 1) to remove the resolution confound.
3. **Report standard deviations** for the main results over the 100 test objects.
4. **Add an ablation row** for joint training with RGB-only feedback (without CCM) to isolate the value of geometric maps.
5. **Expand the limitations section** to discuss failure modes (textureless objects, viewpoint extremes) and the computational overhead of the recursive loop relative to two-stage baselines.
