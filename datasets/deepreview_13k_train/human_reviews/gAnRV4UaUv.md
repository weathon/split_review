# ISCUTE: Instance Segmentation of Cables Using Text Embedding

- Decision: Reject
- Scores: 6, 6, 3

## Abstract
In the field of robotics and automation, conventional object recognition and instance segmentation methods face a formidable challenge when it comes to perceiving Deformable Linear Objects (DLOs) like wires, cables, and flexible tubes. This challenge arises primarily from the lack of distinct attributes such as shape, color, and texture, which calls for tailored solutions to achieve precise identification.
In this work, we propose a foundation model-based DLO instance segmentation technique that is text-promptable and user-friendly. Specifically, our approach combines the text-conditioned semantic segmentation capabilities of CLIPSeg model with the zero-shot generalization capabilities of Segment Anything Model (SAM). We show that our method exceeds SOTA performance on DLO instance segmentation, achieving a mIoU of $91.21\%$. We also introduce a rich and diverse DLO-specific dataset for instance segmentation.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes an instance segmentation framework of cables built on top of CLIPSeg and segment anything model (SAM). By adding learnable adapters for prompt and class, the proposed model is able to achieve good zero-shot generalization capability. Experiments on several datasets show that the proposed approach outperforms several existing methods by a large margin and is relatively robust under different parameter settings.

### Strengths
The proposed approach is relatively straightforward as it is a direct application of CLIPSeg and SAM models to a high specific domain. The main idea of adding adapters is technically sound and also aligns well with the problem setting as in nature well labeled cable images are not easy to acquire. This validates the choice of using adapters in this approach instead of a full fine-tuning. In this sense, the proposed approach is reasonably motivated.

In addition, adding text prompt to the model allows for more flexibility compared to a vision only model. This also improves the zero-shot generalization.  

Despite its simpleness, the proposed approach already works well on some data and outperforms existing approaches.

### Weaknesses
This work is overall good without significant flaws, but I do want to mention that it is more an application of existing models to a new domain with some modifications than a novel approach. The way of using these models is relatively straightforward. However, there still are a few questions to be answered. Please see detailed comments below.

- Although the experiments have shown that the proposed approaches work well in many cases, it is still unclear how well it can generalize. The dataset used for evaluation consists of only 4 colors and all images are high resolution (1920x1080), and cables are placed at a similar distance to the camera and there is limited appearance variation. This can be seen from both training and validation data. This simplifies the problem a lot and can affect the performance of the model when it is tested on more realistic scenarios. For example, when there are "cables in the wild" which have diverse colors and are twisted with each other, or far away from the camera, or have large appearance variance in the training and testing sets, the proposed model may fail. It would be helpful to see how the model performs under this case, so that readers have a better understanding of its behavior on different data.

- The text prompts evaluated are quite limited. Only 3 choices are used, which seem not have enough coverage. In addition, all the 3 text prompts are single words that behave as class labels. Given that both the CLIPSeg and SAM model are very strong at recognizing a broad range of textual concepts. I would like to know how the proposed model reacts towards more complex, detailed text prompts - whether this could improve or reduce the model quality.
In page 7, the authors claim "we observe that the model generalizes better if it is trained using augmentations in the dataset". However, the improvement is very marginal on some data, e.g., from 97.01 to 97.71, which is larger on some other data. Any explanation to that?

- Some sentences are broken:
   - In Section 2.2, "However,Struggingle to" should be corrected. 
   - In Section 2.2, "its prompt encoder with a single capable" should be corrected.

### Questions
- Although the experiments have shown that the proposed approaches work well in many cases, it is still unclear how well it can generalize. The dataset used for evaluation consists of only 4 colors and all images are high resolution (1920x1080), and cables are placed at a similar distance to the camera and there is limited appearance variation. This can be seen from both training and validation data. This simplifies the problem a lot and can affect the performance of the model when it is tested on more realistic scenarios. For example, when there are "cables in the wild" which have diverse colors and are twisted with each other, or far away from the camera, or have large appearance variance in the training and testing sets, the proposed model may fail. It would be helpful to see how the model performs under this case, so that readers have a better understanding of its behavior on different data.

- The text prompts evaluated are quite limited. Only 3 choices are used, which seem not have enough coverage. In addition, all the 3 text prompts are single words that behave as class labels. Given that both the CLIPSeg and SAM model are very strong at recognizing a broad range of textual concepts. I would like to know how the proposed model reacts towards more complex, detailed text prompts - whether this could improve or reduce the model quality.
In page 7, the authors claim "we observe that the model generalizes better if it is trained using augmentations in the dataset". However, the improvement is very marginal on some data, e.g., from 97.01 to 97.71, which is larger on some other data. Any explanation to that?

- Some sentences are broken:
   - In Section 2.2, "However,Struggingle to" should be corrected. 
   - In Section 2.2, "its prompt encoder with a single capable" should be corrected.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a novel structure for DLO instance segmentation, taking advantages of SAM and CLIPSeg. Via an adapter model, the proposed method can provide SAM with proper prompts for generating DLO masks. The overall framework achieves state-of-the-art performance on DLO-specific datasets, providing a new direction of solving DLO segmentation problems.

### Strengths
（1）The proposed method combines SAM with text conditions, and constructs a prompt encoder to help improve the overall DLO segmentation abilities.
（2）The proposed method achieves state-of-the-art performance compared with other recent algorithms on DLO instance segmentation.

### Weaknesses
（1）It seems that the proposed method relies on the assumption that if properly prompted, SAM can always provide correct cable segmentation masks. As the authors claimed, the performance upper-bound is limited by SAM and CLIPSeg. I wonder what is the exact upper-bound of these two methods, and how close can the proposed method reach this bound? Specifically, it is unclear how the prompt encoder is optimized to generate prompts that consistently lead to accurate segmentation by SAM, especially given the variability in cable appearance and background clutter. The paper lacks an analysis of failure cases where the generated prompts lead to suboptimal masks, which is crucial for understanding the limitations of the approach.
（2）Run-time for each method is not evaluated and analyzed in Table 1 and 2. This makes it difficult to assess the practical applicability of the proposed method, especially in real-time scenarios. It is essential to provide a detailed breakdown of the computational costs associated with each component of the pipeline, including the prompt encoder, SAM, and CLIPSeg, to understand the bottlenecks and potential areas for optimization.
（3）Typo in Section 2.2: ” ... that have historically have been difficult to segment ...”

### Questions
(1) What is the exact upper-bound of these two methods, and how close can the proposed method reach this bound?
(2) How much time  does the proposed method need to take for DLO segmentation?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes an adapter model for encoding the text prompts to point prompts and filtering the masks generated by SAM. It achieves 91.21% mIoU on the DLO benchmark.

### Strengths
- Proposed a prompt encoder network to obtain point prompts from text prompts by CLIPSeg.
- Proposed a binary classifier network for the quality of SAM-generated masks.
- Achieved a solid result.

### Weaknesses
 - Utilizing the combination of two powerful models, CLIPSeg and SAM, may be effective but not novel. The paper lacks a clear explanation of how the proposed method significantly advances the state-of-the-art beyond simply combining existing tools. The novelty is further diminished by the lack of a clear problem statement that justifies the need for a new method. 
- The design motivation in the 3.1.2 section (i.e., MLP, cross-attention, self-attention) is missing. The paper does not provide a rationale for the specific architecture choices within the adapter network. The selection of MLP, cross-attention, and self-attention modules seems arbitrary without a discussion of their individual roles and contributions to the overall performance. The lack of justification makes it difficult to understand why this particular combination was chosen over other possible architectures.
- Few baselines. The only other method mentioned is RT-DLO. Considering the author is leveraging strong semantic segmentation methods, including SAM, they should compare their method with those segmentation methods. The paper's evaluation is limited by the lack of comparison with relevant baselines. Specifically, the absence of comparisons with established semantic segmentation methods like DeepLab or Mask R-CNN, especially given the use of SAM, makes it difficult to assess the true contribution of the proposed method. The comparison with only RT-DLO is insufficient to demonstrate the superiority of the proposed method in a broader context.
- No ablation studies were conducted. The paper lacks any analysis of the individual components of the proposed method. Without ablation studies, it is impossible to determine the contribution of each module (e.g., the prompt encoder, the mask classifier) to the overall performance. This absence makes it difficult to understand the importance of each component and to identify potential areas for improvement.

### Questions
- Please explain the motivation for components proposed in the 3.1.2 section.
- Please compare the proposed method with SAM, CLIPSeg, and other strong segmentation models by inference on DLO benchmarks.
- Please conduct ablation studies, including quantitative and qualitative analysis.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor
