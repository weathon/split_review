# Village-Net clustering: A novel unsupervised manifold clustering method

- Decision: Reject
- Avg Score: 3.80
- Scores: 3, 5, 3, 5, 3

## Abstract
We present "Village-Net Clustering," a novel unsupervised clustering algorithm designed for effectively clustering complex manifold data. The algorithm operates in two primary phases: first, utilizing K-Means clustering, it divides the dataset into distinct "villages." Subsequently, a weighted network is created, where each node represents a village, capturing their proximity relationships. To attain the optimal clustering, we cluster this network using the Walk-likelihood Community Finder (WLCF), a community detection algorithm developed by one of our team members. An important feature of Village-Net Clustering is its ability to autonomously determine the optimal number of cluster. Extensive benchmarking on real datasets with known ground-truth labels showcases its competitive performance, particularly in terms of the normalized mutual information (NMI) score, when compared to state-of-the-art methods. Additionally, the algorithm demonstrates impressive computational efficiency, boasting a time complexity of O(N*k*d), where N signifies the number of instances, k represents the number of villages and d represents the dimension of the dataset, making it well-suited for effectively handling large-scale datasets.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces an unsupervised clustering algorithm called "Village-Net Clustering" for effectively clustering complex manifold data. The algorithm consists of two main phases: first, it uses K-Means clustering to divide the dataset into distinct "villages", and then it creates a weighted network where each node represents a village, capturing their proximity relationships. To achieve optimal clustering, the network is clustered using the Walk-likelihood Community Finder (WLCF) algorithm. Experiments on real datasets show that the Village-Net Clustering algorithm possesses certain advantages in terms of clustering performance and computational efficiency.

### Strengths
1. This article introduces some new ideas. Firstly, it uses K-Means to construct coarse-grained "villages" for the raw dataset, and then redefines a distance calculation method between these villages.
2. High algorithm efficiency: VillageNet clustering has lower computational complexity, making it suitable for processing datasets of different scales and dimensions.
3. Ability to handle non-convex clustering structures: VillageNet clustering can handle datasets with non-convex clustering structures, capturing complex structures within the dataset.

### Weaknesses
1. Dependency on K-Means Clustering: The first step of the VillageNet clustering method involves using the K-Means clustering algorithm to create initial "villages." Therefore, the performance and results of K-Means clustering have a certain dependency. This dependency is a significant concern because K-Means is sensitive to initialization and can converge to local optima. The quality of these initial villages directly impacts the subsequent network construction and final clustering results. If K-Means fails to produce meaningful initial clusters, the entire VillageNet algorithm is likely to underperform.

2. Assumption about Data Distribution: VillageNet clustering assumes the presence of some local clustering structures within the dataset, and that these local structures can be successfully separated by the K-Means clustering algorithm. This assumption may not hold suit for most datasets, leading to inaccurate clustering results. Datasets with overlapping clusters or complex manifold structures might not be well-suited for initial separation by K-Means. The algorithm's reliance on this assumption limits its applicability to a specific type of data distribution, and it is not clear how the algorithm would perform on datasets that violate this assumption.

3. Lack of More Experimental Validation: The algorithm was only compared with a few traditional clustering algorithms, and the experimental results indicate that the proposed algorithm performs well only on two datasets. Therefore, it is difficult to demonstrate that the proposed algorithm exhibits competitive performance. The lack of comparisons with more state-of-the-art clustering algorithms, especially those designed for manifold data, makes it difficult to assess the true novelty and effectiveness of the proposed method. The limited number of datasets used in the experiments also raises concerns about the generalizability of the results.

4. The evaluation metrics for the experimental results are too narrow. The author solely relies on NMI as the sole measure. Relying solely on NMI is insufficient to fully evaluate the performance of a clustering algorithm. Other metrics, such as Adjusted Rand Index (ARI), Fowlkes-Mallows Index (FMI), and silhouette score, should also be considered to provide a more comprehensive assessment of the clustering quality. The absence of these metrics makes it difficult to understand the strengths and weaknesses of the proposed algorithm.

### Questions
1. I consider Equation 5 is the distance calculation formula that the author has redefined between villages. I would like the author to clarify whether this calculation method satisfies the conditions for distance definition.
2. The experimental section lacks an analysis of the hyperparameter "r".
3. WLCF is one of the crucial steps in the algorithm. However, the author's description of WLCF is not sufficiently clear. Additionally, during the experimental process, I would like to see some ablation experiments to verify the impact of each step in the algorithm on the final clustering results.
4. I suggest that the author perform visual analysis on some artificial non- convex datasets (such as Two Moon, Flower, etc.) and visualize each step of the algorithm to illustrate the effectiveness of the proposed algorithm.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this work, the authors propose an unsupervised clustering method, Village-Net Clustering, whose core idea is to divide the dataset into multiple "villages" by K-Means algorithm, and then construct a weighted network among these "villages". Finally, the Walk-likelihood Community Finder (WLCF) algorithm is utilized to cluster the network, thus realizing the clustering of the original data.  The authors implemented experimental comparisons to demonstrate that the method achieves impressive computational efficiency on multiple datasets. The authors employ suitable methods and pose a clear research question.

### Strengths
The author describes the fundamental algorithm well; and they seem to give all relevant information to understand and reproduce their algorithm. 

The paper outlines a novel clustering method which is capable of clustering complex manifold data. 

Writing and presentation skill is well.

### Weaknesses
1.Where is the title of unsupervised manifold clustering reflected in the manuscript? The authors should have explicitly described what is innovative about Village-Net. The core novelty of the method, particularly in the context of manifold clustering, is not clearly articulated. It's unclear how the 'village' concept specifically addresses the challenges of clustering data residing on complex, non-linear manifolds. The manuscript needs to highlight the unique aspects of Village-Net that differentiate it from existing manifold clustering techniques.
2.The authors should consider collecting more publicly available data to confirm the validity of their Village-Net Clustering. The experimental validation is limited by the number of datasets used. Expanding the range of datasets, especially those known for complex manifold structures, would significantly strengthen the empirical support for the proposed method. The current selection of datasets might not fully capture the diverse challenges of manifold clustering.
3.The authors did not compare their method with latest state-of-the-art methods. They may need to compare Village-Net with other unsupervised manifold clustering methods. The lack of comparison with recent, state-of-the-art unsupervised manifold clustering algorithms is a significant weakness. Without such comparisons, it's difficult to assess the true performance and competitiveness of Village-Net. The manuscript needs to demonstrate how Village-Net fares against the current best-performing methods in the field.

### Questions
Major Concerns:
1.Where is the title of unsupervised manifold clustering reflected in the manuscript? The authors should have explicitly described what is innovative about Village-Net.
2.The authors should have discussed the effect on the model of the choice of the hyperparameter r. r is a key parameter in Village-Net, and the clustering effect is highly dependent on r. However, the manuscript does not provide any details on how to choose r.
3.The authors should consider collecting more publicly available data to confirm the validity of the Village-Net Clustering. 
4.The authors mention Village-Net clustering outperformed other algorithms on the FMNIST and Letters and is the second best in all the other datasets. The manuscript only use NMI to evaluate the clustering, and also need to consider more evaluation metrics on the performance comparison is more persuasive. 
5.The authors may need to compare Village-Net with other unsupervised manifold clustering methods.
6.How to improve the model generalization ability? For different datasets, the hyperparameter k needs to be adjusted individually to obtain superior results, indicating poor model generalization ability.

Minor Concerns:
1.How to divide a network of villages into disjoint village communities using WLCF? Please describe the WLCF algorithm in detail.
2.Please check that the formula symbols in the manuscript are correct. For example, Page 3 Formula (4).
3.Please check that punctuation is used correctly in the manuscript. For example, Page 1 line 1 ”Village-Net Clustering,” should be changed to “Village-Net Clustering”.
4.Page 4 line 9, “T-SNE” should be changed to “t-SNE”.
5.Page 5 line 12, “O(N ∗ k)” should be changed to “O(N ∗ k)”.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors proposed a clustering method. It first overclusters the data points into initial small clusters (village), then builds a graph on the villages, and finally applies an existing community detection methods to obtain the final clustering. Experiments show the effectiveness of the proposed method. 

The authors violated the double blind rule. For instance, it is mentioned in Page 2 that the idea is inspired by their previous work, MapperPlus and WLCF is developed by one of the authors.

### Strengths
1. The proposed method seems to be accurate and efficient in practice.

### Weaknesses
1. The contribution of the paper is not so clear. The idea of over-clustering + merging is not new, which can be find in many previous methods, like BIRCH.
2. The proposed method is a combination of different techniques, but it is not clear why this combination is unique and which specific unsolved problem it can handle. Specifically, the paper lacks a clear explanation of how the village construction and graph-based merging stages interact to overcome limitations of existing methods. It is not clear what kind of data this approach is particularly suited for, or what the limitations of the approach are.
3. The comparison methods are weak, only K-means and DBSCAN.
4. The performance of the proposed method strongly depend on K-means and hyper-parameters. The paper does not provide a sensitivity analysis on the hyper-parameters, nor does it give a clear guideline on how to select those hyper-parameters. The reliance on K-means for initial clustering makes the method susceptible to the known limitations of K-means, such as sensitivity to initial centroid selection and difficulty with non-convex clusters.
5. The authors violated the double blind rule.

### Questions
See above weakness.

### Soundness
3 good

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The main contribution of this paper is that it proposed a clustering algorithm named Village-Net Clustering, which aims to address the challenge of clustering datasets with non-convex cluster structures while maintaining computational efficiency and scalability. The algorithm is executed in four steps: K-Means initialization, construction of a weighted villages network, partitioning the network of villages into disjoint communities, and final clustering.

### Strengths
1. This paper is well-written and easy to follow. 
2. The proposed algorithm is technically sound. 
3. The algorithm flow in this paper (Figure 1) is vivid and clear.

### Weaknesses
1. The novelty of this work is relatively limited, and it seems that only the construction of a village network is proposed in this paper. While the Village-Net Clustering algorithm introduces a new approach, the core concept of constructing a network-based representation for clustering is not entirely unique. The specific implementation of the village network, particularly the criteria for edge creation and weighting, should be more thoroughly compared and contrasted with existing graph-based clustering methods. For example, how does the village network differ from methods that utilize k-nearest neighbor graphs or shared nearest neighbor graphs? A more detailed analysis highlighting the unique aspects of the village network construction would strengthen the claim of novelty.

2. The comparison algorithms used in the experimental part are few, and all of them are early clustering algorithms, so the comparison experiments with the clustering algorithms in recent years should be added. The paper would benefit from a more comprehensive evaluation against a wider range of state-of-the-art clustering algorithms, including more recent methods. This would provide a more accurate assessment of the proposed algorithm's performance and its advantages over existing techniques. Specifically, the inclusion of algorithms designed for non-convex cluster structures would be particularly relevant.

3. According to the part of the effect of hyperparameters in this paper, the algorithm is affected by k and r, but there is no strategy to analyze the selection of hyperparameters, and r is fixed at 20 in the experiment part, and comparative experiments for hyperparameter analysis should be added. The paper acknowledges the influence of hyperparameters k (number of villages) and r (radius for village construction) on the algorithm's performance. However, it lacks a systematic approach for selecting optimal values for these parameters. The fixed value of r=20 used in the experiments raises concerns about the generalizability of the results. A more thorough investigation into the impact of varying k and r across different datasets, along with a discussion of strategies for selecting appropriate values, is needed. This could involve exploring techniques like sensitivity analysis or automated hyperparameter optimization.

### Questions
1. Compared with recent clustering algorithms, is the performance of the proposed algorithm still better?
2. The values of k and r have a great influence on the clustering performance. How to determine the values of hyperparameters for a new data set?
3. Can the convergence of the proposed algorithm be proved theoretically?
4. When evaluating the performance of the algorithm, Table 2 only takes NMI as an evaluation index. Can the author verify the effectiveness of the proposed algorithm under more evaluation indexes?
5. This paper uses the k-means algorithm for initialization. If the number of class clusters in the data set is large, such as greater than 100 or 1000, is this algorithm applicable?

### Soundness
1 poor

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper presents a clustering method that is based on overclustering (using k-means) followed by aggregation of the inital subclusters (called villages). Subcluster aggregation is performed by first computing a similarity measure between pairs of subclusters that measures how the extension of  the first cluster creates overlap with the second cluster. The similarity matrix is then employed by the Walk Likelihood Community Finder algorithm (WLCF) that essentially provides the final clusters.

### Strengths
The definition of the similarity measure A_{UV} between subclusters U and V seems novel and interesting, however it includes a hyperparameter.

### Weaknesses
 - The method depends on hyperparameters: initial number of clusters k and and parameter r that establishes the neighborhood of each subcluster.
- It is not clear whether the method estimates the final number of clusters or the number of clusters is given as input to the method.
- Experimental part is weak and could be improved (see questions below).


### Questions
1) If the method estimates the number of clusters, then results should be provided on how close are the estimations to the actual values.
2) Since the similarity matrix is computed, typical agglomerative approaches (eg. single linkage) or spectral clustering methods could have been used instead of the WLCF algorithm. What is the advantage of WLCF? 
3) Several approaches based on overclustering and cluster aggregation have been proposed. Some of them could have been used in the experimental study.
4) A short presentation of the WLCF method should be included. Does this method contain hyperparameters? What is the theoretical complexity (not the empirical complexity) of the method? 
5) The number of attributes in Pendigits dataset is not 64 but 16.
6) Experiments using additional datasets could have been be included to draw more reliable conclusions on the performance of the method.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
