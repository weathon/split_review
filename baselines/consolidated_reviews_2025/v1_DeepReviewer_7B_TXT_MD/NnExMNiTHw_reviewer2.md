### Summary

This paper proposes SpecDec++, an adaptive version of speculative decoding that dynamically adjusts the candidate length K based on the probability of rejection. SpecDec++ formulates the choice of candidate length as a Markov Decision Process (MDP) and proves that the optimal policy is a threshold policy, where the speculation should stop when the probability of at least one rejected token exceeds a threshold. To implement this policy, the authors train an acceptance prediction head on top of the draft model that predicts the conditional probability of each token being accepted by the target model. The authors also use a weighted binary cross-entropy loss to train the prediction head. Experimental results show that SpecDec++ outperforms the baseline method in terms of speedup and accuracy.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow. The authors clearly explain the background of speculative decoding and the motivation of the proposed method. The theoretical analysis is also well-presented and easy to understand.

2. The proposed method is novel and theoretically sound. The authors formulate the choice of candidate length as a Markov Decision Process (MDP) and prove that the optimal policy is a threshold policy. This provides a principled way to adaptively adjust the candidate length based on the probability of rejection.

3. The proposed method is technically sound and can be easily implemented by training an acceptance prediction head on top of the draft model. The authors also use a weighted binary cross-entropy loss to train the prediction head, which is a simple and effective approach.

4. The experimental results show that SpecDec++ outperforms the baseline method in terms of speedup and accuracy. The authors also show that SpecDec++ can be seamlessly integrated with other speculative decoding methods.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method requires training an additional acceptance prediction head on top of the draft model. This may increase the training cost and make the method less practical. The authors do not provide a detailed analysis of the training cost, such as the training time and the computational resources required. Specifically, the paper lacks a breakdown of the training time for the acceptance prediction head versus the base draft model, and how this scales with model size. Furthermore, the computational resources (e.g., GPU hours, memory usage) should be reported to provide a more complete picture of the training overhead.

2. The experimental results only show the speedup of the proposed method on a few datasets. It is unclear whether the proposed method can generalize to other datasets and tasks. The authors should provide more experimental results on a wider range of datasets and tasks to demonstrate the generalizability of the proposed method. For example, the paper should include results on datasets with different characteristics, such as varying sequence lengths, vocabulary sizes, and model architectures. This would provide a more comprehensive evaluation of the proposed method's performance.

### Suggestions

The authors should provide a more detailed analysis of the training cost associated with the proposed method. This should include a breakdown of the training time for the acceptance prediction head, as well as a comparison of the training cost with other speculative decoding methods. The analysis should also consider the computational resources required for training, such as GPU hours and memory usage. Furthermore, it would be beneficial to explore techniques to reduce the training cost, such as using a smaller acceptance prediction head or employing more efficient training algorithms. This would make the proposed method more practical and accessible to a wider range of users.

To address the concern about the generalizability of the proposed method, the authors should provide more experimental results on a wider range of datasets and tasks. This should include datasets with different characteristics, such as varying sequence lengths, vocabulary sizes, and model architectures. For example, the paper could include results on datasets with longer sequences, such as those found in code generation or text summarization, as well as datasets with smaller vocabulary sizes, such as those found in low-resource languages. Additionally, the authors should explore the performance of the proposed method on different model architectures, such as transformer-based models and recurrent neural networks. This would provide a more comprehensive evaluation of the proposed method's performance and demonstrate its robustness across different scenarios.

Finally, the authors should investigate the sensitivity of the proposed method to the accuracy of the acceptance prediction head. This would help to understand the robustness of the method and its potential limitations. For example, the authors could explore how the performance of the proposed method changes when the acceptance prediction head is trained with different amounts of data or with different training objectives. This analysis would provide valuable insights into the behavior of the proposed method and help to identify potential areas for improvement.

### Questions

1. How does the proposed method compare to other adaptive speculative decoding methods, such as Kangaroo and Medusa? The authors should provide a more detailed comparison with these methods in terms of both performance and computational cost.

2. How does the proposed method perform on other datasets and tasks? The authors should provide more experimental results on a wider range of datasets and tasks to demonstrate the generalizability of the proposed method.

### Rating

6

### Confidence

4

**********
