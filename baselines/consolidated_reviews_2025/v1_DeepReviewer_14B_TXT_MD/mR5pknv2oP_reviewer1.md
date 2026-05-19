### Summary

This paper introduces a self-learning algorithm to improve the performance of large language models. In the self-learning process, the model is first asked to generate solutions to problems using chain-of-thought reasoning. The model is then fine-tuned with these solutions, and the fine-tuned model is again augmented with chain-of-thought reasoning to solve even harder problems. This process is repeated until the model's performance fails to improve on the problem set. The proposed algorithm is evaluated on the task of addition and demonstrates the ability to improve the model's performance without the need for human-generated training data.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The paper is well-written and easy to follow.
- The idea of using chain-of-thought reasoning as a policy improvement operator is interesting.
- The proposed algorithm is shown to be effective in improving the model's performance on the task of addition.

### Weaknesses

#### Some Related Works

[1] Large Language Models Can Teach Themselves How to Reason.
[2] Language Models Can Teach Themselves to Program Better.
[3] Self-Refine: Iterative Refinement with Self-Feedback.

#### comment

 - The proposed self-learning algorithm is not compared to any existing baselines. For example, the authors could have compared their algorithm to existing self-improvement methods such as STaR [1], Leta [2], and Self-Refine [3].
- The self-learning algorithm is evaluated only on the task of addition. It would be interesting to see how the proposed approach performs on other tasks that require reasoning, such as question answering and mathematical proof generation.

### Suggestions

The lack of comparison to existing self-improvement methods is a significant weakness. While the authors present an interesting approach using chain-of-thought reasoning, it's crucial to understand how it performs relative to other methods. Specifically, the paper should include a comparison to methods like STaR [1], which also explores self-training for reasoning tasks, and Leta [2] and Self-Refine [3], which focus on iterative refinement of model outputs. A direct comparison would involve evaluating these methods on the same addition task, using the same metrics, and analyzing the differences in performance. This would help to contextualize the contribution of the proposed method and highlight its advantages and disadvantages. Furthermore, it would be beneficial to analyze the computational cost and data requirements of the proposed method compared to these baselines. Without such a comparison, it is difficult to assess the true novelty and effectiveness of the proposed approach.

The limited evaluation on only the addition task is another major concern. While addition is a fundamental operation, it may not be representative of more complex reasoning tasks. The authors should evaluate their method on a broader range of tasks that require reasoning, such as question answering datasets like CommonsenseQA or MathQA, and mathematical proof generation tasks using datasets like ProofWriter. These tasks would provide a more comprehensive evaluation of the method's ability to generalize to different types of reasoning. For example, in question answering, the model would need to understand the question, retrieve relevant information, and generate an answer, which involves a different type of reasoning than addition. Similarly, mathematical proof generation requires the model to perform a sequence of logical steps, which is a more complex form of reasoning than simple arithmetic. Evaluating on these tasks would provide a more robust assessment of the method's capabilities.

Finally, the paper should provide more details on the implementation of the proposed algorithm. For example, it would be helpful to know the specific architecture of the language model used, the details of the fine-tuning process, and the criteria used to determine when the model's performance fails to improve. It would also be beneficial to analyze the impact of different hyperparameters on the performance of the algorithm. Furthermore, the authors should provide a more detailed analysis of the generated chain-of-thought reasoning, including the quality and diversity of the generated reasoning steps. This would provide insights into how the proposed method works and how it can be improved. The authors should also discuss the limitations of the proposed method and potential directions for future research.

### Questions

- In Section 3.3.1, the authors mention that the self-training phase requires the model being able to generate both fast and slow styles of addition for numbers larger than it has seen in training. How does the model generate fast additions for larger numbers during the self-training phase when it was not explicitly trained to do so?

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
