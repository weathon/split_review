### Summary

This paper introduces ToolLLM, a framework designed to enhance the tool-use capabilities of large language models (LLMs). ToolLLM comprises a large-scale dataset of 16,464 real-world APIs, a novel depth-first search-based decision tree algorithm for reasoning, and an automatic evaluator for assessing tool-use performance. The authors fine-tune LLaMA on the dataset and equip it with a neural API retriever, achieving performance comparable to ChatGPT and demonstrating strong generalization to unseen APIs. The paper also presents ToolEval, an automatic evaluator for tool-use tasks, and ToolLLaMA, a fine-tuned LLaMA model with a neural API retriever, showcasing its effectiveness in executing complex instructions and generalizing to out-of-distribution tool-use datasets.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper introduces ToolLLM, a comprehensive framework that addresses the tool-use capabilities of LLMs, encompassing data construction, model training, and evaluation. This holistic approach is a significant contribution to the field.
2. The construction of ToolBench, a large-scale dataset with 16,464 real-world APIs, is a valuable resource for the research community. The dataset's scale and diversity enhance the generalizability of the models trained on it.
3. The development of ToolEval, an automatic evaluator for tool-use tasks, is a practical contribution that can facilitate the development and evaluation of tool-using LLMs.
4. The paper presents a novel depth-first search-based decision tree algorithm (DFSDT) that improves the reasoning capabilities of LLMs, enabling them to navigate through reasoning paths strategically.
5. The fine-tuning of LLaMA on ToolBench and the integration of a neural API retriever demonstrate the practical application of the proposed framework, achieving performance comparable to ChatGPT and showing strong generalization to unseen APIs.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational resources required for training and inference. This information is crucial for assessing the practical applicability of the proposed framework.
2. The paper could benefit from a more in-depth discussion of the limitations of the proposed approach. For example, how does the model perform when the available APIs are not well-documented or when the user's instructions are ambiguous?
3. The paper could also explore the potential for incorporating human feedback into the training process to further improve the model's performance.

### Suggestions

The paper should include a more thorough analysis of the computational resources required for training and inference. This should include details on the hardware used (e.g., GPU model, memory), the training time for different model sizes, and the inference latency. Providing this information would allow other researchers to better assess the feasibility of replicating the results and would also help in understanding the trade-offs between model size, performance, and computational cost. Furthermore, it would be beneficial to discuss the scalability of the approach, particularly how the computational requirements change with an increasing number of APIs or more complex instructions. This analysis should also consider the memory footprint of the model and the API retriever, which is crucial for deployment in resource-constrained environments.

To address the limitations of the proposed approach, the paper should include a more detailed analysis of the model's performance under various challenging conditions. Specifically, the paper should investigate how the model handles scenarios where API documentation is incomplete, inaccurate, or ambiguous. This could involve creating a test set with such cases and evaluating the model's ability to still perform the intended actions. Additionally, the paper should explore the model's robustness to ambiguous user instructions, such as those with multiple possible interpretations or those that require complex reasoning. This could be achieved by introducing a benchmark dataset with such instructions and analyzing the model's performance. The paper should also discuss potential strategies for mitigating these limitations, such as incorporating techniques for handling uncertainty in API documentation or using more sophisticated methods for instruction understanding.

Finally, the paper should explore the potential for incorporating human feedback into the training process. This could involve techniques such as active learning, where the model is trained on a small set of human-annotated examples and then used to select the most informative examples for further annotation. Alternatively, the authors could explore reinforcement learning from human feedback, where the model is trained to maximize a reward signal provided by human evaluators. This would allow the model to learn from human preferences and improve its performance on complex tasks. The paper should also discuss the challenges associated with incorporating human feedback, such as the cost of obtaining high-quality annotations and the potential for bias in human evaluations.

### Questions

1. How does the model perform when the available APIs are not well-documented or when the user's instructions are ambiguous?
2. What are the potential for error propagation when using a chain-of-thought approach, especially when dealing with complex, multi-step tasks?
3. How does the model handle cases where the user's instructions are ambiguous or require reasoning beyond the capabilities of the current API set?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
