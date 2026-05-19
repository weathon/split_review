### Summary

This paper focuses on using LLM to do spatio-temporal prediction in urban computing. The authors propose STLLM, which uses a spatio-temporal graph neural network and LLM to generate embeddings from two views. Then the embeddings are aligned through contrastive learning. The authors conducted experiments on several real-world datasets and the results show that STLLM outperforms the baseline methods.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper is well-written and easy to understand.
2. The proposed method is simple and effective.
3. The experimental results show the superiority of STLLM compared to the baseline methods.

### Weaknesses

#### Some Related Works


#### comment

1. Although the authors claim that one contribution of this paper is using LLM, it seems that LLM is just used to convert the spatio-temporal data to embeddings in this paper. 
2. The authors do not provide an in-depth analysis of the reason behind the superior performance of STLLM compared to the baseline methods. For example, the authors may need to show the correlation between the learned embeddings from the two views or the representations of each view before alignment.
3. The authors may need to add several contrastive learning baselines, such as the method in "Spatio-Temporal Graph Convolutional Networks for Traffic Forecasting".

### Suggestions

The paper's core idea of using an LLM to generate embeddings for spatio-temporal data is interesting, but the current implementation and analysis lack sufficient depth to fully support the claims. The authors should provide a more detailed explanation of how the LLM is leveraged beyond simply converting data into embeddings. Specifically, it would be beneficial to explore the LLM's ability to capture semantic relationships within the data and how these relationships contribute to the final prediction performance. For example, the authors could analyze the attention weights of the LLM to understand which parts of the input text are most relevant for generating the embeddings. Furthermore, the authors should investigate different prompting strategies for the LLM to see how the input text structure affects the quality of the embeddings. This would provide a more comprehensive understanding of the LLM's role in the proposed framework and strengthen the claim of using LLM as a major contribution.

To better understand the performance gains of STLLM, the authors should conduct a more thorough analysis of the learned embeddings. This should include a quantitative analysis of the correlation between the embeddings from the two views, perhaps using metrics like cosine similarity or mutual information. Visualizing the embeddings using techniques like t-SNE or UMAP could also provide valuable insights into the structure of the embedding space and how the contrastive learning process aligns the two views. Additionally, the authors should analyze the representations of each view before alignment to understand the initial differences and how the contrastive learning process transforms them. This analysis should go beyond simply showing the embeddings and should include a discussion of the semantic meaning of the embeddings and how they relate to the spatio-temporal data. Such an analysis would provide a more solid foundation for the claims of the paper and help the reader understand the inner workings of the proposed method.

Finally, the authors should include more relevant baselines, especially those that use contrastive learning for spatio-temporal forecasting. While the authors compare against several methods, the absence of contrastive learning baselines makes it difficult to isolate the contribution of the proposed approach. Specifically, the authors should implement and compare against the method in "Spatio-Temporal Graph Convolutional Networks for Traffic Forecasting" as it is a well-known baseline in the field. This would provide a more comprehensive evaluation of the proposed method and help the reader understand its strengths and weaknesses compared to existing approaches. Furthermore, the authors should consider including other contrastive learning methods that are specifically designed for spatio-temporal data to provide a more robust comparison.

### Questions

Please see above.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
