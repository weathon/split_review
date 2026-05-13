# SG-I2V: Self-Guided Trajectory Control in Image-to-Video Generation

- Decision: Accept
- Scores: 5, 6, 5, 6, 6

## Abstract
Methods for image-to-video generation have achieved impressive, photo-realistic quality. 
However, adjusting specific elements in generated videos, such as object motion or camera movement, is often a tedious process of trial and error, e.g., involving re-generating videos with different random seeds. 
Recent techniques address this issue by fine-tuning a pre-trained model to follow conditioning signals, such as bounding boxes or point trajectories. 
Yet, this fine-tuning procedure can be computationally expensive, and it requires datasets with annotated object motion, which can be difficult to procure. 
In this work, we introduce SG-I2V, a framework for controllable image-to-video generation that is self-guided---offering zero-shot control by relying solely on the knowledge present in a pre-trained image-to-video diffusion model without the need for fine-tuning or external knowledge. 
Our zero-shot method outperforms unsupervised baselines while significantly narrowing down the performance gap with supervised models in terms of visual quality and motion fidelity.
Additional details and video results are available on our project page: \url{https://kmcode1.io/Projects/SG-I2V}.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper introduces SG-I2V, a self-guided method designed to achieve zero-shot controllable image-to-video (I2V) generation. Technically, SG-I2V first extracts feature maps from the self-attention module during the video denoising process. To ensure that the generated video’s motion aligns with the given trajectory, the input latent code is optimized by enforcing cross-frame feature consistency along the bounding box trajectory. Furthermore, to preserve the quality of the generated video, the authors propose a post-processing method that retains the high-frequency components of the original latent code. The evaluation on the VIPSeg dataset demonstrates the effectiveness of the proposed method.

### Strengths
S1: The paper analyzes the intrinsic relationship between the motion in the generated video and the UNet feature maps. 

S2: Building on this analysis, a self-supervised framework is designed to achieve zero-shot controllable image-to-video (I2V) generation.

### Weaknesses
W1: The performance values reported in Table 1 on the VIPSeg dataset differ from those in the DragAnything paper, which reports ObjMC, FVD, and FID values of 305.7, 494.8, and 33.5, respectively. Additionally, Table 1 shows DragNUWA outperforming DragAnything, which contradicts the findings in the DragAnything paper. Could the authors clarify the specific versions of DragAnything and DragNUWA used in their experiments, any differences in their evaluation setup compared to the original papers, and whether they used the same evaluation code and metrics? This information would help pinpoint the source of these discrepancies and ensure a fair comparison.

W2: Generally, in the field of video generation, the FVD and FID metrics often exhibit similar trends. I’m curious why SG-I2V performs worse than DragNUWA in FVD (by approximately 45 points) while showing better performance in FID (by about 2 points). Additionally, there seems to be a notable gap between SG-I2V and the best supervised method, with differences of around 45 in FVD and 3.6 in ObjMC. This disparity is quite significant, yet the paper describes the results as "competitive," which appears to be an overstatement.

W3: There is a discrepancy between Table 1 and Figure 4. According to the results in Table 1, SG-I2V performs worse than DragNUWA, while Figure 4 suggests that SG-I2V performs better, leading to contradictory information between the two experiments. Additionally, since DragAnything focuses on entity control, it may be more objective to include a comparison of entity control performance. Furthermore, the primary focus of the comparisons in this paper seems to be on zero-shot methods. Therefore, it would be beneficial for Figure 4 to include a comparison of visual quality with those zero-shot approaches as well.

W4: In the zero-shot baselines, the methods FreeTraj and DragDiffusion are not complete versions of the original models, therefore, more implementation details should be provided. Additionally, the original DragDiffusion model supports drag-based image editing, making it necessary to directly present the model’s performance results in video generation (by dividing the trajectory into 15 segments and running DragDiffusion on each segment individually). 
Furthermore, since DragDiffusion requires an edit region as input, how should this input be provided appropriately to ensure a fair comparison?

W5: Some modules may not appear particularly novel from a technical perspective. For instance, the method of optimizing the input latent code to control the layout of video generation is a technique that has been widely utilized in various zero-shot controllable generation papers.

### Questions
Q1: The paper proposes optimizing the input latent code and applying high-frequency preserved post-processing between steps 30 and 45 during the denoising process. The inference time required to generate a 14-frame video should be reported.

Q2: I am curious why the modified spatial self-attention mentioned in Section 3.2 shows better alignment with the initial frame. A more detailed explanation would be helpful. Additionally, after modifying the self-attention in SVD, there is a gap between the modified inference pattern and the original learnt pattern, could this affect the quality of video generation? It would be beneficial to evaluate the change in FVD for I2V generation before and after modifying the self-attention in SVD. 

Q3: I hope the authors can address the concerns raised in the "Weaknesses" section.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a training-free, self-guided trajectory control framework for image-to-video generation, named SG-I2V. The authors also design operations for semantically aligned feature map extraction, trajectory enforcement, and high-frequency preservation in post-processing, which together constitute the SG-I2V framework. Additionally, comprehensive experiments are conducted to demonstrate the effectiveness of SG-I2V and the impact of specific parameters in SG-I2V.

### Strengths
This paper exhibits several strengths:
1.The motivation behind the research is clear and well-founded.
2.The use of latent optimization for trajectory control appears both intuitive and innovative.
3.The experimental results validate the effectiveness of the proposed method on the SVD model. The findings are convincing, and the ablation study is thorough.

### Weaknesses
This paper exhibits several Weaknesses:
1.There is a lack of generalization verification across various types of video diffusion models, such as VideoCrafter, EmuVideo (based on the U-Net structure), and CogVideoX-I2V (based on Diffusion Transformer). The current evaluation is limited to the SVD model, which may not fully represent the performance of the proposed method across different architectures. Specifically, the method's reliance on specific feature map characteristics within SVD might not translate well to models with different attention mechanisms or network structures. For example, U-Net based models may exhibit different feature map properties that could impact the effectiveness of the proposed trajectory control.
2.The issue of inconsistent features across frames, as discussed in the introduction, may not be universally applicable. This problem might not be evident in some of the latest 3D full attention-based video diffusion models (e.g., OpenSoraPlan 1.2, EasyAnimate V4, and CogVideoX) or when using VideoVAE. The assumption that feature inconsistency is a major problem across all video diffusion models needs further validation, especially considering the advancements in 3D attention mechanisms that inherently promote temporal consistency. The paper should provide more evidence to support the claim that this is a widespread issue and not specific to certain model architectures or training procedures.
3.There are errors in the formula expressions:
1)The symbols in Formula 1 are confusing. Does Fn represent an operation or a feature map? How does Bb,n (denoting [h, w, x, y]) perform matrix operations with feature maps (shape of [h, w, d])? What does “[Bb,n]” signify?
2)There are two instances of zt* in formula 2.
4.In line 194, the author emphasizes "Yet, all of these methods focus on text-based generation." However, MOFT[1] is also training-free and can achieve image-to-video motion control. In addition, MOFT incorporates the concept of optimizing denoising latents. Can the authors elaborate on the similarities and differences compared to MOFT in terms of functionality and methodology?

### Questions
1.How long does it take for SG-I2V to infer a single example?

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
The paper presents a zero-shot image-to-video diffusion framework for controllable motion generation. Specifically, the proposed SG-I2V exploits the self-guidance in the cross-frame attention feature maps to regulate object trajectory. To further improve the video quality, a post-processing with high-frequency noise injection is designed to ensure that the latent distribution is not disrupted in online latent optimization. Experiments conducted on the VIPSeg dataset verify the proposed approach on both object motion control and camera control.

### Strengths
1.	The proposed approach employs the feature map correspondences to regulate video latent updating and achieves object trajectory control in a zero-shot manner.
2.	Both of the quantitative and qualitative experimental results demonstrate the effectiveness of the proposed approach.  
3.	The paper is well-written and the technical figures are very clear.
4.	The investigation and ablation studies (including the visualization of feature maps) on the feature map selection is comprehensive for proposal validation.

### Weaknesses
1.	The major concern for this paper is about the technical contribution. Even though the weakness of the unsatisfactory feature alignment in the up-sampling blocks (the generalization problem in video domain) has been revealed, the latent optimization is still borrowed from the drag-based control methods, e.g., DragDiffusion. The feature map selection and validation are valuable in my personal opinion. Nevertheless, there is no concept new in the whole architecture design. Therefore, it can be treated as another DragDiffusion of the video diffusion version. Moreover, the high-frequency noise initialization is also proposed in FreeTraj, which should not the key technical contribution in this paper.
2.	The motivation of involving Gaussian heatmap $\textbf{G}_{b}$ in the Eq. (1) is not clear.
3.	It is interesting that the performance trend of ObjMC is flickering as shown in the Figure 10. The reason behind this could be discussed and analyzed.
4.	Is there any additional computational (time and memory) cost for the latent optimization? Including some analysis of them will make the experimental section stronger. 
5.	Are there any visualized comparisons on the VIPSeg dataset? All the presented cases seem be derived from the web images with high quality.

### Questions
Please see the weaknesses.

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
5

### Summary
In this paper, the authors first analyze the semantic correspondences among frames in different latent. Then based on the observation, they propose SG-I2V, a training-free framework for trajectory control through aligning the self-attention with given bounding boxes based on pre-trained I2V model SVD. Additionally, SG-I2V supports arbitrary input images and any number of objects or regions of a scene.

### Strengths
1. Authors use PCA to visualize feature maps of SVD and demonstrate inspiring motivation of method design.
2. This method is training-free and thus does not require additional data to tune the modules. Through optimizing the latent, SG-I2V succeeds in generating trajectory-controllable videos with high fidelity.
3. Inspired by previous work, they apply a high-frequency resampling post-processing to preserve the visual quality. The ablation study demonstrates the effectiveness of this module.
4. Exhaustive ablation experiments demonstrate the rationality of the designed modules and parameters.

### Weaknesses
1. MotionCtrl is a well-known method for trajectory control and also provides the official code and pre-trained model for SVD (same backbone). SG-I2V is supposed to compare with MotionCtrl.
2. Since each inference requires individual optimization calculations, authors are supposed to discuss it. If the additional time is too much, is there any way to reduce it?

### Questions
Has the author tried this method on other I2V frameworks? Specifically, what is the generalizability of this method? Can it be adapted to other UNet models, such as DynamiCrafter? What about the DiT architecture?

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
The paper introduces a novel framework for controllable image-to-video generation. The core innovation of SG-I2V lies in its ability to achieve zero-shot control over object motion and camera movement within generated videos, leveraging a pre-trained video diffusion model. The method does not require task-specific fine-tuning or additional external knowledge. The authors propose an approach that analyzes feature maps from the upsampling blocks of video diffusion models to identify weak semantic alignments across frames. To address this, they introduce a modified self-attention mechanism that aligns features across frames, enabling precise control over element positions in the generated video. The framework optimizes the latent space to enforce similarity between aligned features within bounding box trajectories, and a post-processing step is applied to maintain the expected distribution of high-frequency noise expected by the diffusion model. The paper demonstrates that SG-I2V outperforms unsupervised baselines and is competitive with supervised models in terms of visual quality and motion fidelity.

### Strengths
1. The authors have been inspired by tuning-free text-to-video generation methods and have proposed a similarly tuning-free approach for image-to-video tasks. This eliminates the need for computationally expensive fine-tuning procedures, making the framework more accessible and efficient.
2. The paper provides a thorough analysis of semantic feature alignment within a pre-trained image-to-video diffusion model. 
3. The authors have provided a project page that offers a more intuitive presentation of their work.

### Weaknesses
1. While the paper claims the ability to control an arbitrary number of objects, it lacks experimental evidence to support this claim. The examples provided for controlling object motion are limited to simple scenarios with only 1-2 objects, which may not demonstrate the method's capability across more complex scenarios with multiple objects. Specifically, the paper does not explore how the proposed self-attention mechanism scales with an increasing number of objects, nor does it analyze potential interference or crosstalk between different object trajectories when multiple objects are controlled simultaneously. This raises concerns about the practical applicability of the method in real-world scenarios with many interacting elements.
2. The method's robustness is questionable due to the fine-tuning of parameters specifically for the VIPSeg dataset. The learning rate, for instance, is set to a specific value (0.21), raising concerns about whether these parameters would be universally effective across various image-to-video examples without further adjustments. The paper lacks a thorough analysis of the sensitivity of the method to hyperparameter changes, particularly how variations in the learning rate, the number of optimization steps, and the weight of the alignment loss affect the quality and fidelity of the generated videos. Furthermore, the paper does not provide sufficient justification for the specific choice of these parameters, making it difficult to assess the generalizability of the approach.
3. It is unclear whether the proposed method could be adapted to other base video generation models beyond the one used in the paper. The transferability of the method to different models is an important consideration for its broader adoption. The paper does not discuss the potential challenges in adapting the method to different architectures, such as those with different attention mechanisms or feature map structures. This lack of analysis limits the understanding of the method's flexibility and its potential for broader use.
4. The current method appears to support only linear trajectories, which may not be sufficient for more complex motion control. There is a need to explore whether the method can handle other shapes and longer, more complex trajectories. The paper does not discuss the limitations of the current trajectory representation and how it might be extended to accommodate more complex motion patterns. For example, it is unclear how the method would handle curved trajectories or trajectories with varying speeds and accelerations. This limitation restricts the expressiveness and versatility of the method.
5. Lacking of reference or analyze the relationship with related work on trajectory-based image or video generation, including TraDiffusion[1] and DragEntity[2].

### Questions
See Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2
