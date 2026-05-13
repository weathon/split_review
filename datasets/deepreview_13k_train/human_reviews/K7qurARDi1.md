# SeaDiff: Delve into Underwater Image Generation with Symmetrical Parameter Control

- Decision: Reject
- Scores: 5, 3, 5, 3

## Abstract
With the advancement of diffusion models, the controllability of image generation has significantly improved. However, due to the refraction and absorption of light in water, underwater images often exhibit notable variations in luminance and color cast. This leads to challenges for generative models pre-trained on terrestrial images, as they struggle to produce underwater images with a diverse range of these variations, severely limiting the appearance diversity of generated underwater images. To address this issue, we focus on the precise control of appearance in underwater images. We model the appearance of underwater images using three attributes: luminance, dynamic range, and color cast. We propose a new method, SeaDiff, which introduces a Symmetrical Parameter Control structure to achieve precise control over the appearance of underwater images. The proposed method comprises two modules: Appearance Writer, which encodes and injects appearance attributes into the U-Net encoder, and Appearance Reader, which ensures that the generated images align with the desired appearance by analyzing the feature maps. Experimental results demonstrate that the proposed SeaDiff method significantly improves control over underwater image appearance while maintaining image quality, validating its effectiveness in underwater image generation.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper presents SeaDiff, an effective approach for controlling appearance attributes in underwater image generation using diffusion models. The authors model three key attributes (luminance, dynamic range, and color cast) and propose a Symmetrical Parameter Control framework consisting of an Appearance Writer (A-Writer) and an Appearance Reader (A-Reader). Evaluated on the RUOD dataset, the method demonstrates significant improvements over existing approaches in both appearance control and image quality.

### Strengths
The paper addresses controllable image attribute editing, which is a fundamental challenge. The focus on precise control of specific attributes (luminance, dynamic range, and color cast) demonstrates a clear understanding of key image manipulation needs. I think the research direction would leverage a wide range of applications.

### Weaknesses
In method section, I think the paper's unique contributions appear limited, primarily focusing on transferring existing pre-trained priors to a specific field. The proposed model is essentially a fine-tuned version of the pre-trained Stable Diffusion model. While leveraging pre-trained models is common practice, the core contributions and motivations of this work should be more explicitly highlighted to distinguish it from existing approaches.

In Table 1 of the experimental section, there is no analysis of the model's parameters or inference latency, which is essential given the reliance on a computationally heavy pre-trained model. Such an analysis would provide valuable insights into the method's efficiency and practical applicability.

In Section 5.1, the paper acknowledges a bias in existing datasets, which consist of similar frames extracted from the same video. However, the simple re-division of the dataset does not adequately address this distribution bias. Additionally, all experiments were conducted exclusively on the RUOD dataset, raising concerns about the method's generalization capabilities to other underwater datasets.

Meanwhile, the experimental section highlights successful outcomes but lacks a systematic analysis of failure cases or the method's limitations. A thorough examination of these aspects is crucial for understanding the robustness and applicability of the proposed method in diverse scenarios.

### Questions
Underwater image attributes encompass more than just luminance, dynamic range, and color cast. Can the proposed method be adapted to handle additional attributes or support more extensive attribute editing? If so, how would this be achieved?

The results presented in the experimental section demonstrate the method's performance under relatively ideal underwater conditions. However, there is no testing under extreme lighting conditions or severe turbidity. How does the method handle extreme underwater conditions such as severe turbidity, low visibility, and uneven lighting? 

How does the method perform on underwater datasets other than RUOD? Has any cross-dataset evaluation been conducted to assess its generalization capabilities?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper tackles the challenge of managing underwater image appearance by focusing on three key attributes: illumination, dynamic range, and color cast. The method comprises two primary components: Appearance Writer (A-Writer) and Appearance Reader (A-Reader). The former encodes and injects appearance attributes into the U-Net encoder, while the latter ensures that the generated image aligns with the desired appearance by analyzing the feature maps.

### Strengths
This paper is structured in a clear and accessible manner, making it easy to follow for readers. The topic of generating diverse and realistic underwater images is particularly intriguing, as it addresses the challenges faced in underwater imaging and highlights the potential for advancements in this field.

### Weaknesses
1. The results presented are not satisfactory. As shown in Fig. 1, the images fail to meet the expected standards of realism. The generated images exhibit noticeable artifacts and lack the fine-grained details present in real underwater imagery. Specifically, the color gradients appear artificial, and the textures lack the natural variations observed in actual underwater scenes. The overall visual quality is significantly lower than what is typically required for practical applications.
2. Why is it important to generate underwater images, particularly those of low quality (severely degraded)? Will this be beneficial for downstream tasks, or does it serve other purposes? The paper does not adequately justify the need for generating low-quality underwater images. It is unclear how these images, which are visually unappealing and lack fidelity, would be useful for training or evaluating models. The practical applications of such degraded images are not well-defined, and the paper fails to provide a compelling argument for their relevance.
3. The author creates new underwater images based on three attributes: illumination, dynamic range, and color cast. However, the degree of turbid, a key attribute of underwater images is neglected. Turbidity is a critical factor affecting visibility and image quality in underwater environments. By omitting this attribute, the generated images fail to capture the full spectrum of real-world underwater conditions. This omission limits the practical applicability of the method, as it cannot simulate a wide range of underwater scenarios.

### Questions
1. Can the proposed method generate high-resolution underwater images? 
2. What is the inference efficiency of the proposed method?

### Soundness
2

### Presentation
2

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
This work models the appearance of underwater images from three aspects: luminance, dynamic range, and color cast,  achieving precise control over the appearance of underwater images. Additionally, this paper proposes a new method, SEADIFF, which comprises two primary contributions: the Appearance Writer, responsible for encoding and injecting appearance attributes into the U-Net encoder; and the Appearance Reader, which ensures that the generated images align with the desired appearance by analyzing the feature maps.

### Strengths
1.This work models the appearance of underwater images across three aspects: luminance, dynamic range, and color cast. The idea is interesting.

2.This paper is written with clarity and is highly accessible to readers.

### Weaknesses
1. The proposed method is relatively simple, lacking novelty and insight. This work appears to be more of an engineering effort rather than an academic innovation.

2. Although the proposed method achieves superior results based on quantitative metrics, the visualizations make it difficult to discern its advantages. For instance, in Figure 1, it is challenging to observe that the images generated by our method exhibit higher quality compared to those produced by GeoDiffusion.

3.The experiments are not robust, and additional studies are needed to demonstrate that the images generated by the proposed method are beneficial.

### Questions
1. Why do the input resolutions differ across the various methods presented in Table 1?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposed a new underwater data generation method, which can control the luminance, dynamic range, and color cast of the generated images. Experiments prove that this method achieves superior control over appearance while maintaining image quality and layout-consistency. However, its application is limited and its techniques have been widely studyed. Specific reasons are given in weakness.

### Strengths
1) This article achieves precise control over underwater image generation, and the performance is good.
2) To some extent, I believe that this method can serve as an alternative to underwater image enhancement, but the paper itself did not discuss this point.
3) This paper introduces the simultaneous use of luminance, dynamic range, and layout control for underwater image generation.

### Weaknesses
1) its application is limited. From my opinion, the underwater image enhancement and some downstream applications, e.g., object detection and semantic segmentation, are significant. Only generating underwater images is meaningless but this paper only discusses how the proposed method can effectively and controllably generate underwater images, but does not mention the significance of generating underwater images. Only generating images of a specific scene is meaningless. 

2) Besides, the techniques it used have been widely adopted. If this paper proposed a novel technique for underwater image generation, it will still be a valuable work. However, the A-Writer and A-Reader are not novel and interesting enough. Their key contributions are cross-attention and feature supervision. The layout control is also achieved by cross-attention. These techniques have been widely used and are not designed for underwater image generation.

This paper lacks application impact and technological innovation.

### Questions
1) The impact on mainstream applications should be fully discussed, including image enhancement and downstream applications. Generating underwater images only is not important.

2) Underwater-oriented techniques should be studied. Considering the content of this task, I believe it would be more meaningful to design specialized generative components for underwater scenes.

### Soundness
3

### Presentation
3

### Contribution
2
