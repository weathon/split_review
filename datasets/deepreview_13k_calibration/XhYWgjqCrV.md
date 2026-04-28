# MogaNet: Multi-order Gated Aggregation Network

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 8, 6, 6

## Abstract
By contextualizing the kernel as global as possible, Modern ConvNets have shown great potential in computer vision tasks.
However, recent progress on \textit{multi-order game-theoretic interaction} within deep neural networks (DNNs) \pl{reveals the representation bottleneck of modern ConvNets}, where the expressive interactions have not been effectively encoded with the increased kernel size. 
To tackle this challenge, we propose a new family of modern ConvNets, dubbed MogaNet, for discriminative visual representation learning in pure ConvNet-based models with favorable complexity-performance trade-offs. 
MogaNet encapsulates conceptually simple yet effective convolutions and gated aggregation into a compact module, where discriminative features are efficiently gathered and contextualized adaptively.
MogaNet exhibits great scalability, impressive efficiency of parameters, and competitive performance compared to state-of-the-art ViTs and ConvNets on ImageNet and various downstream vision benchmarks, including COCO object detection, ADE20K semantic segmentation, 2D\&3D human pose estimation, and video prediction.
Notably, MogaNet hits 80.0\% and 87.8\% accuracy with 5.2M and 181M parameters on ImageNet-1K, outperforming ParC-Net and ConvNeXt-L, while saving 59\% FLOPs and 17M parameters, respectively.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper introduces a new convolutional neural network for varies of computer vision tasks.
Specifically, it is motivated by the theory of  multi-order game-theoretic interaction in deep neural networks.
This paper finds that popular transformer-based and CNN-based networks have limited interactions on the middle-order interactions. So it introduces the MogaNet with multi-order gated aggregation to solve this problem. 
MogaNet uses convolutions with different kernel size as well as the gated aggregation, which can adatively conduct the multi-order aggregation.

Experiments are perform on several popular benchmarks, such image classification, semantic segmentation, object detection, instance segmentation, and pose estimation. Results show that MogaNet achieves the SOTA performance on several popular benchmarks.

### Strengths
+ The paper is well-written, comprehensively introducing the motivation and method details.

+ The experiments are comprehensive, covering several popular vision tasks as well as varies of network scales.

+ The experimental and visualized analysis is good, helping the reviewer better understand the method.

+ Code has been released, so the reproducibility can be ensured.

### Weaknesses
 - Despite good experiments and visualizations, I think the novelty is limited.
As described in the introduction, the low-order interactions are modeling the local features, such as edge and texture. The high-order on the other hand models high-level semantic features. So multi-order feature aggreation indicates the multiscale aggregation with low and high level features. This paper implements it via depth-wise convolution with different kernel size and further adds gated operation, introducing multi-order gated aggregation.
However, FocalNet exibits similar behavior, proposing hierachical gated aggregation with locality perception and gated aggregation. So I think the proposed MogaNet has similar motivation and mechanism with FocalNet [1].

- Moreover,
The proposed method is a variant of convolutional modulation, but lacks an in-depth discussion on differences with recent CNNs based on convolutional modulations, such as VAN [2], FocalNet [1], and Conv2Former [3]. 
Besides, VAN [2] and FocalNet [1] should be added in Figure 3 for a comprehensive analysis on the interaction strength.

- Regarding to the Figure 7 of ablation study, I am confused that the main improvement is not from multi-order convolution or gate, which are claimed as major contributions of this work. 
Instead, the main improvement is from the CA, which is embedded in the feed-forward network. Note that other networks do not have CA in their feed-forward network, introducing somewhat unfair comparison.
Therefore, I think the authors should better clarify the mechanism of the CA and claim it as the major contribution, not only emphasizing the proposed multi-order gated aggregation.

### Questions
Refer to the weakness.

The major problem is the limited novelty. Besides, there lacks a comprehensive discussion on convolutional modulations.
The major improvement is from the CA, not the modules claimed as major contributions.

### Soundness
3 good

### Presentation
3 good

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
This paper proposes MogaNet, a new form of attentional aggregation mechanism across spatial dimension and channel dimension. The main motivation for this new design is to force the network against learning its implicitly preferred extreme-order interactions, and instead to learn the mid-order interactions more easily. The paper presents empirical evidence that with the proposed spatial and channel aggregation modules, the network can score higher in learning the mid-order interactions as well as achieve state-of-the-art results on multiple computer vision tasks and benchmarks.

### Strengths
## originality
This paper presents a **novel perspective** that we should design neural networks such that it can efficiently learn **multi-order** interactions, esp. the mid-order ones. Guided by this perspective, this paper proposes a new form of **attention** mechanism (Moga Block) for both spatial and channel aggregation. While the proposed Moga Block is **not** exactly of strong novelty, the lens through which the new design is investigated and measured is very **interesting and novel**.

## quality & clarity
This paper is **excellently presented** and backed up with extensive experiments in both the main paper and the supplementary materials. The writing is precise and concise. The figure and table layout is well thought out.

## significance
While the claim on the benefit of learning multi-order interactions still need to be verified with time, I believe the **strong empirical performance** achieved by the new design is of strong significance already.

### Weaknesses
There lacks a **theoretical understanding** on why the proposed Moga Block can help facilitate the learning of more mid-order interactions. There also lacks a **theoretical understanding** on why more mid-order interactions is better for the computer vision tasks. What should the **best curve** for "interaction strength of order" look like? Should it be a horizontal line across all the interaction orders? (If not, why should we automatically believe that more mid-order interactions will be better?)

Figure 7 shows the proposed "Moga(.)" module and "CA(.)" module are helping the model to learn more mid-order interactions. But it would be also very helpful to show how the **internal design** of "Moga(.)" and "CA(.)" modules affect the curve for "Interaction Strength of Order".  For example, why do we choose the "Cl : Cm : Ch = 1:3:4" (section 4.4)? Would different mix move the curve differently? Same question for the design in Figure 4(a) and 4(b), which sub-design is the most effective component in moving the curve?

### Questions
see questions raised above

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper introduces a multi-order gated aggregation network, aiming to encode expressive interactions into ConvNets and increase the representation ability of ConvNets. Particularly, a multi-order spatial gated aggregation module is introduced to encode multi-order interactions of features, while a multi-order channel reallocation module is introduced to reduce information redundancy, which can enhance middle-order game-theoretic interactions. The experiments are conducted on several vision tasks, including image classification, object detection, instance and semantic segmentation, 2D and 3D pose estimation, and video prediction.

### Strengths
+: The experiments are conducted on several vision tasks, and the results show the proposed networks are competitive to existing popular architectures. In my opinion, extensive experiments are main strength of this work.

+: The overall architectures of this work are clearly descried, and seems to be easy implement.

### Weaknesses
 -: The analysis on multi-order game-theoretic interaction encourage to propose the multi-order gated aggregation network. However, in my opinion, relationship between Sec. 3 (i.e., analysis) and Sec. 4 (implementation) seems a bit loose. Specifically, I have a bit doubt on why fine-grained local texture (low-order) and complex global shape (middle-order) can be instantiated by Conv1×1(·) and GAP(·) respectively. And why three different DWConv layers with dilation ratios can capture low, middle, and high-order interactions? What are close relationship between multi-order game-theoretic interaction and multi-order channel reallocation module? Therefore, could the authors give more detailed and rigorous correspondings between analysis in Sec. 3 and module design in Sec. 4?

-: From the architecture perspective, the proposed MogaNet exploit multiple depth-wise convolutions for token mixing and channel attention-based FFN for channel mixing. The idea on multiple depth-wise convolutions for token mixing was used in RepLKNet [RepLKNet], while channel attention-based FFN was explored in LocalViT [LocalViT] and DHVT [DHVT]. So I have a bit doubt on technological novelty of core ideas on designing overall architectures of MogaNet. I suggest the authors can give more detailed analysis on novelty of MogaNet from the architecture perspective.



### Questions
Additional comments:

-: The compared results show that performance gains of the proposed MogaNet over existing popular architectures is not significant. So could the authors show more advantages of the  MogaNet?

-: Besides parameters and FLOPs, latency is more important for practice applications. So could the authors show some results on the latency (e.g., training time and inference time) of the MogaNet?

-: There exist much more efficient and effective channel attention, besides SE. Therefore, the authors would better compare more efficient channel attention methods to verify the effectiveness of CA module.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors introduce a new family of pure CNN architectures, dubbed MogaNet, by analyzing the effects of different-order interactions in deep neural networks. They assert that MogaNet with two new modules for spatial and channel mixing improves middle-order interaction while suppressing extreme-order interaction, yielding promising results for visual recognition. Comparisons on image classification and downstream tasks show the effectiveness.

### Strengths
- The impact of multi-order interaction in neural networks provided by previous work is a fascinating starting point for network architecture design.
- Both quantitative and qualitative experiments demonstrate adequate research work.
- Specific training parameters are provided, which are rather important for reproduction by the community.

### Weaknesses
The core idea of this work is hard to follow. Why the proposed network design is "an appropriate composition of convolutional locality priors and global context aggregations" is not entirely evident. In addition to the quantitative depiction in Fig. 3, qualitative analysis of the reasons why earlier network designs failed at this point would be extremely helpful in explaining this central argument. Please refer to the QUESTIONS section for details.

Primary:
- The perspective on multi-order interactions that serves as the foundation and impetus for this work is presented in [r1]. Analysis of the factors  why existing networks results in an inappropriate composition of local and global context is still lacking.
- It is thought that the self-attention mechanism is more adaptable than typical gate attention. Why does ViT fail to learn middle-order interactions when self-attention is present?
- For the purpose of capturing low-, middle-, and high-order interactions, Moga Block uses three parallel branches. To confirm that the model concentrates more on the middle-order as anticipated, it would be preferable to give the gate values (or attention map).
- The substration $Y-GAP(Y)$, which "forces the network against its implicitly preferred extreme-order interactions," is the main function of FD. Why does the CA block not include this operation?
- Wrong markup in Fig.5, i.e., two $1:0:0$.

Others:
- Will MogaNet be less robust because low-order interation "represents common and widely shared local patterns with great robustness"?
- It would be better if figures following the order they appear in the main-body text.
- It would be interesting to know how the losses (presented in [r1]) and MogaNet pitted against (or collaborate with) each other, because both supervision signal and structure design matter for deep neural networks.
- The two expressions before and after Equation 1 contradict each other, i.e., "in the same shape" and "downsampled features".

### Questions
Primary:
- The perspective on multi-order interactions that serves as the foundation and impetus for this work is presented in [r1]. Analysis of the factors  why existing networks results in an inappropriate composition of local and global context is still lacking.
- It is thought that the self-attention mechanism is more adaptable than typical gate attention. Why does ViT fail to learn middle-order interactions when self-attention is present?
- For the purpose of capturing low-, middle-, and high-order interactions, Moga Block uses three parallel branches. To confirm that the model concentrates more on the middle-order as anticipated, it would be preferable to give the gate values (or attention map).
- The substration $Y-GAP(Y)$, which "forces the network against its implicitly preferred extreme-order interactions," is the main function of FD. Why does the CA block not include this operation?
- Wrong markup in Fig.5, i.e., two $1:0:0$.

Others:
- Will MogaNet be less robust because low-order interation "represents common and widely shared local patterns with great robustness"?
- It would be better if figures following the order they appear in the main-body text.
- It would be interesting to know how the losses (presented in [r1]) and MogaNet pitted against (or collaborate with) each other, because both supervision signal and structure design matter for deep neural networks.
- The two expressions before and after Equation 1 contradict each other, i.e., "in the same shape" and "downsampled features".

I would be glad to raise my rating if thoughtful responses are presented.

[r1] H. Deng, Q. Ren, H. Zhang, and Q. Zhang, “Discovering and Explaining the Representation Bottleneck of DNNs,” in International Conference on Learning Representations (ICLR), 2022.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
3 good
