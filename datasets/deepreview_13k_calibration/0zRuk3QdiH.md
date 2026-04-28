# Multi-Shot Character Consistency for Text-to-Video Generation

- Decision: Reject
- Avg Score: 5.75
- Scores: 5, 5, 8, 5

## Abstract
Text-to-video models have made significant strides in generating short video clips from textual descriptions. Yet, a significant challenge remains: generating several video shots of the same characters, preserving their identity without hurting video quality, dynamics, and responsiveness to text prompts. We present \ourmethod{}, a \textit{training-free} method to enable pretrained text-to-video models to generate multiple shots with consistent characters, by sharing features between them. Our key insight is that self-attention query features (Q) encode both motion and identity. This creates a hard-to-avoid trade-off between preserving character identity and making videos dynamic, when features are shared. To address this issue, we introduce a novel query injection strategy that balances identity preservation and natural motion retention. This approach improves upon naive consistency techniques applied to videos, which often struggle to maintain this delicate equilibrium. 
Our experiments demonstrate significant improvements in character consistency across scenes while maintaining high-quality motion and text alignment. These results offer insights into critical stages of video generation and the interplay of structure and motion in video diffusion models.
Project page: \url{https://research.nvidia.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper targets the problem of character consistency in text-to-video generation. The authors propose a training-free method to solve this problem. They find the query in the attention encodes the information of both motion and identify, which leads to the trade-off between motion dynamics and identity consistency. The experimental model used is VideoCrafter2. To solve the trade-off problem, they propose a new query injection method. Specifically, they share features between different video clips. Then, they replace the Q (query) with those from the original generation (to maintain motion from the original generation). After that, they leverage the flow map from vanilla keyframes to guide the Q injection. Their results achieve the character consistency while keeping the original motion dynamics and text alignment. The text alignment is evaluated via user study. The overall metrics for evaluation are three aspects: motion degree, id consistency, and motion text alignment.

### Strengths
1. The method is tuning-free and does not require any further training.
2. The results outperform baseline methods. Some of the provided visual results look good.

### Weaknesses
1. The paper is relatively hard to follow regarding the details of the method part.
2. Lack of novelty: 1. The id presevering mechanism is built upon the SDSA. the SDSA is adopted from ConsiStory [Tewel et al. 2024] with two minor modifications: (1) The attention not attend to each other with all frames from different clips, but one single frame from each clip. (2) The mask estimation use ClipSeg, rather than estimated from the cross attention. 2. The motion preserving is leveraging TokenFlow [Geyer et al. 2023] to inject the motion based on the flow from original keyframes. Thus, the method is like a A+B combination with some minor modifications.
3. The key insight "self-attention query features (O) encode both motion and identity" lack experimental results to demonstrate.
4. The results are not perfect, e.g., inconsistent hairstyles in the 3rd row of Figure 1.
5. The evaluation does not contain the overall video generation quality and the qualitative semantic alignment scores. 
6. Minor formate issues like inconsistent figure reference:  Figure 1 and Fig. 4; And strange line break at line 244 and line 291.

### Questions
1. Does the overall generation quality decrease after the proposed method?
2. How does the motion quality changed after the proposed method?

### Soundness
3

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
3

### Summary
This paper presents Video Storyboarding, a training-free method that enhances pre-trained text-to-video models to generate multiple shots with consistent characters while maintaining high video quality and responsiveness to text prompts. By leveraging self-attention query features that capture motion and identity, the method addresses the trade-off between character consistency and video dynamics through a novel query injection strategy. Experimental results show significant improvements in character consistency and motion quality, offering insights into the video generation process and the interplay of structure and motion in diffusion models.

### Strengths
1. This paper introduces a training-free method to ensure charactoer consistency and motion adherence in producing multi-shot video sequences.
2. This paper presents a two-phase query injection strategy to balance encoding motion and identity.
3. A benchmark and evalution protocol are proposed to evaluate consistency of video generation.

### Weaknesses
1. The conducted experiments are not comprehensive, including two aspects: (a) The paper only provides several comparison samples. (b) The paper misses some important baseline methods, e.g., VSTAR[1]
2. Although the purpose of the paper is to maintain consistency of characters across different video clips, the results are not particularly good. For example, in Fig.3, the color and style of clothes change across different video shots.

### Questions
1. The paper only demonstrates the performance of a single character across different videos, and the reviewer is curious about how the proposed  method performs with multiple characters.
2. The prompt in the paper provides overly detailed descriptions of the character. Would a more concise description impact character consistency? For example, replace the "Cinematic, middle-aged female athlete" in Fig.8 with "A woman".

### Soundness
3

### Presentation
2

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
This paper proposes a method called "Video Storyboarding" to generate multi-shot videos with consistent characters across different scenes while preserving motion quality.

### Strengths
1. Framewise Subject-Driven Self-Attention to maintain consistency without compromising motion
2. Novel two-phase query injection strategy to balance identity preservation and motion quality
3. Adaptation of refinement feature injection to both conditional and unconditional denoising steps

### Weaknesses
1. Approach limited to short video clips, unsure how it would scale to longer videos
2. Balancing identity preservation and motion quality is still challenging, with potential tradeoffs

### Questions
Overall, this is a well-designed and rigorously evaluated method that represents a significant advancement in generating coherent multi-shot video sequences. The authors have done a commendable job in addressing the complex challenge of maintaining character consistency while preserving natural motion.

Some questions for the authors:

1. Have you explored any strategies to further improve the balance between identity preservation and motion quality? Are there other techniques beyond query injection that could be investigated?
2. How do you envision this approach scaling to longer video sequences? What additional challenges might arise, and how could the method be adapted to handle them?
3. The user study results showed that the ConsiS Im2Vid baseline achieved the highest set consistency among the baselines. Can you comment on the strengths of this approach and how it might be combined or compared with your Video Storyboarding method?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper aims to generate multi-shot videos with consistent characters in a zero-shot manner. They claim that there is a trade-off between preserving character identity and video dynamics, thereby designing a two-phase approach, Q-preservation and Q-Flow, to balance the two respects.

### Strengths
1. **Training-Free Approach for Subject Consistency Across Shots**: This work offers a training-free method for generating subjects with consistent identity across varying scenarios and shot transitions, which is valuable for practical applications where maintaining coherence in subject appearance is essential.

2. **Novel Insights on Self-Attention Query Features**: The authors provide fresh insights into the role of self-attention query features, demonstrating that these features effectively capture both motion and identity.

3. **Query-Preservation and Q-flow Techniques**: By preserving query features during early denoising and applying a tokenflow-inspired approach to select keyframes, the method achieves partial injection of query features to adjacent frames. Although it draws heavily from ConsisStory and TokenFlow, this approach has demonstrated effectiveness in enhancing subject consistency and motion dynamics to a certain extent.

### Weaknesses
1. **Limited Novelty in Video Storyboarding**: The innovation of the proposed video storyboarding approach is limited. The primary method relies on frame-wise SDSA, which largely mirrors the approach used in ConsiStory. The only notable difference lies in the mask source, utilizing CLIPseg and OTSU segmentation rather than cross-attention. This modification, while practical, does not represent a significant conceptual advancement in the core methodology of multi-shot video generation.

2. **Poor Writing and Project Organization**: The paper's writing and the project page's layout hinder comprehension, making it difficult for readers to follow the key contributions the authors intend to convey. The lack of clear definitions for key terms and the complex structure of the method section make it challenging to understand the technical details and the novelty of the approach. The project page lacks clear navigation and detailed explanations, further complicating the understanding of the method.

3. **Minimal Improvement over Baseline Models**: The generated video storyboarding results appear similar to those produced by existing video generation baselines like Videocrafter2 or TokenFlow encoder, with little noticeable difference in output quality. The method does not demonstrate a significant leap in terms of visual fidelity or subject consistency compared to these established baselines, raising questions about its practical utility.

4. **Lack of Motion Dynamics**: The method demonstrates limited motion dynamics. In most video segments, the objects remain static, and in every case, the object consistently occupies the center of the frame, resulting in rigid, uninspired visuals. The lack of varied camera angles and object movement severely limits the expressiveness and realism of the generated videos. The method fails to capture the dynamic nature of real-world scenarios, resulting in a static and unengaging visual experience.

5. **Overclaiming the Benchmark**: The authors’ claim of establishing a benchmark based on a dataset of only 30 videos, each containing 5 video shots, is unsubstantiated. This dataset is insufficiently sized and lacks diversity, with evaluations limited to character consistency and dynamic degree, providing a narrow view that does not comprehensively assess the model's capabilities. The evaluation metrics are also limited, failing to capture other important aspects of video quality, such as background consistency and temporal coherence.

### Questions
1. **Inconsistencies in Object Appearance and Action**: In the ablation study on query preservation (`ablation_q`), inconsistencies persist. For example, in the first video, the right hand of the Muppet character appears red, while in the third shot, it is not. Additionally, although the Muppet is intended to perform aerobics in a Sesame Street setting, it merely flicks its hand briefly, failing to convey the intended action sequence.

2. **Static Object Issues in ConsiStory Component Ablation Study**: In the ablation study on ConsiStory components for video generation, the rabbit character intended to surf, train, and ride a bike appears mostly static in the first and third shots. This raises the question of whether these issues stem from limitations in the base model’s dynamic capabilities. If so, would using models with stronger dynamic performance, such as Dynamic Crafter or CogVideo, potentially improve motion consistency and address these static object limitations?

If the video dynamic problem is addressed, I am willing to increase my score.

### Soundness
2

### Presentation
1

### Contribution
2
