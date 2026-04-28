# STABLE DIFFUSION MODELS ARE SECRETLY GOOD AT VISUAL IN-CONTEXT LEARNING

- Decision: Reject
- Avg Score: 5.33
- Scores: 5, 6, 5

## Abstract
Large language models (LLM) in natural language processing (NLP) have demonstrated great potential for in-context learning (ICL) -- the ability to leverage a few set of example prompts to adapt to various tasks without having to explicitly update model weights. 
ICL has recently been explored for the visual domain with promising early outcomes. These approaches involve specialized training and/or additional data which complicate the process and limit its generalizability. In this work, we show that off-the-shelf Stable Diffusion models can be re-purposed for visual in-context learning (V-ICL). Specifically, we formulate an in-place attention re-computation within the self-attention layers of the Stable Diffusion architecture that explicitly incorporates context between the query and example prompts. Without any additional fine-tuning, we show that this re-purposed Stable Diffusion model is able to adapt  to six different tasks: foreground segmentation, single object detection, semantic segmentation, keypoint detection,  edge detection, and colorization. 
For example, the proposed approach improves the mean intersection over union (mIoU) for the foreground segmentation task on Pascal-5i dataset by 8.9\% and 3.2\% over recent methods such as Visual Prompting and IMProv, respectively. Additionally, we show that the proposed method is able to effectively leverage multiple prompts through ensembling to infer the task better and further improve the performance across all tasks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper demonstrates that stable diffusion models, trained with vast amount of image data, are adept at in-context learning like the foundational LLMs. The paper heavily draws inspiration from Bar et al. Neurips 2022, where they demonstrated that generative models can be made to perform in-context learning with appropriate training. The proposed model leverages the power of diffusion model, effectively creating a form of cross-attention between query and prompt images and ground truth and proposing an approach to aggregate if multiple in-context prompts are provided.

### Strengths
The paper shows an interesting observation, that stable diffusion models, like foundational  LLMs are good at in-context learning, with subtle design choices and engineering. It showed better in-context learning compared to ImProv and VisualPrompting, although in fairness, they were using a weaker VQGAN models, which were not trained over vast data like diffusion. One key advantage of the proposed approach though, is exploiting the emergent properties of Diffusion Models rather than having to train Diffusion models to be able to do In-Context Learning.

### Weaknesses
Although the paper highlights an interesting emergent property of the diffusion model, my main concern is the lack of technical contributions. Diffusion models, in my opinion, inherently outperform VQGANs, as they have been trained on vast datasets and have shown excellent performance across various unsupervised tasks, such as keypoint detection (Hedlin et al., CVPR 2024), classification (Li et al., CVPR 2023), and segmentation (Tian et al., CVPR 2024). Additionally, using distinct key-query and value vectors as a form of cross-attention is quite common in models like VILBERT (NeurIPS 2019) and TRIBERT (NeurIPS 2022). Furthermore, we may observe similar in-context emergent properties with multi-modal LLMs like LLAVA or similar models, which highlight the strength of these models being trained on huge datasets. Overall, I disagree with the authors’ claim of a "novel pipeline" as a contribution. While the observation of in-context learning as an emergent property of diffusion is interesting, I believe it reflects the strengths of the diffusion model itself rather than a technical innovation by the authors.

### Questions
My major concern lies in the authors' technical contributions, as outlined in the weakness section, and in the fairness of comparing diffusion models with VQGAN-based models, given that diffusion models have already been shown to be superior. I would expect the authors to clarify their contributions more clearly.

My second concern is whether this emergent property is unique to diffusion models or if similar properties are observed in other VLMs or multi-modal LLMs, such as LLAVA.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper explores the adaptation of off-the-shelf Stable Diffusion models for visual in-context learning (V-ICL), demonstrating their capability to perform various visual tasks without explicit fine-tuning. By implementing in-place attention re-computation within the self-attention layers of the Stable Diffusion architecture, the model incorporates context between the query and example prompts. This approach effectively adapts the model to six out-of-domain tasks, including foreground segmentation and semantic segmentation, achieving significant performance improvements, such as an 8.9% increase in mIoU for foreground segmentation on the Pascal-5i dataset compared to recent methods. Inspired by feature ensembling in SegGPT, this method also leverages multiple prompts through implicitly-weighted prompt ensembling, enhancing performance across all tasks.

### Strengths
- **Originality:** The proposed traning-free visual in-context learning method is is highly innovative. It proposes a re-purpose technique on the self-attention layers of SD. It integrates attention map contrasting, swap-guidance, and AdaIn mechanisms to enhance prediction quality. While these techniques are inspired by existing work, they are effectively incorporated into the overall framework, contributing to the novelty of the approach.
- **Quality:** The primary innovative technique, in-place attention re-computation, is well-motivated and technically ssound. Experimental results validate its effectiveness, demonstrating a solid foundation for the proposed method.. 
- **Clarity:** The paper is well-written and clearly presented, making it easy for readers to understand the concepts and techniques involved..
- **Significance:** The proposed method significantly outperforms existing approaches on a variety of widely recognized out-of-domain tasks, underscoring the strong impact and benefits of this work.

### Weaknesses
 - **Comparison methods:** This work compares the proposed method against only two existing approaches, which limits the strength of the comparative analysis. Incorporating additional methods (on different tasks) for comparison would enhance the validity and robustness of the results.


### Questions
- SD-VICL involves numerous denoising steps, leading to significantly high inference times. While some studies outside the scope of in-context learning have shown that specific intermediate steps can yield satisfactory results. For instance, references [1] and [2] demonstrate effective outcomes for keypoint detection, while reference [3] focuses on semantic segmentation. Whether the proposed method could leverage a one-step adaptation approach to enhance efficiency without sacrificing performance?

_[1] Tang, L., Jia, M., Wang, Q., Phoo, C.P. and Hariharan, B., 2023. Emergent correspondence from image diffusion. Advances in Neural Information Processing Systems, 36, pp.1363-1389._   
_[2] Zhang, J., Herrmann, C., Hur, J., Polania Cabrera, L., Jampani, V., Sun, D. and Yang, M.H., 2024. A tale of two features: Stable diffusion complements dino for zero-shot semantic correspondence. Advances in Neural Information Processing Systems, 36._   
_[3] Barsellotti, L., Amoroso, R., Cornia, M., Baraldi, L. and Cucchiara, R., 2024. Training-Free Open-Vocabulary Segmentation with Offline Diffusion-Augmented Prototype Generation. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (pp. 3689-3698)._

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
5

### Summary
This paper shows that off-the-shelf Stable Diffusion models can be adapted for visual in-context learning (V-ICL) using in-place attention re-computation within self-attention layers. This method enables the model to leverage example prompts without fine-tuning and effectively adapts to six tasks, including segmentation and detection. Additionally, the approach utilizes multiple prompts through ensembling to improve task inference and overall performance. Experimental results show the effectiveness of this work.

### Strengths
1. The proposed method to perform the in-context inference is quite reasonable.
2. The studied topic is quite interesting, and I believe visual in-context learning is a critical issue.
3. The overall demonstration is good.

### Weaknesses
My major concern is the experimental parts, where I believe there many experiments shall be added.

1. The compared baseline methods are not enough. The author only made comparison with IMProv and MQ-VAE, How about SegGPT, Painter, and LVM? Besides, the results without specifically retrieval process are required to demonstrate the overall performance of the proposed methods. After all, this paper does not target on the design of best-demonstration selection. Finally, the selection-based methods (implemented based on MQ-VAE), such as UnsupPR, SupPR [1], prompt-SelF [2] and InMeMo [3] shall also be compared. 

2. The second one goes to the generalization of this model. As shown in this paper, merely some discriminative tasks are made, where the major of them fall into the discriminative recognition task. I believe for visual ICL or ICL, the most importance point is the generalization. Therefore, more tasks, such as low-light enhancement and in-painting,  are encouraged (Please refer to Painter as a demonstration). Or alternatively, more advanced single-task could be implemented. For instance, SegGPT is able to Segment Anything with the given demonstration, in this way, this model targets on maximizing the potential of the segmenting task. I think either these trials could further demonstrate the effectiveness of the proposed method. In other words, in context for task-specific generalization (SegGPT), or for wide range-of representative tasks (Painter, LVM). 

3. Fairly speaking, stable diffusion is not a pure Visual model instead of a multi-modal model. Therefore, I think more advanced multi-modal models could also be discussed, such as EMU. With the support of text, the in-context learning could be performed with more fancy operation. Regarding this aspect, the proposed method, emphasizing on visual side, is not implemented as expected since the usage of text seems to be overlooked.

### Questions
None

### Soundness
2

### Presentation
2

### Contribution
1
