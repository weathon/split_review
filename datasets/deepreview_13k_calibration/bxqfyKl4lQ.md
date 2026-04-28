# BiDRN: Binarized 3D Whole-body Human Mesh Recovery

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 3, 8

## Abstract
3D whole-body human mesh recovery aims to reconstruct the 3D human body, face, and hands from a single image. Although powerful deep learning models have achieved accurate estimation in this task, they require enormous memory and computational resources. Consequently, these methods can hardly be deployed on resource-limited edge devices. In this work, we propose a Binarized Dual Residual Network (BiDRN), a novel quantization method to estimate the 3D human body, face, and hands parameters efficiently. Specifically, we design a basic unit Binarized Dual Residual Block (BiDRB) composed of Local Convolution Residual (LCR) and Block Residual (BR), which can preserve full-precision information as much as possible. For LCR, we generalize it to four kinds of convolutional modules so that full-precision information can be propagated even between mismatched dimensions. We also binarize the face and hands box-prediction network as Binaried BoxNet, which can further reduce the model redundancy. Comprehensive quantitative and qualitative experiments demonstrate the effectiveness of BiDRN, which has a significant improvement over state-of-the-art binarization algorithms. Moreover, our proposed BiDRN achieves comparable performance with full-precision method Hand4Whole while using just \textbf{22.1\%} parameters and \textbf{14.8\%} operations.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a binarized network for the task of human shape recovery from images. The main design in the proposed Binarized
Dual Residual Network (BiDRN) is the Binarized Dual Residual Block (BiDRB), which is further composed of Local Convolution Residual (LCR) and Block Residual (BR). The LCR is extended to convolution operations with down scale, down sample, fusion up, and fusion down. The design of LCR includes using Hardtanh as pre-activation function and the adoption of RPReLU activation. Experiments are conducted on two datasets to show the effectiveness of the proposed method compared with other binarization methods.

### Strengths
This paper presents detailed design of the binarized dual residual block, which covers the design of the pre-activation function, local convolution residual with channel-wise RPReLU, and block residual.

The Local convolution residual is extended to scenarios where the residual does not match the dimension of the outputs of convolutions.

Both the backbone of the reconstruction task and the face and hand detection network are considered in the network binarization.

Experiments on EHF and AGORA show performance advantages over other binarization methods.

### Weaknesses
The novelty and contribution of the proposed binarization is limited as most of the design is quite straightforward. The block residual is something new to me.

The designed residual block is quite specific for ResNet. This limits the scope of the proposed binarized dual residual block.

The experiment is conducted with comparison to other standard binarization methods, which are designed for general networks. This comparison is kind of unfair as the proposed binarization only works for this particular model, or maybe a broader ResNet-like architecture. A comparison to other binarization/quantization methods for networks in 3D human reconstruction or ResNet-like models is needed.

It is not very clear why the proposed binarization method target at the Hand4Whole method. There are other (latest) methods (with better performance) in the field.

Latency. While the OPs is provided to have a rough idea of the number of operations, It is also necessary to see the change of speed with the proposed binarization.

### Questions
It is not very clear why the proposed binarization method target at the Hand4Whole method. There are other (latest) methods (with better performance) in the field.

Latency. While the OPs is provided to have a rough idea of the number of operations, It is also necessary to see the change of speed with the proposed binarization.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a binarized network for 3D whole-body recovery from images. The core design of the proposed network is a binarized module consisting of (i) the local convolution residual with hardtanh pre-activation to alleviate binarization failures, and (ii) the block residual with a full-precision shortcut to maintain information. The proposed network is compared with several general binarization methods on two public datasets. The experimental results show that the proposed network outperforms the general binarization methods.

### Strengths
\+ The presentation of this paper is good and easy to follow.

\+ This paper provides a good engineering solution for efficient human mesh recovery. It raises the performance of previous binary networks on the EHF and AGORA datasets.

### Weaknesses
- The proposed method is not clarified clearly. In the down sample residual block (Figure 4, left), why the dual binarized convolutions with the same inputs, kernel sizes, and strides are needed? How does it differ from a grouped binarized convolution (i.e., with 2 groups)? As for the FullPrecision convolution in the block residual, its kernel size and stride are 1 and 2, respectively. Will this result in checkboard artifacts?

- None of the competitors is designed for human mesh recovery. I wonder whether the proposed method still has significant advantages in efficiency compared with those tailored for this task (in terms of GPU memory and FPS), such as [1-2].

[1] Dou, Zhiyang, et al. Tore: Token reduction for efficient human mesh recovery with transformer. ICCV 2023.

[2] Zheng, Ce, et al. Potter: Pooling attention transformer for efficient human mesh recovery. CVPR 2023.

- The qualitative results show that some meshes predicted by the proposed method do not align with images well (e.g., hands and faces in Figure 7).

### Questions
I have a few concerns that I wish could be addressed. I may change my decision after reading the rebuttal and other reviewers' comments.

Q1: It would be better to include the results of the baseline (Hand4whole) in the visual examples.

Q2: Why binarized deconvolution and linear layers even yield better performance (L345-346)?

Q3: How is the prediction head of SMPLX parameters binarized?

Q4: A visual architecture comparison with other binarized methods could help to capture the gist and novelty of the proposed design, especially when previous methods have similar components, e.g., Bi-real also adopts a piecewise polynomial function and shortcuts. 

Typos: "e.g.the" -> "e.g., the", "Hands regions" -> "Hand regions".

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper investigates the binarized network for whole-body 3D human mesh recovery. The motivation is to reduce the high computational cost of existing multi-stage pipeline, so that the model can efficiently run on mobile devices. While directly binarizing the backbone causes severe degradation on precision of mesh regression. Built on the baseline, Hand4Whole, this paper redesigns the architecture of backbone, bounding box detector, and decoding heads to reduce the computational costs while alleviating the reduction in precision.  The experiments are conducted on EHF and AGORA to testify the effectiveness of the proposed designs, compared with other common designs. Compared to the previous binarization design, ReCU, the proposed method reduces 17.1% and 4.5% on EHF and AGORA in terms of whole-body MPJPE, meanwhile, reducing the computational costs to 27.8% of the original Params and 15.6%  of the original OPs.

### Strengths
1.	This paper addresses the underexplored challenge of enhancing computational efficiency in whole-body 3D human mesh recovery.
2.	Unlike previous binarization methods, the proposed approach mitigates degradation in mesh regression to an obvious extent.
3.	The reduction in model parameters and operations is substantial, making this method valuable for deployment on mobile devices.

### Weaknesses
This paper introduces a binarization model based on the state-of-the-art multi-stage method, Hand4Whole. The experiments and binarization techniques are tailored specifically to optimize this baseline. However, it remains unclear whether the proposed binarization approach is compatible with more efficient one-stage methods, such as MultiHMR or AiOS, which may offer greater potential for faster performance on mobile devices. If the proposed binarization method cannot be applied to other whole-body HMR methods, its novelty and contribution to the field would be limited.

The challenges are described as engineer problems, such as the quality of backbone features or dimension mismatching. The motivation behind all the binarization designs hasn’t been discussed in an obvious way.

Furthermore, the focus on convolution-based backbones significantly limits the applicability of this work. Many state-of-the-art HMR methods, such as HMR2, TokenHMR, and even MultiHMR when used in its original form, employ ViT-based backbones. The performance gap between convolution-based and ViT-based backbones in these tasks is well-documented, and the inability of the proposed method to support ViT architectures restricts its practical relevance.

### Questions
The scientific value of the proposed method might be determined by whether the proposed method can be generalized to the other HMR methods, especially the one-stage methods, AiOS / MultiHMR, which adopts a very different architecture.

### Soundness
3

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
In this work, the authors focus on the 3D HMR (human mesh recovery) task. They propose a method named BiDRN based on a Binarized Dual Residual Network. They propose to use a binarized boxnet followed by three BiDRNs for the face, hand, and body, respectively. These features are then projected to SMPL-X parameters to animate the human object. As suggested by the authors, they are the first to propose a binarized neural network for the HMR task. The authors have conducted extensive comparisons on EHF and AGORA benchmarks and compared both binarized and non-binarized methods.

### Strengths
+ The proposal of BiDRN is one of the first implementations of a Binarized Neural Network for the HMR task. The motivation is solid (due to rendering time requirements for VR), and the paper is well-written and easy to follow.
+ The authors have conducted comprehensive comparisons with other methods, including both BNN-based and non-BNN-based methods. They show significant improvement over other BNN-based methods, while performance is close to float32 networks, with a huge reduction in computational requirements.
+ The overall improvement is validated with extensive ablation results.

### Weaknesses
This work is interesting, and I have no major concerns. For further improvement, here are some suggestions:

+ For the results shown in Table 1, please consider including more recent BNN-based methods. Currently, the latest work in the table is from 2021, which is three years old. Including more recent work would make the comparison more reasonable, as the BNN domain has advanced in recent years (as stated in the related works).
 + As BNNs significantly reduce computational requirements, it would be helpful to check the FPS rate for a video for the BNN network compared to the original network, which could better illustrate whether the BNN-based model can achieve real-time HMR.

### Questions
If authors are able to provide the FPS rate for the reconstruction for a video, along with the resolution of the frames and computational resources, it can be very helpful to further validate how fast BNN can achieve for HMR task.

### Soundness
3

### Presentation
3

### Contribution
3
