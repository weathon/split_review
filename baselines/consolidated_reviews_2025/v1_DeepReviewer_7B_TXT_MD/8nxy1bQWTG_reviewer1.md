### Summary

This paper proposes a new diffusion model framework, DiffEnc, which introduces a time-dependent encoder to increase the flexibility of the diffusion process while maintaining the same sampling time. The authors also theoretically analyze the assumption of forward and backward variances being equal and prove that, in the continuous-time limit, the optimal ELBO is achieved when the variances are equal. The authors demonstrate that DiffEnc can improve total likelihood on CIFAR-10.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

1. The authors provide a detailed theoretical analysis of the diffusion model framework, including the derivation of the optimal ELBO and the impact of a time-dependent encoder.
2. The authors demonstrate that DiffEnc can improve total likelihood on CIFAR-10, which is a significant achievement.
3. The authors provide comprehensive experimental results and ablation studies to validate the effectiveness of DiffEnc.

### Weaknesses

#### Some Related Works


#### comment

1. The paper is not well-written and is difficult to follow. The authors should improve the clarity and organization of the paper.
2. The authors should provide more details about the experimental setup, such as the training procedure, hyperparameters, and evaluation metrics.
3. The authors should compare DiffEnc with more baseline models, such as other diffusion models and generative models.
4. The authors should discuss the limitations of DiffEnc and potential future work.

### Suggestions

The paper needs significant improvements in clarity and organization to be easily understood by the reader. The introduction should clearly state the problem being addressed, the proposed solution (DiffEnc), and the main contributions of the paper. The methodology section should provide a step-by-step explanation of the proposed framework, including the time-dependent encoder and its impact on the diffusion process. The authors should also clearly define all the mathematical notations and explain the intuition behind each step. The experimental section should be reorganized to present the setup, results, and analysis in a logical order. The authors should provide detailed information about the training procedure, including the optimizer, learning rate, batch size, and number of epochs. The evaluation metrics should be clearly defined, and the results should be presented in a way that is easy to interpret. The authors should also include error bars or confidence intervals to indicate the uncertainty in the results. Furthermore, the authors should provide a more detailed explanation of the experimental results, including the statistical significance of the observed improvements.

To strengthen the paper, the authors should include more comprehensive experimental results. They should compare DiffEnc with a wider range of baseline models, including other diffusion models and generative models. The comparison should be done on multiple datasets and evaluation metrics. The authors should also provide a detailed analysis of the strengths and weaknesses of DiffEnc compared to the baseline models. The authors should also include ablation studies to evaluate the impact of different components of DiffEnc, such as the time-dependent encoder and the continuous-time limit. The authors should also discuss the computational cost of DiffEnc and compare it to the baseline models. The authors should also provide a discussion of the limitations of DiffEnc and potential future work. For example, the authors could discuss the potential for overfitting, the sensitivity of the model to hyperparameters, and the scalability of the model to larger datasets.

Finally, the authors should provide a more detailed discussion of the theoretical analysis of DiffEnc. They should explain the assumptions made in the analysis and the limitations of the analysis. The authors should also provide a more intuitive explanation of the results of the analysis. The authors should also discuss the potential for extending the theoretical analysis to other diffusion models. The authors should also provide a more detailed discussion of the relationship between DiffEnc and other diffusion models. The authors should also discuss the potential for using DiffEnc in other applications. For example, the authors could discuss the potential for using DiffEnc for image editing, inpainting, and other tasks.

### Questions

1. How does DiffEnc compare to other diffusion models in terms of performance and efficiency?
2. What are the limitations of DiffEnc and potential future work?

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
