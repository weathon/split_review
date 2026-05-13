# DIFFNAT: IMPROVING DIFFUSION IMAGE QUALITY USING NATURAL IMAGE STATISTICS

- Decision: Reject
- Scores: 5, 5, 6, 6

## Abstract
Diffusion models have advanced generative AI significantly in terms of editing and creating naturalistic images.
\textcolor{blue}{However, efficiently improving generated image quality is still of paramount interest.}
In this context, we propose a generic ``naturalness'' preserving loss function, viz., kurtosis concentration (KC) loss, which can be readily applied to any standard diffusion model pipeline to elevate the image quality. 
Our motivation stems from the projected kurtosis concentration property of natural images, which states that natural images have nearly constant kurtosis values across different band-pass versions of the image. To retain the ``naturalness'' of the generated images, we enforce reducing the gap between the highest and lowest kurtosis values across the band-pass versions (e.g., Discrete Wavelet Transform (DWT)) of images. Note that our approach does not require any additional guidance like classifier or classifier-free guidance to improve the image quality. We validate the proposed approach for three diverse tasks, viz., (1) personalized few-shot finetuning using text guidance, (2) unconditional 
image generation, and (3) image super-resolution. Integrating the proposed KC loss has improved the perceptual quality across all these tasks in terms of both FID, MUSIQ score, and user evaluation.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes to improve quality and reduce artifacts in diffusion-based generative models. More specifically, they propose a kurtosis concentration loss to increase SNR and therefore improve results' quality. Their method can be applied a wide range of generative pipelines.

### Strengths
1. I think the mentioned problem of naturalness in generative process is important. And the idea to use natural image priors to improve quality is reasonable.

2. The paper writing is clear to follow.

### Weaknesses
1. My main concern is about effectiveness of this KC loss. In the experiment part, the authors gives FID and MUSIQ in Table 1, 2, which I think shows little improvements. And we all know that these metrics can not accurately measure image quality. 
Moreover, in Fig 6, Fig 8, Fig 9 and Fig 10, it is not obvious whether KC loss yields better results. I think the authors need to at lease hightlight the region or illustrate using zoom-out regions to show the difference.

2. Although I also appreciate very much those early works about natural image priors, I think most of them are based on simplistic assumptions which may not be needed in today's large-data-driven methods.
More specically, I doubt that why kurtosis-based losses suit for the mentioned artifacts problem? Actually, losses need to be designed based on properties that you want to distinguish. I think at least statistics of a large amount of artifact images are needed. to prove kurtosis is a proper metric.

3. In Fig 1, the authors show severe unnatural artifacts. However, I wonder is that really a common phenomenon? It is more like a bug in training process, and similar artifacts are not present in the other illustrations in the paper. Then what exactly are the types of artifacts that the authors want to solve?

4. In Equ 5, the authors claim that diffusion models are typically trained using reconstruction loss in image domain. However, as far as I known, many diffusion models do not use such reconstruction loss, for example DDPM, DDIM. 
Moreover, the loss and optimization of diffusion model typically follow mathematical derivations. I wonder if we incorporate KC loss, do the training process still theoretically sound?

### Questions
Please address the problems in weaknessed part.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a novel kurtosis concentration loss to preserve image "naturalness" to enhance image quality within standard diffusion model pipelines by reducing the kurtosis gap between band-pass image versions. The evaluation of the KC loss across diverse tasks show consistent improvements in perceptual quality via metrics like FID, MUSIQ score, and user evaluations.

### Strengths
1. The idea is interesting and novel. The idea of designing a quality measure to align the distribution of natural images and generated images from the diffusion models is novel.
2. The paper is clearly written. The reviewers can easily understand what the authors hope to convey.

### Weaknesses
1. The experiments are not extensive. More comparisons on the conditional image-to-image translation should be provided. The current evaluation lacks a thorough exploration of different conditional settings, such as varying noise levels or different types of conditioning inputs. A more rigorous evaluation should include a diverse set of image-to-image translation tasks, going beyond simple super-resolution or inpainting, to demonstrate the general applicability of the proposed loss.
2. Despite improvement in quantitative results, the visual differences in using the loss or not are minor. The reported quantitative gains do not translate to substantial perceptual improvements. The visual results presented are not compelling enough to showcase the effectiveness of the proposed loss function. It is difficult to discern any significant difference in image quality with or without the KC loss, which raises concerns about its practical impact.
3. This technical route, i.e. using IQA for improving generation quality, seems to be less effective than other alternative routes, e.g. [1]. The paper does not adequately address the limitations of using an image quality assessment metric to guide the training process. There are potentially more effective methods for improving diffusion model sample quality that directly manipulate the generative process, rather than relying on a post-hoc quality measure.
[1] Susung Hong, Gyuseong Lee, Wooseok Jang, Seungryong Kim, "Improving Sample Quality of Diffusion Models Using Self-Attention Guidance," ICCV, 2023.
4. The presented visual results are in small resolutions. Higher resolution results are suggested for putting into the paper. The low resolution of the provided visual results makes it difficult to assess the effectiveness of the proposed method, especially in terms of fine-grained details and textures. The method needs to be evaluated at higher resolutions to demonstrate its practical utility in real-world applications.

### Questions
1. Why are the FID values in the paper so high compared to those in other papers?
2. The PSNR results shown in Table 3 are also very low.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors utilize a generic naturalness, i.e. the kurtosis concentration (KC) loss, to improve diffusion model. The authors validate the proposed KC loss on three diffusion-based tasks, the experimental results show that introducing appropriate prior of natural image could lead to better generation model.

### Strengths
1) The authors validated the effectiveness of KC loss and show that appropriate prior of natural image is beneficial for diffusion model training.
2) The proposed KC loss is easy to optimize.
3) The authors validated the proposed loss on three widely studied tasks, the superiority experimental results validated the effectiveness of the proposed method.

### Weaknesses
1) The authors argue that they provided theoretical insights into the advantage of KC loss, however, the theorems only analyzed the correctness of KC loss but did not analyze why the KC loss is beneficial for diffusion model training. I think the authors over claimed their contribution. Specifically, while the theorems might show that minimizing KC loss leads to a certain mathematical outcome, they do not provide a clear link to why this outcome is particularly helpful in the context of the diffusion process. The analysis lacks a mechanistic explanation of how the kurtosis concentration property interacts with the denoising process inherent in diffusion models.
2) In the literature of natural image prior modeling, a large variaty of models have been suggested for modeling natural image prior. Besides KC loss, are there any other priors which is beneficial for training diffusion models. It is not clear if the choice of KC loss is optimal or if other priors could lead to similar or even better results. The paper would benefit from a broader discussion of alternative priors and a justification for why KC loss was chosen over other options.
3) The authors only analyzed the final generation quality with widely used image quality metrics, it will be the best if the authors could further present other properties of the proposed model, for example, can KC loss improve the convergence speed, will the additional KC loss leads to longer training time? The paper lacks a thorough analysis of the computational aspects of the proposed method. It is important to understand the trade-offs between image quality and computational cost, especially if the proposed method is to be adopted in practical applications.

### Questions
Please refer to the weakness part.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a “naturalness” preserving loss function that can improve generative image quality on diverse tasks including image super-resolution,  unconditional image generation, and personalized few-shot fine-tuning. The proposed loss function is called the kurtosis concentration (KC) loss, which encourages the kurtosis values across different DWT (Discrete Wavelet Transform) of the images to be constant.

### Strengths
1. The proposed method for improving image quality is simple but effective and can be applied in a plug-and-play manner. The theory of KC loss has a solid mathematical base and is persuasive.

2. The quantitative experiments are sufficient to show that KC loss can effectively improve image generative quality.

### Weaknesses
1. The visual results in Fig 6 do not show evident superiority of using KC loss. It is recommended to provide visual results with their corresponding KC statistic maps.

2. The computational complexity of KC loss is not discussed. It is recommended to report the additional time consumption caused by KC loss.

### Questions
Please see the Weaknesses.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
