# X-NeMo: Expressive Neural Motion Reenactment via Disentangled Latent Attention

- Decision: Accept
- Scores: 8, 8, 3, 6

## Abstract
We propose X-NeMo, a novel zero-shot diffusion-based portrait animation pipeline that animates a static portrait using facial movements from a driving video of a different individual. Our work first identifies the root causes of the limitations in prior approaches, such as identity leakage and difficulty in capturing subtle and extreme expressions. To address these challenges, we introduce a fully end-to-end training framework that distills a 1D identity-agnostic latent motion descriptor from driving image, effectively controlling motion through cross-attention during image generation. Our implicit motion descriptor captures expressive facial motion in fine detail, learned end-to-end from a diverse video dataset without reliance on any pre-trained motion detectors.  We further disentangle motion latents from identity cues with enhanced expressiveness by supervising their learning with a dual GAN decoder, alongside spatial and color augmentations. By embedding the driving motion into a 1D latent vector and controlling motion via cross-attention instead of additive spatial guidance, our design effectively eliminates the transmission of spatial-aligned structural clues from the driving condition to the diffusion backbone, substantially mitigating identity leakage. Extensive experiments demonstrate that X-NeMo surpasses state-of-the-art baselines, producing highly expressive animations with superior identity resemblance. Our code and models will be available for research.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a novel portrait animation framework that extracts identity-free motion through a specially designed module and injects the motion using cross-attention, while utilizing GAN to enhance the accuracy of motion capturing. Extensive experiments demonstrate the effectiveness of this approach.

### Strengths
1.This paper is well written, easy to follow.
2.This paper proposes a new portrait animation pipeline that effectively addresses the longstanding issues of identity entanglement and loss of motion expressiveness.
3.Extensive experiments demonstrate the effectiveness of this method.
4.Great work! The motivation and experimental results for each component are solid. The demo in the supplementary materials also looks very impressive; (if it isn’t cherry-picked)

### Weaknesses
1.Since the motion model is trained, could it struggle to adapt to out-of-distribution (OOD) motions, could you provide extreme or unusual facial expressions to demonstrate robustness?
2.In the results provided in the paper and the demo, the facial features of the driving and reference are quite similar. Could you provide more examples where facial features (such as eyes, mouth, nose, etc.) or face position or head pose are inconsistent?
3.As stated in W2, I also cannot tell if this paper truly addresses the issue of identity leakage, as it appears that most of the features in the driving and reference images are quite similar, could you provide more convincing prof or experiments?

### Questions
1.For non-human data, existing methods find it challenging to crop the face. If you were to apply these methods to such data, what kind of solution would you propose?
2.Could you simply train a model with added OOD data to provide results for non-human cases?

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
5

### Summary
This work presents a portrait animation method that diverges from traditional landmark-based approaches. It leverages a latent motion descriptor enhanced by a low-pass filter and incorporates motion priors through cross-attention, eliminating the reliance on aligned pose information. To develop a robust and fine-grained motion descriptor, the method includes a GAN head and employs techniques such as data augmentation and masked modeling.

### Strengths
1. This work proposes a feasible solution to address the limitations of previous portrait animation methods that rely on explicit motion descriptors or the integration of motion information through PoseGuider and ControlNet.
2. This study demonstrates strong visual performance across various samples, showcasing its robust capabilities in motion transfer and stability.
3. This work includes comprehensive comparisons with prior methods and an ablation study to validate the proposed techniques.

### Weaknesses
1. A temporal evaluation of spatially aligned motion injection versus attention-based motion injection is recommended. Intuitively, spatially aligned motion injection is expected to provide better temporal consistency due to its stronger spatial priors. However, the current evaluation lacks a direct comparison of these two injection methods, particularly regarding their impact on temporal stability. The analysis should include a quantitative assessment of temporal coherence, beyond just visual inspection, to support claims about the superiority of the attention-based approach. Specifically, metrics that capture frame-to-frame consistency and the absence of flickering artifacts are needed.
2. Additional analysis and experiments are needed to clarify why X-NeMo achieves such high levels of temporal consistency. Other methods, such as LivePortrait and X-Portrait, also include a stage for training temporal modules, yet they still exhibit some flickering in their results. The paper mentions only temporal modules and prompt traveling as means to achieve temporal consistency, but I remain unclear about the source of X-NeMo's superior performance in this regard. The current explanation lacks a detailed breakdown of the specific mechanisms that contribute to the improved temporal stability, such as the motion descriptor's smoothness or the attention mechanism's role in maintaining temporal coherence. It is also unclear how the training process specifically encourages temporal consistency, beyond the general end-to-end training framework.

### Questions
1. In the quantitative comparisons, do the results for AniPortrait and X-Portrait come from the officially released weights or from weights that were retrained on your training dataset? If the latter, why do the results for both methods perform poorly in cases involving tongue motion, considering that the NerSemble dataset should include training samples with tongue motion? This is particularly concerning for X-Portrait, which is also a non-landmark method.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
The paper proposes X-NeMo, a diffusion-based portrait animation framework. It tries to address identity leakage and capturing diverse expressions. The method involves extracting a 1D identity-agnostic latent motion descriptor from the driving image, using cross-attention for motion control in image generation. It is trained end-to-end with a dual GAN decoder and spatial/color augmentations.

### Strengths
+ The paper is well-structured.
+ The problem of portrait animation with high expressiveness and identity preservation is important.
+ The use of a 1D latent motion descriptor and cross-attention for motion control is reasonable.

### Weaknesses
 - What is the definition of zero-shot here? Firstly the model is trained. Secondly in the inference several reference images are provided. Thirdly the description of zero-shot is missing.
- The method has three training stages. What does it mean by end-to-end learning as described in several places in the paper? It seems each components are trained separately.
- The approach to get identity-agnostic feature is only to augment the images with color jitter, scaling and affine transformation. Such augmentations do not remove the identity information but only change the basic appearance of the facial images. The reviewer also believes such simple augmentations are not innovative.
- The app encode in Fig 2 seems to be not described.
- While the method shows plausible performance on the tested datasets, the generated video seem not to be tested with widely-used metrics like FVD.

### Questions
Please see the weakness.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces X-NeMo, a novel zero-shot, diffusion-based portrait animation framework that animates static portraits using head movements and facial expressions from a driving video of another subject. The authors identify key challenges in existing approaches, such as identity leakage and difficulty in capturing subtle and extreme facial expressions. To overcome these issues, X-NeMo employs a fully end-to-end training process that extracts a 1D identity-agnostic motion descriptor from the driving image, controlling the motion in the generated animation through cross-attention rather than traditional spatial guidance. This technique mitigates the transmission of identity clues from the driving video, reducing identity leakage and improving expressiveness. X-NeMo learns facial motion from diverse video datasets without relying on pre-trained motion detectors, using a dual GAN-based decoder and various augmentations to disentangle motion from identity cues. By embedding motion in a 1D latent vector and leveraging cross-attention, the model avoids transferring spatial structures, thereby preserving identity resemblance in the animated portraits. Experiments demonstrate that X-NeMo surpasses state-of-the-art methods, producing highly expressive animations while maintaining the subject’s identity.

### Strengths
1.	The design of the implicit 1D latent motion descriptor and its integration through cross-attention offers a perspective on addressing identity leakage and expressiveness, overcoming the shortcomings of explicit motion descriptors.
2.	X-NeMO better captures subtle and extreme expressions in the process of portrait animation compared to previous models.

### Weaknesses
1.	X-NeMo addresses the portrait animation task in the image level, and derive latent motion codes from each driving frame without the perception of the whole driving video. This setting neglect the video continuity, and may not capture the subtle coherence of expressions in a driving video.

### Questions
None

### Soundness
2

### Presentation
3

### Contribution
3
