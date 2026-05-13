# X-Drive: Cross-modality Consistent Multi-Sensor Data Synthesis for Driving Scenarios

- Decision: Accept
- Scores: 6, 6, 5, 6

## Abstract
Recent advancements have exploited diffusion models for the synthesis of either LiDAR point clouds or camera image data in driving scenarios.
Despite their success in modeling single-modality data marginal distribution, there is an under-exploration in the mutual reliance between different modalities to describe complex driving scenes. %a specific street view.
To fill in this gap, we propose a novel framework, \ourmethod{}, to model the joint distribution of point clouds and multi-view images via a dual-branch latent diffusion model architecture.
Considering the distinct geometrical spaces of the two modalities, \ourmethod{} conditions the synthesis of each modality on the corresponding local regions from the other modality, ensuring better alignment and realism.
To further handle the spatial ambiguity during denoising, we design the cross-modality condition module based on epipolar lines to adaptively learn the cross-modality local correspondence.
Besides, \ourmethod{} allows for controllable generation through multi-level input conditions, including text, bounding box, image, and point clouds. Extensive results demonstrate the high-fidelity synthetic results of \ourmethod{} for both point clouds and multi-view images, adhering to input conditions while ensuring reliable cross-modality consistency.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces X-DRIVE, a novel framework for generating consistent multimodal data, specifically LiDAR point clouds and multi-view images, for autonomous driving scenarios. The key innovation of this paper is a cross-modality epipoplar condition module that bridges the geometrical gap under spatial ambiguity between point clouds and multi-view images, significantly enhancing modality consistency. Experimental results have demonstrated the effectiveness of the proposed method.

### Strengths
+ This paper introduces the first framework for the joint generation of LiDAR and camera data for autonomous driving scenarios. 

+ The proposed cross-modality epipolar condition module to enhance modality consistency makes sense and works well. 

+ The paper is well-written and easy to follow.

### Weaknesses
1. This paper presents a well-designed diffusion architecture for joint LiDAR and image data generation. My major concern is the novelty. This paper's main contribution is a cross-modality epipolar condition module for consistency constraints. However, epipolar attention for multi-view consistency has been extensively explored in multi-view diffusion models [1, 2, 3]. The core idea of using epipolar geometry to enforce consistency across views is not novel, and the paper needs to clearly articulate how their approach differs fundamentally from existing methods, beyond simply applying it to a different modality pairing. The paper should discuss the specific challenges in adapting epipolar constraints to the LiDAR-camera setting and how their method addresses these challenges in a novel way.

2. Experiments are only conducted on one dataset, nuScenes. This raises concerns about the generalizability of the proposed method. The nuScenes dataset, while comprehensive, may not fully represent the diversity of real-world autonomous driving scenarios. Testing on additional datasets with varying sensor configurations, environmental conditions, and scene complexities is crucial to validate the robustness of the approach. The paper should also include a discussion on the limitations of the nuScenes dataset and how these limitations might impact the performance of the proposed method.

3. It would be great to detail what kind of and how many GPUs are used, as well as the training/inference time. This information is crucial for reproducibility and for assessing the practical feasibility of the proposed method. The lack of detailed information regarding computational resources and time makes it difficult to evaluate the efficiency of the method.

### Questions
Is there a small mistake in Eq. (5)?

### Soundness
3

### Presentation
3

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
- This work proposes a novel technique to perform driving based lidar data generation in the form of range images, and multi-camera data generation while ensuring cross-modal alignment by leveraging latent diffusion models.
- Prior works address multi-camera image generation and lidar based generation individually while this work aims to perform joint generation of lidar and camera data. The major contribution here is in aligning the modalities during generation.
- During denoising of a first modality (camera or lidar), the information from the other modality (lidar or camera) is encoded and transformed into the geometrical space of the first modality (camera or lidar) to ensure alignment. They do this by finding matches from a second modality for a query from first modality by traversing the epipolar line in the second modality corresponding to the query.
- They show qualitative and quantitative results for conditional and unconditional generations. In addition, the authors also display controllability via bounding boxes and language interfaces.

### Strengths
- S1: The work addresses an important problem of lacking aligned lidar camera data. Solutions towards this can reduce/elimintate post-processing work of performing motion compensation via scene flow between consecutive pointcloud frames to address the lack of alignment. This is a cumbersome process.
- S2: The epipolar line based matching technique is neat, intuitive, and has been successfully been used before in literature [1].
- S3: The manuscript is well written and easy to follow. I also like the multi-view consistency results.

[1] Consistent View Synthesis with Pose-Guided Diffusion Models - https://arxiv.org/pdf/2303.17598

### Weaknesses
 - W1: Mapping pointclouds to range images leads to information loss. It is understandable the authors use range images since most of the existing lidar generation work uses range images and in addition, image based generation techniques are much more mature than pointcloud counterparts. However, the major goal here is to ensure alignment between the modalities and not to perform unimodal generations which have been addressed before. Therefore, I would expect point clouds to be effective in filling gaps caused by information loss especially during occlusions and in far ranges. The conversion from point clouds to range images involves a loss of information due to discretization and occlusion, and the subsequent reconstruction back to point clouds will not recover the original point density or coverage, particularly for distant points where collisions in the range image can occur. This is a critical issue since the goal is to synthesize sensor data, and the sensor data itself is in the form of point clouds, not range images. The use of range images as an intermediate representation introduces an unnecessary loss of fidelity.
- W2: I find the qualitative results of specifically the lidar generations lacking when viewed in the form of point clouds. Since the application of this work is to be used for training models, having distributional similarities (elaborated below) with real points is important to serve as valuable indictive biases and I doubt its utility without it.
    - Pattern realism: The lidar patterns shown in the pointcloud figures do not look realistic to me. For instance, the ground points on a rotating lidar typically show-up as thick concentric circles whereas results in supp. Fig 8 look very artificial to me. Comparing this to real pointclouds or even other synthetic lidar generation techniques from literature such as [2, 3], I see a gap that might be important to ignore for a downstream model. The concentric rings in the generated point clouds lack the circular precision seen in real data, and the breaks in these rings, intended to simulate rain, appear as random noise even in clear conditions. This suggests a lack of fidelity in the generation process, and the absence of motion compensation before range image conversion may be a contributing factor. The object shapes in the generated point clouds are not clearly discernible, and even a 32-channel LiDAR should be able to produce more recognizable object shapes than what is shown, especially when compared to results from prior work such as RangeLDM [3].
    - Object realism: The point clouds also lack object shape or object realism in the figures presented in Fig 6 of main paper. For instance, vehicles have a typical shape based on their orientation which are useful biases for a downstream network that consumes this data. These patterns are very evident in other synthetic techniques [2, 3] but seems to be lacking here. Similarly, on the range images for the multi-modal generations in Fig 4, very prominent cars in the scene do not have as many lidar points as I would expect. This was an objective of the work as stated in the manuscript (L64) which I don’t believe has been fully fulfiled. The generated point clouds do not accurately represent object shapes, and the density of points on objects in the generated range images does not match expectations based on real-world data. For instance, vehicles and pedestrians lack the characteristic point patterns that would be useful for downstream tasks. This is a significant issue, as the goal of the work is to generate data that can be used for training models, and the lack of realistic object representations limits the utility of the generated data.
    - Following similar theme, the points on the pedestrian in Fig 4 do not seem realistic to me.
- W3: Related to W2, since the larger goal of this work is to generate data that can be used for training, I would have expected to see results showcasing this utility. The manuscript in the current form does not convey the effectiveness of the data towards this.
- W4: The authors state one of the application is to address long-tail scenarios (L52). They do show results in rain and bounding box can be a way to inject situtations such as cut-ins. However, these are mainly shown in the visual space currently which is also illustrated by prior works such as [4, 5]. The primary evaluation of the work proposed here is not in judging effectiveness of visual generation but alignment between cross-modal generations. The current results in the manuscript do not show such OOD scenarios which can be validated in the point cloud and image space.

I am weighting W2 > W1 > W3 = W4.

### Questions
- Q1: Baseline setting for Tab 1: I don’t completely understand how MagicDrive + RangeLDM was combined to obtain cross-modality score? Was there anything done to ensure alignment between the different modalities from the two models?
- Q2:  I was wondering if the authors made the decision of studying this problem in range-image space based on empirical results or out of convenience (prior work)? In other words, was denoising in pointcloud space studied for this problem?
- Q3: (suggestion) I wonder if the evaluation metrics are unable to capture objectness of pointclouds. Athough not typical in generative learning, techniques like Iterative closest point (ICP) could be useful in measuring shape discrepancies.
- Q4: Performing denoising in each modality while encoding information from the other modality through the denoising time steps seems expensive. It would be helpful to provide the computation time split between the different stages? If possible, also relate it to time taken for unimodal generations.
- Q5: Was the zero initialization from ControlNet deemed necessary empirically? I’m curious if the authors observed any forgetting without it.
- Q6: It looks like the results for lidar to camera is far better than the multimodal and camera to lidar results to me. Do the authors agree? If so, since generating point clouds is difficult, would disnetangling the joint process to a sequential approach of first generating camera data and then performing conditional lidar generation be feasible?
- Q7: Have the authors looked at GenMM [6]? While they do not specifically tackle multi-modal generations, they target alignment between the two modalities using in-painting diffusion models. I wonder on similar lines to Q5 if their approach can be conducive to a sequential approach of using reference patches from camera generations to condition generating point cloud data leveraging in-painting.

Prioritization order: Q1 > Q2 = Q4 > Q7 = Q6 > Q5 > Q3

I welcome the authors to correct me if there was any misunderstanding on my part.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work proposes X-Drive, explicitly addressing LiDAR-image consistency in driving data synthesis. It designs (1) mutual conditioning between corresponding local regions across modalities, (2) an epipolar line-based conditioning module, and (3) multi-source input conditions to mitigate generation inconsistencies. Experiments on nuScenes validate the efficacy of the proposed method.

### Strengths
- The focus on consistency between LiDAR and image generation provides insights to this field.

### Weaknesses
 - Lack of quantitative comparison with baselines. In Table 1, the number of experiments conducted is insufficient to fully support this paper. The authors are encouraged to compare with more previous methods and implement additional vanilla baselines to better illustrate the advantages of X-Drive. Table 1 could be divided by modality and enriched separately.
- Lack of ablation studies. In Table 3, the ablation analysis is presented at a very coarse level. The authors are encouraged to detail the design of each module and analyze their individual impact on the final results.
- Marginal improvements. In Table 1, for JSD in the C→L setting, X-Drive only surpasses MagicDrive by 0.002, while RangeLDM surpasses LiDARGen by 0.106. For FID in the L→C setting, X-Drive only surpasses MagicDrive by 0.19, whereas MagicDrive surpasses BEVGen by 8.65.
- Numerous typos. For example, "several works emerges" in L103, "We extend the vanilla diffusion models to modeling" in L186-187, and "Our FID metric is outoerformed by MagicDrive" in L423-424. These errors should be reviewed and corrected to enhance the clarity and readability of the paper.

### Questions
- In Figure 1(b), what does the distribution at the bottom represent?
- In Figure 2, how is the generation of the LiDAR point cloud achieved?
- What are the additional time and memory costs of the designed module?
- What is the average generation time for one experiment?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
# Review Analysis of X-DRIVE Paper

## 1. Methodology and Key Innovations

### Primary Methods
- Proposed X-DRIVE framework: A dual-branch latent diffusion model architecture for simultaneous generation of LiDAR point clouds and multi-view camera images
- Designed Cross-modality Epipolar Condition Module to enhance consistency between different modalities
- Introduced 3D bounding boxes for geometric layout control and text prompts for attribute control (e.g. weather and lighting)

### Key Innovations
- First work to achieve joint generation of LiDAR point clouds and multi-view camera images with cross-modal consistency
- Novel epipolar-based cross-modal condition module addressing alignment between point clouds and images in different geometric spaces
- Multi-level controllable generation incorporating text, bounding boxes, images and point clouds as conditions

## 2. Innovation Analysis

### Limitations in Innovation
- Weak theoretical foundation for cross-modal consistency, lacking rigorous proof of epipolar-based design effectiveness
- Incomplete solution for "spatial ambiguity", relying solely on epipolar geometry may not fully resolve 3D space ambiguities
- Limited innovation in generation control, mainly applying existing control methods to new scenarios

## 3. Experimental Analysis

### Required Additional Experiments
- Evaluation of generated data utility in downstream tasks (3D object detection, trajectory prediction)
- Need to adopt more advanced transformer architectures like DiT instead of U-Net
- Consider replacing CLIP with T5 for potentially better performance
- Address low resolution issues affecting geometric shapes of distant objects (The current resolution is too low. Objects in the distance have no geometric shapes at all. However, the point cloud may have relatively complete and accurate geometric shapes in the distance. A larger resolution should be used, and because the generated image has slightly less geometric shapes in the distance, the effect is not good, simple and practical super-resolution model. It can only increase the resolution but cannot improve the distant geometry.)
- Investigate video generation capabilities with 3D VAE and 3D attention mechanisms
- Develop quantitative metrics for cross-modal consistency evaluation

## 4. Ablation Study Analysis

### Missing Ablation Studies
- Detailed component-wise analysis of cross-modal epipolar condition module
- Impact assessment of different condition types on generation quality
- Sensitivity analysis of key hyperparameters
- Investigation of different training strategies

## 5. Advanced Experiments (Optional)

### Long-tail Data Generation
- Potential for generating rare/corner cases
- Ability to synthesize challenging scenarios
- Evaluation of model performance on long-tail distributions

## Overall Assessment
While the paper presents novel contributions in cross-modal data generation, it requires strengthening in theoretical foundations, experimental validation, and analysis depth. The framework shows promise but needs additional experiments and rigorous evaluation to fully demonstrate its capabilities.

### Strengths
- First work to achieve joint generation of LiDAR point clouds and multi-view camera images with cross-modal consistency
- Novel epipolar-based cross-modal condition module addressing alignment between point clouds and images in different geometric spaces
- Multi-level controllable generation incorporating text, bounding boxes, images and point clouds as conditions

### Weaknesses
## Limitations in Innovation
- Weak theoretical foundation for cross-modal consistency, lacking rigorous proof of epipolar-based design effectiveness
- Incomplete solution for "spatial ambiguity", relying solely on epipolar geometry may not fully resolve 3D space ambiguities
- Limited innovation in generation control, mainly applying existing control methods to new scenarios

## Experimental Analysis

### Required Additional Experiments
- Evaluation of generated data utility in downstream tasks (3D object detection, trajectory prediction)
- Need to adopt more advanced transformer architectures like DiT instead of U-Net
- Consider replacing CLIP with T5 for potentially better performance
- Address low resolution issues affecting geometric shapes of distant objects (The current resolution is too low. Objects in the distance have no geometric shapes at all. However, the point cloud may have relatively complete and accurate geometric shapes in the distance. A larger resolution should be used, and because the generated image has slightly less geometric shapes in the distance, the effect is not good, simple and practical super-resolution model. It can only increase the resolution but cannot improve the distant geometry.)
- Investigate video generation capabilities with 3D VAE and 3D attention mechanisms
- Develop quantitative metrics for cross-modal consistency evaluation

## Ablation Study Analysis

### Missing Ablation Studies
- Detailed component-wise analysis of cross-modal epipolar condition module
- Impact assessment of different condition types on generation quality
- Sensitivity analysis of key hyperparameters
- Investigation of different training strategies

### Questions
While the work presents valuable theoretical contributions, significant improvements in code availability, documentation, and practical validation are needed for broader impact and reproducibility.

### 1. Code Release Improvements
- Release code on popular platforms (GitHub/GitLab)
- Provide comprehensive documentation
- Include example applications
- Add benchmark results reproduction scripts

### Soundness
3

### Presentation
3

### Contribution
3
