# Dynamic Diffusion Transformer

- Decision: Accept
- Avg Score: 5.50
- Scores: 6, 8, 5, 3

## Abstract
Diffusion Transformer (DiT), an emerging diffusion model for image generation, has demonstrated superior performance but suffers from substantial computational costs. Our investigations reveal that these costs stem from the \emph{static} inference paradigm, which inevitably introduces redundant computation in certain \emph{diffusion timesteps} and \emph{spatial regions}. To address this inefficiency, we propose \textbf{Dy}namic \textbf{Di}ffusion \textbf{T}ransformer (DyDiT), an architecture that \emph{dynamically} adjusts its computation along both \emph{timestep} and \emph{spatial} dimensions during generation. Specifically, we introduce a \emph{Timestep-wise Dynamic Width} (TDW) approach that adapts model width conditioned on the generation timesteps. In addition, we design a \emph{Spatial-wise Dynamic Token} (SDT) strategy to avoid redundant computation at unnecessary spatial locations. Extensive experiments on various datasets and different-sized models verify the superiority of DyDiT. Notably, with <3\% additional fine-tuning iterations, our method reduces the FLOPs of DiT-XL by 51\%, accelerates generation by 1.73$\times$, and achieves a competitive FID score of 2.07 on ImageNet.%

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper introduces the Dynamic Diffusion Transformer (DyDiT), an architecture that dynamically allocates FLOPs to the most demanding areas based on varying timesteps and spatial locations. The paper begins by analyzing computational cost requirements across temporal and spatial dimensions, suggesting that a fixed architecture may be unnecessary during the sampling stage. To address this, it proposes the Timestep-wise Dynamic Width (TDW) mechanism and the Spatial-wise Dynamic Token (SDT) strategy, which can be seamlessly integrated with the attention and MLP blocks in a diffusion model. DyDiT initializes from pre-trained model weights and employs routers to dynamically determine which attention heads, groups, and spatial tokens to process. Extensive experiments demonstrate that DyDiT achieves comparable results to pre-trained diffusion models while adhering to predefined FLOP constraints.

### Strengths
- The motivation is sound and clearly presented, supported by a well-designed teaser figure.
- The proposed TDW and SDT mechanisms enable dynamic adjustment of model modules, and the FLOPs-constrained loss effectively -controls the desired FLOPs of the final model.
- Extensive experiments and thorough ablation studies validate the module's effectiveness.

### Weaknesses
 - It is unclear how the "pre-define" in L214 benefit the sampling stage? I understand that the activation of attention heads and groups is based solely on timesteps, allowing the masks to be precomputed once training is completed. However, tt seems impractical or inefficient to store all possible pre-defined structures, so it primarily saves computational costs on the attention routers. However, this cost doesn’t seem substantial—am I correct?
- The adaptation of the proposed modules to efficient samplers or to samplers with varying sampling steps remains unclear. Since the activation mask depends solely on the timestep t, different samplers using step t could yield the same activation mask, even though 
t might represent different stages of denoising (e.g., one sampler is at the beginning of denoising, while another is close to full denoising). I'm wondering the activation masks should be very different under this scenario right (just as shown in Fig. 5)?

### Questions
Please refer to the weaknesses.

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
4

### Summary
The paper introduces a new efficient architecture, Dynamic Diffusion Transformer (DyDiT), for diffusion-based image generation. The authors observe the redundancy of DiTs in processing small timesteps and unnecessary spatial regions. Accordingly, they propose two main modifications: the timestep-wise Dynamic Width (TDW) and the spatial-wise Dynamic Token (SDT). These two modules dynamically allocate proper computational resources for different timesteps and spatial regions. The method significantly reduces FLOPs and accelerates generation without sacrificing visual quality.

### Strengths
- This paper is easy to follow.
- The authors conduct sufficient ablation studies to evaluate the proposed modules.
- The authors conduct experiments on a wide range of datasets, including ImageNet, Food, Artbench, Cars, and Birds, and compare a lot of state-of-the-art diffusion backbones. The results show the effectiveness of the proposed method.
- The authors also perform experiments on text-to-image generation, demonstrating the plug-and-play nature of SDT and TDW.

### Weaknesses
 - The authors demonstrate the results of their method on PixArt-$α$, which is commendable. However, the acceleration achieved in this text-to-image model is inferior to that in class-to-image generation. A more in-depth analysis of this discrepancy would be valuable. Moreover, providing image samples generated by the accelerated text-to-image model could be helpful for the analysis.

- Providing the image samples generated by the diffusion models accelerated with **different** $\mathbf{\lambda}~$**s** could help understand the FLOPs-Quality trade-offs of the proposed method.

- In Figure 5, the first head is always activated across different timesteps. Is this head manually set or just a result of the learned strategy?

### Questions
please refer to the weakness.

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
- This paper proposes the Dynamic Diffusion Transformer, a model that dynamically adjusts both timesteps and spatial dimensions during the generation process to reduce computational costs. 
- In the temporal dimension, the model width is adaptively scaled; 
- in the spatial dimension, a dynamic token strategy with a token router is introduced to further reduce computation.

### Strengths
- The proposed approach reduces GFLOPs by 51% and achieves a 1.73x speed-up during training.
- Detailed ablation studies are presented to demonstrate the contribution of each component to overall performance.

### Weaknesses
 - The model appears to be somewhat incremental in its contributions. it trains multiple routers to selectively mask certain MHSA heads and MLP blocks.

- I recommend including some state-of-the-art models in Table 1, such as DiffiT [1], SiT [2], and DiMR [3], as these also introduce architectural innovations to the DiT model.

- Also, it would be beneficial to move the 512 result in supp into the main table (and also add other methods), as training speed is a more critical factor in larger-scale generation for the DiT model.

### Questions
Please see the weakness section for details.

Also, i suggest the author provides more implementation details, including training precision. For instance, Fast-DiT [4] has achieved a 95% increase in speed.

[4] https://github.com/chuanyangjin/fast-DiT

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The authors propose Dynamic Diffusion Transformer (DyDiT) that dynamically adjusts its computation along both timestep and spatial dimensions during generation to reduce computational redundancy. This method contains two key components including a Timestep-wise Dynamic Width (TDW) approach and a Spatial-wise Dynamic Token (SDT) strategy. TDW is motivated by the observation in the difference of loss curve between DiT-S and DiT-XL across various time step. SDT is inspired by loss map showing patch-wise difficulty of noise prediction. Extensive experiments are conducted to show the effectiveness of the proposed method. But I fail to see the code or pseudocode.

### Strengths
1. The paper is easy to follow and well-written with many figure to clearly illustrate the idea of the paper as well as the results.

2. The observation is interesting and the method is intuitive and effective.

3. The authors conduct extensive experiments on various datasets, such as ImageNet and Food dataset, and DiT variants like DiT-S and DiT-XL.

### Weaknesses
1. This method is built on a well-pretrained DiT model, which may restrict its application. Is this method applicable for training a DiT model from scratch? 

2. In Fig 3 and Appendix A 3, the comparison with other pruning methods may not be convincing. The authors is recommended to compare the proposed method with other dynamic methods such as repurposed ITOP [1], SViTE, and S2ViTE [2]. And why the authors do not provide the results of lambda over 0.7 in DiT-XL. 

3. It seems that the authors do not choose a consistent lambda value for studies, such as 0.4 in Table 9, 0.5 in Table 10, and 0.9 in Table 14. In other words, this hyperparameter is relatively sensitive to obtain satisfying results under different settings. It would be better to provide some suggestions about the selection of this hyperparameter.

4. The comparison of maintaining the same training iterations for models in Appendix B3 may be partially reasonable. In addition to comparing DyDiT with DiT, the authors should also compare DyDiT with a DiT variant that incorporates the same gating module as DyDiT in the same position, multiplies the module output with the original input, and then uses this weighted input as the final input. In this way, we may keep the same number of parameters and further show the effectiveness of the proposed method. 

5. Though the authors combine DyDiT with LCM (a 4-step model) to show the effectiveness of proposed method, inevitably LCM is contradictory with the motivation of DyDiT because DyDiT, especially the TDW, is inspired by the observation in a 250-step model. I speculate SDT may play a dominant role. In a nutsheel, this method may have a weak influence to those 1-step, 2-step, or 4-step models like LCM.

### Questions
1. Why there is a significant performance drop when using SDT only (II). Could the authors provide a detailed explanation?

2. How about using layer-skip only in Table 3 III (layer-skip), i.e., removing TDW? 

3. Could the authors provide a detailed description about how to obtain the results in Fig 6.

4. Why the authors use 100 DDPM in Table 12 instead of 250 like DiT. How about the results using 250 DDPM?

5. For other questions, please see weakness.

Minor issue: Line954 our-> Our

### Soundness
2

### Presentation
3

### Contribution
2
