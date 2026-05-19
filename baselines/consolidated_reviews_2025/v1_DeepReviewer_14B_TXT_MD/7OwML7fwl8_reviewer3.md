### Summary

The paper proposes a new framework for improving fairness in machine learning models without the use of sensitive attributes. The authors introduce a confidence-based hierarchical structure of variational autoencoder (VAE) architectures called "Reckoner". The framework utilizes learnable noise and a knowledge-sharing mechanism between a dual-model system to achieve improved fairness while maintaining accurate predictions. The paper presents experimental results on real-world datasets, demonstrating the effectiveness of the proposed framework compared to state-of-the-art baselines in terms of both accuracy and fairness metrics.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper addresses an important and timely issue in machine learning, which is improving fairness without relying on sensitive attributes. This is particularly relevant in light of increasing concerns about data privacy and regulatory restrictions on the use of sensitive information.

2. The authors provide a comprehensive analysis of the distribution of non-sensitive attributes across demographic groups at different model confidence levels. This analysis sheds light on the relationship between predictability and fairness and provides valuable insights into how non-sensitive features can impact model predictions.

3. The proposed framework, Reckoner, is a novel and innovative approach to achieving fairness without sensitive attributes. The use of learnable noise and a dual-model system with knowledge-sharing is a creative solution to the problem.

4. The experimental results demonstrate the effectiveness of the proposed framework on real-world datasets. The framework consistently outperforms state-of-the-art baselines in terms of both accuracy and fairness metrics, showcasing its practical utility.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could benefit from a more detailed explanation of the proposed framework, particularly the interaction between the two generators and the role of learnable noise. It is unclear how the knowledge-sharing mechanism works in practice and how it contributes to improved fairness. Specifically, the paper lacks a clear description of how the pseudo-learning process is implemented, and how the parameters of the Low-Conf generator are updated and then transferred to the High-Conf generator. The description of the learnable noise is also vague; it's not clear how the noise is parameterized, optimized, and how it ensures that the model focuses on essential features rather than biased ones. A more detailed explanation of the loss function and the optimization process is needed to fully understand the framework's mechanics.

2. The paper does not provide a thorough analysis of the limitations of the proposed framework. It would be beneficial to discuss potential scenarios where the framework may not be effective or may even exacerbate existing biases. For example, the paper does not address the potential for the framework to fail if the low-confidence samples are not representative of the entire dataset, or if the noise injection inadvertently removes crucial information needed for accurate predictions. Furthermore, the paper does not discuss the computational cost of the proposed method, especially the training of two VAEs and the additional overhead of the noise wrapper.

3. The paper could benefit from a more comprehensive comparison with existing methods for improving fairness without sensitive attributes. While the paper compares the proposed framework with several baselines, it would be helpful to include a more detailed discussion of the strengths and weaknesses of each method and how the proposed framework addresses the limitations of existing approaches. The comparison should also include a discussion of the computational complexity and scalability of the proposed method compared to other methods. A more in-depth analysis of the performance of the proposed method across different datasets and fairness metrics is also needed.

### Suggestions

To address the lack of clarity regarding the framework's mechanics, the authors should provide a more detailed explanation of the pseudo-learning process, including the specific loss functions used for training both the Low-Conf and High-Conf generators. The explanation should clarify how the parameters of the Low-Conf generator are updated and then transferred to the High-Conf generator. A step-by-step walkthrough of the training process, including the role of the learnable noise, would greatly enhance the reader's understanding. The authors should also provide a more detailed explanation of how the noise is parameterized and optimized, and how it ensures that the model focuses on essential features rather than biased ones. This could include a visualization of the noise distribution and its impact on the input data. Furthermore, the authors should include a more detailed description of the loss function and the optimization process, including the specific optimization algorithms used and the hyperparameter settings.

To address the limitations of the proposed framework, the authors should include a more thorough discussion of potential failure scenarios. For example, the paper should discuss the potential for the framework to fail if the low-confidence samples are not representative of the entire dataset, or if the noise injection inadvertently removes crucial information needed for accurate predictions. The authors should also discuss the computational cost of the proposed method, especially the training of two VAEs and the additional overhead of the noise wrapper. This discussion should include an analysis of the time and memory requirements of the proposed method, and how it compares to other methods. The authors should also explore the sensitivity of the framework to different hyperparameter settings, and provide guidance on how to choose appropriate values for these parameters. The authors should also consider the potential for the framework to exacerbate existing biases in the data, and provide strategies for mitigating this risk.

To improve the comparison with existing methods, the authors should include a more detailed discussion of the strengths and weaknesses of each baseline method, and how the proposed framework addresses the limitations of existing approaches. The comparison should also include a discussion of the computational complexity and scalability of the proposed method compared to other methods. The authors should also provide a more in-depth analysis of the performance of the proposed method across different datasets and fairness metrics. This analysis should include a discussion of the trade-offs between accuracy and fairness, and how the proposed method balances these two objectives. The authors should also consider including a comparison with other methods that use VAEs for fairness, to better contextualize the novelty of their approach.

### Questions

1. How does the proposed framework handle scenarios where the low-confidence samples are not representative of the entire dataset? Is there a risk of introducing new biases through the knowledge-sharing mechanism?

2. What are the computational costs associated with the proposed framework, particularly the training of two VAEs and the additional overhead of the noise wrapper? How does it compare to the computational costs of existing methods?

3. How sensitive is the framework to the choice of hyperparameters, such as the confidence threshold and the parameters of the learnable noise? Are there any guidelines for selecting appropriate values for these parameters?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
