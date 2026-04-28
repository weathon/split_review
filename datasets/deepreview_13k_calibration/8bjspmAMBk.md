# Quality Measures for Dynamic Graph Generative Models

- Decision: Accept
- Avg Score: 7.50
- Scores: 8, 8, 6, 8

## Abstract
Deep generative models have recently achieved significant success in modeling graph data, including dynamic graphs, where topology and features evolve over time. However, unlike in vision and language domains, evaluating generative models for dynamic graphs is challenging due to the difficulty of visualizing their output, making quantitative metrics essential. In this work, we develop a new quality metric specifically for evaluating generative models of dynamic graphs. Current metrics for dynamic graphs typically involve discretizing the continuous-evolution of graphs into static snapshots and then applying conventional graph similarity measures. This approach has several limitations: (a) it models temporally related events as i.i.d. samples, failing to capture the non-uniform evolution of dynamic graphs; (b) it lacks a unified measure that is sensitive to both features and topology; (c) it fails to provide a scalar metric, requiring multiple metrics without clear superiority; and (d) it requires explicitly instantiating each static snapshot, leading to impractical runtime demands that hinder evaluation at scale. We propose a novel metric based on the Johnson-Lindenstrauss lemma, applying random projections directly to dynamic graph data. This results in an expressive, scalar, and application-agnostic measure of dynamic graph similarity that overcomes the limitations of traditional methods. We also provide a comprehensive empirical evaluation of metrics for continuous-time dynamic graphs, demonstrating the effectiveness of our approach compared to existing methods.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The primary motivation behind the proposed work is to address the limitations of existing metrics for evaluating generative models for dynamic graphs.
The authors provide various limitation such as: Lack of consideration for temporal dependencies, lacking a unified measure that is sensitive to both features and topology, Absence of a unified scalar metric.

The authors propose Johnson-Lindenstrauss (JL) metric to overcome above limitations.
They leverage the Johnson-Lindenstrauss lemma to project dynamic graphs into a lower-dimensional space. It  allows for comparison of generated and ground-truth graphs using standard distance metrics.


The authors perform evaluation on datasets:  Reddit, Wikipedia, LastFM,
and MOOC.  They compared their proposed JL-Metric with several traditional metrics based on topological and feature-based properties. idelity: Also, they did evaluation w.r.t Diversity,  Sample Efficiency , and Computational Efficiency.  
The authors used real-world and synthetic datasets to test the metrics under various conditions, including perturbations like edge rewiring, time perturbation, and event permutation.

### Strengths
1. Novel Approach to Evaluating Dynamic Graph Generative Models.

2. Strong Empirical Evaluation.

3. Code is shared.

4. Background work is very well cited and explained. Limitations are clearly highlighted and justified by experiments.

### Weaknesses
 1. In 4.1 evaluation:

Are all the types of perturbations independent? Can't the perturbations happen jointly? i.e edge rewiring and time perturbation together? Or have I misunderstood it? Is there any assumption. Kindly clarify. If they are independent, can we understand the impact if they occur jointly? Since in reality, it could happen right?

2. "a timestamp ti is replaced by a uniformly selected one trand ∼ Unif(ti−1, ti+1)"
Why is the range so small? just 3 possibilities? Is there any specific reason for this? Can we increase this range while also preserving the order?



### Questions
Please see weakness section.

1. Dataset statistics seem to be missing.
"We use a subset of these data (details in Appendix C), which were originally introduced
by Jodie (Kumar et al., 2019) and have become standard CTDG benchmarks"

It is not clear what subset for each dataset? The authors should specify clearly.


Check [A]  Table 1 on what information could be useful to add in terms of dataset statistics.

2. Could authors throw some more light on how evolution is capture in their metric? ". The JL-Metric, by
contrast, is more expressive, capturing both temporal and structural changes directly". Can the authors clarify it better. structural + temporal?
I may be missing something. 

[A] TIGGER: Scalable Generative Modelling for Temporal Interaction Graphs
https://aaai.org/papers/06819-tigger-scalable-generative-modelling-for-temporal-interaction-graphs/

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
1

### Summary
The paper introduces a novel quality metric, JL-Metric, for evaluating generative models of dynamic graphs, addressing limitations in current metrics that treat temporal events as independent and fail to capture the integrated evolution of both graph topology and features. By leveraging the Johnson-Lindenstrauss lemma, the authors propose a method that uses random projections to measure similarity between dynamic graphs, resulting in an expressive, scalar metric applicable to continuous-time dynamic graphs. Empirical results suggest this metric achieves high fidelity and computational efficiency compared to traditional metrics.

### Strengths
S1: Unified Metric for Temporal Dynamics: The proposed metric overcomes the limitations of traditional methods by capturing dependencies between events and integrating both topological and feature dynamics, specifically for CTDG, which looks rational to me.

S2: High Efficiency and Practicality: The method’s use of random projections reduces runtime and memory demands, making it feasible for large-scale graph evaluation tasks, along with extensive evaluations, which looks comprehensive to me.

### Weaknesses
See questions.

### Questions
I am not highly specialized in this dynamic graph metric research area, but I do have a few general questions:


Q1: How does the method ensure robust sensitivity to subtle changes in node and edge features, especially when applied to simpler dynamic graphs or those with more complex interactions beyond temporal events? In theory, how do graph scale and interaction complexity influence the performance of this metric?

Q2: This paper covers a range of metrics and theoretical concepts. As a minor suggestion, it might enhance clarity to include a high-level figure illustrating the differences between the proposed metric and others, beyond just presenting post-experimental results.

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
The paper proposes a new metric for measuring similarities between temporal graphs, utilizing the input dimension agnostic property of random projection certified by the JL lemma. The metric is based on a node interaction history representation of a temporal graph, computed via first projecting individual node histories, followed by another random projection that fuses nodes. Experimental results demonstrate that the proposed metric achieves better fidelity and diversity than classic metrics, while being computationally efficient and sample efficient.

### Strengths
- Defining a suitable metric for assessing generation quality of temporal graphs is an important problem in graph generative modeling. The proposed metric is a novel approach that goes beyond the traditional way of using statistical summaries as quality measures.
- The proposed JL metric is shown to behave well empirically, especially in the event permutation sensitivity analysis.

### Weaknesses
 - The proposed JL metric is stated to accommodate both topological information and feature information. While the overall assessments using sensitivity analysis have shown that JL indeed performs better than baselines, it would be more intuitive if the authors provide concrete evidences illustrating the sensitivity to some topological structures that exists in the evaluation datasets.
- In line 277 the authors proposed to use a simplified version of node history as node level presentation. The simplification essentially drops (some) interaction information, i.e., the interaction nodes' identity information. According to my understanding, this simplification inevitably looses capability to account for topological information.

### Questions
- As the authors use JL as their motivation for representation construction, I think it would be interesting if the authors provide the exact JL bounds that incurred during empirical evaluations: How well does JL compresses real world temporal graphs, according to the standard JL bound?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The paper presents a novel metric designed for evaluating generative models of dynamic graphs, where both topology and features evolve over time. The authors propose a new metric based on the Johnson-Lindenstrauss (JL) lemma, which leverages random projections to create an expressive, scalar measure that captures the complex dependencies in dynamic graphs, overcoming limitations in current evaluation methods.

Current metrics for evaluating dynamic graph generative models (DGGMs) rely on static snapshots, and therefore lose the temporal dependencies. Moreover, current metrics fail to capture node and edge features and their relation to the graph topology. They are also only sensible to specific properties resulting to the need of multiple metrics. Many of these metrics are also computationaly inefficient. 

To address these limitations, the authors propose a new Johnson-Lindenstrauss-based (JL) metric, inspired by work in the static graph domain and image-based evaluations. The metric applies random projections directly to continuous-time dynamic graph data, effectively embedding the variable-length sequence of graph events into a fixed-dimensional vector space. This transformation preserves the similarity of data across temporal interactions and node features while avoiding the computational cost of explicit snapshot instantiation.

The author justify the use of random projections on the Johnson-Lindenstrauss lemma, which asserts that random orthogonal projections can approximately preserve the distance between data points. This property allows the proposed metric to map dynamic graph events of varying lengths into a unique dimension. 

Experiments are conducted on both real-world datasets (e.g., Reddit, Wikipedia, LastFM) and synthetic datasets. They show that the JL metric provides consistent, high-fidelity measurements across topological and temporal changes, with reduced computational overhead.

### Strengths
The paper is well written and structured, making it easy for readers to follow.

By leveraging the Johnson-Lindenstrauss lemma for random projections, this method offers several advantages, including the ability to capture temporal dependencies, unify topology and feature changes into a single scalar metric, and reduce computational cost. 

The empirical evaluation demonstrates the effectiveness of the new metric. The experiments validate the interest of the method and its practical utility.

Additionally, Section 3 provides new theoretical insights into why random-network-based metrics may be effective in general, and for dynamic graphs in particular.

### Weaknesses
The methodological novelty of the proposed approach is somewhat limited, as similar frameworks have already been applied, including to static graphs. The authors themselves acknowledge this by stating that they "follow recent analogous work in the static graph domain by Thompson et al., 2022." The contribution is therefore limited.

The applicability of the proposed metric is focused on continuous-time dynamic graph generative models (CTDGs) with a given initial graph. It is a relatively small field within dynamic graph research, where most studies adopt a supervised learning setting. Moreover, new metrics for CTDGs can be integrated within papers introducing novel generative models, as it have been the case for instance in Zhang et al. (2021). The potential impact of this work may be limited.

The paper does not include a discussion of the limitations of the method. For instance, it does not address the fact that the metric evaluates only the changes in the graph over time rather than the graph structure itself, limiting the possible application of the metric. This means that two graphs with very different structures but similar temporal changes could be evaluated as similar. Scalability could be an issue, for example, when applying the method to large graphs with a high number of events. These are just examples and a paragraph on some limitations of the method would be insight full.

The paper does not provide practical recommendations for applying the metric to common datasets. Specifically, there is no guidance on selecting the optimal number of samples, events, or the dimensions of descriptors, which could help in effectively using the metric on various datasets.

Minor comment:
I think that there is a small typo in the formula at the end of line 119.

### Questions
Please, could you comment on the limitations mentioned above? On the fact that the metric only evaluates changes rather than the graph distribution itself and on the scalability issue. 

Could you also comment on the small number of dynamic graph generative models?

### Soundness
3

### Presentation
3

### Contribution
3
