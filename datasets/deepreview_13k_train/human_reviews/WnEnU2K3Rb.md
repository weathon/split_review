# Beyond the Benchmark: Detecting Diverse Anomalies in Videos

- Decision: Reject
- Scores: 6, 3, 5, 3

## Abstract
Video Anomaly Detection (VAD) plays a crucial role in modern surveillance systems, aiming to  identify various anomalies in real-world situations. However, current benchmark datasets predominantly emphasize simple, single-frame anomalies such as novel object detection. This narrow focus restricts the advancement of VAD models. In this research, we advocate for an expansion of VAD investigations to encompass intricate anomalies that extend beyond conventional benchmark boundaries.
To facilitate this, we introduce two  datasets, \ADset\ and \VIOset, to challenge models with diverse action-based anomalies. These datasets are derived from the HMDB51 action recognition dataset.
We further present \methodLong\ (\methodShort), a novel method built upon the AI-VAD framework. 
AI-VAD utilizes single-frame features such as pose estimation and deep image encoding, and two-frame features such as object velocity. They then apply a density estimation algorithm to compute anomaly scores. To address complex multi-frame anomalies, we add a deep video encoding features capturing long-range temporal dependencies, and logistic regression  to enhance final score calculation.
Experimental results confirm our assumptions, highlighting existing models limitations with new anomaly types. \methodShort\ excels in both simple and complex anomaly detection scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The manuscript underscores the importance of Video Anomaly Detection (VAD) in surveillance systems. It criticizes the current focus on simple, single-frame anomalies in benchmark datasets and advocates for expanding the scope of VAD to intricate anomalies. The authors introduce two datasets, HMDB-AD and HMDB-Violence, to challenge models with diverse action-based anomalies, and present Multi-Frame Anomaly Detection (MFAD). MFAD builds upon the AI-VAD framework, incorporating single-frame and two-frame features and applying density estimation. To tackle complex multi-frame anomalies, deep video encoding, and logistic regression are added. Experimental results highlight limitations in existing models with new anomaly types, demonstrating MFAD's proficiency in both simple and complex anomaly detection scenarios.

### Strengths
Strengths of the MFAD approach:

++ Comprehensive Feature Extraction: MFAD extracts four diverse feature types, including object velocities, human pose estimations, deep image encodings, and deep video encodings, enabling a holistic analysis of video data.

++ Adaptive Density Score Calculation: Using Gaussian Mixture Models (GMM) for velocity features and k-nearest neighbors (kNN) for other high-dimensional features, it adapts the density score calculation to the nature of the features, enhancing anomaly detection accuracy.

++ Max Feature Aggregation: The addition of the 'max' feature, which aggregates maximum feature scores per frame, adds value to the approach, improving anomaly detection.

++ Gaussian Smoothing: The application of Gaussian smoothing to anomaly scores reduces noise and provides more stable and interpretable results.

Overall, MFAD's strengths lie in its feature diversity, multi-modal analysis, adaptive density scoring, effective feature fusion, supervised learning, and robust experimental design, making it a powerful method for detecting both simple and complex anomalies in video data.

### Weaknesses
-- Complexity: MFAD's multi-stage process and diverse feature extraction, including object velocities, human pose estimations, deep image encodings, and deep video encodings, leads to a high computational cost. This complexity makes it challenging to deploy in resource-constrained environments, particularly when considering the need for real-time processing. The extraction of four different feature types, each with its own processing requirements, adds to the computational burden. Furthermore, the use of Gaussian Mixture Models (GMM) for velocity features and k-nearest neighbors (kNN) for other high-dimensional features, while adaptive, also contributes to the overall complexity.

-- Model Specificity: The reliance on specific video foundation models, such as VideoMAE, may limit the adaptability of MFAD to different datasets or domains. The performance of the model is likely tied to the pre-training data and architecture of the chosen foundation model. This dependency could hinder the model's ability to generalize to datasets with different characteristics or when applied to new domains where the pre-trained model may not be as effective.

-- Not Real-Time: The computational intensity of MFAD, stemming from its multi-stage processing and diverse feature extraction, makes real-time application challenging. The requirement for separate training and testing data further complicates real-time deployment. The need to extract and process four different feature types, apply density estimation, and then perform supervised learning all contribute to the overall processing time, making it difficult to achieve the low latency required for real-time anomaly detection.

-- Gaussian Smoothing Limitation: Applying Gaussian smoothing to anomaly scores, while reducing noise, may also lead to the loss of important information, especially for anomalies that are short-lived or have sharp transitions. The smoothing process could blur the boundaries of anomalies, making it harder to precisely identify the start and end points of anomalous events. This could be particularly problematic for detecting anomalies that are characterized by rapid changes in video content.

### Questions
There are just a couple of questions that I need clarification on!! 

--> How does MFAD handle the challenge of real-time video anomaly detection given its computational complexity? As I can see the author has provided the note for reproducibility, some insights would be helpful to understand the scope. 
--> Can MFAD adapt to different video datasets and domains effectively, or is it limited by its reliance on specific video foundation models?

Currently, I'm leaning towards accepting this work, if the Authors can provide some insights into the weakness & questions section, that would be helpful to understand the significant contribution.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
Briefly summarize the paper and its contributions. This is not the place to critique the paper; the authors should generally agree with a well-written summary.
This paper proposes a method for video anomaly detection that goes beyond the limitations of current benchmark datasets. The authors introduce two new datasets, HMDB-AD and HMDB-Violence, which challenge models with diverse action-based anomalies. They also present a novel method called Multi-Frame Anomaly Detection (MFAD) that incorporates deep video encoding features to capture long-range temporal dependencies and logistic regression to enhance the final score calculation. The experimental results show that MFAD outperforms existing methods on both simple and complex anomaly detection scenarios.

### Strengths
(1) The paper addresses the limitation of current benchmark datasets for video anomaly detection and proposes two new datasets that allow for the detection of complex action-based anomalies. This expands the scope of what constitutes an anomaly and encourages further research on more comprehensive anomaly types.
(2) The proposed method, MFAD, simply incorporates deep video encoding features and logistic regression to effectively detect both simple and complex anomalies. The experimental results demonstrate the effectiveness of the method on benchmark datasets as well as the newly introduced datasets.
(3) The paper is well-structured and clear. Based on the two datasets proposed in the paper, the method used performs better than existing methods.

### Weaknesses
(1) The paper lacks a more detailed description of the datasets HMDB-AD and HMDB-Violence. It would be beneficial to provide more information on the distribution of normal and abnormal activities, and any specific challenges or characteristics of the datasets. For example, the number of videos per class, the average length of videos, and the variability in camera angles or lighting conditions are not specified. Furthermore, the criteria used to define 'normal' and 'abnormal' within the context of these datasets are not sufficiently elaborated, making it difficult to assess the datasets' suitability for the intended task.
(2) The method proposed in this paper is more like a simple patchwork combination that lacks sound and rigorous theoretical support. The paper does not provide a clear rationale for why the chosen features (pose, velocity, depth, and deep image encodings) are the most appropriate for anomaly detection, nor does it explain how these features are expected to interact. Moreover, the paper lacks a more detailed and visual explanation of the proposed method, specifically how the features are combined and how the logistic regression is applied to produce the final anomaly score. The lack of a clear theoretical framework makes it challenging to understand the method's underlying mechanisms and potential limitations.
(3) The article lacks experimental validation of the effectiveness of the various components of the method. For example, the effect of redundant background information in deep image encodings was not verified. There is no ablation study to demonstrate the contribution of each feature (pose, velocity, depth, and deep image encodings) to the overall performance. It is unclear whether all features are necessary or if some are more important than others. The absence of such analysis makes it difficult to assess the importance of each component and to identify potential areas for improvement.
(4) The article also lacks a comprehensive analysis of the method's limitations, which would have facilitated a discussion of any potential challenges or failures. For example, the sub-optimal performance of the method proposed on the STC and Avenue datasets and the reasons for this should be analysed. The paper should discuss the scenarios where the method is likely to fail, such as when anomalies are subtle or when the background is highly dynamic. A more thorough discussion of these limitations would provide a more balanced view of the method's capabilities.

### Questions
1. How did you distinguish between normal and abnormal activity in multiple scenarios when constructing the two new datasets? What criteria were used?
2. How did you extract the human pose estimation, object velocity and depth image coding, can you provide more details on these?
3. How did you synthesise both few-frame and multi-frame features?
4. What are the limitations or failure cases of the MFAD method?
5. How did you verify the impact of each extracted feature on the results?
6. What are the limitations or failure cases of the MFAD method? Why the proposed method is sub-optimal for experiments on the STC and Avenue datasets?

### Soundness
1 poor

### Presentation
1 poor

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
This paper proposes a multi-frame-based video anomaly detection method, that builds on top of [1]. In [1] mostly frame-level attributes are included, while the proposed method extends the method of [1] by including multi-frames encoding features extracted across 16 frames. 

Furthermore, the paper cherry picks two groups of anomalies from HMDB51 to show the importance of anomalies across the temporal axis. 

The paper reports interesting results not only on the above two subsets of HMDB51, but also on few benchmark anomaly detection datasets. The results on the benchmark datasets are competitive compared to the chosen state-of-the-art methods, but outperforming them on the two subsets of HMDB51. 

[1] Tal Reiss and Yedid Hoshen. Attribute-based Representations for Accurate and Interpretable
Video Anomaly Detection, December 2022. URL http://arxiv.org/abs/2212.00789.
arXiv:2212.00789 [cs].

### Strengths
-Good overview of existing methods and datasets used in anomaly detection. 
-"Introducing" new videos to video anomaly detection for benchmarking.
-Comprehensive and competitive results on the public benchmarks and significantly higher results compared to state-of-the-art on the two subsets of HMDB51.
-Proper ablation study. which also shows the effect of video encoding features in Table 4.

### Weaknesses
Despite the interesting results, the paper's method sounds like a simple extension of [1] by introducing temporal features to [1].
Though the paper has cherry picked videos from HMDB51 and suggests using them for anomaly detection, they need claim this as their data (Table 1), which is not correct.
The abolition study shows that video encoder features alone are producing almost similar results with the entire set of features on the subsets of HMDB51, so what is the point in inclusion of other features?
What about including/cherry picking some other videos from HMDB51 that are normal, but are similar to the abnormal videos already included in the two subsets?

### Questions
Please see the previous section

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors study anomaly detection in video, presenting two datasets with video-level annotations and an adapted version of AI-VAD, called MFAD, which performs well on the proposed datasets. The presented method is also evaluated on three existing datasets, being compared with AI-VAD and other methods from literature.

### Strengths
- Anomaly detection is an interesting and timely topic.
- The paper is well written and easy to follow.

### Weaknesses
 - The proposed method is incremental w.r.t. AI-VAD.
- UCF-Crime and XD-Violence datasets are not included in the comparison provided in Table 1.
- The proposed datasets are rearranged subsets of HMDB51. There was no manual annotation involved, or at least, the authors did not mentione anything about it. Therefore, it is hard to consider the proposed datasets as entirely new. Just as the method, this contribution is incremental.
- The comparison in Table 1 does not reflect the difficulty / diversity advantages suggested by the authors. I do not see the benefits of the proposed datasets w.r.t. recent benchmarks such as UCF-Crime, XD-Violence or UBnormal.
- The proposed datasets contain video-level annotations (the videos are labeled either as normal or abnormal), while other benchmarks contain frame or pixel annotations. I believe this type of annotation does not reflect a realistic scenario.
- There is no time evaluation reported for the presented method. Anomaly detection methods are expected to run in real-time, but it is not clear if MFAD can do this. To me, the method is a bit heavy.
- There are some some language corrections to be made, e.g.:
  - "It’s crucial to" => "It is crucial to" (language abbrevations should be avoided in formal language).

### Questions
Please see the weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
1 poor
