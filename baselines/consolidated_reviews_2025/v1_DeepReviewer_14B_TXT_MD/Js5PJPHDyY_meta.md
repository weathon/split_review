# Js5PJPHDyY — Meta Review

- Model: DeepReviewer 14B
- Decision: Reject
- Rating: 5.75
- Soundness: 3.0
- Presentation: 3.0
- Contribution: 2.75

## Summary

In this paper, I explore a training-free CLIP adaptation method that leverages Gaussian Discriminant Analysis (GDA) to construct a classifier from the statistical properties of the training data, which is then ensembled with CLIP's zero-shot classifier. The method is evaluated on 17 datasets, demonstrating promising results in few-shot classification, imbalanced learning, and out-of-distribution generalization. Additionally, the paper extends the method to base-to-new generalization and unsupervised learning scenarios, showing comparable performance to state-of-the-art methods. The core contributions of this work include the novel application of GDA for training-free adaptation and the integration of visual and textual modalities through ensembling. However, the method's reliance on strong assumptions, such as Gaussian distributions with identical covariance, and the use of common techniques like KNN and EM, raise concerns about its robustness and novelty. Despite these limitations, the paper is well-written, provides clear explanations, and includes ablation studies to support its claims.

## Strengths

I find the proposed method to be a valuable contribution to the field of CLIP adaptation, particularly in its simplicity and effectiveness. The paper revisits the classical algorithm of Gaussian Discriminant Analysis (GDA) and applies it to the downstream classification tasks of CLIP, which is a novel and interesting approach. The method does not require any additional training or optimization, making it highly efficient and easy to implement. The integration of the GDA-based classifier with CLIP's zero-shot classifier through ensembling is a clever way to leverage both the statistical information of the training data and the pre-trained knowledge of CLIP. This ensembling strategy is straightforward and demonstrates good performance across various tasks, including few-shot classification, imbalanced learning, and out-of-distribution generalization. The paper is well-written and easy to follow, with clear explanations of the method, experiments, and results. The authors provide a comprehensive evaluation on 17 datasets, which is a strong point of the paper. The results show that the method can outperform or match state-of-the-art methods in most cases, highlighting its robustness and versatility. The ablation studies and analysis further support the claims and provide insights into the method's performance. Overall, the paper's strengths lie in its simplicity, efficiency, and the novel application of GDA in a training-free setting, which is a significant contribution to the field.

## Weaknesses

Despite the paper's strengths, several limitations and concerns need to be addressed. One of the primary weaknesses is the method's reliance on the assumption that the features of each class follow Gaussian distributions with identical covariance. This assumption is a strong limitation, especially in high-dimensional spaces where the data may not conform to such a simple distribution. The paper does not provide any analysis or discussion on the validity of this assumption, nor does it explore how the method behaves when the assumption is violated. For instance, datasets with high intra-class variance or non-Gaussian distributions, such as fine-grained categories or those with strong intra-class variations due to pose, lighting, or background, could pose significant challenges to the method. The lack of such an analysis leaves a gap in understanding the method's robustness and applicability to diverse datasets. I have a high confidence level in this concern, as the assumption is fundamental to the GDA approach and is not thoroughly validated in the paper.

Another limitation is the use of the K-Nearest-Neighbor (KNN) algorithm to synthesize data for new classes in the base-to-new generalization scenario. While KNN is a simple and widely adopted method, it may not be the most effective or efficient approach, especially when the new classes are semantically distant from the base classes or when the data is high-dimensional. The paper does not compare the proposed KNN-based synthesis with other more sophisticated data synthesis techniques, such as generative adversarial networks (GANs) or variational autoencoders (VAEs). This omission makes it difficult to assess the relative strengths and weaknesses of the KNN approach in this context. I have a high confidence level in this concern, as the paper's method section explicitly describes the use of KNN without any comparative analysis.

The method's performance in few-shot classification is also a point of concern. The paper relies on estimating the covariance matrix, which is challenging in high-dimensional spaces with few training samples. While the authors use shrinkage methods to address this issue, the paper does not provide a detailed analysis of how the performance of covariance estimation degrades with decreasing sample sizes. Specifically, the paper does not explore the condition number of the estimated covariance matrices or the impact of this degradation on the final classification performance. The ablation study in Table 6 does compare different precision matrix estimation methods, but it does not delve into the practical implications of these methods in extreme low-shot scenarios. I have a high confidence level in this concern, as the paper acknowledges the challenge of covariance estimation but does not provide a comprehensive analysis of its limitations.

In the unsupervised learning scenario, the paper employs the Expectation-Maximization (EM) algorithm to estimate the mean and covariance of the unlabeled data. The EM algorithm is known to be sensitive to initialization and may not converge to a stable solution, especially when the data is noisy or has multiple modes. The paper does not provide any details on the initialization or convergence of the EM algorithm, nor does it compare its performance with other unsupervised learning methods, such as clustering or density estimation. This lack of detail and comparison makes it difficult to assess the robustness and stability of the method in unsupervised settings. I have a high confidence level in this concern, as the EM algorithm's sensitivity is a well-known issue, and the paper does not address it adequately.

Finally, the paper's claim of superiority in base-to-new generalization and unsupervised learning is somewhat overstated. While the method achieves comparable results to state-of-the-art methods, the techniques used (KNN and EM) are not novel. The paper does not provide a detailed comparison with other methods that use similar techniques, which could help clarify the specific contributions of the proposed approach. I have a high confidence level in this concern, as the paper's method section and experimental results do not sufficiently differentiate the proposed method from existing techniques.

## Suggestions

To address the identified limitations, I recommend several concrete and actionable improvements. First, the paper should include a more thorough analysis of the Gaussian assumption, particularly the identical covariance assumption. This could involve conducting experiments on datasets known to violate this assumption, such as those with high intra-class variance or non-Gaussian distributions. The authors could use metrics like the Bhattacharyya coefficient or the Kullback-Leibler divergence to quantify the overlap between class distributions and correlate these metrics with the method's performance. This would provide a more nuanced understanding of the method's limitations and help identify scenarios where it is most effective. Additionally, the authors should explore alternative covariance structures, such as allowing for different covariances per class or using a shared covariance matrix that is not necessarily spherical. This would make the method more robust to datasets where the identical covariance assumption does not hold.

For the base-to-new generalization scenario, the authors should consider more sophisticated data synthesis techniques beyond KNN. While KNN is simple, it may not capture the underlying data distribution effectively, especially when the new classes are semantically distant from the base classes. The authors could explore generative models like GANs or VAEs to synthesize more realistic samples for the new classes. Alternatively, they could investigate feature augmentation techniques, such as feature interpolation or extrapolation in the embedding space, to generate new feature representations. The authors should also experiment with different distance metrics in the KNN algorithm, such as cosine similarity or learned distance metrics, to improve the quality of the synthesized data. A comparative analysis of these methods would provide a more comprehensive evaluation of the proposed approach.

Regarding the few-shot classification scenario, the authors should delve deeper into the practical implications of covariance estimation in high-dimensional, low-sample settings. This could involve studying the condition number of the estimated covariance matrices across different shot settings to assess the stability of the method. The authors could also explore alternative regularization techniques, such as adding a small constant to the diagonal of the covariance matrix or using a low-rank approximation, and compare their performance with the proposed shrinkage method. This would strengthen the paper by demonstrating a more comprehensive understanding of the challenges associated with covariance estimation in few-shot scenarios.

In the unsupervised learning scenario, the authors should provide more details on the EM algorithm's implementation and performance. Specifically, they should discuss the initialization strategy for the EM algorithm and how it affects the final results. It would be helpful to show the convergence behavior of the EM algorithm and how the number of iterations impacts the stability of the results. The authors should also compare the performance of the EM algorithm with other unsupervised learning methods, such as clustering algorithms like k-means or hierarchical clustering, and robust versions of the EM algorithm that are less sensitive to initialization and outliers. This would provide a better understanding of the strengths and weaknesses of the EM algorithm in this context.

Finally, the paper should include a more detailed comparison with existing methods that also employ ensembling techniques. The authors should analyze the differences in the ensembling strategies and the specific contributions of their approach. For example, do they use a different weighting scheme for the visual and textual modalities? Do they use a different method for combining the predictions of the zero-shot classifier and the GDA classifier? A more detailed analysis of these aspects would help to clarify the novelty and contribution of the proposed method. The authors should also consider exploring more sophisticated ensembling techniques, such as stacking or boosting, to see if they can further improve the performance of their method. This would demonstrate a more thorough exploration of the potential of ensembling techniques for CLIP-based adaptation.

## Questions

1. How does the method perform on datasets that do not follow the Gaussian distribution assumption, or have different covariances for different classes? Specifically, could you provide experiments on datasets with high intra-class variance or non-Gaussian distributions, and analyze the performance degradation?

2. How does the method compare with other data synthesis methods, such as GANs or VAEs, in the base-to-new generalization scenario? Could you conduct experiments using these methods and compare the results to the KNN-based approach?

3. How does the method compare with other unsupervised learning methods, such as clustering or density estimation, in the unsupervised learning scenario? Could you provide a detailed analysis of the EM algorithm's initialization and convergence, and explore the impact of different initialization strategies on the final results?

4. How does the method scale to larger datasets or more complex tasks? What are the computational and memory requirements of the method, and how do they compare to other training-free adaptation methods?

5. Could you provide a more detailed comparison with existing methods that also employ ensembling techniques? Specifically, how do the ensembling strategies differ, and what are the specific contributions of your approach in terms of weighting and combining predictions from different modalities?

## Full Content

## Summary:

In this paper, I explore a training-free CLIP adaptation method that leverages Gaussian Discriminant Analysis (GDA) to construct a classifier from the statistical properties of the training data, which is then ensembled with CLIP's zero-shot classifier. The method is evaluated on 17 datasets, demonstrating promising results in few-shot classification, imbalanced learning, and out-of-distribution generalization. Additionally, the paper extends the method to base-to-new generalization and unsupervised learning scenarios, showing comparable performance to state-of-the-art methods. The core contributions of this work include the novel application of GDA for training-free adaptation and the integration of visual and textual modalities through ensembling. However, the method's reliance on strong assumptions, such as Gaussian distributions with identical covariance, and the use of common techniques like KNN and EM, raise concerns about its robustness and novelty. Despite these limitations, the paper is well-written, provides clear explanations, and includes ablation studies to support its claims.


## Soundness:

3.0


## Presentation:

3.0


## Contribution:

2.75


## Strengths:

I find the proposed method to be a valuable contribution to the field of CLIP adaptation, particularly in its simplicity and effectiveness. The paper revisits the classical algorithm of Gaussian Discriminant Analysis (GDA) and applies it to the downstream classification tasks of CLIP, which is a novel and interesting approach. The method does not require any additional training or optimization, making it highly efficient and easy to implement. The integration of the GDA-based classifier with CLIP's zero-shot classifier through ensembling is a clever way to leverage both the statistical information of the training data and the pre-trained knowledge of CLIP. This ensembling strategy is straightforward and demonstrates good performance across various tasks, including few-shot classification, imbalanced learning, and out-of-distribution generalization. The paper is well-written and easy to follow, with clear explanations of the method, experiments, and results. The authors provide a comprehensive evaluation on 17 datasets, which is a strong point of the paper. The results show that the method can outperform or match state-of-the-art methods in most cases, highlighting its robustness and versatility. The ablation studies and analysis further support the claims and provide insights into the method's performance. Overall, the paper's strengths lie in its simplicity, efficiency, and the novel application of GDA in a training-free setting, which is a significant contribution to the field.


## Weaknesses:

Despite the paper's strengths, several limitations and concerns need to be addressed. One of the primary weaknesses is the method's reliance on the assumption that the features of each class follow Gaussian distributions with identical covariance. This assumption is a strong limitation, especially in high-dimensional spaces where the data may not conform to such a simple distribution. The paper does not provide any analysis or discussion on the validity of this assumption, nor does it explore how the method behaves when the assumption is violated. For instance, datasets with high intra-class variance or non-Gaussian distributions, such as fine-grained categories or those with strong intra-class variations due to pose, lighting, or background, could pose significant challenges to the method. The lack of such an analysis leaves a gap in understanding the method's robustness and applicability to diverse datasets. I have a high confidence level in this concern, as the assumption is fundamental to the GDA approach and is not thoroughly validated in the paper.

Another limitation is the use of the K-Nearest-Neighbor (KNN) algorithm to synthesize data for new classes in the base-to-new generalization scenario. While KNN is a simple and widely adopted method, it may not be the most effective or efficient approach, especially when the new classes are semantically distant from the base classes or when the data is high-dimensional. The paper does not compare the proposed KNN-based synthesis with other more sophisticated data synthesis techniques, such as generative adversarial networks (GANs) or variational autoencoders (VAEs). This omission makes it difficult to assess the relative strengths and weaknesses of the KNN approach in this context. I have a high confidence level in this concern, as the paper's method section explicitly describes the use of KNN without any comparative analysis.

The method's performance in few-shot classification is also a point of concern. The paper relies on estimating the covariance matrix, which is challenging in high-dimensional spaces with few training samples. While the authors use shrinkage methods to address this issue, the paper does not provide a detailed analysis of how the performance of covariance estimation degrades with decreasing sample sizes. Specifically, the paper does not explore the condition number of the estimated covariance matrices or the impact of this degradation on the final classification performance. The ablation study in Table 6 does compare different precision matrix estimation methods, but it does not delve into the practical implications of these methods in extreme low-shot scenarios. I have a high confidence level in this concern, as the paper acknowledges the challenge of covariance estimation but does not provide a comprehensive analysis of its limitations.

In the unsupervised learning scenario, the paper employs the Expectation-Maximization (EM) algorithm to estimate the mean and covariance of the unlabeled data. The EM algorithm is known to be sensitive to initialization and may not converge to a stable solution, especially when the data is noisy or has multiple modes. The paper does not provide any details on the initialization or convergence of the EM algorithm, nor does it compare its performance with other unsupervised learning methods, such as clustering or density estimation. This lack of detail and comparison makes it difficult to assess the robustness and stability of the method in unsupervised settings. I have a high confidence level in this concern, as the EM algorithm's sensitivity is a well-known issue, and the paper does not address it adequately.

Finally, the paper's claim of superiority in base-to-new generalization and unsupervised learning is somewhat overstated. While the method achieves comparable results to state-of-the-art methods, the techniques used (KNN and EM) are not novel. The paper does not provide a detailed comparison with other methods that use similar techniques, which could help clarify the specific contributions of the proposed approach. I have a high confidence level in this concern, as the paper's method section and experimental results do not sufficiently differentiate the proposed method from existing techniques.


## Suggestions:

To address the identified limitations, I recommend several concrete and actionable improvements. First, the paper should include a more thorough analysis of the Gaussian assumption, particularly the identical covariance assumption. This could involve conducting experiments on datasets known to violate this assumption, such as those with high intra-class variance or non-Gaussian distributions. The authors could use metrics like the Bhattacharyya coefficient or the Kullback-Leibler divergence to quantify the overlap between class distributions and correlate these metrics with the method's performance. This would provide a more nuanced understanding of the method's limitations and help identify scenarios where it is most effective. Additionally, the authors should explore alternative covariance structures, such as allowing for different covariances per class or using a shared covariance matrix that is not necessarily spherical. This would make the method more robust to datasets where the identical covariance assumption does not hold.

For the base-to-new generalization scenario, the authors should consider more sophisticated data synthesis techniques beyond KNN. While KNN is simple, it may not capture the underlying data distribution effectively, especially when the new classes are semantically distant from the base classes. The authors could explore generative models like GANs or VAEs to synthesize more realistic samples for the new classes. Alternatively, they could investigate feature augmentation techniques, such as feature interpolation or extrapolation in the embedding space, to generate new feature representations. The authors should also experiment with different distance metrics in the KNN algorithm, such as cosine similarity or learned distance metrics, to improve the quality of the synthesized data. A comparative analysis of these methods would provide a more comprehensive evaluation of the proposed approach.

Regarding the few-shot classification scenario, the authors should delve deeper into the practical implications of covariance estimation in high-dimensional, low-sample settings. This could involve studying the condition number of the estimated covariance matrices across different shot settings to assess the stability of the method. The authors could also explore alternative regularization techniques, such as adding a small constant to the diagonal of the covariance matrix or using a low-rank approximation, and compare their performance with the proposed shrinkage method. This would strengthen the paper by demonstrating a more comprehensive understanding of the challenges associated with covariance estimation in few-shot scenarios.

In the unsupervised learning scenario, the authors should provide more details on the EM algorithm's implementation and performance. Specifically, they should discuss the initialization strategy for the EM algorithm and how it affects the final results. It would be helpful to show the convergence behavior of the EM algorithm and how the number of iterations impacts the stability of the results. The authors should also compare the performance of the EM algorithm with other unsupervised learning methods, such as clustering algorithms like k-means or hierarchical clustering, and robust versions of the EM algorithm that are less sensitive to initialization and outliers. This would provide a better understanding of the strengths and weaknesses of the EM algorithm in this context.

Finally, the paper should include a more detailed comparison with existing methods that also employ ensembling techniques. The authors should analyze the differences in the ensembling strategies and the specific contributions of their approach. For example, do they use a different weighting scheme for the visual and textual modalities? Do they use a different method for combining the predictions of the zero-shot classifier and the GDA classifier? A more detailed analysis of these aspects would help to clarify the novelty and contribution of the proposed method. The authors should also consider exploring more sophisticated ensembling techniques, such as stacking or boosting, to see if they can further improve the performance of their method. This would demonstrate a more thorough exploration of the potential of ensembling techniques for CLIP-based adaptation.


## Questions:

1. How does the method perform on datasets that do not follow the Gaussian distribution assumption, or have different covariances for different classes? Specifically, could you provide experiments on datasets with high intra-class variance or non-Gaussian distributions, and analyze the performance degradation?

2. How does the method compare with other data synthesis methods, such as GANs or VAEs, in the base-to-new generalization scenario? Could you conduct experiments using these methods and compare the results to the KNN-based approach?

3. How does the method compare with other unsupervised learning methods, such as clustering or density estimation, in the unsupervised learning scenario? Could you provide a detailed analysis of the EM algorithm's initialization and convergence, and explore the impact of different initialization strategies on the final results?

4. How does the method scale to larger datasets or more complex tasks? What are the computational and memory requirements of the method, and how do they compare to other training-free adaptation methods?

5. Could you provide a more detailed comparison with existing methods that also employ ensembling techniques? Specifically, how do the ensembling strategies differ, and what are the specific contributions of your approach in terms of weighting and combining predictions from different modalities?


## Rating:

5.75


## Confidence:

3.75


## Decision:

Reject
