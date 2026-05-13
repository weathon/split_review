# Qihoo-T2X: An Efficient Proxy-Tokenized Diffusion Transformer for Text-to-Any-Task

- Decision: Accept
- Scores: 6, 6, 6, 6, 8

## Abstract
The global self-attention mechanism in diffusion transformers involves redundant computation due to the sparse and redundant nature of visual information, and the attention map of tokens within a spatial window shows significant similarity.
To address this redundancy, we propose the \textbf{P}roxy-\textbf{T}okenized \textbf{D}iffusion \textbf{T}ransformer (\textbf{PT-DiT}), which employs sparse representative token attention (where the number of representative tokens is much smaller than the total number of tokens) to model global visual information efficiently.
Specifically, within each transformer block, we compute an averaging token from each spatial-temporal window to serve as a proxy token for that region.
The global semantics are captured through the self-attention of these proxy tokens and then injected into all latent tokens via cross-attention. 
Simultaneously, we introduce window and shift window attention to address the limitations in detail modeling caused by the sparse attention mechanism.
Building on the well-designed PT-DiT, we further develop the \textbf{Qihoo-T2X} family, which includes a variety of models for T2I, T2V, and T2MV tasks.
Experimental results show that PT-DiT achieves competitive performance while reducing the computational complexity in both image and video generation tasks (e.g., a 49\% reduction compared to DiT and a 34\% reduction compared to PixArt-$\alpha$). The visual exhibition of Qihoo-T2X is available at \url{https://360cvgroup.io/Qihoo-T2X/}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes Proxy-Tokenized Diffusion Transformer to reduce the computational complexity. By utilizing sparse representative token attention, window and shift window attention, the proposed method effectively reduces redundancy in global self-attention computation and optimizes the modeling process of visual information. Also, the Qihoo-T2X family includes multiple models for text to image, text to video, and text to multi view tasks. However, it is difficult to fully demonstrate the effectiveness of the method at various resolutions in the experimental section.

### Strengths
The proposed method significantly reduces computational complexity and has certain competitiveness in various tasks, such as T2I, T2V,and T2MV.

### Weaknesses
1) Insufficient experiments and lack of comparative experiments at high resolution.
2)     How is the value of compression ratio determined, and is it related to both semantic information and resolution size?

### Questions
See weakness.

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
This paper introduces a proxy-tokenized mechanism for transformer-based diffusion models (e.g., DiT), utilizing sparse representative tokens to alleviate redundant computations arising from inherent visual redundancy. Specifically, the authors observe that tokens representing spatially proximate regions tend to exhibit high similarity, while tokens corresponding to spatially distant regions contribute less to meaningful computation in the attention map. Leveraging this insight, the authors propose the use of a proxy token for each window by averaging the tokens within it and subsequently employing self-attention and cross-attention operations involving both proxy tokens and original tokens to ensure efficient interaction across all tokens. Furthermore, the proposed approach integrates a Swin-based architecture to implement efficient attention mechanisms in accordance with these observations. The method achieves competitive performance compared to state-of-the-art approaches across three tasks—text-to-image, text-to-video, and text-to-multiview—at varying resolutions, underscoring its effectiveness and significance within the field.

### Strengths
- The paper is well-crafted, providing a clear exposition of the proposed methodology.
- The approach is conceptually straightforward and highly intuitive.
- The motivation and objectives are innovative, focusing on a token-efficient mechanism for DiT-based generative models, which is particularly significant given the paucity of existing approaches for DiT-based models.

### Weaknesses
 - The lack of ablation studies assessing performance metrics, such as FID with respect to GFLOPs, diminishes the practical relevance of the proposed methodology.
- The discussion and comparison do not sufficiently address related works on token merging (e.g., ToMe [1], ToMeSD [2], CrossGET [3], and TRIPS [4]), which limits the comprehensiveness of the literature review.
- The proposed method integrates a Swin-based architecture within the DiT-based model, employing a straightforward average operation to represent tokens. From the perspective of novelty, this contribution appears to be incremental.

### Questions
- Although the authors provide extensive comparisons between resolution and computational metrics (e.g., memory usage, GFLOPs), I believe that additional comparisons between performance and computational cost relative to other approaches in text-to-image and text-to-multiview tasks are necessary. Assessing the trade-off between performance and computational efficiency, rather than focusing solely on resolution, would offer a more comprehensive evaluation of the proposed method's effectiveness. Since identical resolutions do not inherently guarantee equivalent performance, it is conceivable that approximate methods may result in some performance degradation.

- Several prior works, such as ToMe, ToMeSD, TRIPS, and CrossGET, have also addressed token merging. The absence of a detailed discussion or comparison with these existing studies undermines the claimed novelty of Qihoo-T2X. I suggest that the authors more explicitly delineate the unique contributions and advantages of their approach in relation to these established methods.

### Soundness
2

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
3

### Summary
The paper introduces an efficient Proxy-Tokenized Diffusion Transformer (PT-DiT) for accelerating self-attention mechanism, addressing the redundancy in global self-attention mechanisms of diffusion transformers. It develops Qihoo-T2X family for text-to-any-task applications. PT-DiT uses sparse representative token attention, computing an averaging token from each spatial-temporal window as a proxy, reducing computational complexity. It includes window and shift window attention to enhance detail modeling. The Qihoo-T2X family, which includes models for T2I, T2V, and T2MV tasks, shows competitive performance with reduced computational complexity in image and video generation tasks.

### Strengths
1. The PT-DiT addresses the redundancy in global self-attention by using sparse representative token attention, reducing computational complexity.

2. The introduction of window and shift window attention mechanisms helps to capture fine details and textures, improving the quality of generated images and videos.

3. The method is designed to be adaptable to both image and video generation tasks without structural adjustments, demonstrating competitive performance compared to original models and great flexibility in application

4. This method is simple and effective.

5. This paper is well written.

### Weaknesses
 - Insufficent performance comparison to peer methods such as DAM [1] and AgentAttention [2]. While PT-DiT significantly outperforms baselines, its performance relative to peer methods like DAM and AgentAttention is not clearly superior (see Figure 8). Need more comparison.
- **Need further discussion on the relation and differences to previous methods.**
    - For example, DAM **also finds significant attention map redundancy** by analyzing the Divergence Score and proposes a set of Attention Mediator Tokens. These tokens can also **be seen as a kind of extractor** for extracting information from the original latent codes (Queries and Keys).
    - From this perspective, **based on DAM, PT-DiT only points out that redundancy in attention maps remains due to spatial reasons**, and the proposed average operation and sparse representative token attention may be implicitly included by the interaction between the original Queries/Keys and the Attention Mediator Tokens in DAM.
    - Additionally, PT-DiT doesn't analyze the significance of the observed phenomenon across different denoising timesteps, as DAM does.
- From the ablation study in Table 2(a), the results show that without TCM (an auxiliary module), the performance drops significantly, whereas without GIIM, which is the core component proposed in the paper, the performance decline is much less. Does this imply that auxiliary module TCM is more important than core module GIIM?
- A statistical comparison between Qihoo-T2V with and without PT-DiT is necessary for clearer insights into the model's impact.

### Questions
See weaknesses.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper introduces the Qihoo-T2X series, featuring the Proxy-Tokenized Diffusion Transformer (PT-DiT) for efficient text-to-video generation. PT-DiT uses proxy-tokenized attention to reduce computational redundancy by selecting representative tokens within spatial-temporal windows, enhancing global information capture without the high complexity of full self-attention. This design integrates global semantics efficiently through sparse proxy tokens and refines texture details using window and shifted-window attention, similar to the Swin Transformer. The Qihoo-T2X family demonstrates competitive performance with reduced complexity compared to models like DiT and PixArt-α.

### Strengths
- The paper is well-written and easy to follow. 
- The visualizations are promising. 
- Compared with SOTA methods, the model can achieve a similar level of performance with less training data. Meanwhile, the inference cost is much lower.

### Weaknesses
 - The method section is not clear enough. The mechanisms of window attention and shifting window attention are still not clear.  
- The task of T2MV is a little strange. What would be an application scenario for that task?  
- The "text-to-any-task" is overclaimed. The focused three tasks are essentially video generation (with a single frame or multi-view video).  

See the next question sections for more details.

### Questions
About method section: 
-  l201-203, f, h, w are not the actual frame, height, and width of the video/image, but the latent, right? Also, for images, how does the 3D VAE, with temporal downampling layers, handle them? 
- the texts from l242 to l244 are confusing, $(p_f \cdot p_f, p_h)$ should be ($p_f, p_h, p_w$)? so we have $p_h = p_w$ = <some value depends on resolution> and $p_f$ = 1 for image and $p_f$ = 4 for videos, right?
- Details for the window attention and shifting window attention are missing. Only Figure 4 shows some fundamental ideas of them but how do they work exactly? How does the shifting window work?

About T2MV: 
- Why Text-to-MV task is interesting? At the training level, there is no difference from this task to Text-to-video unless the training data; while for real practice, it's hard to control the generated content from only texts without any reference image. 
- It's hard to evaluate the performance of T2V-MV. Can the T2V-MV work for out-of-distribution prompts? And how about the visual and quantitative evaluations with other models, given that the task setting is following previous approaches? 

Other questions:
- The page limit is 10, no need to move related work to the appendix. 
- Can we use a VAE with a higher compression ratio, or a large patch embedding to achieve a similar level of efficiency? In principle, with the proposed design, more details could be restored compared with directly using a higher compression ratio (but with vanilla attention). It would also be great to show that.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper first highlights the computational redundancy issue of global self-attention in diffusion transformers, stemming from sparse visual information, through an analysis of the attention map. To tackle this problem, the authors propose the Proxy-tokenized Diffusion Transformer (PT-DiT), which substitutes the global self-attention of the vanilla DiT with Global Information Interaction Module (GIIM) and Texture Complement Module (TCM), enabling efficient modeling of both global and local visual information. In experiments, PT-DiT demonstrates theoretical and experimental advantages in computational complexity and shows competitive performance across various tasks, including T2I, T2V, and T2MV, underscoring its generalization capabilities.

### Strengths
-The motivation for reducing the training and inference costs of DiT by minimizing redundant computation in global self-attention is clear.

-The GIIM and TCM design in PT-DiT is promising and straightforward to implement.

-Qualitative and quantitative experiments on a variety of tasks (e.g., Text-to-Image, Text-to-Video, and Text-to-MultiView) are comprehensive and convincing.

### Weaknesses
 -This article lacks results on ImageNet for a fair comparison with existing state-of-the-art diffusion transformer models. Previous studies, such as DiT, MDT, VAR, and SiT, have all been evaluated on ImageNet using metrics like FID and IS. To fully establish its effectiveness, PT-DiT should also be assessed under similar conditions. This is essential for demonstrating its competitive performance despite reduced computational complexity and should be included in evaluations.

-How is the hyper-parameter compression ratio determined in this paper? Why is the compressed ratios set to (1, 2, 2) at a resolution of 256, and will a ratio of (1, 16, 16) result in excessive information loss at a resolution of 1024? The authors should provide further clarification on the rationale and motivations behind the chosen compressed ratios settings in their methodology.

-The extraction of proxy tokens through averaging is straightforward, but how representative are these proxy tokens when obtained in this manner? Could proxy tokens also be extracted using clustering or similarity-based methods for potentially improved representativeness?

### Questions
-What accounts for PT-DiT's 80% improvement over Lumina in Figure 8 (left), especially since this enhancement is significantly greater than the improvements observed for other models?

-How about the training time and inference time of PT-DiT?

-Does the author have any plans to open source the Qihoo-T2X series of models and code?

### Soundness
3

### Presentation
3

### Contribution
4
