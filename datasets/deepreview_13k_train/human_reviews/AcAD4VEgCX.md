# I2VControl-Camera: Precise Video Camera Control with Adjustable Motion Strength

- Decision: Accept
- Scores: 6, 6, 8, 6

## Abstract
Video generation technologies are developing rapidly and have broad potential applications.
Among these technologies, camera control is crucial for generating professional-quality videos that accurately meet user expectations.
However, existing camera control methods still suffer from several limitations, including control precision and the neglect of the control for subject motion dynamics.
In this work, we propose \textbf{\camerapapername}, a novel camera control method that significantly enhances controllability while providing adjustability over the strength of subject motion.
To improve control precision, we employ point trajectory in the camera coordinate system instead of only extrinsic matrix information as our control signal. 
To accurately control and adjust the strength of subject motion, we explicitly model the higher-order components of the video trajectory expansion, not merely the linear terms, and design an operator that effectively represents the motion strength.
We use an adapter architecture that is independent of the base model structure.
Experiments on static and dynamic scenes show that our framework outperformances previous methods both quantitatively and qualitatively.
The project page is: \href{https://wanquanf.io/I2VControlCamera}{\textcolor[rgb]{0.8, 0.0, 0.2}{https://wanquanf.io/I2VControlCamera}}.
\nonumfootnote{$\dagger$ Corresponding author}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The submission pintroduces a new framework for training camer-controllable text-to-video model. To achieve the goal, the authors propose to disentangle the motion into two components: one is 3D rigid transformation of the majority of the underlying 3D scene - presumably this motion component is induced by the camera movement during capturing the scene; and another component that describe the non-rigid transformation of the rest of the scene, which, on the other hand, is supposed to be induced by the movement of the subjects in the scene. 

Following that, a data collection pipeline is proposed to extract associated control signals that represent the camera movement and the subjects movement of each video clip, respectively. Then a didecated adaption network is trained on top of a existing T2V model to learn a camera- and subject movement-controlled model.

### Strengths
The formulation that decouple the motion behind a video clip into 'global' and 'local' motions is sound.

A practical solution, that utilize several existing computer vision techniques, has been introduced to extract the associated control signals as described in that formulation.

The results produced by the proposed method demonstrate good visual quality.

### Weaknesses
Lack of sufficient experimental results. The submission contains a limited set of qualitative results. More video results and comparative visual results are needed to justify the effectiveness of the proposed method.

Small training dataset: The training dataset is relatively small, with only 30k video clips. While I appreciate the authors’ focus on data preparation rather than altering model structures, the limited dataset results in noticeable artifacts, such as flat character bodies in the video results. I am curious why the authors did not use a larger dataset. Is the proposed data pipeline robust and efficient enough for obtaining training data at scale?

Exposition: The paper is somewhat poorly written, leading to an unsmooth reading experience. The writing often complicates the ideas rather than simplifying them. Some expositions are even misleading. For instance, the statement “the entire 3D world can be divided into the static part and the dynamic part” at Line 161 is confusing. I believe “rigid and non-rigid motions” would be more appropriate terminology. The majority of the 3D scene remains relatively static only when the camera is fixed in the 3D scene, but the scope of this work obviously goes beyong fixed cameras.

The point trajectory maps used for training contain unoccupied black regions, which raises concerns about the training process. The paper needs to clarify whether the network is directly trained with these sparse point trajectory maps, and how this might impact the learning process. The projection of 3D point clouds onto novel camera poses to generate these maps requires a more detailed explanation in the paper.

Furthermore, the paper lacks a discussion of the limitations of the proposed method. Specifically, the decomposition of motion into rigid and non-rigid components may not be suitable for all types of videos. For example, videos with substantial non-rigid motion, such as those containing significant water wave movement, could pose a challenge to the method. The paper should address these potential failure cases and discuss the robustness of the approach under such conditions.

### Questions
Breaking the scene motion into ‘global’ and ‘local’ movements makes sense. However, to what extent can the proposed data pipeline work? For instance, how would it handle a fly-through video over the ocean?

The point trajectory mentioned at Line 170 is confusing when it first appears. It can easily be mistaken for 3D trajectories.

The authors claim compatibility with various base models, but there are no experiments to support this claim.

How are the users supposed to provide the dense point trajectories?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper initially defines motion strength as the motion remaining after eliminating camera rotation and translation. Subsequently, adapter layers are incorporated and trained to adhere to the parameters of camera motion and motion strength. These parameters are extracted from captured videos through metric depth estimation, pixel tracking correspondence, and the separation of static and dynamic components via linear motion fitting. The experimental results validate the efficacy of the proposed method.

### Strengths
1.The definition of motion strength aligns with the concept of elastic deformation in physics, referring to the shape deformation that remains after removing rigid motion, which holds theoretical significance. The algorithm for recovering motion strength from videos is meticulously designed.

2. The quality of the generated videos is impressive. The objects in the scene exhibit natural motions, and artifacts such as flickering and inconsistent pixels are rare, even during camera movements.

### Weaknesses
1. Although the paper title emphasizes precise video camera control, the main body primarily discusses motion strength. The camera trajectory control capabilities of the proposed method are comparable to those of SOTA papers, like MotionLORA.

2. The camera trajectory representation is based on the projection of 3D points. Firstly, this makes the representation reliant on an additional input: 3D points. Secondly, the projection of these points onto the camera image plane results only in 2D pixel locations, meaning the projections are largely similar across different viewpoints. I am confused by the projection operation used for representing the camera trajectory.

### Questions
Two questions:

1. What is the range of the 2D coordinates in 3D point projection?  Are they the normalized device coordinates?
2. Which video generation model is used in the proposed method?  I did not find this information. Maybe I miss something.

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
3

### Summary
In this work, the authors propose a novel method to control cameras to generate a video with dynamic camera motion from a given image. The existing methods suffer from coarse controllability of cameras and difficulties to control dynamic motion of the subject, this paper resolves the aforementioned challenges by introducing point-based controlling and new training data pipeline.

From the quantitative and qualitative results provided by the authors, this paper significantly outperforms the existing methods. With the pleasant qualitative results, I think this new approach can bring the significant contribution to the community and thus, I recommend its acceptance.

### Strengths
1) They propose point-based control signals instead of the camera extrinsics. This method can provide dense representation to control the model to generate temporally and spatially coherent video.

2) They resolved the limitations of the in-the-wild video dataset by leveraging the off-the-shelf depth estimation (Piccinelli et al., 2024), point tracking method (Karaev et al., 2023). While this is a bit straightforward, combining with their dynamic/static segmentation, the proposed pipeline can be effective for the future training.

3) The video representation is pleasant and the paper is well written.

### Weaknesses
I do not observe any hard limitation to tackle.

### Questions
Given the proposed formulation (2), the method should be generalized to any camera motion as rotational and translational movements of the camera are function of time. But both the paper and the supplementary videos seem to include one component of the camera motion (only zoom-in/out, only rotation, only translation). I would like to hear authors' perspective of this limited results.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper addresses the limitations of existing camera control methods in achieving precise control and managing subject motion dynamics in video generation. The authors introduce a novel approach, "I2VControl-Camera," which uses point trajectories in the camera coordinate system to improve control precision and stability. The method incorporates higher-order trajectory components, allowing for adjustable motion strength to achieve natural and dynamic subject movements. Experiments show that "I2VControl-Camera" surpasses state-of-the-art methods in both static and dynamic scenes, demonstrating precise control and realistic subject motion even in complex video generation scenarios.

### Strengths
The proposed method derives camera control precision by using point trajectories in the camera coordinate system, enhancing control tractability compared to traditional extrinsic matrix-based methods. This approach enables more accurate motion handling by explicitly modeling subject dynamics.
The method is designed to integrate with forward warp techniques and is compatible with various video generation models due to its adapter-based architecture, which maintains adaptability without modifying base model structures.
In practical applications, the method demonstrates the ability to handle deformations in complex, dynamic scenes with minimal camera movement. This adaptability allows for natural, adjustable subject dynamics and accurate control in diverse environments.
The paper is well-structured and concise, with clear figures and formulas that effectively support the proposed method's technical clarity and readability.

### Weaknesses
1. The authors’ approach of using point cloud poses to control video generation notably enhances control accuracy and dynamism. However, this method faces a key challenge: dense point clouds greatly increase computational cost, which impacts training stability and limits practical application. Specifically, the use of dense point clouds, while providing detailed motion information, necessitates processing a large number of points at each frame, leading to increased memory consumption and longer processing times. This is particularly problematic during the training phase where iterative optimization is performed. A potentially more effective control mechanism could involve using sparse control points—akin to the sparse point clouds generated by Structure-from-Motion (SfM)—which could provide a balanced trade-off between precise dynamic control and computational efficiency. I would highly encourage the authors to include a discussion comparing their method with existing approaches, particularly in terms of computational overhead, inference time, and final output quality.

2. The authors simultaneously consider 3D point motion and camera motion and utilize a unified point cloud trajectory as the control representation for video generation. However, the authors seem to only consider motion as a second-order nonlinear motion described by a Jacobian matrix in Eq.5. Compared to linear motion, what benefits does this second-order representation bring? What computational overhead does it incur? Are there further gains to be had from higher-order representations? The paper does not provide a clear justification for choosing a second-order model over simpler linear models or more complex higher-order models. It would make sense if the authors were to delve deeper and elucidate the reasons behind their choice of second-order representation, including a discussion on the trade-offs between model complexity, computational cost, and motion representation accuracy.

3. From my perspective, the training data is expensive, and the process is redundant. It involves depth estimation and iterative L-BFGS algorithm, which are computationally costly. For complex video generation models, handling depth and solving for Rλ and tλ are expensive, limiting the algorithm's practical applicability. The iterative L-BFGS optimization, while crucial for refining camera parameters, adds significant computational overhead, especially when performed on a per-frame basis for each training sequence. This computational cost could hinder the scalability of the method to larger datasets or higher-resolution videos. Furthermore, the reliance on depth estimation introduces additional complexity and potential inaccuracies, which could propagate through the training process.

4. The authors should provide a more comprehensive explanation of their implementation. For example, details on the specific architecture of the adapter, the loss functions used for training, and the optimization strategies employed are missing. This lack of detail makes it difficult to reproduce the results and assess the robustness of the method.

### Questions
1. The author should provide more details about the experimental setup, e.g., L-BFGS tolerable error, acceptable ratio, iterations, and video length of training.
2. It would be beneficial if the authors could furnish a detailed analysis of the time complexity for each component of the algorithm, as well as the memory requirements during the training process. This information is essential for assessing the algorithm's efficiency and scalability.
3. Despite the authors providing an anonymous GitHub link, it remains difficult to effectively validate the algorithm's actual effectiveness. Does the algorithm support the generation of multiple dynamic objects? What is the finest level of control achievable in terms of precision? We request that the authors provide more practical application examples to validate the algorithm's actual effectiveness, including fine-grained pixel-level control, controllable dynamic range, and sequence length of video generation. Furthermore, we ask the authors to provide additional evidence to support the claims made in the introduction section.

Currently, I would rate this paper as borderline. However, I am willing to reconsider my evaluation if the authors can provide additional clarifications and engage in a more in-depth discussion to address the concerns I have raised.

### Soundness
3

### Presentation
3

### Contribution
2
