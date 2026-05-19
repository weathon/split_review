### Summary

This paper proposes a novel mesh-based graph neural network architecture for anisotropic materials simulation. The key innovation is a directional encoding scheme that preserves directional information during message passing, enabling the accurate modeling of anisotropic material behavior. The method is trained using a physics-based loss function with unsupervised learning.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

- The paper introduces a novel directional encoding scheme for GNNs, which is a significant advancement for simulating anisotropic materials.
- The unsupervised training method reduces the need for labeled data, making the approach more practical for real-world applications.

### Weaknesses

#### Some Related Works

[1] Efficient Learning of Mesh-Based Physical Simulation with Graph Neural Network.

#### comment

 - The proposed method is only tested on simple geometries, such as beams, and the generalization capability to more complex geometries is unclear. The experiments do not explore the method's performance on geometries with significant variations in curvature or topological complexity, which are common in real-world scenarios. This raises concerns about the robustness of the approach.
- The fiber orientation angle is uniformly sampled between 0 and 90 degrees, which may limit the model's ability to generalize to fiber orientations outside this range. While the authors may have chosen this range for simplicity, it is not clear if the model can effectively handle cases where fibers are oriented at angles greater than 45 degrees relative to the principal axes of the geometry, or if the model can handle complex fiber waviness or non-uniform distributions. This limited sampling could lead to poor performance when applied to more diverse datasets.
- The baseline method, MeshGraphNets, is outdated, and the paper does not compare the proposed method with more recent state-of-the-art approaches. The lack of comparison with more recent methods makes it difficult to assess the true advancement of the proposed method. The paper should include comparisons with other recent GNN-based simulation methods to better contextualize its performance.
- The paper lacks visualizations of stress and strain distributions, which could provide more detailed insights into the model's performance. Without visualizations of these quantities, it is difficult to understand how the model is capturing the anisotropic behavior of the material. These visualizations are crucial for understanding the model's internal representations and for identifying potential failure modes.
- The paper does not provide a detailed analysis of the computational efficiency of the proposed method compared to traditional simulation techniques. The lack of a computational analysis makes it difficult to assess the practical applicability of the method. The paper should include a comparison of the computational cost of the proposed method with traditional finite element methods, including the time required for training and inference.

### Suggestions

The paper should significantly expand its experimental evaluation to include more complex geometries and loading conditions. Specifically, the authors should consider testing their method on geometries with varying degrees of curvature, such as torus or sphere-like structures, and also on geometries with more complex topological features, such as those with holes or multiple connected components. Additionally, the loading conditions should be varied to include more complex force distributions, rather than just uniform forces. This would provide a more comprehensive assessment of the method's generalization capabilities. Furthermore, the authors should explore the method's performance on geometries with different aspect ratios and thickness variations to ensure the robustness of the approach. The inclusion of these more complex scenarios would provide a more realistic evaluation of the method's applicability to real-world problems.

To address the limitations of the fiber orientation sampling, the authors should extend their training data to include fiber orientations beyond the 0-90 degree range. Specifically, they should include fibers oriented at angles up to 90 degrees relative to the principal axes of the geometry, as well as fibers with more complex waviness and non-uniform distributions. This could be achieved by augmenting the training data with samples that have fibers at various angles and with different spatial variations. Furthermore, the authors should investigate the model's performance with fibers that are not aligned with the principal axes of the material, as this is a common scenario in real-world materials. This would help to ensure that the model can generalize to a wider range of fiber orientations and distributions. The authors should also consider using a more diverse set of fiber distributions, including those that are not uniform, to better simulate real-world materials.

Finally, the paper should include a more thorough comparison with state-of-the-art methods, including more recent GNN-based simulation techniques. The authors should also include comparisons with traditional finite element methods to provide a more comprehensive assessment of the method's performance. The comparison should include both accuracy and computational efficiency metrics. The authors should also provide visualizations of stress and strain distributions to provide more detailed insights into the model's performance. This would help to understand how the model is capturing the anisotropic behavior of the material and to identify potential failure modes. The paper should also include a detailed analysis of the computational efficiency of the proposed method, including the time required for training and inference, and compare it with traditional simulation techniques. This would help to assess the practical applicability of the method.

### Questions

- How does the proposed method perform on more complex geometries, such as those with intricate curves or non-uniform cross-sections?
- Can the model generalize to fiber orientations outside the 0-90 degree range used during training?
- How does the proposed method compare to more recent state-of-the-art approaches in terms of accuracy and computational efficiency?
- What is the computational overhead of the directional encoding scheme compared to standard message passing?
- How does the model handle scenarios with non-uniform or dynamically changing fiber orientations?
- Can the proposed method be extended to simulate other types of anisotropic materials, such as those found in biological tissues or composites?

### Rating

3

### Confidence

4

**********
