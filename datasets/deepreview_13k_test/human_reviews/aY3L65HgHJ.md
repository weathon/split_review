# MotionClone: Training-Free Motion Cloning for Controllable Video Generation

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Motion-based controllable video generation offers the potential for creating captivating visual content. Existing methods typically necessitate model training to encode particular motion cues or incorporate fine-tuning to inject certain motion patterns, resulting in limited flexibility and generalization.
In this work, we propose \textbf{MotionClone}, a training-free framework that enables motion cloning from reference videos to versatile motion-controlled video generation, including text-to-video and image-to-video. Based on the observation that the dominant components in temporal-attention maps drive motion synthesis, while the rest mainly capture noisy or very subtle motions, MotionClone utilizes sparse temporal attention weights as motion representations for motion guidance, facilitating diverse motion transfer across varying scenarios. Meanwhile, MotionClone allows for the direct extraction of motion representation through a single denoising step, bypassing the cumbersome inversion processes and thus promoting both efficiency and flexibility. 
Extensive experiments demonstrate that MotionClone exhibits proficiency in both global camera motion and local object motion, with notable superiority in terms of motion fidelity, textual alignment, and temporal consistency.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper proposes a training-free method that enables motion cloning from reference videos. It explores the use of sparse temporal attention as guidance for motion cloning, which can be extracted through a single denoising step.  Experiments have been conducted to evaluate the effectiveness both qualitatively and quantitatively.

### Strengths
1. The exploration of temporal attention for motion representation is interesting and novel to me.
2. The presented results exhibit good motion cloning.
3. The paper is well-written and easy to follow.

### Weaknesses
1. The generalization of the proposed method is a concern. The proposed method heavily relies on temporal attention maps, where spatial and temporal attention are separate. Can the proposed method be applied to the latest video methods, such as CogVideoX, which employ the full attention layers?
2. Some existing methods have explored motion guidance in T2V models, such as [1]. The authors should cite and discuss these works.
3. The generated videos exhibit inconsistent details across different frames, such as the robot's eyes and legs in Fig. 1. A better T2V model might help to resolve these inconsistencies.

[1] Xiao, Zeqi, et al. "Video Diffusion Models are Training-free Motion Interpreter and Controller."

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces MotionClone, a training-free framework for motion cloning from reference videos, facilitating motion-controlled video generation for tasks like text-to-video and image-to-video. By utilizing sparse temporal attention weights as motion representations, MotionClone enhances motion transfer across different scenarios. It simplifies the process by allowing direct extraction of motion representations in a single denoising step, improving efficiency. Experimental results demonstrate that MotionClone excels in global camera motion and local object motion, achieving high motion fidelity, textual alignment, and temporal consistency.

### Strengths
1. The paper is well-written and presents a novel method to perform temporally-consistent video editing in a zero-shot manner.
2. The proposed motion control strategy is simple yet effective through motion guidance from sparse temporal attention map.
3. The paper conducts comphresive experiments to verify the superiority in global camera motion and local object action.

### Weaknesses
1. This paper only employs CLIP scores to evaluate the temporal consistentcy of generated videos, which are not convincing. Please provide appropriate metrics like warping error to improve the soundness of MotionClone.
2. MOFT [1] and Space-Time Diffusion Features [2] also performs zero-shot video editing using pre-trained video diffusion models. The proposed method shares similar ideas with them, could the authors give elaborate comparisons with them?

[1] Xiao, Zeqi, Yifan Zhou, Shuai Yang, and Xingang Pan. "Video Diffusion Models are Training-free Motion Interpreter and Controller." arXiv preprint arXiv:2405.14864 (2024).
[2] Yatim, Danah, Rafail Fridman, Omer Bar-Tal, Yoni Kasten, and Tali Dekel. "Space-time diffusion features for zero-shot text-driven motion transfer." In CVPR 2024.

### Questions
1. The supplementary materials only show the generated videos of the proposed method. Could the authors provide the comparisons with other methods?
2. Both VMC and the proposed method employs pre-trained video diffusion models to perform zero-shot video editing. The authors are encouraged to fair compare them under the same setting. 
3. Section 4.7 shows the limitation and failure cases of the proposed method. Could the authors discuss their reasons and potential solutions?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors propose a training-free framework that transfers motion from reference videos to video generation. They find temporal-attention maps drives motion synthesis. Based on this observation, they utilize this temporal-attention maps as motion guidance to control the motion of generated videos. In addition, they conduct extensive experiments to validate the effectiveness of the proposed method.

### Strengths
+ This paper find temporal-attention maps contain important motion information. The temporal-attention map alignment between reference videos and generated videos can transfer motion from reference videos to video generation. This observation is interesting.
+ Based on this observation, the authors propose a simple but effective method, which can transfer global motion into video generation. For efficiency, they also introduce fixed-time motion representation as the motion guidance. It is a practical solution for deployment.
+ The authors conduct extensive experiments to validate the proposed method. Compared with existing methods, the proposed method achieves superior performance on motion-based controllable video generation.

### Weaknesses
- Ablation results. The experiments are exhaustive, but they are only the qualitative results. It is necessary to show the quantitative results for each component. With quantitative results, the proposed method is more convinced.
- Temporal attention block. To my knowledge, down blocks also have temporal attention blocks. Thus, it is an option to apply the proposed motion guidance on down blocks. However, we only show the results with motion guidance applied in up blocks. It is necessary to provide the ablation results of temporal attention in down blocks.
- Guidance weight $\lambda$. The value of $\lambda$ is 2000. To my knowledge, it is too large. What the explanation of this high value is?
- The illustration of Figure 4. The Figure 4 needs to be improved. It is difficult for readers to learn the proposed method clearly only with the contents of Figure 4. Besides, there are some errors in Figure 4. For example, motion representation is not $t_{\alpha}$. According to main text, $t_{\alpha}$ is a time step.

### Questions
The authors need to conduct more experiments and improve Figure 4, see weaknesses.

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
5

### Summary
The paper introduces MotionClone, a training-free framework designed for motion cloning in controllable video generation. Unlike traditional methods that require tailored training or fine-tuning, MotionClone leverages the temporal attention mechanism within video generation models to capture and clone motion from reference videos. This approach allows for detailed motion synthesis while minimizing dependencies on the structural components of the reference video, enabling flexible motion cloning across various scenarios. The framework is versatile, supporting tasks like text-to-video (T2V) and image-to-video (I2V), and it has been shown to outperform existing methods in terms of motion accuracy and text alignment.

### Strengths
1. MotionClone eliminates the need for complex training processes, making it more accessible and efficient.
2. The framework supports multiple video generation tasks, including T2V and I2V, demonstrating its broad applicability.
3. Enhanced Motion Accuracy: MotionClone outperforms existing methods in capturing and cloning localized object motions with higher fidelity.

### Weaknesses
The core idea of this paper, i.e., achieving motion cloning by constraining the temporal attention map, has already appeared in previous work, specifically in UniEdit [1] and MotionMaster [2]. The authors should acknowledge this prior work as the source rather than presenting it as an original contribution.

The primary technical distinction from [1][2] is the proposal to use a sparse temporal mask 
M rather than constraining all temporal attention maps. However, this choice lacks motivation or insight, which makes its effectiveness seem questionable.

Although the authors call this approach “motion cloning,” it is functionally similar to previous video editing methods [1][3], which also replace appearance while preserving motion. The authors should compare their method with this class of approaches. It is noteworthy that UniEdit [1] and MotionMaster [2] appear capable of achieving the same objectives as this work, namely cloning object and camera motion.

As mentioned in (1), the proposed method closely resembles [1][2]. Therefore, these methods should also be included in the comparisons. Moreover, It is recommended that the authors compare FID scores of generated videos to evaluate video quality.

[1] Bai J, He T, Wang Y, et al. Uniedit: A unified tuning-free framework for video motion and appearance editing[J]. arXiv preprint arXiv:2402.13185, 2024.
[2] Hu T, Zhang J, Yi R, et al. MotionMaster: Training-free Camera Motion Transfer For Video Generation[J]. arXiv preprint arXiv:2404.15789, 2024.
[3] Qi C, Cun X, Zhang Y, et al. Fatezero: Fusing attentions for zero-shot text-based video editing[C]//Proceedings of the IEEE/CVF International Conference on Computer Vision. 2023: 15932-15942.

### Questions
Please refer to the Weaknesses section.

### Soundness
3

### Presentation
3

### Contribution
2
