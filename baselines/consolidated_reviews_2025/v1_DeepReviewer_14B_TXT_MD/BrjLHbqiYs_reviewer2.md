### Summary

This paper studies the problem of estimating the amount of synergistic interactions in a semi-supervised setting where labeled unimodal data and unlabeled multimodal data are available. The authors derive lower and upper bounds on the amount of multimodal interactions in this semi-supervised setting. The lower bounds are based on the shared information between modalities and the disagreement between separately trained unimodal classifiers, and the upper bound is derived through connections to approximate algorithms for min-entropy couplings. The authors validate these estimated bounds and show how they accurately track true interactions. Finally, the authors show how these theoretical results can be used to estimate multimodal model performance, guide data collection, and select appropriate multimodal models for various tasks.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well-written and easy to follow. 
- The paper provides a thorough theoretical analysis of the problem of estimating multimodal interactions in a semi-supervised setting. The authors derive lower and upper bounds on the amount of multimodal interactions and provide a clear explanation of the assumptions and limitations of their approach. 
- The paper validates the estimated bounds through experiments on both synthetic and real-world datasets. The authors show how these theoretical results can be used to estimate multimodal model performance, guide data collection, and select appropriate multimodal models for various tasks.

### Weaknesses

#### Some Related Works


#### comment

 - The paper assumes finite sample spaces for features and labels, which may limit its applicability to real-world datasets that are often continuous and/or high-dimensional. 
- The paper does not provide a detailed analysis of the computational complexity of the proposed approach. 
- The paper does not provide a comparison of the proposed approach with existing methods for estimating multimodal interactions in a semi-supervised setting.

### Suggestions

The paper's assumption of finite sample spaces, while simplifying the theoretical analysis, raises concerns about its practical applicability. Many real-world datasets, particularly in domains like image and speech processing, involve continuous and high-dimensional data. The authors should discuss the implications of this assumption more thoroughly, perhaps by exploring how their bounds behave under different discretization schemes or by providing theoretical justification for why their approach is still valid under certain types of continuous distributions. For example, they could investigate the impact of quantization error on the accuracy of their bounds when applied to discretized continuous data. Furthermore, it would be beneficial to see experiments on datasets with varying degrees of dimensionality and continuity to better understand the limitations of the proposed approach.

Regarding computational complexity, the paper lacks a detailed analysis of the time and space requirements of the proposed algorithms. While the authors mention that the bounds can be computed efficiently, they do not provide a formal analysis of how the computational cost scales with the size of the input data and the number of modalities. This is a crucial aspect for practical applications, especially when dealing with large-scale datasets. A more rigorous analysis should include a breakdown of the computational cost of each step in the algorithm, such as the estimation of mutual information and the optimization procedures involved in calculating the bounds. It would also be helpful to compare the computational complexity of the proposed approach with existing methods for estimating multimodal interactions, if any exist, to provide a better understanding of its efficiency.

Finally, the absence of a comparison with existing methods for estimating multimodal interactions in a semi-supervised setting is a significant weakness. While the authors claim that their work is the first to address this specific problem, it is important to contextualize their approach within the broader landscape of multimodal learning. Even if no directly comparable methods exist, the authors should discuss how their approach relates to existing techniques for multimodal representation learning, information bottleneck methods, or other related approaches. This would help the reader understand the novelty and significance of their work and identify potential areas for future research. A thorough comparison, even if qualitative, would greatly enhance the paper's contribution.

### Questions

- How does the proposed approach handle continuous and high-dimensional data? 
- What are the computational requirements for calculating the bounds, and how do they scale with the size of the dataset and the dimensionality of the modalities? 
- How does the proposed approach compare with existing methods for estimating multimodal interactions in a semi-supervised setting?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
