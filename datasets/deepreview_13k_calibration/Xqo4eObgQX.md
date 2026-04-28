# TimeStep Master: Asymmetrical Mixture of Timestep LoRA Experts for Versatile and Efficient Diffusion Models in Vision

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 6, 5, 5

## Abstract
Diffusion models have driven the advancement of vision generation over the past years. 
However, 
it is often difficult to apply these large models in downstream tasks, 
due to massive fine-tuning cost.
Recently, 
Low-Rank Adaptation (LoRA) has been applied for efficient tuning of diffusion models.
Unfortunately, 
the capabilities of LoRA-tuned diffusion models are limited, 
since the same LoRA is used for different timesteps of the diffusion process.
To tackle this problem, 
we introduce a general and concise TimeStep Master (TSM) paradigm with two key fine-tuning stages.
In the fostering stage (1-stage), 
we apply different LoRAs to fine-tune the diffusion model at different timestep intervals.
This results in different TimeStep LoRA experts that can effectively capture different noise levels. 
In the assembling stage (2-stage),
we design a novel asymmetrical mixture of TimeStep LoRA experts,
via core-context collaboration of experts at multi-scale intervals.
For each timestep,
we leverage TimeStep LoRA expert within the smallest interval as the core expert without gating, 
and use experts within the bigger intervals as the context experts with time-dependent gating.
Consequently,
our TSM can effectively model the noise level via the expert in the finest interval,
and 
adaptively integrate contexts from the experts of other scales,
boosting the versatility of diffusion models.
To show the effectiveness of our TSM paradigm, 
we conduct extensive experiments on three typical and popular LoRA-related tasks of diffusion models, 
including 
domain adaptation, 
post-pretraining,
and 
model distillation.
Our TSM achieves the state-of-the-art results on all these tasks, 
throughout various model structures (UNet, DiT and MM-DiT) and visual data modalities (Image, Video), 
showing its remarkable generalization capacity.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors propose a novel LoRA-based fine-tuning method to efficiently adapt large diffusion-based image generation models. They identify limitations in LoRA-tuned models, noting that diffusion models process noisy inputs differently at various time steps, which restricts their generative capability.
To address this, the paper introduces the TimeStep Master (TSM) paradigm, which incorporates different LoRA matrices for distinct time steps, enabling the learning of various processing modes. TSM comprises two main stages:
Fostering Stage: This phase segments the training process into timestep intervals, each using different LoRA modules.
Assembling Stage: This phase combines the TimeStep LoRA experts, facilitating core-context collaboration.
TSM achieves state-of-the-art performance in domain adaptation, post-pretraining, and model distillation tasks. Furthermore, it demonstrates robust generalization across diverse model architectures and visual data modalities.

### Strengths
The authors effectively address the limitations of a single shared LoRA across the entire diffusion process by partitioning it into multiple intervals, enhancing adaptability.
They recognize the efficiency benefits of shared timestep experts, avoiding the need for individual experts for each timestep and proposing a collaborative learning function to maintain efficiency.
The paper is well-structured and provides compelling qualitative and quantitative results.

### Weaknesses
The rationale for using different scales of intervals in the assembling stage is not clearly explained.
The paper lacks a comparison between the asymmetrical MoE (Mixture of Experts) and the standard MoE.

Some other comments: 

In Figure 3, if only a single scale with n=8 intervals were used, would the vanilla MoE already be capable of learning how to combine the context experts with the core expert through top-2 gating?

In addition, the LoRA projection and reconstruction aim to find the best rank for attention. It seems that the rank is chosen as a hyperparameter. Is it not clear why such a choice is made if this is the real rank of the target matrix. In addition, it is hard to justify why different blocks will share the same rank.

### Questions
See weakness

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
The paper finds that using the same LoRA for fine-tuning diffusion models at different timesteps has its limitations. To address this, this paper proposes the TSM paradigm, which employs different LoRA adaptations at various timesteps and integrates them through a novel asymmetrical mixture, achieving state-of-the-art performance across multiple tasks and model structures.

### Strengths
1. This paper identifies a key limitation in using a single LoRA for fine-tuning diffusion models: the significant differences in feature distributions across different timesteps make it challenging for a single LoRA to effectively learn all information. To address the above issue, the paper introduces a two-stage approach that leverages multiple LoRA modules and an ensemble method.
2. Comprehensive experiments are conducted across several tasks, such as domain adaptation, post-pretraining, and model distillation, all yielding promising results.
3. The paper’s illustrations clearly depict the details of the proposed method.

### Weaknesses
1. Since TSM uses a router to dynamically assemble experts based on timestep and previous step results, each timestep may involve multiple expert calls. This results in higher memory usage and greater latency during inference. The paper does not provide a detailed analysis of the computational overhead, such as the exact increase in FLOPs or memory footprint during both training and inference. This makes it difficult to assess the practical applicability of the method, especially for resource-constrained environments.
2. Although the assembling stage can be understood from the flowchart, the explanation of Equation (7) may be somewhat confusing, especially regarding the subscript notation of $\epsilon$, which lacks clarity. The paper should provide a more rigorous mathematical definition of $\epsilon$ and its role in the equation. It is unclear if $\epsilon$ represents a single noise vector or a distribution, and how it interacts with the timestep-specific LoRA parameters.
3. Regarding the results in Table 1, the paper presents various outcomes for SD2 and SD2+X, but the results for SD2 with the proposed method are missing. It is unclear why the authors did not include the direct comparison of their method with the base SD2 model. This omission makes it difficult to assess the true improvement achieved by the TSM method over a standard SD2 model without any additional modifications.
4. In Table 2, the authors provide results on T2I-CompBench and EvalCrafter, yet FID is also a widely accepted and important metric in pretraining works such as Pixart-alpha. The absence of FID scores makes it difficult to compare the performance of the proposed method with other state-of-the-art diffusion models that typically report FID scores. The paper should include FID scores to provide a more comprehensive evaluation.
5. Table 6 shows the ablation study for the first stage of TSM, where it’s observed that the overall performance improves with 8 experts. The paper does not explore the potential for diminishing returns or even performance degradation with an excessive number of experts. A more thorough investigation into the relationship between the number of experts and performance is needed, including a discussion of the trade-offs between performance gains and computational costs.

### Questions
Please refer to the weaknesses part.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces the TimeStep Master (TSM) paradigm for efficiently fine-tuning diffusion models using Low-Rank Adaptation (LoRA). TSM addresses the limitation of applying the same LoRA across all timesteps by introducing two stages: fostering, where different LoRAs are applied to specific timestep intervals, and assembling, which combines these experts asymmetrically with a core-context collaboration. TSM improves diffusion models' ability to handle different noise levels, resulting in better performance across tasks like domain adaptation, post-pretraining, and model distillation, with reduced computational costs.

### Strengths
The TimeStep Master (TSM) paradigm addresses the problem of text adherence deterioration in LoRA-tuned diffusion models by introducing different LoRA modules for distinct timesteps, allowing the model to handle varying noise levels more effectively. The use of an asymmetrical mixture of experts, with a core-context collaboration mechanism, helps improve model adaptability to different noise distributions. TSM demonstrates versatility across tasks such as domain adaptation, post-pretraining, and model distillation, achieving strong results on various benchmarks for both images and videos. Its design also maintains relatively low computational costs, making it an efficient option for fine-tuning large models, with results showing broad applicability across different architectures and data modalities.

### Weaknesses
1. The paper does not clearly compare its method with non-LoRA approaches that address prompt misalignment issues such as attribute disentanglement, spatial relationships (Fig. 1), generation omissions, and distortions (Fig. 4). These include training-free methods like *Training-Free Structured Diffusion Guidance*, *BoxDiff*, and *Training-Free Layout Control with Cross-Attention Guidance*, or training-required methods like *LayoutDiffusion*. A comparison of computational overhead and training parameters would provide more insight into the advantages of the proposed method.

2. Prompt misalignment issues, such as incorrect spatial relationships and attribute binding errors, are common even in pre-trained or fully fine-tuned models. These problems are not exclusive to LoRA-tuned models and may not be solely caused by the different noise levels at various timesteps, as suggested by the authors. More explanation and insight are needed on how the proposed LoRA tuning method resolves these issues. Additionally, to validate the authors' claim that deterioration in LoRA-tuned models is due to using a single LoRA across all timesteps, it might be sufficient to fine-tune only the UNet parameters without modifying the text encoder. Since the text encoder statically computes embeddings and doesn't adjust based on timestep noise levels, any improvements from tuning it may come from upgrading the text encoder itself. More experiments are necessary to confirm this.

3. Combining multiple LoRAs can sometimes impair a pre-trained model's inherent generative ability or cause individual LoRA characteristics to be lost. It’s unclear whether the gating-based combination method explored the potential degradation in model performance. Including comparisons with other LoRA combination methods, such as *Linear Arithmetic Composition* or *Reference Tuning-Based Composition*, could provide more insights. Moreover, ablation studies on LoRA combination methods (beyond just the gating inputs) would be useful. A related work is *Mixture of LoRA Experts*.

4. As mentioned in point 1, non-LoRA methods can address similar issues, potentially with lower computational cost. Some training-free approaches also achieve good results. It remains unclear if the TSM LoRA-tuned method is necessary or optimal for specific application scenarios. While the method is interesting and simple, its practical use in certain scenarios remains to be seen.

5. In Fig. 4, the "in the style of Sci-Fi" prompt does not seem to be well followed, and in Fig. 5, some images (e.g., the black-and-white image) show poor understanding of the prompt.

### Questions
As I understand it, compared to traditional LoRA, the proposed method combines multiple different interval LoRAs at the same timestep, with different LoRAs for different timesteps. Does this only result in an additional 1M parameters? Could the authors clarify more specifically where the 1M increase in training parameters comes from? Is it solely due to the added gating mechanism?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper, focusing on efficiently fine-tuning diffusion models for vision tasks. proposes a new framework, TSM, which improves the LoRA tuning of diffusion models by using different LoRA modules for various timesteps during training. The finetuning consists of a fostering stage, where TimeStep LoRA experts are trained at different timestep intervals to capture varying noise levels, and an assembling stage for an asymmetrical mixture of TimeStep LoRA experts combining these experts at multiple scales, The authors demonstrate the effectiveness of TSM on several tasks and show TSM outperforms vanilla LoRA methods and achieves state-of-the-art results in multiple tasks.

### Strengths
1. Rather than applying the vanilla LoRA, TSM  introduces an innovative way to address the limitations of LoRA in diffusion models by creating specialized experts for different timesteps.
2. TSM achieves SOTA results across multiple tasks on image and video modalities. The results show consistent improvements in model performance and generalization.

### Weaknesses
1. The two-stage TSM approach relies on a relatively complex design, which requires heavy fine-tuning and hyperparameter optimization, such as the interval selection and router design. This may not generalize easily to tasks outside the evaluated benchmarks. The reliance on a two-stage process, with distinct fostering and assembling stages, introduces a level of complexity that could hinder its adoption in scenarios where computational resources or development time are limited. Furthermore, the specific choices for timestep intervals and the architecture of the router network are critical hyperparameters that require careful tuning, potentially limiting the method's practical applicability.
2. Extra parameters limit the scalability of the model. It also inherits the inference procedure of the diffusion process, which is also computationally burdensome. While the authors claim the additional parameters are small, the cumulative effect of multiple LoRA modules, especially when combined with the inherent computational cost of diffusion models, could still pose a challenge for deployment on resource-constrained devices or in real-time applications. The inference process, which involves iterative denoising steps, remains computationally expensive, regardless of the fine-tuning method.
3. Compared to Vanilla LoRA, some improvements, such as in color and shape metrics shown in Table 1, are relatively modest. Although the paper demonstrates improvements across multiple metrics, the gains in color and shape, particularly in Table 1, are not as substantial as one might expect given the complexity of the proposed method. This raises questions about the practical significance of these improvements, especially when considering the added computational overhead and complexity.

### Questions
1. The ablation study shows that the increase of r does not necessarily increase the performance. Were other values of r tested? How would the performance change w.r.t the dimension r?
2. Can this framework be applied to more tasks? For example, image restoration or image segmentation. The reviewer wants to see some simple experiments about this.

### Soundness
2

### Presentation
3

### Contribution
2
