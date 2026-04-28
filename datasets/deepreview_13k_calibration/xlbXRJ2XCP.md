# MaxCutPool: differentiable feature-aware Maxcut for pooling in graph neural networks

- Decision: Accept
- Avg Score: 5.25
- Scores: 6, 6, 6, 3

## Abstract
We propose a novel approach to compute the \maxcut in attributed graphs, \textit{i.e.}, graphs with features associated with nodes and edges. Our approach is robust to the underlying graph topology and is fully differentiable, making it possible to find solutions that jointly optimize the \maxcut along with other objectives.
Based on the obtained \maxcut partition, we implement a hierarchical graph pooling layer for Graph Neural Networks, which is sparse, differentiable, and particularly suitable for downstream tasks on heterophilic graphs.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces an innovative method for computing the MAXCUT in attributed graphs which is fully differentiable, enabling joint optimization of the MAXCUT with other objectives. Leveraging the resulting MAXCUT partition, the authors develop a hierarchical graph pooling layer tailored for Graph Neural Networks. The authors claim that the pooling layer is sparse, differentiable, and effective for downstream tasks on heterophilic graphs, addressing a key challenge in graph learning by providing a versatile and adaptable pooling strategy.

### Strengths
- Introducing the concept of maxcut into attributed graph pooling is novel and meaningful, and it is worth noting the proposed method is feature-aware and differentiable.
- The background and related work are introduced in detail and accompanied by illustrations, which greatly aid in understanding the proposed method.
- It is encouraging that the proposed method was tested on three tasks, including maxcut partition, graph classification, and node classification.

### Weaknesses
 - The authors are advised to theoretically and empirically analyze the complexity of MaxCutPool, showing whether it introduces additional computational overhead to GNNs.
- It is also recommended that the authors provide the code to facilitate a better understanding of the proposed method and to ensure the reproducibility of the experiments.
- The authors claim that MaxCutPool is particularly effective for heterophilic graphs, but no detailed analysis is provided. What is the underlying interaction between MaxCutPool and heterophilic graphs? Additionally, considering that traditional message passing (including GIN) is designed for homophilic graphs and is regarded as a low-pass filter, could this conflict with MaxCutPool and potentially lead to poorer results?
- My primary concern is with the experimental section. In graph classification tasks, the proposed approach does not demonstrate satisfactory performance and even falls below the no-pooling baseline on nearly half of the datasets. In Table 3, the authors mark the performance of the no-pooling baseline in gray, even when it ranks highest, which is confusing.
- Is MaxCutPool-NL learning $\mathbf{s}$ solely with task loss after removing $\mathcal{L}_{cut}$? Does this imply that the core concept of MaxCut has been removed? If so, it still appears to be comparable.
- Although the work emphasizes its advantages on heterophilic graphs, it does not perform better than other pooling methods on the GCB-H and MUTAG datasets, which have the highest levels of heterophily.
- Compared to graph classification, the performance on node classification is satisfactory. However, it seems that datasets are not the commonly adopted ones for node classification (such as Planetoid or OGB) and exhibit very low levels of heterophily.

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper introduces a novel GNN-based approach for solving the MaxCut problem in attributed graphs. The proposed method exhibits good performance across multiple experiments, particularly when evaluated on the newly introduced heterophilic graph benchmark dataset for graph classification tasks.

### Strengths
- The writing is generally reader-friendly, featuring detailed illustrations such as figures and hyperparameters. Theoretical analyses are also provided.
- The proposed method is easy to understand yet remains effective, performing well in experiments.
- This work includes comprehensive experiments covering MaxCut partition computation, graph classification, and node classification, which lend credibility to the conclusions presented in the paper.

### Weaknesses
The method uses HetMP, which can be interpreted as a Laplacian sharpening kernel that enhances differentiation between signals across nodes, thereby reducing smoothness. This approach performs well on heterophilic graphs. However, in Figures 2(b-c), the steps seem to be based on a homophily assumption—where neighboring nodes tend to belong to the same cluster. Specifically, the supernode selection process, while intended to be heterophilic, still relies on nearest-neighbor aggregation for assignment, which inherently assumes that connected nodes should be grouped together. This creates a potential conflict between the heterophilic nature of HetMP and the homophilic nature of the assignment process. Further clarification is needed on how this tension is resolved, especially when the goal is to identify cuts that separate dissimilar nodes.

Beyond Equation (4), it remains unclear how the proposed method would perform with alternative graph kernels or filters, particularly those designed to emphasize high-frequency components or different notions of node similarity. The choice of a standard GCN-based operator may limit the method's ability to capture more complex relationships within the graph. Furthermore, the paper lacks a detailed analysis of the method's performance on homophilic graphs, where the underlying assumption of heterophily might not hold. It is important to understand how the method adapts or fails to adapt in such scenarios, and whether the performance gains observed on heterophilic graphs come at the expense of performance on homophilic ones.

Finally, while the paper claims good scalability, it lacks a rigorous analysis of the practical limitations of the proposed method. It is not clear whether the method can scale to graphs with millions of nodes and edges, or if there are specific bottlenecks that would limit its applicability to large-scale datasets. A more detailed discussion of the time and memory complexity of the pooling layer, along with empirical evidence on its performance with increasing graph sizes, is needed to fully assess its scalability.

### Questions
* The method uses HetMP, which can be interpreted as a Laplacian sharpening kernel that enhances differentiation between signals across nodes, thereby reducing smoothness. This approach performs well on heterophilic graphs. However, in Figures 2(b-c), the steps seem to be based on a homophily assumption—where neighboring nodes tend to belong to the same cluster. Could you provide further clarification on this?
* Beyond Equation (4), how does the proposed method perform when using other graph kernels or filters, such as high-pass filters? Additionally, how does the method perform on homophilic graphs?
* Can the proposed method scale to graphs of arbitrary size, or are there practical limitations on the scalability threshold?

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
4

### Summary
Graph neural networks are constructed out of a few relatively simple building blocks -- A propagation operator, a message function, and a pooling function. These three components have received significant attention over the last few years, with both heuristic and graph theoretic approaches to improve the performance of GNNs on a variety of graph ML tasks. In this work, the authors present a novel pooling operator termed MaxCutPool, that is inspired by the classic graph theory problem of finding the max cut. They provide justification for the value of this pooling operator through robust experiments to find significant performance improvements.

### Strengths
1. The paper is clearly presented
2. The experiments are well defined and clearly motivated
3. The authors make significant efforts to contextualize their work within the rest of the literature.
4. The algorithm is clearly outlined in enough detail to reimplement

### Weaknesses
This paper is well written, but not without weaknesses. In particular:

1. The authors do not discuss the computational cost of running their pooling operators in comparison to others. While potentially less relevant for graph classification tasks, it is highly relevant for node classification tasks. Please include some discussion, at least in the appendix, of this.
2. The authors do not justify _why_ it is expected that the max cut should provide a better pooling operator.
3. The results in experiment 4.2 indicate only mild performance gains, and the presented method frequently underperforms the case with no pooling. It's was hard for me to understand from the text what the intuition for this is.
4. The experiments in section 4.3 are hard to understand without a no-pooling option.

### Questions
1. In experiment 4.1, what were the features used for GNN? Were these learnable vertex embeddings?
2. How does maxcutpool scale with the number of vertices in a graph?
3. What is the intuition as to why learning the max cut operator provides a good pooling operator? Is it just that this is a high-frequency projection?
4. In experiment 4.3, could you provide the tuned baseline for a GNN with no pooling?
5. With $\delta$ set to 2 in your node classification experiments, your propagation operator is already tuned towards heterophilic settings, and the stated intuition for why maxcutpool works is because it is projecting out high frequency components. Could you provide a node-classification results as a function of delta? Given that these datasets are all heterophilic, it's hard to tease out whether the improvements are due to the pooling or the propagation operator.
6. How was hyperparameter tuning performed?
7. Can this work be extended to link prediction in any meaningful way? Would it be possible to view super-node membership as a labeling trick?
8. Does the unpooling operator involve any normalization?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes a novel graph pooling method based on the maxcut algorithm. As MaxCut assigns high scores to disconnected nodes, this paper motivates its connection to one-every-K pooling methods and score-based methods. They formulate a differentiable form of MaxCut which they integrate into a pooling layer that utilizes heterophilic message-passing layers. Several experiments comparing MaxCutPool to other pooling methods are conducted.

### Strengths
The paper proposes an intuitive pooling method. It is very nicely written and nicely describes the current state-of-the-art for graph pooling. I understood almost all of the details.

### Weaknesses
 * W1: Auxiliarly loss: As with other top k pooling approaches, the selction is a discrete action and thus not differentiable. Optimizing $\mathcal{L}_{cut}$ may not lead to an s that is well-suited for the downstream task. Claiming that the proposed pooling operator is fully differentiable is thus misleading. The gradient of the auxiliary loss does not provide information on whether other nodes should have been selected, as the selection itself is non-differentiable. The scores are multiplied with the node states, but this operation does not provide gradient information on whether other nodes should have been selected. This means that the model cannot learn which node selections are beneficial for the downstream task.
* W2: This paper proposes multiple parts without thoroughly analysing each of them:
    * i) Gradient descent for combinatorial problems are typically not preferred as the solution can arbitrarily bad due to local minima. As this paper proposes to use gradient descent for MAXCUT, there needs to be a more detailed comparison with existing methods, ideally in terms of time/space complexity, expected performance and guarantees. 
    * ii) It also remains unclear whether this gradient based approach is better for downstream-tasks. The only experiment that compares the proposed MaxCutPool with existing MAXCUT algorithms is in Table 2, which shows slight improvements. To me it is not convincing to use this gradient based approach vs. traditional algorithms within MaxCutPool.
    * iii) While the nearest neighbor aggregation is proposed as a algorithms for many pooling methods, it is only evaluated in combination with MaxCutPool. As the difference is rather small it is unclear whether this step is needed. If the authors decide to propose such an algorithm, a more detailed evaluation would be needed. 
* W3: The overall contribution is quite limited. As pointed out by the authors, many algorithms for graph pooling exist and the theoretical and empirical benefits of MaxCutPool do not convince me.
* W4 Experiments: 
    * i) There is no reproducible implementation provided.
    * ii) Graph classification: There seems to be a large hyperparameter optimization ofr MaxCutPool, while "all [other] pooling layers were used with the default hyperparameters". This does not seem to be a fair comparison. Especially when only spliiting into train and validation, the search space needs to be of similar size.
    * iii) Heterophilic tasks are only defined for node classification tasks as heterophily is typically defined as having mostly different labels between adjacent nodes. As node labels do not exist for graph-level tasks, it is unclear what heterophilic graph classification means. The authors also did not define what heterophilic graphs are.

Additional minor points:
l.156: Sharpening propagation operators cannot learn any kind of gradients, but sharp gradients.
l.425: "This is the first known instance of a non-expressive pooler passing the expressiveness test provided by this dataset, serving as a counterexample to Theorem 1 in Bianchi & Lachi (2023)". To my understanding, Theorem 1 provides a sufficient condition not a necessary one.

### Questions
* l.289: Is CON always defined using the assignment matrix $\mathbf{S}$ based on nearest neighbor aggregation?
* How well does the differentiable MaxCut approximate MaxCut compared to more other algorithms in terms of approximation and time complexity? 
* Is the differentiable MaxCut required or does this method work with other algorithms for MaxCut?
* How important is the nearest neighbor aggregation?
* How do the other methods perform with the same level of hyperparameter tuning?
* Why is there no reproducible implementation provided?

### Soundness
3

### Presentation
3

### Contribution
1
