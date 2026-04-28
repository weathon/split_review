# LOVECon: Text-driven Training-free Long Video Editing with ControlNet

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5

## Abstract
Leveraging pre-trained conditional diffusion models for video editing without further tuning has gained increasing attention due to its promise in film production, advertising, etc. 
Yet, seminal works in this line fall short in generation length, temporal coherence, or fidelity to the source video. 
This paper aims to bridge the gap, establishing a simple and effective baseline for training-free diffusion model-based long video editing. 
As suggested by prior arts, we build the pipeline upon ControlNet, which excels at various image editing tasks based on text prompts. 
To break down the length constraints caused by limited computational memory, we split the long video into consecutive windows and develop a novel cross-window attention mechanism to ensure the consistency of global style and maximize the smoothness among windows. 
To achieve more accurate control, we extract the information from the source video via DDIM inversion and integrate the outcomes into the latent states of the generations. 
We also incorporate a video frame interpolation model to mitigate the frame-level flickering issue. 
Extensive empirical studies verify the superior efficacy of our method over competing baselines across scenarios, including the replacement of the attributes of foreground objects, style transfer, and background replacement. 
Besides, our method manages to edit videos comprising hundreds of frames according to user requirements.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposed a new long video editing method based on video controlnet and text-to-image latent diffusion models. The main contributions of the proposed method are 1) a cross-clip sparse attention to ensure the consistency of the long video while saving memory, 2) a latent fusion mechanism based on attention maps of the editing target, and 3) a frame smoothing mechanism based on near frame interpolation. The experimental results on 30 videos and the CLIP-based metrics demonstrate that the proposed method has better temporal consistency and video quality than the compared baselines.

### Strengths
- [writing] This paper is easy to follow, and the overall writing is good to me.
- [method] This work tackles the challenging task that editing long videos.
- [experiment] The visual results show that the proposed method allows the editing on the target area while maintaining the other image regions intact. Quantitative results also verify that the proposed method has better video quality and temporal consistency.

### Weaknesses
 - [method] The first drawback of the proposed method is that it is very similar to the VideoControlNet, where the main difference is the modification to tackle long video editing cases. 1) The cross-window attention is a special sparse attention mechanism, which has been widely used by other vision models. Specifically, the implementation details of this cross-window attention, such as the window size, stride, and the specific attention mechanism used within each window, are not sufficiently novel or distinct from existing sparse attention methods. It would be beneficial to see a more detailed analysis of how these parameters are chosen and how they impact performance compared to other sparse attention variants. 2) The latent fusion module has also been used in other works. While the idea of fusing latent representations based on attention maps is intuitive, the novelty of this specific implementation is not clear. A more detailed comparison with other latent fusion techniques, highlighting the differences and advantages of the proposed approach, would be beneficial. 3) The frame interpolation mechanism is a long-history video frame smoothing approach. The specific interpolation method, whether it is linear, cubic, or a more advanced technique, is not clearly specified. The contribution of this smoothing approach is unclear without more detailed analysis of its implementation and its impact on the final result.
- [experiment] In the visual comparison, I find the main visual benefit of the proposed method is that it only edits the target region while keeping the other part intact, which, according to my understanding, is contributed by the latent fusion module, making it hard to evaluate the effectiveness of the cross-window attention. It is difficult to isolate the impact of the cross-window attention from the latent fusion module. More visual comparisons, such as ablating the latent fusion module and only using cross-window attention, would be necessary to understand the contribution of each component. I think more visual (like fig. 5a) and quantitative comparisons without the latent fusion would help.
- [experiment] The experiments are only based on 30 videos, which is far from enough to show the robustness of the proposed method. Moreover, I feel CLIP-based metrics may not be reliable enough to evaluate the overall quality of the generated videos. The CLIP-based metrics may only capture the semantic similarity between the edited video and the text prompt, but it may not reflect the overall video quality, such as temporal consistency, sharpness, and artifacts. IS and FVD (if having a larger evaluation set as the reference) should be used for the quality comparison.

### Questions
No

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper aims to address the problems of limited video length and temporal inconsistency in text-driven video editing task.
It introduces a training-free pipeline based on ControlNet (i.e., LOVECon) for efficient long video editing, including three key designs.
In specific, LOVECon develops a novel cross-window attention mechanism to ensure the consistency of global style.
Secondly, it fuses the latents of source video to obtain more accurate control.
Finally, it incorporate a video frame interpolation model to deflicker the generated videos.

### Strengths
See summary.

### Weaknesses
1. The main contribution of long-video editing is limited in paper. The cross-window attention mechanism is common in long video editing/generation [1].
2. Question about visualization results of ControlVideo-II [2] in Fig.3. ControlVideo-II manages to achieve fine-grained control in original paper[2] (e.g., hair color), but fails to do so in Fig.3. Could the authors explain the reason?

### Questions
See weaknesses.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper focuses on long video editing with training-free diffusion models.  The authors propose a useful cross-window attention mechanism to ensure the consistency and length of the video. They also leverage DDIM for accurate control and a video frame interpolation model to mitigate the frame-level flickering issue. The authors presented rich and excellent experimental results, and provided their code and products in supplementary materials.

### Strengths
Long video editing, consistency maintenance, and structural fidelity are fundamental issues in text guided long video editing. The authors propose a simple and systematic solution for training free long video editing. The authors present a good number of experiments validating the effectiveness of their approach. The paper is overall well written and easy to follow.

### Weaknesses
1. The authors have pieced together too many other people's methods to achieve the goals, so their model capabilities are limited, such as being unable to perform shape transformations, object additions or deletions. So their products are limited to color or style changes.

2. The innovation of the methods proposed by the authors is limited, as they have not effectively established the temporal information of the video. The so-called cross-window is naive (a minor change of ControlVideo **[1]**) and may be helpful for local video smoothing, but it still cannot truly establish the temporal dependence of long videos. This is reflected in the experimental results that although the generated video actions are locally coherent, the overall appearance is somewhat strange.

### Questions
Cross-window attention is proposed to improve inter-window consistency, then how do the authors ensure consistency within the window? 
As shown in Figure 5 (a), fully crossframe attention-based ControlVideo not only maintains the loyalty of the background, but also maintains the temporal consistency of the target subject. On the contrary, the author's method blurs the background and changes the target subject in the temporal sequence (the car window turns red).

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
