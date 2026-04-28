# Cocoon: Robust Multi-Modal Perception with Uncertainty-Aware Sensor Fusion

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6

## Abstract
\looseness=-1
An important paradigm in 3D object detection is the use of multiple modalities to enhance accuracy in both normal and challenging conditions, particularly for long-tail scenarios. To address this, recent studies have explored two directions of adaptive approaches: MoE-based adaptive fusion, which struggles with uncertainties arising from distinct object configurations, and late fusion for output-level adaptive fusion, which relies on separate detection pipelines and limits comprehensive understanding. In this work, we introduce Cocoon, an \textit{object}- and \textit{feature}-level uncertainty-aware fusion framework. The key innovation lies in uncertainty quantification for heterogeneous representations, enabling fair comparison across modalities through the introduction of a \textit{feature aligner} and a learnable surrogate ground truth, termed \textit{feature impression}. We also define a training objective to ensure that their relationship provides a valid metric for uncertainty quantification. Cocoon consistently outperforms existing static and adaptive methods in both normal and challenging conditions, including those with natural and artificial corruptions. Furthermore, we show the validity and efficacy of our uncertainty metric across diverse datasets.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces an object- and feature-level uncertainty-aware fusion framework for robust multi-modal sensor fusion in 3D detection scene of autonomous driving. It designs a valid uncertainty estimator for heterogeneous representations, and then dynamically fuses multi-modal sensor features. Experiments indicate the effectiveness of fusing heterogeneous features in several unrobust scene.

### Strengths
(1) It provides a very intuitive feature fusion analysis to derive the motivation of this paper
(2) All the designs that underpin the motivation of this article are very valid and reasonable.
(3) The results are rich and convincing.

### Weaknesses
Although the writing logic and thinking are clear, the explanation of the method is too complicated, which will bring inconvenience to the reader.

### Questions
No.

### Soundness
3

### Presentation
2

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
The paper introduces Cocoon, a novel framework that addresses the challenge of multi-modal fusion in 3D object detection. The paper proposes a novel uncertainty-aware fusion framework that operates at both object and feature levels through the introduction of Feature Impression and a feature alignment mechanism. This approach leverages conformal prediction theory to quantify uncertainties in heterogeneous sensor data, enabling dynamic weight adjustment between different modalities such as cameras and LiDAR.

### Strengths
1.Proposes a novel framework (Cocoon) that uniquely combines object-level and feature-level uncertainty awareness in multi-modal fusion, addressing a significant gap in existing approaches.
2.Thoroughly evaluates the model under diverse corruption scenarios, including both natural corruptions.
3.Provides solid mathematical foundation for the uncertainty quantification method, with clear derivations and validations across multiple datasets.

### Weaknesses
1.The paper shows a substantial increase in computational latency - from 1.1s to 1.6s when integrating Cocoon with FUTR3D.
2.While the paper demonstrates consistent improvements over baselines, the actual gains are relatively modest in many scenarios.
3.Only evaluates camera and LiDAR fusion, missing other important sensors like radar and ultrasonic.
4. The lack of validation on other datasets raises concerns about the generalizability of the method. Validation can be performed on the Waymo and Argoverse 2 datasets.
5. The method provides marginal gains and performs worse than previous methods such as CMT, BEVFusion, and DeepInteraction.

### Questions
1.While you propose using fewer decoder layers or queries to reduce latency: How does this affect the accuracy-speed tradeoff specifically?
2.Could you provide ablation studies on the importance of different components in your framework? Such as, how much does each component (feature aligner, Feature Impression, uncertainty quantification) contribute to the final performance?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
T​this paper propose a multimodal fusion framework called Cocoon for 3D object detection. The core innovation of Cocoon is to achieve object and feature level fusion through uncertainty quantification. The framework introduces a feature aligner and a learnable alternative truth value (called "Feature Impression") to fairly compare uncertainties between multimodalities and dynamically adjust the weight of each mode. Experimental results show that Cocoon outperforms existing static and adaptive fusion methods under standard and challenging conditions, and performs more robustly under natural and artificial perturbations.

### Strengths
1. The paper is clearly presented and easy to understand.
2. The innovation of uncertainty quantification mechanism is feasible from the principles and experiments in Section 4.
3. What I care about more is that the Cocoon framework has good scalability and can be further applied to more types of modal fusion, such as combining camera, LiDAR and radar data for autonomous driving, or combining visual and language modalities for visual language models (VLM).

### Weaknesses
1. The entire COCOON process, especially the structural comparison shown in Figure 1, and the "FEATURE IMPRESSION-BASED FEATURE ALIGNER" and "UNCERTAINTY QUANTIFICATION" parts in Sec 4.2 and 4.3, made me feel the huge computational overhead. Whether it is based on RGB, LiDAR, or multi-modal fusion target detection methods, I think they cannot be implemented quickly if the real-time performance cannot be guaranteed. The advantages can only be reflected at the numerical level of the paper.
2. Does COCOON rely too much on the quality of feature alignment and calibration in the data? Section 4.2 mentioned that since data from different modalities need to be projected into the same feature space for comparison, the accuracy of this part of the alignment directly affects the reliability of uncertainty quantification. If there are large differences in the quality or sampling frequency of the features of each modality, it will be difficult for the feature aligner to effectively align the data distribution, will this in turn affect the overall fusion effect?
3. At the end of Section 5.1, the value of the hyperparameter $ \alpha $ is set, but Table 4 directly assigns $ \alpha $ to 0.1. And Limitations mentions that the change of alpha will bring about a significant change in the algorithm effect. Is COCOON too dependent on hyperparameters?

### Questions
See Weaknesses.

### Soundness
3

### Presentation
4

### Contribution
3
