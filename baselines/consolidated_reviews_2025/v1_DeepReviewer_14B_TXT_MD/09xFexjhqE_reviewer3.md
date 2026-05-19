### Summary

This paper proposes a new method to improve the robust fine-tuning of pre-trained feature extractors. The authors argue that existing methods suffer from a problem of gradient divergence, where the gradients of the adversarial and natural objectives point in different directions, making the optimization process unstable and sensitive to hyperparameters. To address this issue, the authors propose to use a low-rank branch to disentangle the optimization process, with the adversarial objective optimized through the feature extractor and the natural objective optimized through the low-rank branch. Additionally, the authors propose heuristic strategies for automating the scheduling of the learning rate and the scalars of loss terms. The authors conduct extensive experiments on various downstream tasks and show that their proposed method achieves state-of-the-art results in terms of adversarial robustness.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow. The authors provide a clear motivation for their work and explain their proposed method in detail.
2. The authors conduct extensive experiments on various downstream tasks and show that their proposed method achieves state-of-the-art results in terms of adversarial robustness.
3. The authors provide a thorough analysis of their proposed method and discuss its limitations and potential future directions.

### Weaknesses

#### Some Related Works


#### comment

1. The authors argue that the issue of gradient divergence impedes obtaining adversarial robustness. However, the authors do not provide a theoretical analysis of why this is the case. It is not clear why the divergence of gradients would necessarily lead to a decrease in adversarial robustness. A more rigorous explanation, possibly involving the geometry of the loss landscape or the properties of the optimization trajectory, is needed to support this claim. For example, are there specific conditions on the loss function or the feature space that exacerbate this divergence and lead to poor robustness?
2. The authors propose to use a low-rank branch to disentangle the optimization process. However, the authors do not provide a theoretical analysis of why this works. While the intuition of separating the natural and adversarial objectives is clear, it is not clear why a low-rank branch is the optimal choice for this disentanglement. What are the properties of the low-rank branch that make it suitable for this task? Are there other types of branches that could achieve similar or better results? A theoretical justification for the choice of a low-rank branch is needed.
3. The authors propose heuristic strategies for automating the scheduling of the learning rate and the scalars of loss terms. However, the authors do not provide a theoretical analysis of why these strategies work. The proposed scheduling strategies are based on empirical observations, but there is no theoretical justification for why these specific strategies are effective. For example, why is a step size scheduler for adversarial attack enhanced by using the scheduler for the learning rate? What are the underlying dynamics that make this scheduling effective?

### Suggestions

To strengthen the paper, the authors should provide a more in-depth theoretical analysis of the gradient divergence issue. This could involve analyzing the geometry of the loss landscape and how the gradients of the natural and adversarial objectives interact. For instance, the authors could investigate whether the gradient divergence is related to the curvature of the loss function or the presence of saddle points. A theoretical framework that explains why the divergence of gradients leads to a decrease in adversarial robustness would significantly enhance the paper's contribution. Furthermore, the authors could explore the relationship between the gradient divergence and the generalization performance of the model. This could involve analyzing the properties of the feature space and how the gradients affect the learned representations.

Regarding the use of a low-rank branch, the authors should provide a more detailed theoretical justification for this choice. This could involve analyzing the properties of low-rank matrices and how they affect the optimization process. For example, the authors could investigate whether the low-rank branch introduces any regularization effects that contribute to the improved robustness. It would also be beneficial to compare the performance of the low-rank branch with other types of branches, such as high-rank branches or branches with different activation functions. This would help to determine whether the low-rank branch is indeed the optimal choice for disentangling the optimization process. The authors should also discuss the computational cost of using a low-rank branch and whether it introduces any trade-offs in terms of efficiency.

Finally, the authors should provide a more rigorous analysis of the proposed scheduling strategies. This could involve analyzing the dynamics of the optimization process and how the learning rate and loss term scalars affect the convergence behavior. For example, the authors could investigate whether the proposed scheduling strategies help to avoid local minima or saddle points. It would also be beneficial to compare the performance of the proposed scheduling strategies with other scheduling methods, such as adaptive learning rate methods. This would help to determine whether the proposed strategies are indeed effective and whether they offer any advantages over existing methods. The authors should also discuss the sensitivity of the proposed strategies to different hyperparameter settings and whether they are robust to different datasets and tasks.

### Questions

1. Can the authors provide more details on the theoretical analysis of the gradient similarity and how it relates to the adversarial robustness?
2. Can the authors provide more details on the theoretical analysis of the low-rank branch and how it helps to disentangle the optimization process?
3. Can the authors provide more details on the theoretical analysis of the automated scheduler and how it helps to improve the convergence of the optimization process?

### Rating

6

### Confidence

4

**********
