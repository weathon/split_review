# EmerNeRF: Emergent Spatial-Temporal Scene Decomposition via Self-Supervision

- Decision: Accept
- Scores: 6, 8, 8, 6

## Abstract
We present \method, a simple yet powerful approach for learning spatial-temporal representations of dynamic driving scenes. Grounded in neural fields, \method simultaneously captures scene geometry, appearance, motion, and semantics via self-bootstrapping. \method hinges upon two core components: First, it stratifies scenes into static and dynamic fields. This decomposition emerges purely from self-supervision, enabling our model to learn from general, in-the-wild data sources. Second, \method parameterizes an induced flow field from the dynamic field and uses this flow field to further aggregate multi-frame features, amplifying the rendering precision of dynamic objects. Coupling these three fields (static, dynamic, and flow) enables \method to represent highly-dynamic scenes self-sufficiently, without relying on ground truth object annotations or pre-trained models for dynamic object segmentation or optical flow estimation. Our method achieves state-of-the-art performance in sensor simulation, significantly outperforming previous methods when reconstructing static (+2.93 PSNR) and dynamic (+3.70 PSNR) scenes. In addition, to bolster \method's semantic generalization, we lift 2D visual foundation model features into 4D space-time and address a general positional bias in modern Transformers, significantly boosting 3D perception performance (e.g., 37.50\% relative improvement in occupancy prediction accuracy on average). Finally, we construct a diverse and challenging 120-sequence dataset to benchmark neural fields under extreme and highly-dynamic settings. 
See the project page for code, data, and request pre-trained models: {\small\url{https://emernerf.io}}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces EmerNeRF, an approach for learning spatial-temporal representations of dynamic scenes. EmerNeRF decomposes scenes into static and dynamic fields, with an additional scene flow field modeling the movement of objects across time. The dynamic feature is computed as a weighted sum of features from nearby timesteps, where the sampling operation is determined by the self-supervised scene flow field. Additionally, the paper proposes a method to generate positional encoding (PE) free features from a pretrained feature encoder by leveraging the time-consistent property of PE features. The empirical result indicates the proposed method can achieve better novel view synthesis, flow estimation, and few-shot semantic prediction results compared to the baselines.

### Strengths
- The proposed dataset holds potential value for research in dynamic scene reconstruction field
- EmerNeRF demonstrates better reconstruction quality in driving scene dataset compared to the baselines
- The obtained scene flow exhibits high accuracy compared to baseline method

### Weaknesses
 - Novelty. Many design components of EMerNeRF have been proposed in previous work, including separated static and dynamic fields [2,3], sky head [1], shadow head [2], flow field [4]. The paper lacks a detailed discussion highlighting the differences compared to these previous works, particularly regarding how the specific implementation and combination of these components leads to novel capabilities. The method seems to combine existing ideas without a clear explanation of how the integrated system achieves superior performance compared to simply using the individual components in isolation or other combinations.
- Generalizability. The proposed method lacks verification in existing dynamic scene datasets used in baselines such as Nerfies [5], HyperNeRF [6]. Those datasets contain more complex deformations and a significant proportion of dynamic components. It is necessary to evaluate the robustness and understand the limitations of the proposed design modules, including dynamic density regularization and self-supervised flow field. The absence of testing on these datasets makes it difficult to assess the method's ability to handle more challenging dynamic scenes and its potential for broader applicability.
- Ambiguity of equation 6. The meaning and formulation of the expectation of the dynamic density remain unclear. It is not clear how this expectation is computed in practice, and the paper should provide a more detailed explanation of the mathematical formulation and its implementation. This lack of clarity makes it difficult to assess the validity and impact of this regularization term.
- Baseline. The quantitative evaluation lacks a more recent baseline [7]. The absence of comparison with this recent state-of-the-art method makes it difficult to assess the relative performance of the proposed method and its contribution to the field.

### Questions
- What’s the novel components that EmerNeRF propses?
- How does EmerNeRF perform in more general dynamic scenes?
- How does EmerNeRF compare to recent newer baseline?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a neural field approach that can perform static-dynamic decomposition and scene flow estimation in challenging autonomous driving scenarios. A hybrid 4D scene representation consisting of static, dynamic, and flow fields is adopted and jointly trained with the goal of appearance and feature reconstruction. Experimentation reveals state-of-the-art performance in novel view synthesis and scene flow estimation.

### Strengths
This paper proposes an effective way of jointly modeling the static and dynamic scenes in the setting of autonomous driving. The method is technically sound, from the high-level idea of using hybrid representation for static and dynamic scenes and optimize them under the goal of appearance reconstruction to the details of carefully modeling sky and shadows in the framework.

Even though there is no direct flow supervision or well-adopted supervision such as flow based warping, it's quite novel to see the scene flow estimation "emerges" from the temporal aggregation of features for scene reconstruction.

The experimentation is thorough and the numerical improvements over baselines are obvious.

The writing and presentation of this paper are also pretty good and easy-to-follow.

### Weaknesses
It's good to see more visualization of the model output in the appendix. But it would also be good to include more qualitative comparisons against the baselines in addition to the quantitative results. Also, adding error maps would be more intuitive to highlight the difference.

There also seems to miss the runtime analysis and comparison. How long does this approach take for sensor simulation in training and test time, and how does it compare to the existing approaches? That would be an important piece of information.

### Questions
The experiment setup omit every 10th frame, resulting in 10% novel views for evaluation. It would be better to include ablation study on the sparsity of the sampling and how the method degrade with fewer training frames.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a NeRF based method for learning scene representation. By decomposing the loss function into two separate terms - one handling static elements of the scene and the other dynamic elements the model is able to separate the static and dynamic components with no extra supervision. The model also estimates scene flow in the process as part of the regularization. Finally the method is also applied to "lifting" 2D self-supervised representations (e.g. DINO) into 4D space by a combination of readout heads and a learned positional embedding which rectifies some of the issues associated with these SSL representations.

### Strengths
The paper presents a nice combination of ideas that have been floating around for a while, leveraging the strengths of different approaches in an appealing and relatively elegant way. 
The paper is well presented, well executed and results are impressive all in all (but see below) - this is a good paper.

### Weaknesses
I think there are a couple of weaknesses that may require addressing

* Ablation analysis is lacking - table C1 addresses some of the of the modeling decisions but there are more aspects I would have loved to see analyzed.
* Applicability - I may be wrong, but I feel the use of driving data together with a NeRF based method (that is, need to train on each scene separately) is a bit odd - usually in this use case one would want an online inference model (e.g. an encoder) which can infer elements and structure quickly as the car/robot drives around the scene. On the other hand I feel this is not widely applicable to other types of data (say free form natural scenes with lots of unstructured movement).
* There is a lot of focus on DINO/v2 features and their related issues - I am wondering if other SSL methods suffer from similar PE issues (specifically ones that handle motion such VideoMAE / Siamese MAE etc.)

### Questions
In relation to the above:

* How much dependance is there on LiDAR data? would this method work without direct depth supervision signals?
* It's not written explicitly in the paper - does the data include ground truth camera parameters? (extrinsic and intrinsic, I imagine the answer is yes)
* The dynamics regularization term is a bit simplistic as it is a simple minimization of total density for dynamic elements - have you tried other regularization methods? say assuming sparsity and so on?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes EmerNeRF to decompose a scene into static and dynamic components by learning from videos using a self-supervised manner. The authors further propose to lift visual features from foundation models into the 4D space, by learning a shared PE feature map and PE-free volumetric feature fields. The authors also construct a new benchmark by subsampling video sequences from the Waymo Open Dataset. The proposed method achieves good results on several tasks, including scene reconstruction, view synthesis, and occupancy prediction.

### Strengths
1. The proposed method is intuitive, simple yet effective, achieving promising results on several tasks
2. I like the study of PE patterns in vision foundation models and the solution to it. The visualization in Figure 1 is also good.

### Weaknesses
 **1. Method**
- First of all, the authors claim “no prior works in this field have explicitly modeled temporal correspondence for dynamic objects”, which is wrong. Some related works are missing here [A1-3].
- It seems to me that the formulation of Gao et al. [A2] is very similar to the proposed method. Except Gao et al. [A2] used: (1) MLP-based NeRF instead of hash grids; (2) separate RGB heads for static and dynamic branches; (3) Not using a sky branch. However, Gao et al. [A2] showed that their method would fail without the optical flow regularization. So I wonder what is the core reason that the proposed method can work while Gao et al. [A2] cannot. Is it due to the hash grid? Is it due to ground truth depth supervision (from lidar)? Is it due to the dataset being evaluated (multiview-view, vehicle motions are rigid and thus simpler)? Or is it due to the evaluation protocol (relatively easy to do view synthesis for frame interpolation)? While I prefer such a simple method, the reason that makes it work remains unclear to me.

**2. Experiments**
- For the results in Table 1 and Table 2, is visual feature distillation being used?
- Is it possible to show to number of parameters in Table 1?
- The comparisons with baselines in Table 1 also seems problematic. First, the authors project lidar points to image and use a L2 loss for depth regularization for HyperNeRF and D2NeRF, which is definitely worse than directly regularizing on lidar rays due to many reasons (e.g., projection error, possible occlusions). While the authors claim that neither of these two baselines support lidar ray sampling, it is actually not difficult to incorporate this functionality. An easier way is to use the same way to regularize depth in the proposed framework. Second, StreetSuRF has its own normal supervision and lidar ray preprocessing. Simply disabling them and use the same one as in the proposed method does not seem correct to me.
- While not necessary, would be good to see a comparison on the scene flow estimation task with a SOTA method [A4].

### Questions
Please see the weakness section.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
