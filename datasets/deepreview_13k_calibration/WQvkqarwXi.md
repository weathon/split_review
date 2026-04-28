# Towards Synergistic Path-based Explanations for Knowledge Graph Completion: Exploration and Evaluation

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6

## Abstract
Knowledge graph completion (KGC) aims to alleviate the inherent incompleteness of knowledge graphs (KGs), a crucial task for numerous applications such as recommendation systems and drug repurposing. The success of knowledge graph embedding (KGE) models provokes the question about the explainability: ``\textit{Which the patterns of the input KG are most determinant to the prediction}?'' Particularly, path-based explainers prevail in existing methods because of their strong capability for human understanding. In this paper, based on the observation that a fact is usually determined by the synergy of multiple reasoning chains, we propose a novel explainable framework, dubbed KGExplainer, to explore synergistic pathways. KGExplainer is a model-agnostic approach that employs a perturbation-based greedy search algorithm to identify the most crucial synergistic paths as explanations within the local structure of target predictions. To evaluate the quality of these explanations, KGExplainer distills an evaluator from the target KGE model, allowing for the examination of their fidelity. We experimentally demonstrate that the distilled evaluator has comparable predictive performance to the target KGE. Experimental results on benchmark datasets demonstrate the effectiveness of KGExplainer, achieving a human evaluation accuracy of 83.3\% and showing promising improvements in explainability. Code is available at \url{https://anonymous.4open.science/r/KGExplainer-33A0}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents KGExplainer, a model-agnostic framework designed to provide path-based explanations for knowledge graph completion. The approach leverages a perturbation-based greedy search algorithm to identify the most important synergistic paths that contribute to the prediction of facts within a knowledge graph. The method is grounded in the insight that predictions are often supported by multiple interconnected reasoning chains. To evaluate these explanations, KGExplainer uses a distilled evaluator derived from the target knowledge graph embedding model, ensuring the explanations maintain high fidelity.

### Strengths
- Model-Agnostic Approach. KGExplainer is designed to work with different KGE models, making it a versatile tool for enhancing explainability across various KGC tasks.
- Theoretical Justification. The paper provides a solid theoretical foundation for the proposed framework, in terms of the scalability of KGExplainer.

### Weaknesses
 - Limited Scalability Experiments and Discussion. While the paper mentions that KGExplainer can handle large KGs with small average degrees, there is limited discussion on how the framework scales with increasing graph size and complexity. Specifically, the paper lacks a detailed analysis of how the computational cost of the greedy search algorithm and the retraining of the distilled evaluator scale with the number of nodes and edges in the knowledge graph. The provided analysis focuses on average degree, but does not delve into the impact of varying degree distributions, which can significantly affect the performance of path-based methods. Furthermore, the paper does not explore the memory footprint of KGExplainer, which is a critical factor when dealing with large knowledge graphs.

### Questions
Please see weaknesses.

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
This paper presents KGExplainer, a framework for generating explanations for knowledge graph completion (KGC) predictions by identifying synergistic paths. The work introduces a method to identify multiple synergistic paths for explaining KGC model predictions, moving beyond single-path approaches used in prior work. The authors develop a distillation-based evaluator for assessing explanation quality, providing a quantitative way to measure the effectiveness of the generated explanations. The technical core of the approach is a greedy search algorithm for finding explanatory paths within local subgraph structures. While the framework shows promise in generating more comprehensive explanations than existing methods, there are several aspects that warrant further investigation and improvement.

### Strengths
1. The paper demonstrates the importance of explanations in knowledge graph completion through concrete examples, such as competitor analysis (Alibaba-JD.com case) and drug interaction prediction (Acetaminophen-Warfarin case) shown in Figure 1. These examples clearly illustrate why single-path explanations are insufficient for complex predictions.
2. The paper introduces a novel distillation-based evaluator that achieves comparable performance to the original KGE models, as evidenced by the results in Table 1. For instance, KGExp-RotatE achieves 17.33% Hits@1 on OGB-biokg compared to RotatE's 17.12%, showing the evaluator's reliability.
3. The proposed method shows consistent improvements across multiple datasets, and the method is theoretically proven scalable (in Section 4.4, computation complexity is shown depend mainly on local parameters such as path length and number of paths rather than total graph size.)

### Weaknesses
1. While the paper introduces the concept of "synergistic paths" as a key contribution, it lacks rigorous theoretical analysis of what constitutes meaningful synergy between paths. The paper never formally defines what makes paths truly synergistic versus simply having multiple independent supporting paths. Besides, the greedy search strategy for finding synergistic paths lacks theoretical guarantees about its optimality. I recommend that the authors should formalize the concept of path synergy, perhaps through information theoretic measures that capture the mutual information between paths, or through formal analysis of how different path combinations contribute to prediction confidence. This would strengthen the theoretical foundation of the work beyond just empirical results.
2. The experimental evaluation doesn't sufficiently demonstrate real-world usefulness of the explanations. The human evaluation, while showing 83.3% accuracy, involved only academic participants (students/professors) rather than domain experts or real end users who would actually use such systems. The experiments lack evaluation of how these explanations help in practical tasks like error analysis or model debugging. There are no case studies demonstrating how synergistic paths provide better insights than single paths in real applications. To properly validate the method's practical value, the authors may conduct user studies with domain experts (like biomedical researchers for OGB-biokg), include case studies showing how the explanations help debug model errors, analyze explanation patterns for both correct and incorrect predictions, and demonstrate benefits through concrete application scenarios.

### Questions
1. You state that 'a fact is usually determined by the synergy of multiple reasoning chains', could you provide empirical evidence or analysis showing what percentage of predictions actually require multiple paths versus being explainable by a single path?
2. In Section 4.4 you provide theoretical complexity analysis showing the method scales with path length L and number N rather than graph size. However, the empirical results in Table 4 show significant runtime differences between datasets. Could you explain this apparent discrepancy and provide more details about what factors dominate the practical runtime?
3. Regarding the human evaluation showing 83.3% accuracy, could you provide more details about a) The criteria given to participants for judging explanation quality; b) Whether participants were shown the explanations simultaneously or sequentially; and c) If the 20 test cases were randomly selected or curated?

### Soundness
2

### Presentation
3

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
The paper introduces KGExplainer, a novel model-agnostic framework for generating explainable knowledge graph completion (KGC) by identifying synergistic path-based explanations. This approach leverages a perturbation-based greedy search to identify influential paths and an evaluator distilled from the target knowledge graph embedding (KGE) model to assess the fidelity of explanations. KGExplainer is evaluated against state-of-the-art explainability baselines, demonstrating significant improvements in both faithfulness and explainability metrics. Experimental results on multiple benchmark datasets reveal KGExplainer's strong human-interpretability and competitive performance in preserving predictive accuracy.

### Strengths
1. KGExplainer introduces a model-agnostic approach to generate explainable paths for KGE-based models, which can be applied to various KGC models and datasets.
2. The paper proposes a distilled evaluator to quantitatively assess explanation fidelity, ensuring that the explanations are not only accurate but also reflective of the underlying KGE model's decision-making process.
3. The framework is evaluated on various KGC models and datasets, showing competitive results across different setups and substantial improvements in both F1@1 and Recall@1 metrics, particularly outperforming other path-based methods.

### Weaknesses
1. Limited scopes: The proposed method only focuses on the KGE-based methods, while many advanced KGC methods are based on graph neural networks (GNNs) [1] or other deep learning architectures. It would be beneficial to extend the evaluation to these models to provide a more comprehensive comparison. Besides, it only focuses on path-based explanations, while other high-order structures like subgraph patterns or graph motifs could also be considered.

2. Efficiency concerns: The proposed method requires retraining the KGE model to identify the key paths, which could be computationally expensive. Even though the greedy search is efficient, the overall complexity of the method might hinder its scalability to large-scale knowledge graphs.

3. Evaluation metrics: The paper proposes a novel evaluator to assess the fidelity of explanations. However, the quality of the evaluator is not dissected in detail, making it questionable whether the evaluator can accurately capture the KGE model's decision-making process. A more in-depth analysis of the evaluator's performance and its robustness to different KGE models would strengthen the paper's claims.

4. Some experiment settings are not clearly described.

### Questions
1. How to assess the quality of the proposed evaluator? Can you provide some experiments to demonstrate its effectiveness in evaluating the fidelity of explanations? 

Moreover, how does the architectures of the evaluator, like other subgraph-based method: Grail [1], affect the performance and robustness of evaluation? Will the evaluation results be consistent across different evaluators?

Last, what is the input to the evaluator? Is it purely the graph structures or the embeddings are initialized with the pre-trained KGE models?

2. How the re-training stage of the KGE model affects the overall efficiency of the proposed method? It should be discussed in the complexity analysis section and also included in the cost time analysis of Table 4.

3. In experiments, how is the predictive performance of the "distilled model" evaluated? Is it predicted by the embeddings from re-trained KGE model or inputting subgraphs into the evaluator?

4. How does the hop of enclosed subgraphs affect the performance of the proposed method? The author only set the hop to 2. However, in FB15k-237, the average length of the shortest path connecting head and tail is around 3, which means the hop of 2 might not be enough to capture the long-range dependencies.

[1] Teru, K., Denis, E., & Hamilton, W. (2020, November). Inductive relation prediction by subgraph reasoning. In International Conference on Machine Learning (pp. 9448-9457). PMLR.

### Soundness
3

### Presentation
3

### Contribution
3
