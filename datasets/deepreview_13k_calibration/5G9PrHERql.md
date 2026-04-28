# F2M-Reg: Unsupervised RGB-D Registration with Frame-to-Model Optimization

- Decision: Reject
- Avg Score: 6.00
- Scores: 5, 5, 8, 6

## Abstract
This paper focuses on training a robust RGB-D registration model without ground-truth pose supervision.
Existing methods usually adopt a pairwise training strategy based on differentiable rendering, which enforces the photometric and the geometric consistency between the two registered frames as supervision. However, this frame-to-frame framework suffers from poor multi-view consistency due to factors such as lighting changes, geometry occlusion and reflective materials. In this paper, we present F2M-Reg, a novel frame-to-model optimization framework for unsupervised RGB-D registration. Instead of frame-to-frame consistency, we leverage the neural implicit field as a global model of the scene and use the consistency between the input and the rerendered frames for pose optimization. This design can significantly improve the robustness in scenarios with poor multi-view consistency and provides better learning signal for the registration model. Furthermore, to facilitate the neural field optimization, we create a synthetic dataset, Sim-RGBD, through a photo-realistic simulator to warm up the registration model. By first training the registration model on Sim-RGBD and later unsupervisedly fine-tuning on real data, our framework enables distilling the capability of feature extraction and registration from simulation to reality. Our method outperforms the state-of-the-art counterparts on two popular indoor RGB-D datasets, ScanNet and 3DMatch. Code and models will be released for paper reproduction.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a frame-to-model optimization framework guided by a neural implicit field for unsupervised RGB-D registration. By introducing the differential rendering capabilities of neural radiance fields, better pose supervision can be achieved.  Meanwhile，this paper creates a synthetic dataset for warming up registration model.

### Strengths
1. The paper introduces neural radiance fields to provide global information for the registration training
2. It builds a synthetic dataset to pretrain the model, ensuring the rationality of pose initialization.

### Weaknesses
1. The comparison with existing work seems unfair:  

   - sota methods like PointMBF are trained purely without supervision while the proposed method requires extra dataset with pose labels. In Table 1, the metrics of the proposed method looks slight better than existing unsupervised data. Does the improvement come from the benefit of including extra dataset? Please provide results without the boostrap using the process of training the registration model on the Sim-RGBD dataset for Table 1. Or please consider other ways to make a fair comparison. Will other work benefit the extra dataset with pose labels as well?

   -  In line 368-370, the authors propose to evaluate more difficult setting “evaluating view pairs sampled 50 frames apart” and mentioned “However, due to insufficient overlap in some segments of the data for pairs sampled 50 frames apart, the evaluation significantly distorts both the mean and median values. As a result, we have chosen not to include these results in our experimental presentation.” My question: why this 50 frames apart setting? Also if the insufficient overlap pairs are excluded, 

2. The influence of the warming up dataset is not studied. How large the warming up dataset should be? How similar the warming up dataset should be to the target datasets? What’s is the influence of number objects of ShapeNet on the final metrics? For the construction of datasets, there are already many synthetic datasets for indoor scenes, such as Replica and Habitat. This paper does not demonstrate the advantages of the custom dataset compared to other datasets. 

3. The training efficiency. As NeRF is very slow in training, the proposed method should require much more computation resources than PointMBF and hard to scale.

### Questions
See weakness

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper presents F2M-Reg, an unsupervised RGB-D registration framework that addresses the frame-to-frame registration task by dealing with multi-view inconsistencies with bootstrapping with a synthetic dataset.

### Strengths
1. F2M-Reg stands out by shifting from a frame-to-frame to a frame-to-model approach for RGB-D registration, which is an extension of existing approaches in the context of unsupervised 3D vision tasks. 
2. This use of a neural implicit field as a global scene model to capture broader scene-level information is a possible direction to handle complex conditions, such as low overlap and lighting changes, where traditional methods often fall short.
 3. The introduction of a synthetic bootstrapping dataset, Sim-RGBD, bridges the gap between synthetic and real-world performance in unsupervised settings, which is a notable improvement in unsupervised model initialization.

### Weaknesses
1. Although F2M-Reg is compared with several baselines, it is unclear where the improvement comes from. According to Table 4, the results without bootstrapping are not exciting enough.
2. In order to evaluate the effectiveness of the neural implicit field-guided mechanism, this paper needs additional experiments and comparisons with SOTA approaches without bootstrapping.

### Questions
See weakness.

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
The paper introduces an unsupervised method for robust RGB-D registration without ground-truth pose supervision. Unlike prior methods that rely on frame-to-frame photometric and geometric consistency, which are often affected by lighting changes, occlusion, and reflective materials, F2M-Reg employs a frame-to-model approach. The method begins with pre-training the model on a synthetic dataset, Sim-RGBD, with ground-truth poses, and subsequently fine-tunes it on real-world datasets without ground-truth poses by leveraging a neural implicit field as a 3D scene representation for pose optimization. This approach enhances robustness against multi-view inconsistencies, as demonstrated by experimental results comparing F2M-Reg with existing methods. In summary, F2M-Reg contributes a new unsupervised RGB-D registration framework, a synthetic dataset for initial model training, and an effective frame-to-model approach, setting new benchmarks on popular RGB-D datasets.

### Strengths
The paper identifies the limitations of frame-to-frame matching in unsupervised learning, particularly due to instabilities arising from lighting variations, occlusions, and reflective surfaces. The proposed frame-to-model matching, supported by a neural implicit field (NeRF), effectively mitigates these issues, demonstrating a significant improvement over traditional methods.

### Weaknesses
 - The use of the term bootstrap in the paper is potentially misleading. In deep learning, bootstrapping generally refers to iterative self-training, where a model refines itself by generating pseudo-labels and learning from them. The training on synthetic data described in this paper aligns more with pre-training. However, the fine-tuning on real datasets with initial poses refined through NeRF could be called bootstrapping.

- The performance gains from Sim-RGBD bootstrapping across different datasets is not quite consistent. Can the authors provide insights into why bootstrapping appears less critical for ScanNet compared to 3DMatch?

- NeRF optimization, particularly joint pose and neural field optimization, typically assumes static scenes. This assumption might limit the method's performance in dynamic environments. If this is indeed a constraint, it should be acknowledged in the paper. If not, could the authors clarify why the method remains effective in dynamic scenarios?

### Questions
- The performance gains from Sim-RGBD bootstrapping across different datasets is not quite consistent. Can the authors provide insights into why bootstrapping appears less critical for ScanNet compared to 3DMatch?

- NeRF optimization, particularly joint pose and neural field optimization, typically assumes static scenes. This assumption might limit the method's performance in dynamic environments. If this is indeed a constraint, it should be acknowledged in the paper. If not, could the authors clarify why the method remains effective in dynamic scenarios?

### Soundness
3

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
The paper introduced a method for RGB-D registration using frame-to-model optimization. The pipeline incorporates a pretrained registration model suing PointMBF and Co-SLAM for point cloud registration. The experiments on real-world ScanNet and 3DMatch datasets present the superiority of the proposed method. The ablation studies investigated the effectiveness of each components.

### Strengths
- The writing is comprehensive and easy to follow
- The proposed method demonstrates high performance compared to baseline methods on two real-world RGB-D datasets.
- The ablation study on the main text and supplementary materials are thorough and effectively showcases the efficacy of the proposed framework.

### Weaknesses
 - The proposed method should not be characterized as unsupervised learning as it claimed. Instead, it involves a registration model that has been pretrained on a synthetic RGB-D dataset and subsequently adapted to real-world RGB-D scenes during inference. Strictly speaking, the method aligns more precisely with a zero-shot learning approach. Please ensure the claims are accurately represented.

- The experiments could benefit from utilizing more recent datasets. The ScanNet-v2 dataset, while widely used, is dated and known for sensor noise that results in unreliable depth maps with many gaps containing zero or infinity values. More accurate and high-resolution RGB-D streams are available in newer datasets like ScanNet++ and TUM RGB-D. Conducting additional experiments on these recent datasets is recommended.

- The proposed pipeline incorporates Co-SLAM, which utilizes a tracking system for camera pose estimation, requiring that the input RGB-D stream strictly follow a time series. However, this requirement shows limitations for general RGB-D registration tasks that handle multi-view data, where the input does not necessarily adhere to a time-series format. In scenarios involving unordered data, the effectiveness of a SLAM system may be compromised.

### Questions
- The paper states that the frame-to-frame framework experiences difficulties in maintaining multi-view consistency due to issues like lighting variations, geometric occlusions, and reflective surfaces; however, NeRF encounters similar challenges under these conditions. It should be clarified how the frame-to-model approach addresses these limitations in comparison to the frame-to-frame method.

- In the proposed framework, initial poses are generated using a bootstrap method trained on synthetic RGB-D data. Considering that Co-SLAM, utilized for tracking within the proposed framework, also incorporates its pose initialization strategy based on constant movement assumption, how do these initial poses from the bootstrap method align or integrate with the initial pose assumptions in Co-SLAM? Specifically, please detail any adaptations or refinements made to ensure consistency between the poses initialized by F2M-Reg and the subsequent pose tracking performed by Co-SLAM,

- Please also discuss the limitations of the proposed methods.

### Soundness
3

### Presentation
3

### Contribution
3
