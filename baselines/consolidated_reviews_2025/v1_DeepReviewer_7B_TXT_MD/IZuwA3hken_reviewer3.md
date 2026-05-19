### Summary

This paper investigates the influence of context on LLMs' outputs, focusing on how context affects generation and how to mitigate hallucinations. The authors introduce Context Influence Decoding (CID), a method that amplifies context by adjusting the model's output probabilities using a tunable parameter λ. They provide theoretical bounds on the privacy leakage of CID and empirically evaluate its effectiveness on summarization tasks using Llama-3 and GPT-Neo models. The results demonstrate that CID can improve ROUGE-L scores while reducing hallucination, with a trade-off between influence and privacy leakage.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The authors provide a theoretical analysis of the privacy leakage of CID, which is a valuable contribution to the field.
3. The empirical evaluations are comprehensive and provide insights into the behavior of LLMs under different conditions.

### Weaknesses

#### Some Related Works


#### comment

1. The paper's theoretical analysis relies on certain assumptions about the model's behavior, such as the independence of token probabilities, which may not hold in practice. Specifically, the assumption that token probabilities are independent given the context and query is a strong simplification that likely deviates from the complex dependencies learned by real-world language models. This could lead to inaccurate theoretical bounds and limit the practical applicability of the analysis.
2. The empirical evaluations are limited to summarization tasks, which may not fully capture the generalizability of CID to other tasks. The specific nature of summarization, with its focus on information extraction and compression, might not be representative of other tasks such as question answering, dialogue generation, or creative writing, where different types of context influence and hallucination might be present. This raises concerns about the broader applicability of the findings.
3. The paper does not provide a detailed analysis of the computational overhead of CID, which could be a concern for practical applications. The method involves manipulating the output probabilities of the language model, which could introduce additional computational costs, especially for large models and long contexts. The paper lacks a thorough analysis of these costs, making it difficult to assess the practical feasibility of the approach.

### Suggestions

The authors should address the limitations of their theoretical analysis by exploring alternative models that account for the dependencies between tokens. This could involve incorporating techniques from information theory or statistical mechanics to model the complex interactions within language models. Furthermore, the authors should acknowledge that the theoretical bounds derived under these simplifying assumptions may not directly translate to real-world scenarios. A more thorough discussion of these limitations would enhance the credibility of the theoretical analysis and provide a more realistic perspective on the applicability of the proposed method. It would also be beneficial to investigate the sensitivity of the theoretical results to the specific assumptions made, perhaps by conducting a sensitivity analysis.

To address the limited scope of empirical evaluations, the authors should extend their experiments to include a wider range of tasks beyond summarization. This could involve evaluating CID on tasks such as question answering, dialogue generation, and creative writing. These tasks present different challenges and might reveal different aspects of context influence and hallucination. For example, in question answering, the model needs to extract relevant information from the context, and it is important to understand how CID affects this process. Similarly, in dialogue generation, the model needs to maintain context and generate coherent and relevant responses, and it is important to assess how CID impacts the quality of the dialogue. By conducting experiments on a more diverse set of tasks, the authors can provide a more comprehensive evaluation of the generalizability of CID.

Finally, the paper should include a detailed analysis of the computational overhead of CID. This should include a breakdown of the time and memory costs associated with manipulating the output probabilities of the language model. The authors should also compare the computational cost of CID with other methods for mitigating hallucinations. This analysis should provide a clear understanding of the practical feasibility of the approach and help practitioners make informed decisions about its applicability. Furthermore, the authors should explore potential optimizations to reduce the computational overhead of CID, such as using more efficient algorithms or approximations. This would make the method more practical for real-world applications.

### Questions

See weakness

### Rating

5

### Confidence

3

**********
