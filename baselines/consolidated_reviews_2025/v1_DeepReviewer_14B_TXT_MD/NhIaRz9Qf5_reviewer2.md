### Summary

The paper proposes an adaptive retrieval method that leverages the internal states of LLM for retrieval decision, re-ranking, and reasoning strategies. The authors conducted experiments on both complex QA and simple QA datasets, and results show that the proposed method outperforms non-adaptive RAG and adaptive RAG methods.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple and effective. Results on both complex QA and simple QA datasets show the effectiveness of the proposed method compared to non-adaptive RAG and adaptive RAG methods.
3. The authors provide detailed analysis on the each component of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method relies on the internal states of the LLM, which limits the application of the proposed method. Specifically, the reliance on middle-layer representations for uncertainty estimation may not be universally applicable across different model architectures, and the method's performance could degrade significantly when applied to models with different layer configurations or without accessible internal states. Furthermore, the computational overhead of extracting and processing these internal states is not thoroughly discussed, which could be a practical limitation.
2. The authors only conducted experiments on the 7B LLaMA-2 model. It would be better to conduct experiments on different model families and different sizes to verify the generalization of the proposed method. The lack of experiments on different model families, such as models with different architectures (e.g., encoder-decoder models) or different pre-training objectives, makes it difficult to assess the robustness of the proposed method. The performance of the method might be highly dependent on the specific characteristics of the LLaMA-2 model, and it is unclear how well it would generalize to other models with different parameter distributions and training procedures.

### Suggestions

The paper presents an interesting approach to adaptive retrieval using LLM internal states, but there are several areas where the methodology and evaluation could be strengthened. First, the authors should investigate the sensitivity of the method to different layers. While the paper mentions using the middle layer, a more detailed analysis of how the choice of layer affects performance is needed. For example, a systematic ablation study could be conducted to evaluate the impact of using different layers for uncertainty estimation. This would provide a better understanding of which layers are most informative for retrieval decisions and could potentially lead to improved performance. Furthermore, the authors should explore the computational cost of extracting and processing internal states, and compare it to other retrieval methods. This is important for practical applications, as the computational overhead could be a limiting factor.

Second, the experimental evaluation should be expanded to include a wider range of models. The current evaluation is limited to the 7B LLaMA-2 model, which makes it difficult to assess the generalization of the proposed method. The authors should conduct experiments on different model families, such as models with different architectures (e.g., encoder-decoder models) or different pre-training objectives. This would provide a more comprehensive evaluation of the method's robustness and applicability. Additionally, the authors should investigate the impact of model size on the performance of the proposed method. It is possible that the method's effectiveness could vary depending on the model's capacity, and it is important to understand how the method scales with different model sizes. The authors should also consider evaluating the method on different types of tasks, such as summarization or dialogue, to assess its versatility.

Finally, the authors should provide a more detailed analysis of the retrieval decisions made by the proposed method. It would be helpful to understand when the method decides to retrieve and when it decides to rely on the internal knowledge of the LLM. This could be done by analyzing the uncertainty scores associated with different queries and examining the correlation between uncertainty and retrieval performance. Furthermore, the authors should investigate the impact of the retrieval threshold on the overall performance of the method. A sensitivity analysis of the threshold would provide insights into the trade-off between retrieval accuracy and computational cost. The authors should also consider comparing the proposed method to other adaptive retrieval methods that do not rely on internal states, to better understand the advantages and disadvantages of their approach.

### Questions

1. How does the proposed method perform on other models, such as different model families or different sizes?
2. How does the proposed method perform on other tasks, such as summarization or dialogue?

### Rating

6

### Confidence

4

**********
