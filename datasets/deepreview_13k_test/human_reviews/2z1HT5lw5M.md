# Trajectory attention for fine-grained video motion control

- Decision: Accept
- Scores: 6, 6, 6, 8, 8

## Abstract
Recent advancements in video generation have been greatly driven by video diffusion models, with camera motion control emerging as a crucial challenge in creating view-customized visual content. 
This paper introduces trajectory attention, a novel approach that performs attention along available pixel trajectories for fine-grained camera motion control. 
Unlike existing methods that often yield imprecise outputs or neglect temporal correlations, our approach possesses a stronger inductive bias that seamlessly injects trajectory information into the video generation process. 
Importantly, our approach models trajectory attention as an auxiliary branch alongside traditional temporal attention. 
This design enables the original temporal attention and the trajectory attention to work in synergy, ensuring both precise motion control and new content generation capability, which is critical when the trajectory is only partially available.
Experiments on camera motion control for images and videos demonstrate significant improvements in precision and long-range consistency while maintaining high-quality generation. Furthermore, we show that our approach can be extended to other video motion control tasks, such as first-frame-guided video editing, where it excels in maintaining content consistency over large spatial and temporal ranges.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces a novel approach called Trajectory Attention for fine-grained video motion control, particularly aiming to enhance camera motion control in video generation tasks. By modeling trajectory attention as an auxiliary branch alongside traditional temporal attention, the method leverages available pixel trajectories to inject precise motion information into the video generation process. This design allows the original temporal attention and the trajectory attention to work synergistically. The proposed method demonstrates strong adaptability, e.g., being transferable to architectures like DiT. Experiments across various tasks show significant improvements in control precision and content consistency while maintaining high-quality generation. Extensive ablation studies validate the effectiveness of each module.

### Strengths
1. The proposed method is lightweight, requiring low training costs, making it practical and efficient for real-world applications without the need for extensive computational resources.
2. The method demonstrates strong transferability, showing effectiveness with different architectures such as DiT. 
3. The paper conducts thorough exploration at application level, showcasing the method's effectiveness in multiple tasks, including camera motion control and video editing. Abalation studies are sufficient.

### Weaknesses
1. The method heavily relies on dense optical flow information, as shown in Figure 3 of the supplementary material. This dependency can significantly increase inference time due to the computational cost of processing dense optical flow, especially in real-time applications. 
2. The reliance on dense optical flow makes it challenging to adapt the method to user inputs of sparse trajectories. As noted in DragNUWA, it's difficult for users to input precise trajectories at key points in practical applications, leading to a gap between training and inference. This limitation reduces the method's practicality in scenarios where only sparse motion cues are available.
3. In line 158, H and W represent the dimensions of the latent features, but in Algorithm 3, H and W are used for image dimensions, which is confusing.
4. Some examples in Fig.6 and Fig.9 are not significant, like the second example in Fig.6.

### Questions
I suggest to review and correct the mathematical formulations and notation to enhance the paper's clarity and reliability.

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
The paper introduces Trajectory Attention, a novel approach designed to enhance fine-grained motion control in video generation, particularly focusing on precise camera motion control within video diffusion models. Traditional methods often struggle with imprecise outputs and neglect temporal correlations, leading to inconsistencies in generated videos. This work addresses these challenges by explicitly modeling trajectory attention as an auxiliary branch alongside the standard temporal attention mechanism. By modeling trajectory attention as an auxiliary branch alongside the standard temporal attention, the method explicitly injects available pixel trajectory information into the video generation process. This design allows the temporal attention to focus on motion synthesis and short-range dynamics, while the trajectory attention ensures long-range consistency along specified paths. The approach efficiently integrates trajectory information without modifying the original model parameters and supports sparse trajectories, meaning it can handle partial trajectory data. Experiments demonstrate that this method significantly improves motion control precision and video quality across various tasks, including camera motion control on images and videos, as well as first-frame-guided video editing.

### Strengths
1. The paper introduces a novel concept of Trajectory Attention for fine-grained motion control in video generation. This auxiliary attention mechanism enhances the existing temporal attention in video diffusion models by explicitly incorporating trajectory information, which is a significant advancement in the field.
2. By modeling trajectory attention as an auxiliary branch that works alongside the original temporal attention, the approach allows for seamless integration without modifying the original model parameters. This design choice is both practical and efficient, leveraging pre-trained models and enabling efficient fine-tuning.
3. The proposed method demonstrates significant improvements in motion control precision and long-range consistency over existing methods. The experimental results, including quantitative metrics like Absolute Trajectory Error (ATE) and Relative Pose Error (RPE), validate the effectiveness of the approach.
4. The paper includes thorough experiments and ablation studies that not only demonstrate the superior performance of the proposed method but also validate the design choices. This strengthens the credibility of the findings and provides valuable insights into the method's effectiveness.

### Weaknesses
1. The method is primarily designed for video diffusion models that use decomposed spatial-temporal attention. It is less clear how well the approach generalizes to models with integrated spatial-temporal attention (e.g. 3D DiTs) or other architectures. Expanding the evaluation to include such models would strengthen the contribution.
2. The paper compares the proposed method with a limited set of existing approaches. Including discussions with more recent or state-of-the-art methods, especially those that have emerged concurrently, would provide a more comprehensive evaluation of the method's relative performance. For example, Collaborative Video Diffusion [1] uses epipolar attention to align contents of different camera trajectories, and Camco [2] also uses epipolar, but to enhance the 3D consistency of generated contents.
3. The experimental evaluations are primarily conducted on the MiraData dataset. While this dataset may offer certain advantages, relying on a single dataset limits the ability to generalize the findings. Evaluating the method on additional, diverse datasets would strengthen the claims about its general applicability.
4. While the method supports sparse trajectories, the paper does not extensively explore how it performs when the trajectory information is highly sparse, incomplete, or noisy. Real-world applications often involve imperfect data, so robustness to such conditions is important. Going back to my point 2, this is especially concerning since the model is trained on MiraData, which mostly consists of synthetic videos.

[1] Kuang et al. Collaborative Video Diffusion: Consistent Multi-video Generation with Camera Control, in NeurIPS, 2024.

[2] Xu et al. CamCo: Camera-Controllable 3D-Consistent Image-to-Video Generation, in arXiv, 2024.

### Questions
N/A

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
3

### Summary
This paper proposes injecting a new attention layer along the trajectory into the model to support camera motion control in video generation. During training, optical flow is used as the trajectory, and the new attention operation is performed only along this trajectory. The trained model achieves good results in camera control for image-to-video and video-to-video tasks.

### Strengths
- Metric-wise, it seems the model achieves better camera control.
- The model can be used for first-edited-frame + original-video-guided editing, though how this is achieved is not very clear.

### Weaknesses
1) Figure-1 is confusing. It takes some time to understand the input and output of each task. It would be better to reorganize this figure to make it clearer. Each task could be separated into a small sub-figure with a clear indication of the input and output.

2) In Figure-3, it’s unclear what the model’s input is in two scenarios: (1) when you have multiple frames as input, i.e., ‘camera motion control on videos’ in Figure-1, and (2) when you have multiple frames plus edited frames as input, i.e., ‘first-frame-guided video editing’ in Figure-1.

3) The trajectory attention mechanism operates only in 2D space, making it challenging to distinguish motion orthogonal to the image plane—for example, whether an centered object is moving towards or away from the camera. In such cases, the coordinates remain the same across frames. Could this be a limitation of this method?

### Questions
1) How do you ensure that when attention is applied along the trajectory, the generated pixel also follows the trajectory? Have you observed any cases where control fails?

2) In Algorithm 3, are you feeding \{I_r\} to the model in any particular format? The same question applies for Algorithm 4 with \{V_r\}.

3) Is the comparison to other work (motion control/camera control) fair? They are trained on different datasets, and they may have some issue generalizing to the evaluation dataset used here. How did you select the evaluation set? Were you able to evaluate on the test set of other papers? 

4) In training, optical flow is used as a trajectory, but in inference, the model takes the camera trajectory as input. Could this cause a mismatch between training and inference? Why not use the camera trajectory as guidance during training as well?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper focuses on fine-grained camera motion control in video generation. It has the following contributions:
1. Trajectory Attention Mechanism: Proposes a novel trajectory attention branch alongside the original temporal attention branch. It models attention along available pixel trajectories for camera motion control.
2. Improved Performance: Demonstrates significant improvements in precision and long-range consistency for camera motion control in both images and videos while maintaining high-quality generation.
3. Extension to Other Tasks: Shows that the approach can be extended to other video motion control tasks, such as first-frame-guided video editing, where it excels in maintaining content consistency over large spatial and temporal ranges.

### Strengths
1. Originality: The paper demonstrates originality in its approach to video motion control. The concept of trajectory attention, modeled as an auxiliary branch to traditional temporal attention, is a novel way to incorporate pixel trajectories for fine-grained camera motion control. This approach differs from existing methods that either rely on high-level constraints or neglect temporal correlations.
2. Quality: The experimental setup is comprehensive, using a large-scale dataset and multiple evaluation metrics. The results are presented in a clear and organized manner, with both quantitative comparisons and qualitative visualizations. The ablation study further validates the effectiveness of the proposed components, indicating a high level of quality in the research design and execution.
3. Significance: The significance of the paper lies in its potential impact on the field of video generation and motion control. The proposed method shows improved performance in camera motion control for both images and videos, which is crucial for creating high-quality and customized visual content.

### Weaknesses
1. The paper does discuss trajectory extraction for different tasks such as camera motion control on images and videos, and video editing. However, the description of the extraction process could be more detailed and clear. For example, in Algorithm 3 for trajectory extraction from a single image, some steps might require further clarification for a reader who is not familiar with the underlying concepts. The estimation of the depth map and the rendering of views are steps that could be explained in more detail, including the methods and algorithms used. Similarly, in Algorithm 4 for video trajectory extraction, the point trajectory estimation and the combination with camera motion could be more clearly described.
2. While the proposed trajectory attention method shows promising results in the presented experiments, there is a lack of exploration of more complex scenarios. For example, in real-world video data, there may be occlusions, rapid camera movements, or multiple moving objects, and it is not clear how the method would perform in such situations.
3. The comparison with existing methods, although extensive to some extent, could be more comprehensive. There are many other techniques in the field of video motion control that were not included in the comparison, and it is possible that some of these methods may have unique features or advantages that could have provided a more nuanced understanding of the proposed method's superiority.

### Questions
According to the weaknesses, you can take the suggestions below to make your paper more convincing:
1. In Algorithm 3, please elaborate on which depth estimation method you take in step 1 and how you render a set of views $I_{r}$ and get the translation of pixels $T$ in step 2. In Algorithm 4, please elaborate on which point trajectory estimation method you take in step 2. Meanwhile, could you provide the visual results of the trajectory extraction from a single image and a video to demonstrate the correctness of Algorithms 3 and 4? 
2. Provide results of your method on videos with occlusions, rapid camera movements, and multiple moving objects, respectively.
3. Provide a comparison with more related works, such as [MotionBooth](https://arxiv.org/abs/2406.17758) and [CamTrol](https://arxiv.org/abs/2406.10126). More comparisons to concurrent work are also encouraged but not mandatory.

If the authors could solve my problems, I would raise the score.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper introduces Trajectory Attention, an innovative method for fine-grained camera motion control that attends to available pixel trajectories. The authors identify conflicts between the original temporal attention modules in diffusion models and supplementary trajectory-conditioned temporal modules. To resolve these conflicts, the paper employs optical-flow data to define trajectories, samples the most correlated points along them, and applies a copy attention mechanism to enhance trajectory precision. The original temporal module is retained for consistency. Comprehensive experiments on camera motion control for both images and videos demonstrate significant improvements in precision and long-range consistency without compromising high-quality generation. Furthermore, the approach is shown to be extensible to other video motion control tasks, including first-frame-guided video editing, where it maintains content consistency over extensive spatial and temporal dimensions

### Strengths
- The Trajectory Attention module is intuitive and offers flexibility in capturing temporal correlations in camera motion. This innovative approach effectively addresses the challenges associated with fine-grained control of camera motion.

- The experiments on camera motion control for both images and videos are impressive. They demonstrate significant improvements in precision and long-range consistency, all while maintaining high-quality generation. These results underscore the effectiveness of the proposed method in handling complex camera motion scenarios.

- The paper effectively shows that the approach can be extended to other video motion control tasks. For instance, in first-frame-guided video editing, the method excels at maintaining content consistency over large spatial and temporal ranges. This versatility is a testament to the robustness and general applicability of the Trajectory Attention framework.

### Weaknesses
- The paper raises concerns about object dynamics in the image-to-video case presented in the supplementary material. The examples, such as the dog and the cat, lack additional motion, which could be a limitation. It would be beneficial to see how objects with more complex dynamics are handled by the method.

- There is a concern regarding the generalization of camera pose. In the Image-to-Video (first-frame) scenario, the trajectory module is trained with optical-flow data from only 10K video clips. It's unclear how the method would perform under challenging motions, such as clockwise rotation, high-speed zooming in and out, or 360-degree rotations like those seen in NVS-Solver GitHub. In these extreme trajectories, points visible in the first frame may become invisible, potentially leading to anti-aliasing issues. Additional results or a discussion of the necessary limitations would aid in a more comprehensive assessment of the proposed method.

### Questions
- How can one obtain or customize the appropriate intrinsic and extrinsic parameters when performing trajectory extraction for a single image or video? Does the camera always need to be directed at the center of the image?

- Is it necessary to adjust the camera's intrinsic and extrinsic parameters based on the depth information available?

### Soundness
3

### Presentation
3

### Contribution
3
