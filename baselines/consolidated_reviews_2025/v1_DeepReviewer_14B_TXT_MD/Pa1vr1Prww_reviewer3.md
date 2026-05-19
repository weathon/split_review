### Summary

This paper uses sparse autoencoders (SAEs) to explain in-context learning (ICL) in language models. The authors identify two types of features: task-execution features and task-detection features. Task-execution features encode the model’s knowledge of which task to execute and whose latent vectors causally induce the task zero-shot. Task-detection features activate on instances of a complete task in the training data, specifically on the token that completes the task. The authors develop a novel method called task vector cleaning to decompose task vectors into a sparse sum of SAE features. They also adapt the sparse feature circuits (SFC) methodology to work on the more complex ICL task and the larger Gemma-1 2B model. The authors find that task-detection features are causally connected to task-execution features through attention output and transcoder nodes.

### Soundness

3

### Presentation

2

### Contribution

3

### Strengths

1. The paper presents a novel approach to understanding in-context learning (ICL) in language models by using sparse autoencoders (SAEs) to decompose task vectors into interpretable features. The introduction of task vector cleaning and the adaptation of sparse feature circuits (SFC) to ICL are innovative contributions.
2. The paper provides a comprehensive analysis of the proposed methods, including steering experiments and causal analysis. The authors demonstrate the effectiveness of their approach through extensive experiments on the Gemma-1 2B model.
3. The paper is well-organized and clearly written. The authors provide detailed explanations of the methods and results, making it accessible to readers with a background in mechanistic interpretability.

### Weaknesses

#### Some Related Works


#### comment

1. The paper focuses on a specific setting of ICL and a single model architecture (Gemma-1 2B). It is unclear whether the findings generalize to other models or more complex ICL scenarios. The study's reliance on a single model limits the scope of its conclusions. Specifically, the observed task-execution and task-detection features might be artifacts of the Gemma-1 2B architecture and may not be present in other models with different architectural designs or training regimes. The paper does not explore how the identified features might vary across models with different layer configurations, attention mechanisms, or embedding strategies. This raises concerns about the robustness and generalizability of the findings.
2. The paper does not provide a detailed comparison with other methods for analyzing ICL, such as probing or attention analysis. Without such comparisons, it is difficult to assess the relative strengths and weaknesses of the proposed approach. The lack of a comparative analysis makes it challenging to determine whether the proposed SAE-based approach offers a significant advantage over existing techniques. For example, probing classifiers could potentially identify similar task-related information in the model's hidden states, and attention analysis could reveal which parts of the input sequence are most relevant for task execution. The paper needs to demonstrate that the SAE approach provides unique insights that cannot be obtained through these alternative methods.
3. The paper does not discuss the potential ethical implications of its findings, such as the use of ICL for malicious purposes. The ability to understand and manipulate ICL mechanisms could be misused to create models that are more susceptible to adversarial attacks or that exhibit biased behavior. The paper should address these potential risks and discuss how the research community can mitigate them. Furthermore, the paper does not consider the potential for using these insights to develop more robust and secure models, which is a crucial aspect of responsible AI research.

### Suggestions

The authors should conduct a more thorough investigation into the generalizability of their findings by applying their methods to a wider range of models, including those with different architectures and training procedures. This should include models with varying layer depths, attention mechanisms, and embedding strategies. For example, they could test their approach on models like the Llama family or other open-source models to see if the task-execution and task-detection features are consistent across different architectures. Furthermore, they should explore how the identified features change when the model is trained on different datasets or with different training objectives. This would provide a more comprehensive understanding of the robustness and generalizability of their approach. The authors should also consider using a more diverse set of ICL tasks to ensure that their findings are not limited to the specific tasks used in the current study.

To better contextualize the strengths and weaknesses of their approach, the authors should include a detailed comparison with other methods for analyzing ICL, such as probing and attention analysis. This comparison should not only highlight the advantages of the SAE-based approach but also acknowledge its limitations. For example, they could compare the performance of their method in identifying task-related features with the performance of probing classifiers trained on the same hidden states. They could also analyze the attention patterns of the model to see if they align with the task-execution and task-detection features identified by their method. This would provide a more comprehensive understanding of the unique insights provided by the SAE approach and help to establish its value relative to existing techniques. The authors should also discuss the computational cost and scalability of their method compared to other approaches.

Finally, the authors should include a discussion of the potential ethical implications of their work, particularly the risks associated with the misuse of ICL. This discussion should address the potential for using their findings to create models that are more susceptible to adversarial attacks or that exhibit biased behavior. The authors should also consider the potential for using these insights to develop more robust and secure models. This could include exploring how the identified task-execution and task-detection features could be used to detect and mitigate malicious use of ICL. The paper should also discuss the broader societal implications of their work and how the research community can ensure that these powerful techniques are used responsibly.

### Questions

1. How do the identified task-execution and task-detection features generalize to other models and ICL scenarios? Are there any plans to validate the findings on a broader range of models and tasks?
2. Can the authors provide a more detailed comparison with other methods for analyzing ICL, such as probing or attention analysis? What are the advantages and disadvantages of the proposed approach compared to these methods?
3. What are the potential ethical implications of the findings, and how can they be addressed? Are there any plans to explore the use of the identified features for developing more robust and secure models?

### Rating

6

### Confidence

3

**********
