# Neuro-Inspired Information-Theoretic Hierarchical Perception for Multimodal Learning

- Decision: Accept
- Scores: 8, 6, 5, 6, 6

## Abstract
Integrating and processing information from various sources or modalities are critical for obtaining a comprehensive and accurate perception of the real world in autonomous systems and cyber-physical systems. Drawing inspiration from neuroscience, we develop the Information-Theoretic Hierarchical Perception (ITHP) model, which utilizes the concept of information bottleneck. Different from most traditional fusion models that incorporate all modalities identically in neural networks, our model designates a prime modality and regards the remaining modalities as detectors in the information pathway, serving to distill the flow of information. Our proposed perception model focuses on constructing an effective and compact information flow by achieving a balance between the minimization of mutual information between the latent state and the input modal state, and the maximization of mutual information between the latent states and the remaining modal states. This approach leads to compact latent state representations that retain relevant information while minimizing redundancy, thereby substantially enhancing the performance of multimodal representation learning. Experimental evaluations on the MUStARD, CMU-MOSI, and CMU-MOSEI datasets demonstrate that our model consistently distills crucial information in multimodal learning scenarios, outperforming state-of-the-art benchmarks. Remarkably, on the CMU-MOSI dataset, ITHP surpasses human-level performance in the multimodal sentiment binary classification task across all evaluation metrics (i.e., Binary Accuracy, F1 Score, Mean Absolute Error, and Pearson Correlation).

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes ITHP, a brain-inspired hierarchical information perception model that fuses information from different modalities. ITHP employs the information bottleneck framework to extract relevant information from different modalities in a hierarchical/sequential manner. Extensive experiments on MUStARD, CMU-MOSI, and CMU-MOSEI demonstrate the effectiveness of ITHP.

### Strengths
- the paper is clear and well-organized.
- the proposed ITHP is intuitive and well-grounded in information theory and provides a novel view of information fusing in multi-modal learning.
- extensive experiments demonstrate the effectiveness of ITHP.

### Weaknesses
- ITHP extracts commonly encoded information from different modalities; however, would this procedure be called "fusion" appropriately?
    - suppose the primary modality is $M_p$ and a secondary modality be $M_1$. ITHP cannot capture information encoded in $M_1$ but not $M_p$. In this sense, ITHP would be an information distillation rather than a fusion method.
    - when talking about "fusion," one expects to integrate information of **different** types.
    - in addition, when both modalities contain similar information, if the one in $M_1$ is noisy, would ITHP be affected? Can ITHP correctly identify the noise in $M_1$ and mainly use the information from $M_p$ instead?
    - as the main idea of ITHP is to distill relevant information from different modalities, the starting point would be important. However, the experiments do not show results with different primary modalities.

### Questions
- how do you choose the primary modality? And how would different choices of primary modality affect the performance of ITHP?
- how would ITHP perform in the presence of noise in some of the modalities (the primary or the secondary ones)?
- how can ITHP accommodate tasks that require combining complementary information from different modalities?

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
- This paper introduces the Information-theoretic Hierarchical Perception (ITHP) model, which aims to integrate and process information from multiple modalities effectively. The authors show inspiring motivation corresponding neuroscience research to a model that designates a prime modality and utilizes the concept of the information bottleneck to construct compact and informative latent states, which enable to balance between preserving relevant information and reducing noise in the latent states.

- This paper tries to justify the validity of design philosophy and the effectiveness of the proposed models experimentally with the performance comparison of two tasks such as (1) sarcasm detection from videos and (2) multimodal sentiment analysis. They seem to show better scores in both tasks. (note that seems not to pursue state-of-the-art performances).

### Strengths
- This paper presents interesting connections between neuroscience and proposed models. It provides good motivations for designing the proposed models.﻿ This integration of neuroscience principles into the design of the models adds a novel perspective to the field of multimodal learning.

- The authors demonstrate the effectiveness with competitive performances of the proposed models in the two tasks.

### Weaknesses
- Even though this paper shows interesting modeling design and experimental results, there is a gap between state-of-the-art methods such as UniMSE and SPECTRA, for example, with respect to performances. What kinds of criteria to choose the model configuration and comparative methods in the paper?

- This paper seems not to present enough information on experimental setting and implementation to achieve reproducibility.

- It lacks justification for the component choices. Which points should be clarified through experiments? Why BERT and DeBERTa are utilized as language models? 


* References

  - UniMSE : G. Hu, et al., UniMSE: Towards Unified Multimodal Sentiment Analysis and Emotion Recognition, EMNLP 2022

  - SPECTRA : T. Yu, et al., Speech-Text Dialog Pre-training for Spoken Dialog Understanding with Explicit Cross-Modal Alignment, ACL 2023


----------------------------------------------------------------------------
Post-rebuttal
----------------------------------------------------------------------------
I read the rebuttal and other reviewers' opinions. 
At first, the rebuttal addresses most of my major concerns and provides convincing information to resolve mine.
I'd like to raise my score from 5 to 6.
Thank you for your good contributions to our community!

### Questions
See the Weaknesses above and answer, please.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors develop a new Information-Theoretic Hierarchical Perception (ITHP) model that designates a prime modality and regards the remaining modalities as detectors in the information pathway, serving to distill the flow of information. The primary modality yields the highest degree of information extraction, with subsequent modalities contributing information in a sequentially ordered manner.  To address the challenge of high dimensionality of multimodal data, they construct "Information bottlenecks." These bottlenecks function as compressed latent representations of the data, with each bottleneck responsible for compressing a single modality while retaining  the relevant information of other modalities. 

The method shows impressive performance on the CMU-MOSI dataset surpassing human-level performance for sentiment analysis.

### Strengths
The fundamental premise of the research paper is interesting. It employs the concept of hierarchical information flow in a multi-modal context which was shown to be useful for downstream tasks like sentiment analysis and sarcasm detection.  

The paper is well written and easy to understand.

### Weaknesses
Comparison with other methods in Table 1 for sarcasm detection is insufficient. The authors need to provide comparison results on either additional datasets [3] or other existing methods in literature [4].  
 
[3] Cai Y, Cai H, Wan X. Multi-modal sarcasm detection in twitter with hierarchical fusion model. InProceedings of the 57th annual meeting of the association for computational linguistics 2019 Jul (pp. 2506-2515). 
 
[4] Wen C, Jia G, Yang J. DIP: Dual Incongruity Perceiving Network for Sarcasm Detection. InProceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition 2023 (pp. 2540-2550). 

The paper is specific to the task sentiment analysis whereas the title and presentation of the paper refers to downstream tasks in multimodal learning as a whole. To support the claim the authors should report the method’s performance on some general tasks like visual question answering.  

The literature survey needs to be updated. They are several recent methods of multimodal fusion and representation learning: 
 
[1] Xue Z, Marculescu R. Dynamic multimodal fusion. InProceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition 2023 (pp. 2574-2583). 

 

 

Missing table 5 and 10 on page 9 which were referred to in text.

### Questions
The authors have established a direct quantitative association between the embedding size of modality X and its corresponding priority order for the task. However, the embedding size can be contingent upon the model's architectural characteristics. Does changing the model which provides the embedding has any effect on the priority order?  

How is embedding size related to the amount of context information present in a modality?  

For experiments in table 1, is there any effect of changing the audio and text priority, when all three of the modalities are present?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a neuro-inspired sequential and hierarchical processing model for multi-modality data. The key is to balance the minimization of mutual information between the latent state and the input modal state, and the maximization of mutual information between the latent states and the remaining modal states. The paper presents the theory formulation of the processing steps and evaluate on two multimodality tasks, sarcasm detection and sentiment analysis.

### Strengths
1.	The paper provided detailed formulation of the perception process and deduction of the loss function.
2.	The paper conducted detailed experiments on the ablation of hyperparameters.

### Weaknesses
1.	The inspiration from neuroscience research seems simple, and unnecessary to the main processing pipeline of the main work, making the main work distracting.
2.	The order of the modality in processing the data seems quite important, which highly impacts the performance. For such an importance factor, it is better to provide further theoretical analysis or practical guidance on it.
3.	The paper should include some recent SOTA works, at lease works in 2022, on comparing the sentiment analysis.

### Questions
1.	Why sequential processing is good? Except for inspiration from neural inspirations. This operation introduces the extra problem of the order of modality. 
2.	Does the best beta and gamma share across different tasks? Or it is needed to balance for different tasks, making this method quite cumbersome.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes an Information-Theoretic Hierarchical Perception (ITHP) model, based on the concept of information bottleneck, for effective multimodal fusion.

### Strengths
+ The proposed Information-Theoretic Hierarchical Perception model looks novel to me; This stands in contrast to mainstream multimodal fusion where different modalities are treated equally, and the final prediction is usually acquired by concatenating the features from each modality. The concept of designating a prime modality and using the other modalities to guide the flow of information looks interesting, and makes sense to me --- In many multimodal tasks, modalities do not contribute equally to the final prediction.

+ The experimental results are strong. The analysis about varying Lagrange multiplier in Sec. 3.1 provides good insight.

+ Many design choices (e.g. latent state size, order of modalities) are thoroughly evaluated in the appendix.

### Weaknesses
+ As the authors already point out in Section 5, the proposed approach requires a predefined order of modalities, which could be a problem when there are > 3 modalities and we do not have prior information about the multimodal task.

+ Would the proposed hierarchical architecture introduce some inference latency compared with the standard non-hierarchical approaches (Take Figure 3 as an example, say compared to concatenation of $X_0$, $X_1$ and $X_2$ and then passed to an MLP head)?

+ It seems in the current framework, feature extraction from raw video, audio & text & the proposed ITHP are separate (first feature extraction then use the encoded features in the hierarchical information flow). The temporal nature of these data is not utilized. I wonder if the authors could briefly comment on the potential of extending the ITHP model to handle sequence data (that naturally comes with a temporal order).

### Questions
See weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
