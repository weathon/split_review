# E-DETR: Evidential Deep Learning for End-to-End Uncertainty Estimation in Object Detection

- Decision: Reject
- Scores: 5, 5, 5, 3

## Abstract
Detection transformers (DETR) have emerged as powerful end-to-end learning frameworks for object detection, directly regressing detection parameters as point estimates. However, these networks often lack the ability to express any uncertainty within their estimates. In this work, we replace the regression of point estimates with the direct learning of the posterior distribution in a sampling-free manner by leveraging deep evidential learning, complementing the end-to-end DETR architecture. We present an instance-aware uncertainty framework by extending evidential deep learning with an IoU-aware loss, jointly modelling both classification and localization uncertainties. Furthermore, we enable the model to leverage its uncertainty for self-calibration, aligning the predicted probabilities with the true likelihood of outcomes, and effectively apply evidential deep learning for the task of imbalanced dense object detection. Our approach is easily extensible and requires only fine-tuning, thus leveraging the pre-training of transformers on large datasets. We conduct extensive experiments on two in-domain and three out-of-domain datasets, demonstrating impressive improvements in generalization performance, especially when fine-tuning on heavily imbalanced datasets characterized by data scarcity.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The work presents an approach to incorporate an evidential deep learning mechanism into the DETR architecture, replacing the regression of point estimates with the direct learning of posterior distributions. By leveraging an intersection-over-union (IoU) aware loss within an evidential deep learning framework, the method aims to provide instance-aware uncertainty estimates. This is particularly important for model calibration in safety-critical applications. The approach is mainly plug-and-play and can be extended to any DETR-based architecture. Results are demonstrated on the KITTI and BDD100k datasets.

### Strengths
- The proposed method introduces a straightforward modification that can be easily integrated into existing DETR-based models without adding significant complexity. This plug-and-play nature promotes adoption across various models.
- The paper tackles the important issue of uncertainty estimation in object detection, which is crucial for calibrating detectors in safety-critical applications.
- The structure of the paper is well organized.

### Weaknesses
- The experiments are limited to KITTI and BDD100k datasets. To effectively validate the usefulness of the method, it should be tested on relatively recent DETR-based architectures like DINO [1] and on larger, more diverse datasets such as MS-COCO. Exploring settings like DINO where models are pre-trained on Objects365 and fine-tuned on COCO would provide insights into the method's scalability.
- The paper does not include comparisons with prominent calibration methods that have shown improvements in DETR-based architectures [2,3]. Incorporating these comparisons highlights the advantages or limitations of the proposed approach.
- It is unclear how the Expected Calibration Error (ECE) is calculated. If Detection-ECE [4] is used, specifying the factors considered during computation (e.g., confidence scores, IoU thresholds, etc) is necessary. 
- Additionally, recent metrics proposed in the literature, such as in [5,6], should be included to provide a comprehensive evaluation of calibration performance.
- Though the paper is well organized, some parts of the methodology are difficult to grasp.

[1] "DINO: DETR with Improved DeNoising Anchor Boxes for End-to-End Object Detection." ICLR (2023)

[2]  "Cal-DETR: calibrated detection transformer." Advances in neural information processing systems (2024)

[3] "Bridging precision and confidence: A train-time loss for calibrating object detection." Conference on Computer Vision and Pattern Recognition. (2023)

[4] "Multivariate confidence calibration for object detection." Conference on computer vision and pattern recognition workshops. (2020)

[5] "Towards building self-aware object detectors via reliable uncertainty quantification and calibration." Conference on Computer Vision and Pattern Recognition. (2023)

[6] "On Calibration of Object Detectors: Pitfalls, Evaluation and Baselines." ECCV (2024)

### Questions
- Experiments are currently limited to the KITTI and BDD100k datasets. Have authors considered evaluating method on larger and more diverse datasets like MS-COCO, and on more recent DETR-based architectures such as DINO? Extending the experimental validation could demonstrate the scalability and generalization capabilities of the approach.
- The paper does not include comparisons with prominent calibration methods that have shown improvements in DETR-based architectures. How does the proposed method perform relative to these existing approaches?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper tackles the problem of jointly estimating classification and localization uncertainty estimates in an end-to-end manner for transformer-based detection methods (DETR). The core idea is to extend the deep evidential learning by introducing an IoU-aware loss, thereby jointly modeling the classification and localization uncertainties. The estimated uncertainties are used to self-calibrate the model which aligns the predicted probability with the true likelihood of outcomes. Experiments have been conducted with different variants of DETR. The results have been shown by training on KITTI dataset and evaluating on BDD-100K and nuImages datasets. Reported results claim to surpass the baseline methods and competing methods by notable margins.

### Strengths
**1)** The problem of estimating the classification and localization uncertainty estimation for object detection task carries importance due to its several applications in safety- critical applications.

**2)** The paper proposes an IoU-aware loss to extend deep evidential learning to jointly model the classification and localization uncertainties.

**3)** The uncertainty estimates allows self-calibration of the detection model, which is important to develop trust in its predictions and improve the overall reliability of the model.

**4)** Experiments have been shown with different variants of DETR and the results claim to significantly outperform the baselines and competitive methods.

### Weaknesses
**1)** The scale of experiments is rather small, especially across the diversity and number of datasets, and so it is difficult to fully accept the effectiveness of the method.

**2)** The ablation study is not deep and also conducted on only one dataset and with one baseline detection method.

**3)** Why the expected calibration error (ECE) is used to report the calibration performance of detection methods? It is difficult to understand as it is primarily for reporting classification performance and there are proper metrics such as D-ECE [A], LaECE [B] for revealing the calibration performance of detectors.

**4)** The method section is a bit hard to read because the core contributions of the paper are somewhat hidden.

**5)** The paper claims at several places (e.g., L22, L88, L151) of handling the class imbalance problem, however, there is no dedicated study in the paper which validates this clearly. 

**6)** The paper is missing insights on why and how it is able to substantially boost the performance of transformer-based detection methods, especially the DETR method.

[A] Küppers, F., Haselhoff, A., Kronenberger, J. and Schneider, J., 2022. Confidence calibration for object detection and segmentation. In Deep Neural Networks and Data for Automated Driving: Robustness, Uncertainty Quantification, and Insights Towards Safety (pp. 225-250). Cham: Springer International Publishing.

[B] Kuzucu, S., Oksuz, K., Sadeghi, J. and Dokania, P.K., 2024. On Calibration of Object Detectors: Pitfalls, Evaluation and Baselines. arXiv preprint arXiv:2405.20459.

### Questions
**1)** I would like to see the results (detection performance and calibration performance) on more in-domain and out-domain scenarios, such as Cityscapes (CS) and CS to CS-foggy, Sim10K and Sim10K to BDD100K (same classes as Sim10K. In BDD100K), and COCO.

**2)** Detailed ablation studies to establish the importance of proposed components across 2 more scenarios of in-domain and out-domain.

**3)** It is very important to investigate the performance (both detection and calibration) in different class-imbalance scenarios. Further, I expect to see the performance under dense detection scenarios (other than BDD100K and nuImages) as claimed by the method.  

**4)** L484: The paper mentions that, it is able to significantly improve the DETR performance comparable to newer versions of DETR. My question is how is this result relevant, when the achieved gain when later variants of DETR such as Deformable-DETR itself Is well over three years old.

**5)** How do you set $\lambda_{ann}$ in eq(10).

**6)** It would be good to show that how capable is proposed method in overcoming overconfidence and underconfidence in predictions.

**7)** The first para. of introduction section is missing references, for example L37 and L42.

**8)** Figure 1 Is not referenced anywhere in the text of the paper.

**9)** The paper needs to provide some insights in the form of analyses to better establish the grounding of claimed notable performance gains reported, especially in the case of DETR baseline

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper extends the DETR framework by replacing point estimate regressions with direct learning of the posterior distribution, leveraging deep evidential learning. The method presents an instance-aware uncertainty framework that jointly models classification and localization uncertainties through an IoU-aware loss. It also enables the model to use its uncertainty for self-calibration, aligning predicted probabilities with true outcomes.

### Strengths
1.The motivation is clear and convincing, effectively identifying the current challenges and deficiencies in existing methods, and proposing targeted modular solutions. The results achieved in experiments are commendable.

2.The method shows a certain degree of novelty by applying evidential deep learning to enhance DETR and innovatively presenting an instance-aware uncertainty framework.

3.The paper is well-supported theoretically, using extensive citations and formulas to demonstrate the robustness of the approach.

### Weaknesses
1.The illustrations in the paper are subpar. There is only one "rudimentary" network diagram with very limited information. Although the approach is theoretically inclined, I believe that incorporating high-quality images—such as diagrams, module schematics, and charts analyzing experimental data—is essential for a good paper, as they effectively aid reader comprehension.

2.The paper contains numerous formulas that lack punctuation at the end. A thorough review is recommended.

3.The formatting of tables in the paper appears unconventional, with a significant amount of whitespace.

4.The experimental results are insufficient and somewhat confusing. First, I suggest that the authors conduct additional experiments to further verify their methodology, such as hyperparameter discussions and experiments addressing the identified challenges. Additionally, the accuracy reported for DETR in Tables 1 and 2 seems unusual; I believe these accuracies are unreasonable and recommend that the authors carefully review the implementation of DETR. The specific implementation details for Table 3 are also not described.

5.While extensive use of formulas to argue the method can be persuasive, including all of them in the main text does not facilitate a quick and deep understanding for the reader. I recommend adjusting the description of the method section to emphasize the improvements specific to this work, while placing formulas that in existing other works in the supplementary materials.

### Questions
see Weaknesses

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The proposed work presents an uncertainty estimation method for object detection. Deep evedential learning is used for learning a posterior distribution. The approach is sampling free. An instance-aware uncertainty framework by extending evidential deep learning with an IoU-aware loss, jointly modelling both classification and localization uncertainties is proposed.

### Strengths
1) The paper's narration is easy to follow.

2) The results that were provided are convincing.

3) Uncertainty estimation for object detection is challenging and important. However, there has been a number works published previously (only few of them are cited).

4) The proposed combination of mostly existing pieces is well-designed.

### Weaknesses
1) The organization of the manuscript offers room for improvement. The section on the numerical experiments is short, the method section lengthy, the number of citations does not reflect the existing body of related work.

2) The amount of numerical experiments is thin. How does the method react to semantic out-of-distribution examples? How does it react to adversarial attacks? I find that a consideration of ECE only is not enough. How does the proposed method compare to confidence calibration methods? How does the calibration behave in the study provided in Tab. 2?

3) It is good that the primary object detection performance improves over other methods in Tab. 1 and also the results provided are convincing. However, primary accuracy + ECE are not enough for evaluating an uncertainty estimate in my opinion. How well does the uncertainty correlate with the presence of errors? How does it behave on semantic out-of-distribution objects or adversarial attacks?

Concerns of higher degree of detail:

4) No citations in the paragraphs 1, 2, 4 although several claims are made, such as overconfidence of object detectors etc. In general, the density of citations could be improved. Existing related works like [1,2] have not been considered.

5) The example provided for cross-entropy + softmax suffering from overconfidence, namely rotations applied to the input causing overconfidence, is a general problem caused by domain shift. Is this really mitigated by the proposed approach? With which data is the "I don't know" regularization term trained? Just using the background? Could the authors elaborate on that?

6) In eq. (8) the IoU is introduced in terms of q_ij. An IoU of zero does not provide any learning signal. Could the authors clarify on that?

7) In my opinion, it could be pointed out a bit more strongly which parts of the method are novel.

8) The claim of proposing a highly generalizable uncertainty estimation method seems too strong as it is at the same time proposed only for DETR models

9) The claim that the proposed method "align[s] with the true likelihood" seems a bit strong to me. Can the authors clarify what they mean?

10) Table 1 -- besides ECE, the type of evaluation metric (AP?) could be mentioned in the table.

In opinion, in the current state, the manuscript is not ready for publication at a conference like ICLR.

[1] Miller, Dimity, et al. "Dropout sampling for robust object detection in open-set conditions." 2018 IEEE International Conference on Robotics and Automation (ICRA). IEEE, 2018.

[2] Gasperini,  Stefano et al. "CertainNet: Sampling-free Uncertainty Estimation for Object Detection" IEEE ROBOTICS AND AUTOMATION LETTERS. 2021. 

[3] Riedlinger, Tobias, et al. "Gradient-based quantification of epistemic uncertainty for deep object detectors." Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision. 2023.

### Questions
1) Could you clarify what is the benefit of utilizing evidential deep learning in comparison to other approaches for uncertainty estimation in object detection compared to other approaches like e.g. [2,3] that are sampling free as well? In particular [3] is a post-hoc method which is more widely applicable, can also be traded in for performance and provides calibrated confidences.

2) Nallapareddy et al. (2023) receives a significant portion of the related work section. How is this approach related to the proposed work?

3) Could the authors comment on the questions in weaknesses 2,3,5,6,9?

4) Could the authors explain how they would like to address the remaining weaknesses 1,4,7,8,10?

### Soundness
3

### Presentation
1

### Contribution
2
