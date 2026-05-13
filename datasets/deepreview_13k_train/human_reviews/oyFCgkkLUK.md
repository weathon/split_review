# αMax-B-CUBED: A Supervised Metric for Addressing Completeness and Uncertainty in Cluster Evaluation

- Decision: Reject
- Scores: 8, 3, 5, 3

## Abstract
Assessing the quality of clustering results is a crucial and challenging task. The B-CUBED ($B^3$) precision and recall evaluation metric has gained popularity due to its ability to meet four formal constraints: homogeneity, completeness, rag bag, and size vs. quantity. However, the 'completeness' constraint, which demands that items of the same category be grouped in the same cluster, can pose problems for finer clustering algorithms that identify sub-clusters within clusters. This issue is particularly pronounced when the available labels are imprecise and coarse, resulting in uncertain and fuzzy cluster evaluations. To address this issue, we propose a modified evaluation metric called $\alpha$Max-$B^3$. Our approach accounts for completeness and uncertainty in subgroup evaluation by reorganizing clusters into super-sets based on the most prevalent label and evaluating them alongside the original clusters using a modified weighted $B^3$ metric. The extent of uncertainty, given by $1-\alpha$, can be either explicitly specified or automatically estimated.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents a metric for clustering evaluation based on the earlier B-cube clustering evaluation metric. The new metric addresses a weakness in evaluating the completeness constraint. The B-cube metric favours larger clusters although practically, an algorithm making smaller size clusters may be preferred. The new metric also accounts for imbalanced data sets. By setting the value of uncertainty, it can be controlled whether sub-groups of a cluster are required or not. If not, the measure gives the same results as b-cube

### Strengths
The paper is well written, and the proposed measure has a sound mathematical background. The authors have clearly described the case where the original metric may be problematic and have thus built a case for their metric

### Weaknesses
The paper contributes by suggesting an improvement in the original metric. The authors provide a sound background for their work. However, it is not clear how significant this improvement is practically, since they have used a very small set of clusters as the ground truth, and a very short experimental results section.



### Questions
1) Sections 5.1 & 5.2 could have provided more detail about the results. 

2) A very small sized ground truth dataset with 5 clusters has been used. The authors state that when k<=5, b-cube and the new proposed metric give the same results. Why wasn't a larger dataset used

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The extrinsic B-CUBED metric (precision, recall, and the F-score) is one of the most common clustering evaluation metric. However, this metric does not work well for unbalanced datasets and implicitly assumes that the labels are correct and there are no (relevant) sub-clusters inside groups of equally labeled objects. To address the above issues, the author provides a more fair evaluation metric that is applicable to unbalanced datasets and datasets with uncertain labels. The effectiveness of the proposed metric was verified by clustering experiments on artificial datasets.

### Strengths
The authors provide a new extrinsic clustering evaluation metric that can be applied to unbalanced datasets and labeled uncertain datasets.

### Weaknesses
 The authors provide a new extrinsic evaluation metric for clustering methods that is innovative. However, the paper evaluates the proposed metric using clustering results of k-means for a special artificial dataset, and the results only show higher values compared to the existing B-CUBED metric, and do not demonstrate the advantages of the proposed metrics. A good metric should be able to discover the true structure of the data more accurately in real data experiments compared to existing metrics, and the paper's experiments do not verify this point. Meanwhile, the explanation of notation on the key formula (8) is not clear, leading to difficulties in understanding the evaluation metrics. There are the following minor problems:
(1)	The references of the paper are too old and lack research on the latest work.
(2)	There are some minor errors in the paper, please check carefully, such as in Proposition 1, the formula is missing half a bracket.

### Questions
The author should experimentally verify that the proposed evaluation metric has obvious advantages compared with existing evaluation metrics. If two metrics have a positive correlation, for example, both are large and both are small, it does not indicate the advantage of the proposed metric.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, a Max-algorithm is proposed to solve the problems of ambiguity and uncertainty in labels. Max-algorithm considers the completeness and uncertainty of subgroup evaluation. The results show that the method is suitable for subgroup uncertainty in basic labels and can be extended to unbalanced data sets. Compared to technology, the Max-algorithm can produce more robust and fair results and adapt to label uncertainties.

### Strengths
1. The proposed method is an extension of the clustering evaluation index and has a positive effect in this field.
2. The proposed method is sound technically. 
3. The theoretical foundation seems to be relatively sufficient.

### Weaknesses
1. This work is not innovative enough and the writing storyline is average.
2. The comparison algorithms used in the experimental part are few, only one has been mentioned. And the comparison experiments with more clustering measures should be added.
3. The results of this paper are not presented well, and Figure 3 is very rough.
4. In this paper, all other theorems and corollaries are proved, but Corollary 1 is not.
5. The only comparative evaluation index is B3. Are there no other similar evaluation indexes?
6. In Figure 3, only the left picture is introduced, and the right subgraphs are not introduced for specific. It is not clear whether this subgraph is the result of B3 or M-B3. After all, in Figure 2 maxB3 is not marked with a yellow circle. It is best to unify the format of all clustering subgraphs. Also, in the top left plot of Figure 3, B3 looks like there is no result in a cluster number of 1-4. It turns out that the results overlap. You need to re-adjust the color of the image to make the results more obvious.
7. In the last paragraph of the introduction, it is recommended that the author explain the effectiveness of the proposed method.
8. Should the uncertainty of labels be tested with different types of noise? It is recommended that the author increase the type of label noise to make the method proposed in this article more convincing.

### Questions
1. In this paper, all other theorems and corollaries are proved, but Corollary 1 is not.
2. The only comparative evaluation index is B3. Are there no other similar evaluation indexes?
3. In Figure 3, only the left picture is introduced, and the right subgraphs are not introduced for specific. It is not clear whether this subgraph is the result of B3 or M-B3. After all, in Figure 2 maxB3 is not marked with a yellow circle. It is best to unify the format of all clustering subgraphs. Also, in the top left plot of Figure 3, B3 looks like there is no result in a cluster number of 1-4. It turns out that the results overlap. You need to re-adjust the color of the image to make the results more obvious.
5. In the last paragraph of the introduction, it is recommended that the author explain the effectiveness of the proposed method.
6. Should the uncertainty of labels be tested with different types of noise? It is recommended that the author increase the type of label noise to make the method proposed in this article more convincing.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper proposes an extension of a supervised (external) cluster evaluation measure called B-CUBED (B^3). The extension, called aMax-B^3, incoropates a parameter a specifying the uncertainty related to the existence of sub-clusters within the clusters of a ground truth class. 
It is also claimed that the proposed measure is more robust and fair in the case of imbalanced datasets.

### Strengths
-The proposed measure seems to be a novel extension of B^3 measure for supervised cluster evaluation.
-The paper includes some theoretical proofs.

### Weaknesses
 - The paper lacks considerably in terms of presentation and clarity (see questions below).
- B^3 is not a widely used measure in the clustering literature (such as NMI for example).
- The experimental part is weak and does not involve real datasets.
- The proposed measure could have been compared not only with B^3 but also with other measures (e.g. NMI).

- Presentation of the essential part of the approach in pages 5 and 6 is poor and hard to follow. There are several incomplete sentences and the use of indices i, j and k causes a lot of confusion. For example in eq. (5), \eta^[j]=|C_j|/|S_i| seems to depend also on i.
- Before section 4.1 it is mentioned that "the final F_\beta score is", but F_b is not presented afterwards.
- It is not clear how \alpha is computed or estimated. This is a major issue in the paper.
- The results in Figure 2 and 3 need a much better explanation.
- In the plot of Figure 3 the x-axis corresponds to number of clusters, while in the legend it is mentioned that corresponds to cluster size.
- Experiments with real datasets would add value to the paper. Also it would be interesting to show how other measures such as NMI compare to the proposed measure.

### Questions
1) Presentation of the essential part of the approach in pages 5 and 6 is poor and hard to follow. There are several incomplete sentences and the use of indices i, j and k causes a lot of confusion. For example in eq. (5), \eta^[j]=|C_j|/|S_i| seems to depend also on i.
2) Before section 4.1 it is mentioned that "the final F_\beta score is", but F_b is not presented afterwards.
3) It is not clear how \alpha is computed or estimated. This is a major issue in the paper.
4) The results in Figure 2 and 3 need a much better explanation.
5) In the plot of Figure 3 the x-axis corresponds to number of clusters, while in the legend it is mentioned that corresponds to cluster size.
6) Experiments with real datasets would add value to the paper. Also it would be interesting to show how other measures such as NMI compare to the proposed measure.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair
