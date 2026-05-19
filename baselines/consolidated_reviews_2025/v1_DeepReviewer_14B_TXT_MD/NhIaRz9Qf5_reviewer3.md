### Summary

The paper proposes an adaptive RAG framework, SeaKR, which leverages the self-awareness from the internal states of LLMs to determine when to retrieve and how to integrate retrieved knowledge. The self-awareness is extracted from the internal states in the feed-forward network (FFN) of each layer corresponding to the last generated token. The consistency measure across multiple generations to the same prompt is computed as the self-aware uncertainty score of LLMs. SeaKR also designs two adaptive integration strategies based on the LLM self-awareness: 1) self-aware re-ranking and 2) self-aware reasoning. Experimental results show that SeaKR outperforms existing adaptive RAG methods.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. SeaKR is a novel adaptive RAG framework, which leverages the self-awareness from the internal states of LLMs to determine when to retrieve and how to integrate retrieved knowledge. To the best of my knowledge, this is the first work to leverage self-awareness from the internal states of LLMs to dynamically determine when to retrieve and effectively integrate retrieved knowledge.
3. SeaKR is a tuning-free adaptive RAG framework, which makes it more generalizable and applicable.
4. The authors conduct comprehensive experiments to show the effectiveness of SeaKR.

### Weaknesses

#### Some Related Works


#### comment

1. SeaKR needs to sample k different generations from the LLM for the same input context, whose hidden representations are subsequently used to compute their Gram matrix. This process may introduce additional computational costs. The authors may need to report the additional time cost introduced by SeaKR.
2. SeaKR needs to extract the internal states from the middle layer of the LLM. The authors may need to provide more explanations on how they determine which layer is the middle layer, especially for LLMs with an even number of layers. Furthermore, the rationale for focusing on the middle layer specifically, as opposed to other layers or a combination of layers, is not sufficiently justified. The method's sensitivity to the choice of this layer should be explored.
3. SeaKR needs to set a threshold to determine whether the self-aware uncertainty score is high. The authors may need to provide more explanations on how they determine the threshold. The current explanation lacks detail on how the threshold is optimized and what impact different threshold values have on the overall performance of the model. A more rigorous analysis of the threshold selection process is needed.

### Suggestions

The paper introduces an interesting approach to adaptive RAG by leveraging the self-awareness of LLMs. However, several aspects of the methodology require further clarification and analysis. First, the computational overhead of sampling k generations and computing the Gram matrix needs to be thoroughly investigated. The authors should provide a detailed breakdown of the time complexity of these operations and compare it to other adaptive RAG methods. This analysis should include not only the overall time cost but also the memory footprint, especially when dealing with large language models. Furthermore, the impact of the parameter k on both performance and computational cost should be explored, as this parameter directly affects the number of forward passes through the LLM. It would be beneficial to see a sensitivity analysis of k, showing how performance changes with different values and how this trade-off can be managed in practice.

Second, the choice of the middle layer for extracting internal states needs more justification. While the authors mention that this layer has the most accessible information, a more detailed explanation is needed. Specifically, the authors should explore the information content of different layers and provide empirical evidence to support the claim that the middle layer is optimal. This could involve analyzing the hidden representations of different layers and comparing their ability to capture relevant information for uncertainty estimation. The authors should also consider the possibility of using a combination of layers or a learned weighting scheme to extract more robust uncertainty estimates. The sensitivity of the method to the choice of layer should be analyzed, especially for models with an even number of layers, where the definition of the middle layer is less clear. The authors should also discuss how this approach might generalize to other model architectures and layer configurations.

Finally, the threshold selection process for determining high self-aware uncertainty scores requires more rigorous analysis. The authors should provide a detailed explanation of how the threshold is optimized, including the specific optimization algorithm used and the evaluation metrics considered. It is important to understand how the threshold affects the trade-off between retrieval accuracy and computational cost. A sensitivity analysis of the threshold is needed, showing how performance changes with different values. The authors should also discuss the potential for adaptive thresholding, where the threshold is dynamically adjusted based on the characteristics of the input query or the current state of the model. This would make the method more robust and adaptable to different scenarios.

### Questions

1. How is the internal state of the LLM updated during the generation process? Does the internal state of the LLM for the same input context vary a lot for different generations?
2. How is the threshold determined? Is the threshold determined based on the development set? If so, how is the development set constructed?

### Rating

6

### Confidence

4

**********
