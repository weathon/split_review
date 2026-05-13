# Federated Continual Learning Goes Online: Uncertainty-Aware Memory Management for Vision Tasks and Beyond

- Decision: Accept
- Scores: 8, 6, 5, 5

## Abstract
Given the ability to model more realistic and dynamic problems, Federated Continual Learning (FCL) has been increasingly investigated recently. A well-known problem encountered in this setting is the so-called \textit{catastrophic forgetting}, for which the learning model is inclined to focus on more recent tasks while forgetting the previously learned knowledge. The majority of the current approaches in FCL propose generative-based solutions to solve said problem. However, this setting requires multiple training epochs over the data, implying an offline setting where datasets are stored locally and remain unchanged over time. Furthermore, the proposed solutions are tailored for vision tasks solely. To overcome these limitations, we propose a new approach to deal with different modalities in the \textit{online} scenario where new data arrive in streams of mini-batches that can only be processed once. To solve catastrophic forgetting, we propose an uncertainty-aware memory-based approach.  Specifically, we suggest using an estimator based on the Bregman Information (BI) to compute the model's variance at the sample level. Through measures of predictive uncertainty, we retrieve samples with specific characteristics, and – by retraining the model on such samples – we demonstrate the potential of this approach to reduce the forgetting effect in realistic settings while maintaining data confidentiality and competitive communication efficiency compared to state-of-the-art approaches.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper presents a new federated continual learning setting to deal with different modalities in the online scenario. The proposed uncertainty-aware memory-based approach uses an estimate to measure of predictive uncertainty of samples, The extensive experiments demonstrate the effectiveness of reducing the forgetting effect in realistic settings while maintaining data confidentiality and competitive communication efficiency.

### Strengths
- A real-world online federated continual learning setting is proposed to adapt the practical scenario where new data arrive in streams of mini-batches that can only be processed once.
- Using a bias-variance decomposition of the cross-entropy loss for classification tasks has some merits.
- Experiments are comprehensive and well-designed.

### Weaknesses
 - Some advanced memory replay methods are lacking.
- Why do not consider some uncertainty-aware continual learning methods, such as [1] for comparison?
- Why the number of $M$ is different from different datasets?
- The improvement on the KC-Cell dataset is incremental compared to the other datasets. why?
- On the left of Fig. 3, it is better to discuss the notable performance gap between the proposed method and the others on the last task.

### Questions
Please see the weakness above.

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
The paper proposes an uncertainty aware-memory-based approach for federated continual learning in an online setting where an estimator based on Bregman Information is employed to compute model’s variance at sample level. The proposed method includes predictive uncertainty-aware updated coupled with random replays.

### Strengths
1.	The problem statement is meaningful and not widely talked about.

2.	The proposed method works considering memory management in an uncertainty sampling setting, and handles class imbalance and data scarcity well. 

3.	The performance looks promising and overall the paper is easy to read.

### Weaknesses
1.	The fundamental idea of memory management is based on predictive uncertainty which is highly model-dependent and widely used.

2.	While federated continual learning in online settings is not very common, the paper proposed uncertainty estimator and random sampling for replay sets are not novel.

3.	A scalability issue may arise for large datasets such as ImageNet.

4.	It’d be interesting to see how the proposed method would work if task numbers were increased (>20).

### Questions
In table 5, for BI method, why do you think the last forgetting(F) score is lower than FedCIL for CIFAR100? Is it related to the increased number of classes?

Please refer to weaknesses section.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes a federated learning with end points doing online continual learning (CL), called online-FCL. To address the new task, the paper proposes a memory based CL method that manage samples based on its uncertainty score using Bregman Information (BI). The proposed method is evaluated on CIFAR10/100. On vision, medical and textual datasets, the proposed method does not show much of gain but in multi-modal data, the proposed method improves the performance over the state of the arts by significant gains.

### Strengths
* Proposing a new federated learning with **online** continual learning.
* Proposed method improves the accuracy significantly over the state of the arts in multi-modal (vision-and-textual task) setup

### Weaknesses
 * The proposed method is a straightforward application of Gruber & Buettner (2023), thus the technical novelty is limited.
* Empirical gain seems marginal (also considering the standard deviation) compared to prior arts (Table 1-4). But in Table 5, the empirical gain in vision and textual task seems significant. Any reasoning for this?
* Empirical validation is limited due to the size of the dataset. Although CIFAR-10/100 are popularly used datasets in CL literature, they are quite small sized. ImageNet-1K would be the minimum large scale dataset to validate the value of the proposed method.
* Some results are not clear 
  * In Fig. 3, why the BI and MFCL improve the last accuracy significantly only at the last accuracy?
* In L291-292, it is claimed that "the BI-based estimation of the epistemic uncertainty is meaningful also under distribu- tion shift and able to identify robust and representative samples". But is this fact used in your method? If so, can you analyze that this is true in the Fed CL context?
* Presentation can be improved.
  * In several lines, line break has been removed -- L056, L271, L290 to name a few
  * Some abbreviation is not used without definition -- L072 CF -> catastrophic forgetting (this should be defined in L048)
  * Figure 1 could be larger and clearer. Currently it is drawn with too small fonts, making visibilty bad.
* Misc.
  * Similar previous work that uses CE loss for uncertainty of a sample is missing: Koh et al., **Online Boundary-Free Continual Learning by Scheduled Data Prior**, *ICLR 2023* (the method called CLIB)

### Questions
Please refer to my comments in the weakness section.

### Soundness
3

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
3

### Summary
The paper addresses Federated Continual Learning under the challenges of catastrophic forgetting and online learning, where new data arrives in sequential mini-batches and can only be processed once. The authors introduce an uncertainty-aware memory management strategy that leverages Bregman Information to measure predictive uncertainty. This approach selectively retains samples in memory based on their uncertainty, aiming to improve learning retention while handling various data modalities beyond vision tasks. The paper also showcases the method’s performance on vision and text data, demonstrating its capability to mitigate forgetting across diverse, real-world settings.

### Strengths
1. The paper presents a novel framework for Federated Continual Learning in an online setting, effectively addressing the practical limitations faced in scenarios where clients continuously receive new data without the ability to revisit previous data.

2. The innovative use of Bregman Information for uncertainty estimation allows for selective sample retention based on epistemic uncertainty.

3. The authors conduct extensive experiments with detailed analyses, demonstrating the effectiveness and depth of the proposed approach across various data types and scenarios.

### Weaknesses
1. The performance improvements on the CRC-Tissue and KC-Cell datasets are marginal. Given that these datasets contain more samples than others, could you provide a justification for this outcome?

2. How does the Bregman Information approach to uncertainty estimation compare with recent probabilistic methods in Federated Continual Learning, particularly regarding computational efficiency and predictive accuracy?

3. Most results are primarily compared to other uncertainty measurements, while comparisons with previous continual learning or federated learning methods appear limited.

### Questions
1. The performance improvements on the CRC-Tissue and KC-Cell datasets are marginal. Given that these datasets contain more samples than others, could you provide a justification for this outcome?

2. How does the Bregman Information approach to uncertainty estimation compare with recent probabilistic methods in Federated Continual Learning, particularly regarding computational efficiency and predictive accuracy?

3. Most results are primarily compared to other uncertainty measurements, while comparisons with previous continual learning or federated learning methods appear limited.

### Soundness
3

### Presentation
3

### Contribution
3
