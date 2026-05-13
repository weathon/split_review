# BrainUICL: An Unsupervised Individual Continual Learning Framework for EEG Applications

- Decision: Accept
- Scores: 8, 1, 8, 5

## Abstract
Electroencephalography (EEG) is a non-invasive brain-computer interface technology used for recording brain electrical activity. It plays an important role in human life and has been widely uesd in real life, including sleep staging, emotion recognition, and motor imagery. However, existing EEG-related models cannot be well applied in practice, especially in clinical settings, where new patients with individual discrepancies appear every day. Such EEG-based model trained on fixed datasets cannot generalize well to the continual flow of numerous unseen subjects in real-world scenarios. This limitation can be addressed through continual learning (CL), wherein the CL model can continuously learn and advance over time. Inspired by CL, we introduce a novel Unsupervised Individual Continual Learning paradigm for handling this issue in practice. We propose the BrainUICL framework, which enables the EEG-based model to continuously adapt to the incoming new subjects. Simultaneously, BrainUICL helps the model absorb new knowledge during each adaptation, thereby advancing its generalization ability for all unseen subjects. The effectiveness of the proposed BrainUICL has been evaluated on three different mainstream EEG tasks. The BrainUICL can effectively balance both the plasticity and stability during CL, achieving better plasticity on new individuals and better stability across all the unseen individuals, which holds significance in a practical  setting.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The author proposed to address the problem that EEG-based model trained on fixed datasets cannot generalize well to the continual flow of numerous unseen subjects in real-world scenarios. The authors propose BrainUICL which enables the EEG-based model to continuously adapt to the incoming new subjects, involving the Dynamic Confident Buffer (DCB) to selectively review the past knowledge and Cross Epoch Alignment (CEA) method to align the model at different time states.

### Strengths
The work is tackling an important problem which potentially can have significant impact in real world. The manuscript is easy to follow in general and the method caters well to the problem settings.

### Weaknesses
It is recommended that the authors to test the model on a wider range of EEG datasets covering different tasks for evaluation of model effectiveness, such as DEAP and high gamma etc.

Detailed analysis on memory cost is needed for the proposed operations such as the dynamic confident buffer and the cross epoch alignment. 

How the different individuals are ordered during the continual learning process? Are they ordered by id or other attributes? Would different ordering affect the model performance much?

Recent works that also cover the exact topic of continual learning on EEG signal are missing in related work section, such as [1][2][3].

I would recommend a more modulized fomulation of related works, e.g. explictly divide the continual learning approaches into subsections   such as regularization, memory based approaches etc., and also distinguish between classic EEG decoding with continual EEG decoding for the EEG analysis part.

Given the work tackles specifically the EEG signal related task, better to highlight in introduction of the possible impact for the proposed continual EEG learning algorithm in real world applications.

More detailed explanation is needed for figures in the manuscript such as Fig. 3, 5 etc.

### Questions
As listed in the strength and weaknesses sections above.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
Individual differences are evident in EEG datasets, and the authors employed continuous learning to facilitate adaptive models for handling new subjects or patients.

### Strengths
Authors tried to use continual learning to adaptively manage individual differences in EEG signals.

### Weaknesses
The claim regarding this study’s contribution is confusing, and the related work review is limited. Individual differences in EEG data are a well-known challenge, and substantial prior work in supervised learning and transfer learning has effectively addressed this issue using robust feature representations. There are many popular EEG datasets for classification tasks that were not discussed and considered.

The authors argue that existing EEG models lack practical applicability, especially in clinical settings with diverse patient profiles (refer to abstract). However, their selected EEG datasets do not include patient data, covering only sleep, emotion, and motor imagery tasks—none involving clinical data. Moreover, several widely-used EEG datasets for classification tasks are notably absent from their analysis.

Previous work on the datasets (above mentioned) they examined has achieved over 90% accuracy in classification tasks through supervised or transfer learning, which suggests these approaches can manage individual differences well. In contrast, this study reports accuracy levels around 40%, which raises the question: what factors account for this significant performance gap?

The role of cross-epoch alignment is unclear, particularly regarding its effectiveness in managing within- and across-subject variations. A more detailed explanation of its purpose and impact on these aspects is needed.

### Questions
See above.

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The work proposes a Continual learning-based framework for addressing the need for robustness against user-specific variability in EEG-based BCIs. The model agnostic approach combines Unsupervised Domain adaptation with a Continual learning framework. 3 different tasks with public datasets are used for the benchmark. Evaluation metrics use incremental individual test sets to measure plasticity and a dataset for generalisation to measure the stability of the approach.

### Strengths
The work addresses the domain's appropriate needs in terms of user variability. The approach is well proposed and benchmarked, including metrics compared with relevant SOTA, ablation studies and computational costs.
The work is technically detailed with appendices and presented with fair clarity.

### Weaknesses
The method section could be better represented with additional labels to the stages in Figure 2 that include the three stages explained in the overview: 1) producing pseudo labels, 2) updating models, and 3) updating storage. It wasn't easy to follow the complete process, shifting across figures, the overview section, each BrainUICL subsection and the appendix.

It's not a weakness per se. While the work is novel in its approach, authors can be more specific in contributions about the novelty of the approach across application domains. It is understood that the approach combines previously known approaches in Unsupervised domain adaptation and continual learning with novelty to the strategies in updating the replay buffer and the training loss, including cross-epoch alignment, where the motivation is similar to EwC.

Quoting the lines from authors: Plasticity (P) denotes the model’s adapting ability to newly emerging individuals, while Stability
(S) indicates the model’s generalization ability to unseen individuals (i.e., new subjects)
Stability refers to the ability to maintain performance on previously seen and unseen individuals, including catastrophic forgetting. The current quote may lead to a misunderstanding. How well does it retain the performance on the dataset used for the M0 model?

The authors mention as follows:
We first explore the concept of Unsupervised Individual Continual Learning(UICL) in EEG-related applications, which is well-suited to the real-world scenario.

Is the concept of UICL novel or has it been proposed earlier? It is not clear from the subsequent discussion in related works. How is it different from Unsupervised Domain Adaption and CL combination apart from defining an individual as a domain?

The concept of generating pseudo labels is not clear. Appendix B clarifies the SSL mechanism used for incremental subjects. However, post-training, how are the pseudo-label confidence values generated, and how is the confidence threshold decided is not clear.

In section 3.3.2, the authors mention: "Here, we tend to utilize the real labeled samples for replay rather than the previously preserved
pseudo-labeled samples." Does this mean that the approach uses real labels for the selected pseudo-labeled samples?

Algorithm 1 on page 6 mentions Mg and Mi-1. However, while using DCB and CEA, Mg is not used and instead, Mi-1 is used. At the same time, the text mentions the use of CPC for adapting to the user's domain. Can the authors clarify this?

The authors do not mention the data preparation step for each dataset, i.e. how long the epochs are, any overlaps between the epochs, and details on the block sizes of the CNN. Some of these parameter choices are significant in evaluating the effectiveness and explainability of the approach.

The results reported in Table 3 and Figure 4 caption mention: Notably, all methods have five same input orders, and these orders are randomly different. It is unclear if the individuals added to the model are in the same order for each iteration. And are they shuffled randomly across those five iterations? I assume that the 95% CIs and SDs in Table 3 are coming from these 5 iterations of different orders.

Are the ACC and MF1 values averaged across incremental individuals with models Mi and across the five iterations of the order? The results are not clear after reading through the sections and looking at tabular data.

In Table 4, Figure 5, ablation results, it is surprising that the base performance(AAA and AAF1) does not decline with the addition of individuals. Does the base model have any replay? It would be good if authors could point to the section if already addressed.

### Questions
Quoting the lines from authors: Plasticity (P) denotes the model’s adapting ability to newly emerging individuals, while Stability
(S) indicates the model’s generalization ability to unseen individuals (i.e., new subjects)
Stability refers to the ability to maintain performance on previously seen and unseen individuals, including catastrophic forgetting. The current quote may lead to a misunderstanding. How well does it retain the performance on the dataset used for the M0 model?

The authors mention as follows:
We first explore the concept of Unsupervised Individual Continual Learning(UICL) in EEG-related applications, which is well-suited to the real-world scenario.

Is the concept of UICL novel or has it been proposed earlier? It is not clear from the subsequent discussion in related works. How is it different from Unsupervised Domain Adaption and CL combination apart from defining an individual as a domain?

The concept of generating pseudo labels is not clear. Appendix B clarifies the SSL mechanism used for incremental subjects. However, post-training, how are the pseudo-label confidence values generated, and how is the confidence threshold decided is not clear.


In section 3.3.2, the authors mention: "Here, we tend to utilize the real labeled samples for replay rather than the previously preserved
pseudo-labeled samples." Does this mean that the approach uses real labels for the selected pseudo-labeled samples?


Algorithm 1 on page 6 mentions Mg and Mi-1. However, while using DCB and CEA, Mg is not used and instead, Mi-1 is used. At the same time, the text mentions the use of CPC for adapting to the user's domain. Can the authors clarify this?

The authors do not mention the data preparation step for each dataset, i.e. how long the epochs are, any overlaps between the epochs, and details on the block sizes of the CNN. Some of these parameter choices are significant in evaluating the effectiveness and explainability of the approach.

The results reported in Table 3 and Figure 4 caption mention: Notably, all methods have five same input orders, and these orders are randomly different. It is unclear if the individuals added to the model are in the same order for each iteration. And are they shuffled randomly across those five iterations? I assume that the 95% CIs and SDs in Table 3 are coming from these 5 iterations of different orders. 

Are the ACC and MF1 values averaged across incremental individuals with models Mi and across the five iterations of the order? The results are not clear after reading through the sections and looking at tabular data. 


In Table 4, Figure 5, ablation results, it is surprising that the base performance(AAA and AAF1) does not decline with the addition of individuals. Does the base model have any replay? It would be good if authors could point to the section if already addressed.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
Pre-trained EEG models often cannot be effectively generalized in practice due to high inter-subject variability. In this work, a novel unsupervised continual learning (CL) approach is proposed that aims to balance adaptation and generalization. To mitigate catastrophic forgetting, the method introduces a penalty term based on cross-epoch alignment and uses a dynamic confident buffer to preserve prior knowledge. Experiments conducted on three different datasets demonstrate superior performance.

### Strengths
The research question addressed in the paper is interesting. The results show that the proposed approach outperforms existing methods.

### Weaknesses
1.	The selection mechanism for the buffer samples requires further clarification, particularly with regard to the number of samples retained per individual. To strengthen the evaluation, it would be helpful to compare the effectiveness of the proposed approach with standard memory sampling techniques, such as reservoir sampling, as well as recent advanced methods specifically designed to address inter-subject variability in EEG data

2.	The KL-based penalty term needs further clarification, in particular why it is only applied in every second epoch and not in every training epoch. Furthermore, the mechanism that controls the impact of this penalty term remains unclear. Is there a specific parameter that controls this loss term to regulate its influence during training?

3.	How the datasets are divided into source, target and test sets is unclear. Given the heterogeneity caused by inter-subject variability, if subjects were randomly assigned to each set (source, target, test), conducting the experiments in multiple runs and reporting the averaged accuracy would be advantageous.

4.	Clarification is needed on how the threshold for self-supervised learning (SSL) is determined in the presence of inter-subject data heterogeneity. How effective are the generated pseudo-labels given this variability? Are there specific criteria for setting this threshold? Additionally, considering that the previous model may be biased toward earlier subjects, could inter-subject variability lead to inaccuracies in the pseudo-labels?

5.	How is the plasticity of the incremental set evaluated? Is there a specific incremental split for training and testing?

6.	What is the total number of samples stored in the storage buffer for each individual? In addition, how are the samples of the target domain replaced in the memory?

### Questions
1.	Clarification is needed on how the threshold for self-supervised learning (SSL) is determined in the presence of inter-subject data heterogeneity. How effective are the generated pseudo-labels given this variability? Are there specific criteria for setting this threshold? Additionally, considering that the previous model may be biased toward earlier subjects, could inter-subject variability lead to inaccuracies in the pseudo-labels?
2.	How is the plasticity of the incremental set evaluated? Is there a specific incremental split for training and testing?
3.	What is the total number of samples stored in the storage buffer for each individual? In addition, how are the samples of the target domain replaced in the memory?

### Soundness
2

### Presentation
3

### Contribution
2
