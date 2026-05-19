### Summary

The paper proposes a Graph Neural Network (GNN) approach for simulating anisotropic materials, which is a significant advancement over traditional isotropic models. By introducing directional encodings in edge features, the model effectively captures the directional dependencies in material properties, a challenge that previous GNNs struggled with. The authors validate their model through extensive experiments, demonstrating improvements in accuracy and stability over baseline methods like MeshGraphNets. However, the paper could benefit from broader comparisons with non-GNN methods and a more detailed exploration of the model's generalization capabilities.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

The paper introduces a novel approach to modeling anisotropic materials using GNNs, addressing a gap in current simulation techniques. The directional encoding of edge features is a creative solution that enhances the model's ability to simulate real-world material behaviors accurately.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method is only tested on simple geometries, such as beams, and the generalization capability to more complex geometries is unclear.
2. The fiber orientation angle is uniformly sampled between 0 and 90 degrees, which may limit the model's ability to generalize to fiber orientations outside this range.
3. The baseline method, MeshGraphNets, is outdated, and the paper does not compare the proposed method with more recent state-of-the-art approaches.
4. The paper lacks visualizations of stress and strain distributions, which could provide more detailed insights into the model's performance.
5. The paper does not provide a detailed analysis of the computational efficiency of the proposed method compared to traditional simulation techniques.

### Suggestions

The paper's primary weakness lies in the limited scope of its experimental validation. While the proposed method demonstrates promising results on simple beam geometries, its applicability to more complex, real-world scenarios remains unclear. To address this, the authors should evaluate the method on a wider range of geometries, including those with intricate curves, non-uniform cross-sections, and varying topological features. For example, testing on geometries such as torus-like structures, or those with varying curvature, would provide a more robust assessment of the method's generalization capabilities. Furthermore, the current evaluation is limited to static simulations. It would be beneficial to assess the method's performance in dynamic scenarios, where the material properties and loading conditions change over time. This would provide a more comprehensive understanding of the method's capabilities and limitations.

Another area for improvement is the sampling strategy for fiber orientations. The current approach, which uniformly samples angles between 0 and 90 degrees, may not be sufficient to capture the full range of anisotropic behaviors. To enhance the model's generalization ability, the authors should consider sampling fiber orientations across the full 0-180 degree range, or even beyond, to account for more complex material structures. Additionally, the paper lacks a detailed analysis of the model's sensitivity to different fiber orientation distributions. It would be valuable to investigate how the model performs when presented with non-uniform or dynamically changing fiber orientations. This could be achieved by training the model on a dataset with a diverse range of fiber orientations and then evaluating its performance on a separate test set with different orientation distributions. This would provide insights into the model's robustness and its ability to handle real-world material variations.

Finally, the paper needs a more thorough comparison with state-of-the-art methods and a detailed analysis of computational efficiency. The current comparison with MeshGraphNets is insufficient, as it is an outdated baseline. The authors should compare their method with more recent GNN-based simulation techniques, as well as traditional finite element methods, to provide a more comprehensive assessment of its performance. This comparison should include both accuracy and computational efficiency metrics. Furthermore, the paper lacks a detailed analysis of the computational overhead of the directional encoding scheme compared to standard message passing. The authors should provide a breakdown of the computational cost associated with each component of the proposed method, and compare it with the computational cost of existing methods. This would help to understand the trade-offs between accuracy and computational efficiency, and to assess the practical applicability of the proposed method.

### Questions

1. How does the proposed method perform on more complex geometries, such as those with intricate curves or non-uniform cross-sections?
2. Can the model generalize to fiber orientations outside the 0-90 degree range used during training?
3. How does the proposed method compare to more recent state-of-the-art approaches in terms of accuracy and computational efficiency?
4. What is the computational overhead of the directional encoding scheme compared to standard message passing?
5. How does the model handle scenarios with non-uniform or dynamically changing fiber orientations?
6. Can the proposed method be extended to simulate other types of anisotropic materials, such as those found in biological tissues or composites?

### Rating

5

### Confidence

3

**********
