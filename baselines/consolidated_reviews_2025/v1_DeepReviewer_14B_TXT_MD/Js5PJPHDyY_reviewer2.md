### Summary

This paper proposes a training-free CLIP adaptation method based on Gaussian Discriminant Analysis (GDA). The method estimates the mean vectors and covariance matrices from the training dataset to construct the classifier, which is then ensembled with the CLIP's zero-shot classifier. The method is evaluated on 17 datasets and shows promising results in few-shot classification, imbalanced learning, and out-of-distribution generalization. The method is also extended to base-to-new generalization and unsupervised learning scenarios.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The proposed method is simple and effective, and does not require any additional training or optimization. It leverages the statistical information of the data to construct a classifier based on GDA, which is then ensembled with the CLIP's zero-shot classifier. This approach is novel and interesting, and shows good performance on various tasks.

2. The method is evaluated on a wide range of datasets and tasks, including few-shot classification, imbalanced learning, out-of-distribution generalization, base-to-new generalization, and unsupervised learning. The results demonstrate that the method is robust and versatile, and can outperform or match the state-of-the-art methods in most cases.

3. The paper is well-written and easy to follow. The authors provide clear explanations of the method, the experiments, and the results. The paper also includes ablation studies and analysis to support the claims and insights.

### Weaknesses

#### Some Related Works


#### comment

1. The method relies on the assumption that the features of each class follow Gaussian distributions with identical covariance. This assumption may not hold for some datasets or tasks, especially when the data is complex or heterogeneous. The paper does not provide any analysis or discussion on the validity of this assumption, or how it affects the performance of the method. It would be helpful to provide some examples or cases where the assumption is violated, and how the method behaves in such scenarios. Specifically, the identical covariance assumption is a strong limitation, and the paper should explore the impact of this assumption on datasets with high intra-class variance or when the feature distributions are significantly non-Gaussian. For example, datasets with fine-grained categories or those with strong intra-class variations due to pose, lighting, or background could violate this assumption, and it is unclear how the method would perform in such cases.

2. The method uses the K-Nearest-Neighbor algorithm to synthesize data for new classes in the base-to-new generalization scenario. This approach may not be very effective or efficient, especially when the new classes are very different from the base classes, or when the data is high-dimensional. The paper does not compare the proposed approach with other data synthesis methods, such as generative adversarial networks (GANs) or variational autoencoders (VAEs), which may be more powerful and flexible. Furthermore, the KNN approach relies on the feature space of the base classes, which may not be optimal for the new classes, potentially leading to suboptimal performance. The paper should explore alternative feature spaces or distance metrics for KNN to mitigate this issue.

3. The method employs the EM algorithm to estimate the mean and covariance of the unlabeled data in the unsupervised learning scenario. This approach may not be very robust or stable, especially when the data is noisy or has multiple modes. The paper does not provide any details on the initialization or convergence of the EM algorithm, or how it affects the performance of the method. It would be helpful to provide some analysis or comparison with other unsupervised learning methods, such as clustering or density estimation. Specifically, the EM algorithm is sensitive to initialization, and the paper should discuss how the initialization is performed and how it affects the final results. The paper should also explore the impact of the number of iterations on the convergence of the EM algorithm and the stability of the results.

### Suggestions

The paper should include a more thorough analysis of the Gaussian assumption, particularly the identical covariance assumption. It would be beneficial to include experiments on datasets that are known to violate this assumption, such as those with high intra-class variance or non-Gaussian distributions. The authors could consider using metrics like the Bhattacharyya coefficient or the Kullback-Leibler divergence to quantify the overlap between the class distributions, and then correlate these metrics with the performance of the proposed method. This would provide a more nuanced understanding of the limitations of the method and when it is most effective. Furthermore, the authors should explore alternative covariance structures, such as allowing for different covariances per class, or using a shared covariance matrix that is not necessarily spherical. This would make the method more robust to datasets where the identical covariance assumption does not hold.

For the base-to-new generalization, the authors should explore more sophisticated data synthesis techniques beyond KNN. While KNN is simple, it may not capture the underlying data distribution effectively, especially when the new classes are semantically distant from the base classes. The authors could consider using generative models like GANs or VAEs to synthesize more realistic samples for the new classes. Alternatively, they could explore feature augmentation techniques that can generate new feature representations for the new classes based on the base class features. This could involve techniques like feature interpolation or extrapolation in the embedding space. The authors should also investigate the impact of different distance metrics in the KNN algorithm, as the Euclidean distance may not be optimal for all feature spaces. Exploring metrics like cosine similarity or learned distance metrics could improve the quality of the synthesized data.

Regarding the unsupervised learning scenario, the authors should provide more details on the EM algorithm's implementation and performance. Specifically, they should discuss the initialization strategy for the EM algorithm and how it affects the final results. It would be helpful to show the convergence behavior of the EM algorithm and how the number of iterations impacts the stability of the results. The authors should also compare the performance of the EM algorithm with other unsupervised learning methods, such as clustering algorithms like k-means or hierarchical clustering. This would provide a better understanding of the strengths and weaknesses of the EM algorithm in this context. Furthermore, the authors could explore robust versions of the EM algorithm that are less sensitive to initialization and outliers, such as the Expectation-Maximization with M-estimation.

### Questions

1. How does the method perform on datasets that do not follow the Gaussian distribution assumption, or have different covariances for different classes?

2. How does the method compare with other data synthesis methods, such as GANs or VAEs, in the base-to-new generalization scenario?

3. How does the method compare with other unsupervised learning methods, such as clustering or density estimation, in the unsupervised learning scenario?

4. How does the method scale to larger datasets or more complex tasks? What are the computational and memory requirements of the method?

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
