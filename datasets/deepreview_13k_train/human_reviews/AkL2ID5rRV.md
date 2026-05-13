# PRM:  Photometric Stereo based Large Reconstruction Model

- Decision: Reject
- Scores: 6, 8, 6, 5

## Abstract
We propose PRM, a novel photometric stereo based large reconstruction model to reconstruct high-quality meshes with fine-grained local details.
Unlike previous large reconstruction models that prepare images under fixed and simple lighting as both input and supervision, PRM renders photometric stereo images by varying materials and lighting for the purposes, which not only improves the precise local details by providing rich photometric cues but also increases the model’s robustness to variations in the appearance of input images. 
To offer enhanced flexibility of images rendering, we incorporate a real-time physically-based rendering (PBR) method and mesh rasterization for online images rendering.
Moreover, in employing an explicit mesh as our 3D representation, PRM ensures the application of differentiable PBR, which supports the utilization of multiple photometric supervisions and better models the specular color for high-quality geometry optimization.
Our PRM leverages  photometric stereo images to achieve high-quality reconstructions with fine-grained local details, even amidst sophisticated image appearances. Extensive experiments demonstrate that PRM significantly outperforms other models. Project page: \href{https://wenhangge.io/PRM/}{https://wenhangge.io/PRM/}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes a variation of the large reconstruction models for reconstructing objects (geometry and albedo) from single or multi-view input images. By incorporating physically based rendering pipeline for image synthesis in training, as well as ground truth images rendered under sampled BRDF and lighting conditions, the model is able to utilize additional supervision based on diffuse and specular color maps, in an attempt to improve the generalization ability of the model to images of diverse and complex materials and lighting combinations. The model is evaluated against baselines include InstantMesh, and additional ablation is provided on losses related to PBR, as well as robustness to materials, number of views and field of view.

### Strengths
[1] The paper is able to improve on a line of work around LRMs, by incorporating PBR related insights into training, and showcases by incorporating ground truth and supervision from sampled complex materials and lighting conditions, the model better handles images of those conditions, and additionally gains improvement on geometry estimation due to the improved modeling of physics.

[2] The speed up of PBR rendering with split sum approximation enables efficient on-the-fly view synthesis and ground truth generation in a large parameter space of materials and lighting. Mostly as a technical contribution, but it will enable efficient data generation and augmentation on-the-fly when modeling complex parameter space of PBR.

[3] Extensive evaluation. The model is able to compare on standard benchmarks against baseline models in this task, but additionally provides extensive ablation study to justify the design choices by ablating the PBR-related losses, as well as robustness to number of input views and FOVs.

### Weaknesses
[1] Clarification. Several details need to be clarified to better understand the model and the training strategy.

(a) What does the model estimate w.r.t. the PBR parameters? Does it only estimate albedo? It is unclear if the model also estimates roughness and metallic maps, or if these are fixed during training and inference. The implications of only estimating albedo are significant, particularly for downstream applications that rely on accurate material properties.

(b) With sampled metallic, roughness and lighting envmaps, do we apply the metallic and roughness globally? If yes: 1)what happens if the original CAD model is already associated with spatially-varying (SV) BRDF maps? 2) And if applied globally, does this strategy diminish the model's generation ability towards real images with complex SV materials? 3) Given a good portion of Objaverse models are assigned with PBR materials, does it benefit the training to also predict ground truth BRDF (roughness, metallic) without manually sampling and enforcing global roughness and metallic? The paper needs to clarify how it handles existing material maps and justify the choice of global material properties.

(c) Is the split-sum approximation only applied to synthesizing estimated image from estimated representations, or it is also used to render ground truth images? Are ground truth images rendered on-the-fly for each batch in training? The computational implications of rendering ground truth images, especially with complex lighting and material variations, need to be clarified.

[2] Writing. Language issues are abundant and need to be fixed for a polished version. Examples:

(a)  L015: for what purposes?

(b) L020: Need to introduce the full name of PBR before first use of the abbreviation.

(c) L050, L235: Need to clarify 'dependence on images rendered under fixed and simple lighting conditions' of previous methods. Mostly previous methods use PBR materials and envmap base lighting similar to this paper, so it would be important to clarify this assertion.

(d) L186: functionalities -> downstream applications of ...

(e) L283: what is 'a richer set of equations'?

[3] Additional evaluation results on images of complex lighting and materials. The paper is able to showcase the robustness towards complex lighting and materials in Fig. 9, however one scene is too few, and comparison with baselines on this setting is necessary to further justify the claim. It is important to show quantitative results on complex lighting and material conditions, not just qualitative examples.

### Questions
Please see Weakness section for comments and questions.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This submission addresses the multi-view photometric stereo task and proposes a large reconstruction model (LRM) specifically leveraging photometric stereo. Unlike previous LRM models, in this work the authors train the model on data with varying illumination, material, etc. and instead of the usual triplane representation, they leverage a traditional mesh as the output 3D representation. This allows them to incorporate physically based rendering priors into the training objective. The idea of split-sum approximation from the physically based rendering community is leveraged to speedup the training data setup.

The approach is able to generate 3D models with fine geometric detail, handle a very wide variety of shapes, materials, lighting. Both qualitative and quantitative results are very convincing. However this is large transformer based architecture and training costs are prohibitively high.

### Strengths
The experimental results reported in the paper are very convincing. The performance of the model is quite impressive both from the point of view of the reconstructed 3D geometry, the large range of objects, materials that can be handled as well as the ability to handle a fairly small number of multi-view images.

The quantitative results reported in Tables 1 and 2 on the GSO and Omni3D datasets are quite convincing. A large improvement can be seen compared to prior LRM based baselines.

The method builds on top of the InstantMesh (Xu et al. 2024) model in terms of architecture and the training procedure. However, the model is extended to solve the photometric stereo problem. Leveraging mesh representations for geometry allows additional priors to be incorporated such as depth maps and normal maps (which are available for meshes).

### Weaknesses
This is a well written paper but the technical details were difficult to follow in certain sections. The section describing the use of the split-sum approximation was difficult to understand because it was quite brief. I was also unable to appreciate to what extent this approximation is needed. Is this a standard solution that is used in real-time rendering nowadays and what assumptions or requirements does this method have, which could potential make it inapplicable.



### Questions
How were the hyperparameters tuned and to what extent do the authors think that they matter, or specifically which ones matter more than the others? Given the high training cost, it is infeasible to carefully tune so many hyperparameters. 

I am curious to know what happens on scenes with real, non-trivial backgrounds? Can the proposed model be run on multi-view images of non segmented real objects with natural backgrounds? Will the model reconstruct the object as well as the background? or would it be expected to automatically ignore the backgrounds because of how it was trained.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduced a new LRM method that improves the output quality. The method addressed the limitation of LRMs that they rely on simple lighting and material assumptions as input. The paper integrates photometric stereo principles into large reconstruction models. The key innovations are: (1) using varied materials and lighting conditions during training to improve detail reconstruction and robustness, (2) incorporating real-time rendering with split-sum approximation for flexible online image generation, and (3) utilizing explicit mesh representation with differentiable physically-based rendering (PBR) for better geometry optimization.

### Strengths
- Novel integration of photometric stereo principles into large reconstruction models
- Comprehensive ablation studies that validate each component's contribution
- Practical applications demonstrated through relighting and material editing capabilities
- Impressive handling of specular surfaces, which are traditionally challenging

### Weaknesses
 - Limited discussion of computational overhead compared to simpler approaches
- The 50% probability threshold for material/lighting consistency seems arbitrary
- Results appear sensitive to multi-view diffusion model quality
- Some failure cases (e.g., with lacking depth information) could be analyzed more thoroughly

### Questions
- How does the computational cost of online rendering compare to traditional offline approaches?
- What is the rationale behind the 50% probability threshold for material/lighting consistency?
- Have you considered incorporating depth estimation to improve reconstruction quality for challenging cases?
- How does the method perform on real-world images with unknown lighting conditions?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper "PRM" presents a high-quality 3D mesh reconstruction model with fine-grained local details from sparse image input. Unlike previous large reconstruction models (LRMs) that were trained using data rendered with fixed lighting and without material changes, PRM utilizes photometric stereo images with varied materials and lighting during training, enhancing detail accuracy and robustness. By incorporating split-sum approximation and mesh rasterization for online rendering, PRM effectively captures multiple photometric cues—such as diffuse and specular lighting—making it resilient to complex image appearances. Experiments demonstrate that PRM  outperforms existing models in both 3D geometry accuracy and 2D visual fidelity across public datasets like GSO and Omni3D.

### Strengths
1. This paper focuses on an often overlooked yet crucial factor affecting the performance of prior work --- training data. Unlike prior approaches that relied on data rendered with fixed lighting and without material variations, this method leverages data rendered under varied materials and lighting conditions to enhance both 3D geometry accuracy and 2D visual fidelity.

2. The paper shows better performance than the selective baselines.

### Weaknesses
1. One key motivation of this paper is unconvincing --- why would the online rendering of training data be necessary? The authors argue that offline preparation of training data is challenging due to the "infinite number of potential combinations of materials and lighting" and the high sample counts required for rendering high-quality images. However, for the first reason, one could randomly sample finite combinations of materials and lighting offline, as the model will only be trained on a finite set of combinations given the limited training iterations. For the second reason, if online rendering is not strictly necessary, as suggested, the offline rendering costs without using split-sum approximation would be acceptable, and using default rendering engines would yield better image quality than the split-sum approximation used in this paper.

2. The paper does not compare with some stronger baselines, such as Mesh-LRM, which has released an online demo from its first author before the ICLR submission deadline.

3. The ablation studies are incomplete. The authors provide only qualitative comparisons on 1-2 selected objects, which is quite limited. And the quantitative tables are missing

### Questions
See my weaknesses section

### Soundness
2

### Presentation
2

### Contribution
2
