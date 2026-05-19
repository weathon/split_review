### Summary

This paper addresses the problem of context influence and hallucination in summarization. The authors propose a definition for context influence and Context-Influence Decoding (CID), and then they show that amplifying the context (by factoring out prior knowledge) and the context being out of distribution with respect to prior knowledge increases the context’s influence on an LLM. Moreover, they show that context influence gives a lower bound of the private information leakage of CID. They corroborate their analytical findings with experimental evaluations that show improving the F1 ROGUE-L score on CNN-DM for LLaMA 3 by 10% over regular decoding also leads to 1.5x more influence by the context. Moreover, they empirically evaluate how context influence and hallucination are affected by (1) model capacity, (2) context size, (3) the length of the current response, and (4) different token n-grams of the context.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The paper introduces a novel definition for context influence that follows from Point-wise Cross-Mutual Information and Context-Influence Decoding (CID), which reformulates Context-Aware Decoding (CAD) to better understand and control the influence of the context.
3. The authors analytically show that amplifying the context by factoring out prior knowledge to reduce hallucination causes more influence of the context by an LLM. Moreover, they show that they can use their context influence definition to lower bound the private information leakage of CID.
4. The authors corroborate their theoretic findings by measuring the context influence and hallucination of various LLMs on summarization tasks. In particular, improving the ROGUE-L score by 10% on CNN-DM for LLaMA 3 increases the influence by 1.5x.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed discussion of the limitations of the proposed method. For example, how does the method perform on different types of summarization tasks, such as abstractive summarization or multi-document summarization? How does the method handle noisy or incomplete context? Addressing these questions would provide a more comprehensive understanding of the method's strengths and weaknesses.
2. The paper does not provide a thorough comparison with existing methods for mitigating hallucination in summarization. While the authors mention that their method is different from previous works, they do not provide a detailed comparison of the performance of their method with other state-of-the-art approaches. A more comprehensive comparison would help to better understand the advantages and disadvantages of the proposed method.

### Suggestions

The paper would benefit from a more thorough investigation into the limitations of the proposed Context-Influence Decoding (CID) method. Specifically, the authors should explore how CID performs across various summarization tasks beyond the single-document setting used in the experiments. For instance, evaluating CID on abstractive summarization tasks, where the goal is to generate a concise summary that captures the essence of the input text, would be valuable. Furthermore, the method's robustness to noisy or incomplete context should be examined. This could involve introducing perturbations to the input context, such as random word substitutions or deletions, and assessing how CID's performance degrades. Such an analysis would provide a more complete picture of the method's applicability and limitations in real-world scenarios. The authors should also consider the computational cost of their method, especially when compared to other decoding strategies, as this is a critical factor for practical applications.

To strengthen the paper, a more detailed comparison with existing hallucination mitigation techniques is needed. The authors should not only mention that their method is different but also provide a quantitative comparison with other state-of-the-art approaches. This could involve implementing and evaluating several existing methods on the same datasets used in the paper and comparing their performance in terms of both summarization quality (e.g., ROUGE scores) and hallucination reduction (e.g., using metrics like FactCC or QAGS). This would allow for a more direct assessment of the advantages and disadvantages of CID compared to other methods. Furthermore, the authors should discuss the specific scenarios where CID is expected to outperform existing methods and provide a rationale for these expectations. This would help to clarify the contribution of their work and its potential impact on the field.

Finally, the paper should include a more detailed analysis of the hyperparameter sensitivity of the proposed method. The authors should investigate how the performance of CID varies with different values of the hyperparameters, such as the weighting factor for the context influence term. This analysis should include a discussion of how these hyperparameters should be tuned for different tasks and datasets. Furthermore, the authors should provide guidelines for selecting appropriate values for these hyperparameters, which would be helpful for practitioners who want to use the method. This would also help to understand the robustness of the method and its sensitivity to parameter settings.

### Questions

1. How does the proposed method perform on different types of summarization tasks, such as abstractive summarization or multi-document summarization?
2. How does the proposed method handle noisy or incomplete context?
3. How does the proposed method compare to existing methods for mitigating hallucination in summarization in terms of performance and computational cost?
4. What are the limitations of the proposed method, and how can they be addressed in future work?

### Rating

6

### Confidence

3

**********
