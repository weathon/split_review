### Summary

The paper proposes a novel approach for phishing attack localization in emails. The authors introduce an innovative deep learning-based method derived from an information-theoretic perspective and information bottleneck theory for solving the phishing attack localization problem. The proposed method works effectively in a weakly supervised setting, providing a practical solution that not only accurately predicts the vulnerability of the email data but also has the capability to automatically identify the most important and phishing-relevant information in each phishing email. The authors also introduce appropriate measures for phishing attack localization and conduct comprehensive experiments on seven real-world diverse email datasets, demonstrating the superiority of their proposed method over the state-of-the-art baselines.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

The paper introduces a novel deep learning-based method for phishing attack localization, which is a significant contribution to the field. The authors provide a comprehensive evaluation of their proposed method on seven real-world diverse email datasets, demonstrating its effectiveness and superiority over state-of-the-art baselines. The paper also introduces appropriate measures for phishing attack localization, which are crucial for evaluating the performance of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

The paper could benefit from a more detailed discussion of the limitations of the proposed method and potential future research directions. Additionally, the paper could provide more insights into the interpretability of the proposed method, which is important for understanding how the model makes predictions.

### Suggestions

The paper would be significantly strengthened by a more thorough discussion of the limitations of the proposed method. For instance, the authors should explore scenarios where the method might fail or underperform, such as when phishing emails employ more sophisticated techniques or when the language used is highly nuanced and context-dependent. A detailed analysis of these failure cases would provide a more realistic assessment of the method's robustness and highlight areas for future improvement. Furthermore, the authors should consider the computational cost associated with their approach, especially when dealing with large-scale email datasets. This would help potential users understand the practical constraints of the method and its scalability. The discussion should also include the sensitivity of the method to hyperparameter settings and how these parameters were chosen. A more rigorous analysis of these aspects would enhance the paper's credibility and practical value.

To improve the interpretability of the proposed method, the authors should delve deeper into the mechanisms that drive the model's predictions. While the paper introduces an information-theoretic perspective, it would be beneficial to provide concrete examples of how the model identifies and prioritizes phishing-relevant sentences. For example, the authors could analyze the selected sentences and compare them to known phishing techniques or linguistic patterns. This would help users understand the model's decision-making process and build trust in its predictions. Furthermore, the authors could explore techniques for visualizing the model's attention mechanisms or feature importance scores to provide a more intuitive understanding of how the model operates. This would not only enhance the paper's scientific contribution but also make the method more accessible to a broader audience.

Finally, the authors should consider expanding the evaluation of their method to include a wider range of phishing attack types. While the current evaluation covers several datasets, it would be valuable to assess the method's performance on more diverse and challenging phishing scenarios. This could include emails that use different attack vectors, such as social engineering or phishing through social media. By evaluating the method on a broader range of attacks, the authors could demonstrate its generalizability and robustness. Additionally, the authors should consider comparing their method to a wider range of baselines, including both traditional and state-of-the-art approaches. This would provide a more comprehensive assessment of the method's performance and highlight its unique advantages.

### Questions

1. How does the proposed method handle emails with multiple phishing attempts or when the phishing attempt is not explicitly labeled?
2. Can the authors provide more insights into the interpretability of the proposed method? How can users understand the model's decision-making process?
3. What are the potential limitations of the proposed method, and how might these be addressed in future work?
4. How does the proposed method perform on different types of phishing attacks, and are there any specific types of attacks that it struggles with?

### Rating

5

### Confidence

4

**********
