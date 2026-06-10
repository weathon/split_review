## Summary

This paper proposes Mono-DynGS, a framework for joint camera pose estimation and dynamic scene reconstruction from monocular video without known camera poses. It introduces (1) a relative pose initialization module using local 3DGS optimization on adjacent frame pairs, and (2) a Hexplane-based Gaussian field that shares spatial plane features between static and deformable branches. Experiments on DyCheck, NVIDIA DynamicNeRF, MPI Sintel, and DAVIS evaluate both view synthesis and pose estimation.

## Strengths

- **Relative pose initialization via local 3DGS is an efficient and well-motivated approach to bootstrapping camera poses in dynamic scenes.** The ablation (Tab. 4, rows 1 vs. 2) shows this initialization improves both reconstruction metrics on DyCheck and pose metrics (ATE/RPE) on MPI Sintel relative to training from scratch. The paper reports ~70 minutes for 80 frames, and Tab. 5 shows lower total training time than all compared methods (RoDynRF ~20h, DGMarbles ~5h) — a concrete efficiency advantage.

- **The Hexplane-based Gaussian field shares spatial planes between static and deformable branches**, which is architecturally more unified than prior work (e.g., RoDynRF uses completely separate TensorRFs with no information sharing). The ablation confirms that the triplane deformation field outperforms a simple MLP baseline (Tab. 4, rows 4 vs. 5), providing quantitative support for this design choice.

- **The geometric regularization suite is clearly specified with explicit equations (Eqs. 12–14)** and targets genuine difficulties in monocular dynamic reconstruction: reprojection loss using RAFT optical flow, depth alignment loss with per-frame scale correction, and ARAP rotation smoothness loss guided by CoTracker trajectories. These are concrete, implementable regularizers rather than vague mentions.

## Weaknesses

### Fatal
None.

### Major

- **The source of the static/dynamic mask $M_s$ is never specified, creating a reproducibility gap.** The mask is critical to the method's operation: the static Gaussian field is supervised only through $M_s$ (Eq. 11, line 112–113), the relative pose initialization is conducted "only on the static part of images" (line 75), and the deformable field uses $M_d = 1 - M_s$ (line 149). Yet the paper never explains how $M_s$ is obtained — whether from an off-the-shelf video object segmentation model, motion magnitude from optical flow, or manual annotation. This is especially problematic because the relative pose initialization (Sec. 3.2) needs static-region identification before any scene model exists — a chicken-and-egg problem the paper does not acknowledge. Without this specification, the method cannot be reproduced, and it is impossible to assess how much performance comes from the proposed representation versus the quality of an external segmentation component.

- **The test-time pose-optimization protocol conflates pose-estimation ability with representation quality, and it is unclear whether baselines were treated symmetrically.** The paper states (line 153): "When testing, we optimize for testing poses that maximize PSNR on testing images, while keeping the Hexplane-based Gaussian field unchanged." This means the held-out test image is used to find the optimal camera pose, and then render quality is measured at that optimized pose. This measures a joint pose-optimization-and-rendering task, not novel-view synthesis in the standard sense (generalization to unseen viewpoints with unknown poses held fixed). While the paper cites Fu et al. (2024) as precedent, this is a limitation of the COLMAP-free NVS paradigm that should be explicitly discussed. More critically, Tab. 1 and 2 mix methods evaluated *with* known camera poses (which receive ground-truth test poses without optimization) and methods *without* known poses (which may use different protocols). The paper should clarify whether all methods in the "without known poses" category received identical test-time pose optimization, or the comparison may be asymmetric. Until this is resolved, the headline performance claims are hard to interpret.

### Minor

- **The claim of a "unified representation" overstates the architectural departure from prior work.** The paper frames this as a key distinction (abstract, intro), but the architecture uses two separate decoder branches — a static decoder $\{\phi_s, \phi_c, \phi_q, \phi_\alpha\}$ fed by spatial planes and a deformation decoder $\{\xi_x, \xi_q\}$ fed by spatiotemporal planes — with separate losses applied through separate masks. The representation is "unified" only in that the three spatial planes are shared. This is a modest improvement over RoDynRF's completely independent TensorRFs, not a fundamentally different paradigm. The framing should be calibrated to the actual degree of sharing.

- **Sequential composition of relative poses (Eq. 6) will accumulate drift, which the paper only briefly acknowledges** ("these poses could be noisy"). The magnitude of drift and its downstream impact on final results is not quantified or analyzed. Since the global optimization stage can only partially correct drift, an analysis of residual error would strengthen the contribution.

- **Ablation results are described qualitatively without reporting numerical deltas** (e.g., "our model's PSNR increases," "reconstruction quality and pose error improve"). The actual numbers are in image-form tables (parser artifact), but even in the original submission, the text should report key effect sizes so readers can assess improvements without cross-referencing tables.

### Trivial

- The method is inconsistently named: "Mono-DynGS" in the abstract, introduction, and conclusion, but "Dy-MonoGS" in the Sec. 3 heading and line 28.
- The relative pose initialization (Sec. 3.2, line 75) requires $M_s$ to filter static regions, but $M_s$ is undefined at this stage of the pipeline — a logical inconsistency even if the practical implementation resolves it.

## Nice-to-Haves

- If the static/dynamic mask comes from an off-the-shelf method (e.g., SAM-track, motion segmentation from optical flow magnitude), naming it and ablating its quality would substantially strengthen the paper and clarify what the method contributes independently.
- The paper could more clearly articulate the two evaluation settings (standard novel-view synthesis with fixed test poses vs. test-time pose-optimized rendering) and explain what each protocol measures.
- Confidence intervals or per-scene variance for main metrics would help assess reliability across different scene types.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Tables lacking visible numerical values**: The harsh critic noted that Tab. 1–5 are rendered as images with inaccessible numbers. This is a PDF-parser artifact, not an author error. The original submission contains proper tables.
- **ARAP loss details deferred to appendix** ("More details are discussed in A," line 149): Missing appendix content is a parser-stripping artifact, not a paper flaw.
- **Reproducibility concerns about cited models/tools**: The critic questioned existence or availability of external tools (Depth Anything, CoTracker, RAFT). Per review policy, all cited references are assumed to exist.
- **Strength Finder's generic claim about "addressing an important problem"**: Dropped for being generic and lacking a specific evidence anchor.

## Novel Insights

None beyond the paper's own contributions. Both the harsh critic and strength finder converge on the same essentials: the relative pose initialization and shared-plane Hexplane representation are the core contributions; the missing mask specification and ambiguous evaluation protocol are the key weaknesses. No reviewer identified an angle that the paper's own analysis missed.

## Suggestions

1. **Specify how $M_s$ is obtained.** This is the single most important missing detail for reproducibility. If it comes from an external method (flow magnitude thresholding, video object segmentation, or a pretrained model), name it, cite it, and ideally ablate its impact.
2. **Clearly discuss the test-time pose optimization protocol.** Explain that this follows the convention in COLMAP-free NVS (Fu et al., 2024). Clarify whether all baselines without known poses received identical treatment. State explicitly that this measures joint pose-and-render quality rather than pure novel-view synthesis from fixed poses.
3. **Fix the method name inconsistency** (Mono-DynGS vs. Dy-MonoGS).
4. **Report key ablation deltas in the text** (e.g., "PSNR improves from X to Y") so readers can gauge effect sizes.
5. **Quantify the drift from sequential pose composition** — e.g., report average ATE/RPE before and after global refinement.

## Score and Decision

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>