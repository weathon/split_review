# IFORMER: INTEGRATING CONVNET AND TRANSFORMER FOR MOBILE APPLICATION

- Decision: Accept
- Avg Score: 6.40
- Scores: 6, 6, 6, 6, 8

## Abstract
We present a new family of mobile hybrid vision networks, called iFormer, with a
focus on optimizing latency and accuracy on mobile applications. iFormer effectively
integrates the fast local representation capacity of convolution with the efficient
global modeling ability of self-attention. The local interactions are derived
from transforming a standard convolutional network, i.e., ConvNeXt, to design a
more lightweight mobile network. Our newly introduced mobile modulation attention
removes memory-intensive operations in MHA and employs an efficient
modulation mechanism to boost dynamic global representational capacity. We
conduct comprehensive experiments demonstrating that iFormer outperforms existing
lightweight networks across various tasks. Notably, iFormer achieves an
impressive Top-1 accuracy of 80.4% on ImageNet-1k with a latency of only 1.10
ms on an iPhone 13, surpassing the recently proposed MobileNetV4 under similar
latency constraints. Additionally, our method shows significant improvements in
downstream tasks, including COCO object detection, instance segmentation, and
ADE20k semantic segmentation, while still maintaining low latency on mobile
devices for high-resolution inputs in these scenarios. The source code and trained
models will be available soon.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper designs iFormer, a new family of efficient mobile vision networks combining ConvNet and Transformers. The iFormer evolves from ConvNeXt with a series of efficiency designs. 

Single-Head Modulated Attention(SHMA) is proposed as substitutional Transformer blocks to replace part of the Conv blocks in later stages of the enhanced ConvNeXt. SHMA replaces multi-head attention with single-head attention to improve efficiency and introduces a modulation mechanism to boost performance. 

The resulting iFormer series achieves the best performance compared with state-of-the-art mobile-level models on different downstream tasks with lower latency.

### Strengths
This paper is well-organized and easy to follow. Detailed design specifications and comprehensive experiments enhanced the integrity of the article and demonstrated its contributions.

The main contribution, SHMA, provides a new approach to designing efficient attention and Transformer blocks. The resulting iFormer series outperforms sota baseline mobile networks with stronger performance and lower latency.

### Weaknesses
W1:

The motivation and necessity of substituting half of the conv blocks at the third stage and all blocks at the last stage into Transformer blocks in ConvNeXt are still not very clear. From Figure 2, changing the conv blocks into SHA blocks gains a 0.4% improvement in performance but is also 0.12 ms (about 10%) slower. I'd like to know further explanation for this design and ablation studies on the choice of stages or different ratios of Conv versus Transformer blocks if possible.


W2:

According to the citation of SHViT in this paper, I suppose the SHA refers to the Single-head self-Attention in SHViT design. But in Figure 4, full channels of input (CxHxW) are projected to Q/K/V (CxL) which does not align with the design of SHA in SHViT but looks like the traditional definition of Single-head attention that performs a self-attention on all channels of input using a single head.

Considering there are limited words about the details of SHA in this paper, I would expect further specification of which SHA is used in iFormer and comply with the pipeline figure accordingly.


W3:

In this paper, the additional reshaping operations in MHA are considered as the reason for the slower inference speed compared with SHA. But multiple factors have an impact on the runtime speed difference and there's no evidence to support the extra runtime only or mainly comes from extra reshapings.

First, depending on the code implementation, replacing MHA with Single-head self-Attention may remove the reshaping operation in self-attention, but also introduce additional split and concat operations. And generally, split and concat operations cost more memory and are slower than reshape.

Secondly, SHA applies self-attention on fewer channels, which largely reduces the computational cost and speeds up runtime.

Therefore I suggest the authors conduct an ablation study or provide empirical evidence to isolate the impact of reshaping operations versus other factors like split/concat operation and reduced self-attention channels on the inference speed. This would help clarify the main factors contributing to SHA's efficiency and provide a more comprehensive understanding of the proposed method.

### Questions
1. What is the motivation and justification for the necessity of the design that replaces half of the third stage and full last stage conv blocks with transformer blocks? Please refer to Weaknesses 1. 

2. I wonder what is the performance and latency of MHA as the missing step between 'kernel sz.' and 'SHA' in Figure 2.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a new family of mobile hybrid vision networks. By integrating the rapid local representation capability of convolution with the efficient global modeling ability of self-attention, the proposed architecture, iFormer, achieves significant performance in classification and several downstream tasks, while maintaining low latency on mobile devices for high-resolution inputs.

### Strengths
1. The study of model architecture could inspire further exploration in designing more efficient architectures.
2. The paper is well-organized and easy to follow.

### Weaknesses
1. In Table 1, iFormer-S achieves the same latency as RepViT-M1.0 with slightly fewer parameters, yet in larger variants, iFormer achieves lower latency with substantially more parameters compared to RepViT. What is the reason for this difference?
2. Some studies are not included in the comparison or the related wotk section, such as [1, 2].

### Questions
please refer to weakness

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
5

### Summary
This paper presents a mobile hybrid vision network, iFormer. The paper goes from ConvNeXt to a lightweight mobile network. iFormer removes memory-intensive operations in MHA and employs an efficient modulation mechanism. The author conduct standard benchmark experiments on ImageNet, COCO and ADE20K.

### Strengths
I think the logic of exploration in this article, starting with ConvNeXt, first “lightening” the ConvNeXt to create a streamlined
lightweight network, then exploring the attention module, is reasonable. 

I think the analysis about “cosine similarity between multiples” proves that using a single attention is good and worth supporting. 

I think the experiment reported in this paper is comprehensive (imagenet, coco, ade-20k). The paper also reports some knowledge distillation results, which is suitable in mobile network papers.

### Weaknesses
1:  
Single head self-attention has been conducted in "Shvit: Single-head vision transformer with memory efficient macro design" . 

Alternative to standard self-attention has been conducted in GhostNetV2.

Modulation in the token mixer module has been conducted in Conv2Former. 

This paper references many related methods, and while that is one approach, I don't think it stands out. Although such research is a decent format, I believe it impacts the novelty of this paper. 

2: 
The process of evolving from the ConvNeXt baseline to the lightweight iFormer may not apply to slightly larger models, and some steps show very minimal improvements, making them hard to justify.

### Questions
The largest model shown by iFormer, iFormer-L, is only about 15M, which isn’t considered large, even for edge devices, especially since recent edge LLMs can reach 1B parameters. I wonder how well a larger iFormer (around 100M) would perform.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper presents a new family of mobile hybrid vision networks, called iFormer,  by integrating the fast local representation capacity of convolution with the efficient global modeling ability of self-attention.

### Strengths
1. The paper is easy to follow, with clear writing and presentation.
2. Evaluation results are comprehensive.

### Weaknesses
1. How does this method compare with neural architecture search (NAS) methods?

2. How does the designed model perform on other mobile devices, such as NVIDIA Jetson Nano or Raspberry Pi?

### Questions
Please see the weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
Summary

This paper proposes a mobile friendly vision network that improves the latency and accuracy by combining the strengths of both CNNs and ViTs. The novel aspect of this work is the single head modulation self-attention (SHMA). This SHMA learns spatial context through optimized self-attention. It takes ConvNext as the base model and improves it further with various techniques. The authors streamline the ConvNeXt architecture, making it suitable for real-time use on mobile devices, such as the iPhone 13, focusing on reducing latency rather than FLOPs or parameter count. The combined techniques lead to more than 80% top-1 accuracy with 1.1ms latency on iphone 13. Overall a great contribution to the research community.

### Strengths
1. fast local representation capacity of convolution and the efficient global modeling proficiency of the proposed SHMA
2. A series of novel techniques such as stack of overlapping convolution instead of aggressive non-overlapping patch in the early layers
3. The model is structured in four stages. The early stages use fast convolution to capture local features efficiently, using a modified and lightweight version of ConvNeXt optimized for mobile latency.
4. In the lower-resolution stages, self-attention is used to model long-range dependencies. To address the challenges of traditional multi-head self-attention (MHA), the authors propose SHMA, which uses a single-head attention mechanism to minimize memory costs while retaining high performance. SHMA reduces latency by optimizing reshaping operations and leveraging spatial context interactions. SHMA is combined with a parallel feature extraction branch to enhance feature representation. The outputs from both branches are fused to enable dynamic information exchange, mitigating any performance drop caused by simplifying MHA

### Weaknesses
1. What is the runtime complexity of iFormer network?
2. When running on iPhone (mobile device), what is the peak memory consumption? 
3. How long the iPhone charge will last if an iFormer based app is run on certain fps?

### Questions
See weakness

### Soundness
4

### Presentation
3

### Contribution
3
