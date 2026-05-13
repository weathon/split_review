# FreeNoise: Tuning-Free Longer Video Diffusion via Noise Rescheduling

- Decision: Accept
- Scores: 6, 6, 5, 6

## Abstract
With the availability of large-scale video datasets and the advances of diffusion models, text-driven video generation has achieved substantial progress. However, existing video generation models are typically trained on a limited number of frames, resulting in the inability to generate high-fidelity long videos during inference. Furthermore, these models only support single-text conditions, whereas real-life scenarios often require multi-text conditions as the video content changes over time. To tackle these challenges, this study explores the potential of extending the text-driven capability to generate longer videos conditioned on multiple texts. \textbf{1)} We first analyze the impact of initial noise in video diffusion models. Then building upon the observation of noise, we propose \textbf{FreeNoise}, a tuning-free and time-efficient paradigm to enhance the generative capabilities of pretrained video diffusion models while preserving content consistency. Specifically, instead of initializing noises for all frames, we reschedule a sequence of noises for long-range correlation and perform temporal attention over them by window-based fusion. \textbf{2)} Additionally, we design a novel motion injection method to support the generation of videos conditioned on multiple text prompts. Extensive experiments validate the superiority of our paradigm in extending the generative capabilities of video diffusion models. It is noteworthy that compared with the previous best-performing method which brought about $255\%$ extra time cost, our method incurs only negligible time cost of approximately $17\%$. 
Generated video samples are available at our website: \href{http://haonanqiu.html}{http://haonanqiu.html}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper investigates the effect of initial noise on a diffusion model for video generation, and thus proposes a method to extend the ability of a pre-trained model to generate long videos without fine-tuning, by rescheduling the initial noise of the video frame and by using a window-based temporal attention to achieve long-range visual consistency. finally, a new method of injecting motion trajectories is proposed, which allows the model to generate videos in response to multiple text prompt.

### Strengths
1) The proposed method is simple and effective to expand the model's ability to generate long videos without fine-tuning the model.

2) The use of noise reschedule and window-based attention fusion allows for more consistent video generation.

3) Motion inject allows the model to be fed with a variety of text prompts to generate longer videos with richer meanings.

### Weaknesses
1) The method described in this paper lacks suitable diagrams to help illustrate it.

2) The proposed NOISE RESCHEDULING may limite the content variances of video generation since longer videos are produced by repeating the noises for the short ones. As is shown by the examples, the generated long videos looks like a short video that loops multiple times. I wonder whether this way can produce authentic long videos that contain continous various motions.

### Questions
Try adding more diagrams to better explain the methods in the article, such as noise rescheduling and an overview of the pipeline for generating a video using the methods mentioned in the article.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a method to unlock the long video generation ability of a pretrained text-to-video generation model. The major technical components of this method include: 1. The analysis of artifacts and causes when generating long videos. 2. A noise schedule for long video generation. 3. Windowed attention fusion to keep attention perception field while avoiding content jump between windows, 4. Motion injection for varied textual prompts. The experiments show FreeNoise is a competitive long video generator.

### Strengths
This is a technically solid paper. Long video generation is a tricky long-standing problem. The authors propose a series of insights and techniques that have sufficient novelty to address the difficulties:
1.	The analysis of long video artifacts and causes is valuable for developing better video generators. 
2.	The noise scheduling and window-based attention fusion address the long video difficulties mentioned in the analysis. They are simple yet effective. Window-based attention fusion addresses the notorious content jump problem, which will likely help develop future video generation foundation models.
3.	FreeNoise does not require additional UNet forward propagation. Therefore, the inference cost overshoot is low. 
4.	The qualitative results are marvelous. In human preference evaluation, FreeNoise still achieves the best. The authors provide an anonymous website to show more visual results. The image definition and motion consistency of FreeNoise are both good.
5.	The motion injection technique successfully preserves video contents and drives the video to follow a new text prompt.
6.	The qualitative ablations show each technical component of FreeNoise is effective and important.

### Weaknesses
Major concerns: 
1.	I’m interested in detailed experiment settings. Please include diffusion sampler configurations, sample resolutions, frame stride, etc. in your future revision.
2.	Please add a pipeline figure. It is not very easy to fully understand how and where FreeNoise is working on generating long videos.
3.	Is direct inference, sliding, GenL, and FreeNoise sharing the same pretrained text-to-video model? If it is, then the evaluation is very convincing since they can all generate the same short video using the prompts but only FreeNoise can achieve good long video results.

Minor concerns:
1.	Page 7. In the second line. A full stop is missing before ‘Obviously’.
2.	In which case FreeNoise may fail? A discussion over the limitations is welcomed.
3.	100 evaluation prompts have limited diversity. If it is feasible, please add more evaluation prompts to make the comparison more convincing.

### Questions
1.	The authors claim FreeNoise achieves the maximum long video of 512 frames due to GPU memory limit. Is it possible to unlock even long video generation ability by using the CPU offload technique? 
2.	With the help of ControlNet, is it possible to generate more diverse motion with FreeNoise?

### Soundness
3 good

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper aims to extend the generative capabilities of pre-trained video diffusion models without incurring significant computational costs. It contains three different components, window-based temporal attention, noise rescheduling, motion injection.

### Strengths
1. The proposed method is cleverly represented and very easy to follow.
2. The proposed method is much more efficient than the baseline method Gen-L [1].
3. The observation and Analysis part is well-designed and inspiring, and I appreciate this section.



[1] Gen-L-Video: Multi-Text to Long Video Generation via Temporal Co-Denoising

### Weaknesses
1. Demo quality. From the demos, we can see that the motions of most generated results are restricted. For example in the ablation study, when the horse running, the background and the position of the horse do not change (even though the legs are moved), which is not a reasonable motion. Therefore, I would say that the proposed method corrupts the motions of the original diffusion models.

2. Many ideas of the paper are used in previous works already. (1) For noise rescheduling, Reuse and Diffuse [1] proposed to reuse previous noise in the later frames. (2) For window-based temporal attention, Align Your Latents [2] applies a similar idea for long video generation, which does not change the temp conv part, but uses sliding local attention to resue the trained temporal attention. I think there's no intrinsic difference. (3) The motion injection part: interpolating the context is already proposed in Gen-L [3].

3. The author says they picked only 100 prompts for quantitative experiments and then generated 2400 videos. This statement seems not explicit.


[1] Reuse and Diffuse: Iterative Denoising for Text-to-Video Generation
[2] Align your Latents: High-Resolution Video Synthesis with Latent Diffusion Models
[3] Gen-L-Video: Multi-Text to Long Video Generation via Temporal Co-Denoising

### Questions
See Weaknesses.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a training-free method for extending capabilities of short video diffusion models to generate temporally coherent, longer videos, as well as incorporate multi-text conditioning. The authors propose a novel noise schedule and fused window-based temporal attention to enable more in-distribution, coherent longer generations. In order to enable multi-text conditions, the authors introduce a motion injection method based on conditioning different text prompts at different stages of diffusion sampling.

### Strengths
- The paper is well written, and easy to understand
- The proposed noise schedule + temporal attention modification is interesting as a method to enforce better long-term consistency in video
- Incorporating the proposed method is fairly simple, as it does not require any extra training on a pretrained short text-video diffusion model
- Experiments are concrete, and show much quality generations compared baselines

### Weaknesses
- From looking at the generated videos, although the proposed method can more cleanly generate longer videos, it seems that the spatial structure of the video (e.g. location of a cat) is very similar throughout the entire video. I believe this may be due to the repetitive nature of shuffled noise reptitions which are generally highly correlated with the structure of the resulting video. So it seems that the method may have a hard time generating more dynamic changes in long videos, such as a cat walking across the screen or scene / camera changes. Could the authors comment on this, or if there are generated video examples with larger structural changes through the video?

### Questions
- How would the proposed window fusing (weighted by frame index distance) compared to a simpler scheme such as just merging the current and/or prior window (i.e. similar to a one or two hot version of the frame index weighting).
- Have the authors explored other noise augmentation other than shuffling? In general, shuffling does not seem to be the most intuitive method for perturbing gaussian noise, as it also constrains the epsilons (per frame) to the original samples.
- Section 3.1 mentions that "temporal attention is order independent". Does this imply that the VideoLDM does not have temporal positional embeddings? Or how would it be order independent if it did?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
