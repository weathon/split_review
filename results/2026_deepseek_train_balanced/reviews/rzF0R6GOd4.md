Here is the consolidated review.

---

## Summary

This paper proposes "SDF flow"—the temporal derivative of the signed distance function—as a representation for 3D reconstruction of dynamic scenes from multi-view video. The SDF at any time is obtained by integrating the SDF flow from an initial frame. The paper derives a linear relationship between SDF flow and scene flow (Theorem 2 → Eq. 12), enabling scene flow recovery by solving a least-squares system, and integrates this into a NeRF-based reconstruction pipeline. Experiments on 5 clips from the CMU Panoptic dataset show consistent improvement over NDR and Tensor4D on geometry metrics.

## Strengths

- **Consistent quantitative improvement across all benchmark scenes.** Table 1 shows the proposed method outperforms both NDR and Tensor4D on all 5 CMU Panoptic sequences across all three metrics (accuracy, completeness, overall). The improvement holds for every individual scene, which is a stronger signal than an average-only result. This provides genuine evidence that the overall pipeline advances the state of the art on this benchmark.

- **Scene flow recovery from SDF flow without direct flow supervision.** The linear system derived in Eq. 12 (combining Theorem 2 with the local-rigidity assumption) allows recovering scene flow parameters analytically from the learned SDF flow. Table 2 and Figure 8 demonstrate that the projected scene flow yields optical flow that better matches RAFT estimates than NDR's scene flow. This is a non-trivial consequence of the SDF flow representation.

- **Principled temporal formulation via integration.** Rather than predicting SDF independently per time step (which discards temporal structure), the method models SDF flow and integrates it (Eq. 5) using a second-order Runge-Kutta scheme. This imposes temporal smoothness by construction and allows the network to focus on modeling *change* rather than memorizing full SDF fields per frame. The 2D toy example (Figure 4b) empirically validates the consistency of the SDF-flow/ scene-flow relationship.

## Weaknesses

### Fatal
None.

### Major

1. **Theorem 2 is the well-known level-set equation, presented without acknowledgment.** Theorem 2 states ∂s/∂t = −(∂x/∂t)ᵀ n(x). For a signed distance function (|∇s| = 1, enforced by the paper's own eikonal constraint), this is exactly the level-set equation ∂φ/∂t + v·∇φ = 0 (Osher & Sethian, 1988; Sethian, 1999). The paper presents this as a new "Theorem" with a full proof in the appendix and claims "revealing this relationship" as a contribution (lines 17–18), but neither cites the level-set literature nor acknowledges that this is a known result. While operationalizing this relationship in a NeRF context and deriving the specific linear system (Eq. 12) for scene-flow recovery from SDF flow is a valid contribution, the framing overstates novelty. The paper would be stronger by honestly contextualizing Theorem 2 and focusing novelty claims on the SDF-flow representation itself and the linear-system formulation for scene flow.

2. **No ablation studies.** The paper proposes a novel representation (SDF flow) and a pipeline with multiple interacting components (SDF-flow network, initial-SDF network, eikonal constraint, integration scheme, scene-flow regularization via the derived linear relationship). Yet there is not a single ablation experiment. Critical ablations missing include: (i) learning s(x,t) directly (without the temporal-derivative parameterization) under matched capacity and budget—this is the cleanest test of whether the SDF-flow representation itself provides value; (ii) removing or varying λ (set to 0.1 without justification); (iii) removing the scene-flow regularization; (iv) using different integration schemes. Without these, attributing the reported improvements to the SDF-flow representation specifically, rather than to other implementation choices, is not possible.

3. **Narrow experimental evaluation relative to the strength of the claims.** The evaluation covers 5 clips of 24 frames each from a single dataset (CMU Panoptic), all containing human-centric activities, using only 10 camera views, compared against only two baselines (NDR, Tensor4D). The paper claims "state-of-the-art performance" (lines 5, 232), but the evidential basis for such a broad claim is thin: the temporal window is short (barely more than a snapshot for a method centered on temporal derivatives), the diversity of scene types is limited (no non-human motion, no topology-changing objects like liquids, no natural scenes), and the baseline set omits methods like DynamicFusion-class approaches that could be informative even if they require depth (the CMU Panoptic dataset provides depth maps used for ground truth). A method presented as a general dynamic-scene representation should demonstrate generality across more varied conditions.

### Minor

4. **Optical flow evaluation uses RAFT estimates as pseudo-ground truth.** The paper uses optical flow from RAFT as pseudo-ground truth (line 225) to evaluate scene flow. This measures agreement with a learned 2D optical-flow estimator, not physical 3D motion. RAFT has its own failure modes and biases, so a method that produces flow fields that happen to resemble RAFT's output could rank higher regardless of physical correctness. The paper is transparent about this limitation, but it remains a significant evidential gap—especially since the CMU Panoptic dataset has RGB-D sensors whose depth maps could in principle support 3D scene-flow evaluation, even if that itself is non-trivial.

5. **Computational cost is not contextualized or discussed as a limitation.** Training takes "around 7 days on 2 NVIDIA 4090 GPUs for ten 1920×1080 videos of 24 frames" (line 197). This is a significant requirement (roughly 336 GPU-hours for 240 images). The paper does not report training times for the baselines on the same hardware, nor does it mention inference speed beyond "~1.5ms per ray," and the conclusion has no limitations discussion. For a practical reconstruction method, these numbers need contextualization.

6. **No discussion of failure cases or method limitations.** The paper lacks any limitations section or discussion of when the method might fail—e.g., scenes with rapid motion (violating the smoothness assumption), large topological changes, or motions where the local-rigidity assumption (Assumption 1) is violated (stretching, shearing, fluid-like deformations). Including such discussion would strengthen the paper's scientific rigor.

### Trivial

- Evaluation metrics in Table 1 are reported without variances or confidence intervals across frames and scenes, making it difficult to assess the significance of improvements.
- The MLP architecture (number of layers, hidden dimensions, activation functions) is not specified in the implementation details, reducing reproducibility.
- The balancing weight λ is reported (0.1) but not motivated or studied.

## Nice-to-Haves

- Comparing against a version of the same pipeline that learns s(x,t) directly (same architecture, same budget) would be the most informative ablation and would directly test the value of the SDF-flow representation.
- Including non-NeRF dynamic reconstruction methods (e.g., DynamicFusion) for comparison on the CMU Panoptic data, even if only qualitatively, would help contextualize the method against the broader dynamic reconstruction landscape.
- Reporting per-frame breakdowns of the metrics would help assess temporal consistency.

## Removed Points

- **"If RAFT is treated as ground truth, why not use it as supervision during training?"** — This point misunderstands the paper. Using RAFT for evaluation (relative comparison) is categorically different from using it as training supervision (which would bias the learned representation toward mimicking RAFT). Removed as a strawman.
- **"One could compute a genuine 3D scene-flow ground truth from those depth maps over time."** — Computing scene flow from depth maps is itself a research problem (non-rigid registration) with its own failure modes, not a turnkey operation. This speculative claim does not constitute a concrete weakness. Removed.
- **"K-Planes, HexPlane, and dynamic 3D-Gaussians (4D-GS) have appeared... The paper does not acknowledge how the method compares on training speed."** — These methods target novel view synthesis, not geometry reconstruction. The paper's stated goal is 3D reconstruction, and the chosen baselines (NDR, Tensor4D) are the most directly comparable methods that also evaluate geometry. Removed.
- **Strength claim about "novel mathematical derivation linking SDF flow to scene flow"** — This strength conflicts with the verified weakness that Theorem 2 is the well-known level-set equation. The linear-system formulation (Eq. 12) remains a contribution, but the framing of Theorem 2 as a novel derivation is not supported. Demoted from strengths.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add ablation studies that isolate the SDF-flow representation from other design choices (direct SDF prediction baseline is the most important).
2. Acknowledge Theorem 2 as the level-set equation, cite the relevant literature (Osher & Sethian 1988, Sethian 1999), and reframe the novelty claim to focus on the application in NeRF and the linear-system formulation for scene flow (Eq. 12).
3. Replace or supplement the RAFT-based optical flow evaluation with a 3D scene-flow metric that uses the available depth maps, or at minimum add a detailed discussion of the limitations of using a learned 2D estimator as pseudo-ground truth.
4. Add a limitations section discussing failure modes (rapid motion, non-rigid deformation violating local rigidity, topology changes beyond what's demonstrated).
5. Report training/inference times for baselines and discuss the computational cost relative to alternatives.

## Score and Decision

The paper proposes a conceptually interesting idea (SDF flow) and demonstrates consistent improvement on a standard benchmark. The core representation and the linear-system derivation for scene-flow recovery are genuine contributions. However, the empirical validation has significant gaps—most critically, the complete absence of ablation studies makes it impossible to attribute improvements to the SDF-flow representation specifically, and Theorem 2 is presented as a novel result without acknowledging that it is the well-known level-set equation. The narrow evaluation scope (5 short clips, all human-centric, 2 baselines) does not support the broad "state-of-the-art" claim. These weaknesses are fixable but require substantial additional experiments and more honest contextualization. The paper is not ready for acceptance in its current form.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>