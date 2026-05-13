# Balancing Model Efficiency and Performance: Adaptive Pruner for Long-tailed Data

- Decision: Reject
- Scores: 6, 6, 3, 6

## Abstract
Long-tailed distribution datasets are prevalent in many machine learning tasks, yet existing neural network models still face significant challenges when handling such data. This paper proposes a novel adaptive pruning strategy, LTAP (Long-Tailed Adaptive Pruner), aimed at balancing model efficiency and performance to better address the challenges posed by long-tailed data distributions. LTAP introduces multi-dimensional importance scoring criteria and designs a dynamic weight adjustment mechanism to adaptively determine the pruning priority of parameters for different classes. By focusing on protecting parameters critical for tail classes, LTAP significantly enhances computational efficiency while maintaining model performance. This method combines the strengths of long-tailed learning and neural network pruning, overcoming the limitations of existing approaches in handling imbalanced data. Extensive experiments demonstrate that LTAP outperforms existing methods on various long-tailed datasets, achieving a good balance between model compression rate, computational efficiency, and classification accuracy. This research provides new insights into solving model optimization problems in long-tailed learning and is significant for improving the performance of neural networks on imbalanced datasets. The code is available at \url{https://anonymous.4open.science/r/AEFCDAISJ/README.md}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper introduces a novel pruning approach called the Long-Tailed Adaptive Pruner (LTAP). LTAP is designed to address the challenge of imbalanced datasets where traditional pruning methods often fall short. The LTAP strategy introduces a multi-dimensional importance scoring system and a dynamic weight adjustment mechanism to adaptively determine which parameters to prune, particularly focusing on protecting the critical parameters for tail classes. Extensive experiments on various long-tailed datasets validate LTAP's effectiveness.

### Strengths
- Addressing pruning in the context of long-tailed datasets is both meaningful and highly relevant to real-world applications.
- The method is supported by theoretical foundations that verify its effectiveness.
- The performance improvements achieved by the method are relatively substantial.

### Weaknesses
- The paper is hard to follow, and the writing could be improved. For example, the definition of $w_k$ lacks clarity and could be more explicitly explained.

- The update process of $\alpha_k$ is somewhat confusing. Since it is connected to class $c$, it raises the question: if $\alpha_k$ is defined for each class $c$, then does each class have a unique $\alpha_k$? However, the earlier sections suggest it is shared across all classes. Additional clarification on this would be helpful.

- The way the dynamic weight adjustment mechanism strengthens the protection of parameters for tail classes is not entirely clear. If $\alpha_k$ is indeed shared across all classes, it is unclear why adjusting the weights of different scoring criteria would selectively protect parameters for tail classes. Could there be a scoring criterion that more specifically targets the protection of parameters for tail classes? 

- From the experimental results on the ImageNet-LT dataset, compared to ATO and RReg, it appears that LTAP achieves a larger performance improvement for head classes than for tail classes. This seems to contradict the stated goal of strengthening parameter protection for tail classes in LTAP. 

- There are also some typos, such as in line 700, where "equation eqution" should be "equation."

### Questions
Please refer to the weakness section.

### Soundness
2

### Presentation
2

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
This paper proposes a new model pruning strategy for long-tailed data named Long-Tailed Adaptive Pruner (LTAP). The proposed pruning strategy first calculates the comprehensive importance score for each parameter group to select the group(s) of parameter to be pruned, then updates the weight coefficients for each scoring criteria through Long-Tailed Voting (LT-Vote) mechanism. LT-Vote adjusts the weight coefficients based on the actual performance of each class, thus better protects the tail class parameters.

### Strengths
The extensive experimental results demonstrate that the proposed LTAP strategy effectively identifies low-importance parameters, achieving a better balance between maintaining model performance—particularly on tail classes—and reducing model size. Additionally, the authors provide a theoretical analysis arguing that tail classes should be prioritized in parameter retention to preserve model accuracy, lending strong support to the LTAP approach.

### Weaknesses
1. **Theoretical analysis of LT-Vote**. The authors should further discuss how LT-Vote enhances parameter retention for tail classes, connecting this mechanism more explicitly to the theoretical foundation of tail-biased pruning. Deriving a specific performance guarantee for the LT-Vote mechanism would strengthen the argument.

2. **Ability of retaining tail class effective parameters**. In Section 4.3, the authors analyzes how neurons are masked under different pruning strategies. However, they do not assess whether the proposed strategy actually preserves more parameters for tail classes, leaving the theoretical analysis unvalidated.

3. **Minor issues**. 

    (1) Including a pseudo-code block would clarify the strategy and provide coherence among the presented formulas.

    (2) Some subscripts are not properly rendered. For example, Lemma 1 in Appendix A.1 writes $\mathcal{H}_s$ as $\mathcal{H}c$, $d_{VC,c}$ as $dVC,c$.

    (3) Missing references. Line 686 "Definition ??" and line 693 "e.g., see ?".

### Questions
What is the training/pruning time cost of your model pruning method?

### Soundness
3

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
The paper explores how adaptive pruning strategies during training can balance model performance and efficiency on long-tailed data. It introduces a multi-dimensional importance scoring criterion and a weight allocation strategy to address this challenge. Experimental results demonstrate the effectiveness of the proposed method.

### Strengths
1. Researching how machine learning algorithms tackle the challenges of long-tailed data is both practical and worthwhile.
2. The experimental results demonstrate promising effectiveness.
3. The code is provided, which is a commendable practice.

### Weaknesses
1. The paper is poorly written. For instance, the logic in the first three paragraphs of the Introduction section is disorganized, failing even to clearly articulate the research problem. It begins by discussing the challenges of long-tailed data, then moves to efficiency issues in multi-expert systems and modular designs within long-tailed learning, neglecting mainstream approaches like re-sampling, loss design, and transfer learning. It then shifts abruptly to the challenges of pruning methods in long-tailed learning, without clarifying the specific problem the paper aims to address.
2. $\theta$ in Equation 1 and $p$ in Equation 6 are not defined.
3. There is an inconsistency between Figure 1 and Equations 3 and 4: Figure 1 illustrates 5 criteria, while the latter only includes 4.
4. It is unclear how to set $w_c$ in Equation 1.
5. How to set $w_k$ in Equation 5 is also not explained.
6. The left side of Equation 5 represents a class-agnostic quantity, while the right side includes class c, which is confusing. Additionally, I do not observe any dynamic adjustment effect in Equation 5; \text{acc}_C seems to only function as the temperature coefficient in the softmax function.
7. The setup of $A_{c,\text{target}}$ in Equation 5 is also not specified.
8. In line 149, the selection and role of the reference model are not explained.
9. The method employs validation set accuracy and a reference model during training, which is uncommon. The authors should explicitly highlight and discuss these points.
10. In addition to the results on the long-tail baselines, results on the vanilla baseline, i.e., using standard cross-entropy (CE), should also be presented.
11. How does the method integrate with the long-tail baseline—specifically, which part of Section 2 is modified to achieve this?

### Questions
My questions that need clarification are included in the weaknesses section.

### Soundness
1

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper presents Long-Tailed Adaptive Pruner (LTAP), a novel approach designed to enhance model efficiency while addressing the challenges posed by long-tailed data distributions. LTAP introduces multi-dimensional importance scoring and a dynamic weight adjustment mechanism to prioritize the pruning of parameters in a manner that safeguards tail class performance. The method incorporates a unique voting mechanism (LT-Vote) to adjust the importance of parameters based on classification accuracy across different classes. The authors report substantial improvements in computational efficiency and classification accuracy, particularly for tail classes, on various benchmark datasets, including CIFAR-100-LT, ImageNet-LT, and iNaturalist 2018.

### Strengths
1. LTAP addresses limitations in conventional pruning approaches for long-tailed distributions. The LT-Vote mechanism and multi-stage pruning offer a unique way to balance model efficiency and tail class performance.

2. The paper provides a solid theoretical analysis, justifying the need for specialized parameter allocation in long-tailed distributions.

3. The authors have provided the code for reproducing the results reported in the manuscript, which is commendable. However, I recommend adding a more detailed introduction in the README file to facilitate easy execution of the code.

### Weaknesses
1. The proposed method is similar to post-hoc correction in Logit Adjustment [1]. I recommend including Logit Adjustment in the baseline comparison.

2. Although the manuscript has theoretically proven that over-parameterization benefits the tailed classes, please conduct preliminary experiments to empirically validate this claim.

3. The dynamic nature of LTAP incurs additional computational overhead.


[1] Logit Adjustment: https://arxiv.org/pdf/2007.07314

### Questions
1. What are the negative effects of model pruning on the head classes?

2. How many iterations are required for the model parameters weight selection in Figure 1?

3. Over-pruning can significantly degrade model performance. What criterion does LTAP use to determine the stopping point for the model parameters selection?

### Soundness
3

### Presentation
3

### Contribution
2
