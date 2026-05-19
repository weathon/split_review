### Summary

This paper introduces TRAM, a benchmark designed to evaluate the temporal reasoning capabilities of large language models (LLMs). The benchmark comprises ten distinct tasks that cover various aspects of temporal reasoning, including foundational understanding, temporal interpretation and computation, and advanced temporal and conceptual understanding. The authors evaluate several prominent LLMs, including BERT-style models, RoBERTa-large, and Llama2, on TRAM. The results reveal that while the best-performing model, GPT-4, achieves a high average accuracy of 84.4%, it still falls short of human performance by a significant margin, with human accuracy ranging from 86.0% to 96.3%. The paper highlights the need for further research in improving the temporal reasoning capabilities of LLMs.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a comprehensive benchmark, TRAM, that covers a wide range of temporal reasoning tasks. The tasks are well-structured and designed to evaluate different aspects of temporal reasoning, from basic understanding to more complex reasoning involving arithmetic, causality, and temporal NLP.

2. The paper provides a thorough evaluation of several prominent LLMs, including BERT-style models, RoBERTa-large, and Llama2. The results are presented clearly, and the authors provide detailed error analysis to identify the strengths and weaknesses of each model.

3. The paper highlights the need for further research in improving the temporal reasoning capabilities of LLMs. The authors provide valuable insights into the limitations of current models and suggest potential directions for future research.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the types of errors made by the models. While the authors mention that models often struggle with subtle details and hidden clues across all categories, a more granular analysis of the errors would be beneficial. For example, it would be helpful to know if the models struggle more with certain types of temporal reasoning tasks or if there are specific patterns in the errors that could inform future research.

2. The paper does not explore the impact of different prompting strategies on the performance of the models. The authors mention that they use greedy decoding with a temperature of 0, but they do not explore the impact of other prompting strategies, such as chain-of-thought prompting, which has been shown to improve the performance of LLMs on reasoning tasks. It would be valuable to see how different prompting strategies affect the performance of the models on TRAM.

3. The paper does not provide a detailed discussion of the limitations of the benchmark. While the authors mention that the benchmark covers a wide range of temporal reasoning tasks, they do not discuss the potential biases or limitations of the benchmark. For example, it would be helpful to know if the benchmark is biased towards certain types of temporal reasoning tasks or if there are any limitations in the types of questions that can be asked.

### Suggestions

The paper would benefit from a more in-depth error analysis. Instead of just stating that models struggle with subtle details, the authors should categorize the errors more specifically. For instance, are there specific types of temporal relationships (e.g., before/after, during/while, consecutive events) that models find particularly challenging? Are there errors related to the understanding of temporal quantifiers (e.g., always, sometimes, never)? A detailed breakdown of error types, perhaps using a confusion matrix or a similar visualization, would provide valuable insights into the specific weaknesses of the models. Furthermore, the authors could analyze the correlation between error types and the complexity of the tasks. This would help to identify if certain types of temporal reasoning are more prone to errors than others and could guide future research efforts.

To address the lack of exploration of prompting strategies, the authors should conduct a more systematic evaluation of different prompting techniques. While greedy decoding with a temperature of 0 is a reasonable starting point, it is important to investigate whether more sophisticated prompting methods, such as chain-of-thought prompting, can improve the performance of the models on TRAM. The authors could experiment with different variations of chain-of-thought prompting, such as varying the number of reasoning steps or the way the reasoning steps are presented. They could also explore other prompting strategies, such as few-shot prompting or self-consistency prompting. A thorough analysis of the impact of different prompting strategies would provide valuable insights into how to best leverage the temporal reasoning capabilities of LLMs.

Finally, the paper should include a more detailed discussion of the limitations of the benchmark. While the authors mention that the benchmark covers a wide range of temporal reasoning tasks, they should also discuss the potential biases or limitations of the benchmark. For example, are there any limitations in the types of questions that can be asked? Are there any biases in the dataset that could affect the evaluation results? The authors should also discuss the potential for the benchmark to be gamed by models that are specifically trained on the benchmark. A thorough discussion of the limitations of the benchmark would help to ensure that the results are interpreted correctly and that future research is guided by realistic expectations.

### Questions

1. Could you provide more details on the types of errors made by the models? Are there specific types of temporal reasoning tasks that the models struggle with the most?

2. Have you explored the impact of different prompting strategies on the performance of the models? If so, what were the results?

3. What are the limitations of the benchmark? Are there any potential biases or limitations that could affect the evaluation results?

### Rating

8

### Confidence

4

**********
