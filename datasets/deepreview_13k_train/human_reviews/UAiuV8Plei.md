# FBSVP: Video Prediction Based on Foreground-Background Separation

- Decision: Reject
- Scores: 8, 3, 5, 3

## Abstract
Video prediction is the process of learning necessary information from historical frames to predict future video frames. 
How to focus and efficiently learn features from historical frames is a critical step in this process. For any sequence of video frames, 
the background changes little or remains almost constant, while the foreground changes significantly and is the main focus of our video prediction learning. 
However, current known video prediction learning methods do not consider how to utilize the different characteristics of the foreground and background to further improve prediction accuracy. 
To fully leverage the different characteristics of the foreground and background and enhance prediction accuracy, 
we propose a Foreground-Background Separation Video Prediction (FBSVP) model in this paper. 
Through the foreground and background separation module, historical video frames are separated into foreground and background frames. 
In the video prediction module, the foreground and background frames are predicted and learned separately. 
First, the features of historical frames are fused into the current frame through a historical attention fusion module using an attention mechanism. 
Then, the complementary temporal and spatial features are fused through a spatio-temporal fusion module. 
Finally, the learned foreground and background features are fused in the foreground and background fusion module to predict the final video frame. 
Experimental results show that our proposed FBSVP model achieves the best performance on popular video prediction datasets, demonstrating its significant competitiveness in this field.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors propose a  foreground-background separation video prediction. The proposed method named FBSVP consists of modules. First, an historical attention fusion module employs an attention mechanism. Second, temporal and spatial features are fused through a spatio-temporal fusion module. Third,a  foreground-background fusion module allows the authors to estimate the final video frame.

### Strengths
1) The paper is well organized and relatively well written.
2) The proposed method FBSVP is detailed and reproducible.
3) Experiments are conducted on various datasets such as KITTI and Caltech Pedestrian showing the superiority of FBSVP compared to ten previous methods.

### Weaknesses
1) There are missing references about key surveys in the field of background/foreground separation for novices.

M. Cristani, et al., “Background Subtraction for Automated Multisensor Surveillance: A Comprehensive Review”, EURASIP Journal on Advances in Signal Processing, 24 pages, Volume 2010, 2010.

B. Garcia-Garcia, et al., "Background Subtraction in Real Applications: Challenges, Current Models and Future Directions",  Computer Science Review, Volume 35, February 2020.

2) All over the paper, the authors cite two times as in the sentence "Wang et al. Wang et al. (2017) argued...". Please only let the second citation.

### Questions
It would be interesting to test the proposed method on the CDnet 2014 dataset. Indeed, it is a large-scale dataset used in MOD and it would be interesting if the method can help in this context. If yes, the authors have just to mention it.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes a video prediction model from the perspective of foreground and background separation. This practice may be novel but the motivation is not well related to the solution in this paper. The proposed solution is not novel in my view. The main reason for my rejection rating is the current version may be unfinished and needs major revisions.

### Strengths
1. Divide the video prediction goal into foreground and background parts and process them separately before aggregation.

### Weaknesses
1. The presentation of the entire paper needs to be carefully improved. For example: 
a) The latex citet and citep commands should be used properly.
b) Fig 1 is too small.
c) Figures 3, 4 and 5 express essentially the same process and should be illustrated with a clearer diagram. 
d) The visual comparisons are basically not distinguishable, especially in Figure 7 and 8.
e) Tables 1 to 4 are arranged in an order that does not match the content.
f) Writing and Grammar Issues.

2. The motivation and solution of the paper are not well related and do not clearly illustrate the differences with existing video prediction methods. From my point of view, the contribution is also insufficient and the proposed model components are not novel.

### Questions
1. Fonts differ from the official template.
2. In Table 2, we can find that compared to SimVPv2 the SSIM is better yet the PSNR is worse, which is an interesting observation that is worth analyzing.
3. Why the LPIPS metric is not used in the comparison experiments, but only in the ablation experiments.
4. Why is there no quantitative and qualitative comparison of training on the KITTI training set and testing on the KITTI test set? It has been done in existing methods including [1].

[1] A Dynamic Multi-Scale Voxel Flow Network for Video Prediction, CVPR 2023

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
A proper Foreground-Background Separation Video Prediction (FBSVP) model, has been proposed
in this paper, to enhance prediction accuracy in video prediction.

The features of historical (assumed to be past) frames are fused into the current frame through a historical attention fusion module using an attention mechanism. 

Then, the complementary temporal and spatial features are fused through a spatio-temporal fusion module. Finally, the learned foreground and background features are fused in the
F/G-B/G fusion module to predict the final frame.
Experimental results shows that the proposed FBSVP model achieves the
best performance on few benchmark video prediction datasets, demonstrating its
power.

### Strengths
Good set of results on benchmark datasets; beats few SoA processes
proper analytics given for the process.

Ablation studies also provided.

Method clearly explained.

### Weaknesses
State clearly the difference between the operations:
historical attention fusion
vs
Spatio-temporal fusion.

Difference between the terms information and feature (T & S) should be clarified - unless used interchangeably (specify so then).

What about the use of any probabilistic model in prediction, future may be uncertain (although GT data may provide unique answer) ?

Fig. 1- text inside processing blocks barely legible

Rightmost column of Fig. 7 - is mostly dark - not sure, what the authors want to show to readers.

Only for Kitti D/S the number of test frames is larger than training 10 -> 40, well not actually so, as I am pointing out to.

The real challenge lies in predicting:
(i)  the number of predicted frames is large enough (longer duration), compared to history/past;
(ii) HR frames from LR ones - did not find any such results

(i) is partly addressed, although better to show results on say:
train: 10 --> 20
and then
test 10--> 40 or 80/120 - what happens then.?



F/G-B/G separation is well-studied topic with vast literature, which is often difficult to cover in a Conf. paper.
However,
a few relevant papers which have not been cited, or performance not compared, are given below:

Y. Zhao, D. Luo, F. Wang, H. Gao, M. Ye and C. Zhu, "End-To-End Compression for Surveillance Video With Unsupervised Foreground-Background Separation," in IEEE Transactions on Broadcasting, vol. 69, no. 4, pp. 966-978, Dec. 2023, doi: 10.1109/TBC.2023.3280039.

Motion-aware Contrastive Video Representation Learning via Foreground-background Merging; Shuangrui Ding et. al; CVPR – 2022

Collaborative Video Object Segmentation by Foreground-Background Integration; Zongxin Yang, Yunchao Wei, Yi Yang; ECCV 2020; https://www.ecva.net/papers/eccv_2020/papers_ECCV/html/3385_ECCV_2020_paper.php
(although a later T-PAMI paper, has been cited).

Revisiting Foreground and Background Separation in Weakly-supervised Temporal Action Localization: A Clustering-based Approach; Qinying Liu, Zilei Wang, Shenghai Rong, Junjie Li, Yixin Zhang; Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV), 2023, pp. 10433-10443

ZBS: Zero-Shot Background Subtraction via Instance-Level Background Modeling and Foreground Selection; Yongqi An, Xu Zhao, Tao Yu, Haiyun Guo, Chaoyang Zhao, Ming Tang, Jinqiao Wang; Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2023, pp. 6355-6364

Motion-Aware Contrastive Video Representation Learning via Foreground-Background Merging; Shuangrui Ding, Maomao Li, Tianyu Yang, Rui Qian, Haohang Xu, Qingyi Chen, Jue Wang, Hongkai Xiong; Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2022, pp. 9716-9726

Mitigating and Evaluating Static Bias of Action Representations in the Background and the Foreground;  Haoxin Li, Yuan Liu, Hanwang Zhang, Boyang Li; Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV), 2023, pp. 19911-23.

A Comprehensive Study of Image Classification Model Sensitivity to Foregrounds, Backgrounds, and Visual Attributes;  Mazda Moayeri, Phillip Pope, Yogesh Balaji, Soheil Feizi; Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2022, pp. 19087-19097

### Questions
The term "historical attention fusion" needs more clarification.
Anyway, one needs to obviously learn/gather information features only from past frames, in any problem of video analytics.
So what is the reason of explicitly stating that using this term ? - unless there is significant meaning of something else - 
say, state change in past in latent space, say.

Line 168  vs 182 - ...subscript "s" denotes parameters related to spatial features...
vs
M^st for temporal features, where "s' is a superscript.

the SUM function - limits/range of indices (even if obvious) not specified in Eqns. 1 & 2.

Eqns. (4-5)  -  sigmoid of a feature vector (as argument to the function) ? - something missing there. Pl. clarify

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a video prediction method that trains by separating foreground and background. The method uses MOG2 to separate foreground from background and then predicts future frames by fusing historical frame information into the current frame. The authors validated the algorithm on datasets such as Moving MNIST and TrafficBJ.

### Strengths
1. The authors achieved some performance improvement on multiple datasets, such as TrafficBJ and KTH.
2. The authors conducted both qualitative and quantitative analyses of the proposed method's performance, producing some reasonably good visual results.

### Weaknesses
 1. The proposed idea of training by separating foreground and background has certain limitations. It is based on the assumption that backgrounds change infrequently while foregrounds change frequently (see Lines 014–016), which holds mainly for simple scenes, such as those in datasets like Moving MNIST and KTH used in this paper. In complex scenes, however, both the background and foreground can undergo significant changes, and foreground objects can vary greatly in size and spatial position within the frame (e.g., appearing larger when close, smaller when far). For scenes with complex backgrounds, foreground-background separation itself becomes challenging, and performing video prediction on separately processed foreground and background could be difficult. It would be helpful if the authors could analyze the applicability of this method in complex scenes or test on more challenging datasets such as UCF101 and Kinetics400.

 2. Video prediction can be considered a subtask of mainstream video generation, where the goal is to condition on the first few frames of a video to generate future content. The methods compared by the authors are all based on supervised video prediction, lacking comparisons with mainstream video generation methods like Stable Video Diffusion, OpenSora, and VideoCrafter. Current mainstream video generation methods tend to generalize better in handling complex scenes, with a broader applicability than the supervised methods commonly used in video prediction. It would be beneficial if the authors could compare their approach with mainstream video generation models on datasets representing more general and complex scenes.

 3. Miscellaneous: Figure 1 is too small, and the text is difficult to read. It would be better to use a larger image with adjusted font size for clarity.

### Questions
1. The core selling point of this paper is the prediction of video content by separately processing foreground and background. If the foreground-background separation algorithm is inaccurate, how does this affect the final result? Have the authors conducted any quantitative or qualitative analysis on the performance of the foreground-background segmentation algorithm and its impact on subsequent video prediction? For example, the authors could perform an ablation study using different foreground-background separation algorithms of varying accuracy.
2. I noticed that the captions for Table 1 and Table 2 indicate that video frame prediction is performed by conditioning on 10 frames to predict 10 frames (Table 1) or conditioning on 10 frames to predict 1 frame (Table 2). Have the authors tested results under other settings, such as conditioning on *n* frames to predict *m* frames, with various combinations of *n* and *m*? Testing with different combinations might provide a more comprehensive reflection of the method's effectiveness and robustness in video prediction.

### Soundness
2

### Presentation
2

### Contribution
2
