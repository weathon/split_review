# Link Prediction with Relational Hypergraphs

- Decision: Reject
- Avg Score: 6.50
- Scores: 6, 6, 8, 6

## Abstract
\vspace{-1em}
Link prediction with knowledge graphs has been thoroughly studied in graph machine learning, leading to a rich landscape of graph neural network architectures with successful applications. Nonetheless, it remains challenging to transfer the success of these architectures to  \emph{relational hypergraphs}, where the task of link prediction is over \emph{$k$-ary relations}, which is substantially harder than link prediction with knowledge graphs.
In this paper, we propose a framework for link prediction with relational hypergraphs, unlocking applications of graph neural networks to \emph{fully relational} structures. Theoretically, we conduct a thorough analysis of the expressive power of the resulting model architectures via corresponding relational Weisfeiler-Leman algorithms and also via logical expressiveness.  Empirically, we validate the power of the proposed model architectures on various relational hypergraph benchmarks. The resulting model architectures substantially outperform every baseline for inductive link prediction, and lead to state-of-the-art results for transductive link prediction.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a new method for link prediction in relational hypergraphs, where the task focuses on k-ary relations. It first investigates the expressive power of existing GNNs for relational hypergraphs, and then introduces the hypergraph conditional message passing neural network (HC-MPNN) by utilizing and extending the techniques from conditional message passing neural networks (C-MPNNs) (Huang et al., 2023). The HC-MPNN is further extended to an inductive setting, and show good experimental results.

### Strengths
1. The paper is written in a good structure. Although the definition of the relational hypergraph is a little bit complex; the descriptions in the paper is not difficult to understand. The organization of the paper is good. From the theoretic analysis to model improvement, the techniques are quite clear.

2. Extending the C-MPNN and HR-MPNN to HC-MPNN is technically sound. And the extension to inductive link prediction is interesting.

3. Both theoretic analysis and experiments are comprehensive. It has with both inductive and transductive settings, and the analysis of the initialization and positional encoding is also useful.

### Weaknesses
1. First, I have a concern about the practicality of the method. From my understanding, the relational hyperedge is just like a sentence, and it has fixed directions and positions for entities. So, why do not people just use Transformers for NLP by regarding the relational hyperedge as a sentence? And the query based approach is just like a BERT-based model? I do not see much benefit from modeling it as a hypergraph. I am actually curious to see the results of BERT on the same datasets if possible. Specifically, the paper does not adequately address why a hypergraph approach is fundamentally superior to sequence-based models for this task, given that the relational hyperedges have a clear sequential structure. The positional information and fixed arity of relations seem directly amenable to sequence modeling techniques, and the paper lacks a clear explanation of the limitations of such approaches in this context.

2. Second, although the paper is technically sound and the analysis is complete/rigorious; but every step in the model is not surprising and a little bit trivial. Without the analysis part, the HC-MPNN is like just a migration of C-MPNN to hypergraphs. The inductive link prediction part is more interesting. The core message passing mechanism, while extended to hypergraphs, appears to be a straightforward adaptation of existing techniques. The novelty of the approach is not immediately apparent, and the paper could benefit from a more detailed discussion of the specific challenges in extending C-MPNN to hypergraphs and how the proposed method overcomes these challenges in a non-trivial way.

3. I do not fully understand the training. Since the message passing is query dependent, there must be a lot of queries in the training data. How do you select such queries for training? And for each query, the node representation is different, does not it increase the computational complexity a lot?

### Questions
1. Does a relational hyperedge have a fixed number of entities? For example, can we have r(e1, e2) and r(e1, e2, e3) at the same time? 
2. How to train the model with queries?

### Soundness
2

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
4

### Summary
The authors first give an understanding of the expressive power and limitations of HR-MPNNs and propose the HC-MPNN structure based on HR-MPNN. Compared with current HR-MPNN models, the HC-MPNN structured model HCNet carries out a novel query-specific node initialization method. With the Weisfeiler-Leman test, the author proves that this model can better model isomorphic nodes since it maintains a better expressiveness than the HR-MPNN structured models in the relational hypergraphs.

### Strengths
S1. Clear and well-organized presentation of the whole paper.

S2. Solid proof of the theoretical expressiveness of the proposed method.

S3. Available code.

S4. Transductive experiments have been added.

### Weaknesses
Unfortunately for the authors, I am the reviewer who held a negative opinion on this paper for NeurIPS 2024. Here, I summarize my previous negative feedback:

**Major Concerns:**

C1. The theoretical proof in this paper is unrelated to the inductive setting. Previously, I hoped the authors would compare more transductive settings. This time, **Table 2 has addressed this concern quite well**. Thus, I decided to raise my score.

C2. I previously argued that hyper-relational graphs and relational hypergraphs can be converted with small tricks, which is why many prior studies conducted experiments on datasets like WD50K, WIKIPEOPLE, JF17K, and FBAuto. Therefore, I also suggested that the authors consider experimenting on other hyper-relational graphs. However, the authors hold a different view, and the explanation provided in lines 145-153 is not sufficient to alleviate my concern. Thus, I will retain my suggestion for this submission and discuss it further with other reviewers.

**Minor Concerns:**

C3. Many of the methods presented in Table 1 were published in or before 2020, which may imply that the inductive setting is not currently a major research focus. The authors may need to emphasize the significance of the inductive setting more in the paper.

### Questions
I would like the authors to continue discussing the disagreement over C2, explaining why they insist that relational hypergraphs and hyper-relational graphs have irreconcilable differences. In my view, even if their structures are not identical, small modifications could allow format conversion. The benefits of doing so include:

	1.	Making the proposed method more generalized and applicable to a broader range of scenarios.
	2.	Aligning with many previous studies in the field.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces HC-MPNNs, a novel GNN architecture for link prediction on relational hypergraphs, achieving state-of-the-art results in both inductive and transductive tasks. While highly expressive, the model faces scalability challenges due to its computational complexity.

### Strengths
- **Innovative Approach**: The paper introduces Hypergraph Conditional Message Passing Neural Networks (HC-MPNNs), which generalize existing GNN architectures and target the complex task of k-ary link prediction on relational hypergraphs, moving beyond traditional binary link prediction tasks.
- **Theoretical Rigor**: The authors provide a detailed analysis of HC-MPNNs' expressive power through Weisfeiler-Leman tests and logical expressiveness, which significantly adds to the theoretical foundation of GNNs on hypergraphs.
- **State-of-the-Art Performance**: Empirical results demonstrate that HC-MPNNs outperform existing models for both inductive and transductive link prediction tasks across multiple datasets, showcasing substantial improvements.

### Weaknesses
 - **Computational Complexity**: The paper acknowledges that the proposed HC-MPNNs may be computationally intensive, particularly for large hypergraphs. An in-depth analysis of the computational costs compared to baseline models is needed to assess scalability better. Specifically, the paper lacks a detailed breakdown of the time and space complexity for each step of the HC-MPNN algorithm, such as message passing, aggregation, and update functions, making it difficult to pinpoint the bottlenecks. Furthermore, a comparison of the computational costs with baseline models should include not just execution time, but also memory usage and the scaling behavior with increasing hypergraph size and arity.
- **Limited Scope**: The model is focused solely on link prediction. Exploring its applicability to other tasks, such as node classification or hypergraph-based query answering, would provide more versatility and impact. The current evaluation is limited to link prediction, which does not fully demonstrate the potential of the proposed model. The paper should discuss how the model could be adapted to other tasks, such as node classification, clustering, or hypergraph partitioning, and what modifications would be necessary. This would broaden the impact of the work and show its generalizability.
- **Assumptions on Data Structure**: The approach assumes that hypergraph structures are available and complete, which may not always be feasible in real-world scenarios. The limitations of applying this method to noisy or partially observed hypergraphs are not discussed. The paper does not address the sensitivity of the model to missing or incorrect hyperedges. In real-world scenarios, hypergraph data is often incomplete or noisy, and the model's performance under such conditions is unclear. The paper should include a discussion on how the model might be affected by such data quality issues and potential strategies to mitigate these effects.

### Questions
- **Expressiveness Limitations**: Could the authors provide more details on situations or graph structures where the expressive power of HC-MPNNs might fall short, even with the enhanced encoding?
- **Impact of Hypergraph Structure**: How does the structure or density of a hypergraph affect the model’s performance, especially in cases of sparse or highly connected hypergraphs?
- **Generalization to Noisy Data**: How robust is HC-MPNN to noisy or incomplete hypergraph data, and are there mechanisms in place to handle such cases?
- **Positional Encoding Variants**: The ablation studies show sinusoidal positional encoding as the best choice. Could the authors elaborate on why this is effective in hypergraph contexts compared to other embeddings?
- **Use of Meta-Paths**: Given that meta-paths are important structures in relational (non-hypergraph) graphs [1, 2, 3], could there be advantages to incorporating them in hypergraph contexts?
- **Scalability of the Model**: Is the model feasible to apply in very large-scale hypergraphs (e.g., millions of nodes)? 

[1] Seongjun, Y. et al., Graph Transformer Networks: Learning meta-path graphs to improve GNNs, 2022

[2] Ferrini, F. et al., Meta-Path Learning for Multi-relational Graph Neural Networks, LOG 2023

[3]Fu, Xinyu, et al. "Magnn: Metapath aggregated graph neural network for heterogeneous graph embedding." Proceedings of the web conference 2020. 2020.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work proposes HCNet, which extends state-of-the-art NBFNet and C-MPNN of conventional graph for link prediction to relational hypergraphs for hyper-relation predictions. It first follows the schema of conventional graph neural network works, defines the invariance under relational hypergraph and proves the expressivity of their proposal using proposed WL test for relational hypergraph. Then, it follows the schema of knowledge graph works, proves that the logical reasoning ability of HCNet is same as grade model logic on hypergraph. Besides, this work achieves better empirical results on relational hypergraph benchmarks.

### Strengths
- This works have concrete theoretical justifications on both graph representation and knowledege graph domains including WL test (for relational hypergraph) and power of logical reasoning.
- The empirical result looks pretty good in compare to related works on relational hypergraph baselines.

### Weaknesses
 - Although this work made enough refinement to adpat NBFNet and C-MPNN design onto relational hypergraph, there isn't significiant novelty introduced in the refinement: they are simply directly replace the concepts from conventional graph to relational hypergraph.
- For logical reasoning, I believe it should focus more on explainability to people, but the concept of graded modal logic for hypergraph (the definition and examples) in this paper is too abstract for people to understand their power. I think more evidence of HGML should be provided (in appendix), e.g., is it able to represent all logics or answer all logical queries on relational hypergraph? If not, what's the limitation?
- Since this is a neural network work and link prediction work (where negative sampling is necessary), they will be a lot randomness in experiments, thus it is essential to provide confidence interval at least to your works (I understand that some baselines do not have confidence interval).


### Questions
- I am not familiar with the background of link prediction on relational hypergraph, thus I have questions to the necessity of this problem: It seems that the hyper relation prediction can be decomposed into prediction over a relational path or subgraph, and all three benchark you used seems to built from conventional knowledege graph, thus I am wondering is there a real-world dataset or task where only relational hypergraph methods can handle, and can not be decomposed into conventional relational graph methods?
- Since your method is transductive on relations, can we simply treat each relation as an independent node, and use the hyper relation position as edge attribute between a node and the relation node (e.g., $r(u_k)$ becomes $u_k \overset{k}{\leftrightarrow} r$), thus we can convert this task into a classifition task over multiple edges on conventional graph? Is there any baselines corresponding to this idea?
- Is the order essential in hyper relations? I think it is possible to permute some node positions while not hurts the hyper relation? If so, isn't your definition too strict?
- I think predicting the relation also falls into link prediction catalog, but your link prediciton only focuses on nodes, is it defined only for this work?
- In refinement, I think you want to define $\xi$ is more expressive than $\xi'$ (can distinguish more cases), thus isn't $\xi' \prec \xi$ better than $\xi \prec \xi'$ in representing which one is more expressive?
- How is your method runtime in real-world training and inference? NBFNet is already expensive since the graph convolution has to be redo if the query change, and in your case, hyperedge may introduce exponential increase on the amount of neighbors.

### Soundness
3

### Presentation
3

### Contribution
2
