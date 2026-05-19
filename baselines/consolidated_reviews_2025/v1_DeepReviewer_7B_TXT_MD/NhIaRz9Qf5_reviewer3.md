### Summary

This paper introduces a novel approach called Self-aware Knowledge Retrieval (SEARLE) for adaptive Retrieval-Augmented Generation (RAG). The key idea is to leverage the internal states of Large Language Models (LLMs) to determine when and how to retrieve external knowledge. SEARLE consists of three main components: a search engine for retrieving knowledge, a large language model for generating content, and a self-aware uncertainty estimator for deciding when to invoke retrieval. The authors demonstrate that SEARLE outperforms existing adaptive RAG methods on complex and simple question-answering datasets.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed SEARLE method is novel and interesting. It leverages the internal states of LLMs to determine when and how to retrieve external knowledge, which is a creative approach to adaptive RAG.
3. The experiments are comprehensive and demonstrate the effectiveness of SEARLE on both complex and simple question-answering datasets.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational cost associated with SEARLE, particularly the Gram determinant calculation, which may introduce significant overhead. Specifically, the paper lacks a breakdown of the time spent on uncertainty estimation versus the time spent on actual retrieval and generation. This makes it difficult to assess the practical applicability of the method, especially in resource-constrained environments.
2. The paper does not provide a detailed comparison of SEARLE with other uncertainty-based retrieval methods, such as those based on entropy or probability thresholds. A more thorough comparison would help to highlight the advantages and limitations of the proposed approach. The paper should also discuss how the choice of the Gram determinant as the uncertainty measure compares to other alternatives, and whether this choice is optimal for the task.
3. The paper does not discuss the potential limitations of SEARLE, such as its sensitivity to the choice of hyperparameters or its performance on different types of questions. A more thorough analysis of these limitations would provide a more balanced view of the proposed method.

### Suggestions

The paper should include a detailed analysis of the computational cost of SEARLE, specifically breaking down the time spent on each component: self-aware uncertainty estimation, knowledge retrieval, and generation. This analysis should include a comparison with the computational cost of baseline methods, such as IRCoT, to provide a clear understanding of the trade-offs involved. Furthermore, the authors should investigate techniques to optimize the Gram determinant calculation, such as using low-rank approximations or other efficient matrix computation methods. This would help to make the method more practical for real-world applications where computational resources are often limited. It would also be beneficial to explore the sensitivity of the method to the choice of the Gram determinant parameters, such as the layer from which the hidden representations are extracted, and the number of samples used to compute the determinant.

To strengthen the evaluation, the paper should include a more detailed comparison of SEARLE with other uncertainty-based retrieval methods. This comparison should include a discussion of the advantages and disadvantages of each method, as well as a quantitative evaluation of their performance on the same tasks. The authors should also explore the use of alternative uncertainty measures, such as entropy or probability thresholds, and compare their performance with the Gram determinant. This comparison should include an analysis of the sensitivity of each method to different hyperparameters and the computational cost of each method. The paper should also discuss the theoretical justification for using the Gram determinant as a measure of uncertainty, and whether this measure is optimal for the task of adaptive retrieval-augmented generation. This would provide a more comprehensive understanding of the strengths and weaknesses of the proposed approach.

Finally, the paper should include a more thorough analysis of the potential limitations of SEARLE. This analysis should discuss the sensitivity of the method to the choice of hyperparameters, such as the uncertainty threshold and the number of retrieved knowledge pieces, and how these parameters affect the performance of the method. The authors should also discuss the performance of SEARLE on different types of questions, such as those requiring multi-hop reasoning or those with ambiguous answers. A more detailed analysis of these limitations would provide a more balanced view of the proposed method and help to identify areas for future improvement.

### Questions

1. How does the computational cost of SEARLE compare to that of baseline methods, such as IRCoT, in terms of time and memory usage?
2. Have you considered evaluating SEARLE on other tasks, such as summarization or dialogue generation, to assess its generalizability?
3. How does SEARLE compare to other uncertainty-based retrieval methods in terms of performance and computational efficiency?

### Rating

5

### Confidence

3

**********
