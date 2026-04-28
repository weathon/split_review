# Guiding Masked Representation Learning to Capture Spatio-Temporal Relationship of Electrocardiogram

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 6, 6, 8

## Abstract
Electrocardiograms (ECG) are widely employed as a diagnostic tool for monitoring electrical signals originating from a heart. Recent machine learning research efforts have focused on the application of screening various diseases using ECG signals. However, adapting to the application of screening disease is challenging in that labeled ECG data are limited. Achieving general representation through self-supervised learning (SSL) is a well-known approach to overcome the scarcity of labeled data; however, a naive application of SSL to ECG data, without considering the spatial-temporal relationships inherent in ECG signals, may yield suboptimal results. In this paper, we introduce ST-MEM (Spatio-Temporal Masked Electrocardiogram Modeling), designed to learn spatio-temporal features by reconstructing masked 12-lead ECG data. ST-MEM outperforms other SSL baseline methods in various experimental settings for arrhythmia classification tasks. Moreover, we demonstrate that ST-MEM is adaptable to various lead combinations. Through quantitative and qualitative analysis, we show a spatio-temporal relationship within ECG data.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work proposes a method called ST-MEM (Spatio-Temporal Masked Electrocardiogram Modeling), 
to leverage self-supervised learning (SSL) in order to train a model that can be used for diagnosis of conditions detectable through Electrocardiograms (ECG). 

ST-MEM is based on a Masked auto-encoder and it uses a vision transformers (ViT) architecture. The 12 leads ECG signal is divided into temporal patches. Some patches are masked and the task is to reconstruct the masked signal. Each encoded patch is then added to a LEAD-specific encoding (a way to identify from which lead the signal is coming from) and to the traditional positional encoding (a way to identify temporary where the patch belongs). Additionally, a special token is appended and postponed to each lead signal. Since some leads share a highly correlated signal the decoder is a Lead-wise shared decoder (i.e. it only attempts to decode the signal from 1 lead at the time, this is to ensure that the task is not trivially solved by copying the masked patched from a highly correlated lead).

After training a labeled dataset can be sued to train a linear layer on top of the encoder, or to fully fine-tuned the model.

The proposed model is pre-trained using a total of 188,480 ECGs 12 leads signals coming from three datasets (Chapman, Ningbo, CODE-15), and if tested using two different datasets PTB-XL and CPSC2018 on the task of detecting cardiac arrhythmia and myocardial infarction. Results (in terms of accuracy, F1 and AUROC) show that with linear fine-tuning, the proposed method performs better than other SSL methods albeit it still underperforms the supervised baseline. When fine-tuning, however, the proposed method surpasses also the supervised baselined in all the metrics employed. 

The current method is also resilient to lower amount of data compared to all alternatives tested as shown by achieving the best results in terms of AUROC using only 1% and 5% of the fine-tuning dataset. 

Additionally, the authors perform experiments using only a sub set of the leads or using only 1 lead (as in the PhysioNet2017 dataset). The proposed technique remains the best  performer across all baselines.

### Strengths
The paper tackles an important problem since high quality ECG labeled data are scarce but ECG data in general is much more available. 

The proposed solution is simple yet very effective as shown in the results, also compared to other SSL alternatives.

### Weaknesses
Some part of the manuscript could be improved. For example:
	Figure 2 (c) is not clear. 
	What is “seasonality”?
	See more clarification to add to the manuscript from my questions below

Some experiments could be stronger. For example PTB XL dataset have 4 different conditions but it seems that only a couple were used in the tests.

Having both the SEP token and the leads embedding seems redundant. Have the authors considered an ablation where only the leads embedding are used but not the SEP? If SEP is needed why is it needed twice and not just at the beginning or just at the end?

Have the author considered using only a subset of the 8 augmentations used for the contrastive SSL baselines shown in Appendix D? Some of them could really alter the signal and be counter productive. For example, the Flip, the shift perhaps also the Sine and partial Sine.

The initial statement “detecting various heart diseases” seem to imply that the proposed technique could do so, however, the tests only show a couple of heart condition. For example in the PTB XL dataset there are 4 different conditions, why not show the results on all of them?

“The patches undergo flattening” why is flattening needed here? Isn’t the signal already flat?

The pre-training dataset comes with different sampling rate (two at 500Hz and 1 at 400Hz). How was this taken care of? Was the 500 subsampled? This should be explained.

Similarly the physionet comes with 200Hz, how was it adapted to the pre-trained model?

For signals that are longer than 10 seconds, I assume the signal was split into 10 seconds but how was all the outcome computed? Average? Voting? This should be clarified.

### Questions
Having both the SEP token and the leads embedding seems redundant. Have the authors considered an ablation where only the leads embedding are used but not the SEP? If SEP is needed why is it needed twice and not just at the beginning or just at the end?

Have the author considered using only a subset of the 8 augmentations used for the contrastive SSL baselines shown in Appendix D? Some of them could really alter the signal and be counter productive. For example, the Flip, the shift perhaps also the Sine and partial Sine.

The initial statement “detecting various heart diseases” seem to imply that the proposed technique could do so, however, the tests only show a couple of heart condition. For example in the PTB XL dataset there are 4 different conditions, why not show the results on all of them?

“The patches undergo flattening” why is flattening needed here? Isn’t the signal already flat?

The pre-training dataset comes with different sampling rate (two at 500Hz and 1 at 400Hz). How was this taken care of? Was the 500 subsampled? This should be explained.

Similarly the physionet comes with 200Hz, how was it adapted to the pre-trained model?

For signals that are longer than 10 seconds, I assume the signal was split into 10 seconds but how was all the outcome computed? Average? Voting? This should be clarified.

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
This paper presents a self-supervised pre-training method for multi-lead ECG data that can be generalized to reduced lead sets. The method relies on spatio-temporal patch reconstruction, with led-wise shared decoders. The experiments were performed by pre-training on three ECG datasets and fine-tuning to two different down-stream ECG datasets/tasks. Results demonstrated the improvement in downstream tasks in comparison to supervised baselines and various unsupervised pre-training methods.

### Strengths
The paper was overall clearly written and easy to follow.

The experimentation was thorough, especially in the inclusion of relevant baselines, and the empirical results speak favorably to the contribution of the work.

The use in low-resource settings is interesting, and the gain brought by proposed pre-training more significant.

### Weaknesses
Despite favorable empirical results, the intuition of the spatiotemporal patching based self-supervised learning is not very clear. It is not clear why such patching will help the learning of spatiotemporal representations. Furthermore, the relation with two baselines — MLAE that reconstructs spatial patches and MTAE that reconstructs temporal patches — need to be better clarified. 

The assumption of the method, in particular to what type of ECG signals and tasks this will apply, needs to be better discussed. For instance, the use of temporal patching seems to rely on the assumption that the rhythm  within the input signal length (e.g., 10s) — whether it is normal or abnormal —is regular and periodic.  Is that true? How would this work for rhythms that are irregular (e.g., atrial fibrillation), or rhythms where the abnormal rhythm only shows up in transient beats within a longer segment (which is typical for some PVCs and tachycardias). If the method is not designed for these scenarios, it should be clearly clarified.  

Related to the above comments, more details about the data and classification tasks needed to be given. What are the labels of rhythms being classified? Does each 10-s segment only has one label? The paper did a good job in highlighting the it’s important to develop methodology to the application problem at hand — this should also be reflected when describing data and experimental settings, as different ECG tasks can mean that the features one are looking for is very different (e.g. is it a regular rhythm, is it an irregular rhythm, is it a transient rhythm, etc).

Overall, while the performance gain is notable, they are also overall limited — at 2 decimal points compared to supervised baselines wen using 100% data. It is not clear what is the clinical significance of such performance gain. Perhaps it is because the supervised baselines are already quite good in the tasks considered (over 0.9 AUROC in both downstream datasets). It may be more convincing if the authors could find “harder” base tasks in order to see if the proposed method will have clinical significance.

### Questions
Please clarify the main questions listed in my above comments. 

In addition, it’d be interesting to see Fig 4, the embedding of the ECG signals, across different rhythm types as well, in order to appreciate the clustering across rhythm types versus spatial locations of the lead.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes ST-MEM (Spatio-Temporal Masked Electrocardiogram Modeling) as an approach to learn a feature representation of ECGs which considered both spatial and temporal aspects of the signal. In particular the authors use a lead-specific decoder to guide the network to learn spatial representation. The author demonstrates the effectiveness of the proposed method on multiple datasets includes PTB-XL, CPSC2018 and Physionet 2017 by comparing to supervised learning baseline, as well as other self-supervised learning methods and get superior results on both general setting and low-resource/reduced lead setting. The author also performs quantitative and qualitative analysis of the captured spatial and temporal relationship, with clustering and attention map respectively.

### Strengths
1. The paper is well-written with clear methodology and clarity in details. The presentation is readily comprehensible.
2. The proposed method has superior performance on important public datasets compared to several other contrastive and generative self-supervised learning methods. The favorable performance of proposed method also extends to practical scenarios of reduced lead and low-resource setting.

### Weaknesses
1. The idea of using MAE to learn representation for ECG signal has been explore previous work(Sawano et al., 2022[1] in the reference). The author should highlight the difference.
2. The experiment session seems missing some previous works. For example, Temesgen et al., 2022[2] also report metrics on PTB-XL and seems to have higher AUROC score.

### Questions
1. In the "PERFORMANCE IN REDUCED LEAD SETTINGS" section, 1-lead part was using lead I. How is the choice being made? Would it be valuable to also report 1-lead performance of other 5 leads?
2. In the same section, all methods seem to have larger 6-lead vs 1-lead gap on PTB-XL than CPSC2018. Does the author have insight on why this is the case?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors propose a simple but effective ECG specific generative self-supervised learning framework utilizing both spatial and temporal characteristics of ECG. The project is straightforward, and well examined.

### Strengths
Althogh it's ECG specific, this work provides two important insights. 1) solution for data domain in which cost of labeling is quite high. 2) The electrocardiogram is an indirect observation of the electrical behavior of a single heart from multiple points on the body surface to begin with, and this approach has potential for application to similar data domains that exist not only in medicine.

### Weaknesses
The problem setting is specialized to the ECG, and the scope might be too narrow for the general audiencs of ICLR.

To claim "general ECG representation", it is quite important what actual task was tested. Could you provide more details of classification of myocardial infarction as well as classification of cardiac arrhythmia, e.g., what are the diagnostic criteria of myocardial infarction? What type of arrhythmia are classified?

The authors tested Lead I for the single lead task. In a clinical setting, Lead II is the first choice in many situations. Did the author evaluate for Lead II as well?

It would be quite important for the general audience of ICLR that the authors discuss possible extension of this approach outside of ECG or the medical field.

Minor point.
In Figure 2, the authors assigned the same color code to two different segmentations. Could you change one of them to the other color code such as grayscale?

### Questions
To claim "general ECG representation", it is quite important what actual task was tested. Could you provide more details of classification of myocardial infarction as well as classification of cardiac arrhythmia, e.g., what are the diagnostic criteria of myocardial infarction? What type of arrhythmia are classified?

The authors tested Lead I for the single lead task. In a clinical setting, Lead II is the first choice in many situations. Did the author evaluate for Lead II as well?

It would be quite important for the general audience of ICLR that the authors discuss possible extension of this approach outside of ECG or the medical field.

Minor point.
In Figure 2, the authors assigned the same color code to two different segmentations. Could you change one of them to the other color code such as grayscale?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good
