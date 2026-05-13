## Summary
The paper proposes "trajectory attention," an auxiliary attention branch alongside the standard temporal attention in video diffusion models that performs attention along estimated pixel trajectories for fine-grained camera motion control. The branch inherits QKV weights from temporal attention with a zero-init output projection, allowing efficient fine-tuning (10k clips, ~24 GPU-hours on SVD). Experiments cover single-image NVS, video camera control, first-frame video editing, and an ablation supporting the two-branch + weight-inheritance design.

## Strengths
- The two-branch formulation with zero-init residual is conceptually clean, and the ablation (Table 4) gives direct architectural evidence: vanilla adaptation collapses (ATE 1.78), tuning helps (0.31), the add-on branch improves further (0.072), and weight inheritance reaches 0.0396 — isolating the contribution of each design choice.
- Reframing prior camera-control attention designs (epipolar, row-wise, flow-based) as special cases of attention-along-trajectories is a useful unification of the design space.
- Training efficiency is genuine: 10k clips and ~24 GPU-hours on a single A100 is unusually light for a controllable video generation paper.
- The 12→25-frame inference generalization (Table 1) is a non-trivial demonstration that the branch is not overfit to a fixed frame count.
- Plug-and-play composability with NVS_Solver (Table 2: ATE drops 0.357 → 0.337, FID 129.3 → 112.2) supports the claim that the branch can be combined with frame-wise optimization.

## Weaknesses

### Fatal
None.

### Major
- **Headline NVS table never compares two external baselines side-by-side with the proposed method (Table 1).** Each "frame bucket" pairs Ours with exactly one baseline (MotionCtrl at 14, Motion-I2V at 16, CameraCtrl/NVS_Solver at 25). The paper's justification (different baselines released only certain frame counts) is reasonable but it does mean readers cannot judge baselines against each other in a controlled setting. More importantly, the MotionCtrl ATE of 1.2151 vs. Ours 0.0212 (~60×) is anomalously large for a published camera-control method; the protocol for ATE/RPE (scale-aligned vs. absolute metric) is not specified in Sec. 5 or the metrics paragraph. Without this disclosure, the magnitude of the precision advantage is hard to interpret.
- **First-frame video editing claim is qualitative only.** The abstract and Sec. 5.3 explicitly claim the method "excels in maintaining content consistency over large spatial and temporal ranges" vs. AnyV2V and I2VEdit, but evidence is restricted to Fig. 7. No CLIP frame consistency, warp error, edit-fidelity, or user study is reported. As stated, the editing claim is unsubstantiated by numbers.
- **The most directly comparable trajectory-aware baselines are absent from quantitative tables.** The related-work section frames CamCo (epipolar), ViewCrafter (warped-frame inpainting), and Motion-I2V (flow-attention) as "weaker variants of trajectory-consistent constraint." This is exactly the family the paper must beat to establish the "stronger inductive bias" claim. CamCo and ViewCrafter never appear in any quantitative table; Motion-I2V appears in one isolated row. The conceptual claim is not empirically pinned.
- **No ablation against alternative inductive-bias attentions (epipolar, row-wise, flow-attention).** Table 3 ablates the architectural wrapping (branch, inheritance) but not the *form* of the inductive bias. The claim that trajectory attention subsumes/outperforms these prior mechanisms therefore rests on framing rather than experiment.

### Minor
- **Decoupling depth-warped flow from the attention mechanism.** Algorithm 3 derives the input trajectory from monocular depth + camera intrinsics/extrinsics, i.e., a richer signal than what MotionCtrl/CameraCtrl consume. The paper does not isolate how much of the precision gain stems from this richer input vs. the attention mechanism itself. A baseline that injects the same depth-warped flow into temporal attention via simple addition/cross-attention would address this.
- **FID at 230 samples is noisy.** Differences such as 103.5 vs. 108.7 vs. 115.8 lie within FID's known instability range below ~10k samples, yet the paper draws fine-grained conclusions (e.g., "MotionCtrl generates slightly better results"). No seeds, variance, or CIs are reported. Mention the caveat or expand the eval set.
- **Sparse-trajectory robustness is claimed but not measured.** Algorithm 2 back-projects to a sparse grid (uncovered pixels get zero), so coverage directly modulates trajectory signal strength. The abstract advertises support for partial trajectories, but degradation as a function of trajectory coverage is never quantified.
- **Sec. 4.2 video-control ATE references a synthetic target.** The "ground truth" trajectory is computed from the input video plus a target pose sequence (i.e., a warped reconstruction), not a measured camera trajectory. The numbers in Table 2 are meaningful as relative comparisons but should not be read as SLAM-style absolute errors; this should be stated.
- **Attention-map motivation (Fig. 2) is anecdotal.** The "temporal attention focuses on adjacent frames" claim in Sec. 3.2 is shown on a single example. A token/layer-averaged statistic would substantiate this as a general property rather than a chosen illustration.
- **Full-3D-attention generalization is qualitative only.** Sec. 4.5 supports the "extends naturally" conclusion with a single Open-Sora-Plan figure and no metrics.

### Trivial
None substantive.

## Nice-to-Haves
- A controlled head-to-head against CamCo, ViewCrafter, Motion-I2V at matched frame counts and shared eval pipeline.
- Robustness analysis to monocular depth errors (the input pipeline depends on it).
- Explicit scale-aligned vs. absolute protocol statement for ATE/RPE, plus seeds/variance.
- Performance-vs-coverage curve for sparse trajectories.

## Removed Points
*These points are flagged to be removed, treat them with caution.*

- *"Baselines tested at different frame counts is unfair / asymmetric to baselines."* The asymmetry in Table 1 is partly because some baselines only release certain frame-count checkpoints — comparing each baseline at its native setting is a defensible (not adversarial) choice. The substantive criticism (no row pairs two baselines) is retained above; the framing as bad-faith protocol design is not.
- *"Motion-I2V comparison is unfair because it only attends to the first frame."* This is a property of the baseline, not a manipulation by the authors.
- *Strength: "addresses an important problem / interesting question"* (not in the strength finder verbatim, but the "important problem" flavor) — generic, removed per filter rules.
- *Strength: "Table 1 ATE 0.0411 → 0.0396 is a dramatic improvement."* This is a 4% relative improvement on one metric in one row; calling it "dramatic" is sycophantic. Kept the table-level evidence in Strengths but rephrased.

## Novel Insights
None beyond the paper's own contributions. The unifying view that epipolar/flow/row-wise attentions are special cases of attention-along-trajectories is the paper's own conceptual contribution and is the main novel framing on offer.

## Suggestions
- Add at least one quantitative comparison against CamCo, ViewCrafter, and Motion-I2V at matched frame counts in a shared protocol; this is the central experiment the paper currently lacks.
- Report quantitative editing metrics (CLIP frame consistency, edit-region fidelity, optionally a user study) vs. AnyV2V and I2VEdit.
- Disclose ATE/RPE protocol (scale alignment, units, alignment method) and explain the MotionCtrl gap.
- Add an ablation that injects the same depth-warped flow into temporal attention via addition/cross-attention to isolate the contribution of the trajectory-attention mechanism from the contribution of the richer input signal.
- Quantify degradation under sparse trajectory coverage and under noisy monocular depth.
- Expand FID sample count or report seeds/CIs; explicitly note FID instability at n=230.

## Overall Assessment
**Originality:** Moderate-to-high. The reframing of camera control as attention-along-trajectories and the auxiliary-branch + weight-inheritance instantiation are conceptually clean.
**Importance:** Fine-grained camera control in video diffusion is an active and important problem.
**Support for claims:** Partial. The architectural claim (two branches + weight inheritance > naive adaptation) is well-supported by Table 3. The "stronger inductive bias than prior trajectory-aware methods" claim and the editing claim are not adequately supported quantitatively.
**Soundness:** The method itself is sound; the experimental case is uneven — the evaluation protocol is under-described and the most relevant baselines are absent.
**Clarity:** Reasonably clear; algorithms are well-specified.
**Value:** The two-branch trajectory-attention design is a likely-useful primitive for the community even if the empirical case is incomplete.

The paper has a real and clean methodological contribution that is partially validated, but the empirical case as presented does not establish the comparative claims in the abstract. With added quantitative comparisons against CamCo/ViewCrafter/Motion-I2V at matched settings and quantitative editing metrics, this would be a solid accept; as is, it sits at the borderline.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>