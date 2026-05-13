# Inference of Sequential Patterns for Neural Message Passing in Temporal Graphs

- Decision: Reject
- Scores: 5, 3, 5, 5

## Abstract
The modelling of temporal patterns in dynamic graphs is an important current research issue in the development of time-aware Graph Neural Networks (GNNs).
However, whether or not a specific sequence of events in a temporal graph constitutes a \emph{temporal} pattern not only depends on the frequency of its occurrence.
We must also consider whether it deviates from what is expected in a temporal graph where timestamps are randomly shuffled.
While accounting for such a random baseline is important to model temporal patterns, it has mostly been ignored by current temporal graph neural networks.
To address this issue we propose HYPA-DBGNN, a novel two-step approach that combines (i) the inference of anomalous sequential patterns in time series data on graphs based on a statistically principled null model, with (ii) a neural message passing approach that utilizes a higher-order De Bruijn graph whose edges capture overrepresented sequential patterns.
Our method leverages hypergeometric graph ensembles to identify anomalous edges within both first- and higher-order De Bruijn graphs, which encode the temporal ordering of events. 
Consequently, the model introduces an inductive bias that enhances model interpretability.

We evaluate our approach for static node classification using established benchmark datasets and a synthetic dataset that showcases its ability to incorporate the observed inductive bias regarding over- and under-represented temporal edges. 
Furthermore, we demonstrate the framework's effectiveness in detecting similar patterns within empirical datasets, resulting in superior performance compared to baseline methods in node classification tasks. 
To the best of our knowledge, our work is the first to introduce statistically informed GNNs that leverage temporal and causal sequence anomalies. 
HYPA-DBGNN represents a promising path for bridging the gap between statistical graph inference and neural graph representation learning, with potential applications to static GNNs.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper studies how to model temporal patterns in dynamic graphs and proposes to use statistical graph inference to identify sequence anomalies for graph augmentation and perform message passing on it to capture inductive biases of sequence patterns. The effectiveness of the model is tested on a synthetic dataset and five empirical datasets for static node classification.

### Strengths
- The idea of augmenting the input graph for message passing using a statistical null model to detect abnormal temporal patterns and distinguish sequences beyond frequency is interesting.

- The adapted HYPA offers an interpretable way to identify unusual sequences in dynamic graphs, and the proposed HYPA-DBGNN achieves improved performance over baseline models on multiple empirical datasets.

### Weaknesses
 - The core techniques of using De Bruijn graphs and hypergeometric testing are well established in time series data analysis. The proposed HYPA-DBGNN is, to some extent, an interesting adaptation for GNNs.

- Using De Bruijn graphs with statistical augmentation is a sound approach. However, the paper would benefit from more discussion on why it is optimal for this purpose under the setting for node classification on time-varying graphs, rather than simply improving from DBGNN.

- The evaluation focuses on a limited set of small human interaction networks. Testing on a more diverse set of temporal datasets would better substantiate the model’s broader applicability and generalizability across domains.

### Questions
- Q1 The authors state that computational complexity may not be a limiting factor. Could the authors further clarify the complexity increased from DBGNN. How would they compare to standard temporal GNNs? Meanwhile, all datasets used for evaluation have less than 500 nodes, can the proposed method scale to larger graphs?
- Q2 The results in Tabe 1 on synthetic data try to highlight patterns that only high-order models can discern. However, the results are not convincing or interpretable, especially the discussion of the baseline HONEM (even a strong one in Table 2) is very limited.
- Q3 The proposed method claims to have better interoperability by introducing HYPA. Could the authors elaborate more on how it is made more expressive by not relying on the transitivity assumption?

### Soundness
3

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
This work focuses on relatively novel task, static node property classification for temporal graphs. Different from common trend of temporal graph neural networks, it proposes HYPA-DBGNN that extends a previous work GBGNN (which combines static hyper-order graph neural network on a high-order De Bruijn Graph constructed from time series) by null model correction.

### Strengths
- This work focuses on static node property classification on temporal graph, which is task lack of exploring.

### Weaknesses
 - The notation is lack of consistency, making it hard to follow and the clarify of method details being quite poor. (See questions)
- This paper focuses on a rare task, which I think more real-world justification is needed? For example, what are real-word scenarios? You can pick one of your dataset to explain this in more detail.
- The contribution of the proposal is slightly unclear. It seems that this work simply extends related work DBGNN by introducing null model correction. If my understanding is correct, I think more theoretical justification of the necessity of this correction should be provided, otherwise, the contribution seems to be limited.
- In both the synthetic and real-world experiments, the variance are very large, makes me doubt if the problem is formalized correctly.
- Compare to highly related baseline DBGNN, the experiment results is not quite impressive (confident interval overlaps a lot in many tasks). This makes the contribution of null model correction less sound given no theoretical justification of the necessity.
- The experimental results on real datasets exhibit large confidence intervals, often overlapping with other baselines, which undermines the claim that the proposed method provides a significant improvement for static node prediction on temporal graphs. The lack of a theoretical justification for why certain temporal paths can only be captured by the proposed method, and not by other baselines, further weakens the contribution. A counterexample, theoretically proving the unique capabilities of the method, is needed.
- The paper lacks a discussion of explainability, which is crucial given the claim that the method provides better insights into temporal patterns. The ability to extract key or anomalous paths from the model's inference is not addressed, thus limiting the practical value of the proposed approach.
- Scalability is not sufficiently addressed. The paper does not discuss the feasibility of training and inference on large temporal graphs (millions of nodes), especially considering the computational cost of building and computing over hypergraphs. This is a significant limitation for real-world applications, particularly in domains like finance where transaction data can be massive.

### Questions
- Figure 1: Why we construct a higher-order edge for count 0? Besides, shouldn't we have an arrow from (a) to (d) since we also need 1-order counts to construct 1-order graph in (d)?
- Figure 1: You should extend the figure with how null model in (b) and weights in (c) are really generated, or provide in appendix? This figure fails to explain what you did for (b) and (c) given the poor explanation of section 4.
- line 262: What is $X_{uv}$ and $f(u, v)$? Why they are independent from order $k$?
- line 282: Shouldn't $H(v)$ rely on order $k$ based on your definition? Same to equation (1).
- Page 6: Mix use of higher order nodes and nodes make the notation is bit hard to follow, recommend to replace $v$ by $v^{(k)}$ in all related content, or vector form $\mathbf{v}$. Then, you can claim that $k = 1$ is omitted by default.
- line 292: Why map $h^{1, 0}$ to $h^{k, 1}$ rather than $h^{k, 0}$?
- line 295: Can you provide more explanation how this bipartition is analogous to Markov chain?
- line 304: What is $g$?
- Why this design is limited to temporal node classification? I think this architecture can be used for regression without any modification.
- line 331-351: Hyperparamter configuration can be moved to appendix so that you can have more space to improve clarity of algorithm design sections.
- Experiment: You are comparing with a lot of simple baselines for static graph with only on temporal graph baseline. Based on [1], static and temporal graph representation are indeed equivalent, especially you are performing static node classification on temporal graph. Why you don't compare with other basics such as GAT, GIN, TGAT, DySAT (see [1]), and other state-of-the-art like PNA, PINE, GraphTransformer.
- Given that TGN is designed mainly for evolving graph, should you make some modification to make comparison fair? For example, average node representation of different timestamps for perform static node classification on temporal graph?   
- Your font looks different from template. I think you need to check if you are using the template correctly.

[1] Gao, Jianfei, and Bruno Ribeiro. "On the equivalence between temporal and static equivariant graph representations." International Conference on Machine Learning. PMLR, 2022.

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work introduces a model termed HYPA-DBGNN, which seeks to improve the ability of a GNN in temporal settings to learn high-order time dependent interactions. HYPA-DBGNN has two components, HYPA which detects the ``surprise'' of observing a specific walk, and DBGNN which performs a hypergeometric walk feature extraction. The authors detail this model as an extension of DBGNN, and present experiments which show promising performance gains.

### Strengths
1. The paper is well organized and motivated.
2. The problem of extracting complex relationships from transitions between vertices is an interesting problem with many industrial applications
3. The experiments that are presented appear to be carefully performed and well motivated. The results as presented provide evidence that the method works.

### Weaknesses
1. The paper is unclear in spots. For example, The concept of a De Bruijn graph is mentioned but its basic properties are not discussed. Specifically, the paper does not explain how the De Bruijn graph is constructed from the temporal walks, nor does it discuss the implications of the chosen k-mer size on the resulting graph structure and the information it captures. This lack of clarity makes it difficult to assess the validity of the approach.
2. The mathematical notation is intricate and can be difficult to follow, with some symbols overlapping with standard symbols from the literature. For example, $H(v)$ is the sum of $HYPA$ factors but is traditionally the hidden representation for all vertices. This overloading of notation creates confusion and makes it harder to understand the core mechanics of the proposed model. The paper should adopt a more consistent and less ambiguous notation.
3. The intuition for
4. Minor typos and grammatical issues make the paper somewhat difficult to follow. For example, `fist` -> `first` on line 314. The presence of these errors detracts from the overall quality of the paper and suggests a need for more careful proofreading.
5. Experiments in section 5.2 seem to lack many modern baselines including CAWN, TGAT, DySAT, and others. I would recommend that the authors add additional baselines. Random walk GNNs such as RWGNN could be applicable here as well, as could transformer architectures. The absence of these comparisons makes it difficult to evaluate the true performance of the proposed method relative to the state-of-the-art.
6. The experimental setup is unclear in spots, the baselines may have been untuned, and the graphs are small. The paper lacks details on hyperparameter tuning for both the proposed method and the baselines. The small graph sizes also raise concerns about the scalability of the method and the generalizability of the results.

### Questions
1. Does this new inductive bias lead to a provably more expressive GNN than previous temporal MPNNs?
2. What is the run-time scaling of HYPA-DBGNN? All experiments were run on quite small graphs, so it's hard to understand how scalable of a technique this is.
3. To what extent has hyperparameter tuning been performed?
4. What explains HONEM's good performance in 5.1?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces HYPA-DBGNN, a graph augmentation architecture focused on temporal graph learning. It encodes sequential pattern dynamics in first- and higher-order De Bruijn graphs and corrects graph structures using anomaly statistics. HYPA-DBGNN computes HYPA scores via hypergeometric ensembles to assess edge frequency differences from a random model, adjusting weights to improve accuracy. It uses a multi-order message passing scheme with inductive bias, incorporating HYPA scores and ReLU activation while preserving graph sparsity to optimize efficiency.

### Strengths
1. The paper introduces De Bruijn graphs into temporal graph analysis, which I find to be a novel approach.

2. The paper conducts extensive experiments to demonstrate the effectiveness of the proposed method.

### Weaknesses
1.The paper's exposition is not very clear, with many key pieces of information relegated to the appendices.

2.The paper does not clearly explain why the introduction of De Bruijn graphs enhances performance, making it seem more like a simple combination of existing methods.

3.The explanation of the method is insufficiently clear; a framework diagram could be helpful.

### Questions
1. Could the authors explain the role of De Bruijn graphs?

### Soundness
3

### Presentation
2

### Contribution
1
