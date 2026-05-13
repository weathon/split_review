# Lumina-T2X: Scalable Flow-based Large Diffusion Transformer for Flexible Resolution Generation

- Decision: Accept
- Scores: 8, 8, 6, 8, 6

## Abstract
Sora unveils the potential of scaling Diffusion Transformer (DiT) for generating photorealistic images and videos at arbitrary resolutions, aspect ratios, and durations, yet it still lacks sufficient implementation details. In this paper, we introduce the Lumina-T2X family -- a series of Flow-based Large Diffusion Transformers (Flag-DiT) equipped with zero-initialized attention, as a simple and scalable generative framework that can be adapted to various modalities, e.g., transforming noise into images, videos, multi-view 3D objects, or audio clips conditioned on text instructions. By tokenizing the latent spatial-temporal space and incorporating learnable placeholders such as |[nextline]| and |[nextframe]| tokens, Lumina-T2X seamlessly unifies the representations of different modalities across various spatial-temporal resolutions. Advanced techniques like RoPE, KQ-Norm, and flow matching enhance the stability, flexibility, and scalability of Flag-DiT, enabling models of Lumina-T2X to scale up to 7 billion parameters and extend the context window to 128K tokens. This is particularly beneficial for creating ultra-high-definition images with our Lumina-T2I model and long 720p videos with our Lumina-T2V model. Remarkably, Lumina-T2I, powered by a 5-billion-parameter Flag-DiT, requires only 35% of the training computational costs of a 600-million-parameter naive DiT (PixArt-alpha), indicating that increasing the number of parameters significantly accelerates convergence of generative models without compromising visual quality. Our further comprehensive analysis underscores Lumina-T2X's preliminary capability in resolution extrapolation, high-resolution editing, generating consistent 3D views, and synthesizing videos with seamless transitions. All code and checkpoints of Lumina-T2X are released to further foster creativity, transparency, and diversity in the generative AI community.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper presents Lumina-T2X, a framework focused on enhancing scalability and efficiency in high-quality multi-modal generation. It introduces Flag-DiT architecture that integrates flow matching, RoPE, KQ-Norm, and other techniques to improve stability and enable flexible generation across various resolutions and modalities. Lumina-T2X achieves adaptable, high-resolution outputs for tasks like image and video synthesis without extensive re-engineering, aided by RoPE extensions — NTK-aware scaled RoPE, Time Shifting, and Proportional Attention. Extensive evaluations showcase its high-quality performance in ultra-high-resolution generation and adaptability across tasks, with notable improvements in FID, CLIP, and aesthetic metrics vs. SOTA T2I models.

### Strengths
The paper provides a detailed recipe for training scalable transformers, positioning Lumina-T2X as a practical model for the community to adapt for diverse multi-modal applications.

The paper provides an in-depth walkthrough of the architecture, clearly explaining each component’s role and demonstrating how these elements work together to enable scalable generation — both in terms of model size and output resolution.

The paper is exceptionally well-structured, with each component outlined in order of importance and introduction, making it easy to follow. The writing is clear and easy to understand.

The model achieves impressive results across multiple benchmarks, with notable improvements in FID and CLIP scores for non-CFG generation. 

The paper presents high-quality visuals that showcase Lumina-T2X’s capabilities in ultra-high-definition and cross-modal generation.

The results for multi-view generation appear surprisingly consistent.

### Weaknesses
The paper’s focus is not to introduce or ablate the components but instead to provide a framework and a comprehensive recipe for training. While this approach still offers valuable insights, it makes it difficult to directly compare results with in-domain works, e.g. CogVideoX. Certain design choices, like line/frame splitting with RoPE vs. 3D RoPE, could benefit from further discussion. Specifically, the justification for using 1D RoPE with identifiers instead of a true 3D RoPE is not thoroughly explored, which could limit the model's ability to capture complex spatio-temporal relationships inherent in video data. The paper would benefit from a more detailed comparison of these approaches, including potential trade-offs in terms of computational cost and performance.

While the model addresses scalability, the paper lacks a detailed discussion on potential gains from alternative strategies, such as DiT-MoE, which could further enhance efficiency and scalability. Most evaluations focus on the simpler task of text-to-image generation, limiting insights into performance across more complex tasks where scalability is needed the most. For instance, the paper does not explore how the proposed architecture performs on tasks like high-resolution video generation or 3D synthesis, where the benefits of scalability would be most apparent. Furthermore, the paper does not provide a detailed analysis of the computational resources required for training and inference, making it difficult to assess the practical feasibility of the approach for large-scale applications.

### Questions
(1) Could you provide more details on the FSDP sharing strategy, checkpointing, and related techniques? Was tensor parallelism utilized in the model?

(2) You mention a training duration of 96 A100 days for the T2I model. Was this resource-limited, and would the model benefit from additional training time?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The authors introduce Lumina-T2X a framework for generation of image, video, 3D or audio from text instructions. This work introduces Flag-DiT which is a flow based diffusion transformer architecture which allows for generation of various modalities under varying aspect ratios and resolutions. Additional techniques such as RoPE, KQ-Norm and flow matching to allow for scalability. Specific details are provided for translation into each of the modalities and state of the art quantitative performance is demonstrated compared to recent baselines.

### Strengths
The paper introduces a general generative framework from text to a number of different types of modalities. The main strengths include :
1. **Reproducibility**: The paper has an in depth treatment of most of the implementation details and design choices aiding in easy reproduction of the pipeline. Furthermore, the associated code has been provided (and made open source) further accelerating the ability to use the framework and build upon it. 
2. **Quality**: The paper is well written with adequate motivation for each design element used and experiments justifying the need for each. The authors do a good job of highlighting the key innovations that were important to achieve state of the art performance. These being the use of *RoPE*, *RMSNorm and KQ-Norm* for scalable training, *flow matching* for improved training dynamics, *learnable tokens* for any resolution generation and *carefully curated data* for improved image quality. 
3. **Comparison**: Comparisons are provided against a number of different baselines under matched setting to demonstrate improved performance on the lablel conditioned imagenet generation task. 
5. **Result quality**: The image quality demonstrated in the paper is impressive and the ability to generate at variable resolution and aspect ratios in a unified model is very useful. 
6. **Appendix**: The appendix provides a lot of additional insights and useful empirical findings that is helpful to research in multimodal generation.
6. **Advanced applications:** A number of training free applications like resolution extrapolation and style consistent generation have been demonstrated which highlights the capability of the framework. 
6. **Any resolution generation**: The idea of using learnable `[nextframe]` and `[nextline]` tokens is elegant and simple to incorporate and is potentially useful in a wide variety of token based generative models allowing us to equip these models with the ability to generate at any resolution/ aspect ratio.

### Weaknesses
1. **Novelty** : Although not a very strict weakness, the novelty is somewhat limited by the fact that most of the additional components used in this framework (such as RoPE, RMSNorm, KQ-Norm) have been shown to be effective in previous. Nonetheless, there is some merit in trying to arrive at the optimal combination of such techniques to allow for scalable and efficient generation.
3. **Video Quality**:  Although impressive qualitative results have been shown in the paper for image generation. The videos shared in the supplementary seems to have limited quality. Particularly at high resolution, it seems to generate frames that are super saturated (such as demo number 4 in the supplm). Providing insights about video generation performance at high resolution and potential limitations would help better understand the difference in video vs image quality. In particular, are there specific challenges in video generation that makes it harder/ quality lower than just single frame generation? The use of a standard image VAE for video compression may introduce redundancy and limit temporal coherence, which should be discussed.
4. **Additional Quantitative metrics:** Although the authors have provided extensive quantitative comparisons and ablations, the work would benefit from a user study on generated quality (since FID is mostly a proxy metric). Furthermore, include analysis about prompt adherence for the images generated by different approaches would be insightful .
5. **Audio performance**: Provide some qualitative examples of generated audio in the supplementary materials would help evaluate the performance of the Text-to-Audio mode of the model. In particular, similar to the video and 3D demons in the supplementary, providing a set of generated audio samples for diverse kinds of text prompts would help highlight T2Audio performance of this approach.

### Questions
1. At what frame rates are the video generated?
3. l232-236 : The authors mention that zero-initialized attention induces sparsity in the text conditioning. Is the implication that only 10% of the prompt is being adhered to? Or that only 10% of the prompt embeddings are necessary to generate the image? In particular are there performance benefits (either speed or quality) due to this induced sparsity? Any experiments demonstrating this claim and its associated benefits would be very helpful.
4. The authors mention that videos can be generated upto 128 frames (for a 128K token context window), given that the framework supports any resolution generation, what is the resolution for this generation? (does 1000 token per frame imply a 32*32 latent image?) . Can we generate a lager number of frames at a smaller resolution? In particular, a small graph/ table demonstrating the quality difference as a function of number of frames vs resolution would be helpful. Also, additional insights about how the resolution vs num of frames for the same token budget affects the different T2X modes would provide some value in understanding how to work with different modalities.

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents Lumina-T2X, a family of flow-based large diffusion transformers (Flag-DiT) for multi-modal generation. These models aim to generate content across various modalities like images, videos, multi-view 3D objects, and audio. The authors emphasize that Lumina-T2X is a scalable and adaptable framework that generalizes across different modalities and resolutions.

Motivation: 
- Existing foundational diffusion models, while achieving remarkable results in image and video generation, lack detailed implementation guidance and publicly available source code, or pre-trained checkpoints.
- Existing methods are often task-specific, making it difficult to adapt across modalities.

Technical highlights:
- Adopts DiT (diffusion transformers), but scales it to 7B, beyond previously published work.
- Replaces LayerNorm with RMSNorm and incorporates KQ-Norm to enhance training stability.
- Employs RoPE relative positional embeddings, towards resolution extrapolation, enabling the model to generate images at resolutions beyond those seen during training.
- Adopts the flow matching formulation which constructs continuous-time diffusion paths.
- Incorporates zero-initiated attention for flexible text prompt conditioning.

The authors demonstrated the models' capability to generate images, videos, 3D, and speech, though image generations appears to be the most fleshed out. The modalities (e.g, text-to-image, text-to-video) are trained separately.

### Strengths
Though this paper does not present groundbreaking novelties in its individual components, the combination and effective implementation of existing ideas constitute solid contributions to the community and the advancement of multi-modal generative models.

Strengths:
- Comprehensive and scalable framework. The proposed Lumina-T2X framework offers a unified pipeline for handling diverse modalities like images, videos, multi-view 3D objects, and audio, all guided by text instructions. The authors demonstrate the scalability of Flag-DiT by training models with up to 7B parameters and handling sequences of up to 128K tokens.
- Effective integration of existing techniques. The paper successfully combines a number of existing techniques, such as DiT, RoPE, RMSNorm, and flow matching, to improve the performance and scalability of text-to-image generation. The authors provide thorough ablation studies on ImageNet to validate the advantages of each component.
- Good text-to-image generation results. The text-to-image model within the Lumina model family, achieves very good results in generating high-resolution, photorealistic images with accurate text comprehension. 
- Training-free applications. The paper demonstrates the versatility of the Lumina T2I model by showcasing its capability to perform advanced visual tasks like style-consistent generation, image editing, and compositional generation, all in a training-free manner. This is achieved through clever token manipulations and attention mechanisms.
- The technical details described in the paper, and its open-source (upcoming as the authors indicated) will benefit the research community and foster further exploration in this field.

### Weaknesses
The main weakness, in my opinion, lies in the paper's limited originality. The paper's main contribution lies in the effective integration of existing techniques rather than the introduction of fundamentally new concepts. Many of the individual components, such as DiT, flow matching, have been explored in prior work.



### Questions
A lot of the design (including the incorporation of [nextline] and [nextframe] tokens) appears to indicate that mixed-modality training could be a strength of the work, and yet this was not realized, since the modalities were trained separately. Authors do comment on the "the imbalance of data quantity for different modalities and diverse latent space distribution" being the reason, but more elaboration would be appreciated. 

For image editing, how are the editing prompts incorporated during the Flow ODE solving process? How well-localized are the edits (if the editing instructions refer to a specific object/region)?

In Table 1, it appears the models being compared are of widely varying sizes. It would be great if the size of the models can be indicated in the table, so reader understands what might be effect of scale vs. method/model.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
1. The authors propose Lumina-T2X, a family of Flow-based Large Diffusion Transformers (Flag-DiT) designed for efficient and scalable training. It seamlessly unifies representations across diverse modalities and varying spatial-temporal resolutions.
2. Flag-DiT improves scalability, stability, and flexibility over the original DiT. And it includes four main components, which are frame-wise encoding for different modalities, text encoding with diverse text encoders, input & target construction and network architecture and loss.
3. Lumina-T2X can be used for text-to-image generation, resolution extrapolation and other visual tasks such as style-consistent generation, high-resolution image editing, and compositional generation. And it can achieve these tasks in a tuning-free manner, uniformly tackling these tasks through token operations.

### Strengths
1. Flag-DiT enhances the scalability, stability, and flexibility of the original DiT. 
2. Lumina-T2X can be utilized in multiple applications in a tuning-free manner. The visual quliaty of generated images looks excellent. And it can achieve generative modeling with rapid convergence, robust scalability, and powerful high-resolution capabilities.
3. Lumina-T2X seamlessly unifies the representations of different modalities across various spatial-temporal resolutions.

### Weaknesses
1. Flag-DiT lacks novelty, seems to be a patchwork of techniques borrowed from other methods to address the issues in DiT. For example, RoPE, RMSNorm, KQ-Norm and the flow matching formulation are the technique proposed and used in other works. Please clarify what you consider to be the novel contributions of your work beyond combining existing techniques OR explain the innovation in combining these techniques.
2. Some metrics of Flag-DiT shown in Table.1 do not seem very impressive compared with other state-of-the-art methods. It is clear that the results of some comparison methods are noticeably better.
3. The anthors should provide some visual comparisons of generated images with other SOTA methods to further demonstrate the superiority of Lumina-T2X. The authors can select several methods from Table.1 to perform visual comparisons.

### Questions
1. Did the authors make any modifications on RoPE, RMSNorm, KQ-Norm and the flow matching formulation? Please clarify what you consider to be the novel contributions of your work beyond combining existing techniques OR explain the innovation in combining these techniques.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This manuscript gives detailed introduction on a family of generative models, Lumina-T2X, which shares the same Flag-DiT architectures. By integrating advanced training recipes in the proposed frameworks, the proposed architectures demonstrate superior training stability, easy convergence, and flexible resolution extrapolation. Additionally, preliminary explorations are conducted about its application as an universal architecture for generating data in a wider range of modality.

### Strengths
1.    The proposed framework integrates many advanced techniques for generative models, with clearly demonstration for their motivations and effectiveness. The experience of synergistically combining these components shared in this paper could provide sufficient value for the community.

2.    As a versatile architecture, Flag-DiT has achieved impressively generalizable results across multiple modalities.

### Weaknesses
1.  Despite the appealing properties achieved by integrating many existing techniques, its unique innovative contributions lack clear highlighting.

2.  The quantitative comparisons of the generation for modalities besides image have not been provided.

3.  The paper claims the scalability of the Flag-DiT architecture in many paragraph, but has not convincingly demonstrate the performance gains obtained from scaling.

4.  In L326, “using using” is redundant and should be corrected to a single “using.”

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3
