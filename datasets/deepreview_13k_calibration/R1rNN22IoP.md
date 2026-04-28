# MeshLRM: Large Reconstruction Model for High-Quality Meshes

- Decision: Reject
- Avg Score: 6.25
- Scores: 8, 6, 6, 5

## Abstract
We propose MeshLRM, a novel LRM-based approach that can reconstruct a high-quality mesh from merely four input images in less than one second. Different from previous large reconstruction models (LRMs) that focus on NeRF-based reconstruction, MeshLRM incorporates differentiable mesh extraction and rendering within the LRM framework. This allows for end-to-end mesh reconstruction by fine-tuning a pre-trained NeRF LRM with mesh rendering. Moreover, we improve the LRM architecture by simplifying several complex designs in previous LRMs. MeshLRM's NeRF initialization is sequentially trained with low- and high-resolution images; this new LRM training strategy enables significantly faster convergence and thereby leads to better quality with less compute. Our approach achieves state-of-the-art mesh reconstruction from sparse-view inputs and also allows for many downstream applications, including text-to-3D and single-image-to-3D generation.
  \keywords{Sparse-view reconstruction \and High-quality mesh \and Large Reconstruction Models}

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper presents a transformer-based framework for efficient 3D mesh reconstruction from sparse views. Unlike previous approaches relying solely on NeRF-based volumetric models with marching cubes as a post-hoc mesh extraction solution, MeshLRM incorporates differentiable mesh extraction and rendering directly within the LRM framework. The model undergoes sequential low-to-high-resolution training, followed by DiffMC-aware fine-tuning. Key contributions include DiffMC integration for improved mesh quality, a novel ray opacity loss to eliminate floaters, and training strategies like progressive resolution scaling for improved convergence.

### Strengths
The paper contains valuable insights that improve surface reconstruction quality and speed for LRMs. It makes a straightforward yet impactful contribution by integrating a differentiable isosurface extraction method — specifically DiffMC — into the training framework, enabling more precise mesh extraction. The proposed ray opacity loss demonstrates substantial qualitative improvements, effectively resolving the floater issue. Additionally, the insight about MLP over-parameterization leading to rendering speed slowdowns is important and directly applicable to other LRM-based approaches.

The paper is well-written and structured, clearly guiding the reader through model design, training strategy, and key components such as ray opacity loss and progressive resolution scaling, with their necessity well-supported by ablations.

### Weaknesses
The paper offers a specific training recipe for LRMs, but key components of this approach appear underexplored:

- The ray opacity loss is not entirely novel; ray regularization for zero density in empty space is a standard technique in NeRF approaches. While the formulation may be unique, it is unclear how it performs against simpler density-to-zero regularization or background mask losses. Specifically, the paper does not discuss how the ray opacity loss compares to directly penalizing density values in empty space or using a background mask to enforce zero density outside of the object. A more thorough comparison would be beneficial.
- The inclusion of DiffMC, while valuable, also lacks thorough evaluation. Alternative isosurface extraction methods, such as DMTet, are available, yet the rationale for choosing DiffMC over these options is not discussed. The paper should provide a more detailed justification for this choice, including a discussion of the trade-offs between different methods in terms of speed, memory usage, and mesh quality. Furthermore, the paper does not explore how the performance of DiffMC varies with different density thresholds, which could significantly impact the final mesh quality.
- The paper’s comparative analysis is limited and primarily focuses on a single baseline (Instant3D-LRM). Although MeshLRM demonstrates quantitative improvements, qualitative results are mixed, showing reduced high-frequency details in geometry and texture. For example, textures in most samples in Figure 5 lack sharpness compared to the baseline, and the geometry generally appears to be over-smoothed, e.g. frog’s legs merge with the stand in Sample 4, Fig. 5. The paper should include comparisons with more recent methods to better contextualize its performance.
- The paper does not discuss recent works, such as InstantMesh or TripoSR, suggesting it may not have been updated since its initial publication on Arxiv six months before the submission. Additionally, the baselines used for comparison are approximately a year old, which dilutes the paper's relevance to the community given the rapid advancements in the field.

While the addition of isosurface extraction is important, it lacks thorough investigation. Most training strategy improvements are supported by ablations, but these are not evaluated against alternative options. The value of the paper's proposed recipe is further diluted by the existence of other potentially superior reconstruction methods, such as InstantMesh and TripoSR.

### Questions
- Is there evidence supporting DiffMC as a superior differentiable isosurface extraction method for mesh extraction compared to alternatives like DMTet or FlexiCubes?
- Is there comparative evidence showing that the proposed ray opacity loss formula outperforms existing density regularization techniques?
- How was the density threshold determined for DiffMC vs. standard Marching Cubes in the ablations? This choice could significantly impact surface quality, particularly in the non-finetuned case.
- Given the claimed speed improvements, how does MeshLRM's performance compare to other recently published approaches?

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
The paper introduces MeshLRM that outputs a density and color field suitable for mesh extraction using marching cubes. Building on LRM, MeshLRM incorporates a second training stage where NeRF rendering is replaced with differentiable marching cubes (diffMC) rendering. The authors also present comprehensive ablation studies on additional losses, such as Ray Opacity Loss, which enhance the robustness of the second training stage.

### Strengths
The paper is clearly written, and the quality of the result is noticeably better than previous NeRF-based approach – Inst-LRM in terms of extracted mesh quality. From the perspective of engineering and practicality, the design choice proposed in this paper is sound and seems effective. The ablation in the paper is extensive and seems sound to me.

### Weaknesses
First, I have some reservations about the title "MeshLRM" and certain descriptions in the introduction, which may be over-claimed.  For instance, in lines 67-68, the statement, "We propose to address this with MeshLRM, a novel transformer-based large reconstruction model, designed to directly output high-fidelity 3D meshes from sparse-view inputs," could be misleading. In my view, the network does not "directly" output a mesh; instead, it produces density and color fields similar to its baseline model, which still require marching cubes to extract the mesh. The phrase "direct output mesh" more accurately describes a different family of models, such as MeshGPT [1].

2nd, another concern is the novelty of the paper. While combining LRM with diffMC is an effective and practical engineering approach, the concept appears somewhat ad hoc, mainly merging existing components rather than presenting deep or non-trivial new insights. The core idea of using differentiable marching cubes for mesh extraction from a learned density field is not entirely new, and the paper could benefit from a more thorough discussion of how this approach differs from or improves upon existing methods that use similar techniques. The paper also does not fully explore the limitations of the marching cubes algorithm itself, such as its sensitivity to the choice of isovalue, which can significantly impact the quality of the extracted mesh. Furthermore, the paper could benefit from a more in-depth analysis of the computational cost associated with the differentiable marching cubes step, particularly in comparison to alternative mesh extraction techniques. However, this does not constitute a significant reason for rejection, as the paper still meets the typical standards of previously accepted work.

### Questions
Regarding the second stage of training, I am curious if the authors could elaborate on which parts of the network require fine-tuning. Specifically, could the model be effective with fine-tuning only the tiny MLPs or merely the last few layers of the transformer blocks?

### Soundness
4

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
This paper presents MeshLRM, a large reconstruction model that enables the generation of high-quality 3D meshes from posed sparse-view images. It incorporates differentiable mesh extraction and rendering within the LRM framework, simplifying the architecture and improving training strategies for faster and better quality reconstruction. The model introduces a ray opacity loss for stable DiffMC-based training and achieves state-of-the-art performance in sparse-view mesh reconstruction, supporting applications like text-to-3D and single-image-to-3D generation.

### Strengths
- The incorporation of differentiable mesh extraction and rendering within the LRM framework is reasonable, enabling end-to-end mesh reconstruction without post-optimization steps.
- The introduction of the ray opacity loss is a novel contribution that addresses the challenge of stabilizing training for mesh reconstruction.
- The paper is well-written and easy to follow. The mesh visualization in the teaser is impressive.

### Weaknesses
 - Limited evaluation on real-World data.  
The paper primarily evaluates MeshLRM on synthetic datasets. While the performance on these datasets is impressive, the model's ability to generalize to real-world images with complex lighting and materials is less explored. Incorporating more experiments on real-world datasets such as OmniObject3d [1] could provide a clearer picture of the model's practical applicability. Specifically, the paper lacks a detailed analysis of how the model handles variations in texture, reflectance, and illumination conditions commonly found in real-world scenarios. The absence of such analysis makes it difficult to assess the robustness of the proposed approach.

- Incomplete discussion and comparison with newer baselines.  
The paper compares with Instant3D and LGM, the former is not open-sourced, while the latter is based on Gaussian Splatting and leverages a ConvNet instead of transformer. I think there are some newer methods should be discussed and compared in the paper, e.g., InstantMesh [2], GeoLRM [3] and MeshFormer [4]. Especially, I believe InstantMesh is a pefect baseline for comparison since it is open-sourced and also adopts the "LRM+differentiable mesh extraction" paradigm. The lack of comparison with these more recent methods, particularly those that also leverage large reconstruction models and differentiable mesh extraction, limits the paper's ability to demonstrate its true state-of-the-art performance and highlight its unique advantages.

- Concerns on technical novelty and training stability.  
Pioneer works like Magic3D [5] and InstantMesh have explored the pipeline of two-stage 3D generation by combining the NeRF and mesh representations, so I think the usage of mesh representation is reasonable but not novel.  
Besides, I have another concern on the training stability of mesh representation. According to the paper, the training process of MeshLRM is splitted into two stages, using NeRF and mesh respectively, and "Once trained with volume rendering, our model already achieves high-fidelity sparse-view NeRF reconstruction, which can be rendered with ray marching to create realistic images" (Section 3.3, line 272). Why is stage 1 essential if the proposed ray opacity loss can indeed stablize the training process on the mesh representation? What if we skip stage 1 and directly train the model on the mesh representation from scratch? I think the authors should add some discussions on this issue in the paper. The paper does not adequately explore the necessity of the two-stage training approach. A more detailed analysis of the challenges associated with directly training the mesh representation, and a comparison of the performance with and without the NeRF initialization, would be beneficial.

### Questions
My questions have been listed in the weakness part, the author's response on them will serve as the main basis for my final rating. Besides, the paper does not mention the future availability of code or pre-trained models, which is crucial for reproducibility and further research by the community. Providing such resources would greatly benefit the field.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This manuscript introduces a two-stage feed-forward large reconstruction model that utilizes sparse views as input. In the first stage, NeRF-like volume rendering is employed for supervision, with progressive training regarding resolution. In the second stage, Differentiable Marching Cubes (DiffMC) is leveraged to convert the density field into a mesh, which supports fast rendering and geometry supervision. With the integration of a ray-opacity loss, MeshLRM is capable of generating high-quality meshes. Furthermore, by simplifying the encoder, MeshLRM achieves faster inference speeds.

### Strengths
1. Utilizing DiffMC in LRM is novel. Indeed, meshes offer superior 3D representation.
2. The reconstructed mesh appears to be of high quality, featuring smooth geometry.
3. The proposed ray-opacity loss is technically sound and well-founded.

### Weaknesses
1. The definition of post-optimization in Line 56 is unclear. In traditional multi-view reconstruction tasks with SDF-based volume rendering, meshes can be directly extracted by Marching Cubes (MC) by identifying the zero-level set without any post-optimization. It remains unclear what specific optimization steps are being referred to here, and how they differ from standard mesh extraction from an SDF.
2. A discussion is lacking on why converting NeRFs into meshes leads to a significant drop in rendering quality and geometric accuracy, as mentioned in Line 66. The manuscript should elaborate on the specific mechanisms that cause this degradation, such as the introduction of artifacts or loss of fine details during the mesh conversion process.
3. The definitions of the post-processing steps, specifically Marching Cubes in NeRF and Differentiable Marching Cubes in MeshLRM, should be illustrated more clearly. If both processes are considered post-processing, then the disadvantages of NeRF should not include the need for additional post-optimization. The distinction between these two post-processing steps needs to be more precise, and the implications of each choice should be discussed in detail.
4. There are some grammatical issues. For example, a comma is missing in Line 76.
5. I recommend adding an illustration in Line 75 to depict why NeRF-based LRM pretraining is important. The manuscript should provide a visual comparison to demonstrate the necessity of the NeRF pretraining stage, perhaps showing the results of direct mesh training versus the proposed two-stage approach.
6. Considering there are two-stage optimizations, the claim of end-to-end optimization in Line 83 is not precise enough. The manuscript should clarify the extent to which the two stages are truly optimized end-to-end, and acknowledge any limitations or dependencies between the stages.
7. The assertion in Line 205 is not convincing enough. A comparison with In3D-LRM does not substantiate the claim that DINO cannot handle high-resolution images. There should be an ablation study in MeshLRM to adequately discuss why DINO is not necessary. Since you claim a contradiction in this paragraph, it is crucial to address this. The manuscript needs to provide a more thorough analysis of the impact of DINO features on the performance of MeshLRM, including a quantitative comparison with and without DINO.
8. There is no quantitative comparison between NeRF-based LRM and Mesh-based LRM. Additionally, it appears that NeRF-based LRM achieves better PSNR. The manuscript should include a direct quantitative comparison between the two, using appropriate metrics to assess both rendering quality and geometric accuracy.
9. There is a lack of quantitative comparison in the progressive training regarding resolution. The manuscript should provide a detailed analysis of the impact of the progressive training strategy on the final reconstruction quality, including a quantitative comparison with training directly at the target resolution.
10. There are too few comparison methods. Only LGM and In3D are compared. The manuscript should include a more comprehensive comparison with other state-of-the-art methods in the field, to better demonstrate the advantages of the proposed approach.

### Questions
1. Why are density fields considered more compatible with the Marching Cubes step in Line 73? In traditional multi-view reconstruction tasks, Signed Distance Functions (SDFs) have proven to be more effective than density fields for mesh reconstruction, as surfaces are clearly defined by the zero-level set. What makes density fields preferable in this context?

2. I  do not fully understand the challenges associated with the second-stage mesh-based LRM optimization. When using Flexicube in Instantmesh, there do not appear to be issues related to mesh floater. Could you elaborate on the advantages of choosing Differentiable Marching Cubes (DiffMC) over Flexicube?

### Soundness
2

### Presentation
3

### Contribution
2
