# TAO-Amodal: A Benchmark for Tracking Any Object Amodally

- Decision: Reject
- Avg Score: 6.00
- Scores: 5, 6, 5, 8

## Abstract
Amodal perception, the ability to comprehend complete object structures from partial visibility, is a fundamental skill, even for infants. Its significance extends to applications like autonomous driving, where a clear understanding of heavily occluded objects is essential. However, modern detection and tracking algorithms often overlook this critical capability, perhaps due to the prevalence of \textit{modal} annotations in most benchmarks.
To address the scarcity of amodal benchmarks, we introduce TAO-Amodal, featuring 833 diverse categories in thousands of video sequences.
Our dataset includes \textit{amodal} and modal bounding boxes for visible and partially or fully occluded objects, including those that are partially out of the camera frame.
We investigate the current lay of the land in both amodal tracking and detection by benchmarking state-of-the-art modal trackers and amodal segmentation methods. We find that existing methods, even when adapted for amodal tracking, struggle to detect and track objects under heavy occlusion. To mitigate this, we explore simple finetuning schemes that can increase the amodal tracking and detection metrics of occluded objects by 2.1\% and 3.3\%.

\keywords{Amodal perception \and Large-scale evaluation benchmark \and Multi-object tracking.}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work presents a large-scale video benchmarks for amodal tracking, and the evaluation metrics and baseline trackers are also designed.
The challenges of amodal detection and tracking by evaluating a number of amodal trackers and segmentors are validtated on the created benchmark.

### Strengths
1. A comprehensive annotation for amodal tracking based on TAO dataset is performed.

2. A plugin module for amodal tracking and some data augmentation methods are designed.

3. Extensive experiments and analysis are conducted.

### Weaknesses
1. The contributions of this work seem small. TAO dataset is existing, and the contribution to the benchmark is large-scale annotations. The designed expander is also a simple regressor and data augmentation schemes are also based on existing ones.

2. The motivation of this task is unclear to me. When an object is totally occluded, its state, including position, size and motion, is very difficult to predict. Although authors consume much time to annotate such objects, but the quality can not be guaranteed because we do not know their real states. What are the potential downstream applications or benefits of amodal tracking that motivate this work? How might uncertainty in amodal predictions be handled or utilized in subsequent tasks?

### Questions
The contributions of this work seem small and the motivation is unclear to me.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The TAO-Amodal dataset method was introduced to address the amodal perception problem. It provides video sequences with 833 categories, including amodal and modal bounding boxes for visible and partially or fully occluded objects. This approach aims to address the scarcity of amodal benchmarks. Benchmarking current modal trackers and amodal segmentation methods reveals that existing methods struggle with detecting and tracking heavily occluded objects. Simple fine-tuning schemes were explored to mitigate this, improving the amodal tracking and detection metrics for occluded objects by 2.1% and 3.3%, respectively.

### Strengths
The authors present TAO-Amodal, a comprehensive and high-quality dataset designed to advance amodal perception by providing diverse occlusion annotations across 833 categories and introducing the Paste-and-Occlude (PNO) augmentation method, which simulates various occlusion scenarios to improve model robustness. This dataset enables rigorous benchmarking and reveals the limitations of current tracking algorithms under challenging conditions, offering a reliable foundation for future developments in amodal tracking research.

### Weaknesses
1、Limited Training Data: While the dataset is extensive for evaluation, the relatively small training set may restrict model generalization, especially for categories with fewer instances. This also means that subsequent research can only use this dataset for validation, making it ineffective for robust training.
2、During the data annotation phase, I noticed that the authors conducted detailed annotations, but I have a question: how did you determine the size of the occluded objects for annotation clearly?
3、The comparison is insufficient. The TAO dataset itself is an open-world dataset, but your evaluation method does not incorporate any open-world detection or open-world tracking approaches.
4、The examples of PasteNOcclude (PnO) shown in Figure 5 are overly simplistic. I want to know whether all data augmentation is done in this way.

### Questions
Please see the weakness. If my concerns are solved, I will consider raising my score.

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
5

### Summary
The paper introduces a new benchmark dataset, TAO-Amodal, which focuses on amodal perception. This is the ability to understand the full extent of objects, even when they are partially or fully occluded. The dataset includes diverse object categories and scenarios, such as objects that are both partially or fully occluded, and those that may be out of the frame in video sequences. The authors benchmark several state-of-the-art tracking methods and introduce fine tuning strategies that improve amodal tracking performance slightly.

### Strengths
The paper annotated a large-scale dataset that extends the capabilities of existing modal object tracking systems to amodal scenarios.

The authors benchmark several state-of-the-art tracking methods to evaluate the dataset.

To address occlusion challenges, the paper presents a series of new evaluation metrics suitable for tracking and detecting heavily and partially occluded objects. These metrics enhance the granularity and accuracy of existing evaluation methods.

The writing of the paper is good and easy to follow.

### Weaknesses
1. The main contribution of the paper is building a dataset for occluded objects. However, in Table 1, NuScenes has more Occlude boxes and tracks. Besides, the annotation FPS of TAO-amodal is only 1 fps, which is much smaller than previous datasets.


2. Although this is a paper primarily contributing a dataset, it is better to propose a method related to the most critical point of this paper (occluded objects) in order to effectively convey the importance of this work. The proposed fine-tuning method is too simple. The technique innovation is limited.


3. How can the quality of the annotations in the submitted dataset be ensured? There should be some quantitative metrics to demonstrate the accuracy of the annotations.


4. The TAO-Amodal training set is relatively small, which may restrict the ability to train models from scratch and may require pretraining on modal datasets.


5. What are the primary obstacles preventing end-to-end multi-object tracking (MOT) models from achieving optimal performance on the TAO-Amodal benchmark? What factors primarily contribute to this difficulty?


6. Despite fine-tuning and data augmentation, the performance improvements (2.1% in tracking and 3.3% in detection) are modest, indicating that current systems still struggle with occlusions.


7. Another important issue is the impact of the performance on normal object detection/tracking. It would be problematic if we only obtain minor performance improvements on amodal targets, but gain worse results for normal objects.


8. The experiments conducted in the paper primarily focus on a single dataset (TAO-Amodal). Broader testing across multiple datasets could provide more compelling results.


9. In the experimental section, further Analysis of Data Annotation Uncertainty is needed. The paper does not thoroughly explore the specific impact of uncertainty on evaluation outcomes, which warrants deeper investigation.


10. The compared methods are somehow out-of-date. Thus, the experimental results are not convincing.


11. More details about the baseline are needed, such as network architecture configurations.

### Questions
Please see the above.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces TAO-Amodal, a large-scale benchmark dataset for amodal object tracking, built upon the existing TAO dataset. The work addresses an important gap in computer vision by providing annotations for tracking objects under heavy occlusions and out-of-frame scenarios across 833 diverse categories in 2,907 videos. The authors evaluate current trackers and propose simple but effective finetuning schemes to improve amodal tracking performance.

### Strengths
1. The paper introduces the first large-scale amodal tracking benchmark that encompasses a diverse range of object categories, which is a significant advancement in the field. This benchmark addresses a critical gap in current datasets and tracking evaluations, as it provides a platform to assess and improve tracking algorithms under occlusion scenarios. 
2. The authors have developed a comprehensive annotation protocol that includes rigorous quality control measures, ensuring the reliability of the dataset. They have thoughtfully considered both in-frame and out-of-frame occlusions, which are essential for a holistic evaluation of tracking algorithms. 
3.The dataset is constructed on a large scale, with 332k boxes annotated across 2,907 videos, providing a substantial dataset for training and evaluating tracking models. It covers an impressive 833 object categories, making it one of the most diverse datasets available. The quality of the annotations is exceptionally high, with over 99% of the annotations meeting the quality standards set by the authors, which is crucial for the development and testing of robust tracking algorithms.

### Weaknesses
1. The training set appears to be relatively small compared to the validation and test sets. Could the authors explain the rationale behind this dataset split? It would be useful to discuss how the smaller training set might impact model performance. Additionally, considering options like data augmentation could help maximize the utility of the available training data and potentially improve model robustness.
2. A more detailed analysis of failure cases, such as full occlusion,  would be advantageous, as it would help to better understand the limitations of the models and potential areas for improvement. Including metrics or visualizations to highlight these limitations would add depth to the analysis and offer valuable insights for future research.
3.To maintain the state-of-the-art in tracking research, the authors are encouraged to incorporate the latest tracking methodologies, such as Hybrid-SORT [1] and MeMOTR [2], into the study.

### Questions
1. Could the authors provide more detailed analysis of how performance varies across different object categories?
2. The paper would benefit from more discussion about the annotation uncertainty in heavily occluded cases and its impact on evaluation metrics.

### Soundness
3

### Presentation
2

### Contribution
3
