# Geo-3DGS: Multi-view Geometry Consistency for 3D Gaussian Splatting and Surface Reconstruction

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5, 5

## Abstract
Recently, the emergence of 3D Gaussian Splatting (3DGS) has made real-time and high-quality rendering possible. However, it is still challenging for 3DGS to reconstruct accurate geometry surfaces and achieve higher-quality rendering. To address these challenges, we propose to leverage multi-view geometry consistency for 3DGS and surface reconstruction. We reveal that there exists multi-view geometry inconsistency in 3DGS, preventing 3DGS from achieving higher-quality rendering and accurate surface reconstruction. To mitigate the geometry inconsistency, we first develop a multi-view photometric consistency regularization to constrain the rendered depth of 3DGS, which helps establish more stable and consistent 3D Gaussians to facilitate both rendering and surface reconstruction. To reconstruct geometry surfaces from 3DGS, we introduce a neural Signed Distance Function (SDF) field to represent continuous geometries of 3DGS. Then, we propose a geometry consistency-based SDF learning strategy, which leverages multi-view geometry consistency cues from 3DGS to efficiently optimize the SDF field for surface reconstruction. Extensive experiments on various datasets demonstrate that our method achieves both high-quality rendering and accurate surface reconstruction while keeping a good efficiency. Our code will be released upon publication.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents a new 3D reconstruction method that extends 3D Gaussian Splatting. In detail, the paper presents two main contributions on top of 3D GS. 
1. Usage of photometric loss as a way to regularize ambiguity, augment densification
2. Usage of SDF as a way to promote geometric consistency
In addition to these contributions, the paper provides evaluation on multiple standard dataset for benchmarking against existing state of the art approaches.

### Strengths
The paper makes it clear that the additional regularizations, derived from insights from existing 3D reconstruction methods that promote joint photometric / geometric regularization such as COLMAP MVS, vastly helps the quality and reliability of reconstruction. Each contributions are tailored for 3D Gaussian Splatting pipeline. For example, photometric loss is not only used as a regularization (which is commonly used in existing NeRF or MVS literatures), but as a densification. Similarly, SDF is not used as a geometric representation, but rather, as a way to promote geometric consistency.

### Weaknesses
Major concern with the paper is that the method is not new. Usage of photometric consistency as well as geometric consistency has been around for years in 3D reconstruction, starting from MVS to NeRF. The reviewer understands that these may not have been brought in, in the domain of 3D GS, but finds it unsure if the contributions are enough for ICLR. 

Also, based on the ablation studies provided in the table 4, the reviewer finds photometric regularization and densification to be not as important, compared to the SDF based geometric consistency. It seems like that the model is going for rendering vs. geometric accuracy tradeoff, which is hard to justify as major contribution.

### Questions
What types of SDF architecture has been used? There has been advancements in SDF networks that may benefit your model as well.

Has the authors tried different initialization schemes? There may be better way to initialize SDF given that 3D Gaussians reside near the surfaces (e.g, solving Poisson Equation using Gaussin Splats)

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces a method to regularize the surface reconstruction process in Gaussian Splatting while preserving its rendering quality. Although Gaussian Splatting is effective for rendering, it has limitations regarding multi-view consistency, which this paper addresses. As illustrated in Figure 2, these limitations result in poor depth maps, leading to suboptimal 3D surface reconstructions. To address these issues, the authors propose integrating traditional multi-view stereo techniques, such as PatchMatch [1], to enhance multi-view consistency within the Gaussian Splatting framework. The paper's core contribution is to adapt and extend these techniques to improve surface reconstruction quality while preserving Gaussian Splatting’s high rendering fidelity. Experimental results on the Tanks and Temples and DTU datasets demonstrate that this approach achieves improved surface reconstruction quality without compromising rendering performance.

[1] Schönberger, Johannes L., et al. "Pixelwise view selection for unstructured multi-view stereo.", ECCV 2016.

### Strengths
**Clarity**: The paper is well written and the entire math is easy to follow.\
**Reproducibility**: The code will be released if accepted which will help to reproduce results. \
**Significance**: Extracting high quality 3D surface from Gaussian Splatting without affecting the rendering quality is a relevant problem.

### Weaknesses
 **Novelty:** While the paper presents promising results on the surface reconstruction benchmark, the contribution feels somewhat incremental. The approach primarily extends regularization techniques from NeRF-based methods, such as those introduced in GeoNeus [2], to the Gaussian Splatting framework. The equations used closely resemble those in GeoNeus, with both approaches aiming to improve surface consistency, though GeoNeus achieves this within a volume rendering framework, whereas this work applies it to Gaussian Splatting. It would be helpful if the authors could further clarify the distinct advantages of adapting these regularization specifically to Gaussian Splatting, as well as any unique challenges addressed in this framework. The paper should also discuss the limitations of directly applying these regularization techniques designed for volume rendering to the discrete nature of Gaussian Splatting, particularly regarding how the method handles the sparse and non-uniform distribution of Gaussians compared to the continuous nature of volume rendering.

**Results:** Although this paper shares similarities in approach with GeoNeus, it does not provide a direct comparison of surface reconstruction quality with GeoNeus, as seen in Table 1 for the DTU dataset. Additionally, the improvements in surface reconstruction quality over previous methods appear modest. In the Tanks and Temples dataset, the method’s reconstruction quality is notably lower than that of Neuralangelo [3]. Clarifying the reasons for these results, particularly regarding the performance gap with Neuralangelo, would strengthen the evaluation and highlight any inherent trade-offs or challenges in adapting this approach within the Gaussian Splatting framework. Specifically, the paper should analyze why the proposed method does not achieve comparable results to Neuralangelo, considering that both methods utilize hash grids for acceleration. A more detailed analysis of the architectural and optimization differences that lead to this performance gap is needed.

### Questions
- The convergence time of Neuralangelo seems significantly higher (24hr) compared to this method (48m) as shown in table 2. What is the reason behind this even though both the methods use hash grids? A plot regarding time vs chamfer distance or time vs F1 score will help to understand the convergence speed of both the methods correctly. 

- I am not quite sure what is the purpose of Equation 11? An ablation regarding its effect on the final reconstruction accuracy will be helpful.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper aims to improve the quality of the rendering results and learned geometry. They exploited the multi-view projection to check the inconsistency of 3DGS and used patch-based multi-view projection to add consistency regularization. Meanwhile, they leveraged these consistency information to guide the densification of 3DGS, combined the SDF module to learn the continue geometry, and injected the multi-view projection to constrain the SDF module.

### Strengths
This paper investigate the inconsistency in 3DGS and incorporate the multi-view projection to assist the regularization, densification and  geometry optimization of 3DGS model:
- use the multi-view projection to achieve the consistency regularization.
- use the filtered multi-view consistent depth to achieve densification of Gaussian points.
- use the SDF module to optimize the geometry and inject the multi-view projection.

### Weaknesses
 - to my knowledge, multi-view projection is also a strategy to enhance the accurate of geometry in the multi-view visible region, and it still cannot mitigate the small-overlap or textureless issues you mentioned. And the example shown in Fig. 1 is still a texture-rich scenes (not the true textureless scene like the white background) to some extent, thus the depth of the table region can still be retained.
- maybe combining the SDF module with the 3DGS cannot be regarded as a contribution of this paper, as there are some methods have tried this strategy like NeuSG [1], GSDF [2] and 3DGSR [3]. Maybe the difference is that this paper further use the geometry constraints proposed in Geo-NeuS [4], and I think it's hard to say that this module is novel enough.
- the ablation and experiment of the densification strategy are not enough. This paper used the downsample to control the densified points, and how the number of points affect the performance and efficiency? It's unclear how the downsampling rate affects the final reconstruction quality and the computational cost. A more thorough analysis of this parameter is needed.
- some typos, like Line 261, Tab. 1 and Tab. 2.

### Questions
In the multi-view photometric consistency regularization, how do you choose the base pixel used to calculate the multi-view consistency? And the 3DGS is not the ray-based rendering model like NeRF or NeuS, why do you still choose pixel/patch based projection instead of directly using the entire rendered depth to compute the multi-view projection loss? So what about the performance differences between these two strategies?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
Geo-3DGS first analyzes the consistency problem of depth maps generated from 3DGS and proposes a multi-view photometric consistency regularization to address it. Geo-3DGS utilizes two branches to model scenes: GS for rendering and SDF for surfaces, respectively. Comprehensive experiments demonstrate that Geo-3DGS achieves excellent performance.

### Strengths
1. Geo-3DGS reveals that the depth maps from the GS representation are not consistent across multiple-view images and introduces a regularization technique to enforce multi-view consistency.
2. The paper is good written and easy to follow.

### Weaknesses
1. **Lack of Novelty.** The concept of combining the advantages of 3DGS with neural SDF to enhance both rendering and reconstruction quality has already been proposed by GSDF. It would be beneficial to explain the differences in detail and conduct a comprehensive comparison experiment.
    1. In Section 'Geometry-Assisted Gaussian Densification,' how can the balance between new Gaussian primitives derived from depth maps and the existing Gaussians be achieved? Moreover, since depth maps generated by 3DGS are generally of lower quality compared to those from SDF, why not use depth maps from SDF to guide Gaussian densification, similar to the approach in Section 3.2.2 'Geometry-Aware Gaussian Density Control' in GSDF?
    2. In Section ‘3DGS-driven SDF initialization’, the idea of depth rendered from 3DGS to help initalize SDF is also similar with GSDF, in sec. 3.2.1 ‘Depth Guided Ray Sampling’.
2. **Poor typography.** In Tables 1 and 2, the timing for each baseline is completely incorrect. In Figure 5, it's unclear what's happening—there are too many lines cluttering the figures.
3. **Poor performance.** In surface reconstruction, Geo-3DGS performs significantly worse than Neural-Angelo in Table 2. I'd also like to see Neural-Angelo's performance on the DTU dataset in Table 1. In terms of rendering quality, Geo-3DGS still underperforms compared to 3DGS and Scaffold-3DGS, as shown in Table 3.
4. **Lack of significant improvement.** In the ablation study, the multi-view photometric consistency regularization, which is the paper's most novel contribution, only improves the F1 score by 0.02.
5. **No demos submitted**

### Questions
Which SDF branch did the authors use? Is it the hash-encoding-based Neus? What are the training iterations for the SDF branch? Also, why is the training time for Geo-3DGS only 48 minutes on the Tanks and Temples dataset and 45 minutes on the DTU dataset? I would expect training on Tanks and Temples to be much more challenging than training on DTU.

### Soundness
3

### Presentation
3

### Contribution
2
