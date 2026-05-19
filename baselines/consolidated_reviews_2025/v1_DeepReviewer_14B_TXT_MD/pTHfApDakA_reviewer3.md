### Summary

This paper proposes a zero-shot verification schema called SELFCHECK for LLMs to recognize errors in their own step-by-step reasoning. The authors test SELFCHECK on three datasets and find that it successfully recognizes errors and increases final answer accuracies. The paper also discusses the limitations of the method and suggests future research directions.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper introduces a novel method called SELFCHECK, which is a zero-shot verification schema for LLMs to recognize errors in their own step-by-step reasoning.
2. The authors conduct experiments on three datasets and find that SELFCHECK successfully recognizes errors and increases final answer accuracies.
3. The paper is well-written and easy to understand.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational cost of SELFCHECK. It would be helpful to know how much additional time and resources are required to use SELFCHECK compared to other methods.
2. The paper does not discuss the potential for SELFCHECK to be used in other domains or tasks. It would be interesting to see how SELFCHECK performs on tasks other than math problems.
3. The paper does not provide a comparison of SELFCHECK to other error detection methods. It would be helpful to see how SELFCHECK compares to other methods in terms of accuracy and efficiency.

### Suggestions

The paper introduces an interesting self-verification method, but it would benefit from a more thorough analysis of its computational demands. Specifically, the authors should provide a breakdown of the time spent on each stage of the SELFCHECK process (e.g., target extraction, information collection, step regeneration, and result comparison). This would allow for a more precise understanding of the overhead introduced by the method. Furthermore, it would be beneficial to compare the computational cost of SELFCHECK against other error detection methods, such as those based on symbolic execution or formal verification. This comparison should not only focus on the total time but also consider the number of API calls and the memory footprint of each approach. Such an analysis would help to determine the practical applicability of SELFCHECK in resource-constrained environments.

To further strengthen the paper, the authors should explore the potential of SELFCHECK in domains beyond mathematical reasoning. While the current focus on math problems is valuable, it is important to assess the generalizability of the method. For example, could SELFCHECK be applied to tasks involving natural language understanding, such as question answering or text summarization? In these domains, the notion of 'step-by-step reasoning' might be less explicit, requiring adaptations to the SELFCHECK framework. The authors could consider how the target extraction and information collection stages would need to be modified to handle more complex and less structured reasoning processes. Exploring these aspects would significantly broaden the impact of the proposed method.

Finally, a more comprehensive comparison to existing error detection methods is needed. The paper should not only compare SELFCHECK to other self-correction methods but also to external verification techniques. This comparison should include a detailed analysis of the strengths and weaknesses of each approach, considering factors such as accuracy, efficiency, and the types of errors that each method is best suited to detect. For instance, how does SELFCHECK compare to methods that use external knowledge bases or symbolic solvers? A thorough comparison would help to position SELFCHECK within the broader landscape of error detection techniques and highlight its unique contributions.

### Questions

1. How does the computational cost of SELFCHECK compare to other error detection methods?
2. Can SELFCHECK be used in other domains or tasks besides math problems?
3. How does SELFCHECK compare to other error detection methods in terms of accuracy and efficiency?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
