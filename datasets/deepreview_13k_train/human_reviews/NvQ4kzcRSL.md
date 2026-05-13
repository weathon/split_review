# Graph Clustering with Masked AutoEncoders

- Decision: Reject
- Scores: 3, 3, 3, 5, 5

## Abstract
Graph clustering algorithms with autoencoder structures have recently gained popularity due to their efficient performance and low training cost. However, for existing graph autoencoder clustering algorithms based on GCN or GAT, not only do they lack good generalization ability, but also the number of clusters clustered by such autoencoder models is difficult to determine automatically. To solve this problem, we propose a new framework called \textit{G}raph \textit{C}lustering with \textit{M}asked \textit{A}utoencoders (\textit{GCMA}). It employs our designed fusion autoencoder based on the graph masking method for the fusion coding of graph. It introduces our improved density-based clustering algorithm as a second decoder while decoding with multi-target reconstruction. By decoding the mask embedding, our model can capture more generalized and comprehensive knowledge. The number of clusters and clustering results can be output end-to-end while improving the generalization ability. As a nonparametric class method, extensive experiments demonstrate the superiority of \textit{GCMA} over state-of-the-art baselines.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper presents GCMA, a framework addressing challenges in graph clustering, specifically generalization and automatic cluster number determination. GCMA utilizes a fusion autoencoder based on graph masking for encoding, combined with an improved density-based clustering algorithm as a secondary decoder. This allows the model to capture more generalized knowledge by decoding mask embeddings. The work emphasizes the importance of determining the correct number of clusters in unsupervised learning and highlights issues with existing methods that overemphasize proximity in graph structures. The authors introduce the graph masking autoencoder to clustering tasks, offering enhanced generalization and interpretability, and through extensive experiments, demonstrate its superiority over existing methods

### Strengths
1.  The research problem is significant, as node clustering is a fundamental topic in the graph learning domain. 
2. Overall, the paper is well-structured and well-motivated. 
3. Extensive baselines are compared in the experimental section.

### Weaknesses
1.  The technique novelty is limited.  As they claimed in the introduction, the main contribution of this paper is the usage of graph masking autoencoder for clustering analysis. However, this technique has been well studied in self-supervised learning on graphs/ pretrain models on graphs.  It is not clear why the model can improve the generalization ability.  Another important technique,  density-based clustering algorithm, has also been well-studied in both graph and non-graph domains.

2. Some important claims are not well verified. It claims that the model has better generalization ability. They conduct experiments on noisy/incomplete datasets to verify these claims.  This is confusing.  It is more like robustness instead of generalization.  It is not clear why the model has better interpretability.  

3. Some experiments are confusing. For example,  "but both NMI and ARI values are significantly decreased. This means that the interpretability and generalization performance of the results decreased."  How to infer interpretability and generalization from NMI and ARI  are not clear.  From table 3, GCMA is better than GCMA-A in COra. However, the visualization results in Figure 5 show that GCMA-A is better. There is no explanation or description of that. 

4. The presentation is messy, especially table 4 to table 8.

### Questions
Please check the weaknesses.

### Soundness
3 good

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This article proposes an unsupervised method for graph clustering based on Graph Masked AutoEncoder. The motivation behind this work is that existing methods struggle to automatically select the number of clusters and lack good generalization ability. To address this issue, the paper introduces a density-based clustering algorithm as the Decoder module. The proposed approach can end-to-end select the number of clusters while improving generalization performance. Extensive experiments demonstrate the effectiveness of the proposed method.

### Strengths
- This article addresses a significant drawback of previous graph clustering algorithms, which is the need to pre-determine the number of clusters.

### Weaknesses
 -**Writing Quality**: The writing quality of this article needs improvement. The language used in the article feels difficult to understand. Additionally, the quality of some of the figures, such as Figure 1, could be enhanced.

-**Method is not clearly presented**:  The introduction of the proposed method in this article is quite unclear. For instance, in Section 3.2.2, the authors abruptly introduce a new concept, CFSFDP, making it challenging for readers unfamiliar with this concept to grasp the purpose of this section. It seems that the authors did not effectively emphasize the main focus of this paper. In my view, since Masked Graph Autoencoders are already established content, the author's primary contribution should lie in the clustering part. However, the authors dedicate a significant amount of content to the introduction of Graph masking and AutoEncoder, which, in my opinion, is unnecessary. While the authors provide Algorithm 1 as a summary of the entire model, this algorithm appears overly concise. Furthermore, in Equation (3), the authors propose using mutual information to calculate the loss. However, I fail to discern the connection between Equation (3) and Equation (4) with mutual information.

-**Rationality for the designs**: Some of the designs proposed in this paper appear to rely heavily on intuition, and certain claims lack robust supporting evidence. For example, in Section 3.1.1, it is not clear why masking both modal information at the same time is considered harmful. In Section 3.1.2, the reasoning behind why a graph autoencoder would overemphasize proximity information needs further explanation. In 3.2.1, the motivation behind adding a mask to Z_m is not well-justified.  I hope the authors can provide their own analysis rather than simply following others' claims.

### Questions
Most of my questions have been presented in the Weaknesses.

### Soundness
2 fair

### Presentation
1 poor

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
In this paper, the authors propose Graph Clustering with Masked Autoencoders (GCMA). They claim three different contributions: 
1. the first method to determine the number of clusters specifically for graph data.
2. using the mask graph mechanism allows learned representations to be applied to multiple types of downstream tasks
3. Extensive experiments on five datasets demonstrate that our model outperforms existing state-of-the-art baselines.

### Strengths
Sorry, I really cannot get significant strengths.

### Weaknesses
Originality:
     The whole method is based on GraphMAE (or modified version). The core modification, the "CFSFDP DECODER", is not novel, as the authors themselves acknowledge its prior existence. The adaptation of CFSFDP, while potentially useful, does not constitute a significant departure from existing techniques.
Novelty:
    The novelty remains a concern. The paper combines self-supervised learning on graphs with a clustering-specific loss, but it lacks a direct comparison with standard self-supervised learning approaches on graphs. This makes it difficult to assess the true contribution of the proposed method beyond simply applying a clustering loss to learned embeddings. The absence of experiments isolating the impact of the clustering loss is a significant oversight.
Performance:
    The performance comparison is limited. The paper compares against older graph clustering methods and general clustering methods, rather than focusing on state-of-the-art graph-based methods. The claim of outperforming existing state-of-the-art baselines is not convincingly supported by the experimental results presented. The method's performance appears fair, but it does not demonstrate a clear advantage over more recent graph convolution-only methods, such as NAFS: A Simple yet Tough-to-beat Baseline for Graph Representation Learning.

### Questions
I have no question. But I am still open to observing how the authors convince all reviewers.

### Soundness
3 good

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a new framework called Graph Clustering with Masked Autoencoders, i.e., GCMA, for unsupervised graph clustering. GCMA employs a fusion autoencoder based on graph masking and an improved density-based clustering algorithm to improve the generalization ability of graph autoencoder clustering algorithms. One advantage of the proposed model is that it can automatically determine the number of clusters k. The authors demonstrate that GCMA can outperform other graph clustering baselines on citation graphs.

### Strengths
1. The paper provides a clear introduction to the problem of unsupervised graph clustering and the motivation for the proposed model.

2. A detailed explanation of the fusion autoencoder based on graph masking used in GCMA.

3. GCMA can automatically determine the number of clusters k.

### Weaknesses
1. The novelty contribution is incremental. This paper applies graph MAE for graph clustering. However, MAE is well-known and graph MAE has been used for various graph tasks, the idea is not novel.  

2. The method description is not entirely clear. As a major difference from the parametric baselines, automatically determine k is a claimed advantage, but how it can be done is not clear from the current writing.

3. Empirical evaluation is not sufficient. Only citation graphs are considered. Does the proposed method also work for other types of graphs?

### Questions
1. For Table 3, are the ground truth k used as input for the parametric algorithms? 

2. How do the non-parametric methods perform in terms of those metrics in Table 3, e.g., ACC, NMI, and ARI? 

3. In section 3.2.2, how exactly was k generated? The paper says "Thus the clustering center can be clearly separated from the rest of the data points to get the best k value". The authors may illustrate more.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the problem of graph clustering and proposes a new framework named Graph Clustering with Masked Autoencoders (GCMA). It involves a graph masking into an auto-encoder framework. Extensive experiments demonstrate the superiority of GCMA over state-of-the-art baselines.

### Strengths
- This paper studies a practical problem.
- The main idea of the paper is simple and intuitive.
- The proposed method achieves superior performance on various datasets for different benchmark tasks.

### Weaknesses
 - The evaluation is not sufficient. The method only involves one large-scale datasets, i.e., Ogbn-arxiv, which is not sufficient to support the claim.
- More result analysis should be included in Sec. 4.4. 
- There are some missing prior works about graph clustering in 2022-2023, e.g., [1], which should be included in performance comparison. 
- It seems that your self-optimization modules is similar to Deep Embedding Clustering, which should be discussed.  

### Questions
See weakness.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
