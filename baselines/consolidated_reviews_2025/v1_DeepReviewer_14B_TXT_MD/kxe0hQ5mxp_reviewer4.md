### Summary

The paper proposes a new activation function, the elephant activation function, which is designed to produce both sparse representations and sparse gradients. The authors demonstrate that using this activation function can improve the resilience of neural networks to catastrophic forgetting in continual learning scenarios. The method is tested on regression, class incremental learning, and reinforcement learning tasks, showing promising results, especially in scenarios without replay buffers or task boundary information.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper introduces a novel activation function that addresses a key challenge in continual learning: catastrophic forgetting. The theoretical analysis provides a solid foundation for the proposed method, and the empirical results demonstrate its effectiveness across different learning paradigms.

2. The experimental setup is comprehensive, covering a range of tasks and comparing the proposed method with several baselines. The results are convincing and show that the elephant activation function can lead to significant improvements in continual learning performance.

### Weaknesses

#### Some Related Works


#### comment

1. The paper primarily focuses on the theoretical analysis and empirical evaluation of the elephant activation function. However, it lacks a detailed discussion on the practical implications and potential limitations of using this activation function in real-world applications. For example, how does the computational cost of the elephant activation function compare to other activation functions? Are there any specific scenarios where the elephant activation function might not be the best choice?

2. The paper could benefit from a more in-depth analysis of the hyperparameter sensitivity of the proposed method. While the authors provide some insights into the effect of different parameter settings, a more systematic study of how these parameters affect the performance of the method would be valuable. For instance, how does the performance vary with different values of 'a' and 'd' in the elephant activation function? Are there optimal ranges for these parameters that consistently lead to better performance across different tasks?

3. The paper does not explore the potential of combining the elephant activation function with other continual learning techniques. It would be interesting to see how the proposed method interacts with other approaches, such as replay-based methods or regularization techniques. For example, could the elephant activation function be used in conjunction with experience replay to further improve performance? Or could it be combined with regularization methods to mitigate catastrophic forgetting even more effectively?

### Suggestions

The paper introduces a novel activation function, the elephant activation function, which aims to mitigate catastrophic forgetting in continual learning. While the theoretical analysis and empirical results are promising, further investigation into the practical aspects of this activation function is needed. Specifically, a detailed analysis of the computational overhead introduced by the elephant activation function compared to standard activation functions like ReLU or sigmoid would be beneficial. This analysis should consider both the forward and backward passes, as well as the memory footprint of the function. Furthermore, it would be valuable to explore the behavior of the elephant activation function in scenarios with limited computational resources, such as embedded systems or mobile devices. Understanding these practical limitations is crucial for assessing the real-world applicability of the proposed method. The authors should also investigate the sensitivity of the method to different initialization strategies for the parameters 'a' and 'd' of the elephant activation function. It is possible that specific initialization schemes could lead to faster convergence or better overall performance.

To further strengthen the paper, a more comprehensive analysis of the hyperparameter sensitivity of the proposed method is necessary. The authors should conduct a systematic study to explore how the parameters 'a' and 'd' affect the performance of the elephant activation function across different tasks and datasets. This study should include a range of values for these parameters and analyze the resulting performance curves. It would be particularly useful to identify optimal ranges for these parameters that consistently lead to better performance. Additionally, the authors should investigate the interaction between the parameters 'a' and 'd' and how they jointly influence the behavior of the activation function. This analysis could involve visualizing the activation function and its gradient for different parameter values, providing a deeper understanding of the function's properties. The authors should also consider using techniques like grid search or Bayesian optimization to find optimal parameter values for different tasks.

Finally, the paper should explore the potential of combining the elephant activation function with other continual learning techniques. The authors should investigate how the proposed method interacts with replay-based methods, such as experience replay or generative replay. It would be interesting to see if the elephant activation function can be used to enhance the performance of these methods by reducing the interference between tasks. Furthermore, the authors should explore the possibility of combining the elephant activation function with regularization techniques, such as elastic weight consolidation or synaptic intelligence. This could potentially lead to a more robust and effective approach to mitigating catastrophic forgetting. The authors should also consider the potential benefits of combining the elephant activation function with other architectural modifications, such as progressive neural networks or dynamically expandable networks. This could lead to a more comprehensive and versatile approach to continual learning.

### Questions

1. How does the computational cost of the elephant activation function compare to other activation functions? Are there any specific scenarios where the elephant activation function might not be the best choice?

2. How sensitive is the performance of the proposed method to the choice of hyperparameters? Are there any guidelines for selecting appropriate hyperparameter values for different tasks and datasets?

3. Can the elephant activation function be combined with other continual learning techniques, such as replay-based methods or regularization techniques, to further improve performance?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
