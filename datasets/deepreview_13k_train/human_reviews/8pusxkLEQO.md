# ARLON: Boosting Diffusion Transformers with Autoregressive Models for Long Video Generation

- Decision: Accept
- Scores: 5, 6, 8, 6

## Abstract
Text-to-video (T2V) models have recently undergone rapid and substantial advancements. Nevertheless, due to limitations in data and computational resources, achieving efficient generation of long videos with rich motion dynamics remains a significant challenge. 
To generate high-quality, dynamic, and temporally consistent long videos, this paper presents ARLON,  a novel framework that boosts diffusion Transformers with autoregressive (\textbf{AR}) models for long (\textbf{LON}) video generation, by integrating the coarse spatial and long-range temporal information provided by the AR model to guide the DiT model effectively.
Specifically, ARLON incorporates several key innovations: 
1) A latent Vector Quantized Variational Autoencoder (VQ-VAE) compresses the input latent space of the DiT model into compact and highly quantized visual tokens, bridging the AR and DiT models and balancing the learning complexity and information density;
2) An adaptive norm-based semantic injection module integrates the coarse discrete visual units from the AR model into the DiT model, ensuring effective guidance during video generation; 
3) To enhance the tolerance capability of noise introduced from the AR inference, the DiT model is trained with coarser visual latent tokens incorporated with an uncertainty sampling module. 
Experimental results demonstrate that ARLON significantly outperforms the baseline OpenSora-V1.2 on eight out of eleven metrics selected from VBench, with notable improvements in dynamic degree and aesthetic quality, while delivering competitive results on the remaining three and simultaneously accelerating the generation process. In addition, ARLON achieves state-of-the-art performance in long video generation, outperforming other open-source models in this domain. 
Detailed analyses of the improvements in inference efficiency are presented, alongside a practical application that demonstrates the generation of long videos using progressive text prompts.
See demos of ARLON at \url{http://aka.ms/arlon}.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The manuscript introduces ARLON, a text-to-video framework that efficiently generates high-quality, dynamic, and temporally consistent long videos. By combining Autoregressive models with Diffusion Transformers, ARLON employs innovations like VQ-VAE for token compression, an adaptive semantic injection module, and an uncertainty sampling module to enhance efficiency and noise tolerance. It reduces denoising steps and outperforms OpenSora-V1.2 in both quality and speed, achieving state-of-the-art performance.

### Strengths
1. The integration of Autoregressive models with Diffusion Transformers and innovations like VQ-VAE for token compression, adaptive semantic injection, and uncertainty sampling show originality in addressing long video generation challenges.
2. The generated video spans 600 frames, making it relatively long.

### Weaknesses
1. In Table 2, why does StreamingT2V have a higher Dynamic Degree score (85.64) compared to ARLON (50.42)? This discrepancy needs further clarification, as a higher dynamic degree is generally associated with more complex motion and scene changes. The paper should provide a more detailed analysis of what contributes to this higher score in StreamingT2V, and how it relates to the qualitative aspects of the generated videos.

2. The paper lacks a detailed comparison of the number of parameters in ARLON versus baseline models. This is crucial for understanding the efficiency of the proposed method. A breakdown of parameters for each component (e.g., AR model, Diffusion Transformer, VAE) is necessary to assess the computational overhead of ARLON compared to OpenSora-V1.2 and other baselines.

3. There is no analysis of ARLON's memory footprint during training and inference, which would clarify its computational efficiency relative to models like OpenSora-V1.2. This includes not only the total memory consumption but also the memory usage for each component of the model. Furthermore, the paper should also report the inference time and FLOPs to provide a comprehensive comparison of computational efficiency.

### Questions
Please refer to the weakness part.

### Soundness
2

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
2

### Summary
This paper proposes a long video synthesis pipeline, ARLON. The main idea of this paper is to combine DiT with autoregressive transformers that provide long-range temporal information. To bridge the DiT and the AR transformer, the pipeline novelly adopts 1) a Latent VQ-VAE to enable the AR model to learn on and the DiT to learn on different latent spaces, reducing learning complexity and allowing the AR model to manage coarse temporal dependencies; 2) an adaptive norm-based semantic injection module to guide the DiT using AR generated tokens. Novel training strategies of coarser visual latent tokens for DiT and uncertainty sampling are also proposed to make the training process more stable and generalizable. 

Results are compared with current t2v models over VBench and Vbench-long and achieve notable improvements especially on long video generation.

### Strengths
- The motivation for using the AR model to provide semantic guidance is clear and nice.
- It is a very good extension of existing architectures.
- Good presentation.
- Good qualitative and quantitive results.

### Weaknesses
I overall like this paper, but there are several points for improvement.

- No ablation on the impact of model structure and training data size.
- No discussion on failure cases and limitations.
- There might be some missing references such as nuwa-XL and Phenaki. GAN-based long video generation might also be related.

*[1] NUWA-XL: Diffusion over Diffusion for eXtremely Long Video Generation*

*[2] Phenaki: Variable Length Video Generation from Open Domain Textual Descriptions*

I am not an expert in this field of training large video generation models. I will adjust the final score with other reviewers' comments and also based on the response from the author.

### Questions
- How many seconds can the models generate for the longest videos and how is the performance? For How many seconds do the longest videos that your method generates can last? In my understanding, this is the key advantage of the hierarchical generation framework.
- The main limitation of this work seems to be the huge computational cost of training, but the related information (type and number of GPU, training time) is not provided. It would be nice to know this information.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes to leverage autoregressive models to guide the training of diffusion transformers for text-to-video generation task. The proposed framework incorporate with a latent VQ-VAE, coarser visual latent tokens and a uncertainty sampling module to connect DiT and AR models and inject the information from AR models to DiT training. Massive experiments are conducted with abundant quantitative metrics and visualizations are reported to demonstrate the performance of the proposed model.

### Strengths
- The idea of make DiT and AR models working in one latent space is novel, and many technical improvements are designed to bridge their gap.

- The proposed method reaches a large reduction of denoising step of comparable generation quality.

### Weaknesses
 - It's better to use bold fonts and underscores in Table 1. According to the listed numbers, the proposed method doesn't reach top 3 in many columns. And the reproduced notation is missing.

 - In Fig. 1, two DiT models are employed, and the differences of their roles are not well addressed. Do the numbers of frames to their left indicate there is a temporal coarse-to-fine interpolation process? In Fig. 2 (and Sec. 2.2) there is only one DiT presented.

 - Fig. 1 needs to be overall improved. The arrows from the AR model to different DiT models should be distinguished by colors or texts indicating how they're different. The "reference" connection between the two DiT models is too concise and unclear as no other paragraphs mentions the same word.

 - Fig. 2 also needs to be overall improved. Currently each stage or module is not clearly separate in zones. For example, the latent VQ-VAE and AR model should be in a dedicated area or full row, and so as the outer 3D VAE (middle row) and the DiT models (bottom row). The latent adapter to the right is not clear where and how it is applied and shows too many details. The blurry video frames are a bit confusing: it is mentioned that coarser latent is used for more global information, but why the output of the outer 3D VAE is still blurry, and what is it calculated w.r.t. as the ground truth?

### Questions
- What is the motivation of using a latent VQ-VAE nested inside a pretrained 3D Autoencoder, instead of training a single-stage pixel-to-latent tokenizer? And what is the additional computational cost or gain in comparison?

- The proposed coarse latent token with different compression ratio, while how is this ablated in Table 3 or any other ablation studies? (Does the 4×8×8 row refers to both the same scale training and the 4×16×16 rows refer to different scale training?)

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
4

### Summary
This paper proposes a new text-to-video(T2V) framework consisting of autoregressive (AR) Transformers and Diffusion Transformers (DiT). Based on the input text prompt, the AR model predicts quantized visual tokens of a latent VQ-VAE nested within the 3D VAE of the DiT model. The coarse latent, reconstructed from the predicted tokens, serves as semantic condition to guide the DiT through adaptive normalization for video generation. To mitigate the effect of error introduced from AR inference, the authors introduce two noise-resilient strategies during DiT training, using coarser latent tokens and uncertainty sampling to make the semantic condition noisier.

### Strengths
1.This paper innovatively combines the strengths of autoregressive (AR) Transformers and Diffusion Transformers (DiT) for generating long video with rich dynamic motion.
2. To mitigate the effect of error introduced from AR inference to DiT, the authors introduce two noise-resilient strategies during DiT training.
3. The paper is written and presented clearly and easy to follow.
4. The long video results of the proposed method show improvement on dynamic degree, and long video generation results using progressive text prompts are more consistent throughout the entire video.

### Weaknesses
1. From Table 1, the proposed method lags behind compared methods in many metrics other than dynamic degree, such as Imaging Quality and Subject Consistency. In Table 2, the dynamic degree of proposed method (50.42) is significantly lower than that of the StreamingT2V(85.64).
2. From the demo videos on the webpage, there is some room for improvement for the proposed method compared to others. For example, the result of "A teddy bear is swimming in the ocean." lacks of subject consistency, and its motion is not realistic, which may be consistent with the quantitative results in Table 1 and Table 2.
3. Although the authors introduce noise-resilient strategies for the DiT model training to mitigate the error issue from AR inference, I am concerned that these strategies cannot truly simulate the error of AR inference, which may limit the model performance.

### Questions
1. In Figure1, the previously generated video seems to be used as a reference for the subsequent generation, but this is not illustrated in Figure 2. Does the DiT generate videos in an autoregressive way?
2. In Table 1 and Table 2, do the higher scores of metrics indicate better performance?
3. For long video generation in section 4.2 as well as the demo videos on the webpage, the authors only compare their proposed method with open-source text-to-long video generation models. Why not compare with the commercial closed-source text-to-video generation models like in Table 1?

### Soundness
3

### Presentation
3

### Contribution
3
