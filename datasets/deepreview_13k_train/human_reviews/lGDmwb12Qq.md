# The Sampling-Gaussian for stereo matching

- Decision: Reject
- Scores: 3, 6, 5

## Abstract
The \textit{soft-argmax} operation is widely adopted in neural network-based stereo matching methods to enable differentiable regression of disparity. However, network trained with \textit{soft-argmax} is prone to being multimodal due to absence of explicit constraint to the shape of the probability distribution. Previous methods leverages Laplacian distribution and cross-entropy for training but failed to effectively improve the accuracy and even compromises the efficiency of the network. In this paper, we conduct a detailed analysis of the previous distribution-based methods and propose a novel supervision method for stereo matching, \textit{Sampling-Gaussian}. We sample from the Gaussian distribution for supervision. Moreover, we interpret the training as minimizing the distance in vector space and propose a combined loss of L1 loss and cosine similarity loss. Additionally, we leveraged bilinear interpolation to upsample the cost volume. Our method can be directly applied to any \textit{soft-argmax}-based stereo matching method without a reduction in efficiency. We have conducted comprehensive experiments to demonstrate the superior performance of our \textit{Sampling-Gaussian}. The experimental results prove that we have achieved better accuracy on five baseline methods and two datasets. Our method is easy to implement, and the code is available online.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposed ‘Sampling Gaussian’ as supervision for disparity estimation. Moreover, this paper also studied the issues of using soft-argmax for depth estimation. They also propose a combined loss for disparity estimation. The proposed method is evaluated on the KITTI and SceneFlow datasets to demonstrate their performance.

### Strengths
The paper is tackling an important problem in computer vision.

### Weaknesses
-	Writing. The paper needs significant improvement in writing. The idea is not explained well in the paper. We all agree that soft-argmax cause issues in estimation especially for multimodal distribution. However, there is no such analysis, namely discussions on when the multimodal distribution will happen. It just explains in a way that the soft-argmax will not work well if there will be multimodal distribution.
-	There are a lot of typos in the paper: 
For example: Line85 Taken - >
Line 180 analysis -> analyse
Line 212-213: to calculates -> calculate
Line 289-290: to further to -> to further.


- Section 3.2 (a) and (b) are really not clear to the reviewer. Please write Eq. (5) properly. What is \exp^{z^*}? Could more details be provided for Eqn. (7)? 
 - Please provide more details in Section 4.1 and 4.2. Please write Eq.(8) properly.
 - Please highlight the differences of the Visualisation in Fig. 6.

The main concern about this paper is the big issues in writing. The reviewer cannot link the proposed method with the argument in the paper. The equations presented in the paper are not well explained. While the results look promising, the paper needs significant improvement before its acceptance.

### Questions
Please address the concerns listed above.

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper proposes Sampling-Gaussian, a novel supervision method for stereo matching that uses Gaussian distribution sampling. The proposed method can replace the widely used soft-argmax operation, overcoming the issue of multimodal distributions and improving performance. Based on Gaussian distribution, this paper introduces a combined loss function that integrates L1 loss and cosine similarity loss. This proposed method can be integrated into any soft-argmax-based stereo matching method and outperforms five baseline methods across two datasets.

### Strengths
1. The proposed method is straightforward and easy to follow.

2. The motivation is good, as the authors clearly identify the shortcomings of the existing softmax operation and propose sampling from the Gaussian distribution for supervision.

3. The performance improvement is particularly significant in several well-known softmax-based methods, such as PSMNet and MSN2D.

### Weaknesses
1. I think the innovation of this paper is limited. In this paper, I think the main improvement comes from taking the disparity range below 0 into consideration, eliminating the negative impact on the scheme based on distributed supervision in the disparity range below 0. But with a fixed extended disparity range, i.e., 16, I think it's hard to fit the distribution of the scenarios. Do I need to set a new extended range to fit the distribution range in a new scenario? I think this is an offset that is highly relevant to the scene.

2. I think the improvement of this method over SOTA methods such as IGEV is small. Does this mean that there is no multi-peak distribution problem in iterative optimization schemes similar to IGEV? I suggest that the author analyze the distribution of disparities produced by IGEV compared to other baselines to determine why the effect is not significantly improved on IGEV. And I have another concern. Currently, SOTA schemes are basically iterative frameworks similar to IGEV. Is it difficult for Sampling-Gaussian to significantly improve such frameworks?

### Questions
1. Can the proposed Sampling-Gaussian be applied to more recent methods like PCWNet, CFNet, and GANet to enhance their performance? Perhaps the resulting models could achieve state-of-the-art results.

2. The authors claim that the regression near the endpoints is overlooked (Line 110), which is an important point. To validate the effectiveness of the proposed method, it would be beneficial for the authors to provide results showing improvements in the regions near the endpoints, such as for disp < 10 px and disp > 180, or other relevant divisions.

3. It seems that the proposed method does not show significant improvements on IGEV-Stereo. Could the authors provide an explanation for this?

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
4

### Summary
This paper presents a training method to solve the multimodal problem for stereo matching. Specifically, this paper propose a Gaussian distribution-based supervision method with combined loss, which can be directly applied to any soft-argmax-based methods without extra cost during inference. Experimental results show that performance can be improved on multiple baselines.

### Strengths
The method in this paper is universal and has a significant improvement effect on some baselines.  And the cross-domain generalization result in table 6 also proves the transferability of the method.

### Weaknesses
1. I think the innovation of this paper is limited. In this paper, I think the main improvement comes from taking the disparity range below 0 into consideration, eliminating the negative impact on the scheme based on distributed supervision in the disparity range below 0. But with a fixed extended disparity range, i.e., 16, I think it's hard to fit the distribution of the scenarios. Do I need to set a new extended range to fit the distribution range in a new scenario? I think this is an offset that is highly relevant to the scene.

2. I think the improvement of this method over SOTA methods such as IGEV is small. Does this mean that there is no multi-peak distribution problem in iterative optimization schemes similar to IGEV? I suggest that the author analyze the distribution of disparities produced by IGEV compared to other baselines to determine why the effect is not significantly improved on IGEV. And I have another concern. Currently, SOTA schemes are basically iterative frameworks similar to IGEV. Is it difficult for Sampling-Gaussian to significantly improve such frameworks?

### Questions
1. This extended disparity range is, in principle, scene dependent because it determines the offset of the distribution. The author's training on both sceneflow and kitti uses 16 as the offset. Will this fixed offset of 16 still work in a scene like middlebury with large disparity (up to 800)? Do I need to reset an offset for retraining?
2. I think the improvement of this method over SOTA methods such as IGEV is small. Do Sampling-Gaussian fail to bring significant improvements to frameworks based on iterative optimization? What is the reason for this? This is worth analyzing. I think frameworks based on iterative optimization are not as strongly dependent on soft-argmax, which is one of the possible reasons.

### Soundness
3

### Presentation
3

### Contribution
2
