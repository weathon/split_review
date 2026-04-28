# Enhancing Detail Preservation for Customized Text-to-Image Generation: A Regularization-Free Approach

- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 5, 6, 3

## Abstract
Recent text-to-image generation models have demonstrated impressive capability of generating text-aligned images with high fidelity. However, generating images of novel concept provided by the user input image is still a challenging task. To address this problem, researchers have been exploring various methods for customizing pre-trained text-to-image generation models. Currently, most existing methods for customizing pre-trained text-to-image generation models involve the use of regularization techniques to prevent over-fitting. While regularization will ease the challenge of customization and leads to successful content creation with respect to text guidance, it may restrict the model capability, resulting in the loss of detailed information and inferior performance. In this work, we propose a novel framework for customized text-to-image generation without the use of regularization. Specifically, our proposed framework consists of an encoder network and a novel sampling method which can tackle the over-fitting problem without the use of regularization. With the proposed framework, we are able to customize a large-scale text-to-image generation model within half a minute on single GPU, with only one image provided by the user. We demonstrate in experiments that our proposed framework outperforms existing methods, and preserves more fine-grained details.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper tackles the task of customized text-to-image generation. It trains the PromptNet to map concepts in an input image into a text embedding for subsequent text-to-image generation. During training, the input image is augmented with affine transformation, and the UNet attention layers are fine-tuned. During sampling, the proposed Fusion Sampling method separates the obtained prompt S* and the arbitrary text prompt C, and feed them into UNet separately to avoid S* overriding C.

### Strengths
1. The paper presentation is clear, and easy to follow.
2. This paper presents some nice results of cutomized text-to-image generation.

### Weaknesses
1. The motivation of the need for "regularization-free" is not comprehensively demonstrated. See Question No.1 for more details.
2. The contribution of PromptNet is limited, where the main difference compared to other encoder-based approaches (e.g. ELITE) is that the affine transformation is introduced.
3. Similar ideas towards Fusion Sampling has been seen in several works [1][2], where the input condition is decomposed into multiple segments, and fed into the diffusion model separately.
[1] Compositional Visual Generation with Composable Diffusion Models (ECCV 2022)
[2] Collaborative Diffusion for Multi-Modal Face Generation and Editing (CVPR 2023)


### Questions
1. The motivation is that "regularization can result in detail lost". However, the validity of this claim depends on the degree of regularization applied, and the degree of detail loss suffered. In figure 3, what is the regularization weighting (i.e. lambda)? Have you tried an even smaller regularization weighting, and what is the degree of detail lost then?
2. In section 2.1, the observation is made that "without regularization, the UNet has a tendency to overly prioritize the S* concept, and overshadowing C". The question arises as to why feeding C independently into the UNet can address this issue, since the text-to-image mapping is not altered by the FusionSampling strategy.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a novel framework called ProFusion to tackle the over-fitting problem in customized text-to-image with an encoder network and a novel sampling method. The encoder network receives an image depicting a customized object, which makes the generation condition on that object. Then, a novel sampling method called Fusion sampling is proposed to enhance the generation to be conditioned on both the input image and the arbitrary user input text. The experiments conducted demonstrate the effectiveness and superiority of the proposed framework.

### Strengths
1. The paper is well-organized, and the method is easy to follow. The core contribution Fusion sampling is novel and may have a broad impact on the conditional image generation community.
2. The most important contribution of the paper is that it proposes a framework without regularization techniques to prevent over-fitting in customized text-to-image generation. The encoder network, which converts the image containing the customized object into an embedding $S^*$, makes the diffusion model condition on that object. Unlike previous methods adopting regularization techniques to prevent over-fitting, this paper proposes a novel Profusion sampling method. By assuming $S^*$ and the arbitrary user input text $C$ are independent, the sampling method decomposes the noise prediction into two terms that take both $S^*$ and $C$ into consideration.
3. The experiments show that the proposed method achieves superior capability for preserving fine-grained details.

### Weaknesses
1. Line#5 to Line#7 in Algorithm 1 is the standard diffusion denoising sampling step. However, the intuition behind #Line9 in the algorithm is unclear.
2. The corresponding ablation study showing the difference between using or not using the two stages in the algorithm is not convincing enough.
3. The claim of being "regularization-free" is not well justified. The method still relies on a fine-tuning stage which is prone to overfitting, and the paper does not provide a comprehensive analysis on why this method is better than other methods using regularization techniques in preventing overfitting. The focus seems to be on detail preservation, but the core issue should be the overfitting to the customized object embedding $S^*$.
4. The effectiveness of the proposed Fusion sampling method is not convincingly demonstrated. The ablation study is not thorough enough to justify the design choices in the sampling algorithm. It is unclear how much each component of the sampling method contributes to the final result.

### Questions
1. Please clarify the intuition or motivation behind Line#9 in the fusion stage in the fusion sampling method.
2. Please provide the corresponding ablation studies to support that using m=1 in practice works well for the fusion sampling method.
3. Do the baseline methods all use the data augmentation method in the paper? If not, the comparison may be unfair.
4. It is better to report the exact training time, fine-tuning time, and the GPU devices used for reproduction consideration.
5. Is it possible to combine the proposed sampling method with other regularization techniques to further improve the performance? Or is it possible to adopt the sampling method to other methods to verify its effectiveness in improving detail preservation?
6. One may trade off the detail preservation for more creative generations or the other way around. Can the authors provide such trade-offs in the proposed framework?
6. Is the method capable of capturing the style of the input customized image? For instance, can the method perform style transfer like generating an image by the prompt "a car in the style of $S^*$".

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a regularization-free and detail-preservation approach for customized text-to-image generation.
To this end, this paper introduces PropFusion to tackle over-fitting problem without the widely used regularization.
Therefore, PropFusion significantly reduces training time while achieve enhanced preservation of fine-grained details.
Moreover, it also introduces a novel sampling method namely Fusion Sampling to meet the requirements of text prompts.
Extensive experiments demonstrate the superiority of the proposed method.

### Strengths
See summary.

### Weaknesses
1. Can the authors elaborate more derivation details from Eq.10 to Eq.11?
2. Comparisons with IP-Adapter[1]. IP-Adapter also projects the input image into the text embedding space, but requires no additional finetuning or well-designed sampling. The authors are encouraged to compare to this simple baseline.

### Questions
See weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors observe that the commonly used regularization to avoid overfitting in customized text-to-image generative models may lead to the loss of detailed information on the customized objects. The authors propose to balance the influences of the prompt condition and the customization condition S* instead of applying regularization to avoid overfitting, ensuring the preservation of customized details and flexibility to work with diverse prompts.

### Strengths
- Motivated by interesting observations
- Novel idea of removing regularization to preserve detailed information
- Computational resource-efficient approach

### Weaknesses
 - Encoder-based customized Text-to-Image generation is not new and missing comparisons with important previous works: [1][2][3][4]
- The important term "independent conditions" is not clearly defined.
- Figure 9 shows that before fine-tuning, fusion sampling even leads to worse identity-preserving performance than baseline sampling, implying that performance gain in identity similarity mainly comes from fine-tuning.
- In Figure 4, the proposed method does not present visually better results compared to E4T.
- The effectiveness of the proposed fusion sampling method is not sufficiently demonstrated, with only one qualitative example in Figure 9. The lack of quantitative results or more extensive qualitative comparisons makes it difficult to assess the true impact of this component.
- The paper does not provide a clear analysis of the trade-off between detail preservation and text alignment, particularly concerning the role of regularization. This lack of analysis makes it difficult to evaluate the core motivation of the regularization-free approach.

### Questions
- The authors aim at "detail preservation" but do not clearly explain what information these details include. What is the difference between detail preservation and identity preservation?
- Minor issue of presentation. Figures 6 and 7 on page 8 are squeezed and Figure 7 has slightly occluded the caption of Figure 6. May rearrange for better visualization.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
