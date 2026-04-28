# MOS: Model Synergy for Test-Time Adaptation on LiDAR-Based 3D Object Detection

- Decision: Accept
- Avg Score: 8.00
- Scores: 8, 8, 8

## Abstract
LiDAR-based 3D object detection is crucial for various applications but often experiences performance degradation in real-world deployments due to domain shifts. While most studies focus on cross-dataset shifts, such as changes in environments and object geometries, practical corruptions from sensor variations and weather conditions remain underexplored. In this work, we propose a novel online test-time adaptation framework for 3D detectors that effectively tackles these shifts, including a challenging \textit{cross-corruption} scenario where cross-dataset shifts and corruptions co-occur. By leveraging long-term knowledge from previous test batches, our approach mitigates catastrophic forgetting and adapts effectively to diverse shifts. Specifically, we propose a Model Synergy (MOS) strategy that dynamically selects historical checkpoints with diverse knowledge and assembles them to best accommodate the current test batch. This assembly is directed by our proposed Synergy Weights (SW), which perform a weighted averaging of the selected checkpoints, minimizing redundancy in the composite model. The SWs are computed by evaluating the similarity of predicted bounding boxes on the test data and the independence of features between checkpoint pairs in the model bank. To maintain an efficient and informative model bank, we discard checkpoints with the lowest average SW scores, replacing them with newly updated models. Our method was rigorously tested against existing test-time adaptation strategies across three datasets and eight types of corruptions, demonstrating superior adaptability to dynamic scenes and conditions. Notably, it achieved a 67.3\% improvement in a challenging cross-corruption scenario, offering a more comprehensive benchmark for adaptation. The source code is provided in the supplementary materials.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces a novel approach for test-time adaptation in LiDAR-based 3D object detection: Model Synergy (MOS). The proposed method dynamically selects and assembles historical checkpoints to create a composite "super model" that adapts to domain shifts, including cross-dataset and corruption shifts. The assembly of checkpoints is controlled by Synergy Weights (SW) module, which minimizes redundancy by leveraging output-level and feature-level similarities. The method addresses practical scenarios like cross-corruption shifts, where both dataset and environmental discrepancies occur simultaneously. Experimental results across multiple datasets, including KITTI, Waymo, and KITTI-C, demonstrate that MOS outperforms SOTA test-time adaptation methods, achieving considerable improvements in both standard and complex scenarios.

### Strengths
The paper introduces a novel weighted ensemble of historical checkpoints approach, that helps mitigate catastrophic forgetting while adapting models to unseen domain shifts. This method achieves SOTA performance across multiple datasets and scenarios. 
The proposed method also effectively reduces memory usage by dynamically updating the model bank, retaining only key models with high synergy weights, thus maintaining performance with low resource cost

### Weaknesses
 The paper introduces a novel weighted ensemble of historical checkpoints approach, that helps mitigate catastrophic forgetting while adapting models to unseen domain shifts. This method achieves SOTA performance across multiple datasets and scenarios.
The proposed method also effectively reduces memory usage by dynamically updating the model bank, retaining only key models with high synergy weights, thus maintaining performance with low resource cost

The framework proposed by this paper is generally novel and effective, however, I still have some questions about the approach:
1. The paper demonstrates strong results (outperforms the SOTA methods) for LiDAR-based 3D object detection but does not extend its findings to other modalities or sensors. I'm interested in whether MOS can generalize to other types of data, such as inputs combining LiDAR point clouds and camera images.
2. While the paper contains empirical results for the chosen similarity metrics, more theoretical analysis for determining the synergy weights could be more thoroughly discussed.
3. It would be better if the authors could provide more clarity on how checkpoints are selected and what "unique insights" would improve understanding of the model selection process, I may not quite follow what's the insights here.
4. The rank-based feature-level and output-level similarity functions calculate the inverse Gram matrix, this method is novel but seems to be computational heavily. The paper provides some analysis of the MOS method in the last section, but it'll be great to have more discussion on how these similarity metrics scale with larger datasets or different types of models.

### Questions
Most questions are mentioned in the weakness section above.
Whether MOS can be generalized to other types of data, such as inputs combining LiDAR point clouds and camera images?
How checkpoints are selected and what "unique insights" would improve understanding of the model selection process?
How does the computational cost of calculating the synergy weights scale with the size of the model bank and batch size?
Also, I'm curious about if there's any evaluation of the impact of the proposed method on adaptation scenarios involving different types of LiDAR sensors or point cloud resolutions.
I appreciate the response to these questions.

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper explores the test-time adaptation for LiDAR-based 3D object detection and proposes a model synergy approach that leverages long-term knowledge from historical checkpoints to tackle this task. Experiments are shown to verify the approach by tested against existing test-time adaptation strategies across three datasets.

### Strengths
-The paper focuses on exploring test-time adaptation for 3D object detection and proposes a natural and effective model synergy strategy that dynamically assigns weights to historical checkpoints and aggregates knowledge to tackle task. 
-The paper analyzes and discusses the effectiveness of the synergy weights and makes task-specific modifications. 
-Experiments verifies the method's effectiveness under various conditions, outperforming comparison methods.
-The paper is well-writing and easy to follow.

### Weaknesses
The theory on which the method is based has been considered in prior works. The paper makes minor modifications specific to the 3D object detection task.
A few minor clarifications are required in approach introduction， I have elaborated in the following section

### Questions
To maintain feature diversity, the method assigns higher weights to checkpoints with unique insights. This may lead to more false positive results; how does the method address this issue?

Does improving accuracy at the cost of time and computational resources go against the original intent of test-time adaptation?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work proposes MOS, a framework that dynamically weights a sequence of models to create a more robust model based on the richness of new knowledge. MOS is evaluated in a test-time adaptation setting for LiDAR-based 3D object detection tasks. Experiments conducted in cross-dataset, cross-environment and cross-dataset&environment settings demonstrate the effectiveness of MOS.

### Strengths
- The concept of weighting checkpoints based on newly acquired knowledge is intriguing.
- The cross-dataset &environment setting can positively impact this field.
- This work is well-supported by experiments and ablation studies.

### Weaknesses
 - Additional visualization of detection results is needed, particularly a comparison between methods that do not use new-knowledge-based model aggregation and MOS.
- From Table 9, the reviewer observes that the pedestrian detection results are unsatisfactory, and from Table 8, the reviewer notes that the cyclist detection results could be improved. This could benefit from adding 2D supervision, as rich contextual and color information in 2D images can facilitate the detection of small objects. A similar approach is suggested in recent work: Approaching Outside: Scaling Unsupervised 3D Object Detection from 2D Scene (ECCV '24). The authors are encouraged to include relevant references and discussions.

### Questions
- From Figure 7, the reviewer notes that both the time and memory costs of MOS are increased. Do the authors have any ideas for optimizing this additional cost?
- The reviewer wonders about the average time cost of conducting one experiment.

### Soundness
3

### Presentation
3

### Contribution
3
