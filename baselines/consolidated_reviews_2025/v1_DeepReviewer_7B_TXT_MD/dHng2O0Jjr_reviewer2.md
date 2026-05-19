### Summary

This paper proposes a tool-use framework for LLMs. The framework consists of three parts: data construction, model training, and evaluation. The data construction part is to generate a dataset of tool-use instructions and corresponding API calls. The model training part is to fine-tune an LLM on this dataset. The evaluation part is to evaluate the tool-use performance of LLMs. The authors also propose a Depth-First Search-based decision tree algorithm to improve the reasoning and planning capabilities of LLMs. The authors fine-tune LLaMA on the constructed dataset and evaluate the performance of the fine-tuned model on APIBench. The results show that the fine-tuned model achieves competitive performance with GPT-4.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper is well-written and easy to follow.
2. The paper proposes a tool-use framework for LLMs, which is a novel and important research direction.
3. The paper proposes a Depth-First Search-based decision tree algorithm to improve the reasoning and planning capabilities of LLMs.
4. The paper fine-tunes LLaMA on the constructed dataset and evaluates the performance of the fine-tuned model on APIBench. The results show that the fine-tuned model achieves competitive performance with GPT-4.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the limitations of the proposed framework. For example, the paper does not discuss the potential biases in the dataset and how these biases might affect the performance of the model. The paper also does not discuss the computational cost of the proposed framework and how it scales with the size of the dataset and the complexity of the tasks.
2. The paper does not provide a comparison with other state-of-the-art tool-use frameworks. The paper only compares the performance of the fine-tuned model with GPT-4 on APIBench. It is unclear how the proposed framework compares to other existing frameworks in terms of performance, efficiency, and robustness.
3. The paper does not provide a detailed analysis of the error cases of the fine-tuned model. It is unclear why the model fails to solve certain tasks and what are the common patterns in the error cases. This analysis is important for understanding the limitations of the model and for identifying areas for improvement.

### Suggestions

The paper would benefit from a more thorough discussion of the limitations inherent in the proposed framework. Specifically, the authors should delve into the potential biases that might be present in the generated dataset. For instance, if the instructions are generated using a specific language model, the resulting dataset might be skewed towards the characteristics of that model, potentially limiting the generalizability of the fine-tuned LLM. A detailed analysis of the types of biases that could be introduced, such as those related to specific APIs or task structures, would be valuable. Furthermore, the authors should explore methods to mitigate these biases, such as data augmentation techniques or adversarial training strategies. This would strengthen the robustness of the framework and its applicability to real-world scenarios. Additionally, a more detailed analysis of the computational cost is needed. The authors should provide a breakdown of the computational resources required for each stage of the framework, including data generation, model training, and evaluation. This would allow for a better understanding of the scalability of the framework and its feasibility for large-scale applications. The authors should also discuss the trade-offs between computational cost and performance, and how these trade-offs might affect the practical use of the framework.

To address the lack of comparison with other state-of-the-art tool-use frameworks, the authors should include a more comprehensive evaluation that benchmarks their framework against existing methods. This comparison should not only focus on the performance of the models on APIBench but also consider other metrics such as efficiency, robustness, and adaptability. For example, the authors could compare their framework with other tool-use models that have been fine-tuned on similar datasets or with other tool-use frameworks that employ different reasoning and planning strategies. This would provide a more comprehensive understanding of the strengths and weaknesses of the proposed framework and its position within the broader landscape of tool-use research. The authors should also discuss the specific advantages and disadvantages of their approach compared to these existing methods, highlighting the unique contributions of their work.

Finally, a more in-depth analysis of the error cases is crucial for understanding the limitations of the fine-tuned model. The authors should categorize the types of errors that the model makes, such as errors in API selection, errors in argument parsing, or errors in reasoning about the task. This analysis should be conducted both qualitatively and quantitatively, providing specific examples of the types of errors that the model makes. The authors should also investigate the underlying causes of these errors, such as limitations in the model's architecture, the quality of the training data, or the complexity of the tasks. This analysis would provide valuable insights into the limitations of the model and suggest directions for future research. For example, the authors could explore techniques for improving the model's ability to handle complex tasks or for mitigating the impact of biased training data. This would help to improve the robustness and generalizability of the framework.

### Questions

1. How does the proposed framework handle the potential biases in the dataset?
2. How does the proposed framework compare to other state-of-the-art tool-use frameworks?
3. What are the common patterns in the error cases of the fine-tuned model?

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
