Now I have all the information needed. Let me write the final consolidated review.

## Summary

The paper proposes IC-Light (Imposing Consistent Light transport), a training constraint for diffusion-based illumination editing. The core idea is that light transport linearity—the appearance under mixed lighting equals the sum of appearances under individual lights—can be transferred to diffusion prediction targets, yielding a consistency loss that helps the model modify only illumination while preserving intrinsic properties (albedo, details). The method is scaled to >10M images across three data types (in-the-wild augmentations, 3D renders, light stage captures) and deployed on strong backbones (SDXL, Flux).

## Strengths

- **Physically motivated consistency loss with ablation support.** The paper derives from light transport theory (Eq. 3) that `I*(L₁+L₂) = I*(L₁) + I*(L₂)` in HDR pixel space and shows this linearity can be propagated to diffusion noise targets (Section 3.2, lines 64–78). The ablation in Fig. 4 provides concrete visual evidence that removing this constraint causes "red and blue differences [to] vanish" and introduces color saturation issues. Prior diffusion-based illumination methods (Relightful Harmonization, DiLightNet, SwitchLight) do not impose this kind of cross-condition consistency.

- **Data unification pipeline at significant scale.** Section 3.1 describes converting heterogeneous data sources to a common format: 6 albedo extraction methods, 3 random normal estimators, 20K purchased + 500K Flux-generated shadow materials, CLIP Vision filtering of 50M→6M images, plus Objaverse renders (4M) and light stage captures. This is more comprehensive than prior work and enables training at >10M-image scale.

- **Unsupervised normal map extraction as a byproduct.** Section 4.3 (Eqs. 6–8) derives normal maps by averaging consistent inferences under different lighting and computing per-pixel shading differences—without any normal supervision during training. This cleanly demonstrates that the model's consistency is empirically realized.

## Weaknesses

### Fatal

None.

### Major

1. **Quantitative evaluation is conducted solely on synthetic data, not on real-world images.** The only numerical evidence (Section 4.4, Table 1) is on 50K held-out Objaverse rendering samples—synthetic data from the authors' own rendering pipeline. The paper acknowledges the bias ("Models trained only on 3D data achieved the highest PSNR, but this is likely due to an evaluation bias towards the rendering data"), yet this same biased evaluation is the only quantitative evidence presented. There is no quantitative evaluation on real light stage captures with ground truth, on established relighting benchmarks (e.g., Multi-Illumination dataset), on real photographs via distributional metrics (FID, CLIP scores with illumination descriptions), or via a user study. Given that "in-the-wild" appears prominently in the title and abstract, the absence of quantitative real-world evaluation is a significant gap between claims and evidence.

2. **The MLP φ that mediates the core consistency constraint is unanalyzed.** The elegant physical linearity `I*(L₁+L₂) = I*(L₁) + I*(L₂)` in HDR pixel space becomes `ε_{L₁+L₂} ≈ φ(ε_{L₁}, ε_{L₂})` in latent space, where φ is a 5-layer MLP with 128 hidden units (line 86). The paper acknowledges the domain gap (HDR→latent/LDR) and introduces φ to "learn an implicit adaptation," but provides no analysis of what φ actually learns: does it converge to an approximately additive function? Is the result sensitive to its capacity? Could it be replaced by a simpler operation? Without this analysis, the "physically grounded constraint" is better characterized as a learned consistency regularizer whose behavior is opaque. This weakens the paper's central theoretical claim.

### Minor

1. **Baseline comparison disadvantages competing methods.** SwitchLight and DiLightNet are evaluated on the authors' own synthetic test set (50K Objaverse renders) that matches the authors' training distribution but is out-of-distribution for the baselines. The paper acknowledges the bias but does not provide a complementary evaluation where all methods can be fairly compared (e.g., on a shared real-world benchmark or on data from an independent source). The LPIPS advantage of the full method is the least-biased signal, but without real data it is hard to interpret.

2. **Normal map comparison overstates the finding.** Section 4.5 claims the model's derived normals "exhibit higher quality for human than alternatives GeoWizard and DSINE." This compares an empirical byproduct of a relighting model (acknowledged as "not optimized to approximate light stage ground truths" at line 153) against dedicated geometry estimators trained specifically for normal prediction—two fundamentally different tasks with different standards of evaluation. The qualitative comparison in Fig. 6 is not accompanied by quantitative normal-map metrics.

3. **Ablation (Fig. 4) is only qualitative with two images per condition.** The paper states "more examples in supplementary materials," which is standard practice, but the main text's ablation evidence is thin. Confidence in the ablation conclusions would be improved by quantitative metrics (e.g., on the consistency loss itself) alongside the qualitative examples.

### Trivial

- The choice of 4×4 random masks to decompose L into L₁+L₂ (line 86) is not justified or ablated. While unlikely to change the main conclusions, the sensitivity to this design choice is unclear.

## Nice-to-Haves

- **Analyze the learned MLP φ**: Show whether it learns approximately additive behavior, study sensitivity to its capacity, or attempt to replace it with a simpler operation (e.g., a linear layer or direct addition despite the approximation error). This would substantially strengthen the paper's core claim of physical grounding.
- **Evaluate on real-world data**: Even without ground-truth illumination, distributional metrics (CLIP score with illumination descriptions, FID, or a user study) on real photographs would support the "in-the-wild" claims. A comparison on a standard benchmark (e.g., Multi-Illumination) would be ideal.
- **Provide confidence intervals or variance** for the quantitative results in Table 1 given the 50K sample size.

## Removed Points

These points were surfaced in the input reviews but removed or downgraded per the filtering rules:
- **"No evaluation on light stage data despite having access"** — Demoted from fatal to major (point 1 covers this adequately; the paper does show qualitative light-stage results).
- **"CLIP filtering keywords are vague"** — A reasonable practical choice for filtering, not a substantive weakness.
- **"Frequent references to supplementary materials"** — Standard practice at this venue; not a weakness of the main paper.
- **"The dataset construction pipeline details are not fully specified"** — Common to defer construction details to supplementary; not a core evaluation weakness.
- **"The MLP could learn arbitrary functions"** — The reviewer's speculation about what the MLP "could" do is removed; the concrete weakness (lack of analysis) is retained as Major point 2.
- **"Table embedded as image / parser formatting issues"** — Parser artifacts, not author errors.
- **"Results from Relightful Harmonization taken from original paper (not run by authors)"** — Observational, not a weakness; the comparison is clearly labeled.
- **Generic/superficial strengths** from the Strength Finder (e.g., "addressed an important problem") were dropped as they lack concrete content or conflict with verified weaknesses.

## Novel Insights

None beyond the paper's own contributions. The reviews surface known tensions in this line of work (synthetic-to-real evaluation gaps, learned approximations to physical constraints) but do not contribute new observations about the paper beyond what a careful reader would identify.

## Suggestions

1. **Add quantitative evaluation on real-world data.** The most impactful improvement would be evaluating on the Multi-Illumination dataset (Murmann et al.) or conducting a user study on real photographs. Even without ground truth, distributional metrics would materially support the "in-the-wild" claims.
2. **Analyze the MLP φ.** A simple experiment—plotting `‖φ(ε₁, ε₂) − (ε₁ + ε₂)‖` over training, or ablating φ's capacity—would significantly strengthen the claim that the consistency loss is physically grounded rather than a black-box regularizer.
3. **Evaluate all methods on a shared real-world benchmark** or at minimum clearly frame the synthetic evaluation as a diagnostic test of specific properties rather than a direct performance comparison.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Weak Accept</decision>