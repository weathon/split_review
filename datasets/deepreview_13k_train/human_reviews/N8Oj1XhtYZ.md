# SANA: Efficient High-Resolution Text-to-Image Synthesis with Linear Diffusion Transformers

- Decision: Accept
- Scores: 10, 8, 8, 8

## Abstract
We introduce Sana, a text-to-image framework that can efficiently generate images up to 4096$\times$4096 resolution. Sana can synthesize high-resolution, high-quality images with strong text-image alignment at a remarkably fast speed, deployable on laptop GPU. Core designs include: (1) Deep compression autoencoder: unlike traditional AEs, which compress images only 8$\times$, we trained an AE that can compress images 32$\times$, effectively reducing the number of latent tokens. (2) Linear DiT: we replace all vanilla attention in DiT with linear attention, which is more efficient at high resolutions without sacrificing quality. (3) Decoder-only text encoder: we replaced T5 with modern decoder-only small LLM as the text encoder and designed complex human instruction with in-context learning to enhance the image-text alignment. (4)  Efficient training and sampling: we propose Flow-DPM-Solver to reduce sampling steps, with efficient caption labeling and selection to accelerate convergence. As a result, Sana-0.6B is very competitive with modern giant diffusion model (e.g. Flux-12B), being 20 times smaller and 100+ times faster in measured throughput. Moreover, Sana-0.6B can be deployed on a 16GB laptop GPU, taking less than 1 second to generate a 1024$\times$1024 resolution image. Sana enables content creation at low cost. Code and model will be publicly released upon publication.

## Human Reviews

## Human Reviewer 1

### Rating
10

### Rating Number
10

### Confidence
5

### Summary
The paper presents Sana, a cutting-edge text-to-image synthesis framework that can generate high-resolution images up to 4096×4096. Here are the key highlights:
Unlike conventional autoencoders that compress images by a factor of 8×, Sana's autoencoder achieves a remarkable 32× compression, drastically reducing the number of latent tokens.

Sana innovates by replacing the standard attention mechanisms in the Diffusion Transformer (DiT) with linear attention. This change enhances efficiency at high resolutions without sacrificing image quality.

Decoder-Only Text Encoder: Instead of relying on T5, Sana uses a modern, decoder-only small language model (LLM) as its text encoder. This model, combined with sophisticated human instructions and in-context learning, significantly improves text-image alignment.

Sana introduces Flow-DPM-Solver to cut down on the number of sampling steps and employs efficient caption labeling and selection techniques to speed up training convergence.

These advancements allow Sana to produce high-quality images at a significantly faster pace than existing models.

### Strengths
This work demonstrates its originality through several innovative contributions, including the Deep Compression Autoencoder, Linear DiT, and impressive 4K generation ability. These innovations enhance the quality and efficiency of high-resolution image generation while reducing computational requirements. The paper is well-written and clearly structured, with detailed experiments and results that validate the effectiveness of the proposed methods. Additionally, the significance of the work lies in its practical applications and the removal of limitations from prior models, making high-resolution image synthesis more accessible and scalable.
Overall, I find this work to be a breakthrough for diffusion text-to-image models.

### Weaknesses
1. The Gemma2-2B-IT model in Table 9 needs to be explained, as not all readers have a solid background in LLMs.

2. Further comparisons between Gemma2 and T5-XXL are needed, such as showing HPSv2 metrics on complex prompt benchmarks. The current FID scores in Table 9 are insufficient to highlight the true advantages of Gemma2.

3. Why does SANA perform significantly better than LUMINA-Next, even though both use the Gemma-2B model?

4. I believe some relevant works should be cited or compared, such as high-resolution generation work: UltraPixel: Advancing Ultra-High-Resolution Image Synthesis to New Peaks (NeurIPS 2024) and efficient generation work: Stable Cascade.

### Questions
1. The Gemma2-2B-IT model in Table 9 needs to be explained, as not all readers have a solid background in LLMs.

2. Further comparisons between Gemma2 and T5-XXL are needed, such as showing HPSv2 metrics on complex prompt benchmarks. The current FID scores in Table 9 are insufficient to highlight the true advantages of Gemma2.

3. Why does SANA perform significantly better than LUMINA-Next, even though both use the Gemma-2B model?

4. I believe some relevant works should be cited or compared, such as high-resolution generation work: UltraPixel: Advancing Ultra-High-Resolution Image Synthesis to New Peaks (NeurIPS 2024) and efficient generation work: Stable Cascade.

### Soundness
4

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
4

### Summary
The paper "SANA: Efficient High-Resolution Image Synthesis with Linear Diffusion Transformers" introduces SANA, a high-efficiency text-to-image generation framework capable of producing high-resolution images up to 4096×4096 pixels. SANA employs multiple innovations, including a deep compression autoencoder (compressing images 32× for latency reduction), linearized Diffusion Transformer (DiT) attention to improve high-resolution efficiency, and the use of a decoder-only LLM as a text encoder with "Complex Human Instruction" for enhanced image-text alignment. The model also implements a Flow-DPM-Solver to reduce sampling steps, achieving competitive quality at 100× faster speeds compared to state-of-the-art diffusion models. SANA's improvements are demonstrated on high-resolution benchmarks and support deployment on a laptop GPU.

### Strengths
1. Innovative Efficiency Strategies: SANA’s integration of linear attention, a high-compression autoencoder, and a unique sampling solver enables fast high-resolution generation, which holds practical value for many applications.
2. Effective Use of Large Language Model (LLM) for Text Encoding: SANA’s implementation of a decoder-only LLM with CHI to refine prompts improves text-to-image alignment, enhancing quality without incurring high latency.

### Weaknesses
Limited Ablation in Model Design: While SANA combines existing methods effectively, many techniques—such as linear attention, high-compression auto-encoders, and Flow-based solvers—are iterative upon recent advancements in diffusion transformers. Explicit comparisons with recent models like PixArt-Σ or Playground v3, which also incorporate high-efficiency strategies or decoder-only LLMs, with component by component comparisons would better attribute SANA’s unique contributions.

### Questions
1. SANA uses the Gemma-2 LLM with Complex Human Instruction (CHI) to improve text-image alignment. While similar works like Playground v3 uses Llama3-8B, this paper only compared T5 with Gemma, do we know if larger LLMs can further improve the generation quality?

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
4

### Summary
This paper proposes a text-to-image framework that can efficiently generate images up to 4096 x 4096 resolution. Comparing to existing works, the paper proposes four designs to facilitate fast speed, high quality text-to-image generation: (1) An auto encoder that down samples to input image by 32 times. (2) Replacing the quadratic self attention with linear attention. (3) Applies decoder-only LLM as text encoder. (4) Adopts efficient caption labelling and Flow-DPM-Solver for training and inference. Experimental results show that the proposed model achieves better or comparable results in terms of image quality, text image alignment comparing to existing methods, while having much higher throughput and lower latency

### Strengths
1. The paper is well motivated, as developing method that facilitates high quality, high resolution text-to-image generation in resource limited scenarios is of great application value.
2. The paper addresses the problem from several aspects, including auto encoder design, light weight self attention module, sampling method, and better caption labeling procedure. 
3. The experimental results on resolutions of 512 x 512, 1024 x 1024 show that the proposed indeed achieve better or comparable performance comparing to previous state of the art methods, while having much higher throughput and lower latency. 
4. The ablation experiments of different design components are sufficient and convincing.

### Weaknesses
1. The design of linear attention block needs to be explained in more detail. For example, the original self attention helps modelling long range dependency between tokens, here in the linear attention block, how is the dependency / contextual relation between tokens modeled through the new operations ?
2. The paper claims that the proposed method is able to generate images up to 4096 x 4096 resolution, however, in terms of quality comparison with existing methods, there are only ones with resolution of 512, 1024. For 4096 resolution, only the speed comparison is reported (Table 14), it would be more convincing to include FID and other image-text alignment metrics comparison for 4096 resolution as well.

### Questions
Please see weaknesses section

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
4

### Summary
The paper introduces Sana, a novel framework for efficient text-to-image generation, capable of producing 4K images while maintaining strong text-image alignment at remarkable speed. Sana’s core innovations include: a deep compression autoencoder, a Linear DiT architecture to enhance efficiency and a LLM-based text encoder. The model achieves competitive results compared to much larger models like Flux-12B, boasting significantly lower computational requirements.

### Strengths
1. Efficiency is a really big selling point. With a very high compression rate of deep autoencoder and linear DiT, SANA can generate high-quality images even on a laptop is very impressive. 

2. The fact that using a small but good LLM can outperform a big but bad text encoder is another interesting point. This boosts text-image alignment a lot when used with their proposed complex human instruction (CHI) pipeline.

3. They provide extensive ablation experiments on each components and measure their impact on efficiency and perform of the model, which is very helpful for future work to build upon.

### Weaknesses
1. Although the results are impressive, the contribution of this paper on the technical side is somewhat limited. Their three main components have been already explored in the literature, deep autoencoder in [1], linear DiT in [2] and using LLM as text encoder in [3, 4]. So combining them is not really a significant novel idea.

2. In section 2.3, the author do not fully explain their CHI pipeline, is it same as [5] or completely different. If it is similar then this even reduces the novelty of the work further.

### Questions
I do not have any further question

### Soundness
3

### Presentation
3

### Contribution
2
