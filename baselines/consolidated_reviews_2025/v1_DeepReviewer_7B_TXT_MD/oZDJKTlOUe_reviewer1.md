### Summary

This paper proposes a post-hoc method called LVLM Hallucination Revisor (LURE) to rectify object hallucination in LVLMs. LURE is grounded in three key factors that contribute to object hallucination: co-occurrence, uncertainty, and object position. The authors demonstrate the effectiveness of LURE in mitigating object hallucination in LVLM-generated descriptions through experiments on six open-source LVLMs.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

The proposed method is lightweight and can be easily integrated with any LVLMs.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method is based on the assumption that object co-occurrence, uncertainty, and position are the main factors that cause hallucinations in LVLMs. However, this assumption is not sufficiently justified and seems overly simplistic. The paper does not adequately explore the complex interplay between these factors and other potential contributors, such as the model's training data biases or the inherent limitations of autoregressive generation. For example, a model might hallucinate due to a lack of exposure to certain object co-occurrences during training, rather than a simple co-occurrence bias itself. The paper needs to provide a more nuanced analysis of the causes of hallucinations, moving beyond these three factors.
2. The proposed method relies heavily on the quality of the generated descriptions used to train the hallucination reviser. The paper does not sufficiently address the potential for error propagation from the generated descriptions to the reviser. If the initial descriptions contain subtle or incorrect hallucinations, the reviser might learn to perpetuate these errors, rather than correcting them. The paper should include an analysis of the sensitivity of the method to the quality of the training data for the reviser, and explore methods to mitigate the impact of potentially flawed initial descriptions.
3. The experimental evaluation is limited in scope and does not fully demonstrate the robustness and generalizability of the proposed method. The experiments are primarily conducted on the MSCOCO dataset, which may not be representative of all real-world scenarios. The paper should include experiments on a wider range of datasets, including those with more complex scenes and object interactions, to demonstrate the method's effectiveness in diverse settings. Furthermore, the evaluation should include a more comprehensive set of metrics to assess the quality of the corrected descriptions, such as metrics that measure the factual accuracy and consistency of the descriptions.

### Suggestions

To address the limitations of the assumption regarding the causes of hallucinations, the authors should conduct a more in-depth analysis of the factors contributing to object hallucination in LVLMs. This could involve a more comprehensive literature review that explores the role of training data biases, model architecture, and the specific mechanisms of autoregressive generation. The authors could also consider using techniques such as causal analysis or ablation studies to isolate the impact of each factor on hallucination. Furthermore, the authors should investigate the interplay between these factors and explore how they interact to produce hallucinations. For example, they could examine whether certain combinations of co-occurrence, uncertainty, and position are more likely to lead to hallucinations than others. This more nuanced understanding would provide a stronger foundation for the proposed method and potentially lead to more effective solutions.

To address the reliance on the quality of the generated descriptions for training the hallucination reviser, the authors should explore methods to mitigate the impact of potentially flawed initial descriptions. This could involve using techniques such as data augmentation or adversarial training to improve the robustness of the reviser to noisy data. The authors could also consider using a more diverse set of generated descriptions, including those with varying levels of hallucination, to train the reviser. Furthermore, the authors should investigate the sensitivity of the method to the quality of the training data for the reviser and provide guidelines for selecting appropriate training data. The paper should also include an analysis of the error propagation from the generated descriptions to the reviser, and explore methods to mitigate this issue. This would provide a more comprehensive understanding of the limitations of the proposed method and potential avenues for improvement.

To address the limited scope of the experimental evaluation, the authors should conduct experiments on a wider range of datasets, including those with more complex scenes and object interactions. This would demonstrate the robustness and generalizability of the proposed method in diverse settings. The authors should also include a more comprehensive set of metrics to assess the quality of the corrected descriptions, such as metrics that measure the factual accuracy and consistency of the descriptions. Furthermore, the authors should compare the performance of the proposed method with other state-of-the-art hallucination mitigation techniques, including both post-hoc methods and methods that involve modifying the training process. This would provide a more comprehensive evaluation of the proposed method and its effectiveness compared to existing approaches. The authors should also consider conducting experiments on datasets with different types of hallucinations, such as those involving rare objects or unusual object interactions, to further demonstrate the robustness of the method.

### Questions

1. The proposed method relies heavily on the assumption that object co-occurrence, uncertainty, and position are the main factors that cause hallucinations in LVLMs. However, this assumption is not sufficiently justified and seems overly simplistic. Can the authors provide more evidence or theoretical support for this assumption?
2. The proposed method relies heavily on the quality of the generated descriptions used to train the hallucination reviser. How does the method perform when the generated descriptions contain errors or hallucinations? Are there any mechanisms in place to mitigate the impact of potentially flawed initial descriptions?
3. The experimental evaluation is limited in scope and does not fully demonstrate the robustness and generalizability of the proposed method. Can the authors provide more details about the experimental setup and the datasets used? How does the method perform on datasets with different types of hallucinations or in more complex scenarios?

### Rating

5

### Confidence

4

**********
