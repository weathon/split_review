# GLOMA: Global Video Text Spotting with Morphological Association

- Decision: Accept
- Avg Score: 6.75
- Scores: 8, 8, 5, 6

## Abstract
Video Text Spotting (VTS) is a fundamental visual task that aims to predict the trajectories and content of texts in a video. Previous works usually conduct local associations and apply IoU-based distance and complex post-processing procedures to boost performance, ignoring the abundant temporal information and the morphological characteristics in VTS. In this paper, we propose \model{} to model the tracking problem as global associations and utilize the Gaussian Wasserstein distance to guide the morphological correlation between frames. Our main contributions can be summarized as three folds. 1). We propose a Transformer-based global tracking method \model{} for VTS and associate multiple frames simultaneously. 2). We introduce a Wasserstein distance-based method to conduct positional associations between frames. 3). We conduct extensive experiments on public datasets. On the ICDAR2015 video dataset, \model{} achieves \textbf{56.0} MOTA with \textbf{4.6} absolute improvement compared with the previous SOTA method and outperforms the previous Transformer-based method by a significant \textbf{8.3} MOTA.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This article proposes a more effective tracking method for video text based on the characteristics of the text. In specific, The paper introduce GLOMA to model the tracking problem as global associations and utilize the Gaussian Wasserstein distance to guide the morphological correlation between frames. GLOMA achieves state-of-the-art performance on multiple video text recognition benchmarks.

### Strengths
1. The article is clearly written and easy to understand. 

2. The motivation is strong, Wasserstein distance is indeed a better measurement for video text association. 

3. Extensive experiments demonstrate the effectiveness of the proposed new association method.

4. The proposed method demonstrates improved performance compared to several SOTA methods across multiple benchmarks.

### Weaknesses
1. Compared to TransDETR, which uses learnable query for object tracking, what is the advantage of the proposed association method.

### Questions
See weaknesses

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This manuscript introduces GLOMA, a Transformer-based global tracking approach that frames the tracking challenge as a problem of global associations. It employs the Gaussian Wasserstein distance to facilitate morphological correlation across frames. The efficacy of GLOMA is demonstrated through experimental results on renowned benchmarks, including the ICDAR 2015 video dataset. The contributions of this manuscript are:
1. A Transformer-based global tracking method for VTS that associates frames globally.
2. A Wasserstein distance-based method for measuring morphological similarity.
3. Extensive experiments on public datasets, demonstrating state-of-the-art performance.

### Strengths
**Global Association Approach**: The paper introduces a Transformer-based global tracking method that simultaneously associates multiple frames, effectively utilizing global context information in video sequences.

**Gaussian Wasserstein Distance**:
The use of Wasserstein distance for positional association considers both location and morphological features, enhancing the accuracy of matching, especially in scenarios with fast movement or interference.

**Performance Improvements**:
Achieving a 56.0 MOTA on the ICDAR2015 video dataset, with a 4.6 absolute improvement over the previous state-of-the-art method and an 8.3 MOTA improvement over the previous Transformer-based method, demonstrating significant performance gains.

**Extensive Experimental Validation**:
The paper conducts extensive experiments on public datasets, validating the effectiveness of the GLOMA method, which proves its practicality and efficacy in the field of video text recognition.

### Weaknesses
 **The Choice of the Text Detector/Spotter**:
The paper discusses the use of a 4-point coordinate prediction head for text detection within the GLOMA framework. However, it does not incorporate state-of-the-art text detectors or text spotters capable of detecting text of arbitrary shapes, such as DBNet++ and Mask TextSpotter v3. It would be beneficial to understand why these advanced detectors or spotters were not utilized in the proposed method. Specifically, the paper should address the challenges of integrating these more complex detectors, such as potential increases in computational cost or difficulties in end-to-end training. Additionally, the paper should ideally include a discussion on existing scene text spotting methods as part of its related work, given that these are foundational to the field of video text spotting.

**The Use of the Synthetic Data**:
Regarding the use of synthetic data for training, as demonstrated in TransDETR, synthetic data can significantly enhance model performance when used as pretraining data. For instance, TransDETR achieved a 51.8 MOTA score on the ICDAR 2015 video dataset with synthetic data, compared to a 47.7 MOTA score without it. It would be insightful to know why the proposed GLOMA method did not leverage synthetic data for training purposes. The paper should discuss the potential benefits and drawbacks of using synthetic data, including the challenges of domain adaptation and the potential for introducing bias. Addressing these points could provide a more comprehensive understanding of the design choices made in developing the GLOMA framework and how it compares to other leading approaches in the field.

### Questions
Please give the responses to the concerns in the Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
Summary
The article presents a novel method for video text spotting (VTS) that leverages global associations and morphological information, called GLOMA. This approach primarily addresses the limitations of current VTS methods, which typically rely on local associations and IoU-based distance metrics, often ignoring rich temporal and morphological cues. The main contributions of GLOMA include: a Transformer-based global tracking method, a position association method based on the Wasserstein distance, and extensive experiments demonstrating state-of-the-art performance across multiple benchmark datasets.

### Strengths
Strengths
1. GLOMA makes a significant contribution to the field by utilizing global associations through the Transformer architecture and integrating morphological information with the Gaussian Wasserstein distance. This effectively addresses the limitations of previous methods that primarily relied on local pairwise comparisons.
2. The paper demonstrates significant performance improvements across multiple datasets. For example, the MOTA on the ICDAR2015 video dataset improved by 4.6 absolute points, and compared to the previous best Transformer-based method, MOTA improved by 8.3 points. These results strongly validate the effectiveness of the GLOMA method. 
3. The authors conducted an in-depth ablation study to examine the impact of key components such as sliding window size, distance measurement, attention layers, and semantic embeddings. This provides valuable insights for model design.
4. The paper is well-written, with clear explanations of the method, including architecture, training process, and inference process. Figures and tables effectively illustrate key concepts and results.

### Weaknesses
Weaknesses
Although the experimental results are encouraging, there are still several key issues that need further clarification: 
1. In the abstract, the sentence “ignoring the abundant temporal information and the morphological characteristics in VTS” conveys the idea of neglecting temporal information and morphological features, but it does not sufficiently emphasize the importance of these features for the video text tracking (VTS) task. It is suggested to more explicitly highlight the core role of temporal information and morphological features in VTS to enhance reader understanding.
2. Although the abstract mentions the "Gaussian Wasserstein distance," it does not explain its specific advantages and role in VTS in detail. Readers may want more information on why this method is more effective than traditional IoU distance. Similarly, the innovations of GLOMA could be slightly expanded to show its contributions to solving existing problems.
3. The transitions between different sections in the introduction are not very smooth. For example, the description of existing research methods directly jumps to the introduction of the new model GLOMA, lacking transitional paragraphs to clarify why a new model is needed. It is suggested to add some transition sentences to better guide readers from existing work to the proposal of the new model.
4. Figure 1 does not clearly indicate the specific types of failure situations (such as target loss or target error) before directly introducing global associations to reduce the probability of failure. Perhaps the phrase "To solve the problems" could be removed, and the role of global associations could be directly stated. Additionally, other types of failure situations could be added to enhance persuasiveness and comprehensiveness of the explanation.
5. In section 3.1 Overview, it is mentioned that GLOMA has three parallel modules: detection module, recognition module, and tracking module. However, these modules are not clearly represented in Figure 2, and the aesthetic and logical clarity of the illustration is lacking. It is recommended to use more distinct dividing lines to separate the modules and add text descriptions in the figure, especially in the right-side process section, to enhance overall visualization.
6. The statement "Wasserstein distance can capture both location similarity and morphological similarity" theoretically makes sense, but it lacks detailed explanation on how it specifically captures morphological similarity. It is suggested to add an explanation of how the Wasserstein distance is used to measure morphological features, helping readers understand its advantages over traditional IoU.
7. In equation (8), it is mentioned that α is a hyperparameter, but the text does not detail how to choose this hyperparameter and its impact on model performance. Moreover, the form and role of the function f are not thoroughly discussed. It is recommended to provide details on the hyperparameter selection process, especially the normalization process of f and its impact on the results.
8. Although the text provides a general framework for embedding pool and trajectory association, it lacks detailed explanations about the embedding computation and updating mechanism. For example, how are embeddings updated? How is the length of the sliding window selected? Is there a trajectory drift problem? It is suggested to further elaborate on the embedding update strategy and trajectory construction details during inference.

### Questions
Please refer to my previous comments.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper studies the video text spotting problem by introducing a GLOMA method as a new solution. The proposed GLOMA formulates a global association task to tackle the VTS problem, in which a Transformer tracking method and a Wasserstein distance method facilitates the tracking.

### Strengths
Writing looks good. Results are promising.

### Weaknesses
I have many concerns about the demonstration of novelty. The contributions of this paper also need better clarification. See the questions below.

(1) After reading through the paper, it remains unclear to me why the authors need to devise a specific Transformer and specific association mechanism to fulfill the VTS. To my understanding, there are many SOTA multi-object tracking algorithms and single object tracking algorithms that seem perfectly fit the proposed task. The current SOTA methods do not simply rely on the IoU matching, despite that the VTS fields may have many IoU-based approaches. I am not saying that devising new approaches for VTS is not important, but at least the paper requires a much clearer justification of why existing SOTA multi-/single-object tracking algorithms cannot tackle this task effectively. The potentially related SOTA tracking methods include but not limited to [1,2,3,4]. The comparison (or at least discussion) about more SOTA tracking methods helps better justify why the proposed technique is superior over existing multi-/single-object tracking algorithms.

(2) The presentation is also not very easy-to-understand. In particular, the colorful circles are not easy to interpret. Both figure 1 and 2 lacks sufficient clarifications about the patterns used in the figure. What do the colorful circles exactly refer to? Text spotting results in bounding boxes or masks? What are associated? The current presentation style requires better clarification.

(3) It is not clear to me what new insights are contributed in this paper. All the employed technologies are well-known techniques. In particular, I suggest the authors to explicitly state the novel aspects of their approach and how it differs from simply combining existing techniques. How does this ensemble of existing techniques introduce new design ideas in the community? In addition, I do not quite buy the claim of "global" in this paper, please better clarify what they mean by "global" and how their approach achieves this, given the limited number of frames considered. Lastly, Please provide a more comprehensive and informative justification for using Wasserstein distances specifically, perhaps by comparing it to other distance metrics they considered.

(4) Lastly, the experiments seem not very convincing as well. The compared methods look kind of old. Not many more recent approaches are discussed and compared in the results. This limits the contribution of this paper.  For the compared methods, more recent related literature deserves a comparison or at least discussion. This includes but not limited to [5][6].

### Questions
(1) After reading through the paper, it remains unclear to me why the authors need to devise a specific Transformer and specific association mechanism to fulfill the VTS. To my understanding, there are many SOTA multi-object tracking algorithms and single object tracking algorithms that seem perfectly fit the proposed task. The current SOTA methods do not simply rely on the IoU matching, despite that the VTS fields may have many IoU-based approaches. I am not saying that devising new approaches for VTS is not important, but at least the paper requires a much clearer justification of why existing SOTA multi-/single-object tracking algorithms cannot tackle this task effectively. The potentially related SOTA tracking methods include but not limited to [1,2,3,4]. The comparison (or at least discussion) about more SOTA tracking methods helps better justify why the proposed technique is superior over existing multi-/single-object tracking algorithms. 

(2) The presentation is also not very easy-to-understand. In particular, the colorful circles are not easy to interpret. Both figure 1 and 2 lacks sufficient clarifications about the patterns used in the figure. What do the colorful circles exactly refer to? Text spotting results in bounding boxes or masks? What are associated? The current presentation style requires better clarification. 

(3) It is not clear to me what new insights are contributed in this paper. All the employed technologies are well-known techniques. In particular, I suggest the authors to explicitly state the novel aspects of their approach and how it differs from simply combining existing techniques. How does this ensemble of existing techniques introduce new design ideas in the community? In addition, I do not quite buy the claim of "global" in this paper, please better clarify what they mean by "global" and how their approach achieves this, given the limited number of frames considered. Lastly, Please provide a more comprehensive and informative justification for using Wasserstein distances specifically, perhaps by comparing it to other distance metrics they considered.

(4) Lastly, the experiments seem not very convincing as well. The compared methods look kind of old. Not many more recent approaches are discussed and compared in the results. This limits the contribution of this paper.  For the compared methods, more recent related literature deserves a comparison or at least discussion. This includes but not limited to [5][6]. 

I would like to see the authors' response before making my final decision.

[1] Xu, Yuanyou, Zongxin Yang, and Yi Yang. "Integrating boxes and masks: A multi-object framework for unified visual tracking and segmentation." Proceedings of the IEEE/CVF International Conference on Computer Vision. 2023.
[2] Shim, Kyujin, et al. "Adaptrack: Adaptive Thresholding-Based Matching for Multi-Object Tracking." 2024 IEEE International Conference on Image Processing (ICIP). IEEE, 2024.
[3] Cao, J., et al. "Observation-centric sort: Rethinking sort for robust multi-object tracking. arXiv 2022." arXiv preprint arXiv:2203.14360.
[4] Cheng, Ho Kei, and Alexander G. Schwing. "Xmem: Long-term video object segmentation with an atkinson-shiffrin memory model." European Conference on Computer Vision. Cham: Springer Nature Switzerland, 2022.
[5] Wu, Weijia, et al. "End-to-end video text spotting with transformer." International Journal of Computer Vision 132.9 (2024): 4019-4035.
[6] Wu, Weijia, et al. "DSText V2: A comprehensive video text spotting dataset for dense and small text." Pattern Recognition 149 (2024): 110177.

### Soundness
2

### Presentation
1

### Contribution
2
