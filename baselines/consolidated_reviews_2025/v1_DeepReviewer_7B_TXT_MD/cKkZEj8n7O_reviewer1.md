### Summary

This paper presents a new objective for training neural networks, motivated by a theoretical generalization error decomposition. The proposed objective, GEM, combines the standard empirical risk minimization (ERM) term with an additional regularization term that is related to the empirical risk on a second dataset. The authors show that on CIFAR-100 and ImageNet, GEM outperforms standard ERM training.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

- The paper is well-written and easy to follow.
- The proposed objective is simple and easy to implement.
- The authors conduct a wide range of experiments on various architectures and settings, including ablation studies with different hyperparameters and additional tasks such as few-shot and imbalanced learning.

### Weaknesses

#### Some Related Works

[1] On the relationship between the excess risk and the risk of the empirical minimizer for classification learning.

#### comment

 - The theoretical motivation for GEM is not entirely convincing. The authors motivate the second empirical risk term in GEM as an approximation of the generalization gap. However, this approximation is based on a heuristic argument rather than a rigorous theoretical justification. The connection between the proposed proxy and the true generalization gap is not clearly established, and the paper lacks a formal analysis of the approximation error. Specifically, the authors state that the conditional training variance can be ignored, but this claim is not supported by any theoretical analysis or empirical evidence. A more rigorous treatment of this approximation is needed to strengthen the theoretical foundation of the proposed method.
- The empirical results are not entirely convincing. While GEM outperforms standard ERM training on CIFAR-100 and ImageNet, the performance gains are relatively small. The authors do not provide a clear explanation for why GEM works better than ERM, and the results are not consistent across all architectures and settings. For example, the performance gains on ImageNet are less pronounced than on CIFAR-100. Furthermore, the paper lacks a detailed analysis of the hyperparameters of GEM, and it is not clear how to choose the optimal values for these parameters. A more thorough investigation of the hyperparameter sensitivity is needed to make the method more practical and reliable.
- The paper lacks a comparison with other state-of-the-art methods for improving generalization, such as those based on data augmentation or regularization techniques. The authors should compare GEM with these methods to demonstrate its advantages and limitations. Without such comparisons, it is difficult to assess the true value of the proposed method.

### Suggestions

The paper would benefit significantly from a more rigorous theoretical analysis of the proposed GEM objective. Specifically, the authors should provide a formal derivation of the approximation used to replace the conditional generalization error with the empirical risk on a second dataset. This derivation should include a clear explanation of the assumptions made and a bound on the approximation error. Furthermore, the authors should investigate the conditions under which the conditional training variance can be ignored. This could involve a theoretical analysis of the variance term or an empirical study to quantify its magnitude. A more rigorous theoretical foundation would greatly strengthen the paper's claims and provide a better understanding of the method's behavior.

To address the concerns about the empirical results, the authors should conduct a more comprehensive experimental evaluation. This should include a wider range of architectures, datasets, and training settings. In particular, the authors should investigate why GEM performs better on CIFAR-100 than on ImageNet and provide a detailed analysis of the factors that contribute to the performance differences. Additionally, the authors should perform a more thorough hyperparameter study to determine the optimal values for the hyperparameters of GEM and to assess its sensitivity to these parameters. This study should include a systematic exploration of the hyperparameter space and a discussion of the trade-offs involved in choosing different values. The authors should also compare GEM with other state-of-the-art methods for improving generalization, such as those based on data augmentation or regularization techniques. This comparison should be conducted on a variety of datasets and architectures to provide a comprehensive assessment of the method's performance.

Finally, the authors should provide a more detailed explanation of the practical implications of GEM. This should include a discussion of the computational cost of the method and its scalability to large datasets and models. The authors should also discuss the limitations of the method and identify areas for future research. A more thorough discussion of the practical aspects of GEM would make the paper more useful to the research community and would help to establish its value as a practical method for improving generalization.

### Questions

- How does the performance of GEM compare to other state-of-the-art methods for improving generalization, such as those based on data augmentation or regularization techniques?
- What is the computational cost of GEM compared to standard ERM training?
- What are the limitations of GEM, and under what conditions is it expected to perform well?

### Rating

3

### Confidence

3

**********
