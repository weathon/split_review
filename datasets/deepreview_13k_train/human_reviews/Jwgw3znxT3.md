# Efficient Visual Transformer by Information Bottleneck Inspired Token Merging

- Decision: Reject
- Scores: 6, 6, 8, 3

## Abstract
Self-attention and transformers have been widely used in deep learning. Recent efforts have been devoted to incorporating transformer blocks into different types of neural architectures, including those with convolutions, leading to various vision transformers for computer vision tasks. In this paper, we propose a novel and compact transformer block, Transformer with Information Bottleneck inspired Token Merging, or IBTM. IBTM performs token merging in a learnable scheme. Our IBTM is compatible with many popular and compact transformer networks, such as MobileViT and EfficientViT, and it reduces the FLOPs and the inference time of the vision transformers while maintaining or even improving the prediction accuracy. In the experiments, we replace all the transformer blocks in popular vision transformers, including MobileViT, EfficientViT, ViT, and Swin, with IBTM blocks, leading to IBTM networks with different backbones. The IBTM is motivated by the reduction of the Information Bottleneck (IB), and a novel and separable variational upper bound for the IB loss is derived. The architecture of mask module in our IBTM blocks which generate the token merging mask is designed to reduce the derived upper bound for the IB loss. Extensive results on image classification and object detection evidence that IBTM renders compact and efficient vision transformers with comparable or much better prediction accuracy than the original vision transformers. The code of IBTM is available at \url{https://anonymous.4open.science/r/IBTM_Transformers-053B/}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper studied the problem of token merging/pruning in vision transformers. The authors took inspiration from the connection between token merging and information bottleneck (IB) and introduced a new strategy to leverage the IB principle to guide the token merging process. They derived a variational upper bound loss from the IB loss and proposed optimizing this objective to generate token merging masks. Experiments on ImageNet dataset with multiple tiny-/small-size vision transformers showed considerable improvement of the proposed method over prior works.

### Strengths
1. The paper is well-motivated. Connecting token merging with the IB principle is straightforward and makes a lot of sense. An algorithm guided by this principle is novel and might bring new insights into this research direction.

2. The derivation of the variational upper bound for the IB loss looks technically sound. Empirical analysis also suggests that reducing this upper bound indeed results in lower IB losses for token merging.

3. Experiments on ImageNet dataset with multiple tiny-/small-size vision transformers, and a few experiments on MS-COCO object detection/instance segmentation, showed considerable and consistent improvements in the proposed method over prior works, sometimes by a ;large margin.

### Weaknesses
1. The proposed method, IBTM, requires either additional finetuning epochs to repurpose pretrained models for token merging or extra training time (~30%) to train the vision transformers and the token merging module from scratch. This reliance on additional training or fine-tuning introduces a practical limitation, especially when computational resources are constrained or rapid deployment is needed. The necessity to train the token merging module from scratch alongside the vision transformer also increases the overall training complexity and time, which might be a barrier for some users.

2. IBTM uses hard masks for token merging, which discard a certain amount of the tokens during inference. While the authors mention that the mask is multiplied by a soft mask derived from the gradient, the core operation is still based on a hard selection of tokens. It is not clear if this hard selection is optimal, and it would be beneficial to explore the impact of using soft masks directly for token merging. Additionally, the models with IBTM (thus fewer tokens) perform even better than the original models with more tokens, which is somewhat counter-intuitive. It is important to provide a more in-depth analysis of why this occurs. The explanation that it is due to reduced over-fitting is not fully convincing without further evidence, such as an analysis of the feature space or the generalization performance on different datasets.

### Questions
1. Table 1 suggests that using IBTM will not increase the number of parameters compared to the original models yet Tables 3 and 4 report different scenarios. What is the cause of this difference?

2. Why IBTM is faster than LTMP in inference? These two methods should have the same parametrization scheme and inference pipeline from my understanding of this work.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper introduces a new token merging method on vision transformer, which leverages information bottleneck theory to learn the merging mask. A novel upper bound of IB is derived to optimize the mask module. Experiments of various ViT variants are conducted on ImageNet to validate the effectiveness.

### Strengths
1. This paper proposes a learnable way to merge tokens, which is inspired by information bottleneck and is theoretically feasible for achieving better compression-performance balance compared to previous training-free methods.

2. The performance improvements are consistent and significant.

### Weaknesses
1. The major concern of this method is the requirement of training. According to Table 1, the performance does not get satisfied even after fine-tuning for 50 epochs, this raises concern for the computation cost. The fine-tuning process introduces a significant computational overhead, particularly when compared to training-free token merging methods. The paper should provide a more detailed analysis of the computational resources required for fine-tuning, including GPU memory usage and training time, to better assess the practical implications of this overhead. Furthermore, the paper should explore strategies to reduce the fine-tuning cost, such as using a smaller learning rate or a more efficient optimization algorithm.

2. Lack of experiments to validate the transferrability. ViTs, as the foundation models, are widely adopted in downstream tasks such as transfer learning, object detection and visual-language understanding. As the token merging is trained on ImageNet, it is unknown whether this preference is generic to other tasks and whether the method is better than other token merging methods on transfer tasks. While the paper mentions the use of the proposed method as a feature backbone, it lacks a thorough comparison against other token merging techniques in downstream tasks. It is crucial to evaluate if the learned merging strategy is truly beneficial for diverse tasks or if it is biased towards the ImageNet dataset. A more comprehensive evaluation should include a wider range of downstream tasks and a comparison with other token merging methods to demonstrate the generalizability of the proposed approach.

### Questions
3. What is the superiority of the proposed upper bound of IB objective compared to the existing upper bounds such as CLUB [1]?


[1] Cheng, Pengyu, et al. "Club: A contrastive log-ratio upper bound of mutual information." International conference on machine learning. PMLR, 2020.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The authors propose a novel and compact transformer block (IBTM) that implements token merging in a learnable manner. IBTM is compatible with various popular and compact transformer architectures, effectively reducing both FLOPs and inference time in vision transformers while maintaining or even enhancing prediction accuracy.

### Strengths
1. The authors' motivation is intuitive, and their theoretical analysis from the perspective of the Information Bottleneck framework adds solid support to their claims.

2. The experimental are comprehensive (in particularly, there are detection and segmentation in the appendix) and the results indicate that the proposed approach achieves notable gains and advantages.

3. The authors provide corresponding open-source code, enhancing the credibility and reproducibility of their results.

### Weaknesses
1. The related work on *efficient vision transformers* could be more comprehensive, I suggest including relevant studies such as [1]. Specifically, the discussion should delve deeper into methods that employ learnable token merging or pooling strategies, as these are most directly comparable to the proposed IBTM. A more thorough comparison would clarify the novelty and advantages of the proposed approach over existing techniques. For example, the review should discuss how IBTM handles the trade-off between computational efficiency and information loss compared to other methods.

2. The description of the method could be more concise and clearer; for example, Figure 1 is a bit too brief in its presentation. The explanation of how the learnable merging is achieved, particularly the specifics of the learnable parameters and the merging function, needs more detail. A more detailed illustration or a step-by-step breakdown of the merging process would greatly improve clarity. Furthermore, the connection between the Information Bottleneck framework and the actual implementation in IBTM could be made more explicit.

### Questions
I wonder if incorporating token pruning techniques could lead to better results?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes an innovative Information Bottleneck inspired Token Merging (IBTM) block for ViTs. IBTM block generates a mask for merging tokens by minimizing the difference between the mutual information of the merged tokens with the original tokens and the corresponding class label. With the IBTM block, the merged tokens can better simulate the behaviour of the original tokens during inference. The proposed approach is adapted to four different pre-trained ViT backbones. Comparisons against three token merging methods demonstrate the effectiveness and generalizability of the IBTM block.

### Strengths
1. This paper has compared state-of-the-art token merging methods on various backbones.

2. The proposed token merging strategy with respect to the variation is interesting.

### Weaknesses
 1. 	__Insufficient and unclear motivation__: In the Introduction section, the authors keep arguing that existing token merging methods [1, 2, 3] significantly sacrifice prediction accuracy and claiming their goal is to merge tokens without largely sacrificing performance. However, the reasons why existing token merging methods do not work well and potentially lead to significant performance drops are not clearly explained or justified. As a result, the knowledge gap that IBTM intends to narrow and the drawbacks of existing methods that IBTM is designed to resolve are fairly unclear. In short, the motivation that simply “method A does not work well so we propose a better method B” is weak. The weak motivation essentially affects this manuscript, lowering its academic contribution.

2. 	__Imprecise argument__: In the Introduction section, the authors claim that "existing token merging methods largely sacrifice the prediction accuracy of the original transformer networks for reduced computation costs." However, this assertion is misleading, as with an appropriate token merging ratio, these methods do not experience significant accuracy loss. For instance, ToMe [1] achieves a 20% speed-up on ViT-B/AugReg with only a 0.4% accuracy drop, which cannot be described as "largely sacrificing prediction accuracy."

3. 	__Disorganized structure and weak readability of the Introduction section__: Following Weaknesses 1 and 2, the whole Introduction section is poorly structured. It is overly repetitive and includes unnecessary content, which detracts from the clarity of the main argument. For instance, Lines 67-96 contain repetitive statements and too many details for the Introduction, which should be summarized for readability. And there is no need for a separate subsection 1.1 on the contributions.

4. 	__Unfair comparisons and potential over-claiming__: The authors neglect the finetuning-free nature of some existing token merging methods [1,2] and compare their finetuned IBTM results to the off-the-shelf (i.e., without finetuning) performance of these methods. Such comparisons are not fair and do not accurately reflect the proposed IBTM’s advantages, which also lead to potential over-claiming of the superiority of IBTM.

5. 	__Lack of explanation on applying token merging to hierarchical ViTs__: The paper fails to clarify how existing token merging methods, like ToMe [1] and ToFu [2], are adapted for hierarchical ViTs, such as Swin-Transformer [4]. In fact, most token merging (and token pruning) methods are designed for plain-structured ViTs, and applying them to hierarchical models can conflict with window-based self-attention and downsampling layers. In Table 1, where the authors report the performance of these methods on Swin Transformer and other hierarchical ViTs [5], it is necessary to explain how they adapted the existing token merging methods and their proposed IBTM for these hierarchical ViTs.

6. 	__Missing technical details__: In the Formulation section, it is unclear whether the token merging mask is dynamically generated w.r.t. different inputs or fixed for all the inputs. If the mask is dynamically generated, based on Equations 3 and 4, I do not think this method would be faster than ToMe. If the mask is fixed after finetuning, it is necessary to analyze the mask pattern, which may reflect some hidden token relationships and bring deeper insights.

7. 	__Performance issues__: As shown in Table 7 in Appendix D.2, the proposed IBTM also suffers from a noticeable performance drop when the compression ratio decreases, which undermines its claimed advantages.

8. 	__Writing and presentation issues__:

    8.1.	 Inconsistent and confusing terminology: In Lines 15-16, IBTM is introduced as an abbreviation for "Information Bottleneck inspired Token Merging," while in Lines 52-53, it is referred to as "Transformer with Learning Token Merging," causing confusion. In Line 1059, the proposed method is again referred to as LTM.

    8.2.	 Grammar errors: There are quite a few grammatical errors. For instance, in Line 63, the word "less" should be "fewer“. I suggest the authors carefully proofread this manuscript.

    8.3.	Reference formatting errors: In Line 175, the reference format is incorrect at the start of the sentence. In Line 408, ToFu (Kim et al., 2024) is cited twice unnecessarily.

    8.4.	Line 47 cites _Attention Augmented Convolutional Networks_ [6], which was published earlier than ViT and seems irrelevant to the corresponding claim. In addition, some recent token merging-based methods [7,8] should be cited, which provide necessary insights in this direction.

### Questions
1. According to Weakness 4, could the author please provide IBTM's performance without finetuning on the four ViT backbones for a fair comparison against ToMe and ToFu? 

2. According to Weakness 5, could the author please provide details on adapting existing token merging methods (e.g., ToMe) to hierarchical ViTs (e.g., Swin Transformer), including but not limited to how to perform the downsampling layer, how to split the windows after reduction, how many tokens are there in each layer? 

3. According to Weakness 6, could the author please explain how the token merging mask is generated for various inputs?

4. Could the author please compare their model with token pruning methods, such as EViT [1] and ATS [2], under the same experimental environment? EViT and ATS are strong baseline models, which achieve competitive trade-offs between accuracy and efficiency compared to the token merging methods in various standard experiments [3].

5. Could the authors please explain why choosing efficient ViTs (i.e., FLOPs < 1G) as the backbone for experiments rather than large ViTs? Token reduction technologies (including token pruning and token merging) are initially designed to resolve the massive computational complexity problem of ViTs. They should target expediting large ViTs rather than efficient ViTs. I do not find any significant contribution by reducing the FLOPs of EfficientViT from 0.52G to 0.44G after token merging in terms of real-world application.

[1] Liang, Youwei, et al. "Not all patches are what you need: Expediting vision transformers via token reorganizations." ICLR, 2022.

[2] Fayyaz, Mohsen, et al. "Adaptive token sampling for efficient vision transformers." ECCV, 2022.

[3] Haurum, Joakim Bruslund, et al. "Which tokens to use? investigating token reduction in vision transformers." ICCV, 2023.

### Soundness
3

### Presentation
3

### Contribution
2
