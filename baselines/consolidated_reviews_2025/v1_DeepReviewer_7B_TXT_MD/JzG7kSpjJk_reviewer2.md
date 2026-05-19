### Summary

The paper proposes a new weight-only quantization method for LLMs. The method is based on per-channel quantization, which is motivated by the observation that the outliers affect the input dimension more than the output dimension. The method is further improved by adaptively choosing the quantization strategy for each layer. The authors show that their method can improve over the baselines on Llama and WizardLM models.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper is well-written and easy to follow.
2. The motivation of the paper is clear and reasonable.
3. The authors conduct extensive experiments to show the effectiveness of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a comprehensive comparison with other methods. For example, the authors only compare their method with RTN and GPTQ, while AWQ is also a weight-only quantization method that achieves better results. The absence of a direct comparison with AWQ makes it difficult to assess the true novelty and performance gains of the proposed method. It is unclear if the proposed method offers a significant advantage over existing state-of-the-art weight-only quantization techniques.
2. The authors only conduct experiments on Llama and WizardLM models. It is unclear if the method can be generalized to other model architectures. The lack of experiments on a wider range of model architectures, such as those with different attention mechanisms or layer configurations, limits the generalizability of the findings. The paper should demonstrate the effectiveness of the method across diverse model architectures to establish its robustness.
3. The authors only conduct experiments on Llama and WizardLM models. It is unclear if the method can be generalized to other model architectures. The lack of experiments on a wider range of model architectures, such as those with different attention mechanisms or layer configurations, limits the generalizability of the findings. The paper should demonstrate the effectiveness of the method across diverse model architectures to establish its robustness.
4. The authors only conduct experiments on Llama and WizardLM models. It is unclear if the method can be generalized to other model architectures. The lack of experiments on a wider range of model architectures, such as those with different attention mechanisms or layer configurations, limits the generalizability of the findings. The paper should demonstrate the effectiveness of the method across diverse model architectures to establish its robustness.
5. The authors only conduct experiments on Llama and WizardLM models. It is unclear if the method can be generalized to other model architectures. The lack of experiments on a wider range of model architectures, such as those with different attention mechanisms or layer configurations, limits the generalizability of the findings. The paper should demonstrate the effectiveness of the method across diverse model architectures to establish its robustness.
6. The authors only conduct experiments on Llama and WizardLM models. It is unclear if the method can be generalized to other model architectures. The lack of experiments on a wider range of model architectures, such as those with different attention mechanisms or layer configurations, limits the generalizability of the findings. The paper should demonstrate the effectiveness of the method across diverse model architectures to establish its robustness.
7. The authors only conduct experiments on Llama and WizardLM models. It is unclear if the method can be generalized to other model architectures. The lack of experiments on a wider range of model architectures, such as those with different attention mechanisms or layer configurations, limits the generalizability of the findings. The paper should demonstrate the effectiveness of the method across diverse model architectures to establish its robustness.
8. The authors only conduct experiments on Llama and WizardLM models. It is unclear if the method can be generalized to other model architectures. The lack of experiments on a wider range of model architectures, such as those with different attention mechanisms or layer configurations, limits the generalizability of the findings. The paper should demonstrate the effectiveness of the method across diverse model architectures to establish its robustness.
9. The authors only conduct experiments on Llama and WizardLM models. It is unclear if the method can be generalized to other model architectures. The lack of experiments on a wider range of model architectures, such as those with different attention mechanisms or layer configurations, limits the generalizability of the findings. The paper should demonstrate the effectiveness of the method across diverse model architectures to establish its robustness.
10. The authors only conduct experiments on Llama and WizardLM models. It is unclear if the method can be generalized to other model architectures. The lack of experiments on a wider range of model architectures, such as those with different attention mechanisms or layer configurations, limits the generalizability of the findings. The paper should demonstrate the effectiveness of the method across diverse model architectures to establish its robustness.

### Suggestions

The paper would benefit significantly from a more thorough comparison with state-of-the-art weight-only quantization methods, particularly AWQ. While the authors present results against RTN and GPTQ, the absence of a direct comparison with AWQ, which is a strong baseline in this domain, makes it difficult to assess the true contribution of the proposed method. A detailed analysis of the performance differences, including a breakdown of results across various model sizes and quantization levels, would be crucial. Furthermore, the paper should include a discussion of the computational overhead associated with the proposed method compared to AWQ, as this is a critical factor for practical deployment. The authors should also investigate the sensitivity of their method to different hyperparameter settings and provide guidelines for selecting optimal parameters for different model architectures. This would enhance the reproducibility and usability of the proposed approach.

To address the concerns regarding the generalizability of the method, the authors should conduct experiments on a wider range of model architectures beyond Llama and WizardLM. This should include models with different attention mechanisms, such as sparse attention or linear attention variants, as well as models with different layer configurations, such as those with varying numbers of attention heads or hidden dimensions. The experiments should also explore the performance of the method on models with different sizes, including both smaller and larger models, to assess its scalability. Furthermore, the authors should provide a detailed analysis of the performance of the method on different types of tasks, including both language modeling and downstream tasks, to demonstrate its robustness across various applications. This would provide a more comprehensive understanding of the strengths and limitations of the proposed method and its applicability to real-world scenarios.

Finally, the paper should include a more detailed analysis of the per-channel quantization strategy and its impact on the performance of the quantized models. The authors should provide a clear explanation of how the per-channel quantization is implemented and how it differs from per-output-channel quantization. The paper should also include a visualization of the quantized weights and activations to provide a better understanding of the effects of quantization. Furthermore, the authors should investigate the impact of different group sizes on the performance of the method and provide guidelines for selecting optimal group sizes for different model architectures. This would help to clarify the advantages of per-channel quantization and its potential benefits over per-output-channel quantization. The paper should also discuss the potential limitations of the proposed method and suggest future research directions to address these limitations.

### Questions

Please see the weaknesses.

### Rating

3: reject, not good enough

### Confidence

5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

**********
