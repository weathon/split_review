### Summary

This paper proposes a new setting called Sparse Labels Node Classification (SLNC), where only a few labeled nodes are available for training, and these labeled nodes are not provided on a per-class basis. The authors propose a framework called Estimating Label Information (ELI) to address the SLNC problem. ELI leverages unsupervised learning techniques to estimate label information from a pseudo space. The estimated label information is then used to enhance reformulations of well-known semi-supervised learning frameworks and guide the labeled nodes selection process for training. The authors show that their approach outperforms baselines on SLNC by 10-20% when the number of labeled nodes seen at training is extremely few.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

1. The authors propose a new setting called Sparse Labels Node Classification (SLNC), which is more challenging than the traditional Semi-Supervised Node Classification (SSNC) setting. In SLNC, only a few labeled nodes are available for training, and these labeled nodes are not provided on a per-class basis. This setting is more realistic and challenging than the traditional SSNC setting, where a large number of labeled nodes are available for training, and these labeled nodes are provided on a per-class basis.

2. The authors propose a framework called Estimating Label Information (ELI) to address the SLNC problem. ELI leverages unsupervised learning techniques to estimate label information from a pseudo space. The estimated label information is then used to enhance reformulations of well-known semi-supervised learning frameworks and guide the labeled nodes selection process for training.

3. The authors show that their approach outperforms baselines on SLNC by 10-20% when the number of labeled nodes seen at training is extremely few. The authors also provide a theoretical analysis of their approach and show that it is sound.

### Weaknesses

#### Some Related Works


#### comment

1. The authors only compare their approach with a few baselines, such as LP and SGC. It would be beneficial to compare their approach with more state-of-the-art methods, such as [1,2], to better understand its performance in comparison to the current state-of-the-art.

2. The authors do not provide a detailed analysis of the computational complexity of their approach. It would be helpful to understand how the computational complexity of their approach compares to the baselines, especially in terms of time and memory requirements.

3. The authors do not provide a detailed analysis of the sensitivity of their approach to the hyperparameters. It would be helpful to understand how the performance of their approach varies with different hyperparameter settings, such as the number of clusters, the number of neighbors, and the weights of the different terms in the objective function.

### Suggestions

The paper introduces a novel problem setting, Sparse Labels Node Classification (SLNC), and a corresponding framework, Estimating Label Information (ELI), which is a valuable contribution. However, the evaluation of the proposed method could be significantly strengthened by including comparisons with more recent and relevant baselines. Specifically, the current comparison is limited to a few traditional methods like LP and SGC. To better contextualize the performance of ELI, it is crucial to compare it against state-of-the-art graph contrastive learning methods, which have shown promising results in semi-supervised node classification tasks, especially when labeled data is scarce. For instance, methods that leverage contrastive learning to learn node representations could provide a more challenging benchmark. Furthermore, it would be beneficial to analyze the performance of ELI under different levels of label sparsity, as this is a key aspect of the SLNC problem. A more comprehensive evaluation would provide a clearer picture of the strengths and weaknesses of the proposed approach.

In addition to the limited baseline comparison, the paper lacks a detailed analysis of the computational complexity of the proposed ELI framework. While the authors mention that their approach is efficient, a more rigorous analysis is needed to understand its scalability and practical applicability. This analysis should include a breakdown of the time and memory requirements of each step in the ELI framework, such as the unsupervised clustering, label propagation, and model training. Furthermore, it would be helpful to compare the computational complexity of ELI with that of the baseline methods. This analysis should consider the impact of different hyperparameters, such as the number of clusters and neighbors, on the computational cost. Such an analysis would provide valuable insights into the trade-offs between performance and computational efficiency.

Finally, the paper needs a more thorough investigation of the sensitivity of the ELI framework to its hyperparameters. The performance of machine learning models often depends heavily on the choice of hyperparameters, and it is important to understand how the performance of ELI varies with different settings. The authors should conduct a sensitivity analysis to evaluate the impact of key hyperparameters, such as the number of clusters, the number of neighbors, and the weights of the different terms in the objective function. This analysis should include a systematic exploration of the hyperparameter space and provide guidelines for selecting appropriate values for these parameters. Furthermore, it would be helpful to visualize the performance of ELI under different hyperparameter settings, such as by plotting performance curves or heatmaps. This would provide a more intuitive understanding of the sensitivity of the framework and help practitioners to effectively use it.

### Questions

Please refer to the Weaknesses.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
