# FairDD: Fair Dataset Distillation via Adversarial Matching

- Decision: Reject
- Scores: 3, 6, 8, 6

## Abstract
Condensing large datasets into smaller synthetic counterparts has demonstrated its promise for image classification. However, previous research has overlooked a crucial concern in image recognition: ensuring that models trained on condensed datasets are unbiased towards protected attributes (PA), such as gender and race. Our investigation reveals that dataset distillation (DD) fails to alleviate the unfairness towards minority groups within original datasets. Moreover, this bias typically worsens in the condensed datasets due to their smaller size. To bridge the research gap, we propose a novel fair dataset distillation (FDD) framework, namely FairDD, which can be seamlessly applied to diverse matching-based DD approaches, requiring no modifications to their original architectures. The key innovation of FairDD lies in synchronously matching synthetic datasets to PA-wise groups of original datasets, rather than indiscriminate alignment to the whole distributions in vanilla DDs, dominated by majority groups. This synchronized matching allows synthetic datasets to avoid collapsing into majority groups and bootstrap their balanced generation to all PA groups. Consequently, FairDD could effectively regularize vanilla DDs to favor biased generation toward minority groups while maintaining the accuracy of target attributes. Theoretical analyses and extensive experimental evaluations demonstrate that FairDD significantly improves fairness compared to vanilla DD methods, without sacrificing classification accuracy. Its consistent superiority across diverse DDs, spanning Distribution and Gradient Matching, establishes it as a versatile FDD approach.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes the idea of fair dataset distillation by ensuring that the protected attribute-based samples provide uniform signals across the groups. This is ensured using a distribution matching objective, uniformly distributed across the protected groups. The authors show results on various benchmarks including synthetic and real-world (CelebA) datasets.

### Strengths
- The paper is well-written and clear.
- The experimental results provided are extensive and show improvements.

### Weaknesses
 - Novelty: The biggest concern for me is the novelty. The idea of class-weighting proposed in this work is classically used in class-imbalanced problems. Further, it has been used in the fairness scenarios as well by multiple works [R1, R2]. Although the results are improved it’s hard to see the ingenuity in the approach, it would be great if the authors could please clarify the differences.


- Adversarial Reference is Vague: The authors mention the formulation to be adversarial, however, the loss doesn’t seem to have an explicit adversarial component. Hence, it would be great to clarify the objective clearly concerning the min-max loss component. 


- Theory: Theorem 4.2 is a variant of weighted ERM kind of results, which shows that the weighted loss could be an upper bound to standard ERM kind of loss [R3]. Such weighted results have been extensively studied earlier in literature, hence it’s hard for me to realize the potential of the new results.


- Related Baseline Missing: The following paper [R2] introduces the idea of weighted ERM for fairness with protected sub-groups, using loss weighting and escaping saddle points via SAM [R2, R4] to improve fairness properties. Due to the overlap of the current problem with this, it’s important to compare or contrast the proposed method with a baseline constructed on the basis of these.

### Questions
Is the weighted centroid matching objective in Eq. 4 correct? It might be insufficient, as two groups of samples with entirely different distributions can still have the same centroid. Could you clarify the distribution matching objective better?

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper addresses a crucial issue: fairness in dataset distillation. The first part of the paper shows that if the original dataset is biased, the distilled dataset exacerbates such biases by generating images primarily from the majority group. Thereafter, the paper proposes a simple modification to the loss function to ensure representation from the different groups in the condensed dataset. The authors have shown theoretical evidence for the efficacy of their method and demonstrated its effectiveness across multiple datasets of varying versions. Overall, this is an issue that demands more research and requires further analyses to ensure that the condensed dataset is fair.

### Strengths
1. The loss function FairDD seems intuitive. Instead of optimizing across all samples of a given class, the authors have ensured that each group in the training set gets a fair chance in pulling the condensed dataset towards itself.
2. The analysis on the exacerbation of biases in the distilled dataset is a strong evidence towards the necessity behind further research on this issue.
3. The paper has provided theoretical analysis for their proposed approach.
4. The authors have performed their analysis on a variety of datasets and across multiple model architectures.

### Weaknesses
1. For the ColorMNIST and CelebA, the DEO_M is often comparable to that of the original dataset, showing that the distilled data still may follow the bias of the original dataset, though it hasnt alleviated the bias.
2. One big issue is that it is not clear if the reported scores are statistically signifcant as no std was reported.
3. The only real image dataset for which the analysis was done is CelebA.

### Questions
1. The proposed loss function currently considers all groups, but does not consider their cardinality. Would upweighting the minority groups benefit the loss further, where the weights can be inversely proportional to the group size?
2. How robust is this method to the availability of the spurious/group labels? E.g., if a method like JTT [a] is employed to get pseudo labels for the bias attribute, how would the performance change in terms of fairness?
3. What if the original dataset is group balanced first, and then the traditional distillation losses are applied? Would that automatically help reduce the bias?
4. The target attributes reported for CelebA are either attractive, big nose, or young. Attractive and big nose can be subjective. Does the efficacy of the proposed method hold for a more objective attribute like blond hair, which is a famously reported in the fairness literature?


        [a] Liu, Evan Z., et al. "Just train twice: Improving group robustness without training group information." International Conference on Machine Learning. PMLR, 2021.

### Soundness
3

### Presentation
4

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
This paper addresses a critical issue in dataset distillation (DD), where biases inherent in original datasets tend to amplify within condensed datasets, often exacerbating unfairness toward minority groups. The authors propose "FairDD," a fair dataset distillation framework designed to mitigate these biases by integrating adversarial matching for protected attribute (PA)-wise groups, such as gender and race. Unlike conventional DD approaches that indiscriminately align to the entire dataset distribution (often skewed by majority groups), FairDD aligns synthetic datasets with specific PA groups, aiming to prevent dominance by majority representations. This targeted approach allows for more balanced synthetic data generation, maintaining classification accuracy while improving fairness. The paper’s theoretical analyses and extensive experiments show that FairDD outperforms traditional DD methods in fairness metrics without compromising on accuracy.

### Strengths
Novel Approach to Fairness in Dataset Distillation: The concept of adversarially aligning synthetic datasets with PA-wise groups is an innovative approach that tackles a commonly overlooked issue in DD. FairDD’s adversarial matching mechanism, focusing on each PA group rather than the overall distribution, is a thoughtful solution that could inspire further research in fair dataset synthesis.

Versatility Across Matching-Based DD Methods: The proposed FairDD framework is adaptable to various matching-based DD methods, as shown by its successful application in both Distribution and Gradient Matching methods. This versatility highlights FairDD’s potential as a generally applicable solution in the DD field.

Extensive Theoretical and Experimental Validation: The authors conducted thorough theoretical analyses to support their framework, providing a solid foundation for understanding why FairDD effectively reduces biases in dataset distillation. Additionally, they validated their approach through extensive experiments, consistently showing improved fairness across different DD methods without sacrificing model accuracy. This combination of theoretical and empirical rigor adds credibility to FairDD's effectiveness and reliability.

Maintaining Accuracy while Enhancing Fairness: An important advantage of FairDD is that it achieves fairness without compromising the target classification performance, addressing a common trade-off in fairness-oriented methods.

### Weaknesses
Limited Practicality Discussion: While FairDD’s focus on fairness is commendable, the framework’s real-world applicability could be affected by computational demands introduced by adversarial matching. The authors could discuss the added computational overhead and resource requirements, especially when scaling to larger datasets. The paper lacks a detailed analysis of how the adversarial training impacts training time and memory consumption, particularly as the number of protected attributes or the size of the dataset increases. This is a critical aspect for practical deployment, and the absence of such analysis limits the assessment of the method's feasibility in real-world scenarios.

Scalability to Other Protected Attributes: The paper primarily discusses FairDD’s effectiveness concerning attributes like gender and race. However, it is unclear how well this method generalizes to other protected attributes or more nuanced groups within a PA, especially when there are multiple attributes with intersecting biases. An exploration of such scenarios would enhance the robustness of the approach. The current evaluation does not sufficiently address the method's behavior with a larger number of protected attributes or when these attributes have complex interdependencies, which are common in real-world datasets. This lack of exploration limits the generalizability of the findings.

Potential Dependency on Original Dataset Quality: The framework assumes that PA groups in the original dataset are balanced enough to train FairDD effectively. In real-world applications, where some PA groups might be underrepresented, this assumption could limit FairDD’s effectiveness. The authors could address how FairDD performs under different levels of dataset imbalance. The paper does not explore the sensitivity of FairDD to imbalances within protected attribute groups. In real-world scenarios, it is common for certain groups to be significantly underrepresented, and the performance of FairDD under such conditions is not clear. This is a critical limitation that needs to be addressed to ensure the method's robustness and applicability.

Theoretical Justification: While the paper provides theoretical analysis, a deeper exploration of why adversarial matching effectively reduces bias in condensed datasets could strengthen the contribution. Further theoretical insights could add rigor and help clarify the underlying mechanisms driving FairDD’s success. The current theoretical analysis provides a high-level understanding but lacks a detailed explanation of how the adversarial matching process specifically mitigates bias at the level of individual data points or feature representations. A more granular analysis would strengthen the theoretical foundation and provide a deeper understanding of the method's effectiveness.

### Questions
Good paper. I have no further questions

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
This paper addresses attribute imbalance in dataset distillation, focusing on improving the fairness of condensed datasets. The authors present a unified perspective on data matching and identify unfairness issues in conventional distillation methods regarding protected attributes. To address this, they introduce an adversarial matching loss function that ensures equal contribution from different attribute groups. Their theoretical analysis demonstrates both the equitable treatment of attribute groups and the preservation of vanilla data matching optimization. Experimental results on C-MNIST, C-FMNIST, CIFAR10-S, and CelebA datasets provide both quantitative and qualitative evidence of the method's effectiveness in mitigating unfairness compared to naive matching approaches.

### Strengths
1. This is the first work to identify attribute unfairness in current data distillation methods.

2. The authors propose a simple yet effective method to solve this unfairness.

3. The authors provide theoretical justification for their proposed method in addressing the unfairness issue.

4. The authors present comprehensive experiments to demonstrate the soundness of their proposed method.

5. The paper is well-written and easy to follow.

### Weaknesses
1. Including Vision Transformer architectures as backbone networks would further demonstrate the method's generalizability.

2. Examining its performance on more challenging datasets like CIFAR-100 or ImageNet would strengthen its practical applicability.

3. Including visual examples from the CelebA dataset in the supplementary material would help readers better understand the fairness improvements achieved by the proposed method.

4. The term "adversarial matching" could benefit from additional clarification, as the current mathematical formulation doesn't explicitly show adversarial operations. A brief explanation of this terminology would enhance the paper's clarity.

### Questions
Please see the weaknesses

### Soundness
3

### Presentation
3

### Contribution
3
