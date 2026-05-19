### Summary

This paper proposes a post-hoc method, LVLM Hallucination Revisor (LURE), to mitigate object hallucination in large vision-language models (LVLMs). LURE is grounded in a statistical analysis of key factors underlying object hallucinations, including co-occurrence, uncertainty, and object position. The method is lightweight and can be seamlessly integrated with any LVLM. The authors evaluate LURE on six open-source LVLMs and demonstrate its effectiveness in reducing object hallucinations.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-structured and clearly written, making it easy to follow and understand. The authors provide a comprehensive analysis of object hallucinations in LVLMs, identifying key factors such as co-occurrence, uncertainty, and position. This analysis is insightful and provides a solid foundation for the proposed method.
2. The proposed method, LVLM Hallucination Revisor (LURE), is lightweight and can be seamlessly integrated with any LVLM. This makes it a practical and versatile solution for reducing object hallucinations in real-world applications.
3. The authors evaluate LURE on six open-source LVLMs and demonstrate its effectiveness in reducing object hallucinations. The experimental results are comprehensive and provide strong evidence for the effectiveness of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method, LVLM Hallucination Revisor (LURE), relies on a set of rules to identify and correct hallucinatory descriptions. While these rules are effective, they may not be comprehensive enough to address all types of hallucinations. For example, the method may struggle with more complex or nuanced hallucinations that do not fit neatly into the defined categories. The reliance on a rule-based system could limit its adaptability to diverse scenarios and may require significant manual tuning to cover all potential cases. The method's effectiveness is also tied to the quality of the generated descriptions used to train the hallucination reviser, and any biases or limitations in these descriptions could propagate to the final results.
2. The authors evaluate LURE on six open-source LVLMs, which is a good start. However, it would be beneficial to evaluate the method on a wider range of models, including both open-source and closed-source models. This would provide a more comprehensive understanding of the method's generalizability and robustness. The current evaluation does not fully explore the method's performance across different model architectures and training datasets, which could limit the conclusions that can be drawn about its effectiveness.
3. The authors mention that the method can be seamlessly integrated with any LVLM. However, it would be helpful to provide more details on how the method can be adapted to different types of LVLMs, especially those with different architectures or training objectives. The paper lacks a detailed discussion of the specific implementation challenges and solutions for integrating LURE with various LVLMs. This makes it difficult to assess the method's practical applicability and potential limitations.

### Suggestions

To address the limitations of the rule-based approach, the authors should explore incorporating a more adaptive mechanism that can learn from the model's outputs and adjust the correction strategy accordingly. This could involve using a reinforcement learning framework or a meta-learning approach to fine-tune the hallucination reviser. For example, the reviser could be trained to identify and correct hallucinations based on the model's confidence scores and the context of the generated descriptions. This would allow the method to adapt to different types of hallucinations and improve its overall performance. Furthermore, the authors should investigate the use of more sophisticated techniques for identifying hallucinations, such as attention mechanisms or graph-based methods, which could provide a more nuanced understanding of the model's outputs.

To enhance the evaluation of LURE, the authors should conduct experiments on a wider range of LVLMs, including both open-source and closed-source models. This would provide a more comprehensive understanding of the method's generalizability and robustness. The evaluation should also include a more diverse set of tasks and datasets, including those with more complex scenes and object interactions. This would help to identify the limitations of the method and provide insights into its performance in different scenarios. Additionally, the authors should consider evaluating the method's performance on tasks that require more complex reasoning and understanding of the visual context, such as visual question answering or image captioning.

To address the lack of details on integrating LURE with different LVLMs, the authors should provide a more detailed explanation of the specific implementation challenges and solutions for different model architectures. This should include a discussion of the necessary modifications to the model's input and output formats, as well as the specific training procedures that are required. The authors should also provide examples of how LURE can be integrated with different types of LVLMs, including those with different training objectives and architectures. This would make it easier for other researchers to adopt and adapt the method to their own applications.

### Questions

1. How does the proposed method handle cases where the generated descriptions are already accurate or do not contain hallucinations?
2. What are the computational costs associated with training and deploying the hallucination reviser? How does this compare to the computational costs of other hallucination mitigation methods?
3. How does the method perform on tasks that require more complex reasoning and understanding of the visual context, such as visual question answering or image captioning?

### Rating

6

### Confidence

4

**********
