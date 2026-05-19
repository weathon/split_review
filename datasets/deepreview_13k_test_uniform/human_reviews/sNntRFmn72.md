# Cavia: Camera-controllable Multi-view Video Diffusion with View-Integrated Attention

- Decision: Reject
- Scores: 5, 8, 5, 5

## Abstract
In recent years there have been remarkable breakthroughs in image-to-video generation.
However, the 3D consistency and camera controllability of generated frames have remained unsolved. Recent studies have attempted to incorporate camera control into the generation process, but their results are often limited to simple trajectories or lack the ability to generate consistent videos from multiple distinct camera paths for the same scene. To address these limitations, we introduce \textbf{Cavia}, a novel framework for camera-controllable, multi-view video generation, capable of converting an input image into multiple spatiotemporally consistent videos. Our framework extends the spatial and temporal attention modules into view-integrated attention modules, improving both viewpoint and temporal consistency. This flexible design allows for joint training with diverse curated data sources, including scene-level static videos, object-level synthetic multi-view dynamic videos, and real-world monocular dynamic videos. To our best knowledge, Cavia is the first of its kind that allows the user to precisely specify camera motion while obtaining object motion. 
Extensive experiments demonstrate that Cavia surpasses state-of-the-art methods in terms of geometric consistency and perceptual quality. Project Page: \url{https://ir1d.io/Cavia/}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents a novel framework, Cavia, designed for generating multi-view videos with precise camera control. The authors introduce view-integrated attention mechanisms that enhance 3D consistency across perspectives. Additionally, Cavia is trained on a curated blend of static, monocular dynamic, and multi-view dynamic videos. Cavia demonstrates superior performance over baseline methods in both monocular video generation and cross-view consistency.

### Strengths
1. Novel Framework for Camera-Controllable Video Generation: This paper introduces an innovative framework aimed at generating videos with precise camera control.

2. Superior Performance over Baselines: The proposed method demonstrates an  improvement over baseline models across key performance metrics.

3. Good Monocular Setting Results: Under a monocular setting, the experimental results exhibit substantial improvements in the generated videos.

### Weaknesses
1. Limited Distinction in Visualization Results (Figure 5): The visual examples provided in Figure 5 lack noticeable differences, which undermines the claimed improvements. This inconsistency between visual and metric-based results calls into question the interpretability and significance of the enhancements.

2. Poor Presentation: (i) The method section is minimal, with only three formulars, all of which are borrowed from references. The lack of detailed descriptions of the pipeline leaves the approach unclear and less accessible for readers. (ii) The paper includes non-standardized expressions, such as "(B V F C H W)" in Line 222. Additionally, Section 4 is ambiguously presented, making it difficult to comprehend.

### Questions
1. Visualization vs. Metric-Based Improvement: In Figure 5, the differences among the results appear minimal. What factors contribute to the significant metric-based improvements under the 2-view setting despite the subtle visual changes?

2. GPU Memory Usage of Cross-Frame Attention: Given the extended token length in the cross-frame attention module, does this component impose a significant demand on GPU memory?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces CAVIA, a framework that advances video generator by adding camera controllability and enabling 4D generation. Specially, it focuses on generating multi-view consistent videos, allowing precise control over camera movement while maintaining object and scene consistency across frames. The Plücker embedding is adopted to inject camera features to the video generator. The cross-frame attention is used to enhancing temporal consistency within each video clip, and the cross view attention is utilized to enhance the content consistency between across different video clips. 
CAVIA is also novel in its usage of multiple data sources, including static and dynamic, multi-view datas. This methods tested on various datasets and compared with some existing methods, demonstrating its state-of-the-art performance.

### Strengths
1. Writing is good, and is easy to follow.
2. The model is simple and effective, and easy to use the existing pre-trained video generation models.
3. The data preparation process is logical and effective, it leverages a mix of statics multi-view, monocular videos, and synthetic multi-view datas. The model benefits from such a broader range of training data, enhancing its generalization and robustness.
4. Extensive experiments demonstrate the effectiveness of each design choice.

### Weaknesses
The main weaknesses are in the experiment part:
1. What are the "general" videos come from? Compared to the RealEstate10K dataset, does the "general" videos have larger camera motion? And does the dynamic complexity is limited?
2. In Table 2, there should be some quantitative comparisons with the CVD model.
3. In the provided videos, the object dynamic degree is limited, can you provide a comparison on the object dynamic degree between CAVIA and the base video generation model SVD?

### Questions
See weaknesses

### Soundness
4

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
This paper presents a novel method for camera-controllable multi-view video generation. Leveraging a pre-trained I2V model, the method introduces camera-conditioned Plücker coordinates in the latent space for conditional control. Additionally, it extends spatial attention into cross-view attention and promotes 1D temporal attention into cross-frame 3D attention. These enhancements have been evaluated and found beneficial for achieving cross-view and cross-frame consistency, as well as precise camera control.

To address the challenge of limited multi-view video data, an effective joint training strategy is proposed, utilizing a curated mixture of static, monocular dynamic, and multi-view dynamic videos. Experiments demonstrate the superiority of the proposed method over existing competitors in terms of multi-view consistency and camera control precision. However, it is worth noting that most of the demonstrated examples pertain to specific domains, involving minimal dynamics and simple backgrounds, which raises questions about the method's performance in more general scenarios.

### Strengths
1. From the qualitative and quantitative results, it is evident that this method indeed offers superior camera trajectory control accuracy. This advantage is attributed to the benefits brought by 3D temporal attention (maybe also fulltuning) and the carefully collected training dataset.

2. To overcome the scarcity of multi-view video dataset, a curated mixture of existing available static, monocular dynamic, and multi-view dynamic videos is exploited via joint training scheme. This provides a solution for addressing data issues in future research on this task.

3. The experimental evaluation and comparison are comprehensive, evaluating the geometric accuracy of camera control from multiple perspectives. It demonstrates noticeable superiority of the proposed method.

### Weaknesses
1. The technical novelty is mild. Adopting plucker embedding for camera control is not new. Extending spatial attention for cross-view attention is also straightforward. Anyway, it is inspiring that 3D attention instead of 1D temporal attention is highly desired to help camera control accuracy, and this is well validated by multiple experiments.


2. One of the major weakness is the less convincing results. 
The most important aspects of multi-view video generation are motion synchronization and geometric consistency. However, most of the examples presented in the paper involve minimal object movement (either a single object with a simple, weakly moving background or entirely static scenes), and the camera angles do not vary significantly, with most shots taken from the same side of the object. This makes it difficult to evaluate the proposed method's capabilities in this task.

For example, I would like to see examples like this: "on a street with vehicles and pedestrians, a horse is running, with one camera capturing a global view from behind the horse and another camera tracking from the side". Showing more examples like this would be more convincing and demonstrate the value of controllable multi-view video generation.


3. In my understanding, making use of monocular videos could promote the model's generalization. But most of the cases in the paper, are close to the style of Objeverse dataset. Is it because the fulltuning destroyed the capabiliy of SVD in generating realistic style and scene? If so, this should be claimed as a limitation, especially compared to those adapter plugin methods like MotionCtrl and CameraCtrl.


4. From the results in Fig. 8, it appears that while the introduction of monocular video increases generalization ability, such as maintaining the content of the input images, it also affects the accuracy of multi-view camera control. In the second row of (b), the shooting direction for the fish and the fox did not turn as expected.

### Questions
1. In Table 3, I'm curious why the impact of "w/o cross-view" is even smaller than that of "w/o cross-frame." Intuitively, cross-view should be an essential component for multi-view setups (without it, it's challenging to maintain multi-view consistency and motion synchronization), whereas cross-frame primarily enhances the accuracy. Does this result imply that most of the outcomes are actually static, and similar results could be achieved through independent monocular camera control?

2. Is your model fully tuned? What is the parameter count?

3. Are the results of the ablation study in Table 3 based on monocular camera control or multi-view camera control? It would be advisable to evaluate these two settings separately.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper introduces Cavia, a novel framework for generating multi-view videos with camera controllability. It incorporates view-integrated attention mechanisms—specifically, cross-view and cross-frame 3D attentions—to enhance consistency across different viewpoints and frames. The paper also presents an effective joint training strategy that leverages a curated mix of static, monocular dynamic, and multi-view dynamic videos. This approach ensures geometric consistency, high-quality object motion, and background preservation in the generated results. Experimental results show that Cavia outperforms baseline methods in terms of geometric and perceptual quality for monocular video generation and cross-video consistency. Additionally, the flexible framework can process four views at inference, leading to improved view consistency and enabling 3D reconstruction of the generated frames.

### Strengths
- The Cross-View Attention and Cross-Frame Attention mechanisms are intuitively designed and effectively enhance temporal consistency. The incorporation of 3D attention particularly strengthens this aspect.

- The joint training strategy is commendable for its use of diverse dataset sources, including monocular videos and multi-view videos, which contributes to the robustness of the model.

### Weaknesses
- The video content presented demonstrates low dynamics (object), which may limit the ability to fully showcase the capabilities of the proposed method.

- The contribution of this work appears to be incremental. The proposed method shares significant similarities with CVD, suggesting that the innovations may be more evolutionary than revolutionary.

- The trajectories showcased in the supplementary demo are relatively simple, which raises questions about the model's ability to generalize to more complex scenarios. Further demonstration on a broader range of data would help to substantiate the method's effectiveness.

### Questions
- The camera conditions are normalized to a unit scale, can this approach still achieve variable speed camera control similar to MotionCtrl?

- Is it sufficient for the filter method used in Particle-sfm for camera pose estimation to rely on the number of points for accurate pose estimation in videos with significant object motion?

- It would be beneficial to include data samples from various sources to enhance understanding. Additionally, filtering out poor quality samples is necessary.

### Soundness
3

### Presentation
3

### Contribution
2
