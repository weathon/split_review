# MotionAura: Generating High-Quality and Motion Consistent Videos using Discrete Diffusion

- Decision: Accept
- Avg Score: 7.33
- Scores: 8, 6, 8

## Abstract
The spatio-temporal complexity of video data presents significant challenges in tasks such as compression, generation, and inpainting. We present four key contributions to address the challenges of spatiotemporal video processing. First, we introduce the 3D Mobile Inverted Vector-Quantization Variational Autoencoder (3D-MBQ-VAE), which combines Variational Autoencoders (VAEs) with masked token modeling to enhance spatiotemporal video compression. The model achieves superior temporal consistency and state-of-the-art (SOTA) reconstruction quality by employing a novel training strategy with full frame masking. Second, we present MotionAura, a text-to-video generation framework that utilizes vector-quantized diffusion models to discretize the latent space and capture complex motion dynamics, producing temporally coherent videos aligned with text prompts. Third, we propose a spectral transformer-based denoising network that processes video data in the frequency domain using the Fourier Transform. This method effectively captures global context and long-range dependencies for high-quality video generation and denoising. 
Lastly, we introduce a downstream task of Sketch Guided Video Inpainting. This task leverages Low-Rank Adaptation (LoRA) for parameter-efficient fine-tuning. Our models achieve SOTA performance on a range of benchmarks. 
Our work offers robust frameworks for spatiotemporal modeling and user-driven video content manipulation. We will release the code, datasets, and models in open-source.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents a novel text-to-video framework, providing comprehensive and reasonable technical details from VAE to model architecture, as well as downstream applications. The paper proposes an effective VQ-VAE training strategy, achieving state-of-the-art compression and reconstruction results, which can be utilized by existing generative models. It also introduces an efficient spectral transformer that encodes information into the frequency domain for processing. Furthermore, the design concepts for downstream applications are illustrated within the context of the sketch-guided video inpainting task.

### Strengths
The paper constructs a complete and efficient new framework for text-to-video generation, featuring innovative modules supported by convincing quantitative evaluations and generative results. Specific strengths include:

- For the VQ-VAE, the paper introduces two novel optimization strategies: *random masking* and *Masked Frame Index Loss*, which allow the VAE to learn spatial relationships and temporal consistency. The compression and reconstruction quality reaches state-of-the-art levels, and the visualization results demonstrate strong feature extraction and representation learning capabilities. These strategies could serve as foundational components for future models.
- A diffusion framework for discrete space is proposed, which encodes information such as videos into the frequency domain for computation, featuring an elegantly designed spectral transformer structure. After training, this framework achieves satisfactory results in terms of generation speed and quality.
- Based on the proposed generative framework, the design of the sketch-guided video inpainting task provides a proof of concept for the framework's scalability and efficient transfer applications. According to the paper, this also marks the first introduction of sketch-guided generation for videos.
- The constructed dataset, if made open-source, would be a significant contribution to the community.

### Weaknesses
While the paper is rich in content, there are some potential issues:

- The two supervisory strategies designed for the VAE elevate its capabilities to state-of-the-art levels. Although the paper states that the random masking strategy enables the model to learn spatial information and that supervision for the fully masked frame index prediction enhances temporal consistency, it seems there are no related ablation studies provided to explore the specific reasons for model improvement further. Specifically, the impact of varying masking ratios in the random masking strategy, or the effect of different temporal distances between masked frames in the fully masked frame index prediction, are not explored. This lack of detailed analysis makes it difficult to fully understand the contribution of each component.
- The condition injection framework designed for the sketch-guided video inpainting task appears relatively straightforward, lacking innovative design at the technical level. The method seems to rely on a basic concatenation or addition of the sketch embedding with the video latent representation, without exploring more sophisticated fusion techniques. The paper does not discuss how the model handles potential conflicts between the sketch guidance and the video context, or how the model ensures that the inpainting is both consistent with the sketch and the video content.

### Questions
- Are there any evaluation or ablation study results available regarding Randomly Masking and Fully Mask Frame Index Predicting?
- Will the model or dataset be made open-source?

### Soundness
4

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
3

### Summary
This paper introduces an innovative set of methods designed to enhance video generation. These include the 3D-MBQ-VAE, which improves video compression, a novel text-to-video generation framework, a spectral transformer-based denoising network for superior video generation, and a Sketch Guided Video Inpainting task that utilizes Low-Rank Adaptation (LoRA) for efficient fine-tuning.

### Strengths
1.The authors propose a denoising network named Spectral Transformer that processes video latents in the frequency domain using the Fourier Transform, capturing global context and long-range dependencies effectively.

2.The paper is the first to address the downstream task of sketch-guided video inpainting, using LORA adaptors for parameter-efficient fine-tuning of the denoising network.

### Weaknesses
1.3D-MBQ-VAE Concerns:

(1)W.A.L.T[1] has demonstrated that using a 3D casual VAE can allow for joint training with both images and videos in text-to-video models, significantly improving performance compared to training solely with videos. Can the authors discuss whether the proposed 3D-MBQ-VAE can also support such joint image and video training? If feasible, it would be beneficial to see an experiment demonstrating this capability and comparing it with that of W.A.L.T.

(2) In the comparative experiments listed in Table 1, could the authors provide comparative results of MAGVIT-v2[2] in regard to Video Compression Metrics or Video Reconstruction tasks? Specifically, it would be helpful to see results using the same bit rate and evaluation metrics as MAGVIT-v2 to ensure a fair comparison.

 (3) Codebook (Vocabulary) Size Influence: As far as I understand, the size of the codebook could considerably affect the 3D-MBQ-VAE's reconstruction ability. However, the paper doesn't seem to mention any information relating to the codebook size. Could the authors provide additional details on the impact of varying codebook sizes on video reconstruction, including specific codebook sizes, embedding dimensions, and the resulting impact on reconstruction quality metrics like PSNR, SSIM, and LPIPS?

2.Experiment Setting for Text-to-Video Model: In Table 3, the authors used WebVID10M as the training data and also computed FVD and other metrics on WebVID10M for testing. However, the comparative methods did not use WebVID10M in their training data, which suggests that other text-to-video methods computed FVD and other metrics in a zero-shot manner. In addition, specifics like the sampling schedule, sampling steps, and classifier-free guidance scale used by the authors' proposed method and the comparison methods were not disclosed. To ensure a fair comparison, could the authors evaluate all models (including theirs) in a zero-shot manner on a common test set, like FVD of UCF-101? Also, providing a table or an appendix detailing all the hyperparameters and settings for each method would greatly enhance reproducibility and fairness in comparison.

### Questions
1.Based on my understanding, the videos in the WebVid10M dataset all contain watermarks. I'm curious as to how the videos generated by the model, which was trained on this dataset, do not have any watermarks. Can the authors explain this?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors propose MotionAura, a novel text-to-video generation model. The authors begin with the 3D Mobile Inverted VQVAE to enhance spatiotemporal video compression. The discrete diffusion process is also carried out in the spectral domain rather than the traditional pixel or latent space. The model exhibits SOTA compression results and promiosing results on T2V and downstream tasks.

### Strengths
- The spectral transformer is novel and works better than its counterpart transformer, as evidenced by the ablation study.
- The author proposed pretraining the 3D-MBQ-VAE using random and complete masking and get better results than the counterpart compression models.
- The authors show very pleasing, temporally consistent video samples that showcases the effectiveness of the proposed model

### Weaknesses
 - Some of the ablation experiments are missing e.g., in the 3D-MBQ-VAE with regard to the different losses
- It is generally not clear why the authors would not prefer a continuous space rather than opting for the discrete space
- Some of the training details is still missing, e.g., what is the masking ratio of random masking and full frame masking in 3D-MBQ-VAE?
- The spectral transformer part of the paper can be augmented with more analysis
- It's not clear how the temporal downsampling is performed in the 3D-MBQ-VAE encoder, and the reported Frame Compression Rate of 4 seems inconsistent with Figure S.8.
- The application of FFT to text embeddings lacks clear justification, as it's unclear if text embeddings share structural or frequency-domain similarities with image embeddings.
- The rationale for applying FFT in the cross-attention mechanism, where Q is derived from image tokens and K, V from text tokens, is not well-explained, especially since neither Q nor K, V constitute a continuous image domain.

### Questions
- Traditional DMs (e.g., DDPM, EDM, LDMs) works perfectly fine with the continuous space. Could the authors explain why they see the need of going to the discrete space and transferring the diffusion paradigm to the discrete space? Is it only due to the encoder being more performant in this setting?
- Could the authors explain the $\mathcal{L}_\text{MFI}$ loss which is indicated as *Index of completely masked frame* in Figure 2? Is this supposed to be some auxillary discrimator loss that detects whether the frame is masked or not?
- If the former is true, an ablation experiment that include $\mathcal{L}_\text{MFI}$ in the continuous space would be convincing
- Can you provide more ablation in how $\mathcal{L}_\text{MFI}$ helps? What is the masking ratio of random masking and full frame masking?
- In Table 1, you show a Frame Compression Rate of 4 but I can't find in the paper where you talk how you downsample temporally and seem to be inconsistent with Figure S.8. A little bit of explanation would be nice
- It's excited to see that Fourier transform also works with MSA and can further boost the performance of transformer. Since the self-attention and cross attention are working in a totally separate domain, it would be very interesting to show the activations of the attention in the spectral domain to gain more insight.
- Another question with regard to FFT: In the cross attention part $Q$ is calculated from the image tokens and $K$, $V$ are calculated from the text tokens. Why would FFT still make sense in those domain since neither $Q$ or $K$, $V$ constitutes a continuous image domain? How do you make sure that FFT works on the discrete image tokens and why would FFT even make sense on the text tokens?

### Soundness
3

### Presentation
3

### Contribution
3
