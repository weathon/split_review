## Summary

NoPoSplat proposes a feed-forward network that reconstructs 3D Gaussian scenes from sparse unposed multi-view images by predicting Gaussian primitives in a canonical space anchored to the first input view's coordinate system. The model is trained using only photometric loss (no depth supervision) and achieves 66 fps inference. The canonical-space formulation bypasses the standard "predict-in-local, transform-to-global" pipeline that requires accurate camera poses, and the paper demonstrates applications in novel view synthesis (NVS) and pose estimation.

## Strengths

- **Canonical-space Gaussian prediction is well-motivated and cleanly validated.** The ablation study (row (f) of Tab. 4) shows that the canonical-space prediction outperforms the transform-then-fuse pipeline even when the latter has access to ground truth poses, with qualitative improvements (no ghosting artifacts). This directly supports the paper's central architectural claim.

- **Photometric-only training is a genuine practical advantage.** Unlike DUSt3R/MASt3R/Splatt3R which require ground truth depth, NoPoSplat is trained with only MSE + LPIPS loss (Sec. 3.5). This enables training on large video datasets (RE10K, ACID, DL3DV) that lack depth annotations, which is a meaningful practical contribution.

- **Strong cross-dataset generalization.** The model trained exclusively on RE10K outperforms both pose-required methods (pixelSplat, MVSplat) and Splatt3R (trained on ScanNet++) when tested zero-shot on DTU and ScanNet++ (Tab. 3, Fig. 6). This provides concrete evidence that the minimal geometric priors help generalization.

- **Practical efficiency** — 0.015s (66 fps), 5× faster than pixelSplat and 2× faster than MVSplat on RTX 4090 (Sec. 4.1).

- **Clean resolution of the scale ambiguity problem** via intrinsic token embedding, with three embedding strategies ablated and compared (Sec. 3.4, Tab. 4).

## Weaknesses

### Fatal

None.

### Major

- **Evaluation-time target pose optimization creates an asymmetric NVS comparison (Sec. 4, lines 176–182).** The paper optimizes the target view camera pose (with Gaussians frozen) to maximize agreement with the ground truth image during NVS evaluation. The pose-required baselines (pixelSplat, MVSplat) receive ground truth target poses and perform no such optimization. This means the reported NVS metrics for NoPoSplat reflect reconstruction + test-time pose refinement, while baselines' metrics reflect reconstruction alone. The headline claim that "a pose-free method can outperform pose-dependent methods" (line 44) is weakened by this asymmetry. The paper should either (a) report NVS metrics *without* this optimization, or (b) apply equivalent target-view optimization to the baselines, to cleanly separate reconstruction quality from test-time refinement. The paper acknowledges this practice and cites precedent (Nerfmm, InstantSplat), but precedent does not resolve the evidential gap for the specific claim being made.

### Minor

- **MASt3R initialization is not quantitatively ablated in the main paper (lines 216–218).** The encoder, decoder, and Gaussian center head are initialized with MASt3R weights. The paper states (in truncated text at line 218) that training from scratch "with only RGB supervision — without pre-trained weight from MASt3R — and still achieve[s] similar performance," but no quantitative results for this ablation appear in the main ablation table. Given that MASt3R embodies substantial geometric knowledge from depth-supervised training on large data, the reader cannot assess what fraction of performance derives from the pretrained backbone vs. the proposed formulation. This should be added as a row in the ablation table.

- **Overlap-based evaluation is described but only shown qualitatively (lines 195–196, Fig. 5).** The paper categorizes input pairs by overlap ratio (small/medium/large) but provides no quantitative NVS breakdown by category. The central claim of advantage in low-overlap settings would be significantly strengthened by a table showing PSNR/SSIM/LPIPS for each overlap category.

- **Canonical space limitation not discussed.** The reconstruction is anchored to the first input view's coordinate system (Sec. 3.3), so independent reconstructions are not in a global metric frame and cannot be directly merged. This is appropriate for the paper's stated tasks but deserves explicit acknowledgment as a limitation.

### Trivial

- The PnP-based pose estimation step (line 172) applies PnP to Gaussian centers but does not specify how 2D–3D correspondences are established. Clarifying this would aid reproducibility.

## Nice-to-Haves

- Quantitative NVS breakdown by overlap category to substantiate the low-overlap advantage claim.
- Failure case analysis (very large baselines, textureless scenes, repetitive structures) to help readers calibrate expectations.
- Visualization or probe of what the cross-attention between views learns about 3D structure.

## Removed Points

These points were flagged for removal. Treat them with caution.

- **Pose estimation comparison is "not apples-to-apples" (Harsh Critic's Critical Issue #3).** The critic claims comparing NoPoSplat's pose estimation (via reconstructed 3D Gaussians) against RoMa/DUSt3R is unfair because NoPoSplat uses more information. However, both methods solve the same task (relative pose estimation from image pairs) with the same input. That NoPoSplat achieves this via an intermediate 3D representation is the methodological contribution, not an unfair advantage. **Removed.**

- **"From-scratch claim relegated to appendix" and "RGB shortcut bypasses geometric reasoning."** The from-scratch claim appears in the main paper text (line 218, truncated by PDF parser — the original sentence existed in the submission), not the appendix. The RGB shortcut criticism is speculative (no evidence that the network "bypasses geometric reasoning"). **Removed.**

- **Canonical space = no global metric reconstruction as a criticism of the paper's framing.** The paper explicitly anchors to the first view's coordinate system (lines 132–135). This is a design choice, not an oversight. Demoted to a missing-limitation-discussion point in Minor above. **Moved to Minor.**

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add a row to the ablation table showing NVS performance when training from scratch (no MASt3R initialization). This is the single highest-leverage addition.
2. Report NVS metrics both with and without evaluation-time target pose optimization to separate reconstruction quality from test-time refinement.
3. Provide a quantitative table breaking down NVS performance by input overlap category.
4. Clarify how 2D–3D correspondences are established for the PnP step in pose estimation.

## Score and Decision

The paper presents a clean, well-motivated idea with strong empirical results across multiple tasks. The canonical-space formulation is genuinely novel and validated by careful ablation. The main concern is the evaluation-time pose optimization creating an asymmetric comparison for the headline NVS claim — this is a real issue but it follows established precedent, does not affect the comparison against pose-free methods (where the paper dominates), and does not affect the pose estimation or cross-dataset generalization results, which are independently strong. The MASt3R initialization concern is easily resolvable with an additional ablation row. The paper has a clear contribution and the weaknesses are addressable.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>