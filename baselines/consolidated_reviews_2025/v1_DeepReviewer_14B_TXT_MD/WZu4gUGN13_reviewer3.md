### Summary

This paper proposes a method to learn the hidden physics of fluid simulations from a single 3D video. The method is based on a probabilistic particle-based fluid simulator, which is pretrained on particle data and then adapted to visual observations through a variational inference framework. The method can infer and transfer the hidden physical properties of fluids to novel scenes with different geometries, boundaries, and dynamics. The paper evaluates the method on synthetic datasets and shows its potential for real-world experiments.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper proposes a novel method to learn the hidden physics of fluid simulations from a single 3D video, which is a challenging and important problem in computer graphics and vision.
2. The method is based on a probabilistic particle-based fluid simulator, which is a powerful and flexible model for fluid dynamics.
3. The method can infer and transfer the hidden physical properties of fluids to novel scenes with different geometries, boundaries, and dynamics, which demonstrates its generalization ability and robustness.
4. The paper evaluates the method on synthetic datasets and shows its potential for real-world experiments, which validates its effectiveness and applicability.

### Weaknesses

#### Some Related Works


#### comment

1. The method relies on a probabilistic particle-based fluid simulator, which may be computationally expensive and memory-intensive for large-scale or complex scenes. The paper does not provide a detailed analysis of the computational cost associated with the particle-based simulation, especially concerning the number of particles required to achieve accurate results and how this scales with scene complexity. Furthermore, the memory footprint of storing particle states and intermediate results could become a bottleneck for high-resolution simulations.
2. The method may be sensitive to the quality and quantity of the visual observations, which may affect the accuracy and robustness of the learned physical properties. The paper does not explore the impact of noisy or incomplete visual data on the performance of the method. For example, how does the method handle occlusions, motion blur, or variations in lighting conditions? The robustness of the method to these real-world challenges needs to be more thoroughly investigated.
3. The method may not be able to handle some complex or unusual physical phenomena, such as turbulence, multiphase flows, or chemical reactions. The paper does not provide a clear explanation of the limitations of the method in handling these complex phenomena. For instance, how does the method model the interactions between different fluid phases or the effects of chemical reactions on the fluid dynamics? The paper should discuss the specific challenges and potential solutions for extending the method to these scenarios.

### Suggestions

The paper should include a more detailed analysis of the computational cost of the proposed method, specifically focusing on the particle-based simulation component. This analysis should include a breakdown of the time complexity of the different stages of the simulation, such as particle initialization, force calculation, and particle update. The authors should also investigate the memory requirements of the method, considering the number of particles and the size of the data structures used to store particle states and intermediate results. It would be beneficial to provide a scaling analysis that shows how the computational cost and memory footprint change with the number of particles and the complexity of the simulated scene. Furthermore, the authors should explore techniques to optimize the simulation, such as adaptive particle refinement or parallelization, to improve the efficiency of the method for large-scale simulations. This would provide a more complete understanding of the practical limitations of the method and guide future research in this area.

To address the sensitivity of the method to the quality and quantity of visual observations, the authors should conduct a more thorough evaluation of the method's robustness to various types of noise and incompleteness in the input data. This evaluation should include experiments with different levels of noise, such as Gaussian noise, salt-and-pepper noise, and motion blur. The authors should also investigate the impact of occlusions and variations in lighting conditions on the performance of the method. It would be beneficial to explore techniques to improve the robustness of the method, such as data augmentation, robust loss functions, or regularization methods. For example, the authors could explore the use of adversarial training to make the method more robust to noisy or incomplete data. Additionally, the authors should investigate the minimum amount of visual data required to achieve acceptable performance and provide guidelines for selecting the appropriate amount of data for different scenarios. This would help to ensure that the method can be applied to real-world scenarios where visual data may be noisy or incomplete.

The paper should also provide a more detailed discussion of the limitations of the method in handling complex physical phenomena, such as turbulence, multiphase flows, and chemical reactions. The authors should explain the specific challenges of modeling these phenomena using the proposed method and discuss potential solutions for addressing these challenges. For example, the authors could explore the use of more sophisticated particle-based models that can capture the complex interactions between different fluid phases or the effects of chemical reactions on the fluid dynamics. The authors should also investigate the possibility of incorporating additional physical constraints or regularization terms into the learning objective to ensure that the learned physical properties are physically plausible. Furthermore, the authors should provide a roadmap for future research in this area, outlining the specific steps that need to be taken to extend the method to handle more complex physical phenomena. This would help to guide future research and ensure that the method can be applied to a wider range of real-world scenarios.

### Questions

1. How does the method compare to other methods for learning fluid simulations from data, such as neural networks or Gaussian processes?
2. How does the method handle noisy or incomplete visual observations, such as occlusions, motion blur, or low-resolution images?
3. How does the method scale to large-scale or complex scenes, such as oceans, rivers, or weather systems?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
