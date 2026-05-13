# Grouplane: End-to-End 3D Lane Detection with Channel-Wise Grouping

- Decision: Reject
- Scores: 5, 6, 5

## Abstract
Efficiency is quite important for 3D lane detection due to practical deployment demand. In this work, we propose a simple, fast, and end-to-end detector that still maintains high detection precision. Specifically, we devise a set of fully convolutional heads based on row-wise classification. In contrast to previous counterparts, ours supports recognizing both vertical and horizontal lanes. Besides, our method is the first one to perform row-wise classification in bird’s eye view. In the heads, we split feature into multiple groups and every group of feature corresponds to a lane instance. During training, the predictions are associated with lane labels using the proposed single-win one-to-one matching to compute loss, and no post-processing operation is demanded for inference. In this way, our proposed fully convolutional detector, GroupLane, realizes end-to-end detection like DETR. Evaluated on 3 real world 3D lane benchmarks, OpenLane, Once-3DLanes, and OpenLane-Huawei, GroupLane adopting ConvNext-Base as the backbone outperforms the published state-of-the-art PersFormer by 13.6\% F1 score in the OpenLane validation set. Besides, GroupLane with ResNet18 still surpasses PersFormer by 4.9\% F1 score, while the inference speed is nearly 7$\times$ faster and the FLOPs is only 13.3\% of it.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper introduces anchor-based 3D lane detection utilizing channel-wise grouping features. Additionally, the authors propose a single-win one-to-one matching method that associates a grid belonging to vertical or horizontal lanes. The detection heads predict the existence, visibility, row index, lane category, and offset of lane points to grid centers. The paper provides extensive experimental results, demonstrating high performance on various lane detection benchmarks.

### Strengths
- Provide test results on various datasets and achieved high performances.

### Weaknesses
- The ultra-fast deep lane detection method has already introduced a hybrid anchor-based lane detection that predicts row-and-column anchors corresponding to lanes.
- It is interesting to note that Table 1 and Table 2 exhibit inconsistent results when using different backbone models. It would be nicer if the authors further investigated this issue.

Z. Qin, P. Zhang and X. Li, "Ultra Fast Deep Lane Detection With Hybrid Anchor Driven Ordinal Classification," in IEEE TPAMI, 2022.

### Questions
.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a end-to-end 3D lane detection from a single image. The proposed model is based on technical contributions: (1) a splitting strategy that build several groups of features to represent a line, (2) two groups of heads to recognize, in the bird-eye-view (BEV), horizontal and vertical lines. The resulting model is evaluated on three public benchmarks and outperform existing models.

### Strengths
The paper is nicely written and easy to read. The main contribution, to my point of view, consists in splitting the BEV features into two groups of candidates: horizontal candidates and vertical candidates. Each group has 6 heads to predict existence confidence, visibility, category, row-wise classification index, x-axis offset, and z-axis offset. Since the proposed model splits the group of candidates in horizontal and vertical, the authors proposed an adapted technic called single-win one-to-one matching (SOM) to match each candidate with the training labels.

### Weaknesses
In the experimental part, GROUPLANE is evaluated on three datasets. The selected baseline model is PersFormer (described as the best published model). Can you give details on this choice? Regarding the benchmark webpage, it seems that the best 2022 model is 58% F1 score and that PersFormer is currently ranked 9. The resulting figure 2 is not fair and should be changed with new models.
Moreover, can you add the two following references (ranked 1 and 2) from ICCV2023: 
LATR: 3D Lane Detection from Monocular Images with Transformer
PETRv2: A Unified Framework for 3D Perception from Multi-Camera Images

In the ablation study, the authors compare the Horitontal/Vertical grouping strategy with only a vertical strategy. The proposed strategy increases about 5% the F1 score. It should be interesting to give information on the horizontal/vertical ratio of lines of the dataset. Moreover, it could be interesting to split the results into vertical/horizontal lines.

### Questions
Can you give details on the choice of PersFormer as the baseline for figure 2 and table 3?
Can you give information on the horizontal/vertical ratio of lines of the dataset used for table 6?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents a novel convolutional neural network for end-to-end 3D lane detection. First, the approach splits BEV features into vertical and horizontal groups along the channel dimension. Then, group convolution is applied to both vertical and horizontal groups to extract further features. During the training phase, the authors propose a SOM strategy to match ground truth and predictions. Finally, 3D lanes are detected by performing row-wise classification. Notably, this method achieves state-of-the-art performance in the 3D lane detection task on 3 benchmarks, OpenLane, Once-3DLanes, and OpenLane-Huawei.

### Strengths
1. Idea seems fundamentally sound.
2. Spliting BEV feature for vertical and horizontal lane detection would be valuable, espeically when model is deployed on an edge device.
3. Paper is well written and very easy to read.

### Weaknesses
1. Simply dividing each group into N outputs limited the max output lane number of the model.
2. SOM strategy is simple yet effect, details are not well explained or even missing, eg. the matching cost definition.

### Questions
1. It is unclear what will happen when both the vertical and horizontal heads match the ground truth (GT). The paper does not provide a clear explanation or analysis of this scenario.
2. The paper does not address how to ensure stable predictions. It raises concerns about the possibility of different heads predicting the same lane at different time and one of them is not the optimal prediction. 
3. Can not find the matching cost definition or loss functions in Section 3.4.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
