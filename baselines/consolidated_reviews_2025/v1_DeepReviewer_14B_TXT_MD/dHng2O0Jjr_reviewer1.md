### Summary

The paper introduces a framework to improve the tool-use capabilities of large language models (LLMs) by leveraging a large dataset of real-world APIs. The authors constructed a dataset called ToolBench, which includes 16,464 APIs across 49 categories, and developed a depth-first search-based decision tree algorithm to enhance the reasoning capabilities of LLMs. They also introduced an automatic evaluator, ToolEval, to assess the tool-use performance of LLMs. By fine-tuning LLaMA on ToolBench, the resulting model, ToolLLaMA, demonstrated a remarkable ability to execute complex instructions and generalize to unseen APIs, achieving performance comparable to ChatGPT.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper introduces ToolBench, a large-scale dataset with 16,464 APIs across 49 categories, which significantly enhances the diversity and realism of tool-use scenarios for training LLMs.
2. The depth-first search-based decision tree (DFS) algorithm improves the reasoning capabilities of LLMs by allowing them to evaluate multiple reasoning traces and expand the search space.
3. The paper develops ToolEval, an automatic evaluator to assess the tool-use capabilities of LLMs. This provides a standardized way to measure the performance of LLMs in tool-use tasks.
4. The ToolLLaMA model, fine-tuned on ToolBench, demonstrates a remarkable ability to execute complex instructions and generalize to unseen APIs, achieving performance comparable to ChatGPT.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not discuss the potential biases that might be present in the ToolBench dataset. Since the dataset is constructed using ChatGPT, it may inherit biases from the training data of ChatGPT. These biases could affect the performance and fairness of the tool-use framework, especially when applied to diverse real-world scenarios. For example, if the API documentation used to construct ToolBench contains biases towards certain types of users or use cases, the trained model might exhibit preferential treatment or perform better for those specific groups, while underperforming for others. This could lead to unfair or unethical outcomes when the model is deployed in real-world applications.
2. The paper does not address the scalability challenges of the proposed framework. As the number of APIs and the complexity of tasks increase, the computational resources required for training and inference might become prohibitively expensive. Specifically, the depth-first search algorithm, while effective, might not scale efficiently with a very large number of APIs or highly complex instruction sequences, potentially leading to increased training times and resource consumption. The paper lacks a discussion on how the framework would handle such scaling issues, including potential bottlenecks and strategies for optimization.

### Suggestions

To address the potential biases in the ToolBench dataset, the authors should conduct a thorough analysis of the dataset to identify and quantify any existing biases. This could involve examining the distribution of APIs across different categories, analyzing the types of instructions generated, and evaluating the performance of the model across various demographic groups or use cases. Furthermore, the authors should explore techniques to mitigate these biases, such as data augmentation, re-weighting, or adversarial training. It would also be beneficial to compare the performance of the model trained on ToolBench with models trained on other datasets or with models trained using bias-mitigation techniques to understand the impact of the dataset's biases on the model's performance. This analysis should be included in the paper to provide a more comprehensive understanding of the framework's limitations and potential for unfair outcomes.

To address the scalability challenges, the authors should investigate and discuss potential optimization strategies for the depth-first search algorithm, such as pruning techniques or heuristic-based search methods. They should also explore the use of more efficient data structures and algorithms for handling large-scale API data. Furthermore, the authors should provide a detailed analysis of the computational resources required for training and inference, including the memory footprint, training time, and inference latency, as a function of the number of APIs and the complexity of tasks. This analysis should include a discussion of the trade-offs between performance and computational cost, and it should provide practical guidance for users who want to deploy the framework in resource-constrained environments. The authors could also consider exploring distributed training and inference techniques to further improve the scalability of the framework.

Finally, the authors should consider including a more detailed analysis of the limitations of the ToolEval evaluator. While ToolEval provides a standardized way to measure the performance of LLMs in tool-use tasks, it might not capture all aspects of tool-use capabilities, such as the ability to handle unexpected errors or the ability to adapt to new APIs. The authors should discuss the potential limitations of ToolEval and explore alternative evaluation metrics or methods that could provide a more comprehensive assessment of the framework's performance. This could include human evaluation, qualitative analysis of the model's behavior, or the use of more complex benchmark tasks.

### Questions

1. How does the paper address the potential biases in the ToolBench dataset, and what measures are taken to ensure fairness in the tool-use framework?
2. What are the scalability challenges of the proposed framework, and how does it handle the increasing computational resources required for training and inference with a large number of APIs and complex tasks?

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
