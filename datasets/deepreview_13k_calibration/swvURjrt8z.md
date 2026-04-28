# TabDiff: a Multi-Modal Diffusion Model for Tabular Data Generation

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6, 6

## Abstract
Synthesizing high-quality tabular data is an important topic in many data science tasks, ranging from dataset augmentation to privacy protection. However, developing expressive generative models for tabular data is challenging due to its inherent heterogeneous data types, complex inter-correlations, and intricate column-wise distributions. In this paper, we introduce \method, a joint diffusion framework that models all multi-modal distributions of tabular data in one model. Our key innovation is the development of a joint continuous-time diffusion process for numerical and categorical data, where we propose feature-wise learnable diffusion processes to counter the high disparity of different feature distributions. \method is parameterized by a transformer handling different input types, and the entire framework can be efficiently optimized in an end-to-end fashion. We further introduce a multi-modal stochastic sampler to automatically correct the accumulated decoding error during sampling, and propose classifier-free guidance for conditional missing column value imputation. Comprehensive experiments on seven datasets demonstrate that \method achieves superior average performance over existing competitive baselines across all eight metrics, with up to $22.5\%$ improvement over the state-of-the-art model on pair-wise column correlation estimations.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
While extensive work has attempted to solve the task of tabular data generation, they often face different problems, such as the failure of cross-modal modeling and the additional cost of training auto-encoders. To this end, this paper proposes TabDiff, a diffusion-based model that unifies modal heterogeneity within one single approach. The proposed method, built upon several existing techniques, models numerical and categorical attributes separately and introduces a learnable noise scheduler that further facilitates the sampling process. Extensive experiments verify the effectiveness of TabDiff. Ablation studies also provide additional insights.

### Strengths
1. The paper is well-written and well-structured. It is self-content and easy to follow.
2. The problem investigated in this paper is well-motivated and practical.
3. While most of the techniques have been investigated in prior work, this work seamlessly integrates them and adapts to the tabular data generation task.
4. Extensive experiments sufficiently verify the effectiveness of the proposed approach, and ablation studies further outline the design choices and the benefits of the learnable noise schedulers.

### Weaknesses
1. Despite the claim of cross-modal modeling, the proposed method currently still models numerical and categorical values separately, which might make it difficult to synthesize more complicated tabular datasets. Specifically, while the diffusion process is applied jointly, the underlying noise models and denoising networks are distinct for each data type. This separation could limit the model's ability to capture complex, non-linear interactions between numerical and categorical features, which are often present in real-world tabular data. For example, a strong correlation might exist between a categorical feature like 'region' and a numerical feature like 'average income,' and this type of interaction might not be fully captured by separate modeling.
2. While I generally appreciate the effort and the performance, I am not fully convinced by the claim of the multi-modal diffusion framework. The experiments in Tables 1, 2, and 3 all suggest comparable performance compared to TabSyn. As TabSyn has been published in ICLR 2024, the authors should clearly state the main difference and closely compare the two works. The lack of a clear advantage over TabSyn in the main experiments raises questions about the practical significance of the proposed approach. The authors should provide a more rigorous comparison, potentially including additional metrics or datasets that highlight the strengths of their method.
3. Lack of motivation for schedulers. What is the motivation for choosing power-mean and log-linear schedulers? The choice looks random to me. The paper does not provide a clear justification for why these specific schedulers were chosen over other possible options. A more thorough analysis of the impact of different schedulers on the performance of the model is needed, along with a theoretical or empirical motivation for the chosen schedulers.

### Questions
1. Do numerical and categorical value modeling help each other, or are they just modeled separately?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work proposed a multi-modal diffusion framework for generating high-quality synthetic data. A key innovation is the development of a joint continuous-time diffusion process for numerical and categorical data, where authors propose learnable column-wise noise schedules to counter the high disparity of different feature distributions. Extensive experiments are conducted to demonstrate the superior capacity of proposed approach.

### Strengths
This manuscript demonstrates advantages in multiple aspects. It provides a clear and comprehensive introduction of the research problem, and conducts extensive experiments on multiple data sets and evaluation criteria.

Additionally, the paper elaborates on relevant algorithms and techniques. The algorithmic sections present some innovative and original findings, contributing to advancements in the field of machine learning and offering new insights to the academic community.

### Weaknesses
1. Some necessary explanations are lacking in the description of algorithm provided in the Method and Appendix, requiring more detailed descriptions to enhance the readability of the paper.

2. The description of categorical column needs an example to illustrate the method more clearly.

3. Formula (10) is missing a parenthesis.

4. Why are formula (10) and formula (11) constructed this way? Is there a source? If not, can you explain the construction idea?

### Questions
See weakness.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces an approach called TABDIFF, which develops a joint continuous-time diffusion process for mixed-type data in tabular datasets. The authors address the challenge of high disparity between different feature distributions by proposing feature-wise learnable diffusion processes. The key contribution is a hybrid diffusion process to handle numerical and categorical features.

### Strengths
**1** The experiments are extensive, demonstrating the efficiency of the proposed method.

**2** Hybrid diffusion models are employed to handle mixed-type data in tabular datasets.

### Weaknesses
 **1** The authors claim that they explicitly tackle the feature-wise heterogeneity issue in the multi-modal diffusion process. However, the details about how to handle this problem is missing. Specifically, it is unclear how the proposed method dynamically adjusts the diffusion process based on the varying complexity of different feature distributions. The paper lacks a clear explanation of the mechanism that allows the model to allocate its capacity effectively across heterogeneous features. For example, it does not explain how the model learns to prioritize features with more complex marginal distributions during the training process.

**2** Even though experiments show the efficiency of the proposed method, it lacks of the motivation of considering a masked diffusion for categorical features. The paper does not provide a clear rationale for why a masked diffusion approach is superior to other discrete diffusion frameworks for categorical data in the context of tabular data generation. It is not clear why the loss is only evaluated on masked columns and how this contributes to better performance. The paper should also discuss the potential limitations of using masked diffusion for categorical features, such as the possibility of losing information due to masking.

### Questions
**Q1** The title of this paper is somewhat confusing. Before reading it, I assumed it referred to a diffusion model capable of generating various types of data structures, such as tabular data and images. After reading, I believe the term "modality" may refer to either of two scenarios: (1) multiple modalities within a specific variable (a column in a tabular dataset); (2) columns of a tabular dataset that are mixed-type. If the latter is the intended meaning, the paper should demonstrate how the proposed method differs from TabDDPM, as TabDDPM also handles mixed-type data generation in tabular datasets. It is inappropriate to use such an ambitious title.


**Q2** The proposed method utilizes the masked diffusion for categorical features. What is the point of using masked diffusion?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces TabDiff, an innovative multi-modal diffusion model designed to generate high-quality synthetic tabular data. It addresses the challenges of heterogeneous tabular data, which includes both numerical and categorical features with complex interdependencies. TabDiff employs a joint continuous-time diffusion process with feature-wise learnable components, allowing it to handle different data modalities while adapting to the varying distributions of individual features.

### Strengths
1. Tabdiff introduces a unified joint continuous-time diffusion process with feature-wise learnable components for handling both numerical and categorical data is innovative and allows the model to adapt to the specific characteristics of different data distributions.
2. The paper provides a thorough evaluation of TabDiff on a wide range of metrics, offering a deep and detailed assessment of the model performance from multiple dimensions, which is highly commendable.
3. The paper emphasizes the importance of TabDiff in generating high-quality synthetic data that enables effective model training while ensuring privacy preservation. The authors validate this effectiveness through the use of various metrics, demonstrating that the model not only maintains data fidelity but also safeguards against privacy risks. It's a practical trial for addressing the growing need for privacy-conscious data generation in sensitive domains.

### Weaknesses
1. Although the paper does not explicitly highlight it, the complexity of TabDiff, particularly in handling high-dimensional features through diffusion, could result in increased computational costs compared to simpler models. It would be good to provide a comparison of generation or training speed metrics with other baselines to better illustrate this trade-off.

2. The performance drop of TabDDPM on the News and Diabetes datasets is surprising, especially given that other diffusion-based methods maintain stable results. This discrepancy is beyond expected boundaries, with precision and recall even dropping to 0 in Table 7 and Table 8, and similarly poor performance across other tables for these datasets. 
Thus, while I appreciate the authors' comprehensive comparison across various metrics with baselines, the paper lacks sufficient analysis and discussion of the experimental results, particularly in explaining the performance gaps between TabDiff and the baselines. It would strengthen the paper if the authors provided more detailed discussion, and offered insights into the experimental setup of the baselines.

3. The paper lacks sufficient explanation of the experimental setup for these baselines, which makes it harder to interpret the results. Providing more clarity on these aspects would strengthen the case for TabDiff's performance and offer a more comprehensive understanding of the comparative results.

### Questions
See weaknesses, I will raise the score if all the concerns are addressed.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces TABDIFF, a joint diffusion framework which aims to handle data with both discrete and continuous data types. The authors validated the effectiveness of this framework through comprehensive experiments.

### Strengths
1.The method introduces a new approach by jointly learning the diffusion processes for discrete and continuous features, which is not explored in the previous work.

2. The adaptively learnable noise schedules look novel.

3.The paper provides extensive experimental evaluations across different benchmark datasets, thoroughly validating the method’s performance.

### Weaknesses
In the title of this paper, it is claimed that this paper addresses multi-modal distributions. However, the paper does not clearly specify what multi-modal distribution it handles. Does it only refer to distributions with both discrete and continuous variables?

### Questions
NA

### Soundness
3

### Presentation
3

### Contribution
3
