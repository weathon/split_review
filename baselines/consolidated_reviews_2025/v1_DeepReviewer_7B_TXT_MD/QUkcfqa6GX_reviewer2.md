### Summary

The paper introduces a novel framework called STLLM (Spatio-Temporal Graph Learning with Large Language Model) for urban computing tasks. The framework aims to leverage the strengths of Large Language Models (LLMs) in capturing implicit spatio-temporal dependencies and preserving point of interest information across urban space. The authors propose a cross-view mutual information maximization paradigm to align LLM-based knowledge representations with GNN-based structural embeddings, enhancing the robustness and adaptability of region representations. The paper evaluates the performance of STLLM in three distinct prediction tasks: crime prediction, traffic flow forecasting, and property price prediction. The results show that STLLM outperforms state-of-the-art baselines in various prediction tasks, demonstrating its effectiveness in capturing complex spatio-temporal patterns. The paper also provides a theoretical analysis of the proposed method and conducts extensive experiments to validate its efficacy, robustness, and efficiency.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper introduces a novel framework that integrates LLMs with a cross-view mutual information maximization paradigm to capture implicit spatio-temporal dependencies and preserve point of interest information across urban space. This is a creative combination of existing techniques and has the potential to advance the field of urban computing.
2. The paper provides a theoretical analysis of the proposed method, which is essential for understanding its underlying mechanisms and ensuring its validity.
3. The paper conducts extensive experiments to validate the efficacy, robustness, and efficiency of STLLM. The experiments are well-designed and provide strong evidence for the effectiveness of the proposed method.
4. The paper is well-written and easy to follow. The authors provide clear explanations of the proposed method and the experimental setup.

### Weaknesses

#### Some Related Works


#### comment

1. The novelty of this paper is limited. The authors simply combine LLMs with a cross-view mutual information maximization paradigm, which lacks sufficient innovation. The core idea of using mutual information to align different views is not new, and the specific implementation details do not appear to offer significant advancements over existing methods. The paper does not adequately articulate how the proposed approach differs fundamentally from existing techniques that also leverage mutual information for cross-view learning.
2. The authors do not provide a detailed explanation of how STLLM captures implicit spatio-temporal dependencies. The paper lacks a clear description of the mechanisms through which the LLM and GNN interact to capture these dependencies. It is unclear how the LLM's global context understanding is translated into specific spatio-temporal relationships, and the paper would benefit from a more detailed analysis of the learned representations.
3. The authors do not provide a detailed explanation of how STLLM preserves point of interest information. The paper does not clearly articulate the specific mechanisms that ensure the preservation of POI information. It is unclear how the model avoids overwriting or losing the original POI information during the alignment process. A more rigorous analysis of the information flow and preservation is needed.
4. The authors do not provide a detailed explanation of how STLLM handles dynamic and evolving nature of spatio-temporal data. The paper does not adequately address how the model adapts to changes in the spatio-temporal graph structure over time. It is unclear how the model handles the addition or removal of nodes and edges, and how it maintains the consistency of the learned representations.
5. The authors do not provide a detailed explanation of how STLLM scales to large-scale spatio-temporal data. The paper lacks a discussion of the computational complexity and memory requirements of the proposed method, especially when dealing with large-scale urban datasets. It is unclear how the model's performance and efficiency are affected by the size of the input data.
6. The authors do not provide a detailed explanation of how STLLM performs data augmentation and denoising. The paper does not clearly explain how the model generates new data samples or how it identifies and mitigates noisy data. The description of the data augmentation process is vague, and it is unclear how the model ensures that the augmented data is meaningful and does not introduce biases.
7. The authors do not provide a detailed explanation of how STLLM ensures data privacy. The paper does not discuss any specific techniques used to protect the privacy of the data, especially when dealing with sensitive information such as crime data or traffic patterns. It is unclear how the model avoids exposing sensitive information during the learning process.
8. The authors do not provide a detailed explanation of how STLLM handles missing data. The paper does not adequately address how the model deals with missing values in the spatio-temporal data. It is unclear how the model handles missing data points, and whether it introduces any biases or inaccuracies in the predictions.

### Suggestions

The paper would benefit from a more thorough discussion of the novelty of the proposed approach. While the combination of LLMs and cross-view mutual information maximization is interesting, the paper needs to clearly articulate how this combination differs from existing methods that use mutual information for cross-view learning. Specifically, the authors should provide a detailed comparison with other methods that use similar techniques, highlighting the unique aspects of their approach. For example, the paper could discuss how the specific architecture of the LLM and GNN, or the way they are combined, leads to a novel approach that is not simply a rehash of existing techniques. Furthermore, the authors should provide a more detailed explanation of the specific mechanisms through which the LLM and GNN interact to capture implicit spatio-temporal dependencies. It is not sufficient to simply state that the LLM is used to capture global context; the paper needs to explain how this global context is translated into specific spatio-temporal relationships and how the GNN then uses this information to learn representations. A more detailed analysis of the learned representations, perhaps through visualization or ablation studies, would be beneficial to understand how the model captures these dependencies. 

To address the lack of clarity regarding point of interest information preservation, the authors should provide a more detailed explanation of the specific mechanisms that ensure the preservation of POI information. The paper needs to explain how the model avoids overwriting or losing the original POI information during the alignment process. A more rigorous analysis of the information flow and preservation is needed, perhaps by examining the gradients or the learned representations. The authors should also discuss how the model handles the dynamic and evolving nature of spatio-temporal data. The paper needs to explain how the model adapts to changes in the spatio-temporal graph structure over time, including the addition or removal of nodes and edges. It is important to discuss how the model maintains the consistency of the learned representations when the graph structure changes. The authors should also provide a more detailed explanation of how STLLM scales to large-scale spatio-temporal data. The paper needs to discuss the computational complexity and memory requirements of the proposed method, especially when dealing with large-scale urban datasets. It is important to analyze how the model's performance and efficiency are affected by the size of the input data. 

Finally, the paper needs to provide a more detailed explanation of how STLLM performs data augmentation and denoising, and how it ensures data privacy. The description of the data augmentation process is vague, and it is unclear how the model ensures that the augmented data is meaningful and does not introduce biases. The authors should provide a more detailed explanation of the specific techniques used for data augmentation and denoising, and how these techniques are integrated into the overall framework. The paper also needs to discuss the specific techniques used to protect the privacy of the data, especially when dealing with sensitive information such as crime data or traffic patterns. It is important to explain how the model avoids exposing sensitive information during the learning process. The authors should also discuss how the model handles missing data, and whether it introduces any biases or inaccuracies in the predictions. A more detailed explanation of the strategies used to handle missing data is needed.

### Questions

Please refer to the weaknesses.

### Rating

3

### Confidence

5

**********
