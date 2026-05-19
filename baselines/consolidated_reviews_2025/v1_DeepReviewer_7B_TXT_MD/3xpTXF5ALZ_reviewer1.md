### Summary

The paper proposes a method for determining the importance of sentences in an email for phishing classification. The method learns a selection network that learns to select important sentences in a differentiable manner. The paper uses a variational information bottleneck approach to encourage the selection network to select only important sentences. The paper uses a cross-entropy loss to train the selection network and the phishing classifier jointly. The paper introduces two new metrics, Label-Accuracy and Cognitive-True-Positive, to evaluate the performance of the proposed method. The paper conducts experiments on seven real-world email datasets and compares the performance of the proposed method with five state-of-the-art interpretable machine learning approaches.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

- The paper addresses the important problem of phishing detection and localization. The proposed method provides a way to identify the most important sentences in an email for phishing classification, which can be useful for understanding and mitigating phishing attacks.
- The paper introduces two new metrics, Label-Accuracy and Cognitive-True-Positive, to evaluate the performance of the proposed method. These metrics are designed to measure the accuracy of the selected sentences and their alignment with cognitive triggers used in phishing emails.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a clear motivation for why the proposed method is needed. The paper states that there is a lack of intrinsic interpretable machine learning techniques for phishing attack localization, but it does not explain why existing methods are insufficient for this task. It would be helpful to provide a more detailed discussion of the limitations of existing approaches and how the proposed method addresses these limitations.
- The paper does not provide a clear explanation of the proposed method. The paper introduces several technical details, such as the variational information bottleneck approach and the cross-entropy loss, but it does not provide a clear explanation of how these components work together. It would be helpful to provide a more detailed description of the proposed method and its underlying assumptions.
- The paper does not provide a clear explanation of the proposed metrics. The paper introduces two new metrics, Label-Accuracy and Cognitive-True-Positive, but it does not provide a clear explanation of what these metrics measure and how they are calculated. It would be helpful to provide a more detailed description of the proposed metrics and their relationship to existing evaluation metrics.
- The paper does not provide a clear comparison of the proposed method with existing approaches. The paper compares the performance of the proposed method with five state-of-the-art interpretable machine learning approaches, but it does not provide a clear explanation of how the proposed method outperforms these approaches. It would be helpful to provide a more detailed comparison of the proposed method with existing approaches and highlight its advantages.

### Suggestions

The paper would benefit from a more thorough explanation of the motivation behind the proposed method. While the authors claim a lack of intrinsic interpretable machine learning techniques for phishing attack localization, they do not sufficiently articulate why existing methods are inadequate. For instance, they could discuss how traditional machine learning models, even with post-hoc interpretability methods, struggle to identify the specific sentences that are most indicative of phishing attempts. This could include a discussion of the limitations of feature importance techniques in capturing the nuanced relationships between sentences and the overall phishing context. Furthermore, the paper should clarify how the proposed method addresses these specific shortcomings, perhaps by demonstrating how the selection network can identify the salient sentences that contribute most to the phishing classification, and how this differs from existing approaches. A concrete example, perhaps using a sample email and showing how the selection network identifies the critical sentences, would significantly enhance the paper's motivation.

To improve the clarity of the proposed method, the authors should provide a more detailed explanation of the technical components, particularly the variational information bottleneck (VIB) approach and the cross-entropy loss. The paper should clearly explain how the VIB is used to encourage the selection network to select only the most important sentences, and how this relates to the overall objective of phishing localization. The authors should also explain the role of the cross-entropy loss in training the selection network and the phishing classifier jointly, and how this joint training contributes to the model's performance. A step-by-step walkthrough of the training process, perhaps with a simplified example, would be beneficial. Additionally, the paper should clarify the specific assumptions made by the proposed method and how these assumptions might affect its performance in different scenarios. For example, how does the method handle emails with different structures or writing styles?

Finally, the paper needs to provide a more detailed explanation of the proposed metrics, Label-Accuracy and Cognitive-True-Positive. The authors should clearly define what each metric measures, how it is calculated, and why it is appropriate for evaluating phishing localization. For Label-Accuracy, the paper should explain how the top-1 selected sentence is determined and how this relates to the overall phishing classification. For Cognitive-True-Positive, the paper should provide a detailed explanation of how the cognitive triggers are identified and how the metric measures the alignment between the selected sentences and these triggers. The paper should also discuss the limitations of these metrics and how they compare to existing evaluation metrics. A comparison with other metrics, such as precision, recall, and F1-score, would help to contextualize the proposed metrics and demonstrate their validity. Furthermore, the paper should provide a more detailed comparison of the proposed method with existing approaches, highlighting the specific advantages of the proposed method in terms of both performance and interpretability.

### Questions

- What is the motivation for the proposed method? What are the limitations of existing approaches that the proposed method addresses?
- How does the proposed method work? Can you provide a more detailed explanation of the technical components and their underlying assumptions?
- How are the proposed metrics calculated? Can you provide a more detailed explanation of the proposed metrics and their relationship to existing evaluation metrics?
- How does the proposed method compare with existing approaches? Can you provide a more detailed comparison of the proposed method with existing approaches and highlight its advantages?

### Rating

3

### Confidence

3

**********
