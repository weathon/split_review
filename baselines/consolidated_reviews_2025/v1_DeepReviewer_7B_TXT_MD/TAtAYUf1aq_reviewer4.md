### Summary

This paper proposes a memory network Memoria that applies Hebbian theory to enhance long-term dependencies in neural networks. Memoria stores and retrieves information called engrams at multiple memory levels of working memory, short-term memory, and long-term memory, using connection weights that change according to Hebb's rule. Memoria is a separate module that can be used with various sequence processing models. The authors demonstrate that Memoria outperforms existing methodologies in sorting, language modeling, and text classification tasks.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

- Memoria is a novel memory network that applies Hebbian theory to enhance long-term dependencies in neural networks. It stores and retrieves information called engrams at multiple memory levels of working memory, short-term memory, and long-term memory, using connection weights that change according to Hebb's rule.
- Memoria is a separate module that can be used with various sequence processing models. The authors demonstrate that Memoria outperforms existing methodologies in sorting, language modeling, and text classification tasks.

### Weaknesses

#### Some Related Works


#### comment

 - The paper is not well-written and is hard to understand. The motivation of the paper is not clear.
- The proposed memory model is evaluated on very simple tasks, and the improvements over the baselines are small.
- The paper does not discuss the computational cost of the proposed model.

### Suggestions

The paper needs significant improvements in clarity and motivation. The introduction should clearly articulate the limitations of current Transformer models in handling long-range dependencies and how the proposed Hebbian-inspired memory module addresses these limitations. The connection between the Hebbian learning rule and the specific implementation details of the working, short-term, and long-term memory components needs to be much more explicit. For example, the paper should explain how the Hebbian update rule is applied to the connections between these memory modules, and how this relates to the concept of long-term potentiation. The paper should also provide a more detailed explanation of the memory graph and how the DFS algorithm is used to retrieve information from the long-term memory. Without these clarifications, the proposed model remains difficult to understand and evaluate.

The evaluation of the proposed model needs to be significantly strengthened. The current tasks, sorting and simple language modeling, are not sufficient to demonstrate the effectiveness of the proposed memory module. The paper should include more challenging tasks that require long-range dependencies, such as long document summarization, question answering over long texts, or tasks that involve complex reasoning. The improvements over the baselines are indeed small, and it is not clear if these improvements are statistically significant. The paper should provide a more thorough statistical analysis of the results, including confidence intervals and p-values. Furthermore, the paper should compare the proposed model with other memory-augmented Transformer models, not just the standard Transformer. This would provide a better understanding of the advantages and disadvantages of the proposed approach. The paper should also discuss the computational cost of the proposed model, including the time and memory requirements, and compare it with the standard Transformer. The current discussion of computational cost is insufficient, and the paper should provide more concrete information about the practical implications of using the proposed memory module.

### Questions

- How does the proposed model compare with other memory-augmented Transformer models?
- How does the proposed model scale with the size of the dataset and the model?

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
