# SparseDM: Toward Sparse Efficient Diffusion Models

- Decision: Reject
- Scores: 3, 5, 3, 5

## Abstract
Diffusion models represent a powerful family of generative models widely used for image and video generation. % extensively used in data generation tasks and are recognized as one of the best generative models. 
However, the time-consuming deployment, long inference time, and requirements on large memory hinder their applications on resource constrained devices.
In this paper, we propose a method based on the improved Straight-Through Estimator to improve the deployment efficiency of diffusion models. 
Specifically, we add sparse masks to the Convolution and Linear layers in a pre-trained diffusion model, then transfer learn the sparse model during the fine-tuning stage and turn on the sparse masks during inference.
Experimental results on a Transformer and UNet-based diffusion models demonstrate that our method reduces MACs by $50\%$ while increasing FID by only 0.44 on average. 
Sparse models are accelerated by approximately 1.2x on the GPU.
Under other MACs conditions, the FID is also lower than 1 compared to other methods.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes a pruning strategy for Diffusion models, using mask pruning to achieve progressive multi-step pruning. Ultimately, it realizes 1:2 pruning according to the Ampere architecture. During training, knowledge distillation is used to transfer knowledge from the full model to the pruned model.

### Strengths
The writing is very clear, and the main idea is highlighted effectively.

### Weaknesses
1. The pruning strategy is based on existing structures, with a relatively simple motivation. There are already other methods that achieve similar results, such as using linear attention or directly training a smaller model with distillation.
2. Compared to directly using STE-based pruning, it does not further reduce the computational load.
3. In Section 3.2, "Transfer learn sparse diffusion models" strategy is mentioned, but it does not explain the significant differences between this strategy and the progressive sparse training strategy discussed in Section 2.2. If the focus is solely on testing with perturbed datasets, it may not constitute a significant contribution.
4. A generalized pruning strategy suitable for Transformer networks has not been proposed; simply relying on data perturbations is insufficient to demonstrate applicability to other datasets. Further testing on additional datasets, such as CelebA-HQ, LSUN Church, would be beneficial.
5. Many of the latest comparative algorithms from 2024 are not mentioned, such as "Pruning for Robust Concept Erasing in Diffusion Models" and "LD-Pruner: Efficient Pruning of Latent Diffusion Models using Task-Agnostic Insights."
6. There is no comparison of the parameter counts for each layer of the SD model before and after sparse pruning. It is recommended to include a chart in the appendix to illustrate this.
7. While Section 2.3 mentions applying perturbations to the dataset, it does not provide specific details on how the perturbations were implemented.
8. The experiments only validate the FID score as a single metric; it is advisable to explore additional metrics, such as SSIM.
9. The proposed method is heavily reliant on the specific architecture design of the NVIDIA Ampere architecture, limiting its general applicability as a pruning technique.
10. The comparison between progressive pruning and fixed pruning rates, as shown in Figure 3(b), lacks sufficient experimental validation or theoretical justification beyond the optimizer's training objective.

### Questions
Could the authors provide the parameter counts for each layer of the SD model before and after sparse pruning?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes to improve the efficiency of DM by sparse matrix for 2:4 sparse acceleration GPU. The authors improve the STE method and propose to gradually transfer knowledge from dense models to sparse models.

### Strengths
1.	This paper is well-written.
2.	The motivation is clear enough.
3.	The organization of this paper is great.

### Weaknesses
1.	There is a typo in Eq5. Please also check all equations. Moreover, not all symbols have been explained.
2.	The experiments are relatively limited. Specifically, only two U-ViT and DDPM are tested on the proposed pruning, which are proposed in 2022 and 2020 respectively. More recently proposed DiT or other methods should also be included.
3.	The limitation and discussion are missing in this paper.

### Questions
1.	The authors mentioned that “it does not mean that the greater the sparsity, the better the FID”. Please discuss the reason and why you choose 2:4 sparse.
2.	Please discuss the reason ASP performs so worse in all experiments.
3.	Please also clarify why your method and STE-based pruning fulfill the same MACs.
4.	Please explain the reason that the FID of the proposed method in Fig. 3a obtain a lower FID in the first several steps.
5.	Why the initial FID of 2:4 sparse in Fig.3b and Fig.3d is different?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work aims to reduce the computation of Diffusion Models during inference. The authors suggest a method of straight-through estimation, which applies sparse masks to layers of a pretrained diffusion model and then employs transfer learning for training. Then, they use the same sparse mask during inference to improve compute efficiency.

### Strengths
- The 2:4 sparse model calculation offers practical values for practitioners using NVIDIA Ampere architecture GPUs.

### Weaknesses
 - While it may have some practical value for practitioners using NVIDIA Ampere architecture, the same technique may not benefit other practitioners or general researchers without access to Ampere architecture.

- Besides, the straightforward idea of using masked training is neither interesting nor technically new.

- More disappointingly, the speed acceleration due to this customized training for a particular architecture increases by x1.2 only. Studies related to reducing time steps for Diffusion inference or diffusion quantization/pruning methods may be more effective in achieving the same purpose.

### Questions
Please address the weakness stated above.

### Soundness
1

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces SparseDM, which converts existing diffusion models into sparse models that fit in a 2:4 sparse operator on the GPU. Specifically, the authors propose a Straight-Through Estimator (STE)-based fine-tuning framework that learns sparse masks. These sparse masks accelerate GPU inference speed up to 1.2. Comprehensive experiments validate the effectiveness of the proposed method.

### Strengths
* The paper introduces a simple fine-tuning method that converts existing diffusion models into sparse models, enabling them to be used in scenarios with limited computing power, such as on mobile devices.

* The observations about fixed sparse training are interesting.

* Experiments on various generation scenarios verify the effectiveness of SparseDM compared to baselines.

### Weaknesses
 **Weakness 1: More clarifications on Section 2.3.**

In Section 2.3, the authors claim that diffusion models only consider the distribution shift of the noisy data while sparse pruning methods only consider the model's weight change. Then, referring to RFR, the authors convert the model's weight changes resulting from sparse pruning methods into data changes for the diffusion model's training process. However, typical diffusion models have indicators for perturbed data (such as the noise schedule and timestep embedding), and it is unclear how these relate to perturbations caused by sparse training. Specifically, the interaction between the noise schedule, which dictates the level of noise added at each step, and the sparsity mask, which alters the effective weights of the network, is not well-defined. It is unclear if the RFR method adequately accounts for the combined effect of these two distinct forms of perturbation. The authors need to clarify how the data changes induced by RFR align with the inherent noise schedule and timestep embeddings within diffusion models.

**Weakness 2: Lack of analysis of fixed sparse training**

I am not sure why fixed sparse training would be more effective than traditional progressive sparse training. Based on the experimental results, it seems that fixed sparsity applies a consistent distribution shift across all noise levels in diffusion training, whereas progressive sparse training gradually shifts the predefined noise levels, which may hinder the diffusion training process. However, this claim has not been theoretically verified, so the authors should provide theoretical proof to demonstrate the relationship between diffusion training and sparse training. Furthermore, the authors should provide a more detailed analysis of the optimization landscape under fixed versus progressive sparsity. It is not clear why a consistent distribution shift would be inherently easier to optimize for than a gradual one, especially given the non-convex nature of deep learning optimization. A more rigorous analysis, potentially involving visualization of the loss landscape or analysis of gradient behavior, is needed to support this claim.

### Questions
* In Table 3, some variants (e.g., patch size = 2 and mlp_ratio = 2) are slower than the dense model, why do you think this is?
* I think it would strengthen the effectiveness of SparseDM if the author show that it can also be applied to models like Stable Diffusion.

### Soundness
2

### Presentation
2

### Contribution
3
