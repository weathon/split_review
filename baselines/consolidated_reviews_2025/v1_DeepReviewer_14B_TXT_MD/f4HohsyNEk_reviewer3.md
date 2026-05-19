### Summary

This paper proposes NeuManifold, a method for generating high-quality watertight manifold meshes from multi-view images. The method combines neural volumetric fields for geometry initialization with differentiable rasterization for mesh optimization. The authors demonstrate that their method can generate accurate mesh reconstructions with faithful appearance, comparable to previous volume rendering methods while being faster in rendering. The generated mesh and neural texture reconstruction is also compatible with existing graphics pipelines and enables downstream 3D applications such as simulation.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is reasonable and achieves high-quality watertight manifold meshes.
3. The authors provide extensive experiments to demonstrate the effectiveness of their method.

### Weaknesses

#### Some Related Works


#### comment

1. The authors should provide more details on the implementation of the proposed method, such as the specific network architectures and training procedures. For example, what is the exact architecture of the neural volumetric field? What is the specific loss function used for differentiable rasterization? What are the hyperparameter settings for the optimization process?
2. It would be beneficial to include more ablation studies to analyze the contribution of each component of the proposed method. For instance, how does the choice of neural volumetric field initialization affect the final mesh quality? What is the impact of different differentiable rasterization techniques on the optimization process? How does the number of training views affect the reconstruction quality?
3. The authors should also discuss the limitations of their method and potential future directions. For example, how does the method perform on scenes with complex topologies or thin structures? What are the limitations of the neural texture representation? How can the method be extended to handle dynamic scenes or scenes with varying lighting conditions?

### Suggestions

The paper would benefit from a more detailed explanation of the neural volumetric field implementation. Specifically, the authors should describe the exact architecture of the network, including the number of layers, the type of activation functions used, and the number of parameters. Furthermore, the training procedure should be elaborated upon, including the specific loss functions used for both the volumetric rendering and the differentiable rasterization stages. It would be helpful to know the exact form of the loss function, including any weighting factors or regularization terms. The authors should also provide details on the optimization algorithm used, the learning rate schedule, and any other relevant hyperparameters. This level of detail is crucial for reproducibility and for understanding the method's behavior.

To strengthen the analysis, the authors should conduct more comprehensive ablation studies. For example, they could investigate the impact of different initialization strategies for the neural volumetric field. Instead of just comparing with no initialization, they could explore different pre-training techniques or different neural field architectures. Similarly, the authors should analyze the effect of different differentiable rasterization techniques. They could compare the performance of their chosen method with other alternatives, such as those based on soft rasterization or differentiable rendering. Furthermore, it would be valuable to study the sensitivity of the method to the number of input views. The authors could perform experiments with varying numbers of views and analyze how the reconstruction quality changes. This would provide insights into the robustness of the method and its applicability to different scenarios.

Finally, the authors should provide a more thorough discussion of the limitations of their method. They should address the challenges of reconstructing scenes with complex topologies, such as those with holes or thin structures. It would be beneficial to include examples of failure cases and discuss the reasons for these failures. The authors should also discuss the limitations of the neural texture representation, such as its ability to capture high-frequency details or its memory footprint. Furthermore, the authors should explore potential future directions for their research. This could include extending the method to handle dynamic scenes, incorporating lighting information, or improving the efficiency of the optimization process. A more comprehensive discussion of these aspects would significantly enhance the paper's impact.

### Questions

Please refer to the weakness.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
