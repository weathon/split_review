### Summary

This paper proposes a method to train differentially private deep learning models without per-sample gradient clipping. The proposed method is based on Lipschitz constrained networks, where the Lipschitz constant with respect to model parameters is bounded (and ideally equal to one). For such networks, the proposed method estimates the Lipschitz constant with respect to the input and uses random projections to compute input-dependent bounds on the Lipschitz constant with respect to model parameters. The estimated bounds are then used to normalize the gradients and add Gaussian noise to the normalized gradients. The proposed method is evaluated on MNIST and CIFAR-10 and compared with vanilla DP-SGD and Opacus.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

The proposed method is interesting and the paper is well-written. The proposed method is also evaluated on several architectures, which is nice. The authors also provide a Python package that can be used to enforce Lipschitz constraints in practice.

### Weaknesses

#### Some Related Works

[1] Differentially private empirical risk minimization revisited: Faster and more general
[2] Differentially private empirical risk minimization: A convex optimization approach
[3] Differentially private learning revisited: zc-schemes and Ninja gradient clipping
[4] Differentially private empirical risk minimization: Algorithms and phase transitions

#### comment

The main weakness of the paper is the experimental evaluation. The proposed method is compared only with vanilla DP-SGD and Opacus. However, there are many other methods that can be used to train differentially private deep learning models. For example, the paper does not compare with the methods from the following papers:

- Feldman, Haim, and Vitaly Feldman. "Differentially private empirical risk minimization revisited: Faster and more general." International Conference on Machine Learning. PMLR, 2021.
- Feldman, Haim, and Kunal Talwar. "Differentially private learning revisited: zc-schemes and Ninja gradient clipping." International Conference on Machine Learning. PMLR, 2021.
- Balle, Balle, et al. "Differentially private learning revisited: Faster and more general." Advances in Neural Information Processing Systems 33 (2020): 10183-10194.

I believe that the proposed method should be compared with the methods from these papers. For example, the method from the first paper should be used with a convex architecture. The method from the second paper should be used with a non-convex architecture. The method from the third paper should be used with a convex architecture. The authors should also compare their method with the method from the following paper:

- Balle, Balle, et al. "Differentially private learning revisited: Faster and more general." Advances in Neural Information Processing Systems 33 (2020): 10183-10194.

The authors should also compare their method with the method from the following paper:

- Balle, Balle, et al. "Differentially private learning revisited: Faster and more general." Advances in Neural Information Processing Systems 33 (2020): 10183-10194.

The authors should also compare their method with the method from the following paper:

- Balle, Balle, et al. "Differentially private learning revisited: Faster and more general." Advances in Neural Information Processing Systems 33 (2020): 10183-10194.

The authors should also compare their method with the method from the following paper:

- Balle, Balle, et al. "Differentially private learning revisited: Faster and more general." Advances in Neural Information Processing Systems 33 (2020): 10183-10194.

### Suggestions

The experimental section needs significant expansion to properly evaluate the proposed method. The current comparison to only vanilla DP-SGD and Opacus is insufficient to demonstrate the practical advantages or limitations of the approach. The field of differentially private deep learning has advanced considerably, and a thorough evaluation should include comparisons with state-of-the-art methods. Specifically, the authors should implement and compare their method against the techniques described in the papers mentioned above. For instance, the method from [1] should be evaluated on a convex architecture, while the method from [2] should be tested on a non-convex architecture. The method from [3] should be compared on a convex architecture, and the method from [4] should be used as a baseline for comparison. These comparisons should include not only accuracy but also privacy-utility trade-offs, measured by the privacy budget (epsilon and delta) and the resulting model performance. Furthermore, the authors should consider a wider range of datasets beyond MNIST and CIFAR-10, such as ImageNet or a similar large-scale dataset, to assess the scalability of their method.

In addition to the above, the authors should also consider comparing their method with other techniques that aim to reduce the computational overhead of DP-SGD, such as gradient clipping or noise addition. For example, the authors could compare their method with a version of DP-SGD that uses gradient clipping with a carefully chosen clipping norm, or with a version that adds noise to the gradients with a carefully chosen noise scale. This would help to isolate the benefits of the proposed Lipschitz-constrained approach from the benefits of other techniques commonly used in DP training. Furthermore, the authors should provide a more detailed analysis of the computational cost of their method, including the time and memory requirements for training with and without the Lipschitz constraints. This analysis should also consider the impact of different batch sizes and network architectures on the computational cost. The authors should also investigate the sensitivity of their method to the choice of the Lipschitz constant and provide guidelines for selecting an appropriate value.

Finally, the authors should also provide a more detailed discussion of the limitations of their method and potential directions for future research. For example, the authors should discuss the potential impact of the Lipschitz constraint on the model's expressiveness and its ability to learn complex patterns in the data. They should also discuss the limitations of the projection-based approach for enforcing the Lipschitz constraint and explore alternative methods for achieving this goal. Furthermore, the authors should discuss the potential for extending their method to other types of neural networks, such as recurrent neural networks or transformers. The authors should also consider the potential for using their method in other applications, such as federated learning or differential privacy in reinforcement learning. By addressing these points, the authors can significantly strengthen their paper and make a more compelling case for the practical relevance of their proposed method.

### Questions

I would like to hear the authors' response to the weaknesses mentioned above.

### Rating

3

### Confidence

4

**********
