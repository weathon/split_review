# A Geometric Approach to Personalized Recommendation with Set-Theoretic Constraints Using Box Embeddings

- Decision: Reject
- Scores: 5, 3, 5

## Abstract
Personalized item recommendation typically suffers from data sparsity, which is most often addressed by learning vector representations of users and items via low-rank matrix factorization. While this effectively densifies the matrix by assuming users and movies can be represented by linearly dependent latent features, it does not capture more complicated interactions. For example, vector representations struggle with set-theoretic relationships, such as negation and intersection, e.g. recommending a movie that is “comedy and action, but not romance”. In this work, we formulate the problem of personalized item recommendation as matrix completion where rows are set-theoretically dependent. To capture this set-theoretic dependence we represent each user and attribute by a hyperrectangle or box (i.e. a Cartesian product of intervals). Box embeddings can intuitively be understood as trainable Venn diagrams, and thus not only inherently represent similarity (via the Jaccard index), but also naturally and faithfully support arbitrary set-theoretic relationships. Queries involving set-theoretic constraints can be efficiently computed directly on the embedding space by performing geometric operations on the representations. We empirically demonstrate the superiority of box embeddings over vector-based neural methods on both simple and complex item recommendation queries by up to 30% overall.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes using box embeddings for matrix completion to improve personalized item recommendation with set-theoretic queries. Box embeddings are employed to bypass the limitation of commonly used vector embeddings, which might fail to recommend items for set-theoretic queries consisting of negotiation and intersection relationships. By representing users, items. and attributes as box embeddings, i.e., hyper rectangles in d-dimensional space, the proposed approach can jointly factorize user-item interaction matrix and item-attribute matrix. Then, users and attributes are regarded as boxes containing multiple items. As such, given a query containing set relationships between attributes, the model retrieves top items having the largest box volume shared with those of users as recommendation list. The whole model is trained to capture containing relationships, i.e., user and attribute boxes contain multiple item boxes. Experimental results on four datasets demonstrate the strong performance of the proposed method.

### Strengths
1. The paper studies an interesting yet not well explored problem: personalized item recommendation with set-theoretic queries. The set nature of queries, which consists of set relationships such as negotiation and intersection, leads to an interesting research question: how to capture such relationships to make more accurate recommendations.

2. The employment of box embeddings to represent users, items, and attributes is intuitive and sensible to capture set relationships between these three.

3. Experimental results on four real-world datasets demonstrate good performance of the proposed box embedding method, outperforming vector embedding approaches.

4. The paper is well-structured and easy to follow.

### Weaknesses
1. Despite showing promising recommendation results, the proposed method seems to be a direct application of box embeddings for personalized item recommendation with set theoretic queries, which is somehow a limited contribution.

2. The paper relies heavily on the theory of box embeddings but some key concepts were not described sufficiently. For example, in line 191, how to guarantee $x^\llcorner < x^\urcorner$ for all dimensions $d$; what is the definition of $VolIntGB$ in Equation 3?; what are the parameters of the model to optimize?

3. The baselines are somewhat limited. Although authors already mentioned in Section 2.1., representative baselines such as LightGCN [1] and MultiVAE [2] were not considered. Including more recent and advanced baselines will further ascertain the strength of the proposed method.

4. Lack of efficiency analysis. What is the advantage of using box embeddings over vector embedding w.r.t. running time?

5. Missing descriptions of some important experimental settings, e.g., how many negative sampled required to train Equations in lines 233 and 240. Moreover, ablative analysis of key hyper-parameters is also not presented. For instance, how the number of negative samples affect the model accuracy? The same questions for $w$ in line 240.

### Questions
The paper introduces the notation of query in the context of recommendation systems. What is the difference between query in the context of this paper and query in the context of search engine like Google?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The authors apply box embedding to attribute-specific query recommendation.
They formulated the task of attribute-specific query recommendation and proposed a recommendation method based on box embedding for the task.
The authors also tried establishing an evaluation protocol for this new task and provided detailed analyses based on generalization spectrum gap and compound error.
On the other hand, the current manuscript severely lacks a discussion of existing recommendation fields (e.g., context-aware recommendation), and the technical novelty is unclear.

### Strengths
1. The authors tried to use the latest technique in the NLP field (i.e., box embedding) for a recommendation-related task. 
2. The authors have carefully designed an evaluation protocol for attribute-specific query recommendation based on traditional collaborative filtering.

### Weaknesses
1. The scope of this study is on a rather limited application, which the authors called "attribute-specific query recommendation".
2. The current manuscript lacks related work on "attribute-specific query recommendation". In addition, the authors should discuss the relationship between this study and context-aware recommender systems [a].
3. Some experimental settings are not convincing. See the following questions/comments for details.

### Questions
### Questions
  - (Q1) The authors used nDCG@K for model selection, but evaluated the final performance based on HR@K. Why did the authors use inconsistent metrics for validation and testing? In my opinion, HR@K with 100 negative items is a rather insensitive measure for ranking evaluation. I would like to recommend using Recall@K without negative sampling.
  - (Q2) In the current manuscript, the authors do not mention/discuss the result on MovieLens-20M (Table 7 in Appendix B.3). Also, Table 7 is not self-contained. What is the definition of VEC-*? (probably MF or NeuMF?)
 
### Comments.
   - (C1) To my understanding, "attribute-specific query recommendation" is the task where (1) item attribute values are partially observed and often missing, and (2) in the prediction phase, the positive items are conditioned not only on a user but also on a boolean query. The problem of (1) has been addressed in existing studies (e.g., [b,c]). I am not familiar with (2) in the context of item recommendation, but there might be existing research on it.  A discussion/comparison of existing studies on these points would make it easier to understand the novelty of this work.
   - (C2) In line 368, the authors report that they followed the standard sample scoring procedure described in Rendle et al. (2020). However, to my understanding, using this sampling technique is not recommended for a dataset with a small item catalog such as Last-FM, MovieLens-1M, NYC-R. It may just undermine the reliability of the reported results to reduce a small experimental cost.


## References

 [b] Wu, Le, et al. "Joint item recommendation and attribute inference: An adaptive graph convolutional network approach." Proceedings of the 43rd International ACM SIGIR conference on research and development in Information Retrieval. 2020.

 [c] Xian, Yikun, et al. "Ex3: Explainable attribute-aware item-set recommendations." Proceedings of the 15th ACM Conference on Recommender Systems. 2021.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work addresses the task of personalized recommendation using set-theoretic queries. The authors frame this problem as "set-theoretic matrix completion," highlighting that traditional approaches, such as logistic matrix factorization, do not align with the set-theoretic operations needed during inference.

### Strengths
1.	The study models attribute-specific query recommendation as "set-theoretic matrix completion," treating attributes and users as item sets.
2.	The paper effectively demonstrates the limitations of existing vector embedding models for this specific task.
3.	Experimental results validate the effectiveness of the proposed model.

### Weaknesses
1.	The approach presented in this paper conflicts with the widely used matrix factorization model, which effectively leverages collaborative filtering signals between users and items. It is unclear how the proposed model addresses these signals, particularly in capturing the nuanced relationships that arise from user-item interactions beyond simple set containment. The model's reliance on set-theoretic operations may oversimplify the complex patterns that matrix factorization captures through learned vector embeddings and dot products.
2.	The experimental baselines are not state-of-the-art; comparing the proposed method to more advanced recommendation models, such as those incorporating graph neural networks or attention mechanisms, would better demonstrate its advantages. The current baselines do not provide a strong enough comparison to establish the novelty and effectiveness of the proposed method in the context of modern recommendation systems.
3.	Some equations are difficult to follow due to unclear notation explanations, specifically regarding the precise definitions of the box embeddings and the volume calculation. The lack of clarity makes it challenging to understand the underlying mathematical operations and how they translate into the proposed model's behavior.

### Questions
It is suggested that an efficiency comparison between the traditional vector embedding methods and the proposed box embedding method be discussed.

### Soundness
3

### Presentation
2

### Contribution
2
