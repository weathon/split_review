### Summary

This paper studies the generalization of preference optimization (PO) under noisy feedback, i.e., the preference between two samples is incorrectly labeled with some probability. The authors propose a theoretical guarantee for the generalization risk of GPO under noisy feedback. The generalization risk increases as the noise level increases. The authors also validate this on simulated data and a real-world dataset.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The theoretical results are well-supported by experiments.
3. The authors conduct experiments on simulated data and a real-world dataset, which provides a comprehensive evaluation of the theoretical results.

### Weaknesses

#### Some Related Works


#### comment

1. The proof is based on the assumption that the feature vectors of the positive and negative classes follow a vMF distribution. This is a very strong assumption, and the authors should provide more justification for this assumption. Specifically, while the vMF distribution is unimodal and could represent clustered embeddings, real-world data, especially in NLP, often exhibits more complex structures. The assumption that all data points are concentrated around a single mean direction, even with varying concentration parameters, might be too restrictive. It's unclear how the theory would extend to scenarios with multi-modal preference distributions, which could arise from diverse user preferences or different types of desired outputs.
2. The theoretical results show that the generalization risk increases as the noise level increases. However, the preference optimization methods can sometimes achieve better performance than the supervised method. This seems contradictory to the theoretical results. The theory focuses on generalization risk, which is the expected performance on unseen data, while the empirical success of PO might be due to overfitting on the training data. The theory does not explicitly address the optimization dynamics that could lead to better performance in practice, especially when the model is trained to directly optimize the preference objective.

### Suggestions

The paper makes a valuable contribution by providing a theoretical analysis of preference optimization under noisy feedback. However, the strong assumptions made about the data distribution limit the applicability of the theory. To address this, future work could explore relaxations of the vMF distribution assumption. For instance, one could consider a mixture of vMF distributions to model multi-modal preference patterns. This would require a more complex analysis but would significantly enhance the practical relevance of the theory. Furthermore, it would be beneficial to investigate how the theoretical bounds change under different distributional assumptions and whether the qualitative results, such as the increase in risk with noise level, still hold. It would also be useful to explore the impact of the dimensionality of the feature space on the tightness of the bounds, as high-dimensional spaces are common in practice.

To bridge the gap between theory and practice, it would be beneficial to analyze the optimization dynamics of preference optimization methods under noisy feedback. The current theory focuses on the generalization risk but does not explicitly model the training process. Understanding how the model parameters evolve during training and how this evolution is affected by noise could provide insights into why preference optimization methods sometimes outperform supervised learning. This could involve analyzing the gradient flow of the preference loss function and how it interacts with the noise distribution. Additionally, it would be valuable to investigate the role of regularization techniques in mitigating the effects of noise and improving generalization. The current theoretical framework could be extended to incorporate regularization terms and analyze their impact on the generalization bounds.

Finally, while the experiments on simulated data validate the theoretical results, it would be beneficial to conduct more extensive experiments on real-world datasets with varying levels of noise. This could involve creating synthetic noise in existing datasets or using datasets with known annotation errors. The experiments should also explore the impact of different noise models, as the current theory assumes uniform noise. Furthermore, it would be useful to compare the performance of different preference optimization methods under noisy feedback and analyze how their performance relates to the theoretical bounds. This would provide a more comprehensive understanding of the practical implications of the theoretical results and guide the development of more robust preference optimization algorithms.

### Questions

1. Can the authors explain more about the vMF distribution assumption? Is this assumption realistic for real-world data?
2. Can the authors explain more about the apparent contradiction between the theoretical results and the empirical success of preference optimization methods over supervised learning?

### Rating

6

### Confidence

3

**********
