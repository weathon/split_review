# Towards Optimizing Top-$K$ Ranking Metrics in Recommender Systems

- Decision: Reject
- Scores: 3, 3, 5, 5

## Abstract
In the realm of recommender systems (RS), Top-$K$ metrics such as NDCG@$K$ are the gold standard for evaluating performance. Nonetheless, during the training of recommendation models, optimizing NDCG@$K$ poses significant challenges due to its inherent discontinuous nature and the intricacies of the Top-K truncation mechanism. Recent efforts to optimize NDCG@$K$ have either neglected the Top-$K$ truncation or suffered from low computational efficiency. To overcome these limitations, we propose SoftmaxLoss@$K$ (SL@$K$), a new loss function designed as a surrogate for optimizing NDCG@$K$ in RS. SL@$K$ integrates a quantile-based technique to handle the complex truncation term; and derives a smooth approximation of NDCG@$K$ to address discontinuity. Our theoretical analysis confirms the close bounded relationship between NDCG@$K$ and SL@$K$.  
    Besides, SL@$K$ also exhibits several desirable properties including concise formulation, computational efficiency, and noisy robustness. Extensive experiments on four real-world datasets and three recommendation backbones demonstrate that SL@$K$ outperforms existing loss functions with a notable average improvement of 6.19\%.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
Summary:

This paper proposes a new loss function named SoftmaxLoss@K (SL@K), which could be an alternative choice when it comes to optimizing NDCG@K for recommender system.

### Strengths
Strengths:

-	The idea is simple and intuitive, easy to understand.
-	The experiments are conducted based on well-known datasets and baselines (and algorithms)
-	The authors also provided ablation studies 
-	The authors provided source code for reproducibility and details in the Appendix are also given.

### Weaknesses
Weaknesses:

-	In my opinion, the contribution is marginal, as compared with previous works in [1, 2, 3].
-	It’s still not very clear about the benefits of using SL@K. Simply looking at Table 1, 2, 3, it appears that the best baseline performance is not stable across scenarios, is it an advantage of SL@K for stable / trustable performance?
-	Since the work focuses on SL@K; it’s worth to explore more numbers of K (e.g., 5,10,15,20,25,…100) instead of just a few Ks.
-	As a follow-up, it’s better to compare SL@K, NDCG@K, and LambdaLoss@K across experiments (e.g., Figure 3 and Table 4)
-	If the authors would like to emphasize on the practical applications (as compared to LambdaLoss@K for example), more examples should be given with large dataset such as Netflix or MovieLens20M. I understand Table 3 is given, but in my opinion, small datasets with MF backbone cannot guaranteed its practical application for large-scale RS (as mentioned in L183-200

### Questions
Please refer to the weaknesses section; I may have more questions later.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces a novel ranking loss function that optimises ndcg@k a popular evaluation metric utilised in recommender systems. The authors base the loss function on a sampled version of the softmax loss version where a quantile technique is used to separate the items in the top K from the rest. The authors provide a comparison to other similar loss functions and a fairly extensive experimental section which demonstrates significant gains compared to other loss functions. '
The related work, analysis of the lambda loss function and proofs are included in the appendix.

### Strengths
The paper is well written and easy to follow for the most part. 
The loss function can be of potential practical use in some recommender systems applications. 
The experimental section is fairly extensive.

### Weaknesses
The contribution of the paper is rather limited, over the last 10 years a large number of ranking loss functions have been proposed. 
The core topic of this paper falls somewhat outside of the core interests of this conference, a IR or recommender systems conference might be more appropriate. 
Code is not included in the submission
It is unclear how this loss function would perform compared to the large number of already proposed loss function for recommendation. 
While optimising for IR evaluation metrics is a good way of showing increases in offline experimental results in recommender systems papers it is unclear how relevant these gains are in real online recommendation systems as techniques as off-policy correction and IPS seem to produce bigger gains in real world recommendation engines rather than then latest ranking loss function.

### Questions
My main suggestion is to find a more appropriate venue for this paper that is closer to the core audience that could be interested in the topic.

### Soundness
3

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
4

### Summary
In this paper, the authors propose a new softmax loss as a surrogate for optimizing NDCG@K in ranking tasks. My primary concerns revolve around the paper's motivation and experimental validation.

### Strengths
1. The topic of this paper is highly interesting.
2. The paper provides a theoretical guarantee for optimizing the proposed method.
3. The proposed methods demonstrate significant improvements in experiments.

### Weaknesses
1. The motivation of this paper is problematic.
2. The softmax loss is not novel; therefore, the paper should clarify its novelty and distinguish the proposed methods from existing solutions.
3. The experiments only include small datasets and traditional ranking methods. I highly recommend that the authors use large-scale recommendation datasets and incorporate modern recommendation and ranking models.

### Questions
The authors’ exploration of ranking loss is compelling and relevant to real-world applications. My concerns center on the following aspects. Firstly, the inconsistency between NDCG and NDCG@K appears similar to the difference between NDCG@K1 and NDCG@K2 for different values of K. However, this observation alone does not provide a basis for questioning the NDCG metric itself, as NDCG@K is designed to evaluate ranking performance for the top-K items, which naturally varies with different values of K. I highly encourage the authors to clarify their motivation further. Additionally, if they wish to highlight this observation, it would be useful to evaluate the inconsistency between SL@K1 and SL@K2 as well.

I appreciate the authors' effort in introducing a new loss function, and I suggest they summarize the distinctions between their proposed loss function and existing softmax loss functions [1]. In the experiments, I recommend including models such as DeepFM [2], DIN [3], and SIM [4], as MF and LightGCN are less common in real-world recommendation settings.

[1] On the Effectiveness of Sampled Softmax Loss for Item Recommendation
[2] DeepFM: A Factorization-Machine based Neural Network for CTR Prediction
[3] Deep Interest Network for Click-Through Rate Prediction
[4] Search-based User Interest Modeling with Lifelong Sequential Behavior Data for Click-Through Rate Prediction

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
Recommender systems are often referred to as top-K item recommendation tasks, and as such, much of the literature over the past decade has sought solutions to optimize these top-K ranking metrics. This paper makes a similar argument and proposes a new ranking loss called SoftmaxLoss. The authors provide a reasonable analysis of the difficulty of optimizing NDCG and derive a mathematical derivation of how NDCG might be optimized. In particular, the authors make multiple approximations in Equations 3.3b, 3.3d, 3.3e. Finally, in Equation 3.5, they derive the so-called loss. They perform extensive experiments to show that SoftmaxLoss is a good optimizer for top-N ranking.

### Strengths
(1) The paper is well written and easy to understand, with clear motivation and ideas

(2) The authors provide a rationale for the NDCG optimization problem

(3) A large number of experiments are performed to support the claim

### Weaknesses
(1) While I agree that optimizing top-K metrics such as NDCG or MRR is important for recommendation tasks, the existing literature over the past decade is extensive. Although numerous new solutions have been proposed, the commonly used loss functions still primarily include cross-entropy loss, batch softmax loss [1], and negative sampling-based pairwise ranking [2,3,5]. In my view, this particular solution does not significantly advance the field, as the ranking problem has been well-established in recent years; it is a relatively old topic.

(2) The proposed solution primarily addresses the recall stage, while CTR prediction tasks continue to focus on AUC during the offline phase. The relative improvements in the recall stage may not have a substantial impact on the final ranking stage.

(3) As I mentioned, there is an abundance of related literature, and the authors may have overlooked some key works. For example, the authors compare their approach to BPR loss, which is a well-known baseline function. Many studies have indicated that incorporating negative sampling can significantly enhance BPR's performance. The authors should consider comparing their results with other relevant literature, such as WARP loss[2], LambdaFM loss[3], and batch softmax loss[1].

(4) Additionally, while the topic falls under the realm of learning to rank, it is noteworthy that learning-to-rank has not been prominently featured in recent literature. The 2011 Yahoo Learning to Rank Challenge highlighted that optimization of top-K ranking metrics is not particularly impressive compared to classical regression and classification losses.

All in all, the topic discussed in this article is not really interesting to me personally and it does not address a very important problem in the field of current recommender systems. It feels like just another paper on the subject. 


[1] Sampling-bias-corrected neural modeling for large corpus item recommendations. Recsys2019

[2] WSABIE: Scaling Up To Large Vocabulary Image Annotation. IJCAI 2011

[3] LambdaFM: Learning Optimal Ranking with Factorization Machines Using Lambda Surrogates. CIKM2016

[4] Yahoo! learning to rank challenge overview. Proceedings of the learning to rank challenge 2011

[5] Co-Factorization Machines: Modeling User Interests and Predicting Individual Decisions in Twitter.WSDM 2013

### Questions
No

### Soundness
3

### Presentation
3

### Contribution
2
