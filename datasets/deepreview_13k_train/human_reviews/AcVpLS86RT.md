# Uni$^2$Det: Unified and Universal Framework for Prompt-Guided Multi-dataset 3D Detection

- Decision: Accept
- Scores: 8, 8, 6, 6

## Abstract
We present Uni$^2$Det, a brand new framework for unified and universal multi-dataset training on 3D detection, enabling robust performance across diverse domains and generalization to unseen domains. 
Due to substantial disparities in data distribution and variations in taxonomy across diverse domains, training such a detector by simply merging datasets poses a significant challenge. 
Motivated by this observation, we introduce multi-stage prompting modules for multi-dataset 3D detection, which leverages prompts based on the characteristics of corresponding datasets to mitigate existing differences. 
This elegant design facilitates seamless plug-and-play integration within various advanced 3D detection frameworks in a unified manner, while also allowing straightforward adaptation for universal applicability across datasets. 
Experiments are conducted across multiple dataset consolidation scenarios involving KITTI, Waymo, and nuScenes, demonstrating that our Uni$^2$Det outperforms existing methods by a large margin in multi-dataset training. 
Notably, results on zero-shot cross-dataset transfer validate the generalization capability of our proposed method.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper addresses a critical challenge in autonomous driving research: integrating multiple datasets collected across different locations and using varied sensor types, especially LiDAR-based detection datasets. Due to differences in distribution, such datasets cannot be directly combined for training without significant performance trade-offs. The authors propose a novel, multi-stage prompting approach to effectively leverage the unique characteristics of each dataset and mitigate modality disparities, ultimately enabling a more robust multi-dataset training framework. This multi-stage approach is designed as a plug-and-play module that enhances several advanced 3D detection frameworks by targeting three stages: voxelization, BEV feature processing, and the detection head. Experimental results substantiate that the proposed multi-dataset training technique significantly improves cross-domain performance relative to baseline models, showcasing its effectiveness in harnessing diverse datasets for training.

### Strengths
- The paper tackles a practical issue in autonomous driving, where dataset diversity can restrict the ability to scale training. By addressing how to integrate datasets with different characteristics, the research directly benefits the community by opening up avenues for broader dataset utilization, potentially enhancing the generalization of autonomous driving models.
- The proposed approach is modular, designed as a plug-and-play component compatible with various advanced 3D detectors.
- The use of frame-specific mean shifts for batch normalization is particularly novel. I’m curious whether this concept has been explored in existing literature or if it is an original contribution by the authors.
- The paper includes comprehensive experiments to validate its claims, showing that: (1) the method outperforms baselines like Uni3D, (2) it can be integrated with various 3D detectors, (3) each of the three prompting stages contributes to the improved performance, and (4) OCRL improves the alignment of object size distribution with ground truth data.
- The paper is well-organized and easy to follow, with clear figures. However, providing a list of all abbreviations in figure captions would enhance clarity.

### Weaknesses
While the paper is methodologically sound and well-supported by experiments, there are a few areas that could benefit from additional clarity and detail:
- For mean-shifted BN: 
1) The authors claim that mean-shifted BN introduces dataset-specific characteristics, yet the parameter \alpha appears to capture only frame-specific characteristics rather than broader dataset-level traits. A more intuitive approach might involve defining dataset-specific means and variances to capture the unique properties of each dataset more accurately. I suggest the authors discuss this alternative and clarify how frame-level mean shifts contribute to dataset-level adaptability. Specifically, it is unclear how frame-level shifts, which are inherently instance-based, can effectively capture the broader statistical properties of an entire dataset. The use of a single parameter \alpha for all frames also raises questions about the granularity of adaptation. It would be beneficial to understand if this parameter is learned, fixed, or dynamically computed, and how it is integrated within the model's architecture.
2) It remains unclear how the parameter \alpha is specified within the model. Further explanation of its determination, whether it is learned, fixed, or computed dynamically, would help readers understand its role in adapting the batch normalization to different datasets.
- For the BEV-based range masking component, the authors choose to concatenate the mask as an additional channel rather than directly masking out unwanted regions in the BEV representation. It would be valuable for the authors to provide a rationale for this choice. Specifically, how does the inclusion of the mask as a separate channel improve model performance or facilitate feature extraction compared to direct masking? A discussion on the impact of this approach on model interpretability and cross-domain generalization would also be insightful. It is not clear why the model would benefit from having the mask as an additional channel rather than directly applying it to the feature map. The implications of this design choice on the computational cost and memory usage should also be discussed.
- More discussion about the limitation when applying the approach to the real-world applications will be helpful. Specifically, the assumption that datasets share identical categories is a significant limitation. In real-world scenarios, datasets often feature diverse, non-overlapping, or missing categories, which could severely limit the applicability of the proposed method. Furthermore, the effectiveness of the approach in highly dynamic or heterogeneous environments, where the data distribution may change rapidly, needs to be addressed.

### Questions
Check weaknesses

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
2

### Summary
The paper introduces Uni2Det, a framework designed to tackle the challenges of 3D object detection across multiple datasets. By leveraging multi-stage prompting modules, Uni2Det aims to overcome data distribution discrepancies and enhance generalization capabilities. The framework is evaluated on datasets such as KITTI, Waymo, and nuScenes, demonstrating superior performance compared to existing methods.

### Strengths
(1) Innovative Techniques: 

The introduction of multi-stage prompting modules is a novel approach to address the differences in data distribution among various datasets, potentially setting a new standard for unified 3D detection frameworks.


(2) Comprehensive Experiments: 

The authors conducted extensive experiments across multiple prominent datasets, showing significant improvements in both multi-dataset training scenarios and zero-shot transfer performance. This thorough evaluation strengthens the validity of the proposed method.

(3) Robust Generalization: 

The framework shows impressive zero-shot capabilities, effectively adapting to unseen datasets without additional retraining. This highlights its potential for real-world applications where models need to perform well across diverse environments.

(4) Scalability: 

Uni2Det demonstrates improved scalability by effectively utilizing additional datasets for training, ensuring performance boosts without the pitfalls of negative transfer that other methods might suffer from.

### Weaknesses
(1) Complexity and Implementation:

The multi-stage prompting modules, while innovative, may introduce additional complexity to the framework. This could potentially affect the ease of implementation and deployment in practical scenarios, requiring more resources and expertise. The paper lacks a detailed discussion on the specific engineering challenges associated with implementing these modules, such as the potential for increased debugging complexity or the need for specialized hardware.

(2) Assumption of Identical Categories:

The framework relies on the assumption that datasets share identical categories, which limits its applicability to datasets with diverse or non-overlapping label spaces. This constraint could hinder the adoption of Uni2Det in broader applications. The paper does not explore how the framework would handle scenarios where datasets have unique object categories, or if it could be adapted to learn a shared embedding space for different label sets.

(3) Limited Component Analysis:

The paper could benefit from a more detailed analysis of how each component of the framework contributes to overall performance. Understanding the impact of each module could provide deeper insights and guide future improvements. For instance, the paper could include ablation studies that examine the performance impact of removing or modifying each prompting module individually, as well as combinations of modules.

(4) Computational Overhead:

The potential increase in computational requirements due to the additional modules is not thoroughly discussed. This could be a concern for deploying the framework in resource-constrained environments. The paper should include a more detailed breakdown of the computational costs associated with each module, such as the number of parameters, FLOPs, and memory usage, and how these compare to baseline methods.

### Questions
(1) Sensor Variability: 

How does Uni2Det perform when dealing with datasets that utilize sensors with significantly different specifications? Understanding this could provide insights into its robustness across various sensor setups. For example, how is the performance on indoor datasets like Scannet [2] or SUN-RGBD [1]. 

(2) Extension to Diverse Categories: 

Is it possible to extend the framework to handle datasets with richer categories, like some open-vocabulary 3d object detection works [3, 4]? This would enhance its applicability to a wider range of scenarios. Please provide discussions in the paper.

(3) Efficiency Considerations: 

What are the computational overhead and latency introduced by the multi-stage prompting modules? Providing metrics on efficiency would be beneficial for assessing practical deployment scenarios.

(4) Failure Case Analysis: 

Can the authors provide examples or analysis of scenarios where the framework might underperform? This would help in understanding its limitations and potential areas for improvement. Please include failure cases in the paper.

[1] Shuran Song, Samuel P Lichtenberg, and Jianxiong Xiao. Sun rgb-d: A rgb-d scene understanding benchmark suite. In CVPR, 2015.

[2] Angela Dai, Angel X Chang, Manolis Savva, Maciej Halber, Thomas Funkhouser, and Matthias Nießner. Scannet: Richly-annotated 3d reconstructions of indoor scenes. In CVPR, 2017.

[3] Y. Lu, C. Xu, X. Wei, X. Xie, M. Tomizuka, K. Keutzer, and S. Zhang, “Open-vocabulary point-cloud object detection without 3d annotation,” CVPR, 2023.

[4] Y. Cao, Y. Zeng, H. Xu, and D. Xu, “Coda: Collaborative novel box discovery and cross-modal alignment for open-vocabulary 3d object detection,” in NeurIPS, 2023.

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
4

### Summary
This paper proposes a multi-stage prompting pipeline to use multiple data sources to train one 3D detector. Specifically, they performed mean-shifted batch normalization, applied BEV-based masking, and trained a discriminator on object-conditioned residual using classification loss. The object-conditioned residual is added to the RoI feature for prediction.

### Strengths
1. The paper is easy to understand and has a clear structure.
2. De-meaning data across batches and within one instance is an interesting way to improve generalization. Using dataset-relevant information as prompts is also very interesting.
3. The performance seems good.

### Weaknesses
There are too few classes for evaluation, and the class domain is limited to autonomous driving scenarios. The authors mentioned this in section 3.1.

### Questions
1. In mean-shifted batch normalization, it would be helpful to further explain how to calculate the instance-specific mean. Additionally, it will be wonderful to compare the proposed method with an alternate approach of first de-mean data using instance-specific mean, following batch-wise demeaning without alpha weighting. Further more, what is the influence of completely discarding this stage, only using the backbone and the head?
2. In object-conditional residual learning, how is the dataset id encoded in training? Also, during testing on zero-shot datasets, does this pipeline obtain object-conditional residual before prediction? 
3. In testing, it will be interesting to see how the model performs on classes that do not intersect with existing class vocabulary. At the same time, applying this method to datasets with various scenes, i.e., indoor 3D detection datasets, could provide a broader perspective on its robustness.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this work, the authors propose Uni$^2$Det, a prompt-guided multi-dataset 3D object detection framework. In detail, the authors handle multi-dataset 3DOD from three perspectives (*i.e.*, voxelization, bev features, and detection head). First, the designed point distribution correctness uses instance- and batch-level normalization to deal with the distribution shift in different datasets. Further, the bev-based range masking can select features of corresponding areas of the different datasets. Finally, the authors propose object-conditioned residual learning to inject dataset-specific features into each instance to further decode the bounding boxes. Experiments show that the proposed method can achieve higher results on both in-domain and out-of-domain tasks.

### Strengths
- Experiments show that the proposed Uni$^2$Det can achieve SOTA performance on both cross-domain and multi-dataset training settings.
- The authors treat dataset-specific attributes as prompts which is quite interesting.

### Weaknesses
1. My first question is about the proposed BEV-based range masking. I wonder about the masking strategy during the inference phase. Do we need to know the dataset-specific point cloud range before evaluation? If so, what will happen when we do not know the point cloud range? Besides, in the domain generalization experiments, if we use the point cloud range of the target domain, it seems unfair since the domain-specific knowledge has already been injected into the model.
2. Further, I wonder about the performance using more recent 3D detection models. I fully understand that the authors chose PV-RCNN and Voxel R-CNN for a fair comparison. However, they have been proposed for several years.
3. Questions about experimental settings, especially hyperparameters. I need to know how the authors define the value of hyperparameters such as $\alpha$, there seem no ablation studies about this.
4. The motivation of point mean-shift normalization and object-conditional residual learning is similar to the data-level correction and semantic-level coupling and recoupling. Both of them first handle data-level shifts and then strengthen domain-specific features. The authors need to explain the advantages of the proposed methods.

### Questions
- I know MDF may represent multi-dataset fusion. However, the authors use MDT in the preliminary and then use MDF in the following section. This needs to be modified to avoid confusion.

### Soundness
2

### Presentation
2

### Contribution
2
