# The Low-Rank Bottleneck in Attention

- Decision: Accept
- Scores: 3, 5, 8, 6

## Abstract
Attention-based mechanisms are widely used in machine learning, most prominently in transformers. However, hyperparameters such as the rank of the attention matrices and the number of attention heads are scaled nearly the same way in all realizations of this architecture, without theoretical justification. In this paper, we prove that the rank can have a dramatic effect on the representational capacity of attention. This effect persists even when the number of heads and the parameter count are very large. Specifically, we present a simple and natural target function based on nearest neighbor search that can be represented using a single full-rank attention head for any context length, but that cannot be approximated by low-rank attention unless the number of heads is exponential in the embedding dimension, even for short context lengths. Moreover, we show that, for short context lengths, adding depth allows the target to be approximated by low-rank attention. For long contexts, we conjecture that full-rank attention is necessary. Finally, we present experiments with standard multilayer transformers that validate our theoretical findings.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper presents a theoretical analysis of the role of rank within attention mechanisms. It challenges the prevailing practice of employing low-rank attention and discusses the implications related to the selection of the number of heads. The author establishes that low-rank attention exhibits inferior performance compared to full-rank attention, indicating that the adoption of a higher rank has the potential to enhance attention performance. Preliminary experiments are conducted utilizing toy examples with synthetic data.

### Strengths
The theoretical analysis seems correct.

### Weaknesses
1. The rank of attention is a significant hyperparameter in the design of transformers. A common convention involves the utilization of low-rank attention, typically establishing the number of heads as ( H = d/r ). This paper, however, contests this design choice, proposing that a higher rank can enhance performance. It is crucial to note that the paper does not address the speed-accuracy trade-off associated with this adjustment. It is widely recognized that high-rank attention may yield superior performance at the expense of increased computational costs. When evaluating overall performance, particularly in terms of accuracy within a predetermined computational budget, prevailing practices may ultimately provide more favorable outcomes.

2. The experiments presented in this study lack robustness, as they are primarily limited to toy experiments. I would appreciate observing performance metrics derived from real-world data applied to standard transformer sizes. It is well established that theoretical performance often diverges from practical outcomes in deep learning; thus, empirical experimentation is essential.

3. This work indicates that shallow transformers may experience limitations due to low-rank attention. However, it is imperative to ascertain how these limitations manifest in deep transformers, as shallow transformers are not commonly employed in practice. If this limitation has been substantially mitigated in deep transformers, it may render further examination of this issue unnecessary.

### Questions
N/A

### Soundness
2

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
This article examines the limitations and potential of low-rank attention mechanisms in transformer models, demonstrating that while low-rank attention heads require significantly more heads to match the performance of full-rank models in approximating functions like nearest neighbors, and these limitations can be mitigated by increasing the depth of the model. Through theoretical analysis and empirical validation, the study highlights that full-rank models inherently possess superior representational capabilities, especially with fewer heads, and suggests that adding more layers could partly overcome the deficiencies of low-rank models, though at the cost of increased computational complexity.

### Strengths
1. A deeper exploration of the low-rank problem in Transformer models.
2. The paper is well written and easy to follow.
3. Authors provide ample mathematical proofs to support their conclusions.

### Weaknesses
1. The authors mentioned after Theorem 2 that the theoretical framework should be extendable to cases where N>2. Could you provide more specific explanations for the reasoning behind this inference? This would help further understand the applicability of your theory to specific problems.

2. Although the authors have demonstrated theoretically and experimentally that low-rank attention models are insufficient for fitting certain functions in various scenarios and are significantly weaker than full-rank attention models, further clarification is needed on how these issues impact current mainstream Transformer models (such as the new models shown in Table in Appendix B.1), how the proposed methods in the paper apply to these models, and how performance improvements are achieved. I believe that related experimental results and methodological extensions would greatly help illustrate the contribution of the paper.

### Questions
1. Could simple experiments or additional references to other studies and conclusions be designed to intuitively show the impact of the low-rank problem on the performance of mainstream Transformer models?
2. Could you further elaborate on how the proposed “majority voting” method for improving low-rank models enhances mainstream Transformer models and validate this with relevant experiments? For the experiments, model selection could refer to those in Appendix B.1 and the models used in [1][2], while the datasets could refer to those in [1][2] or other widely recognized benchmark datasets.
[1] Bhojanapalli S, Yun C, Rawat A S, et al. Low-rank bottleneck in multi-head attention models[C]//International conference on machine learning. PMLR, 2020: 864-873.
[2] Shazeer N, Lan Z, Cheng Y, et al. Talking-heads attention[J]. arXiv preprint arXiv:2003.02436, 2020.
3. Also, please refer to weaknesses for other concerns.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper "THE LOW-RANK BOTTLENECK IN ATTENTION" investigates the impact of the rank of attention matrices on the representational capacity of attention-based mechanisms, particularly in transformers. It challenges the common practice of using low-rank attention and proposes that the rank can significantly influence the model's ability to approximate certain functions. Specifically, the authors present a simple and natural target function based on nearest neighbor search that can be represented using a single full-rank attention head for any context length. The paper presents theoretical analysis and empirical experiments to support its claims, suggesting that increasing the rank or the number of attention heads may lead to more expressive and parameter-efficient models.

### Strengths
1. Novel perspective on attention mechanisms: The paper offers a fresh perspective on the role of rank in attention mechanisms by using a simple and natural target function based on nearest neighbor search that can be represented using a single full-rank attention head for any context length, which is an interesting aspect of transformer architectures.

2. Theoretical and Empirical Rigor: It combines theoretical proofs with empirical experiments, providing a robust exploration of the implications of low-rank attention on model capacity and efficiency.

### Weaknesses
1. The results may rely heavily on the assumption of rotational invariance in the data distribution, which may not hold in all real-world applications. Specifically, the paper's theoretical analysis and experiments might not generalize well to datasets where features are not uniformly distributed across all dimensions. This is a significant limitation, as many real-world datasets exhibit strong correlations and dependencies between features, violating the assumption of rotational invariance. The authors should acknowledge that the conclusions drawn from this assumption might not be universally applicable.

2. To make it easier for readers to understand, I kindly suggest that the authors explain in more detail the differences between this paper and previous work [1]. The current explanation lacks a detailed comparison of the methodologies, assumptions, and results. A more thorough discussion should highlight the specific contributions of this work in contrast to [1], particularly in terms of the theoretical analysis and the experimental setup. It's crucial to clarify how this paper advances the understanding of low-rank attention beyond what was already established in [1].

3. Can the proposed method demonstrate its effectiveness on more attention-based models? The paper focuses primarily on transformers with softmax attention. It would be beneficial to see if the findings extend to other attention mechanisms, such as those used in state-space models or other variants of attention. This would strengthen the paper's claims about the general impact of low-rank bottlenecks in attention mechanisms.

### Questions
Please refer to the Weaknesses

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
3

### Summary
This paper questions the conventional number that community use for the rank of attention matrices and the number of attention heads. Authors provide in-depth theoretical explanations and experiments to support their arguments. In the high-accuracy regime, the required number of heads is growing exponentially to remain the performance.

### Strengths
Transformer have dominated many areas but there have been few studies on the choices of numbers of attention heads and dimensions used in attention mechanism. This paper raises doubts about this which is valuable for community to pay attention.

1. The paper is well written and easy to follow. In-depth theoretical explanations are provided.

2. For a simple and natural target function -- nearest neighbor function, authors show low-rank attention is fundamentally weaker than full-rank attention even when choosing very large head numbers.

3. Also, this paper explores the solutions to mitigate the weakness of low-rank attention

### Weaknesses
 1. The paper studies only is  limited to shallow transformers which are not practical to large model.

### Questions
1. I am wondering the reason why authors choose to analysis nearest neighbor functions and are there any other choices of functions.

### Soundness
4

### Presentation
4

### Contribution
3
