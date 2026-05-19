### Summary

This paper proposes a new prompting framework called Problem Representation Enhanced CoT (PRECOT), which aims to improve the reasoning capabilities of large language models (LLMs). The authors argue that constructing problem representations is a crucial aspect of human problem-solving and propose a two-stage approach to incorporate this into the reasoning process of LLMs. The first stage involves extracting the initial and goal states of the problem, while the second stage initiates an enhanced solution process based on the generated problem representation. The authors evaluate their approach on various benchmarks across arithmetic, commonsense, and symbolic reasoning domains, demonstrating that PRECOT outperforms traditional CoT on most tasks in both few-shot and zero-shot settings.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper introduces a novel approach to enhance the reasoning capabilities of LLMs by incorporating problem representation construction, inspired by cognitive psychology. This approach provides a new perspective on improving the performance of LLMs in multi-step reasoning tasks.

2. The authors conduct extensive evaluations on multiple domain benchmarks, demonstrating the effectiveness of their proposed approach. The results show that PRECOT outperforms existing methods in most cases, highlighting its potential for improving the reasoning performance of LLMs.

3. The paper is well-written and easy to follow, with clear explanations of the proposed method and experimental setup. The authors also provide detailed analyses of the results, further supporting the effectiveness of their approach.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational cost associated with the proposed approach. It would be beneficial to understand the additional overhead introduced by the problem representation construction stage and its impact on the overall efficiency of the reasoning process.

2. While the authors mention that their approach is inspired by cognitive psychology, they do not provide a thorough discussion of the connection between their work and relevant theories or findings in this field. It would be valuable to see a more detailed explanation of how the proposed method aligns with or builds upon existing knowledge in cognitive psychology.

3. The paper primarily focuses on the performance improvements achieved by PRECOT compared to existing methods. However, it would be interesting to investigate the interpretability of the generated problem representations and their potential for providing insights into the reasoning process of LLMs.

### Suggestions

The paper introduces an interesting approach by incorporating problem representation into the reasoning process of LLMs, but there are several areas that could be strengthened. First, a more detailed analysis of the computational overhead is needed. While the paper mentions a two-stage approach, it does not quantify the additional time or resources required for the problem representation construction stage. For example, it would be beneficial to know how the time complexity scales with the size of the input problem or the complexity of the reasoning task. Furthermore, it would be useful to compare the computational cost of PRECOT with other prompting techniques, such as Chain-of-Thought (CoT), to understand the trade-offs between performance gains and computational overhead. This analysis should include not only the time taken but also the number of API calls and the overall resource consumption, which are crucial for practical applications.

Second, the connection to cognitive psychology needs to be more thoroughly explored. While the paper mentions inspiration from human problem-solving, it lacks a detailed discussion of specific cognitive theories or models that support the proposed approach. For instance, the authors could discuss how the concept of problem representation aligns with existing cognitive models of problem-solving, such as the problem-space theory or the ACT-R framework. A more in-depth analysis of these connections would strengthen the theoretical foundation of the work and provide a more solid justification for the proposed method. It would also be beneficial to discuss how the proposed method might relate to human cognitive biases or limitations, and whether it can help mitigate these issues in LLMs.

Finally, the paper should delve deeper into the interpretability of the generated problem representations. While the paper demonstrates performance improvements, it does not explore the nature of the representations themselves. It would be valuable to analyze the structure and content of the generated problem representations to understand what kind of information is being captured and how it contributes to the improved reasoning performance. For example, are the representations capturing key entities, relationships, or constraints? Can these representations be visualized or analyzed to gain insights into the reasoning process of LLMs? Furthermore, it would be interesting to investigate whether the quality of the problem representation correlates with the quality of the final solution, and whether poor representations can be identified and corrected.

### Questions

Please see the Weaknesses.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
