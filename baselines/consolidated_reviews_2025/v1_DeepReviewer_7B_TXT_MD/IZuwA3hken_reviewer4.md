### Summary

This paper proposes a principled definition for context influence and Context Influence Decoding (CID), which is a method to control the influence of the context on the output of LLMs. The authors show that amplifying the context (by factoring out prior knowledge) and mitigating hallucination are linked, and that CID can reduce context influence on output while lowering privacy leakage. They also show that amplifying the context by factoring out prior knowledge to reduce hallucination causes more influence of the context on the output, and that the context influence is bounded by the private information leakage of the context. Finally, they show that the influence of the context on the output is affected by model capacity, context size, response length, and different token n-grams of the context.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper is well-written and easy to follow.
- The paper provides a principled definition for context influence and proposes Context Influence Decoding (CID), which is a method to control the influence of the context on the output of LLMs.
- The paper shows that amplifying the context (by factoring out prior knowledge) and mitigating hallucination are linked, and that CID can reduce context influence on output while lowering privacy leakage.
- The paper also shows that amplifying the context by factoring out prior knowledge to reduce hallucination causes more influence of the context on the output, and that the context influence is bounded by the private information leakage of the context.
- The paper shows that the influence of the context on the output is affected by model capacity, context size, response length, and different token n-grams of the context.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a detailed analysis of the computational overhead of CID, which could be a concern for practical applications.
- The paper does not compare CID with other state-of-the-art methods for hallucination mitigation, such as retrieval-augmented generation or fact verification techniques. It would be beneficial to see how CID performs relative to these methods in terms of both hallucination reduction and context influence.
- The paper does not explore the potential limitations of CID, such as its sensitivity to the choice of the tunable parameter λ. It would be helpful to understand how the performance of CID varies with different values of λ and how to choose an appropriate value for a given task.

### Suggestions

The paper introduces Context Influence Decoding (CID) as a method to control the influence of context on LLM outputs, which is a valuable contribution. However, the practical applicability of CID is limited by the lack of a detailed computational cost analysis. The authors should provide a more thorough analysis of the time and memory requirements of CID, especially when applied to large language models and long contexts. This analysis should include a breakdown of the computational costs associated with each step of the CID process, such as the calculation of context influence and the decoding process itself. Furthermore, it would be beneficial to compare the computational overhead of CID with other methods for mitigating hallucinations, such as retrieval-augmented generation or fact verification techniques, to provide a more complete picture of its practical feasibility. This would allow practitioners to make informed decisions about whether to use CID in their applications.

In addition to the computational overhead, the paper would benefit from a more comprehensive comparison of CID with existing state-of-the-art methods for hallucination mitigation. While the paper demonstrates that amplifying context reduces hallucination, it does not compare CID with other techniques that explicitly address hallucination, such as retrieval-augmented generation or fact verification. A thorough comparison should include a quantitative evaluation of both hallucination reduction and context influence, as well as a qualitative analysis of the types of errors made by each method. This would help to establish the relative strengths and weaknesses of CID and to identify the scenarios in which it is most effective. For example, it would be useful to see how CID performs on tasks that require precise factual knowledge versus tasks that require more creative or generative responses.

Finally, the paper should provide a more detailed analysis of the sensitivity of CID to the choice of the tunable parameter λ. The authors should investigate how the performance of CID varies with different values of λ and provide guidance on how to choose an appropriate value for a given task. This analysis should include a discussion of the trade-offs between context influence and other performance metrics, such as hallucination reduction and accuracy. Furthermore, it would be helpful to explore adaptive strategies for setting λ, such as using a validation set to tune the parameter or using a heuristic based on the characteristics of the input context. This would make CID more robust and easier to use in practice.

### Questions

- How does the computational overhead of CID compare to other methods for mitigating hallucinations?
- How does CID compare to other state-of-the-art methods for hallucination mitigation, such as retrieval-augmented generation or fact verification techniques?
- How sensitive is CID to the choice of the tunable parameter λ, and how should λ be chosen for different tasks and contexts?

### Rating

6

### Confidence

3

**********
