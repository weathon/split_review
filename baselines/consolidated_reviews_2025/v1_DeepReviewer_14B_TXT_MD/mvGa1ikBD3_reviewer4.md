### Summary

This paper presents a novel Graph Neural Network (GNN) architecture designed to simulate anisotropic materials, which exhibit direction-dependent properties. Traditional GNNs have struggled with simulating such materials due to their inability to distinguish deformations in different directions, limiting them to isotropic materials. The proposed GNN architecture addresses this limitation by incorporating directional encodings of edge features, preserving directional information during message passing. This innovation allows the model to accurately capture the behavior of anisotropic materials. The paper demonstrates the effectiveness of the proposed approach through both qualitative and quantitative evaluations, showing that it outperforms existing mesh-based GNN methods in modeling anisotropic materials. The research has potential applications in fields such as engineering, computer graphics, and robotics, where simulating anisotropic materials is crucial.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel GNN architecture that effectively addresses the challenge of simulating anisotropic materials, which is a significant advancement over traditional GNNs limited to isotropic materials.
2. The proposed method is validated through a comprehensive set of experiments, demonstrating its superiority over existing approaches in terms of accuracy and efficiency.
3. The paper is well-organized, with a clear presentation of the problem, methodology, and results. The figures and tables effectively support the textual content, making complex concepts more accessible to readers.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method is only tested on simple geometries, such as beams, and the generalization capability to more complex geometries is unclear. Specifically, the paper lacks experiments on geometries with significant curvature or topological variations, which are common in real-world anisotropic materials. This raises concerns about the robustness of the method when applied to more intricate structures.
2. The fiber orientation angle is uniformly sampled between 0 and 90 degrees, which may limit the model's ability to generalize to fiber orientations outside this range. This limited sampling range does not fully explore the potential anisotropic behavior of materials, particularly those with fibers oriented at sharper angles relative to the loading direction. The model's performance with fibers at angles such as 75 or 80 degrees remains untested, potentially limiting its applicability.
3. The baseline method, MeshGraphNets, is outdated, and the paper does not compare the proposed method with more recent state-of-the-art approaches. The lack of comparison with more recent GNN architectures, especially those designed for physical simulations, makes it difficult to assess the true advancement of the proposed method. This omission makes it hard to determine if the performance gains are due to the directional encoding or simply a better choice of baseline.

### Suggestions

To address the limitations regarding geometry complexity, the authors should conduct experiments on a wider range of geometries, including those with significant curvature, such as spherical or toroidal shapes, and varying topologies, such as structures with holes or multiple connected components. This would provide a more comprehensive evaluation of the method's generalization capabilities. Furthermore, the inclusion of more complex loading conditions, such as non-uniform pressure distributions or dynamic loads, would better reflect real-world scenarios and provide a more rigorous test of the method's robustness. These additional experiments would help to establish the practical applicability of the proposed approach beyond simple beam-like structures.

To improve the evaluation of the model's ability to handle different fiber orientations, the authors should extend the training and testing data to include fiber angles beyond the 0-90 degree range. Specifically, they should include fibers oriented at angles such as 75 and 80 degrees relative to the loading direction. This would provide a more complete picture of the model's performance across a wider range of anisotropic behaviors. Additionally, the authors should consider using a more diverse set of fiber distributions, including non-uniform distributions, to better simulate real-world materials. This would help to ensure that the model is not overfitting to the specific uniform distribution used in the current experiments. The inclusion of these more challenging scenarios would provide a more rigorous evaluation of the model's generalization capabilities.

Finally, to provide a more accurate assessment of the proposed method's performance, the authors should compare it against more recent state-of-the-art GNN architectures designed for physical simulations. This would help to determine if the performance gains are due to the directional encoding or simply a better choice of baseline. The inclusion of these comparisons would provide a more comprehensive evaluation of the method's contribution to the field. Furthermore, the authors should consider including ablation studies to isolate the impact of the directional encoding on the overall performance. This would help to better understand the specific contribution of the proposed method and its potential for future research.

### Questions

1. How does the proposed method perform on more complex geometries, such as those with intricate curves or non-uniform cross-sections?
2. Can the model generalize to fiber orientations outside the 0-90 degree range used during training?
3. How does the proposed method compare to more recent state-of-the-art approaches in terms of accuracy and computational efficiency?
4. What is the computational overhead of the directional encoding scheme compared to standard message passing?
5. How does the model handle scenarios with non-uniform or dynamically changing fiber orientations?
6. Can the proposed method be extended to simulate other types of anisotropic materials, such as those found in biological tissues or composites?

### Rating

6

### Confidence

3

**********
