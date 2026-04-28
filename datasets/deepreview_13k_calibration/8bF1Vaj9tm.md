# ViSAGe: Video-to-Spatial Audio Generation

- Decision: Accept
- Avg Score: 6.40
- Scores: 8, 6, 6, 6, 6

## Abstract
Spatial audio is essential for enhancing the immersiveness of audio-visual experiences, yet its production typically demands complex recording systems and specialized expertise. In this work, we address a novel problem of generating first-order ambisonics, a widely used spatial audio format, directly from silent videos. To support this task, we introduce YT-Ambigen, a dataset comprising 102K 5-second YouTube video clips paired with corresponding first-order ambisonics. We also propose new evaluation metrics to assess the spatial aspect of generated audio based on audio energy maps and saliency metrics. Furthermore, we present Video-to-Spatial Audio Generation (ViSAGe), an end-to-end framework that generates first-order ambisonics from silent video frames by leveraging CLIP visual features, autoregressive neural audio codec modeling with both directional and visual guidance. Experimental results demonstrate that ViSAGe produces plausible and coherent first-order ambisonics, outperforming two-stage approaches consisting of video-to-audio generation and audio spatialization. Qualitative examples further illustrate that ViSAGe generates temporally aligned high-quality spatial audio that adapts to viewpoint changes. We will make public our codes and dataset.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper titled "ViSAGe: Video-to-Spatial Audio Generation" introduces a novel framework for generating first-order ambisonics, a spatial audio format, directly from silent video clips. The authors address the challenge of enhancing the immersiveness of audio-visual experiences without the need for complex recording systems or specialized expertise. They present YT-Ambigen, a dataset of 102K YouTube video clips paired with first-order ambisonics, and propose new evaluation metrics based on audio energy maps and saliency metrics. The core of their work is the Video-to-Spatial Audio Generation (ViSAGe) framework, which leverages CLIP visual features and autoregressive neural audio codec modeling to generate spatial audio that is both semantically rich and spatially coherent. The framework outperforms two-stage approaches and demonstrates the ability to adapt to dynamic visual contexts, showing potential for applications in immersive media production.

### Strengths
1. The paper introduces a groundbreaking approach to directly generate spatial audio from video, addressing a previously unsolved problem and offering a significant advancement in the field of immersive media.
2. The ViSAGe framework is an end-to-end solution that integrates neural audio codecs with visual features, which is a novel combination in the context of audio generation from video.
3. The paper is well-structured, with a clear problem statement, including the introduction of a new dataset and evaluation metrics, which are crucial for the field.
4. The creation of YT-Ambigen dataset and new evaluation metrics shows a comprehensive approach to both generating and validating the spatial audio.

### Weaknesses
As shown in Figure 2, the framework designed in this paper uses many different modules. Therefore, the computational complexity (model parameters) and running time (inference time) of the overall framework need to be discussed. Furthermore, the paper does not provide a detailed breakdown of the computational cost associated with each module, making it difficult to pinpoint the bottlenecks in the pipeline. This lack of granularity makes it challenging to assess the practical applicability of the proposed method, especially when considering real-time applications or deployment on resource-constrained devices. A more thorough analysis of the computational demands, including memory usage and processing time for each component, is needed to fully evaluate the framework's efficiency.

### Questions
The audio energy map shown in Figure 3 seems to be highly correlated with the location of the sound source, which can be related to the sound source localization task. In other words, can the relevant design ideas under the sound source localization task provide some guidance here? More specifically, can the cross modal contrastive learning strategy [1] commonly used in sound source localization tasks be applied here to impose some additional constraints?

[1] Chen H, Xie W, Afouras T, et al. Localizing visual sounds the hard way[C]//Proceedings of the IEEE/CVF conference on computer vision and pattern recognition. 2021: 16867-16876.

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
3

### Summary
This paper presents a novel task: generating spatial audio from silent video. Specifically, given a silent video and the camera direction, the proposed model, ViSAGe, leverages CLIP features, patchwise energy maps, and neural audio codes, incorporating a code generation scheme to simultaneously produce multiple spatial channels of audio in the first-order ambisonic format. For this task, the authors introduce a new dataset, YT-Ambigen, which consists of YouTube videos paired with first-order ambisonics. Compared to two-stage models, which first generate mono-channel audio and then perform audio spatialization, the proposed ViSAGe outperforms in overall quantitative metrics.

### Strengths
- The paper is clearly written and well-presented.
- The proposed task of generating spatial audio from silent video is interesting and takes one step further of existing works that tackle this task separately.
- The dataset curation pipeline effectively addresses the limitations of existing datasets, and the dataset would make contribution to the community.

### Weaknesses
 - Lack of moving object samples or objects that are not centered.
    - When listening to the synthesized audio while watching the video, most content appears centered, which makes the synthesis task relatively simple and appears to be similar to the mono audio generation task.
    - To fully demonstrate the effectiveness of the proposed method and task, more qualitative examples are needed that show results in challenging scenarios (e.g., objects moving from left to right, objects not centered, or visual events requiring time-synced audio synthesis).
- This lack raises questions about dataset quality.
    - Since the dataset seems to be collected automatically, is the test set clean or challenging enough to serve as a reliable benchmark? Wouldn’t human annotation or verification be necessary to validate its quality?
    - Furthermore, what distribution does this dataset cover? What types of events or objects appear in it? If the task involves not only audio spatialization but also requires semantic information, then details on the dataset (e.g., statistics, categories) should be provided.
- Clearer visualization and explanation in qualitative results would enhance the work.
    - The generated spectrograms in Fig. 3(a) appear different from the ground truth. If the authors do not highlight the specific areas readers should focus on, important details may be overlooked.
    - Similarly, in Fig. 3(b), overlapping the heatmap with the original video would improve clarity. While the predicted heatmap seems better than the baseline model, it still does not fully align with the real visual events.

### Questions
- Two numbers are highlighted in bold in Table 3: Ablation on Model Components.
- Please check that all figure and table references are correctly cited, e.g., L476 references Figure D.
- Could the authors clearly describe how the 9 codes per timestep in each audio channel are generated? The figures seem to illustrate the process for generating a single code, while the neural codec contains 9 RVQ codes per timestep.

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
- The paper introduces a new problem of generating spatial audio for silent videos.
- The problem is formalized as:  Given silent video and direction of camera -> generate First Order Ambisonics (FOA)
- Due to lack of suitable datasets, the authors collect YT-AmbiGen from Youtube for this task
- They use discrete audio representations for encoding FOA and autoregressive model for generation
- New baselines and evaluation metrics are proposed to compare and evaluate their approach
- A comprehensive comparison with baselines, along with ablation study, show the effectiveness of their proposed approach

### Strengths
- The problem is new, interesting, and important for the research community
- The authors introduce a new dataset for this new task, setting a benchmark for future spatial audio generation research.
- Suitable baselines and metrics are proposed to compare on this new task
- Carefully designed components are incorporated, for eg. FOA encoding, sequence of its generation, rotation augmentation, patchwise energy maps

### Weaknesses
Major:

Missing Subjective tests:
- The paper lacks subjective evaluations; studies assessing quality, and directionality ( or localization accuracy) should be included. Authors should compare their approach with baselines on metrics like mean opinion score (or other subjective metrics).
 
Demo examples
- While the demo examples appear semantically good, the sounds are often too diffuse, making it challenging to precisely localize the direction of the audio.
- Including some static sources with smaller, more focused sound-generation areas can help in better experiencing and analyzing the sound source direction (subjectively). 

Minor:
- Missing relevant references:

Some recent work on spatial audio generation should be referenced. These methods also generate spatial audio (FOA) given some conditions (eg. direction of arrival, and sound source category).

[1] Heydari et. al, "Immersediffusion: A generative spatial audio latent diffusion model"

[2] Kushwaha et. al, "Diff-SAGe: End-to-End Spatial Audio Generation Using Diffusion Models"

### Questions
- Could the authors include subjective test results evaluating metrics such as audio quality and relevance to the specified direction? 

- Would it be possible to create a subset of clean, single-source static sounds as a benchmark and demo set? This would enable evaluation using metrics like Direction of Arrival (DoA) and provide clearer, more focused demo examples.

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
ViSAGe is a framework designed to generate spatial audio, specifically first-order ambisonics, directly from silent videos, enabling immersive audio experiences without complex equipment. Utilizing the YT-Ambigen dataset of over 102,000 video clips with ambisonic audio, ViSAGe integrates CLIP visual features and a neural audio codec for synchronized, viewpoint-adaptive sound. It outperforms traditional two-stage methods by producing temporally aligned, spatially coherent audio, evaluated through innovative metrics based on audio energy and saliency.

### Strengths
1. The paper is well-written
2. The approach of generating spatial audio from FoV holds considerable value for practical applications. Open-sourcing the proposed dataset would provide a valuable resource to the community.
3. The design methodology is reasonable and effective.

### Weaknesses
1. There appears to be no explanation of the camera orientation parameter, which leaves me unclear on how it enhances spatial perception.
2. The method assumes that the CLIP visual representation lacks spatial information. Could replacing it with a visual representation that has stronger local perception, such as DINOv2, improve the quality of spatial audio generation?

### Questions
See weaknesses

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
4

### Summary
The paper introduces ViSAGe, a novel framework for generating first-order ambisonics (a spatial audio format) directly from silent videos. This is significant for enhancing the immersiveness of audio-visual experiences without the need for complex recording systems or specialized expertise.

### Strengths
The paper presents a novel approach to generating spatial audio directly from silent videos, aiming to enhance immersion without complex recording setups. A key contribution is the creation of the YT-Ambigen dataset, which includes 102K video clips paired with spatial audio, providing valuable resources for training and evaluation. The authors propose innovative evaluation metrics that utilize audio energy maps and visual saliency to assess the spatial quality of the generated audio, offering a deeper understanding of audio-visual coherence. Their end-to-end framework, ViSAGe, integrates CLIP visual features with neural audio codecs, avoiding issues associated with traditional two-stage approaches. Lastly, this research has significant implications for media production in film, virtual reality, and augmented reality, potentially revolutionizing audio generation for visual content.

### Weaknesses
The current approach may not fully capture the dynamic changes in audio that correspond to rapidly changing visual scenes. Specifically, the method might struggle with accurately representing the temporal evolution of sound events when visual elements exhibit fast motion or abrupt transitions. The generation of spatial audio is based on neural networks, which may not always adhere to the physical principles governing sound propagation and perception. This could lead to inconsistencies in the generated audio, such as unnatural spatialization or inaccurate reflections, especially in complex acoustic environments.

### Questions
Could the authors elaborate on the diversity of the YT-Ambigen dataset in terms of different acoustic environments and video content types? How does this diversity compare to real-world scenarios?

### Soundness
3

### Presentation
3

### Contribution
3
