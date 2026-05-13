# MAA: Meticulous Adversarial Attack against Vision-Language Pre-trained Models

- Decision: Reject
- Scores: 5, 6, 8, 5, 5

## Abstract
Current adversarial attacks for evaluating the robustness of vision-language pre-trained (VLP) models in multi-modal tasks suffer from limited transferability, where attacks crafted for a specific model often struggle to generalize effectively across different models, limiting their utility in assessing robustness more broadly. This is mainly attributed to the over-reliance on model-specific features and regions, particularly in the image modality. In this paper, we propose an elegant yet highly effective method termed Meticulous Adversarial Attack (MAA) to fully exploit model-independent characteristics and vulnerabilities of individual samples, achieving enhanced generalizability and reduced model dependence. MAA emphasizes fine-grained optimization of adversarial images by developing a novel resizing and sliding crop (RScrop) technique, incorporating a multi-granularity similarity disruption (MGSD) strategy. 
RScrop efficiently enriches the initial adversarial examples by generating more comprehensive, diverse, and detailed perspectives of the images, establishing a robust foundation for capturing representative and intrinsic visual characteristics. Building on this,  MGSD seeks to maximize %the layer- and component-wise feature% 
the embedding distance between adversarial examples and their original counterparts across different granularities and hierarchical levels within the architecture of VLP models, thereby amplifying the impact of the adversarial perturbations and enhancing the efficacy of attacks across every layer and component of the model. Extensive experiments across diverse VLP models, multiple benchmark datasets, and a variety of downstream tasks demonstrate that MAA significantly enhances the effectiveness and transferability of adversarial attacks. A large cohort of performance studies is conducted to generate insights into the effectiveness of various model configurations, guiding future advancements in this domain. The source code is provided in the supplementary material.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces the Meticulous Adversarial Attack (MAA) to address the limited transferability of current adversarial attacks on vision-language pretrained (VLP) models. MAA combines the Resizing and Sliding Crop (RScrop) technique to diversify adversarial examples and the Multi-Granularity Similarity Disruption (MGSD) strategy to enhance embedding distances across different model layers. Extensive experiments demonstrate that MAA improves both the effectiveness and transferability of adversarial attacks across various VLP models, datasets, and tasks.

### Strengths
1.	MAA enhances spatial coherence and model sensitivity by focusing on fine-grained local details through scaling and sliding techniques. It improves adversarial transferability by generating model-generic examples based on shared low-level features.
2.	MAA outperforms existing methods in adversarial transferability and provides valuable insights for adversarial attacks and defense on VLP through extensive parameters, studies and discussion.

### Weaknesses
1.	The author lacks citations and evidence for some of the viewpoints in the paper. In line 78, why are VLP models more prone to relying on specific features and regions to associate images and texts? The paper should discuss the underlying mechanisms that cause this, such as the modality-specific learning biases that lead to a reliance on particular features. Additionally, in line 101, why do vision transformers tend to lose the crucial contextual information in the image? While the self-attention mechanism allows each patch to attend to others, the paper needs to elaborate on how the fixed patch size and lack of inherent spatial inductive biases can limit the capture of multi-scale contextual information, especially compared to convolutional networks which have built-in locality. 
2.	The author needs to add experiments and visualization results to demonstrate that the application of the RScrop technique helps extract finer-grained contextual features from the image. It is not sufficient to claim that it does; the paper needs to show concrete evidence, such as Grad-CAM visualizations or quantitative evaluations on tasks that require fine-grained understanding, to support this claim. For example, an experiment on a visual grounding task could demonstrate how the proposed method improves the localization of relevant image regions.
3.	I suggest that the author explore ensembling multiple source models to further improve transferability and attempt to apply adversarial attacks on larger black-box models, such as GPT-4. The paper should also consider the computational overhead of such approaches and discuss the trade-offs between attack success rate and computational cost.

### Questions
As mentioned in Weaknesses.

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
3

### Summary
This paper presents a new approach to enhance the transferability of adversarial examples across pre-trained vision-language models. The method improves the robustness of a generated adversarial example by (1) forcing the surrogate model to attend to intricate local details and previously overlooked boundary regions, and (2) optimizing feature distances at both low-level (local regions) and high-level (semantic). Evaluation shows that the proposed method can significantly outperform state-of-the-art methods across a large set of vision-language models. Ablation study shows that both techniques contributes to the improved performance.

### Strengths
+ The proposed techniques make sense
+ The evaluation is thorough
+ The evaluation results are good

### Weaknesses
 - The proposed method requires more computation power (iterations), which would either increase the delay of the attack (making it less ideal for real-time attacks), or require more powerful computers
- Performance on BLIP seems not as good
- The writing could be improved. For example, I don't think formula (1) matches its description.
- The method's performance on large models like Llama-3.2 and MiniGPT-4 is not as strong as on smaller models, and the explanation for this is vague.

### Questions
* Please explain why BLIP is excluded from I2T and T2I retrieval experiments, why visual grounding is only done with ALBEF as target, and why image captioning is only done with BLIP?
* Can the generated adversarial examples fool large models like llama 3.2, Claude, and GPT-4o?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a novel transferable adversarial attack method for VL models called Meticulous Adversarial Attack (MAA).

The idea is to minimize dependency on the surrogate model and exploit model-independent features using image augmentations.
This paper proposes a simple resizing and sliding crop (RScrop) technique for image augmentation.
MAA also applies multi-granularity similarity disruption (MGSD), which is similar to the existing VLAttack.

MAA achieves SOTA attack success rate in Image-Text Retrieval, Visual Grounding, and Image Captioning tasks.

### Strengths
- The transferability improvement compared to the SOTA attacks is significant.
- The method is simple, combining existing ideas to improve the transferability: utilizing image augmentations and multi-granularity similarity disruption (MGSD).

### Weaknesses
 - The source model is fixed to CLIP ViT-B/16. Following existing work, it is better to provide results for the other source models for completeness.

- I expect a deeper analysis of the effectiveness of the proposed RScrop. Table 6 should be improved. I am unsure of the contribution and the novelty of RScrop without comparisons between different image augmentation techniques.
    - While the design of the proposed RScrop (resize and slide) seems reasonable, how is it better than other input transformations used in existing methods? What about a comparison between “random resize and padding” (DIM [A]), “translation” (TI-DIM [B]), and “scale and translation” (SI-NI-TI-DIM [C])? Also, the latest method, SIA [D], introduces many different types of augmentations, such as Shift, Rotate, Scale, Noise, etc.
    - The claim that the RScrop is effective because it enables the model “to attend to intricate local details” seems unverified. Since RScrop only zooms in (scale factor > 1.0), a comparison between Unzooming (scale factor < 1.0) / Random scale (e.g., scale factor ranging from 0.5 ~ 2.0) can verify this.
    - “To attend to previously overlooked boundary regions of adjacent patches,” existing augmentations, such as random resize and padding, or translation can be a solution. What are the differences between these augmentations and RScrop?
    - The connection between image augmentation techniques and MGSD is unclear. Does the effectiveness of each image augmentation technique differ when MGSD is applied or not?
- minor
    - A typo in Equation (1): $f^i_{img}$ should input $x$.
    - The citation style is wrong: Authors should correctly use \citet and \citep.

### Questions
- What is the computational cost of MAA? It uses K augmentations and many iterations (60), so I assumed it was large.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
In this paper, the authors propose a new attack method called the Meticulous Adversarial Attack (MAA) that focuses on exploiting model-independent characteristics and vulnerabilities of images. The approach incorporates a novel resizing and sliding crop (RScrop) technique along with a multi-granularity similarity disruption (MGSD) strategy, aiming to overcome the limitations of existing VLP models in capturing detailed aspects and their connections. The experimental results have demonstrated the effectiveness of the proposed method.

### Strengths
1.	The experimental setup in this paper is comprehensive, demonstrating the effectiveness of the proposed method.
2.	This paper is easy to follow.

### Weaknesses
1.	The data augmentation method based on scaling and the joint attack on shallow features proposed in this paper for the image modality are indeed scenario techniques in the field of adversarial examples. Similarly, the method for the text modality is an existing technique.
2.	Although the authors have provided the motivation behind their proposed scheme, the absence of corresponding formula analysis and illustrative figures makes it rather difficult to understand. Moreover, the authors lack in-depth insights to analyze the effectiveness of the proposed RScrop and MGSD strategies. Specifically, the description of how the sliding crop is performed and how the multi-granularity similarity disruption is achieved is not sufficiently detailed. The connection between the RScrop and MGSD and their impact on the final adversarial image is unclear. The paper lacks a clear explanation of how these techniques specifically target vulnerabilities in VLP models.
3.	The main attack algorithm logic in the code provided by the authors is chaotic and cannot be reproduced. Moreover, it fails to correspond to the method section in the paper. The overall code seems to be adapted from the SGA repository. This makes me doubt the effectiveness of the method proposed in this paper.
4.	The experiments in this paper do not provide error bars or results from experiments with different random seeds, which raises my concerns about the validity and stability of the experimental outcomes.
5.	There is a symbolic expression error in Formula 1. It should be $f_{img}^{i}(x_{k})$ instead of $f_{img}^{i}(t)$.

### Questions
See Weakness

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper proposes a Meticulous Adversarial Attack (MAA) method for vision-language pre-trained (VLP) models. It aims to address the limited transferability of existing adversarial attacks. MAA consists of a resizing and sliding crop (RScrop) technique and a multi-granularity similarity disruption (MGSD) strategy. The method is evaluated on various VLP models, datasets, and tasks, showing enhanced effectiveness and transferability of adversarial attacks.

### Strengths
- **Originality**: The proposed MAA method is novel in its combination of RScrop and MGSD strategies. The idea of exploiting model-independent characteristics and vulnerabilities of images for generating adversarial examples is original.
- **Quality**: The experiments are comprehensive, covering multiple VLP models, datasets, and downstream tasks. The ablation study and parameter analysis provide in-depth understanding of the method's components and performance.
- **Clarity**: The paper is well-written and organized. The methodology is clearly explained, and the figures and tables help in understanding the concepts.
- **Significance**: The work is significant as it addresses an important issue in the field of adversarial attacks on VLP models. The enhanced transferability of attacks can have implications for evaluating the robustness of these models.

### Weaknesses
 - The comparison with existing methods could be more detailed. For example, a more in-depth analysis of why MAA outperforms other methods in terms of transferability could be provided.
- The text perturbations are not as thoroughly explored as the image perturbations. Since text perturbations are also an important part of multi-modal attacks, more attention could be given to this aspect.

### Questions
- How does the proposed method compare with other recent methods that have not been included in the comparison?
- Can the method be extended to other multi-modal tasks or domains?
- What are the potential limitations of the RScrop technique in handling very large images or complex image structures?

### Soundness
3

### Presentation
3

### Contribution
3
