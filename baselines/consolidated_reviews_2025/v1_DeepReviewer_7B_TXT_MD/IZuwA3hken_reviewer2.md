### Summary

This paper proposes a principled definition of context influence and Context Influence Decoding (CID), a method that leverages a tunable parameter λ to control the influence of context on LLM output. The authors theoretically demonstrate that amplifying context (by factoring out prior knowledge) and mitigating hallucination are linked, and that CID can reduce context influence on output while lowering privacy leakage. The paper also provides empirical evaluations on summarization tasks, showing how model capacity, context size, response length, and token n-gram influence affect context influence and hallucination.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

1. The paper presents a principled definition of context influence and proposes Context Influence Decoding (CID) as a method to control context influence, which is a novel contribution to the field of LLM interpretability and privacy.
2. The authors provide a theoretical analysis linking context influence and hallucination, which is a valuable insight for understanding the behavior of LLMs.
3. The paper includes extensive empirical evaluations on summarization tasks, demonstrating the effectiveness of CID in reducing context influence and hallucination.

### Weaknesses

#### Some Related Works


#### comment

1. The paper's theoretical analysis relies on certain assumptions about the model's behavior, such as the independence of token probabilities, which may not hold in practice. Specifically, the assumption that token probabilities are independent given the context and query is a strong simplification that likely deviates from the complex dependencies learned by real-world language models. This could lead to inaccurate theoretical bounds and limit the practical applicability of the analysis.
2. The empirical evaluations are limited to summarization tasks, which may not fully capture the generalizability of CID to other tasks. The specific nature of summarization, with its focus on information extraction and compression, might not be representative of other tasks such as question answering, dialogue generation, or creative writing, where different types of context influence and hallucination might be present. This raises concerns about the broader applicability of the findings.
3. The paper does not provide a detailed analysis of the computational overhead of CID, which could be a concern for practical applications. The method involves manipulating the output probabilities of the language model, which could introduce additional computational costs, especially for large models and long contexts. The paper lacks a thorough analysis of these costs, making it difficult to assess the practical feasibility of the approach.

### Suggestions

The paper would benefit from a more nuanced discussion of the limitations of the theoretical framework. Specifically, the assumption of independent token probabilities should be addressed by exploring alternative theoretical models that account for the dependencies between tokens. This could involve incorporating techniques from information theory or statistical mechanics to model the complex interactions within language models. Furthermore, the authors should acknowledge that the theoretical bounds derived under these simplifying assumptions may not directly translate to real-world scenarios. A more thorough discussion of these limitations would enhance the credibility of the theoretical analysis and provide a more realistic perspective on the applicability of the proposed method.

To address the limited scope of empirical evaluations, the authors should extend their experiments to include a wider range of tasks beyond summarization. This could involve evaluating CID on tasks such as question answering, dialogue generation, and creative writing. These tasks present different challenges and might reveal different aspects of context influence and hallucination. For example, in question answering, the model needs to extract relevant information from the context, and it is important to understand how CID affects this process. Similarly, in dialogue generation, the model needs to maintain context and generate coherent and relevant responses, and it is important to assess how CID impacts the quality of the dialogue. By conducting experiments on a more diverse set of tasks, the authors can provide a more comprehensive evaluation of the generalizability of CID.

Finally, the paper should include a detailed analysis of the computational overhead of CID. This should include a breakdown of the time and memory costs associated with manipulating the output probabilities of the language model. The authors should also compare the computational cost of CID with other methods for mitigating hallucinations. This analysis should provide a clear understanding of the practical feasibility of the approach and help practitioners make informed decisions about its applicability. Furthermore, the authors should explore potential optimizations to reduce the computational overhead of CID, such as using more efficient algorithms or approximations.

### Questions

1. How does the theoretical analysis account for the dependencies between tokens in the context?
2. Can the authors provide more insights into the relationship between model capacity, context size, response length, and token n-gram influence on context influence and hallucination?
3. What are the potential ethical implications of using CID, and how can they be addressed?

### Rating

5

### Confidence

3

**********
