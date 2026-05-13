# ComPC: Completing a 3D Point Cloud with 2D Diffusion Priors

- Decision: Accept
- Scores: 6, 6, 8, 8

## Abstract
3D point clouds directly collected from objects through sensors are often incomplete due to self-occlusion. Conventional methods for completing these partial point clouds rely on manually organized training sets and are usually limited to object categories seen during training. In this work, we propose a test-time framework for completing partial point clouds across unseen categories without any requirement for training. Leveraging point rendering via Gaussian Splatting, we develop techniques of Partial Gaussian Initialization, Zero-shot Fractal Completion, and Point Cloud Extraction that utilize priors from pre-trained 2D diffusion models to infer missing regions and extract uniform completed point clouds. Experimental results on both synthetic and real-world scanned point clouds demonstrate that our approach outperforms existing methods in completing a variety of objects.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper addresses the problem of 3D point cloud completion from partial and noisy data, specifically in an open-set setting, where point clouds from unseen categories are completed. The proposed approach introduces a novel, training-free framework that leverages 3D Gaussian Splatting (3DGS) representations and pre-trained 2D diffusion models for guiding the completion process.

First, a Partial Gaussian Initialization (PGI) module estimates a reference viewpoint, $V_p$, that maximizes coverage of the input partial point cloud, $P_{in}$. This viewpoint is used to initialize partial 3D Gaussians, $G_{in}$, and render an image $I_{in}$. The Zero-shot Fractal Completion (ZFC) module then combines $G_{in}$ with another set of 3D Gaussians, $G_m$, which is generated from a noisy variant of the input point cloud, $P_m$. Using the Zero-1-to-3 diffusion model, $G_m$ is refined via Score Distillation Guidance based on the reference viewpoint image $I_{in}$, which optimizes the Gaussians based on a randomly rendered image $I_i$.  A geometric preservation constraint is also introduced by measuring the Chamfer Distance between the input point cloud and the predicted point cloud, $P_{pre}$the predicted one $P_{pre}$ under the reference viewpoint $V_p$. 

Finally, the Point Cloud Extraction (PCE) module extracts surface points, $P_{surf}$, from the 3D Gaussian centers, $G_{all} = {G_{in}, G_m}$, excluding those with low opacity and selecting the ones that are visible from a set of uniform camera poses. To address the non-uniform density of $P_{surf}$, a Grid Pulling step is applied that promotes uniform alignment of $P_{surf}$ along the underlying surface. The framework is evaluated on synthetic and real-world point clouds for the point cloud completion task, achieving superior or comparable performance w.r.t. existing methods.

### Strengths
The proposed framework generates complete point clouds that accurately capture the underlying surface, entirely bypassing the need for training on extensive 3D shape categories. By leveraging a 2D diffusion model to synthesize novel views from a specific input viewpoint, it also removes the need for manual text prompts. Furthermore, this approach achieves superior or comparable performance to other test-time frameworks (e.g., SDS-complete) while significantly reducing computational time. Finally, the adaptation of the NeuraPull approach, using near and far points from the 3D bounding box of the $P_{surf}$ point cloud, while also incorporating geometric details from the input partial point cloud, is able to produce uniformly-sampled point clouds.

### Weaknesses
Although this method claims to rely solely on 3D coordinates, as required by the point cloud completion task, it implicitly introduces additional information by incorporating the 3D normal of each point to encode the color map $G_{in}^c$. This additional input signal, which is not utilized by other methods such as PCN or SDS-complete, may introduce an advantage, as evidenced by its significant impact on performance shown in Table 3 and Figure 7. Furthermore, the method heavily depends on the input partial point cloud throughout all stages: in the ZFC module, the SDS guidance is conditioned on the reference viewpoint image derived from the input partial point cloud, and a geometric preservation constraint is based on the original point cloud. In the PCE module, the initial point cloud is merged with $P_{pull}$ in the Grid Pulling step, further reinforcing reliance on the input partial point cloud. The method's performance also degrades more rapidly under noise compared to other methods, suggesting a lack of robustness to input perturbations. Finally, while the method demonstrates good performance on single-view depth maps, it is unclear how it would perform with significantly more incomplete data, such as point clouds with large occlusions or missing regions beyond a single-view depth map.

### Questions
- As noted in the **Weaknesses** section, this method incorporates the input point cloud across all stages of the pipeline. It would be beneficial to examine how the method performs under varying occlusion levels and perturbation intensities.
- Following the above, could the method leverage multiple reference viewpoints during the ZFC step? Would incorporating additional viewpoints lead to more accurate completion of point clouds, particularly in cases with high noise levels and significant occlusions?
- Could this method benefit from adopting 3D scene representations such as VolSDF [1], as used in SDS-complete, which implicitly encodes the SDF of the underlying surface?
- Clarity: 
  - It’s important to clarify that the SDS-complete method leverages VolSDF [1], rather than NeuS, to represent the 3D scene.
  - Adding a horizontal separator line after the Metrics row in Tables 1, 2, and 9 would improve readability. 
  - Please also add the SeedFormer method in line 418.

[1] L. Yariv et al., “Volume Rendering of Neural Implicit Surfaces”, In Proc. NeurIPS, 2021.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces a test-time point cloud completion framework that leverages 2D diffusion priors. Unlike previous methods, which require manually provided information such as text prompts, the proposed method conditions the diffusion model on a reference image from the partial observation. After initializing the partial Gaussians and rendering the reference image, the framework optimizes the parameters of the Gaussians representing the 'missing' parts and then extracts the completed point cloud. The approach is validated on synthetic and real-world scanned point clouds.

### Strengths
a) The problem of completing partial point clouds in a generalizable way is important, as existing methods mostly yield good results only on in-domain samples. b) 2D/3D priors from diffusion models are well-suited for achieving generalization. c) The paper is well-written, the problem is clearly specified and the solution is well presented.

### Weaknesses
a) As the incompleteness of the partial point cloud increases, the diffusion model may produce different completion results at each optimization. However, the multi-modal nature of the approach is not analyzed. For a small set of shapes, multiple runs can be performed on the same partial input, and the resulting completions can be evaluated using multi-modal metrics such as TMD, UHD, MMD. b) The experiment in A.5 could be performed on observations with varying levels of incompleteness, rather than artificially eliminating points, to better demonstrate the method’s actual performance. For instance, depth maps could be used to obtain incomplete observations by merging points from a different number of views. c) The paper does not include a comparison with recent related work such as [1, 2]. The authors are suggested to compare ComPC with also these recent baselines to better evaluate its completion and generalization performance.

### Questions
All of my questions are listed in the weaknesses section, and I may adjust the rating if they are well addressed.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a new pipeline for point cloud completion. The proposed pipeline consists of three steps. The pipeline initializes a single optimal viewpoint for initial render of point cloud. This render is made so the point cloud is most completely observed. The Gaussian Splatting is used to initialize a frozen set of 3D gaussians by utilizing an optimal viewpoint. In the next step the set 3D gaussians are prepared in the optimal way to cover missing point cloud regions. Further Zero 1-to-3 approach is used to complete missing parts of the point cloud. On the final step the point cloud is extracted from the 3D gaussians distributed uniformly (unlike in the start of pipeline) on the shape surface.

Despite the weaknesses, I recommend accepting this work because the authors definitely introduced a new strong pipeline that incorporates many existing methods. Authors proved that the proposed sequence of methods is successfully used for the important complicated task.

The main reason to accept this work is good results that superior existing point cloud completion methods based on single-modality input data. The method shows good performance in the training domain and out of the training domain. In some cases (depicted in the paper) the density of points seems to be more uniform than in GT point clouds. This feature can be useful in tracking and segmentation tasks.

### Strengths
Learning-based methods perform not good when tested out of the domain they were trained on. The strong point of the proposed method is that authors propose a framework that performs out of the training domain as good as in it. Moreover, the model does not require any additional modalities, so the possibility of application is maximal. Lastly, there are empirical experiments done that prove that proposed method outperforms overviewed analogical approaches. The ablation study is well done: this part of the paper is split into categories and each one is devoted to the specific part of the pipeline.

### Weaknesses
Despite the strengths of the work, there are a number of questions about it. There is a method of missing parts completion in section 3.2. Many side methods like Zero 1-to-3, SDS guidance, PFNet are referenced in this section while there are very few particular discussions that are taken from these works. For example, what is the fractal approach discussion taken from PFNet? The description lacks specifics on how these methods are adapted and integrated into the proposed pipeline. The second question is: what is the point of applying differentiable quantization to set the gaussians' opacity? It seems that there is a quite simple solution. The justification for this design choice is not clear, and the potential benefits over simpler alternatives are not well explained. Another weakness of the proposed work is the absence of the possibility to test the pipeline. The source code that aggregates the mentioned methods can clarify the approach that authors suggest.

### Questions
It might be interesting to compare the density of completed point clouds and compare it with GT density. What is the reason for the density difference? In the section 4.4. of ablation study we can see that point cloud extraction causes a kind of separate clusters. What is the reason?

It is recommended to provide a possibility to test the pipeline on a custom dataset. Moreover, it is recommended to split Figure 2 into two-three separate pictures with clarified steps description. The united scheme makes understanding the pipeline hard.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The work tries to complete a general partial point cloud using  zero123, which gets an object's image and outputs images of the exact object from any unseen direction.
They first model the partial point cloud as gaussians, and render them from the view direction, where the object seems full.
than through SDS iterations using zero123 they complete the object from any noval direction.

### Strengths
They continue works that complete point clouds in the wild and challenge the current weakness of long-running time and the need for textual description.
The work exploits advances in 3D generation for further improvement in point cloud completion.

### Weaknesses
good work

### Questions
1. I can't see how your work can generate a surface like SDS-complete?

### Soundness
3

### Presentation
3

### Contribution
3
