# RadEyeVideo: Enhancing general-domain Large Vision Language Model for chest X-ray analysis with video representations of eye gaze

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 6, 5

## Abstract
Large Vision-Language Models (LVLMs) have demonstrated promising performance in chest X-ray (CXR) analysis. To enhance human-computer interaction, several studies have incorporated radiologists' eye gaze, typically through heatmaps or textual prompts. However, these methods often overlook the sequential order of eye movements, which could provide valuable insights by highlighting both the areas of interest and the order in which they are examined. In this work, we propose a novel approach called RadEyeVideo that integrates radiologists’ eye-fixation data as a video sequence, capturing both the temporal and spatial dynamics of their gaze. The video, featuring a red gaze point overlaid on CXR images, emphasizes regions of focused attention during interpretation. We evaluate this method in CXR report generation and disease diagnosis using three general-domain, open-source LVLMs with a video input capabilities. When prompted with eye-gaze videos, model performance improves by up to 25.4% on Impression generation task and on average 7.9% for all tasks using scaled evaluation metrics. Our approach enhanced open-domain LVLM models, when combined with exemplar reports for in-context learning, outperform medical models as well as those specifically trained for CXR report generation on the benchmark dataset. This work highlights that domain expert's knowledge (eye-gaze information in this case), when effectively integrated with LVLMs, can significantly enhance general-domain models' capabilities in clinical tasks, pointing out a new effective approach of utilising LVLMs in healthcare and beyond.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
To enhance the reliability of large vision-language models (LVLMs) in real clinical environments, this study proposes a novel video prompting method called RadEyeVideo, which integrates radiologists' eye-tracking data as video sequences, capturing the spatial and temporal dynamics of gaze. Red fixation points are superimposed on CXR images to highlight the areas that doctors pay attention to, so as to dynamically present the doctor's eye movement path. Improve the ability of radiologists or AI models to diagnose chest diseases by providing rich contextual information.

### Strengths
1. The proposed method, RadEyeVideo, combines video, text, and eye movement data to realize the fusion of multi-modal information and improve the accuracy and efficiency of diagnosis.
2. The authors conducted a thorough assessment of various eye-tracking integration techniques, providing strong empirical support for their claims.

### Weaknesses
1. In Figure 2, the authors illustrate different prompting methods; however, the figure does not clearly distinguish between the use of text descriptions and video inputs. This ambiguity makes it challenging to understand whether the authors used text descriptions to guide the prompt along with the video input or if they only provided video data. Specifically, the figure lacks a clear separation between textual prompts and visual prompts, making it unclear if the textual descriptions are used in conjunction with the video input or as a standalone alternative. The absence of a visual cue or label to differentiate these input modalities leads to interpretational difficulties.
2. The author's experiments conducted on only one dataset are clearly insufficient in terms of persuasiveness. This limitation may affect the generalizability and applicability of the research findings. To enhance the credibility of the study, it is recommended that the authors validate their approach on different datasets. The lack of diversity in the dataset limits the assessment of the method's robustness across different imaging protocols, patient demographics, and disease manifestations. This single-dataset validation raises concerns about the potential for overfitting to the specific characteristics of the chosen dataset, which could lead to inflated performance metrics that do not translate to real-world clinical scenarios.
3. When the authors use radiologist's eye-tracking sequences as video input, this approach does enhance the model's understanding of prior knowledge in the diagnostic reading process to a certain extent. However, converting eye-tracking data into video format substantially increases the number of tokens, leading to significant computational resource consumption and longer inference times for the model. The conversion of eye-tracking data into a video format, while capturing spatiotemporal dynamics, introduces a large number of frames, each of which is processed as a separate token. This increase in token count directly translates to higher computational demands, specifically in terms of GPU memory and processing time, which could limit the practical applicability of the method in resource-constrained environments.

### Questions
1. The RadEyeVideo method integrates the eye movement data of the radiologist as a video sequence to capture the spatiotemporal dynamics of his gaze. However, the article does not explain in detail how this video sequence is specifically generated, for example, how the eye movement data is sampled and converted into video frames, and how these frames contain temporal and spatial information.
2. In Section 2.3 INPUT REPRESENTATION, to fit the input requirements of LVLM, the authors uniformly sampled the video sequence and selected 16 frames as inputs. However, the article does not explain why 16 frames were chosen and whether this choice had a significant impact on model performance. In addition, whether the impact of using more or fewer frames on model performance has been explored is also a question worth exploring. This helps to further understand the effect of video data length and quality on model performance.

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
5

### Summary
The paper introduces an innovative approach that incorporates radiologists' eye-tracking data as video sequences. This method captures both spatial and temporal patterns in gaze, which provides a more accurate representation of radiologists' attention during chest X-ray interpretation. The approach was evaluated using three general-domain LVLMs, showing significant improvements.

### Strengths
- RadEyeVideo's use of video-based eye-gaze data is a unique contribution that effectively captures the temporal and spatial dynamics of radiologists' focus. I like this idea.
- The study demonstrates substantial improvements, particularly in impression generation, highlighting RadEyeVideo's effectiveness in enhancing diagnostic tasks.
- The language is clearly presented. The authors use precise and concise language so that the reader can easily understand the methodology, and results of the study.

### Weaknesses
 - Although this idea is interesting, it still relies on temporal and spatial information in the inference phase, which is difficult to apply to real clinical scenarios. Do the authors consider involving multiple information inputs only in the training phase and simulating zero-shot scenarios as much as possible in the inference phase?
- The study’s findings are limited by the small size of the MIMIC-Eye dataset, which may not fully capture the variability in real-world clinical settings, raising questions about the generalizability of the results.
- The comparisons primarily focus on selected models with minimal tuning for this domain. Including a wider range of task-specific medical LVLMs could provide a more comprehensive evaluation.

### Questions
- Why the paper lacks an section of related work? e.g., some recent evaluation work of Med-LVLMs [1,2,3]
- The formats of reference is weird. e.g., in Line 311-321. Please check it.

[1] Gu Z, Yin C, Liu F, et al. MedVH: Towards Systematic Evaluation of Hallucination for Large Vision Language Models in the Medical Context[J]. arXiv preprint arXiv:2407.02730, 2024.

[2] Jiang Y, Chen J, Yang D, et al. MedThink: Inducing Medical Large-scale Visual Language Models to Hallucinate Less by Thinking More[J]. arXiv preprint arXiv:2406.11451, 2024.

[3] Xia P, Chen Z, Tian J, et al. CARES: A Comprehensive Benchmark of Trustworthiness in Medical Vision Language Models[J]. arXiv preprint arXiv:2406.06007, 2024.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces eye-tracking data into medical LVLMs and uses video formats to retain the temporal and spatial characteristics of radiologist’s eye movements, providing more comprehensive prior information for the diagnostic model. Compared to heatmaps and textual prompts, this method fully considers temporal features. Evaluation on multiple downstream tasks demonstrate the effectiveness of the approach.

### Strengths
1. This work introduces radiologists' eye-tracking data into LVLMs in video format, highlighting the temporal features of eye movement sequences.
2. The experiments in the paper are comprehensive, validating multiple diagnostic tasks across various datasets.

### Weaknesses
1. The paper mentions using simple stacking of gaze points for heatmap generation, but it does not specify the radius size of the gaze points. Different gaze point sizes can affect the model's interpretation.
2. In-context learning often heavily relies on the provided examples, which can significantly influence the generated results. The paper does not discuss what constitutes suitable examples.

### Questions
1. Are the eye-tracking data collected from a single radiologist? If there are multiple radiologists, how do you handle individual behavioral differences?
2. How is the duration mentioned in line 176 used to control the frame count? This aspect is not explained in the paper. Similarly, the sampling method mentioned in line 194 is not clearly described.
3. Does the sampling of eye-tracking data risk losing short-term diagnostic behaviors, potentially affecting the diagnosis of various types of diseases?

### Soundness
3

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
This article introduces a novel prompting method called RadEyeVideo, which presents radiologists’ eye-tracking data as a video sequence to capture the temporal and spatial order of their gaze (i.e., scan paths). The authors evaluated the effectiveness of this approach in chest X-ray report generation and disease diagnosis tasks using large vision-language models (LVLMs) with video input capabilities. Results show that incorporating eye-gaze video prompts improved model performance by 25.4% on the Impression generation task, with an average performance increase of 7.9% across all tasks.

### Strengths
1. The RadEyeVideo method converts radiologists’ eye-tracking data into video sequences for use in chest X-ray report generation and diagnostic tasks, significantly enhancing the performance of general large vision-language models (LVLMs). Experimental results indicate a 25.4% improvement in the Impression generation task and an average improvement of 7.9% across all tasks, outperforming models specifically designed for medical applications.
2. Comprehensive Evaluation of Eye-Tracking Prompting Methods: This study presents the first thorough evaluation of various eye-tracking integration techniques, including static heatmaps, eye-tracking text prompts, and dynamic video prompts. The results indicate that RadEyeVideo outperforms the other methods in terms of diagnostic accuracy and clinical relevance, establishing a new standard for eye-tracking data prompts.

### Weaknesses
- Methodological Clarity: a) The paper lacks sufficient detail about the video prompt integration process, particularly how the video information is encoded and processed by the LVLMs. The technical implementation of combining video sequences with textual prompts could be more thoroughly explained. Specifically, the paper does not clarify the exact mechanism by which the sampled video frames are converted into a format that is compatible with the LVLM's input requirements. For instance, are the video frames processed through a separate video encoder before being concatenated with the textual embeddings, or is there a more direct integration method? b) There's limited discussion of potential alternatives to full video sequence processing that might achieve similar results with lower computational costs. The paper mentions sampling 16 frames, but it does not explore other temporal sampling strategies such as non-uniform sampling or the use of optical flow to capture motion information, which could potentially reduce the number of frames required while preserving critical temporal dynamics. 

- Data Collection and Generalizability Limitations: a) The methodology requires synchronized eye-tracking data collection during radiologist readings, which is resource-intensive and difficult to scale. The paper does not address the practical challenges of implementing such a system in a real-world clinical setting, where the availability of eye-tracking equipment may be limited, and the process of data collection may disrupt the normal workflow of radiologists. b) The approach may not generalize well to scenarios where real-time eye-tracking data is unavailable or impractical to collect. The paper does not discuss how the model would perform in the absence of eye-tracking data, or whether there are any fallback mechanisms to maintain a reasonable level of performance. c) The current evaluation is limited to a relatively small dataset (2,298 CXR images), raising questions about broader applicability. The paper does not provide a clear justification for the choice of this dataset, or whether it is representative of the broader range of clinical scenarios. The lack of diversity in the dataset may limit the generalizability of the findings to other populations or clinical settings.

- Computational Efficiency Concerns: The direct use of complete eye-tracking video sequences as prompts likely increases computational overhead significantly. While the authors mention sampling k frames (typically 16) from the total sequence, there's limited analysis of the computational trade-offs or optimal sampling strategies. The paper does not provide a detailed analysis of the computational cost associated with processing video prompts, such as the increase in memory usage and processing time compared to image-only or text-only prompts. The method may be computationally prohibitive for real-time clinical applications, particularly in resource-constrained environments.

### Questions
Please address the concern raised in weakness part.
Moreover, there are some questions may help you to address the weakness.
1) What is the computational overhead of processing video prompts compared to traditional image-only or text-only prompts?
2) Have you explored more efficient alternatives to using complete video sequences, such as key frame selection or compressed representations? 3) How do you envision this approach being implemented in real-world clinical settings where real-time eye-tracking data may not be available? 4) Have you considered alternative methods for generating synthetic eye-tracking data that could make the approach more broadly applicable? 5)

### Soundness
2

### Presentation
3

### Contribution
2
