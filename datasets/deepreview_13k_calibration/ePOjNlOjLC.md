# Diffusion in Diffusion: Cyclic One-Way Diffusion for Text-Vision-Conditioned Generation

- Decision: Accept
- Avg Score: 6.25
- Scores: 8, 6, 6, 5

## Abstract
Originating from the diffusion phenomenon in physics that describes particle movement, the diffusion generative models inherit the characteristics of stochastic random walk in the data space along the denoising trajectory. However, the intrinsic mutual interference among image regions contradicts the need for practical downstream application scenarios where the preservation of low-level pixel information from given conditioning is desired (e.g., customization tasks like personalized generation and inpainting based on a user-provided single image). In this work, we investigate the \emph{diffusion (physics) in diffusion (machine learning)} properties and propose our \emph{Cyclic One-Way Diffusion (COW)} method to control the direction of diffusion phenomenon given a \emph{pre-trained frozen diffusion model} for versatile customization application scenarios, where the low-level pixel information from the conditioning needs to be preserved. Notably, unlike most current methods that incorporate additional conditions by fine-tuning the base text-to-image diffusion model or learning auxiliary networks, our method provides a novel perspective to understand the task needs and is applicable to a wider range of customization scenarios \textbf{in a learning-free manner}. 
Extensive experiment results show that our proposed \emph{COW} can achieve more flexible customization based on strict visual conditions in different application settings.  
Project page: \href{https://wangruoyu02.io/cow.io/}{\texttt{https://wangruoyu02.io/cow.io/}}

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This manuscript investigates the diffusion-in-diffusion processes
aiming to enable effective both pixel-level and semantic-level 
visual conditioning. A cyclic one-way diffusion
method is proposed. The cyclic method starts with an image and builds 
the entire scene according to the text information, given a pre-trained 
frozen diffusion model.

Extensive experiments are provided for various applications.
Experimental results, included human evaluation are provided.
The experiments and evaluations demonstrate that the proposed method 
can generate images with high fidelity to both semantic-text
and pixel-visual conditions.

### Strengths
- The manuscript proposes a diffusion-in-diffusion process which is able to enable effective both pixel-level and semantic-level visual conditioning.
- Extensive experiment results are provided for various applications.
-The results indicate that the proposed method can generate images with high fidelity to both semantic-text and pixel-visual conditions.

### Weaknesses
-


### Questions
What is the level of changes that may occur in the region on the seed image following the cyclic one-way diffusion?
According to the results presented some changes occur sometimes in the region of the seed image from the generated image, but not in 
other cases presented.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a training-free method to better preserve the visual conditions in diffusion-based text-vision-conditioned image generation.

### Strengths
1. The paper is well-written and easy to follow. The idea is clearly illustrated.

2. The proposed method is elegant and straightforward to preserve the visual condition.

### Weaknesses
1. The proposed method repeatedly replaces part of the diffusion latent variable x_t with the corresponding visual condition, which strongly maintains the visual condition in the generated image. However, this method may have an intrinsic drawback: the visual condition may be too strong and conflict with other conditions. in which case, the generated image may be unrealistic. Specifically, the method does not provide a mechanism to balance the influence of the visual condition against the text prompt, potentially leading to a generated image that adheres too rigidly to the visual input, even when it contradicts the desired textual content. This could manifest as a lack of diversity in the generated outputs, with images being overly constrained by the visual condition.

2. There are no quantitative analyses of the number of cycles, or positions of the start and end points. These experiments are important for us to understand the effectiveness of the proposed method. The lack of ablation studies on these parameters makes it difficult to assess the robustness and generalizability of the method. For instance, it is unclear how the performance varies with different cycle numbers or if there is an optimal range for the start and end points. Without such analysis, it is hard to determine the sensitivity of the method to these hyper-parameters and how to best tune them for different tasks.

3. According to Table 1, the proposed method is inferior to SD inpainting on both performance and efficiency. The only superiority of the proposed method is training free. However, since it needs cyclical diffusion & denoising, its inference cost is higher than SD inpainting. The superiority may be weakened. The higher inference cost, coupled with the lower performance compared to SD inpainting, raises questions about the practical utility of the proposed method. While being training-free is an advantage, the trade-off in terms of both quality and speed may limit its applicability.

### Questions
See the weakness above

------------------------

The authors' response addresses most of the concerns. And I would like to keep my positive rating.

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
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposed a ``diffusion in diffusion'' approach that leverages both physical diffusion and learning-based diffusion for the text-vision-conditioned generation, e.g., in painting, attribute editing and style transfer. The proposed method is based on inverse seed initialization and "disturb" and "construct" cycles for diffusion.  The proposed method is justified to be able to generate realistic image with higher ID-Distance and Face detection rates.

### Strengths
(1) The idea of diffusion in diffusion for diffusing image to generate consistent background content in the diffusion process is an interesting idea, and can be combined with the pre-trained diffusion model without retraining.

(2) The experiments on inpainting with visual condition, text-vision-conditioned generation showed that the proposed approach can produce realistic images.

### Weaknesses
The overall idea of this approach is interesting. I have some questions mainly on the experimental justifications as follows.

1. Most of these examples are based on putting an object in bounding box to a large image by adding backgrounds. This setting has applications, however, whether this approach can be applied to whole image generation/editing instead of pasting object on a larger image. The current experiments do not sufficiently demonstrate the method's capability for more general image manipulation tasks.

2. In the main body of this paper, the authors should present failure cases if it has, and analyze the reasons. Without a clear understanding of the limitations, the practical applicability of the method is difficult to assess.

3. The inner diffusion cycles for "disturb", "reconstruct" may introduce additional computational overhead. More details on the computational balance on the number of cycles and its effect on the results should be given. The paper lacks a detailed analysis of the trade-off between the number of inner diffusion cycles and the quality of the generated images, and how this impacts the overall efficiency of the approach.

4. There are typos in the paper, e.g., t around eq.(1). Please check the whole paper.

5. On page 4, the cycles are divided into three phases. Is there strict division boundary between these phases, and why these discussions are introduced to the main body of this paper, and how to support these conclusions on the existing of three phases.

### Questions
Please see above for my questions on the experiments and discussions.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This manuscript proposes a new method called Cyclic One-Way Diffusion that integrates diffusion in physics and diffusion in deep learning, providing a learning-free manner by controlling the direction of diffusion in various customization application scenarios.

### Strengths
1. The article proposed a novel method from a new perspective to utilize the capabilities of the diffusion model.
2. A learning-free manner can be widely used in personality customization with one or several conditions.
3. The experiment results show good performance.

### Weaknesses
1. The approach lacks a theoretical foundation, so it is not very intuitive to express why it can work.
2. The results of comparison methods are a bit too bad. More information about the setting should be given.
3. Sections 3.2 and 3.3 lack a theoretical foundation or pseudo-code to facilitate clearer understanding and reading.
4. It is not clear in Section 3.3, paragraph 4. What is the difference between two steps/two ends and t-th diffusion step, and how to use them?
5. The evaluation in Table 2 and in Section 4.2 is not matched.

### Questions
I have some questions for the author to further improve this work.
1. For the consideration of reproducibility, the code of the proposed method is suggested to be provided.
2. Are the comparison methods learning-free? If so, it would be beneficial to provide additional details about the experimental settings. Furthermore, for the comparison experiments, it might be advisable to incorporate some learning-free methods, such as LIVR [1], to ensure a comprehensive evaluation.
3. Sections 3.2 and 3.3 lack a theoretical foundation or pseudo-code to facilitate clearer understanding and reading.
4. It is not clear in Section 3.3, paragraph 4. What is the difference between two steps/two ends and t-th diffusion step, and how to use them?
5. The evaluation in Table 2 and in Section 4.2 is not matched.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
