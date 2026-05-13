# Charting the Design Space of Neural Graph Representations for Subgraph Matching

- Decision: Accept
- Scores: 8, 5, 6

## Abstract
Subgraph matching is vital in knowledge graph (KG) question answering, molecule design, scene graph, code and circuit search, etc.
Neural methods have shown promising results for subgraph matching.
Our study of recent systems suggests refactoring them into a unified design space for graph matching networks.
Existing methods occupy only a few isolated patches in this space, which remains largely uncharted.
We undertake the first comprehensive exploration of this space, featuring such axes as attention-based vs. soft permutation-based interaction between query and corpus graphs, aligning nodes vs. edges, and the form of the final scoring network that integrates neural representations of the graphs.
Our extensive experiments reveal that judicious and hitherto-unexplored combinations of choices in this space lead to large performance benefits.
Beyond better performance, our study uncovers valuable insights and establishes general design principles for neural graph representation and interaction, which may be of wider interest.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents a unified design space for existing neural subgraph matching methods over various dimensions. By carefully controlling the design option for each dimension, it effectively reveals the optimal design option combination for neural subgraph matching with substantial improvement, providing new insights on the previous methods and reported results.

### Strengths
**S1.** The charting of the design space is convincing and well-articulated.

**S2.** Empirical studies demonstrate the effectiveness of the design space in characterizing existing methods and devising superior new methods for the experiments considered.

**S3.** The presentation is quite neat and clear overall.

### Weaknesses
 **W1.** Most datasets considered are for small molecules despite the various applications of subgraph matching mentioned in the introduction.

 **W2.** There is a lack of understanding in subgraph matching performance with respect to the intrinsic challenge of the setting, e.g., highly regular graphs, different graph sizes, different feature distributions, out-of-distribution settings. Such study may be best achieved with synthetic datasets.

**minor**
- The use of notations $\omega$ and $\eta$ are not consistent between L124 and Figure 1.

### Questions
**Q1.** Does the use of hinge distance make sense for set alignment and aggregated-hinge (L216-236)? In particular, the authors justify the use of hinge distance for adjacency matrices, but the adjacency matrices are binary while node/aggregated node embeddings are just real-valued.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents an exploration of the design space for neural subgraph matching, where subcomponents have been presented in existing research. The authors observe that prior methods for neural graph matching have been narrowly focused, with most methods falling into limited design categories. To address this, the authors organize a comprehensive framework including key architectural choices: relevance distance, interaction stages, interactions structures, interaction non-linearity, and interaction granularity. Extensive experiments demonstrate that unexplored combinations within this design space can lead to performance improvement.

### Strengths
- The authors show a detailed and thorough literature survey on neural subgraph matching and introduce general subcomponents for subgraph matching models.
- The authors conduct extensive experiments on all possible combinations within design spaces.
- The authors discover a new combination of subcomponents that outperforms the existing state-of-the-art model.

### Weaknesses
 -  While the paper does a thorough job of exploring the design space or structured ablation studies, it does not provide a principled explanation of why certain configurations (or subcomponents) yield performance improvements. Adding a more in-depth empirical and theoretical analysis can address this issue. This can not only strengthen the contributions but also offer a more principled foundation for future research in this area.
- Although the best combination shows performance benefits, its novelty is limited. The only differences between the best model and the existing state-of-the-art (IsoNet) are the interaction stage and non-linearity (which have been proposed in existing studies). Without providing principled rationales (as the first bullet), this could make the contributions appear incremental.
- The dense presentation makes it challenging for readers to immediately see the paper’s structure and key subcomponents. I think the authors should present a clearer organization and structured outline. In particular, Figure 1 is hard to interpret. I think that the authors can provide more human-readable visualization. Plus, please put some margin to the bottom of Figure 1.

### Questions
.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper studies the problem of neural network based subgraph matching, focusing on several model/system design choices, e.g. early vs late interaction, trainable vs fixed non-linearity, etc. A set of guidelines and best practices are outlined which are the key contributions of this work.

### Strengths
1. The overall problem formulation is interesting and timely considering the various design choices in subgraph matching literature.
2. Ample experimental study is performed adding credibility and rigorousity to the findings and guidelines.
3. Error bar is shown for the results, e.g. in Figure 2.

### Weaknesses
1. It seems all the 10 datasets are relatively small, e.g. up to 50 nodes. I wonder if there is a reason for not choosing much larger graphs, e.g. graphs up to 1M nodes as the target graph to be searched for (while using a small query graph of ~50 nodes).
2. Some of the paper writing can be made more clearer. E.g. “Challenging the widely
held expectation that early interaction is more powerful, IsoNet’s late interaction approach outperforms GMN, even when GMN’s final score computation is made asymmetric” – It is a bit unclear what it means by “asymmetric”, especially due to the fact this is written at the beginning of intro and the audience may not be familiar with this area of research. 
3. It may be useful to introduce/outline the summarized findings at the end of the introduction section.

### Questions
1. How is this work related to neural architecture search (NAS)? It might be worth comparing/surveting works in NAS, e.g. https://arxiv.org/pdf/2403.05064v1, https://openreview.net/pdf?id=GcM7qfl5zY, etc. Referencing such works can position this work better within the broader literature and bring out further discussion.

### Soundness
2

### Presentation
4

### Contribution
3
