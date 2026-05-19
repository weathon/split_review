### Summary

This paper introduces SECT, a method for enabling language models to teach themselves new skills, specifically in the domain of addition. SECT leverages chain-of-thought reasoning as a policy improvement operator, drawing an analogy to AlphaZero's use of MCTS. The model undergoes a two-stage training process: supervised fine-tuning followed by self-training using self-generated data. The authors demonstrate that a 582M parameter model can learn to perform addition with up to 30-digit numbers without chain-of-thought reasoning, despite being initially trained only on smaller addition problems. The paper also addresses the issue of error avalanching, where small errors in the generated data can compound and lead to incorrect training samples. The authors employ self-consistency checks and commutativity checks to filter out erroneous data and ensure the reliability of the self-generated training set.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

- The paper introduces a novel approach to self-learning in language models, specifically focusing on the ability of models to teach themselves new skills through chain-of-thought reasoning. This is a significant departure from traditional methods that rely on large amounts of human-generated training data. The concept of using chain-of-thought reasoning as a policy improvement operator is innovative and draws inspiration from successful reinforcement learning techniques, such as Monte-Carlo Tree Search (MCTS) used in AlphaZero. This approach could potentially lead to more efficient and effective ways of training language models.
- The paper demonstrates the effectiveness of the proposed SECT method through empirical results. A 582M parameter model is shown to learn to perform addition up to 30-digit numbers without chain-of-thought reasoning, despite being initially trained only on smaller addition problems. This highlights the potential of language models to autonomously discover and refine their skills. The use of self-consistency checks and commutativity checks to filter out erroneous data is a practical solution to the problem of error avalanching, which is a common issue in self-training.
- The paper is well-structured and clearly explains the proposed method and the experimental setup. The use of figures and tables helps to illustrate the key concepts and results. The authors provide a detailed description of the two-stage training process, including the supervised fine-tuning and self-training phases. The explanation of the self-consistency checks and commutativity checks is also clear and concise.

### Weaknesses

#### Some Related Works


#### comment

 - The paper's technical contribution is limited, as it primarily combines existing techniques such as chain-of-thought reasoning, self-consistency checks, and commutativity checks. While the application of these techniques to the problem of self-learning in language models is novel, the individual components are not new. The core idea of using chain-of-thought reasoning as a policy improvement operator, while inspired by AlphaZero, is not a fundamentally new concept. The paper could benefit from a more detailed discussion of the specific challenges and adaptations required to apply these techniques to language models, beyond simply demonstrating their effectiveness in this context.
- The paper lacks a thorough comparison with existing methods for self-improvement in language models. While the authors mention some related work, they do not provide a detailed analysis of how their approach differs from and improves upon these methods. A more comprehensive comparison, including quantitative results and qualitative analysis, would help to better position the paper's contribution within the broader field of self-improving language models. The paper should also discuss the limitations of the proposed approach, such as its computational cost and scalability to more complex tasks.
- The paper does not provide a detailed analysis of the computational cost and scalability of the proposed approach. The self-training process involves generating a large amount of data, which can be computationally expensive. The paper should provide a more detailed analysis of the computational resources required for training and inference, as well as the scalability of the approach to larger models and datasets. The paper should also discuss the potential for optimizing the training process to reduce computational costs.

### Suggestions

The paper would benefit from a more in-depth discussion of the specific challenges and adaptations required to apply chain-of-thought reasoning as a policy improvement operator within the context of language models. While the analogy to AlphaZero's MCTS is clear, the paper should elaborate on the unique difficulties of applying this technique to discrete token sequences, as opposed to continuous game states. For instance, how does the paper address the issue of defining a suitable search space for language models, given their discrete nature? What are the specific modifications or challenges encountered when implementing efficient exploration strategies in this domain? Furthermore, the paper should discuss the potential for error propagation in the generated data and how the proposed self-consistency and commutativity checks mitigate this issue. A more detailed explanation of these adaptations would strengthen the paper's contribution and highlight its novelty.

To better position the paper's contribution, a more thorough comparison with existing methods for self-improvement in language models is needed. The paper should include a quantitative analysis of the performance of the proposed approach compared to other self-improvement techniques, such as those based on reinforcement learning or adversarial training. A qualitative analysis of the learned representations and behaviors would also be valuable. The paper should discuss the limitations of the proposed approach, such as its computational cost and scalability to more complex tasks. For example, how does the computational cost of the self-training process scale with the size of the model and the amount of generated data? What are the potential bottlenecks in the training process, and how can they be addressed? A more detailed discussion of these limitations would provide a more balanced view of the paper's contribution and guide future research in this area.

Finally, the paper should include a more detailed analysis of the computational cost and scalability of the proposed approach. The paper should provide a breakdown of the computational resources required for each stage of the training process, including the supervised fine-tuning and self-training phases. This should include the number of GPUs, training time, and memory usage. The paper should also discuss the potential for optimizing the training process to reduce computational costs. For example, what are the trade-offs between the number of self-training steps and the final performance of the model? How can the training process be parallelized to reduce the overall training time? A more detailed analysis of these aspects would make the paper more practical and accessible to a wider range of researchers.

### Questions

Please refer to the weaknesses section.

### Rating

6

### Confidence

3

**********
