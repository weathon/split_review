### Summary

The paper proposes a novel deep learning-based approach for phishing attack localization in emails. The method is based on an information-theoretic perspective and information bottleneck theory. The authors introduce appropriate measures for phishing attack localization and conduct comprehensive experiments on seven real-world diverse email datasets. The results demonstrate the effectiveness and superiority of the proposed method over the state-of-the-art baselines.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel deep learning-based approach for phishing attack localization, which is a significant contribution to the field.
2. The authors provide a comprehensive evaluation of their proposed method on seven real-world diverse email datasets, demonstrating its effectiveness and superiority over state-of-the-art baselines.
3. The paper introduces appropriate measures for phishing attack localization, which are crucial for evaluating the performance of the proposed method.
4. The paper is well-written and easy to follow.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could benefit from a more detailed discussion of the limitations of the proposed method and potential future research directions. Specifically, the paper lacks a discussion on the computational cost associated with the proposed deep learning model, which is a critical factor for practical deployment. Furthermore, the sensitivity of the method to different email formats and content variations should be explored.
2. The paper could provide more insights into the interpretability of the proposed method, which is important for understanding how the model makes predictions. The paper does not discuss how the model's decision-making process can be understood, which is crucial for building trust and identifying potential biases in the model.
3. The paper could benefit from a more thorough comparison with existing methods, including a discussion of the advantages and disadvantages of the proposed method compared to other approaches. The comparison should not only focus on performance metrics but also on other aspects such as computational complexity, interpretability, and robustness.

### Suggestions

The paper should include a more detailed analysis of the computational cost associated with the proposed method. This analysis should consider the time and memory requirements for training and inference, and should also discuss the scalability of the method to larger datasets. Furthermore, the authors should explore the sensitivity of the method to different email formats and content variations. This could involve testing the method on a variety of email datasets with different characteristics, such as different email providers, different email content, and different email formats. The authors should also investigate the robustness of the method to adversarial attacks, which could be a potential vulnerability in phishing detection systems. This would provide a more comprehensive understanding of the method's limitations and its applicability in real-world scenarios.

To enhance the interpretability of the proposed method, the authors should explore techniques for visualizing the model's decision-making process. This could involve techniques such as attention maps or feature importance analysis, which could help to identify the most relevant features that the model uses to make predictions. The authors should also discuss how the model's predictions can be explained in a human-understandable way, which is crucial for building trust and identifying potential biases in the model. For example, the authors could provide examples of how the model identifies phishing-related sentences and how these sentences are used to make the final prediction. This would help to improve the transparency and accountability of the model.

The paper should include a more thorough comparison with existing methods, including a discussion of the advantages and disadvantages of the proposed method compared to other approaches. This comparison should not only focus on performance metrics but also on other aspects such as computational complexity, interpretability, and robustness. The authors should also discuss the limitations of the proposed method and suggest potential directions for future research. This would provide a more comprehensive understanding of the method's strengths and weaknesses and its potential for future development. The comparison should include a discussion of the specific scenarios where the proposed method is expected to perform better or worse than existing methods.

### Questions

1. How does the proposed method handle emails with multiple phishing attempts or when the phishing attempt is not explicitly labeled?
2. Can the authors provide more insights into the interpretability of the proposed method? How can users understand the model's decision-making process?
3. What are the potential limitations of the proposed method, and how might these be addressed in future work?
4. How does the proposed method perform on different types of phishing attacks, and are there any specific types of attacks that it struggles with?

### Rating

6

### Confidence

3

**********
