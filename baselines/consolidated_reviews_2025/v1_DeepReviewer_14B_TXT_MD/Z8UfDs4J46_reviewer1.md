### Summary

This paper proposes a new framework for dealing with delayed rewards in deep reinforcement learning. The authors start by formalizing the delayed-observation MDP and then discuss the challenges of using traditional DRL methods in this setting. They then propose several strategies for overcoming these challenges, including delay-reconciled training for critics, state augmentation for actors, and complementary techniques such as prediction and encoding.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

- The paper is well-written and easy to follow.
- The proposed framework is simple and general, and can be applied to a variety of DRL algorithms.
- The authors provide a theoretical analysis of their methods, showing that they are guaranteed to converge under certain conditions.

### Weaknesses

#### Some Related Works


#### comment

 - The proposed framework is only evaluated on simulated robotic control tasks, which may not be representative of real-world environments.
- The authors do not discuss the limitations of their work in detail, nor do they suggest directions for future research.
- The proposed method is not compared to other state-of-the-art DRL algorithms that are designed to handle delayed rewards, such as the method proposed by Chen et al. (2021).

### Suggestions

The paper's evaluation is limited to simulated robotic control tasks, which raises concerns about the generalizability of the proposed framework. While these simulations provide a controlled environment for experimentation, they often fail to capture the complexities and nuances of real-world scenarios. For instance, real-world robotic systems must deal with issues such as sensor noise, actuator inaccuracies, and unpredictable environmental conditions, which are not fully represented in simulation. To strengthen the paper, the authors should consider evaluating their method on more diverse and challenging tasks, potentially including real-world experiments or more complex simulated environments that incorporate these real-world factors. This would provide a more robust assessment of the framework's performance and its potential for practical application.

Furthermore, the paper lacks a detailed discussion of the limitations of the proposed approach. While the authors mention that their method is designed for continuous control tasks, they do not elaborate on the specific challenges that might arise when applying it to other types of problems, such as those with high-dimensional state spaces or discrete action spaces. Additionally, the paper does not address the computational cost of the proposed methods, which could be a limiting factor in real-world applications. A more thorough discussion of these limitations would provide a more balanced view of the framework's capabilities and its potential for future development. The authors should also consider discussing the sensitivity of their method to hyperparameter settings and the potential for instability during training, as these are critical factors for practical implementation.

Finally, the paper would benefit from a more comprehensive comparison to existing state-of-the-art DRL algorithms that are designed to handle delayed rewards. While the authors mention the work of Chen et al. (2021), they do not provide a direct comparison to their method. This makes it difficult to assess the relative performance of the proposed framework and its potential advantages over existing approaches. A more thorough comparison, including a discussion of the strengths and weaknesses of each method, would provide a more complete picture of the current state of the art and the contribution of this work. The authors should also consider comparing their method to other relevant approaches, such as those based on recurrent neural networks or attention mechanisms, which have been shown to be effective in handling delayed rewards in other contexts.

### Questions

- How does the proposed framework compare to other state-of-the-art DRL algorithms that are designed to handle delayed rewards, such as the method proposed by Chen et al. (2021)?
- What are the limitations of the proposed framework, and what are the potential directions for future research?

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
