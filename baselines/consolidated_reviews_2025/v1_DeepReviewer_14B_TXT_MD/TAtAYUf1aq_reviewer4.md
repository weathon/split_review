### Summary

The paper introduces Memoria, a memory network that applies Hebbian theory to enhance long-term dependencies in neural networks. Memoria stores and retrieves information called engram at multiple memory levels of working memory, short-term memory, and long-term memory, using connection weights that change according to Hebb's rule. Through experiments with popular Transformer-based models like BERT and GPT, the paper presents that Memoria significantly improves the ability to consider long-term dependencies in various tasks.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The paper introduces a novel memory network that applies Hebbian theory to enhance long-term dependencies in neural networks.
3. The paper presents experimental results that demonstrate the effectiveness of Memoria in various tasks.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could benefit from a more detailed explanation of the Hebbian theory and how it is applied in Memoria.
2. The paper could provide more details on the implementation of Memoria and the experimental setup.
3. The paper could include a more thorough analysis of the results and a discussion of the limitations of Memoria.

### Suggestions

The paper would significantly benefit from a more detailed explanation of Hebbian theory, specifically how the 'fire together, wire together' principle is translated into the connection weight updates within Memoria. While the paper mentions that connection weights change according to Hebb's rule, it lacks a concrete mathematical formulation of this rule within the context of the memory network. For instance, it would be helpful to see the exact equations used to update the connection weights between engrams, including the learning rate and any other relevant parameters. Furthermore, the paper should clarify how the co-activation of engrams is measured and how this measurement influences the weight updates. A more rigorous explanation of the Hebbian learning mechanism would greatly enhance the paper's clarity and allow for a better understanding of the proposed method.

To improve the reproducibility and understanding of the experimental results, the paper should provide a more detailed description of the implementation of Memoria. This includes specifying the architecture of the memory network, such as the number of engrams at each memory level (working, short-term, and long-term), the dimensionality of the engram vectors, and the specific activation functions used. The paper should also provide details on the training procedure, including the optimization algorithm, the learning rate schedule, and the batch size. Furthermore, the paper should clarify how Memoria is integrated with the Transformer-based models like BERT and GPT. For example, it would be beneficial to know how the engrams are extracted from the Transformer's hidden states and how the memory read and write operations are performed. A more detailed description of the implementation would allow other researchers to replicate the results and build upon the proposed method.

Finally, the paper should include a more thorough analysis of the results, going beyond simply stating that Memoria improves the ability to consider long-term dependencies. The paper should provide a detailed analysis of the performance of Memoria on different tasks and datasets, including a comparison with other memory-augmented neural networks. It would be beneficial to see a breakdown of the performance gains, showing how much each memory level contributes to the overall improvement. Furthermore, the paper should discuss the limitations of Memoria, such as its computational cost, its sensitivity to hyperparameters, and its potential for overfitting. A more thorough analysis of the results and a discussion of the limitations would provide a more balanced and insightful evaluation of the proposed method.

### Questions

1. How does Memoria compare to other memory-augmented neural networks?
2. What are the computational and memory requirements of Memoria?
3. How does Memoria handle noisy or incomplete data?
4. What are the potential applications of Memoria beyond the tasks presented in the paper?

### Rating

6

### Confidence

3

**********
