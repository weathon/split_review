# Structure-Aware Parameter-Efficient Machine Unlearning on Transformer Models

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 6, 6, 3

## Abstract
Transformer has become fundamental to a vast series of pretrained large models that have achieved remarkable success across diverse applications. Machine unlearning is an emerging field focused on efficiently removing the influence of specific data from trained models, to comply with privacy regulations enforcing the right to be forgotten. The sheer size of Transformer-based models poses a significant challenge to unlearning efficiency. Existing methods find it promising to restrict unlearning updates to a small portion of influence-critical parameters. However, their parameter-efficient unlearning methods are largely devised in a structure-oblivious manner, which tends to inaccurately identify these parameters and leads to inferior unlearning performance for Transformers. In this paper, we propose {\tt SPE-Unlearn}, a structure-aware parameter-efficient machine unlearning approach tailored for the Transformer architecture. {\tt SPE-Unlearn} introduces a learnable pair of masks to respectively pinpoint influence-critical parameters in the heads and filters of Transformers. The learning objective of these masks is derived by jointly considering both desiderata of unlearning, i.e., sufficiency in influence removal and efficiency, and optimized through an efficient algorithm featured by a greedy search with a warm start. Equipped with the identified key parameters, {\tt SPE-Unlearn} facilitates second-order unlearning, memory-free unlearning, and memory-aided unlearning scenarios. Extensive experiments on various transformer models and datasets demonstrate the effectiveness and efficiency of {\tt SPE-Unlearn}~for Transformer unlearning.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces a sparsity-aware machine unlearning method. First, it proposes to adaptively identify influence-critical parameters using a derived score function. Then, it applies existing machine unlearning methods (e.g., second-order unlearning) exclusively to optimize the identified parameters. The process of parameter identification and optimization is performed iteratively.

### Strengths
1. The approach to identifying influence-critical parameters based on the retain set (and the forget set) appears original. The derivation is clear and reasonable. (However, the necessity needs clarification, as mentioned in the weaknesses below.)
2. The paper is well-organized and easy to understand.
3. It is meaningful to explore the applications of the proposed method for both memory-free and memory-aided successive machine unlearning scenarios.

### Weaknesses
1. In line 273, it appears that the differentiation is performed on $\theta$ rather than $m$.
2. Doubts regarding the necessity of the proposed parameter identification approach. The authors derive a score function to identify informative parameters, involving calculating the derivative with respect to $m$ over $D_f$ and $D_r$. Why not directly optimize the mask parameters base on Eq.(4), which seems computationally cheaper and simpler with only once gradient calculation? Or why we need to transform Eq.(4) to Eq.(5)? The transformation from Eq. (4) to Eq. (5) introduces additional computational cost due to the second-order Taylor expansion and also introduces approximation errors. The necessity of this transformation is not clearly justified, especially given the potential for a simpler, direct optimization of the mask parameters.
3. Doubts about the claimed efficiency benefits. The paper claims improved efficiency for machine unlearning, but this may not be the case:
   - Computation: Compared to vanilla second-order unlearning, the proposed method requires additional calculations involving twice the differentiation to identify informative parameters. Furthermore, while the method uses masks, the unlearning phase (Eq. 10) still requires computing gradients for all parameters, not just the masked ones, thus not reducing the computational cost of the unlearning step itself. The mask learning process also requires two gradient calculations, further increasing the computational cost compared to methods that directly optimize parameters.
   - Memory: Although masking hides certain parameters, storing the mask and associated gradients requires extra memory. The memory overhead of storing the mask and its gradients may negate any potential memory savings from masking parameters.
4. Insufficient complexity analysis. A comprehensive analysis is needed, detailing the complexity of both the parameter identification and unlearning phases from perspectives like memory and computation. Specifically, the analysis should consider the computational cost of the second-order Taylor expansion and the memory overhead of storing the masks and their gradients.
5. What are the specific advantages of the proposed method for the successive machine unlearning? The descriptions (e.g., in Line 362) is  too broad and hard to understand. Detailed, clear and reasonable analysis is needed. The advantages should be clearly articulated in terms of both computational efficiency and unlearning performance in both memory-aided and memory-free successive unlearning scenarios.
6. It is recommended to use the standard notation format as outlined by ICLR guidelines instead of using a uniform font throughout all equations. The correct formatting guidelines can be found on the official website.

### Questions
1. Why do we need a layer-wise optimization (Eq.(9)) in addition to the individual optimization (Eq.(8)) during the mask selection process?
2. How is the first item in Eq.(13) derived? It is hard to follow the method description in Sec.3.3.2.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes an efficient unlearning method with multiple benefits, such as reduced time and memory costs. The proposed method is a pruning-based unlearning approach that filters out sensitive weights to forget specific data. By converting to a differential formulation for the masking variable, the authors approximate unlearned weights through a combination of masking and the Fisher information matrix. Using a second-order Taylor expansion and the convergence assumption from LeCun et al., the method is simplified to this combination. In experiments, the authors compare their approach to prior methods and report promising performance.

### Strengths
I believe the strongest benefit of this work is its time and memory efficiency. Across all tables, the authors report significantly reduced costs for unlearning, which highlights a promising advancement in the field of machine unlearning.

### Weaknesses
However, I have several concerns:

1. It is unclear why the method is considered structure-aware. While mask variables are applied to each head in the multi-head attention block, this approach is not unique to Transformers. The authors mention as "widely-adopted unlearning methods in Transformers, e.g., fine-tuning (Golatkar et al. (2020)) and gradient difference (Liu et al. (2022); Jia et al. (2024))," but they are not specified to transformer architecture. As I understand from the manuscript, the authors suggest that their method’s efficiency makes it well-suited to large-scale Transformer models, but large scale is not a Transformer-specific attribute.


2.  Although the method is not specialized for Transformer architectures, much of the paper focuses on Transformer-specific content. Reducing this content could make the paper more concise and focused.


3. In line 190, the authors assume that " L is differentiable with respect to m", to develop Equations (5-9). However, as stated in line 160, $m$ is a binary variable. This raises concerns about whether the differentiability assumption is valid.


4. In line 181, the authors state, "we formulate the unlearning objective (1) with a learnable pair of masks for the heads and filters as a constrained optimization problem." However, objective (1) aims to retain a model with the same architecture trained only on D_r. The proposed method, which involves pruning, alters the architecture, making it misaligned with this objective.


5. The experimental section lacks details on the partitioning of D_r and D_f. This split is an essential part of the experimental setup and should be clearly specified.

6. Evaluation Concerns in Table 2 and Appendix:

6-1) The unlearning performance should be evaluated by comparing it to the performance of a retrained model, as specified by Eq (1). In specific, the MIA metric should follow this protocol, with retrained models serving as the gold standard. However, the authors set the lower values of efficacy and higher values of fidelity are better without any explanation.


6-2) In Table 1, the proposed method unlearns to a greater extent (achieving 85.94% as the lowest Unlearning Accuracy) than other methods, resulting in lower Remaining Accuracy. To ensure a fair comparison, it would be better to report Remaining Accuracy and Testing Accuracy at the point where each method reaches a common Unlearning Accuracy threshold.


6-3) All methods (FT, GD, SA) have hyperparameters that control unlearning speed, such as learning rate, but there is no discussion of these parameters in the manuscript. Without this information, it’s unclear whether the evaluations are fair.


6-4)  The authors used only D_r for Fine-Tuning (FT) and Sparsity-Aware Unlearning (SA) but used both D_r and D_f for their method. This discrepancy in dataset usage should be clarified, and comparisons with more unlearning methods that use both D_r and D_f are recommended.


6-5) Many of the unlearning methods used for comparison are outdated. It would strengthen the evaluation to include more recent works, such as:

[1] Fan, C., Liu, J., Zhang, Y., Wong, E., Wei, D., & Liu, S. (2023). Salun: Empowering machine unlearning via gradient-based weight saliency in both image classification and generation. arXiv preprint arXiv:2310.12508.

[2] Chen, M., Gao, W., Liu, G., Peng, K., & Wang, C. (2023). Boundary unlearning: Rapid forgetting of deep networks via shifting the decision boundary. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (pp. 7766-7775).


7. (Minor) In the second sentence of the Related Work section, "Jang et al." is cited twice in a single sentence.

### Questions
See above

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
3

### Summary
This paper proposes a structure-aware parameter efficient machine unlearning approach for transformer models.

### Strengths
The research problem is interesting and the approach is novel.

### Weaknesses
Some experiments are insufficient, and the experimental setup should be more comprehensive.

For example, in page 7 the author notes that if the number of unlearning requests exceeds a certain threshold, the model must be retrained from scratch to regain its performance. What exactly is this threshold? It is unclear how this threshold is determined and whether it is consistent across different models and datasets. A more rigorous analysis of this threshold is needed, including how it scales with model size and data volume. Additionally, the practical implications of needing to retrain from scratch after exceeding this threshold should be discussed in more detail.

Additionally, in Table 3, is there a specific reason for selecting 90% sparsity instead of alternatives like 85% or 95%? Based on Figures 2 and 3, is this value specific to the model? The choice of 90% sparsity seems arbitrary without a clear justification. The authors should provide a more detailed analysis of how sparsity affects unlearning performance and model utility, including a sensitivity analysis around the 90% value. It is also unclear whether this value is optimal for all models and datasets or if it needs to be tuned for each specific scenario.

### Questions
1. I am interested in the comparison results with other unlearning approaches presented in Table 1. Could you either provide the results of applying the memory-aided unlearning approach to the experiments in Table 1, or explain why this comparison was not included?
2. In the experiments on successive unlearning scenarios on page 9,  the experiments shows the number of requests affect the results. How does the Volume of data affect the performance?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors tackle the challenge of efficient machine unlearning in large Transformer models, essential for meeting privacy regulations. Existing methods, often structure-agnostic, struggle to accurately target influence-critical parameters in Transformers. To address this, the authors introduce SPE-Unlearn, a structure-aware approach that uses learnable masks to identify key parameters within Transformer heads and filters. Optimized via a greedy search, SPE-Unlearn enhances unlearning by balancing efficiency and effectiveness. Extensive experiments show that SPE-Unlearn significantly improves unlearning performance across various Transformer models and datasets.

### Strengths
1. The paper is clearly written, well-formatted, and well-organized. 

2. The mathematical derivations are rigorous.

### Weaknesses
1. The paper mentions that SPE-Unlearn can enhance the effectiveness of various methods; however, the authors only integrate SPE-Unlearn with SO and do not test it with other methods. In Table 2, SPE-SO does not show a significant improvement over SO, while requiring more time.

2. Common LLM unlearning tasks, such as TOFU, MUSE, and WMDP, are missing.

3. Several standard baselines, like NPO and "I don't know," are not included, which weakens the argument.

4. For robustness, the authors employ memory-free and memory-aided unlearning but do not explore other approaches, such as jailbreak prompts.

### Questions
1. Could the authors explore additional LLM unlearning benchmarks, such as TOFU, MUSE, and WMDP?

2. Could the authors evaluate more unlearning methods, like NPO and "I don't know"?

3. For robustness evaluation, would it be possible to include tests like relearning attacks or jailbreak prompts?

4. Additionally, could the authors consider using gradient norm alone to identify saliency? This might offer a more streamlined approach.

### Soundness
2

### Presentation
2

### Contribution
2
