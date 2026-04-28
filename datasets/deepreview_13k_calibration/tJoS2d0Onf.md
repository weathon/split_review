# SV4D: Dynamic 3D Content Generation with Multi-Frame and Multi-View Consistency

- Decision: Accept
- Avg Score: 6.25
- Scores: 5, 6, 8, 6

## Abstract
We present Stable Video 4D (SV4D) — a latent video diffusion model for multi-frame and multi-view consistent dynamic 3D content generation.
Unlike previous methods that rely on separately trained generative models for video generation and novel view synthesis, we design a unified diffusion model to generate novel view videos of dynamic 3D objects. 
Specifically, given a monocular reference video, SV4D generates novel views for each video frame that are temporally consistent.
We then use the generated novel view videos to optimize an implicit 4D representation (dynamic NeRF) efficiently, without the need for cumbersome SDS-based optimization used in most prior works.
To train our unified novel-view video generation model, we curated a dynamic 3D object dataset 
from the existing Objaverse dataset.
Extensive experimental results on multiple datasets and user studies demonstrate SV4D's state-of-the-art performance on novel-view video synthesis as well as 4D generation compared to prior works.
Project page: \urlNewWindow{https://sv4d.io}.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
Stable Video 4D (SV4D) introduces a unified latent video diffusion model for generating multi-frame and multi-view consistent 4D content. Unlike previous methods that use separate models for video generation and novel view synthesis, SV4D simultaneously generates novel view videos from a monocular reference video to ensure temporal consistency. These generated videos are then used to optimize a dynamic NeRF without SDS-based optimization. Trained on a curated dynamic 3D object dataset from Objaverse, SV4D demonstrates sota performance in novel-view video synthesis and 4D generation.

### Strengths
1. Performance: The proposed method SV4D achieves state-of-the-art results. The experiments well validate the effectiveness of the proposed methods.

2. Clarity: The paper is well-written and clearly structured, making the methodology and results easy to understand and follow.

3. Technical Novelty: This paper presents Stable Video 4D (SV4D), a latent video diffusion model that simultaneously handles multi-frame video generation and multi-view synthesis for dynamic 3D objects. Unlike previous approaches that utilize separate generative models for each task, SV4D ensures temporal and spatial consistency by generating novel view videos directly from a monocular reference video.

### Weaknesses
1. For the claim in Section 3.2, line300, "we observe that this dynamic NeRF representation produces better 4D results compared to other representations such as 4D Gaussian Splatting (Wu et al., 2024), which suffers from flickering artifacts and does not interpolate well across time or views.", do you have any experimental results to support this? The comparison lacks specific metrics or visual examples directly contrasting dynamic NeRF with 4D Gaussian Splatting within the same experimental setup. The claim is not sufficiently substantiated, making it difficult to assess the true advantage of the chosen representation.

2. The design of SV4D is closely aligned with that of EG4D, as both utilize SVD and SV3D priors. SV4D uses dynamic NeRF and EG4D uses dynamic GS. This significant overlap raises concerns regarding the distinctiveness and novelty of SV4D. The paper needs to more clearly articulate the unique contributions of SV4D beyond simply combining existing components. The use of dynamic NeRF instead of dynamic GS, while a difference, does not inherently establish significant novelty without further justification and analysis of the impact of this choice.

### Questions
Please refer to weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This work makes attempts to build a multi-view video diffusion model conditioned on reference single-view video and reference multi-view images.  To inherit knowledge learned by previous 3D diffusion models and video diffusion models, the authors carefully design the multi-view video generation network to combine both of them. Specifically, they insert the frame-attention module of the video generation model to 3D generation model to achieve spatial and temporal consistency. To handle GPU memory problem when inferring long-videos, they propose a mixed-sampling scheme. Extensive experiments with regard to novel view video synthesis and 4D generation demonstrate the advantages of the proposed method.

### Strengths
1) The work makes attempts to train a mult-view video diffusion model for 4D generation, which is encouraging and could benifit the community.
 2) The authors test their model on both real-world and synthetic objects to prove the generalization ability of their model.
 3) The authors conduct extensive compairsons with previous mehtods.

### Weaknesses
1) network design: According to Figure 2, frame-attention is inserted after view-attention, and the output of frame-attention directly serves as the final result. However, since frame-attention only operates on the time axis and is not aware of multi-view information, latents processed by it might suffer from multi-view inconsistency, and cannot directly serve as the final result. It is observed that the 4D reconstruction results suffer from a blurry effect, and I suspect it is due to multi-view inconsistency of the generated videos. The blending of spatial and temporal attention outputs is not clearly illustrated in the pipeline figure, making it difficult to understand how multi-view consistency is maintained after the frame attention module.

2) problem setting: The proposed model takes a generated reference video and generated multi-view images of the first frame as input. However, it is possible that the two inputs have conflicts since they are generated independently. For example, if the video depicts an object turning around, it may not be consistent with the generated multi-view images, especially in side and back views. I don't see the authors show objects with such movements in the experiments. The reliance on independently generated reference video and multi-view images introduces a potential source of error and limits the robustness of the approach, especially when dealing with complex object motions and occlusions in the first frame.

3) experiments: I'm curious about the real-world video experiments. The authors only train their model on synthetic data, so the generalization to real-world cases might be difficult. I don't find many visualizations of real-world generated objects. Could the authors point out where the visualizations are? The quality of real-world video generation is a concern, as the model is trained on synthetic data and may not generalize well to the complexities of real-world scenes. The lack of clear visualizations makes it difficult to assess the model's performance on real-world data.

4) Some citations regarding to concurrent works are not accurate, for example (Line245 Wang et al, 2024a) and (Line 149 4Diffusion Yang et al, 2024). The authors are suggested to further check them.

5) The authors claim they can handle arbitrary length videos; however, when the input video is very long, the anchor frames will have little temporal coherence and be out-of-distribution for the proposed model. The proposed sampling strategy may not be sufficient to preserve the appearance of the object in very long videos, as the temporal coherence between sparse anchor frames may degrade significantly.

### Questions
1) training dataset: I can't find the size of the training dataset in the paper. (Maybe I miss it?) However, as far as I know, many animated objects in objaverse datasets are of low-quality, so I'm curious how many models is used in this work after data filtering. 
2) I'm curious why the authors choose dynamic nerf as the 4D representations instead of dynamic gaussians.

### Soundness
3

### Presentation
2

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
This manuscript presents SV4D, a framework tailored for the generation of dynamic 3D content. The key contribution of this framework is a diffusion model characterized by a dual-attention design, capable of simultaneously sampling 5 frames $\times$ 8 views with satisfactory consistency in both dimensions. To generate videos of meaningful length within a reasonable memory budget, this work also proposes a mixed-sampling strategy, which includes interleaved sampling of anchor frames and dense sampling of middle frames conditioned on reference at both sides. For the training of this model, the authors meticulously curated a subset of Objaverse comprising high-quality animated 3D objects.

### Strengths
1.	The paper is overall well-organized and easy to follow.

2.	Their efforts and experience in data curation and training of the 4D generative model have sufficient value to the community, and it can be more valuable with more substantive ablation studies to validate the final design choices.

3.	The proposed mix-sampling strategy is interesting; it effectively extends the local spatial-temporal consistency to a broader scale while avoiding memory constraint.

### Weaknesses
1.	The main contribution of this work lies in the 4D diffusion model; however, there is no ablation on its design and training. It is important to demonstrate to which extent the results are non-trivial and could provide inspiration for subsequent research. Specifically, the lack of ablation on the dual-attention mechanism is a significant oversight. It is unclear how much each attention component contributes to the final performance and whether a simpler design could achieve comparable results. For instance, ablating the frame attention and multi-view conditioning separately would reveal their individual importance. Furthermore, the training process lacks details, such as the effect of different loss functions or optimization strategies on the model's convergence and generalization. In contrast, the ablation provided in this manuscript primarily focuses on the mixed-sampling strategy, which is , while necessary, more like a stopgap solutions to mitigate the memory limitation in this framework.

2.	It is encouraged to provide more generated 4D assets in supplementary videos. 
Now the supplementary video is more like a introduction to the motivation and methodology of this work, which is slightly repetitive with the role of the main paper. The reviewer notices that there are only 12 generated dynamic objects shown in the video, each of them rendered in single fixed-view, which is insufficient to demonstrate multi-view consistency of generated assets. The video should showcase the model's ability to generate diverse and high-quality 4D content, including various object types and complex motions, rendered from multiple viewpoints to properly demonstrate the spatial-temporal consistency.

### Questions
1.	The manuscript has not introduced the scale of ObjaverseDy. Does the author think that the scale of data is sufficient for training a diffusion model for object-centric 4D generation? Is there possibility or necessity for further scaling the data?

2.	L104 claims the capability to handle arbitrarily long input videos. Have the authors tested on substantively longer videos, or is this capability just theoretical?

3.	L264 says that "we only show motion frame extensions here for illustrative purposes." Does this imply that similar extensions could be applied to views?

### Soundness
3

### Presentation
3

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
This paper introduces Stable Video 4D (SV4D), a novel latent video diffusion model designed to generate dynamic, multi-view consistent 3D videos from a single input video. Unlike previous models that separately handled video generation and novel view synthesis, SV4D uses a unified approach to generate multi-frame, multi-view videos that retain both temporal and spatial consistency.  Extensive evaluations on synthetic and real-world datasets show SV4D’s superior performance in novel-view video synthesis and 4D generation.

### Strengths
1. SV4D combines video generation and novel view synthesis within a single framework, overcoming the limitations of separate models and ensuring multi-frame and multi-view consistency.
2. The use of view attention and frame attention blocks ensures alignment across different frames and viewpoints, enhancing dynamic consistency.

### Weaknesses
Although SV4D demonstrates promising results on selected datasets, its performance on a broader range of objects, particularly those with complex or intricate details, is not thoroughly evaluated. The paper lacks a rigorous analysis of how the model handles objects with fine-grained structures, such as detailed textures, thin structures, or highly irregular shapes. The current evaluation primarily focuses on relatively simple objects and scenes, which may not fully represent the challenges of real-world 4D generation tasks. Furthermore, the paper does not provide a clear understanding of the limitations of the view and frame attention mechanisms when dealing with significant occlusions or rapid changes in viewpoint.

### Questions
How does SV4D perform on complex, out of distribution high-detail objects or scenes with intricate textures For example, some of the scenes shown in L4GM website https://research.nvidia.com/labs/toronto-ai/l4gm/.

### Soundness
3

### Presentation
3

### Contribution
3
