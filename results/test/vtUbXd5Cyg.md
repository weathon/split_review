Now I have thoroughly verified the paper content against all reviewer claims. Let me compose the consolidated review.

## Summary

ToMiE proposes a modular growth strategy for the SMPL skeleton to handle complex garments (hand-held objects, loose-fitting clothing) in 3D human Gaussian rendering. The method first localizes parent joints requiring extension via a hybrid assignment of gradient accumulation using LBS weights and a proposed Motion Kernel, then optimizes explicit SE(3) transformations for the grown joints via MLPs. This enables both high-quality rendering and explicit, decoupled animation of garments.

## Strengths

- **State-of-the-art rendering quality on DNA-Rendering, especially on challenging garment regions.** ToMiE achieves 31.28 PSNR(full) vs. 30.22 for GauHuman (next best animatable method, +1.06 dB), and 19.75 PSNR(masked) vs. 18.26 (+1.49 dB) on the garment regions that are the paper's target. These are meaningful margins, not incremental (Table 1).

- **Explicit extra joint optimization enables a novel animation capability absent in prior 3DGS human methods.** ToMiE models external joints with learnable positions and per-frame rotations in SE(3), stored in an extra joint book with explicit parent-child relations. This allows decoupled animation of garments independently of the body's SMPL pose — including direct input of custom trajectories (e.g., "spiral" motion) — whereas GART's implicit auxiliary bones remain tied to traditional SMPL poses. Figure 6 demonstrates this qualitative advantage convincingly.

- **Gradient-based parent joint localization with Motion Kernels addresses a real misclassification problem.** The paper identifies that nearest-neighbor LBS assignment in canonical space misclassifies hand-held object points to unrelated joints (e.g., leg instead of hand), producing rendering voids. The Motion Kernel, measuring relative motion in observation space (Equation 5), combined with LBS weights (Equation 7), corrects this assignment. Figure 3 provides visual evidence of this correction.

- **Adaptive growth via gradient thresholding is principled and avoids unnecessary joint proliferation.** The gradient accumulation formulation (Equation 2) and thresholding (Equation 8) grow only joints whose associated gaussians exhibit sufficient underfitting, preventing memory/computation overhead from arbitrary growth.

## Weaknesses

### Fatal

None.

### Major

- **Animation quality is not quantitatively evaluated despite being a core contribution.** The paper touts explicit animation as a key advantage over prior work (listed as Contribution 1 and emphasized throughout), yet its animation evaluation consists of one qualitative figure (Figure 6) and references to the supplemental video. No quantitative metrics (e.g., temporal consistency, tracking error, user study) or comparison against baselines on animation quality are provided. For a claim of "state-of-the-art results in both rendering and explicit animation" (Abstract), the animation half of this claim lacks rigorous support. While qualitative demonstrations are common in graphics, the strength of the claim demands stronger evidence.

- **The Motion Kernel is not separately ablated.** The "w/o Modular Growth" ablation removes the entire growth pipeline (MK + parent localization + joint optimization), so the individual contribution of the Motion Kernel to gradient assignment cannot be assessed. Since the hybrid LBS+MK assignment (Contribution 2) is a central technical novelty, its lack of isolation is a gap. The qualitative evidence in Figure 3 is helpful but does not substitute for a quantitative comparison (e.g., LBS-only vs. MK-only vs. hybrid).

### Minor

- **The non-rigid deformation network (\(\Phi_d\)) ablation shows an LPIPS inconsistency not discussed.** Removing \(\Phi_d\) improves LPIPS (0.0363 vs. 0.0374) while degrading PSNR and SSIM (Table 2). The paper does not acknowledge or explain this. While PSNR and SSIM both favor the full model, the LPIPS reversal warrants at least a brief comment (e.g., the perceptual cost vs. geometric benefit trade-off).

- **Hyperparameter \(\lambda\) (MK vs. LBS blend weight) and \(\epsilon_{\bm{J}}\) (gradient threshold) lack sensitivity analysis.** These are free parameters that likely affect which joints are grown and the quality of parent localization. No ablation studies explore their impact, making it unclear whether the reported results are robust or finely tuned.

- **Training time and memory consumption are not reported relative to baselines.** Since the method adds extra joints, MLPs, and a growth stage, runtime and memory costs vs. GauHuman/GART would be useful for practitioners to assess the practical overhead of modular growth.

- **LBS network output dimension extension for extra joints lacks initialization or regularization discussion.** The paper states \(\Phi_{\text{lbs}}\) extends its output to include blending weights for extra joints "entirely learned" (line 327), but does not describe how these new weights are initialized or whether any regularization is applied to prevent instability during early post-growth training.

### Trivial

None.

## Nice-to-Haves

- A quantitative comparison of animation quality — e.g., temporal smoothness of rendered garment motion, or a simple user preference study — would substantially strengthen the paper's core animation claim.
- An ablation isolating the Motion Kernel from the rest of modular growth (e.g., w/o MK vs. w/ MK, both with modular growth enabled) would clarify its individual contribution.
- Sensitivity analysis for \(\lambda\) and \(\epsilon_{\bm{J}}\) would improve reproducibility and robustness confidence.
- Reporting per-case results for all 8 DNA-Rendering cases in the main text (rather than only in supplemental) would help readers assess variance across garment types.
- A brief discussion of why removing \(\Phi_d\) improves LPIPS despite hurting PSNR would preempt confusion.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"Only ~0.3 dB better than GART on DNA-Rendering"** — This is factually incorrect. The reviewer conflated GART's ZJU-MoCap score (30.91) with its DNA-Rendering score (29.25). The actual improvement on DNA-Rendering over GART is 31.28 − 29.25 = **2.03 dB**. This error propagates to the claim that gains are "modest" — on the targeted garment dataset, margins are substantial.
2. **"The quantitative gains over the strongest baselines are modest"** — Partially invalidated by the above correction. On DNA-Rendering, ToMiE's PSNR margins are 1.06 dB over GauHuman and 2.03 dB over GART. On ZJU-MoCap (tight clothing, where growth is not needed), margins are small, but the paper acknowledges this is expected. The claim about statistical significance (no variance reported) is retained as a minor observation.
3. **"Qualitative comparisons reflect only two cases"** — The paper tests on 8 cases and explicitly states per-case results are in supplemental. This is standard practice for a paper of this length.

## Novel Insights

The most interesting observation emerging across the reviews is that the paper's dual-purpose design (modular growth for both rendering quality and animation) creates a tension in its evaluation: the rendering improvement can be cleanly quantified (modest but real), while the animation capability — arguably the more novel aspect — resists standard quantitative evaluation in this domain. The paper would benefit from acknowledging this asymmetry directly and developing evaluation protocols for explicit garment animation, which remains an under-evaluated capability in the 3D human literature. The Motion Kernel's hybrid design (LBS + motion priors in observation space) is a principled response to a genuine failure mode of canonical-space-only assignment, but without an ablation isolating it, its effectiveness relative to simply using better LBS weights is unclear.

## Suggestions

1. Add an ablation that isolates the Motion Kernel (e.g., "w/ LBS-only assignment" vs. "w/ MK hybrid assignment") with both keeping modular growth enabled, to demonstrate the MK's individual contribution.
2. Include at least one quantitative metric for animation quality — temporal consistency (e.g., warping error between consecutive frames under animation) or a small-scale user preference study comparing ToMiE animation against GART animation on held-out poses.
3. Provide sensitivity analysis for \(\lambda\) and \(\epsilon_{\bm{J}}\) across 2–3 values each, or justify default choices via a simple grid search.
4. Briefly address the LPIPS reversal in the \(\Phi_d\) ablation.
5. Report training time and peak memory for ToMiE vs. GauHuman and GART to help practitioners assess the cost of modular growth.

## Score and Decision

This paper makes a genuine contribution: the modular growth strategy is a well-motivated, technically sound solution to a real limitation of SMPL-based 3D human rendering for complex garments. The quantitative rendering results on DNA-Rendering are state-of-the-art with meaningful margins, and the explicit animation capability is novel and qualitatively compelling. The main weaknesses are the lack of a motion kernel ablation, the absence of quantitative animation evaluation for a core claim, and a few under-explored design choices. None of these invalidate the contribution — they are addressable gaps in experimental depth. This is a solid paper with a clear advance over prior work.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>