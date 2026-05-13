# Knowing Your Target : Target-Aware Transformer Makes Better Spatio-Temporal Video Grounding

- Decision: Accept
- Scores: 8, 8, 6, 8

## Abstract
Transformer has attracted increasing interest in spatio-temporal video grounding, or STVG, owing to its end-to-end pipeline and promising result. Existing Transformer-based STVG approaches often leverage a set of object queries, which are initialized simply using zeros and then gradually learn target position information via iterative interactions with multimodal features, for spatial and temporal localization. Despite simplicity, these zero object queries, due to lacking target-specific cues, are hard to learn discriminative target information from interactions with multimodal features in the complicated scenarios (e.g., with distractors or occlusion), resulting in degradation. Addressing this, we introduce a novel Target-Aware Transformer for STVG (TA-STVG), which seeks to adaptively generate object queries via exploring target-specific cues from the given video-text pair, for improving STVG. The key lies in two simple yet effective modules, comprising text-guided temporal sampling (TTS) and attribute-aware spatial activation (ASA), working in a cascade. The former focuses on selecting target-relevant temporal cues from a video utilizing holistic text information, while the latter aims at further exploiting the fine-grained visual attribute information of the object from previous target-aware temporal cues, which is applied for object query initialization. Compared to existing methods leveraging zero-initialized queries, object queries in our TA-STVG, directly generated from a given video-text pair, naturally carry target-specific cues, making them adaptive and better interact with multimodal features for learning more discriminative information to improve STVG. In our experiments on three benchmarks, including HCSTVG-v1/-v2 and VidSTG, TA-STVG achieves state-of-the-art performance and largely outperforms the baseline, validating its efficacy. Code will be released.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
In this work, a new method called Target-Aware Transformer for STVG (TA-STVG) is proposed for addressing the Spatio-Temporal Video Grounding (STVG) task. To replace the traditional zero-initialized object queries used in previous methods, TA-STVG is designed to generate target-specific object queries from the given video-text pair, with two main modules named Text-guided Temporal Sampling (TTS) and Attribute-aware Spatial Activation (ASA). Experiments and analysis are conducted to validate the effectiveness of the proposed TA-STVG.

### Strengths
1.The intuitive motivation of TA-STVG is clear and easy to understand, i.e., the adaptively generated object queries containing target-relevant information facilitate the spatio-temporal localization of textual expressions.

2.The proposed method to enhance and keep track of the information about the described subject in the sentence is concise and effective.

3.State-of-the-art performances are achieved by the method across all three datasets.

4.Qualitative results and analysis are adequately given to illustrate the effectiveness of the proposed components.

### Weaknesses
1. It would be better to include more discussions and comparisons on some recent works in the related domain of video grounding. For example, the proposed ASA module adopts similar techniques of spatial activation learning [1] and concept classification [2]. Specifically, the ASA module's approach to learning spatial activation maps bears a resemblance to methods that utilize intra-frame visual cues to highlight target regions. Furthermore, the classification of visual concepts within the ASA module shares similarities with techniques used in weakly-supervised video paragraph grounding, where feature alignment and regression are jointly learned. A more thorough discussion of these connections would provide a clearer understanding of the novelty and contribution of the proposed method.

2. In the proposed TA-STVG, object queries are generated from globally pooling the multimodal features and are repeatedly used for each frame in the video. This way of object query construction seems suboptimal since the frame-specific information is ignored for the queries. The global pooling operation, while providing a consistent target representation, may discard crucial temporal nuances present in individual frames. The lack of frame-specific object queries could limit the model's ability to adapt to dynamic changes in the video content. For instance, if the target object undergoes significant appearance changes or occlusions across frames, the static object query might not effectively capture these variations. Is there any consideration or motivation for such design choice? Why not construct the frame-specific object queries?

3. How are the weights for different loss terms determined? Are there any ablation results? Specifically, the manuscript does not provide sufficient detail on how the loss weights for the Text-guided Temporal Sampling (TTS) loss and the Attribute-aware Spatial Activation (ASA) loss are selected. Without ablation studies or a clear rationale, it is difficult to assess the robustness and sensitivity of the model to these hyperparameters. The absence of this information makes it challenging to replicate the results and understand the impact of each loss term on the overall performance.

4. Some typos exist in the current manuscript, for example, "such" should have been "such as " in Line 29.

### Questions
Please refer to the weaknesses.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces an approach to spatio-temporal video grounding (STVG) using a Target-Aware Transformer (TA-STVG). The method aims to improve the localization of targets within videos based on textual descriptions by generating object queries that are adaptively initialized with target-specific cues extracted from video-text pairs. The key contributions include two main modules: Text-Guided Temporal Sampling (TTS) for selecting target-relevant frames, and Attribute-Aware Spatial Activation (ASA) for exploiting fine-grained visual attribute information. The proposed method achieves state-of-the-art performance on three benchmarks: HCSTVG-v1/-v2 and VidSTG, and demonstrates generality by improving the performance of existing Transformer-based methods like TubeDETR and STCAT.

### Strengths
1. The paper presents a novel approach to STVG by introducing target-aware object queries, which is a significant departure from traditional zero-initialized queries.

2. TA-STVG outperforms existing methods on multiple benchmarks, indicating the effectiveness of the proposed approach.

3. The writing of the paper is good and it is easy to understand.

### Weaknesses
1.The method may require significant computational resources, which may limit its accessibility and practical application, especially for smaller research groups or companies.

2. The paper could provide more discussion on the computational complexity and parameter count compared to other methods, which is crucial for understanding its scalability.

3. The paper could benefit from a discussion on the robustness of the model against various challenges such as occlusion, similar appearances, or noisy text descriptions.

### Questions
1. How does the computational complexity of TA-STVG compare to other state-of-the-art methods in terms of parameters and FLOPS?


2. How does the model handle videos with multiple targets that are described in a single text query?

3. Can the TTS and ASA modules be adapted to work with other types of multimodal data, such as audio descriptions or 3D video data?

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
4

### Summary
The paper introduces a Target-Aware Transformer to address the limitations of traditional zero-initialized queries in STVG. The proposed method leverages target-specific information to generate more adaptive object queries that better interact with multimodal features, leading to improved accuracy. Extensive experiments on multiple benchmarks demonstrate that TA-STVG achieves SOTA performance.

### Strengths
1. Target-specific cues improve object queries over zero-init methods, enhancing feature learning for better localization.

2. Extensive ablation studies support the effectiveness of the TTS and ASA modules, and the generality of modules is further validated by the integration into other models (e.g. TubeDETR, STCAT).

### Weaknesses
1. The method’s contribution is focused primarily on object query initialization for STVG, with the innovation mainly revolving around attention-based filtering for keyframes and target-specific attribute extraction, which makes the innovation limited.

2. The multi-label classification in the ASA module is unclear. Specifically, are the extracted subject features for appearance and motion identical? What is the relationship between weak attribute labels and subject features, and do the weak labels update dynamically?

3. The performance in complex scenarios requires further validation. Since object query initialization relies on the provided video-text pair, how robust is the query generation when visual information is heavily occluded, or the query is vague and lacks clear attributes? The robustness of the model against unclear attribute information should be further explored.

### Questions
See weakness

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
This paper addresses the challenge of spatio-temporal video grounding (STVG) in complex scenarios by introducing the Target-Aware Transformer for STVG (TA-STVG). TA-STVG adaptively generates object queries based on target-specific cues from the video-text pair, utilizing two key modules: text-guided temporal sampling (TTS) and attribute-aware spatial activation (ASA). TTS selects relevant temporal cues using text information, while ASA refines these cues to capture detailed visual attributes for initializing object queries. Experiments on benchmarks, including HCSTVG-v1/-v2 and VidSTG, demonstrate that TA-STVG achieves state-of-the-art performance.

### Strengths
- Unlike previous methods that use zero-initialized object queries, this paper presents the Target-Aware Transformer, which improves STVG by exploring target-specific cues for generating object queries.
- This paper proposes text-guided temporal sampling to select target-relevant temporal cues from videos and introduces attribute-aware spatial activation to leverage fine-grained visual semantic attributes for object query generation.
- Experiments on three datasets demonstrate its effectiveness.

### Weaknesses
 - Given the textual feature, first extract the subject's feature (usually the target to localize) from the textual sentence. My question is, do you typically obtain just one subject representation or multiple? If multiple are obtained, are they all processed through the same flow for decoding, or is there a further selection step?
- Sampled target-relevant temporal appearance and motion features—do they need to have the same quantity? If so, how is this controlled?
- The sampled target-relevant temporal appearance and motion features determine the frame information for the target object. This step can significantly impact subsequent accuracy. What happens if the selected frames do not contain the target object?

### Questions
- Given the textual feature, first extract the subject's feature (usually the target to localize) from the textual sentence. My question is, do you typically obtain just one subject representation or multiple? If multiple are obtained, are they all processed through the same flow for decoding, or is there a further selection step?
- Sampled target-relevant temporal appearance and motion features—do they need to have the same quantity? If so, how is this controlled?
- The sampled target-relevant temporal appearance and motion features determine the frame information for the target object. This step can significantly impact subsequent accuracy. What happens if the selected frames do not contain the target object?

### Soundness
3

### Presentation
3

### Contribution
3
