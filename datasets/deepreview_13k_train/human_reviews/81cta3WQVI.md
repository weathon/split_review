# EdgeRunner: Auto-regressive Auto-encoder for Artistic Mesh Generation

- Decision: Accept
- Scores: 3, 6, 6, 8, 8, 8

## Abstract
Current auto-regressive mesh generation methods suffer from issues such as incompleteness, insufficient detail, and poor generalization. 
In this paper, we propose an Auto-regressive Auto-encoder (ArAE) model capable of generating high-quality 3D meshes with up to 4,000 faces at a spatial resolution of $512^3$.
We introduce a novel mesh tokenization algorithm that efficiently compresses triangular meshes into 1D token sequences, significantly enhancing training efficiency. 
Furthermore, our model compresses variable-length triangular meshes into a fixed-length latent space, enabling training latent diffusion models for better generalization. 
Extensive experiments demonstrate the superior quality, diversity, and generalization capabilities of our model in both point cloud and image-conditioned mesh generation tasks.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces EdgeRunner, an Auto-regressive Auto-encoder (ArAE) model for artistic mesh generation. It proposes a mesh tokenization algorithm to address incompleteness and poor generalization. 

The model can generate 3D meshes with up to 4,000 faces at a spatial resolution 512^3. It also compresses variable-length meshes into a fixed-length latent space, enabling the training of latent diffusion models for better generalization. 

The main contributions include a mesh tokenization algorithm for lossless face compression, an ArAE model for fixed-length latent code generation, the use of this latent space for training latent diffusion models with better generalization.

### Strengths
EdgeRunner demonstrates strengths in the mesh tokenization algorithm and the Auto-regressive Auto-encoder framework, which address previous challenges in mesh generation.

It offers a mesh tokenization algorithm for efficient compression into 1D token sequences, enabling mesh generation with up to 4,000 faces at a 512^3 resolution. The model's ability to compress variable-length meshes into a fixed-length latent space facilitates the training of latent diffusion models for enhanced generalization.

### Weaknesses
A. While the paper presents a compelling case for EdgeRunner's capabilities, a notable weakness is that it does not fundamentally differentiate itself from existing works like MeshGPT and the MeshAnything series in terms of the core generative approach. The reliance on an auto-regressive transformer architecture for mesh generation, while effective, is not a novel contribution in itself. The paper's claim of novelty rests primarily on the mesh tokenization algorithm, but the core generative mechanism remains largely consistent with prior work.

B. Despite the improvements in tokenization and the auto-regressive framework, the generated 3D geometries may not adhere to the modeling and wiring conventions that human artists typically follow. This is a critical limitation because the generated meshes may lack the clean edge loops, consistent face orientations, and logical topology that are essential for further editing and manipulation in standard 3D software. The absence of these conventions can hinder the practical application of the generated meshes within professional 3D content creation pipelines, where adherence to standard modeling practices is often a requirement.

C. The paper also has a limitation in terms of polycount, as the capability of generating meshes with up to 4,000 faces, while an improvement over previous methods, still falls short for many real-world scenarios. The constraint on the number of faces limits the model's ability to capture the complexity and detail required for high-fidelity 3D representations, which further limits the application. For example, generating detailed character models or intricate architectural elements would be infeasible with such a low face count. The paper does not adequately address how the model might be extended to handle higher polygon counts without a significant increase in computational cost or a degradation in mesh quality.

D. Another limitation of the paper is the potentially unfair comparison made with Unique3D, as the latter employs a multi-view approach to 3D generation. Unique3D's methodology is inherently challenged by inconsistencies or deformities that can arise from generating a 3D model from multiview images, which is a different set of problems compared to EdgeRunner. This discrepancy means that the comparison may not accurately reflect the strengths and weaknesses of each method, as they are optimized for different conditions and face distinct sets of challenges. Consequently, the paper's claims about EdgeRunner's superiority might not be fully substantiated. The comparison lacks a controlled setting that isolates the specific contributions of EdgeRunner, making it difficult to assess its true performance relative to other methods.

### Questions
I have a few questions for the authors to consider:

The paper presents an improvement in the number of faces that can be generated compared to previous methods, reaching up to 4,000 faces. However, for many practical applications in industries such as gaming, film, etc, this number is still limited. How to increase the face count further? Are there any technical barriers within the current model that restrict the generation of meshes with even more faces?

Comparison with Unique3D is not fair. How does the method perform when compared with CLAY? How does EdgeRunner compare in terms of quality and diversity of generated meshes? While the code CLAY is not publicly available, its geometric rendering effects can be observed on Hugging Face and its corresponding products are available for comparison.

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
4

### Summary
This paper focuses on generating artistic meshes with up to 4000 faces and a resolution of 512³. It introduces a novel mesh tokenization algorithm based on EdgeBreaker to facilitate lossless face compression. To produce fixed-length latent codes for arbitrary mesh sequences, the authors propose an encoder alongside an auto-regressive decoder. Additionally, they investigate the incorporation of image conditions to guide the generation of the meshes.

### Strengths
1. The proposed method can generate meshes with up to 4000 faces, surpassing the capabilities of previous baselines. 
2. The trained model shows strong generalization on novel inputs.
3. Extensive experiments highlight the advantages of the proposed method in achieving high-quality mesh generation.

### Weaknesses
1. The proposed method and the baselines are trained on different datasets (for example, MeshAnything does not have access to Objaverse-XL and reserves 10% of Objaverse for evaluation). As a result, the comparisons can be unfair.
2. Is the training sequence unique for each mesh? How did you define the start of the sequence?
3. Although the authors report the inference speed, there is no comparison of the inference speed against other methods when generating similar number of faces.
4. The details of user study are missing. How many users are there in the test? What is the details of the task or questions that volunteers are asked to do or answer? Are 8 test cases randomly selected? It is better to have more test cases rather than only 8 ones.
5. To demonstrate the robustness across all test cases, it is better to involve quantitative evaluations like those in *MeshAnything*, where the authors sample points from both the generated mesh and the ground-truth mesh, calculating the CD or ECD.


### Questions
1. What does the dashed line mean in Figure 2?
2. Does the output number of faces strictly adhere to the face count control? For instance, when using a control token of 1000 to 2000, will the model generate only mesh sequences within that range?

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
4

### Summary
This paper introduces EdgeRunner, an auto-regressive mesh generative model that presents a novel and efficient mesh tokenization algorithm capable of handling a higher number of mesh faces and higher resolutions. By encoding variable-length meshes into a unified latent space, the proposed method can generate meshes from point clouds or single-view images. The paper demonstrates a well-motivated and effective approach, creating a cohesive narrative.

However, key information, such as training data and experimental settings, is missing from the main text, which limits readability. Given the novelty and effectiveness of the method, I suggest accepting the paper, but I strongly recommend that the authors restructure the content to improve readability and accessibility.

### Strengths
The paper proposes a novel method for mesh tokenization which allows to handle mesh with more faces and in higher resolution.  It also introduces a latent space with a unified token length, enhancing the model's generalization ability. These two contributions represent the technical novelties of the paper. 

The paper includes a comprehensive comparison with several state-of-the-art mesh generative models, such as MeshAnything, MeshAnythingV2, and Unique3D. This thorough evaluation makes the study well-rounded and complete.

The method is clearly described and easy to follow. The figures and renderings are thoughtfully designed, giving the paper a polished visual appeal. Additionally, the accompanying website provides extensive results, further illustrating the method's effectiveness and aiding in comprehension of its impact.

### Weaknesses
While I find no weaknesses in the method itself, I believe the presentation of the paper needs restructured. Important information, such as experimental settings and training datasets, currently appears only in the supplementary materials, which makes the paper difficult to follow.

Presentation:
- Line 102: The term "EdgeBreaker" appears for the first time without a reference, making this part challenging to understand.
- Line 200: It seems that the mesh tokenization approach is heavily inspired by EdgeBreaker, proposed by Rossignac in 1999. However, there is no mention or citation of this foundational paper. Although the authors provide a comparison in the supplementary material on Line 920, omitting a discussion of this algorithm in the main methods section does not adequately acknowledge its influence.
- Line 358: The experiments section begins directly with results, without any mention of training data, settings, or other critical experimental details. These details appear only in the supplementary material, which is insufficient, as they are essential for understanding the experiments.

### Questions
I have some questions primarily about the implementation and public availability of this work:

- Would it be possible to share the mesh tokenization script on an anonymous GitHub? This would help in understanding how the "traversal" process works and can be implemented.
- I didn’t find any mention in the paper regarding the public availability of the code and pre-trained model. Will these resources be released?

### Soundness
4

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
4

### Summary
The paper proposes a method for 3d mesh generation. They propose a mesh serialization copression algorithm to tokenize 3d meshes. An encoder-auto regressive decoder network operating in this representation is trained to compress this representation into a fixed length latent space. Additionally the authors propose a latent diffusion approach for generating 3d mesh representations in this latent space conditioned on images and 3d point clouds.

### Strengths
The proposed mesh tokenization based on maximizing edge sharing between adjacent triangles is sensible, well referenced and very useful in practice.  It supports lossless compression at 50% rate designed to reduce long range dependencies between tokens which is beneficial for learning.  

The proposed pipeline solves several issues of 3d mesh generation such as the ability to generate variable length outputs through the AR decoder combined with a fixed length latent code which enables the use of diffusion models for conditional generation

Generated examples are shown to be of great quality.

Literature review is comprehensive.

### Weaknesses
There is no discussion about pretraining the model, loss curves showing training progression, or explaining how unconditional generation works compared to the conditional method.

### Questions
Is it possible to generate unconditional samples using your approach?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces a novel mesh tokenization algorithm The tokenization supports lossless face compression and reduces long-range dependencies. This helps in smooth and efficient training of an auto regressive encoder termed as (ArAE). This encoder is capable of compressing point clouds to into fixed-length latent codes representing meshes. ArAE's latent space can be leveraged to train latent diffusion models for better generalization, enabling conditioning of different input modalities such as single-view images. Hence, the method can generate meshes from point clouds or single-view images, showing generalization and multimodal capabilities .

### Strengths
1) The method of tokenization is based on the half edge data structure and is able to achieve 50% more compression than the existing method. This allows for smoother training and avoiding long range dependencies.

2) The paper shows generalization using single-image to mesh examples. The examples shown in the paper are of high quality.

3) The paper shows that the fixed latent space learned by the autoregressive model can be used by the diffusion training to learn many modalities including single-image to mesh capabilities.

### Weaknesses
1) The paper talks about the point cloud sampler but not enough information is provided on it. How is the current method sensitive to the number of points , regions of missing points, and irregularities in the point cloud positions?

2) How is the Siddique et.al's method compared with the output quality? The paper mentions the method in context of the tokenization is lossy reconstruction but does not provide the evidence of the final output quality.

3) The quality of the single-image to meshes would be more exciting to see if the poses of the input images are varied. For example, dog and frog examples in Figure 6, and compared with the comparing method.

### Questions
Please refer to the questions in weakness section.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 6

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper proposes an Auto-regressive Auto-Encoder (ArAE) model for multi-modality mesh generation supporting point clouds and single-view image inputs. Besides, an efficient mesh tokenization inspired by the EdgeBreaker algorithm is designed for more edge sharing during compression.

### Strengths
(i) The idea is very novel. Adapting the EdgeBreaker algorithm for mesh token compression is super interesting with the key insight "maximize edge sharing between adjacent triangles". It is a kind of Renaissance. I really like this style. This solution avoids the use of some lossy VQ-VAE models and preserves the geometry information during tokenization. Meanwhile, the customized traversal can also avoid the computation of long-range dependencies and ensure the face's orientation consistency in each sub-mesh. In addition, the core idea of using ArAE to handle variable-length mesh into fixed-length latent tokens is awesome. This can support the multi-modality inputs and address the variable-length issue in mesh generation.

(ii) The presentation is well-dressed. The writing is clear and easy to follow. The pipeline in Figure 2 is simple and clear to show the workflow of the proposed method. The visual comparison of point cloud conditioned mesh generation in Figure 5 and image conditioned mesh generation in Figure 6 are very clear to demonstrate the advantages of the proposed method over state-of-the-art algorithms.

(iii) The performance is very solid. The proposed method not only achieves more visually pleasant generation results with the highest user study score but also yields a much higher compression ratio to boost the model's efficiency. The experiments are sufficient. Especially the user study in Figures 7 and 8. It seems like more faces lead to finer-grained generated meshes. I also like the style of the visual ablation in Figure 8, studying the effect of resolution and image conditioning strategies.

(iv) The implementation details are all provided in the appendix. I believe other researchers can easily reproduce the results. I trust the authors for the reproducibility.

### Weaknesses
(i) It would be better to remove the ablation study table from the supplementary to the main table as there are no other quantitative evaluation results. Although the visual comparison is good, I think the main paper should have some numerical comparison. It's crucial to have a quantitative measure of performance, such as the Chamfer distance or F-score, to validate the visual results. Without these metrics, it's hard to objectively assess the improvement over existing methods. The ablation study, while visually informative, lacks the necessary numerical support to draw strong conclusions about the contribution of different components.

(ii) Maybe Figure 4 and the left part of Figure 3 should be in the same figure according to the description in Section 3.1. I think Figure 4 , instead of the right part of Figure 3, is more related to the left part of Figure 3. The current separation makes it harder to follow the mesh tokenization process. Combining them would provide a clearer, more cohesive view of the tokenization steps, especially given the close relationship between the EdgeBreaker traversal and the resulting tokens.

(iii) For better understanding, in Line 320, the authors should add some description where to introduce the image condition input since in Line 298 - 302, the ArAE is introduced as a point clouds conditioned mesh generator. The transition from point cloud conditioning to image conditioning is not clearly explained. It would be beneficial to explicitly state how the image features are incorporated into the ArAE architecture, especially given that the initial description focuses solely on point cloud inputs. This lack of clarity makes it difficult to understand how the multi-modality aspect is achieved.

(iv) A small typo: (low-poly *v.s.* high-poly) $\rightarrow$ (low-poly *vs.* high-poly)

### Questions
I am curious about the engineering tricks the authors used to save GPU memory and scale up the training datasets.

### Soundness
4

### Presentation
3

### Contribution
4
