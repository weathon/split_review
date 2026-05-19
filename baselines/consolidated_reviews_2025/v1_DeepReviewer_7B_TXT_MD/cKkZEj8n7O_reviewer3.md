### Summary

This paper proposes a new training framework, GEM, which aims to minimize the generalization error of deep neural networks. The authors first derive a novel bias-variance decomposition of the generalization error. Then, they propose to jointly minimize the conventional training loss and an analytical proxy for the conditional generalization error. The proposed method is evaluated on CIFAR-100 and ImageNet datasets, and the results show that GEM can improve the generalization performance of deep neural networks.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper is well-written and easy to follow.
- The proposed method is simple and easy to implement.
- The experimental results show that GEM can improve the generalization performance of deep neural networks on CIFAR-100 and ImageNet datasets.

### Weaknesses

#### Some Related Works

[1] A Theoretical Analysis of Bagging as a Decorrelator
[2] A Unified Analysis of Noisy Label Learning

#### comment

 - The theoretical motivation for GEM is not entirely convincing. The authors motivate the second empirical risk term in GEM as an approximation of the generalization gap. However, this approximation is based on a heuristic argument rather than a rigorous theoretical justification. The connection between the proposed proxy and the true generalization gap is not clearly established, and the paper lacks a formal analysis of the approximation error. Specifically, the authors state that the conditional training variance can be ignored, but this claim is not supported by any theoretical analysis or empirical evidence. A more rigorous treatment of this approximation is needed to strengthen the theoretical foundation of the proposed method.
- The empirical results are not entirely convincing. While GEM outperforms standard ERM training on CIFAR-100 and ImageNet, the performance gains are relatively small. The authors do not provide a clear explanation for why GEM works better than ERM, and the results are not consistent across all architectures and settings. For example, the performance gains on ImageNet are less pronounced than on CIFAR-100. Furthermore, the paper lacks a detailed analysis of the hyperparameters of GEM, and it is not clear how to choose the optimal values for these parameters. A more thorough investigation of the hyperparameter sensitivity is needed to make the method more practical and reliable.
- The paper lacks a comparison with other state-of-the-art methods for improving generalization, such as those based on data augmentation or regularization techniques. The authors should compare GEM with these methods to demonstrate its advantages and limitations. Without such comparisons, it is difficult to assess the true value of the proposed method.

### Suggestions

The paper would benefit significantly from a more rigorous theoretical analysis of the proposed GEM method. Specifically, the authors should provide a formal derivation of the approximation used to replace the conditional generalization error with the empirical risk on a second dataset. This derivation should include a clear explanation of the assumptions made and a bound on the approximation error. Furthermore, the authors should investigate the conditions under which the conditional training variance can be ignored. This could involve a theoretical analysis of the variance term or an empirical study to quantify its magnitude. A more rigorous theoretical foundation would greatly strengthen the paper's claims and provide a better understanding of the method's behavior.

To address the concerns about the empirical results, the authors should conduct a more comprehensive experimental evaluation. This should include a wider range of architectures, datasets, and training settings. In particular, the authors should investigate why GEM performs better on CIFAR-100 than on ImageNet and provide a detailed analysis of the factors that contribute to the performance differences. Additionally, the authors should perform a more thorough hyperparameter study to determine the optimal values for the hyperparameters of GEM and to assess its sensitivity to these parameters. This study should include a systematic exploration of the hyperparameter space and a discussion of the trade-offs involved in choosing different values. The authors should also compare GEM with other state-of-the-art methods for improving generalization, such as those based on data augmentation or regularization techniques. This comparison should be conducted on a variety of datasets and architectures to provide a comprehensive assessment of the method's performance.

Finally, the authors should provide a more detailed discussion of the practical implications of the proposed method. This should include a discussion of the computational cost of GEM compared to standard ERM, and an analysis of the scalability of the method to large datasets and models. The authors should also discuss the limitations of the method and identify areas for future research. A more thorough discussion of the practical aspects of the method would make the paper more useful to the research community and would help to establish its value as a practical method for improving generalization.

### Questions

- Can the authors provide a more detailed explanation of why minimizing the proposed proxy for generalization error is expected to lead to better generalization compared to other objectives that directly aim to minimize the generalization gap?
- Can the authors provide a theoretical analysis of the convergence properties of the GEM method?
- Can the authors provide a detailed comparison of the computational cost of GEM compared to standard ERM?
- Can the authors provide a thorough analysis of the sensitivity of the GEM method to the choice of hyperparameters?
- Can the authors provide a detailed discussion of the limitations of the GEM method?

### Rating

5

### Confidence

3

**********
