### Summary

This paper studies the issue of hallucination in LLM summarization, where the generated summary contains information that is not present in the original context. The authors propose a definition of context influence and a corresponding decoding method called Context-Influence Decoding (CID). They show that amplifying the context, i.e., reducing the influence of prior knowledge, increases the context's influence on the LLM and can help mitigate hallucination. The authors also show that their context influence metric can serve as a lower bound for the private information leakage of CID. They conduct experiments on two datasets, CNN-DM and PubMedQA, and show that their method can improve the faithfulness of the generated summaries while reducing the context influence.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

- The paper proposes a novel definition of context influence and a corresponding decoding method called Context-Influence Decoding (CID).
- The authors show that amplifying the context, i.e., reducing the influence of prior knowledge, increases the context's influence on the LLM and can help mitigate hallucination.
- The authors show that their context influence metric can serve as a lower bound for the private information leakage of CID.
- The experiments on two datasets, CNN-DM and PubMedQA, show that the proposed method can improve the faithfulness of the generated summaries while reducing the context influence.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a clear and comprehensive discussion of the related work. The authors should discuss the existing work on hallucination in LLM summarization, such as the paper "On Hallucinations in Abstractive Summarization with a Contrastive Objective" (NeurIPS 2022, which won the best paper award). The authors should also discuss the existing work on context influence and private information leakage in LLMs.
- The paper does not provide a clear and formal definition of hallucination. The authors should define what they mean by hallucination and how they measure it. The authors should also discuss the limitations of their definition and measurement of hallucination.
- The paper does not provide a clear and formal definition of private information. The authors should define what they mean by private information and how they identify it in the context. The authors should also discuss the limitations of their definition and identification of private information.
- The paper does not provide a clear and formal definition of the tradeoff between context influence and hallucination. The authors should define what they mean by tradeoff and how they measure it. The authors should also discuss the limitations of their definition and measurement of the tradeoff.
- The paper does not provide a clear and formal definition of the goal of their method. The authors should state what they are trying to achieve with their method and how they evaluate their success.

### Suggestions

The paper needs to significantly improve its discussion of related work, particularly concerning hallucination in abstractive summarization. While the authors mention the problem, they fail to engage with specific techniques and findings from the literature. For instance, the paper "On Hallucinations in Abstractive Summarization with a Contrastive Objective" presents a relevant approach that should be discussed in detail, including how the proposed method compares to and contrasts with contrastive training methods. Furthermore, the authors should explore other relevant work on mitigating hallucinations, such as methods that leverage factuality metrics during training or decoding, or those that use knowledge bases to verify generated content. A more thorough literature review would help to contextualize the contribution of this work and highlight its novelty compared to existing approaches. The current lack of engagement with existing literature makes it difficult to assess the significance of the proposed method.

Furthermore, the paper needs to provide clear and formal definitions for key concepts such as hallucination, private information, and the tradeoff between context influence and hallucination. The current definitions are either implicit or absent, making it difficult to understand the scope and limitations of the proposed method. For example, the authors should specify how they measure hallucination, whether they are using token-level comparisons, semantic analysis, or factuality metrics. They should also discuss the limitations of their chosen metric and how it might affect the evaluation results. Similarly, the definition of private information needs to be made explicit, including what types of information are considered private (e.g., named entities, specific dates, or sensitive attributes) and how this information is identified in the context. Without clear definitions, it is difficult to assess the validity and generalizability of the proposed method. The authors should also formalize the tradeoff between context influence and hallucination, explaining how they measure this tradeoff and what the implications are for the practical application of their method.

Finally, the paper should clearly articulate the goal of the proposed method and how it is evaluated. The authors should state whether the goal is to minimize hallucination, maximize context influence, or find an optimal balance between the two. They should also explain how they evaluate the success of their method in achieving this goal, including the specific metrics used and their limitations. For example, if the goal is to minimize hallucination, the authors should demonstrate that their method achieves a significant reduction in hallucination compared to baseline methods. If the goal is to find an optimal balance, they should explain how they define and measure this balance and provide evidence that their method achieves it. Without a clear goal and evaluation strategy, it is difficult to assess the effectiveness of the proposed method and its potential for practical applications.

### Questions

Please address the weaknesses above.

### Rating

3

### Confidence

4

**********
