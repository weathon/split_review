# 6D Object Pose Tracking in Internet Videos for Robotic Manipulation

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
We seek to extract a temporally consistent 6D pose trajectory of a manipulated  object from an Internet instructional video. This is a challenging set-up for current 6D pose estimation methods due to uncontrolled capturing conditions, fine-grained dynamic object motions, and the fact that the exact mesh of the manipulated object is not known. To address these challenges, we present the following contributions. First, we develop a new method that estimates the 6D pose of any object in the input image without prior knowledge of the object itself. The method proceeds by (i) retrieving a CAD model similar to the depicted object from a large-scale model database, (ii) 6D aligning the retrieved CAD model with the input image, and (iii) grounding the absolute scale of the object with respect to the scene. Second, we extract smooth 6D object trajectories from Internet videos by carefully tracking the detected objects across video frames. The extracted object trajectories are then retargeted via trajectory optimization into the configuration space of a robotic manipulator. Third, we thoroughly evaluate and ablate our 6D pose estimation method on YCB-V and HOPE-Video datasets and demonstrate significant improvements over existing state-of-the-art RGB 6D pose estimation methods. Finally,  we show that the 6D object motion estimated from Internet videos can be transferred to a 7-axis robotic manipulator both in a virtual simulator as well as in the real world. Additionally, we successfully apply our method to egocentric videos taken from the EPIC-KITCHENS dataset, demonstrating potential for Embodied AI applications.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces a pipeline for extracting the 6D pose trajectory from an internet video without the need of the CAD for the specific object. The authors leverage vision features to retrieve the most similar CAD model of the object, then do per-frame alignment leveraging the same vision features of the original image and rendered from the CAD. They further estimate the rough object size using LLM and leverage 2D tracking models to get inter-frame rotation consistency. The authors conduct experiments and demonstrate their superior performance. They also show demos that their trajectory can be retargeted to guide the movement of the robot.

### Strengths
1. The task of predicting the 6D pose of internet videos without additional prior is important for a lot of downstream tasks.
2. The whole pipeline is reasonable, fetch the similar CAD model and do rough alignment. Then further leverage the 2D tracking results to get the smoothed trajectories, that are more motion-consistent across time.
3. The experiments on the retargeted motion on robotics further show the usefulness of the extracted smoothed trajectories.

### Weaknesses
1. The authors demonstrate that compared to model-based methods, whose performances suffer from the inaccurate CAD mode, their method addresses the challenge. However, there is lack of experiments compared to SOTA model-based methods with their fetched CAD models (e.g. FoundationPose with their retrieved CAD model). Specifically, the paper should compare against methods that also use retrieved CAD models, to isolate the impact of the pose estimation method itself, rather than just the CAD model quality. It is unclear if the performance gain is due to the pose estimation method or the specific way the CAD model is used.
2. In the 6D pose alignment part, the method applies a sapling-based trajectory to get the rotation, which potentially limits the accuracy of the rotation. The sampling strategy, while efficient, may not fully explore the rotation space, leading to suboptimal pose estimates. In the results figure, there are some rotation errors, not sure if due to the sampling-based strategy or the DINO feature extractor. It would be beneficial to see an ablation study on the number of samples used and the impact on rotation accuracy.
3. For the robotics demo, the end-effector position control is on 6D pose or only on the rotation? From the Figure 9, the translation of the end-effector seems not consistent with the original video and in the simulator. The lack of consistency in translation between the video and the robot motion raises concerns about the accuracy of the full 6D pose transfer, and it is not clear how the scale is handled in the retargeting process.

### Questions
1. Why in Figure 1 and Figure 2, the same image has two different retrieved CAD models?
2. Can you provide the results of the error based on the quality of the retrieved CAD model?

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
This paper proposes a new approach to detect and track the 6-DoF pose of unknown objects from RGB video. The approach is motivated by robot imitation learning from internet video. The approach uses off-the-shelf open-set object detectors, foundation models for segmentation, vision-language (CLIP), and visual features (DINOv2) to detect objects, retrieve similar shapes from a database of CAD models, and matching the object image with a set of rendered views of the object CAD model to estimate 3D orientation. Experimental evaluation is performed quantititvely on YCB-Video and HOPE-Video datasets and a comparison is made with state of the art object detectors for unseen objects for which the CAD model is assumed known (MegaPose, GigaPose). Also, qualitative results on EPIC-Kitchen, and an example of executing the estimated object trajectories on a real robot are shown.

### Strengths
- The proposed approach for detecting and estimating 6D motion of unknown objects from RGB images is novel and interesting.
- The paper is well written and easy to follow.
- The set of experiments demonstrate the shape retrieval and pose estimation well and also compare with state of the art methods.
- A qualitative example is provided with a real robot which show the robot pouring from one object to another.

### Weaknesses
 - l. 197ff, CAD model retrieval by rendering views and calculating visual features seems expensive in both, the database generation and the retrieval stage for large datasets such as Objaverse-LVIS. What is the retrieval time for these datasets and how is it implemented to make retrieval efficient? Specifically, what is the time complexity of the rendering and feature extraction process for the entire dataset, and what are the practical implications for scaling to even larger datasets?
- l. 220ff proposes to retrieve rotation by matching to a set of rendered views. What is the choice of N in the experiments? What is the avg/std angular distance between sampled rotations? How does the choice of N affect the accuracy and computational cost of the rotation estimation, and what are the trade-offs involved in selecting a specific value for N?
- l. 243ff, the way to prompt the LLM in the supplementary is an offline procedure to collect size estimates for approximately 2200 objects. In the main paper, the description reads as if the LLM is prompted for each detected object using the CLIP text classification. Please describe this more clearly. What if the detected object is not included in the offline calculated set ? How does the method handle cases where the offline LLM-generated descriptions do not accurately represent the detected object, and what is the impact on the scale estimation?
- l. 286, was estimating the motion of the camera relative to the static background evaluated in this work ? Please clarify. It is unclear if the method explicitly accounts for camera motion, and if not, what are the limitations of assuming a static camera in real-world scenarios?
- The optimization problem in eq 4 does not provide a description of the used system dynamics model. What specific dynamic model is used, and how does it affect the accuracy and stability of the optimized trajectories?
- l. 361, please write more clearly, that while a similar mesh is known, the retrieved mesh does not exactly correspond to the ground truth mesh which is an assumption used for MegaPose and GigaPose. How does the discrepancy between the retrieved mesh and the actual object mesh affect the performance of the proposed method compared to methods that assume perfect mesh knowledge?
- Please introduce the pCH metric formally, at least in the supplemental material. The current description is insufficient. A formal definition is needed to understand the metric's properties and limitations, especially in the context of non-identical meshes.
- l. 519ff, the real robot experiment is rather anecdotal and lacks important details in its descriptions and quantitative evaluation (e.g., success rate). How are the observed object trajectories transfered to the real robot experiment incl. considering the change of view point and embodiment? How does the robot know where the manipulated objects are and how is this matched to the observed object motion? What are the specific steps involved in transferring the object trajectories from the video to the robot, and how are the differences in viewpoint and embodiment addressed?
- Fig. 8, in the upper additional qualitative result, the bowl object pose is not correctly tracked. Why does the robot still turn the object in a quite different angle ? What is the cause of the discrepancy between the estimated object pose and the robot's action, and how does this affect the overall performance of the system?

Additional minor comments:
- Fig. 6, rightmost real robot image seems to be a repetition of the image next to it. Was the wrong image included?

### Questions
- l. 323, are the ground-truth meshes contained in the object datasets? 
- Table 1, was the same scale estimate for the meshes used for MegaPose and GigaPose like for the proposed method? 
- Which dynamics model is used for the optimization problem in eq 4? How is tracking of the optimized trajectory implemented?
- See additional questions in sec. "Weaknesses".

### Soundness
3

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
The authors present a novel approach to extract temporally consistent 6D pose trajectories of manipulated objects from Internet videos to be applied with robotic manipulation task. It tackles the challenges posed by uncontrolled capture conditions, unknown object meshes, and complex object motions. Their evaluation on YCB-V and HOPE-Video datasets shows state-of-the-art performance, with successful motion transfer to a robotic manipulator in both simulated and real-world settings.

----------------------------------------------------------------------------------------------------
The authors addressed most of my concerns in the rebuttal phase, and thus I would like to raise my score to 6.

### Strengths
The impact of the paper is dominant in the way that it provides an envision of enriched data for robotic manipulation without human labor force to construct the specific datasets. The methodology is intuitive and the performance enhancement is non-trivial. The paper is overall well-written.

### Weaknesses
My primary concern lies with the methodological novelty, as the approach largely involves applying an existing pipeline to internet videos. Specifically, the use of an LLM for estimating object scale may be questionable, given potential uncertainties around its accuracy in providing a realistic scale for each object. Aside from this, the methodology essentially adapts previous methods to fit the proposed pipeline. Given these factors, I feel this work might not align with ICLR's focus but could be more suited to a robotics conference.

### Questions
1. It might be great if the authors could ablate on the performance variation under different LLMs. Currently it only applies GPT-4, but it is important to know how different LLMs might influence the performance (i.e. one GPT-3.5 & one open-source LLM).
2. What's the efficiency & cost of such pipeline when performing inference on a 1-minute Instructional videos? 
3. Using a CAD model can be costly since it requires a large database to store predefined meshes, and in open-world scenarios, finding an exact match is often unlikely. However, numerous approaches avoid relying on CAD models. For instance, "6DGS: 6D Pose Estimation from a Single Image and a 3D Gaussian Splatting Model" [ECCV 2024]. Have you tried experimenting with such methods? Or say, how do you envision those methods' strengths and weaknesses compared to your method.
4. For the standard evaluation, it might be beneficial to add another dataset evaluation using different cameras, say iPhone sensor as proposed in "Robust 6DoF Pose Estimation Against Depth Noise and a Comprehensive Evaluation on a Mobile Dataset" to further validate the approach's generalizability.

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
The paper pays attention on 6D pose trajectory estimation of a manipulated object from an Internet instructional video with a novel framework. The framework first predicts the 6D pose of any object by CAD model retrieval. Then the smooth 6D object trajectories are extracted and retargeted via trajectory optimization into a robotic manipulator. Experiments on YCB-V and HOPE-Video datasets demonstrate the improvements over RGB 6D pose methods. Moreover, the 6D object motion can be transferred to a 7-axis robotic manipulator.

### Strengths
1 The pose estimation method by retrieving a CAD model, aligning the retrieved CAD model with the object, and grounding the object scale with respect to the scene.

2 Consistent 6D pose trajectory estimation from Internet videos and retargeting trajectories to a robotic manipulator.

3 The pose estimation improvement on YCB-V and HOPEVideo datasets, and transfer from 6D object motion to a 7-axis robotic manipulator.

### Weaknesses
1 The original contributions should be expressed more clearly. In the proposed method, various existing methods are employed. It is suggested to clearly distinguish the original contributions in this paper and usage of other methods. Specifically, the first contribution locates in the pose estimation method by retrieving a CAD model, aligning the retrieved CAD model, and grounding the object scale with respect to the scene. The subsequent question is that what is the original contribution, the whole pipeline or the detailed design of a particular module? The authors are suggested to express this more clearly in the revised version. For the second and third contributions, it is also recommended to present more clear expressions.

2 For robotic manipulation, the running time of the pose estimation method is a key factor. The proposed method in the paper is somewhat time-consuming with 2s for detector, retrieval and scale estimation per scene and 0.2s for pose estimation per object. To further improve the paper, two suggestions are given. For one thing, the comparaions with other methods on running time are suggested to add.  For another, more analysis about the running time is also preferred, such as the recommendations for accelerate the whole method.

### Questions
1 With the similar CAD model retrieval, the classification can also be obtained. I wonder if it is possible to use the CAD model to perform classification directly?

### Soundness
3

### Presentation
3

### Contribution
3
