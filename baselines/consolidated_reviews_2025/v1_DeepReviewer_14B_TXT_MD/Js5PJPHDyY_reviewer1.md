### Summary

This paper introduces a simple method for training-free CLIP-based adaptation. Specifically, they re visite the classical algorithm, Gaussian Discriminant Analysis (GDA), to perform downstream classification of CLIP. The knowledge from both visual and textual modalities is integrated by ensembling it with the original zero-shot classifier within CLIP. Extensive results on 17 datasets validate the effectiveness of the proposed method.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The proposed method is simple and effective, which revisits a classical algorithm, Gaussian Discriminant Analysis (GDA), for training-free CLIP-based adaptation.

- The proposed method achieves comparable results with state-of-the-art methods on few-shot classification, imbalanced learning, and out-of-distribution generalization without additional training time and computational resources.

### Weaknesses

#### Some Related Works


#### comment

 - The proposed method seems too simple, which just employs the classical GDA algorithm for downstream classification of CLIP. Moreover, the idea of combining the knowledge from both visual and textual modalities by ensembling it with the original zero-shot classifier within CLIP has been widely adopted by previous methods.

- The proposed method does not show its superiority in base-to-new generalization and unsupervised learning. For base-to-new generalization, the method proposes using the K-Nearest-Neighbor algorithm to synthesize data for new classes, which is also widely adopted by previous methods. For unsupervised learning, the method employs the EM algorithm to estimate its mean and covariance, which is also not novel.

- The proposed method seems not suitable for few-shot classification, as it requires estimating the covariance matrix, which is hard to estimate precisely in high-dimensional space with few training samples. Specifically, the use of shrinkage estimation, while common, does not fundamentally address the core issue of high dimensionality relative to sample size, potentially leading to unstable or biased covariance estimates, particularly in very low-shot scenarios (e.g., 1 or 2 shots). The paper does not provide a detailed analysis of how the performance of covariance estimation degrades with decreasing sample sizes, nor does it explore alternative regularization techniques that might be more robust in such extreme cases.

### Suggestions

The paper should provide a more thorough analysis of the limitations of Gaussian Discriminant Analysis (GDA) in the context of few-shot learning, especially concerning the estimation of the covariance matrix. While the authors mention using shrinkage estimation, they should delve deeper into the practical implications of this approach when the number of samples is extremely low compared to the feature dimension. For instance, a study of the condition number of the estimated covariance matrices across different shot settings could provide valuable insights into the stability of the method. Furthermore, the authors could explore alternative regularization techniques, such as adding a small constant to the diagonal of the covariance matrix or using a low-rank approximation, and compare their performance with the proposed shrinkage method. This would strengthen the paper by demonstrating a more comprehensive understanding of the challenges associated with covariance estimation in few-shot scenarios.

To address the concern about the simplicity of the proposed method, the authors should provide a more detailed comparison with existing methods that also employ ensembling techniques. Specifically, they should analyze the differences in the ensembling strategies and the specific contributions of their approach. For example, do they use a different weighting scheme for the visual and textual modalities? Do they use a different method for combining the predictions of the zero-shot classifier and the GDA classifier? A more detailed analysis of these aspects would help to clarify the novelty and contribution of the proposed method. Furthermore, the authors should consider exploring more sophisticated ensembling techniques, such as stacking or boosting, to see if they can further improve the performance of their method. This would demonstrate a more thorough exploration of the potential of ensembling techniques for CLIP-based adaptation.

Finally, the paper should provide a more detailed analysis of the performance of the proposed method in base-to-new generalization and unsupervised learning. While the authors mention that their method achieves comparable results with previous methods, they should provide a more detailed comparison with specific state-of-the-art methods in these areas. For example, in base-to-new generalization, they should compare their method with methods that explicitly model the relationship between base and new classes. In unsupervised learning, they should compare their method with methods that use more sophisticated clustering or density estimation techniques. This would help to clarify the strengths and weaknesses of the proposed method in these areas and provide a more comprehensive evaluation of its performance.

### Questions

See the weaknesses above.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
