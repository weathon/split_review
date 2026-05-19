### Summary

This paper proposes a new framework for variational diffusion models, called DiffEnc, by introducing a time-dependent encoder in the diffusion process. The authors provide a detailed analysis of the assumption of forward and backward variances being equal, and prove that in the continuous-time limit, the optimal ELBO is achieved when the variances are equal. The paper also introduces a weighted diffusion loss approach and derives the optimal $\sigma_P^2$ in the continuous-time limit. The authors conduct experiments on MNIST, CIFAR-10, and ImageNet32, demonstrating that DiffEnc improves total likelihood on CIFAR-10.

### Soundness

3 good

### Presentation

2 fair

### Contribution

3 good

### Strengths

- The paper provides a detailed analysis of the assumption of forward and backward variances being equal, and proves that in the continuous-time limit, the optimal ELBO is achieved when the variances are equal. This theoretical result is a significant contribution to the understanding of variational diffusion models.
- The paper introduces a weighted diffusion loss approach and derives the optimal $\sigma_P^2$ in the continuous-time limit. This is a novel contribution that can potentially lead to improved performance of diffusion models.
- The paper conducts experiments on MNIST, CIFAR-10, and ImageNet32, demonstrating that DiffEnc improves total likelihood on CIFAR-10. The experimental results provide empirical evidence for the effectiveness of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

 - The paper is not well-written and is difficult to follow. The authors should improve the clarity and organization of the paper.
- The authors should provide more details about the experimental setup, such as the training procedure, hyperparameters, and evaluation metrics.
- The authors should compare DiffEnc with more baseline models, such as other diffusion models and generative models.
- The authors should discuss the limitations of DiffEnc and potential future work.

### Suggestions

The paper would benefit significantly from a more detailed explanation of the core concepts and methodologies. Specifically, the introduction of the time-dependent encoder and its integration into the diffusion process needs further clarification. The authors should provide a step-by-step breakdown of how this encoder modifies the standard diffusion process, including the mathematical formulations and the underlying assumptions. It would be helpful to include a visual representation of the proposed framework to aid understanding. Furthermore, the theoretical analysis, while interesting, could be made more accessible by providing more intuitive explanations and connecting the results to practical implications. For example, the authors could elaborate on how the derived optimal $\sigma_P^2$ impacts the training dynamics and the quality of generated samples. The paper should also include a more thorough discussion of the limitations of the proposed approach, such as potential computational overhead or sensitivity to hyperparameter choices. 

To strengthen the empirical validation, the authors should provide a more comprehensive comparison with existing state-of-the-art diffusion models. This comparison should not only focus on the final performance metrics but also delve into the training dynamics, convergence behavior, and computational efficiency. For instance, the authors could compare the training time and memory usage of DiffEnc with other models on the same datasets. Additionally, the experimental section should include ablation studies to analyze the impact of different components of the proposed method. For example, the authors could investigate the effect of varying the architecture of the time-dependent encoder or the choice of the weighting function in the weighted diffusion loss. This would provide a more nuanced understanding of the proposed method and its potential for further improvement. The authors should also consider including a more diverse set of datasets to demonstrate the generalizability of the proposed method.

Finally, the paper should include a more thorough discussion of the potential applications and future research directions. The authors should explore how the proposed method could be applied to other domains beyond image generation, such as audio or video processing. They should also discuss potential extensions of the proposed method, such as incorporating attention mechanisms or exploring different encoder architectures. Furthermore, the authors should discuss the potential impact of their work on the broader field of generative modeling and its potential to address real-world problems. This would help to position the proposed method within the broader research landscape and highlight its significance.

### Questions

Please see the weaknesses above.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
