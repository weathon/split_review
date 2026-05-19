### Summary

This paper introduces TRAM, a temporal reasoning benchmark designed to evaluate the temporal reasoning capabilities of large language models. TRAM comprises ten datasets covering various temporal aspects, including event order, arithmetic, frequency, and duration. The authors assess the performance of models like GPT-4 and Llama2 under zero-shot and few-shot conditions, comparing them to BERT-based and domain-specific baselines. Their findings reveal a notable gap between the best-performing models and human-level reasoning.

### Soundness

2 fair

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The benchmark is comprehensive, covering a wide range of temporal reasoning aspects.
3. The evaluation of multiple models provides valuable insights into the current state of temporal reasoning in LLMs.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed explanation of the data construction process, particularly regarding the construction of the dataset based on temporal reasoning. This makes it difficult to assess the quality and potential biases of the benchmark. For example, for the Ordering task, the paper mentions that incorrect choices are formed through random permutations, but it is unclear how the correct answers are determined and whether there are any potential biases in the data. Similarly, for the Frequency task, the paper does not provide details on how the different categories of problems are constructed and whether they are representative of real-world scenarios.
2. The paper does not provide sufficient information about the human evaluation process, including the number of annotators, their qualifications, and the inter-annotator agreement. This makes it difficult to assess the reliability of the human performance results. It is also unclear how the human experts were instructed to answer the questions and whether they were given any specific guidelines or training.
3. The paper does not provide a detailed error analysis, which would be helpful in understanding the specific challenges that LLMs face in temporal reasoning. The paper only provides a high-level overview of the error types, but it lacks specific examples and detailed analysis of the errors made by different models on different tasks. For example, it would be helpful to know which specific types of temporal reasoning problems are most challenging for LLMs and why.

### Suggestions

To address the lack of detail in the data construction process, the authors should provide a more thorough explanation of how each dataset was created, including the specific criteria used to determine correct answers and the methods used to generate distractors. For example, for the Ordering task, the authors should explain how they ensured that the correct order of events is always accurate and whether they considered potential biases in the source material. For the Frequency task, the authors should provide more details on how the different categories of problems were constructed and whether they are representative of real-world scenarios. It would also be beneficial to include examples of each type of problem in the appendix to illustrate the complexity and diversity of the benchmark. Furthermore, the authors should discuss any potential limitations or biases in the data and how they might affect the evaluation results. This would allow readers to better assess the validity and generalizability of the benchmark.

To improve the reliability of the human evaluation results, the authors should provide more information about the human evaluation process, including the number of annotators, their qualifications, and the inter-annotator agreement. The authors should also describe the instructions given to the human experts and whether they were given any specific guidelines or training. It would be beneficial to include a detailed description of the annotation process, including the specific criteria used to determine correct answers and how disagreements between annotators were resolved. This would allow readers to better assess the reliability and validity of the human performance results. Additionally, the authors should consider using a larger number of annotators and calculating inter-annotator agreement metrics such as Cohen's kappa to provide a more objective measure of the reliability of the human annotations.

To provide a more detailed error analysis, the authors should include a more in-depth analysis of the errors made by different models on different tasks. This should include specific examples of the types of errors that LLMs tend to make and a discussion of the underlying reasons for these errors. For example, the authors could analyze the performance of different models on specific types of temporal reasoning problems, such as those involving complex event sequences or ambiguous temporal expressions. The authors should also discuss the implications of these errors for the development of more robust temporal reasoning models. This would provide valuable insights into the specific challenges that LLMs face in temporal reasoning and help guide future research in this area.

### Questions

1. Could you provide more details on the construction of the dataset, specifically how you ensured the quality and diversity of the temporal reasoning challenges?
2. Can you elaborate on the human evaluation process, including the number of annotators, their qualifications, and the inter-annotator agreement?
3. How do you envision TRAM influencing the development of future LLMs, and what are the next steps for research in this area?

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
