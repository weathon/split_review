# Spatial Matching Loss Function for Mass Segmentation on Whole Mammography Images

- Decision: Reject
- Avg Score: 3.67
- Scores: 5, 3, 3

## Abstract
Breast cancer is one of the cancer types with a high mortality rate among women, and mammography is one of the primary means to improve the identification of breast cancer. Deep-learning-based approaches are among the pioneering methods for mass segmentation in mammography images; in this category of methods, the loss function is one of the core elements. Most of the proposed losses aim to measure pixel-level similarities. While the hard-coded location information is provided in these losses, they mostly neglect to consider higher-level information such as relative distance, sizes, and quantities, which are important for mass segmentation. Motivated by this observation, in this paper we propose a framework for loss calculation in mass segmentation for mammography images that incorporates the higher-level spatial information in the loss by spatial matching between the prediction and the ground truth masks while calculating the loss. The proposed loss calculation framework is termed Spatial Matching (SM) loss. Instead of only calculating the loss over the entire masks that captures the similarity of the segmentation and the ground truth only at the pixel level, SM loss also compares the two in cells in a grid that enables the loss to measure higher-level similarities in the locations, sizes, and quantities. The grid size is selected according to each sample, which enables the method to consider the variation in mass sizes. In this study, Binary Cross Entropy (BCE) and Tversky are used as the core loss in experiments for the SM loss. AU-Net is selected as the baseline approach. We tested our method on the INbreast dataset. The results of our experiments show a significant boost in the performance of the baseline method while outperforming state-of-the-art mass segmentation methods.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a new loss function called spatial matching (SM) loss for mass segmentation on mammography images. The paper claims that spatial matching loss incorporates higher-level spatial information, such as distances, sizes, and quantities of the masses. The authors conduct mass segmentation experiments using the INbreast dataset, with AU-Net as the baseline, binary cross entropy loss, and Tversky loss as the core loss.

### Strengths
1. This paper goes beyond pixel-level segmentation losses and proposes a new way to incorporate high-level information. It creates a grid on the prediction and ground truth mask and aggregates the cell losses to reflect the mass distance, quantity and size information, which are important for mass segmentation in mammography images.
2. The authors give a good review of the recent mass segmentation methods for mammography images and loss functions for medical image segmentation and conduct experiments based on the recent mass segmentation network.

### Weaknesses
1. The paper’s main algorithm lacks explanation. In Section 2.3.2, the scale-based loss is to rescale the L_G with the scale ratio. However, how the definition of scale ratio can help overcome the size differences and the differences in the quantities of the masses is not explained at all. Specifically, the scale ratio is defined as the number of cells containing positive pixels in the prediction over the number of cells containing the positive pixels in the ground truth. This definition seems problematic, as a prediction with a much larger positive region than the ground truth will be heavily penalized, while a prediction with a much smaller positive region will receive a low penalty, which is counterintuitive. Thus, the paper’s argument to incorporate the size information is not supported.

2. The paper's contribution appears to be insufficient. The two methods proposed for aggregating cell losses seem straightforward. Moreover, the computation of the scale ratio in Section 2.3.2, which is based on the ratio of the number of cells, seems to achieve the same objective as simply computing the ratio of the number of pixels. The use of cells doesn't seem to offer any significant advantage over a direct pixel-based ratio, and the rationale for using cells instead of pixels is not clearly justified.

3. The paper contains some writing mistakes. Notably, the methodology section is incorrectly placed under "Related Work." Additionally, Eq. 5 and Eq. 8 are flawed, with Eq. 5 missing the indicator function in the numerator and Eq. 8 lacking summation in both the numerator and denominator. Furthermore, Fig. 1(b)'s caption mentions size and location differences, but the figure only depicts location differences. Lastly, Fig. 3(a) and (b) should be swapped.

4. The experiments conducted in the paper solely focus on one dataset, thereby inadequately supporting the claims made. Table 1 indicates that combining the scale loss and distance loss could lead to worse results compared to using either of them individually. In fact, with Tversky loss, the optimal outcome is achieved when the authors utilize the basic loss, which does not incorporate scale or distance. This raises concerns about the generalizability and effectiveness of the proposed combined loss.

### Questions
In Section 2.3.2, the scale ratio is defined as the number of cells containing positive pixels in the prediction over the number of cells containing the positive pixels in the ground truth. This would lead to high penalty when the prediction has much more positive regions than the ground truth, but lead to low penalty when the prediction has much less positive region than the ground truth. Does this make sense?

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposed a novel loss function, Spatial Matching (SM), for image segmentation applied to the problem of segmenting masses in mammography. The SM loss is based on evaluating a loss function over a grid within the mammogram image and then aggregating the local losses along with the overall image loss. An ablation study is performed to assess hyper-parameter choices and a comparison is made to existing state of the art methods on the INbreast dataset.

### Strengths
The paper identifies some of the limitations with conventional losses used such as binary cross entropy. Evaluation approach is appropriate for the problem at hand.

### Weaknesses
The paper is outlining a novel loss for segmentation motivated around the problem of mass segmentation in mammography. It could be argued that this is an artificial problem, in that the typical purpose of mass detection systems is to assist with the recall decision for screening mammograms either as an automated second reader or prompting system. Segmenting the masses itself is of less importance in clinical settings. No real attempt is made to outline why mass segmentation is of use.

As this paper focusses on the introduction of a novel segmentation loss, it would be helpful to see it evaluated on a range of datasets in other imaging domains to see if it has more broad utility. 

Images are resized to 256x256 meaning that the algorithm processes very low resolution images. Does this have any effect detection/segmentation of small lesions?

Object segmentation approaches (i.e. Mask RCNN) are not considered in the background literature or evaluation. 

Minor comments:

Figure 1 is hard to understand and doesn’t really do much to explain the limitations of BCE. 

Figure 2 is also challenging to understand. 

Figure 3 caption labels appear to be the wrong way round. 

Figure 4 caption doesn’t which is ground truth and which is predicted.

No discussion of object detection approaches are taken (i.e. RCNN type).

### Questions
Please clarify why object segmentation type approaches were not considered. (i.e. Mask-RCNN)

### Soundness
3 good

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors present a novel framework for calculating loss in the context of mass segmentation for mammography images. This approach incorporates higher-level spatial information by matching the spatial characteristics of predicted and ground truth masks during loss computation.

### Strengths
(1) The thoughtful design of the loss function is crucial for improving the performance of medical image segmentation models.

### Weaknesses
(1) The Spatial Matching (SM) loss is not sufficiently elucidated. In addition to providing algorithmic details and figures illustrating the method, a comprehensive description of the calculation process within the main text is warranted. Specifically, the precise mathematical formulation of how the spatial characteristics (distance, size, quantity) are incorporated into the loss calculation is missing. It is unclear how the different components of the spatial matching are weighted or combined to produce the final loss value. The description lacks the necessary detail to allow for independent implementation and verification of the method.
(2) Further experimentation with larger datasets is imperative to validate the method's robustness. The current experiments are limited to a single dataset, which may not be representative of the variability seen in real-world mammography images. This limits the generalizability of the findings. It is crucial to test the method on diverse datasets with varying image quality, lesion characteristics, and patient demographics.
(3) It is essential to include distance metrics, such as the Hausdorff Distance (HD), in the evaluation. The current evaluation is limited to Dice scores, which do not fully capture the spatial accuracy of the segmentation. HD is a more sensitive metric for evaluating the distance between predicted and ground truth boundaries, and its inclusion would provide a more comprehensive assessment of the method's performance.

### Questions
(1) While SM loss appears applicable to various medical image segmentation tasks, could you elaborate on its specific relevance and advantages in the context of mass segmentation?
(2) Could you provide a clear explanation for the significance of different colored cubes/circles within the proposed method?
(3) In the related work section, numerous segmentation losses are discussed. It would be beneficial to include comparative experiments to highlight the strengths and weaknesses of SM loss in relation to these existing methods.

### Soundness
1 poor

### Presentation
1 poor

### Contribution
1 poor
