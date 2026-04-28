# Attention-based Graph Coreset Labeling for Active Learning

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 6, 6, 5

## Abstract
GNN-based Active Learning (AL) methods have been proposed to improve labeling efficiency by selecting the most informative nodes in a graph for labeling. The existing graph active learning methods employ different heuristic approaches, while efficiency sometimes, they fail to explicitly explore the influence of labeled data on unlabeled data, thus limiting the generalizability of graph models to various types of graph data. In this paper, we propose an Attention-based Graph Coreset Labeling framework (AGCL). AGCL can, with limited budgets, gradually discover core data to be labeled from a global view so as to obtain a training dataset that can efficiently depict the whole graph space and maximize the performance of GNNs. Specifically, we explicitly explore and exploit the correlations between nodes in the unlabeled pool and those in the labeled pool using an attention architecture and directly connect the correlations with the prediction performance on unlabeled set. Using influence scores, AGCL can identify data for labeling having maximum representation difference from the existing labeled pool. This enhances sample complexity.We theoretically demonstrate the superiority of the attention-based data selection strategy in reducing the covering radius bound, thereby improving the expected prediction performance on unlabeled data.
Our experimental results show that the labeled coreset can improve the generalizability of various graph models across different graph datasets, as well as CNN models on image classification tasks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper discusses a new active learning algorithm for graph data. Instead of implicit or heuristic based approach such as entropy or graph-based information to select labeled node from unlabeled set, the paper proposed to use attention mechanism to obtain correlation between labeled sets and unlabeled sets and select the labeled nodes based on the obtained correlation score. Based on the concept of coreset and its theoretical basis established in CNN's domain, the author attempts to build a similar case for learned graph embeddings and provides a theoretical foundation for the experimental success of the proposed method. The author conducted experiments on different scales of graph datasets and different homo scores and empirically show the advantage of such proposed method. Additionally, the paper shows advantage of the proposed active learning algorithm on the image classification problem as well.

### Strengths
1. The paper provides a comprehensive experiments over different scales of graph datasets as well as different homo levels of graph datasets. Additionally, the paper provides results over different models, demonstrating empirically the proposed methods show some advantages compared to existing active learning approaches on the graph dataset.
2. The paper attempts to establish theoretical basis for the empirical success of the proposed method.
3. The novelty of the method is to leverage attention mechanism to obtain the approximated correlation between labeled and unlabeled nodes instead of heuristic methods. While I am not an expert of active learning domain, I assume the direction of replacing heuristic to learned measure should be a proper path to better quantify the most quality label sets.

### Weaknesses
1. While the paper provides a comprehensive experiments over many datasets, as I am not an expert of active learning field, I found it rather confusing to use hyperparameter to search for an initial set S0. From my perspective, the initial labeled set S0 should be within part of the budget B. If hyperparameter search is allowed for S0, I think that implicitly provides exceeding budget to the proposed methods. I assume only the proposed method has such hyperparameter and therefore this leads to a unfair comparison and makes me doubt if the experimental advantage comes from the exceeding budget.
2. I am not really convinced on the theoretical analysis. In the original CNN paper regarding coreset analysis, the paper explicitly mentioned the data is iid, which is not the case for the graph data as the paper discussed in the introduction. Graph data is non-iid and there is no attempts on resolving such issue in the theoretical analysis. Proof of the proposition 4.1 is also not satisfying. for d(h,hv)<d(h',hv)<rv, what exactly do we know about h and h' in this case. Simply saying that h' = h+d doesn't provide any useful information for obtaining Eq 11. One can simply consider otherwise h = h'+d and obtain a reversed relation for Eq 11. Also, the paper states according to assumption 1, the dL/dh part is basically 0, then Eq 11 really doesn't provide any information from what I understand.
3. There exist multiple typos such as line 781 assumpation ; proposation, line 772 double equation, etc. The notation of the symbol is also very confusing, d is used both as a distance function, derivative, and variable in the proof, even in the same line. all of these lead to bad experience of reading.
4. There lacks a justification over why GCN, GAT and APPNP is used for graph aggregation but not other models, normally common choice should include GraphSage, GIN, etc. I don't find a clear explanation over why these models are selected as backbones.

### Questions
See Weaknesses, especially point 1 and 2.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper is about GNN-based Active Learning, which is an interesting topic. The authors propose an Attention-based Graph Coreset Labeling framework, which can gradually discover core data to be labeled from a global view so as to obtain a training dataset that can efficiently depict the whole graph space and maximize the performance of GNNs. The paper is well written and well organized. However, there are several concerns in the current version of the paper that addressing them will increase the quality of this paper.

### Strengths
1 This paper focuses on the important issues that do face the GNN community.

2 The paper is clearly structured and easy to understand.

### Weaknesses
1 In the abstract, authors should consider introducing more background information for their research so that readers outside the field can better understand it.

2 Figure 1 can be further improved. Currently, we cannot see a clear model structure and the information that can be expressed is limited.

3 Do the authors discuss the computational complexity of the proposed strategy in detail (not just a brief discussion) and analyze the time and memory consumption of the model in the experiments?

4 The datasets used by the authors are limited in size, and the only relatively large dataset has only 160,000+ nodes. This does not require experiments, but I hope the author can further explain what problems the proposed strategy will encounter when facing large-scale datasets, or what benefits it will bring?

### Questions
As above weakness 4.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper "Attention-based Graph Correlation Distillation with Proxy Node" introduces a new framework called Attention-based Graph Coreset Labeling (AGCL) to improve graph neural networks (GNNs) through active learning. The method leverages attention mechanisms to explicitly model correlations between labeled and unlabeled data in graph structures. By selecting unlabeled data with the greatest difference in representation from the current labeled set, AGCL enhances the coverage and diversity of the labeled pool, ultimately reducing prediction loss. The framework is demonstrated to work across various GNN architectures and graph data types (homophilic and heterophilic), and its flexibility allows it to be applied to image classification tasks as well. The paper presents both theoretical proofs and experimental results that show AGCL's superiority over existing graph active learning methods, offering improved accuracy and efficiency for semi-supervised node classification tasks.

### Strengths
1. The paper introduces a new attention-based approach that effectively models correlations between labeled and unlabeled data in graph structures. This novel framework enhances graph neural networks (GNNs) by selecting data that maximizes label diversity and reduces prediction loss, providing an innovative solution to active learning in GNNs.

2. The method demonstrates its flexibility by being applicable to both homophilic and heterophilic graphs, as well as image classification tasks. This versatility allows the framework to be broadly useful across various GNN architectures and data types, showing its potential for wide-scale adoption.

3. The paper backs its approach with solid theoretical foundations and extensive experiments, proving the effectiveness of the framework. The empirical results demonstrate superior performance compared to existing methods, highlighting the model's ability to improve accuracy and efficiency in semi-supervised learning.

### Weaknesses
1. While the paper demonstrates the method's effectiveness on benchmark datasets, it may not fully address the challenges posed by more complex real-world graphs, which often involve dynamic, evolving structures or noisy data. More diverse, real-world testing would be needed to validate its robustness in various practical settings. Specifically, the paper does not explore scenarios with time-varying graph structures, where node connections and features can change over time. This is a significant limitation as many real-world graphs, such as social networks or citation networks, are not static. Furthermore, the evaluation does not consider the impact of different types of noise, such as adversarial attacks or label noise, which are crucial for assessing the robustness of the proposed method in practical applications.

2. While the theoretical analysis in the paper aims to support the coreset selection strategy by minimizing the loss in the representation space, it doesn't fully explore how the attention mechanism or the architecture of the proposed Attention-based Graph Coreset Labeling (AGCL) model specifically affects these theoretical guarantees. The analysis does not provide a clear explanation of how the attention weights are related to the coreset selection process or how the specific architecture of the attention mechanism influences the theoretical bounds. For example, the paper does not discuss the impact of different attention heads or the choice of activation functions on the theoretical guarantees.

### Questions
see weaknesses

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes an Attention-based Graph Coreset Labeling (AGCL) framework for active learning in graph neural networks. By leveraging attention mechanisms, the proposed AGCL aims to identify the most representative nodes for labeling. It addresses the challenge of selecting informative nodes from a global perspective by focusing on representation diversity between labeled and unlabeled nodess. The experiments demonstrate that AGCL effectively enhances model performance with fewer labeled nodes, which outperforms existing methods across various datasets.

### Strengths
AGCL improves label efficiency by selecting nodes that maximize representation diversity, which allows the model to generalize better with fewer labeled samples.

Experiments show that AGCL outperforms existing methods across multiple GNN architectures and datasets

### Weaknesses
In the introduction, the authors fail to adequately explain why traditional active learning methods developed for CNNs cannot be directly applied to GNNs, which might diminish the novelty and motivation for the proposed method.

The authors aim to select "truly informative data points" in graph-structured data but do not provide a clear definition or criteria for what makes a data point "informative." A more precise definition of informativeness, with concrete criteria or theoretical support, would be helpful.

The proposed method uses attention coefficients to capture global influence between labeled and unlabeled nodes. However, I question the reliability of these coefficients, given that initial labels may not provide sufficient supervision for accurate training. Could the authors clarify how they ensure the attention coefficients' accuracy under limited labeled data?

The comparison methods used in the paper are somewhat outdated and may not sufficiently demonstrate the advantages of the proposed algorithm. Incorporating more recent state-of-the-art methods would strengthen the evaluation.

### Questions
How do the authors ensure that attention coefficients are reliable given the limited labeled data available initially? 

Could the authors elaborate on why traditional CNN-based active learning methods are not suitable for GNNs?

### Soundness
2

### Presentation
2

### Contribution
2
