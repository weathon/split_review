Now let me run the bracketing calibration search.Round 1 bracket: **between 5.5 and 7.5.** The paper is clearly above the weak anchors (score ≤ 3 reject papers) and somewhat below the strongest anchors (score 8). Now let me narrow within that bracket.Now I have enough information to write the final review. Let me synthesize everything.

---

## Summary

CasualHDR proposes a unified 3DGS-based framework for HDR 3D scene reconstruction from casually captured auto-exposure video, jointly optimizing a continuous-time SE(3) B-spline camera trajectory, per-frame exposure times, a camera response function (CRF), and an HDR 3D Gaussian scene representation. The core insight is that both motion blur and image brightness are direct functions of the camera's exposure time, enabling unsupervised Δt estimation from random initialization. The method is evaluated on a new synthetic Blender dataset and a self-captured real-world CasualVideo dataset.

---

## Strengths

- **Unified physical imaging model with joint optimization**: Equations 4–5 formalize the integration of exposure time, CRF, and continuous camera motion into a single differentiable model. The ablation in Table 6 directly quantifies each component's impact: joint exposure+CRF optimization contributes ~42% PSNR improvement and continuous trajectory contributes ~24%, confirming all modules are necessary and non-redundant.

- **Continuous SE(3) B-spline across the entire video**: Unlike prior deblurring methods (following BAD-NeRF) that fit short per-frame splines, CasualHDR estimates one trajectory for the whole video (Section 3.2), enabling cross-frame motion constraints. This is a technically sound choice for the casual-video setting and is well-motivated in the related work discussion.

- **Strong quantitative results on synthetic data**: Table 1 shows CasualHDR-random achieves 31.8 / 27.8 PSNR on Trolley / Pool vs. 20.3 / 18.7 for the best competing method (BAD-Gaussians), a decisive margin on a clean evaluation benchmark.

- **Novel insight linking motion blur to exposure time**: The paper explicitly states and mechanically grounded in its model that blur magnitude is an indicator of exposure time (Section 1 and 3.3). This insight has not been formalized in the 3DGS literature and enables truly unsupervised Δt recovery.

- **New challenging dataset with ground-truth validation**: The CasualVideo dataset includes Intel RealSense and Google Pixel 8 Pro sequences with measured (hardware-extracted) exposure times and Vicon motion-capture ground-truth poses for two sequences — enabling credible pose accuracy evaluation in Table 4.

- **Three practical downstream applications demonstrated**: Post-reconstruction HDR editing (Figure 3), input image deblurring (Figure 6–7), and novel-view synthesis are all concretely shown, broadening the method's practical value.

---

## Weaknesses

### Fatal

None.

### Major

- **Real-world evaluation protocol lacks defined methodology** — Section 4.4 states: "Due to the fact that most images in real-world datasets are blurry, we select 5 to 10 sharp images for each sequence to evaluate metric." No criterion for "sharp" is given, nor is it stated whether selection was made before or after examining method outputs. This matters for two reasons: (1) if selection was performed after observing CasualHDR's deblurred outputs, it is circular (frames CasualHDR handled well are evaluated, frames it failed are excluded); (2) even without circularity, restricting evaluation to pre-selected sharp frames removes the diagnostic cases the deblurring mechanism is meant to handle, making the reported NVS numbers non-representative of the typical input. A clear sharpness metric (e.g., Laplacian variance threshold), applied uniformly and blindly to all methods, is needed before the real-world numbers in Table 2 can be taken at face value.

- **Central claim lacks direct numerical validation** — The paper's core technical claim is that "camera motion blur can serve as an indicator of the exposure time" (Section 1) enabling Δt estimation from random initialization. Table 6 ablation shows that *having* exposure optimization contributes ~42% PSNR improvement, but nowhere does the paper show *how accurately* Δt is recovered. The synthetic dataset has ground-truth exposure times per frame (Section 4.1: "images were assigned random exposure times"), making a plot or table of estimated vs. ground-truth Δt per frame straightforwardly achievable. Without this, the mechanism is mechanically plausible but numerically unverified — the ablation only shows that the optimization variable matters, not that it converges to a meaningful physical value.

### Minor

- **"One-stage" framing is potentially misleading** — The abstract and contributions bold "one-stage method," but Section 4.2 specifies that HLoc or DPV-SLAM initialization is required before optimization, and that HLoc fails on Smartphone sequences requiring DPV-SLAM fallback. While the internal optimization is end-to-end, this mandatory external preprocessing stage is non-trivial and not characterized in terms of failure sensitivity. Calling this "one-stage" relative to methods that require manually curated multi-exposure brackets is understandable, but the claim should be qualified.

- **WB/TM factorization creates a potential degeneracy between per-frame variables** — Equation 5 decomposes the CRF as TM ∘ WB, where WB is per-frame (three scalar coefficients per frame) and TM is a global shared MLP. Both the WB coefficients and Δt are per-frame optimizable quantities that affect image brightness. Without explicit regularization or constraint coupling WB to a white-balance prior and Δt to the motion blur signal separately, the two factors can compensate each other, absorbing brightness variation without enforcing physical meaning on Δt. The paper does not discuss this potential degeneracy or how optimization avoids it.

- **Synthetic CRF is an oracle for the CRF module** — Section 4.1 states synthetic LDR images are generated using "the tone-mapping function from HDR-NeRF." The CRF module uses per-channel MLPs (Section 3.3). If these MLPs are expressive enough to exactly recover the HDR-NeRF TM function, the synthetic CRF evaluation tests interpolation rather than generalization. This does not invalidate the deblurring or exposure estimation results, but it means the CRF recovery performance on synthetic data is less diagnostic than it appears.

### Trivial

- Table 6 reports improvements as percentages (e.g., "42% improvement in PSNR," "24% improvement"). Since PSNR is a log-scale metric, these percentages are unintuitive without the baseline absolute PSNR values. Reporting absolute values alongside the percentages would make the ablation more interpretable.

---

## Nice-to-Haves

- A per-frame plot of estimated Δt vs. ground-truth Δt on the synthetic dataset would directly validate the core mechanism and characterize the regime where estimation degrades (e.g., nearly static frames with very short exposure).
- Ablation of N (number of virtual cameras, fixed at 10 in all experiments per Section 4.2) vs. rendering quality and training time.
- A brief robustness-to-initialization experiment (e.g., perturbing SfM poses on one sequence) would provide concrete support for the "robust" claim in the title.
- Specification of CRF MLP architecture (depth, activation, monotonicity enforcement).

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic: "Baseline comparison is overclaimed"** — REMOVED. The paper explicitly acknowledges in Section 4.3 that no existing baseline targets the same problem formulation and that the closest work (I²-SLAM) is not open-sourced. Framing wins over baselines designed for easier sub-problems is standard practice for novel-task papers and is necessary given no directly comparable open-source baseline exists.

- **Harsh Critic: "HDR-NeRF failure mode uncharacterized"** — REMOVED. Section 4.3 clearly states HDR-NeRF requires precise exposure times and fixed-position multi-exposure stacks. Its failure on all real sequences is explained by design, not by fragility of the method itself.

- **Harsh Critic: "Conclusion doesn't discuss limitations"** — REMOVED as a pure presentation nitpick without substantive impact.

- **Strength Finder: "State-of-the-art across multiple benchmarks"** — MODIFIED. Retained for synthetic data (Table 1, clean evaluation) but qualified for real-world results (Table 2) due to the sharp-frame selection issue.

---

## Novel Insights

The paper's most genuinely novel analytical contribution is the formalization of motion blur as a self-supervising proxy for camera exposure time — the physical observation that blur magnitude and image irradiance are both monotone functions of Δt creates a joint constraint that pins the otherwise unobservable per-frame shutter speed without any external metadata. This insight is not merely used as motivation but is architecturally embedded: exposure time is a first-class optimizable parameter jointly constrained by the photometric loss and the physical motion-blur formation model. The cross-frame continuous SE(3) B-spline trajectory (as opposed to per-frame splines in prior deblurring methods) is also a meaningful contribution that leverages video temporal coherence for more stable reconstruction, an approach applicable beyond the HDR setting to any 3DGS reconstruction from temporally ordered degraded video.

---

## Suggestions

1. Define the sharp-frame selection criterion for the real-world evaluation explicitly, apply it with a computable metric (e.g., Laplacian sharpness threshold), and confirm it was applied before inspecting per-method results.
2. Add a table or figure on the synthetic dataset comparing estimated Δt to ground-truth Δt per frame, including a failure-mode analysis (e.g., near-static frames).
3. Discuss the WB/TM degeneracy explicitly and either add a regularizer or show empirically (e.g., per-frame WB values) that the factorization is well-behaved in practice.

---

## Score and Decision

**Calibration anchors:**

| Path | Avg Score | Round | Comparison |
|---|---|---|---|
| NLRo4qhg6t.md | 3.0 | R1-low | Rejected NeRF training acceleration — far weaker contribution, no novel problem formulation |
| uqYjAQ5diD.md | 3.0 | R1-low | Rejected NeRF mapping — limited novelty, narrow scope |
| rDIf6NA5mj.md | 6.0 | R1-mid | Accepted exposure bracketing restoration — different domain (2D, not 3D), comparable evaluation quality |
| Wvi8c0tgvt.md | 6.67 | R1-mid | Accepted 3D blur augmentation — related topic but narrower scope, no new scene representation |
| bLKcCe7hYh.md | 5.8 | R1-mid | Accepted UC-NeRF under-calibration — comparable problem difficulty, slightly weaker insight |
| P4o9akekdf.md | 8.0 | R1-high | Accepted NoPoSplat feed-forward unposed 3DGS — clearly stronger (feed-forward, inference-time) |
| 2prShxdLkX.md | 6.75 | R2 | Accepted MoDGS casual video dynamic 3DGS — most topically comparable; strong experiments, clean evaluation |
| tMG6btjBfd.md | 6.0 | R2 | Accepted SplineGS B-spline dynamic 3DGS — also uses splines in 3DGS, narrower contribution |

**Round 1 bracket: 5.5 – 7.5**

**Round 2 narrowing:** MoDGS (6.75) is the closest topical anchor — both reconstruct 3D scenes from casually captured video with a special degradation-handling module. MoDGS has a cleaner evaluation and its depth estimator reliance is well-characterized; CasualHDR addresses a more novel multi-degradation problem but has the real-world evaluation methodology concern and no direct Δt accuracy validation. SplineGS (6.0) is a spline-based 3DGS paper with narrower novelty — CasualHDR is clearly above it in problem originality and experimental scale.

**Final positioning:** CasualHDR sits between SplineGS (6.0) and MoDGS (6.75), closer to MoDGS in technical sophistication but pulled slightly lower by the major real-world evaluation concern. Score: **6.5**.

**Axis summary:**
- *Originality*: High — novel problem (HDR + blur + unknown exposure in 3DGS), principled physical insight.
- *Importance*: High — enabling HDR 3D reconstruction from consumer devices is practically valuable.
- *Claim support*: Moderate — synthetic claims well-supported; real-world claims limited by cherry-picked evaluation.
- *Experiment soundness*: Moderate — ablations are strong; real-world evaluation methodology is opaque.
- *Clarity*: Adequate — physical model is clearly explained; evaluation methodology is not.
- *Value to community*: Good — new dataset, new benchmark, new problem formulation.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>