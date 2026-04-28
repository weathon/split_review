# Reliable Test-Time Adaptation via Agreement-on-the-Line

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 5, 6, 5

## Abstract
Test-time adaptation (TTA) methods aim to improve robustness to distribution shifts by adapting models using unlabeled data from the shifted test distribution. However, there remain unresolved challenges that undermine the reliability of TTA, which include difficulties in evaluating TTA performance, miscalibration after TTA, and  unreliable hyperparameter tuning for adaptation. In this work, we make a notable and surprising observation that TTAed models strongly show the agreement-on-the-line phenomenon (Baek et al., 2022) across a wide range of distribution shifts. We find such linear trends occur consistently in a wide range of models adapted with various hyperparameters, and persist in distributions where the phenomenon fails to hold in vanilla model (i.e., before adaptation). We leverage these observations to make TTA methods more reliable from three perspectives: (i) estimating OOD accuracy (without labeled data) to determine when TTA helps and when it hurts, (ii) calibrating TTAed models again without any labeled data, and (iii) reliably determining hyperparameters for TTA without any labeled validation data. Through extensive experiments, we demonstrate that various TTA methods can be precisely evaluated, both in terms of their improvements and degradations. Moreover, our proposed methods on unsupervised calibration and hyperparameters tuning for TTA achieve results close to the ones assuming access to ground-truth labels, in both OOD accuracy and calibration error.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Test-time adaptation (TTA) improves model performance in the presence of distribution shifts that happen at test-time, however, its reliability is hard to evaluate as it requires access to labels at test time. To this end, this work proposes to use the, introduced in prior work, agreement-on-the-line phenomenon in order to improve TTA. Agreement between two models, $h$ and $h’$ is defined as $\\mathbb{E}_{x \\sim \\mathcal{D}}[\\mathbb{1}\\{h(x) = h’(x)\\}]$ and the main intuition is that, after updating a model with TTA, there is a linear relationship between the agreement on the in-distribution (i.e., the distribution used to train the original model) and the agreement on the out-distribution, i.e., the distribution shift observed at test time. The authors then use this observation in order to estimate performance on out-of-distribution data after TTA (without needing access to test labels), perform hyperparameter optimization and improve calibration after TTA.

### Strengths
- Reliability of TTA is an important topic and thus this work is a relevant and timely contribution
- The results are convincing, so they could be useful in general for future research on TTA
- The experiments are extensive and cover various tasks

### Weaknesses
 - The novelty of this method is relatively limited; it is an application of Baek et al. (2022) to the TTA setup
- This method requires adapting multiple models during test time at the specific distribution shift in order to compute the agreement and use it to improve TTA. This might limit practical applications where training multiple models is expensive and, furthermore, the improvements on TTA seem to be on hindsight as one first needs to train multiple models in order to understand whether TTA will yield improvement. Furthermore, given that TTA usually operates on a stream of OOD data and provides a stream of predictions, it is unclear how predictions will be made at test time; does one use the ID model, (one of) the TTA models or does one wait up until the agreement-on-the-line has been computed before making any predictions on the stream?
- Some of the details about the method are not clear.

### Questions
Overall, I believe this work is a nice contribution in the field of TTA, as it addresses important issues in TTA. Having said that, the novelty is relatively small, hence my rating. As for questions to the authors:
- What is considered to be $h(x)$? Is it the most probable class under $h$? If so, why not define agreement in terms of the entire distribution on the output space for models, e.g., some kind of expected divergence between $h(x)$ and $h’(x)$? 
- How many models were used to get the agreement / accuracy lines at the figures?
- At algorithm 1, it seems that predictions on the ID and OOD data are done under a model that is continuously updated on OOD data, therefore, the ordering of the batches might have an effect on the agreement lines. Do the results change significantly under different random seeds?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors aim to achieve reliable test-time adaptation (TTA) by tackling three bottlenecks, including performance evaluation without labeled data, miscalibration after TTA, and hyperparameter selection for TTA methods. Specifically, the authors empirically verify the strong correlation in agreement and accuracy between in-distribution (ID) data and out-of-distribution (OOD) data. Based on this phenomenon, the authors adopt the ALine-S/D method to estimate OOD accuracy based on ID data and labels. With the estimated OOD accuracy, they further calculate the optimal scaling temperature to calibrate the model prediction for a lower expected calibration error. Moreover, the authors select the hyperparameters that enable the adapted model to obtain the best performance on the ID data as the optimal TTA hyperparameters on the OOD data. However, some significant issues are required to be further addressed. My detailed comments are as follows.

### Strengths
1. The authors reveal and verify the agreement-on-the-line and accuracy-on-the-line phenomenon in various TTA methods and various datasets, suggesting a new idea of hyperparameter tuning for TTA methods.
2. The authors propose a new evaluation method to estimate accuracy on out-of-distribution (OOD) data without OOD labels, which further enables a more precise model calibration via temperature scaling.
3. Experimental results demonstrate the effectiveness of the proposed unsupervised calibration methods. For example, the proposed unsupervised calibration method is able to reduce the expected calibration error from 13.40 to 2.10 while using TENT under CIFAR100-C.

### Weaknesses
1. The authors have empirically observed the occurrence of agreement-on-the-line (AGL) and accuracy-on-the-line (ACL) following test-time adaptation (TTA). To enhance the manuscript, it would be beneficial for the authors to provide a more extensive explanation and discussion regarding this observed phenomenon. Specifically, the underlying reasons for why a linear relationship exists between ID and OOD performance metrics, and the conditions under which this linearity might break down, should be explored in more detail.
2. The proposed temperature scaling method may not be applicable in latency-sensitive real-world applications when considering efficiency. As described in section 3.2, the optimal temperature is calculated after the network makes predictions on the full test set. Therefore, the proposed method require a significant delay for model adaptation. More discussion on efficiency is required. The authors should quantify the computational overhead of the temperature scaling process, particularly in relation to the inference time of the adapted model itself. Furthermore, the applicability of this method in real-time scenarios should be addressed.
3. Although the authors conduct experiments on different TTA methods, the problem setting of this paper is different from that of TTA. As shown in Algorithm 1, the proposed performance estimation method requires in-domain data and labels, which, however, are inaccessible under the settings of TTA. This discrepancy between the method's requirements and the standard TTA scenario needs to be clearly acknowledged and addressed. The authors should discuss how their method could be adapted or modified to work in a true TTA setting without relying on labeled in-domain data.
4. Figures 1-3 are difficult to understand. For example, it is unclear what the values of the horizontal and the vertical axes in Figure 1 represent. More explanations should be provided. Specifically, the figures should clearly label each axis and the meaning of the plotted points, including the distinction between accuracy and agreement, and how these are calculated. The specific TTA methods and datasets used in each figure should also be clearly stated in the figure captions.
5. The authors only analyze the agreement-on-the-line phenomenon on CNN-based models. However, powerful transformer-based models should also be involved in the experiments, such as ViT[1], Swin Transformer[2], PoolFormer[3], and so on. The generalizability of the AGL and ACL phenomena to other architectures, particularly those with very different inductive biases, needs to be established.
6. In the Introduction, the authors claim that "Baek et al. (2022) show that the ID and OOD agreement between classifiers shows a strong linear correlation". However, Baek et al. (2022) only study the correlation of disagreement and error between classifiers. It would be preferable to provide a more precise description. The authors should clarify the specific findings of Baek et al. (2022) and how they relate to the current work, ensuring that the claims made in the introduction accurately reflect the cited research.
7. In Table 2, the authors only provide insufficient results on several domains of the test datasets to demonstrate the effectiveness of the proposed performance estimation. It would be better if the authors could provide more experimental results under these datasets, such as all 15 corrupted datasets in ImageNet-C. The authors should provide a more comprehensive evaluation of their performance estimation method by including results on all available corruption types in the benchmark datasets.
8. In Figure 3, the authors demonstrate that the phenomenon of AGL and ACL also occurs when varying TTA hyperparameters, such as learning rate and batch size. However, from Table 1 to Table 3, the authors only study the effect of the proposed methods using different architectures or different training checkpoints. More ablation study using different hyperparameter setup is suggested. A more thorough ablation study is needed to demonstrate the robustness of the proposed method across different hyperparameter settings.
9. As shown in Figure 4, varying learning rate in TTT exhibits a negative correlation between ID and OOD accuracies. To establish a comprehensive study, more experiments should be conducted to verify if this phenomenon occurs in other test-time training methods, such as TTT++[4] and TTT-MAE[5]. The authors should investigate the generality of this negative correlation by including more TTA methods in the analysis, and provide an explanation for why such a negative correlation might exist.
10. On page 7, the sentence “let X the random variable” should be changed to “let X be the random variable”.

### Questions
Please refer to the Weakness

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This study addresses critical challenges in Test-Time Adaptation (TTA) methods, used to bolster model robustness against distribution shifts, by leveraging unlabeled data from the test distribution. The authors identify a consistent "agreement-on-the-line" phenomenon in adapted models, regardless of varied hyperparameters and across diverse distribution shifts. Utilizing this insight, they enhance TTA reliability by introducing strategies for estimating Out-Of-Distribution (OOD) accuracy, recalibrating models, and tuning hyperparameters without labeled test data. Comprehensive experiments validate these approaches, demonstrating evaluation of TTA methods and improvements in both OOD accuracy and calibration error, akin to scenarios having access to ground-truth labels.

### Strengths
Highlighting a Critical Problem: The researchers focused on the test-time adaptation (TTA) issue, showing that current methods aren't great at evaluating how well TTA methods work. This work is important because it tells us we need better ways to check if these methods are doing what we want them to do without always having to rely on labeled data.

Interesting Observation about Model Behavior: They found something pretty unexpected in the models after TTA. These models tended to show a "line agreement" behavior more than they did before. It means that after trying to adapt the models to new situations, they started to behave in a predictable pattern, which was interesting and useful to know for future work.

### Weaknesses
 **Insufficient Evidence for OOD and ID Performance Correlation Claims**: The authors' assertions about model behavior correlations lack broad empirical support. The research predominantly revolves around CNNs, which is just one structure among the diverse architectures and applications in deep learning. To substantiate these findings' universality and efficacy, it's crucial to extend the studies to other network models and datasets, such as Vision Transformers (ViT) and Swin Transformers, and more complex tasks like object detection and semantic segmentation. Confirming similar observations across a wider range of contexts would instill greater confidence in the authenticity and applicability of this phenomenon.

**Heavy Reliance on Full Access to In-Distribution Data**: The methods proposed in the study assume complete access to in-distribution training data, an assumption impractical in many real-world scenarios. Constraints like computational resources or data privacy issues might restrict access to comprehensive in-distribution training data, leaving practitioners with only the trained model. Under these circumstances, the proposed evaluation method may become inapplicable, losing its value. The authors need to tackle this limitation, potentially necessitating the design of novel experiments or methods that support evaluation and adaptation in these more restrictive environments.

**Discrepancy Between the Offline Nature of Methods and Practical Needs**: The methods introduced in this research operate within a static, offline setting, overlooking the dynamic, continuous arrival of data in real-world applications. In real-world scenarios, models must accommodate online or incremental data streams, known as online test-time adaptation. The researchers should contemplate this online setting and investigate whether their strategies remain effective when handling continuous data flows. This exploration might require new experimental setups and adaptability tests to simulate the reception conditions of data in the real world.

### Questions
Please address the concerns above.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper investigates a practical and valuable issue of Test-Time Adaptation, that is, how to pre-estimate the TTA performance of TTAed models. The authors found that a strong correlation existed between TTAed models’ OOD performance/agreement and ID performance/agreement. Based on these findings, the authors further proposed methods for the TTAed model’s calibration and hyperparameter selection. The overall findings are novel but still not convincing enough, necessitating further justifications. So I currently give a borderline score and I will re-evaluate the paper after rebuttal. My detailed comments are as follows.

### Strengths
The studied problem is invaluable in TTA but often overlooked by the current community. As many TTA methods modify model parameters during inference and may suffer from an instability issue, in real-world applications, it is essential to pre-estimate the Adaptation Performance to determine whether TTA is needed or how to achieve the best TTA performance using only unlabeled test data. 

The observed correlation between TTA performance and ID performance is novel and interesting. The resulting methods for Calibration and Hyper-parameter Selection are simple yet effective.

### Weaknesses
1. The claim of “OOD and ID performance/agreement correlation” requires more empirical evidence. Please refer to Question 1.
2. The proposed methods rely on full access to the ID data and work in an offline manner, which slightly weakens its application scenarios.
3. Algorithm 1 requires to maintenance of $n$ models for TTA, which may be memory-consuming and inefficient.

### Questions
1. Could the authors include more results regarding more advanced network models in Figures 1 -3, including but not limited to VisionTransformers(Tiny/Small/Base/Large and with different input resolutions) and  SwinTransformers from the Timm repository? These model architectures are quite different from the considered ones and are also trained with more advanced strategies (such as data augmentation, stochastic depth, EMA, dropout, etc.) I am wondering whether the “correlation” still holds under these scenarios. 

2. Are there any (or potential) solutions that can modify the proposed method to be an online version? In other words, how about the performance of Algorithm 1 work in an online setting?

3. Are there any sensitivity analyses about $n$ in Algorithm 1?

4. For Calibration and Hyper-parameter Selection, how many ID samples are needed? Will this ID sample number affect the performance significantly? 

5. How about the performance of the proposed methods under wild test settings proposed by SAR [ICLR 2023]？ 

6. If possible, I am also curious about the ID-OOD correlation of MEMO [Memo: Test time robustness via adaptation and augmentation]  and Contrastive Learning Objectives [Contrastive Test-Time Adaptation].

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good
