### Summary

The paper proposes a new framework called DiffEnc for variational diffusion models. DiffEnc introduces a time-dependent encoder that parameterizes the mean of the diffusion process. The authors analyze the assumption of forward and backward variances being equal and prove that in the continuous-time limit, the optimal ELBO is achieved when the variances are equal. They also introduce a weighted diffusion loss approach and derive the optimal $\sigma_P^2$ in the continuous-time limit. Experiments show that DiffEnc improves total likelihood on CIFAR-10.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

1. The paper introduces a novel framework called DiffEnc for variational diffusion models, which introduces a time-dependent encoder that parameterizes the mean of the diffusion process.
2. The authors analyze the assumption of forward and backward variances being equal and prove that in the continuous-time limit, the optimal ELBO is achieved when the variances are equal.
3. The authors introduce a weighted diffusion loss approach and derive the optimal $\sigma_P^2$ in the continuous-time limit.
4. Experiments show that DiffEnc improves total likelihood on CIFAR-10.

### Weaknesses

#### Some Related Works


#### comment

1. The paper is not well-written and is difficult to follow. The authors should improve the clarity and organization of the paper.
2. The authors should provide more details about the experimental setup, such as the training procedure, hyperparameters, and evaluation metrics.
3. The authors should compare DiffEnc with more baseline models, such as other diffusion models and generative models.
4. The authors should discuss the limitations of DiffEnc and potential future work.

### Suggestions

The paper introduces a novel time-dependent encoder for variational diffusion models, which is a promising direction. However, the presentation needs significant improvement to ensure clarity and accessibility. The authors should provide a more detailed explanation of the mathematical derivations, especially the connection between the time-dependent encoder and the resulting ELBO. Specifically, the paper should clarify how the time-dependent encoder modifies the standard diffusion process and how this modification affects the variational lower bound. The authors should also provide a more intuitive explanation of the theoretical results, such as the conditions under which the optimal ELBO is achieved. Furthermore, the paper should include a more comprehensive discussion of the practical implications of the proposed method, such as the computational cost and the sensitivity to hyperparameter choices. 

To address the lack of experimental details, the authors should provide a more thorough description of the experimental setup. This should include the specific architecture of the time-dependent encoder, the choice of hyperparameters, and the training procedure. The authors should also provide a more detailed explanation of the evaluation metrics used and justify their choice. It would be beneficial to include ablation studies to analyze the impact of different components of the proposed method. For example, the authors could investigate the effect of different encoder architectures or different choices of the weighting function in the weighted diffusion loss. The authors should also compare their method with a wider range of baseline models, including other state-of-the-art diffusion models and generative models. This would provide a more comprehensive evaluation of the proposed method and allow for a better understanding of its strengths and weaknesses.

Finally, the authors should discuss the limitations of their approach and suggest potential directions for future research. This should include a discussion of the potential challenges in scaling the proposed method to larger datasets and more complex models. The authors should also discuss the potential impact of the proposed method on other areas of machine learning, such as image generation and representation learning. Furthermore, the authors should consider the potential for combining their method with other techniques, such as attention mechanisms or normalizing flows, to further improve the performance of variational diffusion models. A more thorough discussion of these aspects would significantly enhance the impact and relevance of the paper.

### Questions

1. What are the limitations of DiffEnc and potential future work?
2. How does DiffEnc compare to other diffusion models in terms of performance and efficiency?
3. What are the potential applications of DiffEnc beyond image generation?

### Rating

5: marginally below the acceptance threshold

### Confidence

2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
