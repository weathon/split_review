### Summary

This paper introduces a novel method for robust fine-tuning (RFT) of pre-trained feature extractors (FEs) to enhance adversarial robustness in downstream tasks. The authors identify a critical issue in existing RFT methods: divergent gradient directions when optimizing both natural and adversarial objectives through the FE, leading to unstable optimization and sensitivity to hyperparameters. To address this, they propose AutoLoRa, a framework that disentangles the optimization process by introducing a low-rank (LoRa) branch. This branch optimizes natural objectives while the FE optimizes adversarial objectives. The authors also introduce heuristic strategies for automating the scheduling of learning rates and scalars, eliminating the need for manual hyperparameter tuning. Experimental results demonstrate that AutoLoRa achieves state-of-the-art robustness performance without requiring hyperparameter tuning.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow, with clear explanations of the motivation, methodology, and experimental results.
2. The proposed AutoLoRa framework addresses a significant issue in robust fine-tuning by disentangling the optimization of natural and adversarial objectives, leading to improved adversarial robustness and reduced sensitivity to hyperparameters.
3. The introduction of a low-rank (LoRa) branch is a novel approach to optimizing natural objectives while maintaining the FE's ability to handle adversarial objectives. This disentanglement strategy is an innovative contribution to the field of robust fine-tuning.
4. The paper provides a comprehensive experimental evaluation, demonstrating the effectiveness of AutoLoRa across various downstream tasks and pre-trained models. The results show that AutoLoRa achieves state-of-the-art robustness performance without requiring manual hyperparameter tuning, which is a significant advantage in practical applications.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed discussion of the limitations of the proposed method. While the authors demonstrate the effectiveness of AutoLoRa in various downstream tasks, they do not address potential scenarios where the method might not perform optimally. For example, it would be beneficial to discuss the sensitivity of AutoLoRa to different types of adversarial attacks, or the potential impact of the low-rank branch on the generalization performance of the model. Specifically, the paper should explore how the choice of rank for the LoRa branch affects the trade-off between robustness and standard accuracy, and whether there are specific scenarios where a fixed rank might not be sufficient. Furthermore, the paper should discuss the potential for the method to be less effective against adaptive attacks that are specifically designed to circumvent the disentanglement strategy.
2. The paper does not provide a thorough comparison with other state-of-the-art methods for robust fine-tuning. While the authors compare AutoLoRa with vanilla RFT and TWINS, they do not discuss how AutoLoRa compares to other recent approaches that also aim to improve robustness in downstream tasks. A more comprehensive comparison would help to contextualize the contributions of AutoLoRa and highlight its advantages and disadvantages compared to existing methods. For instance, the paper should compare AutoLoRa with methods that use different regularization techniques or those that explicitly model the adversarial risk. It would also be beneficial to see a comparison with methods that use different types of feature extractors, such as those trained with different pre-training strategies.

### Suggestions

The authors should provide a more detailed analysis of the limitations of their proposed method. Specifically, they should investigate the sensitivity of AutoLoRa to different types of adversarial attacks, including those that are specifically designed to target the disentanglement strategy. For example, they could explore the performance of AutoLoRa against attacks that manipulate the gradients of the low-rank branch or the feature extractor in a coordinated manner. Furthermore, the authors should explore the impact of the rank of the LoRa branch on the trade-off between robustness and standard accuracy. They could conduct experiments with different ranks and analyze how this affects the model's performance on both clean and adversarial examples. It would also be beneficial to investigate whether there are specific scenarios where a fixed rank might not be sufficient, and if so, what strategies could be used to adapt the rank dynamically. This analysis should include a discussion of the computational cost associated with different ranks and how this might affect the practical applicability of the method.

To strengthen the paper, the authors should include a more comprehensive comparison with other state-of-the-art methods for robust fine-tuning. This comparison should not only focus on the performance of the methods on standard benchmarks but also on their ability to handle different types of adversarial attacks and their computational cost. The authors should compare AutoLoRa with methods that use different regularization techniques, such as adversarial training or robust optimization, and those that explicitly model the adversarial risk. They should also compare AutoLoRa with methods that use different types of feature extractors, such as those trained with different pre-training strategies. This comparison should include a discussion of the advantages and disadvantages of each method, and it should help to contextualize the contributions of AutoLoRa within the broader field of robust fine-tuning. The authors should also consider including a discussion of the limitations of their method in comparison to these other approaches.

Finally, the authors should provide a more detailed analysis of the computational cost of their method. While they mention that the low-rank branch is parameter-efficient, they should provide a more quantitative analysis of the computational overhead associated with the proposed approach. This analysis should include the training time, memory usage, and inference speed of AutoLoRa compared to other methods. The authors should also discuss the scalability of their method to larger datasets and models. This analysis should be conducted on a variety of downstream tasks and pre-trained models to provide a comprehensive understanding of the computational cost of AutoLoRa. The authors should also discuss the potential for optimizing the implementation of their method to reduce its computational cost.

### Questions

1. How does the proposed method perform on tasks with different levels of adversarial vulnerability? Are there specific types of tasks where AutoLoRa is particularly effective or less effective?
2. What is the computational overhead of the proposed method compared to existing robust fine-tuning techniques? How does the introduction of the low-rank branch affect the training time and memory usage?
3. How sensitive is the performance of AutoLoRa to the choice of hyperparameters, such as the rank of the LoRa branch and the learning rate schedule? Are there specific ranges of these hyperparameters that are more effective for different types of tasks?

### Rating

6

### Confidence

3

**********
