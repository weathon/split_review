# GI-GS: Global Illumination Decomposition on Gaussian Splatting for Inverse Rendering

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 6, 8, 6

## Abstract
We present \textit{GI-GS}, a novel inverse rendering framework that leverages 3D Gaussian Splatting (3DGS) and deferred shading to achieve photo-realistic novel view synthesis and relighting. In inverse rendering, accurately modeling the shading processes of objects is essential for achieving high-fidelity results. Therefore, it is critical to incorporate global illumination to account for indirect lighting that reaches an object after multiple bounces across the scene. Previous 3DGS-based methods have attempted to model indirect lighting by characterizing indirect illumination as learnable lighting volumes or additional attributes of each Gaussian, while using baked occlusion to represent shadow effects. These methods, however, fail to accurately model the complex physical interactions between light and objects, making it impossible to construct realistic indirect illumination during relighting. To address this limitation, we propose to calculate indirect lighting using efficient path tracing with deferred shading. In our framework, we first render a G-buffer to capture the detailed geometry and material properties of the scene. Then, we perform physically-based rendering (PBR) only for direct lighting. With the G-buffer and previous rendering results, the indirect lighting can be calculated through a lightweight path tracing. Our method effectively models indirect lighting under any given lighting conditions, thereby achieving better novel view synthesis and relighting. Quantitative and qualitative results show that our GI-GS outperforms existing baselines in both rendering quality and efficiency. Project page: \url{https://stopaimme.io/GI-GS/}.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper present a novel inverse rendering framework, GI-GS, to achieve scene decomposition and photo-realistic relighting.

Existing 3DGS-based methods, due to their nature of non-deterministic geometry, encounter challenges in modeling inter-reflection and self-occlusion, which prevent them from occlusion-aware/indirect-light-aware decomposition or relighting. While recent works like relightable 3DGS use ray tracing to estimate occlusion, preventing shadow from being baked into materials, many of them are still unable to process inter-reflection, or only employ a learnable residual term to model indirect light.

To address this, the paper propose a novel framework with deferred rendering technique, which employs path tracing to achieve indirect illumination computation. Experimental results are provided to demonstrate the effectiveness of the framework, highlighting the promising potential of deferred rendering in efficiently modeling indirect geometry-lighting interactions. In object-level cases, the proposed method outperforms several baselines in both novel view synthesis and decomposition, while achieving comparable performance in relighting. In scene-level cases, the method also demonstrates meaningful results in both decomposition and relighting.

### Strengths
1. The paper propose a novel framework where the deferred rendering technique enables light-weight path tracing on the deferred rendering buffer, which highlights the promising potential of deferred rendering in efficiently modeling indirect geometry-lighting interactions.
2. The method is extended to scene level and successfully produces meaningful decomposition and relighting results.
3. In novel view synthesis tasks, the method achieves best performance over inverse rendering baselines.

### Weaknesses
1. The novel indirect illumination module may require further experimentation to validate its effectiveness. Theoretically, this module has the potential to achieve superior relighting performance compared to solutions that rely on learnable parameters for modeling indirect light, as the fixed inter-reflection in those methods is often inaccurate when relighted under another illumination.

However, the quantitative results presented in Table 1 indicate that the relighting performance is subpar, even when achieving best albedo estimation, which undermines the strength of the paper's key claim. I believe the relighting performance is likely impacted by the inadequate normal estimation, as illustrated in Fig. 9 (Garden, Kitchen, Counter, and Bonsai), rather than suggesting that path tracing is ineffective, especially since the impressive qualitative results in Fig. 6 indicate otherwise.

Therefore, to quantitatively validate the effectiveness of the method, it would be beneficial to conduct an ablation study focused on albedo estimation or relighting. The current ablation study in Table 3 only examines performance changes related to novel view synthesis quality, which is insufficient to support the claims made in the paper.

2. In the absence of quantitative results, the qualitative findings suggest that normal estimation may be inadequate, as demonstrated in Fig. 9 (Garden, Kitchen, Counter, and Bonsai). This deficiency could negatively impact the overall performance of inverse rendering.

### Questions
1. The occlusion map and indirect light map in Figs. 6 and 8 are quite impressive. However, I am curious as to why Fig. 4 shows that the proposed method still retains a significant amount of shadow in the albedo, particularly in the case of the Hotdog.

2. What does the direct light look like? The incorrect direct lighting reconstruction also lead to poor relighting performance.

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
This works introduces GI-GS, a novel gaussian-splatting based inverse rendering pipeline to extract intrinsics from multi-view images. As a follow-up of existing GS-based inverse rendering,  GS-IR, this paper focuses on taking the indirect illumination into account, to solve more accurate material and environment map from photorealistic images.

### Strengths
The paper is intuitive and easy to follow.

Integrating indirect illumination calculation in a GS-based inverse rendering pipeline is a challenging movement.

In the experiments, the model shows comparable results in the task of novel view synthesis, decent performance in relighting, outperforming the GS-based baseline.

### Weaknesses
The way of processing indirect illumination in the pipeline is similar to InvRender: It uses the direct illumination (represented as a radiance function) of 3D points to calculate the indirect illumination. How is the indirect illumination calculation in this paper distincted from the one in InvRender?

Tab. 1: TensoIR performs much better than the proposed method in relighting task. and in figure 4 it is hard to see the differences between GS-IR and proposed method. This harms the soundness of the method. Please add more explanation of the performance.

The usage of I_{dir}(u, v) in the eq. 13 might be inaccurate, since the image RGB value is the combination of diffuse and specular lighting, which is not equal to the illumination from x_hat to x. One way to avoid this to re-apply the first rendering pass with new look-at direction. Is there any specific reason for directly using the RGB values? Please clarify.

While the main focus of the work is on decomposition and relighting, no relighting evaluation for real-world inputs is shown. This challenges the effectiveness of the method in more realistic and complex cases. An experiment conducted on real-world benchmarks (such as Stanford-ORB) can be very helpful to support the claims of the paper.

Other minor issues.
Adaptive Path Tracing happens in the projected camera only, which is not able to take the occluded objects into account.
Eq. (8): $\mathcal_{L}_{n-p}$ looks confusing (might be interpreted as n minus p), $\mathcal_{L}_{n,p}$ might be better.
Tab. 1: Only relighting methods are compared in the NVS column. Please consider adding reconstruction methods as reference.

### Questions
See Weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper propose a efficient path tracing techinque that can calculate indirect lighting. They first render a G-buffer to capture the detailed geometry and material properties of the scene. Then, they perform physically-based rendering only for direct lighting. With the G-buffer and previous rendering results, the indirect lighting can be calcuated through the proposed path tracing. The training is decomposed into three stages: 1. vanilla 3dgs, 2.deferred rendering with split-sum approximation with occlusion calculated from the proposed path tracing, 3.add indirect lighting term on top of stage2.

### Strengths
The paper propose a novel path tracing strategy that can query visibility in screen space.

### Weaknesses
1. in line303-305, I think authors can refer to the uniform sampling in hemi-sphere used by NeILF, which should be better than  sampling in spherical coordinate
2. The authors argure that they are the frist to incorperate indrect illuminance in relighting, however, the proposed lighting model can not model the indirect lighting in specular term, also, the approximation in Equation7 makes it impossible to model sharp shadows as visbility is considered in the integration of direct lighting.
3. The path tracing part is not well introduced. I can't figure out how exactly is the procedure of sampling point on ray. I guess the authors mean they sample many points step by step until the depth of a point is smaller than the rendered depth.
4. The calculation of visibility by comparing the depth of sampled point on the ray with the rendered depth is not comprehensive. There is another condition: the ray (start from the surface) is not occluded by the object, but the sampled points on the ray has a bigger depth value than the rendered depth map. For example, a ray that has a consistent direction as the orientation of the camera, then whether it is occluded is not determined by the rendered depth.
5. I'm also confused about the calculation of indirect light, in line338-341. Is the outgoing radiation indicates $L_p(\hat{x},-\omega_)$? If so, why can it be obtained by indexing the RGB map. And in some conditon, indirect light of a surface point can not be seen by the camera. Equation13 is also confusing.

### Questions
see weakness.

### Soundness
2

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
5

### Summary
This work introduces a novel inverse rendering framework designed to achieve photo-realistic novel view synthesis and relighting by leveraging 3D Gaussian Splatting (3DGS) and deferred shading. Inverse rendering aims to accurately model scene materials, geometry, and lighting from images, a task complicated by the need to account for indirect lighting, which prior methods often model poorly. GI-GS improves upon these methods by incorporating efficient path tracing and deferred shading to compute indirect lighting, which leads to better handling of complex light-object interactions. The framework first uses a G-buffer to capture scene details and perform physically-based rendering (PBR) for direct lighting. Then, it applies lightweight path tracing to compute indirect lighting based on previous results, enabling more realistic global illumination. The authors demonstrate that GI-GS outperforms previous techniques in rendering quality and efficiency, making it a state-of-the-art method for novel view synthesis and relighting.

### Strengths
The paper is well-written and easy to follow, and it includes comprehensive relighting works from the past.

1. GI-GS uses path tracing with deferred shading to accurately model indirect lighting, achieving realistic relighting and view synthesis.

2. By combining 3D Gaussian Splatting with a physically-based pipeline, GI-GS efficiently reconstructs detailed geometry and materials for high-quality results.

3. The framework decouples direct and indirect illumination, enabling good-quality relighting across various conditions.

### Weaknesses
1. This method leverages image-based lighting (IBL) to simulate illumination from multiple directions, addressing both diffuse and specular reflections as outlined in Section 4.2. However, the decomposed diffuse and specular components are not evaluated, even in the supplementary material, which I believe is crucial for your lighting model. The lack of evaluation for the separated diffuse and specular components is a significant oversight. The specular component, in particular, is critical for accurate rendering, and without a proper analysis, it's difficult to assess the quality of the lighting model. The method should demonstrate the accuracy of the separation, especially given the complexity of disentangling these components in real-world scenes.

2. The paper benchmarks against the TensoIR, Gaussian Shader and GS-IR, where these methods, including the relightable 3D Gaussian, offer accessible material evaluations. While the proposed method includes a material map (albedo, specular, roughness, etc.) in its pipeline, there should be an analysis or evaluation of the decomposed material, as material properties are central to reflection. The absence of a detailed material analysis, particularly for specular and roughness, is a major weakness. While albedo is evaluated, the other material properties are equally important for accurate reflection modeling. The paper should provide a quantitative and qualitative analysis of these material components to validate the accuracy of the inverse rendering process. The lack of such analysis makes it difficult to assess the overall quality of the material decomposition.

3. The paper claims that the calculated occlusion models shadowing, a key contribution similar to that of benchmarked methods. However, the experiments do not include a strong evaluation of this feature, despite visibility and occlusion information being available in the benchmarked methods. The evaluation of occlusion is insufficient. While the method claims to model shadowing through occlusion, there is no rigorous comparison against existing methods that also provide visibility and occlusion information. A more detailed evaluation, including quantitative metrics and visual comparisons, is necessary to substantiate this claim. The paper should demonstrate that its occlusion modeling is not only present but also accurate and competitive with existing approaches.

4. Additionally, for indirect lighting, which accounts for bouncing and interreflection, there is no ground truth to verify the accuracy of the modeled indirect illumination. This could also be interpreted as the residual of your reflection during optimization. The lack of ground truth for indirect lighting makes it difficult to validate the accuracy of the modeled interreflection and bounce lighting. The paper should provide a more detailed justification for the indirect lighting model and consider alternative evaluation strategies, such as comparing against physically-based rendering simulations or using proxy metrics that correlate with indirect lighting quality. Without such validation, the accuracy of the indirect lighting model remains questionable.

I have to challenge the novelty and quality of the proposed method, as both occlusion and indirect lighting are also addressed and calculated similarly in these baseline methods and relighting evaluation didn't prove the proposed method achieved better quality than the previous method.

### Questions
1. How does the method validate the effectiveness of its decomposed diffuse and specular components, given that these are crucial for its lighting model but are not evaluated?

2. Given the importance of material properties for accurate reflection, why is there no analysis of the decomposed material map components (albedo, specular, roughness), especially since benchmarked methods include accessible material evaluations?

3. How does the paper substantiate its claim that calculated occlusion effectively models shadowing, considering that benchmarked methods provide visibility and occlusion data but no strong evaluation is presented for this feature?

4. Without ground truth for indirect lighting, how can the accuracy of modeled interreflection and bounce lighting be verified, and might these effects reflect residuals of reflection optimization?

5. In what ways does the proposed method’s relighting evaluation demonstrate superiority over existing methods, especially given that occlusion and indirect lighting calculations are also present in baseline methods?

### Soundness
2

### Presentation
3

### Contribution
2
