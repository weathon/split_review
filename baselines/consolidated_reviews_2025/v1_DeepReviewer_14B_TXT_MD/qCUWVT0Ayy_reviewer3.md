### Summary

This paper proposes LayoutNUWA, a novel approach that treats layout generation as a code generation task. The model leverages the formatting knowledge of large language models (LLMs) to generate layouts in code language, which are then rendered into the final graphic layout. The authors introduce a Code Instruct Tuning (CIT) approach, which consists of three interconnected modules: Code Initialization, Code Completion, and Code Rendering. The experimental results demonstrate that LayoutNUWA significantly outperforms existing methods on multiple datasets, showcasing its strong capabilities in conditional layout generation tasks.

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

1. The paper does not provide a detailed analysis of the computational cost and efficiency of the proposed method compared to existing approaches. This information is crucial for evaluating the practicality of the method in real-world applications. Specifically, the paper lacks a breakdown of the inference time for each module of the proposed method (Code Initialization, Code Completion, and Code Rendering), making it difficult to pinpoint potential bottlenecks. Furthermore, a comparison of memory usage and training time with existing methods would be beneficial.
2. The paper does not discuss the potential limitations or failure cases of the proposed method. Understanding these limitations is important for identifying areas for future improvement. For example, it would be valuable to know how the method performs on extremely complex layouts or when the input conditions are ambiguous or contradictory. The paper should also discuss the sensitivity of the method to the choice of LLM and the impact of different code generation strategies.
3. The paper does not explore the potential for extending the proposed method to other layout generation tasks or domains. This could limit the impact and applicability of the research. For instance, the method's performance on different types of layouts (e.g., web pages, documents, user interfaces) and its adaptability to different design languages should be investigated. The paper should also discuss the potential for incorporating user feedback or constraints into the layout generation process.

### Suggestions

To address the lack of computational cost analysis, the authors should provide a detailed breakdown of the inference time for each module of LayoutNUWA, including Code Initialization, Code Completion, and Code Rendering. This should be compared with the inference times of existing methods, such as LayoutDM, to provide a clear understanding of the computational overhead introduced by the code generation approach. Furthermore, the authors should include a comparison of memory usage and training time, which are crucial for evaluating the practicality of the method. This analysis should be performed on a standardized hardware setup to ensure fair comparisons. It would also be beneficial to explore the impact of different LLM sizes on the computational cost and performance of LayoutNUWA, providing insights into the trade-offs between accuracy and efficiency.

To address the lack of discussion on limitations and failure cases, the authors should conduct a thorough analysis of the method's performance on challenging layouts and ambiguous input conditions. This should include examples of failure cases, along with a discussion of the underlying reasons for these failures. For instance, the authors could investigate how the method handles layouts with a large number of elements, overlapping elements, or unusual aspect ratios. They should also explore the sensitivity of the method to the choice of LLM and the impact of different code generation strategies. This analysis should provide valuable insights into the robustness and reliability of the method and identify areas for future improvement. The authors should also consider incorporating techniques to handle ambiguous or contradictory input conditions, such as using a probabilistic approach or incorporating user feedback.

To enhance the applicability of the proposed method, the authors should explore its potential for extension to other layout generation tasks and domains. This could include evaluating the method on different types of layouts, such as web pages, documents, and user interfaces, and investigating its adaptability to different design languages. The authors should also discuss the potential for incorporating user feedback or constraints into the layout generation process, which would make the method more interactive and user-friendly. Furthermore, the authors should explore the possibility of using the method for layout optimization, where the goal is to find the best layout that satisfies certain criteria, such as aesthetic appeal or usability. This would significantly broaden the impact and applicability of the research.

### Questions

1. Can the authors provide more details on the computational cost and efficiency of the proposed method compared to existing approaches?
2. What are the potential limitations or failure cases of the proposed method, and how can they be addressed?
3. Can the proposed method be extended to other layout generation tasks or domains, and what are the potential challenges in doing so?

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
