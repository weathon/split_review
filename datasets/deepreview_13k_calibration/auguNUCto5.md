# Boosting Temporal Graph Learning From Global and Local Perspectives

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 6, 6, 5

## Abstract
Extensive research has been dedicated to learning on temporal graphs due to its wide range of applications. Some works intuitively merge GNNs and RNNs to capture structural and temporal information, while recent works propose to aggregate information from neighbor nodes in local subgraphs based on message passing or random walk. These methods produce node embeddings from a global or local perspective and ignore the complementarity between them, thus facing limitations in capturing complex and entangled dynamic patterns when applied to diverse datasets or evaluated by more challenging evaluation protocols. To address the challenges, we propose the Global and Local Embedding Network (GLEN) for effective and efficient temporal graph representation learning. Specifically, GLEN dynamically generates embeddings for graph nodes by considering both global and local perspectives. Then, global and local embeddings are elegantly combined by a cross-perspective fusion module to extract high-order semantic relations in graphs. We evaluate GLEN on multiple real-world datasets and apply several negative sampling strategies. Sufficient experimental results demonstrate that GLEN outperforms other baselines in both link prediction and dynamic node classification tasks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper discusses the limitations of existing methods in temporal graph learning, which either focus on global or local perspectives but not both. To overcome this, the Global and Local Embedding Network (GLEN) is proposed. GLEN dynamically generates node embeddings by considering both global and local information. These embeddings are then fused using a cross-perspective module to capture high-order semantic relations. GLEN has been evaluated on multiple datasets and outperforms baselines in tasks like link prediction and dynamic node classification.

### Strengths
S1. Temporal graph is an important problem to address in practical world, yet majority of the research deals with static graphs only.

S2. The analysis of existing RNN-based work and random walk/message passing models provides useful insights.

S3. The writing/organization of the paper is generally clear, although some parts need more clarification. (See W2)

### Weaknesses
W1. The proposed model, while technically valid and sound, is not sufficiently novel or exciting. Combining local and global perspectives are common ideas in graphs. Even on temporal graph, point process based modeling aims to capture the graph-wide evolution pattern from  a global perspective, such as (Lu et al., 2019) and the below paper [a]. A detailed discussion on temporal point processes for temporal graph is warranted, potentially with additional experimental comparison.

[a] Trend: Temporal event and node dynamics for graph representation learning. WWW 2022.

W2. Certain parts in the motivation of the paper are not clearly explained. For example, the following sentences:
"Pairwise interactions observed in different graphs or even the same temporal graph typically have different temporal properties."
"Since the endogenous and exogenous factors driving the generative process ..." 
I'm not exactly sure how they directly connect to or motivate the proposed method.

W3. In Table 2, Random tends to perform the best compared to historical/inductive strategies. It is surprising and more discussion is needed. (Also, I'm not confident of the results in Table 2, as it has some discrepancy with the results in Table 3 -- e.g. for UCI, the results in Table 2 and Table 3 are different.

### Questions
Please see Weaknesses.

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
This paper introduces a novel Global and Local embedding Network (GLEN) for temporal graph representation learning, which captures both local and global information. Specifically, GLEN first generates both local and global embeddings, and then combine these embeddings via cross-perspective fusion module. The proposed GLEN is evaluated on several real-world datasets.

### Strengths
1. The idea of local embedding and global embedding is novel and interesting. For a given window of the temporal graph, GCN is used to extract node embeddings for each time stamp. TCN is used to capture global node embeddings, and a temporal interval weighting module is used over a restricted neighborhood to capture the local embeddings. In the end, the local and global embeddings are combined via a cross-perspective fusion module.
2. The proposed method could significantly outperform SOTA temporal graph embedding methods on several benchmark datasets, and the ablation study demonstrates that each of the proposed component is crucial for model's performance.
3. The writing of the paper is clear in general.

### Weaknesses
 1. The motivation of the cross-perspective fusion module needs further clarification. Why do you use the global embedding as the query but not the local embedding? Why not (1) use global embedding as query to obtain z1, (2) use local embedding as query to obtain z2 and (3) combine z1 and z2? It's not immediately clear why the global embedding should act as the query, given that the local embeddings are designed to capture fine-grained temporal information which might be more suitable for querying the global context. The current approach seems to prioritize the global view, potentially overlooking the nuanced details captured by the local embeddings. A more thorough justification for this design choice is needed, especially considering alternative fusion strategies.
 2. What will happen if you only use the local embedding module but without restricting the size of neighbors? The paper mentions restricting the neighborhood size for the local embedding module, but it doesn't explore the impact of removing this restriction. It's important to understand how the model behaves when considering all historical neighbors, as this could reveal whether the restriction is truly necessary or if it introduces a bias. The computational cost argument is not sufficient without empirical evidence of performance degradation or instability when using the full neighborhood. The potential for capturing more comprehensive local context by considering all historical neighbors should be investigated.
 3. Some details need further improvement.
(1). What are $\hat{y}_0, \hat{y}_1,\dots$? (Between Eq. (8) and Eq. (9))
(2). $\mathbf{h}_v^{(0)} = \mathbf{s}_v^{(t)}+\mathbf{x}_v^{(t)}$?

### Questions
Please refer to weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper propose GLEN, an adventurous method for effective and efficient temporal graph representation learning. GLEN can generates embeddings for graph nodes by considering both global and local perspectives. Sufficient experimental results demonstrate that GLEN outperforms other baselines in both link prediction and dynamic node classification tasks.

### Strengths
1.	The paper clearly explain the motivation of the idea combining global and local perspectives in temporal graph representation learning, and the reason to use RNN-TCN and TGN correspondingly.
2.	The experiments in this paper are comprehensive, and they provide ample evidence of the model's superiority in terms of performance and efficiency.

### Weaknesses
1.	In the specific components of the model, many aspects are not novel. For example, RNN-TCN and TGN are both derived from previous works. In Cross-Perspective Fusion Module, this module is a common transformer.

2.	I still have some doubts regarding the use of RNN-TCN for extracting global information. Both GCN and TGN employ similar information aggregation approaches, aggregating nodes up to n-hops away. Why is RNN-TCN considered to be more effective in representing global information?

### Questions
See “Weaknesses”

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper focuses on temporal graph representation learning. Different from exiting works that utilize GNN-RNN frameworks or local subgraph information to learn effective node representations, this paper proposes to generate node embeddings by considering both global and local perspectives. Specifically, GCN-TCN is utilized to encode global graph information; TGN is used to model local graph information; Then, self-attention mechanism is employed to aggregate node representations from both global and local embeddings. Experimental results on seven datasets demonstrate that the proposed model can achieve satisfied performance on both link prediction and node classification tasks.

### Strengths
1)	This paper investigates temporal graph representation learning, which is an important topic in the graph community.
2)	Various ablation studies are given to show the effectiveness of the proposed components.
3)	Time complexity analysis is given, and model efficiency analyses are also presented in the experiment section.

### Weaknesses
1) The technical contribution of this paper is quite limited. The three components in this paper are all from existing works. The global module is from TCN, and the local module is from TGN. The cross-perspective fusion is a self-attention module. No new module is proposed. The paper claims novelty in combining these components, but the combination itself is straightforward and lacks significant technical depth. The global module uses GCN-TCN, which is a relatively standard approach for processing sequential graph data, and the local module leverages TGN, which is already a well-established method for learning dynamic graph embeddings. The fusion module simply applies a self-attention mechanism, which is also a widely used technique. The lack of novel architectural components or algorithmic contributions is a significant weakness.
2) In the cross-perspective fusion module, it is not clear why query $Q_i$ is the linear projection of $Z^{Global}$. What if we use $Z^{local}$ to generate $Q_i$? In this case, $\tilde{z}$ is the weighted combination of $Z^{global}$ and $z_u = FFN(\tilde{z}_u \Vert z_u^{local})$. More ablation studies should be conducted. The choice of using the global embedding as the query and the local embedding as the key and value is not sufficiently justified. It is unclear why this specific configuration is superior to using the local embedding as the query, which might allow the model to focus on fine-grained temporal information. The paper should provide more detailed analysis on the impact of this design choice and explore alternative configurations.
3) In Table 2, it is not clear why the performance of GraphMixer and TIGER are missing in the setting of historical and inductive negative sampling. The absence of these results makes it difficult to fully assess the performance of the proposed model against existing baselines under these conditions. The paper should address this gap in the experimental evaluation and provide a more comprehensive comparison with all relevant baselines.
4) There are lots of other manners to combine both the global and local perspectives. For instance, $z_u$ is directly generated by concatenating $Z^{local}$ and $Z^{global}$. $z_u$ can also be aggregated with simple attention mechanism instead of self-attention. The paper does not adequately explore alternative fusion methods. While the self-attention mechanism is a reasonable choice, the paper should justify why it is the most effective approach compared to other simpler methods such as concatenation or weighted summation using learned weights. The lack of exploration of these alternatives weakens the analysis.
5) In Equation 10, what if some of the nodes do not have $|\mathcal{N}|$ neighbors? Are there any strategies to handle this situation? The paper does not discuss how the model handles nodes with fewer than $|\mathcal{N}|$ neighbors, which is a common occurrence in real-world graphs. The absence of a clear strategy to handle this situation raises concerns about the robustness and applicability of the model.

### Questions
1)	In Table 2, it is not clear why the performance of GraphMixer and TIGER are missing in the setting of historical and inductive negative sampling. 
2)	There are lots of other manners to combine both the global and local perspectives. For instance, $z_u$ is directly generated by concatenating $Z^{local}$ and $Z^{global}$. $z_u$ can also be aggregated with simple attention mechanism instead of self-attention.
3)	In Equation 10, what if some of the nodes do not have $|\mathcal{N}|$ neighbors? Are there any strategies to handle this situation?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
