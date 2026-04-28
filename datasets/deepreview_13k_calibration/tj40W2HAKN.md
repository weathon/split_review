# Node-wise Filtering in Graph Neural Networks: A Mixture of Experts Approach

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 6, 3, 5, 6

## Abstract
Graph Neural Networks (GNNs) have proven to be highly effective for node classification tasks across diverse graph structural patterns. Traditionally, GNNs employ a uniform global filter—typically a low-pass filter for homophilic graphs and a high-pass filter for heterophilic graphs. However, real-world graphs often exhibit a complex mix of homophilic and heterophilic patterns, rendering a single global filter approach suboptimal.  In this work, we theoretically demonstrate that a global filter optimized for one pattern can adversely affect performance on nodes with differing patterns. To address this, we introduce a novel GNN framework  \method that utilizes a mixture of experts to adaptively select the appropriate filters for different nodes.  Extensive experiments demonstrate the effectiveness of \method on both homophilic and heterophilic graphs.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces NODE-MOE, a GNN framework that uses a mixture of experts (MoE) model to apply node-specific filters, addressing the limitations of traditional GNNs that use a uniform global filter.  NODE-MOE’s architecture includes a gating model, which assigns each node a set of specialized filters from multiple expert models, allowing for dynamic adaptation to the local structure of each node. Experimental results across diverse datasets demonstrate NODE-MOE’s superior accuracy over standard GNNs, especially in noisy environments and with limited labels.

### Strengths
- The use of the Contextual Stochastic Block Model (CSBM) to validate this limitation strengthens the motivation for NODE-MOE’s node-specific filtering approach.
- The NODE-MOE allows each node to dynamically access different filters through a mixture of experts.
- Extensive experiments show NODE-MOE’s effectiveness across both homophilic and heterophilic datasets.

### Weaknesses
 - The abstract and introduction of this paper require revision to reflect the existing literature more accurately. Currently, statements such as “Traditionally, GNNs employ a uniform global filter” in the abstract and introduction *could mislead readers*, including reviewers, by implying that no prior research has explored GNNs with multiple filters. However, as discussed in the related work section, numerous studies share similar motivations and have developed approaches that utilize multiple filters in GNNs. To provide a clearer foundation, the authors should acknowledge these existing contributions in both the abstract and introduction, clarifying how their work builds upon or differentiates from these prior approaches. This adjustment will ensure a more accurate representation of the field and help readers better understand the novelty and contributions of this paper.
- The paper claims that the proposed model offers better computational complexity than previous work discussed in the related section. However, no rigorous analysis is provided to substantiate this claim. Given the highly parallelizable nature of some existing “post-fusion” architectures, these prior models may, in fact, achieve lower computational costs.
- Theorem 1 only provides proof for linear models with lower expressivity than typical GNNs. Moreover, the proof in part 2 relies on a strong assumption that every homophilic and heterophilic node can be perfectly classified and assigned the appropriate filter.
- The proposed NODE-MoE seems to use a larger number of learnable parameters compared to other baselines. How many learnable parameters are used for both the baselines and NODE-MoE, as shown in Table 1? Is the same performance improvement observed, even if the number of parameters for NODE-MoE is adjusted to be on a similar scale as the baselines?
- The proposed NODE-MoE seems to have a broader hyperparameter search space than other baselines. Since its training time per epoch is longer, this broader search space would likely result in a significantly longer training time, including the validation time required to find the best hyperparameter set. Is the same performance improvement observed, even if the total training time, including hyperparameter search, is adjusted to be comparable to the baselines?
- Figures 6 and 15 seem inconsistent with the underlying motivation. While Figure 6 shows that the weights for the high-pass filter decrease as the homophily level rises, the difference between the two weights is not significant across the entire range of homophily. Moreover, even when the homophily level reaches 1, the high-pass filter’s average weight still exceeds that of the low-pass filter. Additionally, in Figure 15, even the trend observed in Figure 6 no longer exists.
- Minor: There appears to be an error in y-tick (density) values in Figure 2, as they are not within the 0-1 range.

### Questions
How did the authors find GIN and ChevNetII as an gating and expert models respectively? What alternatives are considered and why these combination performs the best?

### Soundness
3

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
The paper introduces a Mixture of Experts inspired technique for GNNs aimed to improve classification performance on heterophilic and homophilic nodes in a graph. The paper first, presents some analysis to show how real-world graph contain varying levels of homophily and a single fixed "low" or "high" pass filter may not be the best solution to learn reasonable node features. Thus, motivated by this analysis, the authors propose a mixture of experts technique, wherein a gating model is capable of "soft" selection of representation of a bunch of expert GNN models with varying node wise filter levels. Experiments show that the proposed method generally outperforms previous graph MoE based methods and other standard baselines. Detailed ablations and analysis into the hyper parameters are presented. Some considerations into the efficiency of the proposed methods are also presented.

### Strengths
1) Good motivation and interesting use of MoE for dealing with the problem of node having varying levels of homophilic / heterophilic patterns in real world graphs. 

2) While the use of MoE to graph data is not new, the paper presents some new insights when used for node level tasks e.g., the use of filter smoothing loss, experts with node wise filtering. Experimentally, performs better than other graph based MoE techniques. 

3) Good and reasonable set of experiments on the analysis of the proposed method, detailed experiments on the time complexity and hyper parameter choices.

### Weaknesses
1) Limited novelty of the proposed problem setup (Section 2.1 and 2.2). It is well known that real world graphs contain nodes that exhibit variations in homophilic behavior. [ref - 1,2]. Limited technical novelty since, much of the techniques used in the proposed method is based on earlier work in the MoE area like Top K sampling, use of gating mechanism [3]. The paper does not adequately address the fact that the core idea of using a mixture of experts to handle varying homophily levels is not entirely novel, and the specific implementation details, while differing slightly, rely heavily on existing MoE frameworks. The use of a gating mechanism to select experts based on node characteristics, while intuitive, is a direct application of established MoE principles, and the paper lacks a deeper exploration of how this approach fundamentally differs from existing methods.

2) The gains in performance due to the proposed method "Node-MoE" is not clear compared to other non MoE baselines given the significant overlap of mean standard deviation. Moreover, the heterophilic datasets chosen are known to be problematic [4]. It would a stronger argument, if additional new datasets from [4] are used for the experiments. The reported performance improvements are marginal, and the standard deviations are large enough to question the statistical significance of the results. The paper needs to provide a more rigorous statistical analysis to support its claims. Furthermore, the choice of heterophilic datasets is questionable, as these datasets have known issues that could skew the results. The paper should include a more diverse set of datasets, especially those highlighted in [4], to provide a more robust evaluation.

3) A clear algorithm detailing the different techniques can be presented for better clarity to the reader.

### Questions
1) Given that the performance gains in Table 1 are not very clear (due to the overlap in std. dev. with non MoE baselines) what were the winning hyper parameters from the search space?  The reason I ask is because the paper claims that due to efficiency reasons one can reduce the number of experts (say 2) and utilize gating with Top K = 1. But since that come with the trade-off with accuracy, I am curious about the setting used for the main results presented.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper tackles the challenges faced by Graph Neural Networks (GNN) in real-world graphs that exhibit both hemophilic and heterophilic patterns, which complicates processing with a single global filtering approach. The authors propose a Mixture of Experts (MoE) based node classification method specifically designed to address these issues. By utilizing node-level MoE, the proposed method effectively navigates the complexities of these patterns, demonstrating promising results through extensive experimental evaluations.

### Strengths
The proposal of MoE-like node label filtering is particularly interesting, as it enhances the method's suitability for handling real-world graphs with diverse patterns.

The authors provide a comprehensive analysis throughout the paper, complemented by a thorough set of experimental studies that effectively support their proposed approach.

### Weaknesses
 * Figure 1 serves as a poor illustrative example, as it may lead to confusion. The introduction in Section I states that “nodes tend to connect with others that share similar labels, reflecting homophilic patterns,” yet Figure 1 shows both solid and dashed edge nodes connecting to nodes labeled  and 1 on the right side, which contradicts this description. The figure does not clearly delineate how the homophily/heterophily is determined at the node level, especially when considering that a node can have multiple neighbors with varying labels.
* The message and patterns presented in Figure 2 lack clarity regarding their relevance to the key contributions of the work. The statement that “the majority of nodes in homophilic graphs predominantly exhibit homophilic patterns” raises questions about the definition of homophilic graphs. According to the authors' definition in the Homophily metrics section, this concept only applies to graphs with different labels; otherwise, h(v) will always equal 1. The figure does not provide a clear quantitative measure of the node-level homophily distribution, making it difficult to understand the significance of the observed patterns.
* The paper suffers from overloaded notations that can lead to confusion for readers. For instance, h(v_i) is used in Section 1 to denote the label similarity between a node v_i and its neighbors, while in Section 3.1, the same notation is repurposed to refer to a node classifier. This inconsistency may hinder comprehension.

### Questions
see the details in the weaknesses part

### Soundness
3

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
4

### Summary
In this paper, the authors address limitations in graph neural networks (GNNs) that arise when only a single global filter is used. They observe that graphs may contain a combination of homophilic and heterophilic patterns within the same graph, with varying levels of homophily across different subgraphs or communities. Based on the patterns generated by the  CSBM model, they theoretically analyze the (near) linear separability of nodes when (1) a low-pass global filter is applied to the entire graph and (2) different filters are applied separately to nodes with different patterns. These theoretical insights lead to the development of a novel GNN model that employs a mixture-of-experts approach to adaptively select filters for nodes based on their specific patterns.

### Strengths
**originality**

The originality of the paper is marginal, as it builds on well-known observations (see "weakness").

**quality**

The paper appears to be technically sound, presenting a nice theoretical analysis based on the CSBM model, which motivates the development of its proposed node-wise filtering method.

**clarity**

The paper is well-structured and generally easy to follow. However, Figure 1 could be improved, as it currently reads a bit confusing. For instance, there are no numbers or labels on the right side of Figure 1(a), making it unclear which nodes correspond to those on the left side after applying the global filter. Also, what are the key messages of the figure? The figures in Section 4 (Experiments) could be enhanced, e.g., the font sizes for the x-axis and y-axis labels in Figures 6 and 7 are too small, which makes them difficult to read.

**significance**

The significance of the proposed method is limited due to its marginal originality.

### Weaknesses
 (W1) The observation of varying structural patterns (homophilic and heterophilic patterns within the same graph) is not highly original. While the paper provides a well-illustrated demonstration in Section 2.1, analyzing these patterns from two perspectives: node homophily density and homophily across different communities, this does not significantly enhance the originality. These structural variations are commonly known and have been addressed in previous works using various approaches as discussed in Section 5 Related Works.

(W2) The proposed method assumes that a heterophilic pattern is present when a node’s features significantly differ from those of its neighboring nodes. While this assumption is reasonable, it restricts the method's applicability. Node features do not always correlate with node labels in terms of homophilic and heterophilic patterns, which may reduce the method's effectiveness when feature-label alignment is weak. Although the authors argue that the proposed method is distinct from existing works because those approaches pass all nodes through all filters, these prior methods do not make specific assumptions about heterophilic patterns, instead allowing the filters to adaptively learn from data. Thus, the distinction between the current work and these prior methods seems more like a trade-off rather than a clear improvement.

(W3) The proposed method appears to be a combination of a gating function and a mixture of experts. When multiple GNNs with different filters are used, the model grows in complexity, introducing additional learnable parameters and hyperparameters (such as $\gamma$ for adjusting the influence of the filter smoothing loss, and $K$ for the number of experts). This added complexity typically leads to performance improvements, so the modest gains shown in the experimental results are not surprising.

### Questions
See the questions in "Weaknesses".

For the statement: "... different structural patterns are not uniformly distributed across the graph, and distinct communities
may exhibit varying structural characteristics. To capitalize on this phenomenon, we employ GNNs
with low-pass filters, such as GIN (Xu et al., 2018), for the gating model. These networks are chosen
due to their strong community detection capabilities (Shchur & Günnemann, 2019; Bruna & Li,
2017), ensuring that neighboring nodes are likely to receive similar expert selections", I also have two questions:

1. Could you elaborate on why GIN has strong community detection capabilities?

2. Regarding "ensuring that neighboring nodes are likely to receive similar expert selections", does this apply to both homophilic and heterophilic graphs? If so, how would the approach differ between them? In heterophilic graphs, neighboring nodes are more likely to differ in features or labels, so how would similar expert selections across neighbors work?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper identifies that real-world graphs exhibit a complex mix of homophilic and heterophilic patterns, meaning each node may display varying levels of homophily. Consequently, applying a single global filter leads to suboptimal performance. Using real-graphs and synthetic graphs constructed using the CSBM model, the authors empirically and theoretically demonstrate that a global filter optimized for one pattern increases the loss for other patterns. To address these limitations, they propose Node-MoE: Node-Wise Filtering Via Mixture of Experts.

Node-MoE dynamically applies distinct filters to individual nodes based on their specific patterns. The gating/routing model utilizes a composite vector, applying a GIN network to assign weights to each expert model for each node. Expert models are instantiated using ChebNetII/GCNII with fixed filter initializations, such as low-pass, high-pass, or constant filters. An additional smoothing loss is incorporated to enhance training stability and improve explainability. The proposed method is validated across multiple homophilic and heterophilic datasets, benchmarked against a diverse set of baselines.

### Strengths
* Theoretical and empirical analysis highlighting the limitations of applying a single global filter.

* A suite of experiments across homophilic and heterophilic datasets demonstrating the effectiveness of the proposed method.

* Multiple ablation studies validating specific design choices, such as different gating variants.

### Weaknesses
 * A comparable framework, Link-MoE [1], was previously proposed for link prediction and bears a close resemblance to the overall framework of Node-MoE. However, this work is neither cited nor discussed in the related literature. Given the presence of this recent work, the novelty of the proposed method appears limited. The core idea of using a mixture of experts to handle different data subsets is not new, and the adaptation to node classification, while not trivial, appears to be a relatively straightforward extension of the existing framework.

* While the paper argues that applying different filters to homophilic and heterophilic separately can lead to linear separability, a similar effect might also be achieved by increasing the representation capacity of global filters. For instance, by increasing the order in polynomial filters, or by learning piecewise polynomial filters[2]. Moreover, [3] explores node-wise filters via polynomial graph transformers. A comparison with these methods is necessary to evaluate the effectiveness of Node-MoE. Specifically, the paper should explore how the performance of Node-MoE compares to methods that utilize higher-order polynomial filters or adaptive filter learning techniques, as these approaches could potentially achieve similar results without the added complexity of an MoE architecture. The paper lacks a discussion on the computational cost of the proposed method compared to these alternatives.

* Table 1 compares Node-MoE with ACM-GCN [4]. However, [4] also includes additional results for ACM-GCN+ and ACMII-GCN++, which achieve 76.08% (Node-MoE: 73.64%) on the Chameleon dataset and 69.98% (Node-MoE: 62.31%) on the Squirrel dataset, with similar improvements across other datasets. GCN+ and GCN++ incorporate MLP(A) as additional features. Moreover, [5] demonstrated that incorporating structural information (A) as additional features alongside simple graph filters can yield notable improvements—reaching 77.48% on the Chameleon dataset and 74.17% on the Squirrel dataset. In light of these results, the necessity of an MoE-based approach remains unclear. The paper needs to clarify whether the performance gains are due to the MoE architecture itself or simply due to the use of multiple filters, and it should also consider the impact of using additional structural features as explored in [4,5].

### Questions
See weaknesses.

**Additional questions.**

Q1. The average training time per epoch for ChebNetII and Node-MoE-3/5 are quite similar. What is the end-to-end training time comparison between these methods?

Q2. In Appendix C.2, the strategies for polynomial coefficients include both increasing/decreasing powers of $\alpha^k$ and uniform values. How would initializing each filter randomly impact performance?

Q3. What are some limitations of this work?

### Soundness
2

### Presentation
3

### Contribution
2
