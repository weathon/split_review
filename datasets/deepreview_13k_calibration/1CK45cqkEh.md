# Unsupervised Order Learning

- Decision: Accept
- Avg Score: 5.50
- Scores: 6, 5, 6, 5

## Abstract
A novel clustering algorithm for orderable data, called unsupervised order learning (UOL), is proposed in this paper. First, we develop the ordered $k$-means to group objects into ordered clusters by reducing the deviation of an object from consecutive clusters. Then, we train a network to construct an embedding space, in which objects are sorted compactly along a chain of line segments, determined by the cluster centroids. We alternate the clustering and the network training until convergence. Moreover, we perform unsupervised rank estimation via a simple nearest neighbor search in the embedding space. Extensive experiments on various orderable datasets demonstrate that UOL provides reliable ordered clustering results and decent rank estimation performances with no supervision. The source codes are available at https://github.com/seon92/UOL.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces an unsupervised method to perform clustering when there exists a total order between clusters. This total order can for instance define the age of people in images, and people who are about the same age tend to be in the same cluster or neighbor clusters. The proposed method is similar to soft clustering in the sense that it assigns samples to different clusters (here, at most 3 clusters) and updates the centroids accordingly. However, it also considers some total order on the centroids.

### Strengths
The paper is well-written and the exposition of the method is clear. The difference with standard clustering algorithms that do not consider orders between clusters, and also with other ranking methods that use supervision is well defined. Assuming that there exists an order between the cluster in the dataset, the motivation for using the proposed method is clear.
As motivated in the paper, the method can be used as a pretraining stage for downstream tasks including ordinal regression, or it can facilitate an initial understanding of data characteristics. However, only the latter part is evaluated in the paper.

### Weaknesses
One main limitation of the method is that it assumes that there exists a total order between the categories/clusters, which is not always the case. The idea of the paper is similar to relative attributes [A] although it considers the unsupervised case. Even with relative attributes, it may be difficult to define a total order between categories so an equivalence between pairs of categories is sometimes defined. Partially ordered sets are in general easier to define than total orders.

Moreover, there might exist different ways to define orders between categories. For instance, in ref [A], the orders between face categories might define age, chubbiness, roundness, color, big lips etc... Fortunately, in Fig 1 (c) of the submission, the face images are ordered by age, but another criterion might have been extracted by the method since it is unsupervised, and the reported scores would not have been as good. It is unclear how the method would behave if the data contained multiple, potentially conflicting, ordering criteria, and how the method would converge to a meaningful solution in such cases. The lack of robustness to multiple ordering criteria is a significant weakness.


### Questions
How important is initialization? Assuming that there exist different possible orders between categories, would one initialization reflect one order (for instance age) and another reflect something else (for instance color)? And in this case, how would the method be useful for real-world applications since there is no way to control the extracted clustering order? In particular, if we consider network pre-training, one initialization would improve performance only if the extracted order aligns with the target order.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents an unsupervised algorithm for clustering ordered data. Specifically, it proposes a so-called ordered k-means algorithm, in which the rules to update the centroids and to find the assignments are modified by adding some reference terms with respect to the previous cluster and the next cluster. Experiments on benchmark datasets are conducted, showing some improvements over the listed baseline algorithms.

### Strengths
+ It sounds interesting to modify the ordinary $k$-means algorithm to handle ordered data clustering. 
+ Experimental results on benchmark datasets show promising improvements.

### Weaknesses
 - The difference from the ordinary $k$-means algorithm is the way to update the mean and the way to assign clustering index, both of the two stages are computed by taking a tradeoff between the current clusters and the socalled previous cluster and the next cluster. However, it is not always meaningful to define the previous cluster and the next cluster, if the dimension of the embedding space  (which is also the dimension of the centriods of the clusters) is larger than 2.

- In Eq. (4), the formula to update the centroids contains a parameter $\alpha$.  From the results in Table 9, the performance is sensitive the parameter $\alpha$. Without the proper value for parameter $\alpha$, the promising performance cannot be obtained.

### Questions
- It seems not always meaningful to define the previous cluster and the next cluster, provided that the dimension of the embedding space (which is also the dimension of the centriods of the clusters) is larger than 2. 

- In Eq. (4), the formula to update the centroids contains a parameter $\alpha$. As can be read from Table 9, the performance of the clustering is very sensitive the value of the parameter $\alpha$. The promising performance cannot be obtained without using the proper value of $\alpha$. Is there any principled rule to set it? Moreover, does the proper value of $\alpha$ vary from dataset to dataset?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a new algorithm, called unsupervised order learning (UOL), for clustering ordered data. It aims to discover hidden ranks (or ordered classes) of objects with no supervision.

### Strengths
1. The author proposes the first deep clustering algorithm for ordered data.

2. The authors have introduced the ordered k-means algorithm, which extends the conventional k-means approach.

3. This enhanced method effectively groups object instances and arranges the resulting clusters in a meaningful order. The authors have also provided a proof of the local optimality of the solution.

### Weaknesses
1. As a clustering method, it is inappropriate and unfair to compare only two types of metrics regarding the order of the data, SRCC and MAE. Some basic clustering metrics, such as ACC and NMI, lack comparison. Also this explains why other comparison algorithms achieve poorer performance. The exclusive focus on order-based metrics neglects the fundamental clustering performance, making it difficult to assess the true effectiveness of the proposed method as a clustering algorithm.

2. We question the value of unsupervised order clustering. The important value of clustering as a classical unsupervised method is that it does not require a tedious data preprocessing process such as labeling data in advance. In contrast, the order clustering proposed by the authors has high requirements for the dataset itself (sequentially), and such requirements are usually obtained by tedious manual sorting, which contradicts the advantages of clustering itself. Can the authors provide a real dataset or scenario where sequential order exists and clustering is required? Note that this is different from the manually ordered dataset used by the authors in the experimental section. The need for a pre-existing sequential order in the data limits the applicability of the method to a narrow set of problems, undermining its claim as a general unsupervised clustering technique.

3. Why did you select only two data sets for your different ablation experiments? Did the authors artificially select the datasets to present the ablation experiments? Meanwhile, the parameter \gamma lacks ablation experiments with relevant parameter descriptions. More experimental results are expected. The limited number of datasets for ablation studies raises concerns about the robustness and generalizability of the findings. The lack of a parameter study for \gamma further weakens the analysis, leaving the reader unsure of its impact on performance.

### Questions
1. As a clustering method, it is inappropriate and unfair to compare only two types of metrics regarding the order of the data, SRCC and MAE. Some basic clustering metrics, such as ACC and NMI, lack comparison. Also this explains why other comparison algorithms achieve poorer performance.

2. We question the value of unsupervised order clustering. The important value of clustering as a classical unsupervised method is that it does not require a tedious data preprocessing process such as labeling data in advance. In contrast, the order clustering proposed by the authors has high requirements for the dataset itself (sequentially), and such requirements are usually obtained by tedious manual sorting, which contradicts the advantages of clustering itself. Can the authors provide a real dataset or scenario where sequential order exists and clustering is required? Note that this is different from the manually ordered dataset used by the authors in the experimental section.

3. Why did you select only two data sets for your different ablation experiments? Did the authors artificially select the datasets to present the ablation experiments? Meanwhile, the parameter \gamma lacks ablation experiments with relevant parameter descriptions. More experimental results are expected

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposed an unsupervised order clustering algorithm for dealing with order data To be specific, authors first proposed a ordered k-means algorithm which defines a measurement of the deviation of sample x from the cluster centroid chain in learned embedding space. Then authors claim that the ordered clustering can be defined as the distance between sample x and its centroid and two neighbored centroids. Based on these, authors proposed an ordered k-means algorithm for clustering ordered data.

### Strengths
This paper is well-written and the core idea and motivation are easy to follow.

### Weaknesses
First, In page 3, authors claimed that “we propose the first unsupervised algorithm for order learning”. Actually, this paper belongs to a kind of ordered data clustering task, which has been studied in many previous works, such as 
[1] An ordinal data clustering algorithm with automated distance learning, AAAI, 2020;
[2] Deep repulsive clustering of ordered data based on order-identity decomposition, ICML, 2020.
Thus, this sentence is not precise.

Second, the deviation of sample x from the chain is borrowed from Lim et al. 2020, thus the true contribution of this paper is the ordered k-means algorithm in Algorithm 1 which is easy to deduce if we have Eq. (1). In a word, I think the true contribution is not enough for ICLR.

Thiredly, in experiments, the compared algorithms mostly are traditional clustering algorithms which can not verify the effectiveness of proposed methods.

In all, I prefer to give the “marginally below the acceptance threshold” decision.

### Questions
N/A

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
