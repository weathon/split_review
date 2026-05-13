# GNeRP: Gaussian-guided Neural Reconstruction of Reflective Objects with Noisy Polarization Priors

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Learning surfaces from neural radiance field (NeRF) became a rising topic in Multi-View Stereo (MVS).  Recent Signed Distance Function (SDF)--based methods demonstrated their ability to reconstruct accurate 3D shapes of Lambertian scenes. However, their results on reflective scenes are unsatisfactory due to the entanglement of specular radiance and complicated geometry. To address the challenges, we propose a Gaussian-based representation of normals in SDF fields. Supervised by polarization priors, this representation guides the learning of geometry behind the specular reflection and captures more details than existing methods.  Moreover, we propose a reweighting strategy in the optimization process to alleviate the noise issue of polarization priors. To validate the effectiveness of our design, we capture polarimetric information, and ground truth meshes in additional reflective scenes with various geometry. We also evaluated our framework on the PANDORA dataset. Comparisons prove our method outperforms existing neural 3D reconstruction methods in reflective scenes by a large margin. Supplemental materials can be found in \hyperlink{https://yukiumi13.io/gnerp_page/}{this page}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The article introduces a 3D reconstruction technique based on Nerf, which focuses on capturing 3D geometries of glossy objects. Building on recent progress in utilizing signed distance functions (SDF), as seen in approaches like NeuS or Ref-Neus, this method also incorporates it. However, unlike the scalar SDF in these approaches, this proposed method additionally integrates polarization cues to constrain the surface normal. These added constraints are formulated using a Gaussian splatting approach. As a result, the proposed method demonstrates notably improved accuracy compared to state-of-the-art (SOTA) approaches.

### Strengths
- The primary advantage of the proposed method lies in its utilization of polarization cues to improve the estimated geometry. This strategy is commonly employed to enhance accuracy in conventional 3D reconstruction techniques.
- The additional constraint is devised using a Gaussian splatting technique. Specifically, the original 3D Gaussian on the 3D surface normal is transformed into a 2D Gaussian in the image plane and is constrained by polarization cue.
- The polarization reweighting strategy can guide the proposed method to employ more polarization cues on the area with strong polarization information and employ more radiance on low polarization information.
- The proposed method excels in reconstructing 3D geometry with high precision and capturing intricate details.

### Weaknesses
 - The proposed method only works for glossy objects that exhibit clear polarization information.
- The proposed method comes with many hyperparameters which are hard for users to set in practice. Parameters like alpha and beta typically vary between 0.1 and 1, contingent on the intricacy of the geometry. Regrettably, the authors did not carry out any experiments to assess the optimal selection of these parameters, potentially hindering the method's practical implementation and performance.
- Only the results of a few objects are shown in the experiments.
- There are typographical errors and improper terms, which are described in the questions.

- For the parameter selection of alpha and beta, the authors did not specify the use of identical parameters across all experiments. The exact values for these parameters were not explicitly mentioned in the paper.

- In Section 2.4, the authors stated that "the learned 3D Gaussians imply the anisotropic normals distribution of 3D
points and capture more details of surface geometry." Could the authors elaborate on the description or provide some references?
Does it mean the learned 3D Gaussian is anisotropic? And the anisotropicity results in more details?

- The ablation study could include an examination of the impact of alpha and beta. Additionally, the authors did not provide a clear rationale for why they included only two objects in Table 2 while incorporating four objects in Table 1. The ablation study of the other two objects is not supporting?

- In the last paragraph of Section 3.2.3, the authors stated "Intuitively, the first term measures the complexity of the geometry, while the second term reveals the specific geometric shape." Could the authors elaborate on this description?

Additional comments
+ Typographical errors:
	- alpha in the first paragraph of page 5
	- common scenes in the first paragraph of section 2.3
	- Fig. 4(g) in the first paragraph of page 7. In fact, there is no Fig.4 (g).
	- In Fig. 4 caption: "blue boxes bound diffuse ones".

+ "exact 3D shapes" in the abstract should be replaced by another term such as "accurate".

### Questions
- For the parameter selection of alpha and beta, the authors did not specify the use of identical parameters across all experiments. The exact values for these parameters were not explicitly mentioned in the paper.

- In Section 2.4, the authors stated that "the learned 3D Gaussians imply the anisotropic normals distribution of 3D
points and capture more details of surface geometry." Could the authors elaborate on the description or provide some references?
Does it mean the learned 3D Gaussian is anisotropic? And the anisotropicity results in more details?

- The ablation study could include an examination of the impact of alpha and beta. Additionally, the authors did not provide a clear rationale for why they included only two objects in Table 2 while incorporating four objects in Table 1. The ablation study of the other two objects is not supporting?

- In the last paragraph of Section 3.2.3, the authors stated "Intuitively, the first term measures the complexity of the geometry, while the second term reveals the specific geometric shape." Could the authors elaborate on this description?


Additional comments
+ Typographical errors:
	- alpha in the first paragraph of page 5
	- common scenes in the first paragraph of section 2.3
	- Fig. 4(g) in the first paragraph of page 7. In fact, there is no Fig.4 (g).
	- In Fig. 4 caption: "blue boxes bound diffuse ones".
	

+ "exact 3D shapes" in the abstract should be replaced by another term such as "accurate".

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Neural SDF-based 3D reconstruction excels at smooth Lambertian objects. The paper proposes a 3D Gaussian-based representation of normals in SDF fields, and splat it to 2D Gaussians in the image plane. It shows that the 2D Gaussian can be directly extracted from Angle of Polarization (AoP). This paper proposes to use the proposed 2D Gassians represenation as the additional constraints for 3D normal recovery. Moreover, it proposes to use the Degree of Polarization (DoP) which indicates the complexity of the surface to reweight  AoPalleviate the noise issue of polarization priors.  Their experimental results on PANDORA dataset domstrate the effiectiveness of the proposed method.

### Strengths
This paper proposed the 3D Gaussian representation of surface normal for the volume rendering proposed in NeRF(2020) in EQ4., and furture entend it to 2D Gaussian by using the splatting approach (Zwicker et al). The research demonstrates that the 2D Gaussian representation can be efficiently computed using the Angle of Projection (AoP). Additionally, it is revealed that the Degree of Polarization (DoP) is strongly correlated with the surface complexity. Consequently, the authors propose a novel regularization technique for NeRF, involving the reweighting of constraints on the 2D Gaussian representation of surface normals. The experimental results clearly indicate that the proposed method excels in handling high-frequency BRDF surfaces.

### Weaknesses
The paper presents experimental results only on the PANDORA dataset. It is essential to include discussions regarding failure cases and the limitations of the proposed method. The authors highlight "the creation of a new and challenging multi-view dataset" as a significant contribution. Nevertheless, there is a notable lack of information and discussion about this new dataset in the paper.

### Questions
Please explain in detial about how to get $\hat{\Sigma}, \hat{\Lambda}$ and $\tilde{\Sigma} \tilde{\Lambda}$ in EQ7~9. Pleae explain the experimental setting to get the polarized data. More details are needed for the new multi-view polarized dataset, and how it collected.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a neural volume-based method that utilizes Gaussian-based normal representation and polarization information to improve multi-view 3D reconstruction of highly specular objects. Its volume representation and rendering framework are from NeuS. The major novelty is to model the normal direction of sampled 3D points along the ray with 3D Gaussian distributions, which then can be projected to 2D image plane using Gaussian splatting. A new loss is proposed by comparing the projected normal distribution with the normal distribution computed from polarization information. Experiments on datasets containing highly specular objects shows that the proposed method can achieve much more accurate geometry reconstruction.

### Strengths
1. High-quality geometry reconstruction for highly specular objects.
Multi-view reconstruction of highly specular surfaces is known to be a difficult problem. This paper shows compelling reconstruction quality on several challenging real-world objects. 

2. Convincing improvements compared to prior method on highly specular objects.
Both quantitative and qualitative comparisons show that the proposed method achieve higher geometry reconstruction accuracy compared to prior state-of-the-arts, including a method that also utilizes polarization information and a method designed for specular object. 

3. A polarization-based geometry reconstruction method that does not require complicated setups. 
The proposed method does not make strong assumptions on the material properties and capturing environment, which makes it practical for many applications.

### Weaknesses
1. I have some questions about Sec. 3.2.3, which I would like to understand better. They are not necessarily the weaknesses of the paper.

(a) How to decide the scale factor $s$? Or do we assume the mean loss should be scale invariant and we only care its orientation? It is not clear in the paper how the scale factor is determined in the equation for the projected normal distribution. A more detailed explanation is needed to understand the relationship between the scale factor and the overall loss function.

(b) Do we compute $\mu_i^{j}$ by projecting every $x_{i}^{j}$ along the ray to 2D image, i.e. $M'$ equal to $6M$? The paper mentions sampling points along the ray to estimate the 3D Gaussian distribution. However, it is unclear how these sampled points are used to compute the mean of the projected 2D Gaussian distribution. Clarifying the relationship between $M$ and $M'$ and providing a more detailed explanation of the projection process would be helpful.

(c) I can see that 2D convariance matrices computed from polarization and splatting can both indicate if geometry is changing rapidly in the neighborhood. But it is a bit difficult for me to understand why they should be equal. A side by side visualization of both 2D Gaussian distributions will be useful. In addition, will noisy AoP of diffuse surface cause the 2D covariance matrix from polarization to have very large eigen values? The assumption that the covariance matrices from polarization and splatting should be equal needs further justification. It would be beneficial to provide a visual comparison of the two distributions and discuss the potential impact of noisy Angle of Polarization (AoP) on the covariance matrix in diffuse regions.

(d) Typos: there is an extra $)$ in $L_{\text{mean}}$ and $L_{\text{conv}}$. 

2. Further ablation studies can be useful to verify the effectiveness of Gaussian normal representation. 
Since Gaussian normal representation is the major novelty, it might be good to further verify its effectiveness with more ablation studies. One simple baseline is to render normal through standard volume ray tracing and then use reweighted $L_{\mean}$ loss for training. That may give us a clear answer if we need to sample extra points to compute a Gaussian distribution. 

3. Results on less specular objects may be interesting.
I notice that all real objects shown in the paper are quite glossy. Do we have results on less glossy objects? As shown in the paper, the AoP of diffuse surfaces can be noisy but hopefully the DoP weight can fix this issue. 

4. Missing reference.
One related paper is cite is: [1]

Very minor comments:
Figure 2: the polarized direction may use a different color from that of the x-axis. Zenith angle $\theta$ is mentioned by never discussed in the paper. It may be more useful to label out angle $\varphi$.

### Questions
My major questions are the first two points listed in the weakness section.
1. Can we explain in more details how to compute 2D normal distribution from a polarized image? 
2. Can we further verify if 3D Gaussian distribution is necessary? If we only compute the normal following standard volume ray tracing and then use reweighted $L_{\text{mean}}$ loss, will the results be similar or worse?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a method called GNERP for reconstructing the detailed geometry of reflective objects from multi-view images. The key idea is to extend the geometry representation from scalar Signed Distance Fields (SDFs) to Gaussian fields of normals supervised by polarization priors. The paper introduces a pipeline for learning the surface by volume rendering, and presents a DoP reweighing strategy to alleviate noise and imbalance distribution problems of polarization priors. Additionally, a new multi-view dataset called PolRef, consisting of objects with reflective and less-textured surfaces, is collected to evaluate the performance of3D reconstruction methods. Experimental results show that GNERP improves the geometry details and accuracy of geometry and normals of reflective surfaces compared to existing state-of-the-art methods.

### Strengths
- The paper integrates recent advances in Gaussian Splatting to model the polarization priors for reflective surface recovery, which is innovative and aligns with the current research trends.

- The proposed reweighted polarization priors appear to serve effectively as supervision.

### Weaknesses
 - The explanation of the proposed method is unclear. What is the input? Is a polarization camera required for reconstruction? If not, is the polarization prior regressed during optimization?

- The proposed approach neglects the effect of self-occlusions, which can be severe for complicated objects. The paper should at least include a qualitative discussion about the effects of self-occlusions.

- The property of polarization is closely related to materials. The proposed approach relies on the intermediate output of a coordinate network and hence seems to handle only objects with a uniform material, as shown in Fig. 5.

- The experiments are conducted only on relatively simple objects. It would be beneficial to show results on more complicated objects to better understand its performance.

- It would be great if the authors could provide an illustration of how the polarization priors intuitively improve the performance of NeuS.

### Questions
Please see weakness

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
