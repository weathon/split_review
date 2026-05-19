### Summary

The paper introduces TRAM, a benchmark for evaluating temporal reasoning in large language models (LLMs). It includes ten tasks that cover various aspects of temporal understanding, such as order, frequency, duration, and causality. The benchmark uses multiple-choice questions and evaluates models like GPT-4 and Llama2. The results show that while GPT-4 performs well, there's still a significant gap between model performance and human capabilities, highlighting the need for further research in this area.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The benchmark is comprehensive, covering a wide range of temporal reasoning tasks.
3. The authors conduct extensive experiments on multiple LLMs and analyze the error types and limitations of these models.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide detailed information on how the test set was selected, and whether the test set was randomly sampled from the entire dataset or if there was any stratification based on task type or difficulty level. This lack of transparency makes it difficult to assess the representativeness of the test set and raises concerns about potential biases in the evaluation results. For example, if certain tasks or question types are overrepresented in the test set, the reported performance might not accurately reflect the model's overall capabilities across the entire benchmark.
2. The paper does not provide sufficient details on the human evaluation process, such as the number of human annotators, their expertise, and the instructions they received. Without this information, it is difficult to assess the reliability and validity of the human performance baseline. The lack of detail makes it hard to determine if the human evaluation was conducted rigorously and if the reported human performance is a reliable upper bound for the task.

### Suggestions

To address the lack of transparency regarding the test set selection, the authors should provide a detailed description of the sampling strategy used. This should include the exact method used to select the test set, whether it was a random sample or a stratified sample based on task type or difficulty, and the criteria used for stratification if any. Furthermore, the authors should report the distribution of question types and difficulty levels in the test set to allow for a more thorough evaluation of the model's performance. It would also be beneficial to include an analysis of how the test set compares to the training set in terms of these characteristics. This would help to ensure that the test set is representative of the overall benchmark and that the evaluation results are not biased by any specific characteristics of the test set. For example, if the test set contains a disproportionately high number of questions from a particular task, the reported performance might not accurately reflect the model's overall capabilities.

To improve the reliability and validity of the human performance baseline, the authors should provide a detailed description of the human evaluation process. This should include the number of human annotators involved, their expertise in temporal reasoning, and the specific instructions they received. It would also be helpful to describe the annotation guidelines and the measures taken to ensure consistency and accuracy in the annotations. The authors should also report the inter-annotator agreement, which would provide a measure of the reliability of the human performance baseline. Furthermore, it would be beneficial to include examples of the questions and the corresponding human annotations, which would help to understand the complexity of the task and the challenges involved in human evaluation. This would allow other researchers to reproduce the human evaluation and to compare their results with the reported human performance.

Finally, the authors should consider including a more detailed analysis of the error types made by the models. This analysis should go beyond simply reporting the overall accuracy and should provide insights into the specific types of errors that the models are making. For example, are the models struggling with specific types of temporal reasoning tasks, or are they making errors due to a lack of understanding of the underlying temporal concepts? This analysis would help to identify the specific areas where the models need improvement and would provide a more nuanced understanding of their capabilities and limitations. The authors could also explore the use of error analysis techniques to identify patterns in the errors and to develop targeted strategies for improving the models' performance.

### Questions

See above.

### Rating

6

### Confidence

4

**********
