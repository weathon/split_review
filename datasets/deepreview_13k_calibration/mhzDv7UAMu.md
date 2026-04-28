# Meshtron: High-Fidelity, Artist-Like 3D Mesh Generation at Scale

- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 5, 3, 5

## Abstract
\vspace{-2mm}
Meshes are fundamental representations of 3D surfaces. However, creating high-quality meshes is a labor-intensive task that requires significant time and expertise in 3D modeling. While a delicate object often requires over $10^4$ faces to be accurately modeled, recent attempts at generating artist-like meshes are limited to $1.6${\sc{k}} faces and heavy discretization of vertex coordinates. Hence, scaling both the maximum face count and vertex coordinate resolution is crucial to producing high-quality meshes of realistic, complex 3D objects. We present {\sc{\ourmethod}}, a novel autoregressive mesh generation model able to generate meshes with up to 64{\sc{k}} faces at 1024-level coordinate resolution --over an order of magnitude higher face count and $8{\times}$ higher coordinate resolution than current state-of-the-art methods. {\sc{\ourmethod}}'s scalability is driven by four key components: 
(\textit{i}) an hourglass neural architecture, 
(\textit{ii}) truncated sequence training, 
(\textit{iii}) sliding window inference, 
and (\textit{iv}) a robust sampling strategy that enforces the order of mesh sequences.
This results in over $50{\%}$ less training memory, $2.5{\times}$ faster throughput, and better consistency than existing works. {\sc{\ourmethod}} generates meshes of detailed, complex 3D objects at unprecedented levels of resolution and fidelity, closely resembling those created by professional artists, and opening the door to more realistic generation of detailed 3D assets for animation, gaming, and virtual environments.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors propose an autoregressive approach for generating high-quality meshes from input point clouds. Compared to existing methods, this approach achieves over an order of magnitude increase in face count. The introduction of the Hourglass Transformer and truncated sequence training effectively reduces training memory requirements and enhances computational efficiency.

### Strengths
The paper addresses the challenge of 3D mesh generation by achieving high-quality outputs with up to 64K faces at 1024-level coordinate resolution, representing a significant advancement over existing methods. The intuition and motivation behind the approach are clearly articulated, supported by a thoughtful discussion of real-world data. The authors further validate their method by conditioning on a variety of mesh types, including artist-created meshes and text-to-3D generated meshes, demonstrating its versatility.

### Weaknesses
First, I find it unclear why the Hourglass Transformer is considered the appropriate solution to address the challenge of generating the latter tokens of a triangle. While the authors explain both the difficulty and the Hourglass Transformer reasonably well, the connection between the two could be more explicitly justified. Specifically, it's not clear how the hierarchical processing of the Hourglass Transformer directly translates to an advantage in predicting the final vertices of a triangle, given that all vertices are interdependent in defining the triangle's geometry. The paper lacks a detailed explanation of how the multi-scale feature representation within the Hourglass architecture specifically aids in capturing these interdependencies compared to other transformer architectures. Second, the model’s reliance on curated, high-quality datasets raises concerns about scalability and applicability to domains with limited or noisy data. In real-world scenarios, point clouds are often noisy, yet the paper does not evaluate the robustness of the proposed approach under such conditions. The absence of a systematic evaluation of the model's performance with varying levels of noise makes it difficult to assess its practical utility. Finally, although the authors claim significant advantages over state-of-the-art methods, they only compare their approach to one such method. Broader validation and comparisons with a wider range of methods are necessary to substantiate their claims. The lack of comparison with other mesh generation techniques, particularly those that also achieve high face counts, limits the ability to fully contextualize the method's performance and advantages.

### Questions
While the 64K-face mesh generation represents a notable improvement over existing methods, I question whether this represents the theoretical limit of the proposed approach. In real-world scenarios involving complex scenes, mesh face counts often exceed several million, raising concerns about the scalability of the method to handle such high levels of complexity.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The author presents a methodology for generating high-quality mesh generation from point clouds. The author proposes an autoregressive model that has been well evaluated and chosen regarding the explicit need for mesh generation. The authors claim well-analysed contributions in the chosen neural architecture and the training methodology and reconstruct the mesh by limiting the scope of possible solutions to enforce mesh sequences during training and inference.

### Strengths
The work is well ablated, and the choice in architectural design taken by the authors is reasonable and easy to understand. Overall, the work is well written and well structured, making it easy to understand why and what was chosen and how it was implemented. The appendix is additionally very useful to reimplement this work. Overall, the work seems to have well-reasoned analysis for training mesh generations from autoregressive models and additionally adds limitations to the mesh generation process that seemingly seem to be very impactful in this process.

### Weaknesses
I am not an expert in this research area, but for me, the main weakness is the claim that previous work "recent attempts at generating artist-like meshes are limited to 1.6K faces and heavy discretization of vertex coordinates". I want to refer the authors to works such as [1, 2] that show mesh reconstruction with more that 1.6K faces.
Both of the mentioned works [1, 2] show high-quality reconstructions and are not compared by the authors. The claim regarding the limitation of previous work seems to be overstated, as methods like [1, 2] achieve higher face counts and should be considered in the comparison. The lack of comparison with these methods makes it difficult to assess the true novelty and advancement of the proposed approach.

Furthermore, while the ablation studies are well-executed, the impact of point cloud density on the final mesh generation is not thoroughly explored. The paper lacks a detailed analysis of how varying point cloud densities affect the quality and detail of the generated meshes. This is a crucial aspect, as real-world point clouds often have varying densities, and the robustness of the method to these variations needs to be established. Additionally, the handling of partial point clouds is not addressed, which is a significant limitation considering the practical scenarios where complete point cloud data is rarely available.

### Questions
- How much does the number of points in the point cloud impact the final mesh generation process
- How does the model handle partial point clouds?  
- Above all, I would like the point regarding the comparision with [1, 2] to be addressed and would change my rating if it was a misunderstanding on my side.


[1] Shen, Tianchang, et al. "Flexible Isosurface Extraction for Gradient-Based Mesh Optimization." ACM Trans. Graph. 42.4 (2023): 37-1.
[2]Shen, Tianchang, et al. "Deep marching tetrahedra: a hybrid representation for high-resolution 3d shape synthesis." Advances in Neural Information Processing Systems 34 (2021): 6087-6101.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper presents a method for efficiently generating meshes from point clouds. The authors propose an hourglass transformer network architecture and a truncated sequence training scheme, which enable the generation of meshes with a large number of faces and diverse types. Compared to existing methods, this approach requires less training memory and achieves faster throughput.

### Strengths
The proposed method addresses an important challenge in 3D mesh generation: the number of faces significantly affects the quality and fidelity of the results, making a higher face count crucial. Experimental results indicate that this method can produce highly detailed meshes. 

Additionally, the authors present the motivation for their algorithm design, based on observed issues in real-world data, offering valuable insights for the academic community.

### Weaknesses
The author mentions that the tokens of the last vertex have high perplexity, which led to the design of the Hourglass Transformer to address this issue. However, the causal relationship here does not seem entirely clear. Within the architecture of the Hourglass Transformer, there is no obvious special treatment for the last vertex tokens. While the Hourglass Transformer is an effective structure, linking it directly to the perplexity of the last vertex tokens feels somewhat tenuous. Specifically, the paper lacks a detailed explanation of how the hierarchical processing and dynamic compute allocation inherent in the Hourglass Transformer inherently mitigate the high perplexity observed in the last vertex tokens. Further clarification on the mechanism by which this architecture addresses the perplexity issue would strengthen the paper's argument.


In the experiments, the authors used high-quality point clouds as input. However, in practical applications, point clouds often contain noise. This paper does not discuss or experiment on this issue, which inevitably raises concerns about its practicality. In particular, the paper should investigate the robustness of the proposed method to varying levels of noise and different types of noise distributions. Including experiments with noisy point clouds and a discussion of how the method handles such noise would significantly enhance the paper's applicability to real-world scenarios.


The author only compares their method with one other approach and does not include a related work section. This makes it difficult for those not working in mesh generation to follow the advancements in the field and compare the proposed method. For instance, how does it differ from existing mesh generation methods such as CLAY [1]? A comprehensive comparison with state-of-the-art methods, including both direct mesh generation techniques and iso-surfacing methods, is crucial. Furthermore, a dedicated related work section is necessary to provide context and highlight the novelty of the proposed approach within the broader landscape of mesh generation research.

### Questions
I believe that the problem this paper aims to address (generating detailed meshes) is meaningful. However, there are many areas for improvement in the experimental design and writing.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces a transformer-based approach to mesh generation. Given an input point cloud, the hourglass architecture (MESHTRON), like an Unet or an AE, compresses and reconstructs the mesh as output. The intermediate states (or latent) have an explicit meaning, corresponding to vertex and face representation. During training the model is trained by exploiting the adjacency of the triangles combined with a sliding window approach. Such a choice reduces memory consumption and allows the model to scale to complex and longer mesh sequences.

### Strengths
The proposed approach shows potential. The intermediate latent representation makes use of the geometric construction of meshes. The training procedure allows the architecture to scale to longer and more complex meshes.

### Weaknesses
Although the paper is very promising, several details are unclear. I would appreciate it if the authors clarify them:
1. several details are obscured in the manuscript, or not appropriately presented:
   - the meaning of the intermediate representation is not well presented. It can be inferred from Figure 4, but I the authors should to discuss it in the text for the sake of the reader - please expand Section 3.1;
   - it is not clear how the sliding window is used during inference. For example, how is the sliding window decided? And given that the sequence is truncated during training, how is a larger mesh generated? Please, provide more details on the sliding window inference process in Section 3.2.
2. the authors claim the length of the mesh sequence can be 64K in faces, L158-159. However, I cannot find such examples (even in the supplementary material). Is this a theoretical limit or do authors have examples and did not include them in the material?
3. the authors point out "MESHTRON does not work from time to time", would you please elaborate? This is not an appropriate sentence for a scientific paper.
4. how is the global conditioning obtained? Is the input point cloud feed to the model and then the sequence used for cross attention?
5. would it be possible to condition from an image latent representation (say encoded by DinoViT) and project it onto the latent space of MESHTRON? (it is fine if it is future work, but worth mentioning in the paper)
6. a comparison with MeshGPT would be appreciated even if qualitative. As the code is not available, the authors could maybe reach out to MeshGPT's authors to get some examples.

### Questions
Please see the weakness section.

### Soundness
3

### Presentation
2

### Contribution
3
