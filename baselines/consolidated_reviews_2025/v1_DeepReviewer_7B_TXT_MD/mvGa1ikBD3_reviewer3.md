### Summary

The paper proposes a novel Graph Neural Network (GNN) architecture for modeling anisotropic materials. The key contribution is a direction encoding scheme that preserves directional information during message passing, allowing the GNN to better capture the deformation and anisotropic behavior of materials. The method is evaluated on a set of qualitative and quantitative examples, demonstrating superior performance over the state-of-the-art MeshGraphNets approach in terms of accuracy and convergence speed.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

- The proposed direction encoding scheme is simple yet effective, allowing the GNN to better capture material anisotropy.
- The paper is well-written and easy to follow.
- The method is evaluated on a set of qualitative and quantitative examples, demonstrating superior performance over the state-of-the-art MeshGraphNets approach.

### Weaknesses

#### Some Related Works


#### comment

 - The proposed method is only applied to the simulation of deformable objects, which limits its applicability to other domains.
- The method is only compared to one baseline method, which is not sufficient to demonstrate its superiority.
- The paper lacks a discussion of the limitations of the proposed method.

### Suggestions

The paper's primary weakness lies in its limited scope and lack of comprehensive evaluation. While the proposed direction encoding scheme is interesting, its applicability is restricted to deformable object simulation. To broaden the impact, the authors should explore the method's performance in other domains where anisotropic materials are prevalent, such as biomechanics, geomechanics, or composite material modeling. This would involve adapting the method to different material properties and boundary conditions, which would provide a more robust assessment of its generalizability. Furthermore, the current evaluation is insufficient to demonstrate the method's superiority. The authors should compare their method against a wider range of state-of-the-art techniques, including both traditional numerical methods and other GNN architectures specifically designed for material modeling. This would provide a more rigorous benchmark and highlight the specific advantages of the proposed approach. 

To address the lack of a thorough discussion of limitations, the authors should explicitly acknowledge the constraints of their method. For example, the current implementation may not be suitable for materials with complex microstructures or for simulations involving large deformations. The authors should also discuss the computational cost of their method, particularly in comparison to other approaches. This would help readers understand the trade-offs involved in using the proposed method and identify potential areas for future research. Additionally, the authors should consider the sensitivity of their method to hyperparameter choices and provide guidelines for selecting appropriate values. This would make the method more accessible to other researchers and facilitate its adoption in practical applications. A more detailed analysis of the method's performance under different loading conditions would also be beneficial.

Finally, the paper would benefit from a more in-depth analysis of the method's behavior. For example, the authors could investigate how the direction encoding scheme affects the propagation of stress waves or the onset of material failure. This would provide a deeper understanding of the method's underlying mechanisms and its potential for addressing complex material behavior. The authors should also consider visualizing the learned representations to gain insights into how the GNN captures the anisotropic properties of the materials. This could involve techniques such as dimensionality reduction or feature visualization. By providing a more comprehensive analysis of the method's strengths and limitations, the authors can significantly enhance the paper's impact and contribute to the advancement of the field.

### Questions

- How does the proposed method perform in other domains beyond deformable object simulation?
- How does the proposed method compare to other state-of-the-art methods for material modeling?
- What are the limitations of the proposed method?

### Rating

5

### Confidence

3

**********
