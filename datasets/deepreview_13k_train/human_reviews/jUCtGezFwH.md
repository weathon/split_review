# Online Sequential Learning from Physiological Data with Weighted Prototypes: Tackling Cross-Subject Variability

- Decision: Reject
- Scores: 6, 5, 3, 5

## Abstract
Online Continual Learning (OCL) enables machine learning models to adapt to sequential data streams in real-time, especially when only a small amount of data is available. However, applying OCL to physiological data such as electroencephalography (EEG) and electrocardiography (ECG) is often complicated by inter-subject variability, which can lead to catastrophic forgetting and performance degradation. Existing OCL methods are currently unable to effectively address this challenge, leading to difficulties in retaining previously learned knowledge while adapting to new data. This paper presents Online Prototypes Weighted Aggregation (OPWA), a novel method specifically designed to address the problem of catastrophic forgetting in the presence of inter-subject variability through the use of prototypical networks. OPWA facilitates the retention of knowledge from past subjects while adapting to new data streams.
The OPWA method uses an innovative prototype aggregation mechanism that fuses intra-class prototypes into generalized representations by accounting for both within-class and inter-class variation between subjects. Extensive experiments show that OPWA consistently outperforms existing OCL methods in terms of fast adaptation and mitigation of catastrophic forgetting on different physiological datasets with different modalities, and provides a robust solution for learning on sequential data streams.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The work tackles the problem of online sequential learning from physiological data by introducing a a robust prototype aggregation mechanism that synthesizes global prototypes from cross-subject prototypes. It considers the underlying data distribution of each subject while constructing global prototypes. The aggregation mechanism takes into account intra-class variance and thereby naturally improves the decision boundaries between inter-class prototypes.

### Strengths
The work is tackling an important problem and the paper is easy to follow in general. 

The proposed method fits the problem well by considering the subject variance and distribution shift in generating the prototypes.

The authors performed detailed experiments on top of numerous public EEG datasets and demonstrated the effectiveness of proposed method.

### Weaknesses
1. Given the work tackles specifically the EEG classification task, the authors need to highlight in introduction of the possible application scenarios for the proposed online EEG classification algorithm in real world.
2. It is unclear how the subjects are arranged sequentially, is it arranged by subject id or other attributes? would the author consider difference sequential orders?
3. Would be better if the author could write 1-2 paragraphs in related work to summarize the major strengths and weaknesses of current online decoding approaches specifically in EEG analysis domain, in addition to the introduciton on general continual learning approaches.
4. At the beginning of Section 3, before going into the technical details of the methods/algorithms, please write a summary paragraph about the main feature/benefits/strengths of the proposed approach.
5. It is recommended that the author to provide more detailed explanations and explanations for Fig 3 and 4.
6. In the conclusions, in addition to summarizing the actions taken and results, please strengthen the explanation of their significance. The authors are suggested to enlist limitations of the study in the conclusion also.

Other minors:
line 174, as reinforce learning have very specific meaning, I would suggest change it to something like “enforce learning of past subjects”.
Some of the datasets are for motor imagery and some are for emotion recognition, better to mention the purpose of each dataset in 4.1 description.

### Questions
As listed in strength and weakness section.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents a new method for online continual learning. The presented method, Online Prototype Weighted Aggregation (OPWA), is specifically designed for catastrophic forgetting in the presence of inter-subject variability through the use of prototypical networks. 
The method employs a prototype aggregation mechanism that fuses intra-class prototypes into generalized representations by accounting for both within-class and inter-class variation between subjects. The authors conducted experiments on different modalities using 4 datasets.

### Strengths
The main focus of the paper, catastrophic forgetting, is important in machine learning. The subject variability in bio-signals is a big obstacle to the deployment of the ML algorithms in a wide range of bio-signal applications, making the authors' motivations timely and solid. The paper is well-written and easy to follow.

### Weaknesses
This paper focuses on the catastrophic forgetting problem from the inter-subject variability of bio-signals, especially EEG. Therefore, the problem the authors focus on solving is very similar to domain adaptation/generalization. Since domain adaptation /generalization aims to train the models in a way that when the domain (mostly subjects in bio-signals) changes, the model performs well. Although the authors here formulate the problem from the training (multiple subjects/domains during training), I feel like there should be some baseline comparisons with domain adaptation/generalization works [3-4].

The catastrophic forgetting is generally defined as the phenomenon of forgetting previously learned information when trained on new data. And, the model evaluation is performed when it is forced to learn multiple tasks sequentially. In this paper, sequential learning is formulated subject-wise instead of task-wise, which makes the evaluation and comparison controversial as the domain generalization/adaptation tools can also be used for subject-wise sequential learning.

[1] James Kirkpatrick, Overcoming catastrophic forgetting in neural networks, PNAS 2016.

[2] Sara Babkniya, A Data-Free Approach to Mitigate Catastrophic Forgetting in Federated Class Incremental Learning for Vision Tasks, NeurIPS 2023.

I believe that it would strengthen the paper to include a baseline comparison with existing domain adaptation and generalization methods, particularly those applied to bio-signals across different subjects.
Since the proposed approach has similarities with domain adaptation/generalization—aiming for robustness to inter-subject variability—evaluating the method against these baselines could contextualize its unique advantages and potential trade-offs.


[3] Theo Gnassounou, Convolution Monge Mapping Normalization for learning on sleep data. NeurIPS 2023

[4] Yilmazcan Ozyurt, Contrastive Learning for Unsupervised Domain Adaptation of Time Series. ICLR 2023

### Questions
1) Is there any ablation studies performed by the authors regarding the sequence of subjects, similar to the sequence of tasks?

2) Why not focus on domain adaptation or generalization but sequential subject learning? Are there any preliminary experiments showing this approach is superior? The authors can include a brief discussion in the paper comparing their sequential subject learning approach to domain adaptation, highlighting the key differences and potential advantages.

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
3

### Summary
This paper presents a novel method, OPWA, to address the problem of catastrophic forgetting in the presence of inter-subject variability through the use of prototypical networks. The method considers the underlying data distribution of each subject while constructing global prototypes. The aggregation mechanism takes into account intra-class variance and thereby naturally improves the decision boundaries between inter-class prototypes. The experiment results show that the proposed method achieve superior performance in both adaptation and forgetting mitigation across different modalities.

### Strengths
The proposed method can address the problem of catastrophic forgetting in the presence of inter-subject variability through the use of prototypical networks.

The experiment results highlight the superior performance in both adaptation and forgetting mitigation across different modalities.

### Weaknesses
The technical innovation of the paper is questionable. It appears that the paper does not introduce a novel methodology but rather incorporates the prototypical approach into Online Continual Learning, leveraging the derivation of generalized prototypes that represent the entire data distribution to ensure generalizability in the face of cross-subject variability. Although this approach has a slight novelty, it is not substantial.

The experiments are not solid.  As a continual learning study, the paper only conducts a single experiment without multiple repetitions, and does not swap the order of subjects across multiple experiments, making it difficult to exclude the influence of randomness on the results. Statistical tests are lacking to ensure whether the proposed method demonstrates a significant performance improvement over existing methods.

There is a lack of discussion on the computational demands of the framework, which could be significant given the continual adaptation process and may limit its deployment in resource-constrained settings, particularly in a cross-subjects online continual learning setup.

The presentation of the paper still has considerable room for improvement. For instance: There is a formatting error in the title, the introduction to related work is overly lengthy, the sizing of the figures and tables is inappropriate (Table 2 is excessively large, while Figure 3 is too small), and there are issues with the formatting of the titles.

### Questions
Please see Weakness.

### Soundness
2

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
4

### Summary
This paper proposes a method called Online Prototype Weighted Aggregation (OPWA) for online sequential learning, aimed at addressing the issue of cross-subject variability in online continual learning. By introducing a novel prototype-weighted aggregation mechanism, the paper effectively mitigates this challenge.

### Strengths
1.Appropriate solution to the problem: The paper combines cross-subject prototype weighting and momentum-based prototype updating, accounting for dynamic adaptation to distribution shifts and robustness to outliers.
2.Comprehensive validation: The OPWA method was validated on four datasets, demonstrating its applicability across both EEG and ECG data.

### Weaknesses
1.Limited methodological innovation: Cross-subject prototype weighting and momentum-based prototype updating are common techniques. The contribution of this paper lies more in the combination of these methods rather than in any novel algorithmic development.

2.Need for clarification of online learning concepts: Concepts like incremental learning and continual learning are closely related to online learning. It is recommended that the authors provide a more detailed comparison and explanation of these terms in the paper.

3.High model complexity and computational cost: The prototype-weighted aggregation method introduced in the paper incurs additional computational overhead, particularly with the complex distance calculations and weight normalization involved in cross-subject prototype aggregation. It would be helpful if the authors could compare the computational cost of their method with others.

4.Limited experimental coverage: Although the paper includes experiments on several public physiological datasets, the sample size and diversity are limited, especially in terms of the number of subjects, which may not fully validate the generalizability of the method. Additionally, the DEAP and AMIGOS datasets used in the paper rely on subjective self-reported emotional evaluations, which may introduce significant labeling noise.

5.Lack of reproducibility: The code used in the paper has not been made publicly available, hindering reproducibility.

### Questions
Please see Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2
