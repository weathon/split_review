# ContextGNN: Beyond Two-Tower Recommendation Systems

- Decision: Accept
- Avg Score: 5.80
- Scores: 8, 5, 5, 5, 6

## Abstract
Recommendation systems predominantly utilize two-tower architectures, which evaluate user-item rankings through the inner product of their respective embeddings.
However, one key limitation of two-tower models is that they learn a pair-agnostic representation of users and items.
In contrast, pair-wise representations either scale poorly due to their quadratic complexity or are too restrictive on the candidate pairs to rank.
To address these issues, we introduce \emph{\fullnames} (\names), a novel deep learning architecture for link prediction in recommendation systems.
The method employs a pair-wise representation technique for familiar items situated within a user's local subgraph, while leveraging two-tower representations to facilitate the recommendation of exploratory items.
A final network then predicts how to fuse both pair-wise and two-tower recommendations into a single ranking of items.
We demonstrate that \name is able to adapt to different data characteristics and outperforms existing methods, both traditional and GNN-based, on a diverse set of practical recommendation tasks, improving performance by 20\% on average.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes ContextGNNs, a new architecture for graph-based recommendation. Unlike previous similar approaches, such as pair-wise recommendation solutions, the authors propose a pair-wise representation only for exploring the items in the user's local subgraph, while the architecture employs the usual two-tower method for the item side. Finally, a network is designed and trained to fuse the two representations and provide the final recommendations. 

On the one hand, the ContextGNNs framework first generates a pair-wise representation for users and items, where a $k$-hop subgraph for each user is sampled, and a GNN is leveraged to obtain embedding representations and the overall item ranking. On the other hand, a two-tower representation is exploited on the item side, as it can be shown that: 1) GNNs do not learn useful information on the item side as the item interaction matrix tends to be very dense; 2) shallow item embeddings are effective; 3) GNN item representations can scale poorly with large numbers of items in the catalog. The so-learned item embeddings are injected into the GNN forward pass presented above, to allow the user representations to align with the item ones. Finally, an MLP is trained to fuse the two designed contributions. 

Results on different tasks and datasets from the RelBench platform demonstrate the efficacy of the ContextGNNs proposed baseline, also when compared to different settings of the same model.

### Strengths
\+ The proposed approach is well-placed within the existing literature on (graph)-based recommendation, and the motivations behind ContextGNNs are quite solid and sound

\+ Overall, the paper is well-written and easy to follow

\+ I appreciated the locality score study, which conceptually and empirically supports the rationale behind the approach

\+ I also appreciated how the authors discussed possible extensions of the proposed approach in different and interesting new directions

\+ Even considering the page limitations, I believe the experimental setting is adequately extensive to empirically support the rationale behind the paper

### Weaknesses
 - To my understanding, it seems that the list of baselines for the experiments is not completely diversified and updated to the latest advances in graph-based recommendation. I would have appreciated seeing more recent and popular approaches being tested against ContextGNNs, such as LightGCN (cited in the paper), SGL [i], UltraGCN [ii], SimGCL [iii], and LightGCL [iv]. Specifically, the absence of contrastive learning-based methods is a notable gap, given their recent success in improving the robustness and generalization of graph neural networks for recommendation. Furthermore, the baselines lack methods that explicitly address the issue of over-smoothing in GNNs, which could provide a more comprehensive comparison against the proposed approach. It would also be beneficial to include methods that use different graph aggregation techniques, such as attention-based mechanisms, to evaluate the effectiveness of the proposed GNN architecture.

### Questions
I have a question that does not refer to the one weakness raised. As observed by the authors in the locality score study, it is interesting to see that many validation/test links are not in the users' nearest neighborhood. Moreover, we know from the literature, that graph-based recommender systems may be affected by oversmoothing. On such a basis, my question is: how the graph-based model can learn long-range (and, evidently, ground-truth) products connected to users if the model cannot explore on more than ~3 hops (on average)? Do you have any intuitions for that?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper studies the two-tower architecture for recommender systems. They introduce a context-based GNNs-based framework for link prediction in recommendation by using a pair-wise representation technique for similar items in the user's local subgraph. The proposed method achieves promising performance in their experiments.

### Strengths
1. The research issue is very important in the industry. 

2. Their experimental results demonstrate the effectiveness of the proposed method. 

3. The paper is easy to follow.

### Weaknesses
However, there are some concerns in the paper:

1. The novelty of the proposed method is unclear.
This paper leverages local interaction graph for representation learning. The idea is very mature and has been well-studied.
 Compared with exciting methods, what are the novelty of the proposed method? Additionally, the related work in the paper can be enhanced.
This paper can be improved by discussing more advanced two-tower architectures. Furthermore, the related work cannot demonstrate the novelty of the proposed method.


2. The technical contributions of this work are also unclear. I was wondering what are the main challenges they are addressing.
The proposed idea looks good. However, the proposed method doesn't have any theoretical analysis.
The model design didn't motivate well.
This paper considers the temporal factor in modeling recommendation. However, what are the technical contributions for taking advantage of it?


3. The experimental section can be enhanced before publication. First, they can compare with some advanced recommendation baselines. There are many advanced recommendation methods for modeling user and item representations.
Second, the datasets here are unclear to me. Whether the proposed method can be used for large-scale datasets?

### Questions
See the weakness.

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
This paper proposes a recommendation framework that integrates pair-wise representations with two-tower representations. Specifically, it leverages pair-wise representations to capture fine-grained patterns of past user-item interactions, while utilizing two-tower representations for "distant" items. The authors have validated the effectiveness of their approach on the RELBENCH benchmark.

### Strengths
1. The motivation behind the proposed method is clear and has significant practical implications for large-scale recommendation systems in the real world.
2. The authors have validated the effectiveness of the proposed method on the benchmark datasets.

### Weaknesses
1. The authors emphasize in the abstract and introduction that their method is a relatively general and effective strategy in recommendation scenarios. However, the experimental section only tests the method on datasets that include rich multi-behavioral and temporal interactions. This discrepancy between the claims and the experimental validation raises concerns. Therefore, the authors should either revise their overall statements or consider incorporating a wider variety of datasets for comparative analysis.
2. The experimental section of the paper is quite limited, as it currently only reports the MAP metric and lacks detailed parameter sensitivity analysis. Moreover, the paper does not address how the proposed method's performance may be affected when user behavior information in the dataset is insufficient in type or quantity. Specifically, would we expect a significant decline in performance compared to the baseline algorithms under such conditions? Additionally, I recommend that the authors incorporate a broader range of recent comparison methods to strengthen their empirical evaluation.
3. The paper does not provide the original code, which raises concerns regarding the reproducibility of the results. Additionally, there are some errors in the equations presented.

### Questions
Please refer to the weaknesses

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
* The method uses a pair-wise representation for familiar items in a user's local subgraph and two-tower representations for recommending exploratory items. A final network combines both pair-wise and two-tower recommendations to create a unified ranking of items.

* The study utilizes CONTEXTGNNs in relational deep learning for recommendations within relational databases, which consist of various tables with rich multi-modal features and complex behavioral interactions. This environment provides an ideal setting for testing the model's effectiveness. Additionally, the research explores the challenges of modeling intricate human behavior patterns.

### Strengths
* This article has a clear structure and is easy to follow.

*Tested different tasks, which is rare in previous work.

### Weaknesses
 * It appears that this work has not released the code or dataset, making reproducibility uncertain.

* This work lacks technical innovation and seems quite basic. Such a simple design should emphasize time complexity, runtime efficiency, and scalability, but the paper does not seem to address these aspects.

* This work does not compare with other recent baselines or commonly used models in the industry. Additionally, it does not provide specific data from the dataset. Whether in industry or research, this work does not seem to fit well. Overall, it appears too basic and simple, with relatively little effort involved.

### Questions
* The paper mentions the complexity issues of pair-wise methods. Could you provide a time complexity analysis and runtime efficiency experiments of this work compared to others?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents ContextGNN, a refined approach that classifies items into user-specific selections within a user-centric local graph, alongside other items. Subsequently, the GNN learns the pertinent user and item embeddings, thereby enabling the derivation of both pairwise and two-tower representations for enhanced recommendations.

### Strengths
1. The paper is well-written and easy to understand.
2. The use of both pairwise and two-tower representations for recommendations is quite interesting.
3. The experiments conducted in this paper seem to demonstrate the model's effectiveness.

### Weaknesses
1. The author should consider open-sourcing the code for the proposed method to enhance reproducibility.
2. In the comparison of methods, it would be beneficial to include more recent and advanced GNN-based recommender models beyond NGCF.
3. Given that the author mentions both multi-behavior and temporal graphs, it would be advantageous to illustrate how the GNN backbone is designed to accommodate such graphs.

### Questions
See Weaknesses.

### Soundness
3

### Presentation
4

### Contribution
3
