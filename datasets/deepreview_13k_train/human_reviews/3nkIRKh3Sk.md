# AVSS: a new benchmark for airport video semantic segmentation

- Decision: Reject
- Scores: 5, 3, 5, 6

## Abstract
Airport video semantic segmentation is fundamental to airport surveillance applications, yet there currently lacks a specialized benchmark and algorithms for this task. In this paper, we introduce the first large-scale Airport Video Semantic Segmentation dataset (AVSS) for airport surveillance. AVSS comprises 18 common semantic categories at airports, and 250 videos, totaling over 140,000 frames with accurate manual annotations. AVSS covers a wide range of challenges for airport video surveillance, such as extreme multi-scale, intra-class diversity, inter-class similarity, etc. We analyze statistical information and evaluate 17 state-of-the-art (SOTA) semantic segmentation algorithms on AVSS. The significant performance degradation indicates that current models are far from practical application. Furthermore, we discuss how to develop video semantic segmentation algorithms for airport surveillance and the generalizability of AVSS to other tasks and datasets. AVSS serves as a research resource for airport semantic segmentation and a robustness evaluation tool for segmentation algorithms in practical applications. AVSS is available at www.agvs-caac.com/avss/avss.html.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper introduces a new dataset consisting of 250 short videos of outdoors airport scenes, with segmentation annotations of 18 categories on all frames. A variety of recent image and video segmentation methods are fine-tuned and tested on the dataset, yielding relatively low accuracies on most categories. The dataset is characterized by various analytics and a few metrics.

### Strengths
Demonstrating the low accuracies of popular segmentation techniques on a real-world problem is a significant contribution. The challenges of this dataset are also found in many surveillance datasets, hence addressing them through research on this dataset could have impact in many surveillance domains.

The distribution of annotations and pixels by class is useful to see, Fig. 5. The dataset seems to follow a long-tail distribution which is very common in real-world settings like this, whereas more contrived datasets often have a relatively uniform distribution.

The annotation compactness metric is well formulated, based on a standard spatial moment calculation. It would be interesting to see a comparison to other surveillance segmentation datasets.

The evaluation is quite thorough, testing a variety of current approaches for both image and video segmentation. The low accuracies of all of the algorithms indicate the difficulty of the problem and the utility of the dataset.

### Weaknesses
There is essentially no stated motivation for semantic segmentation at airports. The one mention of this, in the first paragraph is very vague. It would be more convincing to enumerate a set of use cases motivating the need for accurate segmentation rather than bounding boxes. For example, what specific tasks require pixel-level accuracy, and why are bounding boxes insufficient for these tasks in the context of airport operations?

The Intro should clarify that only outdoor scenes are included in the dataset, since there are numerous video surveillance datasets that include indoor scenes are airports and other large facilities. The current description is ambiguous and could lead to misinterpretations about the scope of the dataset.

Downselecting from 5000 collected videos to 250 included videos is a huge reduction. Was this primarily motivated by the cost of creating ground-truth segmentations? The methods used for data selection are not described. What specific criteria were used to select these 250 videos, and how was diversity ensured across different scenes, weather conditions, and lighting variations?

The data annotation section describes the process for annotating one image, but does not mention how video is annotated. In video from a fixed camera, a single annotation of a fixed object e.g. a Building should be transformable to subsequent video frames without editing. Was this method used? Even for movers, the annotation on the previous frame can be copied to the current frame and adjusted, greatly reducing effort and inter-frame annotation variability. The lack of detail on video annotation raises concerns about the efficiency and consistency of the annotation process.

Creating segmentation annotations manually is expensive on images, even more so on video as performed here. The dataset is much smaller than VSPW in terms of number of videos and classes, partly because of the narrower problem domain.
Image coherence, Eq. 1, does not seem to be an advantage nor disadvantage. With a moving camera, image coherence would be very low, for example. A large number of movers would yield low coherence. Similarly, label coherence is a function of camera and object movement, not just label spatial consistency across frames. The purpose of these measures, and the comparison to other datasets, is very unclear and not well motivated. I’d suggest removing this section, or, more significantly, reformulating these metrics to measure how consistent an object label remains across video frames.

The topic of this paper is rather specific and seems more appropriate for a computer vision venue such as WACV, or AVSS (the conference with the same acronym as the dataset).

### Questions
There is a natural hierarchy among some of the classes, such as Building, Terminal (subtype of Building), Tower (subtype of Building). Did you consider defining an explicit class taxonomy rather than just a flat list of classes? A taxonomy would enable natural expansion to additional classes and potentially resolve ambiguities such as incorrectly declaring a false alarm when a Terminal is labeled as a Building.

During data collection, why were the videos so short, 15 sec? Since the cameras are fixed, it seems straightforward to collect long videos e.g. hours in order to capture a diversity of long-range airport activities.

How many airports are in the dataset? How many unique camera views? Many important details are missing.

What proportion of the dataset was used for fine-tuning vs. testing? Were less-frequent classes handled differently than more common ones?

The IOU results on Person are the lowest of any any category, despite the maturity of person detectors. Why? Is it the small pixel size of people in this dataset? What would happen if the images were up-sampled 2X or 4X?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
This paper proposes a novel benchmark for Airport video semantic segmentation and introduces a semantic segmentation algorithm based on a 3D airplane model. The authors identify key challenges in airport scenes, including extreme multi-scale variation, intra-class diversity, and inter-class similarity. Addressing these issues, they propose a benchmark that is evaluated from various perspectives. First, they conduct a statistical analysis by measuring class distribution, inter-frame coherence, and compactness. By applying the proposed method to various models, the authors demonstrate the increased difficulty of their benchmark compared to existing public datasets. To further assess generalizability, they train models on the proposed dataset and compare performance with the VSPW dataset. To this end, the authors present a 3D airplane model-based algorithm tailored specifically for airport segmentation.

### Strengths
1. It provides insights into potential issues in airport semantic segmentation, such as extreme multi-scale, intra-class diversity, and inter-class similarity.
2. The proposed benchmark has been evaluated against various state-of-the-art (SOTA) models.

### Weaknesses
 1. It would be helpful to specify the diversity principles in “Data collection” in detail.

 2. A reference to AnyLabeling in the “Data annotation” should be included.

 3. The analysis of whether the proposed benchmark can cover intra-class diversity, a key challenge in airport semantic segmentation, is insufficient. It would be beneficial to examine various aspects, such as color distribution and feature distribution within the same category, to provide a more comprehensive analysis.

 4. There is a need to analyze whether the proposed benchmark addresses inter-class similarity.

 5. I have doubts about the actual relationship between compactness and segmentation difficulty. For example, in Table 2, while there is a large gap in results between "Runway" and "Liaison Road," the difference in compactness is not significant. Additionally, while there is a small gap in results between "Runway" and "Person," the difference in compactness is large.

 6. For the generalizability analysis experiment, comparing similar categories from another dataset (such as Cityscape) would be more helpful.

 7. The author suggests that a model performing well on AVSS is likely to achieve favorable segmentation results on other datasets (page 8, lines 430-431). However, it would be useful to have an experiment to verify this claim. For example, by comparing the performance differences between the top 3 models with the highest performance and the bottom 3 models with the lowest performance on AVSS, it could provide valuable insights into whether models that perform well on AVSS have a similar tendency on other datasets.

 8. There are no qualitative results for the proposed 3D airplane-based algorithm for airport semantic segmentation.

### Questions
Please refer to the weakness part.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
In this paper, it introduces the first large-scale Airport Video Semantic Segmentation dataset (AVSS) for airport surveillance. AVSS comprises 18 common semantic categories at airports, and 250 videos, totaling over 140,000 frames with accurate manual annotations. AVSS covers a wide range of challenges for airport video surveillance, such as extreme multi-scale, intra-class diversity, inter-class
similarity, etc. The authors analyze statistical information and evaluate 18 state-of-theart (SOTA) semantic segmentation algorithms on AVSS. The significant performance degradation indicates that current models are far from practical application. Furthermore, this paper discuss how to develop video semantic segmentation algorithms for airport surveillance and the generalizability of AVSS to other tasks
and datasets. AVSS serves as a research resource for airport semantic segmentation and a robustness evaluation tool for segmentation algorithms in practical applications.

### Strengths
In conclusion, the main contributions are as follows:
1. this paper establish the novel AVSS, providing a benchmark for airport semantic segmentation.
2. this paper evaluate the generalizability of AVSS and 18 SOTA segmentation algorithms on AVSS.
3. this paper propose principles for designing airport video semantic segmentation models.

### Weaknesses
The weakness can be as follows:

1. In table 1, the paper shows the coherence is higher than other datasets. But for the cohenrence metric equaiton (1) (2), it's not clear how to compute the corresponding pixels between difference frames; in addition, higher coherence means the data variety is low for a video squezze, as the AVSS datasets only has 250 videos, does it mean it has only 250 scenes with just changing people, plane etc but the background is fixed. From this view, the variety of the AVSS dataset can be low.
2. For the 4.3 GENERALIZABILITY,  the first sentence is "test the model trained on AVSS on VSPW", is it a typo? As the table 4 shows "The classes IoU of SOTA models trained on AVSS, evaluated on AVSS and VSPW." For this experiment, it is necessary to conduct the experiment comparing the model trained on VSPW and test on AVSS and VSPW.

### Questions
No.

### Soundness
3

### Presentation
3

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
This paper introduces a new dataset for airport video semantic segmentation (AVSS) with manually labeled masks. It then benchmarks current VSS models on this dataset, highlighting a significant drop in performance when applied to AVSS and providing future insights for designing suitable VSS models for this domain.

### Strengths
+ The dataset is based on novel airport scenes, providing a new perspective to evaluate VSS models and contributing a valuable resource for future researchers.
+ The dataset is manually labeled, ensuring high-quality annotations.
+ The experiments reveal the limitations of existing models on this dataset.

### Weaknesses
 - The scale of AVSS (only 250 videos) is relatively small compared to current VSS datasets.
- The related work section should include more recent advancements in VSS models and benchmarking should add some recent works, such as:
   - Mask propagation for efficient video semantic segmentation
   - Pay attention to target: Relation-aware temporal consistency for domain adaptive video semantic segmentation
   - Temporal-aware Hierarchical Mask Classification for Video Semantic Segmentation

### Questions
Refer to weakness.

### Soundness
3

### Presentation
3

### Contribution
3
