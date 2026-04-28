# Glad: A Streaming Scene Generator for Autonomous Driving

- Decision: Accept
- Avg Score: 5.60
- Scores: 6, 8, 3, 5, 6

## Abstract
The generation and simulation of diverse real-world scenes have significant application value in the field of autonomous driving, especially for the corner cases. Recently, researchers have explored employing neural radiance fields or diffusion models to generate novel views or synthetic data under driving scenes. However, these approaches suffer from unseen scenes or restricted video length, thus lacking sufficient adaptability for data generation and simulation. To address these issues, we propose a simple yet effective framework, named Glad, to generate video data in a frame-by-frame style. To ensure the temporal consistency of synthetic video, we introduce a latent variable propagation module, which views the hidden features of previous frame as noise prior and injects it into the latent features of current frame. In addition, we design a streaming data sampler to orderly sample the original image in a video clip at continuous iterations. 
Given the reference frame, our Glad can be viewed as a streaming simulator by generating the videos for specific scenes. 
Extensive experiments are performed on the widely-used nuScenes dataset. Experimental results demonstrate that our proposed  Glad achieves promising performance, serving as a strong baseline for online generation. We will release the source code and models publicly.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
Collecting large-scale real-world driving data is expensive and labor-intensive. Diffusion generative models have achieved remarkable success in creating diverse and  high-quality video  from textual prompts. Therefore, this paper proposes to use diffusion model as a data generator which produce video data frame by frame in an online manner. To maintain temporal consistency, the authors propose latent variable propagation. The Glad can be used as generator and simulator, according to input. Experimental results show Glad is able to to generate videos of arbitrary lengths and exhibiting good flexibility in the variations of simulated trajectory.

### Strengths
1. The motivation for using diffusion models for data generation in autonomous driving is clearly a promising direction, reducing the labor-intensity. 

2. The paper is well-written and easy to follow. Fig.2 provides a clear illustration of the video data generation pipeline, which makes me easy to understand the method proposed in this paper. 

3. The framework is designed similar to the recurrent network, using the previous frame to predict the current frame. This is make sense for achieving arbitrary length video generation.

### Weaknesses
1. From the method and evaluation sections of the paper, it's not very clear whether this method is able to address the error accumulation when the frame is generated one by one. In the method section, it will be useful to clarify this and explain how this method is able to do so. Specifically, the paper should discuss the impact of error propagation during the iterative generation process. It's unclear how the latent variable propagation handles potential compounding errors over longer sequences. A more detailed analysis of the error characteristics and their mitigation would be beneficial.

2. It is unclear to me how many training data used for Glad and other methods in Table 1, such as Panacea and Oracle. The paper should explicitly state the size and composition of the training dataset used for each method, including the number of video sequences and frames. This is crucial for assessing the fairness of the comparison and the generalizability of the results.

3. It would be interesting if the authors could show the detailed detection performance of 10 classes on the nuScenes. Providing a breakdown of detection performance per class would give a more granular view of the model's strengths and weaknesses. This would help in understanding if the model is biased towards certain object categories or if it struggles with specific types of objects.

### Questions
1. Can the authors clarify with why Glad cannot achieve further improvement by using more video frames in Table 2? I would appreciate if this was clarified.

2. How about the performance of Glad just use the generated data for training.

3. Effective generation of corner cases is essential for providing key data support the model, as mentioned in abstract. I'm wonder if Glab is able to generate such data.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The authors propose a latent propagation method for generating long and consistent driving video in a frame by frame manner.
The latent pronation module simply use the denoised latent of frame t as the noise latent for denoting the latent of frame t+1.
A special streaming data sampler is designed to enable the training of this model.
Extensive experiments on nuscenes showcases the generation quality and effectiveness of using generated data to improve the downstream perception tasks.

### Strengths
1. The authors propose a simple yet effective framework for video generation in driving scenario, the idea of latent propagation is interesting.
2. Although missing some comparison, the experiments and ablation studies are generally solid.

### Weaknesses
1. Confusing writing and missing key reference. I think the whole idea of Glad is to denoise frame t+1 from the fully denoised latent of frame t instead of gaussian noise as suggested in Figure 2, but the whole section 4 tells very little about this fact except the eq 3. Also, the idea is not utterly new as this is know as image noise prior in TRIP[1], which also show great FID/FVD performance compared with other video generation models.
2. Serious issue in paper organization. The section 3 is pretty much redundant as the latent diffusion is introduced in almost 3 years ago and is now well known to the whole AI community and general technique enthusiasts. Also there are tens of works applying stable diffusion or stable video diffusion for video forecasting or world modeling in autonomous driving.
3. Poor literature review. Why not compare with DriveWM[2] and MagicDrive[3] which also do controlled multi-view multi-frame generation and report results on detection and mapping. Also if the authors want to highlight the streaming generation in driving scene(as indicated in the paper title), Vista[4] is a very important method to compare.
4. The paper does not adequately address the impact of multi-scale training on the reported results. The method uses multi-scale training for both generation and downstream tasks, which is not a standard practice in earlier works like DriveWM and Vista. This discrepancy makes it difficult to assess the true contribution of the proposed streaming generation approach, as the performance gains could be partially attributed to this training strategy.

### Questions
1. Intuitively, using the denoised previous frame latent as noise latent seems poses heavy restriction on drastic content change during generation. Could the authors provide more insight about how Glad balance between  frame-to-frame consistency and the quick motion of generated video.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes “Glad”, to generate visual data from scenarios of autonomous driving in a frame-by-frame manner, where most of the previous works generate the entire sequence at a certain amount of time. It is done by injecting the previous frame noise into later frames. In addition, it designs a continuous sampling the original images into a sequence. Experiments are conducted on nuScenes dataset for video generation, and boosting 3D detection.

### Strengths
This paper is overall easy to read. 

Use a previous frame noise to initiate the following frame noise seems to be a good way to maintain the consistency

The streaming data sampler seems to be a good engineering approach to cache the previous timeframe’s noise and inject into the second iteration instead of recomputing.

### Weaknesses
I have several concerns regarding this paper’s motivation, technical novelty, experiments and presentations.

## Motivation concerns

In my humble opinion, this paper has makes a seemingly interesting claim for generating scenes in a frame-by-frame manner but unclear reason why we should do this.

For example, the authors claim in the abstract that “these approaches suffers from unseen scenes or restricted video length”. However, as I understand correctly, the recent diffusion based method can all support such sampling strategy to realize infinite sequence generation. For example, Drive-WM (CVPR2024) and Panacea (CVPR2024) also use the generated frame as the subsequent condition for long video generation. As for unseen scenes, as a layout-dependent generation framework, people in general can pass any unseen layout to generate such unseen scenes. A most recent one [A], although this one is still an Arxiv paper, shows the capability of generating such unseen scenes to boost end-to-end algorithms. Though this cannot be used to directly penalize this work is wrong, it shows that previous approaches can indeed generate unseen scenes, which contradicts to the paper’s core motivation.

[A] Ma et al. Unleashing Generalization of End-to-End Autonomous Driving with Controllable Long Video Generation, arxiv

The second motivation is depicted in Figure 1 (b-c). This paper claims that previous papers focused on offline generate scenes. If I understand correctly, this means previous method takes a pre-defined trajectory, while this paper can take a dynamic trajectory. However, is this merely an engineering approach? After all, I can also passed a more flexible trajectory to the previous generation method.

In addition, even though this motivation is true when you try to encode this “Glad” method into some rendering engine to build a close loop simulator, I did not see any of such validation in the latter experiment section. So I am not convinced this is a valid motivation.

All in all, this paper’s motivations need some further clarification.


## Technical novelty concerns

Is this using a single frame as condition to generate next frame already done in DriveWM and Panacea, by setting the sequence length to 1 frame and keep generating? Please clearly discuss what are the differences between their’s approach and this one.

Streaming data sampler is an engineering effort without much technical novelty. It is just a simple caching mechanism during the python programming.

## Empirical validation concerns

As aforementioned, the motivation of injecting dynamic scenes is not well justified during the experiment sections. The only downstream applications other than video quality is 3D object detection. Please at least use end-to-end autonomous driving or 3D object tracking tasks to showcase if the motivation is validated.

In addition, there is no validation on long sequence video quality.

Also, does the word “online” meaning that on-the-fly rendering? Can you show the complexity and time benchmarking?

## Presentation concerns

This paper made simple mistakes in presentation. For example, it should use ‘citep’ when mentioning a method in a third perspective rather than use ‘cite’ like CVPR template.

### Questions
as above weaknesses

### Soundness
2

### Presentation
2

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
This paper generates multi-view video data in a frame-by-frame style for autonomous driving.

To be honest, I reviewed this paper at NIPS, and seeing it again, I am pleased that the authors have taken into account previous reviewers' feedback, such as modifying the wording and adding discussions about previous methods. However, since there were no changes made to the methodology, considering the limited novelty and suboptimal results, I will maintain a negative score.

### Strengths
1. This paper proposed Glad, which generates multi-view video data in a frame-by-frame style and can generate videos of arbitrary lengths theoretically.

2. The paper proposes two training tricks, i.e., Latent Variable Propagation and Streaming Data Sampler, to achieve frame-by-frame generation.

3. The tables and figures are well-presented.

### Weaknesses
1. Latent Variable Propagation and Streaming Data Sampler appear to be simple training tricks. Many previous U-Net-based works with temporal modules (before Sora and SVD), such as ADriver-I, MagicDrive, and Drive-WM, also employ frame-by-frame video generation strategy. Many works in the video generation area also use cross-frame attention of each frame on the first/former frame to preserve the context, appearance, and identity consistency of the video: Text2Video-Zero: Text-to-Image Diffusion Models are Zero-Shot Video Generators; ControlVideo: Training-free Controllable Text-to-Video Generation; Video ControlNet: Towards Temporally Consistent Synthetic-to-Real Video Translation Using Conditional Image Diffusion Models.

2. The experimental results should provide a comparison between the proposed approach and previous methods, e.g., DriveDreamer-2, considering that DriveDreamer-2 has achieved significantly better results with an FVD of 55.7 compared to the author's Glad approach with 206. The Latent Variable Propagation (LVP) module, which generates noise based on the latent distribution of frame T-1, is conceptually similar to noise prior techniques explored in "Preserve Your Own Correlation: A Noise Prior for Video Diffusion Models" and "VideoFusion: Decomposed Diffusion Models for High-Quality Video Generation". The paper does not provide a theoretical justification for this substitution, making it unclear if it is more than a practical engineering choice. Furthermore, the Streaming Data Sampler, while presented as novel, is a common practice in frame-by-frame video generation methods. Papers like Panacea, Drive-Dreamer, and Drive-WM, which are all based on UNet for generating videos frame by frame, also utilize a form of streaming, which is essentially sequential sampling within clips. The authors need to clarify the specific differences in their approach compared to these methods.

3. The visual results provided by the authors demonstrate poor temporal consistency, with noticeable color fluctuations and object inconsistencies across frames. This raises concerns about the practical applicability of the method, even if the FVD metric is not the sole measure of performance.

### Questions
See Weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces Glad, a novel framework designed to generate and simulate video data in an online setting, addressing the limitations of existing methods in handling unseen scenarios and short video lengths. Glad ensures temporal consistency in the generated videos by incorporating a hidden variable propagation module, which uses the denoised hidden variable features from the previous frame as a noise prior for the current frame. The framework includes a stream data sampler that sequentially and iteratively samples frames from video clips, enabling efficient training and enhancing the model's ability to generate specific scene videos.

### Strengths
1. Glad stands out by enabling online video generation, over traditional offline methods that are limited to fixed-length video generation.
2. By treating the denoised hidden variable features from the previous frame as a noise prior for the current frame, Glad maintains a high level of temporal coherence, which is essential for realistic and seamless video generation.
3. The Stream Data Sampler (SDS) is designed to improve training efficiency by sequentially sampling frames from video clips across multiple iterations. This method not only ensures consistency between training and inference but also optimizes the training process by caching the generated hidden features for use as noise priors in subsequent iterations.
4. Glad integrates both data generation and simulation capabilities within a unified framework, offering a comprehensive solution for autonomous driving applications. Whether generating new scene videos from noise or specific scene videos given a reference frame, Glad demonstrates versatility and effectiveness.

### Weaknesses
1. The paper claims significant advancements in online generation of controllable videos for driving simulation, yet the supporting evidence is lacking. The experiments presented in Fig. 5&6 do not convincingly demonstrate the quality of video generation under novel trajectories from a scientific perspective. It is recommended that the authors provide additional qualitative analysis of Glad's performance under different novel trajectories (e.g.,  sharp turns, lane changes, or varying traffic densities) starting from the same initial frame to substantiate their claims. The current demonstrations lack a systematic evaluation across a diverse set of challenging scenarios, making it difficult to assess the robustness of the proposed approach.

2. The paper does not clearly articulate the fundamental benefits of using past frames as priors for current frame generation compared to methods that incorporate temporal transformer layers, such as Panacea and DrivingDiffusion. An ablation study to validate the effectiveness of this approach is warranted, especially given that Tab. 1 shows Panacea achieving better video consistency (FVD) without the use of an initial frame. The authors can compare their approach with temporal transformer layers with Panacea/DrivingDiffusion, focusing on FID, FVD and computational efficiency. The comparison should explicitly analyze the trade-offs between the proposed latent variable propagation and the temporal transformer's ability to capture long-range dependencies.

3. The authors do not explore or discuss the potential performance gains that could be achieved by training models on data generated with new trajectories. This is a significant oversight that limits the understanding of Glad's full potential. The authors may generate an additional batch of data using novel trajectories rather than original trajectories, use it as a training data for Tab. 3, and then see if this dataset produces a gain in the model. This exploration is crucial to demonstrate the model's ability to generalize beyond the training data and its potential for creating more diverse and realistic driving scenarios.

4. The training data used in the stage one is not detailed in the paper. At L285, the authors fail to specify whether the data comes from public datasets, web sources, self-collected data, or a combination thereof. This lack of transparency raises concerns about privacy issues, the necessity of data annotation, and the distribution of the data. The authors can provide a detailed breakdown of data sources, including preprocessing steps, annotation methods, and measures taken to address privacy concerns. The absence of this information makes it difficult to reproduce the results and assess the generalizability of the approach.

### Questions
My concern revolves around what I perceive as an overclaim by the authors regarding the simulation capabilities of driving video generation. How effectively the authors address this critical point will significantly influence my score on their work.

### Soundness
3

### Presentation
3

### Contribution
2
