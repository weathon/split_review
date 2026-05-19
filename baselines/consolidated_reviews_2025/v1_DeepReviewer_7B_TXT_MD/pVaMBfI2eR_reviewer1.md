### Summary

This paper proposes a novel federated learning method called Federated Dual Prompt Tuning (Fed-DPT) to address the challenges of domain shift and parameter efficiency. Fed-DPT uses a pre-trained vision-language model and applies both visual and textual prompts to facilitate domain adaptation over decentralized data. The method is evaluated on the DomainNet dataset and shows significant improvements over existing methods.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is novel and effective in addressing the challenges of domain shift and parameter efficiency in federated learning.
3. The experimental results show significant improvements over existing methods on the DomainNet dataset.

### Weaknesses

#### Some Related Works


#### comment

1. The paper only evaluates the proposed method on the DomainNet dataset. It would be beneficial to evaluate the method on other datasets to demonstrate its generalizability.
2. The paper does not provide a detailed analysis of the computational cost and communication overhead of the proposed method. It would be beneficial to provide a more detailed analysis of the computational cost and communication overhead of the proposed method, especially in comparison to existing methods.
3. The paper does not discuss the limitations of the proposed method. It would be beneficial to discuss the limitations of the proposed method and potential directions for future research.

### Suggestions

The paper would benefit from a more thorough evaluation of the proposed method. While the DomainNet dataset is a good starting point, it is crucial to assess the method's performance on other datasets with different characteristics. For example, datasets with varying degrees of domain shift, different types of data (e.g., images, text), or different numbers of clients would provide a more comprehensive understanding of the method's strengths and weaknesses. Specifically, the authors should consider datasets such as PACS, OfficeHome, or even multi-domain datasets like VLCS, which are commonly used in domain adaptation research. This would help to demonstrate the robustness and generalizability of the proposed approach. Furthermore, it would be beneficial to analyze the performance of the method under different levels of data heterogeneity across clients, as this is a common challenge in federated learning.

In addition to the empirical evaluation, a more detailed analysis of the computational cost and communication overhead is needed. The paper should provide a breakdown of the computational cost associated with each step of the proposed method, including the prompt tuning process and the federated learning aggregation. This analysis should compare the computational cost of the proposed method with existing federated learning algorithms. Furthermore, the paper should quantify the communication overhead, including the size of the model updates and the number of communication rounds required for convergence. This analysis should also consider the impact of the number of clients and the size of the dataset on the communication overhead. It would be beneficial to provide a comparison of the communication cost with other federated learning algorithms, especially those that are designed for large-scale datasets. This would help to understand the practical implications of the proposed method in real-world scenarios.

Finally, the paper should include a more thorough discussion of the limitations of the proposed method and potential directions for future research. The authors should acknowledge any assumptions made by the method and discuss the potential impact of these assumptions on the results. For example, the paper should discuss the limitations of using a pre-trained vision-language model and how this might affect the performance of the method. The authors should also discuss the limitations of the prompt tuning approach and potential alternatives. Furthermore, the paper should discuss the limitations of the federated learning setting and potential extensions to other federated learning scenarios. This discussion should also include the potential impact of the proposed method on the privacy of the data. By addressing these limitations and discussing potential future research directions, the paper would provide a more complete and balanced view of the proposed method.

### Questions

1. How does the proposed method perform on other datasets with different characteristics?
2. What is the computational cost and communication overhead of the proposed method compared to existing methods?
3. What are the limitations of the proposed method, and what are the potential directions for future research?

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
