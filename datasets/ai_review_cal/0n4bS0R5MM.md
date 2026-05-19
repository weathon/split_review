- Decision: Accept
- Avg Score: 6.20
- Scores: 8, 3, 6, 8, 6
Now I have all the information needed. Let me construct the final review.

## Summary

This paper proposes VD3D, a method for adding 3D camera control to transformer-based video diffusion models (specifically SnapVideo). The core idea is a ControlNet-style conditioning mechanism that injects spatiotemporal Plücker coordinate embeddings through cross-attention layers within the FIT blocks of the video transformer. The method is fine-tuned on RealEstate10K and evaluated against adaptations of MotionCtrl and CameraCtrl to the transformer architecture. The paper claims to be the first to enable camera control for transformer-based video diffusion models, and the user study shows strong preference (82% and 78% over MotionCtrl and CameraCtrl adaptations) for the proposed approach.

## Strengths

1. **First camera-control mechanism for joint spatiotemporal video transformers**: The paper proposes a genuinely novel conditioning scheme — injecting Plücker coordinate embeddings via zero-initialized ControlNet-style blocks into the cross-attention layers of a FIT-based transformer. This is architecturally distinct from prior work (MotionCtrl, CameraCtrl) that conditions only the separate temporal layers of U-Net models. The motivation is well-supported: transformer-based video models do not have standalone temporal layers, so previous approaches are inapplicable. Evidence: Section 3.2, Equations (2)-(3), and the design discussion in lines 121-122 ("it abandons the decomposed spatial/temporal computation nature... which is vital for modern camera conditioning techniques").

2. **Strong empirical evidence from user study**: In a study with 20 participants and 20 side-by-side comparisons per participant, 82% and 78% of comparisons preferred the camera alignment of VD3D over adapted MotionCtrl and CameraCtrl baselines, respectively, with all sub-metrics significant at p<0.001 (χ² test). This is a clean, head-to-head evaluation with multiple sub-metrics (camera alignment, motion quality, text alignment, visual quality, overall preference). Evidence: Section 4.1, lines 241-243.

3. **Ablation studies confirm key design choices**: Experiments show that (a) Plücker embeddings are essential (raw camera matrices yield worse control), (b) the ControlNet-style residual path with zero-initialized layers is critical for learning camera control without degrading quality, and (c) weight copying from pre-trained layers has minor impact — the architecture and zero-initialization are the key components. Evidence: Section 4.2, lines 252-256.

4. **Demonstrated downstream applicability**: The method enables image-to-video generation and image-to-multiview generation for complex, non-object-centric scenes — going beyond prior 3D generation techniques limited to object-centric scenes. While only qualitative, this demonstrates practical utility beyond the core claim. Evidence: Section 4.3, Figures referenced.

## Weaknesses

### Fatal
None.

### Major

1. **Baseline comparison fairness is not fully validated**: The paper's central claim of state-of-the-art performance rests on comparisons against MotionCtrl and CameraCtrl adapted to SnapVideo (Section 3.6). While the adaptations are described, there is no analysis of whether these are *good* adaptations. For MotionCtrl, the original design conditions separate temporal attention layers that do not exist in SnapVideo — the adaptation may be a weak reimplementation. The paper does not explore alternative injection strategies (e.g., different injection points, different fusion of camera signals) or provide evidence of convergence that would confirm the baselines were reasonably tuned. Line 238 states "For fair comparison, we trained all models for the same number of iterations," but equal training budget does not guarantee equal architectural suitability. The gap claimed may be real, but the reader cannot rule out that suboptimal baseline adaptation accounts for some of the reported advantage. This weakens the SOTA claim proportionally to its centrality in the paper.

2. **Evaluation scope is limited to a single domain**: All fine-tuning and evaluation (including camera trajectories for both user study and automated metrics) is on RealEstate10K, which consists of slow, smooth camera movements in static indoor/outdoor real estate scenes. While OOD text prompts from MSR-VTT are tested, the camera trajectories remain from RealEstate10K. The paper's claim of enabling camera control for "large video diffusion transformers" implies general applicability, but generalization to fast zooms, non-linear motion, dynamic object motion, animated content, or different visual domains is not established. This does not invalidate the contribution but caps confidence in generality beyond real estate interiors.

### Minor

1. **No evidence that the upsampler preserves camera alignment**: The paper states (line 178) that "the $288\times512$ upsampler already accurately follows the camera motion of a low-resolution video" and keeps it frozen. No quantitative evidence (e.g., camera pose error on upsampled output vs. base output) is provided to support this claim. The paper does acknowledge this as a limitation in the conclusion (line 283), which partially mitigates the concern, but a brief analysis would strengthen the paper on its own terms.

2. **Camera pose accuracy metric is an indirect proxy**: The evaluation uses ParticleSfM to estimate poses from generated videos and compares those to input trajectories, normalizing scales to address COLMAP's scale ambiguity (line 228-229). This measures "do generated videos look sufficiently like real videos that SfM can recover the intended poses?" — a reasonable proxy — but it is not a direct measure of camera controllability. Noisy geometry in generated frames could confound SfM estimates, and the metric cannot distinguish between a model that executes camera motion perfectly but introduces geometry artifacts vs. one that follows poorly but produces SfM-friendly frames. The paper follows CameraCtrl's pipeline, so this is not a unique flaw, but the caveat merits more prominence.

### Trivial

None.

## Nice-to-Haves

- Report variance (standard deviation or per-scene breakdown) for the camera pose metrics rather than just point estimates.
- Test on one additional domain beyond real estate interiors (e.g., a subset of dynamic YouTube videos with known camera paths or a synthetic dataset with ground truth) to demonstrate broader applicability.
- Provide a diagram showing exactly which layers are frozen vs. newly added for easier comprehension of the architecture (Equation (7) is dense).

## Removed Points

These points from the reviews were removed with justification:

- **"Open source plans not mentioned"** — Per hard rule: questioning existence/availability of any cited model/tool is not valid criticism. The paper cites SnapVideo, MotionCtrl, and CameraCtrl as publicly available; this is sufficient.
- **"Missing learning rate schedule for baselines"** — The paper states all models were trained for the same number of iterations with the same optimizer (LAMB) and learning rate schedule (lines 180-181, 238). Even if the baselines used different hyperparameters, this is a minor detail that would not change the core results.
- **"Comparison to U-Net-based models on their native architecture would strengthen the paper"** — Scope creep. The paper's contribution is about enabling camera control for *transformer* models; comparing to U-Net models on their own architecture is a different evaluation axis and not required.
- **"Too few user study participants"** — The critic themselves notes 20 is acceptable. Pure speculation that more would change results.
- **"Missing appendix/proofs"** — Parser strips these from all papers; they exist in the original submission.
- **"Formatting/style nitpicks"** — Parser artifacts, not author errors.

## Novel Insights

The reviews surface a tension: the paper's strongest evidence (user study showing 82%/78% preference) and its most significant weakness (uncertainty about baseline fairness) are tightly coupled. The user study demonstrates clear *relative* preference over the adapted baselines, but absent evidence that those baselines received a best-effort adaptation to the transformer setting, the magnitude of the *absolute* improvement is uncertain. This is a common challenge when adapting prior methods to a fundamentally different architecture (U-Net decomposed spatiotemporal → transformer joint spatiotemporal) — it is inherently difficult to know whether the gap is structural or engineering. A productive path forward would be to provide evidence that the baselines plateaued in training (e.g., loss curves or validation metrics over iterations) to argue that further tuning would not close the gap. The paper currently provides equal training budget but not convergence evidence. Beyond this, the reviews converge on the core contribution being solid and timely.

## Suggestions

1. **Provide convergence evidence for baselines**: Show that the MotionCtrl and CameraCtrl adaptations reached a plateau (e.g., training/validation loss curves, or camera pose error over training steps) to demonstrate that the comparison reflects a genuine architectural advantage rather than undertuning.

2. **Add at least one out-of-domain evaluation**: Test on a non-real-estate dataset (e.g., a subset of dynamic videos with camera metadata, or a synthetic dataset with known ground-truth poses) to substantiate the claim of general applicability.

3. **Include a brief upsampler analysis**: Compute camera pose error on base vs. upsampled outputs for a small set of examples to either validate or quantify the claim that the upsampler preserves camera alignment.
