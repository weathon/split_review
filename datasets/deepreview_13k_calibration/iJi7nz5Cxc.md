# Diffusion-NPO: Negative Preference Optimization for Better Preference Aligned Generation of Diffusion Models

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 6, 8, 6

## Abstract
Diffusion models have made substantial advances in image generation, yet models trained on large, unfiltered datasets often yield outputs misaligned with human preferences. Numerous methods have already been proposed to fine-tune pre-trained diffusion models, achieving notable improvements in aligning generated outputs with human preferences. However, we point out that existing preference alignment methods neglect the critical role of handling unconditional/negative-conditional  outputs, leading to a diminished capacity to avoid generating undesirable outcomes. This oversight limits the efficacy of classifier-free guidance (CFG), which relies on the contrast between conditional generation and unconditional/negative-conditional generation to optimize output quality. In response, we propose a straightforward but consistently effective approach that involves training a model specifically attuned to negative preferences. This method does not require new training strategies or datasets but rather involves minor modifications to existing techniques. Our approach integrates seamlessly with models such as SD15, SDXL, video diffusion models and models that have undergone preference optimization, consistently enhancing their ability to produce more human preferences aligned outputs.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents a simple and general method for aligning images generated from diffusion models with human preference. The key idea is to distinguish not only favorable images but also undesired ones. To accomplish this, the paper builds on various existing preference optimization approaches and propose negative preference optimization (NPO), which in essence reverses the order of the ranked image pairs for training a second set of diffusion weights that emphasize negative images. The experiments demonstrate strong qualitative results and favorable user study results in comparison to baselines without NPO.

### Strengths
- Simplicity and generality. The method is simple, intuitive, and can augment a variety of existing preference alignment approaches without additional training data and learning objectives.
- Strong results. The method achieves superior qualitative and quantitative results in comparison to baselines not using NPO.
- Efficiency. The method obtain stronger results without losing inference-time efficiency.

### Weaknesses
I did not find major weaknesses of the paper.

Disclaimer: While I find the approach interesting and reasonable, I am not an expert on preference optimization of diffusion models, so I am not able to comment on the novelty of the method and the selection of baselines / benchmarks.

### Questions
I am wondering whether it is optimal to share the same training data for PO and NPO. Humans prefer certain images for obvious reasons: higher visual quality and/or stronger semantic alignment with the text prompt. Oftentimes, the worse image in a training pair for PO still looks reasonable in quality and semantic alignment. The pool of negative images, however, can be larger and more diverse. For example, a negative image can be completely irrelevant to the text prompt, or can have arbitrary artifacts.

### Soundness
3

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
4

### Summary
This paper introduces Negative Preference Optimization (NPO), a novel approach for enhancing the preference alignment of diffusion models by explicitly training the model to recognize and avoid generating outputs that are misaligned with human preferences.The proposed NPO aims to improve diffusion model outputs by creating a separate model component trained to avoid generating undesirable features.  By training models to understand both positive and negative preferences, NPO enhances the effectiveness of classifier-free guidance, which relies on balancing conditional and negative-conditional outputs to improve output quality.The writers designed the NPO to integrate easily with existing diffusion models, such as SD1.5, SDXL, and various preference-optimized versions, improving image and video quality across these models without requiring significant modifications.The paper provides quantitative and qualitative evaluations across several metrics (HPSv2, ImageReward, PickScore, Laion-Aesthetic) and demonstrates that NPO consistently enhances image quality, color accuracy, structural coherence, and alignment with human aesthetic preferences. Overall, this work addresses a gap in preference optimization by focusing on both desirable and undesirable outputs, improving human-aligned generation across diverse applications in image and video synthesis.

### Strengths
This paper introduces a novel technique called Negative Preference Optimization (NPO) to improve the alignment of diffusion models with human preferences. Unlike traditional methods that focus solely on desirable features, NPO addresses the problem of undesirable outputs by training the model to recognize and avoid them. This innovative approach is both creative and practical, as it leverages existing preference data by simply reversing image pair rankings. The paper demonstrates that this simple technique can significantly improve the effectiveness of classifier-free guidance without requiring complex new datasets or training procedures.

The paper is well-executed, providing both theoretical insights and practical validation. It offers a clear and well-organized presentation, with a logical flow from problem statement to methodology and experimental results. The proposed method is grounded in a thoughtful analysis of classifier-free guidance, recognizing the critical role of conditional and negative-conditional outputs in achieving preference alignment. This theoretical foundation is reinforced by a comprehensive suite of quantitative evaluations (using metrics like HPSv2, ImageReward, and PickScore) and qualitative comparisons (sample images with and without NPO) that effectively demonstrate the improvements NPO brings to various diffusion models, including SD1.5, SDXL, and video diffusion models. The experiments are carefully structured to show the plug-and-play nature of NPO, further adding to the paper’s quality. Although some technical concepts may be challenging, the paper is structured to guide readers through them systematically.

The significance of this work is high, as it provides an effective, adaptable solution to a widely recognized issue in diffusion-based image and video generation: producing outputs that align well with human aesthetics and avoid undesired qualities. NPO addresses a core limitation in preference optimization approaches—specifically, the lack of attention to undesirable outputs—while remaining compatible with popular models and training frameworks. The paper’s contributions are likely to influence future work in human preference alignment, particularly in fields where aesthetic quality and user satisfaction are critical, such as digital art, content creation, and interactive AI. Furthermore, NPO’s plug-and-play compatibility makes it a practical choice for both researchers and developers aiming to improve generation quality without extensive re-training or model modification, boosting its applicability across the field.

Overall, the paper presents an original, well-supported, and clearly articulated contribution that addresses a key gap in diffusion model preference optimization, with practical implications for a broad range of image and video generation applications.

### Weaknesses
1. While the paper's introduction of Negative Preference Optimization (NPO) is innovative, the simple reversal of preference pair rankings may oversimplify the complexity of human aesthetics. Negative preferences are not always straightforward opposites of positive preferences, and undesirable features can be subtle or context-dependent. For example, a slightly blurred image might be less preferred than a sharp one, but simply sharpening the blurred image might not make it aesthetically pleasing; other factors like color balance or composition might also be at play. The method's reliance on a direct reversal of preference could lead to the model learning to avoid specific, easily identifiable negative features, rather than developing a more nuanced understanding of overall aesthetic quality.

2. Metrics-driven approach lacking user perspective. While quantitative metrics like HPSv2, ImageReward, and PickScore provide a measure of performance, they do not fully capture the subjective nature of human aesthetic preferences. These metrics, while useful, may not correlate perfectly with human perception of quality, and the paper lacks a comprehensive user study to validate the perceived improvements. The reliance on automated metrics could lead to a model that optimizes for scores rather than genuine aesthetic appeal.

3. The paper validates NPO primarily on general-purpose datasets and models like Stable Diffusion and DreamShaper. While these are commonly used in text-to-image generation, they may not represent the variety of domains where preference alignment is crucial, such as medical imaging, scientific visualization, or highly specialized art styles. The effectiveness of NPO in these specialized domains remains unclear, and the generalizability of the method to diverse applications is not fully established. For instance, in medical imaging, the definition of 'preference' might be related to diagnostic accuracy rather than aesthetic appeal, which is not addressed by the current evaluation.

4. The performance implications of NPO's dual weight system, especially for large-scale or real-time applications, are not fully explored. The paper does not provide a detailed analysis of the computational overhead introduced by NPO, particularly the additional memory and processing time required for maintaining and applying the negative preference weights. This lack of analysis makes it difficult to assess the practical feasibility of NPO for resource-constrained environments or real-time applications. The potential for increased latency or memory usage could limit the applicability of the method in certain scenarios.

5. the paper's focus on CFG-based models limits the exploration of NPO's compatibility with other diffusion architectures. NPO's compatibility with non-CFG diffusion models remains unclear. The method's reliance on classifier-free guidance (CFG) as a basis for negative preference optimization limits its applicability to other types of diffusion models that do not use CFG. This narrow focus restricts the potential impact of NPO and its generalizability across the broader landscape of diffusion models.

### Questions
1. How does NPO distinguish between truly negative attributes and those that are simply neutral or contextual?
2. What are the computational costs of NPO, especially in terms of memory and processing time for real-time applications?
3. How sensitive is NPO's performance to parameter settings, and what are the recommended heuristics for tuning them effectively?
4. How well does NPO perform on domain-specific datasets like medical imaging or abstract art?
5. Beyond quantitative metrics, what is the perceived quality improvement from NPO based on qualitative user evaluations?
6. How does NPO mitigate the risk of reinforcing biases present in preference datasets?
7. Have you discussed ethical guidelines and limitations on NPO's use to ensure responsible application?

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
This paper tackles the task of aligning diffusion-based generative models with human preferences. The authors propose training an additional model that aligns with the opposite of human preferences. At inference, this model serves as the unconditional or negative-conditional component in classifier-free guidance. The method is simple to implement—requiring only a reward inversion (by multiplying it by -1) for reward-based methods or reversing the order of preferred image pairs for DPO-based methods. Evaluations on various text-to-image and text-to-video models show both qualitative and quantitative improvements across the board.

### Strengths
- The main idea is very intuitive, simple to implement, and highly effective.
- The method is compared against several baseline alignment methods on multiple image and video diffusion models. The proposed algorithm is shown to be an improvement using various quality metrics and human user studies.
- The proposed technique is quite general, and can be used alongside any alignment algorithm.

### Weaknesses
The paper doesn’t introduce a new alignment technique; instead, it builds on existing alignment algorithms to train the negative-aligned model. This has both pros and cons: on the plus side, it can work alongside any alignment method, but on the downside, its quality is limited by the performance of the alignment algorithm used. Furthermore, while the method is presented as general, the experiments primarily focus on text-to-image and text-to-video tasks. It is unclear how well this approach would generalize to other modalities or tasks where the notion of 'negative preference' might be less straightforward to define or implement. For instance, in tasks like audio generation or 3D shape generation, defining a clear opposite of a preferred outcome could be challenging, potentially limiting the applicability of the proposed method.

### Questions
Recently, several works have improved text-to-image models by changing the unconditional or negative-conditional component in classifier-free guidance (CFG). The general idea is to use a “worse” version of the model for the second part of CFG. For example, Autoguidance[1] uses an earlier checkpoint in training, and SEG[2] manually corrupts some internal features in the model’s attention layers. Some of these methods don’t need extra training, so it would be interesting to compare them to Diffusion-NPO. While the paper already makes a similar comparison summarized in Figure 5, expanding on this could help show how much improvement comes from using negative preferences versus just a “worse” model.

[1] Karras, Tero, et al. "Guiding a Diffusion Model with a Bad Version of Itself." *arXiv preprint arXiv:2406.02507* (2024).

[2] Hong, Susung. "Smoothed Energy Guidance: Guiding Diffusion Models with Reduced Energy Curvature of Attention." *arXiv preprint arXiv:2408.00760* (2024).

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Many recent methods, such as diffusion DPO, fine-tune pretrained models using preference optimization. This paper highlights that while these methods focus on selecting preferred samples, they overlook the unconditional or negative outputs used in CFG. The paper addresses this by training a model using reverse DPO data for negative preference optimization, then incorporating this model into CFG to move outputs away from the negative values, resulting in improved image quality.

### Strengths
- The paper shows that using a model optimized with a preference for CFG's unconditional/negative term enhances performance.
- Qualitatively, the images generated with NPO show fewer artifacts and are sharper.
- This approach is simple to implement, as it only requires using the existing diffusion DPO method without additional data.

### Weaknesses
 - The paper seems underdeveloped in certain areas. For instance, Table 2 displays scores but lacks discussion in the main text, and Figure 8’s caption does not specify the methods compared.
- It does not clearly demonstrate the difference from scaling up the existing DPO method. The results might be similar to running DPO for a longer period. In the motivating example of Section 2, δ appears proportional to η. Subtracting the resulting model's output seems equivalent to scaling η in the DPO model’s unconditional parameter.

### Questions
- Could you compare the results of this method to those of more intensive DPO training (e.g., running DPO for a longer period)?
- If the original pretrained model is used instead of the NPO-trained model to obtain unconditional/negative outputs, is there a significant performance drop?

### Soundness
3

### Presentation
3

### Contribution
3
