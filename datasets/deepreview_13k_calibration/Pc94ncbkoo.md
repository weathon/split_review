# $A^2$-DP: Annotation-aware Data Pruning for Object Detection

- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 5, 6, 3

## Abstract
As the size of datasets for training deep neural networks expands, data pruning has become an intriguing area of research due to its ability to achieve lossless performance with a reduced overall data volume. However, traditional data pruning usually demands complete dataset annotations, incurring high costs. To tackle this, we propose an innovative Annotation-Aware Data Pruning paradigm tailored for object detection, dubbed
as $A^2$-DP, which aims to reduce the burdens of both annotation and storage. Our approach, consisting of two phases, integrates a hard sample mining module to extract crucial hidden objects, a class balance module to identify important objects in rare or challenging classes and a global similarity removal module that enhances the elimination of redundant information through object-level similarity assessments.
Extensive experiments on 2D and 3D detection tasks validate the effectiveness of the $A^2$-DP, consistently achieving a minimum pruning rate of 20\% across various datasets, showcasing the practical value and efficiency of our methods.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces A2-DP, an Annotation-Aware Data Pruning paradigm for object detection, which aims to reduce the annotation and storage burdens associated with large datasets. A2-DP employs a two-phase framework that includes hard sample mining to extract critical hidden objects, a class balance module to identify important objects in rare or challenging classes, and a global similarity removal module to eliminate redundant information through object-level similarity assessments. The method has been extensively tested on 2D and 3D detection tasks, consistently achieving a minimum pruning rate of 20% across various datasets without compromising performance, demonstrating its practical value and efficiency.

### Strengths
1. This paper focuses on data efficiency for object detection, which is very important for current data-scarce computer vision tasks because the annotations and storage for object detection are both costly and burdensome. 
2. The proposed method seems to be effective under different pruning rate, and has been deomistreted on both 2D and 3D object detection benchmarks.
3. To evaluate the similarity in object level is reasonable because the object detection model typically focuses more on objects instead of scenes.

### Weaknesses
1. The definition of the problem in this work is not clear enough. Although the authors attempt to use the concepts of data pruning, the problem is an active learning problem. The only difference between them is that the portion of labeled samples in active learning is smaller than that in the proposed method. Therefore, there is no essence difference between them. Moreover, the problem statement in section 3.1 is also incomplete in describing the problem of this paper.
2. Lack of novelty. The proposed method leverages the uncertainty and class-balanced weights are very common in the data selection for object detection. Specifically, the aggregation of object-level uncertainty, while presented as a novel approach, is a common practice where object-level uncertainties are often used to derive an overall image uncertainty. Similarly, dynamic class-balanced weighting, while effective, is a standard technique for addressing class imbalance issues in object detection datasets.
3. The presentation needs to be improved. It would be better to switch the order for Figure 2b and Figure 2a according to their reference in the main text. Some math definitions are also not well defined, e.g., the $O$, $o$, and $O_i$.
4. As the paper states, the proportion of data is calculated based on the number of annotated boxes rather than images. The authors may provide specific descriptions of the procedure. The images usually contain different numbers of objects, how to give an exact 20% data according to the number of objects?

### Questions
1. Any other state-of-the-art active learning methods be used for comparison? The compared methods seem to be slightly outdated for the year 2024.
2. It seems that the model trained on only 80% COCO data can outperform that trained on the full data. What is the reason behind this? Does it mean the redundancy data in COCO would have a negative impact on the model?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces Annotation-Aware Data Pruning ($A^{2}\text{-}DP$), an approach for object detection aimed at reducing annotation costs and storage requirements while maintaining model performance. $A^{2}\text{-}DP$ leverages a hard sample mining module to capture hidden objects, a class balance module to prioritize rare or challenging classes and a global similarity removal module to eliminate redundant data through object-level similarity analysis. Experiments on both 2D and 3D detection tasks demonstrate at least a 20% pruning rate.

### Strengths
- Dataset pruning for object detection addresses an important but under-explored area in deep learning.

- The approach of pruning datasets without needing full annotations is impressive and offers practical advantages.

### Weaknesses
 - The technical novelty of this paper seems limited, as several applied modules and concepts—such as uncertainty, class-wise, and object-level learning—have already been explored in [1, 2]. This paper appears to primarily extend [1] to a wider range of datasets, including 3D object detection. However, the reviewer may be overlooking some unique aspects and welcomes clarification on this point.

 - In Section 3.3.1, the authors propose a softmax-based aggregation method to address hard false positives in their hard sample mining scheme. However, it’s unclear how softmax uncertainty scores would address this issue effectively, as they might increase the probability distribution weighting toward the negative class. A visual illustration demonstrating this approach’s effectiveness could clarify its impact.

### Questions
Since one of the main claims of this work is to reduce the need for a fully annotated dataset for pruning, is it appropriate to compare this approach directly with semi-supervised object detection methods [3, 4]? Moreover, how this method compares to semi-supervised approaches in terms of annotation requirements and computational efficiency. What are the potential advantages or disadvantages of the proposed method compared to semi-supervised techniques for object detection?

[3] Xu, Mengde, et al. "End-to-end semi-supervised object detection with soft teacher." Proceedings of the IEEE/CVF international conference on computer vision. 2021.

[4] Zhang, Jiacheng, et al. "Semi-detr: Semi-supervised object detection with detection transformers." Proceedings of the IEEE/CVF conference on computer vision and pattern recognition. 2023.

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
4

### Summary
This paper has two main phases: initial model training and advanced data refinement. In the first phase, a portion of the data is annotated and used to train an initial model, which then selects the most informative samples based on uncertainty and class balance. Redundant samples are further removed using object-level similarity analysis. The second phase further refines the data using hard sample mining, class balance optimization, and redundancy reduction. 
So this paper:
1.Introduced A2-DP, a method that effectively reduces data and annotation volume for object detection without compromising performance.
2.Used entropy-based uncertainty and object-level similarity to choose informative samples and eliminate redundant data.
3.Showed significant pruning rates (at least 20%) across various datasets, demonstrating A2-DP's practical benefits in reducing data requirements for training high-performance models.

### Strengths
1.A2-DP adjusts its pruning strategy based on the data, using both uncertainty and class balance, ensuring that the model focuses on the most valuable data, leading to improved generalization.
2.The authors validated A2-DP on multiple datasets, including both 2D and 3D object detection, achieving a consistent pruning rate of at least 20%. This scalability shows the method's generalizability across different applications and data types.

### Weaknesses
1.The method requires additional training for the initial model, which could increase training costs. The authors should clarify the exact training cost for the initial model. Additionally, an ablation study should be added to compare their method with other advanced methods under the same training cost conditions.
2.In line 502, "conducted" should be replaced with "conduct."
3.The explanation of how the budget parameter (B) works, along with the threshold parameter, is unclear in the algorithm and should be elaborated.

### Questions
refer to the weakness for the rebuttal

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The article presents a novel Annotation-Aware Data Pruning (A²-DP) method aimed at reducing the annotation and storage costs in object detection tasks. The method consists of two phases: Initial Model Construction: This phase involves training a basic object detection model without complete annotations by utilizing techniques such as hard sample mining, class balance adjustment, and global similarity removal. Advanced Data Refinement: This phase focuses on mining hard-to-detect key samples from the previously constructed model and further eliminating redundant data. Finally, the authors provide extensive experiments on both 2D and 3D detection tasks to show the effectiveness of the propsoed method.

### Strengths
- The topic is meaningful. Labelled data, especially the 3D labelled,  is kind of valuable resouces for the current deep learning community. This work provide a data pruning method for both 2D/3D object detection.

- The proposed method is reaonable.

### Weaknesses
 - Limited experiments and inappropriate/unclear experimental setting. It is not clear that what detectors/backbones/experimental settings are used in the experiments. Current numbers are significantly lower than the performance of SOTA methods, and can not support the claims and conclusions. To demonstrate the effectiveness of the proposed method, the author should provide the experimental results of **different object detectors and different backbones with and without the proposed method**. The current experiments are ambiguous and cannot draw effective conclusions。

- Inappropriate ablation study. VOC is out-of-dated dataset for object detection, and the ablation should be conducted on COCO dataset.

- The presentation should be further improved.

### Questions
Please see the weaknesses.

### Soundness
3

### Presentation
2

### Contribution
3
