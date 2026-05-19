### Summary

This paper proposes a novel method to improve the mathematical reasoning ability of LLMs. The authors introduce a new dataset called MetaMathQA, which is generated through a bootstrapping approach. This approach involves generating new questions from existing ones and creating new reasoning paths. The MetaMathQA dataset is then used to fine-tune LLaMA-2, resulting in a model called MetaMath. The authors demonstrate that MetaMath outperforms other open-source LLMs on the GSM8K and MATH benchmarks.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper is well-structured and easy to follow.
2. The authors provide a detailed description of the MetaMathQA dataset and the bootstrapping approach.
3. The experiments are comprehensive, and the results are promising.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a comparison with state-of-the-art models, such as GPT-4 and Claude 3.5, which are widely recognized as top-performing models in the field.
2. The paper does not provide a detailed analysis of the computational cost and efficiency of the proposed method. It would be beneficial to understand how the bootstrapping approach affects the training time and resource requirements.
3. The paper does not explore the generalizability of the proposed method to other mathematical reasoning tasks or datasets. It would be valuable to see how the MetaMath approach performs on more diverse and challenging mathematical problems.

### Suggestions

The paper would significantly benefit from a more thorough comparison against state-of-the-art models. While the authors demonstrate improvements over open-source LLMs, the absence of comparisons with models like GPT-4 and Claude 3.5 leaves a gap in understanding the true performance of the proposed MetaMath model. These models are benchmarks in the field, and a comparison would provide a clearer picture of the practical impact of the proposed method. The authors should consider evaluating their model on the same benchmarks used by these top models to provide a more comprehensive performance analysis. This would also help to contextualize the performance gains achieved by MetaMath and highlight its strengths and weaknesses relative to the current state-of-the-art.

Furthermore, the paper needs a more detailed analysis of the computational cost and efficiency of the proposed bootstrapping method. The authors should provide a breakdown of the time and resources required for each stage of the bootstrapping process, including question generation, reasoning path creation, and dataset construction. This analysis should also consider the scalability of the method, particularly when applied to larger datasets and more complex mathematical problems. It would be beneficial to understand how the training time and resource requirements scale with the size of the dataset and the complexity of the reasoning tasks. This information is crucial for assessing the practical applicability of the proposed method and for understanding its limitations.

Finally, the paper should explore the generalizability of the MetaMath approach to a wider range of mathematical reasoning tasks and datasets. While the authors demonstrate promising results on the GSM8K and MATH benchmarks, it is important to evaluate the model's performance on more diverse and challenging mathematical problems. This could include tasks that involve different types of mathematical reasoning, such as algebraic manipulation, calculus, or geometry. Additionally, it would be valuable to assess the model's performance on datasets that are not specifically designed for mathematical reasoning, such as datasets from other domains that require complex problem-solving skills. This would provide a more comprehensive understanding of the model's capabilities and limitations and would help to identify areas for future research.

### Questions

1. How does the proposed method perform on more diverse and challenging mathematical problems?
2. What are the limitations of the proposed method, and how can they be addressed in future work?

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
