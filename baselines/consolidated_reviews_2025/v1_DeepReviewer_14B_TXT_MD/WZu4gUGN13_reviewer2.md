### Summary

The paper introduces a framework called Latent Intuitive Physics that learns the hidden properties of fluids from a 3D video and transfers this knowledge to a fluid simulator. The key contributions include a probabilistic fluid simulator that considers the stochastic nature of complex physical processes, and a variational inference learning method that can transfer the posteriors of the hidden parameters from visual observations to the fluid simulator. The proposed pretraining-inference-transfer optimization scheme allows for easy transfer of visual-world fluid properties to novel scene simulation with various initial states and boundary conditions. The model is evaluated on synthetic datasets and shows potential in real-world experiments.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper introduces a novel framework called Latent Intuitive Physics that learns the hidden properties of fluids from a 3D video and transfers this knowledge to a fluid simulator.
2. The key contributions include a probabilistic fluid simulator that considers the stochastic nature of complex physical processes, and a variational inference learning method that can transfer the posteriors of the hidden parameters from visual observations to the fluid simulator.
3. The proposed pretraining-inference-transfer optimization scheme allows for easy transfer of visual-world fluid properties to novel scene simulation with various initial states and boundary conditions.
4. The model is evaluated on synthetic datasets and shows potential in real-world experiments.

### Weaknesses

#### Some Related Works


#### comment

1. The paper only considers fluid, but the method is based on particle simulation, which should be applicable to other simulation systems, such as rigid, soft, and other general VDT simulation. The paper will be more solid if the author can extend the method to other systems.
2. The method is complex, can the author provide an analysis of the method's complexity and running speed?
3. The author claims the method is probabilistic, but where is the probability? The author should clarify this point.
4. The author claims the method is latent intuitive physics, but where is the intuition? The author should clarify this point.

### Suggestions

The paper would significantly benefit from a more thorough discussion of the method's applicability beyond fluid dynamics. While the core idea of learning hidden parameters from visual data is compelling, the current focus on fluids limits the impact. The authors should explore, even theoretically, how their approach could be adapted to simulate other physical systems like rigid body dynamics, soft body deformations, or even more general VDT simulations. This would involve addressing how the particle interaction models, which are currently tailored for fluid behavior, could be modified to capture the distinct characteristics of these other systems. For instance, rigid body simulations often require constraints to enforce non-penetration and fixed distances between particles, while soft body simulations need to model elasticity and plasticity. A detailed discussion of these adaptations would greatly enhance the paper's generality and appeal.

Furthermore, the paper needs a more detailed analysis of the computational complexity and runtime performance of the proposed method. The current description lacks sufficient information for the reader to understand the practical implications of using this approach. The authors should provide a breakdown of the computational cost associated with each stage of their pipeline, including the pre-training, inference, and transfer phases. This analysis should consider the number of particles, the dimensionality of the latent space, and the number of iterations required for convergence. Additionally, a comparison of the runtime with existing particle-based simulation methods would be valuable. This would allow the reader to assess the trade-offs between accuracy and computational efficiency. The authors should also discuss the memory requirements of their method, which is crucial for large-scale simulations.

Finally, the claims of probabilistic modeling and latent intuitive physics need further clarification. The authors should explicitly define the probability distributions used in their model and explain how these distributions are learned and utilized. For example, what is the prior distribution over the latent variables, and how is the posterior distribution inferred from the visual data? The paper should also clarify how the learned latent space captures intuitive physical properties. What specific physical quantities or relationships are encoded in the latent space, and how does the model ensure that these representations are physically meaningful? A more detailed explanation of these aspects would strengthen the paper's claims and make the method more transparent and understandable.

### Questions

Please see the weakness.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
