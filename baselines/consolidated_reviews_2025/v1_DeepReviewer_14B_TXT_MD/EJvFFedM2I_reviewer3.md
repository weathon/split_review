### Summary

The paper introduces a new benchmark for evaluating the temporal reasoning capabilities of large language models. The benchmark consists of ten tasks, each with a different focus on temporal reasoning, such as ordering, frequency, duration, and causality. The authors evaluate several popular LLMs, including GPT-4 and Llama2, on the benchmark and compare their performance to human experts. The results show that even the best-performing model lags behind human performance, highlighting the need for further research in this area.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper introduces a new benchmark for evaluating the temporal reasoning capabilities of LLMs, which is an important area of research.
2. The benchmark consists of ten tasks, each with a different focus on temporal reasoning, providing a comprehensive evaluation of LLMs' capabilities in this area.
3. The authors evaluate several popular LLMs on the benchmark and compare their performance to human experts, providing valuable insights into the strengths and weaknesses of these models.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the errors made by the models, which could help in identifying the specific areas where they struggle.
2. The paper does not discuss the potential biases in the benchmark, which could affect the results.
3. The paper does not provide a detailed analysis of the computational resources required to run the benchmark, which could be a concern for researchers with limited resources.

### Suggestions

The paper would benefit from a more in-depth error analysis, going beyond simply identifying the task categories where models struggle. For instance, within the 'ordering' task, it would be valuable to analyze whether models have difficulty with specific types of temporal relationships (e.g., simultaneous events, causally linked events, or events with implicit temporal dependencies). Similarly, for the 'frequency' task, are models struggling with specific time units (e.g., seconds vs. years) or with complex frequency expressions (e.g., 'every other day')? A fine-grained error analysis, perhaps using a confusion matrix to show the distribution of errors across different sub-categories within each task, would provide much more actionable insight into the models' limitations and guide future research efforts. This analysis should also consider the types of linguistic cues that models fail to utilize, such as temporal conjunctions or adverbs, and how these failures contribute to incorrect reasoning.

Regarding potential biases, the paper should explore the demographic or cultural biases that might be present in the benchmark. For example, if the benchmark relies heavily on events or scenarios that are common in Western cultures, models trained on data from other cultures might perform poorly, not due to a lack of temporal reasoning ability, but due to a lack of cultural knowledge. The authors should investigate the diversity of the benchmark in terms of the sources of the data, the types of events, and the cultural contexts. Furthermore, the paper should discuss the potential for annotation bias, where the human experts who created the benchmark might have introduced their own biases into the evaluation data. This could be addressed by analyzing the inter-annotator agreement and by comparing the benchmark to other existing datasets in the field. A thorough discussion of these potential biases is crucial for ensuring the validity and generalizability of the benchmark.

Finally, the paper should provide a more detailed analysis of the computational resources required to run the benchmark. This should include not only the total time but also the memory requirements, the number of GPUs needed, and the specific hardware configurations used for the experiments. The authors should also discuss the scalability of the benchmark, i.e., how the computational cost increases with the number of models being evaluated or the size of the benchmark. This information is essential for researchers who want to use the benchmark, especially those with limited computational resources. The paper should also explore the possibility of optimizing the benchmark to reduce its computational cost, such as by using more efficient evaluation methods or by creating a smaller, more manageable subset of the benchmark that still captures the core challenges of temporal reasoning.

### Questions

1. Can you provide more details on the error analysis of the models? What are the most common types of errors made by the models, and what do these errors suggest about their limitations in temporal reasoning?
2. How do you address the potential biases in the benchmark, and how do you ensure that the results are not affected by these biases?
3. Can you provide more details on the computational resources required to run the benchmark, and how can researchers with limited resources use the benchmark effectively?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
