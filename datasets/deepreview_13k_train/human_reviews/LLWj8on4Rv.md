# Leveraging Driver Field-of-View for Multimodal Ego-Trajectory Prediction

- Decision: Accept
- Scores: 6, 8, 6

## Abstract
Understanding drivers’ decision-making is crucial for road safety. Although predicting the ego-vehicle’s path is valuable for driver-assistance systems, existing methods mainly focus on external factors like other vehicles’ motions, often neglecting the driver’s attention and intent. To address this gap, we infer the ego-trajectory by integrating the driver’s attention and the surrounding scene. We introduce RouteFormer, a novel multimodal ego-trajectory prediction network combining GPS data, environmental context, and driver field-of-view—comprising first-person video and gaze fixations. We also present the Path Complexity Index (PCI), a new metric for trajectory complexity that enables a more nuanced evaluation of challenging scenarios. To tackle data scarcity and enhance diversity, we introduce GEM, a comprehensive dataset of urban driving scenarios enriched with synchronized driver field-of-view and gaze data. Extensive evaluations on GEM and DR(eye)VE demonstrate that RouteFormer significantly outperforms state-of-the-art methods, achieving notable improvements in prediction accuracy across diverse conditions. Ablation studies reveal that incorporating driver field-of-view data yields significantly better average displacement error, especially in challenging scenarios with high PCI scores, underscoring the importance of modeling driver attention. All data, code, and models will be made publicly available.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper introduces a multimodal ego-trajectory prediction model that utilizes driver field-of-view (FOV) data—including first-person video and gaze fixations—along with environmental and GPS information to enhance the accuracy of vehicle trajectory forecasting. The method surpasses conventional models through the implementation of a Path Complexity Index (PCI), which assesses the complexity of diverse driving scenarios. The authors present a novel dataset that provides comprehensive urban driving data enriched with driver FOV information.

### Strengths
- New dataset: the authors contribute GEM, a high-quality dataset focused on urban driving, which includes synchronized FOV and gaze data, filling a critical gap in available resources for trajectory prediction. It will be good to have this dataset for the autonomous driving community. 
- The proposed RouteFormer introduces a unique approach by integrating driver field-of-view (FOV) data, such as first-person video and gaze fixations, with GPS and environmental data, enhancing the accuracy of ego-trajectory prediction.
- Introduction of Path Complexity Index (PCI). The paper proposes a novel PCI metric to quantify the complexity of driving scenarios, offering a more nuanced assessment of prediction challenges compared to traditional metrics.
- The proposed method outperforms the other baselines on both datasets.

### Weaknesses
 - To fully understand how much each modality contribute to the improvement, it will be interesting to add the ablations studies below and compare the ADE and ADE+20PCI.
   1. RouteFormer without video and gaze (Motion only).
   2. RouteFormer without surrounding scenes (Motion + Gaze).

- Stronger baselines are needed. The current baselines (GIMO, Multimodal Transformer) used in this paper are mainly designed for human motion. Compared with at least one vehicle motion predictor is more convincing (e.g., MTR [1], Autobots [2], ...). Or are there any potential reasons that the authors thought the human motion baselines were more appropriate than vehicle baselines?

### Questions
Please refer to the weaknesses above.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper introduces RouteFormer, a multimodal ego-motion prediction network that integrates driver field-of-view (FOV) data with scene and GPS information to improve trajectory prediction. RouteFormer is the best solution on the market for this problem. Its Path Complexity Index (PCI) metric assesses trajectory difficulty and enhances model evaluation in complex scenarios. Additionally, the paper presents GEM, a new dataset containing synchronised driver FOV, gaze, and GPS data, capturing diverse urban driving conditions. RouteFormer significantly improves prediction accuracy, especially in high-complexity scenarios, advancing safety in driver-assistance systems.

### Strengths
This paper has done an impressively solid and hardcore job—it's a pleasure to read, providing a refreshing clarity that’s truly satisfying. It offers genuinely unique insights and, in my opinion, fully meets the standards for conference publication.

1. RouteFormer effectively combines driver FOV, scene, and GPS data, resulting in enhanced accuracy for predicting complex, non-linear trajectories. This multimodal integration marks a notable advancement over existing models.

2. The introduction of the Path Complexity Index (PCI) provides a novel way to quantify trajectory difficulty, allowing for better evaluation of model performance in challenging scenarios, which is often overlooked in traditional metrics.
The GEM dataset fills a significant gap by providing synchronized driver gaze, field-of-view, and GPS data, particularly suited for urban driving conditions with various traffic elements. This dataset enables more nuanced model training and testing, contributing to the broader research community.

3. Extensive testing demonstrates that RouteFormer performs robustly in real-world scenarios, highlighting its potential for practical applications in driver-assistance and AD systems.

### Weaknesses
I have a couple of concerns regarding the definition of corner-case scenarios. The authors propose a model that essentially employs a contrastive learning approach—predicting a trajectory and then categorizing scenarios by comparing it with the ground truth. I believe this method introduces bias, as predictions differ across models. What evidence suggests that the prediction model used here is unbiased? While many recent works adopt similar methods to address long-tail issues, in this particular field, I find the approach still somewhat subjective.

The authors have not clearly defined what constitutes the long-tail phenomenon. It’s unclear why this method is capable of defining rare scenarios. I believe that this method, as described, does not adequately capture or define the essence of long-tail events. Could the authors provide further clarification?

The manuscript is inspired by human visual attention during driving, so it should cite earlier works that introduced similar ideas in trajectory prediction. These are:
(1) Human Observation-Inspired Trajectory Prediction for Autonomous Driving in Mixed-Autonomy Traffic Environments, IEEE International Conference on Robotics and Automation (ICRA 2024)
(2) Less is More: Efficient Brain-Inspired Learning for Autonomous Driving Trajectory Prediction, European Conference on Artificial Intelligence (ECAI 2024)

The related work section could benefit from a broader discussion of recent research. Currently, I find the discussion of the latest studies to be rather limited.

The paper would benefit from a discussion section that addresses its limitations and future challenges. This would provide a more comprehensive perspective.

Could the authors consider open-sourcing the project code and dataset? This would significantly contribute to the community.

### Questions
1. I have a couple of concerns regarding the definition of corner-case scenarios. The authors propose a model that essentially employs a contrastive learning approach—predicting a trajectory and then categorizing scenarios by comparing it with the ground truth. I believe this method introduces bias, as predictions differ across models. What evidence suggests that the prediction model used here is unbiased? While many recent works adopt similar methods to address long-tail issues, in this particular field, I find the approach still somewhat subjective.

2. The authors have not clearly defined what constitutes the long-tail phenomenon. It’s unclear why this method is capable of defining rare scenarios. I believe that this method, as described, does not adequately capture or define the essence of long-tail events. Could the authors provide further clarification?

3. The manuscript is inspired by human visual attention during driving, so it should cite earlier works that introduced similar ideas in trajectory prediction. These are:
(1) Human Observation-Inspired Trajectory Prediction for Autonomous Driving in Mixed-Autonomy Traffic Environments, IEEE International Conference on Robotics and Automation (ICRA 2024)
(2) Less is More: Efficient Brain-Inspired Learning for Autonomous Driving Trajectory Prediction, European Conference on Artificial Intelligence (ECAI 2024)

4. The related work section could benefit from a broader discussion of recent research. Currently, I find the discussion of the latest studies to be rather limited.

5. The paper would benefit from a discussion section that addresses its limitations and future challenges. This would provide a more comprehensive perspective.

6. Could the authors consider open-sourcing the project code and dataset? This would significantly contribute to the community.

Overall, I believe this paper meets the publication standards for ICLR.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this paper, the authors propose an end-to-end multimodal ego-motion prediction network that utilizes driver’s field-of-view data. Specifically, the proposed model predicts egocentric trajectory by taking scene videos, driver field-of-view videos, driver gaze position, and past trajectory as its input. Besides, the authors also propose a metric to measure the trajectory complexity, and an ego-motion dataset with driver positions and perspective. The experimental results show some improvements in the task of trajectory prediction task.

### Strengths
1. The proposed solution sounds solid in theory. Specially, considering driver’s attention and intent as well as surrounding environment is convincing. The driver’s attention and intent is a key impact factor of future trajectory.  
2. The proposed dataset is helpful for other researchers to do more related research on that. 
3. The proposed metric of trajectory complexity is helpful. It is a good indicator while analyzing the performance of a self-driving algorithm.
4. The ablation study and supplementary material are helpful. Readers can get more information from the ablation study results.

### Weaknesses
1. It will be better if the authors could report some failure cases. Especially for those cases which the predictions are totally opposite of the ground truth. 
2. It will be better if the authors could compare their solution with latest schemes published in Year 2023 or 2024.

### Questions
1. What if the estimated gaze positions move quickly (either caused by wrong prediction or the driver moves his/her gazes quickly)? Is there any negative impact on the final results?
2. Line 190, the gaze positions are in the shape of Tx2. Does it mean we only use one gaze for each time stamp?

### Soundness
3

### Presentation
3

### Contribution
3
