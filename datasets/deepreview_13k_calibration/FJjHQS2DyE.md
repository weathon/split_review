# Conditional Support Alignment for Domain Adaptation with Label Shift

- Decision: Reject
- Avg Score: 5.67
- Scores: 5, 6, 6

## Abstract
Unsupervised domain adaptation (UDA) refers to a domain adaptation framework in which a learning model is trained based on the labeled samples on the source domain and unlabelled ones in the target domain. The dominant existing methods in the field that rely on the classical covariate shift assumption to learn domain-invariant feature representation have yielded suboptimal performance under the label distribution shift between source and target domains.
In this paper, we propose a novel conditional adversarial support alignment (CASA) whose aim is to minimize the conditional symmetric support divergence between the source's and target domain's feature representation distributions, aiming at a more helpful representation for the classification task. We also introduce a novel theoretical target risk bound, which justifies the merits of aligning the supports of conditional feature distributions compared to the existing marginal support alignment approach in the UDA settings. We then provide a complete training process for learning in which the objective optimization functions are precisely based on the proposed target risk bound. Our empirical results demonstrate that CASA outperforms other state-of-the-art methods on different UDA benchmark tasks under label shift conditions.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposed conditional adversarial support alignment (CASA) to minimize the conditional symmetric support divergence between the source’s and target domain’s feature representation distributions. Generally, the paper is well-written and easy to follow. They evaluate the model on several benchmarks from various types of results. However, the model's novelty is incremental.

### Strengths
This paper proposed conditional adversarial support alignment (CASA) to minimize the conditional symmetric support divergence between the source’s and target domain’s feature representation distributions. Generally, the paper is well-written and easy to follow. They evaluate the model on several benchmarks from various types of results.

### Weaknesses
The model's novelty is incremental over multiple loss functions. The alignment loss in Eq(10) is more like pair-wise alignment loss, which has been explored before for cross-domain graph alignment. It is hard to verify the novelty.

From the experiments, they show the improvements when \alpha decreases. However, there is no insight why this happens. It is better to discuss the intuition and data used behind. It needs more visualization to demonstrate the improvement.

### Questions
The novelty clarification.
The performance analysis.

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies the distribution shift problem for the machine learning model. Specifically, the authors consider the label shift scenario and analyze the limitations in current label shift research, i.e., the strict identical assumption on the conditional distribution $P_{X|Y}$. To address this problem, a novel metric is developed based on the symmetric support divergence (SSD). Mathematically, the proposed metric can be taken as the sliced SSD on each conditional distribution $P_{X|Y=y}$. A new generalization upper bound and some theoretical properties of the proposed metric are provided, which ensure the metric-based model can reduce the generalization error and show the relation between marginal SSD and conditional SSD. Experiments are conducted to show the superiority of the proposed method.

### Strengths
+ A conditional variant of SSD and corresponding theoretical analysis are provided.
+ A discrepancy optimization model is proposed to address the domain adaptation with label shift.
+ Superior experiment results are achieved.

### Weaknesses
 - The basic problem in this paper is indeed equivalent to the generalized target/label shift, where label distribution and conditional distribution change simultaneously. However, many important and closely related references are not introduced and discussed. Specifically, the paper lacks a thorough discussion of methods that address both label and conditional shifts, which is critical for contextualizing the proposed approach. The absence of this discussion makes it difficult to ascertain the novelty and practical significance of the proposed method.
- Consider the existing results for generalized target/label shift, the generalization error analysis provided in Thm. 1 seems to be less compact and not informative. The bound includes several terms, such as the joint error on both domains and constants induced by IMD, which are not directly controlled by the learning process. This makes the bound less useful for practical algorithm design and analysis. It does not offer clear insights into how the proposed method effectively minimizes the target error compared to existing approaches.
- Important theoretical results for the main merits, i.e., conditional variant of SSD, are missing, which makes the proposed method less technically sound. Specifically, the paper introduces a conditional variant of SSD, but lacks a rigorous proof that this new divergence measure is a valid metric on conditional distributions. The absence of such a proof raises concerns about the theoretical validity of the proposed approach, especially since the conditional SSD is the foundation of the method. The paper should demonstrate that the conditional SSD satisfies the properties of a metric, such as non-negativity, symmetry, and the triangle inequality.
- The organization and clarity should be improved. Some justification and intuition for the math definition or theoretical results are insufficient. For instance, the motivation behind the specific weighting of the divergence terms by label probability masses in the conditional SSD definition is not clearly explained. This lack of clarity makes it difficult to understand the underlying principles of the proposed method.
- The experiment comparison is insufficient, where some related works are omitted. The experimental validation does not include comparisons with several relevant methods that address generalized target/label shift, which limits the ability to evaluate the superiority of the proposed method.

### Questions
1. The essential setting and problem that are considered in this submission is indeed similar to the well-known generalized target/label shift [a-f], which are not properly introduced and discussed. Besides, the label shift problem is also extensively studied and has shown promising theoretical results in many studies. From both the generalized target/label shift view and label shift view, this paper does not provide sufficient discussion with these existing methodological and theoretical results. Thus, it is hard to evaluate this paper's contributions, making this work less persuasive.

2. In the generalized target/label shift literature [e, f], generalization bounds and theoretical analysis are also provided. Compared with these results that compactly decompose the shift on the joint distribution as the terms determined by label discrepancy and conditional discrepancy, this paper induces additional constants, i.e., joint error on both domains and the non-negative constants $\delta, \gamma$ induced by IMD.

3. Considering the existing results, the main contribution in this paper is the new conditional discrepancy metric. However, it seems that it cannot be rigorously considered as the class-wise IMD. Specifically, note for the IMD in Def. 3, the weights of the two expected divergence terms are 1; however, in the conditional variant in Def. 4, the divergence terms are weighted by the label probability masses $P(Y=y)$. In such a definition, it naturally raises an crucial question, i.e., is the conditional SSD in Def.4 defines a metric on conditional distribution? This theoretical property is the foundation for the proposed method and should be treated rigorously.

4. The justifications of the derived theoretical results should be improved. Though Thm. 1 ensures that the generalized label shift correction is sufficient to mitigate the label discrepancy and conditional discrepancy, the constants induced in upper-bound seem to be intractable.

5. The discussion in Remark 3 is insufficient and seems to be improper. The advantages of existing results [e] are not properly stated, i.e., literature [e] does not induce additional constant that cannot be controlled by the learning model. Besides, the related works [d,f] are not discussed and compared.

6. Since there are many related works in correcting label shift and conditional shift simultaneously [a-f], they should also be carefully compared in experiment validation. 

[a] Zhang, Kun, et al. "Domain adaptation under target and conditional shift." International conference on machine learning. PMLR, 2013.

[b] Gong, Mingming, et al. "Domain adaptation with conditional transferable components." International conference on machine learning. PMLR, 2016.

[c] Ren, Chuan-Xian, Xiao-Lin Xu, and Hong Yan. "Generalized conditional domain adaptation: A causal perspective with low-rank translators." IEEE transactions on cybernetics 50.2 (2018): 821-834.

[d] Rakotomamonjy, Alain, et al. "Optimal transport for conditional domain matching and label shift." Machine Learning (2022): 1-20.

[e] Tachet des Combes, Remi, et al. "Domain adaptation with conditional distribution matching and generalized label shift." Advances in Neural Information Processing Systems 33 (2020): 19276-19289.

[f] Kirchmeyer, Matthieu, et al. "Mapping conditional distributions for domain adaptation under generalized target shift." International Conference on Learning Representations. 2022.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes Conditional Adversarial Support Alignment (CASA) whose aim is to minimize the Conditional Symmetric Support Divergence (CSSD) between the source’s and target domain’s feature representation distributions, aiming at a more discriminative representation for the classification task. Theoretical analyses are also provide in this work.

### Strengths
1. The proposed CASA addresses the drawback of Adversarial Support Alignment (ASA) by considering discriminative features to align the supports of two distributions, thus mitigating the risk of conditional distribution misalignment caused by indiscriminate reduction of marginal support divergence.
2. Theoretical target error bound are provided in this work.
3. Extensive experiments are conducted to demonstrate the effectiveness of the proposed method.

### Weaknesses
1. The major difference between this work and ASA is the conditional alignment, specifically CSSD and SSD. However, the label in the target domain is unknown, and the authors utilize the entropy conditioning technique described in [1] to address this issue. As far as I know, the method in [1] is not specifically designed for generating pseudo-labels. Could the authors please explain how they adapt this method to mitigate the error accumulation problem associated with using pseudo-labels? A detailed explanation from the authors would be appreciated.
2. More SOTA methods are suggested to discuss and compare, such as SHOT [2], BIWAA [3], CoVi [4], etc.

### Questions
see Weakness

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
