### Summary

The paper introduces a novel Graph Neural Network (GNN) architecture designed to model the behavior of nonlinear and anisotropic materials. The authors propose a method to encode directional information into edge features, which enhances the GNN's ability to capture material anisotropy. The paper demonstrates that this approach outperforms existing GNN models in capturing material anisotropy through qualitative and quantitative evaluations.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

The paper is well-structured and clearly written, making it easy to follow the proposed methodology and experimental results. The authors provide a detailed description of the GNN architecture and the physics-based loss function, which is essential for understanding the technical contributions.

### Weaknesses

#### Some Related Works


#### comment

The paper's experimental evaluation is limited to a few simple geometries, which raises concerns about the generalizability of the proposed method to more complex scenarios. The authors should consider testing their approach on a wider range of geometries and material properties to demonstrate its robustness and applicability in real-world engineering problems.

While the paper compares the proposed method with MeshGraphNets, it does not explore other state-of-the-art GNN architectures for physics simulations. Including comparisons with other relevant baselines would provide a more comprehensive evaluation of the method's performance and highlight its unique advantages.

The paper lacks a detailed discussion of the computational cost associated with the proposed GNN architecture. It would be beneficial to analyze the scalability of the method with respect to the number of nodes and edges in the mesh, as well as the impact of different hyperparameters on the training time and memory usage.

### Suggestions

To address the limitations in the experimental evaluation, the authors should consider a more rigorous testing methodology that includes a diverse set of geometries and boundary conditions. Specifically, they should explore more complex shapes beyond simple beams and bars, such as plates, shells, and structures with varying topologies. Furthermore, the evaluation should include a wider range of material properties, including different elastic moduli, Poisson's ratios, and anisotropic tensors. This would provide a more comprehensive assessment of the method's ability to generalize to different material behaviors and structural configurations. The authors should also consider using more realistic loading scenarios, such as non-uniform forces and displacements, to test the robustness of the proposed approach. This would involve creating a more comprehensive set of test cases that cover a wider range of physical conditions and structural behaviors, which would better demonstrate the practical applicability of the method.

To strengthen the evaluation, the authors should include comparisons with other state-of-the-art GNN architectures for physics simulations. This could involve implementing and evaluating other relevant models, such as those based on graph convolutional networks or attention mechanisms. The comparison should not only focus on the accuracy of the results but also on the computational efficiency and scalability of the different methods. This would provide a more comprehensive understanding of the strengths and weaknesses of the proposed approach compared to existing techniques. The authors should also consider comparing their method with traditional finite element methods (FEM) in terms of accuracy and computational cost, to provide a benchmark for the performance of their approach. This would help to contextualize the results and demonstrate the potential advantages of using a GNN-based approach for modeling material behavior.

Finally, the authors should provide a more detailed analysis of the computational cost associated with their proposed GNN architecture. This should include a breakdown of the time and memory requirements for different stages of the training and inference processes, such as the forward pass, backward pass, and parameter updates. The analysis should also consider the impact of different hyperparameters, such as the number of layers, the size of the hidden layers, and the learning rate, on the computational cost. Furthermore, the authors should discuss the scalability of the method with respect to the number of nodes and edges in the mesh, and provide insights into how the method can be optimized for large-scale simulations. This would help to understand the practical limitations of the method and provide guidance for future research.

### Questions

1. How does the proposed method perform on more complex geometries and boundary conditions? Can you provide additional experiments to demonstrate its generalizability?

2. Can you compare the proposed method with other state-of-the-art GNN architectures for physics simulations, and discuss the advantages and disadvantages of each approach?

3. What is the computational cost of training and inference with the proposed GNN architecture? How does it scale with the size of the mesh and the number of nodes/edges?

### Rating

3

### Confidence

3

**********
