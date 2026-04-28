# Efficient Incomplete Multi-view Clustering via Flexible Anchor Learning

- Decision: Reject
- Avg Score: 3.75
- Scores: 3, 5, 6, 1

## Abstract
Multi-view clustering aims to improve the final performance by taking advantages of complementary and consistent information of all views. In real world, data samples with partially available information are common and the issue regarding the clustering for incomplete multi-view data is inevitably raised. To deal with the partial data with large scales, some fast clustering approaches for incomplete multi-view data have been presented. Despite the significant success, few of these methods pay attention to learning anchors with high quality in a unified framework for incomplete multi-view clustering, while ensuring the scalability for large-scale incomplete datasets. In addition, most existing approaches based on incomplete multi-view clustering ignore to build the relation between anchor graph and similarity matrix in symmetric nonnegative matrix factorization and then directly conduct graph partition based on the anchor graph to reduce the space and time consumption. In this paper, we propose a novel fast incomplete multi-view clustering method for the data with large scales, termed Efficient Incomplete Multi-view clustering via flexible anchor Learning (EIML), where graph construction, anchor learning and graph partition are simultaneously integrated into a unified framework for efficient incomplete multi-view clustering. To be specific, we learn a shared anchor graph to guarantee the consistency among multiple views and employ a adaptive weight coefficient to balance the impact for each view. The relation between anchor graph and similarity matrix in symmetric nonnegative matrix factorization can also be built, i.e., each entry in the anchor graph can characterize the similarity between the anchor and original data sample. We then adopt an alternative algorithm for solving the formulated problem. Experiments conducted on different datasets confirm the superiority of EIML compared with other clustering methods for incomplete multi-view data.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes Efficient Incomplete Multi-View Clustering via Flexible Anchor Learning (EIML), a method designed for clustering incomplete multi-view data at large scales. Specifically, building on traditional anchor learning objectives, EIML directly integrates the graph partitioning function, aiming to fuse graph construction, anchor learning, and graph partitioning into a unified framework.

### Strengths
The paper's motivation and approach of integrating graph construction, anchor learning, and graph partitioning into a unified framework to avoid separate procedures is compelling.

### Weaknesses
The proposed method does not address missing views in a meaningful way, lacking specific techniques for incomplete multi-view clustering. This deviation from the core theme reduces the relevance of the approach to the stated problem of incomplete multi-view data.

The experimental section lacks sufficient comparison methods, with limited engagement with recent advancements in the field. Additionally, the description of datasets is brief and does not adequately highlight the method’s capacity to handle large-scale data.

The illustrations in the paper are of low quality, lacking clarity and depth. They do not effectively convey the core concepts, which may hinder the reader’s understanding of the proposed method.

The layout of the paper is inconsistent, with poor alignment between text descriptions and related figures or tables. This inconsistency disrupts the reading flow and detracts from the paper's overall presentation quality.

### Questions
How does the proposed method address the issue of missing views in multi-view data? Are there specific strategies or mechanisms integrated into the framework to manage incomplete views?

In Figures 4-7, the clustering performance appears to increase despite higher missing rates. Could the authors explain this phenomenon and provide insights into why clustering results improve as missing rates increase?

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes an incomplete multiview clustering method to handle large-scale datasets. Their method is based on two parts, i.e., anchor graph learning and symmetric nonnegative matrix factorization.

### Strengths
1. This paper is easy to read.
2. The experiments are abundant and comprehensive.

### Weaknesses
1. This paper lacks novelty. In fact, anchor graph learning and symmetric nonnegative matrix factorization are two very common methods in multi-view clustering. This paper is an easy combination of these two methods. I think that the quality of this paper does not meet the standards of ICLR.
2. Since the objective function includes the cluster assignment matrix $F$, I think that the initialization may heavily influence the clustering results. The authors should conduct experiments to verify whether the different initializations have different clustering performances.
3. The paper lacks the necessary theoretical explanations, such as a convergence analysis.
4. The resolution of Figure 1 is too low and needs to be adjusted.

### Questions
See "Weaknesses".

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper proposes a novel fast incomplete multi-view clustering method for the data with large scales, termed Efficient Incomplete Multi-view clustering via flexible anchor Learning (EIML), where graph construction, anchor learning and graph partition are simultaneously integrated into a unified framework for efficient incomplete multi-view clustering. To be specific, the authors learn a shared anchor graph to guarantee the consistency among multiple views and employ a adaptive weight coefficient to balance the impact for each view. The relation between anchor graph and similarity matrix in symmetric nonnegative matrix factorization can also be built, i.e., each entry in the anchor graph can characterize the similarity between the anchor and original data sample.

### Strengths
1. Novelty. This paper gives a new insight to the community of incomplete multi-view clustering for large scale datasets, i.e., graph construction, anchor learning and graph partition in efficient incomplete multi-view clustering can boost each other, which are able to be integrated into a problem. The combination of these three issues is the focus in our work. While most existing work treat graph construction, anchor learning and graph partition as separated problems in incomplete multi-view clustering for the datasets with large scales. 

2. Quality and Clarity. There are no technical errors, and the presentation and writing are very clear.

3. Significance. The authors we constrain the factor matrix with rigorous interpretation to be cluster indicator representation by introducing the orthogonal constraint on the actual bases and use the alternative algorithm for solving the formulated problem. Extensive experiments are performed on different datasets to demonstrate the superiority of EIML in terms of effectiveness and efficiency.

### Weaknesses
1. The authors state that each entry in the anchor graph $ Z $ describes the similarity between data sample and anchor. Since the symmetric constraint on $ Z\in R^{m\times n} $ are not guaranteed in factorization with $ m\ll n $, the authors remove such constraint on anchor graph $ Z $ and this is the main difference between anchor graph and similarity matrix in symmetric nonnegative matrix factorization. In this part, the authors are expected to give the reason why each entry in the anchor graph $ Z $ describes the similarity between data sample and anchor.

2. The authors list the detailed clustering results of EIML and the compared approaches on different datasets in terms of four metrics in Tables 1-4. The authors also compare EIML with IMVC-CBG and FIMVC-VIA under different missing ratios on several datasets under different metrics. According to Tables 1-4 and Figs. 4-7, the authors then draw some following conclusions. However, the authors do not bold the best clustering performance in Tables 1-4 in terms of four metrics for this paper. 

3. The authors perform the parameter selection for the trade-off parameter $ \lambda $ in the range of $ [0.001,0.1,1,10,100,1000] $ to study how these this parameter influences the final clustering performance and find that better performance is achieved when $ \lambda=1 $ under the same $ m $ on different datasets. Besides, the clustering result of EIML is relatively stable over different parameter values on these datasets, which shows that EIML is generally robust to the trade-off parameter $ \lambda $. However, the authors do not give the detailed reason why the $ [0.001,0.1,1,10,100,1000] $ is chosen for parameter selection in this paper.

4. The authors perform ablation study to validate the superiority of adopting a unified framework integrated by graph construction, anchor learning and graph partition. In comparative experiments, the authors first learn anchors and construct the graph to obtain informative representation. Then the graph partition is isolated from the above two processes in the designed experiment. However, the authors do not give the detailed specific values analysis regarding the superiority of adopting a unified framework integrated by graph construction, anchor learning and graph partition.

### Questions
1. The authors conduct convergence analysis of EIML on different datasets by showing the evolution process of the objective function with iterations in terms of ACC and observe that EIML monotonically decreases with iterations and tends to converge in about some iterations on these datasets. Here, how many iterations are needed for the proposed EIML in reaching convergence?

2. The authors show the running time of EIML and the compared approaches on different benchmark datasets in Table 5. However, the authors do not give the memory description of the used device. What is the memory value of the used device?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
The topic of this paper is incomplete multi-view anchor graph clustering. It combines existing methods for graph construction, anchor learning, and graph partitioning into a unified formulation. However, its contribution appears quite limited.

### Strengths
1. This paper combines the graph construction, anchor learning, and graph partition in a unified form.
2. The research topic that incomplete data learning is meanful.

### Weaknesses
1.This paper is a modification of previous work published in CVPR (https://ieeexplore.ieee.org/document/9880247). It lacks any novel insights into incomplete multi-view anchor graph clustering, which limits its contribution. Based on this, I do not believe it is suitable for acceptance at ICLR.

2.The construction of the incomplete anchor graph follows the approach in the aforementioned work, and the graph partition method (matrix factorization) is also a similar method in TIP-21(https://ieeexplore.ieee.org/abstract/document/9305974). The paper does not offer any significant new ideas or contributions.

3.Incomplete anchor graph clustering is not a novel topic and has been extensively studied. Consequently, the significance of this paper's contribution appears minimal.

4.The paper does not compare its results with any deep learning-based baselines for incomplete data, which limits the assessment of its effectiveness.

5.The optimization method used is alternative optimization, no new techniques or improvements are proposed.

6.The experiments conducted are quite common and fail to deliver any particularly exciting results.

### Questions
In addition to the weaknesses highlighted, there are a few more concerns:

1. The paper claims to use nonnegative matrix factorization; however, it appears to be a general matrix factorization method. It is mistaken.

2. What are the novel insights in this work compared to those in CVPR-22 and TIP-21?

3. How does the method perform on large-scale datasets? The datasets used in this study are relatively limited in size.

4. Why is DAIMC unable to handle the smaller WebKB dataset but can handle the larger CIFAR-100 dataset?

5. The baseline comparisons should be updated to include more recent methods for a fairer assessment.

### Soundness
2

### Presentation
1

### Contribution
1
