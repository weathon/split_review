# Understanding Heterophily for Graph Neural Networks

- Decision: Reject
- Avg Score: 5.80
- Scores: 8, 6, 3, 6, 6

## Abstract
Graphs with heterophily have been regarded as challenging scenarios for Graph Neural Networks (GNNs), where nodes are connected with dissimilar neighbors through various patterns.
In this paper, we present theoretical understandings of heterophily for GNNs by incorporating the graph convolution (GC) operations into fully connected networks via the proposed Heterophilous Stochastic Block Models (HSBM), a general random graph model that can accommodate diverse heterophily patterns.
Our theoretical investigation comprehensively analyze the impact of heterophily from three critical aspects.
Firstly, for the impact of different heterophily patterns, we show that the separability gains are determined by two factors, i.e., the Euclidean distance of the neighborhood distributions and $\sqrt{\mathbb{E}\left[\operatorname{deg}\right]}$, where $\mathbb{E}\left[\operatorname{deg}\right]$ is the averaged node degree.
Secondly, we show that the neighborhood inconsistency has a detrimental impact on separability, which is similar to degrading $\mathbb{E}\left[\operatorname{deg}\right]$ by a specific factor.
Finally, for the impact of stacking multiple layers, we show that the separability gains are determined by the normalized distance of the $l$-powered neighborhood distributions, indicating that nodes still possess separability in various regimes, even when over-smoothing occurs.
Extensive experiments on both synthetic and real-world data verify the effectiveness of our theory.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents theoretical understandings of the impacts of different heterophily patterns for GNNs by incorporating the graph convolution (GC) operations into fully connected networks via the proposed Heterophilous Stochastic Block Models (HSBM).

### Strengths
Good paper with high originality and high quality. The paper is well-written and makes some new contributions to the relevant field.

### Weaknesses
More large-scale datasets are suggested to be added.

### Questions
I do not have any questions.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper focuses on understanding the heterophily patterns for Graph Neural Networks (GNNs). It proposes an HSBM graph generation model to generate diverse heterophilious patterns and then analyzes the relationship with the performance of GNN and MLPs.

### Strengths
The paper provides a detailed analysis of GNNs using the HSBM graph generation model. The theoretical analysis and empirical evaluations demonstrate the effectiveness of the analysis.

### Weaknesses
1. The paper lacks comparisons with existing methods. Previous methods [1,2] have provided analysis on heterophily from the perspective of node degree and neighborhood distribution. It would be beneficial to include discussions and comparisons from the standpoint of assumptions, graph generation, and results.

2. The paper does not provide suggestions for learning on heterophilous graphs. The analysis of heterophilous patterns in relation to model performance is provided, but it would be helpful to offer some guidance on model design when dealing with these graphs. Alternatively, the paper could explain why existing methods succeed on these graphs. 

3. The paper could benefit from evaluations on larger-scale graphs. In section 5, the evaluations on the HSBM model are too simplistic to demonstrate its effectiveness, and it would be advantageous to increase the graph size. Specifically, the current evaluation uses graphs with only 1000 nodes, which is insufficient to demonstrate the scalability of the proposed analysis and the generality of the conclusions.

### Questions
No more

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper delves into the theoretical effects of various heterophily patterns on GNNs by integrating graph convolution (GC) operations into fully connected networks using the newly proposed Heterophilous Stochastic Block Models (HSBM). The study reveals three key findings: 
1) Applying a GC operation results in separability gains determined by the Euclidean distance of neighborhood distributions and the square root of node degree. 
2) Topological noise negatively affects separability. 
3) Using multiple GC operations reveals that separability gains are linked to the normalized distance of l-powered neighborhood distributions, suggesting sustained node separability as l approaches infinity across different conditions.

### Strengths
Theoretical Insight into Heterophily Patterns: A significant strength of this work lies in its analytical treatment of the heterophily pattern. By dissecting and delving into the theoretical facets of heterophily, the paper offers an elevated understanding of datasets characterized by this pattern. This examination provides a foundational framework for future investigations into heterophily-rich datasets.

### Weaknesses
Limited Novelty: While the paper takes steps toward analyzing the heterophily problem, the extent of innovation remains somewhat constrained. I found that the conclusions and the main method they use are very similar to this ICML 21 paper: Graph Convolution for Semi-Supervised Classification: Improved Linear Separability and Out-of-Distribution Generalization [1]. In that paper, they also analyze the SBM model and show that graph convolution extends the regime in which the data is linearly separable by a factor of roughly 1/sqrt(D), where D is the expected degree of a node, which was rediscovered by this paper. Besides, the paper Two Sides of the Same Coin: Heterophily and Oversmoothing in Graph Convolutional Neural Networks [2] also mentions that the node degrees play an important role in the heterophily and oversmoothing problem.

Regarding Assumption 1: I noticed that the conclusion derived for Assumption 1 is predominantly based on statistical information from a small subset of datasets. Could you elucidate how you might validate this assumption? Alternatively, is there a possibility to derive this conclusion from a broader statistical perspective or from an extended range of datasets?

Empirical Validation with Real-World Data: In the presented real-world experiments, it seems that only a limited number of datasets were employed to validate the proposed heterophily pattern concepts. Considering the importance of comprehensive empirical validation, would it be feasible to provide additional experiments across a wider range of datasets to reinforce your conclusions?

### Questions
See the weakness above.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper aims to provide a theoretical understanding of the effects of different heterophily patterns on GNNs. The novel Heterophilous Stochastic Block Models (HSBM) is introduced to integrate graph convolution (GC) operations into fully connected networks. The paper offers insights into the factors determining the separability gains when applying GC operations and the influence of topological noise. The study validates the theory with experiments on synthetic and real-world data.

### Strengths
* The paper provides solid theoretical insights into the interplay of heterophily patterns and GNNs. It addresses the challenge of understanding the impacts of heterophily on classification tasks.

* The HSBM is a unique proposition that can accommodate a variety of heterophily patterns. This is likely to be beneficial to the research community aiming to handle diverse graph structures.

* The authors present an in-depth analysis of the separability gains in the context of GC operations, shedding light on factors like Euclidean distance of the neighborhood distributions and averaged node degree.

### Weaknesses
 * While the authors have acknowledged the limitations of their model and analysis, they are significant. The assumptions on which the theory is based, especially Gaussian node features and independence among node features and edges, might not hold true in many real-world scenarios. The future directions suggested by the authors, including extending the analysis to other feature distributions and considering dependencies among nodes and edges, are crucial for the model's broader applicability. Specifically, the assumption of Gaussian node features limits the applicability of the theoretical results, as real-world node features often exhibit more complex distributions, such as multi-modal or heavy-tailed distributions. Additionally, the independence assumption between node features and edges is a strong simplification, as in many real-world graphs, the node features and the graph structure are inherently correlated. For example, in social networks, users with similar profiles are more likely to be connected, violating the independence assumption. These assumptions, while simplifying the analysis, significantly constrain the model's capacity to accurately represent real-world scenarios.

 * Discussion on potential real-world applications or case studies where HSBM could be applied would enhance the paper's relevance and appeal to a broader audience. The current presentation lacks a clear connection to practical applications, making it difficult to assess the real-world impact of the proposed theoretical framework. While the theoretical insights are valuable, the absence of concrete examples where the HSBM model could be effectively utilized diminishes the paper's overall impact. For instance, the authors could explore applications in areas like social network analysis, recommendation systems, or biological network analysis, where heterophily plays a crucial role. Without such examples, it remains unclear how the theoretical framework translates into practical benefits.

### Questions
*  It would be beneficial for the authors to delve deeper into the implications of the assumptions they have made, providing justifications or scenarios where these assumptions are most likely to hold true.

*  The authors should consider elaborating on the experimental section, providing more detailed results, methodologies, and potential pitfalls or challenges. The benchmarks used in https://arxiv.org/abs/2302.11640 are suggested.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper focuses on heterophily in Graph Neural Networks (GNNs) and its impact on node classification. It proposes the Heterophilous Stochastic Block Models (HSBM) to incorporate different heterophily patterns in GNNs. The authors present theoretical analyses of the effects of heterophily patterns on GNNs, considering graph convolution operations. They reveal that the separability gains in GNNs depend on the Euclidean distance of neighborhood distributions and the averaged node degree. The paper also discusses the impact of topological noise on separability and the influence of stacking multiple graph convolution operations. The theoretical results are supported by experiments on synthetic and real-world data.

### Strengths
The authors provide sufficient theoretical analysis.

### Weaknesses
Two related works need to be discussed [1,2].

"Its primary objective is to accurately categorize samples into their respective classes while distinguishing them from samples belonging to other classes." I think this is the same as the statement about intra- and inter-class node distinguishability in [1]. What is the difference and advantage of your "ideal Bayes classifier" over the optimal Bayes classifier in [1]?

Although this paper gets some similar conclusions as the previous paper about heterophily, I don't think it reduce a lot about is contribution. Thus, I'll give it a 6.

### Questions
1. Two related works need to be discussed [1,2].

2. "Its primary objective is to accurately categorize samples into their respective classes while distinguishing them from samples belonging to other classes." I think this is the same as the statement about intra- and inter-class node distinguishability in [1]. What is the difference and advantage of your "ideal Bayes classifier" over the optimal Bayes classifier in [1]?

Although this paper gets some similar conclusions as the previous paper about heterophily, I don't think it reduce a lot about is contribution. Thus, I'll give it a 6.



[1] When do graph neural networks help with node classification: Investigating the homophily principle on node distinguishability. arXiv preprint arXiv:2304.14274.

[2] Demystifying Structural Disparity in Graph Neural Networks: Can One Size Fit All?. arXiv preprint arXiv:2306.01323.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
