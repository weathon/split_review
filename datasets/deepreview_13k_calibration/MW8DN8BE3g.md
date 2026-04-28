# Uni-Map: Unified Camera-LiDAR Perception for Robust HD Map Construction

- Decision: Reject
- Avg Score: 6.25
- Scores: 5, 6, 8, 6

## Abstract
High-definition (HD) map construction methods play a vital role in providing precise and comprehensive static environmental information essential for autonomous driving systems. The primary sensors used are cameras and LiDAR, with input configurations varying among camera-only, LiDAR-only, or camera-LiDAR fusion based on cost-performance considerations, while fusion-based methods typically perform the best. However, current methods face two major issues: high costs due to separate training and deployment for each input configuration, and low robustness when sensors are missing or corrupted. To address these challenges, we propose the Unified Robust HD Map Construction Network (Uni-Map), a single model designed to perform well across all input configurations. Our approach designs a novel Mixture Stack Modality (MSM) training scheme, allowing the map decoder to learn effectively from camera, LiDAR, and fused features. We also introduce a projector module to align Bird's Eye View features from different modalities into a shared space, enhancing representation learning and overall model performance. During inference, our model utilizes a switching modality strategy to adapt seamlessly to any input configuration, ensuring compatibility across various modalities. To evaluate the robustness of HD map construction methods, we designed 13 different sensor corruption scenarios and conducted extensive experiments comparing Uni-Map with state-of-the-art methods. Experimental results show that Uni-Map outperforms previous methods by a significant margin across both normal and corrupted modalities, demonstrating superior performance and robustness. Notably, our unified model surpasses independently trained camera-only, LiDAR-only, and camera-LiDAR MapTR models with a gain of 4.6, 5.6, and 5.6 mAP on the nuScenes dataset, respectively. The source code will be released.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a unified robust high-definition map construction network (Uni-Map), a single model suitable for all input configurations. They designed a novel Mixed Stack Modal (MSM) training scheme, enabling the map decoder to effectively learn information from camera, LiDAR, and fusion features. This paper also introduced a projection module to align BEV features from different modalities into a shared space, enhancing representation learning and overall model performance. During inference, the model employs a switching modality strategy to ensure compatibility with various modalities. The experiments show the effectiveness.

### Strengths
(1)This paper is well-written, and the experiments have also shown effectiveness.
(2)The structure of this paper is clear and intelligible, making it easy to apply in real-world scenarios.

### Weaknesses
 (1) The method presented in this paper is straightforward and lacks new insights. For example, the projector module is supervised (via gradient back-propagation) to implicitly align BEV features from different modalities and inputting stacked BEV features into the same map decoder increases the diversity of the BEV feature space. These operations are fairly obvious in sensor-fusion based methods. How to verify the MLP-based projector can achieve the alignment? I think the misalignment is mainly caused by the inaccurate Camera-to-BEV View Transform process? Why not apply the projector only on the camera BEV feature?  Additionally, is the stack operation on BEV features just concatenation? How does this differ from the fusion methods like BEVfuison[1] or Pointaugmenting[2]? 
(2) About the Inference Phase of the switching modality strategy,  what training strategy (e.g., loss functions) is used to ensure the effectiveness of the switching modality strategy during inference?

### Questions
Please see the Weaknesses section.

### Soundness
3

### Presentation
4

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This study addresses the challenges of generalizability and robustness in HD map construction by proposing Uni-Map, a model capable of handling different input configurations, including camera-only (C), LiDAR-only (L), and fused camera-LiDAR (C+L) modalities. This model is based on the MapTR model and employs a Mixture Stack Modality (MSM) training scheme, wherein each sample in the training batch is augmented to include all input configurations (C/L/C+L) by stacking along the batch dimension. The study introduces a projector module, a multi-layer perceptron designed to align BEV features across modalities into a shared representation space. The model's robustness is evaluated across 13 sensor corruption scenarios, including cases of missing inputs and corruption in camera, LiDAR, or both modalities simultaneously. The study provides in-depth comparisons with related work, rigorous ablation studies assessing the contributions of the MSM training scheme and projector module, and a t-SNE visualization.

### Strengths
1. **Originality:** The study proposes simple design changes like MSM batch augmentation and modality switching which are new to HD map construction literature.

2. **Quality & Significance:**
- Strong empirical results compared to prior work.
- The paper includes ablation experiments on several of the components.
- Extensive robustness analysis with 13 types of sensor corruptions.

### Weaknesses
1. **Motivation and Hypothesis:** The necessity for generalizability between C, L and C+L configurations is questionable. Typically, sensor configurations in autonomous systems are determined early, based on cost and performance considerations, making the flexibility to switch between modalities less relevant. While modality switching could theoretically enhance robustness, the current approach requires prior knowledge of the corrupted modality, which can be challenging to detect autonomously in real-world scenarios, especially with complex corruptions like LiDAR crosstalk. Furthermore, the paper does not adequately address the practical scenarios where such modality switching would be beneficial, given that autonomous vehicles are typically designed with a fixed sensor suite. The assumption that a system would need to dynamically switch between modalities is not well-justified, and the paper lacks a clear explanation of the specific use cases where this would be necessary or advantageous.
2. **Limited Novelty:**
- The MSM scheme essentially augments each batch by including samples in all three modalities (C/L/C+L), resembling data augmentation rather than a fundamentally novel training strategy. The reported performance improvements could result from this increased data (as the training time increases significantly; table 2) rather than an intrinsic improvement in the methodology. The paper does not provide sufficient analysis to isolate the effect of the MSM scheme from the simple increase in training data, making it difficult to ascertain the true contribution of this approach. A more rigorous analysis, perhaps by training the baseline model with a similar amount of data, is needed to validate this claim.
- The projector module is conceptually similar to BEV encoders, such as those in BEVFusion [1], which also align modality features to address misalignment. While the implementation may differ, the underlying purpose remains the same, raising questions about the novelty of this component in addressing feature misalignment. The paper does not provide a detailed comparison of the projector module with existing BEV encoders, making it difficult to assess its unique contributions. A more thorough analysis, including a comparison of the architectural differences and performance characteristics, is needed to justify the novelty of this component.
- The claim that this is the first study to explore robustness in HD map construction (line 161) overlooks relevant prior work, such as the RoboDrive challenge [2] (and subsequent studies based on this), which addresses similar sensor corruption scenarios and includes additional corruption types. The paper fails to acknowledge the existing body of work on sensor robustness in autonomous driving, which undermines the claim of novelty in this area.

### Questions
1. How does the modality switching operate in practice? Is it automated, or does it require prior information about which modality to use, particularly in corruption cases?
2. Was corrupted data used solely for zero-shot analysis, or was it included in training? If included, was the MapTR baseline also trained with this data?
3. Could the authors clarify the total training data used (Table 2) and comment on whether the performance boost might stem from increased data, given that MSM triples the sample count per scenario?
4. How does the projector module differ from the BEV encoder used in BEVFusion?
5. Could the authors comment on whether modality switching is the best approach for handling corruptions, given that even a corrupted sensor may still provide valuable information, and completely discarding its data might not be optimal?

 I am open to updating my rating if the authors provide reasonable responses to these questions and address the mentioned weaknesses.

### Soundness
2

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
This paper introduces a new method for HD map construction. The proposed approach employs a simple but effective scheme (such as Projector Module and MSM Training) to project the BEV features of different modalities into a shared space, which leads to notable improvement for map construction under camera-only, Lidar-only and camera-LiDAR fusion settings. Besides, this approach also shows robustness on various multi-sensor corruption types.

### Strengths
1. This paper is well-written and easy to follow.
2. This paper provides extensive qualitative and quantitative experiments to support their claims.
3. This method is motivated and effective, which could also benefit other information fusion research, such as RGB-D segmentation.

### Weaknesses
1. From the Table 1 in  Experiment section,  previous state-of-the-art method for HD map construction is HIMap, which is different from the statement in Line 32 and Line 96.

### Questions
1. Is it appropriate to put Figure 9 from the Appendix to the main body of the paper and put Table 4 to the Appendix?

### Soundness
4

### Presentation
3

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
Summary:

They proposed a novel Unified Robust HD Map Construction Network (UniMap): 

1. A novel Mixture Stack Modality (MSM) training scheme is proposed to allow the map decoder to glean rich knowledge from the camera, LiDAR, or fused features.

2. A novel projector module is presented to map Bird’s Eye View (BEV) features of different modalities into a shared space.

3. A switching modality strategy is designed to enable precise predictions by Uni-Map when utilizing arbitrary modality inputs.

4. Extensive experiments demonstrate that Uni-Map can achieve high performance in different input configurations while reducing the training and deployment costs of the model.

### Strengths
Strengths:

1. Very careful and detailed analysis of HD map construction task.
2. Very clear figure presentation (i.e. Fig. 2 and Fig. 3 and Fig. 6). The readers are easy to follow the manuscript.
3. Very extensive experiments are conducted in Experiment section and Appendix. 
4. Problem configuration is meaningful to the field of autonomous driving.

These strengths reflect that the authors are the experts in this field.

### Weaknesses
Weaknesses:

1. Method does not have sufficient theoretical analysis, or theoretical insight. Method section contains lots of engineering details. 
2. Why the switching modality strategy can be seamlessly adapted to arbitrary modality inputs?
3. Why MLPs in Eqs. (1-3) work well?  

Although extensive expierments show the effectiveness of the proposed method, there lack sufficient theoretical analysis or convincing explanations in their method section.

### Questions
Although extensive expierments show the effectiveness of the proposed method, there lack sufficient theoretical analysis or convincing explanations in their method section. Based on this fact, I have to rate this paper as marginally above the acceptance threshold.

### Soundness
3

### Presentation
3

### Contribution
3
