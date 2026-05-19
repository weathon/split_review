### Summary

This paper proposes a GNN-based method for modeling the behavior of nonlinear and anisotropic materials. The key innovation is a direction encoding scheme that preserves directional information during message passing, allowing the model to better capture material anisotropy. The authors demonstrate the effectiveness of their approach through a series of experiments, showing superior performance compared to existing methods.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel direction encoding scheme that effectively captures material anisotropy, which is a significant advancement in the field of material simulation.
2. The method is evaluated on a variety of qualitative and quantitative examples, demonstrating its effectiveness and robustness.
3. The paper is well-written and easy to follow, with clear explanations of the methodology and experimental setup.

### Weaknesses

#### Some Related Works


#### comment

1. The experiments are limited to a few simple geometries, which may not fully demonstrate the generalizability of the method to more complex scenarios. Specifically, the paper does not explore the performance of the method on structures with varying topologies or boundary conditions, which are common in real-world applications. The current experiments are limited to basic shapes, and it is unclear how the method would perform on more complex geometries with intricate details or varying material properties.
2. The paper does not provide a detailed analysis of the computational cost of the method, which is an important factor for practical applications. The paper lacks a discussion of the time and memory requirements of the proposed method, making it difficult to assess its suitability for large-scale simulations. A comparison of the computational cost with existing methods would be beneficial.
3. While the paper compares the proposed method with MeshGraphNets, it does not explore other state-of-the-art GNN architectures for physics simulation. The paper should include a comparison with other relevant GNN models to demonstrate the advantages of the proposed method over existing approaches. The current comparison is limited, and it is unclear how the proposed method compares to other state-of-the-art GNN architectures for physics simulation.

### Suggestions

The authors should significantly expand the experimental evaluation to include more complex geometries and boundary conditions. This would involve testing the method on structures with varying topologies, such as beams with different cross-sections, or structures with complex connections. Furthermore, the authors should explore the performance of the method under different loading conditions, including non-uniform forces and displacements. This would provide a more comprehensive assessment of the method's generalizability and robustness. The experiments should also include a detailed analysis of the method's performance on structures with varying material properties, such as different elastic moduli or Poisson ratios. This would help to identify the limitations of the method and provide insights into its applicability to real-world scenarios.

To address the lack of computational analysis, the authors should provide a detailed breakdown of the time and memory requirements of the proposed method. This should include a comparison of the computational cost with existing methods, such as finite element methods or other GNN-based approaches. The analysis should also consider the scalability of the method with respect to the size of the simulation, including the number of nodes and edges in the mesh. The authors should also discuss the potential for optimizing the method to reduce its computational cost, such as by using more efficient message-passing algorithms or by parallelizing the computation. This would make the method more practical for large-scale simulations.

Finally, the authors should include a more comprehensive comparison with other state-of-the-art GNN architectures for physics simulation. This should involve comparing the performance of the proposed method with other relevant GNN models, such as those based on graph convolutional networks or attention mechanisms. The comparison should include a detailed analysis of the strengths and weaknesses of each method, as well as a discussion of the factors that contribute to their performance. The authors should also discuss the potential for combining the proposed method with other GNN architectures to further improve its performance. This would provide a more complete picture of the state-of-the-art in GNN-based material simulation and help to identify the unique advantages of the proposed method.

### Questions

1. How does the proposed method perform on more complex geometries and boundary conditions?
2. What is the computational cost of the proposed method compared to existing methods?
3. How does the proposed method compare to other state-of-the-art GNN architectures for physics simulation?

### Rating

6

### Confidence

3

**********
