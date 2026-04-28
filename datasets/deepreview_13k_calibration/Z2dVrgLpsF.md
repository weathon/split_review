# On partial prototype collapse in clustering-based self-supervised learning

- Decision: Reject
- Avg Score: 5.25
- Scores: 6, 6, 3, 6

## Abstract
A prominent self-supervised learning paradigm is to model the representations as clusters, or more generally as a mixture model. Learning to map the data samples to compact representations and fitting the mixture model simultaneously leads to the representation collapse problem. Regularizing the distribution of data points over the clusters is the prevalent strategy to avoid this issue. While this is sufficient to prevent full representation collapse, we show that a partial prototype collapse problem still exists in these methods, that leads to significant redundancies in the prototypes. Such prototype redundancies serve as shortcuts for the method to achieve a marginal latent class distribution that matches the prescribed prior distribution. We show that by encouraging the model to use diverse prototypes, the partial prototype collapse can be mitigated. Effective utilization of the prototypes enables the methods to learn more fine-grained clusters, encouraging more informative representations. We demonstrate that this is especially beneficial when pre-training on a long-tailed fine-grained dataset.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper underlines a prevailing phenomenon of previous self-supervised learning works:the regularization of marginal latent class distribution to a specific prior distribution, often leading to partial prototype collapse. Based on this observation, this paper proposes a regularization loss that maximizes the differential entropy of the prototype vectors, aiming to enhance cluster diversity. The experiments are focused on improving the performance on long-tailed fine-grained datasets, specifically demonstrated on the linear probing accuracy on iNaturalist-2018.

### Strengths
1.	The recognition of partial prototype collapse illuminates a previously overlooked phenomenon for SSL.
2.	This paper proposes an interesting term to quantitatively assess the uniqueness of prototypes and pinpoints the shared characteristics of previous SSL works, namely the mismatch between initialized prototypes and unique prototypes.
3.	The writing is clear, offering both numerical experiments for elucidation and theoretical deductions for integrating previous works cohesively.
4.	The proposed method brings some noticeable improvement on its baseline, tackling the long-tailed scenario with minor adjustments to the method design.

### Weaknesses
1.	The proposed method mainly works on long-tailed datasets, however, its motivation does not rigorously align with its goal. Although the authors mention that previous works encourage MLCD to match a prescribed uniformed prior distribution, why could KoLeo-proto regularization move away from such a conventional prior? More elaborations are needed to shed light on how the KoLeo-proto regularization could help with the long-tailed problem. Specifically, while the paper identifies that previous methods may collapse prototypes, it does not clearly explain why maximizing the differential entropy of the prototype vectors directly addresses the challenges posed by long-tailed distributions. The connection between prototype diversity and improved performance on imbalanced datasets needs further clarification. It is not immediately obvious why preventing prototype collapse would inherently lead to better handling of minority classes, which is the core challenge in long-tailed learning.

2.	The KoLeo-proto regularization mainly aims to improve the diversity of the learned clusters while reducing partial prototype collapse. Another stream of study [R1], which explores the neural collapse phenomenon that also scatters the prototypes into an ETF geometric structure, also proves to be effective for imbalanced learning. Are there any similar spirits between this KoLeo-proto regularization and the neural-collapse-inspired design?
[R1] Inducing Neural Collapse in Imbalanced Learning: Do We Really Need a Learnable Classifier at the End of Deep Neural Network, NeurIPS, 2022.

3.	The KoLeo-proto regularization does not seem to improve the transfer performance (-0.7% on ViT-base and +0.1% on ViT-small ), as pointed out by the authors in Table 3. The authors explain that it is a common trade-off also existing in other works whose performance thrives in few-shot scenarios but falls short in transfer learning. Unfortunately, there are no further explanations for why this trade-off exists. Also, it seems that KoLeo-proto generally gains negligible improvement on finetuning tasks, as also indicated in Table2, 4. It would be better to elaborate on the results. The lack of improvement in transfer learning and fine-tuning scenarios raises concerns about the general applicability of the proposed regularization. It is crucial to understand why the method, which is effective in specific long-tailed scenarios, does not translate well to more general settings.

### Questions
This paper mainly takes iBoT-vMF as its baseline. Considering the simple and elegant form of KoLeo-proto regularization, would it also benefit other baselines either in qualitative (i.e. the uniqueness of prototypes) or quantitative (i.e. the performance) ways?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper investigates the issue of Partial Prototype Collapse (PPC) in self-supervised learning (SSL), which can lead to a significant decrease in classification performance. Additionally, the study introduces a novel prototype-based regularization strategy and experimental results confirm the effectiveness of this strategy in mitigating the PPC phenomenon.

### Strengths
1. This study marks the first to propose the issue of Partial Prototype Collapse as an inherent challenge in the field of self-supervised learning (SSL). Furthermore, it extensively delves into the existing SSL methods in the Introduction section.

2. The proposed method is simple yet effective. The overall solution is technique sounds and might become a new baseline of SSL.

3. The paper's structure is well-organized, and it provides a relatively clear description of the method.

4. The claims made in the paper are substantiated by the results and findings obtained through the conducted experiments.

### Weaknesses
1.  The employed objective function is rather conventional, which may limit the overall innovation of the study.

2. The experiments in the paper mainly compare the proposed strategy with the baselines, without a direct comparison with the existing regularization techniques.

3. The impact of regularization paramete $\lambda$ on the effectiveness of the proposed regularization method may not have been thoroughly explored in the paper. 

4. The paper heavily relies on textual descriptions, with limited use of graphics to explain the issues or algorithms, which might pose difficulties for readers.

### Questions
1. How is the number of prototypes determined for different datasets?

2. How does the proposed regularization strategy perform in terms of robustness under different hyperparameters?

3. The paper claims that the proposed method is more effective in long-tail classification tasks. Does this suggest that long-tail distributions are more likely to lead to Partial Prototype Collapse?

4. Employing visuals to illustrate Partial Prototype Collapse could enhance readers' comprehension.

5. Is it necessary to determine the initial number of prototypes before the algorithm is executed?

6. Some details of the experimental setup were not clarified. For instance, what optimizer was used? 

7. This paper only utilizes various ViT-based architectures, does the Partial Prototype Collapse also observed in CNN-based architectures?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This work reveals a partial prototype collapse problem which leads to significant redundancies in the prototypes. Such prototype redundancies serve as shortcuts for the method to achieve a marginal latent class distribution that matches the prescribed prior distribution. By encouraging the model to use diverse prototypes, the partial prototype collapse can be mitigated, which is especially beneficial when pre-training on a long-tailed fine-grained dataset. Effective utilization of the prototypes produces fine-grained clusters, encourages more informative representations, and may reduce computational expenses.

### Strengths
1. The paper is easy to follow with good writing, well organization, and comprehensive literature review.
2. The analysis of regularizations in the DINO family of SSL methods is helpful to grasp the principle of the proposed method.
3. The definition of partial prototype collapse is clear and reasonable.

### Weaknesses
1. The title of this work seems to explore the partial prototype collapse for all clustering-based SSL methods. However, without any clarification, all explorations and discussions are focused on the DINO family of SSL methods by default.
2. The last sentence of the Sec. Conlusion claims the superior learning efficiency of the proposed method. However, there is no experiment to prove that.
3. Although several experiments justify the efficacy of the proposed method on long-tailed fine-grained datasets and few-shot settings, there is no convincing explanations.
4. The proposed method is implicitly built on an assumption that improving the uniformity of the representation space while keep its alignment will produce a better sample distribution. However, without superior distribution priors, the trials of the proposed methods report limited performance improvements on standard SSL evaluations.

### Questions
See the weaknesses.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors found that a partial prototype collapse problem still exists in self-supervised learning methods.  So they proposed to regularize the diversity of prototypes, which can mitigate the partial prototype collapse problem. Experiments on several benchmarks demonstrate the benefit of this reguparization.

### Strengths
The authors defined a partial prototype collapse and demonstrate its occurrence in the DINO family of methods using different backbone models, and proposed KoLeo-proto regularization to prevent the partial prototype collapse. Overall, the paper is well organized and prepared.  
1.  Self-supervised learning is very useful for representation learning, and the collapse problem seriously affecting the quality of features. The motivation of  solving a partial prototype collapse problem is soundness.
2. The experiments are comprehensive, including imagenet classification, transfer learning, long-tail dataset, and sensitivity analysis.

### Weaknesses
1. Is there any theoretical results to guarantee that minimizing $L_{KP}$ will make the prototypes to  be uniformly distributed in the latent space?  Why not just minimizing $-\sum_{i}\sum_{j}||\mu_{i}-\mu_{j}||^{2}$?
2. Overall, the improvement is small when compared with the baseline iBOT-vMF. For example, the classification accuracy of imagenet in Table 2 are very close for iBOT-vMF and  iBOT-vMF (kp). 
3. The authors should give more quantitative or qualitative results to demonstrate how the proposed KP regularization can solve the partial prototype collapse problem, e.g. visualization.

### Questions
1. Is there any theoretical results to guarantee that minimizing $L_{KP}$ will make the prototypes to  be uniformly distributed in the latent space?  Why not just minimizing $-\sum_{i}\sum_{j}||\mu_{i}-\mu_{j}||^{2}$?
2. Overall, the improvement is small when compared with the baseline iBOT-vMF. For example, the classification accuracy of imagenet in Table 2 are very close for iBOT-vMF and  iBOT-vMF (kp).  
3. The authors should give more quantitative or qualitative results to demonstrate how the proposed KP regularization can solve the partial prototype collapse problem, e.g. visualization.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
