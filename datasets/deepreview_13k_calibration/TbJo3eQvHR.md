# Coupling Category Alignment for Graph Domain Adaptation

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 6, 3, 5, 6

## Abstract
Graph domain adaptation (GDA), which transfers knowledge from a labeled source domain to an unlabeled target graph domain, attracts considerable attention in numerous fields. 
Emerging methods commonly employ message-passing neural networks (MPNNs) to learn domain-invariant representations by aligning the entire domain distribution. However, these methods overlook the category-level distribution alignment across different domains, potentially leading to confusion of categories. 
To address the problem, we propose an effective framework named \textbf{Co}upling \textbf{C}ateg{o}ry \textbf{A}lignment (\method{}) for GDA, which effectively addresses the category alignment issue with theoretical guarantees.
\method{} incorporates a graph convolutional network branch and a graph kernel network branch, which explore graph topology in implicit and explicit manners. To mitigate category-level domain shifts, we leverage knowledge from both branches, iteratively filtering highly reliable samples from the target domain using one branch and fine-tuning the other accordingly. Furthermore, with these reliable target domain samples, we incorporate the coupled branches into a holistic contrastive learning framework. This framework includes multi-view contrastive learning to ensure consistent representations across the dual branches, as well as cross-domain contrastive learning to achieve category-level domain consistency.
Theoretically, we establish a sharper generalization bound, which ensures the effectiveness of category alignment.
Extensive experiments on benchmark datasets validate the superiority of the proposed \method{} compared with baselines.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a coupling category alignment method for graph domain adaptation, which includes a graph convolutional network branck and a graph kernel network branch. There two branches iteratively filter reliable samples and training. Based on existing theoretical framework, the authors establish a sharper generalization bound for the proposed method.

### Strengths
The authors highlight a category alignment issue in graph domain adaptation that is often overlooked in existing methods.

They also establish a tighter generalization bound with theoretical guarantees.

Experimental results demonstrate the effectiveness of the proposed method.

### Weaknesses
The novelty of this paper appears incremental. Specifically, the proposed graph convolutional network branch and graph kernel network branch are very similar to the two branches presented in [1]. Additionally, the proposed multi-view contrastive learning and cross-domain contrastive learning approaches are closely aligned with the cross-branch contrastive learning and cross-domain contrastive learning proposed in [1].

This paper lacks self-containment. Many mathematical symbols are used without definition; for example, in line 139, it is unclear what Z, h, and \hat{h} represent.

Some theorem definitions lack rigor. For instance, "Theorem 2" is not a true theorem but rather a corollary inferred from Theorem 1, as also stated in [2]. Similarly, "Theorem 4" should not be classified as a theorem, as it is also a corollary based on an existing theorem.

Theorem 2 seems to be built on a binary classification task. Does Theorem 4, which builds on Theorem 2, apply to the multi-class tasks in this paper? Further explanation is needed here, given that the paper addresses category-level domain shifts.

Experiments are conducted on very small datasets. The proposed method should be validated on other widely used graph domain adaptation datasets, such as the Microsoft Academic Graph (MAG) and Pileup datasets.

### Questions
See weaknesses.

### Soundness
2

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
5

### Summary
The paper proposes a framework named Coupling Category Alignment (CoCA) for graph domain adaptation. The framework incorporates a message passing neural network branch and a shortest path aggregation branch to address the category alignment issue in graph domain adaptation. The authors also provide theoretical guarantees for the effectiveness of category alignment. Extensive experiments on benchmark datasets demonstrate the superiority of the proposed CoCA compared to baselines.

### Strengths
(1) The paper proposes a framework, CoCA, which effectively addresses the category alignment issue in graph domain adaptation.
(2) The framework incorporates both implicit and explicit topological semantics through the message passing branch and shortest path aggregation branch, respectively.
(3) The authors provide theoretical guarantees for the effectiveness of category alignment in the CoCA framework.

### Weaknesses
 (1) The motivation of this manuscript is not clear. The authors should clearly claim the challenging issues in previous methods.

### Questions
See Weaknesses

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper revisits Graph Domain Adaptation (GDA) methods and incorporates a dual-branch network to explore graph topology in implicit and explicit manners. To leverage knowledge from both branches, the authors iteratively filter highly reliable samples from the target domain using one branch and fine-tuning the other. The authors also present a contrastive learning strategy from multi-view to achieve category-level domain consistency information. The experiments on several benchmarks show the performance of the CoCA compared to the baselines.

### Strengths
1. The motivation is clear and the GDA semantic alignment framework is well-designed.
2. A specific contrastive learning-based mechanism is developed under the GDA framework and shows promising results compared with conventional GDA methods.

### Weaknesses
Experimental analyses are insufficient. As in CoCo and DEAL, the experiments on real-world benchmark datasets (e.g., DD, COX2, COX2_MD, BZR, and BZR_MD) will be much more informative. Authors could prove the effectiveness of their strategies by constructing experiments on various real-world datasets as the previous work CoCo and DEAL. Besides, the new processed dataset is also not publically available, from the paper I can't get a sufficient understanding of this specific setting.
2.Although the results in Table 1 and Table 2 are impressive, it is unclear if the comparison is completely fair. Specifically, this paper compares their results with other works on the conventional graph network backbone. The authors exploit a new GMT graph network as the MPbranch while many methods in Table 1 and 2 do not use a new graph network. Comparing previous methods with the proposed attention-based method on conventional graph network is not fair.

3. The method seems like an application on the GDA network with respect to the graph kernel method. In the introduction, the first contribution is not specific to this paper. The discussion for solving the discrepancy in the distribution of graph categories between the source and target domains was already in DEAL.

### Questions
1. Most of the compared GDA methods were published before 2022. To fully validate the superiority of the proposed CoCA model, more SOTA UDA methods should be included in comparison experiments.
2. More insightful analyses should be provided. For example, the visualization of the feature refined by the SP branch should be shown.
3. The current experiments are conducted on specially set datasets, which is not sufficient. It is recommended to conduct on real-world datasets as previous works CoCo[1] and DEAL[2].

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a new approach called "Coupling Category Alignment" (CoCA) aimed at addressing category-level distribution alignment in graph domain adaptation. The method leverages a dual-branch framework, combining message-passing neural networks with shortest path aggregation, to manage domain shifts between source and target graphs. CoCA incorporates cross-domain and multi-view contrastive learning to enhance representation consistency, showing theoretical guarantees of reduced empirical risk bounds and validating its effectiveness through extensive experiments across various datasets.

### Strengths
1. This work targets a significant and challenging problem in domain adaptation for graphs, with an emphasis on category alignment, which is often overlooked in the literature.
2. The dual-branch design provides an interesting approach to combining implicit and explicit semantic extraction, potentially improving representation robustness across domain shifts.
3. The proposed CoCA model is theoretically grounded, offering formal guarantees of its effectiveness, which is a positive addition to the methodological contributions.
4. The experimental results indicate that CoCA outperforms existing baselines, demonstrating the method's potential for practical applications in graph domain adaptation.

### Weaknesses
1. The paper makes ambitious claims about CoCA’s effectiveness across multiple datasets; however, the lack of a rigorous ablation study to dissect each component’s contribution weakens the evidence of its effectiveness. Without such analysis, it’s unclear if the improvements stem from the method itself or merely the combination of existing techniques. Specifically, the paper needs to demonstrate the individual impact of the dual-branch architecture (message-passing networks vs. shortest path aggregation) and the contrastive learning components (cross-domain vs. multi-view). The ablation study should quantify the performance drop when each component is removed or replaced with simpler alternatives. For example, what is the performance when using only message-passing networks without shortest path aggregation, or when using a standard domain adaptation loss instead of contrastive learning?

2. The theoretical guarantees provided seem somewhat underdeveloped for the complexity of the task. While the paper introduces bounds, the assumptions and conditions for these bounds are not well-explained, which limits their practical relevance and could make it difficult for others to validate or build upon this work. The paper needs to explicitly state the assumptions about the data distributions, the graph structures, and the behavior of the alignment mechanisms. For instance, are there specific requirements on the graph connectivity or node feature distributions for the bounds to hold? The theoretical analysis should also clarify how the chosen distance metric and contrastive loss function affect the derived bounds. Without these details, the theoretical contribution remains abstract and difficult to verify.

3. The paper's presentation could be more accessible; currently, it assumes a high level of familiarity with domain-specific jargon and concepts. A broader contextualization of the problem in simpler terms would make the work more approachable for a wider audience. The introduction should provide a more intuitive explanation of graph domain adaptation and category-level alignment, avoiding overly technical language. The paper should also include a glossary of key terms to help readers unfamiliar with the specific terminology. Furthermore, the methodology sections should start with a high-level overview before diving into the technical details, making it easier for a broader audience to grasp the core ideas.

4. The introduction and contributions are not clearly delineated. The authors should explicitly outline the main research gaps addressed by CoCA and clarify how each component contributes to solving these gaps. The introduction should clearly state what limitations exist in current graph domain adaptation methods, particularly in handling category-level domain shifts. The paper should then explain how CoCA's dual-branch architecture, contrastive learning, and theoretical guarantees specifically address these limitations. The contribution section should also explicitly state the novelty of each component and how it advances the state-of-the-art.

5. The Related Work section could be expanded, particularly to discuss univariate and multivariate graph-based domain adaptation approaches. This would help situate CoCA more clearly within the broader field. The related work should provide a comprehensive overview of existing graph domain adaptation techniques, including methods that focus on node-level, edge-level, and graph-level adaptation. It should also discuss the differences between univariate and multivariate approaches and how CoCA relates to these different categories. This would help readers understand the novelty and significance of the proposed method in the context of existing research.

6. There is a lack of analysis on the algorithmic complexity of CoCA, especially regarding the iterative optimization and contrastive learning modules. This could be a concern for scalability in large datasets and should be addressed. The paper needs to provide a detailed analysis of the computational complexity of each step in the CoCA algorithm, including the message-passing, shortest-path aggregation, contrastive learning, and iterative optimization. This analysis should consider the impact of various parameters, such as the number of nodes, edges, layers, and the dimensionality of the feature vectors. The paper should also discuss the practical implications of the complexity analysis, such as the scalability of the method to large-scale graph datasets.

### Questions
1. Could the authors provide a complexity analysis of the CoCA model, especially concerning the iterative branch coupling and contrastive learning components? If such an analysis is infeasible, please clarify why.
2. How sensitive is the CoCA model to different threshold and path length parameters in real-world applications? Some practical insights here would enhance the paper's contribution to applied graph domain adaptation.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper focuses on graph domain adaptation (GDA). It pays attention to the category-level distribution alignment in graph domain adaptation, which is neglected by previous works. It proposes a framework called Coupling Category Alignment (CoCA). They introduce two branches that interact with each other and formulate a contrastive learning framework. Theoretical insights are provided in the paper. Extensive experiment results prove the effectiveness of the proposed method.

### Strengths
1. This paper is well-written and easy to follow. 
2. As a machine learning paper, I think it is good to provide theoretical insights. 
3. The experiment results seem to be extensive and abundant.

### Weaknesses
1. The idea of this paper, especially category-level alignment, may be neglected by graph domain adaptation (eg. [1]), but it is not new in domain adaptation. I think the novelty of this paper is ok for me, but not very high.

[1] Conditional Adversarial Domain Adaptation

2. The authors can have more discussions on the limitations of the proposed method, eg. the training cost, failure cases, the scenarios it cannot tackle, etc.

### Questions
I am willing to discuss with the authors on the limitations of the proposed method, especially the failure cases. 
I also want the authors to have more explanations about the novelty of the paper, which can help me understand this work better.

### Soundness
3

### Presentation
3

### Contribution
3
