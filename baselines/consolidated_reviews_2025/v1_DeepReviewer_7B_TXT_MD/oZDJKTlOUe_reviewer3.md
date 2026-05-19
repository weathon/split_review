### Summary

This paper proposes a post-hoc method to mitigate object hallucination in LVLMs. The authors first analyze the root causes of object hallucination in LVLMs and propose a method to post-hoc rectify object hallucination in LVLMs by constructing a hallucination dataset using GPT-3.5 and training a hallucination revisor. Experiments on six open-source LVLMs show that the proposed method can effectively reduce object hallucination.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The authors analyze the root causes of object hallucination in LVLMs and propose a method to post-hoc rectify object hallucination in LVLMs by constructing a hallucination dataset using GPT-3.5 and training a hallucination revisor.
2. Experiments on six open-source LVLMs show that the proposed method can effectively reduce object hallucination.
3. The paper is well-organized and easy to follow.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method is based on the assumption that object co-occurrence, uncertainty, and position are the main factors that cause hallucinations in LVLMs. However, this assumption is not sufficiently justified and seems overly simplistic. The paper does not adequately explore the complex interplay between these factors and other potential contributors, such as the model's training data biases or the inherent limitations of autoregressive generation. For example, a model might hallucinate due to a lack of exposure to certain object co-occurrences during training, rather than a simple co-occurrence bias itself. The paper needs to provide a more nuanced analysis of the causes of hallucinations, moving beyond these three factors.
2. The proposed method relies heavily on the quality of the generated descriptions used to train the hallucination reviser. The paper does not sufficiently address the potential for error propagation from the generated descriptions to the reviser. If the initial descriptions contain subtle or incorrect hallucinations, the reviser might learn to perpetuate these errors, rather than correcting them. The paper should include an analysis of the sensitivity of the method to the quality of the training data for the reviser, and explore methods to mitigate the impact of potentially flawed initial descriptions.
3. The experimental evaluation is limited in scope and does not fully demonstrate the robustness and generalizability of the proposed method. The experiments are primarily conducted on the MSCOCO dataset, which may not be representative of all real-world scenarios. The paper should include experiments on a wider range of datasets, including those with more complex scenes and object interactions, to demonstrate the method's effectiveness in diverse settings. Furthermore, the evaluation should include a more comprehensive set of metrics to assess the quality of the corrected descriptions, such as metrics that measure the factual accuracy and consistency of the descriptions.

### Suggestions

The paper would benefit from a more thorough investigation into the underlying causes of object hallucination in LVLMs. The current analysis, while identifying co-occurrence, uncertainty, and position as key factors, lacks a deeper exploration of the interplay between these factors and other potential contributors. For instance, the authors could explore the impact of different training data biases on hallucination, such as the frequency of certain object co-occurrences or the presence of specific types of captions. Furthermore, the paper should investigate the limitations of autoregressive generation in the context of object hallucination, such as the accumulation of errors during the generation process. A more nuanced analysis of these factors would strengthen the theoretical foundation of the proposed method and provide a more comprehensive understanding of the problem.

To address the reliance on the quality of generated descriptions, the authors should explore methods to mitigate the impact of potentially flawed initial descriptions on the hallucination reviser. This could involve techniques such as data augmentation, where the generated descriptions are perturbed to create a more robust training set, or the use of adversarial training, where the reviser is trained to be robust to noisy descriptions. Additionally, the paper should investigate the sensitivity of the method to the quality of the training data for the reviser, and provide guidelines for selecting appropriate training data. The authors could also explore methods to identify and filter out potentially flawed initial descriptions, such as using a separate model to detect hallucinations in the generated descriptions before they are used to train the reviser. These approaches would enhance the robustness and reliability of the proposed method.

Finally, the experimental evaluation should be expanded to include a wider range of datasets and metrics to demonstrate the robustness and generalizability of the proposed method. The current evaluation is primarily conducted on the MSCOCO dataset, which may not be representative of all real-world scenarios. The authors should include experiments on datasets with more complex scenes and object interactions, such as those found in natural images or videos. Furthermore, the evaluation should include a more comprehensive set of metrics to assess the quality of the corrected descriptions, such as metrics that measure the factual accuracy and consistency of the descriptions. The authors should also compare their method to other state-of-the-art hallucination mitigation techniques, including both post-hoc methods and methods that involve modifying the training process. This would provide a more comprehensive evaluation of the proposed method and its effectiveness compared to existing approaches.

### Questions

1. How does the proposed method handle cases where the generated descriptions are already accurate or do not contain hallucinations?
2. What are the computational costs associated with training and deploying the hallucination reviser? How does this compare to the computational costs of other hallucination mitigation methods?
3. How does the method perform on tasks that require more complex reasoning and understanding of the visual context, such as visual question answering or image captioning?

### Rating

6

### Confidence

4

**********
