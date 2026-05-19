### Summary

This paper proposes a decoding method to mitigate hallucinations in LLMs at inference time. The method works by contrasting the logits of the original input and the masked input to filter out the hallucination tokens. The proposed method is evaluated on several QA datasets, showing better performance than the baseline.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

- The proposed method is simple and easy to understand.
- The proposed method is evaluated on several QA datasets, showing better performance than the baseline.

### Weaknesses

#### Some Related Works


#### comment

 - The proposed method is very similar to the contrastive decoding method proposed in Leng et al. (2024), which is not properly discussed in the paper. The authors should clearly differentiate their method from Li et al. (2023a) and Leng et al. (2024).
- The evaluation is not comprehensive. The authors should evaluate their method on more datasets, such as TruthfulQA, and on more LLMs, such as Llama 2 and Mistral. The current evaluation is limited to a single model and a few datasets, which does not provide a strong basis for the claims of general applicability.
- The writing of the paper can be improved. For example, the authors should explain the concept of hallucination in more detail, and provide more examples of hallucination. The current explanation is too brief and lacks sufficient context for readers unfamiliar with the problem.
- The authors should discuss the limitations of the proposed method. For example, the authors should discuss the potential impact of the method on the model's ability to generate diverse and creative text. The paper lacks a thorough analysis of the trade-offs between reducing hallucinations and maintaining other desirable properties of LLM outputs.

### Suggestions

The paper would benefit significantly from a more detailed comparison with existing contrastive decoding methods. The authors should not only acknowledge the similarity but also provide a rigorous analysis of the differences in methodology, assumptions, and performance. Specifically, they should discuss how their method's masking strategy differs from that of Leng et al. (2024), and how these differences impact the effectiveness of hallucination mitigation. A more thorough discussion of the theoretical underpinnings of their approach, compared to the empirical focus of Li et al. (2023a), would also be valuable. This would help to establish the novelty and contribution of their work more clearly. Furthermore, the authors should include a more comprehensive evaluation of their method, including a wider range of datasets and models. The current evaluation is limited and does not provide sufficient evidence to support the general applicability of the proposed method. The inclusion of datasets like TruthfulQA, which specifically targets factual accuracy, would be particularly relevant. Additionally, evaluating the method on different LLMs, such as Llama 2 and Mistral, would help to assess its robustness across different architectures and training paradigms. The authors should also consider evaluating their method on tasks beyond question answering, such as text summarization or dialogue generation, to demonstrate its versatility.

To improve the clarity of the paper, the authors should provide a more detailed explanation of the concept of hallucination, including concrete examples of how it manifests in LLM outputs. This explanation should be accessible to readers who are not experts in the field. The authors should also discuss the potential impact of their method on the model's ability to generate diverse and creative text. While reducing hallucinations is important, it is also crucial to ensure that the model retains its ability to generate novel and varied outputs. The authors should analyze whether their method introduces any unintended biases or limitations in the model's text generation capabilities. This analysis should include both quantitative and qualitative evaluations of the generated text. For example, they could measure the diversity of the generated text using metrics such as n-gram diversity, and they could also conduct human evaluations to assess the creativity of the generated text.

Finally, the authors should provide a more thorough discussion of the limitations of their method. This discussion should include a critical analysis of the potential drawbacks and trade-offs associated with their approach. For example, they should discuss the computational cost of their method, and they should also discuss the potential for their method to introduce new types of errors or biases. The authors should also discuss the potential for their method to be less effective in certain scenarios, such as when the model is dealing with highly complex or ambiguous inputs. By acknowledging these limitations, the authors can provide a more balanced and realistic assessment of their work. This would also help to guide future research in this area and to identify potential avenues for improvement.

### Questions

See weaknesses.

### Rating

3

### Confidence

4

**********
