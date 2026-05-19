### Summary

This paper investigates how contextual information influences LLMs and their tendency to hallucinate during summarization tasks. The authors propose a definition for context influence and introduce Context-Influence Decoding (CID), a method to control this influence. They show that amplifying context (by reducing reliance on prior knowledge) increases its impact on the LLM, which can lead to more hallucinations but also potentially more faithful summaries when the context is reliable. The study provides both theoretical analysis and experimental results, demonstrating the trade-offs between context influence and hallucination.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper introduces a novel definition for context influence in LLMs, which is a valuable contribution to understanding how contextual information affects model outputs.
2. The authors provide a comprehensive analysis of various factors affecting context influence, including model capacity, context size, and response length.
3. The paper presents a thorough experimental evaluation on multiple datasets (CNN-DM, PubMedQA) and models (OPT, LLaMA 3, GPT-Neo), providing strong empirical support for the theoretical findings.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a clear and comprehensive discussion of the related work. The authors should discuss the existing work on hallucination in LLM summarization, such as the paper "On Hallucinations in Abstractive Summarization with a Contrastive Objective" (NeurIPS 2022, which won the best paper award). The authors should also discuss the existing work on context influence and private information leakage in LLMs.
2. The paper does not provide a clear and formal definition of hallucination. The authors should define what they mean by hallucination and how they measure it. The authors should also discuss the limitations of their definition and measurement of hallucination.
3. The paper does not provide a clear and formal definition of private information. The authors should define what they mean by private information and how they identify it in the context. The authors should also discuss the limitations of their definition and identification of private information.
4. The paper does not provide a clear and formal definition of the tradeoff between context influence and hallucination. The authors should define what they mean by tradeoff and how they measure it. The authors should also discuss the limitations of their definition and measurement of the tradeoff.
5. The paper does not provide a clear and formal definition of the goal of their method. The authors should state what they are trying to achieve with their method and how they evaluate their success.

### Suggestions

The paper needs to significantly improve its discussion of related work, particularly concerning hallucination in abstractive summarization. While the authors mention the problem, they fail to engage with specific techniques and findings from the literature. For instance, the paper "On Hallucinations in Abstractive Summarization with a Contrastive Objective" presents a relevant approach that should be discussed in detail, including how the proposed method compares to and contrasts with contrastive training methods. Furthermore, the authors should explore other relevant work on mitigating hallucinations, such as methods that leverage factuality metrics during training or decoding, or those that use knowledge bases to verify generated content. A more thorough literature review would help to contextualize the contribution of this work and highlight its novelty compared to existing approaches. The current lack of engagement with existing literature makes it difficult to assess the significance of the proposed method.

Furthermore, the paper needs to provide clear and formal definitions for key concepts such as hallucination, private information, and the tradeoff between context influence and hallucination. The current definitions are either implicit or absent, making it difficult to understand the scope and limitations of the proposed method. For example, the authors should specify how they measure hallucination, whether they are using token-level comparisons, semantic analysis, or factuality metrics. They should also discuss the limitations of their chosen metric and how it might affect the evaluation results. Similarly, the definition of private information needs to be made explicit, including what types of information are considered private (e.g., named entities, specific dates, or sensitive attributes) and how this information is identified in the context. Without clear definitions, it is difficult to assess the validity and generalizability of the proposed method. The authors should also formalize the tradeoff between context influence and hallucination, explaining how they measure this tradeoff and what the implications are for the practical application of their method.

Finally, the paper should clearly articulate the goal of the proposed method and how it is evaluated. The authors should state whether the goal is to minimize hallucination, maximize context influence, or find an optimal balance between the two. They should also explain how they evaluate the success of their method in achieving this goal, including the specific metrics used and their limitations. For example, if the goal is to minimize hallucination, the authors should demonstrate that their method achieves a significant reduction in hallucination compared to baseline methods. If the goal is to find an optimal balance, they should explain how they define and measure this balance and provide evidence that their method achieves it. Without a clear goal and evaluation strategy, it is difficult to assess the effectiveness of the proposed method and its potential for practical applications.

### Questions

1. How does the proposed method compare to other state-of-the-art techniques for mitigating hallucination in summarization?
2. Can the authors provide more detailed analysis of the tradeoff between context influence and hallucination, including specific examples where increasing context influence leads to more hallucinations and vice versa?
3. How does the choice of λ affect the privacy leakage, and can the authors provide a more detailed analysis of this tradeoff?

### Rating

5

### Confidence

3

**********
