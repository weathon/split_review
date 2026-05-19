### Summary

This paper applies Koopman operator theory to linearize the training trajectory of DNNs to accelerate training. Different from the previous methods, this paper proposes to combine Koopman operator theory with differential learning, where different parts of the network can undergo different learning rates during training. This method selectively accelerates the training of some variables to further improve the training efficiency.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

The authors propose a new training acceleration method based on Koopman operator theory. The core idea is to apply different learning rates to different variables according to the prediction from Koopman operator theory. This method selectively accelerates the training of some variables to further improve the training efficiency.

The authors conduct comprehensive experiments to demonstrate the effectiveness of the proposed method. The experiments include evaluating the convergence with different numbers of prediction steps, prediction intervals, starting epochs, and past snapshot counts.

### Weaknesses

#### Some Related Works


#### comment

The method seems to lack novelty since it is a simple combination of Koopman operator theory and differential learning. The core idea of applying different learning rates to different variables based on Koopman predictions is not fundamentally new, as differential learning methods already explore variable-specific learning rates. The integration with Koopman operator theory, while interesting, appears to be a straightforward application of existing techniques for predicting weight updates, rather than a novel methodological contribution. It is more appropriate to say that the contribution of this paper is to accelerate differential learning using Koopman operator theory instead of accelerating SGD.

The experiments are not solid enough to demonstrate the effectiveness of the proposed method. The method is quite unstable when the prediction steps are large, as shown in Figure 9(a). This instability is a significant concern, as it limits the practical applicability of the method. The paper does not provide a clear analysis of the trade-off between acceleration and stability, and it is unclear how to choose the prediction parameters in practice. As shown in Figure 6, the proposed method only has a slight improvement in performance compared to the baseline, and the authors do not provide the code to verify the results. The lack of code makes it difficult to reproduce and validate the experimental findings, which is a major limitation.

The authors do not compare the proposed method with other existing training acceleration methods. This lack of comparison makes it difficult to assess the relative performance of the proposed method. It is important to compare the proposed method with other state-of-the-art training acceleration techniques to demonstrate its advantages and disadvantages.

### Suggestions

To strengthen the paper, the authors should focus on demonstrating the practical advantages of their method more clearly. The current results show only a marginal improvement over the baseline, and the instability issues raise concerns about its real-world applicability. The authors should conduct a more thorough analysis of the method's sensitivity to different hyperparameter settings, especially the prediction steps and intervals. It is crucial to provide clear guidelines on how to choose these parameters to achieve a good balance between acceleration and stability. Furthermore, the authors should investigate the reasons behind the instability at larger prediction steps and propose potential solutions to mitigate this issue. For example, they could explore adaptive prediction strategies that adjust the prediction step based on the training dynamics. The authors should also provide a more detailed analysis of the computational overhead of their method. While the per-iteration cost might be similar to SGD, the additional computations for Koopman operator prediction could introduce a significant overhead, which needs to be quantified and discussed.

In addition to the above, the authors should provide a more comprehensive comparison with existing training acceleration methods. This comparison should include not only the final performance but also the convergence speed, stability, and computational cost. The authors should consider comparing their method with techniques such as adaptive learning rate methods (e.g., Adam, RMSprop), second-order optimization methods (e.g., Newton, BFGS), and other methods that exploit the training dynamics. This would provide a more complete picture of the strengths and weaknesses of the proposed method. The authors should also provide a more detailed explanation of the theoretical underpinnings of their method. While the paper provides a high-level description of how Koopman operator theory is used to predict weight updates, it lacks a rigorous mathematical analysis of the method's convergence properties and stability. A more in-depth theoretical analysis would help to establish the validity of the method and provide a better understanding of its behavior.

Finally, the authors must provide the code for their experiments. This is essential for ensuring the reproducibility of their results and for allowing other researchers to build upon their work. The code should be well-documented and easy to use. The authors should also include detailed instructions on how to reproduce the experiments presented in the paper. Without the code, it is impossible to verify the claims made in the paper, and the contribution of the work is significantly diminished. The authors should also consider releasing the code under an open-source license to encourage further research and development in this area. Addressing these points will significantly improve the quality and impact of the paper.

### Questions

The authors only compare the proposed method with SGD. It would be better to compare the proposed method with other existing training acceleration methods.

### Rating

3

### Confidence

4

**********
