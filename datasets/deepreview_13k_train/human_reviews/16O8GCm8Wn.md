# Robust Watermarking Using Generative Priors Against Image Editing: From Benchmarking to Advances

- Decision: Accept
- Scores: 6, 6, 6, 8, 6

## Abstract
Current image watermarking methods are vulnerable to advanced image editing techniques enabled by large-scale text-to-image models. These models can distort embedded watermarks during editing, posing significant challenges to copyright protection. In this work, we introduce~\textbf{W-Bench}, the first comprehensive benchmark designed to evaluate the robustness of watermarking methods against a wide range of image editing techniques, including image regeneration, global editing, local editing, and image-to-video generation. Through extensive evaluations of eleven representative watermarking methods against prevalent editing techniques, we demonstrate that most methods fail to detect watermarks after such edits. To address this limitation, we propose~\textbf{VINE}, a watermarking method that significantly enhances robustness against various image editing techniques while maintaining high image quality. Our approach involves two key innovations: (1)~we analyze the frequency characteristics of image editing and identify that blurring distortions exhibit similar frequency properties, which allows us to use them as surrogate attacks during training to bolster watermark robustness; (2)~we leverage a large-scale pretrained diffusion model SDXL-Turbo, adapting it for the watermarking task to achieve more imperceptible and robust watermark embedding. Experimental results show that our method achieves outstanding watermarking performance under various image editing techniques, outperforming existing methods in both image quality and robustness

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper presents VINE, a watermarking method designed to withstand various image editing techniques enabled by advanced generative models. It also introduces W-Bench, a benchmark that evaluates watermark robustness against multiple types of edits, making it a valuable resource for watermarking research.

### Strengths
- The paper is clearly written and organized, with effective figures explaining both W-Bench and VINE.

- The paper provides rigorous evaluations, testing VINE and eleven other watermarking models on diverse editing techniques.

### Weaknesses
 - EditGuard is primarily designed for editing detection, not robust watermarking, and it was not tested with its most robust configuration. This impacts the fairness of the evaluation, as EditGuard’s focus and strengths differ from VINE’s intended use.



### Questions
See weakness.

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
This paper introduces W-Bench, the first comprehensive benchmark designed to evaluate the robustness of watermarking methods against a wide range of image editing techniques, including image regeneration, global editing, local editing, and image-to-video generation. Authors reveal that image editing and blurring distortion predominantly remove watermarking patterns in high-frequency bands, while those in low-frequency bands remain less affected. Based on this, distortions are used as surrogate attacks to overcome the challenges of using T2I models during training and to enhance the robustness of the watermark. The authors approach the watermark encoder as a conditional generative model and introduce two techniques to adapt SDXL-Turbo, a pretrained one-step T2I model, for the watermarking task. Experimental results demonstrate that VINE is robust against multiple image editing methods while maintaining high image quality.

### Strengths
1.	The proposed method is easy yet effective. The combination of different losses is reasonable.
2.	The validation of watermarking patterns in high-frequency bands after image editing and blurring is solid.
3.	The experimental results show the proposed watermarking method is robust enough against multiple image editing methods.

### Weaknesses
1.	This paper lacks the validation of hypotheses in Line 249.
2.	The task of watermarking against Image Editing seems worthless.
3.	The watermarking pattern existing in high-frequency bands after image blurring is not a new discovery. However, the author spends too much text on it.

### Questions
1. Although the watermarking against Image Editing is interesting and novel, I cannot get the value of this task. Can you elaborate the perspective of this task?
2. The author hypothesizes that a powerful generative prior can facilitate embedding information more invisibly while enhancing robustness (Line 249). Why hypothesize that? What are the assumptions based on?
3. What is the purpose of finetuning VINE-B to VINE-R using Instruct-Pix2Pix? (Line 323)
4. Why is the resolution not unified? (Line 1042) 
5. Is VINE only work on the Image Editing task? What about other common watermarking tasks?

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
This paper introduces a new evaluation benchmark, W-Bench, designed to test the robustness of image watermarking methods under image editing supported by large-scale generative models. W-Bench includes image regeneration, global editing, local editing, and image-to-video generation. The authors also propose VINE, a watermarking method utilizing generative priors to enhance the robustness and visual quality of watermark embedding. Experiments show that VINE outperforms existing watermarking methods across various image editing techniques.

### Strengths
1. Comprehensive Evaluation Framework: W-Bench covers a variety of image editing techniques, providing a comprehensive platform for assessing the robustness of watermarking methods.

2. Innovative Use of Generative Priors: VINE embeds watermarks by adapting pretrained large-scale generative models, making the embedding more imperceptible and robust.

3. This task is innovative, focusing on watermarking that is robust against image editing methods.

### Weaknesses
TreeRing, Gaussian Shading, and RingID, which add watermarks in the frequency domain of the initial noise, are generally considered robust against image editing (e.g., prompt2prompt) and regeneration. This paper lacks this crucial comparison. If these methods are also robust to image editing, the contribution of this paper may be diminished.

Specifically, the paper does not address the robustness of frequency-domain watermarking techniques against the specific types of image manipulations included in W-Bench. It is unclear whether the proposed VINE method offers a significant advantage over these existing methods, especially considering that frequency-based methods are often designed to be resilient to common image transformations. A more detailed analysis comparing VINE's performance against these methods under the W-Bench conditions is needed to fully assess its contribution.

### Questions
1. I have doubts about the results in Figure 5(a). The experimental results show that 250-step noise in image regeneration can significantly disrupt the watermark（bit acc). Does this mean that global image editing (e.g., SDedit, prompt2prompt) with 250 steps can also completely remove the watermark? If so, I believe this result does not demonstrate robustness, as global image editing often uses even more denoising steps.

### Soundness
2

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
This paper introduces an image watermarking benchmark, specifically aiming to evaluate the watermark robustness against four image editing methods. In addition, an image watermarking that is robust against image editing is proposed.

### Strengths
1. This paper focuses on the image watermark robustness against image editing, which is important but has rarely been explored.
2. The proposed benchmark includes different types of image editing approaches, rendering it comprehensive to some extent.
3. The proposed SDXL-Turbo-based robust image watermarking method is novel, and the experiments demonstrate its effectiveness.
4. The paper is overall well-written.

### Weaknesses
1. The benchmark only considers four types of image editing methods (image regeneration, global editing, local editing, and image-to-video generation). Other image editing methods such as style transfer, which can significantly alter image statistics and potentially disrupt watermarks, are not considered. Furthermore, the global editing category is broad and could benefit from more granular evaluation, such as separating color adjustments, geometric transformations, and texture modifications.
2. Only one image-to-video generation method is included in the benchmark. The robustness against other image-to-video generation methods such as [1] is not evaluated. This is a significant limitation, as different video generation models may employ distinct architectures and training strategies, leading to varying degrees of watermark robustness.

### Questions
1. What is the reason for choosing only these four types of image editing methods (image regeneration, global editing, local editing, and image-to-video generation) to evaluate the image watermarking robustness, against image editing?  
2. What is the motivation for using SDXL-Turbo as the generative prior for watermark encoding? If it is just to avoid multi-step sampling, there should be lots of one-step generative models to choose from, for example, the SDXS [2]. 

[2] Song, Yuda, Zehao Sun, and Xuanwu Yin. "SDXS: Real-Time One-Step Latent Diffusion Models with Image Conditions." arXiv preprint arXiv:2403.16627 (2024).

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
4

### Summary
The paper evaluates eleven watermarking methods against prevalent image editing techniques and demonstrates that most methods fail to detect watermarks after such edits. It also introduces a watermarking model based on SDXL-Turbo, which exhibits high robustness against these editing methods while maintaining high image quality.

### Strengths
The paper presents the first holistic benchmark that incorporates four types of image editing techniques to assess the robustness of watermarking methods. This is significant for evaluating the robustness of future watermarking methods, as it helps to promote the standardization and comprehensiveness of robustness assessments. By addressing a critical gap in evaluating watermark resilience against sophisticated transformations enabled by modern generative models, this work encourages researchers in the field of image watermarking to focus on the robustness of their methods against emerging image editing technologies, including image regeneration, global editing, local editing, and image-to-video generation. Overall, the paper is clearly articulated and well-supported.

### Weaknesses
1. The paper explains the reasons behind the watermarking algorithm's resistance to image editing from the perspective of the frequency domain. It notes that the watermarking methods exhibiting high robustness against image editing in certain scenarios display prominent patterns in the low-frequency bands, which aligns with the general understanding of watermark robustness. However, the paper primarily focuses on the robustness of watermarking methods against image editing techniques based on generative models. Therefore, summarizing the unique effects of such image editing techniques on the watermark is more meaningful.
2. We observe that the proposed watermarking method, VINE, shows higher brightness in the central region of the frequency domain, which corresponds to the author's analysis of watermark robustness. However, the paper does not clarify why this watermarking model based on SDXL-Turbo exhibits such characteristics, leading to the author's specific design of the watermark algorithm. In other words, there seems to be a disconnect between the author's analysis of watermark robustness and the design of the watermark model.

### Questions
1.Figure 6 in the appendix shows that VINE exhibits higher brightness in the central region, providing evidence for why the proposed watermarking method demonstrates strong robustness against image editing. If the author can thoroughly elucidate the principles underlying this phenomenon, it may address the previously mentioned issue of "a disconnect between the author's analysis of watermark robustness and the design of the watermark model."

2.The experimental results demonstrate that the proposed watermarking method, VINE, significantly enhances robustness against various image editing techniques. Has the author considered using representative image editing as an attack template, incorporating the associated attack loss as one of the objective functions during the training phase? Alternatively, how might integrating the specific effects of image editing on watermarks into the design of the watermarking model influence the results of the watermarking algorithm?

3. In the experimental section, some of the differences between the subjective experimental results are difficult to discern visually. The author could consider selecting a subset of images and enlarging specific regions to facilitate reader comprehension.

### Soundness
2

### Presentation
3

### Contribution
2
