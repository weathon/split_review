# Self-Supervised Heterogeneous Graph Learning:  a Homophily and Heterogeneity View

- Decision: Accept
- Scores: 8, 6, 6, 8, 8, 6

## Abstract
Self-supervised heterogeneous graph learning has achieved promising results in various real applications, but it still suffers from the following issues: (i)  meta-paths can be employed to capture the homophily in the heterogeneous graph, but meta-paths are human-defined, requiring substantial expert knowledge and computational costs; and (ii) the heterogeneity in the heterogeneous graph is usually underutilized, leading to the loss of task-related information. To solve these issues, this paper proposes to capture both homophily and  heterogeneity in the heterogeneous graph without pre-defined meta-paths. Specifically, we propose to learn a self-expressive matrix to capture the homophily from the subspace and nearby neighbors. Meanwhile, we propose to capture the heterogeneity by aggregating the information of nodes from different types. We further design a consistency loss and a specificity loss, respectively, to extract the consistent information between homophily and heterogeneity and to preserve their specific task-related information. We theoretically analyze that the learned homophilous representations exhibit the grouping effect to capture the homophily, and considering both homophily and heterogeneity introduces more task-related information. Extensive experimental results verify the superiority of the proposed method on different downstream tasks.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper addresses challenges in self-supervised heterogeneous graph learning. It points out two main issues: reliance on human-defined meta-paths, and underutilization of graph heterogeneity. To tackle these, the authors propose a method that captures homogeneity without predefined meta-paths using a self-expressive matrix. Additionally, they capture heterogeneity by aggregating information from different node types. Two losses are introduced to ensure consistency between homogeneity and heterogeneity and to preserve task-related information. Theoretical analysis suggests the learned representations effectively capture homogeneity and introduce more task-related information. Experimental results demonstrate the method's superiority across various downstream tasks.

### Strengths
S1. I really like the idea of learning homogeneity and heterogeneity without pre-defined meta-paths. It is fresh and interesting.

S2. They theoretically analyze that the learned homogeneous representations exhibit the grouping effect to capture the homogeneity, and considering both homogeneity and heterogeneity introduces more task-related information

S3. The use of a self-expressive matrix to capture homogeneity without predefined meta-paths is a creative solution, potentially reducing the need for expert knowledge. The introduction of consistency and specificity loss functions enhances the model's ability to extract and preserve task-related information.

S4.  Extensive experimental results demonstrate the effectiveness and superiority of the proposed method across various downstream tasks, validating its practical utility. The paper evaluates the proposed method thoroughly on different downstream tasks, showcasing its versatility and robust performance.

### Weaknesses
W1. Complexity and Computational Cost: The paper doesn't extensively discuss the computational complexity and resource requirements of the proposed method, leaving potential concerns about its scalability in large-scale applications, especially the comparison with traditional meta-path-based approaches. Specifically, the analysis lacks a detailed breakdown of the time and space complexity associated with the self-expressive matrix computation and the aggregation of heterogeneous information. A comparison of the computational cost with meta-path based methods, especially in terms of memory usage and training time, is missing, which is crucial for practical applications.

W2. The whole workflow is a little complicated, which may raise concerns about reproducibility. The interaction between the self-expressive matrix, the consistency loss, and the specificity loss is not clearly delineated, making it difficult to understand the exact contribution of each component. The lack of a step-by-step breakdown of the training process and the hyperparameter tuning strategy further complicates the reproducibility of the results.

W3. Some important work missing, the author should discuss them in their paper, including but not limited to Self-supervised Hypergraph Representation Learning for Sociological Analysis. TKDE; Heterogeneous Hypergraph Embedding for Graph Classification. WSDM

### Questions
please see in the above section

### Soundness
3 good

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes HERO, a self-supervised heterogeneous graph learning method that captures both homogeneity and heterogeneity in the input heterogeneous graph. The authors theoretically analyze the grouping effect provided by capturing homogeneity and the task-related information provided by capturing both homogeneity and heterogeneity. In experiments, HERO outperforms state-of-the-art baselines on both heterogeneous graph datasets and homogeneous graph datasets.

### Strengths
The idea of collectively and explicitly capturing homogeneity and heterogeneity for better SHGL is novel and interesting. The paper is generally well-written without obvious typos or grammatical errors.

### Weaknesses
1. The authors confuse homogeneity and homophily, which impairs the technical soundness of this paper. The definition of homogeneity in the paper is more like homophily. Homogeneity (single node/edge type) and homophily (connected nodes tend to have the same class label) are two different concepts.
2. Overall, many of the arguments proposed by the authors sound far-fetched. It also seems that the authors take many things for granted.
    1. Some claims of the authors are not true. For example:
        - "previous SHGL methods generally overlook or cannot effectively utilize the heterogeneity." Many existing SHGL methods, such as metapath2vec, can capture the heterogeneity. All those GNN-based SHGL methods can also capture both aspects as long as they employ heterogeneous GNN models.
        - "metapaths are employed to capture the homogeneity in the heterogeneous graph." Actually, many SHGL methods also leverage metapaths to capture the heterogeneity, such as metapath2vec, which applies DeepWalk to the node sequences (containing multiple types of nodes) generated by the pre-defined metapath.
    2. Unclear benefit of mining heterogeneity. The example given in the introduction section is hard to understand.
    4. Missing formal definitions for some important terminologies, including homogeneity, heterogeneity, and homogeneity rate.
    5. Missing derivations or theorem proof for some HERO components, including Equation (10) and Equation (11).
    6. The observations stated in Section 2.3 come with no supporting evidence.
3. Missing important baseline: metapath2vec.

### Questions
Please check the weaknesses above for the main issues. Here are some additional questions/comments.
1. What is the evaluation protocol for HERO and other baselines? Is it to train a linear classifier (e.g., SVM) on top of (frozen) representations learnt by self-supervised methods?
2. Metapaths can also associate two nodes with different node types. The definition of metapaths given on page 3 is therefore misleading. It's just many GNN-based methods tend to use the same-type version to construct homogeneous graphs.
3. The idea of this paper is kind of similar to DHGCN [1], which also explicitly and separately aggregates heterogeneous neighbors (heterogeneity) and metapath-guided same-type neighbors (homogeneity).
4. Definition 2.1 is currently hard to understand. The sentence "if the conditions ... hold" may need to be changed to "if $|c_{ik}-c_{jk}|\rightarrow 0$ ($\forall 1 \leq k \leq F^\prime$) hold for every $v_i, v_j$ satisfying $v_i \rightarrow v_j$ (i.e., $||x_i-x_j||_2 \rightarrow 0$)"
5. It would be better to also visualize the self-expressive matrix, to show that it indeed captures homogeneity/homophily.

[1] Saurav Manchanda, Da Zheng, George Karypis: Schema-Aware Deep Graph Convolutional Networks for Heterogeneous Graphs. IEEE BigData 2021: 480-489

### Soundness
2 fair

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
A different insight is given in this paper, compared to previous self-supervised heterogeneous graph representation learning, i.e. capture the homogeneity and heterogeneity without meta-paths. The authors have performed theoretical analysis of the proposed framework from the perspective of grouping effect and downstream tasks.  In addition, sufficient experimental results show that the proposed method achieves best results in several datasets.

### Strengths
(1)	The paper is clearly written and describes a novel insight and framework for the SHGL, which is rare in similar works.

(2)	Some theoretical guarantees are given to illustrate the proposed method.

(3)	Some ablation studies are conducted to verify the effectiveness of each component.

### Weaknesses
(1)	The proposed method uses the same projection head to map homogeneous and heterogeneous representations into the same potential space. It is not clear why this is the optimal choice. Using separate projection heads could allow for more flexible mapping of the different types of representations, potentially capturing unique characteristics of each. The paper should explore the implications of using different projection heads, including a discussion of the potential benefits and drawbacks, and provide empirical evidence to justify the current design choice. For example, does using the same projection head force the homogeneous and heterogeneous representations to be more similar than they should be, potentially losing valuable information?

(2)	The proposed method employs the closed-form solution of the self-expressive matrix to capture the homogeneity in the heterogeneous graph. While the paper mentions this solution, it lacks a detailed explanation of the derivation process within the main body. This makes it difficult for readers to fully grasp the method's mechanics and assess its validity. A more thorough explanation of how the closed-form solution is derived, including the key mathematical steps and assumptions, is necessary to improve the paper's clarity and accessibility. The current explanation in the appendix is insufficient for a comprehensive understanding.

### Questions
The proposed method is also evaluated on the homogeneous graph datasets, e.g. Amazon-photo. On homogeneous graph datasets, does the method proposed in this paper not require data augmentation? What are the advantages of the method proposed in this paper compared to popular self-supervised methods on homogeneous graphs that require data augmentation?

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes to understand the self-supervised heterogeneous graph learning without pre-defined meta-paths from the perspective of homogeneity and heterogeneity. To do this, this paper captures the homogeneity from both the subspace and nearby neighbors as well as to discard pre-defined meta-paths. Moreover, the proposed method further extracts the consistent and specific contents between homogeneous and heterogeneous representations to introduce more task-related information. Experimental results and theoretical analysis demonstrate the superiority of the proposed method.

### Strengths
1.	The authors provide a deeper insight (i.e., heterogeneity mining and homogeneity mining) into existing self-supervised heterogeneous graph representation learning, which is interesting and reasonable.

2.	This paper proposes to use the self-expression matrix rather than traditional meta-paths to capture homogeneity in the heterogeneous graph, which opens up a new possibility for the self-supervised heterogeneous graph learning community to enhance its scalability and effectiveness.

3.	Comprehensive comparison experiments, visualization, and ablation studies are greatly valued. Sufficient datasets from different domains have been used to evaluate the proposed method on different downstream tasks, and the proposed method has been thoroughly discussed through experiments.

4.	I overviewed the code provided by the authors. It seems well-organized and detailed. Moreover, I tried to run the provided code with the saved checkpoints, and it can easily reproduce the results reported in the paper.

### Weaknesses
1. This paper aims to make the first attempt to simultaneously extract the homogeneity and the heterogeneity without meta-path in the heterogeneous graph. So, what’s the difference and relationship between the homogeneity extraction and the heterogeneity extraction in the heterogeneous graph? Specifically, while the paper mentions extracting 'consistent and specific contents' between homogeneous and heterogeneous representations, it is not entirely clear how this is achieved at the algorithmic level. The paper would benefit from a more detailed explanation of how these two types of information are disentangled and then recombined to enhance task-related information. For instance, what specific mechanisms ensure that the 'consistent' information is truly shared and the 'specific' information is unique to each representation? 

2. As this paper proposes a self-supervised framework for SHGL methods, some recent related works in self-supervised learning can be added in the related work section. It would be beneficial to see a more thorough discussion of how the proposed approach relates to contrastive learning methods, or other self-supervised techniques that are commonly used in graph representation learning. This would help to better position the contribution of this work within the broader field of self-supervised learning.

3. The paper needs more proofreading and some typos should be fixed. For example, 
In the second paragraph of page 4: neighbor set->neighbors set.

### Questions
see above

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
* This work captures both homogeneity and heterogeneity in the heterogeneous graph without pre-defined meta-paths. 

* A self-expressive matrix is used to capture the homogeneity from the subspace and nearby neighbors. Meanwhile, the heterogeneity is captured by aggregating the information of nodes from different types. 

* The proposed method extracts the consistent information between homogeneity and heterogeneity and preserves their specific task-related information, leading to the effectiveness. 

* The experimental results show that the proposed method achieves SOTA in various datasets, compared to numerous comparison methods.

### Strengths
* The motivation of the proposed method is clearly stated with the illustrative examples and empirical studies. I really appreciate the examples used in the Introduction. Moreover, the design of the framework is easy to understand.

* The method part is solid, and exploring homogeneity and heterogeneity in the heterogeneous graph without predefined meta-paths makes sense.

* Theoretical analysis verifies that the proposed method captures the homogeneity in the heterogeneous graph and is expected to obtain better performance than previous methods.

### Weaknesses
 * A corollary is shown in the Appendix to verify that the representations with both homogeneity and heterogeneity indeed obtain a better downstream task performance than the representations with homogeneity or heterogeneity only. I think this is a strong addition to Theorem 2.3 and should be mentioned in the main text.

* The proposed method seems to yield overall smaller improvements on homogeneous graph datasets than on heterogeneous graph datasets when compared to comparative methods.

### Questions
* The idea of capturing the homogeneity from the subspace and nearby neighbors is interesting. Can it be used in other related domains, such as computer vision?

* Why replace the heterogeneous encoder with GCN to implement the proposed method on homogeneous graph datasets? What happens if the heterogeneous encoder is replaced with other similar encoders, e.g., GAT?

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 6

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
To capture homogeneity and heterogeneity in the heterogeneous graph without pre-defined meta-paths, this work proposes to adaptively learn a self-expressive matrix and employ the heterogeneous encoder to obtain homogeneous and heterogeneous representations. In addition, the proposed method designs the objective function to extract the consistent information between homogeneous representations and heterogeneous representations and to maintain their specific information in different latent spaces. Moreover, the authors theoretically demonstrate the effectiveness of the proposed method and support the claims made in this paper.

### Strengths
a)Idea in this work is overall novel and attractive, and it will inspire researchers in related fields to explore new methods to capture the homogeneity in the heterogeneous graph without meta-paths, which induces inconveniences and large computation costs.

b)Extensive experimental results demonstrate the effectiveness of the proposed method on both homogeneous and heterogeneous graph datasets in terms of different downstream tasks.

c)Claims in this paper are supported well. That is, the learned homogeneous representations are demonstrated to exhibit the grouping effect to capture the homogeneity, and considering both homogeneity and heterogeneity introduces more task-related information to benefit downstream tasks.

### Weaknesses
a)Not clear why the concatenation mechanism is directly employed to fuse homogeneous representation and heterogeneous representations to obtain final representations for downstream tasks. What would be the impact on the performance of the method if other fusion methods were used, such as average pooling? The authors could add such ablation studies. It is not clear if the concatenation is performed on the raw embeddings or after some transformation, and how the dimensionality is handled. A more detailed explanation of the fusion process is needed, including the dimensionality of the homogeneous and heterogeneous representations before and after concatenation.

b)It would be better to add some details of experiments. For example, the detailed information of all datasets used in this paper, including the number of nodes, edges, and types of each node and edge, as well as the splitting strategy for training, validation, and testing. Furthermore, the hyperparameter settings for the proposed method and the baselines should be included.

### Questions
a)The effectiveness of the proposed HERO and other comparison methods are evaluated through two downstream tasks, namely, node classification and similarity search. What are the significant distinctions between these tasks?

b)Theorem 2.3 does not constrain the type of downstream tasks. Does it mean that the proposed method is expected to achieve better performance on different downstream tasks, compared to the methods considering the homogeneity only?

Overall, this paper holds considerable value and potential, and I will increase my rating if the weaknesses and questions can be addressed and discussed.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
