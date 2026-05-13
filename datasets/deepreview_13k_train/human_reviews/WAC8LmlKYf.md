# PivotMesh: Generic 3D Mesh Generation via Pivot Vertices Guidance

- Decision: Accept
- Scores: 6, 8, 6

## Abstract
Generating compact and sharply detailed 3D meshes poses a significant challenge for current 3D generative models. Different from extracting dense meshes from neural representation, some recent works try to model the native mesh distribution (i.e., a set of triangles), which generates more compact results as humans crafted. However, due to the complexity and variety of mesh topology, these methods are typically limited to small datasets with specific categories and are hard to extend. In this paper, we introduce a generic and scalable mesh generation framework PivotMesh, which makes an initial attempt to extend the native mesh generation to large-scale datasets. 
  We employ a transformer-based auto-encoder to encode meshes into discrete tokens and decode them from face level to vertex level hierarchically. Subsequently, to model the complex typology, we first learn to generate pivot vertices as coarse mesh representation and then generate the complete mesh tokens with the same auto-regressive Transformer. This reduces the difficulty compared with directly modeling the mesh distribution and further improves the model controllability. PivotMesh demonstrates its versatility by effectively learning from both small datasets like Shapenet, and large-scale datasets like Objaverse and Objaverse-xl. Extensive experiments indicate that PivotMesh can generate compact and sharp 3D meshes across various categories, highlighting its great potential for native mesh modeling.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper introduces PivotMesh, a framework for generating compact and detailed 3D meshes at scale. The approach leverages a transformer-based auto-encoder to encode meshes into discrete tokens, which are then decoded hierarchically from face to vertex level. A key contribution is the use of pivot vertices as a coarse representation to guide the generation of complete mesh tokens, allowing for complex topology modeling. The method is evaluated on diverse datasets, including ShapeNet, Objaverse, and Objaverse-xl, demonstrating its versatility and effectiveness in generating high-quality 3D meshes.

### Strengths
1. PivotMesh addresses a significant challenge in 3D mesh generation by proposing a scalable framework that can handle large-scale datasets with simplified triangles. The use of pivot vertices as a coarse representation for guiding mesh generation is innovative and effectively handles complex topologies.
2. The paper provides a thorough evaluation of PivotMesh across various datasets and applications, including mesh generation, variation, and refinement. The generated meshes are of high quality, with sharp details and complex geometries, outperforming existing methods.

### Weaknesses
1. Diversity of Generated Meshes: While the paper shows diverse mesh generation, a more systematic analysis or quantification of diversity could strengthen the results. The evaluations on more diverse shapes with complex topologies are encouraged to be conducted, such as some shapes with lots of holes, the thin structures (ficus in nerf-synthetic data), and so on.
2. More direct comparisons with the current state-of-the-art methods, especially in terms of computational efficiency and mesh quality, could be beneficial. There is more relative work, such as meshanything(2), EdgeRunner, the comparison is very essential to demonstrate the superiority of the proposed method.
3. The limitations and failure cases should be discussed comprehensively. And the paper acknowledges that the controlling ability of PivotMesh is not sufficient, and sometimes undesired geometries are produced. Enhancing the control mechanisms could be a valuable addition.

### Questions
The paper is well-written and presents a contribution to the field of 3D mesh generation. I am impressed with the quality of the generated results, but there are some minor issues: the comparison with other similar baselines and more diverse generated shapes. With the above suggestions addressed, the paper would be a strong candidate for publication. I recommend accepting this paper with minor revisions.
Detailed questions please refer to weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
In this work, the authors propose a novel framework for explicit mesh generation that can be trained on large-scale datasets. They employ a transformer-based autoencoder to obtain discretized tokens representing the mesh, which are later decoded hierarchically. Additionally, the generative networks are designed to first produce a sequence of pivot mesh vertices as a coarse representation, then use these as conditions to generate the actual mesh tokens. Experimental results demonstrate that the proposed framework achieves comparable and often superior performance to concurrent works. The authors also showcase various downstream applications of their method.

### Strengths
- The exploration of generating pivot vertices before faces appears to be a novel approach. Ablation studies validate its effectiveness, particularly without pivot guidance and degrees selection.
- Extensive experiments compare unconditional generation quality across both small and large datasets, such as ShapeNet and ObjaverseXL. The proposed framework outperforms existing methods in all settings.
- The framework demonstrates versatility through various applications, including point cloud-guided generation, mesh variations, and coarse mesh refinement.
- A novel analysis ensures the diversity and originality of the generated objects.

### Weaknesses
Although concurrent works are mentioned, several studies have begun exploring the generation of compact meshes in large datasets, demonstrating some success to a certain extent. It is recommended to revise the introduction and abstract to avoid claiming that existing work is difficult to extend to large datasets.



### Questions
- Including MeshXL's quantitative results would be highly beneficial, despite its use of a different training dataset. While this is concurrent work and the results would be for reference only, they could serve as a valuable benchmark, helping readers better understand the effectiveness of the proposed method.
- The paper claims that the proposed pivot mesh formulation can generate shorter sequences, providing estimated sequence lengths in Table 1. However, measuring these lengths on a real dataset would offer more clarity and insight into the method's efficiency.

Justification of Rating:
Overall, this work provides a novel direction for compact mesh generation and demonstrates its effectiveness in various aspects. The quantitative and qualitative comparisons show that it achieves good performance compared to existing and concurrent works. Additionally, various applications have outlined its potential beyond unconditional generative tasks. Despite some minor suggestions, I am currently leaning towards acceptance of this work.

### Soundness
4

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
This paper focuses on conditional triangle mesh generation based on the pivot vertices of the provided mesh.  The authors proposed to tokenize the mesh with transformer, rather than the GCN architecture used by MeshGPT. The pivot-guided method is shown to outperform PolyGen and MeshGPT.

### Strengths
- A transformer-based auto-encoder is proposed to encode the triangle meshes into discrete tokens.
- An auto-regressive transformer is proposed to generate the complete mesh tokens from pivot vertices.
- By conditioning on pivot vertices, the proposed method outperforms PolyGen and MeshGPT. 
- Downstream applications of the method are shown for mesh variation and coarse mesh refinement.

### Weaknesses
 - Both the auto-encoder and auto-regressive transformer use 24 layers of transformers, resulting the method to be memory taken and less efficient.

 - It is confusing how the discrete mesh tokens from auto-encoder and pivot vertices are combined for conditional mesh generation.  
- In lines 303-306 of page 6, the authors mentioned about face filtering in the datasets. Is there a distribution map to summarize the number of vertices and faces in the training and test meshes?

### Questions
- It is confusing how the discrete mesh tokens from auto-encoder and pivot vertices are combined for conditional mesh generation.  
- In lines 303-306 of page 6, the authors mentioned about face filtering in the datasets. Is there a distribution map to summarize the number of vertices and faces in the training and test meshes?

### Soundness
3

### Presentation
2

### Contribution
3
