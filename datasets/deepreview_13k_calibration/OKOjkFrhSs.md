# Prompt-Guided Dynamic Network for Image Super Resolution

- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 3, 3, 3

## Abstract
Existing single image super-resolution (SISR) methods learn the convolutional kernel solely from a single image modality. However, the SR performance is limited by the diversity of input modality and the insufficient image-level information in low-resolution images. In this paper, we seek to use multi-modal prompts (texts or images) to assist existing SR networks to learn more discriminative features, leading to superior SR performance. To this end, we develop the Dynamic Correlation Module in a plug-and-play form for existing SR networks, which learns meaningful semantic and textural information from multi-modal prompt embeddings extracted from a large-scale vision-language model (such as CLIP). Specifically, Spatially Multi-Modal Attention Module is proposed to generate the pixel-wise cross-modal attention mask which would highlight the interest regions given certain prompts. Moreover, to the best of our knowledge, we are the first ones that introduce multi-modal prompts into convolutional kernel estimation which can better handle spatial variants and retain cross-modal relevance. Extensive experiments and ablation studies demonstrate the effectiveness of the proposed Dynamic Correlation Module which exploits the discriminative prompt features to recover realistic high-resolution images, elevating existing SR performance by a notable gap.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a prompt-guided dynamic network (PDN) and dynamic correlation module (DCM) for single image super-resolution (SISR). The key contributions are:

- PDN introduces powerful multi-modal representations like text descriptions or similar images into existing SISR frameworks through the DCM module. This allows the model to learn more meaningful semantic information from the prompts.

- DCM contains two main components: a spatially multi-modal attention module and a prompt-guided dynamic convolution module. The attention module highlights image regions relevant to the prompts. The dynamic convolution uses the prompts to generate convolutional kernels, enabling better modeling of cross-modal coherence and spatial variations. 

- DCM can be conveniently incorporated into various SISR networks. Experiments show DCM improves performance over state-of-the-art methods on benchmark datasets, especially for larger scale factors.

- To the best of the authors' knowledge, this is the first work to introduce multi-modal prompts for convolutional kernel estimation in SISR. 

In summary, the paper proposes a novel way to leverage multi-modal prompts to boost SISR performance through a flexible DCM module that can be plugged into existing networks. Key innovations are the cross-modal attention and prompt-guided dynamic convolutions.

### Strengths
**Originality**
- The specific techniques for integrating prompts are novel, including cross-modal attention and prompt-guided dynamic convolutions. Outperforms the related TGSR paper.

**Quality**
- Technically sound approach with extensive experiments that validate the quantitative improvements.

**Clarity**
- Excellent writing quality and clear presentation of the proposed method.

**Significance**  
- Addresses the important problem of improving generalization in super-resolution.
- Shows the benefits of leveraging multi-modal information for this task.
- Could inspire further research in using prompts.

### Weaknesses
The high-level idea of using multi-modal prompts to improve super-resolution generalization is not entirely novel, as the TGSR paper proposed this first.

While the specific techniques in this paper differ from TGSR, the overall framework is quite similar conceptually (leveraging prompts to aid super-resolution). Compared to TGSR, the innovations here seem more incremental - attention modules, dynamic convolutions, etc. Rather than proposing an entirely new overall architecture. The extent to which these specific contributions generalize may be limited.

More analysis could be provided on how the approach differs from and improves upon TGSR technically. The conceptual similarity should be addressed more directly.

Additionally, like most learning-based SR methods, the reliance on synthetic training data means real-world robustness is unclear. Evaluation of realistic degraded images could better validate effectiveness.

In summary, the high-level novelty is diminished by the prior TGSR work. More analysis comparing TGSR technically and conceptually could strengthen the paper. Real-world evaluations could provide further evidence of the robustness and generalization abilities.

### Questions
Here are some questions and suggestions for the authors:

- The TGSR paper proposed using multi-modal prompts for super-resolution first. Could you more clearly explain how your approach technically differs from and improves upon TGSR? Some more analysis comparing your method to TGSR may be helpful.

- The overall framework of using prompts to aid super-resolution seems conceptually quite similar to TGSR. Do you view your innovations as more incremental improvements in architecture, or is there a fundamental difference in how prompts are leveraged that should be clarified?

- Like most learning-based SR methods, you rely on synthetic training data. How confident are you that the approach will be robust to real-world degradations? Evaluating real degraded images could help validate this.

- Have you considered applying the approach to other image restoration tasks beyond super-resolution, to demonstrate generalization?

- Is the performance sensitive to the choice of prompts? How robust is it to unrelated or poor prompts? More analysis here could help.

- Are there limitations to the architectures you proposed for integrating prompts? Could any negative impacts result from the attention modules or dynamic convolutions?

- Could you provide more details on the training methodology? Some hyperparameters and training details are missing.

Overall, addressing the conceptual similarity to TGSR, evaluating real degradations, and analyzing the generalization abilities could help strengthen the paper. I look forward to the author's response.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a novel approach that leverages multi-modal cues, such as text or additional images, to enhance the capabilities of existing super-resolution networks. It introduces a Dynamic Correlation Module in a plug-and-play format for existing super-resolution networks and a Spatially Multi-Modal Attention Module to create pixel-wise cross-modal attention masks that emphasize regions of interest based on specific cues. The evaluation results conducted on 4 benchmarks (ie, Set5, Set14, Urban100, and Celeba-HQ) seems to validate the efficacy of the proposed method.

### Strengths
+ The paper is well organized and easy to follow.
+ It is interesting to incorporate the prompt text as a guidance to improve the super-resolution recovery.
+ The presented results well support the claims in the main paper.

### Weaknesses
- Technically the novelty is very limited because the incorporate the prompt text as a guidance in very incremental. 
- The CNN backbone is a little out of date. I would like to suggest the authors apply the similar idea to the SOTA SISR methods with both Transformers and diffusion models. 
- All the competing baselines in Section 4.2 are not SOTA methods any more, as they were published at least 3 years ago.
- The references are obviously inadequate, as no 2023 papers are included and cited in the paper. The authors should cite the following papers:
1. Yuanbiao Gou, et al. Rethinking Image Super Resolution from Long-Tailed Distribution Learning Perspective. CVPR 2023.
2. Sicheng Gao, et al. Implicit Diffusion Models for Continuous Super-Resolution. CVPR 2023.
3. Yinhuai Wang, et al. GAN Prior Based Null-Space Learning for Consistent Super-resolution. AAAI 2023.
4. Bin Sun, et al. Hybrid Pixel-Unshuffled Network for Lightweight Image Super-resolution. AAAI 2023.

### Questions
- Why are the quantitative results of EDSR in Table 3 and Table 4 not consistent?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes to use text driven prompts to render diversification in image superresolution workflow. The primary claim is that existing single image supreres methods learn the convolution kernel from single image modality. By introducing coherent text based prompts by way of CLIP latents, this bottleneck can be removed to a large extent. The authors propose a spatially multi-modal attention module and prompt guided DCM. The attention module first computes an attention mask between the prompt and the image features and then weights the image features based on the attention weights. The prompt embedding is further utilized to learn N sets of weights \pi to be used as combination weights for dynamic convolution.

### Strengths
The idea is interesting and can be exploited more by incorporating the multi-modal prompts into many CV pipelines. For images with captions this might be a great way to include captions in the superres pipeline. 

Originality: The development seems original enough.
Quality: The technical development of the material can be improved from its current state. 
Clarity: The Prompt Guided DCM module section is just 6 lines long, where it is one of the two claims of this paper! I strongly feel that this part needs to be written better.
Significance: The paper has been designed as an application paper. I believe the underlying idea can be used for many different applications.

### Weaknesses
The primary problem I have with the paper is the explanation for the prompt guided technique itself. Starting from Fig 2. which states a) and b) but does not show two subfigures. The equations for the prompt being used in subsequent convolution modules are mentioned in Fig. 2 but not in the main text. It is almost assumed that reviewers know the contents of the Dynamic Convolution paper [Yang et al. 2019] and hence, the authors did not spend any time to develop the concept independently. 

For the comparative methods, the authors claim that they add this module within existing workflows. They add one additional block in one method and three additional blocks in another. What is the basis of these choices. What does it do the parameter count for these methods and how does that compare to just increasing the number of layers in these methods?

For the image datasets which do not have captions, the authors propose to use CLIP image features for the horizontally flipped image. Again, no explanation of these choices are provided. Providing a flipped image to other SR techniques and then somehow integrating the results from the two outputs might be an interesting study for existing methods as well.

### Questions
I would request the authors to first explain the method and all the mathematical steps involved fully to make it a paper which stands on its own. 

The attention visualization in Fig. 5 are much better than Fig. 4. What is the difference between them?

Some questions are in the previous section and authors can chose to answer them together.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposed a prompt-guided dynamic network which introduces the text embedding to existing SR framework. The key component is Dynamic Correlation Module which has a spatially multi-modal attention module and a prompt-guided dynamic convolution module. The work is the first to introduce the text into convolution kernel estimation for feature transformation. The comprehensive analyses of effectiveness of proposed modules are demonstrated.

### Strengths
1. This paper introduce the text into convolution kernel estimation for feature transformation which is interesting and novel. 
2. The paper is easy to follow.
3. The performance is much improved than the SOTA method.
4. The ablation study on the prompt and DCM is solid.

### Weaknesses
The only concern is unfair comparison. Since the most of the baselines are trained on the DIV2K which has less images than the training data used in this work. I can not find the claim that the baseline models are trained on the same dataset from the scratch. This may make the paper less convincing.

I have no idea how you get the result. But clearly in the Table 2 the results have some problems comparing with the result in your main paper. You said you trained the RCAN/EDSR on coco dataset. Why the result is the same as Table 1 in the main paper? That makes the paper even less convincing.

### Questions
See weakness. 

How does it perform if the prompt is fixed as "high detailed image"? For most cases of SR, it is hard to describe the image using text.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
