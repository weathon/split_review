### Summary

This paper proposes a method for fluid simulation based on a single video. The method first pre-trains a neural network on a dataset of particle-based fluid simulations. Then, it uses this network to estimate the posterior distribution of the latent fluid properties from the input video. Finally, it uses these estimated properties to simulate the fluid in novel scenes. The paper demonstrates the effectiveness of the proposed method through experiments on synthetic datasets and real-world experiments.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well-written and easy to follow.
- The proposed method is novel and interesting.
- The paper provides a thorough evaluation of the proposed method, including quantitative and qualitative results on synthetic and real-world datasets.
- The paper also discusses the limitations of the proposed method and potential directions for future work.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a detailed analysis of the computational cost of the proposed method. It would be helpful to understand how the computational cost scales with the number of particles, the resolution of the input video, and the complexity of the fluid simulation.
- The paper does not compare the proposed method with other state-of-the-art methods for fluid simulation. It would be helpful to see how the proposed method performs compared to other methods in terms of accuracy, efficiency, and generalization ability.
- The paper does not provide a detailed discussion of the limitations of the proposed method. It would be helpful to understand the scenarios where the proposed method may fail or perform poorly.

### Suggestions

The paper would benefit from a more thorough analysis of the computational complexity of the proposed method. Specifically, the authors should provide a breakdown of the time and memory requirements for each stage of the pipeline, including the pre-training, inference, and simulation phases. This analysis should consider how these costs scale with the number of particles, the resolution of the input video, and the complexity of the fluid simulation. For example, it would be useful to know how the training time and memory usage change as the number of particles in the simulation increases, or how the inference time scales with the resolution of the input video. This analysis would help readers understand the practical limitations of the method and identify potential bottlenecks for future optimization efforts. Furthermore, it would be beneficial to compare the computational cost of the proposed method with other relevant methods in the literature, providing a clear understanding of its efficiency relative to existing approaches.

In addition to the computational analysis, the paper should include a more comprehensive comparison with existing state-of-the-art methods for fluid simulation. The authors should not only compare the accuracy of the proposed method with other methods, but also consider other important factors such as the ability to generalize to unseen scenarios, the robustness to noise and perturbations, and the computational efficiency. For example, the authors could compare their method with other particle-based methods, as well as more traditional grid-based methods, to highlight the advantages and disadvantages of their approach. This comparison should be performed on a variety of datasets and scenarios to provide a more complete picture of the method's performance. Furthermore, the authors should discuss the limitations of the proposed method in more detail, including scenarios where it may fail or perform poorly. This discussion should be based on both theoretical considerations and empirical observations, and should provide guidance for future research directions.

Finally, the paper should provide a more detailed discussion of the limitations of the proposed method. This discussion should include both theoretical limitations, such as the assumptions made by the model and the potential for bias, and practical limitations, such as the sensitivity to hyperparameter settings and the computational cost. For example, the authors should discuss the limitations of using a single video as input, and how this might affect the accuracy and generalizability of the method. They should also discuss the limitations of the particle-based representation, and how this might affect the method's ability to simulate complex fluid phenomena. Furthermore, the authors should discuss the limitations of the training data, and how this might affect the method's ability to generalize to unseen scenarios. This discussion should be based on both theoretical considerations and empirical observations, and should provide guidance for future research directions.

### Questions

- How does the proposed method compare to other state-of-the-art methods for fluid simulation in terms of accuracy, efficiency, and generalization ability?
- What are the limitations of the proposed method, and how can these limitations be addressed in future work?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
