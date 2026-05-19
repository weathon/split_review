### Summary

This paper studies the problem of structure learning in DAG models. The authors show that the scale of the data can lead to incorrect graph structure recovery for various loss functions. They also propose a new loss function that is robust to scale changes. Experiments on simulated data are provided to demonstrate the effectiveness of the proposed method.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.

2. The theoretical results are sound and interesting.

3. The experiments are comprehensive and convincing.

### Weaknesses

#### Some Related Works


#### comment

1. The authors should provide more details on the real-world data experiment. Specifically, it is unclear how the 'ground truth' graph is obtained for the real-world dataset. The description of the experimental setup lacks sufficient detail to allow for reproducibility. For instance, the specific method used to generate the scale-affected variable is not clearly explained, making it difficult to understand the precise nature of the manipulation and its impact on the results.

2. The proposed method is limited to discrete structure learners. This significantly restricts the applicability of the method, as many real-world problems involve continuous variables and are better modeled using continuous structure learners. The paper does not adequately address the challenges of extending the proposed approach to continuous domains, which is a major limitation.

3. The paper does not discuss the relationship between the proposed method and existing approaches for structure learning. A more thorough comparison with existing methods, including both discrete and continuous structure learners, is needed to properly contextualize the contribution of this work. The lack of such a discussion makes it difficult to assess the novelty and significance of the proposed method.

### Suggestions

The authors should significantly expand the description of the real-world data experiment. This should include a detailed explanation of how the 'ground truth' graph is obtained, or if it is not known, how the expected graph structure is determined. The method used to generate the scale-affected variable needs to be described with sufficient detail, including the specific parameters used and the rationale behind the chosen approach. For example, if a specific variable is scaled by a constant factor, the value of that factor and the reason for choosing that particular variable should be clearly stated. Furthermore, the authors should provide more details on the data preprocessing steps, such as normalization or standardization, that were applied before structure learning. This would allow for a better understanding of the experimental setup and improve the reproducibility of the results. The authors should also consider including a sensitivity analysis to assess the impact of different scaling factors on the performance of the proposed method.

The limitation of the proposed method to discrete structure learners is a significant drawback that needs to be addressed. The authors should discuss the challenges of extending the method to continuous domains and propose potential solutions. This could involve exploring alternative loss functions or developing new techniques for handling continuous variables. For example, the authors could investigate the use of kernel methods or other non-parametric approaches to model continuous relationships. Additionally, the authors should discuss the computational complexity of the proposed method and compare it to existing approaches. This would provide a better understanding of the trade-offs between accuracy and efficiency. The authors should also consider providing a theoretical analysis of the convergence properties of the proposed method, which would further strengthen the contribution of the paper.

The paper would benefit from a more thorough discussion of the relationship between the proposed method and existing approaches for structure learning. The authors should provide a detailed comparison with both discrete and continuous structure learners, highlighting the advantages and disadvantages of each approach. This should include a discussion of the assumptions made by each method and the types of problems for which they are best suited. For example, the authors could compare their method to score-based methods that use different loss functions, such as the Bayesian Information Criterion (BIC) or the Akaike Information Criterion (AIC). Furthermore, the authors should discuss the limitations of their method and identify areas for future research. This would help to contextualize the contribution of the paper and provide a roadmap for future work in this area.

### Questions

1. In the real-world data experiment, how is the ground truth obtained? 

2. Is it possible to extend the proposed method to continuous structure learners?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
