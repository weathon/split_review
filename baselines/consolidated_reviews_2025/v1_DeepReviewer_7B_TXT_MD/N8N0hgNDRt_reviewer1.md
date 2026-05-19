### Summary

This paper proposes a novel method to enhance the mathematical reasoning capabilities of large language models (LLMs). The authors address the challenge of training LLMs to solve complex mathematical problems by creating a new training dataset called MetaMathQA. This dataset is built through a bootstrapping approach, which involves generating new questions and reasoning paths from existing mathematical problems. The core idea is to improve the diversity and quality of the training data, thereby enhancing the model's ability to understand and solve mathematical problems. The authors then fine-tune an LLM, specifically LLaMA-2, on this dataset to create a new model called MetaMath. The experimental results demonstrate that MetaMath achieves state-of-the-art performance on two benchmark datasets, GSM8K and MATH, significantly outperforming other open-source LLMs.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper introduces a novel bootstrapping method for generating training data, which is a creative approach to improving the diversity and quality of mathematical reasoning datasets.
2. The MetaMath model achieves significant performance gains on the GSM8K and MATH benchmarks, surpassing other open-source LLMs. This demonstrates the effectiveness of the proposed method.
3. The paper is well-organized and clearly explains the methodology, experimental setup, and results. The figures and tables are helpful in understanding the findings.

### Weaknesses

#### Some Related Works


#### comment

1. The paper's reliance on LLaMA-2 as the base model raises concerns about the generalizability of the findings to other LLM architectures. It would be beneficial to see how the proposed method performs with models that have different architectures and training paradigms.
2. The bootstrapping approach, while innovative, may introduce biases or inconsistencies in the generated data. A more detailed analysis of the potential impact of these biases on the model's performance is needed.
3. The paper could benefit from a more thorough comparison with existing methods for improving mathematical reasoning in LLMs. A detailed analysis of the advantages and disadvantages of the proposed method compared to other approaches would strengthen the paper's contribution.

### Suggestions

The authors should consider expanding their experiments to include a wider range of LLM architectures beyond LLaMA-2. This would provide a more comprehensive understanding of the method's generalizability and robustness. Specifically, it would be valuable to test the approach on models with different architectural designs, such as those employing attention mechanisms or transformer architectures, to determine if the performance gains are consistent across diverse model types. Furthermore, the authors should investigate the impact of varying model sizes within each architecture to assess the scalability of the proposed method. This would help establish the practical applicability of the method across different computational resources and model capacities. A more detailed analysis of the computational cost associated with the bootstrapping process would also be beneficial, especially when considering the application to larger models.

To address the potential biases introduced by the bootstrapping approach, the authors should conduct a more rigorous analysis of the generated data. This could involve examining the distribution of question types, the complexity of the reasoning paths, and the diversity of the mathematical concepts covered. It would be useful to quantify the extent of any biases that may be present and to explore methods for mitigating these biases. For example, the authors could implement techniques such as adversarial training or data augmentation to improve the robustness of the model. Additionally, a detailed error analysis of the model's performance on different types of questions would help identify specific areas where the model struggles and where the bootstrapping approach may have introduced biases. This analysis should also consider the impact of the bootstrapping process on the model's ability to generalize to unseen mathematical problems.

Finally, the paper would benefit from a more comprehensive comparison with existing methods for improving mathematical reasoning in LLMs. The authors should provide a detailed analysis of the advantages and disadvantages of their approach compared to other techniques, such as those based on reinforcement learning or symbolic reasoning. This comparison should not only focus on performance metrics but also consider factors such as computational cost, data requirements, and the interpretability of the results. A thorough discussion of the limitations of the proposed method and potential avenues for future research would further enhance the paper's contribution. This would help to contextualize the findings and provide a more complete picture of the current state of the art in mathematical reasoning for LLMs.

### Questions

1. How does the proposed method compare to other techniques for improving mathematical reasoning in LLMs, such as reinforcement learning or symbolic reasoning?
2. What are the computational costs associated with the bootstrapping process, and how do they scale with the size of the model and dataset?

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
