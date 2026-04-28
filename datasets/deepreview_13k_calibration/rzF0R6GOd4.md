# Neural SDF Flow for 3D Reconstruction of Dynamic Scenes

- Decision: Accept
- Avg Score: 8.00
- Scores: 8, 8, 8, 8

## Abstract
In this paper, we tackle the problem of 3D reconstruction of dynamic scenes from multi-view videos. Previous dynamic scene reconstruction works either attempt to model the motion of 3D points in space, which constrains them to handle a single articulated object or require depth maps as input. By contrast, we propose to directly estimate the change of Signed Distance Function (SDF), namely SDF
flow, of the dynamic scene. We show that the SDF flow captures the evolution of the scene surface. We further derive the mathematical relation between the SDF flow and the scene flow, which allows us to calculate the scene flow from the SDF flow analytically by solving linear equations. Our experiments on real-world multi-view video datasets show that our reconstructions are better than those of the state-of-the-art methods. Our code is available at https://github.com/wei-mao-2019/SDFFlow.git.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes an algorithm for implicit surface reconstruction in dynamic scenes. The key is to bridge the SDF flow and sceneflow by assuming the two hypothesis. Also, typically this paper requires RGBD data which is to sample points nearby surface and to make this algorithm feasible. Accordingly, this paper could be understood as 4D surface tracker.

### Strengths
This paper brilliantly bridge the concept of sceneflow and the proposed SDF flow. Based on the two assumptions, one for rigidity and the other for the linearlization (?), the proposed SDF flow is differentiably convertible into the sceneflow, which enables the network to encode sceneflow from RGBD frames. As far as my understanding, this is the pioneering work. For experiment parts, comparison with NDR (Neurips 2022) is reasonable.

### Weaknesses
W-1. Low fidelity results

Despite the novel idea, the reconstruction quality is far below my expectation. Even though the results from NDR (Neurips 2022) are also not that good enough, there are not that much dramatic change after the authors applied the proposed SDF flow.

Of course, I can see the sceneflow visualization in Fig8 of the manuscript, the reconstruction quality is not really good enough. Moreover, __we cannot judge whether the quality of the sceneflow is correct or not.__

W-2. Validity on the assumption 2.

Can the authors further elaborate the validity of the proposed 2nd assumption? What geometric insight reside within this hypothesis?

_"[Assumption 2] As the time period Δt approaches zero, the absolute SDF change |Δs| of a surface point x equals the distance from x to the tangent plane to the evolved surface at the corresponding point x′ and the sign of Δs is determined by the angle between that tangent plane’s normal and the scene flow (as shown in Figure 3)."_

W-3. Necessity of Sec 3.3

While training the network, does the understanding of sec 3.3 is needed? While this paper proposes an algorithm for bridging the SDF flow and sceneflow, there are not much material or experiments that clearly demonstrate the accuracy of the sceneflow. Moreover, the proposed assumptions are not used when training the methods. Accordingly, it is quite confusing me to understand the precise pipeline of this paper.

### Questions
Please refer to the question above. Especially for W-3, if there are some things that I misunderstood, please let me know.

Overall, I am quite positive to this paper. Depending on the rebuttal, let me change my score.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes to predict the first-order derivative of a signed distance function (SDF) at a point, termed as SDFflow. By using SDFlow, the dynamic recontruction to recover a SDF at time t can be treated as space-time integration of the SDFflow from time t_0 to t and its starting SDF at time t_0. The authors further demonstrate how locally rigid scene-flow can be recovered least-square optimization given the locally rigid assumption for small motions. The results demonstrate the method is outperforming previous baselines using alternative shape and flow representation.

### Strengths
* The approach is technically sound. It is kinda intuitive that this representation should work. 
* From the quantitative comparison, it is clear the method is outperforming previous methods by a relatively large margin. 
* The author also provides connection of SDF flow to scene flow with a math derivation. It is helpful for readers to understand its connection if without background in optimization based motion estimation.

### Weaknesses
 * The flow evaluation in the paper is very weak. The method only compares to NDR on 2D project error using RAFT as pesudo ground truth. This should not be hard to achieve if using a synthetic dataset, if using the rigid moving toy example being shown in the paper. 
* The flow estimation also lacks details. Solving the least-square optimization requires sample multiple points, which the author say "we select more than 6 points" and sometimes it still be ill-conditioned depending on the property of the sampled points, but I don't see any discussion related to this and how the results are generated. The lack of discussion on the conditioning of the least-squares problem is a significant oversight. Specifically, the matrix A, constructed from surface normals and positions, can become rank-deficient if the sampled points are collinear or coplanar, leading to unstable or incorrect flow estimates. The paper should include a discussion on how to detect and mitigate these ill-conditioned cases, such as using a robust solver or adding regularization. Furthermore, the number of points used for the least-squares problem is vaguely defined as "more than 6", which lacks the necessary rigor for a scientific publication. The authors should provide a detailed analysis of how the number of points affects the accuracy and stability of the flow estimation and justify their choice of the number of points.
* The main contribution of this paper is the SDFlow and a claim that it is beating alternative representation (SDF with warping field for example). This can be much clearer if the authors can provide more ablations studies on the contrast of the two representations. Two small experiments they author can simply do is to 1) have the network predict the integral of flow in eq. (7), or 2) predict the time dependent SDF s(x, t), all with fixed hyper-parameters. The contrasts in this ablation can reflect the performance difference in predicting SDF flow. Though the authors provide comparisons to alternative papers that the other papers compound too many other terms, and I don't think I can get the insights of why SDF flow works better here.

### Questions
1. Though the method is outperforming previous methods by big margin in the qualitative comparisons, the difference in qualitative comparison is less clear to me from all figures in the paper. In particular compared to Tensor4D, I can see each method wins in different level of details being captured. The paper currently summarizes it as "all of its results share similar artifacts which we conjecture are due to the tensor decomposition. Our method performs comparably to the baselines, with fewer artifacts." I am not sure I can capture this from the current presentation. Will love to know a concrete summary of the areas where the model increase performance best. 
2. I did not see any discussions about the limitations of existing methods or representations. As all current multi-view dynamic reconstruction work, I assume this work will face the same limitations in  large motion (which will also break the linear motion relation between scene flow and sdf flow) and number of views. But I'd like to some more technical insights of potential downside using SDF flow in some scenarios compared to other representation.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a novel representation, namely SDF Flow, for solving multi-view dynamic scene reconstruction by representing the dynamic scene as a 4-D SDF field and modelling its derivative w.r.t. time instead of the SDF value. The proposed representation has several nice properties and can be used to compute the scene flow analytically. Experimental results on public datasets have shown competitive reconstruction quality compared to state-of-the-art, and better scene flow estimation.

### Strengths
1. The proposed representation is novel. I’ve never seen similar representations before. The idea is clear and elegant but effective. It has the potential to open up a new paradigm for dynamic scene reconstruction and provide great insight for the community.

2. The authors also revealed the relationship between SDF flow and scene flow through mathematical derivation, and have shown that the scene motion can be computed analytically by solving linear equations.

3. Quantitative and qualitative experiments have shown the proposed method could achieve promising reconstruction quality. The scene flow estimation result also looks promising.

### Weaknesses
1. In Sec 3.3, the authors made two assumptions when deriving the computation of scene motion from SDF flow, which is justified by a 2D toy example. However, it would be great to have a more in-depth theoretical analysis and experiments to understand its convergence behaviour. Specifically, the assumption that the change in SDF, \(\Delta_S\), can be approximated by the projection of the displacement vector onto the surface normal, while intuitive, lacks rigorous justification. The provided 2D example is insufficient to demonstrate the validity of this assumption in complex 3D scenarios with intricate surface deformations. The assumption that the closest point on the evolved surface, \(\mathbf{x}''\), is infinitely close to the displaced point, \(\mathbf{x}'\), as \(\Delta t\) approaches zero, needs more careful consideration. The difference between assumed \(\Delta_S\) and real value looks quite big, especially when the surface undergoes significant non-rigid deformation, which could lead to inaccurate scene flow estimation.

2. The optimisation takes too long, which limits its practical usage. The paper does not provide sufficient details on the computational complexity of the proposed method. It would be beneficial to have a more detailed analysis of the time taken for each step of the algorithm, including the SDF flow computation, the scene flow estimation, and the surface reconstruction. This would allow for a better understanding of the bottlenecks and potential areas for optimization. The lack of discussion on the scalability of the method with respect to the scene complexity and the number of input views is also a concern.

### Questions
Please see weakness.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper tackles dynamic surface reconstruction and scene-flow estimation from multi-view RGB video with known camera parameters. It uses a global coordinate-based MLP that outputs the SDF in canonical space (t=0), which then gets converted to density via VolSDF's formula, enabling NeRF-style rendering. Training uses an RGB reconstruction loss and an Eikonal regularizer for the SDF. The method departs from prior dynamic NeRFs in its deformation model: a separate MLP is trained to predict the temporal change (derivative) of the SDF at any point in space. These changes get integrated with Runge-Kutta over time to obtain the time-dependent SDF. Furthermore, the paper shows how this SDF flow can be converted into scene flow. Experiments show that the geometry is either less noisy or more detailed than prior methods on the CMU Panoptic dataset and another existing dataset.

### Strengths
Expanding the dynamic NeRF field in the direction of reconstruction/geometry is worthwhile in my opinion, as it enables more applications than novel view synthesis alone would. Correspondences are also interesting for the same reason. Thus, the problem setting is a big strength of the paper.

The method's SDF flow parametrization is novel, as far as I know. It seems generic enough to be potentially valuable for problem settings very different from the setting in the submission.

The illustrations are done well and the paper in general is written very well.

The method outperforms prior methods quantitatively. Qualitatively, it is better in at least one aspect compared to each prior method, while on par in the other aspects, and hence overall better.

### Weaknesses
 *** Method:

[Tangential Motion] The paper should more clearly state that tangential motion causes issues when converting a time-dependent SDF into scene flow. Specifically, the method relies on solving a linear system to extract scene flow from the SDF flow, and this system becomes ill-conditioned when the motion is tangential to the surface, leading to potentially unstable or incorrect scene flow estimates. This limitation should be explicitly acknowledged and discussed in the paper.

[Topology Change] The results don't show any good instances of topology change. I do not understand this claim. The best example I could find is at 0:45. Are there any other good instances? I'm also lost as to which aspect of the method helps with topology change. Please mark that more clearly. While the method might be capable of representing topology changes, the paper doesn't clearly demonstrate or explain how the proposed SDF flow representation facilitates this capability compared to other dynamic scene representations. The examples provided are not convincing and lack a detailed analysis.

*** Experiments:

[Scene Flow Evaluation] The paper doesn't show any appearance/novel view results. That's okay since it focuses on the geometry, and appearance is only used as an auxiliary to deal with the RGB input. However, I would still be curious to see video results where the appearance is taken from t=0 and propagated via the SDF flow. That would allow to visualize longer-term correspondence drift and whether tangential motion causes issues in practice. Currently, the SDF flow (and thus the derived scene flow) only cares about short-term "geometrical" correspondences. - This is relevant because the paper doesn't just claim that the SDF flow is a helpful parametrization but rather that it enables scene flow, i.e. correspondences. Currently, the qualitative and quantitative scene flow evaluation is only short-term, even though the method requires long-term correspondences (equation 7). The quantitative scene flow evaluation is also only a single sequence. The paper should provide a more comprehensive evaluation of the scene flow, including long-term tracking and a more diverse set of sequences to validate the robustness of the method.

[Integral Evaluation] How does the temporal integration scale with scene length? Presumably linearly? Is that why only 24 frames are used? How many function evaluations does the Runge-Kutta solver need for the last (24th) frame? The computational cost of the temporal integration, which scales linearly with the number of frames, is a significant limitation that should be discussed. The paper should analyze the practical implications of this scaling behavior, especially for longer sequences, and explore potential optimizations to mitigate this issue. The number of function evaluations for the Runge-Kutta solver should be explicitly stated for clarity.

[Weak Qualitative Geometry] Tensor4D gives detailed, noisy results and NDR is less noisy but lacks detail. The submission's results have the level of detail of Tensor4D and the low noise level of NDR. Still, none of these results are overwhelming or that impressive. (Doesn't need to be addressed in the rebuttal.)

*** Paper:

[Related Work] The related work section isn't that thorough. For example, the dynamic NeRF papers Fang et al. Fast dynamic radiance fields with time-aware neural voxels and Li et al. Neural 3D Video Synthesis are missing. Li et al., like NSFF, can also handle topology changes. Furthermore, shape-from-template methods aren't mentioned. Scene flow methods (e.g. Song et al. PREF: Predictability Regularized Neural Motion Fields) aren't discussed. Also, since NDR is compared to, mentioning some of the papers in the RGB-D line of work would be good, e.g. DynamicFusion, VolumeDeform, KillingFusion, OcclusionFusion. And TARS (Duggal et al. Topologically-aware deformation fields for single-view 3d reconstruction) seems relevant since it isn't restricted to blend skinning (a typo ("blender") in the submission). The related work section lacks a comprehensive overview of relevant literature, particularly in dynamic NeRFs, shape-from-template methods, scene flow techniques, and RGB-D based dynamic reconstruction. This omission weakens the paper's positioning within the broader research landscape.

[Limitations] Please discuss limitations.

*** Minor:

[Input Assumptions] Since the mathematical derivation matters here, please state what assumptions go into the paragraph between equation 5 and 6, which talks about the continuity and differentiability of a time-dependent SDF. In theory, there is nothing preventing an object from appearing out of nowhere, an SDF does not inherently have any restrictions on its temporal evolution (while it does have restrictions in space, namely the Eikonal equation). In real-world cases, geometry noise (say, due to the sensor or an imperfect reconstruction) pops randomly into existence and vanishes randomly over time, which leads to discontinuities w.r.t. the time parameter. Unless point x is meant to be a Lagrangian particle rather than an Eulerian grid coordinate? Figure 2 looks Eulerian though. --- Please state the assumptions that go into that paragraph. The paper needs to clarify the assumptions made about the temporal continuity and differentiability of the SDF. The current explanation is insufficient and does not address the potential for discontinuities in real-world scenarios.

[Wrong Argument] The argument at the end of Sec. 3.1 is that most dynamic NeRF methods have issues with topology changes. That's not the case for most dynamic NeRF methods that handle general objects since most condition the canonical model in some manner on time (e.g. HyperNeRF). An extreme case of that is Neural Scene Flow Fields. The argument only holds for D-NeRF-style methods like Nerfies or NR-NeRF. For the others, the better argument would be to say that they use density to parametrize geometry rather than SDF and hence the geometry tends to be very noisy and lack a clearly defined surface. The paper's argument about topology change limitations in other dynamic NeRF methods is inaccurate and should be revised to reflect the capabilities of time-conditioned models.

[Labelling] Figure 2 would benefit from labelling the two ellipses with their respective timesteps (t=0 and t=6?).

### Questions
I have listed my concerns in Weaknesses. The concerns under "Minor" don't need to be addressed in a rebuttal, except that clearing up [Input Assumptions] would help me. For all others, I'd appreciate a response. In particular, the most important concerns I have are [Topology Change] and [Scene Flow Evaluation]. If these are not addressed in a rebuttal in some form, I am against accepting the paper. I would still want the rebuttal to address the other major concerns to feel like I have a decent grasp of the submission.

Overall, I lean towards reject. Even though the results are not that impressive, the paper shows nice technical contributions. If the rebuttal addresses my two main concerns well, I could increase my score to acceptable.

=====

Post-rebuttal justification: The rebuttal addressed all concerns very well.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good
