### Summary

This paper proposes LVLM Hallucination Revisor (LURE), a post-hoc method to reduce object hallucination in large vision-language models (LVLMs). The method is grounded in a statistical analysis of key factors underlying object hallucinations, including co-occurrence, uncertainty, and object position. The authors evaluate LURE on six open-source LVLMs and find it outperforms the baselines in reducing object hallucination.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is lightweight and can be easily integrated with any LVLMs.
3. The authors conduct extensive experiments on six open-source LVLMs and show that LURE outperforms the baselines in reducing object hallucination.
4. The authors provide a comprehensive analysis of object hallucination in LVLMs, identifying key factors such as co-occurrence, uncertainty, and object position.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method is based on the assumption that object co-occurrence, uncertainty, and position are the main factors that cause hallucinations in LVLMs. However, this assumption is not sufficiently justified and seems overly simplistic. The paper does not adequately explore the complex interplay between these factors and other potential contributors, such as the model's training data biases or the inherent limitations of autoregressive generation. For example, a model might hallucinate due to a lack of exposure to certain object co-occurrences during training, rather than a simple co-occurrence bias itself. The paper needs to provide a more nuanced analysis of the causes of hallucinations, moving beyond these three factors.
2. The proposed method relies heavily on the quality of the generated descriptions used to train the hallucination reviser. The paper does not sufficiently address the potential for error propagation from the generated descriptions to the reviser. If the initial descriptions contain subtle or incorrect hallucinations, the reviser might learn to perpetuate these errors, rather than correcting them. The paper should include an analysis of the sensitivity of the method to the quality of the training data for the reviser, and explore methods to mitigate the impact of potentially flawed initial descriptions.
3. The experimental evaluation is limited in scope and does not fully demonstrate the robustness and generalizability of the proposed method. The experiments are primarily conducted on the MSCOCO dataset, which may not be representative of all real-world scenarios. The paper should include experiments on a wider range of datasets, including those with more complex scenes and object interactions, to demonstrate the method's effectiveness in diverse settings. Furthermore, the evaluation should include a more comprehensive set of metrics to assess the quality of the corrected descriptions, such as metrics that measure the factual accuracy and consistency of the descriptions.

### Suggestions

The paper's core weakness lies in its oversimplified assumption that object co-occurrence, uncertainty, and position are the primary drivers of hallucination in LVLMs. While these factors may play a role, the paper fails to acknowledge the complexity of the problem. For instance, training data biases could significantly influence hallucination, as certain object co-occurrences might be underrepresented, leading to models generating hallucinations for objects that are rarely seen together. Similarly, the inherent limitations of autoregressive generation could contribute to hallucinations, as the model might struggle to maintain consistency across the generated sequence. The paper should explore these alternative explanations and provide a more nuanced analysis of the causes of hallucination. This could involve analyzing the training data for biases, conducting ablation studies to isolate the impact of different factors, and exploring the limitations of autoregressive generation in the context of object hallucination. A more thorough investigation into these aspects would significantly strengthen the paper's claims and provide a more comprehensive understanding of the problem.

Furthermore, the paper's reliance on the quality of generated descriptions for training the hallucination reviser is a significant concern. The method's effectiveness is directly tied to the accuracy of the initial descriptions, and any errors or hallucinations in the generated descriptions could be propagated to the reviser. The paper should include a detailed analysis of the sensitivity of the method to the quality of the training data. This could involve training the reviser with descriptions that contain varying levels of hallucination and evaluating the performance of the method under these conditions. Additionally, the paper should explore methods to mitigate the impact of potentially flawed initial descriptions. This could involve using techniques such as data augmentation, adversarial training, or incorporating uncertainty estimates into the training process. Addressing this issue is crucial for ensuring the robustness and reliability of the proposed method.

Finally, the experimental evaluation is limited in scope and does not fully demonstrate the robustness and generalizability of the proposed method. The experiments are primarily conducted on the MSCOCO dataset, which may not be representative of all real-world scenarios. The paper should include experiments on a wider range of datasets, including those with more complex scenes and object interactions, to demonstrate the method's effectiveness in diverse settings. Furthermore, the evaluation should include a more comprehensive set of metrics to assess the quality of the corrected descriptions, such as metrics that measure the factual accuracy and consistency of the descriptions. This could involve using metrics such as object hallucination rate, entity consistency, and description coherence. A more thorough evaluation would provide a more robust assessment of the method's performance and its applicability to real-world scenarios.

### Questions

Please refer to the weaknesses.

### Rating

6

### Confidence

4

**********
