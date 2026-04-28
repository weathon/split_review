# Ground-A-Video: Zero-shot Grounded Video Editing using Text-to-image Diffusion Models

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 8, 6, 6

## Abstract
Recent endeavors in video editing have showcased promising results in single-attribute editing or style transfer tasks, either by training 
text-to-video (T2V) models on text-video data or adopting training-free methods.
However, when confronted with the complexities of multi-attribute editing scenarios, they exhibit shortcomings such as omitting or overlooking intended attribute changes, modifying the wrong elements of the input video, and failing to preserve regions of the input video that should remain intact.
To address this, here we present a novel grounding-guided video-to-video translation framework called Ground-A-Video for multi-attribute video editing.
Ground-A-Video attains temporally consistent multi-attribute editing of input videos in a training-free manner without aforementioned shortcomings.
Central to our method is the introduction of Cross-Frame Gated Attention which incorporates groundings information into the latent representations in a temporally consistent fashion, along with Modulated Cross-Attention and optical flow guided inverted latents smoothing.
Extensive experiments and applications demonstrate that Ground-A-Video's zero-shot capacity outperforms other baseline methods in terms of edit-accuracy and frame consistency.
Further results and code are available at \textit{\href{http://ground-a-video.io}{http://ground-a-video.io}.}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper focuses on an interesting problem, namely multi-attribute editing in the video domain. The proposed method relies on recent techniques, such as GLIP, and ControlNet, and integrates the grounding information to perform a sequence of editing operations. The aim is also to propose a training-free pipeline by using pre-trained models in a zero-shot setting. For video-level editing, a stable diffusion backbone is extended for video data with DDIM inversion, and optical flow and depth maps are integrated as conditional to improve video editing quality. The evaluation is conducted on a set of videos and the evaluation is performed qualitatively with a comparison to SOTA and quantitatively by a user study with 28 participants.

### Strengths
The topic of paper, multi attribute editing in videos, is a challenging and interesting problem. 

The paper seems mostly the integration and extension on available recent T2I pipelines for video domain. But, the selected models are recent and they fit well within the proposed pipeline. Moreover, the pipeline avoids additional training stages that is good for zero-shot pipeline.

### Weaknesses
The paper is a well-designed integration of mostly existing techniques for video editing pipeline. The authors explain the steps in subsections with details. However, I found the overall text flow confusing as the stable-diffusion model and the layers of it are explained in multiple  sections, e.g. 3.2 and 3.4, rather than a whole. Additionally, the integrations of the controlNet and optical flow into the whole pipeline are not clear. I think a revised figure with math representations consistent with the text may help to explain the model better. 

A more detailed qualitative evaluation of the model could be presented in the experimental section. For instance, to assess the impact of a particular component on the pipeline, the ablation section (Section 4.3) only includes the edited video outputs generated using with and without this component. However, this evaluation could also be conducted quantitatively (as in Table 1) to see the impact of some evaluated components on the pipeline.

### Questions
What is the video set used for comparison and evaluation in Table 1? 

How similar are the paper's evaluation metrics with CAV (Chen et.al 2023)?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents the ﬁrst grounding-driven video editing framework, which is intended to solve the problem of neglected editing, wrong element editing and temporal-inconsistency in context of the complexities of multi-attribute video editing scenarios. Moreover, the proposed method is training-free which overcomes the obstacle of excessive computational cost on video tasks. Spatial-Temporal Attention, Cross-Frame Gated Attention and Modulated Cross Attention are introduced to further enhance consistency, depth map is used as an additional condition to better preserve structure and 3D information and the binary mask calculated through the optical ﬂow map can help maintain the consistency of the background area. Eﬀectiveness has been proven by suﬃcient experiments and convincing qualitative results.

### Strengths
S1. This paper presents the ﬁrst training-free grounding-driven video editing framework, which is relatively innovative.

S2. The proposed method and experimental results are consistent with their motivation and eﬀectively solve the problem of multi-attribute video editing in complex scenes.

S3. The method is clearly stated, and the details are comprehensive.

### Weaknesses
W1. Since the introduced depth map and optical ﬂow map both reﬂect pixel-level structural information, will this cause the structure before and after editing to be too consistent, so that if the foreground is replaced by an object with inconsistent structure, the editing result will be poor and lack of ﬂexibility? e.g. replace the “rabbit” in the phrase "A rabbit is eating a watermelon on the table" with an animal without long ears.

W2. For similar reasons, this may also limit the editing method to the task of adding or deleting objects.

### Questions
See weaknesses above.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Ground-A-Video proposes a training-free framework for grounded multi-attribute editing. The grounding ability is achieved by introducing the pretrained GLIGEN gated self-attention module into existing video editing pipelines. The paper also proposes several techniques including "cross-frame attention" and "flow-guided latent smoothing" to improve temporal consistency.

### Strengths
1. Grounded video editing is a novel task. Bounding box grounding allows users to accurately select the regions to edit. It is a useful feature that allows better location controllability and content disentanglement over the existing popular sentence-level video editing works.

2. The overall framework is training-free. The proposed framework is built upon several pretrained models like Stable Diffusion, Control Net, GLIGEN, and training-free inversion techniques like Null-text Inversion, so the framework itself requires no additional training on video data.

3. The framework effectively associates editing prompts with the grounded areas. The results in the paper show better text alignment compared to previous sentence-level video editing approaches like Tune-A-Video, and ControlVideo.

### Weaknesses
1. Although under the same framework, the technical contributions are quite disconnected from one another and some of them might not be closely related to the grounded video editing task. Two main technical contributions (Modulated Cross-Attention and Flow-guided Latent Smoothing) in the paper lie in finding temporally smooth and faithful latent noise during inversion, which serves as a preparatory step and seems to be less relevant to the grounded editing task. On the other hand, the grounded editing capability mainly comes from the pretrained GLIGEN gated self-attention module, which brings limited addition to the previous image grounding task.

2.  Although the proposed framework is training-free, it is still noteworthy that the per-frame null-text inversion requires gradient-based optimization on the null-text embeddings and could be time-consuming for longer videos. Moreover, the new Modulated Cross-Attention mechanism requires jointly optimizing all frames, which requires large memory.

3. I am not very clear about the flow-guided smoothing after reading the description: does it only work on static areas? If not, why there are not any warping operations mentioned? I also find the terms "spatially continuous" and "spatially discrete" a bit confusing and hard to understand what continuous and discrete refers to.

### Questions
Please kindly address the questions in the weakness section.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
this paper aims to address the challenge of multi-attribute editing in video editing. By incorporating the outputs of grounding models like GLIP and employing a designed attention mechanism, the proposed approach enables precise and temporally consistent video attribute editing. The authors conducted comparative experiments with recent methods, demonstrating superior performance.

### Strengths
1. This paper addresses a highly significant problem of achieving consistent fine-grained attribute editing in videos. The introduction of grounding conditions proves to be a direct and effective approach.
2. In addition to the design of grounding conditions, the authors propose mechanisms such as noise smoothing and cross-attention.

### Weaknesses
This paper lacks substantial technical innovation as its main contribution lies in expanding the experiments on the input conditions, whether it is the depth or grounding results. The approach used for injecting conditions is based on ControlNet or cross-attention, which is a common practice in stable diffusion and related applications of ControlNet. The paper does not sufficiently explore the limitations of these existing methods when applied to video, nor does it provide a detailed analysis of why the proposed modifications are necessary beyond a basic implementation of these techniques. The core method appears to be an assembly of existing techniques rather than a novel contribution to the field.

This paper also lacks a thorough investigation into the parameter sensitivity of the proposed method. Specifically, the thresholds used in the smoothing process are not sufficiently justified, and the paper does not present a comprehensive analysis of how these thresholds impact the quality and consistency of the generated videos. The absence of objective metrics for different threshold values makes it difficult to assess the robustness and reliability of the proposed approach. The visual comparison of the flow smooth effect is also limited, with only a single example provided, which is insufficient to demonstrate the general effectiveness of the method.

### Questions
1. The authors provided a visual comparison of the flow smooth effect in Figure 6, but it only includes a single example. Are there additional examples and comparisons with baseline and other methods (excluding flow smooth) demonstrating their effects under the same prompt?
2. during the smoothing process, thresholds are introduced. Are there objective metric comparisons for different thresholds and experiments to evaluate the robustness of the thresholds?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
