### Summary

This paper proposes a method to reduce hallucinations in LLMs by contrasting the outputs of the original and masked input. The authors evaluate their method on several QA datasets and show that it can improve performance on context-rich datasets.

### Soundness

3

### Presentation

2

### Contribution

2

### Strengths

- The method is simple and easy to understand
- The method is evaluated on several datasets

### Weaknesses

#### Some Related Works


#### comment

 - The paper is not well written and is hard to follow
- The evaluation is limited to QA datasets and does not include other types of tasks
- The method is not compared to other methods for reducing hallucinations

### Suggestions

The paper would benefit significantly from a more thorough evaluation beyond question-answering tasks. While QA datasets are relevant, the method's effectiveness on other tasks, such as text summarization, translation, or code generation, remains unclear. The authors should consider evaluating their method on a diverse set of tasks to demonstrate its general applicability. For example, in text summarization, the method could be tested on datasets like CNN/DailyMail or XSum, and the performance could be compared against existing summarization models. Similarly, for code generation, the authors could use datasets like HumanEval or MBPP, and compare their method against established code generation techniques. This would provide a more comprehensive understanding of the method's strengths and weaknesses.

Furthermore, the paper lacks a comparison with existing methods for reducing hallucinations. While the authors mention that their method is inspired by contrastive decoding, they do not provide a detailed comparison with other relevant techniques. For instance, methods that use adversarial training or reinforcement learning to mitigate hallucinations should be considered as baselines. The authors should also compare their method with techniques that explicitly model uncertainty or use ensemble methods to reduce hallucination. A thorough comparison with these methods would help to position the proposed method within the existing literature and highlight its unique contributions. This comparison should include both quantitative metrics and qualitative analysis of the generated outputs.

Finally, the paper needs to be significantly improved in terms of writing and clarity. The current presentation makes it difficult to understand the proposed method and its contributions. The authors should provide a more detailed explanation of the method, including the specific masking strategies used and the rationale behind their design choices. The experimental setup should also be described in more detail, including the specific datasets used, the evaluation metrics, and the hyperparameter settings. The authors should also provide a more thorough analysis of the results, including a discussion of the limitations of their method and potential directions for future research. The paper should be written in a clear and concise manner, with proper grammar and spelling.

### Questions

- How does the method perform on tasks other than QA?
- How does the method compare to other methods for reducing hallucinations?

### Rating

5

### Confidence

3

**********
