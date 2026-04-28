# MeshAnything: Artist-Created Mesh Generation with Autoregressive Transformers

- Decision: Accept
- Avg Score: 6.00
- Scores: 5, 5, 6, 8

## Abstract
Recently, 3D assets created via reconstruction and generation have matched the quality of manually crafted assets, highlighting their potential for replacement.
However, this potential is largely unrealized because these assets always need to be converted to meshes for 3D industry applications, and the meshes produced by current mesh extraction methods are significantly inferior to Artist-Created Meshes (AMs), i.e., meshes created by human artists. 
Specifically, current mesh extraction methods rely on dense faces and ignore geometric features, leading to inefficiencies, complicated post-processing, and lower representation quality.
To address these issues, we introduce \name, a model that treats mesh extraction as a generation problem, producing AMs aligned with specified shapes.
By converting 3D assets in any 3D representation into AMs, \name~can be integrated with various 3D asset production methods, thereby enhancing their application across the 3D industry.
The architecture of \name~comprises a VQ-VAE and a shape-conditioned decoder-only transformer. We first learn a mesh vocabulary using the VQ-VAE, then train the shape-conditioned decoder-only transformer on this vocabulary for shape-conditioned autoregressive mesh generation. Our extensive experiments show that our method generates AMs with hundreds of times fewer faces, significantly improving storage, rendering, and simulation efficiencies, while achieving precision comparable to previous methods.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work introduces a method for conditional "artist-created" mesh generation. 
The key idea is employing auto-regressive transformer on top of a VQ-VAE pre-trained latent space, with additional conditioning for VQ-VAE and noise tricks to improve generalization. Quantitative results on toy datasets suggest that the method outperforming recent baselines.

### Strengths
+ The paper is well-written and is easy to follow. 
+ The overall architecture of the method makes sense, and the problem of conditional mesh generation is important. 
+ There are several interesting techniques that could be useful for practitioners: e.g. conditioning VQ-VAE on the shape to improve reconstruction, and the gumbel noise trick to improve VQ-VAE's decoder robustness.
+ Quantitative results (Table 2) suggest that the method outperforms competitors.

### Weaknesses
- The motivation for focus on artist-generated meshes is not very clear - would exactly the same method not work on a collection of reconstruction-based meshes? My assumption would be that the reason is that the method cannot scale to any realistic number of vertices.
- The method is a combination of existing architectures (VQ-VAE based on BERT + OPT transformers), whereas the encoding scheme is the same as in polygen / meshgpt.
- The scalability of the method is very questionable: both in terms of training and inference. If my undertstanding is correct, memory scales quadratically with the number of mesh faces, and authors explicitly mention that they filter out meshes with less than 800 faces. There is discussion of this in the appendix, but it is worth providing more information (memory and/or runtime numbers) which would be critical to get a complete impression of how usable the method actually is.
- Comparison to diffusion-based methods (e.g. point-e) would be interesting (converting point clouds to meshes should be supported by publicly available code).

### Questions
- Can you provide details on the scalability of the method - i.e. what is the max number of faces/vertices the model can handle?
- Is there anything specific about architecture why artist-generatedness of the meshes is critical?
- How does this method stack against diffusion-based methods for mesh/point-cloud based generation (e.g. point-e)?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper introduces Meshanything for shape-conditioned AM generation. Meshanything first trains a VQ-VAE to obtain a set of mesh tokens and employs a noise-resistant decoder to enhance mesh generation quality. Subsequently, a shape-conditioned autoregressive transformer is trained to generate artist-created meshes. Experiments show that Methanything outperforms previous mesh generation methods with fewer faces.

### Strengths
- Mesh generation toward artist creation has been seldom explored in previous research. This work could serve as an improved remeshing tool, facilitating a more rational topology for the generated 3D assets.

- The visualization is good. The final mesh reconstructions are nice looking, and the method outperforms previous methods in the experiments.

- This work constructs coarse meshes for sampling point clouds as inputs, thereby narrowing the gap between training and inference. This approach is reasonable.

### Weaknesses
 - This paper mainly focuses on the task of point cloud -> mesh, which is usually referred to as mesh reconstruction, rather than mesh generation. Though a transformer-based autoregressive architecture is applied, I still don't think it is appropriate to name the paper a mesh generation paper. 

- It is unfair to use meshes generated by Rodin as the shape conditioning for comparison with MeshGPT. From my understanding, the Rodin engine largely (or purely) provides the generation ability while MeshAnything only acts as a remesher component.

- Another concern is that the number of AM mesh faces generated by MeshAnything is limited to a maximum of 800. Using such a limited number of faces makes it insufficient for representing meshes with more complex structures.

- This work appears to have stringent data requirements, as the authors were only able to filter 56k high-quality artist-created meshes from the Objaverse and ShapeNet datasets for training. So it may be challenging to scale this method up to more data and modeling parameters (but it might be sufficient to train a point cloud reconstructor/mesh remesher).

### Questions
My suggestion is to change the description of mesh generation to mesh reconstruction/remeshing. 

I regard the proposed method as a novel learning-based remesher (AR applied), but I don't think the paper could be classified into a generation paper.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper tackles the important question of converting various 3D representations to explicit mesh representations similar to what artists create. For this, the authors adopt the idea of MeshGPT and inject shape-conditioned information to make the model focus on learning topology. To make the model agnostic to specific 3D representations, e.g., NeRF or Gaussian Splats, the authors choose to convert all representations to point clouds and generate the mesh based on the features from the point cloud. Further, the authors develop a fine-tuning strategy for the VQ-VAE's decoder to create a noise-resistant one to reduce the gap between the data in training and real usages. A user study demonstrates the effectiveness of the proposed approach.

### Strengths
- originality-wise: the choice of converting all representations to a point cloud and using the point cloud to generate corresponding mesh is interesting;
- quality-wise: qualitative results are of high quality;
- clarify-wise: the paper is well-written and easy to follow;
- significance: to produce a mesh similar to what artists create is of great importance to bridge the current 3D generation research into real-world usage.

### Weaknesses
## Concerns about the user study

Since the goal of the project is to produce artist-created meshes, it is important to make sure that the model's output is aligned with real artists' preferences. However, there is no information about whether the 41 users who participated in the study (L517) are qualified especially Tab. 1 is the main results reported in the paper. For "qualified" users, I mean people who are artists with enough experience in the field of 3D creation or editing, etc.

Can authors clarify? If the users are not qualified, I would not be convinced by the result.

## Concerns about comparison with mesh generation pipeline

In L508, the authors state:
> MeshAnything is a shape-conditioned mesh generation method, we sampled shapes randomly from the evaluation set of Objaverse as inputs for MeshAnything, while for the baseline methods, we performed random sampling directly.

Further, in L862, the authors state:
> We quantitatively evaluate mesh quality by uniformly sampling 100K points from the faces of both the ground truth meshes and the predicted meshes, and then computing a set of metrics to assess various aspects of the reconstruction.

If I understand correctly:
- the procedure for evaluating MeshAnything is: 1) sample a mesh and then sample points from the evaluation set; 2) run MeshAnything on the sampled point cloud to obtain a predicted mesh; and 3) sample points from the predicted mesh.
- the procedure for the baselines are 1) directly run the generation; and 2) sample points from the generated mesh.

Such a setup is quite unfair in my opinion. Essentially, MeshAnything generates meshes aligned with the evaluation dataset. I think it will surely perform well in terms of those metrics for evaluating generation qualities in Tab. 2. Especially on Objaverse, which has tons of various categorical objects, the unfairness will be amplified.

I also agree that it is not easy to compare with baselines as MeshAnything needs to have a point cloud conditioning. ShapeNet may be more suitable due to the constrained categories.

## Questions about generation procedure

Can the authors clarify how the generation is conducted? As a generative framework, should the model output various plausible meshes based on the input point cloud? However, in the paper, there is always one mesh corresponding to the input. Does this mean that the authors always use **max** logits during the sampling, i.e., greedy search? Can authors provide more generation variants, e.g., with beam search? I would like to know how diverse the mesh generation could be.

Further, a question related to the evaluation on Tab. 2 is whether the authors only use **max** sampling to evaluate.

## Insufficient qualitative results

There are actually no qualitative comparisons to baselines, e.g., MeshGPT and PolyGen in the paper. Please provide.

## Citation format

Please refer to the template instructions and use the correct citation commands. Currently, all citations are with `\citet` instead of `\citep`. They look so weird as those citations appearing without parenthesis break the sentences.

### Questions
See "weakness".

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents MeshAnything, a model framing mesh extraction as a generative task, resulting in artist-crafted meshes that align with specified shapes. The approach first establishes a mesh vocabulary through VQ-VAE, followed by training a shape-conditioned, decoder-only transformer with a noise-resistant decoder design on the learned vocabulary, enabling shape-conditioned autoregressive mesh generation. This paper is well-crafted, and I anticipate that it will positively influence the field of 3D content generation though the pipeline appears somewhat straightforward. The performance of the method seems promising.

### Strengths
This is a well-written paper that clearly conveys the authors' contributions. The topic is highly relevant to the field, as it addresses the gap between generated shapes and practical applications - I expect the authors will consider open-sourcing their code to facilitate further research. The effectiveness of the method is demonstrated in the experimental sections.

### Weaknesses
I recommend that the authors showcase real-world application examples to highlight the significance of their research. For example, the authors could demonstrate how Artist-Created Meshes (AMs) improve shape manipulation for artist-driven shape modifications or offer enhanced rendering performance (e.g., efficiency) compared to conventional dense meshes.

The logic here seems unclear. Generally, mesh topology pertains to the connectivity of vertices, while geometric features relate to vertex positions. Could the authors clarify how "poorer topology quality (relying on dense faces)" affects "geometric characteristics"?

Additionally, recent advancements in 3D reconstruction and generation could be acknowledged, such as:
- Part123: Part-aware 3D Reconstruction from a Single-view Image (SIGGRAPH 2024)
- SyncDreamer: Generating Multiview-consistent Images from a Single-view Image ICLR 2024.
- CLAY: A Controllable Large-scale Generative Model for Creating High-quality 3D Assets (SIGGRAPH 2024)

### Questions
1. Will the data and code be available for reproducibility?
2. Can the limitations and potential future work be expanded in the main paper? Are there any failure cases the method cannot handle? Additionally, what would happen if watertightness is required during generation? Including these discussions could enhance the paper.
3. "Due to its generative nature, our method is not as stable as reconstruction-based mesh extraction methods." Could the authors clarify the meaning of "stable" in this context?
4. How does the method perform on open surfaces?

### Soundness
3

### Presentation
4

### Contribution
4
