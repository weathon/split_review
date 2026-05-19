### Summary

The paper introduces a novel approach called Self-Education via Chain-of-Thought Reasoning (SECT) that enables large language models to teach themselves new skills, specifically in performing addition. The authors demonstrate that a 582M parameter model can learn to perform addition up to 30-digit numbers without chain-of-thought reasoning, despite being initially trained only on smaller addition problems. The model achieves this through a two-stage process: supervised fine-tuning on smaller addition problems followed by self-training using self-generated data. The key innovation lies in the use of chain-of-thought reasoning as a policy improvement operator, similar to how Monte-Carlo Tree Search (MCTS) is used in AlphaZero. The paper also addresses the issue of error avalanching, where small errors in the generated data can compound and lead to incorrect training samples. The authors employ self-consistency checks and commutativity checks to filter out erroneous data and ensure the reliability of the self-generated training set. The results show that the model can progressively improve its ability to perform addition, with accuracy decreasing as the number of digits increases after self-training begins. This paper presents a significant step towards self-learning in language models, demonstrating the potential for models to autonomously discover and refine their skills without relying on external human-generated data.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The paper introduces a novel approach to self-learning in language models, specifically focusing on the ability of models to teach themselves new skills through chain-of-thought reasoning. This is a significant departure from traditional methods that rely on large amounts of human-generated training data. The concept of using chain-of-thought reasoning as a policy improvement operator is innovative and draws inspiration from successful reinforcement learning techniques, such as Monte-Carlo Tree Search (MCTS) used in AlphaZero. This approach could potentially lead to more efficient and effective ways of training language models.

2. The paper demonstrates the effectiveness of the proposed SECT method through empirical results. A 582M parameter model is shown to learn to perform addition up to 30-digit numbers without chain-of-thought reasoning, despite being initially trained only on smaller addition problems. This highlights the potential of language models to autonomously discover and refine their skills. The use of self-consistency checks and commutativity checks to filter out erroneous data is a practical solution to the problem of error avalanching, which is a common issue in self-training.

3. The paper is well-structured and clearly explains the proposed method and the experimental setup. The use of figures and tables helps to illustrate the key concepts and results. The authors provide a detailed description of the two-stage training process, including the supervised fine-tuning and self-training phases. The explanation of the self-consistency checks and commutativity checks is also clear and concise.

### Weaknesses

#### Some Related Works


#### comment

1. The paper's technical contribution is limited, as it primarily combines existing techniques such as chain-of-thought reasoning, self-consistency checks, and commutativity checks. While the application of these techniques to the problem of self-learning in language models is novel, the individual components are not new. The core idea of using chain-of-thought reasoning as a policy improvement operator, while inspired by AlphaZero, is not a fundamentally new concept. The paper could benefit from a more detailed discussion of the specific challenges and adaptations required to apply these techniques to language models, beyond simply demonstrating their effectiveness in this context.

2. The paper lacks a thorough comparison with existing methods for self-improvement in language models. While the authors mention some related work, they do not provide a detailed analysis of how their approach differs from and improves upon these methods. A more comprehensive comparison, including quantitative results and qualitative analysis, would help to better position the paper's contribution within the broader field of self-improving language models. The paper should also discuss the limitations of the proposed approach, such as its computational cost and scalability to more complex tasks.

3. The paper does not provide a detailed analysis of the computational cost and scalability of the proposed approach. The self-training process involves generating a large amount of data, which can be computationally expensive. The paper should provide a more detailed analysis of the computational resources required for training and inference, as well as the scalability of the approach to larger models and datasets. The paper should also discuss the potential for optimizing the training process to reduce computational costs.

4. The paper does not explore the potential of the proposed approach for other tasks beyond addition. While the authors mention that the method can be applied to other domains, they do not provide any empirical results or detailed discussion of the challenges and adaptations required to apply the approach to more complex tasks. The paper should discuss the potential for generalizing the approach to other tasks, such as multiplication, division, or logical reasoning, and provide a roadmap for future research in this area.

### Suggestions

The paper would benefit from a more in-depth discussion of the technical challenges and adaptations required to apply chain-of-thought reasoning as a policy improvement operator in the context of language models. While the inspiration from AlphaZero is clear, the paper should elaborate on the specific modifications and challenges encountered when adapting MCTS to the discrete nature of language models. For example, the paper could discuss the difficulties in defining a suitable search space for language models, the challenges in implementing efficient exploration strategies, and the potential for error propagation in the generated data. A more detailed analysis of these challenges would help to highlight the novelty and significance of the proposed approach. Furthermore, the paper should provide a more thorough comparison with existing methods for self-improvement in language models, including a quantitative analysis of the performance gains and a qualitative discussion of the differences in the learned representations and behaviors. This would help to better position the paper's contribution within the broader field and highlight its unique advantages.

To address the lack of computational analysis, the paper should include a detailed breakdown of the computational resources required for training and inference, including the number of GPUs, training time, and memory usage. The paper should also discuss the scalability of the approach to larger models and datasets, and provide a roadmap for optimizing the training process to reduce computational costs. For example, the paper could explore the use of techniques such as model parallelism, data parallelism, and knowledge distillation to improve the efficiency of the training process. The paper should also discuss the potential for using more efficient search algorithms, such as Monte Carlo Tree Search (MCTS) with a reduced number of simulations, to generate training data. This would help to make the approach more practical and accessible to a wider range of researchers.

Finally, the paper should provide a more detailed discussion of the potential for generalizing the approach to other tasks beyond addition. While the authors mention that the method can be applied to other domains, they do not provide any empirical results or detailed discussion of the challenges and adaptations required to apply the approach to more complex tasks. The paper should discuss the potential for adapting the self-training process to different types of tasks, such as multiplication, division, or logical reasoning, and provide a roadmap for future research in this area. For example, the paper could explore the use of different types of chain-of-thought reasoning for different tasks, and discuss the challenges in defining appropriate self-consistency checks and commutativity checks for these tasks. This would help to highlight the broader applicability of the proposed approach and encourage further research in this area.

### Questions

1. How does the proposed method compare to other approaches for self-improvement in language models, such as AlphaZero and MuZero? What are the key differences and advantages of the proposed approach?

2. What are the computational costs and scalability limitations of the proposed approach? How does the self-training process scale with model size and dataset size?

3. How can the proposed approach be generalized to other tasks beyond addition? What are the potential challenges and adaptations required to apply the approach to more complex tasks?

4. What are the limitations of the proposed approach, and what are the potential directions for future research?

### Rating

5

### Confidence

3

**********
