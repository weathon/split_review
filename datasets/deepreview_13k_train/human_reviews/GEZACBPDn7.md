# KDGCN: A Kernel-based Double-level Graph Convolution Network for Semi-supervised Graph Classification with Scarce Labels

- Decision: Reject
- Scores: 5, 5, 8, 3

## Abstract
Graph classification, which is significant in various fields, often faces the challenge of label scarcity. Under such a scenario, supervised methods based on graph neural networks do not perform well because they only utilize information from labeled data. Meanwhile, semi-supervised methods based on graph contrastive learning often yield complex models as well as elaborate hyperparameter-tuning. In this work, we present a novel semi-supervised graph classification method, which combines GCN modules with graph kernels such as Weisfeiler-Lehman subtree kernel. First, we use a GCN module as well as a readout operation to attain a graph feature vector for each graph in the dataset. Then, we view the graphs as meta-nodes of a supergraph constructed by a graph kernel among graphs. Finally, we use another GCN module, whose inputs are the graph feature vectors, to learn meta-node representations over the supergraph in a semi-supervised manner. Note that the two GCN modules are optimized jointly. Compared to contrastive learning based semi-supervised graph classification methods, our method has fewer hyperparameters and is easier to implement. Experiments on seven benchmark datasets demonstrate the effectiveness of our method in comparison to many baselines including supervised GCNs, label propagation, graph contrastive learning, etc.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper views graphs as meta-nodes and constructs a super graph, which then enables semi-supervised graph classification learning, akin to semi-supervised node classification learning. Specifically:

1. First, a GNN is used to learn a representation for each graph, serving as the initial node representation of the supergraph,
2. Next, the WL kernel is employed to determine the similarity between graphs, forming the edges of the supergraph,
3. Finally, another GNN is used for semi-supervised learning on the supergraph.

The experiments implied that this method can achieve SOTA or comparable to SOTA results on several datasets.

### Strengths
1. Compared to other methods based on contrastive learning, utilizing a supergraph for semi-supervised learning eliminates the need to construct negative samples, simplifying the whole framework.

2. It achieves SOTA results on smaller datasets and comes close to SOTA on medium-sized datasets.

### Weaknesses
1. The datasets used for experiments are relatively small, and it seems that the advantages are not as pronounced on larger datasets, necessitating validation on larger datasets. Specifically, while the COLLAB dataset is mentioned as large, the paper needs to clarify the specific challenges it poses for graph classification, such as high variance in graph sizes or complex structural patterns, and how the proposed method addresses them. The lack of a clear definition of 'large' in the context of graph datasets makes it difficult to assess the generalizability of the findings.

2. A comparison is needed with the following two papers:

    [1]. **Few-Shot Learning on Graphs via Super-Classes based on Graph Spectral Measures**

    [2]. **PRODIGY: Enabling In-context Learning Over Graphs**

In paper [1], a supergraph is constructed for Few-Shot graph classification, while in paper [2], a supergraph is built for In-context few-shot node and *edge classification*. The paper needs to clearly articulate the differences in the supergraph construction and usage compared to these existing methods. It is not sufficient to simply state that the tasks are different; a detailed comparison of the technical approaches is necessary to highlight the novelty of the proposed method.

### Questions
1. This paper mentions that the two GCNs are optimized jointly, implying that during training, all graphs in the dataset must be inputted into the hardware simultaneously. Does this limit the model's ability to be trained on large-scale datasets?

2. If KDGCN only supports the Transductive setting, while the compared methods MVGRL, SimGRACE, and GLA can support the Inductive setting?

3. If it is the Transductive setting, must the entire dataset be inferred together during inference? Please describe the inference budget, including platform, memory usage, and inference time.

4. Is this paper the first to perform semi-supervised graph classification by constructing a supergraph? The core innovative point of the article needs to be re-emphasized.

### Soundness
3 good

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
- The paper studies the problem of graph classification with scarce labels. The authors propose a semi-supervised graph classification method called KDGCN, which consists of two GCN modules. The first GCN module obtains feature vectors for each graph through a readout operation. Then, the authors construct a supergraph using graph kernels. The second GCN module employs a semi-supervised approach to learn meta-node representations on the supergraph, capturing sufficient structural information from both labeled and unlabeled graphs. Typically, semi-supervised methods based on graph contrastive learning result in complex models and intricate hyperparameter-tuning. However, the method proposed by the authors has fewer hyperparameters and is easy to implement.

### Strengths
- The paper is overall easy to understand.
- The idea of constructing a supergraph is novel and interesting.
- When graph labels are extremely scarce, the proposed method has shown some improvements on certain datasets.

### Weaknesses
 - The section about supergraph construction mentions using a predefined similarity threshold (τ) to determine the existence of edges, but it does not explain how to select this threshold. The impact of this threshold on the supergraph's structure and the overall performance of the method is unclear. Specifically, the paper lacks a discussion on how different values of τ might lead to either overly sparse or overly dense supergraphs, and how these structural changes would affect the information propagation during the semi-supervised learning phase.
- While the experiments demonstrate that the WL subtree kernel performs well in certain cases, should the paper provide a more detailed comparison and analysis to explain why this kernel was chosen over other possible kernels? The paper does not sufficiently justify the choice of the WL subtree kernel over alternatives such as graphlet kernels or random walk kernels, which might capture different aspects of graph similarity. A more thorough analysis of the properties of the WL subtree kernel and its suitability for the task is needed.

### Questions
- Can more information be provided to explain the structure and properties of the supergraph and how it impacts the method's performance?
- I am concerned about the limitations of the proposed method and its potential application scenarios. Additionally, is the complexity of the proposed method scalable on large datasets?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presented a semi-supervised method for graph classification. The proposed model is composed of two GCNs, one is for individual graphs and the other is for a super graph of all graphs, where the super graph is constructed by a graph kernel. The proposed method is compared with its competitors such as graph contrastive learning on benchmark datasets, where different labeling rates have been considered.

### Strengths
1. The problem studied in the paper, namely graph-level semi-supervised learning with scarce labels, is an important and challenging problem. 
2. The proposed method is based on a double-level GCN model, which has two GCNs. The first one performs graph convolution for each graph and the second one performs graph convolution for a global graph defined (by graph kernel) over all the graphs. This idea is very novel and appealing.
3. The proposed method is compared with state-of-the-art methods such as SimGRACE and GLA as well as classical methods such as GCN and WL kernel. It has competitive performance.
4. The proposed method is simple and easy to implement.

### Weaknesses
 1. The authors claimed that their method has fewer hyperparameters but they did not provide specific comparison with other methods such as GLA in terms of the number of hyperparameters. 
 2. The similarity graph among graphs is constructed by a graph kernel such as WL-subtree kernel and there are two different post-processing method for $\mathcal{K}$. it is not clear which one is better and which one was used in the experiments. 
 3. The writing can be further improved.

### Questions
1. At the beginning of Section 3.1, $\mathbf{S}$ is a binary matrix. However, in Section 3.3, the kernel matrix given by a graph kernel may not be binary or sparse. Do the sparsification and binarization have a significant impact on the performance of the proposed method? 
2. In Section 4.2, the authors set $d=d’=64$. Is this the best setting? How do $d$ and $d’$ as well as $d’’$ influence the classification accuracy?
3. What are the numbers of layers in the two GNNs in the experiments? Does the depth matter?
4. In Figure 2, the two post-processing methods for the global kernel matrix are compared. It seems that the one related to $c$ is better than the one related to $\tau$. I wonder if the authors reported the results of the method related to $c$ in Tables 2, 3, and 
5. It is not clear why the authors did not include the results of larger labeling rates such as 30% or 50%.
6. Are their any time cost comparison?
7. In Table 4, it seems that the performance of graphlet sampling kernel is always the worst. I suggest the authors discuss the difference between graphlet sampling kernel and other kernels.
8. It is necessary to compare the number of hyperperameters of the proposed method with those of the baselines. In the proposed method, one has to determine $c$ or $\tau$, which affect the classification performance.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a novel semi-supervised graph classification method that combines GCN modules with graph kernels, resulting in a model with fewer hyperparameters. Experiments on seven benchmark datasets demonstrate its effectiveness compared to various baselines, including supervised GCNs and graph contrastive learning."

### Strengths
- Graph classification is a very fundamental problem for graph-related problems, and exploring semi-supervised graph classification is a very interesting topic.
- The paper is well-organized and easy to be understood.

### Weaknesses
 - The introduction of the graph kernel concept in semi-supervised graph classification methods is not a novel idea, and it has been mentioned in many previous studies [1-3]. However, the authors have not referred to it or provided a detailed comparison, and I strongly recommend that they compare and discuss their work in relation to these existing studies.
- It seems that the graph kernel in the paper is not learnable, which results in the quality of the supergraph construction being entirely dependent on the learned node representations and the chosen threshold. Turning the graph kernel into a learnable component could be a better approach.
- The model is evaluated only on small datasets and doesn't know the scalability on large-scale datasets.
- This task also has several highly relevant works, which the authors have not mentioned or compared to in their paper. To ensure the novelty of their method and the superiority of its results, it is advisable for the authors to provide supplementary comparisons and engage in a detailed discussion. [4-6].

### Questions
The novelty of the paper and the absence of important baselines are the two most critical factors affecting the quality of the article. I recommend that the authors make significant revisions.

### Soundness
1 poor

### Presentation
2 fair

### Contribution
1 poor
