### Summary

This paper proposes a training-free familiarity-aware evidence compression method (FAVICOMP) to improve retrieval-augmented generation (RAG). The core of FAVICOMP is to combine the decoding probabilities from the compression model and the target model to generate context that is more familiar to the target model. Experimental results show that FAVICOMP outperforms some evidence compression baselines on multiple open-domain QA datasets.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

1. The writing is clear and easy to understand.

2. The experimental results are convincing and the improvements are significant.

3. The method is training-free and can be applied to different RAG processes.

### Weaknesses

#### Some Related Works


#### comment

1. The novelty of the proposed method is limited. The technique of ensembling the token logits from different models is a common approach in the field of LLM, and this paper just applies it to the context compression domain.

2. The core motivation of the paper is not clear. Although the authors mention that it is to balance the integration of parametric and non-parametric knowledge, it is not clear why the proposed method can achieve this goal. The method may rely heavily on the target model's ability to filter out unfamiliar information from the compression model. If the target model has poor generalization capabilities, the resulting performance may suffer.

3. The generalization of the method is limited. The authors employ three compression and target model pairs, where two pairs use the same model for compression and target, and one pair uses different models. It is not clear how the method would perform when applied to different model families, such as Qwen and LLaMA.

4. The analysis of the impact of the ensemble coefficient α on performance and perplexity is not deep enough. The authors claim that when α exceeds 0.5, performance declines as perplexity decreases due to the lack of evidential knowledge during evidence compression. However, this explanation is not convincing, as there is no clear correlation between the performance and perplexity of individual samples.

### Suggestions

The paper's core idea of ensembling token logits from a compression model and a target model to generate more familiar context is not inherently novel, as logit manipulation is a common technique in LLMs. However, the specific application of this technique to the evidence compression domain within RAG systems could be considered a novel contribution if properly framed. To strengthen the paper, the authors should more clearly articulate the specific challenges in evidence compression that this method addresses and how the proposed approach provides a unique solution compared to existing methods. For example, the authors could discuss the limitations of existing compression techniques in handling noisy or irrelevant information and how their method mitigates these issues through the ensembling process. Furthermore, a more detailed analysis of the method's behavior under different conditions, such as varying levels of noise in the retrieved documents, would be beneficial to demonstrate the robustness and effectiveness of the proposed approach.

To address the concern about the method's reliance on the target model's generalization capabilities, the authors should conduct more extensive experiments using a wider range of target models with varying generalization abilities. This would help to clarify the relationship between the target model's generalization performance and the effectiveness of the proposed method. Specifically, the authors could evaluate the method's performance on models with different sizes and architectures, and analyze how the method's performance changes as the target model's generalization capabilities vary. Additionally, the authors should provide a more detailed explanation of how the proposed method balances the integration of parametric and non-parametric knowledge. This explanation should go beyond the simple claim that the method leverages both types of knowledge and should provide concrete examples of how the method utilizes both the compression model's output and the target model's internal knowledge to generate the final context. A more thorough analysis of the method's behavior in different scenarios, such as when the retrieved documents are highly relevant or irrelevant, would also be beneficial.

Finally, the analysis of the ensemble coefficient α needs to be more rigorous. The authors should provide a more detailed explanation of the relationship between α, performance, and perplexity. The current explanation that performance declines as perplexity decreases when α exceeds 0.5 is not convincing, as there is no clear correlation between the performance and perplexity of individual samples. The authors should conduct a more fine-grained analysis of the impact of α on the generated context and how this context affects the final performance. For example, the authors could analyze the diversity and relevance of the generated context for different values of α and how these factors correlate with the final performance. Additionally, the authors should provide a more detailed explanation of why the optimal value of α is around 0.5 and how this value balances the contributions of the compression model and the target model. A more thorough analysis of the ensemble coefficient would significantly strengthen the paper's claims and provide a more complete understanding of the proposed method.

### Questions

See weaknesses.

### Rating

5

### Confidence

4

**********
