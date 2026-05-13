# Domain Indexing Collaborative Filtering for Recommender System

- Decision: Reject
- Scores: 6, 3, 5, 5

## Abstract
In cross-domain recommendation systems, addressing cold-start items remains a significant challenge. Previous methods typically focus on maximizing performance using cross-domain knowledge, often treating the knowledge transfer process as a black box. However, the recent development of domain indexing introduces a new approach to better address such challenges. We have developed an adversarial Bayesian framework, Domain Indexing Collaborative Filtering (DICF), that infers domain indices during cross-domain recommendation. This framework not only significantly improves the recommendation performance but also provides interpretability for cross-domain knowledge transfer. This is verified by our empirical results on both synthetic and real-world datasets.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces Domain Indexing Collaborative Filtering (DICF), an adversarial Bayesian framework designed to address the cold-start problem in cross-domain recommendation systems. 

DICF infers domain-specific indices that capture domain relationships and enhance the interpretability of cross-domain knowledge transfer. The approach is validated on synthetic (Rec-15 and Rec-30) and real-world (XMRec) datasets, demonstrating superior performance over methods like Domain Adversarial Neural Networks (DANN) and Taxonomy-Structured Domain Adaptation (TSDA). The model is good at producing recommendations with domain-specific and generalizable features.

### Strengths
The paper uses a domain indexing approach with the adversarial Bayesian. This idea is innovative and enhances the interpretability of "black-box" recommendation system.

The paper addresses the cold-start issue by isolating domain-specific and domain-generalizable features, leading to better recommendations in data-poor domains. This isolation process is efficient and meaningful.

### Weaknesses
DICF(introduced by this paper) relies on data's meaningful domain relationships for effective knowledge transfer. This dependence may limit its generalization potential in scenarios with unrelated or highly diverse domains, where domain indices may not capture relevant transfer patterns. Specifically, if the domains are semantically distant or if the feature spaces have minimal overlap, the learned domain indices might not facilitate effective knowledge sharing, potentially leading to negative transfer. For example, transferring knowledge between a movie recommendation domain and a medical diagnosis domain might be ineffective due to the lack of shared underlying patterns.

The model is not explicitly designed to handle evolving domains, where domain characteristics and user preferences can change over time. This limits its utility in fast-evolving industries where product turnover and user preferences shift frequently, potentially requiring regular model retraining. The current framework assumes static domain characteristics, which may not hold in real-world scenarios where user preferences and item features evolve. For instance, in fashion e-commerce, trends change rapidly, and a model trained on past data might not perform well on new trends without adaptation.

### Questions
Can you provide more details on the experimental setup, specifically regarding the tuning of baseline models like PMF, CDL, and DANN? Were these baselines optimized with the same rigor as DICF?

The framework assumes that domain indices remain independent of domain-invariant features. How robust is this assumption in practice, especially when there are overlapping characteristics between domains?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper addresses the cold-start challenge in cross-domain recommendation systems by introducing a novel framework, Domain Indexing Collaborative Filtering (DICF). DICF is an adversarial Bayesian approach that infers domain indices during recommendation, enhancing both performance and interpretability in cross-domain knowledge transfer.

### Strengths
1.	This paper presents a new adversarial Bayesian approach, DICF, which infers domain indices for cross-domain recommendation.
2.	Experimental results on both synthetic and real-world datasets demonstrate the effectiveness of DICF.
3.	The research topic, cross-domain recommendation, is promising and highly relevant to practical applications.

### Weaknesses
1.	The novelty of this paper is limited. The framework appears to be a combination of commonly used techniques, and the reasoning behind the selection of these techniques—such as the use of the Evidence Lower Bound—lacks clarity. Specifically, the paper does not adequately justify why a variational approach with an Evidence Lower Bound (ELBO) is necessary over simpler alternatives for domain index inference. The use of adversarial training, while common, is not motivated by a specific need or problem within the context of domain indexing, making its inclusion seem somewhat arbitrary.
2.	The experiments are limited in scope, as they include a small number of datasets, raising concerns about the generalizability of the proposed method. The datasets used are not sufficiently diverse to demonstrate the robustness of the method across different types of data and domain characteristics. Additionally, the baselines used are insufficient to verify the method’s state-of-the-art performance. The choice of baselines does not include recent, competitive methods in cross-domain recommendation, which makes it difficult to assess the true contribution of the proposed approach.
3.	Figure 3 is difficult to interpret, and it would be beneficial to consider an alternative visualization method to better convey the item context features of Rec-15. The current visualization does not effectively illustrate the relationship between item features and domain indices, making it hard to understand the impact of the domain indexing mechanism.

### Questions
Overall, the proposed method feels formulaic and lacks a unique innovative aspect. Additionally, the experiments do not include sufficient datasets or baseline methods to fully establish the advancement of the method.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper focuses on cold-start problem in cross-domain scenarios. Two terms are intensively emphasized: domain index and spurious features (domain-specific and cannot generalize across domains). The former aggregates from spurious features and captures relationships among domains. The method is based on two properties of  spurious features. A probabilistic graphical model is used, incorporating domain-specific and invariant features into the recommendation process. The authors conducted experiments on two synthetic datasets and a real-world dataset. It enhances recommendation quality across domains by introducing interpretable domain indices.

### Strengths
1. The method DICF combines Bayesian modeling and adversarial learning, allowing fine-grained feature separation. This ensures that only domain-invariant features contribute to the recommendation, reducing noise and improving prediction accuracy.
2. The probabilistic graphical model and ELBO-based training enhance DICF's ability to capture complex dependencies among features and improve model generalization across different domains.

### Weaknesses
1. The introduction is too simple and not clear. Giving a toy example would be better to illustrate the problem of this paper.
2. This paper does not point out the challenges of problem or motivation of its method.
3. Results from two synthetic datasets are not convincing because they are generated from the assumption your model has. When synthetic data is generated with assumptions aligned to the model, it can indeed inflate performance results.
4. I think there is a mistake in Figure 2. It should be $p(\beta|\gamma)$ instead of $p(\gamma|\beta)$, right? The input should be $\gamma$ if my understanding is right.

### Questions
1. I think there is a mistake in Figure 2. It should be $p(\beta|\gamma)$ instead of $p(\gamma|\beta)$, right? The input should be $\gamma$ if my understanding is right.

2. Results from two synthetic datasets are not convincing because they are generated from the assumption your model has. When synthetic data is generated with assumptions aligned to the model, it can indeed inflate performance results.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper focuses on cross-domain recommendation and proposes an adversarial Bayesian framework called Domain Indexing Collaborative Filtering (DICF). Extensive theoretical analysis and experiments on three datasets demonstrate the effectiveness of the approach. Furthermore, visualizing domain indices intuitively illustrates its effectiveness by showing the correlation between the domain indices and the geographical/continental information of the countries.

### Strengths
S1: The writing and structure of this paper is clear.

S2: The approach is innovative, employing an adversarial Bayesian method for cross-domain recommendation—a technique that has not been previously explored.

### Weaknesses
W1: As for the chosen baselines, since this paper focuses on cross-domain recommendation, but no baselines specific to this area were selected, instead, only baselines related to domain adaptation are used. More appropriate baselines in cross-domain recommendation are needed.

W2: Regarding the datasets, since numerous public cross-domain recommendation datasets are available, why the authors choose to use a synthetic dataset, which is relatively small. Compared to established datasets like Amazon, Rec-15, and Rec-30, which contain only 750 and 1,500 users and items, this smaller dataset is less convincing.

W3: Furthermore, the related work section should be expanded, particularly concerning cross-domain recommendation. The paper only includes studies prior to 2022, and more recent research outputs should be incorporated.

Overall, although the framework is theoretically solid, technically, it heavily relies on prior work, specifically VDI [1], which gives the impression of being incremental. Furthermore, issues remain with the selection of baselines and datasets.

### Questions
See Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2
