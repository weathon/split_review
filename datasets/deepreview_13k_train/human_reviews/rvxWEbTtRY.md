# Training-Free Dataset Pruning for Instance Segmentation

- Decision: Accept
- Scores: 6, 6, 6

## Abstract
Existing dataset pruning techniques primarily focus on classification tasks, limiting their applicability to more complex and practical tasks like instance segmentation. Instance segmentation presents three key challenges: pixel-level annotations, instance area variations, and class imbalances, which significantly complicate dataset pruning efforts. Directly adapting existing classification-based pruning methods proves ineffective due to their reliance on time-consuming model training process. To address this, we propose a novel **T**raining-**F**ree **D**ataset **P**runing (**TFDP**) method for instance segmentation. Specifically, we leverage shape and class information from image annotations to design a Shape Complexity Score (SCS),  refining it into a Scale-Invariant (SI-SCS) and Class-Balanced (CB-SCS) versions to address instance area variations and class imbalances, all without requiring model training. We achieve state-of-the-art results on VOC 2012, Cityscapes, and MS COCO datasets, generalizing well across CNN and Transformer architectures. Remarkably, our approach accelerates the pruning process by an average of **1349$\times$** on COCO compared to the adapted baselines.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents a novel Training-Free Dataset Pruning (TFDP) method designed for instance segmentation tasks. Unlike existing dataset pruning techniques that focus on image classification and require time-consuming model training, TFDP leverages shape and class information from image annotations to prune datasets without any model training. The authors introduce a Shape Complexity Score (SCS), which is further refined into Scale-Invariant (SI-SCS) and Class-Balanced (CB-SCS) versions to address the challenges of instance area variations and class imbalances. This approach is intuitive and appears effective, with promising results.

### Strengths
- This approach is intuitive and appears effective
- This is the first work to address dataset pruning for instance segmentation.
- By eliminating the need for model training, TFDP aligns well with the goal of dataset pruning, which is to reduce resource consumption. And significantly accelerates the pruning process.
- The paper is well-structured, with clear and concise explanations supported by intuitive figures.

### Weaknesses
 - Given that instance segmentation tasks are often data-scarce due to the high cost of annotations, the immediate practical utility of dataset pruning in this domain may be limited.
- As prior work on instance segmentation pruning is lacking, the authors’ adaptation of classification-oriented methods may make baseline comparisons less compelling.

### Questions
Some thoughts and explorations:
1. Impact of Annotation Quality: The masks in the tested datasets are manually annotated, implying potential inaccuracies, especially for smaller objects. Since SI-SCS may assign lower scores to smaller objects due to annotation errors, it could lead to a bias towards pruning these objects. Given that the mean average precision (mAP) metric is averaged over instances, pruning smaller objects could disproportionately affect the overall mAP score.
2. Balancing Scale Diversity: While SI-SCS aims to make the score scale-invariant and CB-SCS balances class contributions, it would be interesting to explore whether incorporating additional mechanisms to balance the pruning of objects across different scales could further improve performance, particularly in scenarios where small objects are critical for overall accuracy.

### Soundness
3

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
4

### Summary
This paper introduces a training-free dataset pruning method specifically for instance segmentation for the first time. The method leverages object shape information to propose two scores, SI-SCS and CB-SCS, which are then used to select the most challenging samples from the dataset. The method outperforms training-based approaches across different network architectures and datasets.

### Strengths
The writing in the paper is clear and easy to understand.
The paper provides thorough experiments across multiple datasets and network architectures.

### Weaknesses
1. It is too simple to set the random sample selection strategy as the training-free baseline. Other intuitive selection methods should be compared as baselines to understand better why the proposed method is effective. For example, select images with the most objects or those containing rare categories.

2. The minimum training unit for instance segmentation is the object, not the image. In the proposed dataset pruning task for instance segmentation, is it appropriate to define the pruning ratio based on the number of images? It is suggested that the authors report
both image-level and instance-level pruning ratios for each experiment, and discuss how this affects the interpretation of the results.

3. Does the method show performance improvement over the baseline for all categories? It is suggested that the authors provide a category-wise performance breakdown, highlighting any categories where the proposed method underperforms the baselines, and analyzing potential reasons for these discrepancies.

4. In addition to the random strategy, results at high pruning rates should also include other training-based adaptation methods.

### Questions
The main concern is the rationality of the proposed task definition. As shown in Figure 6, the selected images predominantly contain a high number of objects, which implies that the actual object pruning rate could be smaller than the corresponding image pruning rate. The comparison between averaging image scores and summation image scores in the paper also supports this point. From this perspective, the comparison of the proposed method with other baseline methods may be unfair. The authors are suggested to:
1. Provide a detailed analysis of how the image-level pruning translates to instance-level pruning.
2. Discuss the implications of this discrepancy on the results and comparisons.
3. Conduct additional experiments by controlling the total number of object instances rather than images when comparing methods. This would help address the potential bias towards selecting images with many objects and provide a more equitable comparison.

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
The cropping method for classification tasks is ineffective in instance segmentation applications. The paper proposes a Training-Free Dataset Pruning (TFDP) method, which utilizes the shape and class information in image annotations to design a Shape Complexity Score (SCS) to address issues of instance region variation and class imbalance.

### Strengths
This paper proposes the Shape Complexity Score method around the simple P/A ratio concept. It introduces a relatively simple cropping method in the instance segmentation task. On the other hand, it significantly shortens the time for sample sorting in the cropping method. In addition, this method is more prominent in solving the instance segmentation task compared to previous methods. As mentioned above, the proposed method in this work has certain innovation, the paper framework is logically clear, and the integrity of the paper is relatively high.

### Weaknesses
1.It is suggested that the author add literature on different pruning methods in the instance segmentation task in the Introduction section or the Dataset Pruning section of the related work, or provide a relevant summary analysis.

2.It is suggested that detailed explanations be provided for formulas (5) to (12) in the paper, such as what does T represent in formula (5)?

3.The discussion and derivation of SI-SCS content in Section 3.3.2 of the text are not detailed enough, and it is recommended to add supplementary explanations.

4.The experimental part of the paper is not sufficiently comprehensive. 1) Important details regarding the training and inference stages are not provided in the experimental setup; 2) No detailed explanation is given for the poorer results in Table 4 after using SI. In addition, the authors have not provided a detailed analysis of the experimental results for all figures and tables in the experimental section.

5.The visualization results presented in Figures 6 and 9 can be intuitively observed to show that for some complex scenarios, when dealing with targets of more intricate shapes, or when addressing the local areas of the targets, the performance may be somewhat underwhelming.

### Questions
1. Combining theoretical and experimental results, we have considerable doubts about the use of P/A ratio and other metrics as Shape Complexity Scores in the instance-level score calculation in the paper. 

2. In SCS, the CB-SCS actually balances the number of instance objects in each diagram, but for datasets like COCO, the number of instances in some categories is very small. Does this potentially cause bias in the data distribution? Additionally, is the consumption of computing resources relatively high?

3. For the ablation experiments of SI and CB in SCS, it can be seen from Table 4 that the experimental results obtained by increasing SI or CB alone are not satisfactory. However, the authors did not provide relevant analysis in the paper. Why does increasing the module individually affect the performance of the original model? Why does the combination of the two result in better outcomes?

### Soundness
3

### Presentation
3

### Contribution
3
