# Directed graph transformers meet metabolic networks

- Decision: Reject
- Avg Score: 4.67
- Scores: 5, 3, 6

## Abstract
Technical advances in sequencing have allowed the reconstruction of genome-scale metabolic models (GEMs) for a wide range of microorganisms. These models have been particularly useful for the prediction of essential genes and reactions, which are potential targets for antimicrobial therapies. However, current methods for essentiality prediction are computationally limited and are not able to accommodate the increasingly available data. Motivated by the success of data-driven approaches in other domains, this work introduces the metabolic transformer, a model designed for holistic identification of essential reactions in  genome-scale models, entirely trained on synthetic knock-out data.  It is demonstrated that the problem of essential reaction prediction can be theoretically formulated as the identification of redundant nodes in directed bipartite graphs. This reveals the limitations of message-passing schemes and motivates the development of a novel graph transformer architecture specifically tailored for metabolic networks. The proposed architecture is capable of addressing the essential reaction identification problem by capturing both the directionality and global structure of metabolic networks. To demonstrate the effectiveness of our approach, we composed a large-scale dataset of genome-scale models reconstructed from real microorganisms.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper is aimed at predicting gene essentiality in metabolic networks. The authors propose "Metabolic Transformer", a directed-graph-based transformer architecture for learning the task.

### Strengths
The paper proposes a synergistic simulation-machine learning approach to an important problem in metabolic engineering, by combining Flux Balance Analysis, a linear programming-based approach for simulating the steady-state of a metabolic network, with a graph Transformer architecture. The Transformer part is based on recent approaches (Chen et al., 2022, and Rampasek et al, 2022).

### Weaknesses
As the authors mention, the Transformer architecture is based on prior work, and not novel in itself. The authors claim that a machine learning model trained on the results from FBA can provide the ability to scale essentiality prediction beyond what is possible with FBA, but do not provide a convincing example in the experimental validation.

The experimental results also do not show conclusively that the method performs better than prior work, the F1 scores are similar or lower, while the AUROC is higher - however, information about precision-recall curve (AUPR) is not provided.

The authors may want to reconsider the use of the work "synthetic", it seems from that manuscript that it is used as equivalent to "in silico". "Synthetic" is typically used as part of the term "synthetic lethality" in gene essentiality studies.

### Questions
What are the AUPR values in the experiments?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper presents a novel graph transformer architecture designed for holistic identification of essential reactions in genome-scale models (GEMs), leveraging a large dataset of over 23,000 GEMs from a variety of microorganisms. The authors formally define "essential reactions" and employ synthetic knock-out data for training, which they claim addresses the computational limitations of current methods in handling large-scale metabolic data.

### Strengths
1. Addressing the identification of essential reactions in metabolic networks is a significant 
2. The proposed dataset seems to be new for this direction

### Weaknesses
1. The most insightful section to formulate the essential reaction prediction problem is not this paper's contribution, as it's already formally stated in FlowGAT's Method

2. The major issue of this paper is a simple application of directed graph transformer on essential reaction prediction task. It lacks novelty in the methodological approach; the architectural innovations appear incremental, as the "directed graph transformer" already exists and is not proposed by authors 

3. the experimental results are weak. Because the validation of the synthetic data and the incongruent results between F1 scores and ROC AUC metrics suggest potential issues in model evaluation and performance stability.

### Questions
1. Is there any novelty in the model architecture? what's the difference between this architecture and "Transformers Meet Directed Graphs" https://arxiv.org/pdf/2302.00049

2. In Sec. 5, "Metabolic Transformer" refers to the GPS-based or SAT-based model?

3. In Tab. 1, why does FlowGAT get a high F1 while ROC AUC < 0.5 indicates non-learning?

4. Is FlowGAT the only baseline? How about other standard GNNs or Graph Transformers?

5. Why in Tab. 2, does FlowGAT have much higher F1 while much lower ROC AUC?

### Soundness
2

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
2

### Summary
The paper introduces metabolic transformers, a new transformer based architecture tailored for processing metabolic networks. They apply this model to prediction of reaction essentiality in metabolic networks.

### Strengths
The paper will release a curated dataset of >20k GEMs from more than 100 different microorganisms.

Introduces "metabolic transformers"

### Weaknesses
The problem of predicting reaction essentiality is not adequately motivated, given there are already other efficient means of solving it (LP). In comparison to this, the authors claim that their metabolic transformer can process all reactions in a network in parallel, but it is not clear in what context could this be necessary.

Furthermore, the claim of processing all reactions in parallel needs more clarification. While it is true that a single forward pass of the transformer can generate predictions for all reactions, the computational cost of this single pass, especially with large metabolic networks, is not discussed. The authors should provide a more detailed analysis of the computational complexity of their approach compared to LP, including memory requirements and practical runtime considerations. It is also unclear if the parallel processing is truly advantageous given the potential overhead of loading the entire network into memory for a single forward pass.

### Questions
As the authors mention, reaction essentiality can be computed by solving an LP program for each reaction. Can the authors further comment on the advantages of their metabolic transformer approach vs. the LP based one ?

Can the metabolic transformer be used to address other more challenging problems about metabolic networks ? For example, sampling feasible flux vectors, solving convex optimization problems posed on metabolic networks (see arXiv:1501.02454) ?

### Soundness
4

### Presentation
3

### Contribution
2
