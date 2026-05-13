# TopInG: Topologically Interpretable Graph Learning via Persistent Rationale Filtration

- Decision: Reject
- Scores: 6, 5, 6, 6

## Abstract
Graph Neural Networks (GNNs) have shown remarkable performance in various scientific domains, but their lack of interpretability limits their applicability in critical decision-making processes. Recently, intrinsic interpretable GNNs have been studied to provide insights into model predictions by identifying rationale substructures in graphs. However, existing methods face challenges when the underlying rationale subgraphs are complicated and variable. To address this challenge,
we propose TopIng, a novel topological framework to interpretable GNNs that leverages persistent homology to identify persistent rationale subgraphs.
Our method introduces a rationale filtration learning technique that models the generating procedure of rationale subgraphs, and enforces the persistence of topological gap between rationale subgraphs and complement random graphs by a novel self-adjusted topological constraint, topological discrepancy. We show that our topological discrepancy is a lower bound of a Wasserstein distance on graph distributions with Gromov-Hausdorff metric. 
We provide theoretical guarantees showing that our loss is uniquely optimized by the ground truth under certain conditions.
Through extensive experiments on varaious synthetic and real datasets, we demonstrate that TopIng effectively addresses key challenges in interpretable GNNs including handling variiform rationale subgraphs, balancing performance with interpretability, and avoiding spurious correlations. 
Experimental results show that our approach improves state-of-the-art methods up to 20%+ on both predictive accuracy and interpretation quality.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
In this paper, the authors propose a graph explanation method based on the persistent homology to identify stable rational subgraphs via persistent rationale filtration learning. Specifically, they propose a topological discrepancy loss to achieve the goal. Experimental results seem to outperform state-of-the-art models in most datasets.

### Strengths
- The idea of using topological data analysis for graph explanation is novel and interesting. 

- The derivation of the proposed method seems to be solid with theoretical insights.

### Weaknesses
 - The preliminary, especially the TDA, is not very clear, making it hard for readers without the knowledge of persistent homology (I don’t think it is necessarily a prerequisite knowledge for graph explainability). What is the difference of $H$ between the $p$-homology functor $H_p (\mathcal{F} (G))$ and $H_p (G_{\le t})$? Figure 1 is also not easy to understand with a clear explanation of the homology groups. The caption is over lengthy and not illustrating the intuitive idea very well. It will be better to segment the long caption into several parts to make it more readable.

- In the introduction, they mention one challenge that exists in current graph explanation models: that different graphs may contain different core subgraphs even within the same category. Yet, I don’t see why the proposed method can tackle this problem well. The training procedure involves learning a filtration function to separate the graph. How such a mechanism can tackle the challenge and why the separating method in other methods cannot are not well discussed. It is recommended to add more analysis (or examples) to demonstrate why the proposed method can address this challenge and others cannot.

- The prior regularization seems to be empirical. The hyperparameters of the prior are not trivial. This raises concern whether the proposed method is sensitive to the selection of the prior and the corresponding parameters. More discussion is encouraged.



### Questions
- See the weakness above

- The results of MUTAG are not impressive in terms of both interprebility and accuracy. Further analysis for these results are required for better understanding the proposed method.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces TOPING, a novel intrinsically interpretable framework for GNNs that uses topological data analysis (TDA) to identify stable rationale subgraphs. TOPING addresses key limitations in existing interpretable GNN models by using a rationale filtration learning approach. Extensive experimentation shows improvements over state-of-the-art interpretability and predictive performance.

### Strengths
S1. Using TDA for intrinsically interpretable GNNs is interesting. 

S2. The authors provide theoretical guarantees to show that topological discrepancy optimally captures rationale subgraphs. 

S3. The authors present extensive experiments across multiple datasets.

### Weaknesses
W1. The mathematical notation and presentation could be improved, as some definitions and descriptions are unclear or ambiguous. Clarifying these elements would enhance the paper’s readability for readers less familiar with topological data analysis. Specifically, the explanation of how the filtration values relate to the subgraph construction is confusing, and the definition of topological invariants is not mathematically rigorous.

W2. The paper would benefit from a detailed time complexity analysis and runtime study, particularly in comparison with baseline methods. This addition would clarify whether TOPING’s performance improvements come at the cost of efficiency. The current analysis lacks a discussion of the computational cost associated with persistent homology calculations, which are known to be computationally intensive, and how this impacts the overall scalability of the method.

W3. Since TOPING requires learning a filtration function that assigns values to each edge, this method may become impractical for large graphs due to the need to compute and store $|E|$ values. The paper does not adequately address the memory requirements for storing these edge filtration values, nor does it provide a clear strategy for handling graphs with millions or billions of edges. Further discussion on how TOPING might be adapted or approximated for larger graphs would be valuable.

### Questions
Q1. The explanation of TDA in Section 2.2 is unclear. In Figure 1, the subgraph $G_{t}$ appears to have more edges as $t$ decreases. However, in line 170, it seems that $G_{t}$ should contain more edges as $t$ increases. Could the authors clarify this apparent discrepancy?

Q2. In line 271, the term "topological invariants $\tau$ " is introduced without a clear mathematical definition. Could the authors provide a formal definition for $\tau$ to improve understanding?

Q3. In line 278, Equation (3) is not properly referenced. Besides, it appears disconnected from the context. Could the authors clarify its relevance here?

Q4.  The authors state that $f_\phi$ and $h_\phi$ share parameters. However, $f_\phi$ is defined as a function mapping to $[0,1]^{|E|}$, while $h_\phi$ seems to map to $\mathbb{R}^{|V|}$. Could the authors explain how parameter sharing is feasible between these two functions with distinct output spaces?

### Soundness
2

### Presentation
1

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
This paper proposes an interpretable GNN framework that leverages techniques from topological data analysis, specifically persistent homology. The method splits an input graph into a rationale subgraph (important subgraph) and a noise subgraph, where the rationale subgraph is used for both predicting the target and providing an explanation for the prediction. The authors introduce a novel loss function that quantifies the topological discrepancy between the rationale and noise subgraphs and jointly optimize this loss along with the prediction loss. The framework is evaluated using several synthetic datasets and two real-world molecular datasets, demonstrating its effectiveness.

### Strengths
1.	This paper introduces an innovative use of topological analysis to provide intrinsically explainable GNNs, offering a promising direction for future research.
2.	The authors proved that the method can optimize to the true important subgraph under certain conditions, providing a solid mathematical foundation for the approach.

### Weaknesses
1.	The writing is difficult to follow due to unclear definitions of the mathematical symbols used (see questions below). The figures are not well-explained and can be confusing, especially for readers with limited knowledge of topological analysis.
2.	The experimental datasets are limited, focusing only on synthetic and relatively simple molecular datasets. Additionally, qualitative visualizations for the MUTAG dataset are missing, which reduces the clarity of the results.

### Questions
1. What is $\beta_1$ in Fig. 1?
1. In Eq. 3, what is $\mathcal R$?
2. What is the difference between $f_{\phi}, h_{\phi}$? In Fig.2 they are all equal to $GNN_\phi$ so they are the same? And is $\phi$ the parameters of GNN?
3. After reading Sec 3 I still have problem understanding how the model predicts. In Fig.2 it seems that the model first generates a subgraph $G_X$ according to the edge score from $f_\phi(G)$, feed it into a GNN $h_\phi$, somehow concatenate with $\mathcal T_X, \mathcal T_\epsilon$, and use a classifier to get the final prediction. What is $\mathcal T_X, \mathcal T_\epsilon$ and how are they concatenated with output of GNN $h_\phi$? A more detailed explanation of Fig.2 is needed.
4. Row 267-269:the defined $\mathcal G, \mathcal F(\mathcal G)$ are never used.
5. Does the measure of topological discrepancy also consider the node/edge features? It would be interesting to see how the method performs on graphs where not only topological structure but also node/edge features are relevant.

### Soundness
2

### Presentation
2

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
This paper proposes a framework TOPING for XGNN, which is similar to the GSAT pipeline. It introduces a rationale filtration learning technique and a topological discrepancy constraint to separate important subgraphs from random ones. The method offers theoretical guarantees and improves both accuracy and interpretability, outperforming existing approaches by over 20% in experiments. However, the comparison with other methods is potentially unfair due to differences in evaluation metrics or datasets.

### Strengths
1. This paper introduces an existing method based on the assumption, "either explicitly or implicitly that the subgraph rationales are nearly invariant across different instances within the same category of graphs." This is a reasonable and novel aspect of the problem. However, there are few experiments to support this idea.
2. This paper introduces the $p$-homology functor to XGNN, which is a novel approach to addressing this problem.

### Weaknesses
1. Some expressions are confusing. For example, in Equation 3, the meaning of $\mathcal{R}$ is unclear. In Figure 2, the meaning of $L_{topo}$ is also not explained. Furthermore, the persistent barcode visualization in Figure 1 lacks explanation, making it difficult to understand the topological features being extracted.
2. In subsection 3.2, the distribution of the prior is determined by the hyperparameters $\mu$ and $r$. However, $\mu$ is a pre-defined parameter, raising the question of how to set this parameter. Additionally, $r$ is a learnable parameter. Will this setting lead to a trivial solution, where the divergence between $\mathcal{N}(\mu_1,r_1)$ and $\mathcal{N}(\mu_2,r_2)$ is small? The use of a bimodal Gaussian prior for edge filtration values, while novel, requires more justification, especially given that other methods use different prior distributions. The potential for mode collapse, where the learned variances $r_1$ and $r_2$ become too small, also needs to be addressed.
3. The comparison is potentially unfair. In Appendix C.2.1, all baselines are based on the GIN backbone, while TOPING uses the CINpp backbone, which could result in biased comparisons. The performance differences could be attributed to the backbone architecture rather than the proposed method itself. The instability of baseline methods with the CINpp backbone needs further investigation and explanation. It is unclear why the baseline methods fail to converge when using the CINpp backbone, and this issue should be addressed in the paper.

### Questions
1. In Figure 1, the meaning of the row lines is unknown.

### Soundness
2

### Presentation
2

### Contribution
2
