### Summary

The paper proposes a novel method for phishing attack localization that identifies the most important sentences in an email to determine if it is a phishing attempt. The proposed method is based on an information-theoretic perspective and information bottleneck theory. The method is evaluated on seven real-world email datasets and compared with five state-of-the-art interpretable machine learning approaches. The results show that the proposed method outperforms the baselines in terms of accuracy and cognitive-true-positive metrics.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The paper addresses an important and timely problem of phishing attack localization in emails, which is crucial for email security.
2. The proposed method is based on a novel information-theoretic perspective and information bottleneck theory, which is a unique approach to phishing attack localization.
3. The paper provides a comprehensive evaluation of the proposed method on seven real-world email datasets, which demonstrates the effectiveness of the method.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a clear motivation for the proposed method. The authors should explain why the proposed method is needed and how it addresses the limitations of existing methods.
2. The paper does not provide a clear explanation of the proposed method. The authors should provide a more detailed description of the proposed method and its underlying assumptions.
3. The paper does not provide a clear explanation of the proposed metrics. The authors should provide a more detailed description of the proposed metrics and their relationship to existing evaluation metrics.
4. The paper does not provide a clear comparison of the proposed method with existing approaches. The authors should provide a more detailed comparison of the proposed method with existing approaches and highlight its advantages.

### Suggestions

The paper needs to clearly articulate the specific limitations of existing phishing detection methods that the proposed approach aims to overcome. For instance, if current methods struggle with nuanced language or require extensive labeled data, the authors should explicitly state this and explain how their information-theoretic approach provides a more robust solution. Furthermore, the paper should delve deeper into the theoretical underpinnings of the proposed method. A more detailed explanation of how the information bottleneck principle is applied in this context is needed. This should include a discussion of the specific information channels being considered and how the method minimizes the mutual information between the input email and irrelevant information while preserving the relevant information for phishing detection. The authors should also provide a more detailed explanation of the selection network, including the specific architecture and the rationale behind its design. This would help the reader understand how the network is able to identify the most important sentences for phishing classification.

The paper should also provide a more thorough explanation of the proposed evaluation metrics. It is not sufficient to simply introduce Label-Accuracy and Cognitive-True-Positive metrics; the authors need to justify why these metrics are appropriate for evaluating phishing localization and how they relate to other commonly used metrics in the field. For example, how do these metrics capture the nuances of phishing emails compared to traditional accuracy or precision metrics? The authors should also provide a detailed explanation of how the cognitive triggers are identified and how the Cognitive-True-Positive metric is calculated. This should include a discussion of the potential biases in the selection of cognitive triggers and how these biases might affect the evaluation results. Furthermore, the paper should include a more detailed comparison of the proposed method with existing approaches. This comparison should not only focus on the performance metrics but also on the interpretability and explainability of the methods. The authors should clearly highlight the advantages of their approach in terms of both accuracy and interpretability compared to existing methods.

Finally, the paper should include a more comprehensive discussion of the limitations of the proposed method. This should include a discussion of the potential biases in the training data, the computational complexity of the method, and the generalizability of the method to different types of phishing emails. The authors should also discuss potential future research directions that could address these limitations. For example, how could the method be extended to handle more complex email structures or to incorporate other types of information, such as user behavior or network traffic? Addressing these limitations would significantly strengthen the paper and provide a more balanced and realistic assessment of the proposed method.

### Questions

1. What is the motivation for the proposed method? What are the limitations of existing approaches that the proposed method addresses?
2. How does the proposed method work? Can you provide a more detailed explanation of the technical components and their underlying assumptions?
3. How are the proposed metrics calculated? Can you provide a more detailed explanation of the proposed metrics and their relationship to existing evaluation metrics?
4. How does the proposed method compare with existing approaches? Can you provide a more detailed comparison of the proposed method with existing approaches and highlight its advantages?

### Rating

3

### Confidence

3

**********
