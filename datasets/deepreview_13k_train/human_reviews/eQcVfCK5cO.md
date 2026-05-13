# Where is the Invisible: Spatial-Temporal Reasoning with Object Permanence

- Decision: Reject
- Scores: 5, 5, 5, 5

## Abstract
Object permanence is a cognitive ability that enables humans to reason about the existence and location of objects that are not visible in the scene, such as those occluded or contained by other objects. This ability is crucial for visual object tracking, which aims to identify and localize the target object across video frames. However, most existing tracking methods rely on deep learning models that learn discriminative visual features from the visual context and fail to handle the cases where the object disappears from the image, e.g., occluded or contained by other objects. In this paper, we propose a novel framework for tracking invisible objects based on Qualitative-Quantitative Spatial-Temporal Reasoning (QQ-STR), inspired by the concept of object permanence. Our framework consists of three modules: a visual perception module, a qualitative spatial relation reasoner (SRR), and a quantitative relation-conditioned spatial-temporal relation analyst (SRA). The SRR module infers the qualitative relationship between each object and the target object based on the current and historical observations, while the SRA module predicts the quantitative location of the target object based on the inferred relationship and a diffusion model that captures the object's motion. We devise a self-supervised learning mechanism that does not require explicit relation annotations and leverages the predicted trajectories to locate the invisible object in videos. We evaluate our framework on a synthetic dataset (LA-CATER) and a new real-world RGB-D video dataset for invisible object tracking (iVOT) that contains challenging scenarios of human-object interactions with frequent occlusion and containment events. Our framework achieves comparable performance to state-of-the-art tracking methods that use additional relation annotations, demonstrating its generalization ability to novel scenes and viewpoints.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
NOTE: My review is fully re-edited on Nov.10 because what was written before is about another paper.

The paper proposed a new method, QQ-STR, for invisible object tracking.
QQ-STR mainly contains of 3 modules:
- A Visual Module (VM) consisting of an object detector and a human pose estimator for visual perception from input video frames.
- A Spatial Relation Reasoner (SRR) that generates possible spatial relationship graph for objects in each frame at every timestamp
- A Spatial-temporal Relation Analyst (SRA) that predicts possible trajectories and select the best one as the prediction

Experiments are done on 3 datasets including one proposed by the authors themselves and the results suggest QQ-STR can achieve better or comparable performance as previous state-of-the-arts. Ablation studies support some important design choices.

### Strengths
- Experiments are done on 3 datasets and show seemingly competitive results
- Adapt a diffusion model for trajectory generation looks interesting
- Some ablation studies are provided to support a few important design choices.

### Weaknesses
 - Many important details are not well explained or missing. For example, hand positions are extracted as in Sec. 3.3, but how it is being used is never mentioned in latter sections.

- Some parts don't make much sense. For example:
   - When generating spatial relationship graphs, do you distinguish occlusion and containment? If not, why?
   - Also, when generating the graphs, why do you only use object trajectories without identity information? The object characteristic should affect occlusion and containment, in my opinion.

- The method needs to "enumerate all possible spatial relations in the first frame and form the candidates PG1." This may cause some problems when there are too many objects.

- Despite a relative straightforward main idea of estimating occlusion / containment status based on past trajectories, there are a lot of twists and tweaks involved, for example, lots of hyperparameters and those correction stages, making the whole system over-complicated and vague to understand. The effects of most of them are unclear, and may hinder the generalizability to other datasets.

- The presentation needs to be improved. The whole idea is acutally Also, please double check inconsistent or incorrect notions, for example, "H_i = {(pl_i^t, pr_i^t), (pl_i^t, pr_i^t), . . . , (pl_i^t, pr_i^t)}" should be H_i = {(pl_i^1, pr_i^1), (pl_i^2, pr_i^2), . . . , (pl_i^t, pr_i^t)}

### Questions
Please address my concern according to the Weaknesses part.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
- The paper focuses on the problem of 2D bounding box-based object tracking under occlusion and containment.
The proposed approach is named QQ-STR, Qualitative-Quantitative Spatial-Temporal Reasoning. It has three components.
- a) Visual perception: Per frame object detection and human pose estimation using off-shelf methods. 
- b) Qualitative spatial relation reasoning: Predicts the spatial relationship between objects in a frame and considers multiple possible object relationships as a graph by maintaining potential candidates. 
- c) Quantitative relation-conditioned spatial-temporal relation analyst: Brings time into consideration. Error corrects and analyses the trajectory of the object. Helpful in tracking completely invisible objects.
- Evaluation is done on three datasets, LA-CATER, Liang et al. (2018), iVOT (collected by the authors).
- iVOT is RGB-D, 49 videos, 0.5 to 1.5 minute long - 12 scenes, 31k frames and 171 annotated trajectories.
- Baselines: OPNet (Shamsian et al. 2020), PA (Liang et al. 2021), RAM (Tokmakov et al. 2022), AAPA (Liang et al. 2021).
- The proposed method QQ-STR outperforms baselines on both synthetic and real datasets (mIoU metric).

### Strengths
- The paper is well-organized and easy to follow.
- The fundamental idea of using the graph structure for occlusion/containment reasoning for multi-object tracking is technically novel. The proposed modules make sense, and it is interesting to see the combination of the two components (qualitative and quantitative) working towards the state estimation of invisible objects.
- The experiments are done over multiple datasets, synthetic and real. The authors also contribute a dataset iVOT in this work, which is much appreciated. The scale of the dataset is also reasonably large compared to existing datasets focused on the same tasks.
- Ablations are done in Table. 4 to provide insights into the effectiveness of each components, SRR and SRA.

### Weaknesses
 - No qualitative results: There is no single image in the main paper visualizing the tracking results of the proposed method. 
Please consider showing multiple frames (which can be manually selected) of an object sequence and the tracked bounding boxes for QQ-STR and the closest baseline method (say RAM). This will tell us the improvements QQ-STR brings over the existing methods. If space permits, consider adding a failure case visualization highlighting the limitations. Note that the supplemental consists of two short videos (3 secs from Liang et al and 5 secs from LA-CATER) showing the results of the proposed method but no comparison to the baseline. It is a missed opportunity to not show video results on the collected iVOT dataset in the main paper or supplementary.

- Evaluation on the CATER dataset: Sec. 2 argues that the CATER dataset was not used in the evaluation as it only has classification and relation labels. However, in comparison to LA-CATER (the substitute), the CATER dataset is more widely used by current methods and has a more evolved list of quantitative performance of related methods. The results of the proposed method QQ-STR can still be evaluated on the CATER dataset, similar to the  CATER-Snitch localization task Table 1 of [1].

- Effect of number of objects on performance/Generalization: The proposed method considers all possible relations between the objects; the complexity of such a graph will increase when more objects come into the picture. This questions the ability of the method to generalize to conditions beyond five objects (which is the maximum used to show results). Testing on real-world tracking datasets like KITTIT (similar to RAM paper's Table. 2) would be a great way to showcase in-the-wild generalization of the proposed method.

- More descriptive method figures: Fig.1 and Fig.2 treat the proposed modules, VM, SRR, and SRA, as black boxes and tell nothing about the method. Please consider adding details about these components and provide insights into the inner workings of these blocks. Method figures are excellent visual tools to quickly convey the key ideas to the reader, which takes a while if it is only text-based (which is the case currently).

### Questions
As listed above,
1. Visual comparision of the QQ-STR and baseline.
2. CATER evaluation.
3. Going beyond the toy-object datasets, testing in-the-wild generalization.
4. Improved paper presentation (specific focus on the method figure).

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a qualitative-quantitative reasoning framework for tracking invisible objects. The proposed method consists of three main modules, where a visual perception module is used to embed visual frames, SRR module is used to generate spatial relations between different objects, and SRA module predicts the location of the object based on the inferred relationships and a diffusion model. Experiments are performed on both synthetic and real-world datasets. Besides, this paper proposes a real-world RGB-D dataset, containing various scene categories, longer sequences, and more complex spatial relations.

### Strengths
1. This paper proposes a real-world RGB-D dataset, which might be beneficial for future research on the related task.
2. This paper proposes a novel qualitative-quantitative reasoning framework, separating the explicit qualitative reasoning analysis and the quantitative location prediction, which might provide a new sight to solve object permanence.

### Weaknesses
1. The different modules in the proposed framework don’t look compact, but independent. The framework integrates many separate models to address separate problems, like an object detector, a human pose estimation, the correction module, and a diffusion-model-based trajectory predictor. These different models are also trained separately, but not in an end-to-end manner. The lack of end-to-end training raises concerns about the framework's ability to learn optimal representations and interactions between modules. The paper does not clearly articulate how the outputs of one module are effectively utilized as inputs for the subsequent module, and how the error signals are propagated through the entire system. Compared with SOTA methods, results in Table2 are also not evident enough to show the advantages brought by this kind of complex design. Besides, the framework seems to bring many hyperparameters, I think it's necessary to explain these hyperparameter settings, and also perform corresponding experiments to show the robustness of the proposed framework on different hyperparameter settings.

2. Some detailed designs are not explained clearly. For example:
(1) For the object detection model, the classification of the general detection task is to identify different categories of objects, while I think the proposed method needs an object-level classification, the paper didn't mention much about this. It is unclear how the object detector distinguishes between different instances of the same object category, which is crucial for tracking individual objects. The paper should clarify whether the object detector is instance-aware or if additional mechanisms are used to differentiate between object instances. (2) For the shiver error in the correction module, what if the size of the object itself changes in adjacent frames, like aspect ratio change or scale change? The paper does not address how the correction module handles changes in object appearance, such as scale or aspect ratio variations, which are common in real-world scenarios. The correction module's reliance on a fixed 'shiver error' seems inadequate for handling dynamic object transformations.

3. One of the main contributions of this paper is to propose a new dataset, however, there are very few descriptions of this new dataset. The paper lacks detailed information on the dataset's characteristics, such as the number of sequences, the average length of sequences, the diversity of scenes and object types, and the annotation process. Besides, there is also a lack of experimental results of SOTA methods on the proposed dataset iVOT (Table3).

4. The paper is a bit hard to read since:
(1) the definition and use of some variables and formulas seem a bit complicated and have some typos. For example, the definition of hand positions H_i, the use of t/T/k, inconsistent use of superscript and subscript on different formulas, and so on. (2) Fig1&2 are not connected tightly with text. The cases shown in the figures are not well explained in the text.

### Questions
Please find my concerns in the above "Weaknesses".
I am concerned most about issues 1,3 and 2 in order. I'll consider changing my rate if the authors explain them well.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
- This work proposes a novel method for tracking invisible/occluded objects in videos using object permanence from developmental psychology. 
- The proposed method consists of three modules, namely, a Visual perception Module (VM), a qualitative spatial relation reasoner (SRR) and a quantitative relation-conditioned spatio-temporal relation analyst (SRA). 
- The SRR module infers the spatial relationship between all the objects in a frame, i.e. whether the target object is occluded, using past and current information. The SRA module, modeled using a conditioned diffusion model, uses this information to predict the possible location of the target object in the future frame.
- Authors perform experiments on a synthetic and two real datasets and show competitive performance against contemporary methods.

### Strengths
- The use of diffusion models for tracking is interesting and useful to the community.

### Weaknesses
 - Looking at a high level, the current method mimics the classical Kalman and Particle filter very closely (predict future location based on past observations and update the posterior based on current observations). Given the similarities, I believe comparing to such classical methods is necessary. I'm sure with the power of deep networks, the proposed method can outperform such classical methods but it is essential to know the gap in performance. Are the deep networks even necessary or does Kalman filter just solve the synthetic dataset?
- Authors demonstrate results on two real world benchmarks but I believe some more experiments are necessary to properly understand the contributions. RAM (Tokmakov et.al.) show results on KITTI benchmark. The ID-Switch problem in Multi-Object Tracking (MOT) is a result of models failing to understand object permanence. If authors claim their method is good at reasoning object permanence, it is essential to report results on these tracking datasets. I don't expect the authors to show state-of-the-art performance on Tracking/MOT but showing that this work improves some metric, like reducing the number of ID switches, is a good indicator of this method working on real world data. I strongly recommend authors to perform these experiments and report results on these tasks and datasets.
- Also consider reporting results on Occluded Video Instance Segmentation (OVIS) dataset [1] which deals with segmenting occluded objects in videos. 
- A few design decisions haven't been ablated to understand their significance. Why did authors choose to go with diffusion models for object tracking? Why not go with the well tested trackers like SORT[2] or DeepSORT[3]? Or some recent state of the art MOT trackers [4]? I think this experiment is necessary to justify the use of diffusion models.

### Questions
**Kindly address the concerns mentioned in the Weakness section for me to improve my rating**
- Not a major issue but make sure the tables and figures in the paper appear at the top of the page. This is probably my own preference but I would like the authors to consider this, to make the paper look more professional.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
