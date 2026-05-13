# Unknown Domain Inconsistency Minimization for Domain Generalization

- Decision: Accept
- Scores: 6, 6, 5, 6

## Abstract
The objective of domain generalization (DG) is to enhance the transferability of the model learned from a source domain to unobserved domains. To prevent overfitting to a specific domain, Sharpness-Aware Minimization (SAM) reduces source domain's loss sharpness. Although SAM variants have delivered significant improvements in DG, we highlight that there's still potential for improvement in generalizing to unknown domains through the exploration on data space. This paper introduces an objective rooted in both parameter and data perturbed regions for domain generalization, coined Unknown Domain Inconsistency Minimization (UDIM). UDIM reduces the loss landscape inconsistency between source domain and unknown domains. As unknown domains are inaccessible, these domains are empirically crafted by perturbing instances from the source domain dataset. In particular, by aligning the loss landscape acquired in the source domain to the loss landscape of perturbed domains, we expect to achieve generalization grounded on these flat minima for the unknown domains. Theoretically, we validate that merging SAM optimization with the UDIM objective establishes an upper bound for the true objective of the DG task. In an empirical aspect, UDIM consistently outperforms SAM variants across multiple DG benchmark datasets. Notably, UDIM shows statistically significant improvements in scenarios with more restrictive domain information, underscoring UDIM's generalization capability in unseen domains.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper focuses on domain generalization through extending the flattened loss landscape in the perturbed parameter space to the perturbed data space. Specifically, they first simulate the unknown domains via perturbing the source data, and then reduce the loss landscape inconsistency between source domains and the perturbed domains, thereby achieving robust generalization ability for the unobserved domain. Theoretical analysis and extensive experiments demonstrate the effectiveness and superiority of this method.

### Strengths
1.This work extends the parameter perturbation in existing SAM optimization to data perturbation, achieving loss landscape alignment between source domains and unknown domains. Experiments show the validity of the proposed objective.  

2.This work establishes an upper bound for DG by merging SAM optimization with the proposed objective.

3.The proposed objective can be combined with multiple SAM optimizers and further enhance their performance, demonstrating the necessity of the loss landscape consistency between source and unknown domains.

### Weaknesses
1. I believe that the proposed data perturbation method is consistent in both ideology and essence with traditional domain augmentation and adversarial attack techniques. So, what is the main difference and advantage of the proposed objective? And what if combining some domain augmentation techniques with the SAM optimizers?

2. How to guarantee that the perturbed data is still meaningful, rather than generating some noisy samples? If so, will enforced the loss landscape alignment across domains bring negative impact? Besides, the unknown distribution may not necessarily be within the scope of perturbed data region.

3. What is the sampling strategy for sampling data from $D_s$ to generate perturbed data?

4. Is the optimization only conducted on the perturbed samples during the formal training phase? Would it be more stable to train on both the source and perturbed samples simultaneously?

5. Since the training procedure involves gradient calculation, what is the time complexity after applying the BackPACK technique?

### Questions
See weakness.

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
This paper considered both parameter- and data-  perturbation in domain generalization. The method is inspired by sharpness aware minimization (SAM). A theoretical analysis is further conducted to show the importance of different perturbations. Finally, the model is deployed in standard benchmarks with improved performance.

------Post-rebuttal 
I would appreciate the rebuttal, which addressed my concerns. I would maintain a positive rating.

### Strengths
1. This paper considered a reasonable solution in domain generalization. Both parameter and data perturbations are conducted for a robust OOD generalization. 
2. The idea seems novel for me in some settings. 
3. Extensive empirical results.

Based on these points, I would recommend a borderline positive.

### Weaknesses
1. Sometimes I find it a bit hard to understand the rationale of the proposed approach. Why do we need to consider both parameter and data perturbation? For example, in paper [1], a theoretical analysis is proposed, which is analogous to equation (11) as the parameter robust. Specifically, while the paper motivates the need for both parameter and data perturbation, the precise mechanism by which they interact to improve generalization remains unclear. The theoretical justification, while present, could benefit from a more intuitive explanation of how the combined perturbations lead to a more robust model compared to parameter perturbation alone, as in [1].
2. Does the choice of data perturbation matter? We know we may face many different possible data-augmentation approaches. Which method(s) do you think should work in this scenario? It's not clear if the method is robust to the choice of data perturbation. The paper should discuss the sensitivity of the proposed method to different data augmentation techniques. For instance, would geometric transformations like rotations and scaling work as well as pixel-based perturbations? A more thorough exploration of this aspect is needed to understand the method's practical applicability.
3. Is it possible to consider the subgroup distribution shift in the context of fairness such as papers [2-3]? A short discussion could be great. The connection to fairness is not immediately obvious. While the paper aims for domain generalization, it would be valuable to discuss how the proposed method could potentially address fairness concerns related to subgroup performance disparities. A brief discussion on whether the method inherently promotes fairness across different subgroups, or if additional steps would be needed, would be beneficial.

### Questions
See weakness part.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper, titled "Unknown Domain Inconsistency Minimization for Domain Generalization," introduces an approach to improve domain generalization using Unknown Domain Inconsistency Minimization (UDIM) in combination with Sharpness-Aware Minimization (SAM) variants.  The paper's novelty lies in its approach to improving domain generalization by focusing on both parameter and data perturbed regions. UDIM is introduced as a novel concept, addressing the need for robust generalization to unknown domains, which is a critical issue in domain generalization. The idea of perturbing the instances in the source domain dataset to emulate unknown domains and aligning flat minima across domains is innovative. While SAM-based approaches have shown promise in DG, UDIM extends the concept to address specific shortcomings, which is a novel contribution.

### Strengths
1. The paper appears to be technically sound. It provides a well-defined problem statement for domain generalization and formulates UDIM as an optimization objective. The authors validate the theoretical foundation of UDIM and provide empirical results across various benchmark datasets, demonstrating its effectiveness. The methodology is explained clearly, and the experiments are well-documented.

2. The paper is well-structured and clearly written. It provides a thorough introduction, problem definition, and a detailed explanation of the proposed method. The methodology is presented step by step, and mathematical notations are used effectively. The experimental setup and results are also presented in a clear and organized manner. However, the paper is quite technical, and readers with less familiarity with domain generalization and machine learning might find some sections challenging to follow.


3. The paper addresses an important challenge in domain generalization, namely, the ability of models to generalize to unknown domains. The proposed UDIM method appears to be effective in improving the performance of existing SAM-based approaches, as demonstrated through experimental results. The potential impact of this paper on the AI research community is significant, particularly in the field of domain generalization.

### Weaknesses
1. Baselines. The baselines are not enough because the latest DG method is Fisher, which is published at 2022.

2. The performance of Fisher on the PACS dataset in this paper differs significantly from the results reported in [1] (85.5 vs. 81.3). It raises the question: what factors contribute to this discrepancy?

3. Furthermore, the newly introduced baselines exhibit inferior performance compared to ERM across most benchmarks. This raises concerns about their utility or suggests that these baselines may not offer significant value.

4. The decision to exclusively employ the leave-one-out setting warrants clarification. Understanding the rationale behind this choice would contribute to a more comprehensive evaluation.

### Questions
see weakness

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper highlights the importance of exploring the perturbation in data space to enhance the performance of domain generalization based on the sharpness-aware minimization approach. The authors proposed an unknown domain inconsistency minimization approach, which combines data perturbation to generate the worst-case unseen domains and weight perturbation which is sharpness-aware minimization. They further showed some theoretical analysis for their algorithm. Experiments have shown the effectiveness of the algorithm.

-----Post rebuttal

I appreciate the efforts in writing the response. While the efficiency problem is not solved, I acknowledge the efforts in trying to address it. Therefore, I increase my score to 6.

### Strengths
1. The idea of combining data perturbation with weight perturbation is interesting. The weight perturbation is a pretty “standard” approach to learn robust models and the combination of data perturbation can further enhance such robustness.
2. The paper is easy to understand and follow. The algorithm design is clear.
3. The experiments have shown the effectiveness of the approach.

### Weaknesses
1. The novelty of the approach is limited since the perturbation of input data is somewhat similar to existing approach called CrossGrad [Shankar et al., 2018] which also perturbs existing training data by reversing their gradient direction to generate unseen training domains. That being said, the paper can be seen as a combination of CrossGrad (by adding original data perturbation) and sharpness-aware minimization.
2. There lacks guaranteed proof showing that by perturbing the input to the size of $\rho$ (which is pretty similar to adversarial perturbation), the generated unseen domains can cover the entire space of unseen domains. It seems that with the size of $\rho$ becomes larger, the generalization risk (Eq. 3) is smaller. However, in that way, the sampling and generating efficiency will be heavily impacted. There are no clear analysis on the parameter $\rho$: what kind of perturbation can help the method already generalize the same as existing ones; better than existing ones, or worse than existing ones?
3. Insufficient experiments. The common benchmark in domain generalization is DomainBed, but the paper did not use it; instead, it used CIFAR-10-C and PACS, which are clearly not sufficient. DomainBed has other challenging datasets inclusing CMNIST and DomainNet, which should be tested.

### Questions
1. I cannot see the advantage of UDIM in Figure 5: it seems that the loss landscape (bottom right) of UDIM is no better than SAGM and GAM? Can authors offer further explanations?
2. On PACS, the results are not consistent with the original results from DomainBed. Authors should double check their results.
3. What is the efficiency of the method?
4. What do the generated domains look like?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
