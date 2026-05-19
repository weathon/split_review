### Summary

This paper introduces the concept of model kinship to measure the similarity between LLMs and uses it to guide the model merging process. The authors first demonstrate that model kinship correlates with average performance gain in model merging. Then, they propose a new model merging strategy: Top-k Greedy Merging with Model Kinship, which can yield better performance on benchmark datasets.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The authors provide comprehensive experiments to support their claims.
3. The authors propose a novel approach to improve the model merging process.

### Weaknesses

#### Some Related Works

[1] Model Breadcrumbs: Simple Knowledge Fusion for Large Language Models
[2] The Llama 3 Herd of Models
[3] Llama 2: Open Foundation and Fine-Tuned Chat Models

#### comment

1. The authors only conduct experiments with Mistral model. It would be better to conduct experiments with more models, such as Llama [1], Llama 3 [2], and Llama 2 [3]. The lack of diversity in model architectures and training methodologies limits the generalizability of the findings. Specifically, the Mistral model family, while effective, may have unique characteristics that make the observed kinship correlations less applicable to other model families. For example, models with different attention mechanisms or pre-training datasets might exhibit different kinship patterns and merging behaviors. It is crucial to validate the proposed approach across a wider range of models to ensure its robustness and broad applicability.
2. The authors only use the GSM8K, Winogrande, and TruthfulQA MC2 datasets to evaluate the model merging performance. It would be better to use more datasets for evaluation. The current selection of datasets primarily focuses on specific types of reasoning and question-answering tasks. Expanding the evaluation to include datasets that assess other capabilities, such as natural language understanding, common sense reasoning, and code generation, would provide a more comprehensive assessment of the proposed merging strategy. The limited dataset diversity might not fully capture the potential benefits or limitations of the proposed merging approach across different task domains.

### Suggestions

To strengthen the paper, the authors should conduct a more extensive evaluation of their model merging strategy across a diverse set of models and datasets. Specifically, they should include models with different architectures, such as the Llama family [1,2,3], which have different pre-training procedures and architectural designs. This would help to determine whether the observed kinship correlations and the effectiveness of the proposed merging strategy are consistent across different model families. Furthermore, the authors should consider using a wider range of evaluation datasets that cover various tasks, including natural language understanding, common sense reasoning, and code generation. This would provide a more comprehensive assessment of the proposed merging strategy's capabilities and limitations. For example, datasets like GLUE or SuperGLUE could be used to evaluate the model's performance on a variety of natural language understanding tasks, while datasets like BigBench could be used to assess its performance on a wide range of reasoning tasks. Additionally, code generation datasets could be used to evaluate the model's ability to generate code. By expanding the evaluation to include these diverse datasets, the authors can provide a more robust and comprehensive assessment of their proposed merging strategy.

In addition to expanding the evaluation, the authors should also investigate the impact of different merging parameters on the performance of the merged models. For example, the authors could explore how the choice of the top-k models affects the final performance, and whether there is an optimal value for k. They could also investigate the impact of different merging techniques, such as averaging the model weights or using more sophisticated merging algorithms. Furthermore, it would be beneficial to analyze the computational cost of the proposed merging strategy and compare it to other merging techniques. This would help to determine whether the proposed approach is not only effective but also efficient. The authors should also provide a more detailed analysis of the kinship metric itself, exploring its sensitivity to different model architectures and training procedures. This would help to better understand the underlying mechanisms that drive the observed kinship correlations and how they relate to the merging performance.

Finally, the authors should consider providing a more detailed analysis of the limitations of their proposed approach. For example, they could discuss the potential challenges of applying their approach to very large models or to models that have been trained on very different datasets. They could also discuss the potential for the proposed merging strategy to introduce biases or to amplify existing biases in the original models. By acknowledging and addressing these limitations, the authors can provide a more balanced and nuanced assessment of their work and guide future research in this area. Furthermore, it would be beneficial to explore the interpretability of the kinship metric, investigating what specific model characteristics are captured by this metric and how they relate to the merging performance. This would provide a deeper understanding of the underlying mechanisms driving the observed results and could lead to further improvements in the merging strategy.

### Questions

Please see the Weaknesses above.

### Rating

5

### Confidence

3

**********
