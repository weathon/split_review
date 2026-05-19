### Summary

The paper proposes a new adaptive RAG framework, called SeaKR, to help LLMs better decide when to retrieve and how to integrate retrieved knowledge. It extracts uncertainty estimates from the internal states of LLMs and uses them to decide when to retrieve, how to re-rank, and how to reason with retrieved documents. Experiments show that SeaKR outperforms existing adaptive RAG methods on both complex and simple QA datasets.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow. The motivation and the idea are clearly explained.
2. The proposed method is novel, simple, and effective. It is the first work to leverage self-awareness from the internal states of LLMs to adaptively decide when to retrieve and how to integrate retrieved knowledge.
3. Experiments show that SeaKR outperforms existing adaptive RAG methods on both complex and simple QA datasets.

### Weaknesses

#### Some Related Works


#### comment

1. The retrieval decision is based on the uncertainty estimator, which is an internal state extractor. It may require large training data to train the extractor. However, in the proposed method, the uncertainty estimator is tuning-free. Is it proposed or existing from other papers? If it is an existing method, it should be cited.
2. The experiments are based on a specific LLM (LLaMA-2-chat 7B). It would be better to conduct experiments on other LLMs to evaluate the generalization of the proposed method.
3. The paper does not discuss the computational cost of the proposed method. The method requires extracting internal states of LLMs for each token generated, which may be time-consuming. It is necessary to compare the efficiency of the proposed method with other RAG methods.

### Suggestions

The paper introduces an interesting approach to adaptive RAG by leveraging internal states of LLMs for uncertainty estimation. However, the practical applicability of the method could be significantly enhanced by addressing the computational overhead. Specifically, the paper should include a detailed analysis of the time complexity associated with extracting internal states for each token generation. This analysis should consider the number of layers in the LLM, the size of the hidden states, and the cost of computing the Gram matrix. Furthermore, it would be beneficial to explore methods to reduce this computational cost, such as using a smaller subset of layers for uncertainty estimation or employing more efficient algorithms for Gram matrix computation. A comparison with other RAG methods in terms of latency and throughput would also be valuable to understand the trade-offs between accuracy and efficiency.

To further strengthen the paper, it is crucial to investigate the sensitivity of the proposed method to different hyperparameters. The top-k value for retrieving documents and the threshold for triggering retrieval are two key hyperparameters that can significantly impact the performance of the method. The paper should include a sensitivity analysis to show how the performance varies with different values of these hyperparameters. This analysis should also provide guidelines on how to choose the optimal values for these hyperparameters for different datasets and LLMs. Moreover, it would be beneficial to explore adaptive strategies for setting these hyperparameters based on the characteristics of the input query or the uncertainty estimates. This would make the method more robust and adaptable to different scenarios.

Finally, while the paper demonstrates the effectiveness of the proposed method on both complex and simple QA datasets, it would be beneficial to evaluate the method on a wider range of tasks and datasets. For example, it would be interesting to see how the method performs on tasks such as summarization, dialogue, or other tasks that require different types of reasoning. This would provide a more comprehensive evaluation of the generalization ability of the method. Additionally, it would be valuable to investigate the performance of the method with different types of retrieval models, such as those based on semantic embeddings or transformer-based models. This would help to understand the robustness of the method to different retrieval strategies.

### Questions

1. How does the proposed method perform on other LLMs?
2. What is the computational cost of the proposed method compared to other RAG methods?
3. How does the method decide the top-k value for retrieving documents and the threshold for triggering retrieval?

### Rating

6

### Confidence

4

**********
