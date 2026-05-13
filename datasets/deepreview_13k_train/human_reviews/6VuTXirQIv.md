# Feature Driven Graph Coarsening for Scaling Graph Representation Learning

- Decision: Reject
- Scores: 6, 3, 5, 5

## Abstract
Graphical modelling for structured data analysis has gained prominence across numerous domains. A significant computational challenge lies in efficiently capturing complex relationships within large-scale graph structures. Graph coarsening, which reduces graph size by merging nodes and edges into supernodes and superedges, enhances scalability and is crucial for graph neural networks (GNNs). However, current methods either construct graphs from large-scale attribute data or assume a pre-existing graph before coarsening, limiting their applicability, especially in domains like healthcare and finance where graph structure is often unavailable. In this paper, we present a novel framework that directly learns a coarsened graph from attribute information, reducing computational complexity and enhancing robustness against adversarial attacks, which commonly target vulnerabilities in graph structures. By integrating label information, our framework also enables semi-supervised learning, leading to improved performance on downstream tasks. Extensive experiments show that our method outperforms state-of-the-art coarsening techniques in both accuracy and computational efficiency.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper studies the scalability and structural limitations of existing graph coarsening techniques. It proposes a new framework, Coarsened Graph Learning (CGL), to directly learn a reduced graph from attribute data alone, eliminating the need for a pre-existing graph. By learning the graph from features, CGL enables scalable GNN training, is resilient against adversarial attacks, and incorporates semi-supervised learning with label information for enhanced downstream task performance. Experimental comparisons show that CGL outperforms state-of-the-art methods in node classification accuracy and computational efficiency across various datasets, proving its potential in large-scale, real-world applications.

### Strengths
1. The method relies solely on node features and labels, achieving impressive performance even without an initial graph structure. This approach shows potential for unifying graph data with other data formats.

2. This method stands out for its efficiency and resilience against structural attacks.

3. Bridging the sparsity of PY with the homophily of coarsening introduces an innovative and promising concept.

### Weaknesses
1. Since validation and test labels should remain hidden during training, it would be helpful to clarify how they are masked, perhaps by introducing a specific notation or symbol for this purpose. The masking process needs to be explicitly defined in the methodology, detailing how the labels are partitioned and utilized during the learning of the coarsened graph. Specifically, it is unclear how the label information is propagated from the original graph to the coarsened graph while ensuring no leakage of validation or test labels during training. A clear mathematical formulation of this process would be beneficial.

2. Some baseline results are not fully reproduced. For instance, GCond typically produces results close to those of the full dataset, suggesting that the authors may not have adjusted the dataset split to 80%/10%/10% when replicating GCond’s performance. The discrepancy in GCond's performance raises concerns about the experimental setup. It is crucial to verify that the baseline methods are implemented correctly, using the same data splits and hyperparameter tuning procedures as the proposed method. A more detailed explanation of the experimental setup, including the specific parameters used for each baseline, is needed to ensure reproducibility.

3. Testing this method on large heterophilous graphs, such as Penn94, would add valuable insights into its scalability and effectiveness in diverse graph structures. The current evaluation primarily focuses on homophilous datasets. Expanding the evaluation to include heterophilous graphs would provide a more comprehensive assessment of the method's robustness and generalizability. The performance on heterophilous graphs is particularly important because the method's reliance on feature similarity might not be as effective when node features are not strongly correlated with their labels.

4. This method shares similarities with FGC [1] in objective design and learning approach. However, a more in-depth methodological comparison between the two would be beneficial for understanding their differences and relative strengths. Adding a dedicated section on related works to systematically compare various graph coarsening and condensation methods [2] would further enhance the paper. The comparison should not only focus on the algorithmic differences but also on the theoretical underpinnings and practical implications of each approach. A detailed analysis of the computational complexity and memory requirements of the proposed method compared to FGC [1] and other related methods would also be valuable.

### Questions
Although the runtime for each experiment is very fast, this method depends heavily on extensive hyperparameter tuning. Do the authors have any suggestions for how to select the hyper-parameters?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper introduces the optimization-based framework Coarsened Graph Learning (CGL), which directly learns a coarsened graph from feature data alone. This framework addresses the challenges of scalability and the reliance on initial graph structures. The authors highlight that while graph neural networks (GNNs) are good at modeling graphs, they are vulnerable to adversarial edges that can degrade performance by contaminating node neighborhoods. CGL aims to improve robustness against these adversarial attacks by learning a coarsened graph independently of the original graph structure. CGL formulates the problem as a multi-block, non-convex optimization problem, solved using the Block Successive Upper-bound Minimization (BSUM) technique. The authors compare CGL and its semi-supervised variant (SCGL) against GCOND, SCAL and FGC methods on both homophilic and heterophilic datasets, measuring both classification performance and computational efficiency. Additionally, the incorporation of label information into the objective function significantly enhances downstream task performance.

### Strengths
The optimization approach focuses on deriving a coarsened graph directly from node features, combining graph structure learning with coarsening. By removing dependency on initial graph structures, CGL could mitigate issues caused by adversarial and noisy edges. The writing is clear and accessible, with well-defined concepts that facilitate understanding of complex ideas.

### Weaknesses
The motivation for learning from structureless graphs is limited, making it unclear why this direction is essential or where it’s practically relevant.

CGL is the combination of graph structure learning and graph coarsening, the comparison and discussion of related works are not sufficient. In experiment settings, the baseline of graph coarsening methods are also limited.

While choosing the BSUM methods for non-convex optimization, for large-scale problems, BSUM can be computationally expensive and may converge slowly. As the number of variables and the size of each block are large in some large-scale graph datasets, this might reduce efficiency in practical applications.

The motivation of each optimization procedure is not clear. For example, CGL adapts the idea of paper “A unified framework for structured graph learning via spectral constraints” to optimize the structure of coarsened graph directly, lacking motivation and details for the arguments.

### Questions
Could the authors provide more details on the rationale for addressing structureless graphs and the specific real-world applications this approach is intended to serve?

Why were other coarsening methods not included as baseline comparisons, given the abundance of related work?

BSUM may face scalability issues, especially with high-dimensional data or large block sizes. Did the authors encounter efficiency or convergence challenges on large datasets, and if so, how were these managed?

About the different optimization strategies used, could the authors illustrate why choose these methods and compare with other advantages od doing so?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes a graph coarsening approach that only depends on the node attributes (feature matrix and optionally labels) of the larger graph. Each node is allocated to a super-node (or a node in the coarsened graph), which is learned by solving a multiblock nonconvex optimization problem. This optimization also learns the coarsened graph’s feature matrix and adjacency matrix. The results indicate superior performance across different datasets, improved computational complexity, and robustness against adversarial attack. The latter is due to the elimination of dependence on graph structure in their approach.

### Strengths
1. Tackles the highly relevant problem of graph coarsening, which is especially useful for large graphs.
2. Eliminates dependence on graph structure, achieving much lower computational complexity compared to baselines.
3. Demonstrates adversarial robustness

### Weaknesses
While the underlying problem is topical and interesting, I have below concerns:

1. Lack of clarity and structure: I believe the presentation can be significantly improved. For example, in the introduction, the authors discuss scalability issues for large graphs, critique existing graph coarsening methods (especially their reliance on graph structure), and need for adversarial robustness. However, the discussion feels scattered and difficult to follow.
2. The method itself is simple and intuitive to follow. However, the design choices are not well-motivated. For example, the approach assigns each node to a super-node. This seems to assume an inherent clustering of nodes. This is further reinforced by using node labels and adding the constraint that similar labeled nodes should be assigned to the same super-node. Wonder why hard assignments should be used instead of soft assignments? Is it to aid optimization? An analysis of the relationship between original nodes and supernodes would have been helpful. Moreover, it seems that the coarsened graph may not improve performance when the node labels and downstream tasks are not correlated.
3. The reported performance on the complete dataset doesn’t match the values from previous work [1, 2] for Cora, Citeseer, and Flickr. This raises concerns regarding fairness of comparison. The exact experimental settings and how they differ from referenced work have not been covered even in the appendix.

### Questions
1. In the introduction, emphasis has been given on the adversarial robustness of the proposed approach. However, under experiments, the result and most of the discussion have been deferred to the appendix. Wondering if it may be useful to include a part of the results in the main text for consistency.
2. In table 10, it is interesting to observe that the performance for perturbed data at certain rates is higher compared to unperturbed data. Do you have any comments on this phenomenon?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a graph-coarsening framework that directly learns a coarsened graph from attribute information. The framework also includes a semi-supervised learning pipeline for GNNs that incorporates label information.  The paper proposes two settings: coarsened graph learning CGL and semi-supervised coarsened graph learning SCGL,  and shows the improved performance on downstream tasks.

### Strengths
Pros:
1.  Coarsened Graph Learning is important for the downstream task. 
2. The paper proposes two settings for the downstream tasks, such as coarsened graph learning CGL and semi-supervised coarsened graph learning SCGL.

### Weaknesses
Cons:
1. Why use the coarsened graph for node classification learning to get better node classification performance? It is better to highlight the motivation and prove it with theoretical support.
2. It is better to show the performance of the graph-coarsening framework on other graph-level tasks, such as graph classification and compare it with related baselines.
3. The motivation of the paper needs to be better highlighted. Why only using data features is effective? In fact, the graph structure, even though the noisy/incomplete graph structure is important for the graph coarsing .
4. Some of the notations need to be better illustrated in the paper, such as Wh.Data, L.Data.
5. It is suggested to give some coarsened graph cases to demonstrate the effectiveness of the proposed framework compared with baselines.

### Questions
See the above weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2
