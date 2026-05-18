Now I have a thorough understanding of the paper and all the review claims. Let me write the consolidated review.

---

## Summary

This paper proposes Variational Bayes Gaussian Splatting (VBGS), which frames Gaussian splat optimization as variational inference over model parameters. By leveraging conjugate exponential-family distributions (NIW for spatial Gaussians, fixed-covariance Normal for color), the authors derive closed-form update rules that are additive in sufficient statistics, enabling order-invariant continual learning without replay buffers. Experiments on Tiny ImageNet (2D), Blender 3D objects, and Habitat rooms demonstrate that VBGS maintains stable reconstruction quality in streaming settings where gradient-based methods catastrophically forget.

## Strengths

1. **Principled derivation of closed-form VB updates for Gaussian splatting.** The paper correctly leverages conjugacy (NIW priors for spatial parameters, fixed-covariance Normal for color) to derive additive natural-parameter updates (Equations in Section 3.3). This is a technically sound contribution that departs from the standard gradient-through-renderer paradigm.

2. **Convincing demonstration of forgetting-free continual learning.** On 2D image patches (Figure 2a), VBGS maintains stable PSNR across timesteps while the gradient baseline drops catastrophically. On 3D Blender objects (Figure 3b), VBGS holds ~21 dB whereas the gradient method falls below 10 dB after 200 frames. The Habitat room experiments (Figure 5b) further show that VBGS integrates information across frames even without the reassignment heuristic.

3. **Competitive static reconstruction with the simplified gradient baseline.** On Blender 3D objects (Table 1), VBGS with data initialization outperforms the gradient baseline on 5 of 8 objects and is competitive on the remainder — under the same simplified setup (no spherical harmonics, fixed camera).

4. **Computational efficiency of single-pass inference.** VBGS requires ~0.03 seconds (single update) versus ~0.05 seconds for the gradient method to reach equivalent performance (t-test p=0), measured on Tiny ImageNet.

## Weaknesses

### Fatal
None.

### Major

1. **Overclaimed static-dataset performance.** The abstract states that VBGS "matches state-of-the-art performance on static datasets." This is misleading because the only point of comparison is a simplified gradient baseline (no spherical harmonics, fixed camera pose, fixed z-coordinate). Full 3D Gaussian Splatting (Kerbl et al.) achieves PSNR >30 dB on the Blender scenes; VBGS achieves ~20–25 dB. The paper never compares to actual 3DGS, and the phrase "state-of-the-art" implies a bar the method does not reach. The contribution is about continual learning, not static reconstruction quality; the paper should be honest about where it stands. The conclusion already acknowledges limitations relative to 3DGS (line 370–373), so the abstract needs to be brought into alignment.

2. **Missing comparison to replay-buffer baselines, which the paper explicitly motivates against.** The paper repeatedly frames VBGS's central advantage as "eliminating the need for replay buffers" (abstract, introduction, related work, discussion). Yet the continual-learning experiments compare only to a gradient baseline that does *not* use a replay buffer. The standard mitigation for catastrophic forgetting in 3DGS (e.g., SplaTAM, SPLAT-SLAM, iMAP — all cited by the paper) *does* use replay. Without showing that VBGS is competitive with or superior to gradient-based methods that employ even a small replay buffer (e.g., the last K frames), the claimed advantage is unsubstantiated. This is a significant gap in the evaluation.

### Minor

3. **Ambiguous description of the continual-learning update rule (Section 2.1).** The paper states that "assignments q(z) are always computed with respect to the *initial* posterior over parameters" (line 203) and that this makes updates order-invariant (line 233). This claim is *technically correct and not self-contradictory* — fixing assignments based on initial component positions while accumulating sufficient statistics does yield order-invariant updates. However, the description would benefit from (a) explicitly stating that this is a deliberate design choice that departs from standard CAVI (where assignments and parameters are iteratively refined), and (b) explaining *why* this choice is sufficient (i.e., spatial coverage from data initialization makes re-computing assignments unnecessary). A reader unfamiliar with this variant will reasonably wonder whether the assignments are being recomputed from the current posterior (standard online VB) or frozen — the text should remove this ambiguity.

4. **Limited evaluation metrics.** Only PSNR is reported for reconstruction quality. SSIM and LPIPS are standard in the 3DGS and novel-view synthesis literature and would give a more complete picture of rendering quality, especially since VBGS's fixed color covariance and simplified spatial model may produce different visual artifacts than the gradient baseline.

5. **Fixed color covariance assumption not discussed in terms of its impact.** The model fixes the color covariance to εI via a Delta distribution (line 150), which forces each Gaussian to represent a region of nearly constant color. While the paper notes this prevents color blending (line 138), it does not discuss how this limits representational power on high-frequency textures relative to methods with learnable color representations. The impact of this choice could be empirically quantified.

### Trivial
None.

## Nice-to-Haves

- The reassignment heuristic (Section 3.4) is introduced for the Habitat room setting where data coverage is unknown. Testing it on the Blender objects (where it might close the gap on scenes like "ship") would be informative, though the static evaluation setting is not the primary use case for this mechanism.
- An ablation showing the effect of the ε hyperparameter in the fixed color covariance would help readers understand the sensitivity of this design choice.

## Removed Points

- **"Initial posterior makes method broken" (Harsh Critic, Critical Issue #2, first sub-bullet):** The critic claims that using initial parameters for assignments "would ignore all subsequent evidence when assigning new data – a recipe for poor reconstructions." This is factually incorrect. Assignments determine only which component a data point belongs to; the sufficient statistics (color, spatial spread) still accumulate all observed evidence. With data-initialized spatial coverage, this design choice is sound and the experiments confirm it works. Removed as a misunderstanding.
- **Critic's claim that Table 1 "confirms the gap" to full 3DGS:** Table 1 compares VBGS to the *simplified gradient baseline* (same setup), not to full 3DGS. The gap to full 3DGS is real (hence the overclaim criticism is kept), but Table 1 does not itself "confirm" this gap. Removed as a misreading.
- **Critic's claim about "random init" underperformance being an unaddressed weakness:** The paper acknowledges this and introduces the reassignment heuristic specifically to address it. The critic's suggestion to test reassignment on Blender objects is a nice-to-have, not a weakness.

## Novel Insights

The most interesting observation from the review process is that the paper's approach to continual learning — fixing component assignments based on initial (pre-data) parameters — is *more radical* than first appearances suggest. Standard variational continual learning (e.g., VCL, online VB) re-computes assignments/posteriors as new data arrives, which introduces order-dependence through changing responsibilities. VBGS instead freezes the responsibilities entirely, achieving strict order-invariance at the cost of never revisiting cluster membership. This is a meaningful design point in the continual-learning space that deserves clearer exposition and explicit comparison to alternative Bayesian continual learning strategies. The fact that it works as well as it does suggests that for Gaussian splatting (where spatial coverage via data initialization is straightforward), the ability to refine assignments is not as critical as it is in other mixture-model settings.

## Suggestions

1. **Rewrite the abstract** to replace "matches state-of-the-art performance on static datasets" with a measured statement such as "achieves competitive reconstruction quality with a simplified gradient-based Gaussian splatting baseline on static datasets, while its main strength lies in continual learning."
2. **Add at least one replay-buffer baseline** to the continual learning experiments. A straightforward experiment: the gradient method with a replay buffer storing the most recent 10–20 frames, evaluated under the same streaming protocol.
3. **Clarify Section 2.1** by (a) explicitly stating that assignments use the initial (pre-data) parameterization and are *not* recomputed, (b) explaining why this is sufficient (spatial coverage from initialization), and (c) contrasting this with standard CAVI where assignments are iteratively refined.
4. **Add SSIM/LPIPS metrics** to the 3D reconstruction tables if feasible; at minimum, acknowledge the limitation in the paper.
5. **Discuss the fixed-color-covariance trade-off** more explicitly, including the effect of the ε hyperparameter.

## Score and Decision

After careful review, the paper has a genuine technical contribution (closed-form VB for Gaussian splatting with order-invariant updates) and provides convincing evidence of forgetting-free continual learning. However, the overclaimed abstract and the absence of the natural replay-buffer baseline — which the paper explicitly motivates against — are significant weaknesses that should be addressed before publication. The core idea is sound and the issues are fixable.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>