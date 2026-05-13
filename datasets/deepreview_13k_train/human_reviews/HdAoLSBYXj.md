# Topic Modeling as Multi-Objective Contrastive Optimization

- Decision: Accept
- Scores: 6, 6, 6

## Abstract
Recent representation learning approaches enhance neural topic models by optimizing the weighted linear combination of the evidence lower bound (ELBO) of the log-likelihood and the contrastive learning objective that contrasts pairs of input documents. However, document-level contrastive learning might capture low-level mutual information, such as word ratio, which disturbs topic modeling. Moreover, there is a potential conflict between the ELBO loss that memorizes input details for better reconstruction quality, and the contrastive loss which attempts to learn topic representations that generalize among input documents. To address these issues, we first introduce a novel contrastive learning method oriented towards sets of topic vectors to capture useful semantics that are shared among a set of input documents. Secondly, we explicitly cast contrastive topic modeling as a gradient-based multi-objective optimization problem, with the goal of achieving a Pareto stationary solution that balances the trade-off between the ELBO and the contrastive objective. Extensive experiments demonstrate that our framework consistently produces higher-performing neural topic models in terms of topic coherence, topic diversity, and downstream performance.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper aims to address challenges in neural topic models (NTMs) caused by recent approaches that optimize the combination of ELBO and contrastive learning. These challenges include capturing low-level mutual information and a conflict between ELBO's focus on input details for reconstruction quality and contrastive learning's goal of generalizing topic representations. To overcome these issues, the authors propose a novel setwise contrastive learning method for sets of documents, aiming to capture shared semantics among documents. Additionally, they formulate contrastive topic modeling as a multi-objective optimization problem to achieve a balanced solution. Experimental results on 4 benchmark datasets demonstrate that their approach consistently produces higher-performing NTMs in terms of topic coherence, diversity, and document classification performance compared to existing methods.

### Strengths
+ The key idea of this paper (i.e., learning low-level mutual information of neural topic models that optimize ELBO and contrastive learning together) is very well-motivated.

+ The usage of setwise contrastive topic modeling is reasonable. Casting it as a multi-task learning problem and adopting multi-objective optimization to find a Pareto solution are technically novel.

+ A comprehensive set of benchmark datasets and baselines are considered. The authors also perform detailed ablation studies, hyperparameter analyses, and case studies.

### Weaknesses
 - Statistical significance tests are missing. It is unclear whether the gaps between the proposed model and baselines/ablation versions are statistically significant or not. In particular, some gaps in Tables 3 and 6 are quite subtle, and the variances of classification scores in Table 2 are unknown, therefore p-values should be reported. The lack of statistical testing makes it difficult to ascertain if the observed improvements are genuine or simply due to random variation, especially given the relatively small performance differences in some cases. For instance, a difference of 0.01 in a metric might be practically meaningless if the standard deviation is also around 0.01 or higher.

- Only automatic metrics (e.g., NPMI and TD) are used to evaluate topic quality. Although the authors also examine document classification as a downstream task, the classification performance is just an indirect measurement of topic quality. Recent work [1] has shown that automatic metrics may deviate from humans' judgment. Therefore, I feel human evaluation (e.g., the intrusion test [2]) is still needed. The reliance on automatic metrics alone is a limitation because these metrics might not fully capture the semantic coherence and interpretability of the topics from a human perspective. While NPMI and topic diversity (TD) are useful for assessing certain aspects of topic quality, they do not directly measure how well the topics align with human understanding.

### Questions
- Could you conduct statistical significance tests to compare your method with the baselines in the experiment tables?

- Could you perform human evaluation (e.g., the intrusion test) to directly examine the quality of extracted topics?

### Soundness
2 fair

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a setwise contrastive learning algorithm for neural topic model to address the problem of learning low-level mutual information of neural topic models. This work explicitly casts contrastive topic modeling as a gradient-based multi-objective optimization problem. Extensive experiments are performed to demonstrate the effectiveness of this method.

### Strengths
1. This paper is well-organized and equations are clearly written.
2. Extensive experimental are performed and results show this method consistently presents high performance.
3. Codes are provided in supplementary materials to ensure reproducibility.

### Weaknesses
1. Since [1] also uses contrastive learning to capture useful semantics of topic vectors which is similar to the proposed method, this paper does not clearly compare with [1] and explain its novelty. 
2. This paper omits important baselines. For example, [1] also presents great performance in this task but this paper does not compare with it in the experiments. Which contrastive learning method performs better? 

### Questions
1. I have a question about the baselines. Table 5 shows topic diversity (TD) score of WeTe is 0.878±0.012 when T = 50 in AG News dataset. However, in [1], this score is 0.966 without data augmentation and 0.991 with data augmentation. There is a large gap between these scores. I wonder how authors implement these baselines. Could you please provide more details or any codes?

[1] Xiaobao Wu, Anh Tuan Luu, and Xinshuai Dong. Mitigating data sparsity for short text topic modeling by topic-semantic contrastive learning. arXiv preprint arXiv:2211.12878, 2022.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a set-wise contrastive learning algorithm for neural topic models, where the input document batch is divided into sets and positives and negatives are constructed by augmenting and pooling instances in each set. It casts the proposed method as a multi-objective optimization problem to balance the trade-off between the ELBO and the contrastive objectives. The ChaptGPT API is used for data augmentation to generate negative samples. Experiments demonstrate the effectiveness of the proposed method.

### Strengths
- The set-wise contrastive learning is new and effective for resolving low-level mutual information of neural topic models. 
- Formulating the contrastive learning as a multi-task learning problem and solving it by a multi-objective optimization algorithm is an interesting idea. 
- Experimental comparisons with state-of-the-art neural topic models that include recent ones such as WeTe demonstrate the effectiveness of the proposed moethod.

### Weaknesses
 - The effectiveness of the ChatGPT-based data augmentation is unclear.
- The formal definition of the contrastive loss is  missing in the main text, while incomplete definition can be found in Algorithm 1. 
- The justification of the use of MaxPooling is unclear. 
- The authors seem to assume as if it is possible to find "the optimal" Pareto solution (a Pareto optimal solution with optimal balance), while there is no superiority or inferiority between Pareto optimal solutions.

### Questions
In Section 4.1, the authors adopt ChatGPT API to perform the augmentation with the specific prompt.
However, at the end of Section 5.1, they use Word2Vec as pretrained embedding for their embedding-based augmentation.
This is confusing. Do they perform both ChatGPT-based and embedding-based augmentations for comparisons? 
Anyway, they should show the effectiveness of the ChatGPT-based augmentation. 

In Section 5.5 on page 9, they justify the use of MaxPooling, for extracting set representation,  as MaxPooling directly retrieving strong features. In Table 6, they compare different pooling functions including max and min poolings. 
However, in Algorithm 1, both MaxPool and MinPool are used. Here, MinPool is used for positive pair. 
They should clarify the reason why.

The purpose of multi-objective optimization is to find a  (possibly diversified) set of Pareto optimal solutions so that it represents the Pareto frontier. Therefore, I would like to know the average and standard deviation of the $\alpha$  obtained at the end of each run to see how it is diversified. If it is not diversified, then I would like to know the reason.  

Judging from the definition of $\mathcal{L}_{set}$ in Algorithm 1, both the positive and the negative pairs are generated within the same set and the loss is then accumulated for all the sets. If this is the case, then the first sentence of the Hard Negative Sampling paragraph sounds confusing. Differenciating among sets may be more difficult, but the contrastive pair for differenciating is generated within a set not among sets.  In Algorithm 1,  $\exp(s_i^{min}, s_i^{+})$ should be $\exp(f(s_i^{min}, s_i^{+}))$. 

How and what value for the contrastive weight $\beta$ is determined?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
