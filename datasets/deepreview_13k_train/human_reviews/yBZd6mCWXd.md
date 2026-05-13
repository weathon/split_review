# WI3D: Weakly Incremental 3D Detection via Visual Prompts

- Decision: Reject
- Scores: 5, 5, 6

## Abstract
Class-incremental 3D object detection demands a 3D detector to locate and recognize novel categories in a stream fashion, while not forgetting its previously learned knowledge. However, existing methods require delicate 3D annotations for learning novel categories, resulting in significant labeling cost. To this end, we explore a label-efficient approach called Weakly Incremental 3D object Detection (WI3D), which teaches a 3D detector to learn new object classes using cost-effective 2D visual prompts. For that, we propose a framework that infuses (i) class-agnostic pseudo label refinement module for high-quality 3D pseudo labels generation, (ii) cross-modal knowledge transfer for representation learning of novel classes, and (iii) reweighting knowledge distillation for preserving old class information. Extensive experiments under different incremental settings on both SUN-RGBD and ScanNet show that our approach learns well to detect novel classes while effectively preserving knowledge of base classes, and surpasses baseline approaches in WI3D scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a method for class-incremental learning of 3D detection in RGBD pointcloud data. The method begins with a 3D detector trained on the base classes, and a 2D detector trained on all classes, and then attempts to transfer the novel-class knowledge from the 2D model to the 3D one. The method involves generating pseudo-labels using the 2D model, and then correcting these using the 3D model, and then training the 3D model with its own estimates. The method also incorporates two regularization losses, called the "Cross-Modal Knowledge Transfer" loss which increases cosine similarity between the 2D features and the 3D ones, and a "Reweighting Knowledge Distillation" loss that does a similar thing but (1) with a learnable weighting and (2) applied to logits too.

### Strengths
This paper is fairly well written, and does not make large over-claims about the novelty or impact or results. The figures are helpful in understanding the work. The method does well against its main considered baseline, SDCoT.

### Weaknesses
I have a variety of clarification questions that I hope the authors can address. I will put them into the Questions tab. 

One clear weakness might be the evaluation. Why is there only one baseline in the evaluation? Other parts of the paper seem to acknowledge three closely related works: Zhao & Lee, 2022; Zhao et al., 2022; Liang et al., 2023. Is it possible to compare against all of them?

### Questions
The paper says "Inspired by the human visual system that excels at learning new 3D concepts through 2D images, we propose to incrementally introduce novel concepts to a 3D detector with the visual prompts generated from a cost-free 2D teacher other than revisiting 3D annotations for both base and novel classes as shown in Fig. 1." I do not understand the connection to the human visual system. I do not understand what it means for visual prompts to be "generated from a cost-free 2D teacher other than revisiting 3D annotations for both base and novel classes". 

In Figure 2 it's unclear to me what method was used to generate the 3D boxes. The one in column b is especially egregious, since it seems like this does not even meet the edges of a plausible 2D box. 

The method section says that it will "pose the noise of 3D pseudo labels directly generated from 2D predictions" and I don't know what this means. (What does it mean for noise to be posed or unposed?)

Section 3.1 says "we adopt a simple way to generate coarse 3D pseudo labels from 2D preditions" but it is never made clear what this method is. 

Section 3.3 introduces a module called PRF which produces an offset to a given box. It is unclear how this module is trained. (Where do the ground-truth offsets come from? Does this training happen on all classes, or just base classes, or just novel classes?)

Section 3.3 introduces a module called BCH, which to my understanding takes the exact same input as the PRF module. If this is the case, it would be great to say so in the text, instead of re-stating the list of inputs as if it were unique. Also, it is unclear to me how this BCH module is trained. (Where does the ground truth "presence" label come from?) 

Section 3.4 mentions difficulties associated with "extracting regional representations". This is fine, except that this is the first time in the method that regional representations are ever mentioned. What are they? 

Section 3.4 mentions briefly that the IOU between the 2D predictions and the projected 3D predictions will be used "the cost function", but there is no equation given for this, and it's unclear to me if this is really one of the training objectives in Section 3.5. What is the exact form of the supervision? (Is it maybe the generalized differentiable IOU from Rezatofighi et al.?)




how to introduces -> how to introduce 

Pseuod -> Pseudo

preditions -> predictions

objectiveness -> objectness

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper addresses a novel task, which involves substituting 3D annotations of novel classes in class-incremental 3D object detection with 2D supervisions from images, termed Weakly Incremental 3D Object Detection (WI3D). The authors present a framework that extends the class-incremental 3D object detection method SDCoT. They adopt an existing approach for weakly supervised monocular 3D object detection to generate coarse 3D pseudo labels for novel classes. To address the challenges posed by noisy pseudo labels, they introduce a Pseudo Label Refinement (PLR) module, which directly refines these labels. Additionally, the authors employ cross-modal knowledge transfer techniques to enhance the robustness of the learned representation. Furthermore, they modify the base knowledge distillation loss within SDCoT that is used to mitigate the catastrophic forgetting of base knowledge. The proposed method is evaluated on two benchmark indoor datasets, under the batch incremental 3D object detection setting as proposed in SDCoT.

### Strengths
1. The problem of Weakly Incremental 3D Object Detection addressed in this paper is indeed a valuable area of exploration as it holds the potential to reduce annotation requirements significantly.
2. The proposed framework seamlessly integrates several pre-existing techniques, forming a technically sound architecture. The rationale behind the incorporation of each module is well-founded.

### Weaknesses
 **1. The paper could benefit from providing more detailed and clear explanations.**

Firstly, the method for generating coarse pseudo labels is not clearly presented. While the authors mention adopting a method from (Peng et al., 2021), the specifics of this method need further clarification. It's essential to note that the method in Peng 2021 is intended for outdoor Lidar point clouds, which have different characteristics from indoor point clouds. Moreover, the process for predicting 3D object boxes in Peng 2021 may not be straightforward and may involve model training. Therefore, the paper should provide more details on how these coarse pseudo labels are generated, including the specific clustering algorithm and parameters used to group points within projected 2D bounding boxes, and how they adapt to the indoor point cloud setting. The paper should also clarify whether the 3D bounding box estimation involves PCA or another method, and how the rotation, center, and size are determined.

Secondly, the architecture and training strategy of the PLR module lack detailed explanations. Key aspects, such as the normalization step in Fig. 4, require clarification. Specifically, the paper should specify how the point cloud coordinates, as well as the center coordinates and dimensions of the pseudo boxes, are normalized. Additionally, the training process of the PLR module in Stage 1, whether it is trained alongside the 3D detection backbone or separately, is not clear. The paper should clarify whether the PLR module is trained end-to-end with the 3D detection network, or if it is trained in a separate stage, and what loss function is used to train the PLR module itself.

Thirdly, when comparing with SDCoT, the authors mention they “modify the training of SDCoT (Zhao & Lee, 2022) to fit our weakly incremental learning setting”, but there lacks a specific description of this modification (e.g., how to obtain annotations for novel classes). Also, the details of the fine-tuning and freeze-and-add setup in the WI3D task need to be clarified. The paper should specify exactly how the pseudo-labels are incorporated into the SDCoT training procedure, and what changes are made to the loss function or training process. Furthermore, the paper should define what parameters are fine-tuned in the fine-tuning setup, and which parameters are frozen in the freeze-and-add setup.

Fourthly, the paper mentions splitting the category set into C_base and C_novel according to SDCoT, but the procedure is not identical to SDCoT (e.g., comparing Table 1 in this paper vs. Table 1 in SDCoT). The paper should clarify the exact procedure for selecting the base and novel classes, and how this differs from the original SDCoT paper, if at all. The paper should also explain why the class splits are different from SDCoT, if that is the case.

Lastly, the term "vanilla" in Table 5 needs clarification. The distinction between "vanilla" and "ours" is not made clear. The paper should explicitly state what components are included in the "vanilla" version and what is added to achieve the "ours" results.

**2. While the overall framework is sound, the paper's technical contributions are subject to doubt.**

Firstly, the PLR module appears to share significant similarities with the BoxPC network in [REF1], which is also designed to refine pseudo labels for novel classes by predicting 3D bounding box residuals and binary probabilities. The paper should provide a more detailed comparison of the two methods, highlighting the key differences in network architecture, loss functions, and training procedures. The paper should also address the specific novelty of the PLR module compared to BoxPC, beyond the differences in motivation and settings.

Secondly, when designing the intra-modal base knowledge distillation, the authors argue that “previous work usually directly utilizes all the predicted responses and treat knowledge equally.” As such, the reweighting modulation factor alpha_i should be the major modification compared to SDCoT. However, the authors omit comparing it with the version that removes alpha in the ablation study (refer to Table 7). This omission makes it challenging to discern the contribution of this modification. The paper should include an ablation study that specifically evaluates the impact of the reweighting factor alpha_i on the performance of the knowledge distillation.

**3. The paper does not present results in the sequential incremental learning setting, which is a common evaluation setting in Class-Incremental Learning.**

**4. The paper would benefit from visualization**, particularly in the form of 2D-3D bounding box pairs (bipartite matching results). Additionally, the validity of the example shown in Fig 2(a) is in question. I suspect such a misalignment might only occur when the 2D bounding box is entirely incorrect. The authors should provide a more detailed explanation or real-world examples to support the claim made in this figure.

### Questions
Please refer to the comments in the weaknesses section.

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposed a framework WI3D, using cost-effective 2D visual prompts for weakly class-incremental 3D object detection, which is an unexplored but important field. Under the supervision of intra- and inter- modal teacher in both feature space and output space, WI3D could effectively learn the novel classes while retaining the knowledge of base classes. Experiments conducted on SUN RGB-D and ScanNet show that WI3D outperforms all other methods in weakly-supervised manner.

### Strengths
1. The topic of weakly incremental 3D detection is quite novel.
2. The paper makes clear illustrations of the major challenges and problems that need to be solved and proposes effective solutions correspondingly. And weaknesses of the proposed method are also clearly illustrated. 
3. The proposed method is simple and easy to implement. 
4. WI3D could reach relatively better performance. The extensive ablation study and analysis demonstrate the effectiveness of the proposed components.

### Weaknesses
1. There are two concerns about the method: (1) While generating the coarse pseudo labels, the method proposed in WEAKM3D is used. However, WEAKM3D is designed for the outdoor dataset, which is much sparser and instances are separate. It might lead to some failures and lower the quality of refined pseudo labels. Specifically, the DBSCAN clustering used in WEAKM3D might not be optimal for indoor scenes where objects are often densely packed and occluded, potentially leading to merged or fragmented pseudo-labels. (2) The knowledge transfer is only conducted on novel classes, while base classes still keep the original representation. This could create a representational divergence between novel and base classes, as the novel classes are explicitly encouraged to align with the teacher network's output, while base classes are not, which may lead to suboptimal performance when both types of classes are present in a scene.
2. Most technical parts can be found in other works and the technical contribution is marginal. The core idea of using pseudo-labels for weakly supervised learning and knowledge distillation for incremental learning are not novel. The specific implementation details, such as the feature projection and reweighting modulation, also appear to be incremental improvements over existing techniques.
3. Some illustrations are not clear, e.g., how does teacher predict reweighting modulation factor; the “fine-tuning” method in 4.2 is described as “tune the whole model on novel classes”, while in I3DOD (Liang et al., 2023) and SDCoT (Zhao & Lee, 2022), it was described as “tune all parameters (except the old classifier) with a new classifier for C_novel”, I am not sure whether they are the same; what does vanilla method stands for in Table 5. The description of the reweighting modulation factor lacks clarity on how the objectness score is calculated and used to modulate the learning process. The distinction between tuning the 'whole model' and 'all parameters except the old classifier' needs to be clarified, as these two descriptions can lead to different interpretations.
4. The quality of pseudo labels is of great importance. It would be better to show the mAP or recall of refined pseudo labels for further analysis, which is also a more intuitional way to clarify the effectiveness of PRF module. Without a quantitative assessment of the pseudo-label quality, it is difficult to ascertain the true contribution of the proposed pseudo-label refinement module. Providing metrics like precision, recall, and mAP for both coarse and refined pseudo-labels would provide a more comprehensive understanding of its effectiveness.
5. The number of stages and total classes is a little small. I wonder how the method will scale under more learning stages and more classes (e.g. 10 stages for ScanNet200). The current evaluation is limited to a small number of incremental stages and classes, which doesn't provide sufficient evidence on the scalability and robustness of the proposed method. Testing on more challenging scenarios with more stages and classes is necessary to demonstrate the method's practical applicability.

### Questions
1. “Weakm3d: Towards weakly supervised monocular 3d object detection.” was published in 2022 but not in 2021 as mentioned in the reference. You need to check the references carefully.
2. It would be better to show the performance of WI3D on outdoor datasets as supplementary experiments, for these are widely used for some promising areas like autonomous driving.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
