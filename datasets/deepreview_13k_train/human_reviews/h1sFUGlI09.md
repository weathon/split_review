# DFormer: Rethinking RGBD Representation Learning for Semantic Segmentation

- Decision: Accept
- Scores: 3, 6, 8

## Abstract
We present \nMethod{}, a novel RGB-D pretraining framework to learn transferable representations for RGB-D segmentation tasks.
\nMethod{} has two new key innovations:
1) Unlike previous works that encode RGB-D information with RGB pretrained backbone, we pretrain the backbone using image-depth pairs from ImageNet-1K, and hence the \nMethod{} is endowed with the capacity to encode RGB-D representations; 
2)  \nMethod{} comprises a sequence of RGB-D blocks, which are tailored for encoding both RGB and depth information through a novel building block design.
\nMethod{} avoids the mismatched encoding of the 3D geometry relationships in depth maps by RGB pretrained backbones, which widely lies in existing methods but has not been resolved.
We finetune the pretrained \nMethod{} on two popular RGB-D tasks, \ie RGB-D semantic segmentation and RGB-D salient object detection, with a lightweight decoder head.
Experimental results show that our \nMethod{} achieves new state-of-the-art performance on these two tasks with less than half of the computational cost of the current best methods on two RGB-D semantic segmentation datasets and five RGB-D salient object detection datasets.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
In this paper, the authors propose an RGB-D pretraining framework for RGB-D semantic segmentation and salient object detection (SOD). First, they use an off-the-shelf depth estimator to generate depth maps for ImageNet-1K. Then, they use the image-depth pairs from ImageNet-1K to pretrain the backbone. Next, they insert an existing head on the backbone and then finetune the model on the RGB-D semantic segmentation and salient object detection datasets.

### Strengths
1.	To improve the model performance, the authors pretrained the backbone on ImageNet-1K with image-depth pairs.
2.	The authors conducted experiments on two RGB-D segmentation tasks.

### Weaknesses
1. The novelty and contributions are too limited. 
First, the proposed RGB-D block slightly modifies popular techniques, i.e., self-attention mechanism (Vaswani et al., 2017), depth-wise convolution, and attention weights (Hou et al., 2022), and combines them to fuse RGB and depth features. Second, the design of the RGB-D block follows the widely used idea in SOD, i.e., global and local information fusion. Third, the decoder directly uses the existing head from SegNext (Guo et al., 2022a) without any novel design. Thus, the contribution only comes from the pretraining idea, which is limited.

2. The authors missed some related methods [1-4] for comparison.

[1] Visual Saliency Transformer. ICCV 2021.

[2] 3-d convolutional neural networks for rgb-d salient object detection and beyond. TNNLS 2022.

[3] Bi-Directional Progressive Guidance Network for RGB-D Salient Object Detection. TCSVT 2022.

[4] UCTNet: Uncertainty-aware cross-modal transformer network for indoor RGB-D semantic segmentation. ECCV 2022.

3. To demonstrate the effectiveness of the pretrained backbone, the authors should replace the previous backbone in the compared methods with the proposed one to see whether improvements can be achieved.

4. The authors ignore existing pre-training methods [5, 6] for discussion and comparison.

[5] RGB-based Semantic Segmentation Using Self-Supervised Depth Pre-Training

[6] Self-Supervised Pretraining for RGB-D Salient Object Detection. AAAI 2022.

5. Some widely used RGB-D SOD benchmark datasets [7-9] are also ignored.

[7] Depth-induced multi-scale recurrent attention network for saliency detection. ICCV 2019.

[8] Learning selective mutual attention and contrast for rgb-d saliency detection. TPAMI 2021.

[9] Saliency detection on light field. CVPR 2014.

### Questions
Please see weaknesses.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper introduces a RGB-D pretraining framework for transferable representations in RGB-Depth segmentation tasks. In the proposed methods DFormer, the RGB-depth backbone is pretrained using RGB-D pairs from ImageNet-1K, with the aim of enabling effective encoding of RGB-D information. It incorporates a sequence of RGB-D blocks designed for optimal representation of both RGB and depth data.

### Strengths
The proposed RGB-D pretraining framework can be used to solve the representation distribution shift between RGB and the depth information, and to increase the performance of RGB-D representation. 

A building block is proposed to perform RGB and depth feature interaction early in the pretraining stage, thus it is possible to reduce the interaction outside the backbone in the fine-tuning stage.

### Weaknesses
The comparison of using RGB-Depth pretraining on other previous works is missing. The most improvement seems from the join pretraining by using additional depth information as compared to previous methods.

The analysis of the depth generation is less included. Only one depth estimation method is used to generate the depth image for ImageNet. 

There is generalization limitation in combining two modalities for pre-training. The performance of pre-training or fine-tuning on downstream tasks seems to be highly dependent on the generation or estimation of another modality besides RGB.

### Questions
What is the effect of using different depth estimation models? How effective is the accuracy of depth estimation for RGBD model pre-training, and will there be accumulation of errors?

How is the comparison between the fusion building block and the fusion module proposed in previous methods, such as cmx? Also, do the authors try to perform RGB-D pretraining for other methods, so as to perform a more comparable setting? 

How does the DFormer perform if only RGB pretrain + D initialization for finetuning?

How is the effect and how is improvement from the light hamburger decoder in the proposed model? Whether the authors try to use other decoders? 

Why to perform feature interaction between RGB and depth information in the last two stages?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper presents an RGB-D scene understanding framework with RGB-D pertaining weights. Two tasks are considered, including RGB-D semantic segmentation and salient object detection. A global awareness attention module and a local enhancement attention module are designed. RGB-D pre-training is performed on ImageNet-1K with estimated depth data. The proposed model achieves state-of-the-art performance and maintains good efficiency compared to existing works. As shown in Table 3, the benefit of using RGB-D pre-training is significant. Extensive ablation studies and parameter studies are conducted.

### Strengths
1. This work is one of the first works to consider RGB-D pertaining to enhance RGB-D scene understanding. The results show that the benefit of RGB-D pretraining is significant.
2. The proposed model is highly efficient compared to existing works.
3. Table 1 presents a nice way of comparing with code-public-available works.
4. The paper is overall well-written and nicely structured.

### Weaknesses
1. MultiMAE also uses RGB-D pretraining. However, in this work, a different depth estimation model is used. Would it be nice to provide a more fair comparison by using the same depth estimation model as MultiMAE to produce ImageNet depth data?  It is unclear how much the choice of depth estimation impacts the final performance, and using a consistent depth estimation method would isolate the impact of the proposed architecture.
2. Again regarding fairness, the RGB-D pertaining is based on ImaegNet RGB-D data, and the depth estimation leverages important knowledge learned on other datasets. However, this knowledge is not used by existing RGB-D segmentation works like CMX. This discrepancy in pretraining data and methodology could be more thoroughly discussed. The advantage gained from the depth estimation model's pretraining should be acknowledged and its impact on the overall results should be analyzed.
3. Will the pretraining weights be released? Would the ImageNet depth data be released? This could be discussed. The lack of publicly available resources hinders reproducibility and further research based on this work.
4. In the introduction, it was argued: "the interactions are densely performed between the RGB branch and depth branch during
finetuning, which may destroy the representation distribution". Do you have any observations to support this argument? E.g., some destroyed distributions or feature maps could be analyzed. The claim about representation distribution destruction needs more concrete evidence, such as visualization of feature maps or statistical analysis of feature distributions before and after fine-tuning.
5. There are still some writing mistakes. E.g., "we conduct a depth-wise convolution" should be "We conduct a depth-wise convolution". "Our DFormer perform better segmentation accuracy than the current state-of-the-art" should be "Our DFormer produces higher segmentation accuracy than the current state-of-the-art". 
6. ACNet (ICIP 2019) should be added to Table 1.
7. How to scale to other modalities like RGB-thermal, RGB-LiDAR, X-Y-Z data, or even more modalities and datasets? This is not well discussed in the future work section. Different from depth data which can be produced by robust depth estimation models, it is harder to have large-scale thermal and LiDAR datasets for pertaining. This can be better discussed. The limitations of the current approach in handling diverse modalities should be addressed, and potential solutions for generalizing to other modalities should be explored in more detail.
8. As the main contribution lies in the study of RGB-D pertaining, more and recent advanced pertaining strategies could be compared and discussed. The main technical design lies in the fusion blocks, but there are no specific pertaining designs. Please discuss this and assess more pertaining choices. The paper should delve deeper into the specific design choices related to pretraining, and compare the proposed approach with other advanced pretraining strategies.

### Questions
The proposed model is highly efficient and it has large gains thanks to the RGB-D pertaining.  If the RGB-D pertaining strategy is applied to heavier state-of-the-art RGBD segmentation models like CMX and CMNeXt, how much gain can be achieved? If it is possible, this could be assessed and would help provide a fairer comparison.

Fig. 11 shows that the proposed module is sophisticated. Would it be nice to provide more detailed ablations to study other design choices based on this module architecture?

Sincerely,

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
