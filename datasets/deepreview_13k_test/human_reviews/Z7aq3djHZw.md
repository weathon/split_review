# JPEG-LM: LLMs as Image Generators with Canonical Codec Representations

- Decision: Reject
- Scores: 8, 6, 6, 5

## Abstract
Recent work in image and video generation has been adopting the autoregressive LLM architecture due to its generality and potentially easy integration into multi-modal systems. The crux of applying autoregressive training in language generation to visual generation is discretization---representing continuous data like images and videos as discrete tokens. Common methods of discretizing images and videos include modeling raw pixel values, which are prohibitively lengthy, or vector quantization, which requires convoluted pre-hoc training. 
In this work, we propose to directly model images and videos as compressed files saved on computers via canonical codecs (e.g., JPEG, AVC/H.264). Using the default Llama architecture without any vision-specific modifications, we pretrain \imagemethodname~ from scratch to generate images (and \videomethodname~ to generate videos as a proof of concept), by directly outputting compressed file bytes in JPEG and AVC formats. Evaluation of image generation shows that this simple and straightforward approach is more effective than pixel-based modeling and sophisticated vector quantization baselines (on which our method yields a 31\% reduction in FID). Our analysis shows that \imagemethodname~ has an especial advantage over vector quantization models in generating long-tail visual elements. Overall, we show that using canonical codec representations can help lower the barriers between language generation and visual generation, facilitating future research on multi-modal language/image/video LLMs.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The article uses compression algorithms like JPEG to encode image data into discrete tokens, then leverages current large language models to learn from these encoded tokens. The advantage of this approach is that it avoids artifacts and distortions often introduced by some existing image tokenizers during reconstruction. I find this innovation compelling, yet I have significant concerns that make me cautious about these issues.

Firstly, JPEG has a limited compression ratio under visually lossless conditions. Meanwhile, DNN-based tokenizers are continuously improving, with better reconstruction quality and increasing compression ratios. Additionally, I didn’t find any convincing comparative experiments in the article, such as comparisons with works like Llamagen or VAR. I’ve given it a score of 6, but if you can address my concerns, I will revise my score.

### Strengths
1. This article is well-organized and easy to understand.

2. I trust the authors' experiments; they look very interesting and demonstrate that JPEG compression, along with other compression algorithms, can be applied to image compression, decompression, and image/video generation.

3. The article shows substantial innovation. I believe it’s a good paper.

### Weaknesses
1. This article lacks many necessary experiments, such as comparisons with VAR and Llamagen.

2. I have doubts about the scalability of this approach, as JPEG has a limited compression ratio. Even with a 4-10x compression ratio (where higher compression ratios often lead to low-quality generated content), it may still be insufficient to support long-duration video generation.

3. Generating high-quality images may require more time.

### Questions
1. Why wasn’t a comparison made with Llamagen and VAR?

2. Why wasn’t Llama 3 used?

3. The metrics seem unreasonable—why wasn’t there conditional image generation included?

### Soundness
3

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
5

### Summary
The paper introduces JPEG-LM and AVC-LM, two autoregressive language models that generate images and videos using standard codecs (JPEG for images and AVC/H.264 for videos) instead of specialized, vision-specific tokenization or pixel-based sequences. By directly modeling compressed byte sequences, these models avoid complex pre-processing or training processes typical of vector quantization (VQ) models. JPEG-LM, trained on JPEG image bytes, consistently outperforms VQ-based models in generating realistic visuals and demonstrates particular robustness in long-tail visual elements, such as small facial features and text characters.

### Strengths
1. Efficiency and Simplicity: JPEG-LM and AVC-LM bypass the need for complex tokenization and preprocessing by using JPEG and AVC codecs, which simplifies training compared to VQ-based methods.

2. Performance on Long-Tail Elements: The approach excels in generating visually complex, less frequent elements (like small text or detailed faces) where VQ models often degrade in quality.

3. Versatility in Modeling: Using a standard LLM architecture without vision-specific adjustments, JPEG-LM extends the utility of language models to image and video generation effectively, aligning with LLMs for text.

4. Robustness in Out-of-Distribution Scenarios: The codec-based approach is less sensitive to distributional shifts, potentially due to its reliance on stable, non-neural compression methods.

### Weaknesses
1. Limited Improvements Over Diffusion Models: While JPEG-LM shows promise, its performance does not match the leading results from diffusion-based models, especially in complex or higher-resolution tasks.

2. Dependency on JPEG Compression Constraints: Although effective, relying on JPEG and AVC formats may limit the granularity of generated details, especially in nuanced textures or high-frequency patterns.

3. Scalability for Video Generation: While AVC-LM is a compelling proof of concept, its application is limited to low frame rates and resolutions, indicating potential constraints in real-world, high-resolution video synthesis.

### Questions
1. How does JPEG-LM handle artifacts introduced by JPEG compression, and would incorporating a post-processing step improve image quality?

2. Could this codec-based approach extend effectively to other file formats, such as PNG for lossless compression or HEVC for higher-definition video?

3. Have you considered integrating JPEG-LM with diffusion techniques to leverage the best of both methods for higher fidelity in complex textures?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this paper, the authors propose a new auto-regressive model that directly generates compressed binary data in JPEG or AVC formats. As such canonical codec provides compressed discrete representation of data, it allows the model to simply follow the standard architecture of language models without any vision-specific modification. The experimental results show that the proposed model outperforms the baseline method that adopts VQ-VAE for tokenization, especially when less common contents appear in the image.

### Strengths
- The main research question is quite simple but really interesting: can LLM-like models directly generate compressed binary data in an efficient and effective manner? The experimental results shown in this paper provide a positive answer to this question, which would be worth reporting in the community.

- The design of the proposed model is also simple. It follows LLaMA-2 model architecture, and its vocabulary is basically a simple byte one slightly extended by byte-pair encoding to handle a few frequently appearing sequences in metadata and headers. This simplicity enhances reproducibility of the method and is suitable as a baseline for future studies.

- The experimental results show that the proposed model outperforms VQ Transformer using learning-based discrete representations obtained by VQ-VAE, which follows a popular design in recent studies. They would let us rethink how to effectively compress data for generative models.

### Weaknesses
- The JPEG images for training were compressed with a very low quality factor of 25 (compared with 70-90 in standard usage), which causes many artifacts, such as ringing and block noise, in the generated images as shown in Section 5 and appendix. I conjecture that this choice aims to substantially reduce the number of tokens processed by the proposed method. It would be beneficial if the authors could provide some justification on this setting.

### Questions
- Model architecture
  - Does "no 2D positional embedding" indicate that the proposed model simply adopts the standard rotary positional embedding from the default setting of LLaMA2?

- Experiments
  - Is there any possibility that the proposed model generate collapsed binary data (which is impossible to decode)? If yes, how did the author treat such data in the experiments?
  - Were the test images used for prompts and FID computation also encoded by JPEG with quality=25? The results of VQ and ImageGPT shown in Fig. 2 seem to contain some ringing artifacts and block noise, which should not occur without JPEG encoding. Could you clarify the reason for these artifacts?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper introduces JPEG-LM, a novel autoregressive model for image and video generation using canonical codecs as representations. The authors aim to simplify the task of visual generation by eliminating the need for vision-specific modifications or complex discretization processes such as vector quantization (VQ). Their key contribution is the use of JPEG and AVC codecs to transform continuous visual data into discrete tokens, significantly reducing sequence length while maintaining generation quality. The models, based on a Llama-2 architecture, achieve state-of-the-art performance in generating realistic images and videos, especially outperforming VQ-based approaches in handling long-tail visual elements. Experiments demonstrate that JPEG-LM can generate high-quality visual content with fewer complications and show robustness in generating fine details like human faces or text.

### Strengths
Overall I find that the writing is clear, concise, and well-structured, making it easy for readers to follow the arguments and understand the key points. I like the novel idea of using canonical codecs to transform continuous images and videos into discrete tokens without the need for training VQ-VAEs. This opens up a promising direction of unified multimodal modeling using a joint transformer decoder.

### Weaknesses
* The method section of this paper lacks more technical details or background knowledge of the proposed method, especially for readers without much knowledge of canonical codecs. (Although I know the core idea of this paper is quite straightforward.)
* The biggest problem is that this paper only shows the inpainting results of image generation and preliminary results of video generation. It lacks standard results on benchmarks like ImageNet and COCO (Text-to-Image) to fully demonstrate the potential of the proposed framework. The only inpainting results are restricted to the "auto-regressive" manner, which deviates from conventional inpainting with arbitrary shapes and makes the comparison with diffusion models unfair. The paper claims to remove all visual-specific design to achieve unified framework with language models, but conducts no multimode experiments such as text-to-image generation, even though it uses data from LAION-5B.
* There is a similar work [1], which uses the same idea to model molecules.

[1] Flam-Shepherd, Daniel, and Alán Aspuru-Guzik. "Language models can generate molecules, materials, and protein binding sites directly in three dimensions as xyz, cif, and pdb files." arXiv preprint arXiv:2305.05708 (2023).

### Questions
* I really like the idea of this paper, but concerned about the experiments. If the above concerns can be addressed, I am willing to raise my score.
* I am not familiar with JEPG representation. Can it keep the spatial shape of an image? The paper claims not to use 2d RoPE, then how can it generate images/videos with different shapes or lengths?

### Soundness
2

### Presentation
4

### Contribution
3
