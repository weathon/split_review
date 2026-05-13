# AdvPaint: Protecting Images from Inpainting Manipulation via Adversarial Attention Disruption

- Decision: Accept
- Scores: 6, 6, 6, 8

## Abstract
The outstanding capability of diffusion models in generating high-quality images poses significant threats when misused by adversaries. In particular, we assume malicious adversaries exploiting diffusion models for inpainting tasks, such as replacing a specific region with a celebrity. While existing methods for protecting images from manipulation in diffusion-based generative models have primarily focused on image-to-image and text-to-image tasks, the challenge of preventing unauthorized inpainting has been rarely addressed, often resulting in suboptimal protection performance. To mitigate inpainting abuses, we propose ADVPAINT, a novel defensive framework that generates adversarial perturbations that effectively disrupt the adversary’s inpainting tasks. ADVPAINT targets the self- and cross-attention blocks in a target diffusion inpainting model to distract semantic understanding and prompt interactions during image generation. ADVPAINT also employs a two-stage perturbation strategy, dividing the perturbation region based on an enlarged bounding box around the object, enhancing robustness across diverse masks of varying shapes and sizes. Our experimental results demonstrate that ADVPAINT’s perturbations are highly effective in disrupting the adversary’s inpainting tasks, outperforming existing methods; ADVPAINT attains over a 100-point increase in FID and substantial decreases in precision.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors propose AdvPaint, a method for crafting adversarial image to degrade the performance of Stable Diffusion inpainting model. The perturbation is crafted by maximizing the distance between the cross-attention queries, and self-attention qkv between the perturbed and clean image. These objectives are applied to both foreground and background masks.
Qualitative results show that AdvPaint effectively confuses the attention mask, leading to incorrect inpainting. And quantitative results show consistent improvement in FID and LPIPS scores over previous methods

### Strengths
- The writing is clear and easy to follow, with well-presented method and good coverage of literature review
- The protection effects are interesting: foreground inpainting produces a "nothing in the masked regions" effect, while background inpainting creates a "blind spot" effect, making generated regions repetitive and lacking harmony with the foreground object - This protection effects are novel compared to previous chaotic/noisy effects

### Weaknesses
 - A potential weakness is that the method was tested only on Stable Diffusion Inpainting; evaluating its performance against Diffusion Transformer architectures (e.g., SD3/Flux) would be interesting, given their different patchify and norm mechanisms. 
While crafting perturbations for these models may require significant modification, the authors could first show the result of perturbation crafted by SD Inpainting on these models to show its robustness.
- Another weakness is that the method appears effective only when the foreground inpainting prompt is a noun phrase, or when the background prompt includes a phrase where the noun represents the foreground object (that lead to the repetitive effect). Given that an attacker could easily modify the prompt, it would be interesting to test the method on a wide range of prompts (suggested in questions section)

### Questions
- What are the run time and memory requirements to run AdvInpaint?
- What is the condition prompt when crafting the perturbation?
- When testing, if I change the prompt to inpaint the foreground object, with the actual object itself (e.g in figure 5, if I change the prompt to `A person` instead of `A sunflower`), will the "nothing in the masked regions" effect still apply?
- Also, on the background prompt, the notable artifacts will happen when the editing prompt contains the object. I wonder if omitting the object from the inpainting prompt (e.g in figure 4, instead of "A monkey on a rocky slope", I just use the prompt "rocky slope") still affect the quality of the image. The problem is that the attacker can quickly adjust the prompt, so in this case, the noisy artifacts from previous method might be advantageous than AdvInpaint.

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
3

### Summary
This paper proposes a method of adding adversarial noise into images, aiming to prevent unauthorized use of datasets (inpainting tasks). Specifically, the method leverages SAM to divide  Images into two regions: foreground and background, then optimizes to disrupt the cross- and self-attention block.

### Strengths
1.	Considering the popularity of text-to-image models, the topic of preventing image abuse holds practical significance.

2.	Based on the experiments presented in the paper, the proposed method shows promising results.

### Weaknesses
1.  **The discussion with related work is insufficient.** Considering that there is a similar work [1] utilizing adversarial noise to disrupt attention layers, discussion about the technical difference between these methods is necessary. Specifically, the paper should clarify how its approach to perturbing attention layers differs from [1], particularly in terms of the specific layers targeted (cross-attention vs. self-attention) and the optimization strategies employed.

2.  The proposed method is complex, involving different processes like (1) generating prompts using ChatGPT, (2) using SAM for segmentation. However, **the evaluation experiments are not comprehensive** for these pre-progresses. Is it guaranteed that these preprocessing steps are 100% accurate? Do different methods of prompt generation and segmentation produce the same final results? The paper lacks a thorough analysis of how variations in prompt generation (e.g., using different models or prompt structures) and segmentation (e.g., using different segmentation algorithms or parameters) impact the effectiveness of the proposed adversarial noise. The evaluation should include a sensitivity analysis to demonstrate the robustness of the method to these variations.

3.  **The assumptions may not align with real-world scenarios.** It seems the authors assume that the object divided by SAM is the exactly target for inpainting. In multi-object images, is the inpainting target always the object that SAM segmented, or would users focus on different objects? The paper needs to address the scenario where users might target different objects or combinations of objects for inpainting, and how the proposed method would perform in such cases. The evaluation should include experiments where the inpainting target differs from the SAM-segmented object.

4.  **A minor concern**: Though numerous works (AdvDM, Mist, CAAT, SDST) were proposed to prevent unauthorized usage by adding adversarial noise, some works [2,3] point out that the noise generated by these methods can be easily disturbed and lose effectiveness. Given this, I believe that, compared to the protection effectiveness (e.g. FID rise and ACC decline), the resistance against these disturbing works [2,3] is more critical. Otherwise, these works may lack practical significance. The paper should include a more comprehensive evaluation of the robustness of the proposed method against purification techniques, such as those described in [2,3], and quantify the degree to which the adversarial noise is preserved after such processing. The evaluation should not only focus on the effectiveness of the protection but also on its resilience.

### Questions
See Weakness.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors propose ADVPAINT, a defensive framework that generates adversarial perturbations to mitigate inpainting abuses of diffusion models, such as replacing a specific region with a celebrity. ADVPAINT targets the self- and cross-attention blocks in a target diffusion inpainting model and employs a two-stage perturbation strategy which divides the perturbation region based on an enlarged bounding box around the object. Experimental results demonstrate that ADVPAINT’s perturbations can disrupt the adversary's inpainting tasks.

### Strengths
1. The inpainting abuse of diffusion models studied in this paper is an important problem.

2. The authors propose a method for disrupting inpainting tasks, while previous works mainly focused on image-to-image tasks or text-to-image tasks.

### Weaknesses
1. It's unclear whether ADVPAINT will be effective if some countermeasures against adversarial perturbations, such as Gaussian noise, JPEG compression and super-resolution, are applied to the perturbed images. 

2. Lack of important details in the experiments.

(1) ADVPAINT uses a set of masks to optimize perturbation, but the paper does not specify whether $m^{out}$ in Section 5.6 exceeds all masks to optimize.

(2) Section A.2.2 shows different performances when using different models to optimize perturbations. However, the model used to perform inpainting remains unknown.

(3) Image-to-image tasks and text-to-image tasks are not specified in the paper, so it's confusing how the experiments in Figure 7 and Figure 8 are conducted.

3. There is no comparison of ADVPAINT's performance when models to optimize perturbation and models to perform inpainting are different, which means that most experiments may be conducted as white-box attacks. It is impractical to mainly consider the white-box settings.

### Questions
1. Will ADVPAINT be effective if perturbed images are processed with Gaussian noise, JPEG compression or super-resolution before performing inpainting?

2. Does $m^{out}$ in Section 5.6 mean the generated segmentation masks used to perform inpainting exceed all masks used to optimize perturbation?

3. Does Section A.2.2 use the same model to perform inpainting as that to optimize perturbation?

4. Can the authors detail the experiments of Figure 7 and Figure 8?

5. Do the authors only use one version of the inpainting model in their main experiments?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper proposes a defense framework named ADVPAINT, designed to protect images from inpainting attacks based on diffusion models, specifically to prevent malicious actors from making unauthorized changes to specific regions of an image using such models. The method generates perturbations to disrupt the attention mechanisms of diffusion models (including self-attention and cross-attention blocks), thereby disturbing semantic understanding and the generation process. Additionally, ADVPAINT employs a two-stage perturbation strategy, applying different perturbations to the target region and the background, which enhances robustness under various masking conditions.

### Strengths
ADVPAINT employs a two-stage perturbation generation approach, dividing the image into target and background regions and applying different perturbations to each. This strategy enhances the method’s robustness across various mask shapes and sizes, enabling ADVPAINT to maintain a high level of protection against diverse attack methods.

### Weaknesses
1. ADVPAINT's approach of dividing the target region and background is fixed, resulting in limited flexibility when facing custom masks created by adversaries. In real-world scenarios, an attacker could select masking regions that do not overlap or only partially overlap with the predefined target mask, potentially weakening ADVPAINT's protective effect. I recommend that the authors conduct experiments to demonstrate ADVPAINT’s robustness under various custom mask configurations.

2. The paper does not explore the effect of varying noise levels and different PGD iteration steps on the robustness of the ADVPAINT model. The experiments use a fixed noise budget and iteration count, leaving it unclear how the model's performance might change under different adversarial intensities. I suggest the authors conduct experiments to analyze the robustness trend across various noise magnitudes and iteration counts to provide a more comprehensive evaluation of ADVPAINT's protective capabilities.

3. The paper lacks experiments on scalable diffusion models with Transformers. The evaluation focuses on standard Stable Diffusion models, leaving uncertainty about ADVPAINT’s effectiveness and adaptability on larger, Transformer-based diffusion architectures. I recommend that the authors test ADVPAINT on scalable Transformer-based diffusion models to better assess its robustness in more extensive generative frameworks.

### Questions
See weakness

### Soundness
4

### Presentation
4

### Contribution
3
