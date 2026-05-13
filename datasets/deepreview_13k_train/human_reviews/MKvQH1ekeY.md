# Zigzag Diffusion Sampling: The Path to Success ls Zigzag

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Diffusion models, the most popular generative paradigm so far, can inject conditional information into the generation path to guide the latent towards desired directions. However, existing text-to-image diffusion models often fail to maintain high image quality and high prompt-image alignment for those challenging prompts. To mitigate this issue and enhance existing pretrained diffusion models, we mainly made three contributions in this paper. First, we theoretically and empirically demonstrate that the conditional guidance gap between the denoising and inversion processes captures prompt-related semantic information. Second, motivated by theoretical analysis, we derive Zigzag Diffusion Sampling (Z-Sampling), a novel sampling method that leverages the guidance gap to accumulate semantic information step-by-step throughout the entire generation process, leading to improved sampling results. Moreover, as a plug-and-play method, Z-Sampling can be generally applied to various diffusion models (e.g., accelerated ones and Transformer-based ones) with very limited coding costs. Third, extensive experiments demonstrate that Z-Sampling can generally and significantly enhance generation quality across various benchmark datasets, diffusion models, and performance evaluation metrics. Particularly, Z-Sampling is good at handling those challenging fine-grained prompts, such as style, position, counting, and multiple objects, due to its guidance-gap-based information gain. Moreover, Z-Sampling can even further enhance existing diffusion models combined with other orthogonal methods, including Diffusion-DPO.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces Z-Sampling, a novel sampling method for diffusion models that improves image generation quality and prompt alignment. The paper investigates that if the latent variable contains the sementic information, the sampling result would be enhanced. The key insight is that the guidance gap between denoising and inversion processes can capture semantic information. Rather than doing end-to-end semantic injection, Z-Sampling accumulates semantic information step-by-step through zigzag sampling. At each step, the denoising process is followed by inversion. The authors provide a theoretical analysis showing why this approach is more effective than end-to-end injection. The paper demonstrates empirical improvements across multiple diffusion models, datasets, and evaluation metrics. The method is particularly effective for challenging prompts involving style, position, counting, and multiple objects.

### Strengths
1. Interesting observation and reasonable method: The paper found that the latent variable contains semantic information, and the sampling result would be enhanced. The paper does the denoising and inversion process iteratively by using different semantic scales to add the semantic information in the latent variable. The method is intuitive and reasonable.

2. Strong Theoretical Foundation: The paper provides rigorous theoretical analysis explaining why Z-Sampling works, including detailed proofs showing how semantic information accumulation differs between end-to-end and zigzag approaches. 

3. Comprehensive Evaluation: The authors evaluate their method across multiple diffusion models, various datasets and different metrics. They also provide extensive ablation studies examining the impact of different parameters.

4. Practical Applicability: Z-sampling is a plug-and-play method that can enhance existing diffusion models without requiring model retraining. It can also be combined with other optimization techniques like Diffusion-DPO and AYS-Sampling for further improvements.

### Weaknesses
1. Large computation: Z-sampling requires additional computation due to the zigzag steps. While they show that it can achieve better results with fewer steps, the method still requires more computation than standard sampling for the same number of steps. The paper does not fully explore the trade-offs between the increased computational cost and the gains in image quality. It would be beneficial to see a more detailed analysis of the computational overhead, including a breakdown of the time spent on denoising versus inversion steps, and how this scales with image resolution and number of sampling steps.

2. Limited to Deterministic Samplers: The method's effectiveness is reduced when used with stochastic samplers due to inversion inaccuracies. This limitation restricts its applicability to deterministic sampling methods like DDIM. Besides, the inversion such as DDIM have approximate errors. The paper should investigate how it impacts the results of some experiments. The paper does not fully explore the impact of these approximation errors on the overall performance of Z-Sampling. A more detailed analysis of how these errors propagate through the zigzag sampling process, and their effect on the final image quality, would be valuable.

### Questions
1. Could you clarify how the semantic information gain term and approximation error term interact? While equation 10 separates these terms, it's unclear how they might counteract or reinforce each other in practice.
2. Can the method be extended to Video generation or 3D generation?

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
This paper identifies that the guidance gap between denoising and inversion captures prompt-specific semantic information and proposes Z-Sampling to gradually accumulate this information throughout the generation process, through iteratively denoising and reversing. Extensive experiments demonstrate that  Z-Sampling significantly improves image quality and prompt alignment, outperforming other baseline models.

### Strengths
1. The paper demonstrates strong problem identification and analysis, accurately pinpointing the reasons behind guidance failures with certain seeds in text-to-image diffusion models.

2. The presentation of the paper is clear and well-structured, making it easy to follow and understand the theoretical insights and proposed methods.

3. The experimental results are thorough, covering multiple baselines and benchmarks to robustly validate the effectiveness of the approach.

### Weaknesses
1. My major concern is that the qualitative results appear unsatisfactory. In almost all qualitative examples, Z-Sampling exhibits a pronounced **oversaturation** effect, with excessively vivid subject colors and significantly blurred backgrounds. While this approach may excel on certain benchmarks, these results are unlikely to be perceived as high-quality by users in practical evaluations.

2. Following from weakness 1, this oversaturated, unrealistic effect often occurs at very high CFG scales. As shown in Figure 3, Z-Sampling may essentially function as a high-CFG sampling method to enforce guidance. The paper does not provide a detailed comparison between Z-Sampling and high-CFG sampling, either theoretically or experimentally, and the results suggest that both approaches share similar drawbacks.

3. The paper lacks deeper theoretical analysis. The mathematical proofs provided rely on basic formula applications, but Z-Sampling alters the sampling path, creating a shift between the denoising trajectories of inference and training. In contrast, standard CFG sampling has rigorous theoretical backing. Revisiting the score function to analyze how training and inference could align under Z-Sampling conditions would strengthen the paper’s theoretical foundation.

4. Limited technical innovation. The proposed iterative inverse-and-denoise approach has already been used in various image editing applications, and also, in image to video methods like Tune-A-Video[1] to enhance structural coherence. The paper would benefit from further elaboration to clarify its unique technical contributions.

5. Lack of comprehensive analysis. CFG sampling incorporates not only semantic information but also an unconditional branch that helps with structural aspects. By attributing improvements solely to semantic response, the paper misses an analysis of structural and visual enhancements. A more detailed examination here could strengthen the paper’s argument and overall impact.

6. There are some typographical errors. For instance, in Algorithm 1, the steps for denoising and inversion are mistakenly reversed.

### Questions
1. In Tables 1 and 2 of the main results, what guidance scales were used for each model, and what was the specific setting for $\gamma_1$?
2. In Figure 10, how is the x-axis varied? My understanding is that the time taken for a model to generate a single image should be constant.

3. How might Z-Sampling be integrated into the training phase to achieve improved results? Currently, the oversaturation effect seems too pronounced.

4. $\gamma_2$ is set to 0 in most cases, suggesting that the reverse process disregards unconditional information entirely. Could a more detailed theoretical explanation be provided for this finding?

### Soundness
3

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
5

### Summary
The paper introduces a novel approach called Zigzag Diffusion Sampling (Z-Sampling) to enhance the performance of existing diffusion models, particularly for complex and fine-grained prompts in text-to-image generation tasks. This method employs a zigzag-like alternating denoising and inversion process, which progressively accumulates semantic information. Z-Sampling enables flexible control over the injection of semantic information, is applicable across various diffusion models, and requires minimal code modifications. Extensive validation on multiple benchmark datasets, diffusion models, and evaluation metrics demonstrates its effectiveness, especially in handling complex prompts such as style, position, counting, and multiple objects. As a training-free approach, Z-Sampling significantly improves baseline performance with lower computational cost, showing substantial practical value.

### Strengths
- Through zigzag sampling, semantic information in the latent space is progressively accumulated, effectively enhancing the alignment between generated content and prompts, especially for complex prompts.

- Z-Sampling is a plug-and-play method that can be seamlessly applied to different types of diffusion models with minimal code modifications.

- As a training-free sampling method, Z-Sampling reduces computational costs while maintaining high generation quality, with experiments demonstrating its performance superiority over standard sampling within the same time frame.

### Weaknesses
 - The authors’ insight—that the semantic information contained in the latent affects generation results—is quite evident.
- The method’s process is very simple and straightforward, which reminds me of time travel. The difference is that, in time travel, noise is added when tracing back, while zigzag uses inversion. The improvement in time travel comes from the inherent bias in the sampling process. By performing additional noise addition and denoising steps, the distribution can be pulled back onto the intermediate data manifold, thereby improving quality. Thus, to imbue $x_t$ with more semantic information of $c$, using inversion instead of time travel’s random noise to pull the data distribution back onto the intermediate data manifold $p_t(x_t|c)$ for enhancing conditional sampling quality seems like an obvious approach.

### Questions
- See Weakness
- In each zigzag optimization, only one step of denoising and one step of inversion is performed. Have you considered performing multiple steps of denoising and multiple steps of inversion?
- I am also curious about Figure 9. Theoretically, using the zigzag algorithm indeed quick and effective alignment, but as the number of optimization steps approaches infinity, the accumulated prediction errors should lead to a gradual downward trend. However, Figure 9 does not reflect this; it even shows an accelerating upward trend. How can this phenomenon be explained?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents a novel sampling method, Zigzag Diffusion Sampling (Z-Sampling), designed to enhance the generation quality of text-to-image diffusion models. The key contribution lies in leveraging the guidance gap between the denoising and inversion processes to accumulate semantic information throughout the generation process. This leads to improved image quality and prompt-image alignment, especially for challenging prompts. Z-Sampling is a plug-and-play method that can be easily integrated into various diffusion models. Extensive experiments demonstrate its superior performance across different datasets, models, and evaluation metrics.

### Strengths
- Clear and well-organized paper: The paper is well-structured, making it easy to follow the authors' arguments.
- Theoretical and empirical analysis: The authors provide a strong theoretical foundation for the guidance gap between the denoising and inversion processesand  their approach and support it with extensive empirical evidence.
-  Z-Sampling is a unique contribution to the field of diffusion models, offering a new way to improve generation quality.
- Plug-and-play nature: The method's simplicity and ease of integration make it attractive for researchers and practitioners.
- Strong experimental results: The authors demonstrate the effectiveness of Z-Sampling through comprehensive experiments.

### Weaknesses
 - Comparison to other training-free enhancement techniques: While the paper mentions other training-free enhancement techniques, a more in-depth comparison with methods like SAG[1], SEG[2], and CFG++[3] would strengthen the paper. This would provide a clearer understanding of Z-Sampling's unique advantages. Specifically, a detailed analysis of the computational overhead, memory requirements, and the impact on inference speed compared to these methods is needed. Furthermore, the paper should explore the sensitivity of Z-Sampling to hyperparameter settings and how these compare to the cited methods.
- Comparision to "Text-to-Image Rectified Flow as Plug-and-Play Priors"[4]: The proposed method has similarity with this paper in terms of utilizing the forwad and reverse process to enhance the quality. The paper should provide a more detailed comparison of the theoretical underpinnings of Z-Sampling and the rectified flow approach, highlighting the differences in their mathematical formulations and the specific assumptions they make about the underlying data distribution. A discussion of the practical implications of these differences, such as the ease of implementation and the potential for generalization to different types of diffusion models, is also necessary.

### Questions
- Would you compare Z-sampling with other training-free enhancement techniques?
- Would you compare Z-sampling with "Text-to-Image Rectified Flow as Plug-and-Play Priors"?

### Soundness
3

### Presentation
3

### Contribution
3
