# FLATTEN: optical FLow-guided ATTENtion for consistent text-to-video editing

- Decision: Accept
- Scores: 8, 5, 5, 8

## Abstract
Text-to-video editing aims to edit the visual appearance of a source video conditional on textual prompts.
A major challenge in this task is to ensure that all frames in the edited video are visually consistent. 
Most recent works apply advanced text-to-image diffusion models to this task by inflating 2D spatial attention in the U-Net into spatio-temporal attention.
Although temporal context can be added through spatio-temporal attention, it may introduce some irrelevant information 
for each patch and therefore cause inconsistency in the edited video. 
In this paper, for the first time, we introduce optical flow into the attention module in the diffusion model's U-Net to address the inconsistency issue for text-to-video editing.
Our method, \textbf{FLATTEN}, enforces the patches on the same flow path across different frames to attend to each other in the attention module, thus improving the visual consistency in the edited videos.
Additionally, our method is training-free and can be seamlessly integrated into any diffusion-based text-to-video editing methods and improve their visual consistency.
Experiment results on existing text-to-video editing benchmarks show that our proposed method achieves the new state-of-the-art performance. In particular, our method excels in maintaining the visual consistency in the edited videos.
The project page is available at \footnotesize{ \url{https://flatten-video-editing.io/}}.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Summary: The paper focuses on text guided video editing. Previous methods to tackle this problem extend the text-to-image U-net to the temporal dimension to implement spatiotemporal attention where patches from different frames attend to one another. The paper argues that such methods introduce irrelevant information, since they allow all patches in the video to attend to one another where in fact many of these spatiotemporal patch to spatiotemporal patch connections might be irrelevant. To address this problem, the paper suggests using optical flow to guide the attention. Specifically, a pre-trained optical flow network is used to estimate the flow field and tracks of patches along flow trajectories are aggregated to enforce only patches on the same trajectory to attend to one another in a second step of MHSA. This results in more visual-consistent videos as the paper demonstrate both qualitatively and qualitatively 

Method: First, the "standard" the text to image U-net architecture is inflated to account for the temporal dimension and the image patch spatial self attention mechanism is replaced with spatiotemporal self-attention with all patches in the video used as tokens for Q,K,V. Secondly, a pre-trained optical flow network is employed to compute the flow field along the frames of the video. Tracks of patches (in the latent space) are aggregated using the downsampled flow field. Next, self attention is performed between patch-embeddings on the same track. Specifically, the queries are taken from the original dense spatiotemporal MHSA, but for every query associated with a specific patch - the keys and values in MHSA are only the ones which are associated with patches on the same track. Note that this method does not require re-training as it only refines the existing embedded spatiotemporal patch embedded tokens with additional information by applying MHSA again but with restrictions on which patches can attend to one another (where this "restriction" is derived from the flow field).

Experiments: the paper compares the proposed method against 5 publicly available text-to-video editing methods on two standard benchmarks. The proposed method performs favourably both in terms of visual quality/alignment metrics  and visual consistency metrics. The paper also presents quantitative results as well as a user-study demonstrating the effectiveness of the method, particularly in the aspect of visual-consistency when motion is introduced.

### Strengths
The proposed method is sound and original. The framework is very simple, does not require further training and can be easily plugged to various existing architectures. The paper is well written and the effectiveness of the method is demonstrated relatively well.

### Weaknesses
In my opinion, a drawback of the method is the heavy reliance on pre-computed flow field using a pre-trained network that is used as a black box. Thus, errors in this step can negatively affect the results of the proposed pipeline. However, the paper does not address this issue and there are no results to measure the robustness of the method. See question in the section below.

### Questions
As I understand, the method is designed to improve visual consistency, particularly with respect to motion. The method relies on optical flow to "enhance" the embedded tokens with motion information derived from the flow field. As the pipeline relies on flow field computation and errors introduce in that step may affect the results. Something that is missing in the paper in my opinion is some discussion/experiments/results on how robust is the method to mistakes in the flow field computation. Specifically: 

1. How well the proposed method can handle large motion (large displacement in the flow field) or abrupt motion? are there any examples you can provide? 
2. How well the proposed method can handle videos in which both global motion (camera movement) and local motion (object movement) are present? are there any examples you can provide? 
3. Are there any situations where the method can do "more harm than good"? I mean, cases where the errors in the flow-field computation can cause the method to produce worse results than the baseline? how often do they occur? 
4. Are there any examples that you can provide in which the flow field is far from accurate? In those cases, are the results worse than the baseline, meaning the method did "more harm than good"?
5. How does the results change with respect to accuracy of the flow field? For example, by taking a specific video and flow field results from several models where some perform dramatically worse than others or by gradually corrupting the flow field and measuring the affect on the results?

I find that the qualitative results provided the supplemental video are extremely helpful (particularly the "racing trucks" example in which the results of other methods are provided). I would be grateful if the authors would be able to provide more examples that address the questions above.

### Soundness
4 excellent

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
To improve the visual consistency for text-to-video editing， FLATTEN is proposed to enforce the patches on the same flow path across different frames to attend to each other in the attention module. Experiment results on existing text-to-video editing benchmarks show that the proposed method achieves the new state-of-the-art performance.

### Strengths
The proposed Flow-guided attention is intuitive and makes sense.

### Weaknesses
1. The method is only suitable for scenarios where every pixel in the original video aligns spatially with the generated video. For misaligned areas, the optical flow trajectory of the original video is not appliable for the motion of the generated video, leading to incorrect key and query identifications. For instance, in the example of transforming a cat to a tiger in Figure 1, the tiger's face is larger than the cat and thus there exist pixels that belong to the tiger's face and belong to the background in the cat example. For the original video with the cat, these pixels belong to the background with an optical flow near zero. However, for the tiger, it's part of the face and should rotate with the head, requiring an optical flow describing a leftward movement. This sets too high a requirement for editing scenarios.

2. If optical flow tracking is accurate enough, why not simply select a keyframe and then directly copy pixels following the same optical flow path to other frames? This approach seems more accurate than aligning through attention. For example, bilinear interpolation combined with optical flow is often used to predict the next frame in videos.

3. In the provided MP4, there is only one visual comparison, which is too limited. It's suggested not to cherry-pick comparisons so that the effectiveness of the method can be judged intuitively.

### Questions
See Weakness.

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
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes text-guided video editing systems that considers optical flow to preserve temporal consitency
In detail the temporal attention is guided by the paths estimated from optical flow.

### Strengths
[+] The idea makes sense that involves optical flow into the diffusion model for holding temporal consistency 
[+] Performances are enhanced compared to previous editing systems

### Weaknesses
[-] Optical flow can be effective when a single objective appears. However, we can easily come up with other cases including occlusion, objects' appearing or disappearing, or else. Therefore the method seems sensitive to the input video, which can ruin the attention or even worse than previous temporal attention methods. Can you explain why the method should be better than previous temporal attention?

[-] The performances are better than many previous works. What are the samples that this method validates? I am quite curious about the videos that they evaluated.

[-] Are there any qualitative or quantitative results about the trajectory patches in the aforementioned cases in question [1]? I want to see if the trajectory is truely following the flow of objectives in the video.

### Questions
My questions are above

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper investigates the text-to-video editing task. To improve the temporal consistency, they introduce dense spatio-temporal attention and flow-guided attention to acquire information from the whole video. The proposed method achieves good performance on the test videos.

### Strengths
1. The proposed flow-guided attention is novel and effective.

2. The proposed flow-guided attention can be applied to other base models to further improve the temporal consistency.

3. Extensive experiments and ablation studies demonstrate the effectiveness of the proposed method.

### Weaknesses
1. The comparison with previous works is very limited. For the video editing task, multiple images should be shown for qualitative comparison in the main paper (Figure 5), which is important to verify the temporal consistency. Furthermore, even in the supplementary material, only one example is compared with previous works, which is not convincing. I compared the ``wolf’’ example with the TokenFlow example on its website. The results of this paper are not good to me.

2. From my perspective, the text information for editing is only acquired by cross attention with editing prompts. Other editing techniques like prompt-to-prompt are not used. This might cause the inaccurate editing of the background. For example, in the first example of Figure 5, the grass also turns yellow, while TokenFlow and FateZero can better keep the background. The core issue is that the method's reliance solely on cross-attention for textual alignment may limit its ability to perform precise edits, especially when compared to techniques that explicitly emphasize the edited regions. The paper's results, particularly the truck example, seem to contradict this, showing better editing than TokenFlow, which is unexpected given TokenFlow's use of PnP-Diffusion. A direct comparison under identical settings with examples from the TokenFlow website is needed to clarify this discrepancy.

3. DSTA conducts cross attention across all 32 frames, which takes many computational resources. It is better to compare the computational cost and inference time with other methods. Furthermore, the VRAM requirements of DSTA are likely substantial, especially when considering that TokenFlow applies DSTA only to keyframes, and methods like Pix2Video and ControlVideo use cross-frame attention on a limited number of reference frames. The paper should provide a detailed analysis of VRAM usage, as this is a crucial factor for practical application, especially for users without high-end GPUs like 80GB A100s.

4. There are also some works based on optical flow trajectory for video generation [ref-1,ref-2,ref-3], which should also be discussed in the related work.

### Questions
The paper is good, but I still have some concerns as in the weaknesses.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good
