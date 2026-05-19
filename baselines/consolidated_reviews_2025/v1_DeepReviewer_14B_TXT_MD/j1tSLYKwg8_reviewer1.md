### Summary

This paper adapts pre-trained autoregressive models such as GPT-2 and LLaMA to diffusion models, and scale the diffusion models up to 7B parameters. The adaptation is done through attention mask annealing and shift operations, and the training objective for diffusion models is derived under the absorbing discrete diffusion framework. The adapted models, DiffuGPT and DiffuLLaMA, are evaluated on various downstream tasks, and the authors find that DiffuGPT outperforms GPT-2 on most tasks. DiffuLLaMA, while not exceeding LLaMA2 in all tasks, shows competitive performance and excels in infilling tasks.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- This paper proposes a novel approach to adapt pre-trained autoregressive models to diffusion models, which enables scaling diffusion models to larger sizes and leverages the pre-trained knowledge of autoregressive models.
- The authors conduct extensive experiments on various downstream tasks, providing a comprehensive evaluation of the adapted models.
- The authors release their models, code, and scripts, which enhances the reproducibility and impact of their work.

### Weaknesses

#### Some Related Works


#### comment

 - The motivation for adapting autoregressive models to diffusion models is not very clear. Since diffusion models are a type of non-autoregressive models, it is expected that they would struggle to leverage the pre-trained knowledge of autoregressive models. The authors should provide a more detailed explanation of why this adaptation is necessary and what advantages it offers compared to training diffusion models from scratch or using other non-autoregressive models.
- The novelty of the absorbing discrete diffusion framework is limited, as it has been proposed in previous work. While the application of this framework to adapt autoregressive models is novel, the underlying diffusion mechanism is not. The authors should clearly acknowledge the prior work and focus on highlighting the novel aspects of their adaptation method.
- The experimental results do not demonstrate the superiority of diffusion models over autoregressive models. In fact, the adapted models often perform worse than their autoregressive counterparts. The authors should provide a more in-depth analysis of the limitations of their approach and discuss the potential reasons for the performance gap. It is also unclear if the adapted models exhibit any unique advantages that justify the adaptation process.

### Suggestions

The authors should provide a more detailed explanation of the specific challenges they encountered when adapting autoregressive models to diffusion models. For example, how does the attention mask annealing address the inherent differences in the training objectives of autoregressive and diffusion models? What are the specific limitations of using a pre-trained autoregressive model's weights for a diffusion model, and how does the shift operation help to overcome these limitations? A more thorough discussion of these challenges and the proposed solutions would significantly strengthen the paper's contribution. Furthermore, the authors should explore alternative adaptation strategies and compare their performance to the proposed method. This would provide a more comprehensive understanding of the effectiveness of their approach and highlight its advantages over other potential methods.

To better demonstrate the advantages of diffusion models, the authors should focus on tasks where diffusion models are expected to excel, such as parallel text generation and global planning. The current evaluation primarily focuses on tasks where autoregressive models are already strong, which makes it difficult to assess the unique capabilities of diffusion models. The authors should design experiments that specifically highlight the strengths of diffusion models, such as their ability to generate multiple tokens in parallel or their potential for intermediate token correction. For example, they could evaluate the models on tasks that require complex reasoning or planning, where the parallel generation capability of diffusion models could be beneficial. Additionally, the authors should investigate the impact of different diffusion sampling strategies on the performance of the adapted models. This would provide a more complete picture of the capabilities and limitations of the proposed approach.

Finally, the authors should provide a more detailed analysis of the computational cost of their approach compared to training autoregressive models from scratch or using other non-autoregressive models. While the authors mention that diffusion models are more computationally expensive, they should provide a quantitative comparison of the training and inference costs. This would help to assess the practical feasibility of their approach and identify potential areas for improvement. The authors should also discuss the scalability of their approach to larger models and datasets. This would provide a more comprehensive understanding of the potential of their approach for real-world applications. Furthermore, the authors should explore techniques to improve the efficiency of diffusion models, such as reducing the number of diffusion steps or using more efficient sampling algorithms.

### Questions

- Could the authors provide more details on the attention mask annealing process, such as the specific schedule used and the impact of different annealing rates on the performance of the adapted models?
- How does the shift operation affect the training dynamics of the diffusion models, and what are the potential limitations of this approach?
- What are the specific advantages of using a time-embedding-free architecture for diffusion models, and how does this compare to other approaches that use time embeddings?

### Rating

6

### Confidence

4

**********
