### Summary

This paper introduces a new benchmark, MMA, to evaluate the performance of MLLMs on ambiguous contexts. The benchmark consists of 261 textual contexts and questions with ambiguous meaning, categorized into lexical, syntactic, and semantic ambiguities. The authors evaluate 24 MLLMs on this benchmark and find that they often overlook scenario-specific visual information, perform worst under syntactic ambiguity, and that open-sourced models generally perform lower than proprietary MLLMs.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

- The paper introduces a new benchmark that fills a gap in the evaluation of MLLMs, as it tests the models' ability to integrate visual information to resolve textual ambiguities, which has been a largely untested area in previous benchmarks.
- The paper provides a comprehensive evaluation of 24 MLLMs, including both proprietary and open-sourced models, which gives a broad view of the current state of MLLMs' performance on ambiguous contexts.

### Weaknesses

#### Some Related Works


#### comment

 - The benchmark size is relatively small, with only 261 questions, and the distribution of ambiguity types is not balanced (only 20 questions for semantic ambiguity). This limits the comprehensiveness of the benchmark and may not fully represent the complexity of real-world scenarios.
- The paper only tests each model once, and the error analysis is not very deep. For example, it is unclear whether the errors are due to the models' inability to understand the text, the visual information, or the interaction between the two.
- The paper does not provide a detailed analysis of the difficulty of each question, which makes it difficult to understand the specific challenges that each question poses to the models.
- The paper does not provide a detailed analysis of the error cases, which makes it difficult to understand the specific types of errors that the models are making.
- The paper does not provide a detailed analysis of the performance of the models on different types of questions, which makes it difficult to understand the specific strengths and weaknesses of the models.

### Suggestions

The authors should consider expanding the benchmark to include a more balanced distribution of ambiguity types, especially for semantic ambiguity, which is currently underrepresented. The small number of semantic ambiguity questions limits the ability to draw strong conclusions about model performance in this area. A larger, more balanced dataset would provide a more robust evaluation of MLLMs' ability to handle different types of ambiguities. Furthermore, the authors should investigate the possibility of creating more fine-grained categories within each ambiguity type to capture the nuances of different types of ambiguities. For example, within syntactic ambiguity, they could differentiate between prepositional phrase attachment and coordination ambiguity, as these may pose different challenges to MLLMs. This would allow for a more detailed analysis of model performance and a better understanding of the specific types of ambiguities that are most challenging for MLLMs.

To improve the error analysis, the authors should conduct a more in-depth investigation into the causes of errors. This could involve analyzing the attention maps of the models to understand which parts of the input are being attended to when making predictions. It would also be helpful to categorize the errors into different types, such as errors due to misinterpretation of the text, errors due to misinterpretation of the visual information, and errors due to misintegration of the text and visual information. This would provide a more detailed understanding of the specific types of errors that the models are making and would help to identify areas for improvement. Additionally, the authors should consider conducting ablation studies to determine the contribution of different components of the MLLMs to performance on the benchmark. For example, they could remove the visual encoder or the text encoder to see how this affects performance. This would help to identify the specific components that are most important for handling ambiguities.

Finally, the authors should provide a more detailed analysis of the difficulty of each question and the performance of the models on different types of questions. This could involve assigning difficulty scores to each question based on the performance of the models and analyzing the correlation between difficulty and ambiguity type. It would also be helpful to analyze the performance of the models on different types of questions to identify the specific strengths and weaknesses of each model. For example, some models may perform better on lexical ambiguities, while others may perform better on syntactic ambiguities. This would provide a more nuanced understanding of the performance of the models and would help to identify areas for improvement. The authors should also consider including more challenging questions in the benchmark to better evaluate the limits of MLLMs' ability to handle ambiguities.

### Questions

- How did you ensure the quality and accuracy of the text-only questions? Did you conduct any pilot studies or expert reviews to validate the questions?
- How did you select the images to pair with each question? What criteria did you use to ensure that the images accurately represented the different interpretations of the ambiguities?
- What are the limitations of using generated images in the benchmark? Could the use of generated images introduce any biases or inaccuracies in the evaluation of the models?
- How did you ensure that the human evaluation was accurate and reliable? What measures did you take to train the annotators and ensure the quality of their annotations?

### Rating

3

### Confidence

4

**********
