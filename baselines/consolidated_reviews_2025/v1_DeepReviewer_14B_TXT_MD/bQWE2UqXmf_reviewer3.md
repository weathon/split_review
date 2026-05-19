### Summary

This paper proposes a novel approach for detecting AI-generated text. The key idea is to leverage the rewriting behavior of LLMs. The authors observe that LLMs tend to modify human-written text more than AI-generated text when prompted to rewrite. They introduce the RAIDAR method, which detects AI-generated content by prompting LLMs to rewrite text and calculating the editing distance of the output. The method is evaluated on multiple datasets and shows significant improvements over existing detection models.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper presents a novel and insightful observation about the rewriting behavior of LLMs, which forms the basis of the proposed detection method.
2. The RAIDAR method demonstrates significant improvements in detection performance compared to existing models across various domains.
3. The method is compatible with black-box LLMs and does not require access to internal model representations.
4. The paper includes thorough experiments and analysis, demonstrating the effectiveness and robustness of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could benefit from a more detailed analysis of the computational cost and efficiency of RAIDAR, especially when dealing with large volumes of text or real-time detection scenarios.
2. While the paper demonstrates robustness to rephrased text, a more thorough investigation into the method's performance against other types of adversarial attacks or evasion techniques would be valuable.
3. The paper could explore the potential limitations of RAIDAR in cases where the distinction between human and AI-generated text is subtle or where the content is highly technical or domain-specific.

### Suggestions

The paper should delve deeper into the computational demands of the RAIDAR method, particularly concerning its scalability. While the method's core idea is novel, the practical application hinges on its efficiency. The authors should provide a detailed breakdown of the computational resources required, including memory usage, processing time, and the number of LLM calls for varying input sizes. This analysis should consider the impact of different LLMs used for rewriting, as their computational costs can vary significantly. Furthermore, the paper should explore optimization strategies to mitigate these costs, such as parallel processing or efficient text chunking methods. A comparative analysis against existing methods in terms of computational efficiency would also be beneficial to understand the trade-offs.

To strengthen the robustness analysis, the paper should investigate the method's performance against a wider range of adversarial attacks. While rephrasing attacks are considered, other techniques such as paraphrasing, style transfer, or adversarial perturbations could be explored. The authors should also consider attacks that manipulate the semantic content of the text while preserving its overall meaning. This would provide a more comprehensive understanding of the method's vulnerabilities and its ability to generalize to unseen attack scenarios. Additionally, the paper should discuss potential defense mechanisms against these attacks, such as adversarial training or input sanitization techniques. A thorough analysis of these aspects would significantly enhance the practical applicability of the proposed method.

Finally, the paper should address the limitations of RAIDAR in scenarios where the distinction between human and AI-generated text is subtle or highly technical. The authors should explore the method's performance on domain-specific datasets, such as scientific papers, legal documents, or medical reports. These domains often exhibit unique linguistic patterns and technical vocabulary that may challenge the method's detection capabilities. The paper should also discuss the potential for fine-tuning the method for specific domains or exploring alternative features that are more robust to domain-specific variations. Furthermore, the authors should investigate the method's sensitivity to different writing styles and levels of expertise, as these factors can influence the rewriting behavior of LLMs. A more nuanced analysis of these limitations would provide a more realistic assessment of the method's applicability in diverse real-world scenarios.

### Questions

1. How does the computational cost of RAIDAR compare to existing detection methods, especially when dealing with large volumes of text?
2. Have you explored the potential of using RAIDAR for detecting AI-generated content in other modalities, such as images or audio?
3. What are the potential ethical implications of using RAIDAR, particularly in cases where it might be used to falsely accuse individuals of generating AI-text?

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
