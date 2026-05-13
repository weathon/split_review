# The Effectiveness of Curvature-Based Rewiring and the Role of Hyperparameters in GNNs Revisited

- Decision: Accept
- Scores: 6, 6, 5, 6

## Abstract
Message passing is the dominant paradigm in Graph Neural Networks (GNNs). The efficiency of it, however, can be limited by the topology of the graph. This happens when information is lost during propagation due to being \textit{oversquashed} when travelling through bottlenecks. To remedy this, recent efforts have focused on graph rewiring techniques, which disconnect the input graph originating from the data and the computational graph, on which message passing is performed. A prominent approach for this is to use discrete graph curvature measures, of which several variants have been proposed, to identify and rewire around bottlenecks, facilitating information propagation. While oversquashing has been demonstrated in synthetic datasets, in this work we reevaluate the performance gains that curvature-based rewiring brings to real-world datasets. We show that in these datasets, edges selected during the rewiring process are not in line with theoretical criteria identifying bottlenecks. This implies they do not necessarily oversquash information during message passing. Subsequently, we demonstrate that SOTA accuracies on these datasets are outliers originating from sweeps of hyperparameters---both the ones for training and dedicated ones related to the rewiring algorithm---instead of consistent performance gains. In conclusion, our analysis nuances the effectiveness of curvature-based rewiring in real-world datasets and brings a new perspective on the methods to evaluate GNN improvements.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper investigates the effectiveness of curvature-based rewiring in mitigating bottlenecks in graph machine learning tasks. It argues that the theoretical conditions for edges being considered as bottlenecks are not necessarily satisfied for edges being modified in practice. It further argues that the superior performance of some existing methods is likely due to hyperparameter selection rather than systematic improvement.

### Strengths
1) The paper takes a careful look at some of the curvature-based methods proposed in the literature and examines whether theoretical conditions match empirical practice. From this perspective, the paper represents a move towards the right direction in evaluation of graph machine learning methods.

2) Detailed description of experimental setup provides helpful guideline for future research in terms of conducting rigorous empirical evaluation. The argument on hyperparameter selection is interesting and points to the importance of a probabilistic view in performance evaluation.

3) The paper is clearly motivated and generally well written. The visualisations are helpful to aid understanding.

### Weaknesses
1) As discussed in the paper briefly, I don’t feel the datasets being tested are the most appropriate ones (see Questions below). This makes the findings less surprising and not entirely convincing (although in fairness this is probably a limitation of previous methods as well).

2) Given that this is a paper on empirical validation, experiments should perhaps be done on more than one rewriting method and one single GNN model.

3) I don’t think homophily is the only factor that determines the long-rangeness of the task. It should depend on the graph topology (e.g., diameter), node features, and the nature of the task as well. Although this is not necessarily the focus of the paper, discussion about this can be made more precise.

### Questions
1) It is unclear whether any dataset in Table 1 would possess bottlenecks that hinder (in particular long-range) interactions that might be necessary for the task (in some sense this is also a limitation of the experiments in Topping et al. 2022), which is one of the main reasons why curvature-based rewiring was proposed in the first place. Therefore the analyses presented in this paper are, albeit interesting and pointing towards the right direction, not entirely surprising. This has been briefly discussed in Section 5, but it might be helpful if the authors can conduct experiments on datasets are may possess long-range interactions, for example the ones described in Dwivedi et al. (https://arxiv.org/abs/2206.08164). Note that the suitability of these datasets are themselves under active debate (see https://arxiv.org/abs/2309.00367), nevertheless they might be more appropriate than the datasets chosen in the paper.

2) The experiments are mostly based on a single rewiring technique and a single GNN model, i.e., the GCN. While this is reasonable starting point, for a more comprehensive evaluation and conclusive evidence, more rewiring methods and GNN models (e.g., GraphSage, ChebNet, or GIN) should be tested. I appreciate the former is recognised as a limitation of the current work, but it makes it less clear how generalisable the findings are.

3) I don’t think homophily is the only factor that determines the long-rangeness of the task. It should depend on the graph topology (e.g., diameter), node features, and the nature of the task as well. Although this is not necessarily the focus of the paper, discussion about this can be made more precise.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper revisits the effectiveness of curvature-based graph rewiring techniques on real-world datasets. The authors reveal that the identified bottlenecked edges are not in line with theoretical criteria identifying bottlenecks, which thus do not necessarily oversquash the information. Furthermore, the authors demonstrate that the improved accuracies of rewiring techniques on these datasets are outliers originating from sweeps of hyperparameters—both the ones for training and dedicated ones related to the rewiring algorithm—instead of consistent performance gains. They further nuances the effectiveness of curvature-based rewiring in real-world datasets and bring a new perspective on the methods to evaluate GNN improvements

### Strengths
1. This paper reveals an important issue in the evaluation of graph rewiring techniques, especially for curvature-based graph rewiring.
2. The theoretical analysis is thorough and solid.

### Weaknesses
1. The analysis and empirical study are specific to the curvature-based method (Topping et al., 2021).
2. As the over-squashing issue is highly related to the long-range dependency, the work doesn't include the long-range graph benchmark (Dwivedi et al., 2022), which a bit weakens the study and analysis.
3. The analysis is only on GCN (Kipf & Welling, 2016). It will be more comprehensive to include other widely used MPNNs, e.g., GraphSAGE (Hamilton et al., 2017), GatedGCN (Bresson & Laurent, 2018), GAT (Veličković et al., 2018). This can help better understand the impact of MPNNs on the performance of graph rewiring techniques.

### Questions
No further questions beyond weaknesses

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
This paper reconsiders the effect of rewiring according to curvature on GNN effects. Through a large number of experiments, it points out that the rewiring does not meet the identification criteria of the message-passing bottleneck in the figure, and the effect is not significantly improved under a large number of hyperparameter attempts.

### Strengths
1. This article gives a very detailed introduction to curvature rewiring, which is very helpful for readers who are new to the field to understand the work.
2. This paper explains the bottleneck conditions of curvature rewiring from the theoretical point of view and verifies the effect of various methods through experiments, which is very convincing.
3. The paper proves its point through a large number of experiments, which show that the existing methods are ineffective in solving the problem.

### Weaknesses
1. The author merely presents a problem, not a solution to it.  The work lacks sufficient integrity.
2. There are some problems with the selection of datasets. For example, MUTAG and PROTEIN, which are themselves molecules and proteins, have biochemical implications. Therefore, performance may not be significantly improved after rewiring. For different areas of graph data, we need to be more profound.
3. The baseline of the experiment needs to be increased. In the task of node classification, the importance of node characteristics is very important. Therefore, the authors need to add an MLP as a baseline. If you can't explain the effectiveness of the edge in this task, then you can't fully explain the problem of rewiring.

### Questions
1. Can the author provide a comparison of experimental results without using edges? (an MLP with the same number of layers) In general, in a node classification task, node characteristics play a crucial role in the classification effect, often sometimes the role of edges is not obvious.
2. For Other questions please see Weaknesses.

### Soundness
2

### Presentation
2

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
The paper revisits the effectiveness of curvature-based rewiring in Graph Neural Networks, focusing on its role in alleviating the over-squashing problem. In GNNs, message passing can suffer from information bottlenecks, where messages get compressed, leading to worse downstream performance. Curvature-based rewiring, which involves modifying the graph’s structure to improve information flow, has been proposed as a solution. This paper reevaluates its performance on real-world datasets.

The authors find that in real-world scenarios, the edges selected during the rewiring process do not align with theoretical predictions about bottlenecks, suggesting that the over-squashing issue may not be as prevalent in these datasets. Furthermore, the paper argues that state-of-the-art results from curvature-based rewiring often stem from hyperparameter tuning rather than consistent performance improvements. The study questions the practical benefits of curvature-based rewiring for GNNs and calls for a more nuanced evaluation of GNN improvements.

### Strengths
- Clear motivation: The paper has a clear motivation to revisit and critically evaluate the effectiveness of curvature-based rewiring in Graph Neural Networks, and to specifically test whether the theoretical justifications for these methods are genuinely applicable to real-world datasets.
- Extensive experiments: The authors conduct a thorough experimental analysis, testing various curvature measures and examining their effects on node and graph classification tasks. They scrutinize both the theoretical underpinnings and the practical outcomes of rewiring, demonstrating that the edges selected by the rewiring process do not always correspond to bottleneck points. Additionally, they show that state-of-the-art performance is often a result of hyperparameter tuning rather than inherent benefits from rewiring.

### Weaknesses
 - Presentation: pages 8 and 9 could benefit from some reorganization, for example by better integrating table 2 and figure 2 into the text. Table 2 could also benefit from the best-performing setting being highlighted. I also find Figure 3 hard to read: perhaps it would be better to split the figure in two, i.e. have one figure with the curvature distributions and one with the mean test accuracies.
- More nuanced discussion: while this may be a minor point, I would suggest that the authors include a sentence or two about the role of curvature in graph machine learning more broadly in their discussion section, for example by referring to [1]. While I welcome that the paper pushes back against curvature-based rewiring and consider it good science, this does not mean that curvature is generally not useful for GNNs.
- Long-range datasets: again a minor point, but additional graph-level datasets would further strengthen the paper's message. The authors could, for example, look at Peptides-func and Peptides-struct in the LRGB datasets [2].

### Questions
Could the authors explain why they focus on the theoretical results related to SDRF and not the ones related to BORF, another curvature-based method? Their theoretical results seem less restrictive than what’s presented in the SDRF paper, so I'm wondering what an analogue of Table 1 could look like in this context.

### Soundness
3

### Presentation
2

### Contribution
3
