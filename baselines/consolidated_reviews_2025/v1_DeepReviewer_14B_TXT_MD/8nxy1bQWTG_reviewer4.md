### Summary

The paper proposes a new class of diffusion models called DiffEnc, which introduces a time-dependent encoder in the diffusion process. This encoder improves the flexibility of diffusion models without affecting sampling time, as it is only needed during training. The paper also analyzes the assumption of forward and backward variances being equal, and proves that relaxing this assumption leads to a weighted diffusion loss. The authors show that the optimal Evidence Lower Bound (ELBO) is achieved when variances are equal in continuous time. Experiments show that DiffEnc achieves a statistically significant improvement in likelihood on CIFAR-10, and improves latent loss across datasets without compromising diffusion loss.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper presents a novel framework, DiffEnc, which introduces a time-dependent encoder in the diffusion process. This is a significant contribution as it enhances the flexibility of diffusion models without affecting sampling time.
2. The authors provide a rigorous theoretical analysis of the assumption of forward and backward variances being equal. They prove that relaxing this assumption leads to a weighted diffusion loss and that the optimal ELBO is achieved when variances are equal in continuous time. This theoretical insight is valuable for the field.
3. The experimental results demonstrate that DiffEnc achieves a statistically significant improvement in likelihood on CIFAR-10. Furthermore, the framework improves latent loss across datasets without compromising diffusion loss, showcasing its practical effectiveness.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could benefit from a more detailed discussion of the limitations of the proposed DiffEnc framework. While the authors mention that the encoder is exclusively employed during the training phase, it would be helpful to understand the potential challenges or trade-offs associated with this approach. For instance, how does the introduction of a time-dependent encoder impact the computational complexity of the model, both during training and inference? A more thorough analysis of the computational overhead, including memory usage and training time, would be beneficial. Furthermore, it would be valuable to explore the sensitivity of the model to the specific architecture and hyperparameters of the time-dependent encoder, as this could impact its practical applicability.
2. The paper could provide more context on how the proposed DiffEnc framework compares to other state-of-the-art diffusion models. While the authors mention that diffusion models are state-of-the-art in various domains, it would be helpful to understand how DiffEnc stacks up against other recent advancements in the field. A more detailed comparison with models that incorporate similar techniques, such as those using learnable noise schedules or adaptive sampling methods, would be valuable. Specifically, how does DiffEnc's performance compare to models that also aim to improve the flexibility of the diffusion process, and what are the trade-offs in terms of performance, computational cost, and implementation complexity?

### Suggestions

To address the identified weaknesses, the authors should include a more comprehensive analysis of the computational costs associated with the DiffEnc framework. This should include a detailed breakdown of the training time, memory usage, and inference time, comparing it to standard diffusion models. It would be beneficial to provide a theoretical analysis of the computational complexity, as well as empirical results on various hardware configurations. Furthermore, the authors should investigate the sensitivity of the model to the architecture and hyperparameters of the time-dependent encoder. This could involve conducting ablation studies to understand the impact of different encoder architectures, layer sizes, and activation functions on the overall performance of the model. This analysis should also explore the potential for overfitting or underfitting when using different encoder configurations, and provide guidelines for selecting appropriate hyperparameters.

In addition, the authors should provide a more detailed comparison of the DiffEnc framework with other state-of-the-art diffusion models. This comparison should go beyond simply stating that diffusion models are state-of-the-art and should include a discussion of how DiffEnc compares to models that incorporate similar techniques, such as those using learnable noise schedules or adaptive sampling methods. The authors should also discuss the trade-offs between DiffEnc and these other models in terms of performance, computational cost, and implementation complexity. This could involve conducting experiments on a common set of benchmarks and providing a detailed analysis of the results. It would also be valuable to discuss the potential for combining DiffEnc with other techniques, such as those used in latent diffusion models, to further improve performance.

Finally, the authors should consider including a more detailed discussion of the potential limitations of the DiffEnc framework. This could include a discussion of the assumptions made by the model, the potential for failure modes, and the limitations of the theoretical analysis. It would also be valuable to discuss the potential for future research directions, such as exploring different types of time-dependent encoders or extending the framework to other types of data. By addressing these limitations, the authors can provide a more complete and nuanced understanding of the DiffEnc framework and its potential impact on the field.

### Questions

1. How does the introduction of a time-dependent encoder impact the computational complexity of the model, both during training and inference?
2. How does DiffEnc compare to other state-of-the-art diffusion models in terms of performance, computational cost, and implementation complexity?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
