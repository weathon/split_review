## Human Reviewer 1

### Summary
This paper explores the impact of modulation-based text conditioning on text-to-image diffusion models. The authors demonstrate that this technique is an important factor in increasing the quality of generated images. They introduce a simple, training-free method that improves performance across various diffusion models without imposing any additional computational burden at inference time.

### Strengths
- The paper is well-written, presenting its concepts and results with clarity.
- The proposed approach is easy to apply, computationally inexpensive, and demonstrably improves generation quality.
- The method is validated through a sound evaluation on state-of-the-art models, confirming its effectiveness.
- A significant advantage is the method's broad applicability, as it can be used even with models that do not rely on a CLIP text encoder.

### Weaknesses
- Based on the observation presented in Table 1 that adding CLIP embeddings can increase the quality of images generated from short prompts, it would be beneficial if the authors would also separate their evaluation based on the criteria of prompt length, to demonstrate that modulation can increase generation quality even with long prompts. A more detailed analysis would strengthen the method's reliability.
- The evaluation lacks a comparison to common, practical methods for quality enhancement. For example, many users simply add phrases like "good quality image" or "very detailed image" to their prompts or use negative guidance, which is a standard feature in many diffusion model interfaces.
- A potential trade-off between the enforced modulation and prompt fidelity is not explored. If the aesthetic qualities introduced by the modulation contradict the user's explicit request in a prompt, it could negatively impact prompt-following. An exploration of this dynamic would strengthen the submission.

### Questions
- The quality improvement shown in Figure 5 appears to stem largely from guiding the outputs to look more photographic, particularly with the introduction of blurred backgrounds. While this is often desirable, it raises a question about the trade-off between this aesthetic guidance and prompt fidelity. For example, if a user explicitly asks for a plain background, will the modulation override this request to produce a more "image-like" result with depth of field? Have the authors evaluated this trade-off?

### Soundness
3

### Presentation
4

### Contribution
3

### Rating
4

### Confidence
4

---

## Human Reviewer 2

### Summary
This paper investigates the role of the CLIP modulation component within Text-to-Image (T2I) diffusion models. The authors begin by questioning its necessity, demonstrating through ablation that its removal has a minimal impact on overall generation performance. Despite this finding, the authors argue that this component enable controllable shifts in the generation process. They propose a novel method that involves altering the modulation guidance at different blocks of the diffusion transofmer. This claim is supported by a thorough quantitative analysis across several T2I models and is further extended to text-to-video models. The authors show that their method improves generation quality in terms of aesthetics and complexity. They also demonstrate that it mitigates common generation failures, such as incorrect object counts and anomalous finger generation.

### Strengths
The paper is clearly written and well-structured. A primary strength lies in its comprehensive experimental validation. The experiments are thorough and are conducted on 4 T2I models that are trained with CLIP modulation, and even included additional model that was not using CLIP, training it to incorporate CLIP modulation. Furthermore, they include text-to-video models, thereby broadening the applicability of their findings.

### Weaknesses
The primary weakness is the limited novelty of the method. This method (with the exception of choosing the dynamic modulation strategies) was already presented in [1] as a naive approach (Equation 2). If the authors disagree, I would be happy to discuss and understand the novelty better.

A second, smaller weakness, concerns the justification for the proposed dynamic modulation strategies. These strategies are heuristically derived from observed attention patterns within the model. This reliance is a potential weakness, as attention weights are not always a reliable or faithful indicator [2] of a model's internal semantic processing at different hierarchical levels. While the authors attempt to validate these attention-driven heuristics through an ablation study, the results appear inconclusive and fail to provide a definitive justification for the chosen strategies.

[1] TokenVerse: Versatile Multi-concept Personalization in Token Modulation Space (Garibi and Yadin et al. 2025)
[2] Attention is not Explanation. (Jain et al. 2019)

### Questions
- The analysis suggests that CLIP modulation is more influential for short prompts compared to long prompts. Do the authors have a hypothesis for this observed phenomenon?

### Soundness
4

### Presentation
4

### Contribution
4

### Rating
8

### Confidence
3

---

## Human Reviewer 3

### Summary
This paper revisits the role of global text conditioning in diffusion transformers. In response to the prevailing trend of abandoning modulation mechanisms in favor of attention-only approaches, the authors demonstrate through analysis that while conventionally used pooled text embeddings contribute limited benefits, repurposing them as a guidance mechanism can effectively adjust the diffusion trajectory toward more desirable attributes. This approach, termed modulation guidance, is training-free, straightforward to implement, and enhances performance across multiple tasks including text-to-image, text-to-video generation, and image editing.

### Strengths
1. The revisiting and discovery that global text conditioning can be leveraged as a powerful control signal—rather than being merely a passive input—is novel. The proposed dynamic modulation guidance demonstrates a clear ability to address classic and stubborn challenges in T2I generation, such as hand synthesis and object counting, which is a significant finding.

2. The paper is impressive in its extensive experimental scope, demonstrating effectiveness across a diverse set of tasks—including text-to-image, text-to-video, and instruction-guided editing—and model architectures, encompassing transformer-based DMs and the CLIP-free COSMOS model.

3. The paper is well-structured and easy to follow.

### Weaknesses
I have the following two major questions:

1. I noticed that different hyperparameters are used for different tasks and generation types/styles In Tab.5. Could the authors provide more detailed guidance on the process of selecting the appropriate strategy and its associated hyperparameters for a **new, unseen task**? Is this process largely heuristic, requiring manual search for each new situation, or are there general principles or a methodology that can be derived from the observations in Figure 3 to make this selection more systematic?

2. **Connection and Distinction to h-space Methods:** The work [1] demonstrates that diffusion models possess a semantic latent space (h-space) and that rescaling the difference in latent features ($\Delta h$) can control attribute strength. Could the authors discuss the primary distinction between their method and this prior work? Specifically, is it possible to achieve a similar guidance effect by simply rescaling $\Delta h$, analogous to Equation 3 in this paper, instead of explicitly using the CLIP embedding to compute $y(p^+, t) - y(p^-, t)$?

[1] Mingi Kwon, Jaeseok Jeong, Youngjung Uh. "Diffusion Models Already Have a Semantic Latent Space". *ICLR*, 2023.

### Questions
Please see my **Weaknesses** part.

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
4

---

## Human Reviewer 4

### Summary
This paper revisits the role of global (pooled) text conditioning in diffusion transformers, which has recently been discarded in favor of attention-only conditioning. The authors first demonstrate through empirical analysis that the pooled CLIP embedding contributes little to generation quality in several state-of-the-art models (e.g., FLUX, HiDream-Fast), especially with long prompts. However, they propose a novel perspective: repurposing the pooled embedding for modulation guidance—a training-free, plug-and-play technique that steers the diffusion process toward desirable visual properties (e.g., aesthetics, complexity, hand realism) by extrapolating in the modulation space using positive/negative prompt pairs. The method is simple, incurs negligible overhead, works with or without classifier-free guidance (CFG), and can be retrofitted into models that originally lack pooled embeddings. Extensive experiments across text-to-image, text-to-video, and image editing tasks show consistent improvements in human evaluations and automatic metrics.

### Strengths
1. The paper provides a clear and convincing empirical investigation into why global text conditioning appears ineffective in current models, filling an important gap in understanding.

2. Modulation guidance is training-free, easy to implement, computationally lightweight, and broadly applicable across architectures and tasks.

### Weaknesses
1. The core idea of using pooled embeddings for guidance resembles prior work on semantic directions in GANs (e.g., StyleGAN) and recent methods like TokenVerse or Concept Sliders, though the application to modulation space in diffusion transformers is new.

2. The method introduces new hyperparameters (guidance scale w, layer indices), requiring tuning for different tasks—though ablations help, this adds complexity compared to plug-and-play baselines.

### Questions
NA

### Soundness
2

### Presentation
2

### Contribution
1

### Rating
4

### Confidence
3