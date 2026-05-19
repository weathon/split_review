- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 3, 5, 3
Now I have a thorough understanding of the paper and the reviews. Let me produce the consolidated review.

## Summary

UniContact proposes a framework for contact synthesis on rigid and articulated objects: given a point cloud, target wrench, and robot URDF, it outputs contact positions, forces, and collision-free joint configurations. The pipeline combines contact-aware point cloud segmentation, an attention-based neural network to select contact points from feasible region sets, a convex optimization module to refine contact positions and forces, and a potential-field-based collision-free IK solver. A large dataset of 100K+ objects with seven manipulators is also contributed.

## Strengths

- **Well-formulated general problem**: The paper defines a clean, general contact synthesis problem with explicit inputs (point cloud, target wrench, robot URDF) and outputs (contact positions, forces, joint values), covering both rigid and articulated objects and arbitrary manipulators. *Evidence: Section 3 (Technical Approach) and the contributions list in Section 1.*

- **Novel pipeline combining segmentation, learning, and optimization**: The contact-aware segmentation (clustering points by wrench basis matrix, verifying region-set feasibility via convex hull) reduces learning complexity and weights small but important surface regions equally to large ones. The neural network uses multi-head attention conditioned on robot hand features and region masks for sequential point selection. *Evidence: Sections 3.1–3.2 describe the segmentation rationale and the attention-based decoder architecture.*

- **Convex optimization for joint contact position and force refinement**: The fine-tuning module (Section 3.3) formulates a convex subproblem (Eqn. 3) via Taylor expansion that linearizes the grasp mapping matrix, enabling joint optimization of contact positions and forces with convex constraints (friction cone, step bound). This is a technically clean design for refining network predictions.

- **Collision-free IK solver using artificial potential fields**: The two-stage solver (Section 3.4) first attaches fingertips to target points, then uses a gradient-based update with Jacobian projection to push other links away from the object surface via a signed-distance potential. This is a principled approach to a practical problem.

- **Large-scale, diverse dataset**: The dataset comprises 100K+ objects from five sources (Objaverse, ShapeNet, ABC, Thingi10K, GAPartNet) across 1K+ categories, with seven manipulators and millions of training examples generated via hierarchical sampling. *Evidence: Section 4.*

- **Demonstrated generalization to a novel manipulator**: The M-Allegro Hand (standard Allegro with one finger removed, unseen during training) achieves competitive results in Table 1, suggesting the framework can adapt to novel gripper geometries.

## Weaknesses

### Fatal
None.

### Major

- **The primary baseline comparison (UniGrasp) is problematic and undermines the quantitative claims.** The paper acknowledges that UniGrasp is designed for force-closure grasps (resisting arbitrary external wrenches), whereas UniContact solves a different problem—generating contacts for a *specified target wrench*. The paper states, "Our setting's annotations aren't a good fit for UniGrasp" (Section 5.1), yet proceeds to compare and claim superiority on SR, OT, and OD without explaining how UniGrasp was adapted to this fundamentally different task (e.g., was its output post-processed? fed into the same optimization?). The reported higher performance may reflect task mismatch rather than genuine method superiority. This weakens the core experimental claim of the paper. *Verified: Section 5.1, lines 173–175.*

- **Articulated object claims are not substantiated.** The paper claims the framework "seamlessly" handles articulated rigid bodies and that "the target wrench is enough" (Section 3), but provides only one qualitative real-world example (microwave door) with no quantitative evaluation—no success rate, no wrench error, no comparison on articulated tasks. The argument that articulation "only influences which kind of wrench we should choose" (Section 3) oversimplifies the problem: manipulating articulated objects typically requires enforcing kinematic constraints (e.g., a door must rotate about its hinge) that go beyond specifying a single target wrench. Without evidence that the method respects such constraints, this claimed capability is unsupported. *Verified: Section 3, lines 45–46; Section 5.2 provides only a single qualitative mention.*

- **Evaluation lacks statistical rigor; key experiments are deferred.** Table 1 reports only single values per metric (SR, OT, OD) with no standard deviations, number of trials, or confidence intervals. Success rate is a binary metric that varies across instances; a single number tells nothing about reliability or variance. Three of six experimental questions (Q4: noise robustness, Q5: region-set ablation, Q6: real-world quantitative results) are deferred entirely to the project website. Real-world experiments are reported only as qualitative images of four objects (bottle, cup, pan, microwave) with no success rates, trial counts, or quantitative wrench errors. The claim of "extensive experiments both in simulation and in the real-world" is not supported by the evidence in the paper. *Verified: Table 1 (single values); Section 5 line 162–166 (Q4–Q6); Section 5.2 (qualitative only).*

### Minor

- **Network training details are not in the paper body.** The loss function, supervision signal (how ground-truth contact points are obtained), training hyperparameters, and test-time inference procedure are deferred to "the project website" (Section 3.2, line 87). While likely available in supplementary materials, the paper as read cannot be fully evaluated on its core learning component without these details. *Verified: Section 3.2, line 87.*

- **No analysis of optimization failure cases or iteration counts.** The paper mentions that if no feasible IK solution exists, the network is asked to produce another contact point set (Section 3.3, line 96). How often does this occur? What is the average number of re-sampling iterations? Understanding the computational cost and reliability of the full pipeline is important for practical deployment.

- **IK solver evaluation is qualitative only.** The IK solver evaluation (Section 5.1, line 181) describes a visualization (hand intersecting the cup in Stage One, correct contact in Stage Two) but reports no quantitative metrics—no penetration depth, success rate, or solve time comparison against standard IK solvers (e.g., from MoveIt). The claim that it addresses a "challenging problem" would benefit from quantitative evidence.

- **The Taylor expansion linearization (Eqn. 3) is a local approximation.** The optimization ignores second-order terms of δp and δf (Section 3.3, line 108). The paper does not discuss when this approximation may break down (e.g., for large contact position movements) or how the step bound s is chosen to ensure validity.

- **No limitations section.** The conclusion (Section 7) restates contributions without acknowledging any limitations of the approach (e.g., quasi-static assumption, point-contact only, dependence on clean point clouds, lack of dynamic effects). A brief limitations discussion would improve scientific value.

### Trivial
None.

## Nice-to-Haves

- **Enhance the baseline comparison.** Rather than comparing against a force-closure grasping method designed for a different task, the paper would benefit from reasonable baselines within the target-wrench setting: (a) random contact points + the same optimization, (b) a learning model that predicts contact points directly from point cloud and wrench without region-based selection (to isolate the contribution of segmentation and attention), (c) an optimization-only approach starting from heuristically chosen contact regions. This would directly answer whether the neural network provides useful initialization.

- **Bring deferred experiments into the main paper.** A summary of noise-robustness results and the region-set-vs-whole-point-cloud ablation (Q4, Q5) should appear in the main text with at least a small table or figure.

- **Quantify real-world performance.** Running 10–20 trials per real object and reporting success rate, mean wrench error, and failure modes would substantiate the real-world claim.

- **Report standard deviations** in Table 1 over a fixed number of test instances (e.g., 1000 per robot).

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Criticism that the "neural network model is under-specified, undermining reproducibility" (Harsh Critic #3).** The paper says training details and loss function are on the project website. The paper also states "Supplementary and Videos are on the website" in the abstract. Per the meta-review rules, content that existed in the original supplementary materials (which the parser would have stripped) should not be treated as absent. This criticism is downgraded to a Minor note about the paper body lacking these details, but it is not treated as a reproducibility failure.

- **"The extension to articulated bodies is claimed but not demonstrated" framed as a fatal/structural flaw.** This is a real gap but it does not invalidate the paper's core contribution on rigid-body contact synthesis. It is kept as a Major weakness above but not treated as fatal.

- **Generic "Strengthening the Paper on Its Own Terms" suggestions** that overlap with the Nice-to-Haves section above (better baselines, bring deferrals into main text, quantify real-world) have been consolidated into Nice-to-Haves rather than listed as standalone weaknesses.

- **Strength about "quantitative comparison showing higher success rate than UniGrasp" (Strength Finder #5)** is retained but qualified: the comparison is compromised by the task mismatch and does not cleanly demonstrate superiority.

## Novel Insights

The human review inputs do not surface a genuinely novel observation about the paper beyond what the paper itself states. The key tension is clear: the paper presents a technically well-designed pipeline (segmentation → neural network → convex optimization → collision-free IK) with a substantial dataset, but its experimental evaluation is too thin to support the breadth of its claims, particularly regarding articulated objects and comparison against baselines designed for different tasks. The reviews do not identify any hidden flaw or new connection that the paper's own discussion misses.

## Suggestions

1. **Replace or substantially augment the baseline comparison.** Drop the UniGrasp comparison as a primary result, or keep it only as a supplement with a clear statement of the task mismatch. Add proper within-task baselines: random contact initialization + optimization, and a learning variant without region-based masking.
2. **Add statistical reporting.** Report means and standard deviations over a fixed number of trials in Table 1.
3. **Provide quantitative evidence for articulated object manipulation.** At minimum, report success rates and wrench errors on a set of articulated objects, and clarify the kinematic assumptions (single-link manipulation, hinge constraints).
4. **Move a summary of at least Q4 (noise robustness) and Q5 (region-set ablation) into the main paper.** A small table or figure would suffice.
5. **Run and report quantitative real-world trials** with success rates over multiple attempts per object.
6. **Add a limitations paragraph** in the conclusion acknowledging the quasi-static assumption, point-contact model, and dependence on clean point clouds with normals.
7. **Report the average iteration count** for the optimization loop (how often does the network need to re-sample due to IK failure?).
