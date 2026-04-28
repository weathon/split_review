# EEGMamba: Bidirectional State Space Model with Mixture of Experts for EEG Multi-task Classification

- Decision: Reject
- Avg Score: 4.60
- Scores: 6, 6, 3, 5, 3

## Abstract
In recent years, with the development of deep learning, electroencephalogram (EEG) classification networks have achieved certain progress. Transformer-based models can perform well in capturing long-term dependencies in EEG signals. However, their quadratic computational complexity poses a substantial computational challenge. Moreover, most EEG classification models are only suitable for single tasks and struggle with generalization across different tasks, particularly when faced with variations in signal length and channel count. In this paper, we introduce EEGMamba, the first universal EEG classification network to truly implement multi-task learning for EEG applications. EEGMamba seamlessly integrates the Spatio-Temporal-Adaptive (ST-Adaptive) module, bidirectional Mamba, and Mixture of Experts (MoE) into a unified framework. The proposed ST-Adaptive module performs unified feature extraction on EEG signals of different lengths and channel counts through spatial-adaptive convolution and incorporates a class token to achieve temporal-adaptability. Moreover, we design a bidirectional Mamba particularly suitable for EEG signals for further feature extraction, balancing high accuracy, fast inference speed, and efficient memory-usage in processing long EEG signals. To enhance the processing of EEG data across multiple tasks, we introduce task-aware MoE with a universal expert, effectively capturing both differences and commonalities among EEG data from different tasks. We evaluate our model on eight publicly available EEG datasets, and the experimental results demonstrate its superior performance in four types of tasks: seizure detection, emotion recognition, sleep stage classification, and motor imagery. The code is set to be released soon.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents EEGMamba, a model tailored for multi-task EEG classification. It aims to overcome the limitations of existing models in terms of computational complexity and generalization across tasks with varying signal lengths and channel counts. EEGMamba integrates three main innovations: the Spatio-Temporal-Adaptive (ST-Adaptive) module for unified feature extraction, Bidirectional Mamba to balance accuracy and computational efficiency, and a Task-aware Mixture of Experts (MoE) to handle the differences and similarities across EEG tasks. Evaluated across eight public datasets and covering seizure detection, emotion recognition, sleep stage classification, and motor imagery, EEGMamba demonstrates strong performance and adaptability.

### Strengths
EEGMamba achieves state-of-the-art performance across multiple EEG tasks, demonstrating robust multi-task capability. Its bidirectional Mamba blocks enable efficient handling of long sequences, avoiding the high memory demands of Transformer models. The flexible ST-Adaptive module supports EEG signals of varied lengths and channels, and the task-aware Mixture of Experts (MoE) enhances task-specific accuracy, reducing interference across tasks. This adaptability and strong generalization across datasets position EEGMamba as a versatile model for EEG classification.

### Weaknesses
EEGMamba’s evaluation lacks comparison the newest baseline models (notably LaBRaM from ICLR 2024), which limits the interpretability of its reported gains. The Spatio-Temporal-Adaptive (ST-Adaptive) module, while flexible for varying signal lengths and channel counts, may not adequately capture complex channel-time dependencies crucial in EEG data. Furthermore, training the ST module on a per-task basis could lead to representations that are too specialized, reducing generalizability, particularly for out-of-distribution (OOD) tasks, which were not included in the study. Additionally, the paper lacks a related works section detailing prior applications of SSMs or Mamba in EEG classification, making it difficult to contextualize EEGMamba’s specific advancements in this space. The evaluation also does not explore the performance of EEGMamba on longer EEG contexts, which is a key area where Mamba models are expected to excel.

### Questions
Could you elaborate on the choice of baseline models? How does EEGMamba’s performance compare with multi-task EEG models specifically designed for generalization across diverse tasks?

How does the ST-Adaptive module capture interactions between channels and temporal features, which are critical in EEG data? Have you considered modeling these dependencies more explicitly?

How would EEGMamba perform on out-of-distribution tasks or tasks not seen during training? Have you tested its ability to generalize to entirely new EEG task types?

Could you clarify how this work builds on or differs from previous applications of SSMs or Mamba models in EEG classification? Adding this context could help readers better understand the specific contributions of EEGMamba.

Can you evaluate this on longer contexts to better get a sense for the necessity and usefulness for Mamba?

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
The paper introduces EEGMamba, a novel EEG classification network designed for multitask learning. It integrates spatiotemporal adaptive (ST-Adaptive) modules, bidirectional Mamba, and a mixture of experts (MoE) approach. This addresses challenges in EEG classification, such as computational complexity and variations in signal length and channels. The model efficiently handles long sequences and adapts to feature extraction while capturing both task-specific and general features. Evaluations on multiple public EEG datasets demonstrate that EEGMamba outperforms existing models in seizure detection, emotion recognition, sleep quality, and emotion recovery.

### Strengths
### **Originality**
The originality of EEGMamba lies in its novel approach to EEG classification through the integration of bidirectional Mamba, Spatio-Temporal-Adaptive (ST-Adaptive) modules, and task-aware Mixture of Experts (MoE). The innovative combination of these elements addresses the computational complexity and variability in signal length and channels, which are critical challenges in EEG classification. This creativity, particularly in applying multitask learning to EEG signals, represents a significant advancement in the field.

### **Quality**
The quality of this work is demonstrated through rigorous evaluations on multiple publicly available EEG datasets. EEGMamba's superior performance in seizure detection, emotion recognition, sleep quality, and emotion recovery highlights its robustness and effectiveness. The model's ability to handle long sequences and adapt to different feature extraction tasks while maintaining high accuracy and fast inference speed.

### **Clarity**
The authors provide a detailed description of the EEGMamba architecture and its components. The step-by-step explanation of how the bidirectional Mamba, ST-Adaptive module, and task-aware MoE are integrated and function together contributes to a well-structured and coherent narrative.

### **Significance**
The model's design, which allows for the efficient capture of both task-specific and general features, has the potential to transform how EEG data is processed and analyzed. This can lead to more accurate and comprehensive analyses of complex brain signal data, benefiting various applications such as medical diagnostics and cognitive research.

### Weaknesses
 Overall, the experiments in this paper are comprehensive; however, in Section 4.1, the discussion on single-channel and multi-channel models only compares memory usage and inference speed, without evaluating the impact of multi-channel models on performance metrics. Additionally, the t-SNE visualization lacks layer-by-layer analysis of the model's influence on clustering results, which does not adequately demonstrate the feature extraction capability of each layer. It is recommended to visualize feature clustering by module.

### Questions
In Section 4.2's experimental comparison, was the model trained using all the datasets at once? Could there be interactions between the datasets? Would training the model on each dataset separately improve the performance metrics? Have you conducted any experiments on this? I'm quite interested.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper "EEGMAMBA: Bidirectional State Space Model with Mixture of Experts for EEG Multi-Task Classification" presents EEGMamba, a multi-task learning framework for EEG classification tasks, addressing challenges related to signal length and channel variability. EEGMamba integrates a Spatio-Temporal-Adaptive (ST-Adaptive) module, bidirectional Mamba blocks, and a task-aware Mixture of Experts (MoE) to enhance adaptability and task-specific processing across diverse EEG datasets. The ST-Adaptive module standardizes data of various lengths and channel numbers, while the bidirectional Mamba captures temporal dependencies in EEG sequences, and the task-aware MoE module selects experts based on task, enhancing classification accuracy and generalization. Tested on eight datasets spanning four task types (seizure detection, emotion recognition, sleep stage classification, and motor imagery), EEGMamba achieves state-of-the-art results, demonstrating superior efficiency, memory usage, and accuracy across tasks.

### Strengths
EEGMamba achieves superior memory efficiency and faster inference speed than traditional transformer-based models, especially on longer EEG sequences, thus proving its practical value. 

The proposed model demonstrates an approach to handling EEG data of varying lengths and channels, incorporating a class token for temporal adaptability and a task-aware MoE to distinguish task-specific features.

### Weaknesses
1. Limited Contribution: The author claims that EEGmamba is the first universal EEG classification network to effectively implement multi-task learning for EEG applications. However, several established methods are available that can be applied to multi-task EEG learning, as cited in [1][2][3].

2. Inappropriate Comparisons: The choice of baselines for comparison lacks relevance. For instance, using AttnSleep [4] as a baseline for seizure detection/emotion recognition is incongruous, as it is specifically designed for sleep staging. Additionally, the author does not include multi-task learning methods as baselines, instead comparing against smaller models tailored to individual tasks. For fair assessment, each specific task should be compared to the most relevant model designed for that purpose. To evaluate cross-task capabilities, comparisons should involve multi-task learning methods like those in [1][2][3][5][6].

3. Efficiency Evaluation: The author should provide quantitative evidence demonstrating the proposed method's efficiency advantages over previous approaches.

### Questions
Plz go and check weakness

### Soundness
2

### Presentation
3

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
The authors introduce EEGMamba, a model designed for multi-task EEG classification. EEGMamba consists of an ST-Adaptive module that learns spatial filters for each task, transforming EEG inputs with varying channel counts into a uniform feature space. The module then tokenizes the data using both small and large kernels to capture short-term and long-term features. These tokens are processed by a BiMamba backbone with task-aware Mixture of Experts (MoE) layers, enabling the model to capture both task-specific and shared features. Finally, each task has a dedicated classification head.

EEGMamba allows for multi-task EEG classification in a single training session. The authors evaluated the model’s performance against five other models across eight public datasets, covering tasks such as epilepsy detection, sleep stage classification, emotion recognition, and motor imagery. The experiments used a 5-fold cross-validation approach, where specific subjects were reserved for the test set in each fold. Results show that EEGMamba outperformed competing models under this evaluation, and it demonstrated efficient memory usage and inference speed, particularly with long-sequence data.

### Strengths
1. The authors successfully introduce the new Mamba architecture to EEG decoding, achieving strong results across 8 public datasets.

2. Mamba demonstrates memory efficiency and fast inference, making it advantageous for real-world applications.

3. The model effectively addresses the multi-task classification problem, showcasing the feasibility of training a single model for multiple downstream tasks.

### Weaknesses
1. The motivation for multi-task training is somewhat unclear. The authors should clarify why multi-task training is necessary and how it can be beneficial for specific applications.

2. Certain questions remain unanswered regarding the practical use of the proposed model, which limits its potential impact. For instance, under the current evaluation scheme, it is unclear how the model would generalize to new datasets or subjects, particularly when new datasets vary in channel count. Does introducing a new dataset require retraining or additional multi-

task training even if it is single-task? Additionally, what would be the training strategy for developing a subject-dependent model within the multi-task framework if only one task is available from the subject? To address this, the authors could consider testing the model on an additional dataset to evaluate whether the pre-trained model can transfer effectively. If it cannot, are there still advantages to the EEGMamba multi-task approach?

3. The authors should discuss the relatively low classification accuracy on the motor imagery datasets, which is currently too low for practical motor imagery classification. If this is due to the evaluation setting, additional experiments with per-subject models should be conducted to assess performance, and these results should be compared to other models.

4. Statistical tests are needed to confirm whether the observed differences between models or modules are significant. For instance, statistical analysis should be conducted for the results in Figure 1 comparing EEGMamba and Single-task EEGMamba, as well as for the different ablation models in Figure 6.

### questions:
 1. Introduction: (line 49-50):

The authors claim that CNNs are unable to handle long EEG signals, citing three papers: (Sakhavi etal.,2018), (Thuwajit etal.,2021) and (Schirrmeister etal.,2017). However, none of these studies provide evidence to support such a conclusion. In fact, Thuwajit et al. (2021) proposed EEGWavenet, which utilizes a multiscale CNN-based spatiotemporal feature extraction module. This module gradually increases its receptive field to match the length of the input EEG signal, indicating that CNNs can handle the global input sequences in certain contexts. While the authors' claim is not entirely substantiated, it raises interesting questions that I would like to see addressed:

a. For EEG classification, what defines a "long" signal in terms of sample size? At what point does a short receptive field cause CNN performance to degrade?

b. Is global sequence modelling truly necessary for long-term EEG signals? From a neuroscience perspective, how much does brain activity from, say, 10 seconds ago, affect the current state? Which types of tasks specifically require such long-term modelling?

2. section 2.2 ST-Adaptive Module:

The authors propose a spatio-temporal-adaptive module that transforms arbitrary EEG inputs into a uniform feature dimension, as depicted in Figure 3. However, I have several concerns:

a. Scalability to New Datasets: Is this approach scalable to new datasets once the model is trained? Given that different Conv1d layers are used to transform varying numbers of EEG channels into a common hidden state in the Spatial-Adaptive Convolution, how flexible is this method for new tasks where the number of channels may differ from the training datasets? Even if the number of channels is the same, the channels themselves vary. It appears that the model learns dataset-specific spatial filters rather than a truly global spatial representation, which may limit its generalizability to new datasets, which is a big issue for a backbone model, since people would like to use it on different tasks later on.

b. Tokenize Layer: In the tokenize layer, two branches of CNN are used: one with a short kernel (15) and another with a long kernel (49). Was this choice based on experimental results? Why are there only two branches, and why were kernel sizes 15 and 49 specifically chosen? Since there’s no discussion of this configuration in the ablation study, it’s unclear whether this is the most optimal setup.

3. section 3.2 Data Division:

In this study, the 5-fold cross-validation experiment was implemented as leave-subject-out, which is not a common approach in the BCI field due to the significant subject variability. This evaluation approach faces two challenges: (1) developing a population model trained on a group of subjects, and (2) addressing subject transfer by evaluating the model on unseen subjects. This raises several concerns:

a. Subject Variability Impact: In tasks with minimal subject variability, such as seizure detection and sleep stage detection, the classification results are high, as shown in Figure 1. However, tasks like motor imagery and other BCI tasks exhibit high subject variability, which severely impacts model performance. This is evident in the low accuracies achieved on the BCI-IV-2a task (44%) and the SEED task (57.2%), which are insufficient for practical BCI applications. A discussion on this performance discrepancy is necessary to demonstrate how the proposed model addresses these challenges and whether it shows superiority in domains with high subject variability.

b. Performance Discrepancy with Benchmark Models: Many benchmark models, such as EEG Conformer (Song et al., 2022), were not designed to handle population transfer. EEG Conformer, for instance, was trained in a subject-specific manner and achieved state-of-the-art performance on the same BCI-IV-2a (78.66%) and SEED (95.30%) datasets. However, in this study, the EEG Conformer’s performance dropped significantly to 35.2% and below 50%, respectively. Could the authors explain this stark performance difference? Is it primarily due to the leave-subject-out evaluation setting? If so, would the proposed EEGMamba model also retain its high performance if evaluated in a subject-specific manner like EEG Conformer?

c. Use of Separate Test Sets: Datasets like BCI-IV-2a include a separate test set specifically intended for evaluation. In this study, it is unclear whether the authors utilized this test set. Since many studies report performance on this designated test set, comparing the classification accuracy reported here with those from other studies may not be straightforward. Clarification on whether the official test set was used, or if an alternative test split was applied, is needed to ensure a fair comparison with prior work.

4. section 4.1 Single-Task EEGMamba Performance Comparison

Line 377: The authors mention the memory and inference time challenges of transformer models when handling long sequences. Similar to my previous concern, what qualifies as a "long" sequence in terms of signal length for transformers to encounter this bottleneck? Is there a real-world application where such long sequences need to be tackled? Many EEG tasks are only a few seconds in length, so it would be helpful to clarify the practical need for handling significantly longer sequences.

5. section 4.2 EEGMamba for EEG Multi-Task Classification

While the idea of training a single model to perform well across multiple datasets is interesting, its practical application is unclear. From Figure 1, the single-task models appear to achieve similar or even better performance on 5 out of the 8 benchmarked datasets (Siena, BCI-IV-2a, Shu, SEED, CHB-MIT). This raises a few questions:

a. Benefit of Multi-Task Training: Is there a demonstrable benefit to multi-task training? Specifically, is there any statistical difference between the performance of the single-task model and the multi-task model on the datasets? It would be helpful to clarify whether multi-task training consistently improves performance or if its benefits are marginal.

6. Lines 454-456:

The authors argue that the model only needs to be trained once. However, the analysis was performed offline on 8 selected public datasets solely. To assess whether this model can be applied in real-world scenarios, the following questions need to be addressed:

a. Cross-Session Issues: In practice, many EEG-based applications require short calibration sessions to adjust for cross-session variability in subject-dependent models. Does the proposed model also require such calibration? If calibration is needed, would this involve further training or fine-tuning of the pre-trained model? In the case of the multi-task model, would calibration require data from other tasks as well, or could it be done independently?

b. Generalization to New Datasets: How well does the model perform on a new dataset that belongs to one of the pre-trained tasks? If the model only needs to be trained once, does this mean it can be directly applied to similar tasks without additional training? For example, how would the model handle BCI-IV-2B, which has only 3 channels but is still a motor imagery task, or another sleep stage classification dataset? If yes, how would the model manage inconsistencies in the number of channels, and what performance can be expected? If not, wouldn’t this imply that researchers would still need to retrain the model, making it not different from other models?

b. Domain-Specific Advantages: If multi-task training is advantageous, is this benefit domain-specific? For example, should a researcher developing a motor imagery decoder expect better results from multi-task training? How can researchers determine whether a single-task or multi-task approach will yield better performance for a specific domain or task?

c. Practicality of Multi-Task Training: In practice, most researchers focus on specific tasks and experiments, collecting data for single tasks. Does this multi-task approach suggest that researchers in the future should also record additional tasks or rely on public datasets to improve performance? Or is there a scenario where it would make sense for a model to simultaneously classify motor imagery, emotion, sleep stages, and seizure events? More guidance on when and why to use multi-task training would be valuable.

7. section 4.4 Ablation Study:

In Figure 6, it appears that the performances of the different configurations, except for the single-directional Mamba, are quite similar. Is there a statistically significant difference between these configurations? It would be helpful to include a discussion on whether the variations in performance are meaningful or simply within the margin of error.

8. Conclusion lines 526-527:

The authors claim that EEGMamba is the first model to truly implement multi-task learning for EEG applications. However, I am curious about how EEGMamba differs from a simpler approach, such as using a shared backbone model as a feature extractor with separate classification heads for different tasks, as done in [1]. Could the authors clarify the key differences between the proposed model and such an approach using MoE?

[1] Xie Y, Wang K, Meng J, Yue J, Meng L, Yi W, Jung TP, Xu M, Ming D. Cross-dataset transfer learning for motor imagery signal classification via multi-task learning and pre-training. J Neural Eng. 2023 Oct 20;20(5). doi: 10.1088/1741-2552/acfe9c. PMID: 37774694.

9. Conclusion line 531:

The authors claim that the proposed model can better learn the commonalities among EEG signals from different tasks. However, what specific commonalities are being referred to? Is there any interpretation or evidence to support this claim? It would be helpful to understand how these commonalities are identified and whether the model offers any insight into them.

Addressing the above questions could help clarify specific weaknesses and improve the overall impact of the study, more specifically:

Question 5: Answering this question would clarify Weakness Point 1, providing more insight into the motivation for multi-task training.

Questions 1, 2(a), and 6: Answering these would address Weakness Points 2 and 3, which would significantly enhance the study's potential impact and score by clarifying practical applications and the model’s performance on motor imagery datasets.

Questions 4 and 7: These would address Weakness Point 4 by supporting the comparisons with a statistical validation.

### Questions
1. Introduction: (line 49-50):

The authors claim that CNNs are unable to handle long EEG signals, citing three papers: (Sakhavi etal.,2018), (Thuwajit etal.,2021) and (Schirrmeister etal.,2017). However, none of these studies provide evidence to support such a conclusion. In fact, Thuwajit et al. (2021) proposed EEGWavenet, which utilizes a multiscale CNN-based spatiotemporal feature extraction module. This module gradually increases its receptive field to match the length of the input EEG signal, indicating that CNNs can handle the global input sequences in certain contexts. While the authors' claim is not entirely substantiated, it raises interesting questions that I would like to see addressed:

a. For EEG classification, what defines a "long" signal in terms of sample size? At what point does a short receptive field cause CNN performance to degrade?

b. Is global sequence modelling truly necessary for long-term EEG signals? From a neuroscience perspective, how much does brain activity from, say, 10 seconds ago, affect the current state? Which types of tasks specifically require such long-term modelling?

2. section 2.2 ST-Adaptive Module:

The authors propose a spatio-temporal-adaptive module that transforms arbitrary EEG inputs into a uniform feature dimension, as depicted in Figure 3. However, I have several concerns:

a. Scalability to New Datasets: Is this approach scalable to new datasets once the model is trained? Given that different Conv1d layers are used to transform varying numbers of EEG channels into a common hidden state in the Spatial-Adaptive Convolution, how flexible is this method for new tasks where the number of channels may differ from the training datasets? Even if the number of channels is the same, the channels themselves vary. It appears that the model learns dataset-specific spatial filters rather than a truly global spatial representation, which may limit its generalizability to new datasets, which is a big issue for a backbone model, since people would like to use it on different tasks later on.

b. Tokenize Layer: In the tokenize layer, two branches of CNN are used: one with a short kernel (15) and another with a long kernel (49). Was this choice based on experimental results? Why are there only two branches, and why were kernel sizes 15 and 49 specifically chosen? Since there’s no discussion of this configuration in the ablation study, it’s unclear whether this is the most optimal setup.

3. section 3.2 Data Division:

In this study, the 5-fold cross-validation experiment was implemented as leave-subject-out, which is not a common approach in the BCI field due to the significant subject variability. This evaluation approach faces two challenges: (1) developing a population model trained on a group of subjects, and (2) addressing subject transfer by evaluating the model on unseen subjects. This raises several concerns:

a. Subject Variability Impact: In tasks with minimal subject variability, such as seizure detection and sleep stage detection, the classification results are high, as shown in Figure 1. However, tasks like motor imagery and other BCI tasks exhibit high subject variability, which severely impacts model performance. This is evident in the low accuracies achieved on the BCI-IV-2a task (44%) and the SEED task (57.2%), which are insufficient for practical BCI applications. A discussion on this performance discrepancy is necessary to demonstrate how the proposed model addresses these challenges and whether it shows superiority in domains with high subject variability.

b. Performance Discrepancy with Benchmark Models: Many benchmark models, such as EEG Conformer (Song et al., 2022), were not designed to handle population transfer. EEG Conformer, for instance, was trained in a subject-specific manner and achieved state-of-the-art performance on the same BCI-IV-2a (78.66%) and SEED (95.30%) datasets. However, in this study, the EEG Conformer’s performance dropped significantly to 35.2% and below 50%, respectively. Could the authors explain this stark performance difference? Is it primarily due to the leave-subject-out evaluation setting? If so, would the proposed EEGMamba model also retain its high performance if evaluated in a subject-specific manner like EEG Conformer?

c. Use of Separate Test Sets: Datasets like BCI-IV-2a include a separate test set specifically intended for evaluation. In this study, it is unclear whether the authors utilized this test set. Since many studies report performance on this designated test set, comparing the classification accuracy reported here with those from other studies may not be straightforward. Clarification on whether the official test set was used, or if an alternative test split was applied, is needed to ensure a fair comparison with prior work.

4. section 4.1 Single-Task EEGMamba Performance Comparison

Line 377: The authors mention the memory and inference time challenges of transformer models when handling long sequences. Similar to my previous concern, what qualifies as a "long" sequence in terms of signal length for transformers to encounter this bottleneck? Is there a real-world application where such long sequences need to be tackled? Many EEG tasks are only a few seconds in length, so it would be helpful to clarify the practical need for handling significantly longer sequences.

5. section 4.2 EEGMamba for EEG Multi-Task Classification

While the idea of training a single model to perform well across multiple datasets is interesting, its practical application is unclear. From Figure 1, the single-task models appear to achieve similar or even better performance on 5 out of the 8 benchmarked datasets (Siena, BCI-IV-2a, Shu, SEED, CHB-MIT). This raises a few questions:

a. Benefit of Multi-Task Training: Is there a demonstrable benefit to multi-task training? Specifically, is there any statistical difference between the performance of the single-task model and the multi-task model on the datasets? It would be helpful to clarify whether multi-task training consistently improves performance or if its benefits are marginal.

6. Lines 454-456:

The authors argue that the model only needs to be trained once. However, the analysis was performed offline on 8 selected public datasets solely. To assess whether this model can be applied in real-world scenarios, the following questions need to be addressed:

a. Cross-Session Issues: In practice, many EEG-based applications require short calibration sessions to adjust for cross-session variability in subject-dependent models. Does the proposed model also require such calibration? If calibration is needed, would this involve further training or fine-tuning of the pre-trained model? In the case of the multi-task model, would calibration require data from other tasks as well, or could it be done independently?

b. Generalization to New Datasets: How well does the model perform on a new dataset that belongs to one of the pre-trained tasks? If the model only needs to be trained once, does this mean it can be directly applied to similar tasks without additional training? For example, how would the model handle BCI-IV-2B, which has only 3 channels but is still a motor imagery task, or another sleep stage classification dataset? If yes, how would the model manage inconsistencies in the number of channels, and what performance can be expected? If not, wouldn’t this imply that researchers would still need to retrain the model, making it not different from other models?

b. Domain-Specific Advantages: If multi-task training is advantageous, is this benefit domain-specific? For example, should a researcher developing a motor imagery decoder expect better results from multi-task training? How can researchers determine whether a single-task or multi-task approach will yield better performance for a specific domain or task?

c. Practicality of Multi-Task Training: In practice, most researchers focus on specific tasks and experiments, collecting data for single tasks. Does this multi-task approach suggest that researchers in the future should also record additional tasks or rely on public datasets to improve performance? Or is there a scenario where it would make sense for a model to simultaneously classify motor imagery, emotion, sleep stages, and seizure events? More guidance on when and why to use multi-task training would be valuable.

7. section 4.4 Ablation Study:

In Figure 6, it appears that the performances of the different configurations, except for the single-directional Mamba, are quite similar. Is there a statistically significant difference between these configurations? It would be helpful to include a discussion on whether the variations in performance are meaningful or simply within the margin of error.

8. Conclusion lines 526-527:

The authors claim that EEGMamba is the first model to truly implement multi-task learning for EEG applications. However, I am curious about how EEGMamba differs from a simpler approach, such as using a shared backbone model as a feature extractor with separate classification heads for different tasks, as done in [1]. Could the authors clarify the key differences between the proposed model and such an approach using MoE?

[1] Xie Y, Wang K, Meng J, Yue J, Meng L, Yi W, Jung TP, Xu M, Ming D. Cross-dataset transfer learning for motor imagery signal classification via multi-task learning and pre-training. J Neural Eng. 2023 Oct 20;20(5). doi: 10.1088/1741-2552/acfe9c. PMID: 37774694.

9. Conclusion line 531:

The authors claim that the proposed model can better learn the commonalities among EEG signals from different tasks. However, what specific commonalities are being referred to? Is there any interpretation or evidence to support this claim? It would be helpful to understand how these commonalities are identified and whether the model offers any insight into them.

Addressing the above questions could help clarify specific weaknesses and improve the overall impact of the study, more specifically:

Question 5: Answering this question would clarify Weakness Point 1, providing more insight into the motivation for multi-task training.

Questions 1, 2(a), and 6: Answering these would address Weakness Points 2 and 3, which would significantly enhance the study's potential impact and score by clarifying practical applications and the model’s performance on motor imagery datasets.

Questions 4 and 7: These would address Weakness Point 4 by supporting the comparisons with a statistical validation.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
To address the issues of quadratic computational complexity in handling long-term dependencies in EEG classification models, and the lack of cross-task generalization as most models are designed for single tasks, this paper proposes the EEGMamba model. The model introduces the ST-Adaptive module to address the problem of varying EEG signal lengths and channel numbers across different datasets. It also proposes the Bidirectional Mamba to improve computational efficiency and incorporates the MoE (Mixture of Experts) module to simultaneously capture both the commonalities and differences in EEG signals. Relevant experiments were conducted on eight datasets across four EEG tasks.

### Strengths
This paper presents a novel multi-task EEG classification model that incorporates the Bidirectional Mamba and MoE modules, offering a structurally innovative approach. Experiments were conducted on eight datasets, covering a wide range of downstream EEG tasks. The paper is clearly written and easy to follow, with a particularly well-explained method section.

### Weaknesses
This paper proposes a multi-task EEG classification model aimed at performing classification across multiple datasets (downstream tasks) using a single model. However, the experimental results do not demonstrate a clear advantage over other single-task models, making it difficult to convincingly argue for the benefits and necessity of the multi-task approach. Additionally, the ablation study results for the various modules lack significant and consistent differences, making it challenging to prove the effectiveness of each module. Moreover, the motivation for using the Bidirectional Mamba is insufficiently justified. The ST-Adaptive method, proposed to address the issue of varying EEG channel numbers across datasets, is essentially a module integration, lacking in innovation.
1. In this work, the ST-Adaptive module applies a different one-dimensional convolution for each task, transforming the varying original channel numbers into a fixed number of $D$ channels. However, this approach does not seem to fully achieve the concept of being "adaptive." If a new task emerges with a number of channels outside the predefined range of $C_0$ to $C_N$ in the model, how would this be addressed? This raises concerns about the generalizability and flexibility of the current method in handling unforeseen tasks with different channel configurations.
2. The purpose of using Mamba in this paper is to reduce computational complexity, conserve resources, and improve efficiency. Generally, the ultimate goal of improving efficiency in EEG models is to achieve real-time recognition. Given that EEG signals, like natural language, possess temporal characteristics, theoretically, a unidirectional Mamba would better meet this requirement, as it only requires past data rather than future information. The motivation for employing Mamba, especially Bidirectional Mamba, in this work is not sufficiently clear or logically aligned with this objective. The authors should clarify why bidirectional processing is necessary, given that real-time EEG analysis typically requires causal processing.
3. In Section 4.1, the authors present the performance of the single-task EEGMamba and other transformer-based models concerning memory usage and inference speed as the sequence length increases. However, it is not clearly evident from Figure 4 that EEGMamba demonstrates a significant advantage over the other methods. Additionally, while it is acknowledged that memory usage increases and inference speed decreases with longer sequence lengths for both single-channel and multi-channel scenarios, the authors do not specify the actual sequence lengths employed in the current eight EEG tasks. This omission lacks a reference point, making it difficult to ascertain whether EEGMamba exhibits superior performance. Furthermore, as indicated in Appendix I, EEGNet appears to perform better in terms of memory usage and inference speed, while also demonstrating commendable performance across various datasets. This further undermines the effectiveness of the proposed method in this paper. The authors should provide a more detailed comparison, including specific sequence lengths used in each task and a more thorough analysis of why EEGMamba outperforms EEGNet in relevant scenarios.
4. In Section 4.2, the authors present the performance of EEGMamba in multi-task classification. However, I observe that EEGMamba does not demonstrate a significant advantage over the baseline models, and in many datasets, its performance is inferior to that of other single-task models, indicating that the multi-task approach does not facilitate mutual enhancement among tasks. Therefore, I question the necessity of employing a single model to address multiple tasks rather than utilizing several smaller models for different tasks, which might yield better results. The existing findings lack persuasiveness and do not adequately support the motivations for this work or the claims regarding the strong generalization capabilities of the proposed multi-task model. The authors need to provide a more compelling argument for the benefits of multi-task learning in this specific context, especially given the observed performance discrepancies.
5. Regarding Figure 5, I observe that, apart from the sleep stage task, where there is a considerable variation in the activation probabilities of different experts, the activation probabilities for the other tasks across the eight experts are generally quite uniform. This uniformity makes it challenging to demonstrate a particular preference for any specific expert. How can the effectiveness and necessity of the MoE approach be substantiated under these circumstances? The authors should provide a more detailed analysis of the expert activation patterns and explain why the observed uniformity does not undermine the MoE module's effectiveness.
6. Figure 6 presents the ablation study results for the various modules of EEGMamba. However, the data indicate that these modules appear to have minimal discernible impact, as the experimental results across the Siena, CHB-MIT, and SHHS datasets show little variation. This raises concerns regarding the ability to substantiate the effectiveness of each module. The authors should provide a more rigorous ablation study with more diverse datasets and metrics to demonstrate the contribution of each module more convincingly.

### Questions
1. Could you please specify how the EEG tasks are encoded into task tokens?
2. I noticed that the DEAP dataset was utilized in this study, but only data from four electrodes were selected. What is the rationale behind this choice? Additionally, regarding the binary classification on the DEAP dataset, does it pertain to valence, arousal, liking, or dominance? Furthermore, in Table 1, the authors provide the optimal segment lengths for all datasets. What references were used to determine these durations? I observed that, unlike most existing works that employ shorter segments of 1s, 2s, or 4s for the DEAP and SEED datasets, this paper utilizes segment lengths of 60s and 20s. What is the reasoning for selecting such unusually long data lengths?
3. This work employs five-fold cross-validation for data partitioning, which does not appear to be a commonly used EEG dataset partitioning method. What is the rationale or basis for this choice?

### Soundness
2

### Presentation
3

### Contribution
2
