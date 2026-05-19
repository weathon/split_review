### Summary

This paper introduces TRAM, a benchmark designed to evaluate temporal reasoning (TeR) in large language models (LLMs). TRAM comprises ten distinct tasks across various temporal aspects, including order, frequency, duration, typical time, arithmetic, and causality. The benchmark evaluates both LLMs and BERT-based models using multiple-choice questions, with human performance serving as an upper bound. The results show that GPT-4 outperforms other models, including Llama2 and RoBERTa, but still falls significantly short of human performance. The authors highlight the need for further research to improve LLMs' temporal reasoning capabilities.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

- Temporal reasoning is an important capability for LLMs, and this paper contributes a comprehensive benchmark that covers a wide range of temporal tasks.
- The benchmark includes a diverse set of tasks, from basic temporal ordering to more complex reasoning involving arithmetic, causality, and temporal NLP. This breadth allows for a thorough evaluation of LLMs' temporal reasoning abilities.
- The paper provides detailed experimental results, comparing various LLMs and BERT-based models. The analysis of error types and the comparison with human performance offer valuable insights into the current limitations of LLMs in temporal reasoning.

### Weaknesses

#### Some Related Works


#### comment

 - The benchmark primarily uses multiple-choice questions, which may not fully capture the nuances of temporal reasoning in open-ended scenarios. The multiple-choice format, while convenient for evaluation, limits the assessment of models' ability to generate or interpret complex temporal sequences, which is a crucial aspect of real-world temporal reasoning.
- The paper could benefit from a more in-depth discussion of the limitations of the current benchmark and potential biases in the datasets used. Specifically, the paper does not address potential biases in the datasets, such as an over-representation of certain types of temporal events or a lack of diversity in the time periods represented. This could lead to models that are not generalizable to real-world scenarios.
- While the paper compares various models, it does not explore the impact of different prompting strategies or fine-tuning techniques on temporal reasoning performance. The choice of prompting strategies is limited, and the paper does not investigate the effect of different fine-tuning techniques, such as task-specific fine-tuning or data augmentation, on the models' temporal reasoning capabilities. This limits the practical implications of the benchmark.
- The evaluation metrics are primarily accuracy and F1 score, which may not fully capture the complexity of temporal reasoning tasks. For example, in tasks involving temporal arithmetic, the model might arrive at the correct answer through an incorrect reasoning process, and the metrics do not distinguish between these cases. Similarly, for temporal NLP tasks, the model might select a correct answer based on superficial cues rather than a deep understanding of the temporal relationships.

### Suggestions

The authors should consider expanding the benchmark to include open-ended question-answering tasks that require models to generate temporal sequences or explain their reasoning processes. This would provide a more comprehensive evaluation of temporal reasoning capabilities. For example, instead of multiple-choice questions, the benchmark could include tasks where models are asked to generate a timeline of events based on a given description or to explain the temporal relationships between different events. This would better assess the models' ability to understand and manipulate temporal information in a more nuanced way. Furthermore, the authors should explore the use of more fine-grained evaluation metrics that can capture the quality of the generated temporal sequences, such as metrics that measure the accuracy of the generated timeline or the correctness of the explanations provided by the model. This would provide a more detailed understanding of the models' strengths and weaknesses in temporal reasoning.

To address the limitations of the current benchmark, the authors should conduct a thorough analysis of potential biases in the datasets and propose strategies to mitigate these biases. This could involve techniques such as data augmentation, re-weighting, or the use of diverse datasets that cover a wider range of time periods and event types. The authors should also investigate the impact of different prompting strategies and fine-tuning techniques on the models' temporal reasoning performance. This could involve experimenting with different types of prompts, such as chain-of-thought prompting, and fine-tuning the models on specific temporal reasoning tasks. The authors should also explore the use of data augmentation techniques to improve the models' generalization capabilities. This would help to ensure that the models are not overfitting to the specific characteristics of the benchmark datasets and can generalize to real-world scenarios.

Finally, the authors should consider incorporating more complex temporal reasoning tasks that involve multiple interacting temporal constraints. For example, the benchmark could include tasks that require models to reason about the temporal relationships between events that are governed by different types of temporal constraints, such as causal relationships, periodic events, and temporal hierarchies. This would provide a more comprehensive evaluation of the models' ability to handle complex temporal reasoning scenarios. The authors should also explore the use of more advanced evaluation metrics that can capture the complexity of these tasks, such as metrics that measure the accuracy of the model's reasoning process or the correctness of the generated temporal sequences. This would provide a more detailed understanding of the models' strengths and weaknesses in handling complex temporal reasoning tasks.

### Questions

- How do you ensure that the multiple-choice questions do not introduce unintended biases or shortcuts in the evaluation process?
- Can you provide more details on the human evaluation process, including the number of participants, their expertise, and the instructions they received?
- Have you considered expanding the benchmark to include open-ended question-answering tasks that require models to generate temporal sequences or explain their reasoning processes?

### Rating

6

### Confidence

4

**********
