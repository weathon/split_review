### Summary

This paper presents a method to learn the hidden physics of fluids from a single 3D video. The key idea is to represent the hidden physical properties in visual observations using probabilistic latent states. The latent space connects the particle space and visual space to infer and transfer hidden physics with probabilistic modeling. The framework consists of a probabilistic particle transition module, a physical prior learner, a particle-based posterior estimator, and a neural renderer. The latent features are drawn from trainable marginal distributions that are learned to approximate the visual posterior distribution obtained from a learned neural renderer. The model is validated in three ways: (i) novel scene simulation with the learned visual-world physics, (ii) future prediction of the observed fluid dynamics, and (iii) supervised particle simulation. The model demonstrates strong performance in all three tasks.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The idea of learning the hidden physics of fluids from a single 3D video is novel and interesting.
3. The method is validated in three ways, and the model demonstrates strong performance in all three tasks.
4. The paper provides a detailed description of the method, including the probabilistic particle transition module, the physical prior learner, the particle-based posterior estimator, and the neural renderer.

### Weaknesses

#### Some Related Works


#### comment

1. The method relies on a probabilistic particle-based fluid simulator, which may be computationally expensive and memory-intensive for large-scale or complex scenes. Specifically, the particle-based approach, while offering flexibility, can become inefficient when dealing with a large number of particles, leading to increased computational time and memory requirements. This could limit the applicability of the method to scenarios with high particle counts or intricate fluid dynamics.
2. The method may be sensitive to the quality and quantity of the visual observations, which may affect the accuracy and robustness of the learned physical properties. The reliance on visual data means that the method's performance is directly tied to the quality of the input video. Factors such as low resolution, motion blur, or occlusions could significantly impact the accuracy of the inferred physical properties. Furthermore, the method's ability to generalize to unseen scenarios might be limited if the training data does not adequately cover the range of possible fluid behaviors.
3. The method may not be able to handle some complex or unusual physical phenomena, such as turbulence, multiphase flows, or chemical reactions. The current framework is designed for single-phase fluid dynamics and may not be directly applicable to more complex phenomena like turbulent flows, which involve a wide range of spatial and temporal scales, or multiphase flows, where interactions between different fluid phases need to be considered. The method's ability to model chemical reactions within the fluid is also unclear, as this would require additional considerations beyond the current framework.

### Suggestions

To address the computational cost associated with the particle-based simulator, the authors could explore techniques to optimize the simulation process. This could involve implementing adaptive particle refinement strategies, where the number of particles is dynamically adjusted based on the local fluid dynamics, or exploring alternative simulation methods that are more computationally efficient while still capturing the essential physics. Furthermore, investigating the use of parallel computing techniques could help to reduce the simulation time for large-scale scenarios. The authors should also consider providing a more detailed analysis of the computational complexity of their method, including the time and memory requirements as a function of the number of particles and the complexity of the simulated scene. This would help to better understand the limitations of the method and guide future research in this area.

To improve the robustness of the method to variations in visual data quality, the authors could explore data augmentation techniques during training. This could involve introducing synthetic noise, blur, or occlusions to the training data to make the model more resilient to these types of imperfections in real-world scenarios. Additionally, the authors could investigate the use of more robust visual feature extraction methods that are less sensitive to variations in image quality. It would also be beneficial to evaluate the method's performance on a wider range of visual datasets with varying levels of quality and complexity to better understand its limitations and identify areas for improvement. Furthermore, the authors should consider exploring techniques to handle occlusions, such as incorporating temporal information or using multi-view reconstruction methods to recover the missing information.

To extend the method to handle more complex physical phenomena, the authors could explore the use of more sophisticated particle-based models that can capture the dynamics of turbulent flows, multiphase flows, and chemical reactions. This could involve incorporating additional physical constraints or regularization terms into the learning objective to ensure that the learned physical properties are physically plausible. For example, the authors could explore the use of turbulence models or multiphase flow models within their framework. Furthermore, the authors should consider incorporating additional information, such as temperature or concentration fields, to model chemical reactions within the fluid. This would require extending the current framework to handle additional variables and interactions. The authors should also discuss the limitations of their method in handling these complex phenomena and suggest potential future research directions to address these limitations.

### Questions

1. How does the method compare to other methods for learning fluid simulations from data, such as neural networks or Gaussian processes?
2. How does the method handle noisy or incomplete visual observations, such as occlusions, motion blur, or low-resolution images?
3. How does the method scale to large-scale or complex scenes, such as oceans, rivers, or weather systems?

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
