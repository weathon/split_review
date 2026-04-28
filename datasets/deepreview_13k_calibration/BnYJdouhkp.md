# Promptus: Representing Real-World Video as Stable Diffusion Prompts for Video Streaming

- Decision: Reject
- Avg Score: 5.83
- Scores: 5, 5, 5, 8, 6, 6

## Abstract
With the exponential growth of video traffic, traditional video streaming systems are approaching their limits in compression efficiency and communication capacity. To further reduce bitrate while maintaining quality, we propose Promptus, a disruptive novel system that streaming prompts instead of video content, which represents real-world video frames with a series of "prompts" for delivery and employs Stable Diffusion to generate videos at the receiver. To ensure that the prompt representation is pixel-aligned with the original video, a gradient descent-based prompt fitting framework is proposed. Further, a low-rank decomposition-based bitrate control algorithm is introduced to achieve adaptive bitrate. For inter-frame compression, a temporal smoothing-based prompt interpolation algorithm is proposed. Evaluations across various video genres demonstrate that, compared to H.265, Promptus can achieve more than a 4x bandwidth reduction while preserving the same perceptual quality. On the other hand, at extremely low bitrates, Promptus can enhance the perceptual quality by 0.139 and 0.118 (in LPIPS) compared to VAE and H.265, respectively, and decreases the ratio of severely distorted frames by 89.3% and 91.7%. Our work opens up a new paradigm for efficient video communication. Promptus will be open-sourced after publication.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this paper, the authors leverage a stable diffusion model as a compression method to encode video into text (embedding format), using this text embedding as the video representation. The entire process resembles information distillation, where trainable low-rank features are used to form the prompt embedding. After optimization, these low-rank factor matrices become the compressed video representation. The authors propose several solutions to control bitrate, perform inter-frame compression, and ensure pixel alignment.

### Strengths
(+) Using stable diffusion as a distillation approach is interesting.

(+) The paper is well-written, with most figures well-designed, illustrated, and easy to follow.

### Weaknesses
(-) My major concern is whether there are severe flicker issues or temporal over-smoothing in the decoded video, as the authors did not submit any video as a supplementary file. Considering that the rebuttal can only show images, I suggest the authors present an x-t slice, as used in [1], for a highly dynamic video. The x-t slice would provide a better visual understanding on the temporal consistency.

(-) Could the authors justify why it is necessary to use stable diffusion as the intermediate medium for video compression? Why not directly use CLIP or the SD decoder to distill the frames? Is it because CLIP is not powerful enough?

(-) The VAE could introduce significant color tone-mapping issues and spatial blurriness. Did the authors encounter similar issues on a large scale? I can see severe color issues in Figure 10, particularly in the boy's eye and background. Consequently, I am also concerned about some analyses in Section 4.4. In my understanding, the performance drop on the Animerun dataset occurs because those frames are edge cases for SD/VAE, which is why there are numerous color mapping issues.

(-) Since the VAE and diffusion models are fixed, how do the authors ensure that the frames being represented and compressed fall within the diffusion model's domain of knowledge? Additionally, is the main source of encoding performance derived from CLIP/VAE or the U-Net? I did not see a related discussion on this matter.

(-) The qualitative result comparisons are insufficient and do not convincingly demonstrate the proposed method's promise.

### Questions
All my questions are outlined in the weaknesses section. My major concerns are the necessity of using stable diffusion as a streaming approach, the insufficient qualitative result comparisons, and the generalization issues related to the VAE or other components.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposed a pipeline called Promptus, which uses prompts instead of video content for streaming and uses Stream Diffusion to generate video at the receiving end. In order to ensure that the prompt representation is aligned with the original video, a prompt fitting framework based on gradient descent is proposed. In addition, a bitrate control algorithm based on low-rank decomposition is introduced to achieve adaptive bitrate. The paper conducted experiments on several individual videos such as QSR Animerun to prove that Promptus can achieve more than 4 times bandwidth reduction while maintaining the same perceptual quality. At the same time, the perceptual quality is higher than that of traditional methods at extremely low bitrates.

### Strengths
Modules such as gradient descent based prompt fitting are proposed to solve the inconsistency problem of diffusion model generation in video streaming transmission.
Experiments demonstrate the effectiveness of this method in LPIPS, compression ratio.
The real-time issues are well covered in the supplementary material.

### Weaknesses
According to the supplementary, Promptus requires 8952MB of memory to run, but most existing methods [1, 2] do not require such a high video memory requirement, and in actual scenarios, many devices do not have such a high video memory, such as mobile phones. Therefore, this diffusion model-based method can only be used on high-performance PCs with high video memory in the context that diffusion models still require high memory. The high memory requirement significantly limits the practical applicability of the proposed method, especially when compared to traditional codecs that can operate on resource-constrained devices. Furthermore, the paper does not adequately explore the trade-offs between memory usage and compression performance, which is crucial for practical deployment.

As far as I know, there are still many unique problems in the diffusion model in content generation, such as "multiple fingers" and "words cannot express" problems. I hope the author can provide relevant experiments to prove what results the method in this paper will have when facing the unique problems of SD itself. The paper should include a more thorough analysis of the failure modes of the diffusion model, particularly in scenarios where the prompt fitting struggles to accurately represent complex details or when the diffusion model generates artifacts. This analysis should include specific examples and a discussion of the limitations of the proposed approach.

Although the author said in the experiment that the resolution can be arbitrary, since this work relies on the representation capability of SreamDiffusion[3] based on SD-Turbo or LCM, many "high-resolution" images are not included in the training set of SD-Turbo or LCM. Can Promptus effectively transmit videos with various resolutions and high resolutions that it has not seen during SD training? The paper lacks a detailed investigation into the impact of resolution on the performance of the proposed method. Specifically, it is unclear how the prompt fitting process adapts to resolutions significantly different from those used during the training of the underlying diffusion model. The paper should include experiments that systematically vary the resolution and analyze the resulting impact on perceptual quality and compression efficiency.

The specific diffusion model version used is not written in the main text. It is recommended to write it in the main text. In addition, the time speed and memory overhead of this method will be the primary consideration for most people. I suggest the author will move such experiments into the main paper. The absence of these crucial details in the main paper makes it difficult to assess the practical viability of the proposed method. The paper should include a detailed breakdown of the computational cost, including encoding and decoding times, as well as the memory footprint, to allow for a fair comparison with existing video compression techniques.

### Questions
This paper is novel in the field of video streaming, and the idea of using prompt to transmit video is very interesting. However, the application scenarios are narrow, and there is a lack of more feasibility experiments on diffusion models. Therefore, I suggest that the author first provide sufficient evidence to fully demonstrate that Stable Diffusion is a feasible representation.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces Promptus, an innovative system that represents real-world video frames as prompts for Stable Diffusion, enabling ultra-low bitrate video streaming by sending prompts instead of raw video content. Evaluations show that Promptus achieves more than a 4x reduction in bandwidth compared to H.265 while preserving similar perceptual quality and demonstrating significant quality improvements at extremely low bitrates.

### Strengths
1. Novel application of GAN AI for video streaming: By leveraging Stable Diffusion for video generation through prompts, Promptus introduces a novel approach to reducing video bandwidth requirements.
2. The gradient descent-based prompt fitting framework ensures pixel-level alignment, maintaining visual consistency with original frames, which is challenging for generative models.
3. The low-rank decomposition approach allows Promptus to adjust bitrate based on network conditions, enhancing usability in fluctuating bandwidth situation.
4. Temporal smoothing regularization reduces the need to transmit prompts for every frame, significantly cutting down bandwidth usage.
5. Promptus shows a marked improvement in bandwidth efficiency, achieving a fourfold reduction over H.265 while maintaining perceptual quality, especially in complex or high-frequency video content.

### Weaknesses
1. Promptus’s primary goal is to find an inverse prompt that moves points represented by noise to the target image’s location in latent space. However, it’s unclear how the model handles abrupt scene cuts within videos. Scene cuts could disrupt continuity, as prompts optimized for one scene may not generalize to an entirely different visual context, the generated frames might misrepresent scene transitions.
2. As described in 485 lines, as bitrate decreases, Promptus reduces the descriptive capacity of prompts. How the model maintains accurate content representation at these lower bitrates. Why this simplification not lead to slight misalignments in generated frames? More insights into the model’s mechanisms for preserving spatial and temporal consistency at low bitrates would clarify this point.
3. The paper predominantly relies on LPIPS as the primary evaluation metric. Incorporating additional metrics, such as SSIM or VMAF, would provide a more holistic assessment of visual quality, particularly in capturing structural integrity and perceptual alignment.
4. Although the supplementary materials provide information on the complexity of the proposed method, the paper lacks direct comparisons with the computational complexity and runtime of other state-of-the-art (SOTA) benchmarks. 
5. The experimental results compare Promptus only with H.265 and a VAE model, omitting comparisons with other recent SOTA benchmarks in video compression and generation.

### Questions
1. The paper primarily uses linear interpolation for temporal smoothing between frames. Has the team explored other interpolation methods?
2. The visualizations in Figure 10 show noticeable color discrepancies between the generated and original videos. Was the model trained in RGB or YUV color space?
3. Figure 5 shows that while fine details such as hair strands are preserved, specific elements like earrings disappear. Why does Promptus struggle to preserve certain details?

### Soundness
3

### Presentation
3

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
The paper proposed an interesting new paradigm for representing videos by inversing them into prompts, replacing traditional video encoding/decoding. In video communication, the sender transmits prompts, while the receiver uses these prompts to control Stable Diffusion to generate (reconstruct) the original video. It is impressive that the generated video can achieve pixel alignment with the original video, and the gradient descent fitting approach is quite pleasing. The methods of controlling bitrate through low-rank decomposition and achieving inter-frame compression via prompt interpolation are sound. The results, particularly in comparison to H.265, demonstrate the potential of Promptus in video communication.

### Strengths
1. Clear setting. Reducing video bitrate is a practical and important problem, as video traffic can be quite expensive for content providers. This paper offers a revolutionary new perspective by representing videos with prompts and employing generative models for video reconstruction. 

2. Well motivation. The main ideas and tricks can be easily understood. Many concerns at first glance are addressed in the following sections. The paper systematically discusses the challenges of prompt streaming, such as bitrate control, inter-frame compression, and real-time playback, and presents a comprehensive solution.

3. Simple yet effective, making it easy to follow. In the gradient descent framework, there appear to be many potential improvements for further work.

### Weaknesses
1. Considering that random packet loss occurs in network transmission, how would this influence the performance of Promptus? Would incomplete prompts severely degrade the quality of the generated video? Please clarify.

2. To reduce bitrate, semantic communication is an emerging paradigm. Although some related work is introduced in the related work section, the authors do not explicitly compare Promptus with semantic communication. Is Promptus an instance of semantic communication or a potential alternative? Please clarify.

3. This paper should thoroughly clarify the fundamental differences between prompt inversion and video encoding/decoding. While P5 L269 touches on this point, the authors do not provide further explanation.

4. What is the scalability of Promptus? Although it can generate videos in real-time from prompts, the overhead of the inversion from video to prompts cannot be ignored, as acknowledged in the limitation section. How would this cost increase on a video platform with billions of users?

### Questions
Please address the weaknesses above.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces Promptus, a new video streaming system that reduces bandwidth by transmitting video frames as Stable Diffusion prompts rather than raw video data. Utilizing gradient descent for pixel alignment and low-rank decomposition for bitrate control, Promptus achieves over 4x bandwidth reduction compared to traditional methods, maintaining high perceptual quality at low bitrates.

### Strengths
1. Novel in the sense of reforming the paradigm of traditional video streaming system by transmitting prompt streaming instead of video streaming.
2. Ensure pixel alignment in this kind of paradigm based on generative model is inspiring.
3. The workflow of the proposed method is well presented. The effectiveness of components is well discussed.
4. The authors openly discuss limitations of using prompts for video streaming system.

### Weaknesses
1. The authors discuss recent SOTA works on neural-based video compression in the “Introduction” and “Related Works” sections. However, Figures 8, 9, and 10 do not include a comparison of the results with representative methods from these works. Additionally, what is the significance of the comparison with VAE?
2. Although the authors address this in the paper, I do think that PSNR and SSIM should still be considered alongside LPIPS.
3. I think the paper should include more comparisons of subjective results at different bitrates to highlight its advantages on pixel alignment.
4. Since the paper introduces Stable Diffusion as part of the method, and the authors have also noted this increase in complexity, can the increase in model parameters be discussed? Furthermore, can more details on the training process be provided?

### Questions
The questions are mentioned in the “Weaknesses” section.

What’s more, the citation format needs further adjustments according to the conference requirements. e.g., VP8 (Bankoski et al., 2011) instead of  “VP8 Bankoski et al. (2011)”.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 6

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper propose Promptus, a novel system that replaces video streaming with prompt streaming by representing video frames as Stable Diffusion prompts. To achieve this goal, this paper conducted experiments in three aspects: ensuring pixel alignment, achieving adaptive bitrate, and inter-frame compression. Experiments shown that Promptus can achieve more than 4x bandwidth reduction while perserving the same perceptual quality compared to H.265.

### Strengths
1.	Promptus provides a new communication paradigm, using only prompts to stream a video.
2.	The paper is easy to understand well and clearly written.
3.	The effect at low bitrates is significantly improved. Compared with VAE and H.265, Promptus's perceptual quality is improved by 0.139 and 0.118 (in LPIPS), respectively, and the proportion of severely distorted frames is reduced by 89.3% and 91.7%, respectively.

### Weaknesses
1.	The experiments and evaluation are not sufficient enough.

a) Only the decoding time is listed in the appendix, but not the encoding time. 

b) For measuring the generated video sequences, it is recommended to open source these videos, or show examples frame by frame to prove the stability of the generation.

c) Since Promptus is aimed at low-bitrate video compression, it is recommended to release more subjective comparison results to prove the advantages of the Promptus. 

d) The paper only mentions the interpolation of prompt. It's suggested to be compared with applying the interpolation in the pixel domain among video frames in terms of generation performance and complexity to prove the effectiveness of interpolation of prompt.

e) There is also a lack of comparison with other specific state-of-the-art video compression methods. It is recommended to compare with more video compression methods (e.g. [1][2]).

2.	This proposed diffusion-based video compression method shows several limitations. For example, the relatively large delay and complexity, because the prompt needs to be inserted into the intermediate frame, so the subsequent frames must be received before playback. The second is the usage scenario, which is currently limited to low-bitrate video streaming scenarios.

### Questions
1.	The comparison with more advanced codec like H266 is also suggested.
2.	Since SD is not very good at generating features like human fingers and text, could you show how Promptus performs in places with a lot of high-frequency information such as fingers and text?

### Soundness
3

### Presentation
3

### Contribution
3
