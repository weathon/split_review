# UniVAE: A Unified Frame-Enriched Video VAE for Latent Video Diffusion Models

- Decision: Reject
- Scores: 3, 6, 6, 3

## Abstract
Variational Autoencoder (VAE) underscores its indispensable role along the growing prominence of Latent Video Diffusion Models (LVDMs). Nevertheless, current latent generative models are generally built upon image VAEs, which compress the spatial dimension only. While, it is vital for video VAE to model temporal dynamic patterns to produce smooth high quality video reconstruction. To address these issues, we propose UniVAE, which compresses videos both spatially and temporally while ensuring coherent video construction. Specifically, we employ 3D convolutions at varying scales in the encoder to temporally compress videos, enabling the UniVAE to capture dependencies across multiple time scales. Furthermore, existing VAEs only reconstruct videos at a low resolution and fps, bounded by limited GPU memory, which makes the entire video generation pipeline fragmented and complicated. Thus, in conjunction with the new encoder, we explore the potential of the VAE decoder to perform frame interpolation, aiming to synthesize additional intermediate frames without relying on standalone add-on interpolation models. Compared with existing VAEs, the proposed UniVAE explores a unified way to compress videos both spatially and temporally with jointly designed encoder and decoder, thus achieving accurate and smooth video reconstruction at a high frame rate. Extensive experiments on commonly used public datasets for video reconstruction and generation demonstrate the superiority of the proposed UniVAE. The code and the pre-trained models will be released to facilitate further research.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper presents a video VAE that compresses input videos both spatially and temporally. The key contributions are twofold. First, unlike most previous approaches that use a fixed temporal kernel size for downsampling, the authors propose a multi-kernel temporal convolution scheme to better capture the video’s temporal dynamics. Second, they incorporate an interpolation decoder alongside a reconstruction decoder, conditioned on both the sampled latent and the reconstructed outputs, enabling flexible video generation. Experimental results are provided for both video reconstruction and generation tasks.

### Strengths
+ The multi-kernel convolution approach in the encoder network is intriguing and should be further explored
+ Integrating an interpolation module within a VAE model is novel and could provide a more efficient approach for unified video compression and generation.

+ The quantitative results are strong.
+ The paper is generally well-written.

### Weaknesses
- *The various ideas introduced in the paper lack sufficient motivation, and the technical contribution is limited.* 

    - The introduction does not convincingly explain why we need the proposed multi-kernel convolution approach.

   - Why does temporal pooling operation limit the ability of video VAEs (Line 51)? Why would applying different kernels across channel partitions necessarily facilitate better temporal modeling? How did the authors decide to apply the kernels for each channel partition? Which partition uses the smaller temporal kernels and the larger ones?

    - Why is the multi-kernel convolution applied only during downsampling? Did the authors employ the same scheme in the upsampling stage? As the spatiotemporal dimension has to match across the partitions, a larger temporal kernel also implies using larger temporal padding and stride which could be counterintuitive to the basic benefit the authors are arguing.

    - If the interpolation decoder is trained independently, isn't it the same as training a separate interpolation model (given that the encoder and the reconstruction decoder are frozen)? How important is it to use the sampled latent as an input to the interpolation decoder? What is the benefit of adding the reconstructed frames in the interpolation decoder? How does the overall approach compare with just using a pre-trained, state-of-the-art interpolation model on top of the reconstructed frames? There should be a more thorough analysis in this regard. 

    - The claim that this is the first paper to unify spatial and temporal modeling in the encoder is too strong and not correct (Line 111). Many previous works such as OS-VAE and OD-VAE do both spatial and temporal compression.

    - The authors claim their work is specifically for video data (Line 106). Then, what is the motivation for using causal 3D convolutional networks which are commonly used for joint image and video encoding/decoding? Why formulate the problem using N+1 frames?
 

- *Several important details are missing, making it challenging to assess whether a fair experimental comparison was conducted.*
 
    - What is the dataset used for training the proposed VAE? Why use 10^6 steps for the second stage? Isn’t it too much? What are the coefficients used for the different loss functions? Did the authors train their model from scratch or initialize it with pre-trained weights from image VAEs? Did the GAN training start at the same time as the reconstruction training in stage 1? Do both stage 1 and stage 2 use the same set of loss functions?

    - The resolution of the videos used for evaluation in Table 1 is quite small (x256). Why? Why not try the inference at a higher resolution if the design is GPU-efficient?

    - For the competing baselines, did the authors use pre-trained checkpoints or train from scratch? I understand it is not an easy task to train the other models from scratch and I don’t expect that. However, given the significant leap in reconstruction performance (+3dB), I want to hear more about the efforts the authors put on to ensure the comparisons are as fair as they can be.

    - Why is the FVD score so high in Table 2? What is the length of the video clips used for evaluation? How many clips are generated? The numbers indicate poor generation quality (i.e. very high FVD). Isn’t it counterintuitive to the reconstruction performance of the decoder? What are the settings used in generation training and evaluation?


- *The experimental results and ablations are not thorough enough to fully demonstrate the proposed ideas' merits.*

    - The authors fail to convincingly argue why their proposed approach gives a very strong performance compared to previous methods in Section 4.2. What makes the proposed approach very unique to achieve such a performance? Does using multiple kernels give such a performance boost? 

    - The qualitative analysis in Fig. 4 is not very informative. An example depicting the differences between the different methods would have been better.

    - The claim in Lines 419-420 does not hold unless a comparison with a pre-trained interpolation method is shown

    - Which video dataset is used for the experiment in Section 4.4? The performance gap between OD-VAE and UniVAE in Fig. 6 does not seem to be large for small (17) or medium (65) length frames. This appears to be contradictory to the results reported in Table 1 which are evaluated at 25 frames. Why is that?

    - The ablation results in Fig 7 are not convincing. It can be argued that the results of UniVAE-v2 seem to be better (sharper details)  than UniVAE

- *The qualitative analysis is limited.*

    - There are no video results for either reconstruction or generation tasks. This is critical to visualize the benefit of the proposed design choices beyond quantitative numbers. 
    
    - The overall qualitative analysis in the paper is also quite limited

### Questions
Please refer to the questions (or issues) mentioned in the Weaknesses section.

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
The paper introduces two key improvements to the VAE model architecture: the Multi-Scale Spatial-Temporal Downsampling method, which captures information across different temporal scales to address the existing flickering issue in VAEs, and the Latent-Guided Refinement Training approach, which explores the potential of interpolating within the VAE's latent space. The authors provide both quantitative and qualitative analyses of the proposed VAE's performance, demonstrating commendable results.

### Strengths
1. The usage of Multi-Scale Spatial-Temporal Downsampling is good, as it effectively captures content across different temporal scales. The accompanying ablation experiments convincingly demonstrate that this downsampling approach yields substantial improvements in the performance metrics.
2. This paper explores the potential of latent space for frame interpolation, providing a valuable perspective and reference for future research.
3. The study also investigates the degradation of current VAEs when video duration is extended, offering a noteworthy analysis angle.

### Weaknesses
The effectiveness of the refinement decoder is not sufficiently demonstrated, as it relies solely on the qualitative analysis presented in Figure 5. However, I have observed a color bleeding phenomenon in the interpolated images. While this is a good idea, I would appreciate more discussion on this aspect.

### Questions
1. Given that most current VAEs utilize tiling to reduce inference memory, I wonder if the Multi-Scale Spatial-Temporal downsampling method imposes any limitations within tiling. Can it still ensure satisfactory performance in such scenarios?
2. Have the authors attempted to use latent videos generated by diffusion models (e.g., Latte) as input to the refinement decoder? This approach may pose greater challenges compared to directly encoding videos and performing interpolation, but it could also provide stronger evidence for the significance of the proposed method.

### Soundness
3

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
4

### Summary
This paper explores how to design a better Video VAE for Video Latent Diffusion Models. Existing works either use image VAEs or video VAEs with simple single-scale convolution kernels, which fail to effectively model temporal consistency, thus requiring additional video frame interpolation models. This paper employs a multi-scale temporal convolution architecture across the channel dimension, helping the VAE Encoder capture dynamic patterns across different time scales without introducing additional computational cost. Furthermore, the authors propose a latent-guided refinement training scheme that integrates the frame interpolation function into the decoder to generate high frame rate videos, thereby producing videos with better temporal consistency, eliminate the need of extra video interpolation models. The effectiveness of the proposed method is demonstrated through experiments on video reconstruction and generation.

### Strengths
1. Using multi-scale temporal convolution to replace single-scale convolution is a reasonable approach. The multi-scale convolutions are designed across the channel dimension without introducing additional computational cost.
2. Introducing the frame interpolation function into the VAE decoder through latent-guided refinement training to improve temporal consistency in video generation and reconstruction is a very interesting idea.
3. The authors demonstrate the superiority of the proposed UniVAE on public datasets for both video reconstruction and generation.

### Weaknesses
1. The writing of the paper left me somewhat confused. In lines 79-80, what does "Our observations indicate..." refer to? How did the authors come to the subsequent conclusion that "If the encoder can effectively model temporal variations, the decoder could theoretically synthesize frames, leading to high fps videos without the for separate interpolation models"? Specifically, it's unclear what experiments or analysis led to this observation. The connection between the observation and the conclusion is not explicitly stated, making it difficult to follow the authors' reasoning. It would be beneficial to have a more detailed explanation of the empirical basis for this claim, perhaps referencing specific results or figures in the paper.
2. The paper emphasizes that both the Encoder and Decoder in UniVAE are causal. What specifically does "causal" mean in this context? The paper does not provide a formal definition of causality in the context of video processing, and it is not clear how this causality is enforced in the architecture. What would be the results if either or both were non-causal? For example, would a non-causal encoder be able to capture temporal dependencies more effectively, or would it introduce artifacts? The implications of this design choice need to be more thoroughly discussed.
3. Could the latent-guided refinement training scheme proposed in this paper also be used to enhance the performance of other pre-trained VAE?

### Questions
Please refer to the Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper introduces a unified video VAE for video diffusion models. It’s motivated by recent video diffusion models often relying on image-based VAEs, which only handle spatial compression and miss out on temporal compression. To solve this, the authors employ 3D convolutions to their video VAE, so it can compress both spatial and temporal information. They also include an interpolation decoder to improve smoothness in video output. The training process has two steps: first, they train the basic VAE encoder and decoder, then freeze them and train the interpolation decoder separately. They use Latte as the video diffusion model to evaluate UniVAE.

### Strengths
a. Clarity and Simplicity: The idea presented is straightforward, and the method section is generally easy to understand.
b. The experiments are comprehensive and convincing. The results demonstrate that the proposed method surpasses existing image-based VAE.
c. UniVAE includes an interpolation decoder that enables the generation of higher FPS videos.

### Weaknesses
1. Limited Novelty in Video VAE Design: Many recent video generation models, like CogVideoX, already use video VAEs that compress both spatial and temporal information. Hence the proposed UniVAE combining spatial and temporal compression is not novel to the field.
2. Interpolation Decoder Training: The interpolation decoder is trained on its own after freezing the basic VAE encoder and decoder, making it more like an independent interpolation model. It would be more meaningful if the basic VAE encoder and decoder and the interpolation decoder are trained together to improve the representation ability of latent space.
3. Interpolation Quality: The interpolation results shown in Fig.5 are less convincing, with obvious issues like loss of hand details. This further highlights the limitation of training the interpolation decoder separately.
4. Comparison with existing interpolation models: The paper lacks the comparison of UniVAE’s interpolation results with other interpolation methods. Adding this would give a clearer view of UniVAE’s effectiveness in generating higher frame rates and would address the concerns about it.

### Questions
1. The main limitation of this paper is the lack of novelty. The authors should explain how their VAE is different from current methods and what makes it stand out.
2. The authors need to show the real impact of the interpolation decoder and compare it with recent interpolation methods.

### Soundness
3

### Presentation
4

### Contribution
2
