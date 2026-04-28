# DeltaGNN: Graph Neural Network with Information Flow Control

- Decision: Reject
- Avg Score: 4.80
- Scores: 5, 6, 5, 5, 3

## Abstract
Graph Neural Networks (GNNs) are popular machine learning models designed to process graph-structured data through recursive neighborhood aggregations in the message passing process. When applied to semi-supervised node classification, the message-passing enables GNNs to understand short-range spatial interactions, but also causes them to suffer from over-smoothing and over-squashing. These challenges hinder model expressiveness and prevent the use of deeper models to capture long-range node interactions (LRIs) within the graph. Popular solutions for LRIs detection are either too expensive to process large graphs due to high time complexity or fail to generalize across diverse graph structures. To address these limitations, we propose a mechanism called information flow control, which leverages a novel connectivity measure, called information flow score, to address over-smoothing and over-squashing with linear computational overhead, supported by theoretical evidence. Finally, to prove the efficacy of our methodology we design DeltaGNN, the first scalable and generalizable approach for long-range and short-range interaction detection. 
We benchmark our model across 10 real-world datasets, including graphs with varying sizes, topologies, densities, and homophilic ratios, showing superior performance with limited computational complexity.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes DeltaGNN which considers the long-range node interaction via information flow control or semi-supervised node classification.
The key idea is to take use of first delta embeddings $\Delta_u^t$ and the variance of second delta embeddings $\mathbb{V}_t[\Delta_u^2]$.
If the node is connected with the same labels, then $\Delta_u^t$ tends to be some, since the features from neighbors are close to center embeddings.
If the node works as a bottleneck, then the aggregated features in each layer will have a huge difference, which might cause the big variance of $(\Delta^2)_u^t$, denoted as $\mathbb{V}_t[\Delta_u^2]$.
Based on this, information flow score is used to measure the nodes that is responsible for over-smoothing and over-squashing.
Then, with graph filtering on edges, the graph cuts edges to increase the homophily for short-range interaction, and connect the selected components for long-range interactions.
Combined with these two, the author proposes the DeltaGNN.

### Strengths
1. This paper propose an interesting idea to connect first and second delta embedding with over-smoothing and over-squashing. 
	The proposed two lemma demonstrate the relationship between them. 
	Such relationship provides insight for developing algorithm to measure and alleviate over-smoothing and over-squashing problems considering the node embeddings.
2. The proposed metric inforation flow score can numerically find the nodes that might cause over-smoothing and over-squashing in this graphs.

### Weaknesses
1. While it is good to have a numerical metric to identity the key nodes and edges for over-smoothing and over-squashing.
	The connection of heterophilic graphs in DeltaGNN to these two metric is not that strong. 
	First, it seems like heterophilic graphs is not related to solve the over-smoothing or over-squashing problem.
	Second, if using informative flow control can perfectly solve the over-smoothing or over-squashing problem, 
	why model can not get perfect results?
	In other words, why heterophilic graph is needed in this case? 
	Does the introduction of heterophilic graph will cause further questions about non-existing interactions?
	This part needs to be further justified. The motivation and experiments of the reasons to use this part need to be provided.

2. As a suggestion, some numerical experiments can be provided to demonstrate that with the information flow control, 
	the new homophilic graph can have less over-smoothing or graph bottleneck issues on real-world datasets.
	For example, the homophilic ratio of a node can be calculated and compared between the original graphs and the rewired graphs.

3. The experiments is a little weak, and more and larger graph datasets should be included like ogb datasets.

### Questions
1. What is the formulation of equation of $\Theta_t\left(\mathbf{A}^{t-1}, K(t, \theta)\right.$, Score $\left.^t\right)$ that is used to filter the graph?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work targets the prevalent issues of over-smoothing and over-squashing in GNNs. It highlights that current approaches often face challenges such as high computational complexity and lack of generalizability. To tackle these issues, the authors introduce a mechanism termed 'information flow control', which employs an innovative metric known as the 'information flow score'. This mechanism is designed to mitigate over-smoothing and over-squashing while maintaining linear computational overhead. Empirical evaluations demonstrate its superior performance under constrained computational conditions.

### Strengths
1. The suggestion in Lemma 1—that identifying nodes connected by heterophilic edges through measuring feature differences during message aggregation— appears to be constructive.
2. The introduction effectively outlines the problems of over-smoothing and over-squashing, and provides a comprehensive overview of existing methods aimed at resolving these challenges.
3. The proposed method for addressing the problems of over-smoothing and over-squashing is both innovative and promising. The approach involves decoupling the original graph into a homophilic subgraph and a heterophilic subgraph using the proposed information flow score. Subsequently, the method performs dual aggregation on these subgraphs to capture both short-term and long-term dependencies.
4. The complexity of method information flow score is superior to those of other rewiring methods.
5. The proposed method demonstrates strong performance in terms of prediction accuracy and scalability.

### Weaknesses
1. "$\triangle^t_u$ can be interpreted as the velocity at which the node embeddings are aggregated at layer t." The concept of aggregation velocity is somehow confusing. More background knowledge and explanation, also examples, are required to help readers to understand the  measurement of aggregation velocity.

2. The authors propose using $(\triangle^2)^t_u = d(\triangle^t_u - \triangle^{t-1}_u)$ to measure the rate of change in the rate at which node embeddings are aggregated. However, $\triangle^t_u$ and $\triangle^{t-1}_u$ are outputs from different layers and thus belong to different spaces. Therefore, the rationale for measuring the distance between points in these two spaces is questionable. Please provide justification for this measurement.

3. The Information Flow Control (IFC) mechanism is a core component of the proposed method. Therefore, the implementation details of the IFC mechanism, including the score hill ascent framework, should be included in the main text rather than in the appendix. As currently presented, the score hill ascent framework is difficult to follow.

4. In Figure 2, some subgraphs are difficult to interpret. For example, the 'feature density - feature value' plot and the 'score - node' plot could benefit from additional clarification or improved labeling. What do the different curves in the feature density - feature value plot represent? Additionally, the phrase 'and enhance the graph score' lacks clarity. A definition of the term 'graph score' would be helpful.

5. The proof of Lemma 1 is difficult to follow. Specific issues are detailed in the following list. **Additional background information and explanation are needed to help readers understand the proof**.
   - In line 727, the term 'valid' is used to ensure that the assignment respects the given homophily ratio $\mathcal{H}_u$. However, the concept of 'valid' is not clearly defined, and it is unclear how this term ensures compliance with the specified homophily ratio. Additional background information and explanation are needed to help readers understand these aspects.
   - The relationship between $\triangle^t_u$ and the valid assignment $s$ is not explained.
   - In the equation $U(\mathcal{H}_u)_u = \operatorname{max}_{s\in S}(\triangle^t_u)$, the representation of $U$ is unclear.
   - Due to the lack of clarity, it is not possible to understand why 'any node $u$ with $\triangle^t_u > p$ will have $\mathcal{H}_u < \mathcal{H}$.'

6. The phrase 'as this quantity depends on the homophily of the node $u$', in line 727,  requires clarification. It is not immediately apparent why this quantity should depend on the homophily of the node. A clear explanation is needed to elucidate this dependency.

7. Mirror issues: a) in line 723, should "neighbourhood $N(u)$" be revised to "neighbourhood $\mathcal{N}(u)$" to consist to notation of neighborhood? b) $\bigoplus\limits_{v \in \mathcal{N}(u)}\mathbf{M}_u$ should be revised to $\bigoplus\limits_{v \in \mathcal{N}(u)}\mathbf{M}_v$.

### Questions
1. In Table 1, it is evident that the Information Flow Score (IFS) method underperforms other rewiring methods when combined with the GIN model, unlike with other models. This discrepancy may be due to the fact that GIN uses sum aggregation, whereas other models typically use weighted mean aggregation. The sum aggregation in GIN likely results in a higher variance for $\{\sum\limits_{v \in \mathcal{N}(u)}\mathbf{M}_v \mid u \in \mathcal{V}\}$ compared to $\{\mathbf{M}_u \mid u \in \mathcal{V}\}.$  Consequently, the so-called 'aggregation velocity' depends not only on node features but also on node degrees. This suggests that the proposed method may not be well-suited for models that use sum aggregation. Is my understanding correct?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper identifies that Long-Range Interactions (LRIs) are crucial for node classification tasks. Standard GNNs struggle to capture these long range dependencies due to issues such as over-smoothing and over-squashing. To address these challenges, the authors propose information flow control, a graph rewiring mechanism. Further, the paper introduces DeltaGNN, which implements information flow control to capture both long- and short-range dependencies. The proposed method is validated on several graph datasets with varying levels of homophily and sizes.

### Strengths
* The paper is well-written and easy to follow.

* It introduces a novel connectivity measure, called the information flow score, which is supported by both theoretical analysis and empirical evidence.

* DeltaGNN demonstrates consistent improvements across various datasets, outperforming all baseline methods compared in the study.

### Weaknesses
 * DeltaGNN is proposed as a scalable approach for detecting both long-range and short-range interactions. However, there are no large-scale experiments to validate this claim, as all experiments were conducted on small graphs. It would be beneficial if the authors could report results on larger homophilic datasets, such as ogbn-arXiv, as well as on large-scale non-homophilous graphs from [1].

* The related work section does not adequately situate the current research within the context of existing GNN work based on Graph Filters (e.g., [3, 4]). Specifically, graph filters can be interpreted as a form of graph rewiring, and it is essential to discuss how the proposed information flow control mechanism relates to these methods.

* Lines 361-363 indicate that DeltaGNN is compared against state-of-the-art (SoTA) GNNs. However, GCN, GAT, and GIN are not the current SoTA for the chosen benchmarks. The authors should compare DeltaGNN with more recent GNNs (e.g., ACM-GCN+ / ACMII-GCN++ from [2]) to more accurately assess its effectiveness. Furthermore, the comparison should include methods that are known to perform well on heterophilic graphs, as the current baselines are not sufficient for this task.

* It is unclear why MLP is not included as a baseline in Table 1. MLP has been shown to outperform on the three non-homophilous datasets (Texas, Wisconsin, Cornell) as reported in [4]. A comparison against graph filter-based methods, such as GPR-GNN [3] or PPGNN [4], would provide further insights into the performance of DeltaGNN. The absence of these comparisons makes it difficult to assess the true contribution of the proposed method, especially on heterophilic graphs where simpler models can be competitive.

### Questions
* From Table 7 in the appendix, DeltaGNN variants consume approximately 2-3 times more GPU memory than GCN on small graphs. Could the authors discuss whether this would lead to memory issues when applied to larger graphs?

* Did the authors evaluate DeltaGNN on more challenging heterophilic datasets, such as Squirrel or Chameleon [3]?

*  [Minor] Typo in Line 181: "$∆^t_u$ the first" $\rightarrow$ "$∆^t_u$ be the first."

### Soundness
3

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
The paper  introduces a mechanism to mitigate over-smoothing and over-squashing in Graph Neural Networks (GNNs) by implementing an "information flow control" strategy that utilizes an "information flow score." This approach allows for effective management of node embeddings across varied graph structures, demonstrating enhanced performance in large-scale graphs while maintaining computational efficiency.

### Strengths
originality: good
quality: medium
clarity: medium
significance: medium

### Weaknesses
1. "These long-range interactions (LRIs) are crucial for node classification tasks, as they help distinguish between different classes and improve classification accuracy" This is not true. For example, graph transformers are good at capturing long-range node dependencies. However, they perform poorly on node classification tasks, especially on heterophilic graphs [1]. It is found that distant information is not always useful, and the over-globalization can cause performance degradation of graph models [2].
2. "over-smoothing is not only a topological phenomenon but is primarily a consequence of graph heterophily." There is no causal relation between over-smoothing and heterophily. As stated in [3], over-smoothing only happens in deep GNNs, but not in shallow GNNs. Heterophily will cause performance degradation to all GNN models, not matter they are deep or shallow.

### Questions
1. the information flow score, which identifies graph bottlenecks and heterophilic node interactions,

2. In definition 1, the first Delta embeddings look like the "norm" of the high-pass filtered graph signal or the neighborhood diversification[4]. The second Delta embedding is a new and interesting one.

3. So how can lemma 1 and 2 offer insights into the graph’s homophily and topology? Explain with sentences.

4. How did you get equation (2)? Why "nodes with low values of this measure are likely to correspond to regions where over-smoothing and over-squashing occur"?

5. "The long-range dependencies are then learned via a GNN heterophilic aggregation." What is "heterophilic aggregation"? Do you mean aggregation from long-range nodes in different classes? Are such long-range dependency beneficial?

6. "This concept of homophily-based interaction-decoupling is crucial to prevent over-smoothing by avoiding using a standard GNN aggregation on heterophilic edges." The "decoupling" is indeed important, for example in [4], the authors use 3-channel architectures to address heterophily. But the objective is not to prevent over-smoothing, it is to improve node distinguishability [5]. A direct proof on why and how your proposed method can improve node distinguishability is recommended.

7. Missing comparison with some SOTA models on heterophilic graphs, e.g. [4,6,7]. More comparisons on the real challenging heterophilic datasets suggested in [3] are recommended.



[1] Müller L, Galkin M, Morris C, Rampášek L. Attending to Graph Transformers. Transactions on Machine Learning Research.

[2] Less is More: on the Over-Globalizing Problem in Graph Transformers. InForty-first International Conference on Machine Learning.

[3] The heterophilic graph learning handbook: Benchmarks, models, theoretical analysis, applications and challenges. arXiv preprint arXiv:2407.09618. 2024 Jul 12.

[4] Revisiting heterophily for graph neural networks. Advances in neural information processing systems. 2022 Dec 6;35:1362-75.

[5] When Do Graph Neural Networks Help with Node Classification? Investigating the Homophily Principle on Node Distinguishability. Advances in Neural Information Processing Systems. 2024 Feb 13;36.

[6] Simplifying approach to node classification in graph neural networks[J]. Journal of Computational Science, 2022, 62: 101695.

[7] Diverse message passing for attribute with heterophily[J]. Advances in Neural Information Processing Systems, 2021, 34: 4751-4763.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces a score based on node features aggregated in a GNN layer, that aims at capturing the likelihood of a node to be responsible for oversmoothing and oversquashing. By leveraging such score in a graph-filtering pipeline, the authors propose a framework to alter the graph connectivity within a GNN scheme.

### Strengths
I think that it is valuable addressing issues like oversquashing and oversmoothing simultaneously, rather than studying them in isolation and independently of one another. I also liked the idea of leveraging "moments" from the feature distribution at different layers to guide the graph-filtering process.

### Weaknesses
There are important aspects of the submission that require reworking.

**Message and Presentation**

- In the introduction, there is often some ambiguity in the way you mention oversmoothing and oversquashing, as if they were interchangeable concepts. This is not the case, and should be emphasized. Oversmoothing is a problem that occurs for *some* GNNs and is independent of the topology (as a phenomenon, not how quickly that occurs) and is somewhat orthogonal to long-range interactions since in the limit of many layers, node features become indistinguishable irrespectively of their distance. Oversquashing instead, is an issue that occurs for *all* 1-hop GNNs and is very much dependent on the topology (namely, their commute time) and hence affects long-range interactions, independent of the depth or the ability to capture local interactions.
- Even more significantly, you keep overlapping the issue of oversmoothing with that of heterophily (for example Line 110, Line 121, Line 161 but this notion is repeated throughout the paper). This is wrong. While Definition 2.1 accounts for the labels, this to me represents more of a choice, as oversmoothing is the convergence of node features to the same representation over a connected component of the graph. As such, it is actually simply caused by low-frequencies dominating over high-frequencies in the graph spectrum. In fact, it can be mitigated or avoided by relying on architectures that do not operate via low-pass filters. I suspect that what you are implying here, is that oversmoothing becomes more of an issue in the presence of heterophily, as nodes with different labels become indistinguishable, but *this is a consequence of and not the cause of oversmoothing and should be rectified*.

- Quite a few citations are missing in the related work, for example regarding rewiring [1,2,3] but also Graph-Transformers.. 
- The presentation of the framework is a little contrived (see my questions below). Also, while you try to distinguish yourself from graph-rewiring algorithms, your approach removes edges, and this is a key part of it. For this reason, I think it is a little misleading to distinguish yourself from graph rewiring techniques. You should be more specific, and mention that the rewiring is adaptive and based on GNN layer outputs more than topological connectivity measures.

**Theory**

- I am a little confused by Lemma 1. To me, the homophily of a node only depends on the label information and the topology and has nothing to do with the architecture being used and/or the features. This indeed seems to be reflected also in your Definition 2.2 where I am reading that $\Phi$ can be taken to be the ground-truth label assignment. However, it seems that in Lemma 1 you are deriving the homophily of a node based on what can be mapped/separated from the node features, i.e. it has more to do with distinguishability from node features. If so, this should be clearly emphasized. As such, I would not really talk about homophily but node features separability.

- I don’t think that Lemma 2 is an actual Lemma since your proof is essentially a discussion based on  the results of Nguyen et al. You should remove the statement and replace it with a discussion based on what you have in the appendix. As it stands, I find it confusing and indeed informal, to a point that this is not a mathematical statement.

- In light of my comments regarding Lemma 2, I don’t think that your score definition is that well motivated. More precisely, I can see why the denominator makes sense in relation to oversmoothing, since it measures node features separability after rounds of message passing (and *not* homophily), but I struggle to see how the numerator relates to oversquashing. You should expand on the “proof” from Lemma 2, which is not really a proof, to better motivate this score.

**Experiments**

Evaluation is not  convincing. On all the benchmarks you used, it is highly debatable that long-range interactions are present at any level. In fact, I believe majority of people would argue that LRIs are not present on Cora, Pubmed, etc.. Additionally, datasets like Texas, Wisconsin, etc are known to have several issues and the community has proposed alternative options. I personally struggle to accept claims of “state of the art improvements by 1 %” on the likes of Cora and Pubmed this day. Graphs like Cornell, Texas and Wisconsin are also extremely small and super sensitive to tuning. The paper overall proposed a methodology, and as such, should be thoroughly tested on more relevant benchmarks.

### Questions
- Equation (1) is not the most general way of writing a 1-hop GNN aggregation, as there is no residual term. Namely, one would typically expect $\phi$ to take two arguments i.e. $(\mathbf{X}_u^t, \bigoplus...)$
- Line 159: The expression “embedding agnostic” is a little vague to me, so perhaps you can specify a little more clearly what you are implying here.
- Line 285: What is a “homophilic GNN”?
- The paragraph 283-291 uses too many vague words and is all but clear. For example, line 288-289, what would an “heterophilic graph condensation” be? 
- Line 330–331: How can removing edges that are bottlenecks necessarily reduce oversquashing? What if now you have disconnected components? This process can only work if one identifies correctly node labels, but this is something that your algorithm in general cannot know in advance.

### Soundness
2

### Presentation
2

### Contribution
2
