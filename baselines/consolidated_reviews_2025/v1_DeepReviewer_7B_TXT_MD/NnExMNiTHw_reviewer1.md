### Summary

This paper proposes a new method to improve speculative decoding. The key idea is to dynamically adjust the candidate length based on the probability that the candidate tokens will be rejected by the target model. The authors formulate the choice of candidate length as a Markov Decision Process and prove that the optimal policy is a threshold policy, which means that the model should stop the current speculation when the probability of at least one rejected token exceeds a certain threshold. The authors then propose to implement this idea by training an acceptance prediction head on top of the draft model, which predicts the conditional probability that a candidate token will be accepted by the target model. The experimental results show that the proposed method can achieve better speedup compared to the baseline method.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper proposes a novel idea to improve speculative decoding by dynamically adjusting the candidate length based on the probability of rejection. This idea is well-motivated and theoretically sound. The authors formulate the problem as a Markov Decision Process and prove that the optimal policy is a threshold policy. The proposed method is also technically sound, as it can be easily implemented by training an acceptance prediction head on top of the draft model.

2. The paper is well-written and easy to follow. The authors provide a clear explanation of the background of speculative decoding and the motivation of the proposed method. The theoretical analysis is also well-presented and easy to understand.

3. The experimental results show that the proposed method can achieve better speedup compared to the baseline method. The authors also show that the proposed method can be easily integrated with other speculative decoding methods.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method requires training an additional acceptance prediction head on top of the draft model. This may increase the training cost and make the method less practical. The authors do not provide a detailed analysis of the training cost, such as the training time and the computational resources required. The paper lacks a comparison of the training cost with other speculative decoding methods, which makes it difficult to assess the practicality of the proposed method. Specifically, the paper should include a breakdown of the training time for the acceptance prediction head versus the base draft model, and how this scales with model size. Furthermore, the computational resources (e.g., GPU hours, memory usage) should be reported to provide a more complete picture of the training overhead.

2. The experimental results only show the speedup of the proposed method on a few datasets. It is unclear whether the proposed method can generalize to other datasets and tasks. The authors should provide more experimental results on a wider range of datasets and tasks to demonstrate the generalizability of the proposed method. The current evaluation is limited to a few datasets, which may not be representative of all possible use cases. For example, the paper should include results on datasets with different characteristics, such as varying sequence lengths, vocabulary sizes, and model architectures. This would provide a more comprehensive evaluation of the proposed method's performance.

### Suggestions

The paper introduces an interesting approach to dynamic candidate length selection in speculative decoding, but there are several areas where the evaluation and analysis could be strengthened. First, the paper should provide a more detailed analysis of the training cost associated with the proposed method. This should include a breakdown of the training time for the acceptance prediction head, as well as a comparison of the training cost with other speculative decoding methods. The authors should also report the computational resources required for training, such as GPU hours and memory usage. This would allow readers to better assess the practicality of the proposed method and compare it with existing approaches. Furthermore, it would be beneficial to explore techniques to reduce the training cost, such as using a smaller acceptance prediction head or employing more efficient training algorithms.

Second, the experimental evaluation should be expanded to include a wider range of datasets and tasks. The current evaluation is limited to a few datasets, which may not be representative of all possible use cases. The authors should include results on datasets with different characteristics, such as varying sequence lengths, vocabulary sizes, and model architectures. This would provide a more comprehensive evaluation of the proposed method's performance and demonstrate its generalizability. For example, the paper could include results on datasets with longer sequences, such as those found in code generation or text summarization, as well as datasets with smaller vocabulary sizes, such as those found in low-resource languages. Additionally, the paper should explore the performance of the proposed method on different model architectures, such as transformer-based models and recurrent neural networks.

Finally, the paper should provide a more detailed analysis of the relationship between the threshold for the acceptance prediction head and the resulting speedup. The authors should explore how different threshold values affect the performance of the proposed method and provide guidelines for selecting an appropriate threshold. This analysis should include a study of the trade-off between speedup and accuracy, as well as a discussion of the factors that influence the optimal threshold value. Furthermore, the paper should investigate the sensitivity of the proposed method to the accuracy of the acceptance prediction head. This would help to understand the robustness of the method and its potential limitations.

### Questions

1. The authors claim that the proposed method can achieve better speedup compared to the baseline method. However, the proposed method requires training an additional acceptance prediction head, which may increase the training cost. Can the authors provide a detailed analysis of the training cost and compare it with other speculative decoding methods?

2. The experimental results only show the speedup of the proposed method on a few datasets. Can the authors provide more experimental results on a wider range of datasets and tasks to demonstrate the generalizability of the proposed method?

### Rating

6

### Confidence

3

**********
