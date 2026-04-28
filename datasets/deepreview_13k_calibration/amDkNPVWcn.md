# Denoising Autoregressive Transformers for Scalable Text-to-Image Generation

- Decision: Accept
- Avg Score: 6.20
- Scores: 6, 8, 6, 6, 5

## Abstract
Diffusion models have become the dominant approach for visual generation. They are trained by denoising a Markovian process which gradually adds noise to the input. We argue that the Markovian property limits the model’s ability to fully utilize the generation trajectory, leading to inefficiencies during training and inference. In this paper, we propose DART, a transformer-based model that unifies autoregressive (AR) and diffusion within a non-Markovian framework.  DART iteratively denoises image patches spatially and spectrally using an AR model that has the same architecture as standard language models. DART does not rely on image quantization, which enables more effective image modeling while maintaining flexibility. Furthermore, DART seamlessly trains with both text and image data in a unified model. Our approach demonstrates competitive performance on class-conditioned and text-to-image generation tasks, offering a scalable, efficient alternative to traditional diffusion models. Through this unified framework, DART sets a new benchmark for scalable, high-quality image synthesis.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes DART, a new method to learn a distribution over images by autoregressively denoising a noise image to obtain high-quality generated images. They claim that DART leverages all the latents within the trajectory in oppose to existing methods that only use the previous latent. They compare their method with DiT and observe improvements in generated contents as evaluated by FID and CLIP Score.

### Strengths
The method is scalable and efficient as explained in the paper.

### Weaknesses
I think that the comparison to existing work is not comprehensive. Is DiT the only other model that this work should be compared with?

### Questions
I want the authors to clarify the comprehension of their evaluation. Also, I'd want to see how the autoregressive generation is the cause of improvements. Can authors run any experiments supporting the fact that autoregressive generation, where attention happens with all previous tokens, has a huge role?

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
The paper presents DART, al generative model combining diffusion and autoregressive (AR) frameworks for efficient and scalable image synthesis. DART addresses limitations in traditional diffusion models, particularly their Markovian process, which restricts generative efficiency by only leveraging information from the previous denoising step.

### Strengths
The idea is interesting, exploring if we can use AR to model the image diffusion and denoising processes to generate image.

1. The technique is well-supported by a theory. 

2. The results are good on border benchmarks. The T2I results seem promising.

### Weaknesses
My major concern is that the comparison is not comprehensive. DART integrates diffusion in the AR model, using the AR to model the diffusion. MAR [1] uses diffusion for the AR model, using the diffusion to model the tokenization. Even though their two different approaches, the comparison should include MAR, as MAR has already shown good generalization ability on multimodal generation [2]. It is becoming a trend. With this comparison, we can see if DART has this potential.



### Questions
1. In the inference stage, does the DART-FM also show the short-step sampling property? How to realize short-step sampling with DART-FM.

2. I still have no idea why DART-AR is better than DART. For me, the whole image processing mechanism should work better. Could the authors give me more detailed explanation?

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
The paper, introduces DART, a novel generative model that integrates autoregressive and diffusion approaches within a non-Markovian framework. Key contributions of the work include:
- DART Model: A non-Markovian diffusion model that uses autoregressive techniques to capture the full denoising trajectory, improving generation efficiency and flexibility.
- DART-AR and DART-FM Modules: DART-AR enables token-level autoregressive modeling for enhanced control and quality, while DART-FM employs flow-based refinement to increase model expressiveness.

### Strengths
1. The integration of autoregressive and non-Markovian diffusion in a unified framework is innovative, particularly by moving beyond the Markovian assumptions that traditionally constrain diffusion models. DART's AR and FM extensions add novel approaches for token-based and flow-matching refinement in image generation.
2. Experiments are carried out on low-resolution class-conditional and text-to-image generation as well as multimodal generation, demonstrating its effectiveness on different classes.

### Weaknesses
1. My biggest concern is the lack of comparison to SOTA approach, either in the form of diffusion models or auto-regressive models, for image generation tasks. The whole paper literally only shows comparison to the baseline DiT model which is published in 2022. There're a flourished set of literature for transformer-based image generation (SD-3[1], PixArt[2], etc.) and multimodal generation (Chameleon[3], Transfusion[4], etc.), yet none of these is compared in the paper. As such, it is really hard to understand the performance and actual benefits this approach brings us.  
2. The efficiency of the model is a big concern. As shown in Fig 7 and Fig. 9(a), although a finer grain modeling by DART-AR could bring a marginal improvement, it would introduce 100x more latency, making it hard to justify whether this efficiency-performance tradeoff is ideal. Scaling up a diffusion model that consume 100x more latency may have better performance. This comparison would be good to show in Fig 7.

### Questions
Please refer to the weakness section.

### Soundness
3

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
DART unifies autoregressive (AR) and diffusion models within a non-Markovian framework, addressing the limitations of traditional diffusion models' Markovian property.

### Strengths
1. DART has well-grounded theoretical framework connecting non-Markovian and Markovian processes.

2. It can handle multiple modalities. 

3. The experiments across different tasks are comprehensive.

### Weaknesses
1. While the technical contributions are solid, the paper's narrative structure prioritizes theoretical formulation over an intuitive explanation of the approach. The image is first transformed into several patches in the latent space through a Variational Autoencoder (VAE). The basic version of DART processes these patches simultaneously, predicting their denoised mean values, and then continues denoising in a manner similar to traditional diffusion models. The authors can include a more accessible explanation of how DART works in practice.

2. Even though, I think this paper's results are good, and show generalization ability, I am not sure whether this AR+diffusion method become new trend for future visual generation. Is is better than transfusion, show-o, and mar manner? (I recognize those should be concurrent work. This is just for curiosity, and I will not penalize the paper in terms of scoring).

### Questions
see Weaknesses.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents DART, a model that integrates autoregressive and diffusion methods within a non-Markovian framework for efficient, scalable text-to-image generation. DART uses autoregressive denoising to retain the full generation trajectory, improving image coherence and generation quality. Key features include DART-AR for token-level autoregressive modeling and DART-FM for flow-based refinement, both enhancing image fidelity and flexibility. DART beats standard DiT in class-conditioned and text-to-image tasks and adapts well to multimodal generation, providing a unified and scalable approach for high-quality visual synthesis.

### Strengths
Overall I find that the writing is clear and well-structured, making it easy for readers to follow the arguments and understand the key points. This paper starts by revisiting key design choices of diffusion models and naturally denoising autoregressive transformer, which is a relatively novel framework aiming to integrate the strength of both diffusion and autoregressive models. Besides, this paper provides plenty of experiments and demos in terms of class/text-conditional image generation.

### Weaknesses
* My main concern is that while the paper’s title is Denoising Autoregressive Transformers for **Scalable** Text-to-Image Generation, I am worried about whether the proposed method can truly scale to higher-resolution images. In Line 264, it mentions using  T = 16 , which results in around 4000 tokens for a 256x256 image. So, for resolutions like 512 or 1024, can it really be trained and sampled efficiently using this framework? Although VAR also adopts a similar progressive generation approach, it uses different resolutions in its generation trajectory, whereas DART’s generation trajectory consists of full-sized, noisy images. I would like to see the experiments on higher resolutions (512 and 1024).
* The paper presents many different models (DART, DART-AR, DART-FM, Kaleido-DART), without providing a sufficient explanation of these models, such as their strengths and weaknesses. After reading this paper, I do not know how to choose between them since there is no consistent winner in the provided experiments. I would like to see a table to clearly describe differences, strengths, and weaknesses of each DART variant.
* The paper only compares the DART family with the original DiT on the ImageNet benchmark. However, DiT is originated from a paper two years ago, and there are a bunch of related works with improvements in both diffusion/autoregressive transformers that should be discussed and compared, e.g., SiT [1], VAR [2], MAR [3], etc... It is better to provide comparisons with these sota models in terms of FID scores and inference efficiency.

### Questions
* Is the proposed DART compatible with existing techniques for diffusion models, e.g., DDIM, DPM-Solver, etc. I think it is a bit unfair to directly compare with original DiT with 16/256 steps without using any of these advanced samplers.

### Soundness
3

### Presentation
3

### Contribution
3
