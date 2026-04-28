# WMAdapter: Adding WaterMark Control to Latent Diffusion Models

- Decision: Reject
- Avg Score: 5.20
- Scores: 6, 6, 6, 5, 3

## Abstract
Watermarking is crucial for protecting the copyright of AI-generated images. We propose WMAdapter, a diffusion model watermark plugin that takes user-specified watermark information and allows for seamless watermark imprinting during the diffusion generation process. WMAdapter is efficient and robust, with a strong emphasis on high generation quality. To achieve this, we make two key designs: (1) We develop a contextual adapter structure that is lightweight and enables effective knowledge transfer from heavily pretrained post-hoc watermarking models. (2) We introduce an extra finetuning step and design a hybrid finetuning strategy to further improve image quality and eliminate tiny artifacts. 
  Empirical results demonstrate that WMAdapter offers strong flexibility, exceptional image generation quality and competitive watermark robustness.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents WMAdapter, a plug-in solution for diffusion-based watermarking. The authors propose training a contextual adapter and introduce a hybrid fine-tuning scheme to mitigate grid artifacts. Experimental results highlight WMAdapter's advantages, particularly in terms of visual quality.

### Strengths
1. WMAdapter is compatible with various diffusion models and watermarking decoders, enhancing its adaptability for real-world applications.
2. The hybrid fine-tuning scheme is innovative, effectively reducing artifacts.

### Weaknesses
1. The mechanism behind hybrid fine-tuning is not fully explained. After fine-tuning the adapter with the VAE decoder, it is unclear why it achieves better quality with the original decoder (Adaptor-I in Table 5), yet produces degraded reconstructions with the fine-tuned decoder (Adaptor-V in Table 5). Further clarification is needed.

2. Although WMAdapter demonstrates superior visual quality, its robustness is weaker than that of StableSignature (Figure 8) and SSL (Table 2). Given the trade-off between distortion and robustness, a more balanced comparison could involve evaluating all methods at comparable visual quality levels to assess robustness fairly.

3. The bit length used by methods like RoSteALS is not specified. Do these methods also embed a consistent 48 bits? If so, are they trained on this bit length for a fair comparison?

### Questions
Please refer to the weakness.

### Soundness
3

### Presentation
2

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
The paper proposes WMAdapter, a watermarking solution for latent diffusion models that embeds user-specific watermarks without altering the underlying diffusion components, maintaining image quality. Key innovations include a Contextual Adapter that adapts watermark embeddings based on image content and a Hybrid Finetuning strategy to enhance visual quality while preserving watermark robustness.

### Strengths
1. The paper is generally well-written and easy to follow.

2. : The idea of Content-Aware Watermarking is knid of interesting and different from previous work: Contextual Adapter adapts watermark embedding based on the image's content, improving the concealment and robustness of watermarks while minimizing visual impact.

3. High Image Quality Preservation.

### Weaknesses
1. Limited novelty in watermarking pipeline.

2. Not comprehensive evaluation of robustness in adaptive settings.

3. Dependency on Pretrained Components.

### Questions
1. The watermarking pipeline shares similarities with Stable Signature, particularly in its foundational approach. However, while Stable Signature fine-tunes the Diffusion U-Net, this study emphasizes modifications to the VAE decoder. Additionally, the concept of integrating an external adaptor is not novel. It is recommended to explicitly highlight the distinctions between this work and prior methods, such as Stable Signature and ControlNet, to better establish its unique contributions.

2. For robustness part, most perturbations evaluated in experiments are common image post-processing methods, such as JPEG and Crop. Apart from surrogate detecor attack and regeneration attack, there are more adaptive attacks such as query-based black-box attack or white-box attack. It is important to consider a comprehensive setting.

3. In terms of robustness, it is observed that the bit accuracy drops to approximately 0.9 when JPEG compression at a quality level of 80 is applied. Is this reduction sufficient for practical robustness? Given that JPEG 80 is considered a moderate perturbation, it would be valuable to analyze the system's response to more severe JPEG compression levels to understand the potential vulnerabilities if an attacker deploys more aggressive degradation techniques.

4. Is there existing literature that defines PSNR values of 32 or 30 as indicative of poor visual quality? This question is relevant since some adaptive attacks result in significant decreases in bit accuracy even when the PSNR remains above 30.

### Soundness
2

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
5

### Summary
The paper proposes a method for generating watermarked images without visible artifacts by introducing a module called the contextual adapter and a targeted fine-tuning strategy.

### Strengths
This method offers a dynamic watermarking mechanism, allowing watermarking of a given image with any arbitrary key (binary message) without needing retraining to adapt to a new key.

### Weaknesses
1. **Lack of Baseline Comparisons**:
*   **Post-hoc watermarking**: The authors have shown some comparisons with frameworks like StegaStamp [1] and RivaGAN [2]. However, a more comprehensive evaluation could have been conducted to establish stronger baseline comparisons. Specifically, the evaluation lacks a thorough analysis of the trade-offs between watermark robustness and image quality compared to other post-hoc watermarking methods. It would be beneficial to see a comparison across a wider range of attacks, including more complex image manipulations, and a more detailed analysis of the performance under varying watermark strengths.
*   **Native watermarking**: Stable Messenger [3], a similar steganography framework to RoSteALS, demonstrates a better trade-off between accuracy and image quality. However, the authors did not provide any comparisons with this approach. This omission is significant, as it leaves the reader unsure of how the proposed method performs against state-of-the-art native watermarking techniques, particularly in terms of the balance between watermark imperceptibility and robustness.

2. **Confusing Contribution**:
The authors claim hybrid fine-tuning as a key contribution of this paper. However, in Table 5, the results of no extra fine-tuning and hybrid fine-tuning primarily demonstrate a trade-off between accuracy and image quality, a common issue in this field. This leaves the exact contribution of this fine-tuning strategy unclear. The paper does not sufficiently articulate why this specific fine-tuning approach is superior to other potential methods, or how it uniquely addresses the challenges of balancing watermark robustness and image fidelity. The lack of ablation studies on the fine-tuning process further obscures its contribution.

3. **Unclear Robustness Evaluation**:
While it's beneficial to see the method's robustness against regeneration attacks, Figure 5 does not clearly demonstrate if WMAdapter is more robust to these attacks than other watermarking methods such as Stable Signature or AquaLoRA. The evaluation lacks a detailed analysis of the specific types of regeneration attacks used and how the proposed method performs against a range of such attacks. A more thorough comparison with other watermarking methods under identical attack conditions would be necessary to establish the robustness claims.

### Questions
Please refer to Weaknesses part.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
Watermarking serves as a prominent means for actively identifying generated content, extensively applied in diffusion model image detection and attribution. Existing methods integrate watermark embedding with image generation but have not considered the relationship between watermark information and image semantics. This paper proposes a watermarking method for diffusion models called WMAdapter, which designs a Contextual Adapter to fuse watermark information with the VAE features in the diffusion model. To further improve the visual quality of watermarked images, the paper also proposes a Hybrid Finetuning strategy. This strategy first fine-tunes the adapter, then simultaneously fine-tunes both the adapter and the VAE decoder, using the fine-tuned adapter with the original VAE decoder during final image generation. Experimental results show that WMAdapter can effectively reduce artifacts.

### Strengths
- The paper is well-written and clearly explained, making it easy for readers to understand.
- A Hybrid Finetuning Strategy is proposed, which further reduces artifacts in the watermark through multiple rounds of fine-tuning.
- WMAdapter is lightweight and easy to deploy, with low training overhead.

### Weaknesses
 - The WMAdapter integrates features from the VAE with watermark information, representing a contextual watermark. However, the authors state in line 413 that WADIFF "uses a context-less structure to encode the watermark." I do not believe that WADIFF is a context-less watermark, as it combines latent representations with watermark information and passes them through a trainable UNet layer. Therefore, both WMAdapter and WADIFF can be considered contextual watermarks. I encourage the authors to provide a more comprehensive comparison between the two methods.
- Based on the experimental results (Table.2 and Figure.8), compared to Stable Signature, this paper sacrifices some robustness in order to achieve better visual quality.
- I believe the experimental setup for the FID metric needs to be reconsidered. FID is used to measure the quality of generated images, and in related work, it is typically calculated between watermarked images and real images from the dataset to assess the impact of the watermark on the model's generation quality. This approach would be more reasonable.
- In section 4.3, "Robustness to More Attacks," this paper only presents results for WMAdapter-F against the Regeneration attack and the Surrogate detector attack. To better evaluate the robustness of WMAdapter, the results for WMAdapter-I should also be included.
- The Hybrid Finetuning strategy is a highlight of this paper; however, the final implementation uses the original VAE decoder instead of the finetuned VAE decoder. While Figure 6 intuitively demonstrates the effectiveness of this approach, I hope the authors can further investigate the reasons behind the occurrence of lens flare artifacts.

### Questions
- I believe the experimental setup for the FID metric needs to be reconsidered. FID is used to measure the quality of generated images, and in related work, it is typically calculated between watermarked images and real images from the dataset to assess the impact of the watermark on the model's generation quality. This approach would be more reasonable.
- In section 4.3, "Robustness to More Attacks," this paper only presents results for WMAdapter-F against the Regeneration attack and the Surrogate detector attack. To better evaluate the robustness of WMAdapter, the results for WMAdapter-I should also be included.
- The Hybrid Finetuning strategy is a highlight of this paper; however, the final implementation uses the original VAE decoder instead of the finetuned VAE decoder. While Figure 6 intuitively demonstrates the effectiveness of this approach, I hope the authors can further investigate the reasons behind the occurrence of lens flare artifacts.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposed a method called WMAdapter which introduced an external component to the latent diffusion model to add a contextual watermark onto the generated images. The experiments showed that WMAdapter achieved similar bitwise accuracy to other methods while maintaining better image quality. The robustness of the proposed method is also evaluated on some image post-processing method.

### Strengths
1. The proposed method maintains better image quality than the existing ones.
2. The robustness of the proposed watermarking method is evaluated on some commonly seen image processing methods.
3. The contextual watermarking idea is interesting.

### Weaknesses
1. Though the authors claim that they keep the diffusion model intact to get better image quality, their watermarking method changes the internal embedding within the VAE decoder. I think both changing VAE decoder's parameters and changing the internal embedding will hugely affect the quality of the generated image. The core issue is that any modification to the latent space, whether through parameter changes or embedding manipulation, will inevitably alter the output distribution of the VAE decoder. It's not clear why modifying the internal embedding should be fundamentally less disruptive than modifying the decoder parameters, given that both operate on the latent representation.
2. The robustness of the proposed method against adversarial attacks is worrying. Specifically, the bitwise accuracy drops significantly under adversarial perturbations, indicating a vulnerability to even minor image manipulations. The fact that the watermark can be easily removed with a PSNR around 30 suggests a lack of practical security in real-world scenarios where attackers can introduce small perturbations.
3. The reason why hybrid finetuning works is not clarified. The paper lacks a clear explanation of why fine-tuning both the VAE decoder and the watermark module, but only using the watermark module during inference, achieves better results than other variants. This raises questions about the underlying mechanism and the specific interaction between the fine-tuned decoder and the watermark module during training.

### Questions
1. I do not think changing the VAE decoder's parameters and changing the internal embedding of the image are mathematically different. Both of them will affect the quality of the generated images. Given the results shown in Table 2 in which WMAdapter achieves worse robustness results compared to other methods, does it mean that the better image quality of WMAdapter is just simply a trade-off between image quality and robustness?
2. In Figure 5, WMAdapter achieves bad robustness results against adversarial perturbations. Specifically, the bitwise accuracy decreases to almost 50% when the PSNR is around 30, which means the watermark can be easily removed by the attacker in the real-world scenario.
3. For hybrid finetuning, it is confusing that finetuning both the VAE decoder and the watermark module and using only the watermark module during the inference achieves better results than  other variants. I think detailed explanations and more experiments should be included for this part.
4. For Figure 8 in Appendix, the proposed method also shows worse robustness compared to Stable Signature, which also shows the improvement in image quality is only a trade-off.

### Soundness
2

### Presentation
3

### Contribution
2
