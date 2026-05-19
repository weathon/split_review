### Summary

This paper proposes a confidence-based hierarchical structure of variational autoencoder (VAE) architectures called “Reckoner” for reliable fairness learning under the assumption of missing sensitive attributes.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

The paper is well-written

### Weaknesses

#### Some Related Works


#### comment

1. The method is not clearly described in the paper, for example, the objective function for training the models is not clearly stated in the paper.

2. The used datasets are only two.

3. The proposed method is not significantly better than the baseline.

### Suggestions

The paper needs to provide a more detailed explanation of the training process, specifically regarding the objective function used for the VAEs. The current description lacks the necessary mathematical rigor to fully understand how the models are optimized. For instance, the paper should explicitly state how the reconstruction loss and the KL divergence term are weighted, and whether any additional regularization terms are included. Furthermore, it is unclear how the confidence-based hierarchical structure is integrated into the VAE training. A clear mathematical formulation of the objective function, including all relevant terms and hyperparameters, is crucial for reproducibility and for the reader to grasp the technical contribution of the work. The authors should also clarify how the pseudo-learning process is implemented and how it interacts with the standard VAE training.

To strengthen the empirical evaluation, the authors should consider expanding the number of datasets used for experimentation. While the two datasets used may be common in the fairness literature, the limited number of datasets makes it difficult to assess the generalizability of the proposed method. The authors should consider including datasets with different characteristics, such as varying sizes, feature types, and sensitive attribute distributions. This would provide a more robust evaluation of the method's performance and its ability to handle diverse scenarios. Additionally, the paper should include a more detailed analysis of the results, such as reporting the standard deviation of the performance metrics across multiple runs, which would provide a better understanding of the method's stability.

Finally, the paper needs to address the issue of the proposed method not showing significant improvement over the baseline. The authors should provide a more in-depth analysis of the results, exploring why the method does not achieve a substantial advantage. It would be beneficial to investigate the limitations of the proposed approach and identify the scenarios where it is most effective. The authors should also consider comparing their method to a wider range of baselines, including more recent approaches in fairness learning. A more thorough comparison would help to better position the proposed method within the existing literature and highlight its potential contributions.

### Questions

1. The paper was submitted with all datasets and sensitive attributes removed. How does this relate to real-world scenarios where sensitive attributes are genuinely unavailable, and how does the proposed method ensure fairness without access to such critical information?

2. What is the objective function for training the models?

3. How many runs are used to get the results in Tables 2 and 3 and why the standard deviation is not reported?

4. Why the proposed method is not significantly better than the baseline?

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
