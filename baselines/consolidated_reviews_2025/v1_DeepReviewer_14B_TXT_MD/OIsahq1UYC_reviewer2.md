### Summary

This paper proposes a method for sampling from intractable densities by combining diffusion models with ideas from GFlowNets. The main idea is to introduce an additional neural network that learns to predict the unnormalized target density at any intermediate diffusion time. This allows the model to be trained with shorter trajectories and to receive learning signals at intermediate steps. The authors demonstrate that this approach leads to lower gradient variance and better performance on several benchmark sampling tasks.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well-written and easy to follow.
- The proposed method is a novel and well-motivated combination of diffusion models and GFlowNets.
- The experiments are thorough and demonstrate the effectiveness of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

 - The method introduces additional complexity compared to standard diffusion models, which may make it harder to implement and train.
- The experiments are limited to relatively low-dimensional settings. It would be interesting to see how the method scales to higher dimensions.

### Suggestions

The paper introduces an interesting approach by combining diffusion models with GFlowNets, but there are several areas where the methodology and evaluation could be strengthened. First, while the introduction of an additional neural network to predict the unnormalized target density at intermediate diffusion times is a novel idea, the paper does not provide sufficient detail on the architecture and training of this network. Specifically, what is the network architecture used? How is it trained in conjunction with the diffusion model? What is the computational overhead of training this additional network? Providing these details would help assess the practical feasibility of the method. Furthermore, the paper should explore the sensitivity of the method to the choice of this network's architecture and hyperparameters. A more thorough analysis of these aspects would be beneficial.

Second, the paper claims that the method leads to lower gradient variance, but this claim is not sufficiently supported by the experiments. While Figure 2 shows a reduction in gradient variance, it is not clear how this reduction translates into improved sampling performance. The paper should provide a more detailed analysis of the relationship between gradient variance and sampling quality. For example, it would be helpful to show how the reduced gradient variance affects the convergence rate of the sampling process. Additionally, the paper should compare the gradient variance of the proposed method with other relevant baselines, such as standard diffusion models with different training objectives. This would provide a more comprehensive understanding of the benefits of the proposed approach.

Finally, the experimental evaluation is limited to relatively low-dimensional settings. While the authors acknowledge this limitation, it is crucial to evaluate the method on higher-dimensional problems to assess its scalability. The paper should include experiments on higher-dimensional benchmark tasks, such as those used in the original Path Integral Sampler paper. This would provide a more realistic assessment of the method's performance in practical settings. Furthermore, the paper should analyze the computational cost of the method as the dimensionality of the problem increases. This would help determine the practical limitations of the proposed approach and identify potential areas for future research.

### Questions

- How does the performance of the method compare to other approaches for sampling from intractable densities, such as normalizing flows and Markov chain Monte Carlo methods?
- How does the method perform in higher-dimensional settings?
- How does the choice of the reference process affect the performance of the method?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
