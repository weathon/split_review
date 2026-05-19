### Summary

This paper proposes LayoutNUWA, a model that treats layout generation as a code generation task to enhance semantic information and harness the hidden layout expertise of large language models (LLMs). The approach comprises three interconnected modules: Code Initialization (CI), Code Completion (CC), and Code Rendering (CR). The CI module quantifies numerical conditions and initializes them as HTML code with strategically placed masks. The CC module employs the formatting knowledge of LLMs to fill in the masked portions within the HTML code. The CR module transforms the completed code into the final layout output, ensuring a highly interpretable and transparent layout generation procedure that directly maps code to a visualized layout. The paper demonstrates significant state-of-the-art performance on multiple datasets, showcasing the strong capabilities of LayoutNUWA.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper introduces a novel approach to layout generation by treating it as a code generation task, which is a creative and innovative idea.
2. The proposed Code Instruct Tuning (CIT) approach is well-designed and effectively leverages the formatting knowledge of large language models (LLMs).
3. The experimental results demonstrate that LayoutNUWA significantly outperforms existing methods on multiple datasets, showcasing its strong capabilities in conditional layout generation tasks.
4. The paper is well-written and easy to follow, with clear explanations of the methodology and experimental setup.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational cost and efficiency of the proposed method compared to existing approaches. This information is crucial for evaluating the practicality of the method in real-world applications.
2. The paper does not discuss the potential limitations or failure cases of the proposed method. Understanding these limitations is important for identifying areas for future improvement.
3. The paper does not explore the potential for extending the proposed method to other layout generation tasks or domains. This could limit the impact and applicability of the research.

### Suggestions

The paper would benefit from a more thorough analysis of the computational overhead introduced by the code generation approach. While the authors mention the use of LLMs, they do not provide a detailed breakdown of the inference time for each module (Code Initialization, Code Completion, and Code Rendering). A comparison of the inference time with existing methods, such as LayoutDM, would be valuable. Furthermore, the paper should include a discussion of the memory requirements and training time, which are crucial for practical applications. This analysis should include a breakdown of the time spent in each stage of the pipeline, allowing for a better understanding of the bottlenecks and potential areas for optimization. For example, the authors could analyze the time spent on tokenization, LLM inference, and code rendering, and compare these to the time spent on similar tasks in other layout generation methods. This would provide a more complete picture of the computational cost of the proposed approach.

To address the lack of discussion on limitations and failure cases, the authors should provide a more in-depth analysis of the scenarios where the proposed method might struggle. For example, it would be beneficial to explore how the method performs on extremely complex layouts or when the input conditions are ambiguous or contradictory. The paper should also discuss the sensitivity of the method to the choice of LLM and the impact of different code generation strategies. A qualitative analysis of failure cases, including visual examples, would be particularly helpful in understanding the limitations of the approach. Furthermore, the authors should investigate the robustness of the method to variations in the input data, such as different types of layout elements or varying levels of noise. This would help to identify the strengths and weaknesses of the proposed method and guide future research directions.

Finally, the paper should explore the potential for extending the proposed method to other layout generation tasks or domains. For example, the authors could investigate the applicability of the method to different types of layouts, such as web pages, documents, or user interfaces. They could also explore the possibility of incorporating user feedback or constraints into the layout generation process. This would significantly broaden the impact and applicability of the research. The authors should also discuss the potential challenges in adapting the method to different domains, such as the need for domain-specific code templates or the difficulty of handling different types of layout elements. This discussion should include a consideration of the trade-offs between the generality of the approach and its performance on specific tasks.

### Questions

1. Can the authors provide more details on the computational cost and efficiency of the proposed method compared to existing approaches?
2. What are the potential limitations or failure cases of the proposed method, and how can they be addressed?
3. Can the proposed method be extended to other layout generation tasks or domains, and what are the potential challenges in doing so?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
