- Decision: Reject
- Scores: 5, 3, 3, 3

## Merged Review

### Summary
This paper addresses the problem of “symmetry mismatch” in equivariant policy learning for robotic manipulation when cameras are placed at side-views rather than overhead. The authors propose two preprocessing techniques: (1) reprojection of RGBD images to virtual top-down views by generating point clouds and interpolating missing data, and (2) perspective transformation of RGB images to map the ground plane onto a top-down view. Experiments across six simulated tabletop manipulation tasks using both reinforcement learning (SACfD) and imitation learning show that these steps improve performance of O(2)-equivariant networks compared to using raw side-view images.

### Strengths
- The paper identifies a practical problem – the performance degradation of equivariant policies due to camera viewpoint – and offers a simple, intuitive solution.
- Both methods require only camera intrinsics and extrinsics, are easy to implement, and work for RGB and RGBD without additional training data or privileged information.
- The empirical evaluation is thorough, covering multiple tasks, modalities, and baselines (2D/3D equivariant and non-equivariant methods).
- The discussion of occluded regions (RGBD) and out-of-plane distortion (RGB) adds practical considerations for real-world deployment.

**Note:** Reviewer 1 (score 5) particularly emphasized the relevance of the problem and the clarity of the presentation, while Reviewers 2‑4 (score 3 each) generally acknowledged the intuitiveness and demonstrated effectiveness but judged the contribution as limited.

### Weaknesses
- **Novelty and technical depth:** Reviewers 2, 3, and 4 considered the technical contribution minimal. The transformations (RGBD reprojection, perspective warp) are well‑established in computer vision and are applied without any adaptation for robotic‑specific challenges such as depth‑sensor noise, lighting variations, or occlusions. Reviewers 2 and 4 characterized the work as a “pre‑processing trick” or “technical report”. Reviewer 1 did not raise this concern.
- **Problem significance:** Reviewer 2 questioned whether the problem is genuinely important – if only side‑view images are available, a non‑equivariant policy might be a more natural choice. Other reviewers did not directly challenge the framing, but Reviewer 4 noted that the proposed method does not close the performance gap with the oracle top‑down view.
- **Lack of real‑world experiments:** Reviewers 3 and 4 deemed real‑world validation indispensable for a method targeting practical camera placement. All experiments are limited to six simulated environments, which are clean and lack real‑world complexities (lighting, sensor noise, dynamic backgrounds). Reviewer 1 did not comment on this.
- **Missing baselines and comparisons:**
  - For the RGB‑D camera‑angle analysis (Sec 5.6, Fig 5, Table 1), a point‑cloud equivariant baseline (e.g., PointNet++) is absent. Without it, the source of robustness (reprojection vs. inherent point‑cloud invariance) remains unclear (Reviewer 1).
  - Reviewer 1 requested comparisons with DrQ‑v2 (data augmentation) and tests on out‑of‑distribution camera viewpoints (train on one angle, test on others).
  - Reviewer 2 requested that each baseline’s concrete structure and the group on which its equivariance is defined (e.g., O(2), SO(3), SE(3)) be clearly stated.
  - Reviewer 2 also noted that all baselines share the same SACfD framework; comparisons with other state‑of‑the‑art methods (e.g., Diffusion Policy) are needed.
  - Reviewer 3 asked whether the method benefits general‑purpose robot learning methods (e.g., Diffusion Policy) and whether multi‑view RGBD point clouds (as in RiEMann [1]) would change the comparison.
- **Incomplete analysis of limitations:**
  - The performance gap with the oracle top‑down view persists; the paper does not analyze why (e.g., how much is due to occluded objects/grippers) nor explores potential mitigations such as learned inpainting or occlusion reasoning (Reviewer 4).
  - Information loss from the side‑to‑top transformation, especially depth detail, is mentioned but not analyzed; scenarios where the method might fail are not discussed (Reviewer 3).
- **Ambiguities and missing details:**
  - Are the models in Fig 7(a,b) trained and tested on the same camera angle, or tested on unseen angles? A test on held‑out viewpoints is lacking (Reviewer 1).
  - The gripper representation (Fig 11 in appendix) is crucial to understand the method; it should be moved to the main paper (Reviewer 1).
  - The sample‑efficiency advantage over the point‑cloud equivariant baseline is not clearly demonstrated – performance appears comparable in Fig 5 and Table 1. Analysis of point‑cloud resolution and density is needed (Reviewer 1).
  - Reviewer 3 requested a list of how many and which existing equivariant methods could benefit from the proposed preprocessing.
  - Reviewer 1 asked whether equivariant policies are biased toward specific action spaces (e.g., end‑effector pose, joint velocities, joint positions) and whether the gripper representation generalizes to dextrous manipulation.