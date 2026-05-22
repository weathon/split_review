Here is the consolidated final review:

---

## Summary

CP4D presents a compositional framework for text-driven 4D scene generation that decouples the problem into static background and dynamic foreground. The pipeline follows three stages: (1) generating stylistically coherent 3D Gaussian representations of background and foreground via image editing and image-to-3D models, (2) simulating foreground motion through a hybrid strategy that combines physics solvers (MPM, rigid-body, PBD) with SDS refinement from video diffusion models, and (3) automatically composing foreground and background via a depth-aware heuristic and sequential scale/position optimization. The compositional design also enables zero-shot editing of individual scene components.

## Strengths

1. **Well-motivated compositional decomposition (Section 4, Figure 1).** Decoupling 4D generation into static background + dynamic foreground is conceptually clean and practically effective. The styling strategy (generating a background image, then editing the foreground into it before separate 3D reconstruction) avoids the common problem of style mismatch between independently generated components (e.g., realistic background + cartoon object). The editing applications in Figure 6 directly demonstrate the practical value of this design.

2. **Hybrid motion synthesis with clear ablation evidence (Section 4.2, Figure 5).** The two-step process — physics simulator for base trajectories, then SDS refinement for material parameters and displacement — is well-reasoned. The ablation study (Figure 5) is persuasive: removing material optimization leads to unstable motion from inaccurate VLM-inferred parameters, and removing position optimization produces spurious collisions from grid-approximation errors. This directly validates the necessity of both components.

3. **Strong quantitative results across multiple established metrics (Tables 1, 2).** CP4D achieves the highest scores on VBench Motion (0.998), VBench Consistency (0.972), WorldScore Photo Consistency (97.42), WorldScore 3D Consistency (95.55), WorldScore Motion Smoothness (93.52), GPT-4o Physical Realism (0.694), Photorealism (0.759), and Semantic Alignment (0.747). It outperforms both physics-driven methods (PhysGen3D, PhysGen, Omni-PhysGS) and commercial video generators (Sora, Runway). While the metrics are proxies, the consistent across-the-board improvement is substantive.

4. **Principled automated composition mechanism (Section 4.3, Figure 3).** The depth-aware heuristic (Eq. 8) that constrains foreground scale via frustum containment, followed by sequential scale-then-translation optimization (Eq. 9), provides a clean solution to the under-constrained problem of placing independently generated 3D content into a scene. This is a non-trivial engineering contribution that the quantitative results support.

## Weaknesses

### Fatal
None.

### Major

1. **Evaluation on only 17 examples with no variance or significance reporting (Section 5.1).** The paper states "We curate a dataset of 17 examples for evaluation" but reports no confidence intervals, standard deviations, or significance tests in Tables 1 or 2. On a dataset this small, a few favorable examples can dominate aggregate scores. Several margins are extremely narrow (e.g., VBench Motion: 0.998 vs. 0.997 for PhysGen3D; VBench Consistency: 0.972 vs. 0.966 for PhysGen), and there is no way to assess whether these differences are meaningful or noise. The paper should include per-example results, error bars, or significance tests to establish the reliability of the reported improvements.

2. **Central claim of "faithful adherence to complex physical dynamics" is not directly validated.** No evaluation in the paper directly measures whether generated trajectories obey physical laws (e.g., conservation of momentum in collisions, free-fall acceleration under gravity, correct material stiffness from stress-strain relationships). The metrics used (VBench, WorldScore) measure video quality and 3D consistency — not physical correctness. The GPT-4o "physical realism" score (Table 2), while following the standard set by PhysGen3D, is a language-model proxy for human judgment, not a measurement of physical accuracy. The physics simulator backbone grounds the method, so the claim is not unsupported, but it would be substantially stronger with any direct physics validation — e.g., comparing object trajectories against analytical solutions for simple cases (free fall, pendulum), or measuring parameter recovery error on scenes with known ground-truth material properties.

### Minor

1. **Limited qualitative illustration of claimed multi-material and multi-object capabilities (Figure 4).** The main paper shows only two qualitative cases: a T-shirt on a balcony (deformable) and a falling bottle (rigid). Despite claiming support for elastic, rigid, and fluid materials, and multi-object interactions, no fluid example or complex multi-object scene (with different interacting material types) is visualized in the main paper. The paper references "more results in Appendix E and F," but the appendix is stripped from this review. Showing one diverse qualitative example would significantly strengthen reader confidence.

2. **Unanalyzed tension between physics simulation and video diffusion priors.** The paper's introduction argues that video generation models "typically lack an explicit characterization of the underlying physical principles" and produce "physically inconsistent" results. Yet the method uses SDS from these same models to refine the physics simulation output. This creates a potential failure mode: the SDS gradient could pull the simulation toward visually appealing but physically incorrect dynamics. The ablation (Figure 5) shows both components improve results, but there is no controlled experiment to measure whether, or under what conditions, SDS refinement degrades physical accuracy relative to the raw simulator output. An analysis (e.g., varying the weighting of SDS vs. physics constraints, or comparing against ground-truth parameters in a synthetic setting) would address this concern.

### Trivial

- The caption in Table 1 labels the third column "Imaging†" — this should match the metric name used in the text (the paper uses "image quality" in Section 5.1).
- The "Bold: Best. Underline: Second Best" note in Table 1 uses inconsistent capitalization/formatting.
- In Equation (8), the denominator divides by 2, but the geometric rationale for this factor is not explained.

## Nice-to-Haves

- A dedicated physics benchmark (e.g., measuring whether object speeds follow free-fall acceleration, or whether collision outcomes satisfy momentum conservation) would directly support the core claim.
- Including one fluid simulation example and one complex multi-object interaction in the main paper (rather than only in appendix) would better showcase the method's full capability.
- Error bars or per-example breakdowns on the 17 evaluation examples would substantially strengthen the quantitative evidence.

## Removed Points

These points were considered and removed from the main review, with justification:

- **"Missing PhysDreamer, DreamPhysics, PhysGaussian as baselines"** — Partially incorrect. The paper cites PhysGaussian (Xie et al., 2024a) and DreamPhysics (Huang et al., 2025) in Section 2.2. The experimental comparison includes PhysGen, PhysGen3D, and Omni-PhysGS, which are the closest comparable physics-based methods. The harsh critic's claim of "critical omission" overstates the gap.
- **"Comparison with 2D video generators is inappropriate"** — The paper includes both physics-driven methods AND 2D video generators as baselines. Including Sora/Runway is standard practice for showing broader capability. The physics-driven baselines (PhysGen, PhysGen3D, Omni-PhysGS) are the primary competitors for the physics claim.
- **"Metrics cannot measure physical accuracy" as a fatal flaw** — While the metrics are indeed proxies, the method uses actual physics simulators as its backbone, and the evaluation follows the established protocol of PhysGen3D. This is a limitation worth noting (and is covered in the Major weaknesses) but does not invalidate the paper.
- **"Stage I failure points not analyzed"** — The paper acknowledges the strategy is "simple yet effective" and provides empirical results demonstrating its success. The criticism is speculative.
- **"Differentiability of physics solvers not discussed"** — The stripped appendix likely covers implementation details. MPM solvers (Hu et al., 2018, which the paper cites) are differentiable.
- **"Depth-aware heuristic assumes foreground fully visible"** — The paper explicitly states this assumption as part of the design (Section 4.3, "the foreground object should be entirely visible within the image plane"). This is a stated design choice, not a flaw.

## Novel Insights

A recurring theme across both the harsh and supportive reviews is that the paper's compositional decomposition creates a structural advantage beyond what the authors explicitly claim. By separating background from foreground, the method inherently supports novel-view rendering (since the background is a full 3D scene, not a 2D plane) and enables the editing applications shown in Figure 6. However, both reviewers also converge on the same core concern: the evaluation framework does not match the strength of the physics claim. The metrics are standard for video quality and 3D consistency, but the paper would benefit from recognizing that its primary empirical contribution is better characterized as "visually plausible physics-grounded generation" rather than "faithfully accurate physics simulation" — the latter requires direct physical validation that is not currently provided.

## Suggestions

1. **Increase evaluation size and add variance reporting.** 17 examples is small even for this field. At a minimum, report per-example scores in an appendix or include error bars. Ideally, expand to 50+ diverse examples.

2. **Add one direct physics validation experiment.** A clean test would be: generate a scene with a known physical setup (e.g., dropping a ball from a known height under gravity), compare the simulated trajectory against the analytical solution, and measure the deviation before and after SDS refinement. This would directly validate the method's physics faithfulness and calibrate the trade-off between physical accuracy and visual appeal.

3. **Include one more diverse qualitative example in the main paper.** A multi-object interaction with different material types (e.g., a rigid ball hitting a deformable cloth) would convincingly demonstrate the claimed multi-material capability without adding experimental overhead.

4. **Acknowledge and discuss the potential for SDS to degrade physical accuracy.** Even a brief qualitative analysis or a supplementary experiment would resolve the design tension that the paper currently leaves unaddressed.

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>