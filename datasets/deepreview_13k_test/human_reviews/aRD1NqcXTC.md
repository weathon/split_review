# High-Quality Joint Image and Video Compression with Causal VAE

- Decision: Accept
- Scores: 8, 8, 5, 6, 6

## Abstract
Generative modeling has seen significant advancements in image and video synthesis. However, the curse of dimensionality remains a significant obstacle, especially for video generation, given its inherently complex and high-dimensional nature. Many existing works rely on low-dimensional latent spaces from pretrained image autoencoders. However, this approach overlooks temporal redundancy in videos and often leads to temporally incoherent decoding. To address this issue, we propose a video compression network that reduces the dimensionality of visual data both spatially and temporally. Our model, based on a variational autoencoder, employs causal 3D convolution to handle images and videos jointly. The key contributions of our work include a scale-agnostic encoder for preserving video fidelity, a novel spatio-temporal down/upsampling block for robust long-sequence modeling, and a flow regularization loss for accurate motion decoding. 
Our approach outperforms competitors in video quality and compression rates across various datasets. Experimental analyses also highlight its potential as a robust autoencoder for video generation training. Code and models will be open-sourced.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper presents a novel approach to joint image and video compression via a causal variational autoencoder (VAE) that leverages 3D convolutional and self-attention mechanisms. Designed to tackle the challenge of temporal and spatial redundancy in video data, the proposed model incorporates a dual-path architecture for downsampling and upsampling, as well as a flow regularization loss to maintain temporal coherence. Key contributions include a scale-agnostic encoder, a dual-path network for robust spatio-temporal feature extraction, and a loss function to enhance motion preservation in compressed sequences. The experimental results show the model’s superiority in video fidelity and compression rates over existing methods, particularly in handling large motions and maintaining temporal consistency.

### Strengths
Hybrid Approach: The paper successfully integrates causal 3D convolutions with self-attention layers to handle temporal and spatial redundancy in video compression, creating a versatile model capable of high-quality compression for both images and videos. This hybrid approach is particularly relevant as it extends beyond existing methods that often separate these tasks or overlook temporal redundancy.
Robust Encoder-Decoder Design: By leveraging a dual-path downsampling and upsampling mechanism, the proposed model achieves a high compression rate without significant quality loss, evidenced by its superior PSNR and SSIM scores in Table 1. Additionally, the FILM encoder’s ability to handle large motion in compressed videos aligns well with contemporary needs in video compression.
Comprehensive Evaluation: The paper rigorously evaluates its model across multiple datasets and compression settings, supporting its claims with ablation studies and comparisons to several state-of-the-art methods. The qualitative results further emphasize its performance in preserving motion fidelity and detail, especially for fast-moving objects.

### Weaknesses
* The paper should cite the recent ECCV 2024 work, Hybrid Video Diffusion Models with 2D Triplane and 3D Wavelet Representation, as this paper also explores autoencoder backbones and addresses related challenges in video compression. A comparative analysis, including quantitative and qualitative evaluations against this baseline, would strengthen the evidence for the proposed model’s advantage.
* The claim that the dual-path network is "temporally agnostic and can encode and decode arbitrarily long videos at varying lengths" may be overstated. The performance improvements in Table 4’s ablation study do support better temporal adaptability; however, the reliance on learnable kernels suggests some degree of generalization error remains, as evidenced by performance drops with different sequence lengths. It would be more accurate to moderate this claim, acknowledging the limitations indicated by remaining performance variability.
* Given the paper’s focus on maintaining high spatio-temporal quality in compressed videos, metrics specifically targeting spatio-temporal fidelity must be also compared, such as STREAM (ICLR 2024 STREAM: Spatio-TempoRal Evaluation and Analysis Metric for Video Generative Models). These metrics could provide a more nuanced understanding of the model’s strengths and areas needing improvement in terms of temporal coherence and spatial detail.
* The model’s large size and complexity might raise concerns about overfitting, particularly when evaluated on datasets like UCF101 and SkyTimelapse. To address this, a thorough analysis for potential overfitting or memorization is recommended, especially in cases where generated samples closely resemble training data. Expanding the qualitative analysis in Figure 4 to include more diverse sample comparisons would help clarify this aspect.
* Table 1 demonstrates the model’s robustness at more severe compression rates (e.g., 4\times8\times8 and 8\times8\times8), but the performance at commonly used settings such as 1\times8\times8 and 4\times4\times4 is not discussed. Adding a direct comparison at these standard settings would provide a more balanced view, allowing for an "apple-to-apple" comparison with other models. Such an addition could reveal how the model’s advantages scale across different compression intensities, offering deeper insights into the model’s comparative performance under varying constraints.
* To provide readers with an estimation of computational resources and convergence speed, including additional details on training time until convergence would be beneficial. This information would help contextualize the model’s practical application feasibility.
* Please elaborate more on 3D Model Extension in GAN Training.
* Although the introduction mentions experiments on noise corruption and varying sequence lengths, these are not included in the main text. Readers may find it disorienting without a clear reference directing them to the Appendix for these analyses. Please note this clearly. 
* Is normalization applied during the concatenation of FILM’s outputs? Wouldn't it be problematic if they are not normalized (due to different output statistics from different scales)?
* Any specific reason for using 1+T over T? 
* In the conclusion, "3 key contributions" -> "three key contributions"

### Questions
Please see Weaknesses

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces a novel architecture for 3D Causal VAE aimed at image and video compression, addressing three key issues found in existing video VAE architectures: 

1. Handling Small and Fast-Moving Objects at Higher Compression Rates: Standard encoders struggle with these objects. The authors tackle this by proposing a FILM-based encoder.

2. Downsampling and Upsampling Challenges: Non-learnable downsampling loses high-frequency spatiotemporal (ST) information, while learnable downsampling tends to overfit. To address this, the authors propose a novel Down and Upsampling layer design that employs a dual-path network with parallel branches utilizing both learnable and non-learnable kernels.

3. Motion Reconstruction Quality and Smoothness: To enhance these aspects, the authors introduce a novel Flow Regularization loss that facilitates in Video VAE training.

The authors trained their 3D VAEs at various compression rates (T × H × W) such as 4 × 8 × 8 (256), 8 × 8 × 8 (512), 16 × 8 × 8 (1024), and 16 × 16 × 16 (4096). Their experiments showed strong results when compared to other baselines.

Overall, this is a good paper that introduces novel architectural decisions for Video-VAE and shows strong experimental results. However, it would benefit from including additional experimental results and details (See Weaknesses and Questions).

### Strengths
1. Importance: This paper addresses a critical issue of training a high-quality VAE for image and video compression.

2. Novelty: The paper introduces a unique and previously unexplored approach to tackle the aforementioned problem.

3. Results Quality: Experimental results demonstrate strong performance compared to existing baselines. Notably, the paper provides results for very high video compression rates (16 × 8 × 8 and 16 × 16 × 16).

4. Clarity: The main text of the paper is well written and easy to follow.

5. Ablations: Ablation studies clearly illustrate the positive impact of the proposed architectural decisions.

### Weaknesses
1. Missed comparisons: Tables 1 and 2 do not include comparisons with CogVideoX VAE [1] and CV-VAE [2], which are significant baselines in this field.

2. Video quality metrics: Table 1 reports only frame-wise video quality metrics and neglects any temporal consistency metrics. It is recommended to measure the Fréchet Video Distance (FVD) between original and reconstructed videos (rFVD) to provide a more comprehensive evaluation.

3. Video generation results: The video generation results in Table 3 were conducted on relatively simple video datasets such as SkyTimelapse and UCF-101. It is recommended to include experiments on more complex datasets and tasks, such as text-conditional video generation on the WebVid dataset, to better assess the proposed method's capabilities.

4. Evaluation resolution: The authors have not specified the evaluation resolution for videos in Tables 1 and images in Table 2, which is crucial for assessing the results accurately. 

5. Analysis on different resolutions: The paper lacks an analysis of how the proposed VAE performs across different resolutions compared to other baselines. The performance on high-resolution videos (e.g., 720p) is particularly relevant and should be explored.

6. Inference time: Information about the inference time of the models in Tables 1 and 2 is missing. Including this data would provide a better understanding of the practical utility of the proposed method.

7. Method’s limitations: The paper does not provide an analysis of the limitations of the proposed method, which is necessary for a comprehensive evaluation.

### Questions
My main concerns and comments regarding the paper are related to the experiment section:

1. Tables 1 and 2 would benefit from including results for CogVideoX VAE [1] and CV-VAE [2], adding rFVD metric,  providing information about evaluation resolution and inference time of the models. Please refer to weaknesses 1, 2, 4, and 6 for more details.

2. The paper would benefit from adding limitation analysis of the proposes method. Especially interesting to see how the method generalizes to different video resolutions (128x128, 256x256, 512x512, 480p, and 720p) in comparison with other methods. For more details see weaknesses 5 and 7.

3. Table 3 provides video generation results for relatively simple datasets and tasks. It is recommended to test the model on text-conditional video generation on the WebVid dataset if possible. Refer to weaknesses 3 for more details.

[1] Yang, Z., Teng, J., Zheng, W., Ding, M., Huang, S., Xu, J., ... & Tang, J. (2024). CogVideoX: Text-to-video diffusion models with an expert transformer. arXiv preprint arXiv:2408.06072.

[2] Zhao, S., Zhang, Y., Cun, X., Yang, S., Niu, M., Li, X., ... & Shan, Y. (2024). CV-VAE: A Compatible Video VAE for Latent Generative Video Models. arXiv preprint arXiv:2405.20279.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a video VAE for video compression and generation tasks. It features 4 major components: a causal 3D residual block, spatio-temporal downsampling module, spatio-temporal attention module, and FILM encoder. The proposed VAE is tested with the autoencoding and generation tasks.

### Strengths
The proposed method is evaluated with both the video/image autoencoding task and the video generation task. Moreover, extensive ablation studies were conducted to validate the effectiveness of the proposed method.

### Weaknesses
(1) The title “joint image and video compression” is misleading. I believe the task is focused primarily on video generation, not video transmission or compression (i.e. the autoencoding task). If the task is video compression/autoencoding, the resulting rate-distortion performance of the proposed method should be compared with that of the prior works on end-to-end learned video compression. However, this was not done when the authors reported results on the video/image autoencoding task. Just because the resulting latents have smaller dimensionality does not suggest that they would have smaller bit rates.

(2) In terms of the newly proposed components, I have the impression that their novelty is not very high.

(3) The necessity of causality is unclear in the context of video generation. If the aim is to enable both image and video generation, the image generation task is not explored in the current writing.

### Questions
(1) The title “joint image and video compression” is misleading. I believe the task is focused primarily on video generation, not video transmission or compression (i.e. the autoencoding task). If the task is video compression/autoencoding, the resulting rate-distortion performance of the proposed method should be compared with that of the prior works on end-to-end learned video compression. However, this was not done when the authors reported results on the video/image autoencoding task. Just because the resulting latents have smaller dimensionality does not suggest that they would have smaller bit rates.  

(2) In Table 1, Video LDM (1 x 8 x 8) actually performs quite well particularly on DAVIS with large motion, as opposed to your better performing variant (4 x 8 x 8). Notably, Video LDM has relatively better TS performance. This leads to an impression that the proposed method cannot model well fast-motion sequences.

(3) The model size and MAC/pixel are currently missing in Table 1. Also, except TS, all the quality metrics are for images, not video. Why not use VMAF?

(4) I wonder if the competing methods adopt the GAN loss for training. This needs to be clarified in Table I. In addition, it is unclear how much the GAN loss contributes to the performance of the proposed method.

(5) For the image autoencoding task, how is the proposed method used?

(6) For the video generation task, it is unclear whether the proposed VAE is trained or fine-tuned together with the diffusion model. It appears to me that the proposed VAE is pre-trained to generate latents that follow a simple Gaussian distribution. 

(7) In addition, the proposed VAE can be a stand-alone approach to video generation. I wonder how it performs as compared to the diffusion-based modeling of the video latents.  

(8) In Figure 4, I wonder whether the proposed method can generate well fast-motion sequences. 

(9) FILM encoder is shown to be effective in the ablation study. But, the proposed VAE does not appear to work well on the autoencoding task in Table I, as compared to Video LDM.  This is a bit confusing.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents several improvements to the Video VAE architecture. First, it introduces 3D causal convolutions to encode images and videos simultaneously. Second, it employs a 2 + 1D attention layer for separate interactions of spatiotemporal information, referred to as the STAttnBlock in the paper. Third, it utilizes a two-pathway approach in the upsampling module, with one pathway being learnable and the other non-learnable. Lastly, an interesting contribution is the introduction of the FILM encoder, which shares encoder weights to handle videos resized to different scales. The experiments claim that the proposed method achieves significant results. However, I think that important parameters are not presented in the experiments, and these parameters could greatly affect the experimental metrics.

### Strengths
1. The proposed FILM Encoder is designed well: its pyramid structure enhances the model's ability to reconstruct targets of varying sizes, improving detail retention and overall reconstruction quality. The use of shared modules also bolsters the model's robustness. Additionally, the ablation experiments presented in the paper demonstrate that the FILM Encoder indeed improves reconstruction performance.
2. The Flow Regularization introduced in this paper will contribute positively to motion continuity in video reconstruction.
3. The experiments conducted on video generation effectively demonstrate that this VAE structure can be utilized for downstream diffusion training.

### Weaknesses
Although the model is well designed, I am skeptical about the correctness of the experiment. In previous work (such as the SD3 report and the CogVideo X report), the number of latent channels has been emphasized as having a significant impact on reconstruction performance and metrics. The CogVideo report demonstrates that a model with a configuration of 4x8x8 and 8 latent channels achieves about 3 points higher PSNR compared to a model with 32 latent channels. However, in the experiments of this paper, the 4x8x8 model shows nearly 4 points higher PSNR than the compression rate model, while the 8x8x8 compression rate model surpasses the PSNR of the 4x4x4 token compression rate VideoGPT by 0.23 points, despite having a 64 times higher compression rate. Even in the 16x8x8 model, the LPIPS metric remains superior to VideoGPT, which is quite surprising. The paper does not specify the number of latent channels in the model, raising concerns about the comparability with similar models (e.g., Open-Sora, which has only 4 latent channels). I believe that the overall compression rate (considering latent channels) is a fundamental factor limiting VAE reconstruction performance. If the total compression rates were the same, the differences in metrics would likely not be so pronounced. Therefore, I am concerned about the rigor of the experiments presented.

### Questions
1. Has the author explored the number of latent channels? If so, I would like to see those findings and understand why they were not presented in the paper.
2. How can the authors explain the superior performance of the 8x8x8 compression rate model over the 4x4x4 compression rate model, given the 64 times difference in compression ratio? Similarly, the 16x8x8 model outperforms the 4x4x4 model in LPIPS metrics, despite a 128 times difference in compression ratio. I believe this discrepancy cannot be solely attributed to training tricks or model design.

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
3

### Summary
This paper presents valuable improvements in the video VAE domain. The main innovations include a multiple-scales encoder, dual-path spatio-temporal sampling module, and flow regularization loss. The experimental design is comprehensive, particularly in downstream task validation.

### Strengths
This paper presents valuable improvements in the video VAE domain. The main innovations include a multiple-scales encoder, dual-path spatio-temporal sampling module, and flow regularization loss. The experimental design is comprehensive, particularly in downstream task validation.

### Weaknesses
If the following areas can be optimized, the quality of the paper will improve. Key areas for enhancement include:

1.Enhanced Visualization in Experiments
Current Observation: While the experiments are comprehensive, covering downstream tasks such as image and video generation, this section primarily relies on metric comparisons and lacks crucial visualization analysis.
Recommendations:
Figure 4 Enhancement: Add a comparison of videos generated by OpenSora and the combination of your method with OpenSora. This will provide a clearer visual demonstration of the improvements introduced by your approach.
Ablation Study Visualization: In Figure 5, include visual results showcasing the effects of individual components. For example, display results with and without Spatio-Temporal Down/Upsampling, with and without flow regularization, and with and without Spatio-Temporal Attention. This will help illustrate the contribution of each component to the overall performance.

2.Comparison with SVD-VAE
Current Observation: The paper lacks a comparison with SVD's Variational Autoencoder (SVD-VAE), which is relevant to the presented work.
Recommendation: Incorporate a comparison with SVD-VAE in Table 2. This will provide a more comprehensive evaluation of your method against existing approaches and highlight its relative strengths and weaknesses.

3.Innovation of Improvement Methods
Current Observation: The three proposed improvement methods in the paper are generally intuitive but lack a certain degree of innovation.
Recommendation: To enhance the paper's contribution, consider elaborating on the novelty of each improvement method. Provide deeper insights into how these methods advance the current state of the art beyond intuitive enhancements.

### Questions
1. Clarification of the Ablation Study
   How can the ablation study section be enhanced to clearly demonstrate the impact of adding or removing individual metrics? Additionally, would it be beneficial to include comparisons for configurations such as baseline + a, baseline + b, baseline + c, baseline + d, and the combined baseline + a + b + c + d?

2. Inclusion of Visualization Analysis in Experiments
   While the experiments are thorough and encompass downstream tasks like image and video generation with metric comparisons, the analysis lacks essential visualization components. Could the authors incorporate visualization analyses to complement the metric-based evaluations?

3. Comparison with SVD-VAE in Table 1 
   I recommend adding a comparison with SVD-VAE in Table 1 to provide a more comprehensive evaluation of the proposed method against existing models.

These refined questions and suggestions aim to provide constructive feedback that can help clarify ambiguities, address potential limitations, and enhance the overall quality of the work during the rebuttal and discussion phases.

### Soundness
3

### Presentation
3

### Contribution
2
