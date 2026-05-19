### Summary

This paper proposes ToolLLM, a general tool-use framework encompassing data construction, model training, and evaluation. ToolBench is constructed automatically using ChatGPT. A novel depth-first search-based decision tree algorithm is developed to enhance the reasoning capabilities of LLMs. ToolEval is developed as an automatic evaluator. ToolLLaMA is fine-tuned based on LLaMA and equipped with a neural API retriever. Experiments show ToolLLaMA exhibits comparable performance to ChatGPT and demonstrates strong zero-shot generalization ability in an out-of-distribution tool-use dataset: APIBench.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. ToolLLM is a general tool-use framework including data construction, model training, and evaluation. It is a complete work.
2. ToolBench is a high-quality instruction-tuning dataset constructed automatically using ChatGPT. It is large-scale and diverse.
3. A novel depth-first search-based decision tree algorithm is developed to enhance the reasoning capabilities of LLMs.
4. ToolEval is developed as an automatic evaluator.
5. ToolLLaMA is fine-tuned based on LLaMA and equipped with a neural API retriever.
6. Experiments show ToolLLaMA exhibits comparable performance to ChatGPT and demonstrates strong zero-shot generalization ability in an out-of-distribution tool-use dataset: APIBench.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational resources required for training and inference. This information is crucial for assessing the practical applicability of the proposed framework. Specifically, the paper lacks details on the GPU memory footprint, training time per epoch, and inference latency for different model sizes and API retrieval configurations. This makes it difficult to reproduce the results or to understand the trade-offs between performance and computational cost.
2. The paper could benefit from a more in-depth discussion of the limitations of the proposed approach. For example, how does the model perform when the available APIs are not well-documented or when the user's instructions are ambiguous? The paper should also discuss the potential for error propagation when using a chain-of-thought approach, especially when dealing with complex, multi-step tasks. Furthermore, the paper does not address the potential for the model to generate API calls that are syntactically correct but semantically inappropriate for the given task.
3. The paper could also explore the potential for incorporating human feedback into the training process to further improve the model's performance. The current approach relies solely on automatically generated data, which may not capture the nuances of human tool use. The paper should discuss the potential benefits and challenges of incorporating human-in-the-loop feedback, such as active learning or reinforcement learning from human feedback.

### Suggestions

The paper should include a detailed analysis of the computational resources required for training and inference. This should include the GPU memory footprint, training time per epoch, and inference latency for different model sizes and API retrieval configurations. The authors should also provide a breakdown of the computational cost associated with each component of the framework, such as the API retriever, the LLM, and the decision tree algorithm. This analysis should be presented in a clear and concise manner, with tables and figures to illustrate the key findings. Furthermore, the authors should discuss the trade-offs between performance and computational cost, and provide recommendations for users with different resource constraints. This would greatly enhance the practical value of the paper and allow other researchers to reproduce the results.

The paper should also include a more in-depth discussion of the limitations of the proposed approach. This should include an analysis of how the model performs when the available APIs are not well-documented or when the user's instructions are ambiguous. The authors should also discuss the potential for error propagation when using a chain-of-thought approach, especially when dealing with complex, multi-step tasks. Furthermore, the paper should address the potential for the model to generate API calls that are syntactically correct but semantically inappropriate for the given task. The authors should provide concrete examples of these limitations and discuss potential mitigation strategies. This would provide a more balanced and realistic assessment of the proposed framework.

Finally, the paper should explore the potential for incorporating human feedback into the training process. This could involve techniques such as active learning, where the model is trained on a small set of human-annotated examples and then used to select the most informative examples for further annotation. Alternatively, the authors could explore reinforcement learning from human feedback, where the model is trained to maximize a reward signal provided by human evaluators. The paper should discuss the potential benefits and challenges of incorporating human-in-the-loop feedback, and provide a roadmap for future research in this direction. This would help to further improve the model's performance and make it more robust to real-world scenarios.

### Questions

1. How does the model perform when the available APIs are not well-documented or when the user's instructions are ambiguous?
2. What are the potential for error propagation when using a chain-of-thought approach, especially when dealing with complex, multi-step tasks?
3. How does the model handle cases where the user's instructions are ambiguous or require reasoning beyond the capabilities of the current API set?
4. How does the model handle cases where the available APIs are not well-documented or when the user's instructions are ambiguous?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
