### Summary

This paper proposes SpecDec++, an adaptive version of speculative decoding that dynamically adjusts the candidate length K based on the probability of rejection. SpecDec++ formulates the choice of candidate length as a Markov Decision Process (MDP) and proves that the optimal policy is a threshold policy, where the speculation should stop when the probability of at least one rejected token exceeds a threshold. To implement this policy, the authors train an acceptance prediction head on top of the draft model that predicts the conditional probability of each token being accepted by the target model. The experimental results show that SpecDec++ outperforms the baseline method in terms of speedup and accuracy.

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

The paper introduces an interesting adaptive approach to speculative decoding, but several aspects could be strengthened to enhance its practical applicability and generalizability. First, the authors should provide a more detailed analysis of the computational overhead introduced by training the acceptance prediction head. This should include a breakdown of the training time for the head itself, as well as the additional training time required for the draft model. Furthermore, the authors should investigate how the size of the acceptance prediction head impacts the overall training cost and performance. It would be beneficial to explore techniques to reduce the training cost, such as using a smaller acceptance prediction head or employing more efficient training algorithms. This would make the proposed method more practical for real-world applications where computational resources may be limited.

Second, the experimental evaluation should be expanded to include a wider range of datasets and tasks. The current evaluation is limited to a few datasets, which may not be representative of all possible use cases. The authors should include results on datasets with varying sequence lengths, vocabulary sizes, and model architectures. For example, it would be valuable to see how the proposed method performs on tasks with longer sequences, such as those found in code generation or text summarization. Additionally, the authors should explore the performance of the proposed method on different model architectures, such as transformer-based models and recurrent neural networks. This would provide a more comprehensive evaluation of the proposed method's generalizability and robustness. The authors should also consider evaluating the method on tasks with different levels of difficulty to better understand its limitations.

Finally, the authors should provide a more detailed analysis of the trade-offs between speedup and accuracy. While the proposed method achieves a speedup, it is important to understand how this speedup affects the overall performance of the model. The authors should investigate the relationship between the threshold for the acceptance prediction head and the resulting speedup and accuracy. This analysis should include a study of the sensitivity of the proposed method to the accuracy of the acceptance prediction head. It would be beneficial to explore how the performance of the proposed method changes when the acceptance prediction head is trained with different amounts of data or with different training objectives. This would help to identify potential areas for improvement and provide a more complete understanding of the proposed method's behavior.

### Questions

1. How does the proposed method compare to other adaptive speculative decoding methods, such as Kangaroo and Medusa? The authors should provide a more detailed comparison with these methods in terms of both performance and computational cost.
2. How does the proposed method perform on other datasets and tasks? The authors should provide more experimental results on a wider range of datasets and tasks to demonstrate the generalizability of the proposed method.

### Rating

6

### Confidence

4

**********
