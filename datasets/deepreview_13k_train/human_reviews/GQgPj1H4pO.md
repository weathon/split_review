# Weakly Supervised Video Scene Graph Generation via Natural Language Supervision

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Existing Video Scene Graph Generation (VidSGG) studies are trained in a fully supervised manner, which requires all frames in a video to be annotated, thereby incurring high annotation cost compared to Image Scene Graph Generation (ImgSGG). Although the annotation cost of VidSGG can be alleviated by adopting a weakly supervised approach commonly used for ImgSGG (WS-ImgSGG) that uses image captions, there are two key reasons that hinder such a naive adoption: 1) Temporality within video captions, i.e., unlike image captions, video captions include temporal markers (e.g., before, while, then, after) that indicate time-related details, and 2) Variability in action duration, i.e., unlike human actions in image captions, human actions in video captions unfold over varying duration. To address these issues, we propose a weakly supervised VidSGG with Natural Language Supervision (VSNLS) framework that only utilizes the readily available video captions for training a VidSGG model. VSNLS consists of two key modules: Temporality-aware Caption Segmentation (TCS) module and Action Duration Variability-aware caption-frame alignment (ADV) module. Specifically, TCS segments the video captions into multiple sentences in a temporal order based on a Large Language Model (LLM), and ADV aligns each segmented sentence with appropriate frames considering the variability in action duration. Our approach leads to a significant enhancement in performance compared to simply applying the WS-ImgSGG pipeline to VidSGG on the Action Genome dataset. As a further benefit of utilizing the video captions as weak supervision, we show that the VidSGG model trained by VSNLS is able to predict a broader range of action classes that are not included in the training data, which makes our framework practical in reality.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents VSNLS, a weakly supervised approach for VidSGG that uses only video captions for supervision. The paper addresses two key challenges: temporality within captions and variability in action duration. The solution comprises three main components: Temporality-aware Caption Segmentation (TCS), Action Duration Variability-aware Caption-Frame Alignment (ADV), and a novel Pseudo-Labeling strategy based on Motion cues (PLM).

### Strengths
- Enabling VidSGG training using only video captions.
- Reduction in annotation costs compared to existing approaches.
- Well-identified key challenges in adapting image-based weak supervision to videos.
- Modular architecture with TCS and ADV components. 
- PLM module handling negative action classes.
- Effective use of LLMs for temporal understanding.

### Weaknesses
 - Limited discussion of LLM choice impact in TCS module.
- No detailed analysis of failure cases.
- An effective temporal consistency metric could be added.
- Analysis of performance on longer videos is missing.

### Questions
- Can you provide LLM selection criteria and impact on TCS performance?
- Can you clarify the robustness of K-means clustering for action duration estimation?
- Can you include an analysis of performance vs. video length?
- Can you provide an ablation experiment of TCS and PLM without ADV?
- Can you make use of a temporal consistency metric to make the analysis fair and comprehensive?
- What is the justification for the threshold value in the PLM? Have you done any experiments?

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
5

### Summary
This paper introduces a framework, VSNLS, for Video Scene Graph Generation (VidSGG) that leverages natural language supervision from video captions to reduce the high cost of manual annotation. Unlike existing methods, VSNLS uses two modules tailored for video data: a Temporality-aware Caption Segmentation (TCS) module to capture time markers in captions, and an Action Duration Variability-aware Caption-Frame Alignment (ADV) module to align captions with frames based on action duration. This approach enables the model to learn from weak supervision, allowing it to predict dynamic relationships and even generalize to unseen actions. The proposed method is shown to be effective on the Action Genome dataset, demonstrating improved performance over traditional image-based weak supervision techniques.

### Strengths
VSNLS addresses the high annotation cost of fully supervised Video Scene Graph Generation (VidSGG) by using weak supervision from video captions. This method eliminates the need for extensive manual annotation of all frames, which is both time-consuming and costly.

### Weaknesses
-Dependency on Co-occurrence Priors: VSNLS, like many video-based scene graph models, often relies on co-occurrence priors to estimate relationships. This dependency can reduce the generalizability of the model to unseen object combinations, potentially limiting its performance on diverse or novel datasets where the objects and relations deviate from the training distribution.

-Handling Long-term Relations: Clip-based methods in VSNLS might struggle with capturing relations that unfold over extended sequences, which require a larger receptive field. If clip length is limited (e.g., fixed at 30 frames), the model may miss detecting relations that span longer temporal windows, thereby impacting its ability to accurately model long-term dependencies.

-Occlusion and Tracking Limitations: Although clip-based approaches are often advocated for mitigating long-term tracking issues like occlusion, the use of short-term tubelets might still face challenges in fragmented tracking. Occlusions or visual artifacts can still lead to lost tracklets or misalignments, reducing the reliability of relationship detection over long video durations.

-High Computational Cost for Short Clips: Analyzing shorter clip sequences may require repeated processing of overlapping frames to maintain temporal context, leading to higher computational and memory demands. This could make the model less efficient and limit scalability for very long video sequences where full contextual understanding is crucial.

-Important References Missing:
[1] Video visual relation detection via iterative inference. ACM MM 2021.
[2] Winner: Weakly-supervised hierarchical decomposition and alignment for spatio-temporal video grounding. CVPR 2023.
[3] In Defense of Clip-based Video Relation Detection. TIP 2024.

### Questions
The results are reported on the Action Genome dataset, but it is unclear how well the framework would perform on other VidSGG datasets with different types of actions or domain-specific captions. How about VidOR dataset?

How does VSNLS handle noisy or ambiguous captions? Since the method depends on the quality of video captions, it would be helpful to understand how robust the framework is to variations in caption detail and accuracy.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper conducts video scene graph generation in a weakly supervised manner. Several key steps are employed to generate scene graph labels from video-text annotations. The authors first design text prompts for multimodal large language models to parse the video captions into sentences along a time horizon. Then, a clustering-based caption-frame alignment framework is designed to align video frames with the segmented sentences. With images and their aligned texts, the authors use existing scene graph parsing methods and scene grounding methods to generate scene graphs. The authors also conduct experiments on the video scene graph generation benchmark , the Action Genome (AG) dataset, to validate the effectiveness the proposed method.

### Strengths
1. This paper proposes a weakly supervised pipeline for video scene graph generation, an important research topic in multimodal learning. Researchers can build a larger scene graph generation dataset with this pipeline from annotated video-text pairs. Researchers can also leverage the MLLMs to generate scene graphs without any human labels in further days.
2. The design of the temporality-aware caption segmentation module is interesting; it can convert the video's text caption into multiple sentence segments. MLLM may find it challenging to finish such tasks. It would be helpful to add more details about the segment process. 
3. Aligning the segmented sentences with the video frames is critical for generating a scene graph. The authors provide many details about conducting the clustering-based alignment.

### Weaknesses
Although the proposed VSNLS pipeline can achieve good results on VidSGG tasks, its innovation still needs to be enhanced and emphasized. The VSNLS pipeline has four critical steps: the temporality-aware caption segmentation part, the action duration variability-aware caption-frame alignment part, the generation of pseudo-localized scene graphs part, and the adverse action classes generation part. Except for the action duration variability-aware caption-frame alignment part, I am unclear about the novelty and technical insights in other sections. 
1. In section 2.2, the authors design prompts to segment the video captions into sentences. Since there are a lot of prompt engineering works, what are the new insights in this part that can motivate the following researchers to conduct their work? Are there some key points that need to be noticed in design prompts? Specifically, how does the prompt ensure temporal consistency in the segmentation, and what are the limitations of this approach when dealing with complex sentence structures or coreferences that span multiple sentences?
2. In section 2.4, the scene graph parsing and grounding utilize state-of-the-art methods to generate graph nodes. I guess readers are more willing to see how the authors develop some techniques to make these state-of-the-art methods conduct parsing or grounding more accurately. For instance, how are the inherent challenges of video, such as motion blur, fast movement, and occlusion, addressed when grounding the scene graphs? What specific modifications or enhancements are made to the existing methods to handle these video-specific issues?
3. The experimental setting is organized in a bit of chaos. How the training, validation, and testing sets are split is not introduced. From line 316 to line 325. the reader can hardly understand whether the model is trained on the AG dataset or the combination of the AG caption and the MSVD caption dataset. It is crucial to clarify the exact data split and usage for each stage of the pipeline. The lack of clarity makes it difficult to reproduce the results and understand the true performance of the proposed method.
4. There is no ablation study on the effectiveness of the microdesign in the ADV part. How different clustering strategies influence the final results is important to understand the rationale behind the VSNLS framework. Specifically, how does the choice of clustering algorithm (e.g., K-means, agglomerative, GMM) affect the quality of the caption-frame alignment and the final scene graph generation performance? A detailed analysis of these choices is needed to justify the design.

### Questions
I have no further questions. Please see the weakness part.

### Soundness
4

### Presentation
4

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
This manuscript tackles the problem of extracting scene graphs from video inputs by only using raw video captions during the training stage. The proposed method focuses on extracting pseudo training data from the raw captions to be consumable by supervised VidSGG models. The proposed method consists of TCS (temporally sorting the atomic events in the complex captions), ADV (handling the variable length of atomic actions), and k-means clustering with some smoothings to assign clusters of frames to each of the atomic actions.

### Strengths
VidSGG is an important problem, and IMO has been overlooked. I believe this line of research is very important, and I believe that authors selected a good approach by utilizing only captions to train a vidsgg.

Also, the temporal inconsistency and variability of action lengths are two main difficulties for any video-language tasks. I believe that this paper systematically decomposed them and addressed them each separately.

### Weaknesses
The main weakness of this manuscript is that it does not contribute to any core learning methods. For example, no visual understanding or natural language understanding method has been improved. It is mostly a wise tooling over LLMs and some basic approaches like clustering. Even the final training has been delegated to off-the-shelf vidsgg methods.

### Questions
1- In Table 1, what about combining the full supervision and weak supervision data to see if the weak supervision can give a boost to supervised results? The combination could be combining the training data or doing pretraining on weak supervision and then fine-tuning on fully supervised data. IMO, we can always have some supervised data, and the value of this work will shine if we see that it can boost the results on top of that.

2- Lines 240-244: I think this part needs more clarification. A) Does this filtering contribute to the final results? B) In the given example, will I^1 be assigned to S1, or will it not be assigned to either S1 or S2? C) Videos can be formed of different shots that can jump between two actions back and forth. How those cases will be handled? 

3- Do the clustering steps have any other purpose than computation efficiency? Why not compare each singleton frame and the Segmented Sentences?

4- I would like to see the examples that have been passed to the LLM. A) How are they selected? B) How does the quality of output change by changing those examples? I see a reproducibility risk here.

### Soundness
3

### Presentation
3

### Contribution
2
