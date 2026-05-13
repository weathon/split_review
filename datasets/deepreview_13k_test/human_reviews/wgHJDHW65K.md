# Representational Knowledge Distillation Across Wearable Biosignals

- Decision: Reject
- Scores: 8, 8, 3, 6, 3

## Abstract
Modern wearable devices can conveniently and continuously record various biosignals in the many different environments of daily living, ultimately enabling a rich view of individual health. 
However, not all biosignals are the same: high-fidelity measurements, such as photoplethysmography (PPG), contain more physiological information, but require optical sensors with a high power footprint. In a resource-constrained setting, such high-fidelity biosignals may be unavailable. Alternatively, a lower-fidelity biosignal, such as those from an accelerometer, has a significantly smaller power footprint and is available in almost any wearable device. While multi-modal modeling and cross-modal reconstruction of biosignals have been done before, here, we demonstrate that we can distill representational knowledge across biosignals with different levels of fidelity, i.e., from PPG to accelerometer, using 20 million minutes of unlabeled data collected from ~172K participants in the Apple Heart and Movement Study under informed consent. Our knowledge distillation framework does not require labels; we pre-train PPG encoders via self-supervised learning, and then distill the representational knowledge from the PPG encoders to accelerometer encoders. We first demonstrate strong cross-modal alignment on unseen data, e.g., 99.2% top-1 accuracy for retrieving PPG embeddings from accelerometer embeddings. We show that distilled accelerometer encoders have significantly more informative representations compared to self-supervised or supervised encoders trained on accelerometer data for downstream targets, observed by at least 23%-49% improved performance for predicting heart rate and heart rate variability, and are readily predictive of a wide array of downstream targets including demographic variables, health conditions, use of medications, and lifestyle habits. We also demonstrate that our framework can be applied to different encoder architectures with different pre-training strategies of the strong encoder, and can be used to simultaneously do cross-modality distillation and model compression. Additionally, we perform various ablations for augmentations, hyperparameters and multi-modal training. We believe our proposed representational knowledge distillation framework may unlock new opportunities for developing digital biomarkers from any wearable device with lower-fidelity biosignals, and help individuals track their health more frequently and conveniently.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents a novel approach to learning representations from wearable sensor data by combining accelerometer and PPG signals. The authors propose a two-stage training process: first, a student model learns to predict heart rate from accelerometer data, guided by a teacher model that uses PPG signals; second, a shared embedding is learned from both modalities. This approach shows promising results on heart rate and heart rate variability estimation tasks.

### Strengths
- The proposed method cleverly leverages two modalities in a cooperative way. Using accelerometer data to guide the learning of heart rate estimation from less reliable acceleration data is a novel and practical approach.

- The authors demonstrate the effectiveness of their method on benchmark datasets, achieving competitive performance on HR and HRV estimation tasks.

- The paper clearly articulates the motivation behind the proposed approach and provides a comprehensive analysis of its benefits.

### Weaknesses
-  While the authors acknowledge some related work, a more in-depth comparison to models that directly use acceleration as input and heart rate as output is missing. This would help to better understand the specific advantages of the proposed distillation-based approach.

- The largest model evaluated has 6.3M parameters, which might be insufficient to fully leverage the large dataset. Exploring the impact of scaling the model further could reveal additional performance gains.

- The evaluation focuses solely on HR and HRV estimation. Exploring a wider range of downstream tasks, such as sleep stage classification, activity recognition, or stress detection, would provide a more comprehensive assessment of the learned representations.

### Questions
- How does the proposed method compare to models that directly map acceleration to heart rate without any distillation, such as those presented in Hallgrímsson et al. (2018), Spathis et al. (2021), and Ni et al (2019)?

-- Hallgrímsson, Haraldur T., et al. "Learning individualized cardiovascular responses from large-scale wearable sensors data." arXiv preprint arXiv:1812.01696 (2018).

-- Spathis, Dimitris, et al. "Self-supervised transfer learning of physiological representations from free-living wearable data." Proceedings of the Conference on Health, Inference, and Learning. 2021.

-- Ni, Jianmo, Larry Muhlstein, and Julian McAuley. "Modeling heart rate and activity data for personalized fitness recommendation." The World Wide Web Conference. 2019.

- What is the impact of scaling the model size on the performance of both the student and the teacher models? Did you observe any evidence of underfitting with the current model sizes?

- Why did you choose to focus only on HR and HRV estimation tasks? Have you considered evaluating the learned representations on other downstream tasks, such as those explored in Abbaspourazad et al. and Spathis et al., to demonstrate the generalizability of the learned embeddings?

- How does the choice of different teacher network architectures affect the student's performance and the quality of the learned embeddings?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper addresses the challenge of creating low-power, high-fidelity biosignal encoders in wearable devices by distilling knowledge from high-fidelity photoplethysmography (PPG) signals to accelerometer signals. This work is based on a large-scale dataset from the Apple Heart and Movement Study (AHMS), containing 20 million minutes of data from approximately 172,000 participants. Key contributions of the paper include:

* A representational knowledge distillation framework across biosignals, aiming to leverage high-fidelity signals for improved lower-fidelity signal representation.

* Demonstrating significant improvements in representation quality, evaluated through heart rate and heart rate variability predictions.

### Strengths
* **Relevant Problem:** The paper addresses a significant real-world problem with direct applications in wearable health technology.
* **Effective Solution:** The proposed method effectively improves the representation of accelerometer signals for health applications.
* **Detailed Ablation Studies:** The ablation studies provide a comprehensive analysis of the method’s behavior under various configurations.
* **Clear Writing:** The paper is well-structured, making it accessible and easy to follow.

### Weaknesses
* **Limited Novelty:** While the approach is effective, the novelty is somewhat limited as similar representational knowledge distillation methods exist for biosignals.
* **Contribution Clarification:** Some contributions, such as ablation studies, are essential for verifying robustness rather than stand-alone contributions.

### Questions
## Major Comments

* **Misleading Contribution Title:**
The first listed contribution, “Representational Knowledge Distillation across Biosignals,” could be misleading. While it is possibly a novel application to wearable signals, other biosignal domains have explored knowledge distillation. Clarifying this distinction could help prevent misunderstandings about the paper’s contributions.

* **Contrastive Learning Experiment Setup:**
In Section 3.1.2, where contrastive learning is applied as an alternative to masked autoencoding, the architecture changes alongside the learning paradigm. This confounds the results, making it difficult to isolate the effects of each factor. It may be beneficial to conduct experiments with a fixed architecture across learning paradigms to achieve a more controlled comparison.

* **Justification for Segment-Level Pair Selection:**
In Section 3.1.2, participant-level positive pairs are replaced with segment-level pairs to enhance the model’s ability to learn segment-specific information. While this adjustment is intuitive, an experiment supporting this decision would add robustness to the claim.

* **Confusing Results in Table 4:**
The results in Table 4 appear to contradict the discussion on page 10, where it is claimed that simultaneous training on both modalities causes a significant performance drop (132%, 66%, and 50%). These values do not align with the reported figures in Table 4, creating confusion. Clarifying these discrepancies would improve result interpretation.

## Minor Comments

* **Citation for AHMS Dataset:**
When the AHMS dataset is introduced in the introduction (page 2, line 077), it should be properly cited to enhance clarity and give credit to the dataset source.

* **Ablation Studies as a Contribution:**
The fifth contribution, “Ablation Studies,” may be better categorized as part of the robustness evaluation rather than a unique contribution. Demonstrating the necessity of ablation studies supports the robustness of the findings but may not stand alone as a contribution.

* **Reference for SDNN and RMSSD:**
In Section 4.2, line 307, SDNN and RMSSD are mentioned as commonly used targets without any citation. Adding references for their relevance in prior works would provide supporting context for their selection.

* **Purpose of Untrained Model Results:**
In Table 1, the results for “Accel-random” and random selection are reported without clear context. These numbers may be of limited utility, as comparing an untrained model or random selections provides little practical insight. Justifying their inclusion would improve result interpretation.

POST REBUTTAL EDIT: Changed Score from 6 -> 8

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents a framework to distill representational knowledge from PPG to accelerometer data. As the deployment of PPG (optical) sensors are expensive, the authors proposed to use PPG during training without labels and use accelerometer after deployment for heart rate and heart rate variability. The authors used 20 million minutes of unlabeled data collected from ∼172K participants in the Apple Heart and Movement Study under informed consent for self-supervised training.

### Strengths
The paper used a large scale dataset for experiments. The topic of interest is important as the wearable devices are widely used. The motivation is well framed with a good amount of reference to previous works.

### Weaknesses
The main idea and the specific components of the paper are not novel. Obtaining a better representation from a low-fidelity signal using a high-fidelity one is already explored [1]. All the components of the framework, masking, augmentations, loss functions, distillation, tokenizing, are known to the machine learning community. No application specific novel modification is introduced.  


The main weakness of the paper is its evaluation. The used dataset is private without an open access, therefore, it is hard to find the details. But the website indicates the study only requires Apple Watch and iPhone [2]. This arises the significant question of how ground truth heart rate and heart rate variability are obtained. If the ground truth values are obtained from Apple Watch, the current experiments and the presented results are significantly limited. There are several works that show the HR and HRV from Apple Watch are not highly correlated with ground truth HR values that are obtained from gold standard ECG signals [3-4-5], especially during the motion.
In my opinion, if the evaluation of the presented framework is performed with the values that are prone to errors, this invalidates the claims in the paper. 


[1] Pritam Sarkar. CardioGAN: Attentive Generative Adversarial Network with Dual Discriminators for Synthesis of ECG from PPG. AAAI 2021.

[2] https://appleheartandmovementstudy.bwh.harvard.edu/

[3] Daniel Fuller, Reliability and Validity of Commercially Available Wearable Devices for Measuring Steps, Energy Expenditure, and Heart Rate: Systematic Review. JMIR 2020.

[4] Brinnae Bent, Investigating sources of inaccuracy in wearable optical heart rate sensors, NPJ digital medicine 2020.

[5] Benjamin W. Nelson, Guidelines for wrist-worn consumer wearable assessment of heart rate in biobehavioral research, NPJ digital medicine, 2020.


The baseline comparison is also extremely limited. Out of three comparisons, two of them are random guessing and random weight models. I would expect at least two more methods from signal conversion (low to high) to show and support the claim that the proposed framework is better than previous methods in non-private datasets. 

As a minor weakness, the title claims "Across Wearable Biosignals" but, the paper only focuses from PPG to IMUs. The title should be modified. The current version misleads the reader.

### Questions
1) For the downstream task of HR estimation, why not reporting RMSE and Pearson correlation? These metrics are widely used in HR estimation [1-3-4] problem and give detailed information about the data and model.

2) The importance of the augmentations are known in self-supervised learning, did the authors explore specific augmentations for specific modality? In literature, there are several examples [2-3] showed that the augmentations chosen by the authors are not effective for the modalities.

3) During the first stage of the training, why all PPG channels (4-channels) are used? And, for 60-second long? Is there an ablation study for that? 

4) What does the statement "demonstrated robustness to the number of available training labels" show us about the data and method? Normally, in self-supervised learning methods, when the amount of training labels increased, the performance also increases [1] and the variation decreases. But, in this case, even though the amount of labels increased by 1000, the improvement is close to 0.


[1] Yuzhe Yang, SimPer: Simple Self-Supervised Learning of Periodic Targets, ICLR 2023.

[2] Hangwei Qian, What makes good contrastive learning on small-scale wearable-based tasks? In Proceedings of the 28th ACM SIGKDD 2022.

[3] Berken Utku Demirel, Finding Order in Chaos: A Novel Data Augmentation Method for Time Series in Contrastive Learning, NeurIPS 2023.

[4] Jeremy Speth, Non-Contrastive Unsupervised Learning of Physiological Signals from Video. CVPR 2024

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work presents a cross-modality knowledge distillation method between PPG and Accelerometry data. They show that one can predict HR features from the accelerometry data by aligning the accelerometry data to the pre-trained PPG feature space.

### Strengths
Although cross-modality knowledge distillation has been studied before, applying this onto biosignals is a novel and interesting problem. The problem framing is well justified, in terms of using lower cost accelerometry signal to model PPG signals. The plots showing how distilling ppg encoder information into the accelerometry encoder improves performance is compelling, especially in regards to label efficiency compared to the supervised model.

### Weaknesses
* Potential overclaiming on distillation and representation capabilities
	* Results are based upon linear probing on HR, SDNN, and RMSSD. Each of these metrics are heart-rate-derived statistics, which somewhat form a limited evaluation on the capabilities of the knowledge distillation. Heart rate is trivially captured from PPG by measuring peak-to-peak differences, so these results only show that frequency information was distilled to the accelerometry encoder. I would be interested in understanding what other representation information from PPG data could be reflected in the accelerometry data after distillation, for example predicting a participants specific health diagnoses. Alternatively, the authors can argue how each of these 3 metrics are distinctive and capture unique information, such that the representation needs to represent 3 distinctive different ideas after distillation. This is my biggest concern with this work.


* Unclear ablation study approach
	* in Section 3.1.2 "we perform ablation in regards to the teacher pre-training method and architecture via contrastive learning with EfficientNets ". Why does it make sense to conduct ablation studies of architecture with the contrastive pre-training objective rather than the teacher pre-training MAE objective?
	* Do the ablation studies in Sec. 5.5 use a contrastive learning objective for the teacher?

### Questions
* Are there any hypothesis or further studies as to why augmentations lead to a stronger performance? 
* Without any alignment between a PPG encoder and an Accel encoder, it should be obvious that the two respective embedding dimensions exist in different feature spaces. Therefore, rows 2-4 in Table 1 and Figure 2 seem to present trivial results. It is okay to keep as is, but marking these as a main claim seems to be a reach.

POST REBUTTAL EDIT: Changed Score from 5 -> 6

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes a cross-modal representational knowledge distillation framework that aims to transfer knowledge between high-fidelity PPG and low-fidelity accelerometer signals. The encoders for the two modalities are trained using two self-supervised methods, and the distillation process is achieved through cross-modal contrastive learning. While the application of this work has practical value, there are several limitations.

### Strengths
This work has practical value.

### Weaknesses
1.Limited Methodological Innovation: The knowledge transfer between modalities is performed using basic cross-modal contrastive learning, a widely used approach. Many recent works combine both intra-modal and cross-modal self-supervised contrastive learning to learn representations, making the approach in this paper less novel.
2.Lack of Comprehensive Comparative Experiments: The paper lacks comparisons with state-of-the-art (SOTA) cross-modal distillation methods, as well as accelerometer-based prediction methods, which limits the evaluation of the proposed method's performance.
3.Unclear Impact of Data Augmentation: While the paper highlights the importance of data augmentation in cross-modal distillation, it does not provide a detailed comparison or analysis of different augmentation strategies. Additionally, wearable device data is likely to contain noise and artifacts, and although the authors mention that augmentation can help the model adapt to noisy environments, no thorough analysis is provided.
4.Limited and Unlabeled Dataset, Insufficient Downstream Tasks: Although the framework demonstrates the advantages of unsupervised learning, it lacks detailed experiments on labeled datasets, limiting the validation of its performance on tasks such as classification. The downstream tasks explored in the paper are not sufficient to fully showcase the framework's potential.

### Questions
Please see Weaknesses.

### Soundness
1

### Presentation
2

### Contribution
2
