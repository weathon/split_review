### Summary

This paper proposes an inference-time approach, called Delta, to reduce hallucinations in large language models (LLMs) without requiring model retraining or additional training data. The core idea is to randomly mask tokens in the input sequence, generate outputs from both masked and unmasked inputs, and then adjust the output logits by contrasting the two distributions. This method aims to reduce the likelihood of hallucinations by amplifying contextually relevant tokens and suppressing those that are not grounded in the input. The authors evaluate Delta on several question-answering benchmarks, such as SQuAD v1.1, SQuAD v2, TriviaQA, and Natural Questions, demonstrating improvements in exact match and F1 scores. However, the method shows limited effectiveness on datasets that require commonsense knowledge or general knowledge, such as CommonsenseQA and MMLU.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The proposed method is computationally efficient as it does not require additional training data or model retraining.
2. The method shows significant improvements in handling unanswerable questions, as evidenced by the no-answer exact match score on SQuAD v2.

### Weaknesses

#### Some Related Works


#### comment

1. The method's effectiveness is limited to context-rich tasks and does not generalize well to tasks requiring commonsense or general knowledge. This limitation is significant because many real-world applications of LLMs rely on commonsense reasoning. The authors should consider the following:
- Expanding the evaluation to include a wider range of tasks that assess different types of hallucinations, such as those involving commonsense reasoning or factual knowledge.
- Investigating whether the method can be adapted to improve performance on tasks that require implicit or general knowledge, possibly by incorporating external knowledge sources during inference.

2. The choice of a 0.7 masking ratio seems arbitrary and lacks sufficient justification. A more thorough analysis of how different masking ratios affect performance would strengthen the paper. Specifically, the authors should explore a wider range of masking ratios and provide a detailed analysis of the trade-offs between performance and computational cost. The current justification is insufficient to understand the sensitivity of the method to this hyperparameter.

3. The paper does not provide a clear explanation for why the method performs better with sampling during inference. This aspect requires further investigation and clarification. The authors should provide a more detailed analysis of the interaction between sampling and the proposed method, including a discussion of how sampling affects the contrastive decoding process and why it leads to improved performance in certain cases.

4. The paper does not provide a detailed analysis of the computational overhead introduced by the method. While the authors claim the method is computationally efficient, they do not provide a quantitative analysis of the additional time and memory requirements. A detailed analysis of the computational cost, including the time complexity and memory footprint, is necessary to assess the practical applicability of the method.

### Suggestions

The authors should expand their evaluation to include a more diverse set of tasks that assess different types of hallucinations, beyond just context-rich question answering. This should include tasks that specifically test commonsense reasoning, factual knowledge, and the ability to handle implicit or general knowledge. For example, evaluations could be performed on datasets like Winogrande, HellaSwag, or TruthfulQA, which are designed to assess different aspects of reasoning and knowledge. Furthermore, the authors should investigate methods to adapt their approach to improve performance on these types of tasks. This could involve incorporating external knowledge sources during inference, or modifying the masking strategy to better capture the nuances of commonsense reasoning. A more comprehensive evaluation would provide a clearer picture of the method's strengths and limitations, and help to identify areas for future improvement.

To address the concern regarding the masking ratio, the authors should conduct a more thorough analysis of how different masking ratios affect performance. This should include a systematic exploration of a wider range of masking ratios, and a detailed analysis of the trade-offs between performance and computational cost. The analysis should not only focus on the final performance metrics, but also on the intermediate steps of the method, such as the quality of the contrastive distributions. The authors should also provide a clear explanation of why a particular masking ratio is chosen, and how this choice affects the overall performance of the method. This analysis should be presented with clear visualizations and statistical analysis to support the claims made in the paper. Furthermore, the authors should investigate whether the optimal masking ratio is task-dependent, and provide guidance on how to choose the appropriate masking ratio for different types of tasks.

Finally, the authors should provide a more detailed analysis of the computational overhead introduced by their method. This should include a quantitative analysis of the additional time and memory requirements, as well as a discussion of the time complexity and memory footprint. The analysis should also consider the impact of different hyperparameters, such as the masking ratio, on the computational cost. This analysis should be presented in a clear and concise manner, and should provide practical guidance for users who want to apply the method in real-world scenarios. Furthermore, the authors should investigate potential optimizations to reduce the computational overhead of the method, such as using more efficient masking strategies or parallelizing the inference process.

### Questions

1. How does the method perform on other types of hallucinations beyond those in question-answering, such as factual inaccuracies in open-ended generation tasks?
2. What is the impact of different masking strategies (e.g., masking entire sequences vs. partial masking) on the performance of the method?
3. How sensitive is the method to the choice of masking ratio, and is 0.7 optimal across different datasets and tasks?
4. What is the computational overhead introduced by the method, and how does it scale with the size of the input and the complexity of the task?

### Rating

3

### Confidence

4

**********
