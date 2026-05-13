# Rethinking Independent Cross-Entropy Loss For Graph-Structured Data

- Decision: Reject
- Scores: 3, 6, 5

## Abstract
Graph neural networks (GNNs) have exhibited prominent performance in learning graph-structured data. Considering node classification task, based on the i.i.d assumption among node labels, the traditional supervised learning simply sums up cross-entropy losses of the independent training nodes and applies the average loss to optimize GNNs' weights. But different from other data formats, the nodes are naturally connected. It is found that the independent distribution modeling of node labels restricts GNNs' capability to generalize over the entire graph and defend adversarial attacks. In this work, we propose a new framework, termed joint-cluster supervised learning, to model the joint distribution of each node with its corresponding cluster. We learn the joint distribution of node and cluster labels conditioned on their representations, and train GNNs with the obtained joint loss. In this way, the data-label reference signals extracted from the local cluster explicitly strengthen the discrimination ability on the target node. The extensive experiments demonstrate that our joint-cluster supervised learning can effectively bolster GNNs' node classification accuracy. Furthermore, being benefited from the reference signals which may be free from spiteful interference, our learning paradigm significantly protects the node classification from being affected by the adversarial attack.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper argues that existing approaches for graph learning assume independent cross-entropy loss and ignores the inter-dependence induced by observed graph structures. In light of this, the authors propose a new objective that incorporates the inter-dependence among node points into the loss computation. This ensures that the loss for each node is dependent on other nodes during the training. Experiments on many benchmark datasets and using various GNNs as backbones verify the effectiveness of the new loss over the traditional loss function.

### Strengths
1. The paper is well written and easy to follow

2. The proposed method seems reasonable and sound

3. Experiments entail a lot of datasets and different GNNs as backbones

### Weaknesses
The major concern on this work is the potential over-claiming. The authors argued that existing approaches ignore the inter-dependence among node points for loss computation, which is incorrect. There are in fact quite a few existing works that already considered designing inter-dependent loss for graph learning tasks. 

For example, [1] proposes a new objective based on conditional random field for node classification, and [2] harnesses label propagation as a re-weighted loss. Besides, there are also recent works proposing self-supervised loss that considers enforcing the consistency between connected nodes [3]. These approaches integrate the inter-dependence of nodes into the loss function for training.

Another weakness lies in the comparison in experiments. The current experiment only compares with the traditional cross-entropy loss, which is a very weak baseline. More comparison with other advanced methods, particularly the above-mentioned models are needed to well justify the efficacy of the new design.

[1] Meng Qu, et al., Neural Structured Prediction for Inductive Node Classification, ICLR 2022

[2] Hande Dong, et al., On the Equivalence of Decoupled Graph Convolution Network and Label Propagation, WWW 2021

[3] Hengrui Zhang, et al., Localized Contrastive Learning on Graphs

### Questions
See weakness above

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper studies the problem of discrepancy between the non-i.i.d. property of GNN and the MLE learning. It proposed a new loss function to address the problem and its performance is demonstrated by extensive experiments.

### Strengths
1. The studied problem is important.
2. The idea of the proposed method is novel.
3. The method is effective in comparison to the baseline cross-entropy loss.

### Weaknesses
1. Some notations or definitions haven't been clearly explained. See the questions.
2. The discussion about the connection between (5) and (4d) is missing. This makes it difficult to follow (5).

### Questions
1. More explanation about the equivalance between (4c) and (4d) should be provided.
2. In the definitions of $\bar{z}_m$ and $\bar{y}_m$, there are two indices $k$ and $i$ that are confusing. 
3. In (5), $y _i\bar{y} _m^\top$ is a matrix, which is not consistent with the shape of output of $g _\phi$.
4. What are the labeling rates for the datasets in Table 1? How does labeling rate influence the classification accuracy?
5. How did the authors determine the hyperparameters of the compared methods?
6. It is not clear why the improvement on balanced data is higher than imbalanced data.

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
The paper proposes joint-cluster supervised learning for graph neural networks. Instead of adopting the cross-entropy loss for each node independently, the paper models the joint distribution of node and cluster labels, given their respective representations. Extensive experiments are conducted across multiple benchmarks, demonstrating the proposed loss can boost the performance of different backbone GNNs and robustness against adversarial attack.

### Strengths
1. The proposed joint modeling of node and cluster is novel and sound.

2. The scope of the experimental evaluation is broad, including small graphs and large graphs.

3. The empirical analyses are comprehensive in terms of necessary discussions, comparisons, and visualizations.

### Weaknesses
1. The backbones adopted for experiments are mostly not those that perform the best on these benchmarks. It would be more convincing to see how the proposed loss boost the performance of strong GNN models, e.g., GCNII on Cora, that may give rise to sota performance.

2. Similar concern to 1 also exists for analyses like Table 6 (with GCN) and Table 7 (with MLP).


[1] Chen et al. Simple and deep graph convolutional networks. In ICML.

### Questions
1. Could more results with stronger backbones be provided on these datasets? e.g., GCNII on Cora.

2. It is vague how this technique helps improve the best models that prevail on different tasks. For example, at least a comprehensive table which enumerates most recent or best performing methods on several datasets should be presented to give the readers an overview how this approach situate in the rich literatures in GNN-based node classification.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
