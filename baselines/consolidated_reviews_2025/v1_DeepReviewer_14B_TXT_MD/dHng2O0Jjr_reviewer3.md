### Summary

This paper presents ToolLLM, a framework for training large language models (LLMs) to use external tools (APIs) to fulfill human instructions. The framework includes a large-scale dataset of 16,464 real-world APIs, a novel depth-first search-based decision tree algorithm for enhancing the reasoning capabilities of LLMs, and an automatic evaluator for assessing the tool-use capabilities of LLMs. The authors fine-tune LLaMA on the dataset and equip it with a neural API retriever to recommend appropriate APIs for each instruction. The results show that the model exhibits comparable performance to ChatGPT and demonstrates strong zero-shot generalization ability in an out-of-distribution tool-use dataset.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper introduces a large-scale dataset of 16,464 real-world APIs, which is a valuable resource for training and evaluating LLMs for tool use.
2. The depth-first search-based decision tree algorithm is a novel approach to enhancing the reasoning capabilities of LLMs, which enables the model to evaluate multiple reasoning traces and expand the search space.
3. The automatic evaluator, ToolEval, is a useful tool for assessing the tool-use capabilities of LLMs, which provides a standardized way to measure the performance of LLMs in tool use.
4. The paper demonstrates the effectiveness of the proposed framework by fine-tuning LLaMA on the dataset and equipping it with a neural API retriever, which shows that the model exhibits comparable performance to ChatGPT and demonstrates strong zero-shot generalization ability in an out-of-distribution tool-use dataset.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not discuss the potential biases that might be present in the ToolBench dataset. Since the dataset is constructed using ChatGPT, it may inherit biases from the training data of ChatGPT. These biases could affect the performance and fairness of the tool-use framework, especially when applied to diverse real-world scenarios.
2. The paper does not address the scalability challenges of the proposed framework. As the number of APIs and the complexity of tasks increase, the computational resources required for training and inference might become prohibitively expensive. The paper does not provide any analysis of the computational cost associated with the depth-first search-based decision tree algorithm, which could be a significant bottleneck for large-scale applications.

### Suggestions

The authors should investigate the potential biases present in the ToolBench dataset. Since the dataset is generated using ChatGPT, it is crucial to analyze whether the generated instructions and API usage patterns reflect any biases present in the pre-training data of ChatGPT. This analysis should include an examination of the types of tasks, the diversity of API usage, and the potential for demographic or other biases to be present in the dataset. Furthermore, the authors should explore methods to mitigate these biases, such as data augmentation or re-weighting techniques, to ensure the fairness and robustness of the tool-use framework. A detailed analysis of the dataset's composition and potential biases is essential for the reliable deployment of the proposed framework in real-world scenarios.

To address the scalability concerns, the authors should provide a more detailed analysis of the computational cost associated with the depth-first search-based decision tree algorithm. This analysis should include the time and memory complexity of the algorithm, as well as the impact of the number of APIs and the complexity of tasks on the computational resources required. The authors should also explore alternative algorithms or optimization techniques to reduce the computational cost of the framework, such as pruning techniques or heuristic search methods. Furthermore, the authors should consider the practical implications of deploying the framework in resource-constrained environments and provide recommendations for how to adapt the framework to different computational settings. A thorough analysis of the computational cost and scalability of the framework is crucial for its practical applicability.

Finally, the authors should consider the limitations of the current evaluation metrics. While the paper introduces ToolEval, it is important to acknowledge that the evaluation of tool-use capabilities is a complex task that may require more nuanced metrics. The authors should explore alternative evaluation metrics that can capture the quality of the generated API calls, the efficiency of the reasoning process, and the overall user experience. This could include metrics that measure the correctness of the API parameters, the number of API calls required to complete a task, and the user satisfaction with the generated solutions. A more comprehensive evaluation framework would provide a more complete picture of the tool-use capabilities of the proposed framework.

### Questions

1. How does the paper address the potential biases in the ToolBench dataset, and what measures are taken to ensure fairness in the tool-use framework?
2. What are the scalability challenges of the proposed framework, and how does it handle the increasing computational resources required for training and inference with a large number of APIs and complex tasks?

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
