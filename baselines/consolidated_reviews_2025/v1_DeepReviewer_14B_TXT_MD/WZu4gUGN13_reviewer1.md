### Summary

The paper introduces Latent Intuitive Physics, a transfer learning framework for physics simulation that can infer hidden properties of fluids from a 3D video and simulate the observed fluid in novel scenes. The key idea is to represent the hidden physical properties in visual observations, which may be difficult to observe, using probabilistic latent states. The latent space connects the particle space and visual space to infer and transfer hidden physics with probabilistic modeling.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper introduces latent intuitive physics, a transfer learning framework for physics simulation that can infer hidden properties of fluids from a 3D video and simulate the observed fluid in novel scenes.
2. The key idea is to represent the hidden physical properties in visual observations, which may be difficult to observe, using probabilistic latent states.
3. The latent space connects the particle space and visual space to infer and transfer hidden physics with probabilistic modeling.

### Weaknesses

#### Some Related Works


#### comment

1. The related work should include more latest particle-based simulation.
2. The paper only considers fluid, but the method is based on particle simulation, which should be applicable to other simulation systems, such as rigid, soft, and other general VDT simulation. The paper will be more solid if the author can extend the method to other systems.
3. The method is complex, can the author provide an analysis of the method's complexity and running speed?
4. The author claims the method is probabilistic, but where is the probability? The author should clarify this point.
5. The author claims the method is latent intuitive physics, but where is the intuition? The author should clarify this point.

### Suggestions

The paper would benefit from a more thorough discussion of recent advancements in particle-based simulation. Specifically, the related work section should include a detailed analysis of methods that utilize neural networks for particle interaction and dynamics prediction. This would help to contextualize the proposed approach within the broader landscape of physics simulation and highlight its unique contributions. Furthermore, the authors should clarify how their method compares to existing techniques in terms of computational efficiency and accuracy, especially when dealing with complex fluid behaviors. A more detailed comparison with state-of-the-art methods would strengthen the paper's claims and provide a clearer understanding of its limitations.

While the focus on fluid simulation is understandable, the paper should address the potential of the proposed method for other simulation systems. Given that the method is based on particle simulation, it should be possible to extend it to rigid, soft, and general VDT simulations. The authors should discuss the challenges and modifications required to adapt the method to these different systems. For example, the interaction forces and constraints between particles would need to be adjusted to account for the specific properties of each system. The authors could also consider including experiments on these other systems to demonstrate the versatility of their approach. This would significantly enhance the impact and applicability of the proposed method.

The authors should provide a more detailed analysis of the method's computational complexity and running speed. The current description of the method is quite complex, and it is difficult to understand its computational cost. The authors should provide a breakdown of the time complexity of each step in the algorithm, including the training and inference phases. They should also discuss the memory requirements of the method and how they scale with the number of particles. Furthermore, the authors should provide a comparison of the running speed of their method with existing particle-based simulation techniques. This would help to assess the practicality of the proposed method for real-world applications.

### Questions

Please see the weakness.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
