# MixSup: Mixed-grained Supervision for Label-efficient LiDAR-based 3D Object Detection

- Decision: Accept
- Avg Score: 6.67
- Scores: 6, 8, 6

## Abstract
Label-efficient LiDAR-based 3D object detection is currently dominated by weakly/semi-supervised methods.
Instead of exclusively following one of them, we propose \textbf{\namenospace}, a more practical paradigm simultaneously utilizing massive cheap coarse labels and a limited number of accurate labels for \textbf{Mix}ed-grained \textbf{Sup}ervision.
We start by observing that point clouds are usually \emph{textureless}, making it hard to learn semantics.
However, point clouds are \emph{geometrically rich} and \emph{scale-invariant} to the distances from sensors, making it relatively easy to learn the geometry of objects, such as poses and shapes.
Thus, \name leverages massive coarse \emph{cluster-level} labels to learn semantics and a few expensive \emph{box-level} labels to learn accurate poses and shapes.
We redesign the label assignment in mainstream detectors, which allows them seamlessly integrated into \namenospace, enabling practicality and universality.
We validate its effectiveness in nuScenes, Waymo Open Dataset, and KITTI, employing various detectors.
\name achieves up to \textbf{97.31}\% of fully supervised performance, using cheap cluster annotations and only 10\% box annotations.
Furthermore, we propose \textbf{PointSAM} based on the Segment Anything Model for automated coarse labeling, further reducing the annotation burden.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors proposed MixSup for efficient LiDAR-based 3D object detection. It mainly consists of two contributions: (1) a cluster-level coarse labeling scheme by just labeling the 3 bounding box corners in bird's eye view, which the authors claim to have only 14% labeling time compared to full 3D labeling; (2) a learning strategy that utilizes both few full 3D labels and many coarse labels by training classification / proposal stage with only coarse labels and regression stage with full 3D labels. The authors show that on mulitple dataset and with multiple different detection mdoels, the proposed method can achieve the performance of the full supervised counterpart using all full 3D labels.

### Strengths
- The paper is overall easy to follow.
- The paper focuses on efficient learning for 3D detection, especially with an emphasis on autonomous driving applications. This active subarea holds significant promise to reduce the cost in autonomous vehicles.
- The proposed method is overall simple but with good performance in various settings.
- The authors also explored the automatic coarse labeling setting utilizing a SAM model.

### Weaknesses
1. Discussing and comparing with [Meng et al. 2020; 2021]. As pointed out in the related works in the paper, there are a bunch of existing works trying to reduce the labeling cost in the 3D detection task, and one of the closest works to this paper is probably [Meng et al. 2020; 2021], where they explored a similar setup: training models with many weakly labeled and few fully labeled 3D data. As a reader, I would expect to see further discussion and comparison between the proposed work and this work (e.g. the difference in labeling cost, the performance difference, and why the proposed method is a better approach). I do read that in Sec 4.5 and the main results, the authors did compare the proposed method with some of the label-efficient frameworks, but it looks like the comparison with [Meng et al. 2020; 2021] is missed out. It is important to understand how the proposed method compares to these specific works, especially regarding the practical aspects of annotation effort and the generalizability of the approach to different detector architectures, given that [Meng et al. 2020; 2021] also focus on weakly supervised 3D detection.

2. The hypothesis is not fully backed up: in the last paragraph of Sec 3 (pilot study), the authors concluded: "This phenomenon suggests that LiDAR-based detectors indeed only need a very limited number of accurate labels for geometry estimation. Massive data is only necessary for semantic learning." If I understand correctly, the pilot experiments only provide evidence to some degree in the first half, but the latter half "Massive data is only necessary for semantic learning" seems not fully grounded. An evaluation of how well the model can perform with different amounts of semantic labels could better support the claim. The pilot study only shows that geometry estimation is robust to the amount of data, but it does not directly demonstrate that semantic learning requires massive data, which is a separate claim that needs its own supporting experiments. For example, an ablation study varying the amount of coarse labels used for the classification/proposal stage would be necessary to validate this claim.

3. The study on the labeling costs is not fully grounded. In Sec 5.3, the authors claim "The average time cost of a coarse cluster label is only 14% of an accurate box label." In Sec 4.2, the authors also claim "In addition, it is also non-trivial for annotators to make an accurate center click." However, evidence is missing for these claims. Where does the "14% cost" come from? How much harder / more inaccurate is it for the annotator to click the center? Do you perform a user study with a reasonable number of annotators? How similar are the coarse labels from the annotators to the simulated coarse labels used in the experiments? I would suggest the authors include more details to back the claim. The lack of a user study makes it difficult to assess the practical viability of the proposed labeling scheme, and the absence of a comparison between human-annotated and simulated coarse labels raises concerns about the validity of the experimental results.

4. Presentation:

    a) I would suggest the authors be more specific about "semantic" and "geometry" from the beginning of the paper. If I understand correctly, by "semantic" the authors meant to coarsely identify object locations and types, and by "geometry" they meant to accurately regress the discovered object's location, dimensions, and heading. It is a bit confusing when reading the 3rd paragraph of the introduction. The terms "semantic" and "geometry" are used in a somewhat ambiguous way, and a more precise definition of these terms in the context of 3D object detection would improve the clarity of the paper.

    b) The writing in Sec 4 is somewhat confusing and unclear. Firstly, Figure 3 is not referred from anywhere in the main text and the caption is not self-contained, resulting in little help for understanding the idea. And Sec 4.2 is confusing: what does it mean by "assignment"? If I understand correctly after carefully reading into the latter parts, what the authors meant was that to properly supervise the proposal/classification stage for the detector. It is not self-contained in this sense, i.e. a reader without good knowledge of how these detectors are designed will have an even harder time understanding the method. The description of the method in Section 4 needs to be significantly improved, with clear explanations of each step and proper references to figures. The term "assignment" is not well-defined, and the connection between the proposed method and the underlying detector architecture is not clearly established.

### Questions
Please see the weaknesses section. Additionally,

1. In Table 4, it looks the PointContrast and the ProposalContrast have negative performance gains compared with training with 10% frames. But from the GCC-3D paper [Liang et al. 2021], the PointContrast usually can improve over the from-scratch baseline. The results reported here look inconsistent with previous literature. I am wondering how are these baselines trained?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work aims to improve the 3D object detection accuracy using cheap annotations. The authors are motivated by three distinct properties of LiDAR point clouds when designing their method, i.e., texture absence, scale invariance, and geometric richness. The following assumption is then made: *“A good detector needs massive semantic labels for difficult semantic learning but only a few accurate labels for geometry estimation”*.

In their endeavor to substantiate this assumption, an insightful pilot study is put forth. The study's essence is to underscore that extant 3D object detectors excel at deducing geometric information. This is highlighted by the observation that *“detector performance remains relatively stable across data sizes ranging from a mere 5% to a comprehensive 100%”*.

This work then proposes MixSup for conducting mixed-grained supervision on LiDAR-based 3D object detectors. MixSup utilizes massive cheaper cluster labels and a few more accurate box labels for label-efficient learning, where the cluster labels can be retrieved via three coarse clicks around the object corners. To further reduce human annotation effort, the authors use SAM to generate coarse instance labels from the camera images and then refine and map these labels to the point cloud.

Experiments on nuScenes, Waymo Open, and KITTI datasets verified the effectiveness of the proposed approach.

### Strengths
- This research is firmly rooted in a well-articulated motivation and logical progression.
- The proposed approach is intuitive and efficient in handling LiDAR-based 3D object detection.
- This paper is overall very well written and pleasant to read. Meanwhile, the authors made a promise of making their code open-source, which could facilitate future research in this task.

### Weaknesses
 - Several design decisions appear to be largely heuristic in nature. A number of assertions lack rigorous justification or analytical backing.
- The paper omits certain pivotal implementation specifics. This omission hampers a clear assessment of the proposed method's true efficacy.

### Questions
### Questions to the Authors

- **Q1:** The pilot study's design and outcomes could gain depth with a more granular breakdown of the experimental setup and subsequent insights. Furthermore, could you elucidate the term “data size”? Is it suggestive of the detectors' adaptability to varying “object/instance sizes”?

- **Q2:** The mechanics of the “clicking annotation” remain somewhat elusive. How were the annotators guided in executing this task? Was there a specific strategy adopted for different instance types? Was this manual labeling extended to all point clouds during training? If not, how were the crucial clicking points discerned? This reviewer believes a more thorough exposition on this subject would be beneficial in the rebuttal phase.

- **Q3:** The acronym “SAR” makes its debut in Sec. 4.3 without any contextual introduction. The authors are suggested to revise this.

- **Q4:** The narrative on connected components labeling (CCL) in Sec. 4.3 is quite succinct, leaving readers wanting more details on its practical implementation.

- **Q5:** It remains unclear which pre-trained semantic segmentation model was harnessed to create the 2D semantic masks. The possible implications of such a model leading to inadvertent data leakage need to be addressed. This information is indispensable to ensure that the experimental comparisons are grounded in validity.

- **Q6:** Several contemporary studies, including [R1], [R2], and [R3], harness SAM for segmenting objects from LiDAR point clouds. What distinct advantages does ACL offer when juxtaposed against these existing methodologies?

- **Q7:** Camera-LiDAR calibrations might not always achieve perfection. In scenarios where calibration discrepancies exist, there's potential for the SAR-derived coarse instance masks to be tainted with errors. The authors are suggested to consider conducting auxiliary experiments to probe whether calibration inaccuracies compromise the efficacy of the proposed method.

- **Q8:** This paper could be enriched with comparative analyses against some of the latest entrants in the domain of weakly and semi-supervised 3D object detectors.

- **Q9:** A minor formatting suggestion: For improved readability, perhaps anchor tables such as Table 2, Table 4, Table 5, Table7, and Table 10 to the top of their respective pages.

- **Q10:** This paper could benefit from having a standalone paragraph discussing the limitations and potential negative social impact of this work.

---

### Justification of the Rating

- The paper is overall well written with good insights. I am lean to upgrade the rating if the authors could resolve the concerns raised above.

---

### References
- [R1] D. Zhang, et al. “SAM3D: Zero-Shot 3D Object Detection via Segment Anything Model.” arXiv preprint arXiv:2306.02245.

- [R2] Y. Liu, et al. “Segment Any Point Cloud Sequences by Distilling Vision Foundation Models.” arXiv preprint arXiv:2306.09347.

- [R3] R. Chen, et al. “Towards Label-free Scene Understanding by Vision Foundation Models.” arXiv preprint arXiv:2306.03899.

### Soundness
3 good

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduce MixSup, a 3D object detection model that allow for mixed-grained supervision. The paper describe the phenomenon that a general point clouds detector rely heavily on coarse label for semantic recognition and require only few precise labels for object geometry. The method has been adapted for mainstream detectors and tested on various datasets, achieving nearly 97.31% of full supervised performance with reduced annotation.

### Strengths
The author's illustrations are well-done, and the article is written in a relatively coherent manner.

### Weaknesses
1. The illustration of distinct properties of point clouds compared to images in the introduction section seems not very relevant to the motivation and the concept of the study (The paper is not about multi-modality fusion).
2. The detail of pilot study is not quite clear. It seems that well-classified dataset contains only region-level point cloud. To let a spconv-based detector train on this dataset is not same as training on the point cloud scene, as the scene level point cloud can provide more context information.
3. The motivation "good detector needs massive semantic labels
for difficult semantic learning but only a few accurate labels for geometry estimationhis" is simply another way of expressing a common phenomenon in object detection, which is the high recall often contribute more on high average precision (AP).
4. The author proposed to create cluster-level supervision as the parallelogram of three click. If one can generate massive pseudo-boxes from clicks. Why not just using a region-based network (e.g. the second stage PointNet in LiDAR-RCNN) to refine these boxes as precise box-level supervision?
5. From author's experiment in Table 4, previous methods like MV-JAR can achieve very close performance to author's with 10% anotations. Considering author use massive cluster-level semantic supervision, does this indicate the massive semantic label is not that important?

### Questions
1. What is the difference between the settings of 10% boxes annotation and 10% frames annotation?
2. The author use cluster center to substitue the object center for semantic learning. I think this will introduce instability of training due to the cluster containing noise as it is generated from clicking/SAM model. I suggest author can perform another experiment by training the semantic head by leveraging voxel-to-point interpolation (eg. used in PVCNN, SASSD) and imposing point-level supervision.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
