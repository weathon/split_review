Now I have all the information I need. Let me construct the final consolidated review.

---

## Summary

This paper proposes EpiMISR, a multi-image super-resolution method designed for the novel setting where input images have arbitrary, potentially large camera pose differences. The core idea replaces optical-flow-based registration with explicit epipolar geometry: features from each view are sampled along epipolar lines via a deterministic Cast-And-Project module and fused through a cascade of two transformers (view transformer then ray transformer). Experiments on the DTU dataset with 4× SR show a 0.84 dB PSNR improvement over the burst-SR state-of-the-art (BSRT), and the method remains competitive even with estimated poses from HLOC.

## Strengths

- **First generic MISR setting with arbitrary camera poses**: The paper correctly identifies that prior MISR work (burst, video, stereo, lightfield) assumes small geometric disparity. This is the first method tackling arbitrary camera poses with large disparities (11°–33° between views), validated on the DTU multi-view dataset. This opens a practically important but previously unaddressed problem.

- **Significant and consistent quantitative improvement**: EpiMISR achieves 28.51 dB PSNR on DTU, outperforming BSRT (27.67 dB) by 0.84 dB and DBSR (26.97 dB) by 1.54 dB. NeRF-SR (20.37 dB) is not competitive due to its different setting. The qualitative examples (Fig. 2) confirm visible detail recovery. These gains are consistent across multiple SISR-FE backbones (Table 2), with the multi-view fusion gain holding steady at ~1.6 dB PSNR over the SISR-only baseline.

- **Practical robustness to imperfect camera poses**: Section 4.5 shows that with poses estimated from HLOC (no ground-truth calibration), EpiMISR still achieves 28.10 dB PSNR — superior to BSRT which needs no poses at all. The sensitivity analysis (Fig. 5) demonstrates graceful degradation under moderate pose noise, supporting the claim that correct 3D geometry modeling is a key advantage.

- **Interpretable attention-based depth estimation**: Section 4.6 provides compelling visual evidence (Fig. 4) that the ray transformer's attention weights peak at the epipolar alignment region where all views image the same 3D point, and that the attention maximum can produce an unsupervised depth map. This demonstrates that the transformer fusion is genuinely learning geometric correspondences rather than just memorizing patterns.

- **Systematic parameter analysis**: Figure 3 evaluates the impact of number of views (V) and number of ray points (P), showing saturation beyond 8 views and 256 points. This validates the chosen hyperparameters and provides practical guidance for deployment.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Degradation model ambiguity**: The paper states (Sec. 4.1) that 400×300 HR images are obtained via bicubic downsampling, and that "degraded LR images are derived" from these, but never explicitly specifies the operation that generates the LR inputs. The standard SR convention (bicubic downsampling) is the natural reading, but given the paper's motivation for real-world applicability (security cameras, in-the-wild collections), the lack of explicit specification is a clarity issue. Additionally, all experiments use synthetic bicubic degradation — the standard in SR benchmarks, but the paper would benefit from acknowledging this limitation explicitly.

2. **Adaptation of burst-SR baselines not fully detailed**: The paper states burst methods (BSRT, DBSR) were "retrained using the authors' code" with "a minor modification... to use RGB images instead of RAW mosaiced images" (Sec. 4.1). The RAW-to-RGB conversion strategy is not described (e.g., demosaicing approach, input channel handling). While retraining to maximize validation performance partially addresses fairness concerns, a more detailed description would strengthen confidence that the baselines are not unfairly handicapped.

3. **MIFF transformer ordering not ablated**: The paper states (Sec. 3.1.2) that "performing the aggregation along the ray and then along the views is not optimal" due to computational constraints. While the computational justification is reasonable, no ablation compares view-then-ray vs. ray-then-view vs. a simpler (non-transformer) fusion baseline (e.g., learned weighted average of epipolar features). Such an ablation would clarify which design choices drive the improvement.

4. **No failure case discussion**: The paper does not discuss scenarios where the method might struggle (e.g., occlusions, very large baselines, textureless regions where epipolar correspondences are ambiguous). Given the practical motivation, discussing limitations would strengthen the paper.

5. **Inference time not reported**: Training takes 7 days on 4 A100s, but no inference runtime or model size is reported. For a method that processes many points along rays (P=256 per pixel), computational cost is relevant for practical applicability.

### Trivial

1. **Units for pose perturbation missing**: The sensitivity analysis (Sec. 4.5, Fig. 5) uses parameters σ_translation and σ_rotation without stating units (e.g., degrees, metric), making the x-axis in Figure 5 difficult to interpret practically.

2. **Minor clarity on "not optimal" claim**: The paper states the view-then-ray ordering is "not optimal" (line 130) but does not explain what optimality criterion is being invoked (performance? computational cost?). The justification given is computational constraints, which would make it "not computationally feasible" rather than "not optimal."

## Nice-to-Haves

- Add a simple fusion baseline (e.g., SISR features sampled at 3D points via known depth from stereo, then averaged) to directly test whether the transformer-based fusion provides benefit beyond geometric alignment alone.
- Quantitatively validate the attention-based depth estimation against DTU's ground-truth depth maps to strengthen Section 4.6.
- Include a qualitative example on real multi-view images with natural degradations (e.g., from an MVS dataset with natural blur) to demonstrate robustness beyond synthetic bicubic degradation.
- Report model parameter count and inference speed.

## Removed Points

The following points from the harsh critic were removed per the meta-review rules:

- **Missing related work in remote sensing MISR**: Removed per the rule "DO NOT mention missing related works, as you do not have external sources to confirm their existence."
- **"Unrealistic degradation" framing**: The critic claimed the bicubic degradation is "unrealistic" and that this is a "fundamental weakness." Bicubic degradation is the standard evaluation protocol in the SR literature. The paper is being evaluated against its own community's norms. The clarity issue (not specifying the operation) is kept as Minor; the "unrealistic" characterization is removed.
- **"SwinIR backbone may explain high PSNR"**: The critic suggested the large backbone may explain the results. The paper's Table 2 already addresses this by showing RLFN-based EpiMISR (a lightweight backbone) also outperforms BSRT. This concern is already addressed by the paper.
- **"Missing appendix / proofs / references"**: Removed per the rule that the parser strips these sections; they exist in the original submission.

## Novel Insights

Beyond the paper's own contributions, one observation that emerges across the reviews is that the paper has effectively identified a "blind spot" in the SR literature: while optical-flow-based burst SR and geometry-aware NeRF-based novel view synthesis have been pursued on largely separate tracks, EpiMISR demonstrates that combining explicit epipolar geometry (from the NeRF toolkit) with a learned, scene-general fusion model (from the SR toolkit) unlocks a setting neither community has addressed. The depth-from-attention result (Section 4.6) further shows the method implicitly learns 3D correspondences as a byproduct of the SR task — suggesting that geometry-aware MISR may have dual用途 in joint SR + depth estimation.

## Suggestions

- **Explicitly state the degradation model used for LR generation** in a single clear sentence early in the experimental section.
- **Add an ablation of the transformer ordering** (view-then-ray vs. ray-then-view vs. a non-transformer fusion baseline) to isolate the contribution of each component.
- **Describe the RAW-to-RGB conversion for burst baselines** and consider including a simple image-based rendering baseline (e.g., per-view SISR results averaged in 3D) to strengthen the comparative evaluation.
- **Report inference time and model size** for practical reference.
- **Include a brief limitations paragraph** discussing when the method might fail (occlusions, very large baselines, textureless regions).

## Score and Decision

This paper makes a clear and well-motivated contribution: it identifies a genuinely new setting (MISR with arbitrary camera poses), proposes a principled method that replaces optical flow with epipolar geometry and transformer-based feature field fusion, and demonstrates convincing results with thorough analysis (pose robustness, parameter sweeps, depth visualization, SISR-FE ablations). The weaknesses are minor — none threaten the core claims. The method is sound, the experimental design is appropriate for the setting, and the paper is clearly written.

MY FINAL SCORE: <score>8.0</score>
MY FINAL DECISION: <decision>Accept</decision>