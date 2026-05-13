# Feast Your Eyes:  Mixture-of-Resolution Adaptation for Multimodal Large Language Models

- Decision: Accept
- Scores: 6, 6, 5, 6, 6

## Abstract
Despite  remarkable progress, existing multimodal large language models (MLLMs) are still inferior in granular visual recognition. Contrary to previous works, we study this problem from the perspective of image resolution, and reveal that a combination of low- and high-resolution visual features can effectively mitigate this shortcoming.  Based on this observation, we propose a novel and efficient method for MLLMs, termed \emph{Mixture-of-Resolution Adaptation} (MRA). In particular, MRA adopts two visual pathways for  images with different resolutions, where  high-resolution visual information is embedded into the low-resolution pathway via the novel \emph{mixture-of-resolution adapters} (MR-Adapters). This design also   greatly  reduces the input sequence length of MLLMs. To validate MRA, we apply it to a recent MLLM called LLaVA, and term the new model  \textit{LLaVA-HR}. We conduct extensive  experiments on 11 vision-language (VL) tasks, which show that LLaVA-HR outperforms existing MLLMs on 8 VL tasks, \emph{e.g.,} +9.4\% on TextVQA.  More importantly,    both training and inference  of LLaVA-HR remain efficient with MRA, \emph{e.g.,}  \textbf{\textit{20 training hours}} and  \textbf{\textit{3$\times$ inference speed}}  than LLaVA-1.5.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper aims to enhance MLLM by enlarging resolution of input images. By combining features from ViT and a CNN encoder through an adapter, performances of MLLM are improved a lot. Meanwhile, fusing high-resolution features from convolution-based encoder into low-resolution features from transformer-based encoder does not increase vision tokens to LLM decoder, so that additional computational cost is low. Proposed LLaVA-HR increases effective resolution for MLLM to 1024 and outperforms concurrent MLLMs.

### Strengths
This work proposed a novel method to increase resolutions of MLLMs, which is an important problem in the field and critical in fine-grained  vision tasks. Without large modification of training recipe and computational cost of its baseline, LLaVA-1.5. 
Evalutions are conducted on many existing benchmarks and performance of LLaVA-HR is quite impressive. Besides, the computational cost involved is quite small compared with related works.

### Weaknesses
Please see as in questions.

1. In section4.3(line 258), the statement, global average pooling is confusion, is the features are pooled into 1 global token? If so, it seems to be not consistent with figures. Please clarify the exact dimensions of fv after global average pooling.
2. In Table 1, resizing LLaVA-1.5 to 672 pix achieves close performance with 768pix version of LLaVA-HR, is there a direct comparision between 768-pix version of them?
3. In table 2, there is an ablation of "tune vision" referring to finetune vision encoder. However, I think the vision encoder in LLaVA-1.5 is fixed, can you provide a detailed description about this. For example, implementation and aim of tuning vision encoder.
4. LLaVA-HR is proposed to process input resolution of 1024, what if input images larger than 1024. Is there any extended experiments for even larger images such as 4K ones.
5. What do you mean by "stages" in vision transformers? And, currently only final features from ConvNext is utilized, is there any experiments of multi-stage feature integration for that of CNN encoder?

### Questions
1. In section4.3(line 258), the statement, global average pooling is confusion, is the features are pooled into 1 global token? If so, it seems to be not consistent with figures. Please clarify the exact dimensions of fv after global average pooling.
2. In Table 1, resizing LLaVA-1.5 to 672 pix achieves close performance with 768pix version of LLaVA-HR, is there a direct comparision between 768-pix version of them?
3. In table 2, there is an ablation of "tune vision" referring to finetune vision encoder. However, I think the vision encoder in LLaVA-1.5 is fixed, can you provide a detailed description about this. For example, implementation and aim of tuning vision encoder.
4. LLaVA-HR is proposed to process input resolution of 1024, what if input images larger than 1024. Is there any extended experiments for even larger images such as 4K ones.
5. What do you mean by "stages" in vision transformers? And, currently only final features from ConvNext is utilized, is there any experiments of multi-stage feature integration for that of CNN encoder?

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
In this paper, the authors propose the Mixture-of-Resolution Adaptation method to embed the high-resolution features into the low-resolution pathway. The MRA enhances the visual perception ability in MLLMs, and allow them to benefit from high-resolution visual inputs with reduced computational cost. Extensive experiments demonstrate the effectiveness of the MRA.

### Strengths
1. The paper is well-written and easy to follow.
2. The comparison of MRA and other high-resolution adaptation solutions is clear, highlighting the effectiveness of the dual visual pathways.
3. The experiments are well-conducted and quite comprehensive.
4. The study demonstrates strong performance on most datasets compared with other MLLMs.

### Weaknesses
1. In Table 1, the MRA is compared to other high-resolution adaptation methods that use a single visual pathway. However, the introduction of a new visual encoder in the MRA raises concerns about the fairness of this comparison. The performance gains could be attributed to the increased model capacity from the additional encoder rather than the proposed Mixture-of-Resolution Adapter itself. A more rigorous comparison would involve a baseline that also utilizes dual visual pathways, but without the MR-Adapter, to isolate the specific contribution of the adapter.
2. The analyses of the MRA’s architecture and design details are insufficient, particularly regarding $\mathcal{F}_l$, $\mathcal{F}_h$, and the gate function. The paper lacks a detailed exploration of why a convolutional layer is chosen for $\mathcal{F}_l$ and an MLP layer for $\mathcal{F}_h$. Furthermore, the specific role and impact of the gate function are not thoroughly investigated. Ablation studies should be conducted to evaluate the necessity and contribution of each of these components, including different choices of layers and activation functions within the gate.
3. The main novelty of the paper appears to be the Mixture-of-Resolution Adapter. While the application of dual visual pathways for high-resolution adaptation in MLLMs is innovative, the overall contribution of the paper seems somewhat insufficient. The core idea of fusing features from different resolutions is not entirely novel, and the paper does not sufficiently demonstrate a significant advancement over existing methods. If the MR-Adapter could integrate a wider variety of low- and high- resolution visual encoders, and explore more complex fusion mechanisms, its contribution would be significantly enhanced.

### Questions
1. There are several micro-designs in the Mixture-of-Resolution Adapter, including $\mathcal{F}_l$, $\mathcal{F}_h$, and the gate function. Why do we choose a conv layer for $\mathcal{F}_l$, an MLP layer for $\mathcal{F}_h$? Are these layers and functions necessary? Please provide some analyses.

2. In the Mixture-of-Resolution Adapter, the authors choose the addition operation to fuse features of different resolutions. (Deformable) Cross Attention is also an option. I wonder which method is better?

### Soundness
3

### Presentation
3

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
This paper presents a new approach for efficient multimodal large language models (MLLMs) by addressing the high computational cost of processing high-resolution images. The authors introduce Mixture-of-Resolution Adaptation (MRA), a method that combines both low- and high-resolution visual features to enhance model efficiency without compromising visual recognition quality. MRA uses two visual pathways: one for low-resolution and one for high-resolution images, with novel mixture-of-resolution adapters (MR-Adapters) that embed high-resolution information into the low-resolution pathway. This design significantly reduces input sequence length and computational load.

The authors apply MRA to the LLaVA model, resulting in an improved version called LLaVA-HR, which demonstrates superior performance across 15 out of 17 vision-language (VL) tasks, including a 5.2% increase in accuracy on TextVQA. Furthermore, LLaVA-HR maintains efficient training and inference times, showing improvements over LLaVA-NeXT.

### Strengths
1. The paper is well-written and easy to follow.

2. Figures 2 and 3 are effectively designed and enhance understanding of the framework.

3. The ablation study is solid to reveal the contribution of component.

### Weaknesses
 > ### 1. LImited performance imprvement.

The performance gains with MRA are modest. The low-resolution branch operates at 448×448, so the appropriate baseline is LLaVA-1.5 with 448-pixel resizing. Compared to this baseline, the improvements MRA achieves are minimal (e.g., +0.7 on VQA v2, +31 on MME, and +0.8 on POPE). Training cost and inference speed are also similar between MRA and LLaVA-1.5-448, reducing the practical benefit.

> ### 2. Limited novelty

The dual-pathway, high-and-low-resolution approach isn’t particularly new. Similar strategies have been explored in other works, such as Mini-Gemini and CogAgent, yet the authors do not compare their method with these models. Explicitly differentiating MRA from these approaches would help clarify its unique contributions.

> ### 3. Limited generalizability

The authors apply MRA solely to LLaVA-1.5. Expanding the evaluation to other MLLMs, like Qwen-VL, would strengthen claims of the method’s generalizability across architectures.

### Questions
> ### 1. Clarification on Visual Encoder Notation

In line 206, it states that $F_{I_l}$ and $F_{I_h}$ are visual encoders for high- and low-resolution images, which seems to be a typo. The correct notation should reflect that $F_{I_l}$ and $F_{I_h}$ correspond specifically to low- and high-resolution encoders, respectively.

> ### 2. MR-Adapter Placement in ViT Architecture

Figure 2 shows the MR-Adapter is applied starting from the second stage of the ViT architecture. Does this mean the initial stage of the ViT does not utilize high-resolution features? Clarifying this could help illustrate the feature extraction flow more clearly.

> ### 3. Implementation of LLaVA-1.5-448

For LLaVA-1.5-448, only the image resolution is modified at the fine-tuning stage. Have you considered modifying the visual backbone from ViT-336 to ViT-448 and retraining it for both pre-training and fine-tuning? This comparison could provide insight into performance differences when using higher resolution throughout the model’s entire training process.

> ### 4. $SEED^{img}$ Performance Comparison

Could you provide the $SEED^{img}$ performance for LLaVA-1.5, LLaVA-1.5-448, and LLaVA-NeXT? This metric would help evaluate relative image-processing capabilities across these models.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper focuses on the efficient high-resolution adaptation for multimodal large language models (MLLMs) and proposes a mixture-of-resolution adaptation (MRA) method for MLLMs. To be specific, the proposed MRA employs two visual pathways for images of different resolutions, where high-resolution visual information is embedded into the low-resolution pathway via the mixture-of-resolution adapters. Besides, the paper conducts extensive experiments to verify the effectiveness of the proposed model.

### Strengths
1. The paper aims to explore the high-resolution adaptation for MLLMs, which is crucial and engaging.
2. The paper is well written and easy to follow.
3. The paper is well motivated and the proposed MRA appears reasonable.

### Weaknesses
1. As demonstrated in Table 1, it seems that there is no significant gap between ‘Avg. Pooling’ and the proposed MRA for the VQAv2 task, which is perplexing. The paper should explain the experimental phenomenon.
2. The paper should carry out a qualitative experiment between the proposed MRA and the model variant in Table 2.
3. The paper fails to clarify the version of LLaVA-1.5 used in Figure 4.

### Questions
As mentioned, in Table 1, it seems that there is no significant gap between ‘Avg. Pooling’ and the proposed MRA for the VQAv2 task, which is perplexing. The paper should explain the experimental phenomenon.
2. The paper should carry out a qualitative experiment between the proposed MRA and the model variant in Table 2.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces an novel high-resolution adaptation method for multimodal large language models (MLLMs), termed Mixture-of-Resolution Adaptation (MRA). MRA employs a dual visual pathway design to process high- and low-resolution images simultaneously from both macro and micro perspectives, while integrating high-resolution information into the low-resolution pathway through the Mixture-of-Resolution Adapter (MR-Adapter). This approach reduces the number of visual tokens while preserving rich visual semantics, significantly enhancing the model's visual descriptive power.

### Strengths
- Unlike previous strategies that divide high-resolution images into sub-images, this paper introduces an innovative dual visual pathway structure, offering a fresh perspective for high-resolution adaptation. The MR-Adapter effectively embeds high-resolution information into the low-resolution pathway, introducing a new adaptation mechanism within the visual processing framework of MLLMs. This design overcomes the efficiency limitations of traditional high-resolution processing.

- The paper conducts extensive experiments across multiple vision-language tasks, providing a range of comparisons, with promising results.

- The writing is clear and easy to follow. It effectively highlights MRA's performance gains and efficiency advantages across different tasks, helping readers fully understand the model’s effectiveness and strengths.

### Weaknesses
1. The processing of both low-resolution and high-resolution images in the paper is mainly square-based, such as 448x448 and 1024x1024. Is there any adaptation mechanism for handling images with different aspect ratios? Would processing high-resolution images in a way that matches the input image's aspect ratio lead to better performance? Specifically, the paper does not discuss how the dual-pathway architecture handles non-square images, which is a common occurrence in real-world scenarios. The current approach of forcing square inputs might lead to information loss or distortion, particularly for images with extreme aspect ratios. A more detailed analysis of how the model performs with varying aspect ratios, and potential modifications to the architecture to handle them more effectively, would be beneficial.

2. For high-resolution image inputs, we are more focused on improvements in OCR-related tasks. The results for OCRVQA in Table 5 don’t seem to be the best. Additionally, Table 6 only presents results for LLaVA-HR+, but it lacks results for LLaVA-HR-7B, LLaVA-HR-13B, and LLaVA-HR-X with less training data. It would be helpful to include these results to better illustrate the impact of MRA on OCR-related tasks. The paper should provide a more comprehensive evaluation of the model's OCR capabilities across different model sizes and training regimes. The current results are not sufficient to fully demonstrate the effectiveness of MRA for OCR tasks, especially given the focus on high-resolution inputs where OCR performance is crucial. A more granular analysis of the OCR performance, including metrics beyond overall accuracy, would also be valuable.

3. Could the authors further explain why the MR-Adapter is inserted in the last 3 stages? What is the design principle behind this decision? Could it be inserted in the earlier stages instead? The paper lacks a detailed justification for the specific placement of the MR-Adapter within the network architecture. While the last 3 stages might be empirically optimal, a more thorough explanation of why this is the case, and why earlier stages are not suitable, is needed. This should include a discussion of the feature hierarchy within the ViT and how the MR-Adapter interacts with these features at different stages. A more in-depth analysis of the impact of MR-Adapter placement on the model's performance would strengthen the paper.

### Questions
See Weakness.

### Soundness
3

### Presentation
3

### Contribution
3
