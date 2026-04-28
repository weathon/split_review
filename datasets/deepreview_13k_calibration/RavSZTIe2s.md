# Shape as Line Segments: Accurate and Flexible Implicit Surface Representation

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 8, 6, 6

## Abstract
Distance field-based implicit representations like signed/unsigned distance fields have recently gained prominence in geometry modeling and analysis. However, these distance fields are reliant on the closest distance of points to the surface, introducing inaccuracies when interpolating along cube edges during surface extraction. Additionally, their gradients are ill-defined at certain locations, causing distortions in the extracted surfaces. To address this limitation, we propose Shape as Line Segments (SALS), an accurate and efficient implicit geometry representation based on attributed line segments, which can handle arbitrary structures. Unlike previous approaches, SALS leverages a differentiable Line Segment Field to implicitly capture the spatial relationship between line segments and the surface. Each line segment is associated with two key attributes, intersection flag and ratio, from which we propose edge-based dual contouring to extract a surface. We further implement SALS with a neural network, producing a new neural implicit presentation. Additionally, based on SALS, we design a novel learning-based pipeline for reconstructing surfaces from 3D point clouds. We conduct extensive experiments, showcasing the significant advantages of our methods over state-of-the-art methods. We have included the source code in the Supplemental Material.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents a learnable surface extraction method based on edge-based dual contouring. Similar to Neural Dual Contouring (NDC), it uses a network to predict an intersection or crossing flag per edge. However, unlike NDC, it optimizes vertex locations within each cell using a Quadratic Error Function (QEF) rather than predicting them directly through the network. This optimization requires both the position of the intersection along each edge and its normal direction. Consequently, in addition to predicting the intersection flag, the network is also trained to output a scalar value representing the intersection position on the edge, using a concatenation of the corresponding cell vertices as input. Instead of the normal direction the paper uses the gradient of this intersection scalar  which is shown to  align with the the normal direction.

Extensive experiments validate the method’s effectiveness, leveraging the ABC and non-manifold ABC datasets to evaluate implicit representation in addition to DeepFashion3D, Synthetic Rooms, and Waymo datasets to illustrate generalization of  models trained with a subset of Thingi10k.

### Strengths
- The paper is well-written and easy to follow.
- The focus on edges (segments) rather than points for predicting intersection positions, combined with the novel approach of linking the gradient with the surface normal, effectively leverages QEF optimization for vertex positioning.
- **Evaluation and performance:** The evaluations are thorough, showing clear improvements over state-of-the-art methods.

### Weaknesses
 - **Motivation and comparison with Neural Dual Contouring (NDC):** The paper could better clarify its approach relative to NDC, particularly why optimizing vertex locations with QEF outperforms direct network predictions. The distinction between predicting intersection points directly via a network, as in NDC, versus using a QEF optimization is not sufficiently motivated. A more detailed explanation of the limitations of direct prediction and the advantages of the QEF approach, especially concerning generalization and robustness to varying grid resolutions, would be beneficial.
- **Training and inference times:** A table comparing performance, training time, and inference time would provide clarity. The method appears slower in inference than others; for instance, NDC achieves sub-second inference at a 128 resolution. Then, the question is  how good is  the trade-of between performance and inference time of the proposed method ? The paper lacks a detailed analysis of the computational overhead introduced by the QEF optimization step. While the method demonstrates good performance, the computational cost, particularly during inference, needs to be more thoroughly examined and compared against other methods, such as NDC, which are known for their speed. A breakdown of the time spent on different stages of the pipeline (e.g., network prediction, QEF optimization, mesh extraction) would be valuable.
- **Dependence on K-NN size for point cloud surface reconstruction:** The paper lacks details on how the K-NN value is chosen for each dataset and point cloud density, which would help to understand its impact on performance. The impact of the K-NN parameter on the reconstruction quality is not sufficiently explored. The paper should provide a more rigorous analysis of how the K-NN value is selected and how it affects the reconstruction accuracy across different datasets and point cloud densities. A discussion on the sensitivity of the method to this parameter and guidelines for choosing an appropriate value would be helpful.

### Questions
- How good is the trade-of between performance and inference time of the proposed method compared to other methods?
- How the K-NN value is chosen for each dataset and point cloud density, which would help to understand its impact on performance?
- To solve the QEF optimization, the gradient the network w.r.t e one of the edge vertices should be used. Which one do you use? Also since they have different orientations how does this choice impact the stability of the optimization and the overall performance?

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
The paper proposes Shape as Line Segments (SALS), an accurate and efficient implicit geometry representation based on attributed line segments, which can handle arbitrary structures. The authors then design a novel learning-based pipeline for reconstructing surfaces from 3D point clouds. The experiments show the method produces better results than the state-of-the-art methods.

### Strengths
- The paper's contributions are clearly defined, with comprehensive experimental validation on several benchmark datasets.

- Paper writing is clear and it’s easy to read.

### Weaknesses
 - Some results exhibit only minor differences, as seen in Figure 8, where the outcomes of Ours and GeoUDF appear quite similar. Presenting additional results, such as error maps or normal maps, may provide clearer visual distinctions.

- Lack of analysis of limitations. It would be interesting to evaluate how the proposed method performs on thin structures, such as leaves, or particularly complex geometric structures, like a basket, to better understand its applicability to different types of shapes.

### Questions
- I suggest add normal maps, which may highlight the differences more clearly in certain results, such as in Fig. 11.
- Some related works need to be added. [1-3].

- In the network design, I’m interested in exploring the results of replacing max pooling with mean pooling, as it may provide more information of neighbors in feature aggregation.

- Discuss the limitations.

[1] Fast Learning of Neural Implicit Surfaces for Multi-view Reconstruction
[2] NeUDF: Learning Neural Unsigned Distance Fields with Volume Rendering
[3] NeAT: Learning neural implicit surfaces with arbitrary topologies from multi-view images

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a novel method for sharper surface reconstruction. It proposes to model the implicit surfaces as a field of line segments, in comparison to the previous fields for points.

### Strengths
- A novel implicit representation of surfaces based on line segments is proposed. 
- For the novel line segments field, surfaces are extracted with edge-based dual contouring.
- The LSF-method is extend to surface reconstruction from point clouds. 
- Experimental demonstrations are provided for manifold and non-manifold structures.

### Weaknesses
 - Quantitative comparison are only provided for a limited amount of shapes in ABC dataset. 
- The improvement in surface quality appears incremental. The line segment field uses query grids of $128^3$. What is the counterpart resolution of point queries for the compared methods? 
- Given the method’s focus on sharper surface reconstruction, it is recommended that the authors also report metrics evaluated specifically around surface edges, similar to those used in ``Neural Dual Contouring (Chen et al., SIGGRAPH 2022)''.

### Questions
- For the applications to Waymo data, are the data also rescaled to a unit cube?

### Soundness
3

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
The paper presents a new approach for implicitly encoding 3D surfaces. The idea is to encode how an arbitrary line segment intersects a surface, represented by a binary variable showing intersection or not, and a scalar within [0,1] showing the ratio of the intersection point along the line segment. The motivation for using such a line segment representation is that to extract surfaces from implicit fields, one usually has to find such intersection points for regular grid edges, as done in marching cubes and dual contouring. The paper does analysis of this line segmentation representation, presents a dual contouring adaptation for this representation, develops a learning based network design for generating such a representation, and conducts experiments for shape encoding and shape reconstruction from point clouds, where the method shows improved accuracy than alternative representations like SDF and UDF. 

The idea makes sense intuitively by directly catering for the surface extraction step when learning the implicit rep, and is novel as far as I know. Given the novelty of the approach, some questions can be answered to better understand the approach. See the questions below.

### Strengths
The idea of representing shapes as intersections with respect to arbitrary edges is pursued and turned into a concrete design, and shows improved accuracy than alternative distance field representations due to its direct compliance with surface extraction algorithms like dual contouring.

The paper is well written and easy to read overall.

The paper shows the advantage of the new representation in two different tasks, i.e. shape encoding and shape reconstruction from point clouds. The dataset used is also challenging and diverse, including nonmanifold CAD shapes, scenes and open boundary shapes.

### Weaknesses
There remain some key technical questions that can be explored for this novel representation.

- How to handle cases where a line segment should intersect the surface multiple times? Such cases should be common when the line segment is larger than the local feature size. The method, as described, appears to only capture a single intersection point, potentially leading to inaccurate surface representations when multiple intersections exist along a single line segment. This is a critical limitation that needs to be addressed, especially in areas with high curvature or complex geometry.

- I am not sure the proof for Theorem 1 is correct. Why are p and n not functions of u/v? What assumptions have to be made about the surface, to ensure this invariance to u/v? The proof seems to assume a constant normal and point on the tangent plane, which is not generally true for arbitrary surfaces. The relationship between the chosen point and normal and the line segment endpoints u and v needs to be rigorously established.

- Eq(2), should there be a square of the dot product? Otherwise the minimization is not bounded from below. The current formulation of the loss function in Eq(2) lacks a square term on the dot product, which would result in an unbounded minimization problem. This needs to be corrected to ensure proper training.

- Sec.3.3, it's said that surface normal is determined as the gradient of s. But the gradient is taken with respect to which variable? u or v? What if they give different gradients? The method for determining the surface normal using the gradient of 's' is ambiguous. It is unclear whether the gradient is computed with respect to 'u' or 'v', and if these gradients differ, how the normal is consistently defined. This could lead to inconsistencies in the surface reconstruction.

- Related to the above question, the network producing the line-segment field should have certain invariance and equi-variance. That is, with respect to the switch of u/v, its output o (binary intersection) should be invariant, and its output s (ratio) should be equivariant. But the network design in its current form seems not preserve such properties. The network architecture needs to be carefully designed to ensure that the intersection flag 'o' remains invariant to the order of endpoints 'u' and 'v', while the ratio 's' transforms appropriately when the endpoints are switched. The current design does not explicitly enforce these properties.

The results frequently show holes that are undesirable. Such holes would not appear for SDF based methods. What can be done to fix such issues? The presence of holes in the reconstructed surfaces is a significant drawback. The method needs to be more robust to avoid these artifacts, especially when compared to SDF-based methods that typically produce closed surfaces.

The ablation about normal vectors (Sec.4.3) is quite obscure, with only one visual example and minor differences. Can quantitative differences be observed with or without normal vector for dual contouring? The ablation study on the use of normal vectors is insufficient. A single visual example is not enough to demonstrate the impact of normal vectors on the reconstruction quality. Quantitative metrics are needed to assess the contribution of normal vectors to the dual contouring process.

### Questions
See weakness section.

### Soundness
3

### Presentation
3

### Contribution
3
