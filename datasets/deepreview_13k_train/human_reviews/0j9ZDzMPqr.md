# UNR-Explainer: Counterfactual Explanations for Unsupervised Node Representation Learning Models

- Decision: Accept
- Scores: 6, 6, 6, 8

## Abstract
Node representation learning, such as Graph Neural Networks (GNNs), has become one of the important learning methods in machine learning, and the demand for reliable explanation generation is growing. Despite extensive research on explanation generation for supervised node representation learning, explaining unsupervised models has been less explored. To address this gap, we propose a method for generating counterfactual (CF) explanations in unsupervised node representation learning, aiming to identify the most important subgraphs that cause a significant change in the $k$-nearest neighbors of a node of interest in the learned embedding space upon perturbation. The $k$-nearest neighbor-based CF explanation method provides simple, yet pivotal, information for understanding unsupervised downstream tasks, such as top-$k$ link prediction and clustering. Furthermore, we introduce a Monte Carlo Tree Search (MCTS)-based explainability method for generating expressive CF explanations for **U**nsupervised **N**ode **R**epresentation learning methods, which we call **UNR-Explainer**. The proposed method demonstrates improved performance on six datasets for both unsupervised GraphSAGE and DGI.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work explores explanation generation for unsupervised node representation learning.  The authors propose a Monte Carlo Tree Search (MCTS)-based method to generate counterfactual (CF) explanations. Specifically, this method aims to identify the most important subgraphs that cause a significant change in the k-nearest neighbors of a node. The proposed method is incorporated into unsupervised GraphSAGE and DGI, and the performance on six datasets confirms the efficacy of the proposed method.

### Strengths
1. It is an interesting research topic to improve the interpretability of unsupervised learning models on graphs. 
2. This can help to find the explanations of  GNN models with unseen downstream tasks.
The proposed method is tested on several datasets and shows satisfactory results.
3. The paper is well-structured and organized.

### Weaknesses
1. The work is somehow incremental work. SubgraphX proposed a Monte Carlo tree search algorithm to efficiently explore different subgraphs. Compared with SubgraphX, the authors seem to just add a new policy, “restart”, in the Selection step to mitigate the search bias. The design makes sense but results in limited novelty.
2. The indicators of counterfactual explanations are not rigorous. The perturbations of the input graph not only change the node embedding of interest ($emb_{v} \neq emb_{v}^{'}$) but also change other node embeddings. It does not match the Figure 1 (b) and (c) illustrated.
3. The motivation should be further improved. The authors do not state the challenges of generating counterfactual explanations in unsupervised learning compared with supervised methods, such as CF-GNNExplainer, RCExplainer, and CF2.
4. The authors do not provide real-world applications or pilot studies to support their claim that "the perturbation strategy of adding edges or nodes has a significant risk in real-world scenarios"
5. Minor error: Page 9 The first line is not left-justified; Measures in Table 1 are not arrowed.

### Questions
1. Why do the authors choose the MCTS-based framework rather than other gradient-based or causal-based interpretable methods? Can you show the relevant analyses?
2. Can the authors state what new challenges your approach addresses compared to existing counterfactual explanation methods on supervised learning?
3. Can the author give some applications of real-world scenarios or do some pilot studies to show the benefit of the perturbation strategy of only removing edges?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces a novel method for explaining graph neural networks. The authors focus on counterfactual explanations and propose the UNR-Explainer, which aims to identify subgraphs that, when perturbed, lead to significant changes in node embeddings. The paper evaluates various explanation methods in unsupervised settings using synthetic and real-world datasets. The proposed method leverages the Monte Carlo Tree Search (MCTS) for efficient traversal in large search spaces. The paper also provides a theoretical analysis of the upper bound of Importance and discusses the algorithm for calculating Importance.

### Strengths
1)	The paper tackles CF reasoning in unsupervised settings, a relatively unexplored area potential implications for explainability in graph neural networks and unsupervised learning.
2)	The paper leverages the Monte Carlo Tree Search (MCTS), a technique from reinforcement learning, to efficiently traverse the search space of potential subgraphs. MCTS is known for its effectiveness in large search spaces, making it a suitable choice for this problem.
3)	The paper clearly defines the counterfactual property for unsupervised representation learning models, providing a solid foundation for their method.
4)	The paper includes a theoretical analysis of the upper bound of Importance for GraphSAGE, adding a rigorous foundation to their empirical findings.

### Weaknesses
1) While the paper does evaluate on both synthetic and real-world datasets, it might benefit from testing on more diverse datasets, especially those from different domains or with different characteristics. Information on how the method scales with larger datasets or more complex graphs, and its computational efficiency, would be valuable. Specifically, the paper lacks a thorough analysis of the computational cost associated with the Monte Carlo Tree Search (MCTS) when applied to graphs with varying densities and node degrees. The current evaluation does not sufficiently explore the trade-offs between explanation quality and computational resources, which is crucial for practical applications.
2) I believe the paper would greatly benefit from additional visual illustrations or diagrams to depict the proposed method. Visual aids can provide a clearer understanding and offer readers an intuitive grasp of the methodology. Given the complexity and novelty of the approach, diagrams or flowcharts could enhance comprehension and make the content more accessible to a broader audience. The absence of a clear visual representation of the MCTS exploration process and the perturbation mechanism makes it difficult to grasp the core mechanics of the UNR-Explainer.

### Questions
1)	How does the method scale with larger and more complex graphs? Are there any computational or memory constraints that might limit its applicability to very large datasets?
2)	How sensitive is the method to the degree of perturbation applied to the subgraph? Would minor changes in perturbation lead to significantly different results in the algorithm of importance?
3)	Given the contrastive approach employed by DGI and the inductive learning capability of GraphSAGE, how might these characteristics influence the types of counterfactual explanations generated? Furthermore, how would the proposed counterfactual explanation method adapt and perform when integrated with generative models such as GraphGAE or S2GAE?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a method called UNR-Explainer for generating counterfactual explanations in unsupervised node representation learning models. The goal of these explanations is to provide information for understanding unsupervised downstream tasks. UNR-Explainer performs Monte Carlo Tree Search to find the explanation subgraph. The subgraph importance is measured by the change of the top-k nearest neighboring nodes after perturbation. UNR-Explainer is evaluated on six datasets including both synthetic ones and real-world ones, and UNR-Explainer is shown to outperform existing explanation methods.

### Strengths
1. UNR-Explainer shows the good quantitative performacne, and the case study on NIPS shows UNR-Explainer can select qualititatively meaningful subgraphs.

2. The importance metric proposed in Equation 1 is novelt to me.

3. Time complexity analysis and discussion of limitation are both included in the appendix.

4. Code is provided for reproducibility.

### Weaknesses
1. Lacking discussions. Some baseline methods considered in the experiment section are very simple but achieve strong performance without discussion or analysis. Specifically, the 1hop-2N and 1hop-3N baselines achieve surprisingly high precision on synthetic datasets, and this is not adequately addressed. The paper should delve into why these simple baselines perform so well in these specific cases, rather than just reporting the results. This lack of analysis weakens the overall argument for the proposed method's superiority.

2. Efficiency. MCTS-based explanation can be slow compared to other explanation methods, e.g., gradient-based methods, especially on large graphs. This is verified by the time complexity as well. The paper acknowledges this but does not fully explore the implications for practical use cases. The computational cost of MCTS could be a significant barrier for real-world applications with large graphs, and this limitation needs more thorough discussion.

3. Presentation can be further improved. Some figures have text that is too small to read. For example, embedding labels in figure 2. The small text makes it difficult to understand the details of the visualization, hindering the reader's ability to grasp the results effectively.

### Questions
1. In Table 1 for the synthetic datasets, the naive random selection baselines 1hop-2N and 1hop-3N achieve the best results in terms of precision. Why? Any discussions?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors introduce a new method to obtain counterfactual (CF) explanations from unsupervised node learning. Their method uses a learned unsupervised node learning method to get embeddings. They then define their method via the importance function which they try to maximize while minimizing the edge alterations to the graph (minimizing the counterfactual explanation). They provide an upper bound on the Importance function. 

They alter a Monte Carlo Tree Search (MCTS) method to get the CF. The MCTS uses the Importance function as a reward which looks for subgraphs that are important but sparse. They show that their MCTS does not degrade the expressiveness of subgraph explanations like the vanilla MCTS would by altering the reward function. They do this by choosing the action where the upper confidence boundary (UCB a term used in their MCTS which dictates which edge to take in traversal) is larger. They also show analysis showing that the UCB for an edge that leads to a new node is greater thus prioritizing exploring new paths. They claim these alterations to the vanilla MCTS leads to more expressive explanations which are partially supported by theoretical claims. 

They also have quite a large and expansive set of experiments. They do experiments on 3 synthetic datasets (BA-Shapes, Tree-Cycles, and Tree-Grid) and 3 real datasets (Cora, CiteSeer, and PubMed), parameter sensitivity study, ablation study and a case study. They conduct their experiments on 8 methods (including theirs) on several metrics: Precision/Recall, Validity, size of the model and Importance. They show promising behaviour of their method in comparison to other methods in many settings with various evaluation metrics. They also show a case study on the NIPS dataset a social network of citations. They show by perturbing explanation graphs on a particular author they can obtain a graph that belongs to a different author that belongs to a different subfield of ML. They also conduct an ablation study showing variants of the MCTS algorithm which is fundamental to their methodology. They show their variant of MCTS can find expressive explanations (high importance score) while being efficient. Finally they also show experiments of parameter sensitivity. They show what effects the choice of the restart parameter, perturbation parameter, and the number of neighbors has on their method. They do this by varying the choice of hyperparameter and evaluating the importance score on the Cora Dataset.

### Strengths
The paper is very well written. The design of the paper from problem definition, to methodology, to experimental evaluation follows clearly and is well designed. The authors also motivate their work by addressing the problem in a well defined manner. The Importance measure is novel and inventive way to quantify the counterfactual explanation. The alterations to the MCTS to construct these counterfactual explanations is reasonable and well grounded by theory to supplement their decisions. The paper also employs theory on the Importance measure to show an upper bound. 

The experimental list is fairly exhaustive and shows superior performance to several other methods in multiple datasets and cases. The case study is a nice touch to display their method’s ability to obtain meaningful counterfactual explanations. The ablation study shows that their variant of MCTS can find expressive subgraphs while being efficient in comparison to other tree search methods. Finally, having a study to show their methods sensitivity/robustness to choices of hyperparameters is important for anyone seeking to employ this method.

### Weaknesses
There could be more discussion on experiments where the UNR-Explainer underperforms compared to other methods. 

Also further explanation on certain hyperparameter choices could be made more clear for the readers. Such as the choice of k in each experimental setting. A discussion on when to use a particular larger/smaller value of k would be interesting. The authors do have experiments showing the sensitivity of the number of neighbors, they also have a limited discussion on this phenomenon. However this hyperparameter is central to their method (their importance measure is heavily influenced by it) a discussion to explain what settings would require very large k vs very small k would be beneficial to solidify their work although it is not necessary.

### Questions
Although the authors provided a study of hyperparameter sensitivity, why did they select k=5. Clearly, as seen in the experiments the choice of k does seem to impact the importance score. More discussion of the effect of the choice of k would be beneficial for practitioners. 

Also their method seems to underperform in the synthetic experiments particularly with the precision measure. Significantly smaller methods do better than UNR-Explainer in these settings which is seemingly consistent throughout the synthetic experiments. Any discussion as to why this is would be beneficial to readers and the authors.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
