# Binarized Convolutional Neural Networks with Channel Quadrupling and Smooth Downsampling

- Decision: Reject
- Scores: 5, 6, 6, 5, 5

## Abstract
This paper proposes novel binarized convolutional neural networks (BCNNs) named **QB-Net** and **QSB-Net**, specifically designed to **Q**uadruple the number of channels and incorporate a so-called **S**mooth downsampling in **B**CNNs for low-cost mobile environments. The proposed models combine FP32 depthwise separable (DS) convolutions with binarized $1 \times 1$ pointwise convolutions, offering reduced computational costs in the pointwise convolutions. To enhance the degraded performance of the above naive combination, the proposed models start with a small number of channels in shallow layers and expand them during downsampling by a factor of four, effectively managing model complexity in the downsampling. The proposed model structure maintains low computational costs in the shallow blocks and increases model complexity in the deep blocks, providing a wider dynamic range to manage information in the frequency domain. As a result, the proposed models overcome the limitations of existing BCNNs, delivering improved performance while reducing the total computational costs. For further performance enhancements, we propose a novel smooth downsampling with heightwise and widthwise sequential downsampling steps, doubling the number of channels at each step. Besides, we show that the channelwise self-attention (SE) is applicable with minimal additional computational costs in the proposed models. Besides, multiple binarized convolutions in the fully-connected (FC) layer reduce storage costs without requiring 8-bit quantized convolutions. Experimental results demonstrate the efficiency of the proposed models in terms of performance, computational costs, and inference latency on real hardware. Notably, the QSB-Net-Large with SE achieve 71.2\% Top-1 accuracy on ImageNet-1K and 69.2 mean intersection over union (mIoU) in the semantic segmentation on the PASCAL VOC dataset, outperforming other counterparts.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces novel binarized convolutional neural networks (BCNNs), QB-Net and QSB-Net, designed to enhance performance in low-cost mobile environments by quadrupling the number of channels and incorporating smooth downsampling. The models combine FP32 depthwise separable (DS) convolutions with binarized 1×1 pointwise convolutions to reduce computational costs. The proposed structure starts with a small number of channels in shallow layers and expands them during downsampling, managing model complexity effectively. Experimental results demonstrate improved performance.

### Strengths
1. The proposed QB-Net and QSB-Net models offer a new approach to channel expansion and downsampling in BCNNs, which is a  contribution to the field of model compression and quantization.
2. The paper demonstrates substantial performance improvements over existing BCNNs, which is a strong contribution for mobile and edge computing applications.
3. The paper provides a detailed explanation of the technical methods, including the new structure for channel quadrupling and smooth downsampling techniques.

### Weaknesses
1. The paper may be seen as more of an engineering solution rather than a contribution to the foundational knowledge of the field.
2.  Although the paper claims reduced computational costs, the quadrupling of channels and the introduction of smooth downsampling could potentially increase the model's complexity, especially in deeper layers. This could lead to higher computational requirements that may offset the benefits of reduced pointwise convolution costs, especially the additional connections..
3. The abstract mentions improvements in inference latency on real hardware, but it does not discuss the energy efficiency of the models. For mobile environments, energy consumption is a critical factor, and the proposed models' impact on this aspect should be evaluated.

### Questions
Mixed use of fp32 and binary value will increase the complexity of hardware design, how to solve it?

### Soundness
2

### Presentation
2

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
This paper introduces QB-Net and QSB-Net, novel binarized convolutional neural network architectures specifically designed for mobile environments. It designed "channel quadrupling" that starts with fewer channels in shallow layers and expands them four-fold during downsampling, along with a "smooth downsampling" technique.

### Strengths
1. Provides a fresh approach to BCNN design, moving beyond traditional methods.

2. The authors conduct real hardware testing on both Raspberry Pi 4B and Samsung Exynos processor, and the results demonstrate real-world applicability for mobile/edge devices. This is good.

### Weaknesses
1. A major concern is that the performance improvement is marginal or null when compared with SoTA BNN. This method performs worse than PokeBNN [1], which was published three years ago. PokeBNN has a top1 acc of 70.5 on ImageNet, while it has fewer flops.

2. Lacks deeper analysis of the relationship between model architecture and performance gains. I noticed that there are some performance degradation when trained from scratch. I am not sure if this performance gain from the designed modules themselves or from the training.

### Questions
The proposed architectures combine FP32 depthwise separable convolutions with binarized pointwise convolutions, effectively reducing computational costs while maintaining performance through increased model complexity in deeper layers. It may improve the efficiency in terms of flops. **In system level, does the mix-precision design hurt the inference efficiency?**

### Soundness
3

### Presentation
4

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
This paper proposes novel binarized convolutional neural networks, which quadruple the number of channels and incorporate smooth downsampling. 
It is a mixed model with FP32 depthwise separable and binarized pointwise convolutions. 
It also starts with a few channels in shallow layers and expands them during downsampling by a factor of four, to improve the performance while reducing the total computational costs. 
Besides, a novel smooth downsampling, channel-wise self-attention and multiple binarized convolutions in the fully connected layer are also used. 
Experimental results demonstrate the efficiency of the proposed models in terms of performance, computational costs, and inference latency on real hardware on both ImageNet-1K classification and PASCAL VOC semantic segmentation.

### Strengths
1. The motivation is reasonable. They hypothesize that information loss during downsampling can impact model performance, and develop a novel strategy for configuring channel expansion and downsampling in BCNNs.
   2. The result is comparable with the state-of-the-art.

### Weaknesses
 1. Typo: page 2 line 85, "signficant" should be "significant".
   2. Previous work [1] has proved the effectiveness of SE and its variant in BNNs, thus, it could not be regarded as a contribution. 
   3. The author claims they mainly focus on performance, computational costs, and inference latency. However, multiplying binarized convolutions in the fully-connected layer aims to reduce storage costs, and has no relation to this claim. 
   4. Why does the author quadruple the channel number? Could we set another expanding ratio like 3 or 5, instead of 4 used in this paper?

### Questions
As listed in weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents novel binarized convolutional neural networks (BCNNs), termed QB-Net and QSB-Net, which achieve state-of-the-art performance among BCNNs and are tested on edge devices. Experiments demonstrate the real-world deployment potential of QB-Net and QSB-Net.

### Strengths
1.The deployments on RPi 4B and Exynos strengthen the practical relevance of this work.
2.The results across various datasets and tasks validate the effectiveness of QB-Net.

### Weaknesses
1. The channel quadrupling technique is not novel; previous works, such as TResNet, have employed it. However, this work lacks a discussion on its application.

2. Figure 1(b) is unclear; moving the legend outside the figure may improve clarity.

3. The choice of model design requires a more thorough discussion.

4. The writing could be improved for clarity.

5. Additional tables in the Ablation Study section would be beneficial.

6. Could you clarify the impact of downsampling width first versus height first?

### Questions
see weaknesses

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper introduces two novel binarized convolutional neural network (BCNN) architectures, QB-Net and QSB-Net, which leverage CHANNEL QUADRUPLING and SMOOTH DOWNSAMPLING to optimize performance in resource-constrained settings. The proposed models integrate FP32 depthwise separable (DS) convolutions with binarized 1x1 pointwise convolutions. To manage model complexity effectively, both models use narrow channels in initial layers and expand channels by a factor of four during downsampling. Additionally, they introduce a smooth downsampling technique that progressively doubles the channel count at each stage. Further, the design incorporates channelwise self-attention (SE) with minimal computational overhead. Experimental results on ImageNet-1K and PASCAL VOC show that QB-Net and QSB-Net achieve superior performance among binarized networks.

### Strengths
- The integration of channel quadrupling and smooth down-sampling within BCNNs represents a new approach that effectively balances computational efficiency with model performance.
- The reported accuracy on ImageNet-1K and PASCAL VOC datasets substantiates the efficacy of the proposed models.
- The latency measurements conducted on both the Raspberry Pi 4B and Samsung Exynos-9820 processor demonstrate the practical feasibility of the models in real-world applications.
- The paper offers comprehensive descriptions of the model architectures, experimental setups, and training protocols, enhancing transparency and supporting reproducibility.

### Weaknesses
 # Major Concern:
While the results presented are promising, the novelty of this paper appears somewhat limited. The model design heavily relies on a handcrafted architecture coupled with a brute-force search for optimizing the binary (or, more accurately, mixed-precision) network architecture. The core contribution seems to stem from a specific configuration of channel quadrupling and smooth downsampling, rather than a more generalizable or theoretically grounded approach. Given the current pace of advancements in the field, this approach may offer limited benefit to the broader community and does not fully align with the novelty standard typically expected at a top-tier machine learning conference.

# Minor Comments:

- The proposed models require over 500 epochs to converge, which is considerably longer than the conventional training time on the ImageNet dataset. To provide a more complete comparison with other binary and full-precision models, it would be beneficial to analyze the impact of these extended training requirements and the use of a teacher model on final model performance. Specifically, the paper should investigate whether the performance gains are primarily due to the architectural innovations or simply a result of the prolonged training and knowledge distillation process.
- Although the proposed models incorporate a range of established techniques through channel quadrupling and smooth down-sampling, the paper would benefit from additional ablation studies to clarify the individual contributions of these primary techniques to model performance. For example, it is unclear how much each contributes to the final accuracy, and whether the performance gain is due to the combination of both or if one is more dominant.
- Additional visualizations of feature maps could be helpful in illustrating the effects of the proposed smooth down-sampling technique. This would also help clarify whether the observed performance improvements stem from the design itself or from added computational complexity. It would be beneficial to visualize feature maps at different stages of the network to understand how smooth downsampling affects feature representation.
- The paper’s primary focus is on image classification tasks, with limited experimental results on the VOC dataset for semantic segmentation. A broader range of experiments, particularly on larger and more diverse datasets (e.g., COCO detection or segmentation tasks), would help to more convincingly demonstrate the generalizability of the proposed model. The current evaluation does not sufficiently demonstrate the model's applicability to diverse vision tasks.
- It appears that more recent works on lightweight network design are missing from the comparisons in Table 3. Including these works would provide a more comprehensive context for evaluating the proposed model’s contributions. Specifically, the paper should compare against state-of-the-art lightweight models, not just older or less performant ones.

### Questions
- Could the paper provide a more extensive set of comparative experiments across a broader range of visual tasks and larger-scale datasets (e.g., COCO detection or segmentation tasks) to further validate the generalizability of the proposed model?
- Would it be possible to analyze and compare the impact of training costs on the final performance between the proposed models and existing binary or full-precision models? This would add valuable insight into the efficiency of the proposed approach.
- Could the authors include ablation studies to illustrate the individual contributions of channel quadrupling and smooth down-sampling to the overall model performance? This would clarify the significance of these techniques within the model design.

### Soundness
3

### Presentation
3

### Contribution
2
