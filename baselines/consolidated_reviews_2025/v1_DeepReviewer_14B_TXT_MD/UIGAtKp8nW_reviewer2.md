### Summary

This paper introduces MUBen, a benchmarking tool designed to evaluate uncertainty quantification (UQ) methods in molecular representation models. It assesses various UQ approaches, including Bayesian neural networks, post-hoc calibration, and ensembles, across different state-of-the-art backbone models for molecular property prediction. The study provides insights into selecting appropriate UQ methods for backbone models, aiming to enhance reliability in critical applications like drug discovery and materials science.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The selection of backbones and UQ methods is representative.
3. The results are rich in detail and comprehensive.

### Weaknesses

#### Some Related Works


#### comment

1. The conclusions drawn from the experiments are not sufficiently informative and lack persuasiveness. For example, the statement "none provides a consistent guarantee of performance improvement over the deterministic baseline, except for Deep Ensembles, and MC Dropout for regression" is not a reasonable conclusion. This issue is also evident in other parts of the paper. The lack of a clear, consistent trend in performance across different UQ methods and datasets makes it difficult to draw actionable insights. The conclusion seems to be based on a superficial analysis of the results, without delving into the underlying reasons for the observed performance variations. For instance, it is not clear if the lack of improvement is due to the limitations of the UQ methods themselves, or the specific characteristics of the datasets or backbone models used.

2. The analysis of the experimental results is not in-depth enough. For example, the paper does not discuss the impact of different molecular descriptors on the performance of UQ methods. This is a significant oversight, as the choice of molecular descriptor can greatly influence the representation of the molecules and, consequently, the effectiveness of the UQ methods. The paper also does not explore the sensitivity of the UQ methods to different hyperparameter settings, which could provide valuable insights into their robustness and applicability.

### Suggestions

To improve the paper, the authors should focus on providing more detailed and nuanced analysis of the experimental results. Instead of making broad statements about the overall performance of UQ methods, they should investigate the specific factors that contribute to their success or failure in different scenarios. For example, they could analyze the correlation between the performance of UQ methods and the size and diversity of the datasets, or the complexity of the molecular descriptors used. This would provide a more granular understanding of the strengths and weaknesses of each UQ method and help identify the conditions under which they are most effective. Furthermore, the authors should explore the impact of different molecular descriptors on the performance of UQ methods. This could involve conducting experiments with different types of descriptors (e.g., 2D, 3D, or hybrid) and analyzing how they affect the uncertainty estimates. This analysis should also consider the computational cost and interpretability of different descriptors, providing a more comprehensive view of their trade-offs. 

Additionally, the authors should conduct a more thorough investigation of the hyperparameter sensitivity of the UQ methods. This could involve performing a grid search or using more advanced optimization techniques to identify the optimal hyperparameter settings for each method and dataset. The results of this analysis should be presented in a clear and concise manner, with visualizations that illustrate the impact of different hyperparameters on the performance of the UQ methods. This would provide valuable guidance for practitioners who want to apply these methods in their own research. The authors should also consider exploring the use of more advanced UQ methods, such as those based on Bayesian neural networks or Gaussian processes, which may offer better performance and more robust uncertainty estimates. A comparison of these methods with the ones presented in the paper would provide a more comprehensive overview of the state-of-the-art in UQ for molecular property prediction.

Finally, the authors should provide a more detailed discussion of the limitations of their study and suggest directions for future research. This could include addressing the challenges of applying UQ methods to more complex molecular systems, or exploring the use of UQ methods for other types of molecular properties. By acknowledging the limitations of their work and suggesting future research directions, the authors can contribute to the advancement of the field and encourage further investigation of this important topic.

### Questions

Please refer to the Weaknesses.

### Rating

5

### Confidence

3

**********
