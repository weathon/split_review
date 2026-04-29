# Position: Graph Learning May Have Been Misled By Over-smoothing And Over-squashing

- Decision: Reject
- Scores: 5, 5, 3

## Abstract
The prevalent focus in graph learning research on theoretical challenges like over-smoothing and over-squashing may be misguiding, as their practical relevance in real-world scenarios is questionable. While Graph Neural Networks (GNNs) have achieved significant success across various applications, theoretical work has extensively discussed issues such as over-smoothing and over-squashing for the past eight years. This paper argues that the continued emphasis on these problems might be misplaced. For node-level tasks, we suggest that performance decreases often stem from uninformative receptive fields rather than over-smoothing, as optimal model depths remain small even with mitigation techniques. For graph-level tasks, over-smoothing can even be beneficial if the smoothed state is label-informative. Similarly, we challenge the notion that over-squashing, i.e., the compression of exponentially growing information into fixed-size node embeddings, is always detrimental in practical applications. We argue that the distribution of relevant information over the graph frequently factorises and is often localised within a small $k$-hop neighbourhood, questioning the necessity of jointly observing entire receptive fields or engaging in an extensive search for long-range interactions. Our empirical findings demonstrate that while methods exist to mitigate over-smoothing and over-squashing, they often do not yield significant performance gains with increased model depth on standard benchmarks, and can lead to substantial computational costs. In this position paper, we advocate for a paradigm shift in theoretical research, urging a diligent analysis of future learning tasks and datasets to better understand the localisation and factorisation of label-relevant information. This will ensure that theoretical advancements align with the real needs and challenges of real-world graph learning problems.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper argues a position that graph learning might be misled by oversmoothing and oversquashing. Authors discuss the background works and mitigation techniques on both oversmoothing and oversquashing. They further conducted experiments on the small or medium-scale node-level and graph-level tasks to demonstrate that the effects of oversmoothing and oversquashing may not be the actual reason for performance degradation.

### Strengths
1. The presentation of the paper is impressive and very easy to follow.

2. A good amount of background work is discussed for both Oversmoothing and Oversquashing.

3. The experimental analysis is moderate. The corresponding discussions further support the position of the paper.

### Weaknesses
1. At lines 153-154, the authors claim that oversmoothing occurs due to the uninformative receptive field, not for stacking multiple message passing layers. This is not true because oversmoothing happens when the receptive field overlaps with increasing the hops. Authors should rephrase or explain in detail their thoughts. 

2. Only a few small datasets do not imply that oversmoothing or overquashing has no impact on the graph learning paradigm. Experiments on some OGB datasets can be beneficial. 

3. In the experiments, the authors showed that overquashing may not be severe for node and graph-level tasks. I disagree with the empirical results. Refer to the work [1] that extensively analyzes the impact of oversquashing in the molecular graphs, and they resolved it through rewiring.  Furthermore, experiments should also be done on LRGB datasets [2].

I am ready to increase my score if my concerns are addressed. 

[1] Barbero, Federico, et al. "Locality-aware graph-rewiring in GNNs." ICLR 2023.

[2] Dwivedi, Vijay Prakash, et al. "Long-range graph benchmark." Advances in Neural Information Processing Systems 35 (2022): 22326-22340.

### Questions
Check the weakness section.

### Presentation
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper discusses about the well known problems in Graph Neural Networks of over-smoothing and over-squashing. It argues that instead of focusing on the problems, a different approach towards the quantification of the problem is required to develop better suited model architectures.

For over-smoothing, the argument presented in this paper is that the it occurs only with much deeper GNNs which have large receptive fields. Quatifying the receptive field suitable for a problem, is more important than trying to solve over-smoothing. For problems that require smaller receptive fields, over-smoothing will not be a problem since the GNN would not be much deep, and for problems that require larger receptive field, there are alternative architectures like Graph Attention Networks and virtual nodes.

A similar argument has been brought up for over-squashing as well - practically, a small neighbourhood is enough to get all relevant information for the learning task.

### Strengths
The paper explores the relevant background and existing methods quite well. It cites various other position papers and works that tried to mitigate the above problems. They have shown empirical results of performance of some baseline models and methods to mitigate over-smoothing and over-squashing with exponentially increasing number of layers. The results support their arguments that designing mitigation methods alone is not enough to tackle these problems, rather a better understanding of the problem is required for better suited model architectures.

### Weaknesses
For the empiricla results, they have only compared the mitigation methods with GCN. While the objective was to show the improvement over vanilla grpah convolution, it would be better if some widely used methods were also included, like GraphSAGE and Graph attention networks.

### Questions
Check Weakness

### Presentation
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper argues that the practical impact of oversmoothing and oversquashing in GNNs is often overstated. For node-level tasks, performance drops are due to uninformative receptive fields rather than oversmoothing. The authors claim that oversquashing is less harmful when relevant information is local and ``factorised'', making deep models and long-range aggregation unnecessary. Empirically, mitigation methods often do not lead to performance improvements when deep models are considered while being computationally costly. The paper calls for refocusing theoretical research on understanding how label-relevant information is distributed in real-world tasks.

### Strengths
- The manuscript is well-structured, easy to follow, and accessible to a broad audience in ML.
- The subject is highly pertinent to ongoing research in GNNs. Many papers aim to alleviate oversmoothing and oversquashing.

### Weaknesses
Overall, I found the empirical analyses weak:
  - The paper only considers 4 datasets (for node-level tasks), 3 of which are homophilic networks. The authors should expand this selection (e.g., OGB datasets). Regarding oversmoothing, what is the rationale for expecting deeper models to outperform shallower ones on highly homophilic graphs? Also, the authors do not consider established benchmarks such as those in [1], which could provide stronger empirical grounding for claims about oversquashing.
  -  Oversmoothing is assessed only on node-level tasks, leaving out other settings (e.g., graph-level tasks).
  - Prior works have proposed different metrics to assess oversmoothing and oversquashing. None of them are reported in the paper. Thus, the relationship between these metrics and downstream accuracy is not explored.
  - The reported results lack error bars, making it difficult to assess significance.
  - On Empire (the only heterophilic dataset), the highest accuracy is at layer 64, not at layer 4 as denoted in the paper. This conflict withs paper's position.

Finally, the work does not offer theoretical insights or formal analysis, which limits its impact and generalizability.

[1] Long range graph benchmark. NeurIPS 2022.

### Questions
See weaknesses.

### Presentation
3
