- Decision: Reject
- Avg Score: 3.67
- Scores: 3, 3, 5
Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper proposes a dense RGB-D SLAM system that couples an implicit multi-resolution TSDF hash grid with explicit 3D Gaussian ellipsoids. The hybrid map provides continuous geometric constraints that improve depth estimation and pose accuracy, while dynamic management of ellipsoids (submapping, fixing, deleting) keeps computation manageable. On the Replica dataset, the method achieves 0.30 cm ATE RMSE — best among 3DGS-based methods — while running at 45.1 FPS, which is 30× faster than SplaTAM and 8× faster than GSS.

## Strengths

1. **State-of-the-art tracking accuracy combined with dramatic speedup over prior 3DGS-based SLAM.** On the Replica dataset, the method achieves the best average ATE RMSE (0.30 cm) among 3DGS-based methods, outperforming GSS (0.50 cm) and SplaTAM (0.41 cm), while running 45.1 FPS on room 0 versus 2.7 FPS (GSS) and 14.5 FPS (SplaTAM) — a 30× speedup over SplaTAM and 8× over GSS (Tables 1 and 4 in the paper, as described in Sections 4.2 and 4.3). This directly validates the claim of state-of-the-art tracking at dramatically higher speed.

2. **Hybrid map representation significantly improves depth estimation on novel views.** The ablation study (Table 5) on Replica room 0 shows that adding the implicit TSDF hash grid constraint reduces Depth L1 on training views from 0.86 cm to 0.56 cm and on novel views from 1.24 cm to 0.84 cm. This quantitative evidence supports the paper's central claim of enhanced generalization for depth estimation — a direct benefit of the geometric constraint that prior 3DGS-based SLAM methods lack.

3. **Systematic ablation demonstrates that each key component (hybrid map, keyframe selection, bundle adjustment) contributes to tracking improvement.** Table 6 on ScanNet scene 0000 shows ATE RMSE dropping from 7.83 cm (no hybrid map) to 3.74 cm (with hybrid map), then to 1.58 cm (adding keyframe selection), and finally to 0.73 cm (adding bundle adjustment). This careful isolation of contributions is a strength over many SLAM papers that only report end-to-end results.

4. **Principled dynamic Gaussian ellipsoid management keeps model size competitive.** Section 3.3.1 describes a clear pipeline: submaps from recent keyframes bound the active ellipsoid count, and ellipsoids are fixed or deleted based on opacity, gradient, and TSDF thresholds. Table 4 confirms that model parameters on Replica room 0 (32.7 MB) are only slightly higher than GSS (26.8 MB) and lower than SplaTAM (33.8 MB), despite the system being substantially faster — evidence that the management strategy is effective without bloating storage.

5. **Evaluated on three standard datasets (Replica, ScanNet, TUM) with multiple runs.** Results are averaged over five random runs, and comparisons include both 3DGS-based methods (SplaTAM, GSS) and NeRF-based methods (NICE-SLAM, ESLAM, Co-SLAM), as well as classical baselines (ORB-SLAM2, Kintinuous, BAD-SLAM).

## Weaknesses

### Fatal

None.

### Major

1. **No speed ablation for the headline "30× faster" claim.** The paper's most practically significant claim — operating up to 30× faster — is presented only as an end-to-end result (Table 4) without decomposing the speedup across components. The system-level contributions (TSDF hash grid constraint, SH-0, Gaussian submapping, fixation/deletion heuristics) all affect runtime, but their individual contributions are not disentangled. Table 6 (system ablation) abates tracking accuracy only, not FPS. Without such a decomposition, the reader cannot tell whether the speed advantage comes primarily from the core geometric TSDF constraint, from the reduced rendering cost of zero-order SH, or from the aggressive Gaussian management heuristics. The statement in Section 4.4 that HM improves accuracy "when operating at nearly the same speed" is a useful qualitative observation but does not constitute a quantified speed ablation.

2. **Numerical values for nearly all hyperparameters are omitted.** The paper introduces multiple thresholds (τₒ, τₛ, τₔ, τₜ, τ₉, τₛ₁, τₘ, dₜ) and loss weights (λ꜀, λₔ, λ_ḏ, λᵣ, λᵢₙ, λₒᵤₜ) but never provides their numerical values. The Gaussian fixation criterion (Eq. 8) and initialization criteria (Section 3.3.1) are defined only symbolically. The keyframe decision threshold τₘ and the "top Nₖ most relevant frames" criterion for bundle adjustment are described without specifying how relevance is measured. These omissions make the system difficult to reproduce and impossible to assess for hyperparameter sensitivity.

### Minor

1. **SH-0 confound for the GSS speed comparison.** The paper sets spherical harmonic order to zero (Section 3.1, line 81). GSS uses higher-order SH in its default configuration. Since SH order directly affects per-Gaussian compute and memory, a portion of the 8× speedup over GSS may be attributable to this design choice rather than to the TSDF constraint itself. This does not affect the 30× claim against SplaTAM (which also uses SH-0), but it weakens the decomposition of the GSS comparison. The paper does not acknowledge or quantify this factor.

2. **"Implicit training converges quickly" is stated as reasoning, not empirically supported.** At the end of Section 3.2 (line 127), the paper says "This explains why implicit training converges quickly and enforces stronger constraints." This is presented as deductive reasoning about one-to-many vs. one-to-one constraints, but no convergence curves or empirical comparisons of convergence rates are provided. This is a minor gap — the claim is plausible and not central to the paper's contributions, but it is presented as a factual strength without evidence.

3. **Post-training map conversion to explicit 3DGS is mentioned but not demonstrated.** Section 4.3 states that "once training is complete, our method can transform our map into an explicit 3DGS map through a one-time query." This is presented as a useful feature, but no quantitative results (conversion time, resulting rendering quality vs. the hybrid map) are reported, and no comparison to baselines is made.

### Trivial

None.

## Nice-to-Haves

- A brief justification of the opacity conversion formula (Eq. 2) from TSDF, beyond citing prior work.
- A concrete, measurable definition of the "inductive biases" that the TSDF constraint is claimed to mitigate, with targeted experiments showing reduction of specific artifacts (e.g., floaters, depth inconsistencies in novel views), beyond the qualitative Figure 1.
- A controlled comparison where GSS is also run with SH-0 to isolate the speed contribution of the TSDF constraint vs. SH order.

## Removed Points

These points were flagged by reviewers but are removed from the main assessment for the reasons below:

- **"Tables are presented as images and cannot be inspected quantitatively"** — This is a parser artifact from the text extraction. The original PDF renders tables correctly; the extracted text format is not the authors' fault.
- **"Baselines may not have been run on the same hardware / with the same iterations or keyframe frequency"** — Speculative. The paper states its hardware (RTX 3090, i7-12700) and follows standard evaluation protocol. It is standard practice to run all methods on the same machine. No evidence suggests otherwise.
- **"Opacity conversion from TSDF lacks justification"** — This is a minor presentation suggestion, not a weakness. The formula is taken from prior work (Or-El et al., 2022; Johari et al., 2023), which is standard practice.
- **Missing related works** — Per guidelines, the reviewer cannot determine what related works exist or are missing without external sources.
- **Formatting/style nitpicks** — Various minor presentation concerns are parser artifacts or subjective preferences.

## Novel Insights

None beyond the paper's own contributions. The two reviews largely converged on the same set of issues (speed decomposition, SH-0 confound, missing thresholds) and strengths (hybrid map novelty, SOTA accuracy + speed, thorough ablation). The harsh critic's framing of the speed claim as being potentially attributable to engineering choices rather than the core geometric idea is the most incisive observation, though it overstates the concern by not distinguishing between the SplaTAM comparison (30×, unaffected by SH-0) and the GSS comparison (8×, partially affected).

## Suggestions

1. **Add a dedicated speed ablation.** Starting from a minimal 3DGS baseline (e.g., a stripped SplaTAM-like renderer), add each component (SH-0, TSDF hash grid constraint, Gaussian submap, fixation/deletion) one at a time and report FPS and ATE after each addition on at least one scene. This would isolate the speed contribution of the core geometric constraint from the auxiliary engineering and significantly strengthen the paper's central claim.

2. **Add a table of all hyperparameter values** (thresholds τₒ, τₛ, τₔ, τₜ, τ₉, τₛ₁, τₘ, dₜ, loss weights λ, and the number of hash grid levels L, sampled points Nᵤ/Nₔ, etc.) to the appendix or main paper.

3. **Define the "top Nₖ most relevant frames" criterion** for bundle selection — specify whether relevance is measured by pose distance, feature overlap, or another metric.

4. **Quantify the SH-0 effect on speed** by either running GSS with SH-0 (reporting any accuracy degradation) or adding a sentence acknowledging the confound and estimating its magnitude.

5. **Add convergence curves** (loss vs. iteration) for implicit vs. explicit training to substantiate the convergence claim, and report post-training map conversion time/quality to substantiate the explicit-conversion feature.
