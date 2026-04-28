# Reflective Gaussian Splatting

- Decision: Accept
- Avg Score: 6.50
- Scores: 8, 6, 6, 6

## Abstract
Novel view synthesis has experienced significant advancements owing to increasingly capable NeRF- and 3DGS-based methods. However, reflective object reconstruction remains challenging, lacking a proper solution to achieve real-time, high-quality rendering while accommodating inter-reflection. To fill this gap, we introduce a Reflective Gaussian splatting (Ref-Gaussian) framework characterized with two components: (I) Physically based deferred rendering that empowers the rendering equation with pixel-level material properties via formulating split-sum approximation; (II) Gaussian-grounded inter-reflection that realizes the desired inter-reflection function within a Gaussian splatting paradigm for the first time. To enhance geometry modeling, we further introduce material-aware normal propagation and an initial per-Gaussian shading stage, along with 2D Gaussian primitives. Extensive experiments on standard datasets demonstrate that Ref-Gaussian surpasses existing approaches in terms of quantitative metrics, visual quality, and compute efficiency. Further, we show that our method serves as a unified solution for both reflective and non-reflective scenes, going beyond the previous alternatives focusing on only reflective scenes. Also, we illustrate that Ref-Gaussian supports more applications such as relighting and editing.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
Though powerful in novel view synthesis, vanilla 3DGS encounters challenges in extending to physically-based rendering or modeling inter-reflection due to lack of deterministic geometry. This work introduces a novel approach Ref-Gaussian, which achieves real-time high-quality rendering of reflective objects while also modeling inter-reflection effects.

The paper proposes several key techniques:
(a) Geometry enhanced technique: employing 2DGS to bridge deterministic geometry with Gaussian splatting and enhancing the geometry by the novel material-aware normal propagation.
(b) PBR optimization framework for 3DGS-based methods: using per-Gaussian PBR initialization followed with physically-based deferred rendering.
(c) Gaussian-grounded inter-reflection: applying real-time ray-tracing to the extracted mesh from 2DGS.

Extensive experiments demonstrate the effectiveness of these techniques and that the proposed method outperforms several baselines significantly.

### Strengths
1. By extracting explicit geometry, the paper addresses the inter-reflection issue in Gaussian splatting, which is important in realistic PBR. Experimental results showcase its SOTA performance in novel view synthesis and decomposition on reflective cases.
2. Instead of per-Gaussian PBR (like Relightable 3DGS or Gaussian Shader), The proposed method employs an effective PBR deferred rendering to achieve better PBR performance (similar to 3DGS-DR). Further ablation study demonstrates the superiority of such a deferred rendering technique over the per-Gaussian solutions.
3. The proposed method employs a material-aware normal propagation. This enhances normal estimation by periodically increasing the scale of 2D Gaussians with high metallic and low roughness, which demonstrates interesting material-normal interaction in 3DGS-based PBR.

### Weaknesses
1. The effectiveness of inter-reflection technique lacks further qualitative evidence (e.g. providing indirect components in Fig.5 or showcasing indirect components in Ref-Real dataset where the multiple objects provide rich inter-reflection), as the ablation study in table 3 indicates only a slight decrease in PSNR when rendering without inter-reflection.
2. The ablation study in table 3 only takes PSNR changes into account, while the influences on geometry may need further demonstration (e.g. normal MAE or qualitative illustration), in order to provide stronger evidence for effectiveness of each techniques.
3. The inter-reflection modeling appears to be limited by its visibility calculation, which is only accurate for specular surfaces. The method calculates a single reflected direction using $2(\omega_i\cdot N)N-\omega_i$, which is physically accurate only for fully specular surfaces. Furthermore, the approximation from Eq. 8 to Eq. 9 seems to ignore the roughness term of BRDF materials, suggesting that the method is designed exclusively for fully specular surfaces. This is further evidenced by the binary visibility maps and the seemingly overestimated indirect light component in Figure 12. The lighting model, represented by Gaussian-level spherical harmonic (SH) attributes, are optimized during training and cannot be reconstructed for relighting purposes, even for specular surfaces.

### Questions
1. What's the main difference between the "material-aware normal propagation" in the paper and the "normal propagation" in 3DGS-DR? According to 3DGS-DR, their normal propagation are also aware of reflection strength. Is there any key improvement over their solution? Otherwise, is it an adaptation from reflection-strength-aware to PBR-attribute-aware?

### Soundness
3

### Presentation
4

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
This paper proposed a novel Gaussian Splatting based inverse rendering framework, which focus on reflective object reconstruction. This method rely on deferred shading to achieve more smooth and cohesive rendering results, as well as the combination of mesh-based visibility and per-Gaussian indirect lighting to model the inter-reflection. The experimenta evaluation demonstrate that this method can accurately reconstruct reflective object while maintaining real-time rendering capabilities.

### Strengths
- Rendering quality is excellent, and reconstructed normals are accurate.
- Training time and rendering speed are satisfactory

### Weaknesses
 - The contribution of this paper may lack novelty. For the deferred shading part of the pipeline, I think many previous 3DGS-based inverse rendering methods[1][2][3] have adopted these techniques and [2][3] also use split-sum approximation to handle the intractable rendering equation. Further more, assigning each Gaussian with a new attribute to model the indirect lighting has also been proposed in previous methods[4]. The innovation of this method lies in the new visibility modeling scheme and optimization techniques. Unlike previous methods that use baked volume or Gaussian-based ray-tracing to model occlusion, the proposed method attempts to first extract the mesh using TSDF and then use mesh-based ray-tracing to obtain occlusion.

- To determine the visibility, this method consider the occlusion at the reflected direction $\boldsymbol{R}=2\left(w_i \cdot \boldsymbol{N}\right) \boldsymbol{N}-w_i$. This means that this method only considers the indirect lighting of the specular surface. For glossy or diffuse surfaces, this estimation may not be not accurate enough, and such objects do exist in the dataset. For example, for the Potion in figure.5, The lid of the bottle is obviously a rough diffuse surface. Since the proposed method focuses on the reconstruction of the reflective object, this does not seem to be a serious problem, but I would like to know if there is a way to improve this.

- In addition, since the visibility only considers the reflected direction, I am a little confused about the integral in equation 9. Because this method does not calculate the integral over the entire hemisphere $\Omega$. So I want to know how the rendering equation is finally calculated.

### Questions
- In ablation study, the normal of 2DGS is much better than 3DGS. Since accurate normals are very important for PBR, does this mean that the performance gain of the proposed method over other methods comes largely from the better geometry reconstruction quality of 2DGS? This is important for evaluating the technical contribution of this paper. I hope the author can give quantitative data (**use 3DGS as representation and keep the rest of the pipeline unchanged to evaluate the rendered results**) to show how much performance improvement can be achieved by using 2DGS representation compared to 3DGS.
- Since indirect lighting is modeled as an attribute of each Gaussian, which represents the inter-reflection under the lighting conditions corresponding to the training stage. Is it possible to build indirect lighting when relighting?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper proposes a Reflective Gaussian splatting (*Ref-Gaussian*) framework to achieve real-time high-level novel view synthesis for reflective objects with inter-reflection effects. The framework consists of 2 main parts: (i) physically-based deferred rendering, which associates each Gaussian with material properties and leverages physically-based surface rendering (rendering equation and split-sum approximation) to compute the rendered color; (ii) Gaussian-grounded inter-reflection, which computes the visibility of the reflected ray and model indirect view-dependent color as a per-Gaussian spherical harmonics. The proposed method also leverages several techniques to enhance the underlying geometry. This paper evaluates the proposed method with qualitative and quantitative experimental results and validates its design components by an ablation study. It shows that the method can outperform baselines.

### Strengths
1. The key designs proposed by the paper are rational. It is not surprising that leveraging physically-based rendering can significanty improve the performance of specular rendering.
2. I like the idea of material-aware normal propagation. Seems like it can greatly improve the quality of surface normal reconstruction.
3. Extensive qualitative and quantitative experiments demonstrate that the proposed method outperforms baselines.
4. I appreciate the comprehensive ablation study that covers lots of specific design choices.

### Weaknesses
1. Missing details. L233-234: "During optimization, we periodically extract the object’s surface mesh using truncated signed distance function (TSDF) fusion." The authors need to specify the number of steps as the period of mesh extraction.
2. Unclear explanations. I have several confusions when reading the paper, and please see the "Questions" part. I believe that the paper writing can be improved to explain the method more clearly.
3. Baselines. Although this method is based on 3DGS, it should also include more methods based on other representations (such as NeRF) as its baseline, such as (a) NeRO: Neural Geometry and BRDF Reconstruction of Reflective Objects from Multiview Images (SIGGRAPH 2023) (b) Neural Directional Encoding for Efficient and Accurate View-Dependent Appearance Modeling (CVPR 2024).
4. Limitation of Gaussian-grounded inter-reflection: In Eq. (8), it is clear that the direct lighting part can capture rough specular effect. But in Eq. (10), the method only traces a single reflected ray to compute the indirect reflection, which will introduce errors for rough surfaces. This should be added as a limitation.
5. Experiments. The method leverages the extracted mesh to compute visibility, so I think the author should also show (at least qualitative) results of the extracted mesh in the experiment section.

### Questions
1. L239-244. More details are required to describe how the indirect lighting is rendered. To be specific,
    - Does the method conducts explicit ray tracing for the reflected ray and computes ray-Gaussian intersection? Or does the method uses Gaussian splatting in the reflected ray directions?
    - In Eq. (10), the meaning of the symbol $N$ in $i\in N$ is unclear: does it denote the set of Gaussians intersected with the reflected ray?
2. L254: "To mitigate this, we apply the rendering equation at the Gaussian level to achieve geometry convergence initially." What does "rendering equation at the Gaussian level" mean? What is the difference between this and Eq. (8)?
3. Are the training hyperparameters the same across different scenes?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper focuses on novel view synthesis for reflective objects. It proposes a method called Reflective Gaussian Splatting, which uses Gaussian Splatting as its primary representation and introduces two additional techniques: (a) physically-based deferred shading and (b) an accurate approximation for modeling inter-reflection effects within the Gaussian Splatting framework. The effectiveness of this method is validated using various benchmark datasets. Additionally, the method is compute-efficient, making it suitable for applications such as relighting and material editing.

### Strengths
1. The proposed method achieves state-of-the-art performance on several benchmark datasets, validating its significance. 
2. The proposed method offers a good trade-off between performance and efficiency. The introduced deferred shading technique, plus the occlusion approximation using a TSDF mesh, sounds reasonable for these goals.
3. The paper is well-written and easy to follow. The paper has enough details for reproduction.

### Weaknesses
1. While efficient in modeling the occlusion with an extracted mesh, its performance may rely on the accuracy of the extracted mesh. Since extracting a good mesh for the reflective object is non-trivial,  such a non-differentiable approximation may lead to worse results. The method uses a TSDF mesh, which is known to be sensitive to noise and may not accurately represent complex geometries, particularly those with thin structures or intricate reflective surfaces. This could lead to inaccuracies in occlusion calculations and, consequently, in the final rendered images. Furthermore, the non-differentiable nature of the mesh extraction process prevents end-to-end optimization, potentially limiting the overall performance.

2. While built upon 3DGS-DR, its performance (LPIPS) on real datasets appears limited over 3DGS-DR. The LPIPS metric, being sensitive to perceptual differences, suggests that the proposed method might not capture the fine details and textures as effectively as 3DGS-DR on real-world data. This discrepancy raises questions about the generalizability of the method to diverse and complex real-world scenarios, particularly those with subtle variations in lighting and surface properties.

### Questions
1. From the paper, I assume that the geometry is important for disentangling appearance and those PBR materials. I would like to know if PBR modeling will also benefit geometry. 

2. Why is the LIPPS metric of the proposed method on the real dataset worse than 3DGS-DR?

### Soundness
3

### Presentation
4

### Contribution
3
