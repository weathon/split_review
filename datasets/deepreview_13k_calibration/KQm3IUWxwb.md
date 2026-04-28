# Disentangled Heterogeneous Collaborative Filtering

- Decision: Reject
- Avg Score: 4.67
- Scores: 6, 3, 5

## Abstract
Modern recommender systems often utilize low-dimensional latent representations to embed users and items based on their observed interactions. However, many existing recommendation models are primarily designed for coarse-grained and homogeneous interactions, which limits their effectiveness in two key dimensions: i) They fail to exploit the relational dependencies across different types of user behaviors, such as page views, add-to-favorites, and purchases. ii) They struggle to encode the fine-grained latent factors that drive user interaction patterns. In this study, we introduce DHCF, an efficient and effective contrastive learning recommendation model that effectively disentangles users' multi-behavior interaction patterns and the latent intent factors behind each behavior. Our model achieves this through the integration of intent disentanglement and multi-behavior modeling using a parameterized heterogeneous hypergraph architecture. Additionally, we propose a novel contrastive learning paradigm that adaptively explores the benefits of multi-behavior contrastive self-supervised augmentation, thereby improving the model's robustness against data sparsity. Through extensive experiments conducted on three public datasets, we demonstrate the effectiveness of DHCF, which significantly outperforms various strong baselines with competitive efficiency.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a Disentangled Heterogeneous Collaborative Filtering (DHCF) for a recommendation system. Specifically, the model integrates a parameterized heterogeneous hypergraph network with a hierarchical contrastive learning paradigm, to capture the latent intent factors and the multi-behavior dependencies in an adaptive and self-supervised manner.

### Strengths
1. The task of recommendation with heterogeneous interactions is interesting and valuable. 
2. The paper is written well and is easy to understand.
3. Extensive experiments have been conducted to validate the proposed model.

### Weaknesses
1. The methods proposed in the paper lack innovation significantly. Sections 3.1-3.5 follow very common design paradigms, and their method designs exhibit a certain degree of similarity to HCCF, ICL, and others. The paper should discuss the differences in the technical details between them. Specifically, the hypergraph construction and the message-passing mechanism, while effective, are not novel and appear to be a straightforward adaptation of existing techniques. The disentanglement module, although presented as a core contribution, lacks a clear explanation of how it differs fundamentally from existing disentanglement methods used in collaborative filtering. A more rigorous comparison detailing the specific architectural differences and the impact of these differences on the performance is needed.
2.  In section 3.6, there are two loss functions proposed for relationship learning but in reality, they belong to the same paradigm. The paper lacks sufficient theoretical justification for their validity. Both losses, while framed differently, are fundamentally contrastive losses operating on different levels of granularity (node and graph). The paper should provide a formal analysis demonstrating that these two losses are not redundant and that they contribute to learning distinct aspects of the user-item interaction graph. The lack of theoretical justification for the specific design choices in these loss functions is a major concern.
3.  The font size in Figure 1 is too small.

### Questions
My major concern lies in the technical details. Many of the described methods bear a resemblance to existing approaches. It is crucial to clearly explain the distinctions and improvements made by DHCF in comparison to these existing methods. Additionally, please provide a more detailed explanation of the motivations behind these improvements.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper addresses the problem of modern recommender systems that often utilize low-dimensional latent representations to embed users and items based on their observed interactions. However, many existing recommendation models are primarily designed for coarse-grained and homogeneous interactions, which limits their effectiveness in two key dimensions: i) They fail to exploit the relational dependencies across different types of user behaviors, such as page views, add-to-favorites, and purchases; and ii) They fail to disentangle the latent intent factors behind each behavior, which leads to suboptimal recommendations.

The authors argue that these limitations can be addressed by a novel recommendation model called Disentangled Heterogeneous Collaborative Filtering (DHCF). DHCF effectively disentangles users' multi-behavior interaction patterns and the latent intent factors behind each behavior. The authors propose a parameterized heterogeneous hypergraph architecture that captures the complex and diverse interactions among users, items, and behaviors. They also introduce a novel contrastive learning paradigm that improves the model's robustness against data sparsity.

### Strengths
1. The authors' approach is based on a hypergraph structure that allows for the modeling of multiple types of interactions among users and items. The hypergraph structure is parameterized, which means that the model can learn the weights of the hyperedges that connect users and items based on their interactions.

2. Contrastive learning is a technique that learns representations by contrasting positive and negative examples. In the context of DHCF, the authors use contrastive learning to learn representations of users and items that are optimized for predicting the interactions between them. By using contrastive learning, the authors are able to learn more robust representations that are less sensitive to data sparsity.

3. The authors' experiments show that DHCF significantly outperforms various strong baselines on three public datasets, which further supports the effectiveness of their approach.

### Weaknesses
1. The proposed Dynamic Hypergraph Collaborative Filtering (DHCF) approach presents a unique take on recommendation systems; however, its distinctiveness and advancements over existing methodologies in the literature are not sufficiently highlighted. To strengthen the paper, the authors should conduct a more comprehensive comparison of DHCF with prevailing models, pinpointing exact areas of improvement and innovation. Integrating and discussing the influence of more contemporary trends in recommendation systems, such as applications of deep learning or graph neural networks, would further enrich the paper's relevance and depth.

2. The paper currently lacks clarity and detail regarding the algorithms and techniques underpinning the DHCF approach. To remedy this, a more explicit elucidation of the methodology is required. Additionally, incorporating visual aids or concrete examples could help in visualizing the hypergraph structure and elucidating the concept of behavior-wise contrastive learning, making the paper more accessible and informative.

3. A more thorough examination of DHCF would contribute to a balanced and comprehensive understanding of the approach. Specific areas such as the scalability of DHCF to larger datasets and its sensitivity to hyperparameter choices warrant detailed discussion.

### Questions
1. In the paper, you mention that many existing recommendation models fail to exploit the relational dependencies across different types of user behaviors. Could you provide more details on how DHCF addresses this limitation? How does the parameterized heterogeneous hypergraph architecture capture the complex and diverse interactions among users, items, and behaviors?

2. In the paper, you also mention that many existing recommendation models fail to disentangle the latent intent factors behind each behavior. Could you provide more details on how DHCF disentangles the latent intent factors behind each behavior? How does the behavior-wise contrastive learning paradigm facilitate adaptive data augmentation at both the node and graph levels?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this work, the authors focus on combining intent disentanglement and multi-behavior modeling for collaborative filtering. The proposed method -- DHCF utilizes parameterized heterogeneous hypergraph to encode intents embeddings, and introduces behavior-wise contrastive learning to improve model robustness. Offline experiments are conducted on public datasets to demonstrate the performance of DHCF on Top-k item recommendation.

### Strengths
1. This paper provides insight on utilizing multi-behavior data in recommendation systems.
2. The proposed method outperforms the baseline methods on HR and NDCG for top-10 recommendation. 
3. Ablation analysis is included.

### Weaknesses
1. The model consists of multiple components, which are difficult to optimize and converge. It is hard to be applied in the real-world case.
2. The robustness analysis is not convincing. To demonstrate the model's robustness, we expect it to achieve stable performance on difficult tasks, where baseline methods perform poorly compared to easy tasks. However, in Figure 3, the baseline methods achieve similar performance on different user groups. This comparison is not convincing evidence of the method's robustness.

### Questions
1. It is strange that the basic methods like NCF achieve similar performance on different user groups (in Figure 3). Instead of evaluating on tailed items, why did the authors test the performance on different user groups for robustness analysis?
2. Is the meta-learning process considered while calculating the complexity in section 3.7?
3. Any evidence to support the convergence of the learnable hypergraphs?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
