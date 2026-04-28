# Improving MLP Module in Vision Transformer

- Decision: Reject
- Avg Score: 4.75
- Scores: 3, 3, 8, 5

## Abstract
Transformer models have been gaining substantial interest in the field of computer vision tasks nowadays. Although a vision transformer contains two important components which are self-attention module and multi-layer perceptron (MLP) module, the majority of research tends to concentrate on modifying the former while leaving the latter in its original form. In this paper, we focus on improving the MLP module within the vision transformer. Through theoretical analysis, we demonstrate that the effect of the MLP module primarily lies in providing non-linearity, whose degree corresponds to the hidden dimensions. Thus, the computational cost of the MLP module can be reduced by enhancing the degree of non-linearity in the nonlinear function. Leveraging this insight, we propose an improved MLP (IMLP) module for vision transformers which involves the usage of the arbitrary GeLU (AGeLU) function and integrating multiple instances of it to augment non-linearity so that the number of hidden dimensions can be effectively reduced. Besides, a spatial enhancement part is involved to further enrich the non-linearity in the proposed IMLP module. Experimental results show that we can apply our method to a wide range of state-of-the-art vision transformer models irrespective of how they modify their self-attention part and the overall architecture, and reduce FLOPs and parameters without compromising classification accuracy on the ImageNet dataset.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper introduces a derivative of GeLU called arbitrary GeLU (AGELU) that aims to improve the capability of MLP in vision transformers. AGeLU is used in the MLP and is further combined with the concatenation operators, and extra spatial depthwise convolution (DWConv) following the tuple of BN/GELU  is included in the end. The authors provide some theoretical backups for justifying the proposed element with the experiments on ImageNet-1K.

### Strengths
- The idea is simple and easily applicable to any vision transformers.
- Some theoretical justifications are provided.

### Weaknesses
 - This paper primarily addresses the activation functions, but many related works are missing, which have emerged after GeLU:
  - Mish: A Self Regularized Non-Monotonic Activation Function, BMVC 2020
  - Padé Activation Units: End-to-end Learning of Flexible Activation Functions in Deep Networks, ICLR 2020
  - Smooth Maximum Unit: Smooth Activation Function for Deep Networks using Smoothing Maximum Technique, CVPR 2022

- The performance enhancements provided by the proposed activation function are marginal and non-existent in some instances. The proposed activation function fails to improve accuracy in larger models like Deit_B and LVT-R4; moreover, it actually leads to a decline in performance for Swin-B and Poolformer-M48.

- The main issue identified by the reviewer is the performance gains of this work appear to depend largely on employing depthwise convolution, which has been already recognized in many prior hybrid architectures. The ablation studies presented in the manuscript further underscore this reliance as well. As a result, the paper's contribution is considered to be very limited.

- This paper needs more experiments to justify the claim:
  - Experimental comparisons with simple simple activation functions such as SoftPlus, ELU, ReLU6, Swish, and so on are not compared. 
  - Downstream tasks in the Appendix contain limited results with a few backbones.

- It is speculated that the proposed method's effectiveness relies on KD (Table 2 evidently shows this), which requires a teacher model. Consequently, training budgets may not be preserved equally. 
 
- The reviewer acknowledges that while the theories included do enhance the paper, it lacks a crucial explanation—specifically, the rationale behind why AGeLU with concatenation is necessary has not been addressed via theory. 

- The proposed variant of GeLU is not exclusively applicable to vision transformers. It can also be utilized in architectures like ConvNeXt, which shares similar building blocks, excluding self-attention, where the proposed element could serve as a replacement for standard GeLUs.



### Questions
See above weaknesses.

- Please specify how KD works when training with the proposed activation function.

- The reviewer highlights Table 3, noting it presents a surprising and crucial result of the study. The authors are requested to provide insights or intuitions into why such an outcome occurred.

- The results in Table 4 are not clearly explained. 

- Why is the additional shortcut needed for the dwconv and BN should follow it subsequently?

Pre-rebuttal comments) This paper proposes a variant of GeLU to improve the MLP module in the vision transformer module. However, the identified shortcomings and the raised questions lead to the conclusion that the paper does not meet the publication standards of ICLR in its present state. I would like to see the authors' responses and the other reviewer's comments.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors propose a modified MLP module for vision transformers which involves the usage of the arbitrary GeLU (AGeLU) function and integrating multiple instances of it to augment non-linearity so that the number of hidden dimensions can be reduced. Besides, a spatial enhancement part is involved to further enrich the nonlinearity in the proposed  modified MLP module.

### Strengths
1. Base model design is an important topic in our community.
2. This paper is easy to understand.

### Weaknesses
1. My major concern is the effectiveness, we can see some parameter and computational cost savings from Table 1, but this method introduced lots of hardware unfriendly operations like DW conv. 
2. No actual latencies are provided for the proposed models and the throughput is more critical than the number of parameters and FLOPs for real applications.
3. From Table 3, I can't see a solid improvement from AGeLU.

### Questions
Can you offer the actual latencies?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper conducts a theoretical analysis of the MLP module within the architecture of vision transformers, showing that the MLP fundamentally acts as a non-linearity generator. Consequently, the paper proposes an Improved Multilayer Perceptron (IMLP) module, which augments non-linearity across both the channel and spatial dimensions, while concurrently reducing computational complexity by diminishing the hidden dimensions. Experiments suggest that for state-of-the-art models, such as ViT, Swin, and PoolFormer, the substitution of the original MLP with the IMLP module can significantly reduce model complexity without compromising accuracy.

### Strengths
1. The paper proposes a solid theoretical analysis by delving into the math of the MLP module, successfully establishing it as a non-linearity generator. 
2. This paper introduces AgeLU to form a more nonlinear function and improves the non-linearity within the channel dimension of the IMLP module. The paper extends the non-linearity enhancement to the spatial dimension as well, using a comprehensive approach to improve the IMLP module's capabilities.
3. The empirical validation is compelling, with a variety of architectures and tasks being employed to verify the effectiveness of the proposed IMLP module.
4. The writing in the paper is well done, with a clear structure that makes it easy to understand. The way the ideas are presented is thoughtful and makes for an engaging and informative read.

### Weaknesses
1.	In Equation (5), AGeLU and AGeLU′ are introduced as two nonlinear functions. It prompts an intriguing inquiry: what would the outcome be if the division was into more parts, say four? A more comprehensive ablation study should be conducted to provide a richer understanding of the behavior and performance of these functions. Specifically, the paper should explore how varying the number of divisions impacts both the model's capacity to learn complex features and its computational efficiency. Furthermore, it would be beneficial to analyze the effect of different activation functions within each division, rather than just using AGeLU and AGeLU'.
2.	In Section 4.3, there lack of comparative experiments with other non-linear blocks like bottleneck in ResNet or linear bottleneck in MobileNetV2, which could have showcased the unique advantages or potential shortcomings of the proposed method in a broader context. The paper should include a more thorough comparison with these established non-linear blocks, particularly focusing on how the proposed IMLP module compares in terms of parameter efficiency, computational cost, and overall performance across different network architectures. This would help to contextualize the contribution of the IMLP module more effectively.
3.	The proposed IMLP module has only been experimented with a few models like ViT and Swin, which have been proposed for several years. It raises the question of the module's effectiveness on more recent, higher-accuracy models like iFormer. The validation of the IMLP module across a broader spectrum of models could provide a clearer picture of its versatility and efficacy in current vision transformer landscapes. It is crucial to demonstrate the module's adaptability to diverse architectures and its ability to maintain or improve performance on state-of-the-art models, which would significantly strengthen the paper's claims.

### Questions
See weaknesses above.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents significant enhancements to the design of the MLP module, referred to as IMLP, aimed at augmenting its non-linear capabilities. A key innovation in this work is the introduction of a novel activation function, termed AGeLU. Additionally, a convolution layer has been meticulously crafted to bolster the spatial information within the module. Extensive experimental results are provided in the paper by applying the IMLP module in diverse vision transformer architectures. The results demonstrate that the proposed method can help the transformers obtain similar performance with fewer parameters by reducing the hidden channels of MLP modules.

### Strengths
1.	The MLP module's non-linearity is intuitively illustrated in a clear and intriguing manner.
2.	The effectiveness of the proposed method is validated across various tasks and diverse transformer models, encompassing both isotropic and stage-wise variants.
3.	The paper provides a theoretical analysis of the bounds of the modified IMLP module, providing valuable insights for parameter selection within the module.

### Weaknesses
1.	The AGeLU's standalone performance appears suboptimal. Table 2 suggests that the primary performance improvements stem from knowledge distillation or spatial enhancement, with the paper lacking a clear demonstration of the enhanced non-linearity's effectiveness, i.e., the proposed AGeLU. Specifically, the gains from AGeLU alone are not isolated, making it difficult to assess its contribution independently of the spatial enhancement and other factors. The experimental design does not sufficiently decouple the effects of AGeLU from the other modifications, such as the depthwise convolution, which makes it hard to determine if the observed improvements are due to the activation function itself or the spatial enhancement.
2.	There is ambiguity regarding whether the kernel size is consistently set to 5 for large-scale models such as DeiT-B or Swin-B, lacking a definitive explanation in the paper. The paper does not provide a clear rationale for choosing a kernel size of 5 for larger models, nor does it explore the impact of varying kernel sizes on performance and computational cost. This lack of clarity makes it difficult to understand the design choices and their implications for different model scales.
3.	The remarkable performance drops attributed to the addition of GeLU with four times the number of channels raise questions. Since the fully connected (fc) layer entails linear calculations, it appears that the addition operation merely doubles the original output, which requires further clarification. The paper does not adequately explain why simply increasing the number of channels with added GeLU layers leads to such a significant performance degradation. The linear nature of the fully connected layers should not, in theory, cause such a drastic drop, suggesting a potential issue with the implementation or a lack of understanding of the interaction between the added layers and the overall network architecture.

### Questions
Please see the weakness part. Additionally, introducing spatial enhancement after the GeLU operation (as 'a' in Figure 4) would help to conclusively demonstrate the impact of enhanced non-linearity in parameter reduction.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good
