# DIRECTIONALITY IN GRAPH TRANSFORMERS

- Decision: Reject
- Avg Score: 4.25
- Scores: 3, 5, 3, 6

## Abstract
We study how one can capture directionality in graph transformers, for learning over directed graphs. Most existing graph transformers do not take edge direction into account. We therefore introduce a novel graph transformer architecture that explicitly takes into account the edge directionality. To achieve this, we make use of dual encodings to represent both potential roles, i.e., source or target, of each pair of vertices linked by a directed edge. These dual encodings are learned by leveraging the latent adjacency information extracted from a novel directional attention module, localized with $k$-hop neighborhood information. We also study alternative approaches to incorporating directionality into other graph transformers to enhance their performance on directed graph learning tasks. To evaluate the importance of edge direction, we empirically characterize via randomization whether direction really matters for the downstream task. We propose two new directional graph datasets where direction is intrinsically related to learning. Via experiments on directional graph datasets, we show that our approach yields state-of-the-art results.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces Directed Graph Transformer (DiGT), a novel graph transformer architecture that effectively addresses the challenge of analyzing directed graphs. DiGT incorporates edge direction and graph connectivity as integral elements within the Transformer framework, enabling it to dynamically learn dual node encodings that capture the directionality of edges. Experimental results demonstrate that DiGT significantly outperforms state-of-the-art graph neural networks and graph transformers in directed graph classification tasks, particularly when edge directionality is a crucial aspect of the data.

### Strengths
1) Exploring the utilization of graph transformers to encode the directed information within graphs is a promising avenue of research.
2) DiGT, as an approach that leverages a graph transformer to encode directedness, shows promise, and the experimental results provide evidence of its effectiveness to a certain extent.

### Weaknesses
1) The three modules of DiGT are all based on heuristic methods, lacking some theoretical explanations and insights. Specifically, the method for generating the dual node encodings, while inspired by HITS, lacks a rigorous mathematical justification for its specific formulation within the transformer architecture. The learnable adjacency matrix, while flexible, introduces additional complexity without a clear theoretical understanding of how it interacts with the attention mechanism to capture directedness.
2) DiGT contains many linear layers and learnable parameters, making it quite complex. While the author briefly describes the complexity of DiGT in Appendix F, I recommend conducting a more detailed theoretical analysis and empirical validation. For example, a study of the parameter sensitivity and the impact of different initialization schemes on the model's performance would be beneficial. Furthermore, the computational cost of the model, especially in comparison to simpler baselines, should be more thoroughly investigated.
3) In the experiments, the author mentions abandoning the use of some available datasets because they think the directionality of these datasets is unimportant. I don't entirely agree with this viewpoint. I think that even if directionality is not crucial, if a model can encode directionality, it should still yield some benefits. The model should be evaluated on a wider range of datasets, including those where directionality is less prominent, to fully understand its capabilities and limitations.
4) Some important baselines were not compared in the experiments. For example, the method proposed in the paper "Transformers Meet Directed Graphs [1]" achieved the SOTA result on Ogbg-Code2.

### Questions
Please refer to the aforementioned weaknesses.

### Soundness
2 fair

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a directional graph transformer that utilizes dual encodings to represent the different roles of source or target of each connected node pair. The dual encodings are acquired through the utilization of latent adjacency information, which is extracted using the directional attention module localized with k-hop neighborhood information. Additionally, the paper introduces alternative methods for incorporating directionality within the Transformer architecture. In the experimental study, the paper examines the role of directionality in current datasets, and proposes two new directional graph datasets. By conducting a comparison on directional graph datasets, the authors demonstrate that their approach achieves state-of-the-art results.

### Strengths
1. The work introduces a method that does not fully rely on the explicit directed graph structure, which allows the central node to receive extra information from non-neighbors. At the same time, the positional encodings and the k-hop localization ensure that the attention scores do not deviate too much from the original data structure.

2. The proposed model outperforms GT and GNN alternatives on five reported datasets. It also surpasses the other directional GTs on three out of five datasets. 

3. The paper provides two new datasets that offer new benchmarks to evaluate directional graph modeling.

### Weaknesses
1. How the learnt attention scores are related to the original graph structure or the edge directions is not fully revealed (probably can be done by visualization and comparison).

2. Some designs are not well justified by either theoretical or empirical evidence. For example, the design of the positional encoding. No illustration, for instance, unidirectional counterparts or theoretical justification, has been provided about why the design is suitable for the directional situation.

3. The computational complexity of the proposed model appears high. It may have scalability issues when applied to large datasets.

### Questions
1. Would it be possible to include some node-level experiments to further examine the capability of the model? There are a few commonly used benchmark datasets with directed graphs for node level tasks, e.g., Actor. Are such graph datasets too large for the proposed model to handle?
 
2. Based on the recent literature, [1] also presents a positional encoding design tailored for directed graph Transformers. It would be valuable to see a comparative evaluation of your proposed model with this work.
 
[1] Geisler, Simon, Yujia Li, Daniel J. Mankowitz, Ali Taylan Cemgil, Stephan Günnemann, and Cosmin Paduraru. "Transformers meet directed graphs." In International Conference on Machine Learning, pp. 11144-11172. PMLR, 2023.

### Soundness
2 fair

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes Directed Graph Transformer (DiGT), a global self-attention transformer specialized in encoding directed networks via dual node embeddings for source and target representations, learnable implicit adjacency information via directed attention, and k-hop neighborhood localization. For experimentation, the paper first explores the directionality of existing directed graph classification datasets by performing a random flip test, from which it finds that directionality is not a crucial factor in most datasets. Due to such limitation, the paper synthesizes two novel datasets, FlowGraph and Twitter, where the graph label is explicitly related to the edge direction pattern. Experiments on these datasets show that DiGT attains best performance across various message-passing GNN and graph Transformer baselines.

### Strengths
- [S1] Developing a Transformer architecture for learning directed graphs is a fairly underexplored topic, yet there is a clear demand in the community due to datasets where directionality occurs naturally.
- [S2] The overall methodology behind DiGT is well-written with great detail.

### Weaknesses
 - [W1] **There are some questionable design choices in DiGT that seemingly contradict with the overall direction, yet are missing additional explanations.** 
  - In particular, the end of Section 2 mentions how directed message-passing GNNs "suffer from convolutional inductive bias... restricted to only the given neighborhood structure", yet DiGT uses attention that is localized to the k-hop neighborhood. Doesn't this essentially downplay the advantage GTs have over message-passing GNNs? 
  - Also, the end of Section 3 mentions that "DiGT uses dual node embeddings in all layers", but Equations (9) and (10) imply that dual embeddings do not remain dual throughout the encoder, but are instead merged together into a single embedding $\mathbf{Y} \in \mathbb{R}^{n \times d_p}$, then separated via linear layers $L_{VS}$ and $L_{VT}$ once every layer. Why is this the case? Furthermore, the commutativity of vector addition in Equations (9) and (10) means that the source and target embeddings are summed before being passed through separate linear layers, which would lose information on the ordering of the two embeddings. Specifically, the operation $L_{VS}(S+T)$ is equivalent to $L_{VS}(T+S)$, and thus the model cannot distinguish between which node is the source and which is the target after this operation. A more appropriate way to fuse the embeddings while preserving the source/target ordering would be to fuse the embeddings via  $S' = S+ L_{VS}(T)$ (similar to feature fusion in [A]), instead of $S' = L_{VS}(S+T)$ which is used in the presented work.
- [W2] **The experimental setup is unconvincing.** 
  - The paper claims that directionality does not play a significant role in existing datasets, proceeds by proposing synthetic datasets, and then performs graph classification on those networks instead. However, the first observation in Table 1 is not really comprehensive (experiments are only shown with certain model-dataset pairs), and the numbers do not necessarily overlap in standard deviation, which then leads to the question of "Are these results truly indicative of directionality not playing a significant role in these datasets?". Furthermore, while the authors refer to Tables 6 and 7 in the appendix, I believe they meant Tables 3 and 4 since Tables 6 and 7 pertain to another experiment. Regardless, these results still do not cover all model-dataset settings and the numbers still are not really convincing. 
  - The pipeline used to generate the Twitter datasets also seems problematic, due to how the label of each graph is chosen. Specifically, Twitter5 has 5 labels, each corresponding to the perturbation rate in [0, 25, 50, 75, 100]% used to rewire or reverse each edge in the original ego-network. Then for the experiments in Table 1, randomly flipping 50% of the edges in a Twitter5 graph labeled 1 (originally perturbed by 25%) would return a graph that is equivalent to a graph labeled 3 (originally perturbed by 75%) with no edge-flipping. In essence, it is unclear whether the drop in performance shown in Table 1 is simply due to having noisy labels, rather than the dataset exhibiting significance on directionality.

### Questions
- [Q1] **Details on number of parameters.** Could the authors clarify the exact number of parameters used for each model in Table 2? Due to its dual attention mechanism, I suspect DiGT would use more parameters compared to other models if using the same number of layers. Having the model sizes alongside performance metrics would help clarify whether the performance gains are due to the proposed mechanisms, and not due to having more parameters.
- [Q2] **Missing results for Malnet-tiny of Tables 2 and 3.** Are these all blank due to out-of-memory issues? If so, it would be better to fill them in with OOM.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Summary: This paper focuses on directionality of edges in graphs and introduces a new graph transformer architecture called DiGT that explicitly models edge directionality in directed graphs. The key ideas are: i) Dual node representations to capture source and target roles; ii) Directionality incorporated via asymmetric attention and dual query/key matrices, and iii) Localization via k-hop neighborhood attention.

Contributions:
- Proposes DiGT, a transformer that uses dual node encodings and directional attention to capture directionality.
- Introduces strategies to make other graph transformers directional via asymmetric/dual attention.
- New directional graph datasets where direction correlates with labels.
- Shows superior performance over GNNs and graph transformers on directional benchmarks.

### Strengths
Strong Points:
- Dual node encodings in DiGT elegantly capture directionality throughout the model.
- Directional attention neatly exploits query/key asymmetry for modeling direction.
- DiGT significantly outperforms baselines on directional graphs.
- Quantifies dataset directionality via entropy measure.
- New directional graph datasets enable better evaluation, although it may be biased in the context of this work.

### Weaknesses
Weaknesses and Questions:
- While dual encodings are powerful, they double model size. Could this be optimized?
- Although computational limitation of the proposed architecutre is discussed briefly, the runtime complexity is quadratic in number of nodes like vanilla transformers. If sparsity helps, how would the complexity differ for DiGT compared to other non-directional graph transformers?
- Are there other ways to quantify directionality of graphs besides SCC entropy?
- A closely related work "Edge Directionality Improves Learning on Heterophilic Graphs", Rossi et al., 2023, is not discussed in this work which would be important and provides (i) necessary context on novelty (ii) applicability of DirGNN on vanilla GTs.

### Questions
included together with weaknesses

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
