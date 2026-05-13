# Experts on Demand: Dynamic Routing for Personalized Diffusion Models

- Decision: Reject
- Scores: 3, 3, 3, 5

## Abstract
Diffusion models have excelled in the realm of image generation, owing to their expansive parameter space. However, this complexity introduces efficiency challenges. Most users only exploit a fraction of the available capabilities for specialized image categories. In this paper, we introduce Mixture of Expert Diffusion Models (MoEDM), a tailored and efficient strategy for large-scale diffusion models specific to certain applications. By employing dynamic routing, MoEDM selectively activates only indispensable neurons, thereby optimizing runtime performance for specialized tasks while minimizing computational costs. Our MoEDM doubles the sampling speed without compromising efficacy across various applications. Moreover, MoEDM's modular design allows straightforward incorporation of state-of-the-art optimization methods such as DPM-Solver and Latent Diffusion. Empirical assessments, validated by FID and KID scores, confirm the advantages of MoEDM in terms of both efficiency and robustness.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors of this paper introduced a series of techniques aimed at enhancing the efficiency of diffusion models. Summarized briefly, their approach includes:

1. Trimming the bottommost layers of the UNET structure, which serves to decrease the total number of parameters.
2. Duplicating the remaining layers and then activating these copies selectively, based on the specific timestep in the diffusion process.
3. Employing knowledge distillation from alternative diffusion models, which lessens the dependency on high-quality data.

When these strategies are applied together, the refined model exhibits a modest boost in both speed and precision compared to the original baseline, especially after being fine-tuned on a narrow and specific dataset

### Strengths
S1: The challenge of expediting diffusion models is critically vital and possesses a broad spectrum of applications across numerous fields.


S2: The concept of integrating Mixture of Experts (MOE) within diffusion models presents an intriguing avenue for investigation and merits further exploration.

### Weaknesses
W1: While the paper contributes to ongoing discussions in the field, the technical novelty could be further strengthened. The concept of layer removal has precedents, such as in the design of SDXL [1]. Additionally, the current application of Mixture of Experts (MOE) seems to follow familiar patterns, similar to those seen in EDiff-I [2], which might benefit from a more rigorous comparative analysis. The use of distillation to enhance data efficiency is an interesting approach, though its integration with the other proposed methods (aiming for efficiency improvements) appears tangential and warrants a clearer rationale.

W2: The experimental validation presented could be more robust. The majority of efficiency gains appear attributable to the removal of intermediate layers, raising questions about the relative contribution of other proposed innovations. The focus on a singular class from ImageNet may not sufficiently demonstrate the model's generalizability. For the text-to-image results, the paper only present a few curated images, and it would benefit from a broader set of comparisons to fully ascertain the model's effectiveness.

W3: The clarity and structure of the paper would greatly benefit from revision. For instance, the processes following the removal of intermediate layers, including whether the model undergoes fine-tuning with the original dataset, are not clearly outlined. A more detailed discussion in the technical sections, perhaps with an expanded explanation of the loss functions used, would enhance the reader's understanding.

### Questions
please find my comments in the weakness section.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a personalization method based on diffusion models, named MoEDM. This method aims to accelerate computational cost and time while preserving performance metrics across various datasets. Experiments are conducted on ImageNet and FFHQ with FID and KID evaluation metrics.

### Strengths
1.The paper tackles a relevant application (i.e., personalization) of the prominently used diffusion models.
2.The proposed method can incorporation of the technique of model acceleration, e.g., DPM-Solver.

### Weaknesses
1.The first and perhaps the main weakness of the paper is its poor presentation. 1) the term "an all-encompassing arsenal" is introduced in the second paragraph of the Introduction but is not explained or mentioned later, leading to confusion regarding this concept. 2) In the Introduction, the paper mentioned “…, deploying a general-purpose diffusion model is not just inefficient but egregiously wasteful”. However, the paper does not provide a comprehensive explanation of why it is inefficient and wasteful. Furthermore, Figure 1 also fails to illustrate this point. 3) In the Introduction, the paper mentioned “…often fall short in preserving the performance attributes of diffusion models”. The paper also does not provide a comprehensive explanation of why these methods are “fall short in preserving the performance…”. As such, it is recommended that further provide qualitative and quantitative experiments. The same issue still applies to the remaining sections.
2.As mentioned in the paper, the term 'minimal computational cost' is used, but it lacks a clear definition, making it a concept that may lead to confusion.
3.In Section 3.1, the paper mentions that the convolutional layers 'constitute approximately 80% of the model’s parameters.' However, the paper does not provide the calculation method used to obtain this value.
4.Why setting diffusion models to zero is work ? 
5.It’s better to provide experiments comparing with model acceletion methods (DPM-Solver, DPM-Solver++, DDIM, ToMe) to prove that MoEDM enhances the inference efficiency.
DDIM: Denoising Diffusion Implicit Models;
ToMe: Token merging for fast stable diffusion; 
DPM-Solver: A Fast ODE Solver for Diffusion Probabilistic Model Sampling in Around 10 Steps; 
DPM-Solver++: Fast Solver for Guided Sampling of Diffusion Probabilistic Models;
The experimental validation is not convincing:
1.The paper only provides 64x64 and 256x256 resolution outputs, while diffuison-based models can generate high-resolution results of 512x512 (e.g., Stable DIffusion).
2.In this paper, the proposed method aims to reduce computational costs, but its effectiveness may not be fully convincing. Training experiments require 8 NVIDIA A100 GPUs, and even for sampling, a single NVIDIA A100 with 80GB of memory is needed.
3.It would be more valuable to see if this method can be built with more diffusion models, like Stable Diffusion and DeepFloyd-IF.
It would be better to compare the proposed method with current personalization methods based on diffusion models, such as CustomDiffusion and DreamBooth.
CustomDiffusion: Multi-Concept Customization of Text-to-Image Diffusion; DreamBooth: Fine Tuning Text-to-Image Diffusion Models for Subject-Driven Generation;

### Questions
see Weaknesses

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces MoEDM, a novel approach for building a mixture-of-experts tailored for personalized large-scale diffusion models. MoEDM starts by layer-wise pruning a dense diffusion model, which reduces memory requirements. Subsequently, it constructs a mixture of the pruned models via  dynamic routing, achieving faster sampling speeds without requiring additional training. The proposed approach is thoroughly validated through experiments conducted on image datasets to demonstrate its effectiveness.

### Strengths
- The paper tackles a timely and practically-relevant problem supported by a fair amount of experiments, and stands as a pioneering study in attempting to build mixtures of diffusion expert models.

### Weaknesses
 - In general, the writing is difficult to follow, and lacks technical details.
    - How is the channel sensitivity metric $\cal{S}_c$ calculated and what is its computational overhead? 
    - It's unclear whether the gating vector $\cal{G}$ is trainable or how it's determined.
    - The paper could benefit from providing an explicit pruning algorithm to enhance understanding.
    - There's a lack of clarity regarding when and how dynamic gating is utilized to construct the mixture of experts. MoE typically involves training with load balancing loss, but there are no details about dynamic gating in this context.
- The performance for high-resolution images appears to be only marginally improved, which could be discussed in more detail.
- Ablation study regarding the number of experts should be included, as most experimental results consistently show a 50% boost in inference speed.
- The experiments are limited to U-Net-based models, and it's uncertain whether the proposed method is applicable to various architectures such as DiT [1].
- The paper lacks baselines. For example, [2] can be served as a pruning baseline.

### Questions
- How many random seeds are used throughout the experiments? 

[1] Peebles et al., “Scalable Diffusion Models with Transformers.” 2022.\
[2] Fang et al., “Structural Pruning for Diffusion Models.” 2023.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper introduces a personalized MoE (mixture of expert) structure of diffusion models, named as MoEDM, for text2image generations. The proposed MoEDM enhances the inference efficiency for the desinated tasks, mantaining intact the task-specific performance metrics. The parameter sparse strategy effectively navigates the trade-off between efficiency and capability, establishing it as a feasible optimization technique for diffusion models. The experimental results show the good performances of the proposed MoEDM model.

### Strengths
This paper introduces a sparse mixture of expert structure of diffusion models to enhances the inference efficiency for the text2image generation tasks. The experimental results show the good inference performances of the proposed models.

### Weaknesses
1. Novelty is limited. The MoE structure is widely applied for the AIGC models, especially large foundation models. As for the diffusion models, MoE structure is not firstly introduced for the text2image diffusion models, e.g. [RAPHAEL: Text-to-Image Generation via
Large Mixture of Diffusion Paths].  The sparse parameter pruning with MoE is also widely used for the large dense model，e.g. [Task-Specific Expert Pruning for Sparse Mixture-of-Experts]. Although this paper introduces a sparse MoE structure to prune the large scale of parameters of dense diffusion models, the novelty of the proposed methods is limited.

2. Experiments are probably not sufficient. It is not easy to evaluate the performance of the image generation method. The evaluation metrics, KID and FID  are actually insensitive to the generated image  quality and these metrics cannot evaluate the image  quality well.

### Questions
1. Please highlight the novelty and contribution of the proposed sparse strategy with the Diffusion models
2. Please clarify more details, e.g. the expert balance operation, of the proposed MoEDM.
3. Please add more image quality comparison between the proposed MoEDM and baseline

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
