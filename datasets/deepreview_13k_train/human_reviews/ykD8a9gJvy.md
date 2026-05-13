# Generative Inbetweening: Adapting Image-to-Video Models for Keyframe Interpolation

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
We present a method for generating video sequences with coherent motion between a pair of input key frames. We adapt a pretrained large-scale image-to-video diffusion model (originally trained to generate videos moving forward in time from a single input image) for key frame interpolation, i.e., to produce a video in between two input frames. We accomplish this adaptation through a lightweight fine-tuning technique that produces a version of the model that instead predicts videos moving \emph{backwards} in time from a single input image. This model (along with the original forward-moving model) is subsequently used in a dual-directional diffusion sampling process that combines the overlapping model estimates starting from each of the two keyframes. 
   Our experiments shows that our method outperforms both existing diffusion-based methods and traditional frame interpolation techniques. Please see our project page at \href{https://svd-keyframe-interpolation.io/}{ svd-keyframe-interpolation.io}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents Generative Inbetweening, a method for creating intermediate frames between two keyframes by adapting a pre-trained image-to-video diffusion model. This model adapts Stable Video Diffusion with dual-directional diffusion: generating video frames that interpolate both forwards and backwards in time. 
This approach achieves motion-coherent inbetween frames through a technique that involves reversing the temporal self-attention maps within the U-Net model to generate backward motion from the endpoint keyframe, then combining this with forward-motion frames to produce smooth video sequences.
Evaluations on the Davis and Pexels datasets show the method’s performance against the existing techniques, including TRF and FILM, in terms of frame coherence and motion fidelity for larger motion gaps.

### Strengths
Strengths
The paper’s fine-tuning approach makes effective use of a pre-trained model (SVD) to generate backward motion without requiring extensive additional data or full retraining. This demonstrates an efficient approach to model adaptation.
By developing forward-backward motion consistency through temporal self-attention, the method generates smooth and coherent transitions, especially in scenarios with long differences between keyframes. 
The paper provides good experimental results, using both qualitative comparisons and metrics like FID and FVD to validate performance improvements over established baselines (FILM, TRF, etc.).
Ablations explore the impact of various components and the paper transparently discusses limitations, providing clarity on the model's boundaries, especially with non-rigid motion types.

### Weaknesses
While the paper includes comparisons with baseline models, it lacks an in-depth discussion on the unique metrics or benchmarks used to capture differences between models, particularly in subjective aspects like motion realism. Including a more detailed discussion on why certain metrics (e.g., FID or FVD) were selected over others could clarify the relevance of the performance gains. Specifically, the paper does not delve into how well FID and FVD correlate with human perception of motion quality, which is crucial when evaluating video generation tasks. A discussion of the limitations of these metrics, such as their potential insensitivity to certain types of artifacts or motion incoherencies, would also be beneficial.

The model relies heavily on SVD’s motion priors, which, as the authors note, can struggle with non-rigid or complex kinematic movements. While the paper acknowledges this, further discussion on how future models might address such limitations, possibly by incorporating other motion datasets or additional temporal constraints, would add depth to the future directions. For instance, the paper could explore the potential of incorporating optical flow or pose estimation as additional inputs to guide the generation process, which might help in handling more complex motion patterns. The current approach seems to be limited by the inherent biases of the pre-trained model, and it would be useful to see a discussion on how these biases might be mitigated.

Although the fine-tuning approach is a strength, it may be challenging for readers unfamiliar with diffusion models to follow the model adaptation process fully. More visual aids or pseudocode detailing the fine-tuning and dual-directional sampling steps would enhance clarity. The paper could benefit from a more detailed explanation of the specific modifications made to the SVD model, including the exact layers that are fine-tuned and the rationale behind these choices. Furthermore, a step-by-step breakdown of the dual-directional sampling process, including how the forward and backward motion components are combined, would greatly improve the accessibility of the method.

### Questions
Given the model's limitations with non-rigid motions, did the authors explore any alternative solutions, such as enforcing additional temporal consistency constraints or incorporating motion priors for articulated objects?

While the quantitative results are promising, did the authors consider conducting a user study to assess perceived motion realism, as subjective assessments might capture nuances that FID/FVD cannot?

Could the authors elaborate on how sensitive the model's performance is to the choice of the 180-degree rotation in the self-attention map? Did they experiment with other configurations for reversing the temporal interaction?

### Soundness
3

### Presentation
2

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
The paper focuses on the keyframe interpolation problem, which has been overlooked in existing large-scale video generation models. The article proposes a solution to this task by treating keyframe interpolation as a forward video generation from the first frame and a backward generation from the last frame, followed by a coherent fusion of the generated frames. Based on this, the paper reuses existing large-scale image-to-video models to obtain a video generation model for backward motion by reversing temporal interactions. Additionally, it uses sampling techniques to blend paired frames generated by the forward and backward temporal directions with synchronized paths, producing intermediate frames.

### Strengths
This paper fills a gap in the field of large-scale video generation, specifically keyframe interpolation, at a related lower cost. As summarized earlier, this paper presents a novel pipeline to generate synchronized frames and targeted frame fusion techniques to achieve smooth transitional videos.

### Weaknesses
The keyframes shown in the paper have relatively small motion ranges and require extensive pixel mapping; otherwise, obvious artifacts occur (as mentioned in the limitations), making this approach unsuitable for large-scale object or camera movements. Specifically, the method struggles with significant occlusions and disocclusions between keyframes. The reliance on pixel-level correspondence between keyframes limits its applicability to scenarios with substantial changes in viewpoint or object pose. Furthermore, the method's performance is likely to degrade when the motion between keyframes involves complex deformations or non-rigid transformations, as the simple averaging fusion may not be sufficient to handle such cases, leading to ghosting or blurring artifacts.

### Questions
1. As noted in the weaknesses, I observed that in the cases provided, the camera and object movements between keyframes are slight. Can this method still perform well when there is a significant difference between the given keyframes? Additionally, when the keyframe difference is large, the backward generation may be unable to reuse the rotated attention matrix from the forward generation, potentially causing large discrepancies in frames generated at the same time step. In such cases, can fusion still work effectively?
2. This generation pipeline seems to require a substantial number of corresponding points between keyframes. Beyond the issue of low overlap mentioned earlier, I’m also curious whether the method could still generate smooth transitions if, for example, one object in the keyframes—such as a fish in the ocean—undergoes a mirrored flip, meaning every point has a mapped counterpart but with an orientation change.
3. The paper adopts simple averaging for intermediate frame fusion (line 281), but intuitively, frames generated closer to the initial keyframe might exhibit higher quality. Why not use weighted averaging instead? For example, linearly blending frames based on their proportional distance from each keyframe might yield smoother transitions and higher quality.

### Soundness
4

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
The author proposes a novel method for distant keyframe interpolation, leveraging pretrained image-to-video diffusion models. This approach generates intermediate frames by predicting and fusing forward and backward video sequences, conditioned respectively on the given start and end frames. The author introduces a lightweight fine-tuning technique to tackle the key challenge of predicting backward video sequences from the end frame. Additionally, a dual-directional diffusion sampling strategy is employed to effectively fuse noise in both forward and backward directions.

### Strengths
- The paper is clear and easy to understand, with well-presented motivation and methodology.
- The proposed method is novel, straightforward, and effective, demonstrating improvements over the selected baseline interpolation methods.

### Weaknesses
Further ablation studies on the proposed method could explore:
1. **Training Dataset Scale**: In the paper, the model is fine-tuned with only 100 videos. It would be interesting to investigate how the scale of the training dataset affects the model’s performance.
2. **Fine-tuning Modules**: The paper fine-tunes only the value and output projection matrices in the self-attention layers of the backward framework. Since there might be a gap for the forward motion in the context of the image-to-video task and the interpolation task, it would be worth exploring whether the interpolation performance could be further improved by fine-tuning both the forward and backward framework matrices while preserving the attention map rotation operation.

### Questions
Please kindly refer to the Weaknesses.

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
This paper addresses the keyframe interpolation problem by leveraging the large-scale image-to-video diffusion model, Stable Video Diffusion, to generate frames between a pair of keyframes. 

Unlike traditional image-to-video models that generate frames in a forward-moving manner, this paper proposes finetuning the model for backward-moving videos and utilizing both the original and finetuned models together during inference. 

To leverage the knowledge from the forward-moving model, only the value and output projection matrices of the 3D self-attention layers are trained, and the attention maps from the forward-moving videos are rotated by 180 degrees and inserted into the finetuned backward-moving model. 

During inference, the attention maps generated by the forward-moving model are rotated and applied to the finetuned backward-moving model, and the predictions from both models are fused. 

This approach demonstrates superior performance over FILM and TRF on the Davis and Pexels datasets, despite being trained on only 100 videos.

### Strengths
- This method is both parameter-efficient and data-efficient, making it highly effective even with limited resources.

- It leverages an open-source model, which enhances its accessibility and contributes to the broader video interpolation research community.

- It demonstrates superior qualitative and quantitative performance compared to FILM, a well-known method for large motion interpolation, as well as TRF, which also uses Stable Video Diffusion.

- In Section 5, the qualitative results are thoroughly explained, clearly highlighting the strengths of this approach in various aspects.

### Weaknesses
 - Video interpolation performance can vary significantly based on FPS and the magnitude of motion, but the paper does not provide any analysis of these factors. Besides the motion bucket ID mentioned in the paper, Stable Video Diffusion also takes FPS as a condition. The paper would benefit from demonstrating whether the method still outperforms FILM and TRF when varying the motion bucket ID and FPS during finetuning and inference.

- The proposed method requires both the base forward-moving model and the finetuned backward-moving model during both training and inference, making it more computationally intensive compared to a baseline of  
 fine-tuning on video interpolation dataset.

### Questions
- There are three publicly available weights for Stable Video Diffusion (img2vid, img2vid-xt, img2vid-xt-1-1). Which of these weights did the authors use?

- Stable Video Diffusion applies different classifier-free guidance scales to each frame. Did the authors use the same approach in this paper?

### Soundness
3

### Presentation
3

### Contribution
3
