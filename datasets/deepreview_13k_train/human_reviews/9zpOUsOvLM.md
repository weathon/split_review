# Aligning Persistent Homology with Graph Pooling

- Decision: Reject
- Scores: 3, 5, 3, 6

## Abstract
Recently, there has been an emerging trend to integrate persistent homology (PH) into graph neural networks (GNNs) to enrich expressive power. However, naively plugging PH features into GNN layers always results in marginal improvement with low interpretability. In this paper, we investigate a novel mechanism for injecting global topological invariance into pooling layers using PH, motivated by the observation that filtration operation in PH naturally aligns graph pooling in a cut-off manner. In this fashion, message passing in the coarsened graph is performed along persistent sub-topology, leading to improved performance. Experimentally, we apply our mechanism to a collection of graph pooling methods and observe consistent and substantial performance gain over several popular datasets, demonstrating its wide applicability and flexibility. Code is open-sourced at https://anonymous.4open.science/r/TIP.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a PH-based pooling layer called TIP (topology-invariant pooling). The proposed approach resamples graph connections (after soft-cluster assignments) and scales edge weights with persistence information (from 1-dim persistence diagrams). In addition, TIP applies a new loss that enforces topology-preservation based on multiple vectorizations of the 1-dim diagrams. Experiments on 3 synthetic and 7 real-world datasets aim to show the efficacy of TIP when combined with well-known pooling methods (DiffPool, MinCutPool, and DMoNPool) and GNNs.

### Strengths
- To my knowledge, this is the first paper to leverage PH for graph pooling;
- The proposed method is simple and can be easily integrated (as pooling method) into several GNNs.

### Weaknesses
 - [Theory] Theorem 1 states that distinguishing graphs based on 1-dimensional persistence diagrams is more expressive than 1-WL. **I believe this is false**. For instance, let $G$ and $G'$ be two graphs comprising one and two isolated nodes, respectively. The 1-dimensional diagrams for these graphs are identical (and empty) for any filtration function. However, 1-WL distinguishes graphs with different numbers of nodes. In addition, since the paper leverages filtration functions on node features, for graphs that share the same single feature vector (or same color), 1-dim diagrams cannot go beyond Betti-1, which is clearly less expressive than 1-WL. 

 - [Methodology] Since 1-dim persistence diagrams have limited persistence (the death times are identical), it seems the proposal mainly relies on cycle-preserving pooling (do the authors agree?). At a conceptual level, I am not convinced that this design choice is a desideratum for general-purpose graph pooling and/or graph classification tasks. Overall, I found the motivation for adopting only 1-dimensional PD weak;

 - [Experiments] Due to the lack of a strong/principled motivation, I would expect to see more empirical evidence to support the proposed method. The paper only considers TU Datasets, and therefore does not exploit recent efforts (e.g., OGB) to strengthen the evaluation of GNNs. Moreover, except for the Enzymes dataset, the empirical gains do not look significant (with differences in mean accuracies usually within one std, overall) compared to pooling-free approaches. Lastly, the ablation study should consider other datasets and pooling layers.

### Questions
1. Could you elaborate on how PH coarsens graphs (as in Figure 1)?
2. Do the persistence ratios in Fig. 1(b) include 0-dim persistence diagrams? If so, it seems misleading to use Fig(b) as a motivation and only exploit 1-dimensional PH information for pooling. 
3. Does the proposed method apply multiple filtration functions? If so, how are the 1-dimensional persistence diagrams processed (or combined)? 
4. The paper says: "PH cannot directly extract meaningful topological features from A". Can't we apply edge-level learned filtration functions, where the nested sequence of subgraphs is obtained according to the filtration values at each edge?
5. I believe it would be helpful to see examples of (1-dim) persistence diagrams before and after applying TIP. For instance, I am curious to see the diagrams for the ring and grid2d datasets.
6. In the introduction, the paper says 'in addition to concatenating vectorized PH diagram as supplementary features, ..." However, the methodology section doesn't mention these additional features. Is the proposed approach also using 0-dim persistence information as additional node features (like in TOGL)?
7. Is TIP isomorphism invariant?
8. In section 4, the paper uses vectorized 1-dim diagrams to measure topological similarity. However, Fig. 5 shows learning curves using the Wasserstein distance. I was confused. The same happens with the filtration functions --- Forman curvature vs. learnable filtration function --- it seems the former is only used for evaluation purposes (table 1). These choices should be clarified.


Minor comments and suggestions:
- Page 3: $V=\\{i, x_v\\}$ $\rightarrow$ $V=\\{v, x_v\\}$;
- Page 3: Highlight that the GNN in Eq. (2) is not the same as the one in Eq. (4); 
- Page 3/4: Filtration functions are defined as $f: \mathcal{G} \rightarrow \mathbb{R}$. However, later in the same paragraph, it appears as $f(x_v)$. We can also find $f(e)$. Please be precise here.  
- Page 4: What would be the case (3) "all other edges will be paired with the maximum value of the filtration"? Each edge either creates a cycle (case 1) or not (case 2), no?!
- In Eq. (6), computing the Hadarmard product between $A (n \times n)$ and $(\mathcal{D}_1[1] - \mathcal{D}_1[0]) (m \times 1)$ might be problematic. I suggest being more precise.
- In Eq. (7), the variable $t$ should appear on the right-hand side of $h_t = \text{transform}(D_1)$.
- What do you mean by persistent sub-topology?
- Give more details about the Forman curvature used as the filtration function.
- The caption of Fig. (6) says: "a pair of isomorphic graphs that cannot distinguished by 1-WL but can be distinguished by TIP". It is not clear what the paper wants to convey here (including the plot and the caption).

### Soundness
1 poor

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a new graph coarsening method based on persistent homology, aiming to preserve the topology of the coarsened graph. In particular, it adds the topological loss between the coarsened graph and the original graph into the graph pooling loss function. Experiments on several benchmarks show its effectiveness.

### Strengths
Using persistent homology to enhance graph coarsening is new to the best of my knowledge. 

The proposed model manages to effectively preserve the topological information, as suggested by the empirical validations.

### Weaknesses
1. My biggest concern is that it is unclear why we need to preserve the mentioned topological information, e.g., the 1-th Betti Number (number of cycles) during graph coarsening. For example, in a molecule graph, a benzene ring can be represented by a 6-cycle (a cycle with 6 nodes), and thus can be captured by PH. The cycle can be coarsened to a point, which is reasonable since it will preserve the structural information. However, it will lead to a change in the 1-th Betti Number.

2. Another highly related question is the unclear illustration of Figure 1. What is the chosen filtration of PH in Figure 1(a) and Figure 1(b)? If the filtration is the color of the nodes, then the nodes with the same color should appear or disappear at the same time. In addition, in Figure 1(c), which graph does the diagram correspond to, and which cycle/connected component does each persistence point corresponds to? Furthermore, from my perspective, Figure 1(b) denotes that we can use a graph pooing function to capture the change of the PH information since the correspondence is stable regardless of different datasets. In other words, we do not need additional efforts to preserve the mentioned topological information.

3. In the experiment part, since TU datasets are suffering from high standard deviation, I recommend adding more popular benchmarks such as ZINC and the OGB datasets. In addition, the running time should be reported on different benchmarks.

### Questions
See Weakness

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
The paper addresses an important problem, graph pooling, which is a key component of GNNs for graph classification tasks. The authors aim to integrate topological structural information from graphs into the pooling process. They introduce the Topology-Invariant Pooling model, demonstrating significant improvements compared to conventional pooling methods.

### Strengths
1. The idea keeping the topology information during pooling process is novel, and it can address one of the issues in GNNs in graph classification tasks.
2. The results in benchmark datasets are very good.

### Weaknesses
1. While the concept is quite promising, the implementation falls short in terms of its strength. The authors have attempted to utilize persistent homology to maintain consistent topological information during the pooling process; however, the approach they propose doesn't align with their intended outcome. To achieve their objective, the integration of persistent homology should be fundamentally different.

2. The theorem is a bit irrelevant here as the existence of a filtration function in this context does not mean much for practical purposes.

3. For classification results, it would provide more valuable insights into the performance of the proposed model if the authors compared it with State-of-the-Art (SOTA) GNN results rather than basic models. This approach would offer a more meaningful assessment of the model's capabilities.


=============== 

More specific concerns:

4. Use of PH is a bit problematic here. You are using sublevel filtration with a node function as far as I see. Since you are using single filtration, edge weights have no importance here. Therefore, the concepts of resampling and persistence injection, which involve varying the edge weights, may not align well with the method's underlying principles.

5. When employing sublevel filtration with a filtering function 'f,' it's crucial to recognize that the resulting persistence diagram does not reflect the topology of the graph itself. Instead, it depicts the evolution of topological features within the subgraphs (complexes) defined by the filtering function. As a result, the persistence diagram consists of tuples of values from your filtering function.
In the context of graph coarsening, the primary objective is to reduce the graph's size while preserving its coarse topological structure. The sublevel filtration applied to the original graph is irrelevant to this goal and holds no significance in this specific context.

6. Including dataset statistics would enhance the exposition.

### Questions
This is more of a remark than a question. The notion of introducing topological information into the pooling process is intriguing, but it does present a certain contradiction. The original graph may possess numerous topological features, yet the objective of graph pooling is to transition to a smaller, more compact graph. As a result, expecting the coarsened graph to retain similar topological information from the original one is not very meaningful, especially when using PH with sublevel filtration.

One potential solution in pursuit of this goal involves using TDA to guide the graph pooling process. However, this approach often demands a completely different filtration type, such as the Vietoris-Rips (or power) filtration, which can be computationally expensive. Balancing the desire for topological preservation with the computational cost remains a significant challenge in this context.

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors develop a model called Topology-Invariant Pooling (TIP) to improve the pooling process in graph neural network. The model is motivated by their observation that filtration process in persistent homology aligns with the graph pooling process, thus if the reduced graphs share similar topological information with the original graph, the pool process will be efficient. They characterize the topology of the graphs by using persistent homology and design a corresponding topological loss term to guide the graph pooling. They have incorporated the TIP model into a collection of graph pooling methods. The results are very promising.

### Strengths
The key innovation of the paper is the design a topology-based pooling process. Different from previous pooling process when preserving the cluster/community structure is the main focus, the TIP model is to maintain the topological similarities in terms of persistent homology information, during the graph pooling process.

### Weaknesses
Even though the authors claim that “The core of PH is the computation of filtration”, they have not provided a convincing argument of their choice of Forman-Ricci curvature as the filtration parameter. The authors state that Forman-Ricci curvature “incorporates edge weights and graph clusters to better capture the topological features of the coarsened graphs”, but this is not a sufficient justification. Forman-Ricci curvature, like other discrete Ricci curvature models, primarily captures local geometric information, and it's unclear why this is the most appropriate choice for a filtration parameter aimed at preserving global topological features. The paper lacks a discussion of alternative filtration functions and a comparison of their potential impact on the results. The notations in the paper is confusing and need to be improved. For instance, Page 3, $V={(i, x_v)}_{v\in 1:n}$, the notation {i} is redundant; $X\in R^{n*d}$, it is not explicitly stated that $d$ is the dimension of the node vector. On Page 4, for the “sequence of nested subgraphs”, the subindex is from 0 to n, which implies nodes are added one by one during filtration, which is likely not the case. On Page 5, in equation (5), the operation of min and max is not clearly defined; if it is for the elements of the matrix, the min($A^l$) will result in a scalar, not a matrix. Finally, on Page 5, in equation (6), “$D_1$” is defined as “ph()”, but on page 4, “ph()” is defined as a collection of “$D_0$”, “$D_1$”, etc. Also, $A^l$ is a matrix while $D_1[1]- D_1[0]$ is a vector, making the Hadamard product undefined.

### Questions
1)The authors use Forman-Ricci curvature as the filtration parameter and their reason is that it “incorporates edge weights and graph clusters to better capture the topological features of the coarsened graphs”. In fact, Forman-Ricci curvature is one type of discrete Ricci curvature models. The other discrete Ricci curvature model is Ollivier-Ricci curvature (thus it may be better to call it Forman-Ricci curvature instead of Forman curvature).  Essentially, all these discrete Ricci curvature models only characterize the “local” geometric information of the graph or simplicial complex. It is not sure why the authors choose to use it as the filtration parameter.

2)The authors state that “The core of PH is the computation of filtration, which presents a challenging task due to its complexity”. What is the meaning of “computation of filtration”? Is it to design a proper filtration parameter, to construct a series of simplicial complexes from the filtration process, or to calculate the persistence of homological generator from the filtration process?

3)Some notations in the paper are very confusing. For instance, Page 3, $V={(i, x_v)}_{v\in 1:n}$, why the notation {i} is needed?; $X\in R^{n*d}$, I guess $d$ is the dimension of the node vector? 

4)Page 4, for the “sequence of nested subgraphs”, the subindex is from 0 to n, this implies that nodes are added into the filtration process one by one, which is clearly not the case. To avoid the confusion, it is better to use a different way of notations.

5)Page 5, in equation (5), the operation of min and max is in terms of what? If it is for the elements of the matrix, the min(A^l) will result in a number (scale). 

6)Page 5, in equation (6), note that “D_1” is defined to be “ph()”, but in page 4, “ph()” is defined to be collections of  “D_0”, “D_1”, etc. Further, $A^l$ is defined as the Hadamard product of $A^l$ and $D_1[1]- D_1[0]$. Here $A^l$ is a matrix and  $D_1[1]- D_1[0]$ is a vector. They may have very different dimensions.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good
