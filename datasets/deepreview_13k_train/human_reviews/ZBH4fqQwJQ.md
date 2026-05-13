# Contrastive guidance and feedback: A Suitable way to improve 3D Consistency of Multi-view Diffusion Model

- Decision: Reject
- Scores: 5, 5, 6, 3

## Abstract
Recently, diffusion models have shown potential in 3D generation tasks, and the novel view synthesis (NVS) task, a bridge between 2D and 3D generation, has received great attention. The goal of the NVS task is to generate multi-view images from reference images, and the core challenge is to maintain the 3D consistency between different view images.
Recent works construct large 3D consistency multi-view image datasets and utilize the supervised fine-tuning (SFT) method to improve the 3D consistency. However, the SFT method suffers from the distribution shift, data inefficient problems, and lacks theoretical insight. To solve these problems, we discuss how to provide a suitable direction to the multi-view models and achieve better performance. More specifically, we first analyze the training-free guidance-based method and prove that contrastive guidance, which contains ground-truth and generated samples, can provide the right direction to improve 3D consistency. Based on the theoretical insight, we further design a contrastive 3D consistency metric and use it as the feedback in the following phase. To avoid the distribution shift problem, we use direct preference optimization (DPO) to fine-tune the multi-view diffusion models. Through qualitative and quantitative experiments, we demonstrate that after the fine-tuning phase with the above method, the 3D consistency of the multi-view images is significantly improved and achieves better performance compared to the SFT method.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes a novel approach to enhance 3D consistency in multi-view diffusion models by applying Direct Preference Optimization (DPO) with a specially designed 3D consistency metric that employs a contrastive strategy. Additionally, it provides theoretical proof for the use of contrastive guidance, demonstrating that trivial guidance cannot guarantee 3D consistency.

### Strengths
1. The application of DPO-based optimization and designing 3D consistency metric to multi-view diffusion models is both novel and intriguing.

2. A strong theoretical foundation for the use of a contrastive strategy, which is particularly valuable given that 3D generation often lacks comprehensive theoretical grounding.

### Weaknesses
1. Experimental validation of 3D guidance:
i) Showing the extent of performance improvement and the limitations of using only guidance would support the argument that while 3D guidance achieves better consistency than trivial guidance, it is not sufficient, necessitating fine-tuning.
It would be helpful to include experimental results demonstrating how well 3D guidance works during the inference phase. 

ii) Additionally, if 3D guidance is effective, why does it not work well on pre-trained multi-view diffusion models without additional fine-tuning? It would be interesting to see how this guidance performs when applied to a general pretrained multi-view diffusion model. Clarifying the general applicability of guidance would add value.

2. Clarity of the connection between Guidance and Fine-tuning:
While the role of guidance is well-explained, a clearer explanation of how it connects to the use of contrastive loss during fine-tuning would be beneficial. Enhancing the logical connection between guidance and fine-tuning could help readers better understand how these two components synergize. As mentioned in line 397, transitioning from stating that guidance cannot achieve ultimate improvements to using fine-tuning may feel abrupt and could be explained more smoothly.

3. Complexity in writing:
The writing in the paper is somewhat difficult to follow. It might be helpful to explain the DPO for the Multi-view Diffusion Models section earlier in conjunction with Figure 2 to improve clarity.

4. The advantages of the proposed method are not clear:
i) The experimental setup does not fully demonstrate the advantages of the proposed method. Specifically, it would be valuable to explain clearly how using DPO + contrastive loss outperforms existing multi-view diffusion methods in terms of performance or resource efficiency.

ii) It is also unclear why the experiments do not include comparisons with the latest SOTA models and instead only use models trained by the authors. There are several models that outperform SyncDreamer, and comparing against these would provide a stronger case for the proposed method. Additionally, a comparison with CARV3D, which uses RLFT, would be essential for a more comprehensive evaluation.

### Questions
1. Could you clarify what is meant by "unfriendly to users" in 053?
2. In line 689, it is mentioned that the training took "400 A100 days." 
3. The images in Figure 2 appear to include examples such as construction vehicles and forklifts. It is correct to add two different object types in Figure 2?

### Soundness
2

### Presentation
2

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
This work addresses the challenge of maintaining 3D consistency in the novel view synthesis (NVS) task. The authors analyze a training-free, guidance-based method and demonstrate that contrastive guidance can effectively enhance 3D consistency. Based on this insight, they design a contrastive 3D consistency metric and incorporate it as feedback in the subsequent phase. Additionally, a Direct Preference Optimization (DPO) procedure is proposed to fine-tune multi-view diffusion models. Qualitative and quantitative results are presented, comparing the proposed method to the supervised fine-tuning (SFT) approach, demonstrating its effectiveness.

### Strengths
The motivation of the paper is clear and well-founded, with a detailed theoretical analysis provided. The solution derived by the authors is theoretically sound and logically consistent.

The paper is well-written and presented.

### Weaknesses
As 3D consistency is a primary focus of this work, the absence of reconstruction from synthesized multi-view images limits the evaluation of 3D consistency. This type of assessment is crucial to demonstrate the robustness of the proposed approach in maintaining consistent geometry across multiple views.

The showcased results are limited, focusing primarily on the eye and multi-object problems. To better evaluate the method's effectiveness, objects with more complex appearances and geometries should also be tested.

### Questions
The authors avoided running COLMAP on the generated multi-view images, stating that they only produced orthographic views, which were insufficient for the algorithm. However, why not generate a greater number and variety of images to ensure sufficient data for running COLMAP and fully evaluate the 3D consistency of the method?

The authors adopt DINOv2 to obtain embeddings of the reference image. Would using an image encoder with a stronger 3D prior knowledge (e.g., CroCo or DUSt3R) lead to improved performance?

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
3

### Summary
This paper presents a novel approach to enhance multi-view diffusion models using Direct Preference Optimization (DPO). The authors first analyze training-free guidance methods, demonstrating that contrastive guidance in real and generated images during the guidance process helps improve 3D consistency. By using ground-truth multi-view images and the reference image as positive pairs,  images generated by Zero123  and reference images as the negative samples, and utilizing a fine-tuned DINOv2 model as evaluation model. Both qualitative and quantitative experiments validate the effectiveness of their DPO-based method.

### Strengths
- The authors provide a fully theoretical proof to demonstrate the effectiveness of their method, and the experimental results also provide strong support for their theory.
-  Instead of using large reconstruction models as reward model, this paper just use the diffusion model's ouptuts as negative samples. It's quite simple and efficient, which can be easily adapted to other models.
- The visual results demonstrate that the method can effectively addresses a key limitation in multi-view generation, where models trained directly with SFT fail to generate reasonable views. This is a significant problem in the field.

### Weaknesses
 -  Both methods (SFT and DPO) score about the same on technical metrics like LPIPS, SSIM, and PSNR. Adding some human feedback evaluation would help us get a better picture of which one actually works better.


### Questions
Would using different models (besides Zero123), such as Zero123++, as sources of negative samples produce different effects on the results? Since SyncDreamer's base model was trained on Zero123, would using outputs from other models have any significant impact?

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
3

### Summary
This paper proposes a new method to improve the multiview consistency of multiview diffusion models.
The proposed method first trains a multiview diffusion model using 3D ground-truth data. 
Then, the method is further optimized with a direct preference optimization (DPO) loss without requiring ground truth.
This DPO will utilize a contrastive learning-based model to determine the preference of the generated images, where multiview consistent images will be preferred.
Experiments demonstrate the DPO improves the consistency in the multiview generation.

### Strengths
The paper combines the multiview diffusion model (MVDream, SyncDreamer), DPO (D3PO), and contrastive learning to design a new multiview generation framework. The framework is novel to me.

### Weaknesses
1. The main weakness is the writing of the paper. I can understand Section 3, which introduces the existing techniques like diffusion, D3PO, and multiview diffusion. Section 4 seems to be the key idea of the paper but I cannot understand it.
1) What is X^{3D}? I'm not sure whether this means a 3D model or multiview images here.
2) Why X^3D can be represented by a linear transformation of Gaussian noise in assumption 1? Both definitions seem not to be valid here. 
After that, I totally get lost in the rest discussion of the section.
2. Experiments are not convincing enough. The best way to evaluate the multiview consistency is to conduct 3D reconstruction from the generated multiview images and check the quality of the 3D reconstruction. However, only some NVS metrics like PSNR are provided in the experiments. 
3. Meanwhile, the experiment lacks comparison with recent multiview diffusion models like Era3D, Zero123++, etc. Does the proposed framework also work on these new models?
4. The proposed method seems to be an incremental combination of three existing works. The motivation for introducing the RLFT in multiview diffusion models is to resolve the domain-shifting problem. However, the evaluation seems still to be synthetic images, which does not support the claim here.

### Questions
Refer to weaknesses.

### Soundness
2

### Presentation
1

### Contribution
2
