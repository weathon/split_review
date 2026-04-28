# AFDGCF: Adaptive Feature De-correlation Graph Collaborative Filtering for Recommendations

- Decision: Reject
- Avg Score: 6.50
- Scores: 8, 5, 5, 8

## Abstract
Collaborative filtering methods based on graph neural networks (GNNs) have witnessed significant success in recommender systems (RS), capitalizing on their ability to capture collaborative signals within intricate user-item relationships via message-passing mechanisms. However, these GNN-based RS inadvertently introduce excess linear correlation between user and item embeddings, contradicting the goal of providing personalized recommendations. While existing research predominantly ascribes this flaw to the over-smoothing problem, this paper underscores the critical, often overlooked role of the over-correlation issue in diminishing the effectiveness of GNN representations and subsequent recommendation performance. Up to now, the over-correlation issue remains unexplored in RS. Meanwhile, how to mitigate the impact of over-correlation while preserving collaborative filtering signals is a significant challenge.
To this end, this paper aims to address the aforementioned gap by undertaking a comprehensive study of the over-correlation issue in graph collaborative filtering models. Firstly, we present empirical evidence to demonstrate the widespread prevalence of over-correlation in these models. Subsequently, we dive into a theoretical analysis which establishes a pivotal connection between the over-correlation and over-smoothing issues. Leveraging these insights, we introduce the \underline{\textbf{A}}daptive \underline{\textbf{F}}eature \underline{\textbf{D}}e-correlation \underline{\textbf{G}}raph \underline{\textbf{C}}ollaborative \underline{\textbf{F}}iltering (AFDGCF) framework, which dynamically applies correlation penalties to the feature dimensions of the representation matrix, effectively alleviating both over-correlation and over-smoothing issues.
The efficacy of the proposed framework is corroborated through extensive experiments conducted with four representative graph collaborative filtering models across four publicly available datasets. Our results show the superiority of AFDGCF in enhancing the performance landscape of graph collaborative filtering models.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper discusses the possible connections between over-smoothing and over-correlation in graph neural networks-based recommender systems. Indeed, while over-smoothing has been debated in graph-based recommendation for quite some time now, the authors claim over-correlation is still not properly analysed as happening in graph representation learning. Through an initial empirical study, the authors demonstrate that the negative effects of the two issues seem to be directly dependent and go along with the performance degradation of the models (i.e., usually after the third message-passing layer). After that, the paper underlines how over-smoothing and over-correlation may present a direct mapping to rows and columns in the node embedding matrix, respectively, and mathematically proves that the two are proportional. In this respect, as alleviating one of the two would tackle also the other, the authors propose a loss function named adaptive feature decorrelation, that comes into a static and dynamic version. An extensive experimental setting comprising four recommendation datasets and nine baselines demonstrates the efficacy of the proposed approach. Indeed, when applied to existing graph-based recommender systems, the adaptive feature decorrelation loss function is beneficial to improve the performance in terms of recommendation accuracy and requiring much less epochs to reach convergence. Finally, an ablation study justifies the soundness of the proposed architectural choices.

### Strengths
+ The addressed problem (i.e., over-smoothing and over-correlation in graph-based recommendation) is relatively new to the literature.
+ The empirical analysis supported by the mathematical proofs help justifying the existing problem and opening to possible solutions.
+ The experimental setting is extensive with numerous evaluation dimensions.
+ The code and datasets are released at review time.

### Weaknesses
- Some details about the introduced methodology need to be clarified. Specifically, the exact mechanism through which the adaptive feature decorrelation loss function is integrated into the existing graph-based recommender systems requires more elaboration. For instance, it's not entirely clear how the static and dynamic versions of the loss function differ in terms of their implementation within the message-passing framework, and how these versions affect the gradient flow during training. A more detailed explanation of the algorithmic steps and the corresponding mathematical formulations would be beneficial for reproducibility and understanding.
- The authors may have not considered other graph-based recommendation baselines whose solutions are like the proposed one. While the paper touches upon the issue of over-correlation, it would be beneficial to explicitly acknowledge and discuss existing methods that also aim to address similar problems, even if through different means. For example, techniques that perform feature selection or dimensionality reduction before or after the graph convolution layers could be relevant. A more comprehensive discussion of the related work would strengthen the paper's position within the existing literature.

### Questions
* To the best of my understanding, I cannot find the reason why the authors state that “it is crucial to maintain the smoothness of deep representations while restricting the feature correlations of the model’s representations” (beginning of page 7). The paper seems to claim that when reducing over-correlation for deeper representations, also over-smoothing will be tackled. In this sense, I cannot see the point in the quoted statement. Would you please elaborate on that?
* Did the authors consider graph-based recommendation approaches which leverage decorrelation in a similar manner to the proposed one (e.g., disentangled graph collaborative filtering, DGCF [1]). In authors’ opinion, what would it be (even intuitively) the effect of performing a double decorrelation if the proposed loss function was applied to DGCF? Would it have a positive or a negative impact, and why?

[1] Xiang Wang, Hongye Jin, An Zhang, Xiangnan He, Tong Xu, Tat-Seng Chua: Disentangled Graph Collaborative Filtering. SIGIR 2020: 1001-1010

**After the rebuttal.** The rebuttal answered all questions.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper analyzes the feature correlation issues in graph collaborative filtering. The author(s) present empirical studies on the smoothness and correlation of each layer of various graph collaborative filtering methods. Then, the author(s) propose AFDGCF that incorporates an auxiliary loss function to explicitly optimize the over-correlation issue. Extensive experiments on four public datasets and four popular GCF backbones show the effectiveness of the proposed method. Code is available and the author(s) promise to release all the code after the reviewing phase.

### Strengths
1. The paper studies an important task, i.e., graph collaborative filtering.
2. The proposed model is implemented by an open-source framework, making it easy to reproduce. Code is available during the reviewing phase.
3. Extensive experiments on four public datasets and four popular GCF backbones show the effectiveness of the proposed method.

### Weaknesses
1. Limited novelty. The paper seems like a straightforward application of existing literature, specifically the DeCorr [1] that focuses on general deep graph neural networks, in a specific application domain. The contribution of this study is mainly the transposition of DeCorr's insights into graph collaborative filtering, with different datasets and backbones. Although modifications like different penalty coefficients for users and items are also proposed, the whole paper still lack enough insights about what are unique challenges of overcorrelation in recommender systems. The core idea of applying a decorrelation penalty to the feature embeddings is not novel in itself, and the paper does not adequately explore the specific nuances of how this affects recommendation performance compared to other domains where similar techniques have been used.

2. It could be better if one additional figure could be illustrated, i.e., how Corr and SMV metrics evolve with the application of additional network layers—mirroring the Figure 2, but explicitly showcasing the effects of the proposed method—the authors could convincingly validate their auxiliary loss function's efficacy. The current presentation makes it difficult to assess whether the proposed auxiliary loss is genuinely addressing the over-correlation issue or simply acting as a regularizer. A direct comparison of the correlation and smoothness metrics before and after applying the proposed loss would strengthen the argument.

3. Presentation issues. The y-axis labels of Figure 2 lack standardization, e.g., 0.26 vs. 0.260 vs. 2600 vs. .2600.

### Questions
According to Theorem 1, there exists a proportional relationship between column correlation and row correlation of a matrix. So whether existing works on alleviating row correlation issues like contrastive learning also solve the correlation issues? Once the row correlation is alleviated, according to the proportional relationship, the column correlation should be alleviated as well. If so, why do we need the proposed auxiliary loss to explicitly alleviate the column correlation issue?

### Soundness
3 good

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors focus on analyzing feature over-correlation in graph-based collaborative filtering, and propose an adaptive feature de-correlation regularization in graph-based collaborative filtering. Column-wise feature over-correlation will introduce redundant information for representation learning, the proposed feature de-correlation regularization can significantly improve the representation quality. Besides, the proposed feature de-correlation is very flexible and lightweight, which can coupled with representation-based CF. Experiments on several benchmarks show the effectiveness of the proposed method.

### Strengths
1. Interesting research topic of this paper, tacking feature over-correlation in collaborative filtering is an effective direction.
2. The proposed feature de-correlation regularization is flexible and effective in graph-based collaborative filtering. De-correlation is helpful in learning more high-quality representation for collaborative filtering.
3. Experiments conducted on several graph-based backbones demonstrate the effectiveness of the proposed de-correlation regularization.

### Weaknesses
1. The motivation of this paper should be highlighted. Why do the authors analyze over-correlation combined with over-smoothing? Does feature over-correlation only occur on graph-based collaborative filtering non other methods such as Matrix Factorization? Specifically, the paper lacks a clear explanation of why over-correlation is a significant problem in graph-based collaborative filtering, and whether it is unique to this approach compared to other collaborative filtering techniques like Matrix Factorization. The authors should provide a more detailed analysis of the underlying mechanisms that lead to over-correlation in GNNs, and why these mechanisms are not as prevalent in other methods.
2. The reason for existing over-correlation in low-dimensional collaborative filtering is not clear. It will be more interesting if the authors deeply explain the behind reasons. Besides, does alleviating over-correlation can help to reduce over-smoothing issues in graph-based collaborative filtering? The authors should give a more explanatory illustration. The paper needs a more in-depth discussion on the causes of over-correlation in low-dimensional spaces within GNN-based CF. Furthermore, it is unclear whether the proposed de-correlation method directly addresses over-smoothing, or if the observed improvements are merely a side effect. A more detailed analysis of the relationship between over-correlation and over-smoothing is needed, possibly with empirical evidence to support the claims.
3. Lacking comparisons of related works, disentangled collaborative filtering should be involved. Besides, column-wise de-correlation can be also viewed as self-supervised learning. The authors should discuss with current self-supervised graph collaborative filtering method[1,2,3,4]. The paper lacks a thorough comparison with existing disentangled collaborative filtering methods, which also aim to learn more independent representations. Additionally, the proposed column-wise de-correlation technique bears similarities to self-supervised learning methods, and the authors should discuss how their approach relates to and differs from current self-supervised graph collaborative filtering techniques. The current comparisons are insufficient to fully contextualize the contribution of the proposed method.

### Questions
Mentioned as the weakness.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper draws attention to the challenges of over-smoothing and over-correlation in GNN-based collaborative filtering methods. In particular, the paper provides a detailed analysis of the over-correlation problem, which has been largely overlooked in existing works. Through rigorous theoretical analysis, the paper establishes a proportional association between the over-smoothing issue and the over-correlation issue, shedding light on their interconnected nature.

To tackle these issues, the paper proposes a model-agnostic constraint with adaptive weights. This constraint is designed to effectively mitigate over-smoothing and over-correlation problems in GNN-based collaborative filtering. The adaptive weights allow the constraint to dynamically adjust and optimize the learning process.

Comprehensive experiments are conducted to validate the effectiveness of the proposed constraint. The results demonstrate significant improvements in overall performance, enhanced training efficiency, and the efficacy of the adaptive approach. These findings provide strong evidence for the practical benefits of the proposed constraint in addressing the over-smoothing and over-correlation challenges in GNN-based collaborative filtering methods.

### Strengths
- The paper highlights the issue of decorrelation in collaborative filtering, which has received little attention in previous works.
- Through a comprehensive theoretical analysis, the paper establishes a clear association between the over-smoothing problem and the decorrelation issue.
- To address the challenges of over-smoothing and decorrelation, the paper proposes an effective solution. The proposed scheme is extensively evaluated through rigorous experiments, demonstrating its effectiveness.
- The paper is well-written and provides clear explanations. It includes illustrative figures and pilot experiments that enhance understanding and readability.

### Weaknesses
 - I have reservations regarding the dataset preprocessing approach employed in the paper. The authors chose to exclude users and items with fewer than 15/10 interactions in some datasets. However, in my experience, this approach has the potential to create highly dense datasets and introduce bias. Specifically, removing low-degree nodes can artificially inflate performance metrics, as the remaining nodes are likely to have stronger connections and thus be easier to predict. This preprocessing step may not accurately reflect real-world scenarios where long-tail distributions are common.
- It would have been beneficial if the paper had explored the recent advancements in self-supervised learning for collaborative filtering, as these techniques have demonstrated superior performance in related studies. The lack of comparison with state-of-the-art self-supervised methods makes it difficult to assess the true novelty and effectiveness of the proposed approach. For example, methods that leverage contrastive learning or graph augmentation techniques could provide a more robust baseline for comparison.

### Questions
I would expect the authors to clarify the two issues mentioned in the weaknesses part.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good
