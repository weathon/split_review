# Latent Consistency Models: Synthesizing High-Resolution Images with Few-step Inference

- Decision: Reject
- Scores: 5, 6, 6, 5

## Abstract
Latent Diffusion models (LDMs) have achieved remarkable results in synthesizing high-resolution images. However, the iterative sampling process is computationally intensive and leads to slow generation.
Inspired by Consistency Models~\citep{song2023consistency}, 
we propose Latent Consistency Models (\textbf{LCMs}), enabling swift inference with minimal steps on any pre-trained LDMs, including Stable Diffusion~\citep{rombach2022high}. 
Viewing the guided reverse diffusion process as solving an augmented probability flow ODE (PF-ODE), LCMs are designed to directly predict the solution of such ODE in latent space, mitigating the need for numerous iterations and allowing rapid, high-fidelity sampling. 
Efficiently distilled from pre-trained classifier-free guided diffusion models, a high-quality 768$\times$768 2$\sim$4-step LCM takes only 32 A100 GPU hours for training.
Furthermore, we introduce Latent Consistency Fine-tuning (LCF), a novel method that is tailored for fine-tuning LCMs on customized image datasets. Evaluation on the LAION-5B-Aesthetics dataset demonstrates that LCMs achieve state-of-the-art text-to-image generation performance with few-step inference. Project Page: \url{https://latent-consistency-models.io/}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes latent consistency models (LCMs) to swiftly inference with minimal steps on any pre-trained LDMs, e.g., Stable Diffusion. LCMs are designed to directly predict the solution of an augmented probability flow ODE in latent space to allow rapid, high-fidelity sampling. A latent consistency fine-tuning (LCF) is further introduced to fine-tune LCMs on customized image datasets. Experiments on the LAION-5B-Aesthetics dataset demonstrates the effectiveness of the proposed LCMs.

### Strengths
+ The idea is interesting to view the guided reverse diffusion process as solving an augmented probability flow ODE.

+ The performance looks good on both qualitative and quantitative results and in some cases the results of the proposed method with less steps are better than those of other methods with more steps.

+ Some ablation studies are provided to facilitate the understanding of how the performance benefits from different components, including ODE solvers, skipping-step schedule and guidance scale.

### Weaknesses
 - Although the authors claim several contributions, it is not clear which ones have the most significant impact on efficiency and quality.

- What is the computational complexity of solving augmented PF-ODE?

- The experiments shows that the proposed method reduces the inference steps, however, how much faster is the inference time exactly compared with other methods?

- What about the performance when the proposed LCMs are applied to other LDMs besides Stable Diffusion?

### Questions
1. It is not clear which contributions have the most significant impact on efficiency and quality.

2. What is the computational complexity of solving augmented PF-ODE?

3. How much faster is the inference time exactly compared with other methods?

4. What about the performance when the proposed LCMs are applied to other LDMs besides Stable Diffusion?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors apply the consistency model to the latent diffusion, significantly reducing the inference steps in diffusion models. They also implement guided distillation, enhancing quality through classifier-free guidance, and introduce time step skipping to expedite the distillation process. The effectiveness is demonstrated through experiments on LAION subsets.

### Strengths
* The paper is well-written and the method is intuitive to understand.
* The results are impressive. The proposed method can significantly reduce the sampling steps of the diffusion models while achieving a decent quality performance.

### Weaknesses
 * The authors should benchmark their approach against the single-step diffusion model [InstaFlow](https://github.com/gnobitab/InstaFlow) [1], and also include results from the original 50-step Stable Diffusion as a baseline. It's currently unclear how their method's speed gains affect performance.
* The proposed latent consistency fine-tuning seems not working, as shown in Figure 6. On the Simpsons dataset, the quality of 30K finetuning is worse than the original LCM.
* The paper lacks results on realistic photo generation, featuring only artistic illustrations. Including realistic photo results would strengthen the evaluation.
* The paper's novelty appears limited. It primarily adapts consistency models to latent space and uses guided distillation in Meng et al. [2] to support Classifier-Free Guidance. While skipping time steps shows efficacy, it doesn't substantially elevate the paper's technical novelty. Are there some challenges of applying consistency models to latent space compared to pixel space?

### Questions
* No corresponding text prompts in the visual results (e.g., Figure 1).
* Typo. Section 3 Preliminaries -- Diffusion Models: "origin data distribution" -> "original data distribution"

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
This paper proposes latent consistency models for fast high-resolution image generation. In addition, it provides a simple and efficient one-stage guided consistency distillation method for few-step (2∼4) or even 1-step sampling. Experiments show that the LCMs achieves state-of-the-art text-to-image generation performance with few-step inference.

### Strengths
1. The idea is novel and interesting. The author proposes latent consistency models that leverage consistency model in latent space, achieving few-step or even one-step sampling.
2. The experimental results look impressive. The latent consistency model outperforms state-of-the-art methods by large margin especially with one step.

### Weaknesses
1. The paper is not well-organized. The introduction of the proposed method in Sec.1 is too concise. The description and motivation for each design should be more detailed. Figure.1 takes up too much space and can be reduced appropriately. 
2. Insufficient content for related work.
3. Lack of ablation studies. The authors should provide qualitative results of the ablation studies on the ODE solvers & skipping-step schedule as well as qualitative and quantitative results on guided consistency distillation.

### Questions
1. What's the overall pipeline of the proposed method? It seems that the authors do not describe or show the pipeline in detail.
2.  It is better to show the comparisons between training time and memory.

### Soundness
3 good

### Presentation
2 fair

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
This paper proposes to train consistency models using a pretrained large latent diffusion model (i.e., Stable Diffusion). The main difference between the original consistency models follows: (a) Consideration of augmented ODE with guidance scale $\omega$ to enable the distillation in a single stage, (b) use skipping timesteps for distillation since pretrained Stable Diffusion uses larger timestep (1,000) than original consistency models that use EDM formulation.

### Strengths
- The paper is generally well-written and easy to follow.
- Compared with other efficient sampler or distillation methods, the proposed method shows a considerable performance improvement in a smaller sampling step regime.

### Weaknesses
 - My major concern is about the technical novelty and contribution of this work. The paper argues there are two main contributions: (a) usage of augmented ODE and (b) skipped timestep (e.g., $k=20$) for better distillation. For (a), it seems quite straightforward to consider augmented ODE since the Stable Diffusion uses cfg. Specifically, the application of classifier-free guidance (CFG) within the ODE framework is a well-established technique, and the paper does not present a novel formulation or analysis of this augmentation. For (b), it also seems straightforward since Stable Diffusion uses a large timestep ($T=1000$), unlike EDM formulation in the original consistency model paper, and thus, one can easily expect using consecutive timesteps for distillation is inefficient. The choice of skipping timesteps is a direct consequence of the large timestep space in Stable Diffusion and doesn't introduce a new algorithmic insight. In these respects, I think both (a) and (b) looks too straightforward and marginal technical contribution to be accepted at ICLR. 
-  Title -- "Latent" Consistency model? I expected the authors to consider unique aspects of the "latent" diffusion model in incorporating the concept of consistency models; for instance, the original consistency model paper argues using perceptual metrics is efficient for better distillation. However, it seems the proposed method does not depend on whether the pretrained model is a latent diffusion model or not; it can be applied to any diffusion model that uses a large timestep (e.g., $T=1000$); thus, I think including "latent" in the title is unnecessary. 
- For figures for qualitative illustrations, it's better to provide text prompts to show the image-text alignment as well.

### Questions
- Why is the DDIM sampler mainly used for LCD (main experiments; Table 1 and 2)? What if the method uses a different ODE solver/sampler? 
- Which metric does LCD use for distillation? The original consistency model paper mainly uses the LPIPS score, but it seems such a metric is not applicable since this method deals with latent diffusion models.

### Soundness
3 good

### Presentation
3 good

### Contribution
1 poor
