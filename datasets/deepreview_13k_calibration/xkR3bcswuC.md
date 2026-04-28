# Generative Models: What Do They Know? Do They Know Things? Let's Find Out!

- Decision: Reject
- Avg Score: 5.75
- Scores: 5, 6, 6, 6

## Abstract
Generative models excel at mimicking real scenes, suggesting they might inherently encode important intrinsic scene properties. In this paper, we aim to explore the following key questions: (1) What intrinsic knowledge do generative models like GANs, Autoregressive models, and Diffusion models encode? (2) Can we establish a general framework to recover intrinsic representations from these models, regardless of their architecture or model type? (3) How minimal can the required learnable parameters and labeled data be to successfully recover this knowledge? (4) Is there a direct link between the quality of a generative model and the accuracy of the recovered scene intrinsics?

Our findings indicate that a small Low-Rank Adaptators (LoRA) can recover intrinsic images---depth, normals, albedo and shading---across different generators (Autoregressive, GANs and Diffusion) while using the same decoder head that generates the image. As LoRA is lightweight, we introduce very few learnable parameters (as few as 0.04\% of Stable Diffusion model weights for a rank of 2), and we find that as few as 250 labeled images are enough to generate intrinsic images with these LoRA modules. Finally, we also show a positive correlation between the generative model's quality and the accuracy of the recovered intrinsics through control experiments.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper focuses on investigating the intrinsic knowledge encoded within various generative models, such as GANs, autoregressive models, and diffusion models. The study aims to uncover whether these models inherently capture fundamental scene properties, including Depth, Surface Normals, Albedo, and Shading. Through the use of Low-Rank Adaptation (LoRA), a lightweight technique that introduces minimal learnable parameters, the authors propose a model-agnostic approach to recover these intrinsic features.

### Strengths
1. Their findings reveal that a minimal amount of labeled data, sometimes as few as 250 images, suffices for the effective recovery of these intrinsic images.
2. The research claims a positive correlation between the generative quality of a model and the accuracy of its recovered intrinsic properties, which is interesting.

### Weaknesses
1. In Table 1, why do different generative models exhibit varying abilities to capture scene intrinsics without altering the generator head? For instance, even within the same model, such as SG-XL, all scene intrinsics (e.g., Normal, Depth, Albedo, and Shading) are recoverable for the FFHQ dataset, while none of these intrinsics can be captured for ImageNet. Are there any hypotheses regarding which properties of the models or datasets might influence their differing abilities to capture intrinsic features?

2. While the paper asserts that “enhancements in image generation quality correlate positively with intrinsic recovery capabilities”, this claim seems not convincing enough due to the following reasons:

a) Figure 2 attempts to validate the claim by showing a relationship between generated image quality (measured by FID) and recovery errors. However, it includes only three generative models (SG-XL, SGv2, and VQGAN), which represent GAN-based and autoregressive models but exclude diffusion models. This limited selection makes it challenging to empirically confirm the claim. It would be better to provide more generative models in Figure 2, including diffusion models as well. Moreover, discussing the technical reasons behind such correlations would strengthen the argument.

b) The claim lacks rigor due to inconsistencies. For instance, Figure 2 suggests that SG-XL outperforms SGv2 and VQVAE in generative quality, yet Table 2 shows SG-XL occasionally underperforming them, such as in Shading (on FFHQ). Moreover, factors beyond the generative model itself, like the dataset, also impact performance. For example, SGv2 performs worse in Depth but better in Shading when switching from FFHQ to LSUN Bedroom. Please provide a more in-depth statistical analysis of the correlation between generative quality and intrinsic recovery capabilities across all models and datasets.

3. One of the paper’s objectives is to demonstrate that “tiny new parameters and data are enough for intrinsic recovery”. However, as mentioned in this paper, several existing works (e.g., [1]) have already shown that parameter-efficient adaptation methods, like linear probes, can effectively extract intrinsic features such as depth. This work merely replaces linear probes with LoRA and demonstrates its effectiveness, which feels somewhat incremental. Besides, it would be better to discuss more, e.g., it would be helpful to discuss further -- for example, whether there are particular scenarios where LoRA outperforms linear probes or if LoRA provides any advantages beyond performance.

4. The paper notes a lack of ground truth data for certain maps (like albedo), which raises the question of whether using a light physics simulator or tools like Unreal Engine could provide high-quality ground truth labels. This approach could also enable the creation of more complex scenes and lighting conditions for more rigorous model testing. I am curious about the feasibility of incorporating such simulators or tools into this work, and whether this approach could substantially enhance the reliability of the results.

### Questions
Please refer to Weaknesses.

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
4

### Summary
This paper investigates the intrinsic information (e.g., normal, depth, albedo, and shading) encoded in various generative models, including GANs, autoregressive models, and diffusion models. Key findings include (1) Intrinsic information is a byproduct of training generative image models; (2) Low-Rank Adaptation (LoRA) is a generic technique to study the intrinsic information encoded, better than other approaches such as linear probing and fine-tuning; (3) The quality of a generative model and accuracy of its recovered intrinsics (e.g., depth prediction accuracy) are positively correlated. To recover each intrinsic property, a structured prediction module (e.g., depth prediction) has been used to provide pseudo groundtruth during the LoRA optimization. Experiments have been conducted mainly on depth and normal prediction.

### Strengths
- [S1: Originality] Though the proposed method is very standard, the paper presented a generic approach and demonstrated that the approach recovers intrinsic information across diverse generative models, including GANs, autoregressive models, and diffusion models. 

- [S2: Clarity] The motivation, methodology, and results are clearly articulated, enabling a good understanding of the research contributions.

### Weaknesses
 - [W1: Deeper understanding] While the paper establishes what intrinsic knowledge is encoded, it doesn't delve into how generative models utilize this knowledge during image generation. 
  - [W1.1] For example, the reviewer would like to understand if intrinsic property emerges with a half-trained generative model (or at different training epochs).

- [W2] The reviewer find that most intrinsic property do not contain high-frequency details (e.g., sharp edges in the depth prediction). This could be the shortcoming of using LoRA fine-tuning in the design. Although multi-step diffusion inference has been added in Section 5, the question still remains if a single-step approach is sufficient to recover high-fidelity intrinsic information.
  - [W2.1] How does multi-step inference apply to other generative models such as StyleGAN?
  - [W2.2] What’s the motivation of applying LoRA to attention layers of a diffusion model?
  - [W2.3] The ablation studies on applying LoRA to different modules (Appendix B) is interesting. It seems to suggest that LoRA is not successful when applied to up or down blocks. What’s the insight behind the discovery?

- [W3] The reviewer does not fully understand the claim that StyleGAN-XL trained on ImageNet is an exception (Line 365). For example, StyleGAN-XL achieved a much lower FID (Line 452) compared to other generative models, which seems to contradict with the claim that StyleGAN-XL’s limited ability to generate realistic images (Line 366). Please clarify this point in the rebuttal.

- [W4] Specific to the comparison between SD-1.X and SD-2.1,  how much of the performance difference can be attributed to the improved encoder-decoder? Is it possible to recover the intrinsic property by applying LoRA fine-tuning on encoder-decoder alone?

### Questions
Please address the comments in the weakness section.

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
The paper investigates whether current generative models possess a genuine understanding of the world they're generating, rather than just statistical pattern matching. The authors propose using the generation of image intrinsics (such as depth maps, normal maps, etc.) as a proxy for evaluating the models' physical understanding and explainability. They demonstrate that a simple adaptation method (LoRA) can effectively recover these intrinsic properties and conduct extensive analyses to support their hypothesis about models' world understanding.

### Strengths
- The work raises fundamental questions about the nature of internal representations in generative models and their relationship to generation quality, contributing to our understanding of these architectures.
- The research demonstrates that world representations in powerful generative models are more concrete and accessible than previously assumed, establishing important connections to explainable AI.
- The authors present compelling insights about the minimal data requirements for intrinsics recovery, suggesting that the underlying knowledge is already embedded in the model's parameters.
- The methodology is straightforward yet effective, making the findings easily reproducible and applicable to various generative models.

### Weaknesses
 - The paper appears to have originated as a study specifically focused on diffusion models, with other generative architectures added later to broaden its scope. While Section 4's experiments and Section 5's generation quality refinements primarily use Stable Diffusion, validating these findings across different architectures would strengthen the paper's claim of developing a general approach.
- The experiments in Section 4.2 focus solely on normal map recovery when determining optimal rank and dataset size. The authors should clarify whether these optimal settings generalize to other intrinsics or if each intrinsic property requires specific configurations.
- The paper would benefit from a deeper analysis of why LoRA is particularly effective for intrinsic recovery. While Line 102 suggests that "intrinsic information is distributed throughout the network," this insight isn't fully developed in Section 4.4 or elsewhere. Understanding this mechanism could also inform the development of future recovery methods.

### Questions
- Related to the last weakness, Section 4.4 identifies LoRA as the superior method for intrinsic image recovery, but the underlying reasons remain unclear. Could the authors provide insights into its advantages over alternative methods?
- The authors demonstrate a positive correlation between image intrinsics and generation quality. Could they elaborate on the nature of this relationship? Specifically, does better intrinsic understanding lead to improved generation quality, vice versa, or is there a bidirectional relationship between these aspects?

### Soundness
2

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
3

### Summary
This paper proposes to use pretrained generative models extended with trainable LoRA layers as image intrinsic predictors. The proposed approach aims to learn effective intrinsic extractors with as few LoRA parameters and training samples as possible. Extensive experiments are conducted to primarily show that (1) with less LoRA parameters and data samples than state-of-the-art approaches, extracting intrinsic images is still possible (2) it is the prior knowledge in pretrained generative models that helps extract intrinsic image, or in other words, generative models do encode useful intrinsic knowledge though it is not clear how such intrinsic knowledge are used during generation.

### Strengths
1. The paper is well-written and easy-to-follow

2. The approach is straightforward and effective by using LoRA to adapt pretrained generative models for downstream tasks beyond image generation. The predicted intrinsic results look decent.

3. By using LoRA instead of retraining or finetuning the whole model, the approach requires less data and parameters to perform the image intrinsic estimation task. As an experimental work, the paper mostly supports the claims therein with extensive experiments.

### Weaknesses
1. Fig 8 and Fig 9 show that there is a performance peak as the number of LoRA params or training samples vary. Why there is a peak? For  the case of fixed number of training samples, with more LoRA params than Rank 8, the performance degrades. Is this due to underfitting that there is no enough data to train larger LoRA well enough? Similarly, for the case of fixed number of  LoRA params, is this due to overfitting that more data overfits a relative small LoRA? It would be beneficial to explore the training dynamics more thoroughly, perhaps by visualizing the loss curves for different LoRA ranks and dataset sizes. This could provide more insight into the observed performance peaks and degradation.

2. A relevant question to 1.  If you increase the number of LoRA and the number of training data at the same time avoiding overfitting or underfitting, can you outperform existing approaches eventually as shown in Table 3? Furthermore, the paper shows qualitative results for all four intrinsics Surface Normal, Depth, Albedo and Shading throughout the paper, but shows quantitative results on only Surface Normal, Depth in Table 3. Is there is any reason for this practice? The lack of quantitative results for Albedo and Shading makes it difficult to fully assess the method's performance on these important intrinsic components.

3. The paper overclaims a bit about "minimal" requirements on parameter updates and data. Why do you say minimal and in what sense it is minimal? Thought the approach is able to work with fewer params and data , the quantitative performance doesn't outperform existing approaches as shown in Table 3. The term "minimal" is not well-defined and should be clarified or replaced with a more precise term. It is important to acknowledge that while the approach uses fewer resources, it does not achieve state-of-the-art performance.

4. Typo Table 3 caption, "intrinsicsacross"->"intrinsics across"

### Questions
To AC: I can clearly understand the task, the proposed approach and the experiments in the paper. Overall, I find the paper supports the claims with properly designed experiments, but I cannot evaluate the importance and novelty of the paper at the moment since I don't follow literature on this intrinsic estimation topic. I would evaluate these two aspects later by referring to opinions from other reviewers. So please use this review with proper weight when make decisions.

### Soundness
3

### Presentation
4

### Contribution
3
