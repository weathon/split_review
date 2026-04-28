# Theoretical Analyses of Hyperparameter Selection in Graph-Based Semi-Supervised Learning

- Decision: Reject
- Avg Score: 5.25
- Scores: 6, 3, 6, 6

## Abstract
Graph-based semi-supervised learning is a powerful paradigm in machine learning for modeling and exploiting the underlying graph structure that captures the relationship between labeled and unlabeled data. A large number of classical as well as modern deep learning based algorithms have been proposed for this problem, often having tunable hyperparameters. We initiate a formal study of tuning algorithm hyperparameters from parameterized algorithm families for this problem. We obtain novel $O(\log n)$ pseudo-dimension upper bounds for hyperparameter selection in three classical label propagation-based algorithm families, where $n$ is the number of nodes, implying bounds on the amount of data needed for learning provably good parameters. We further provide matching $\Omega(\log n)$ pseudo-dimension lower bounds, thus asymptotically characterizing the learning-theoretic complexity of the parameter tuning problem. We extend our study to selecting architectural hyperparameters in modern graph neural networks. We bound the Rademacher complexity for tuning the self-loop weighting in recently proposed Simplified Graph Convolution (SGC) networks. We further propose a tunable architecture that interpolates graph convolutional neural networks (GCN) and graph attention networks (GAT) in every layer, and provide Rademacher complexity bounds for tuning the interpolation coefficient.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper delves into the theoretical analysis of hyperparameter selection in graph-based semi-supervised learning, specifically focusing on label propagation algorithms and modern graph neural networks.

### Strengths
- The paper presents a novel theoretical analysis of hyperparameter selection in graph-based semi-supervised learning, particularly for GNNs.
- The theoretical guarantees can guide the design of efficient and robust hyperparameter selection methods in practice.

### Weaknesses
 - The paper presents a novel theoretical analysis of hyperparameter selection in graph-based semi-supervised learning, particularly for GNNs.
- The theoretical guarantees can guide the design of efficient and robust hyperparameter selection methods in practice.

 - The experiment in the main body of the paper is limited.
- Considering the proposed GCAN is part of the central contribution of this paper, the comparison between GCAN and baselines should be included in the main body instead of the appendix.

### Questions
How do the proposed methods compare to existing hyperparameter tuning techniques, such as grid search and Bayesian optimization, in terms of efficiency and accuracy?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper studies hyperparameter tuning in GNN frameworks through Rademacher complexity analysis.

### Strengths
The theoretical approach to studying hyperparameter tuning is interesting.

### Weaknesses
 - The core Rademacher complexity analysis largely builds upon work from [1]
- The paper's positioning is unclear - whether it aims to propose a new framework competing with GAT and GCN, or purely offers theoretical analysis of hyperparameter tuning

- Results in Table 1 show minimal practical significance:

  - Many means are identical with only slight interval differences 
  - Where differences exist, they appear negligible

- The definition of $n$ is inconsistent between lines 140-145 (instances per problem) and line 295 (total labeled/unlabeled datapoints)
- The independence of bounds from $n$ in Theorems 4.2 and 4.3 requires explanation
- The rationale for GCAN's additional hyperparameter search isn't justified given the marginal improvements

### Questions
**More Questions:**

- Does this analysis extend to node classification or graph classification in GNNs?
- Can this approach generalize to other hyperparameter tuning scenarios beyond GNNs?
- Please clarify how CIFAR-10 is treated as a graph dataset
- Could you elaborate on your work's relationship to [2]?
- What justifies the additional complexity of GCAN's hyperparameter search?

---

**References:**

- [1]: Vikas Garg, Stefanie Jegelka, and Tommi Jaakkola. Generalization and representational limits of graph neural networks. In Hal Daumé III and Aarti Singh (eds.), Proceedings of the 37th In- ternational Conference on Machine Learning, volume 119 of Proceedings of Machine Learning Research, pp. 3419–3430. PMLR, 13–18 Jul 2020. 

- [2]: Hsu, Kelvin, Richard Nock, and Fabio Ramos. "Hyperparameter learning for conditional kernel mean embeddings with rademacher complexity bounds." Machine Learning and Knowledge Discovery in Databases: European Conference, ECML PKDD 2018, Dublin, Ireland, September 10–14, 2018, Proceedings, Part II 18. Springer International Publishing, 2019.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper takes a theoretical examination of hyperparameter tuning for graph-based semi-supervised learning (GSSL) algorithms, focusing on label propagation methods and graph neural networks (GNNs). New pseudo-dimension upper bounds and matching lower bounds for hyper-parameter tuning are proved, and the Rademacher complexity bound for tuning the weight of SGC is provided, together a new model, GCAN, that interpolates between GCNs and GATs.

### Strengths
1. The paper offers a rigorous theoretical analysis with novel insights into hyperparameter tuning complexities. To the best of the reviewer’s knowledge, this is the first to provide generalization guarantees to the problem of hyperparameter selection.

2. It presents a unified approach to analyze different GSSL algorithms, which is commendable. The introduction of the GCAN model is innovative and empirical results support its potential effectiveness.

### Weaknesses
1. It is unclear about the practical usefulness of the theoretical studies. This paper only considers tuning the single real-valued hyperparameter; it is unclear whether or not the proposed theoretical guarantees and models are able to apply to learning multiple hyper-parameters. The analysis focuses on bounding the Rademacher complexity with respect to a single hyperparameter, but in practice, many GSSL algorithms have multiple hyperparameters that interact in complex ways. For example, GNNs often have multiple layers, each with its own set of hyperparameters, such as learning rate, dropout rate, and weight decay, and it is not clear how the presented analysis can be extended to this more realistic scenario. Furthermore, the theoretical bounds are derived under specific assumptions about the graph structure and data distribution, which may not hold in real-world applications, thus limiting the practical applicability of the results.

2. The analysis is specific to certain algorithms (i.e., SGC), and it is unclear how these findings generalize to other models. While the paper presents a unified approach for analyzing label propagation methods, the theoretical results for GNNs are primarily focused on SGC and the proposed GCAN model. It is not clear if the same proof techniques and bounds can be applied to other popular GNN architectures, such as GCN, GraphSAGE, or GAT, which have different aggregation mechanisms and parameterizations. For example, the analysis relies on specific properties of the SGC model, such as its linear nature, which may not hold for more complex GNNs. Therefore, the generalizability of the theoretical findings to a broader range of GNN models remains a significant concern.

### Questions
1. How do the theoretical bounds scale with different dataset sizes and graph structures?

2. Can the GCAN approach be extended to interpolate between other GNN architectures?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper studies the problem of hyperparameter selection in graph-based semi-supervised learning. The theoretic analysis starts from three classical label propagation algorithms: local and global consistency algorithm, smoothing-based algorithm and normalized adjacency matrix-based algorithms. For each of them, the authors show that the upper and lower bound of the pseudo-dimension is of order $\log (n)$, where $n$ is the number of nodes in graph. Then the authors turn to some modern GNN models including SGC, GCN and GAT. Concretely, the authors propose a GNN model named GCAN that linearly combines the update of GCN and GAT via a hyperparameter $\eta$. For the case that $\eta=0$ and $\eta=1$, the GCAN degenerates to GCN and GAT, respectively. For SGC and GCAN, the authors analyze the upper bounds for the Rademacher complexity of tuning the interpolation coefficient. Both of them are of order $\sqrt{\log m/m}$, where $m$ is the number of training nodes with labels. Finally, the authors conduct experiments to demonstrate that GCAN has a matched or better performance compared to GAT and GCN.

### Strengths
The problem studied in this paper is significant, i.e., analyzing the sample complexity of selecting a proper hyperparameter for graph-based semi-supervised learning algorithms, since the selection of hyperparameter has a significant effect on the performance of learning algorithms. From my own perspective, the main contribution of this paper is the analysis for three classical label propagation algorithms, where the authors present both upper and lower sample complexity bounds for each of them. Particularly, the upper and lower bounds are matched, which makes the theoretic results convinced. And, the proof technique of deriving the lower bounds is novel and interesting, where the authors carefully construct a hard learning example.  I believe that these results could bring some new insights to the community.

### Weaknesses
 - The theoretic analysis in this paper only consider single real-valued hyperparameter, e.g., the one control the trade-off between the
 local and the global consistency or the interpolation between two update rules. This significant limits the application of the theoretic results. Particularly, this kind of analysis is less sufficient for modern GNN models. There exist many hyperparameters in the optimization algorithm used for training, e.g., the learning rate and the weight decay in Adam, and they also have significant impact on the performance of model. It seems that the technique used in this paper could not be easily extend to these cases since the Rademacher complexity could not directly reflect the impact from learning algorithms. Also, I think that the title of this paper seems to exaggerate its actual workload.
- The analysis for SGC and GCAN seems to rely on the technique and assumption used in (Garg et al., 2020), i.e., treating each node as a computation tree and requiring that these trees are independent to each other. This assumption seems too strong for GNN models and raises a gap between theory and practice. Indeed, the training and evaluation of model GNNs follows the transductive learning setting [1,2], i.e., some nodes are sampled without replacement from the graph and their labels are revealed to the GNN model. Therefore, the training and test nodes are dependent. I think that using the transductive learning setting [3,4,5] to conduct the theoretic analysis could be better.

### Questions
Q1: It seems that the experiments result in this paper only demonstrate the performance of the proposed GCAN model, and there are no other ones about the bounds you derived. Could you provide some experiments to verify your theoretic results ?

Q2: I am concerned about some steps in the proof of Lemma C.1. In line 1004-1010, it seems that you have used the following inequalies
$$
\frac{1}{\sqrt{(d_i+\beta)(d_j+\beta)}} = \frac{1}{\sqrt{d_i d_j + \beta (d_i + d_j) + \beta^2}} \leq \frac{1}{\sqrt{C^2_{dl} + 2\beta C_{dl} + \beta^2}} = \frac{1}{C_{dl}+\beta},
$$
where the inequality comes from $d_i, d_j \leq C_{dl}$. However, the following could not be true
$$
\left\\Vert \frac{1}{\\sqrt{(d_i+\beta)(d_j+\\beta)}} - \\frac{1}{\sqrt{(d_i+\beta')(d_j+\beta')}} \right\Vert \\leq \left\\Vert \\frac{1}{C_{dl}+\\beta} - \frac{1}{C_{dl}+\beta'} \right\\Vert
$$
since the sign of the second term is negative. I think that the right one should be derived as follows:
\begin{equation}
\begin{aligned}
& \left\\Vert \frac{1}{\\sqrt{(d_i+\beta)(d_j+\\beta)}} - \\frac{1}{\sqrt{(d_i+\beta')(d_j+\beta')}} \right\Vert  \\\\
= & \left\Vert \frac{(d_i+\beta)(d_j+\\beta) - (d_i+\beta')(d_j+\\beta')}{\\sqrt{(d_i+\beta)(d_j+\\beta)}\\sqrt{(d_i+\beta')(d_j+\\beta')}[\\sqrt{(d_i+\beta)(d_j+\\beta)}+\\sqrt{(d_i+\beta')(d_j+\\beta')}]} \right\Vert \\\\
= & \left\Vert \frac{(d_i+d_j+\\beta+\\beta')(\\beta-\\beta')}{\\sqrt{(d_i+\beta)(d_j+\\beta)}\\sqrt{(d_i+\beta')(d_j+\\beta')}[\\sqrt{(d_i+\beta)(d_j+\\beta)}+\\sqrt{(d_i+\beta')(d_j+\\beta')}]} \right\Vert \\\\
\leq & \left\Vert \frac{2(C_{dh}+C_{dl})}{(\beta+C_{dl})(\beta'+C_{dl})[(\beta+C_{dl})+(\beta'+C_{dl})]} (\beta - \beta') \right\Vert \\\\
\leq & \\frac{C_{dh}+C_{dl}}{C^3_{dl}}\Vert \beta - \beta' \Vert.
\end{aligned}
\end{equation}
And other results should be revised accordingly.

### Soundness
3

### Presentation
2

### Contribution
2
