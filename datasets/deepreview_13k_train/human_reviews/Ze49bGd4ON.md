# SAM2Long: Enhancing SAM2 for Long Video Segmentation with a Training-Free Memory Tree

- Decision: Reject
- Scores: 5, 8, 3, 5

## Abstract
The Segment Anything Model 2 (SAM~2) has emerged as a powerful foundation model for object segmentation in both images and videos, paving the way for various downstream video applications.
The crucial design of SAM~2 for video segmentation is its memory module, which prompts object-aware memories from previous frames for current frame prediction.
However, its greedy-selection memory design suffers from the ``error accumulation" problem, where an errored or missed mask will cascade and influence the segmentation of the subsequent frames, which limits the performance of SAM~2 toward complex long-term videos.
To this end, we introduce SAM2Long, an improved \textbf{training-free} video object segmentation strategy, which considers the segmentation uncertainty within each frame and chooses the video-level optimal results from multiple segmentation pathways in a constrained tree search manner. 
In practice, we maintain a fixed number of segmentation pathways throughout the video.
For each frame, multiple masks are proposed based on the existing pathways, creating various candidate branches. We then select the same fixed number of branches with higher cumulative scores as the new pathways for the next frame. After processing the final frame, the pathway with the highest cumulative score is chosen as the final segmentation result.
Benefiting from its heuristic search design, SAM2Long is robust toward occlusions and object reappearances, and can effectively segment and track objects for complex long-term videos. 
Without introducing any additional parameters or further training, SAM2Long significantly and consistently outperforms SAM~2 on five VOS benchmarks. Notably, SAM2Long achieves an average improvement of \textbf{3.0} points across all 24 head-to-head comparisons, with gains of up to 5.3 points in $\mathcal{J} \& \mathcal{F}$ on long-term video object segmentation benchmarks such as SA-V and LVOS.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This article presents SAM2Long, an improved training-free video object segmentation strategy designed to address the limitations of the Segment Anything Model 2 (SAM2) in long video segmentation. It identifies the "error accumulation" issue in SAM2's greedy memory selection design, where errors in mask predictions for one frame negatively impact subsequent frames, particularly in complex long videos. SAM2Long introduces a constrained tree memory structure that maintains a fixed number of segmentation pathways, allowing for the generation of multiple candidate branches for each frame and selecting the best pathways based on cumulative scores. To enhance robustness, it prevents premature convergence on incorrect predictions by selecting hypotheses with distinct predicted masks in uncertain situations and includes only high-quality segmentation masks and confidently detected objects in the memory bank. Empirical evaluations show that SAM2Long significantly outperforms SAM2 across various video object segmentation benchmarks, achieving an average improvement of 3.8 points, with some cases showing up to a 5-point increase in J&F scores on long-term video benchmarks. Overall, SAM2Long enhances the memory module and introduces a new selection mechanism, effectively improving segmentation and tracking of objects in complex long video scenarios.

### Strengths
1.The introduction of a constrained tree memory structure is a novel contribution that effectively addresses the limitations of the existing SAM2 model, particularly in handling long video segmentation tasks.
2.The method's ability to prevent error accumulation by maintaining multiple segmentation pathways enhances its robustness, which is crucial for real-world applications where occlusions and complex scenes are common.

### Weaknesses
This article introduces a new constrained tree memory structure to avoid error accumulation. The method compares the results obtained from multiple decodings, selecting the optimal one from each path to update the new memory bank. However, there are some unclear aspects in the description of the method:

1. Unclear Source of Memory Bank Updates: What is the source of the memory bank updates for each path? Is it derived from the previous state of another branch or the previous state of the current branch? The description of the tree memory structure is not clear and complete. It is recommended to provide a detailed explanation of this process or to include visual examples to help readers better understand.

2. Mask Storage and Calculation Method: Does each memory bank store the overall mask for all targets, or does it store individual masks for each target? The calculation of the IoU for the masks also needs clarification—does it represent the average of the masks for multiple targets, or is it calculated in another way? Additionally, are all the threshold settings designed based on statistical results, or are they set randomly? This point requires further explanation.

There are also shortcomings in the experimental results:

1. Lack of Comparative Experiments: There is a lack of comparative experiments with SAM2 on the YouTube VOS and MOSE datasets. These comparative experiments are crucial for validating the effectiveness of the new method, and it is suggested to supplement relevant results.

2. Unreasonable Parameter Design in Ablation Experiments: In Tables 6, 7, and 8, the threshold for conf is set to [0.5, 2, 5], which has too large of an interval and does not meet statistical standards. Furthermore, have all the thresholds been statistically analyzed based on the actual IoU and conf situations across all frames? Would it be better to design thresholds based on statistical data? Is there any inconsistency in the actual IoU and conf situations across different datasets? These questions need further exploration and explanation.

### Questions
1.Unclear Source of Memory Bank Updates: What is the source of the memory bank updates for each path? Is it derived from the previous state of another branch or the previous state of the current branch? The description of the tree memory structure is not clear and complete. It is recommended to provide a detailed explanation of this process or to include visual examples to help readers better understand.

2.Mask Storage and Calculation Method: Does each memory bank store the overall mask for all targets, or does it store individual masks for each target? The calculation of the IoU for the masks also needs clarification—does it represent the average of the masks for multiple targets, or is it calculated in another way? Additionally, are all the threshold settings designed based on statistical results, or are they set randomly? This point requires further explanation.

3.Lack of Comparative Experiments: There is a lack of comparative experiments with SAM2 on the YouTube VOS and MOSE datasets. These comparative experiments are crucial for validating the effectiveness of the new method, and it is suggested to supplement relevant results.

4.Unreasonable Parameter Design in Ablation Experiments: In Tables 6, 7, and 8, the threshold for conf is set to [0.5, 2, 5], which has too large of an interval and does not meet statistical standards. Furthermore, have all the thresholds been statistically analyzed based on the actual IoU and conf situations across all frames? Would it be better to design thresholds based on statistical data? Is there any inconsistency in the actual IoU and conf situations across different datasets? These questions need further exploration and explanation.

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
4

### Summary
Authors propose SAM2Long model that builds on the precursor SAM2 for video object segmentation and tracking while ensuring it works in long-term tracking scenarios. They propose using a constrained tree based memory within SAM2 framework that allows for exploring multiple valid pathways and overcoming issues with occlusion or going out of the field of view then back in. They evaluate on various benchmarks including LVOS, VOST in addition to standard benchmarks such as DAVIS showing consistent improvement over their baseline SAM2 with a considerable margin.

### Strengths
- Strong results and gain w.r.t the baseline SAM2
- Interesting work that focuses on segmentation and tracking in long videos which is indeed a challenging scenario.

### Weaknesses
 - a full evaluation of the computational efficiency in terms of runtime, FLOPS and parameters is needed so we can evaluate the overhead of their method w.r.t SAM2 beyond what is presented in Table 5. Specifically, a breakdown of the FLOPS for each module (image encoder, memory encoder, mask decoder, memory attention) would be beneficial to understand where the computational bottlenecks are and how the proposed tree-based memory impacts the overall efficiency. Furthermore, reporting the throughput (e.g., frames per second) would provide a more practical measure of the method's real-world performance. It is also unclear if the reported throughput in Table 5 is with respect to the SAM2-Large model or the SAM2-ViT-H model, which would be useful to clarify.

 - Ablation on the modulation in Table 8, how were these parameters ranges selected during the ablation? What happens outside that range? Also the changes seem to be quite minor and negligible in the last two rows so would be good to see what happens as we increase this? It would be helpful to understand the sensitivity of the model to these modulation parameters, and whether there is a risk of performance degradation if the parameters are not tuned correctly. The current ablation study only explores a narrow range of values, and it is not clear if this range is optimal or if there are other ranges that could lead to better performance or instability.

### Questions
- Ablation on the modulation in Table 8, how were these parameters ranges selected during the ablation? What happens outside that range? Also the changes seem to be quite minor and negligible in the last two rows so would be good to see what happens as we increase this?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper focuses on tackling the problem of video object segmentation for long videos. The proposed solution, SAM2Long, is an enhancement to the Segment Anything Model 2 (SAM2), designed to address its limitations in segmenting long videos, specifically in handling occlusions and preventing error accumulation. To achieve this, SAM2Long utilizes a training-free, constrained memory tree structure that tracks multiple segmentation pathways, selecting the most reliable ones over time. The effectiveness of the method is demonstrated through evaluations across various benchmarks, showing significant performance improvements over SAM2 in terms of J&F scores on occlusion-heavy and long-term video object segmentation datasets.

### Strengths
1. The proposed approach is intuitively reasonable.

2. The proposed SAM2Long outperforms strong SAM2 on standard VOS benchmarks without extra training.

3. The proposed approach does not significantly raise computational expenses.

### Weaknesses
1. The paper provides little insights for the video object segmentation community. Although the constrained memory tree and memory bank management strategies are useful, they seem to be heuristic engineering rather than research findings. For instance, all mask selection processes are treated on a case-by-case basis. Consequently, it seems unlikely that the approach can handle all possible scenarios. Does SAM2 consistently predict the IoU/occlusion scores for both small and large instances? How can we ensure the reliability of the predicted IoU/occlusion scores? What happens if SAM2 produces incorrect predictions for all N candidates? Are there no other cues available to enhance the robustness of VOS beyond IoU/occlusion scores?

2. The proposed method restricts SAM2 to ground-truth mask prompts. One of the strengths of SAM2 lies in its ability to handle various types of prompts (e.g., boxes, points, masks) and interactive scenarios. However, the presented approach eliminates this versatility by overfitting to a single scenario.

3. The paper lacks discussions on limitations or analyses of failure cases. Simply presenting a single failure case in the supplementary video without further analysis offers limited value to the readers.

4. There is no analysis of the effectiveness in long-term and occlusion-heavy scenarios. The paper only presents quantitative and qualitative results on full benchmark datasets. As a result, it is difficult to conclude that this work truly excels in such challenging conditions, as argued in L107. The paper can provide a performance comparison based on the number of frames and the number of occluded instances.

5. The paper reports lower performance of the SAM2 baselines compared to the official implementation (see https://github.com/facebookresearch/sam2#model-description). The paper should explain the reasons behind this performance gap.

6. Experimental results on YouTube-VOS 2019 are missing. This benchmark is widely used in the VOS field, and SAM2 demonstrates strong performance on it. Given that YouTube-VOS 2019 also includes complex occlusion-heavy scenes, it would be beneficial to include the results from this benchmark in the paper.

7. L162: we redesign -> We redesign

### Questions
My primary concerns include the limited insights, overfitting to the mask prompt, and a lack of experimental analysis. My initial recommendation stands at rejection; however, I'm open to revising this rating if the aforementioned shortcomings are properly addressed.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes SAM2Long, a method comprising multiple strategies to enhance SAM2. SAM2Long maintains multiple memory banks and selectively includes frames with high-quality segmentation masks to reduce error accumulation. The method demonstrates improved performance across multiple benchmarks.

### Strengths
1. The paper is easy to understand. 

2. Constructing multiple memory banks to reduce error accumulation is reasonable, and the method achieves improved performance on VOS.

### Weaknesses
1. This paper expands memory banks to improve performance, the idea is reasonable but brings limited new insights.

2. The method comprises a set of strategies with hyperparameters, adding complexity to the baseline and affecting efficiency, with unclear generalization.

3. The ablation study is incomplete, making it difficult to understand the effect of each individual strategy.

4. The limitations of the proposed method are not discussed.

### Questions
See Weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2
