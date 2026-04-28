# Neuro-symbolic Entity Alignment via Variational Inference

- Decision: Reject
- Avg Score: 5.75
- Scores: 5, 6, 6, 6

## Abstract
Entity alignment (EA) aims to merge two knowledge graphs (KGs) by identifying equivalent entity pairs. Existing methods can be categorized into symbolic and neural models. Symbolic models, while precise, struggle with substructure heterogeneity and sparsity, whereas neural models, although effective, generally lack interpretability and cannot handle uncertainty. We propose NeuSymEA, a probabilistic neuro-symbolic framework that combines the strengths of both methods. NeuSymEA models the joint probability of all possible pairs' truth scores in a Markov random field, regulated by a set of rules, and optimizes it with the variational EM algorithm. In the E-step, a neural model parameterizes the truth score distributions and infers missing alignments. In the M-step, the rule weights are updated based on the observed and inferred alignments. To facilitate interpretability, we further design a path-ranking-based explainer upon this framework that generates supporting rules for the inferred alignments. Experiments on benchmarks demonstrate that NeuSymEA not only significantly outperforms baselines in terms of effectiveness and robustness, but also provides interpretable results.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces NeuSymEA, a neuro-symbolic framework for entity alignment (EA) across knowledge graphs (KGs). NeuSymEA addresses limitations in both symbolic and neural models by integrating them through a variational EM framework. This integration allows for better handling of substructure heterogeneity, sparsity, and uncertainty. The symbolic component uses Markov random fields and weighted rules for structured reasoning, while the neural component uses embedding-based models for high recall. The framework is optimized iteratively, updating rule weights and neural parameters. Furthermore, an explainer is introduced to provide interpretable justifications for entity alignments, making the model results transparent and understandable. The proposed method outperforms various baselines on benchmark datasets and demonstrates robustness, especially in low-resource scenarios.

### Strengths
1. The model achieves state-of-the-art results on entity alignment benchmark datasets, significantly improving alignment effectiveness. This validates the efficiency of the neuro-symbolic fusion approach and highlights its potential for broader applications in knowledge graph integration.
2. The inclusion of an explainer component provides rule-based interpretations for entity alignments, which is a major advantage for applications that require transparency and accountability, such as medical knowledge systems or legal databases.
3. The logical decomposition strategy reduces the computational complexity of rule-based inference, enabling the method to scale to larger knowledge graphs. This efficiency also facilitates handling long-tail entities effectively, making the approach practical for real-world, large-scale scenarios.

### Weaknesses
1. The descriptions of the variational EM algorithm and inference steps are dense and complex. For readers unfamiliar with probabilistic modeling, these sections may be difficult to understand. Simplifying the explanations or including more illustrative diagrams could enhance readability and comprehension.

2. While the paper claims efficiency improvements, it lacks a thorough complexity analysis. Specifically, the impact of rule length and dataset size on runtime and memory usage should be explicitly quantified to strengthen the argument for scalability and efficiency.

3. The paper does not provide an in-depth exploration of scenarios where NeuSymEA might underperform. For example, the framework could face challenges in extremely sparse or highly heterogeneous knowledge graphs, which warrants further discussion and empirical analysis.

4. The framework’s performance is quite sensitive to hyperparameters, such as the rule threshold (δ) and the number of EM iterations. A more comprehensive analysis of how these hyperparameters influence performance would be valuable for demonstrating the robustness of the method.

5. Although interpretability is a key feature of the framework, the utility of the rule-based explanations could be further validated. Conducting user studies or qualitative assessments would help to confirm whether the generated explanations are practically useful in real-world applications.

### Questions
See the Weaknesses.

### Soundness
2

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
2

### Summary
This paper proposes a neuro-symbolic framework, NeuSymEA, for entity alignment in knowledge graphs. NeuSymEA combines the interpretability of symbolic models with the high recall rate of neural models, optimizing entity alignment through a variational EM framework. Additionally, it includes an interpreter that generates rule-based explanation paths and confidence scores for alignment results. The main contributions are: the seamless integration of symbolic and neural models, enhancing efficiency and interpretability; an efficient logical reasoning mechanism that reduces computational complexity by decomposing long rules into shorter ones; improved interpretability through a path-ranking-based interpreter, increasing transparency and user comprehension; and finally, NeuSymEA's outstanding experimental performance, significantly surpassing baseline models on multilingual datasets and demonstrating robust performance in low-resource environments.

### Strengths
The NeuSymEA framework combines the interpretability of symbolic models with the high recall rate of neural models, optimizing entity alignment through a variational EM framework. This integration enables the model to effectively handle complex entity alignment tasks while balancing the strengths and weaknesses of both models within a unified framework.

### Weaknesses
The symbolic and neural models in the paper are integrated through the EM framework, but the trade-offs between the two in the optimization process are not explored in depth, especially in high-dimensional datasets. As a result, symbolic reasoning may still face efficiency issues, while the neural model tends to rely heavily on sparse data. Therefore, the handling strategies in these situations require further discussion.

### Questions
Currently, the model outperforms other methods in low-resource settings. However, will NeuSymEA's performance improve further with an increase in data volume? Is this improvement significantly different from existing baseline models?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents a neuro-symbolic framework, NeuSymEA, that combines the strengths of symbolic and neural models for entity alignment in knowledge graphs. It employs a variational EM algorithm to optimize the joint probability of entity alignments, integrating embedding-based similarity and rule-based symbolic reasoning. The framework includes a path-ranking-based explainer that generates supporting rules for inferred alignments, enhancing interpretability. Experiments on DBP15K demonstrate that NeuSymEA significantly outperforms existing methods in terms of effectiveness, robustness, and interpretability.

### Strengths
- **Combined strengths**. The work integrates symbolic and neural models, leveraging the precision of symbolic reasoning and the high recall of neural embeddings to improve entity alignment.

- **Good performance**. The proposed framework shows superior performance and robustness across benchmark datasets, outperforming existing methods.

- **Interpretable results**. The proposed framework can provide interpretable results through a path-ranking-based explainer, enhancing the interpretability of entity alignment.

### Weaknesses
 - **Unclear definition of rules**. According to Eq. (1), the rules used in the work are not horn rules. Instead, they are path pairs from anchor pairs. So, it would be better to provide a clear definition of the used rules, specifying how these path pairs are constructed and what constraints are imposed on their structure. The current description lacks the necessary detail to fully understand the nature of these rules and how they contribute to the entity alignment process.

- **Increased complexity**. The integration of symbolic and neural models with a variational EM algorithm may be complex. The paper does not provide a thorough analysis of the computational complexity, particularly regarding the scalability of the approach. The framework may still face challenges with extremely large knowledge graphs due to the exponential growth of the search space for rules, and the paper does not discuss strategies to mitigate this issue. A detailed analysis of the time and space complexity of each step in the algorithm, including the rule mining and reasoning processes, is needed to assess the practical applicability of the method.

- (Minor) Missing related work: "Xiaobin Tian, Zequn Sun, Wei Hu: Generating Explanations to Understand and Repair Embedding-Based Entity Alignment. ICDE 2024: 2205-2217"

### Questions
-  How are the rules mined? Is it done using the algorithm described in Appendix A.2? What is the complexity of generating supporting rules?

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
This paper proposes a neuro-symbolic method for entity alignment and optimizes it with the EM algorithm. The authors also design a path-ranking explainer to provide supporting rules for the predicted alignments. Experiments on the DBP15K dataset demonstrate state-of-the-art performance of the proposed method.

### Strengths
Leveraging the EM algorithm to alternatively learn the embedding and the path scorer is novel and interesting.

The overall writing is good.

The results of NeuSymEA compared with the baselines are promising.

### Weaknesses
At the beginning of the methodology section, the authors may introduce more insights into why leveraging the EM algorithm and its connection to the given problem.

The dataset is quite outdated. The authors highlight the strengths of the proposed method on long-tail entities, but DBP15K is constructed with popular entities. The authors may consider conducting experiments on OpenEA or newer datasets.

PARIS performed badly in the paper, while it has very strong performance on the OpenEA dataset. Can the authors explain this phenomenon?

Recently, there have been some methods (e.g., [1]) possessing symbolic reasoning properties and they do not require two-step optimization and the additional explainer, which seems more effective. Can the authors compare them with the proposed NeuSymEA?

### Questions
Please see Weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2
