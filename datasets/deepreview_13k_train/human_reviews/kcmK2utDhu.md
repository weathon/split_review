# MV-Adapter: Multi-view Consistent Image Generation Made Easy

- Decision: Reject
- Scores: 6, 6, 6, 6, 5

## Abstract
Existing multi-view image generation methods often make invasive modifications to pre-trained text-to-image (T2I) models and require full fine-tuning, leading to (1) high computational costs, especially with large base models and high-resolution images, and (2) degradation in image quality due to optimization difficulties and scarce high-quality 3D data.
In this paper, we propose the first adapter-based solution for multi-view image generation, and introduce MV-Adapter, a versatile plug-and-play adapter that enhances T2I models and their derivatives without altering the original network structure or feature space.
By updating fewer parameters, MV-Adapter enables efficient training and preserves the prior knowledge embedded in pre-trained models, mitigating overfitting risks.
To efficiently model the 3D geometric knowledge within the adapter, we introduce innovative designs that include duplicated self-attention layers and parallel attention architecture, enabling the adapter to inherit the powerful priors of the pre-trained models to model the novel 3D knowledge.
Moreover, we present a unified condition encoder that seamlessly integrates camera parameters and geometric information, facilitating applications such as text- and image-based 3D generation and texturing.
MV-Adapter achieves multi-view generation at 768 resolution on Stable Diffusion XL (SDXL), and demonstrates adaptability and versatility.
It can also be extended to arbitrary view generation, enabling broader applications.
We demonstrate that MV-Adapter sets a new quality standard for multi-view image generation, and opens up new possibilities due to its efficiency, adaptability and versatility.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes a novel module called MV-Adapter, designed as a plug-and-play solution for enhancing pre-trained text-to-image (T2I) models in multi-view image generation. 

MV-Adapter addresses key limitations of existing methods, such as high computational costs, incompatibility with model derivatives, and limited versatility. By integrating with T2I models without invasive modifications or full-parameter training, MV-Adapter enables efficient high-resolution synthesis while maintaining compatibility with various extensions and derivatives like personalized models and plugins. 

It supports diverse conditioning signals, facilitating applications in text and image-based 3D generation and texturing. Experiments show that MV-Adapter sets a new standard in generating multi-view consistent images, combining efficiency, adaptability, versatility, and high performance.

### Strengths
- MV-Adapter streamlines the training process by eliminating full fine-tuning, enabling efficient high-resolution image generation with reduced computational costs.

- MV-Adapter seamlessly integrates with various derivatives and extensions of the base T2I model, such as personalized models and plugins like ControlNets, enhancing its versatility across different applications.

- MV-Adapter supports diverse conditioning inputs (e.g., text, images, geometry), and MV-Adapter broadens the scope of multi-view generation and ensures consistent, high-quality output across various tasks.

### Weaknesses
I would like to positively acknowledge that the results are impressive. 
- However, the weakness I found in this paper is that the contributions seem somewhat limited. The main contribution appears to be the application of self-attention, and if there are other contributions, could you revise the paper to emphasize those points? It would be helpful to clearly explain what differentiates this work from existing self-attention methods in multi-view generation, and what new methods, beyond self-attention, have been introduced in this paper.

- Additionally, I believe that including an evaluation comparing parallel and serial architectures would make this a stronger paper. Conducting an ablation study to compare the proposed parallel architecture with a serial architecture and evaluating generation quality, multi-view consistency, and computational efficiency would be beneficial.

- Overall, since the consistency of the results is good, enhancing the novelty aspect would make this a better paper. What is the novelty of this paper compared to existing multi-view generation methodologies? Furthermore, mentioning the potential applicability of this paper and highlighting potential new applications would also be helpful.

### Questions
It has been stated in the Weaknesses section. I hope the authors will address these points in the rebuttal session.

### Soundness
3

### Presentation
4

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
This paper introduces MV-Adapter, a plug-and-play module for text-to-image diffusion models that facilitates efficient 6-view image generation with multiple conditions. MV-Adapter overcomes the limitations of existing methods, such as high computational costs, incompatibility with T2I derivatives, and limited versatility in handling various conditioning signals. It achieves this through a condition guider that processes camera pose or geometry information and a decoupled attention mechanism that incorporates multi-view and image cross-attention. The authors evaluate MV-Adapter on various T2I models and derivatives, demonstrating its effectiveness in generating high-quality multi-view images from text, image, or geometry prompts.

### Strengths
1: The paper is well-written and easy to follow.

2: The motivation is straightforward and intuitive. The study explores various design choices for text-to-multi-view diffusion models, making progress in all examined aspects.

3: The experiments are solid. Qualitative results showcase promising visual fidelity and view consistency across various T2I models and tasks. Quantitative evaluation also demonstrates competitive performance compared to baselines.

### Weaknesses
1: A key limitation is the fixed 6-view output of MV-Adapter. While sufficient for some tasks, it falls short compared to video-diffusion models like Emu-Video used in im-3d and vfusion3d (16 views) or SV3D (20 views). Additionally, MV-Adapter cannot synthesize novel views from arbitrary angles, a capability demonstrated by SV3D and Cat3D. This restricts its use in applications requiring more comprehensive 3D understanding or flexible viewpoint control.

2: The quantitative improvements over baselines appear modest (with GSO image-to-multi-view). More compelling evidence is needed to showcase the impact of MV-Adapter. A user study or an anonymous webpage hosting video comparisons for direct assessment would strengthen these claims.

3: Minor: The proposed components draw heavily from existing work, which may lead to a perceived lack of novelty. The condition guider is inspired by T2I-Adapter, and the decoupled attention borrows from Era3D.

### Questions
1: The paper primarily focuses on generating a fixed set of views. Did the authors considered enabling novel view synthesis with arbitrary viewing angles, similar to methods like SV3D or Cat3D? If so, how to envision adapting MV-Adapter to achieve this?

2:  Could the authors please provide more details about the experimental setup for the image-to-multiview comparison on the GSO dataset? Specifically, how many gso assets are used? Did top/bot views covered for evaluation?

I am currently leaning towards a weak rejection (more like a 4 score), and my final recommendation hinges on the authors' response to the raised weaknesses and questions in their rebuttal. Specifically, I would appreciate a discussion on the possibility of extending MV-Adapter to handle arbitrary viewpoints and a more in-depth analysis of the quantitative results.

After the rebuttal, I would like to recommend a borderline acceptance for this submission.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces MV-adapter, a plug-and-play module for pretrained T2I models, enabling them to support multi-view generation. Beyond the base image generation models, the proposed adapter can be integrated with other custom models, such as ControlNet. It allows for camera pose guidance, geometry guidance, and can optionally use an image as a condition. The authors conduct extensive experiments on various use cases and perform ablation studies to investigate network design choices.

### Strengths
1. The paper is well-written, clearly organized, and easy to follow.
2. The experiments are comprehensive. The proposed method is tested on multiple base networks, including SD2.1, SDXL, and other fine-tuned models derived from these two.
3. The proposed method supports both geometry-guided and camera pose-guided generation, significantly expanding its potential real-world applications.
4. The module can be integrated with ControlNet, reusing the control signals learned from ControlNet.

### Weaknesses
While I do not observe any major weaknesses in the paper, I still have some questions regarding the implementation and experimental details:

1. The paper does not provide much detail about the T2I-UNet used for image cross-attention. Is this UNet identical to the diffusion UNet? What timestep is used for feature extraction?

2. The proposed method is very similar to T2I-adapter in terms of network structure. Can the MV-adapter be combined with a learned T2I-adapter, similar to ControlNet?

3. How is the CFG calculated at inference time, since the network now has multiple conditions.

### Questions
Please refer to the weaknesses listed above.

### Soundness
4

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
4

### Summary
This paper introduces MV-Adapter, a plug-and-play adapter designed to support various conditions when generating multi-view consistent images. It preserves the base T2I model’s priors, improving efficiency by eliminating the need for constant full fine-tuning. Additionally, MV-Adapter supports multiple conditioning inputs, enhancing versatility. All the contributions above make the performance better.

### Strengths
1. MV-Adapter supports various conditions, which provides a possible solution for multi-view generation with more conditional control.
2. MV-Adapter is more efficient and has less training costs according to the data shown in the paper.

### Weaknesses
1. The paper does not present the metrics results of 3D reconstruction using the generated multiviews, a downstream task that most directly reflects the consistency of the generated views. It would be beneficial to include evaluations using standard 3D reconstruction metrics such as volumetric IoU or Chamfer distance. This would provide quantitative insights into the multi-view consistency and help validate the quality of the generated outputs.
2. The proposed “image cross-attention” mechanism is not novel, as it has already been employed in Zero123++. It would be helpful to explicitly compare the proposed method with the implementation in Zero123++, focusing on any specific differences or improvements.

### Questions
1. How does the result of reconstructing 3D with MV-Adapter method compare with other multi-view generation methods? Does it offer any distinct advantages, or are there potential limitations that need to be addressed?
2. I noticed that the paper does not mention whether the text captions used for training are sourced directly from the Cap3D dataset or if they were separately annotated by the authors. Could you clarify the origin of these text captions.
3. For multi-view generation, the primary focus should be on the quality of the generated outputs rather than merely reducing the number of trainable parameters. I am curious how the model would perform if subjected to full-model fine-tuning while keeping the current design unchanged. This could further validate the architecture by demonstrating that comparable results can be achieved without the need to fine-tune all parameters, providing additional insights into the effectiveness of the proposed design.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a new method for consistent multi-view image generation. The proposed method followed the core idea of T2I-Adapter and made some extensions to it (e.g., conditions, training data) to be applied to the multi-view image generation task. The experimental results demonstrate the effectiveness of the proposed method.

### Strengths
- This paper is well-written and easy to follow.
- The results are visually pleasing and show improvement against previous methods.

### Weaknesses
 - My major concern is that the technical contributions of this paper are a bit thin. Specifically, this paper can be viewed as an extension of T2I-Adapter [1] to the consistent multi-view image generation task. Therefore, most of the merits of the proposed method (e.g., efficiency, adaptability, versatility, performance) are inherited from the T2I-Adapter but are not original. The true contributions of this paper are actually the modifications to T2I-Adapter, which are incremental.

[1] Mou, C., Wang, X., Xie, L., Wu, Y., Zhang, J., Qi, Z. and Shan, Y., 2024, March. T2i-adapter: Learning adapters to dig out more controllable ability for text-to-image diffusion models. In Proceedings of the AAAI Conference on Artificial Intelligence (Vol. 38, No. 5, pp. 4296-4304).

- For the modifications to T2I-Adapter, the conditions (Sec. 4.1) and attentions (Sec. 4.2) are mostly borrowed from previous works (the references are included in the paper) and there are no significant new insights as well.

Therefore, I think the paper is publishable but maybe not at a top conference like ICLR.

### Questions
Please see the weaknesses mentioned above.

### Soundness
3

### Presentation
3

### Contribution
2
