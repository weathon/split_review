### Summary

This work applies sparse autoencoders to study in-context learning in large language models. Specifically, the work builds on top of the task vector and sparse feature circuit concepts. Through the task vector cleaning (TVC) method, the authors find task-execution features that can replace task vectors. The authors also find task-detection features with SFC that are involved in identifying the specific task being performed earlier in the prompt.

### Soundness

2

### Presentation

1

### Contribution

2

### Strengths

- The paper proposes TVC, a method to decompose task vectors into a sparse sum of dictionary vectors. TVC could be a useful tool to study in-context learning.

- The paper adapts the SFE methodology to the ICL task and larger models, introducing the concept of task-detection features.

### Weaknesses

#### Some Related Works


#### comment

 - The paper is not very well written. Many details are missing and the overall flow is not clear. I will list some below:
    - The TVC algorithm is not clearly described. It would be helpful to describe the algorithm in text (as is done for other things in the paper) in addition to the figures. Specifically, the optimization objective and the exact steps for updating the sparse decomposition weights are unclear. The connection between the loss function and the resulting task execution features is not explicitly stated.
    - It would be helpful to describe the datasets used for the steering experiments. The lack of detail makes it difficult to assess the generalizability of the findings. What types of tasks are included? What is the size of the dataset? Are there any specific characteristics of the dataset that might influence the results?
    - It would be helpful to describe the layers used for SFE. Are they from the encoder or the decoder? What is the rationale for choosing these specific layers? How does the choice of layers impact the identified feature circuits?
    - It is unclear what Figure 7 shows. The axes are not labeled, and the meaning of the colored regions is not explained. It would be helpful to describe the experiment in text in addition to the figure caption. What are the inputs and outputs of the experiment? What is the significance of the results?
- The paper does not clearly explain the significance and implications of the findings. It would be helpful to summarize the findings and explain their significance in the context of what is already known. For example, how do the discovered task-execution features compare to previously identified task vectors? What new insights do the task-detection features provide about the mechanism of in-context learning? What are the limitations of the current approach?

### Suggestions

To improve the clarity and impact of the paper, I suggest a thorough revision of the methodology and results sections. For the TVC algorithm, a step-by-step description of the optimization process, including the specific loss function used and the update rules for the sparse decomposition weights, is necessary. A clear explanation of how this optimization leads to the identification of task-execution features is also crucial. For example, the authors could explain how the sparsity constraint influences the selection of features and how these selected features relate to the original task vectors. Additionally, providing a pseudocode representation of the TVC algorithm would greatly enhance clarity. Furthermore, the authors should elaborate on the datasets used for the steering experiments. This should include a detailed description of the task types, dataset size, and any specific characteristics that might influence the results. For instance, if the dataset consists of various NLP tasks, the authors should specify the range of tasks (e.g., text classification, question answering, summarization) and provide examples of each. This would allow readers to better understand the scope and limitations of the experimental setup. The authors should also justify the choice of layers used for SFE, explaining whether they are from the encoder or decoder and the rationale behind this selection. A discussion of how the choice of layers impacts the identified feature circuits would be beneficial. For example, the authors could discuss whether features from earlier layers are more related to general task detection, while features from later layers are more specific to task execution. This would provide a deeper understanding of the hierarchical nature of the model's representation. Finally, the authors need to provide a more detailed explanation of Figure 7, including clear labels for the axes and a description of the colored regions. A textual description of the experiment, including the inputs, outputs, and significance of the results, is also necessary. For example, the authors could explain that the experiment measures the causal effect of task-detection features on task-execution features by ablating the detection features and observing the change in execution feature activations. They could then discuss the implications of the observed causal relationships for understanding the mechanism of in-context learning. For example, a strong causal link between a specific task-detection feature and a corresponding task-execution feature would suggest that the detection of the task directly triggers the execution mechanism. The authors should also discuss the limitations of the current approach and suggest directions for future research. For example, they could discuss the potential impact of using different sparse autoencoder architectures or exploring the dynamics of feature activation across multiple layers.

### Questions

Please address the concerns mentioned in the weaknesses section.

### Rating

3

### Confidence

3

**********
