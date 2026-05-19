### Summary

This paper introduces SECToR (Self-Education via Chain-of-Thought Reasoning), a method that enables language models to teach themselves new skills using chain-of-thought reasoning. The authors demonstrate that language models can learn to solve addition problems up to 29 digits without access to ground truth examples beyond an initial supervised fine-tuning phase. The central hypothesis is that chain-of-thought reasoning can act as a policy improvement operator, similar to how Monte-Carlo Tree Search is used in AlphaZero.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper introduces a novel approach to self-learning in language models using chain-of-thought reasoning, which has the potential to significantly reduce the reliance on human-generated training data.
2. The method is evaluated on a benchmark task (addition) and shows promising results, with the model achieving 98%+ accuracy on up to 29-digit addition problems.
3. The paper provides a clear and detailed description of the method, including the self-training loop and the use of self-consistency checks to mitigate error avalanching.

### Weaknesses

#### Some Related Works


#### comment

1. The method is evaluated only on the task of addition, which is a relatively simple task. It is not clear how well the method would generalize to more complex tasks. The current evaluation lacks a rigorous analysis of the method's performance on tasks with varying levels of complexity, such as those involving multiple steps, logical reasoning, or symbolic manipulation. The limited scope of the evaluation makes it difficult to assess the true potential of the approach.
2. The paper does not compare the proposed method to any other existing methods. It is not clear how the proposed method compares to other methods in terms of performance and efficiency. Without a comparative analysis against established baselines, it is challenging to determine the relative advantages and disadvantages of the proposed approach. This makes it difficult to contextualize the contribution of the work.
3. The paper does not provide any analysis of the limitations of the proposed method. It is important to understand the limitations of a method to be able to use it effectively. The absence of a discussion on the potential failure modes, computational costs, and sensitivity to hyperparameters makes it difficult to assess the practical applicability of the method. A thorough analysis of the limitations is crucial for understanding the scope and potential impact of the work.

### Suggestions

To address the limitations of the current evaluation, the authors should consider expanding their experiments to include a more diverse set of tasks that vary in complexity and reasoning requirements. For example, tasks involving symbolic manipulation, logical inference, or multi-step problem-solving could provide a more comprehensive assessment of the method's generalization capabilities. Furthermore, it would be beneficial to analyze the performance of the method on tasks with varying levels of noise or ambiguity to understand its robustness. This could involve introducing errors in the input data or using more complex and less structured problem statements. Such an analysis would provide a more nuanced understanding of the method's strengths and weaknesses and its potential for real-world applications. The authors should also consider using established benchmark datasets for these tasks to facilitate comparisons with other methods.

To better contextualize the performance of the proposed method, the authors should compare it to existing approaches for self-learning and chain-of-thought reasoning. This comparison should include both quantitative and qualitative analyses. Quantitatively, the authors should compare the performance of their method to other methods on the same tasks, using appropriate metrics. Qualitatively, they should analyze the differences in the reasoning processes employed by different methods and discuss the advantages and disadvantages of each approach. This comparison should also include an analysis of the computational cost and efficiency of the different methods. This would provide a more complete picture of the method's performance relative to other approaches and help to identify its unique contributions.

Finally, the authors should provide a more thorough analysis of the limitations of their method. This analysis should include a discussion of the potential failure modes, computational costs, and sensitivity to hyperparameters. The authors should also discuss the assumptions that the method makes and the conditions under which it is likely to perform well or poorly. This analysis should be supported by empirical evidence and should provide specific examples of cases where the method fails or performs poorly. This would help to identify areas for future research and provide a more complete understanding of the method's capabilities and limitations.

### Questions

1. How does the proposed method compare to other existing methods in terms of performance and efficiency?
2. How well does the proposed method generalize to more complex tasks?
3. What are the limitations of the proposed method, and what are the potential directions for future research?

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
