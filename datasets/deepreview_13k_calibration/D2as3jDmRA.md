# LinFusion: 1 GPU, 1 Minute, 16K Image

- Decision: Reject
- Avg Score: 6.25
- Scores: 6, 5, 6, 8

## Abstract
Modern diffusion models, particularly those utilizing a Transformer-based UNet for denoising, rely heavily on self-attention operations to manage complex spatial relationships, thus achieving impressive generation performance. 
However, this existing paradigm faces significant challenges in generating high-resolution visual content due to its quadratic time and memory complexity with respect to the number of spatial tokens. 
To address this limitation, we aim at a novel linear attention mechanism as an alternative in this paper. 
Specifically, we begin our exploration from recently introduced models with linear complexity, \textit{e.g.}, Mamba2, RWKV6, Gated Linear Attention, \textit{etc}, and identify two key features—attention normalization and non-causal inference—that enhance high-resolution visual generation performance. 
Building on these insights, we introduce a generalized linear attention paradigm, which serves as a low-rank approximation of a wide spectrum of popular linear token mixers. 
To save the training cost and better leverage pre-trained models, we initialize our models and distill the knowledge from pre-trained StableDiffusion (SD). 
We find that the distilled model, termed LinFusion, achieves performance on par with or superior to the original SD after only modest training, while significantly reducing time and memory complexity. 
Extensive experiments on SD-v1.5, SD-v2.1, and SD-XL demonstrate that LinFusion enables satisfactory and efficient zero-shot cross-resolution generation, accommodating ultra-resolution images like 16K on a single GPU. 
Moreover, it is highly compatible with pre-trained SD components and pipelines, such as ControlNet, IP-Adapter, DemoFusion, DistriFusion, \textit{etc}, requiring no adaptation efforts.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper introduces LinFusion, a versatile pipeline designed to enhance GPU memory efficiency and boost sampling speed across various diffusion models for image generation. Specifically, LinFusion investigates recent linear-attention mechanisms to identify key factors that enable their effectiveness in diffusion models and subsequently proposes an improved, generalized linear attention to replace standard self-attention. To simplify training, the models are not trained from scratch; instead, LinFusion selectively distills its linear attention module from the original diffusion models, keeping all other weights fixed. Additional supervision is applied to align both the final output and intermediate feature representations. Extensive experiments demonstrate that LinFusion can be effectively integrated with different diffusion models, significantly accelerating image generation.

### Strengths
- The motivation is clear and well-founded, with a thorough analysis of existing linear attention mechanisms to identify the key factors contributing to their effectiveness in diffusion.
- Extensive experiments across various applications support the claims that LinFusion is both efficient and generalizable to different diffusion models as well as existing training and testing pipelines.
- Overall, the writing is fluent and easy to follow, with informative figures that provide ample supporting information.

### Weaknesses
 - The comparisons are conducted only during the sampling stage. Since the proposed LinFusion module may also provide similar benefits during training, are there any metrics available for this stage?
- Related to the previous point, the paper includes only fine-tuning experiments. It would be valuable to investigate whether training a diffusion model from scratch with LinFusion replacing self-attention results in any performance drop. If so, what is the extent of this drop? Experiments on a class-conditional image generation task would be informative, even without a large-scale text-to-image model.
- The memory and efficiency comparisons primarily utilize PyTorch 1.13, which does not incorporate memory-efficient methods like flash-attention or flash-attention v2. How significant is the difference in memory consumption and sampling efficiency when these newer techniques are considered?
- The method by which LinFusion generates ultra-high-resolution images is somewhat unclear. Can LinFusion directly generate 16K-resolution images, thereby avoiding patch-wise splitting, or does it produce a lower-resolution image that is later upsampled with techniques like SDEdit?
- Why does removing the patchification operation in DemoFusion in Table 5 (A -> B) increase the sampling speed? Since patchification typically reduces training and sampling costs, it seems counterintuitive.
- How the 25% of unremoved self-attention layers in PixArt-Sigma selected? Are they from shallow layers, deep layers or just randomly sampled? Can distillation twice alleviate this problem (e.g., replace 50% in the first time and train the model as described, followed by replacing the other half in the second time)? 
- Minor typo: In Table 3, it should read "Bi-Directional Mamba2 w/o Gating & RMS-Norm + Normalization."

### Questions
- Why does removing the patchification operation in DemoFusion in Table 5 (A -> B) increase the sampling speed? Since patchification typically reduces training and sampling costs, it seems counterintuitive.
- How the 25% of unremoved self-attention layers in PixArt-Sigma selected? Are they from shallow layers, deep layers or just randomly sampled? Can distillation twice alleviate this problem (e.g., replace 50% in the first time and train the model as described, followed by replacing the other half in the second time)? 
- Minor typo: In Table 3, it should read "Bi-Directional Mamba2 w/o Gating & RMS-Norm + Normalization."

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work introduces a generalized linear attention paradigm and extracts knowledge from Stable Diffusion to develop a distilled model called LinFusion. LinFusion avoids the quadratic increase in complexity associated with traditional attention mechanisms as the number of tokens grows, enabling the efficient generation of high-resolution visual content. Extensive experiments demonstrate that LinFusion achieves satisfactory and efficient zero-shot cross-resolution generation.

### Strengths
	Compared to the original SD-v1.5, LinFusion offers significant advantages in speed and GPU memory usage for generating high-resolution images.
	The extensive amount of open-sourcing and experiment reproducibility is greatly appreciated.

### Weaknesses
 	The comparison experiments in the paper are not comprehensive; for instance, the experimental section lacks an analysis of parameters and data size. 
	It is unclear whether LinFusion can outperform the latest lightweight diffusion methods, such as BK-SDM[1], on the COCO 256×256 30K dataset.
	In Table 7, LinFusion shows a significant decrease in FID scores. In contrast, LinFusion exhibits better compatibility with other components and pipelines of SD, which would be better to analyze why this occurs.
	The visual quality of the generated images does not seem particularly impressive.

### Questions
	Please address questions in "Weaknesses".

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
4

### Summary
This paper introduces a novel text-to-image model named LinFusion, addressing the challenge of generating high-resolution visual content with diffusion models. To optimize this, the authors propose to ultilize the popular linear attention and present methods for normalization-aware and non-causal operations, achieving performance on par with or even superior
to the original diffusion model while significantly reducing time and memory complexity. Experiments demonstrate that LinFusion achieves comparable or superior performance to the original Stable Diffusion on tasks like zero-shot cross-resolution generation, with excellent results on MS COCO.

### Strengths
- The paper presents an efficient text-to-image model, LinFusion, which innovatively addresses the computational inefficiencies inherent in high-resolution image generation with diffusion models.
- Two notable innovations of LinFusion are normalization-aware mamba and non-causal mamba, which significantly improving the model's performance.
- The authors have conducted an extensive set of experiments, demonstrating LinFusion's effectiveness across various resolutions and showcasing its superior capability in generating ultra-high-resolution images like 16K on a single GPU.
- The writing is clear and methodical, effectively guiding readers through the complex technical details while maintaining a focus on the practical implications of the research.
- The paper stands out for its thorough experimental validation, which not only benchmarks LinFusion against existing models but also integrates it with various components and pipelines, highlighting its versatility and compatibility in real-world applications.

### Weaknesses
 - While LinFusion demonstrates significant improvements in computational efficiency, mamba2 is designed for language models. Could you give more comparison with state-of-the-art linear attention methods[1,2,3] in computer vision.

- The results of the experiment are unconvincing. Could provide a more holistic assessment of LinFusion's performance across different aspects of image generation., such as HPSv2，T2I_Combench，DPG?

- Could the linear attention combined with the MM-DiT blocks，which are popular in state-of-the-art diffusion models，SD3 and FLUX?

- The training cost of this method is low. Is the training sufficient? Will longer training or increasing the training resolution (1k or 2k) further improve the model effect?

### Questions
Please referring to the Weaknesses above.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents a new method for efficient image generation in linear computation complex. To achieve this goal, a generalized linear attention paradigm is introduced. For training, they distill the knowledge from the pre-trained SD. This distilled LinFusion model achieves better or on-par performance than the original teacher. This model also enables many down-streaming plugins, which makes this paper far more interesting.

### Strengths
1. The usage of linear attention and network distillation is an interesting direction in efficient text-to-image generation.
2. Different Mamba architecture is considered and ablated, providing a reference for other related topics. 
3. This paper is well-written. The detailed experiments show the advantages of the proposed method and even some down-streaming plug-and-play applications.

### Weaknesses
My main concern about his paper is the experiments.

1. This paper introduces three loss functions, i.e., $\mathcal{L}_{simple}$.
  $\mathcal{L}{kd}$, $\mathcal{L}{feat}$ and two hyper-parameters ($\alpha$, $\beta$). However, there is no ablation study for each of them. The lack of ablation studies makes it difficult to understand the contribution of each loss term and the sensitivity of the model to the hyper-parameters. Specifically, it is unclear how the model's performance changes when each loss term is individually removed or when the hyper-parameters are varied across a reasonable range. This makes it hard to assess the robustness of the training process and the importance of each component.
2. Several down-streaming extensions (LoRA, ControlNet, etc.) have been evaluated. However, there is no further discussion of why the original network extensions work and why some of the results are better than the baseline and others are not. The paper does not provide any mechanistic explanation for why certain extensions perform better or worse than others. For example, it is not clear if the observed performance differences are due to the specific architecture of the extensions, the training procedure, or some other factors. A deeper analysis is needed to understand the interaction between the proposed LinFusion model and these extensions.

### Questions
1. What about the influences of each loss in the training objective?
2. In L512 - L516, LinFusion uses SDEdit tricks for higher-resolution generation, and comparing with DemoFusion. Is this comparison fair? LinFusion is a specific base model. A better comparison should be to use the same settings as DemoFusion.

### Soundness
3

### Presentation
3

### Contribution
4
