# Inverse Rendering for Shape, Light, and Material Decomposition using Multi-Bounce Path Tracing and Reservoir Sampling

- Decision: Accept
- Scores: 8, 3, 8, 6

## Abstract
We present a novel two-stage inverse rendering framework that jointly reconstructs and optimizes explicit geometry, materials, and lighting from multi-view images. 
Unlike previous methods that rely on implicit irradiance fields or oversimplified path tracing algorithms, our method first extracts an explicit triangular mesh in the initial stage. 
Subsequently, it employs a more realistic physically-based inverse rendering model in the second stage, utilizing multi-bounce path tracing and Monte Carlo integration. 
By leveraging multi-bounce path tracing, our method not only effectively estimates indirect illumination (including self-shadowing and internal reflections). but also enhances the intrinsic decomposition of shape,
material, and lighting. Moreover, we incorporate reservoir sampling into our framework to address the noise in Monte Carlo integration, enhancing convergence and facilitating gradient-based optimization with low sample counts. 
Through both qualitative and quantitative assessments across various scenarios, especially those with complex shadows, we demonstrate that our method achieves state-of-the-art performance in decomposition results.
Additionally, our optimized explicit geometry supports further applications in scene editing, relighting, and material editing, compatible with modern graphics engines and CAD software.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes a two-stage inverse rendering framework to jointly reconstruct geometry, materials, and lighting from multi-view images. In this framework, geometries are represented as triangular meshes with trainable vertex offsets, and this representation enables explicit path tracing technique similar to the classic PBR pipeline, which is sped up with reservoir sampling for direct illumination. With these contributions, the reported results showed better reconstruction quality for geometry, materials, and lighting both quantitatively and qualitatively.

### Strengths
1. This work adapts well-studied PBR techniques, such as path tracing and reservior sampling, to the domain of inverse rendering. I personally appreciate the adaptation of these computer graphics knowledge to address a more computer vision problem, and the results do show an improvement with these contributions.
2. The most related work to this submission is NVdiffrec-MC. From the reported results, this work achieves a better performance both quantitatively and qualitatively.
3. This paper is well written and easy to follow. The entire formulation is physically sound and all the theoretical details are explained in an intuitive way for readers with background in physics-based rendering and inverse rendering. Sufficient ablation studies are provided to verfiy the effectiveness of each component.
4. Given the long-standing and inherently ill-posed nature of inverse rendering, I believe this work makes a valuable contribution to this field. It can inspire further research and solutions aimed at advancing the understanding and solving of this challenging problem.

### Weaknesses
1. This work relies on a high-quality intialization of geometry, for which the authors chose NeuS2. However, the authors acknowledged that some artifacts may still persist in certain areas, which cannot be fully corrected by the subsequent refinement step. Additionally, they discussed the instability of DMTet for geometry representation, which is used by NVdiffrec-MC. I would be interested to see some visual comparisons between these two geometry representations.
2. As the formulation only considers primary rays, it cannot handle objects with transparent materials (e.g., a glass sphere exhibiting Fresnel effects). This might be an interesting direction to explore for future work.

### Questions
1. In Lines 084 -- 086, you mention the effectiveness of a denoiser inspired by NVdiffrec-MC; however, I was unable to find further discussion or detailed follow-up content about it in the manuscript. Could you elaborate on the design of this denoiser and how effective it is for the final rendering?
2. Since an explicit environment map is also being optimized, it would be helpful to include visualizations of the optimized environment maps for some scenes to better understand the impact of this optimization.
3. In Lines 401 -- 403, you mentioned some adjustments made to the albedo and rendered images. Could you provide more details about the specific adjustments used?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a framework for joint reconstruction of shape, material and lighting. The framework consists of two stages. In the first stage, it uses neural SDF optimization to reconstruction the initial object geometry and radiance field. In the second stage, it uses differentiable rendering combined with differentiable marching cube to optimize geometry, materials and lighting, with indirect illumination being properly handled. Experiments on synthetic and real object datasets show that the proposed framework achieves compelling results compared to several strong baselines.

### Strengths
1. A novel inverse rendering framework that combines the advantages of neural SDF reconstruction and physically-based differentiable rendering. 
2. The paper overall is easy to follow and well organized. 
3. High-quality inverse rendering results on both synthetic and real datasets compared to several prior strong baselines.

### Weaknesses
1. Technical novelties of the paper is very limited.

This paper's major contributions are covered by two previous works that are not properly cited. Neural-PBIR, Cheng et al.. ICCV 2023 adopts a similar pipeline to first train a neural SDF to get high-quality geometry and then run PBDR to further optimize geometry, materials and lighting. Neural-PBIR also models multiple bounces and uses unbiased gradient for geometry optimization in the PBDR stage. "Parameter-space ReSTIR for Differentiable and Inverse Rendering", Chang et al., SIGGRAPH 2023 adopts Reservoir sampling into inverse rendering by exploring the temporal coherence across gradient iterations. It provides a much deeper theoretical analysis and more detailed comparisons. 

It will significantly enhance the paper if we can explicitly discuss how the proposed method differs from or improves upon Neural-PBIR and Parameter-space ReSTIR. We may consider adding a paragraph comparing the propoesd approach to these prior works, highlighting any key differences or advancements.

2. Design choices of Reservoir sampling may not be completely technically sound. 

It is reasonable to explore temporal coherence to reduce the noise and hence reduce the sample. as demonstrated in Chang et al. SIGGRAPH 2023. However, the motivations described in the Eq. (9) emphasizes that there is no analytical integral of $L(\omega_i)f(\omega_i, \omega_o)$ so that we need reservoir sampling to approximate the distribution of $L(\omega_i)$. This makes much less sense as there is a clear solution to sample the environment map lighting and we can even consider MIS to sample both BRDF and lighting. The last paragraph of Section 4.1 mentioned temporal reuse and spatial reuse but we may need more detailed discussion. 

It will be beneficial to have a deeper discussion to why we need reservoir sampling to sample environment map and also more analysis on the impact of temporal reuse and spatial reuse. 

3. Optimization time is too long.

The total optimization time is 4.5 hours, which is 4 times longer than Neural-PBIR. This is contradictory to the motivation of using reservoir sampling to reduce the number of sample. One thing to note is that the running speed of PBDR heavily depends on system engineering. This paper may consider using more advanced PBDR framework, such as Mitsuba 3, to see if the optimization time can be significantly reduced. A breakdown of the current optimization will also help us identify the issue. 

4. Other minor issues:
1. Line 196 - 202: Why not directly use Neus2 for shape reconstruction? Why run instant-NGP first? Please provide more discussion and analysis. 
2. Line 242: the notation $\Delta \mathbf{v} $ is in consistent with the notation in Figure 2 $\Delta \mathbf{x}$. Please ensure notation consistency to avoid confusion. 
3. Line 263: Why skip metallic? Please provide reasoning on this design choice and the potential impacts. 
4. Experiments: Can we include experiments on Stanford-ORB to have a more complete comparison with prior methods? Can we show visualization of the environment maps to help reader understand the lighting reconstruction quality?

### Questions
I would like to see more arguments about technical novelties in the paper and how this paper is different from prior work. In addition, more technical details of reservoir sampling will be welcome.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The novel mesh-based reconstruction method, Multi-bounce Inverse Rendering using Reservoir Sampling (MIRReS), introduced in this paper, decomposes geometry, material parameters (diffuse albedo and roughness), and illumination from multi-view images using multi-bounce path tracing with Monte Carlo integration. 
The method produces reconstruction results of unparalleled quality due to the authors' use of global illumination (Monte Carlo ray tracing) to explicitly and physically account for indirect lighting. This is only possible because, for the first time in Inverse Rendering, ReSTIR (Reservoir-based Spatio-Temporal Importance Resampling) is employed to accelerate the costly global rendering.
An evaluation of the new method and a comparison with the latest and best reconstruction methods for geometry, material and lighting (NVDiffRecMC 2022, TensorIR 2023 and GS-IR 2023) shows the comparatively very good reconstruction quality, both of geometry and albedo and with regard to relighting the reconstructed scenes.

### Strengths
1.) The paper is very well written and easy to follow.
2.) It contains a very good summary of the current state of the art on Inverse Rendering for Shape, Light and Material reconstruction.
3.) The idea to use Reservoir-based Spatio-Temporal Importance Resampling to reduce the computational load of a global illumination calculation is novel and should definitely be published.

### Weaknesses
There is no code available to evaluate the method  independently. 

The evaluation and the (very good) comparison with other state-of-the-art methods lack a comparison of the results of the specular reflection. Is this estimate much worse than for the other methods? In the appendix, this is mentioned as a limitation of the procedure.

### Questions
As there is currently no code from which further details about the method can be obtained. This leaves a few questions unanswered. 
1.) How does the rough estimate of the geometry in stage 1 of the algorithm affect the rendering, and how does the algorithm determine when the geometry is sufficiently accurate to begin material reconstruction and global illumination simulation in stage 2? 
2.) In this context, it would be interesting to know how the inaccurate initial estimate of the geometry affects the estimate of the specular reflections. 
3.) The paper mentions an important feature: the reconstruction result as a triangle mesh is compatible with current graphics engines and CAD software. However, the texture is modeled implicitly using Instant NGP in the method. How is it transferred to the triangle mesh?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents MIRReS to jointly optimize geometry, materials, and lighting. The authors propose to extract an explicit triangular mesh in the initial stage. Subsequently, they employ physically-based rendering and utilize multi-bounce path tracing and Monte Carlo integration for indirect illumination. They also incorporate a novel technique called reservoir sampling to address noise in Monte Carlo integration.

### Strengths
1. The paper propose to use path tracing for indirect illumination, which use PBR to compute the indirect illumination. This can be more accurate than using radiance field cache.
2. The paper propose to use reservoir sampling in the integral of rendering equation (only for direct light).

### Weaknesses
1. Compare to using implicit field as geometry, the use of triangle mesh may harm the rendering equality. This is common as the mesh extraction can lead to an degration in geometry quality.
2. The paper proposes to refine mesh with fixed face topology, only an offset of each vertice can be optimized, which I think the influence of the refinement is limited. 
3. A derivation of Equation 9 can improve the clarity. And $p_{dir}$ in $\gamma_i$ remains unkown.

### Questions
see weakness

### Soundness
3

### Presentation
3

### Contribution
3
