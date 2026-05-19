### Summary

In this paper, the authors propose a new class of activation functions, elephant activation functions, that can generate both sparse representations and sparse gradients. They show that by simply replacing classical activation functions with elephant activation functions, we can significantly improve the resilience of neural networks to catastrophic forgetting.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The proposed elephant activation functions can generate both sparse representations and sparse gradients, which can improve the resilience of neural networks to catastrophic forgetting.

2. The authors provide a theoretical analysis of the proposed method, which shows that the elephant activation functions can satisfy the properties required for continual learning.

3. The authors conduct experiments on various tasks, including streaming learning for regression, class incremental learning, and reinforcement learning, and show that the proposed method outperforms the baselines.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed elephant activation functions have not been tested on large-scale datasets, such as ImageNet. It is unclear how the proposed method would perform on more complex tasks with a larger number of classes and more diverse data.

2. The proposed method is based on the analysis of the training dynamics of neural networks, which may not be applicable to all types of neural networks and tasks. For example, the analysis is based on a simple regression task and it is not clear if the same analysis would hold for more complex tasks.

3. The proposed method requires the selection of two parameters, a and d, which control the width and slope of the elephant function. The authors do not provide a clear guideline on how to choose these parameters, and the sensitivity of the method to these parameters is not fully explored. While some experiments are conducted, a more systematic analysis of the impact of these parameters on performance across different tasks is needed.

### Suggestions

The authors should conduct experiments on larger, more complex datasets such as ImageNet to demonstrate the scalability and generalizability of the proposed elephant activation functions. This would involve training models on ImageNet with and without the elephant activation functions and comparing the performance in terms of accuracy and catastrophic forgetting. Furthermore, it would be beneficial to analyze the computational cost of using the elephant activation functions compared to standard activation functions, especially when dealing with large-scale datasets. This analysis should include the time and memory requirements for both training and inference. The authors should also investigate the performance of the proposed method on a wider range of tasks, including those with more complex data distributions and task structures. This would help to establish the robustness of the method and its applicability to different problem domains.

To address the concern about the applicability of the training dynamics analysis, the authors should provide a more detailed explanation of how the analysis extends to more complex neural network architectures and tasks. This could involve providing theoretical arguments or empirical evidence that the key properties of the elephant activation functions, such as their ability to generate sparse representations and gradients, are preserved in more complex settings. It would also be helpful to explore the limitations of the analysis and identify the types of tasks and architectures where the analysis may not be applicable. The authors should also consider comparing their method with other continual learning methods that are based on different principles, such as regularization-based methods or replay-based methods, to provide a more comprehensive evaluation of the proposed approach.

Finally, the authors should provide a more systematic approach for selecting the parameters a and d. This could involve conducting a sensitivity analysis to determine the optimal range of values for these parameters across different tasks and datasets. The authors could also explore the use of adaptive methods for setting these parameters, such as using a validation set to tune the parameters during training. It would be beneficial to provide a clear guideline on how to choose these parameters based on the characteristics of the task and dataset. This would make the method more practical and easier to use for other researchers and practitioners.

### Questions

1. How does the proposed method perform on large-scale datasets, such as ImageNet?

2. How does the proposed method compare to other continual learning methods that are based on different principles, such as regularization-based methods or replay-based methods?

3. How sensitive is the proposed method to the selection of the parameters a and d? Are there any guidelines on how to choose these parameters for different tasks and datasets?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
