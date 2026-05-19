### Summary

This paper proposes a method to scale Diffusion Language Models (DLMs) by adapting pre-trained Autoregressive (AR) models. The authors introduce techniques like attention mask annealing and shift operations to bridge the gap between AR and diffusion objectives. They demonstrate that their adapted models, DiffuGPT and DiffuLLaMA, achieve competitive performance compared to AR models on various benchmarks.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper presents a novel approach by adapting existing AR models to diffusion models, addressing the challenge of resource-intensive training for DLMs from scratch. The introduction of techniques like attention mask annealing and shift operations to align AR models with diffusion objectives is innovative and well-executed.
2. The authors provide a thorough evaluation of their adapted models across various benchmarks, demonstrating that DLMs can achieve competitive performance compared to AR models. The experiments are well-designed and the results are clearly presented.

### Weaknesses

#### Some Related Works


#### comment

1. While the paper demonstrates the effectiveness of the adaptation approach, it could benefit from a deeper analysis of why diffusion models, despite the adaptation, still lag behind AR models in certain capabilities. Specifically, the paper lacks a detailed investigation into the specific mechanisms that cause diffusion models to underperform in tasks requiring strong autoregressive capabilities, such as complex reasoning or long-range dependencies. A more thorough analysis should explore the information flow and gradient propagation within the diffusion model architecture, and how these differ from AR models, potentially leading to the observed performance gaps.
2. The paper could explore more on the potential benefits of DLMs over AR models, providing a stronger justification for the adaptation approach. The paper does not sufficiently articulate the theoretical advantages of diffusion models in specific scenarios, such as parallel generation or robustness to adversarial examples. A more detailed discussion should focus on the unique properties of diffusion models, such as their ability to generate multiple tokens simultaneously and their inherent resistance to certain types of noise, and how these properties could be leveraged in practical applications.

### Suggestions

To strengthen the paper, the authors should delve deeper into the architectural differences between diffusion and autoregressive models, focusing on how these differences impact performance on various tasks. Specifically, they should analyze the gradient flow and information propagation within the diffusion model during the reverse process. This analysis should include visualizations of the attention patterns and how they differ from those in AR models, particularly in tasks requiring long-range dependencies. Furthermore, the authors should investigate the impact of the number of diffusion steps on model performance, as this parameter directly affects the model's ability to capture complex dependencies. A detailed study of how the model's performance varies with different numbers of steps, and how this relates to the model's ability to capture long-range dependencies, would be beneficial. This analysis should also consider the computational cost associated with increasing the number of steps, providing a trade-off analysis between performance and efficiency.

Additionally, the authors should provide a more comprehensive discussion of the potential advantages of diffusion models over autoregressive models. This discussion should go beyond the general claim of parallel generation and delve into specific scenarios where diffusion models might excel. For example, they could explore the potential of diffusion models for generating diverse and creative text, or their robustness to adversarial attacks. The authors should also investigate the ability of diffusion models to perform tasks that are difficult for autoregressive models, such as generating text with specific constraints or properties. This could involve exploring the use of guidance techniques during the sampling process to steer the model towards desired outputs. A detailed analysis of how these techniques can be used to control the generation process and achieve specific goals would be valuable.

Finally, the authors should consider exploring alternative training strategies for diffusion models that might better align with the autoregressive loss. This could involve investigating different noise schedules or loss functions that are more suitable for language modeling. The authors should also explore the use of techniques such as curriculum learning or adaptive sampling to improve the training process. Furthermore, the authors should investigate the impact of different model sizes on the performance of diffusion models, and how this relates to the scaling laws observed in autoregressive models. A detailed study of how the model's performance scales with the number of parameters, and how this compares to the scaling behavior of autoregressive models, would be beneficial.

### Questions

1. How do the training dynamics and convergence properties of diffusion models compare to those of AR models, especially at scale? Are there specific architectural considerations or hyperparameters that are crucial for the successful adaptation of AR models to diffusion models?
2. What are the computational trade-offs between diffusion and AR models, particularly in terms of training and inference efficiency? How do these trade-offs scale with model size and dataset size?
3. Can the proposed adaptation approach be extended to other types of non-autoregressive models, and what are the potential benefits or limitations of doing so?

### Rating

6

### Confidence

4

**********
