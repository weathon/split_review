# KAA: Kolmogorov-Arnold Attention for Enhancing Attentive Graph Neural Networks

- Decision: Accept
- Scores: 6, 6, 8, 6

## Abstract
Graph neural networks (GNNs) with attention mechanisms, often referred to as attentive GNNs, have emerged as a prominent paradigm in advanced GNN models in recent years. However, our understanding of the critical process of scoring neighbor nodes remains limited, leading to the underperformance of many existing attentive GNNs. In this paper, we unify the scoring functions of current attentive GNNs and propose Kolmogorov-Arnold Attention (KAA), which integrates the Kolmogorov-Arnold Network (KAN) architecture into the scoring process. KAA enhances the performance of scoring functions across the board and can be applied to nearly all existing attentive GNNs. To compare the expressive power of KAA with other scoring functions, we introduce Maximum Ranking Distance (MRD) to quantitatively estimate their upper bounds in ranking errors for node importance. Our analysis reveals that, under limited parameters and constraints on width and depth, both linear transformation-based and MLP-based scoring functions exhibit finite expressive power. In contrast, our proposed KAA, even with a single-layer KAN parameterized by zero-order B-spline functions, demonstrates nearly infinite expressive power. Extensive experiments on both node-level and graph-level tasks using various backbone models show that KAA-enhanced scoring functions consistently outperform their original counterparts, achieving performance improvements of over 20% in some cases.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces Kolmogorov-Arnold Attention (KAA), with a novel scoring method for graph attention. KAA enhances the performance of scoring functions and can be applied to nearly all existing attentive GNNs. To further analyze the expressive power of scoring functions in various graph attention mechanism, this paper introduces Maximum Ranking Distance (MRD) to quantitatively estimate their upper bounds in ranking errors. Extensive experiments on both node-level and graph-level tasks show the KAA can outperforms their original counterparts.

### Strengths
1. Exploring KAN for graph attention is novel.
2. Based on the analysis tool of graph attention in GATv2 [1], this paper proposes more powerful tools, Importance Ranking and Ranking Distance, to analyze the expressive power of graph attention.
3. The KAA is extensively evaluated in various downstream tasks.

### Weaknesses
1. The motivation to redesign the graph attention with KAN is not convincing. Current graph attention and graph Transformer have provided very good performance. The authors are encouraged to illustrate when the proposed KAN will significantly outperform current graph attention, including GATv2 [1], and graph Transformer.
2. I am confused by MRD theory. If there exists an optimum ranking for each node, and KAA always provides a good ranking that is very close to the optimum ranking, does KAA still needs multi-head attention? It seems that different attention heads will provide very similar attention. However, multi-head attention has been proven to be a very successful tech in attention.
3. The assumption that "the selected central node is connected to all other nodes in the graph" is not realistic. Even graph Transformers [3] are trying to incorporate various graph structures, which violate the assumption.
4. As claimed by the authors, the expressive power of KAA is much better than GAT and GATv2. However, better expressive power could result in severe overfitting [1]. I wonder how the authors tackle the severe overfitting issue in KAA.
5. The inclusion of KAN would significantly increase the computational cost. Thus the authors are encouraged to compare its computational cost (, including both time and space) with current graph attention and graph Transformer.
6. The comparisons with baselines could be unfair. The authors do not choose the recommended hyper-parameters as in the original paper or tune better results. For example, the dropout ratio in the GAT [2] paper is 0.6, and [2] achieves better results than the scores reported in this paper, under the same data split settings.

### Questions
Please refer to Weaknesses.

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
4

### Summary
This paper introduces a novel scoring function, Kolmogorov-Arnold Attention (KAA), which integrates the Kolmogorov-Arnold Network (KAN) architecture to enhance the performance of scoring functions in attentive Graph Neural Networks (GNNs). The authors propose a unified framework for scoring functions and introduce the Maximum Ranking Distance (MRD) to quantitatively measure their expressive power. Extensive experiments demonstrate that KAA-enhanced models outperform their original counterparts across various tasks and backbone architectures, with significant improvements in some cases.

### Strengths
### Strengths:

1. The paper presents a creative approach to enhancing GNNs by integrating the Kolmogorov-Arnold Network into the scoring process, which is a novel contribution to the field of graph neural networks.

2. The authors not only propose a new model but also provide a rigorous theoretical analysis of its expressive power compared to existing methods, backed by extensive experimental results that validate the effectiveness of KAA.

3. The paper demonstrates substantial performance improvements over some baselines on both node-level, link-level, and graph-level tasks, highlighting the practical applicability and benefits of the proposed KAA framework.

### Weaknesses
### Weaknesses:

1. I have one concern that despite the interesting introduction of KAA into the scoring function in graph attention networks, it is not that big to modify the architecture of attention computing mechanism for existing GNN community since there have been various GNN architectures beyond attention functions in the past years.

2. Then in the experiments, the authors only compare with some **old and weak** baselines with shallow layers ( $\le$ 4 layers), which further support my claim in the first concern.

### Questions
Check the questions below.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
leveraging Kolmogorov-Arnold Network (KAN), the authors proposed to use the KA attention to enhance attention-based GNN architectures. The paper provides extensive experiments to show that attention-based GANs are enhanced on both node-level and graph-level tasks across a wide range of benchmarks.

### Strengths
1. The authors provides a thorough analysis and recap over KAN and its application and components on attention-based GNNs, for example the expressive power of scoring functions and theoretical bounds of transform-based attention, MLP-based attention, and the proposed KAA. The theoretical analysis shows that KAA exhibits the strongest expressive power.
2. Extensive experiments across a wide range of benchmarks for node-level and graph-level tasks show that KAA could provide moderate and consistent improvements.

### Weaknesses
1. The author provides a very interesting plugins for attention-based GNNs and shows relatively good improvement. I personally like this idea and it shows potential of KAA on graph applications. however, one major concern is that nowadays, attention is still considered not necessary for GNN architectures and many SOTA architectures did not utilize attention mechanism within their architecture design, e.g. [1] for node classification and [2] for link prediction. As a result, it would be better if there were more comparison with other SOTA GNN models who did not include attention mechanisms. This is a kind suggestion and new experimental results is not necessary.
2. There seems to be lack of empirical analysis/ablation studies for different ranking methods proposed in section 4.2.2.

### Questions
1. Could you provide an empirical ablation study over the ranking methods proposed in section 4.2.2 to demonstrate the effectiveness of proposed MRD?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this paper, the authors unify scoring functions of current attentive GNNs and propose Kolmogorov-Arnold Attention (KAA), which integrates the Kolmogorov-Arnold Network (KAN) architecture into the scoring process. KAA enhances the performance of scoring functions across the board and can be applied to nearly all existing attentive GNNs. They also introduce Maximum Ranking Distance (MRD) to quantitatively estimate upper bounds in ranking errors for node importance. Experiments are provided on both node-level and graph-level tasks using various backbone models including KAA-enhanced scoring functions.

### Strengths
The Architecture of the proposed model is overall clearly written, and the background on KAN is well introduced. 

Table 1 on the formulas are informative with many experiment benchmarks evaluated against.

### Weaknesses
Can the authors more clearly indicate why GAT’s attention mechanism which uses a learnable alpha weight via local neighborhoods is insufficient in terms of expressive power?  

How does KAA attention compare to the more informative hierarchical attention mechanisms? The author should discuss this in the Related Work section. Here are recent relevant papers on this topic: 

[WWW 2019] Heterogeneous Graph Attention Network. In The World Wide Web Conference (WWW '19). Association for Computing Machinery, New York, NY, USA, 2022–2032. https://doi.org/10.1145/3308558.3313562

[IEEE ICDM 2021] "Bi-Level Attention Graph Neural Networks," in 2021 IEEE International Conference on Data Mining (ICDM), Auckland, New Zealand, 2021 pp. 1126-1131.
doi: 10.1109/ICDM51629.2021.00133

I have a concern that the novelty of the work is limited as it seems to be mainly using KAN (already proposed), with other already proposed components such as multi-head attention, and MLP like components. Can the authors more clearly distinguish their contributions from prior works? 

Table 1 on the formulas are informative with many experiment benchmarks evaluated against. However, the GNN models seem to be quite outdated, and even the other benchmarks are mostly variant models of the author’s proposed KAA. Other KAN based benchmarks should also be provided.

### Questions
I have a concern that the novelty of the work is limited as it seems to be mainly using KAN (already proposed), with other already proposed components such as multi-head attention, and MLP like components. Can the authors more clearly distinguish their contributions from prior works? 

Table 1 on the formulas are informative with many experiment benchmarks evaluated against. However, the GNN models seem to be quite outdated, and even the other benchmarks are mostly variant models of the author’s proposed KAA. Other KAN based benchmarks should also be provided.

### Soundness
3

### Presentation
3

### Contribution
2
