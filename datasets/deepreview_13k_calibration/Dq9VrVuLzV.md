# SyntheOcc: Synthesize Geometric-Controlled Street View Images through 3D Semantic MPIs

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5, 5

## Abstract
The advancement of autonomous driving is increasingly reliant on high-quality annotated datasets, especially in the task of 3D occupancy prediction, where the occupancy labels require dense 3D annotation with significant human effort. In this paper, we propose \methodname, which denotes a diffusion model that \uline{Synthe}size photorealistic and geometric-controlled images by conditioning \uline{Occ}upancy labels in driving scenarios. This yields an unlimited amount of diverse, annotated, and controllable datasets for applications like training perception models and simulation. SyntheOcc addresses the critical challenge of how to efficiently encode 3D geometric information as conditional input to a 2D diffusion model. Our approach innovatively incorporates 3D semantic multi-plane images (MPIs) to provide comprehensive and spatially aligned 3D scene descriptions for conditioning. As a result, SyntheOcc can generate photorealistic multi-view images and videos that faithfully align with the given geometric labels (semantics in 3D voxel space). Extensive qualitative and quantitative evaluations of SyntheOcc on the nuScenes dataset prove its effectiveness in generating controllable occupancy datasets that serve as an effective data augmentation to perception models.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper presents SyntheOcc, a method for generating multi-camera images and videos of driving scenarios, using occupancy and text prompt as guiding inputs. The innovation of SyntheOcc lies in its proposed MPI encoder, which projects the raw occupancy of different depth ranges onto the camera plane, combining them into semantic multiplane images. These semantic multiplane images are then encoded as guidance for image generation. The paper provides a robust qualitative and quantitative comparison of generated images and videos. Additionally, it demonstrates the performance of perception models trained on the synthetic data and tested on real validation sets, as well as perception models trained on real data and tested on synthetic validation sets, to validate the proximity of SyntheOcc-generated images to the real domain.

### Strengths
1. SyntheOcc has potential for generating rare long-tail data that could support downstream tasks in real-world scenarios.
2. The experiments are solid, offering extensive qualitative and quantitative comparisons. The key validation experiments, blending generated data with real data, are particularly convincing.

### Weaknesses
 - [W1] The paper does not include several very relevant work in the literature review. Most of the baselines used in the paper come from publications within the past two years. The reviewer feels that two relevant papers on camera simulation is missing [NewRef1] and [NewRef2] from the literature review.

- [W2] This paper does not compare against an important baseline UniSim [Yang et al., CVPR 2023].
While the proposed method is pure data-driven, is it possible to showcase the results on Pandaset used in the Unisim? It is unclear whether the proposed method is superior to UniSim as a camera image simulator or simply works well on Nuscenes dataset but does not generalize to other datasets (e.g., Pandaset, Waymo Open Dataset). The reviewer feels that such discussions and experimental comparisons are needed as a strong justification for acceptance.
  - [W2.1] It is important to understand whether the proposed method is transferrable to other datasets with minimum fine-tuning or adaptation. For example, as shown in Figure 6 of GeoSim paper [NewRef1], the same pipeline works for a different city in the Argoverse dataset.

- [W3] While the data augmentation experimental results are interesting (section 4.3, first two rows in Table 1), this paper does not comment on the role of synthetically generated data in nuScenes occupancy prediction.
  - [W3.1] The semantic categories with significant improvements are bus, traffic cones, trailer, driving surface, other flat, and sidewalk. It is unclear how and why synthetically generated data help for such categories but not the other categories. Is it possible to provide convincing qualitative examples with explanations?
  - [W3.2] Comment on the overall improvements to the driving system (e.g., behavior prediction and motion planning). How much does the long-tailed scene generation help the downstream tasks?

### Questions
What specific perception model was used in the experiments?

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
5

### Summary
This paper introduces SyntheOcc, a controllable camera image simulation framework in the autonomous driving domain. The proposed framework uses 3D semantic occupancy grid as the conditions for camera image simulation, where multi-plane semantic images (MPIs) projected from 3D semantic occupancy grids have been used as conditional input to a 2D diffusion model. The effectiveness of SyntheOcc is demonstrated through improved performance in Real-to-sim evaluation and Sim-to-real data augmentation on the NuScenes dataset.

### Strengths
- [S1: Quality] The paper has demonstrated extensive experimental results and showcased that the proposed method is superior under both real-to-sim evaluation and sim-to-real data augmentation, when compared against existing methods. The paper also includes ablation studies including the MPI encoder architecture and reweighing methods.

- [S2: Clarity] The proposed method is well described in detail with clear illustrations (e.g., Figure 1 and Figure 2).

### Weaknesses
1. The practicality of occupancy editing in 3D space should be addressed. It is crucial to automate or accelerate the editing process to make it feasible for practical applications requiring large amounts of data. The authors may report the time required to generate a new image through editing, and discuss possible solutions to scaling up data. Specifically, the current method requires manual manipulation of the 3D occupancy grid, which is not scalable for large scene generation or complex editing tasks. The authors should investigate methods to streamline this process, such as incorporating user-friendly interfaces or automatic object placement algorithms.
2. The paper use occupancy as a condition due to its spatial information. It would be beneficial to discuss the fundamental differences between using occupancy and using of depth&segmentation maps as conditions to control image generation [1]. Experimental comparisons between using depth&semantic maps versus occupancy as conditions could be conducted to evaluate metrics like FID and inference time. The authors should clarify how the choice of occupancy over depth and segmentation impacts the controllability and fidelity of the generated images, particularly in scenarios with occlusions or complex object arrangements. A more thorough analysis of the trade-offs between these conditioning methods is needed.
3. The multi-view consistency appears not so good. In Figure 5 (b) (c), the color of the car in the first row changes in the second and third images. The authors could includsa comparative analysis of the generation results from different models (e.g., MagicDrive) within the same scene. The color inconsistency across views suggests a potential weakness in the model's ability to maintain object identity across different viewpoints. This issue needs to be addressed to ensure the generated scenes are coherent and realistic. A quantitative analysis of multi-view consistency, beyond qualitative observations, would also be beneficial.
4. The concept of imbalance mentioned by the authors in Line 272 requires further clarification. It is essential for the authors to provide a detailed explanation of what this imbalance refers to and how it impacts their proposed framework. The authors should specify whether this imbalance refers to class imbalance, spatial imbalance, or another form of data distribution issue. Furthermore, they should elaborate on how this imbalance affects the training process and the quality of the generated images, and what steps they have taken to mitigate its effects.
5. The examples of editing provided in paper mostly revolve simple cars. In Figure 6, it would be beneficial to explore if the model can accurately move and position more complex, irregularly shaped vehicles or pedestrians to demonstrate the capability of the framework in generating new, diverse scenes. The current examples do not fully showcase the model's ability to handle complex object geometries and interactions. Testing the model with a wider range of object types and poses is necessary to demonstrate its robustness and versatility.
6. While the paper discusses some designs related to temporal consistency, only qualitative results are presented. It would be valuable for the authors to report metrics like FVD compared to existing works such as DrivingDiffusion and Panacea to provide a more comprehensive evaluation of the proposed framework. The lack of quantitative evaluation makes it difficult to assess the true performance of the model in terms of temporal consistency. The authors should provide a detailed analysis of the temporal stability of the generated videos, including metrics such as FVD and other relevant measures.
7. Missing reference: [2-4]

### Questions
Please address the questions raised in the weaknesses section.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces SytheOcc, a novel image generation framework enabling precise 3D geometric control for applications like 3D editing and dataset generation. By leveraging 3D semantic multiplane images (MPIs), the framework achieves finer geometry and semantic control, enhancing image quality and recognizability. Experimental results show the effectiveness of synthetic data in augmenting 3D occupancy prediction tasks, indicating a significant advancement over existing methods.

### Strengths
1. SytheOcc offers finer and precise 3D geometric control, allowing for intricate manipulation of object shapes and scene geometry, which is crucial for tasks like 3D editing and dataset generation.
2. Experimental results demonstrate that the synthetic data generated by SytheOcc exhibit better recognizability, indicating a substantial advancement in image quality over existing methods.
3. The synthetic data produced by SytheOcc prove to be highly effective for data augmentation in 3D occupancy prediction tasks, enhancing the performance and robustness of perception models in such applications.

### Weaknesses
1. The practicality of occupancy editing in 3D space should be addressed. It is crucial to automate or accelerate the editing process to make it feasible for practical applications requiring large amounts of data. The authors may report the time required to generate a new image through editing, and discuss possible solutions to scaling up data.
2. The paper use occupancy as a condition due to its spatial information. It would be beneficial to discuss the fundamental differences between using occupancy and using of depth&segmentation maps as conditions to control image generation [1]. Experimental comparisons between using depth&semantic maps versus occupancy as conditions could be conducted to evaluate metrics like FID and inference time.
3. The multi-view consistency appears not so good. In Figure 5 (b) (c), the color of the car in the first row changes in the second and third images. The authors could includsa comparative analysis of the generation results from different models (e.g., MagicDrive) within the same scene.
4. The concept of imbalance mentioned by the authors in Line 272 requires further clarification. It is essential for the authors to provide a detailed explanation of what this imbalance refers to and how it impacts their proposed framework.
5. The examples of editing provided in paper mostly revolve simple cars. In Figure 6, it would be beneficial to explore if the model can accurately move and position more complex, irregularly shaped vehicles or pedestrians to demonstrate the capability of the framework in generating new, diverse scenes.
6. While the paper discusses some designs related to temporal consistency, only qualitative results are presented. It would be valuable for the authors to report metrics like FVD compared to existing works such as DrivingDiffusion and Panacea to provide a more comprehensive evaluation of the proposed framework.
7. Missing reference: [2-4]

[1] UniControl: A Unified Diffusion Model for Controllable Visual Generation In the Wild

[2] Generalized Predictive Model for Autonomous Driving

[3] Vista: A Generalizable Driving World Model with High Fidelity and Versatile Controllability

[4] SimGen: Simulator-conditioned Driving Scene Generation

### Questions
By conducting these expanded experimental comparisons, the authors can more comprehensively validate their claims and provide more compelling evidence for the effectiveness of the proposed SytheOcc framework.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper proposes SyntheOcc, a novel image generation framework that can synthesize photorealistic and geometric-controlled street view images by conditioning on 3D occupancy labels. The key innovation is the use of 3D semantic multi-plane images (MPIs) to efficiently encode 3D geometric information as conditional input to the 2D diffusion model. The extensive experiments demonstrate that the synthetic data generated by SyntheOcc can effectively augment perception models for 3D occupancy prediction tasks.

### Strengths
1. The paper proposes an innovative approach by replacing ControlNet with multiplane images, enhancing image synchronization from occluded views.
2. The provided video effectively demonstrates and supports the proposed method.
3. The writing is clear and easy to follow.
4. The experiments are comprehensive, covering both quantitative and qualitative evaluations.

### Weaknesses
1. **Clarification on excluding ControlNet**: The paper should more thoroughly explain the decision to exclude ControlNet. The rationale for why ControlNet fails to meet 3D requirements remains unclear. Since multiplane images could serve as conditions for ControlNet.

2. **Incorporating KPM evaluation for consistency**: It would be beneficial for the paper to include KPM evaluations from Driving into the Future [1] to better assess temporal and multiview consistency.

3. **Additional out-of-domain results**: Presenting more out-of-domain results, such as experiments with variations in camera intrinsic and extrinsic parameters, would explain the ability of generalization of the model.

4. **Weak video quality**: Some objects in the provided video appear twisted or lack realistic representation. And the videos look a little bit unreal but I cannot tell why.

5. **World model integration**: Considering that driving scene generation works nowadays provides world model results—capable of forecasting future layouts and generating future images based on actions. It would be valuable for the paper to explore integration with world models. For example, testing if the generation method can be adapted to synthesize occupancy predictions, as seen in recent work on occupancy-based world models [2]. It will showcase potential for further real-world applications.

[1] Wang, Yuqi, et al. "Driving into the future: Multiview visual forecasting and planning with world model for autonomous driving." CVPR 2024.
[2] Zheng, Wenzhao, et al. "Occworld: Learning a 3d occupancy world model for autonomous driving." ECCV 2024

### Questions
I am still wondering why the paper cannot use ControlNet, as multiplane images are still images and could potentially be used as input for ControlNet.

### Soundness
2

### Presentation
2

### Contribution
2
