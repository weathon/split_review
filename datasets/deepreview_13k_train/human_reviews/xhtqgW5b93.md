# ToMA: Token Merging with Attention For Diffusion Models

- Decision: Reject
- Scores: 6, 3, 3, 6, 6

## Abstract
Diffusion models have emerged as leading models for image generation. 
Plug-and-play token merging techniques have recently been introduced to mitigate the heavy computation cost of transformer blocks in diffusion models. 
However, existing methods overlook two key factors: 1. they fail to incorporate modern efficient implementation of attention, so that, the overhead backfires the achieved algorithmic efficiency 2. the selection of token to merge ignores the relation among tokens, limiting the image quality. 
In this paper, we propose Token Merging with Attention(ToMA) with three major improvements. Firstly, we utilize a submodular-based token selection method to identify diverse tokens as merge destinations, representative of the entire token set. Secondly, we propose an attention merge, utilizing the efficient attention implementation, to perform the merge with negligible overhead. Also, we abstract the (un-)merging as (inverse-)linear transformations which also allows shareable transformation across layers/iterations. Finally, we utilize the image locality to further accelerate the computation by performing all the operations on tokens in local tiles.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents three significant advancements aimed at enhancing the token merging mechanism in diffusion models for generative tasks: identifying representative merge destinations, optimizing the merging and unmerging processes, and reducing computational complexity. Specifically, the proposed method employs a greedy-based algorithm to determine a representative subset that serves as merge destinations. This is followed by an additional cross-attention operation and matrix multiplication to effectively execute the merging process. During the unmerging phase, the authors leverage the inverse (or transpose) matrix from the merging step, thereby improving the overall efficiency of the unmerging procedure. Moreover, the authors introduce strategies to merge only tokens located within the same local region and to share destination and merge matrices across iterations and layers, further mitigating computational costs. When compared to an existing approach (i.e., ToMeSD), the proposed method achieves notable improvements in text-to-image generation tasks across two datasets (GEMRec and ImageNet-1k) evaluated using three metrics (CLIP, DINO, and FID), highlighting its efficacy and substantial contribution to the field.

### Strengths
- This paper is well-crafted and effectively articulates both the proposed methodology and the corresponding experimental outcomes.
- The implementation of the approach is methodical and straightforward, which supports practical applicability.
- The comprehensive implementation details, supplemented by the provided code, significantly bolster the reproducibility of the research.

### Weaknesses
 - The title and scope of the paper may lead to potential misunderstandings. While diffusion models have applications beyond generative tasks, the experiments in this work are solely focused on generation. It would be advisable to revise the title to more accurately reflect the scope of the contributions.
- The experimental evaluation is restricted to text-to-image tasks, which limits the generalizability and perceived practical impact of the proposed approach.
- The discussion and comparative analysis do not sufficiently engage with related work on token merging, such as CrossGET [1] and TRIPS [2], which diminishes the thoroughness of the literature review.
- The comparative evaluation is limited to ToMeSD, and there are notable inconsistencies when compared to the results reported in the original paper. Specifically, the reported inference time reduction in the original ToMeSD paper is not observed in the current work, even at higher compression rates.

### Questions
- There are numerous existing token merging approaches that extend beyond their application in diffusion models and generative tasks. The proposed method appears to function as a plug-and-play token merging technique. How does it perform when integrated with baseline models and discriminative tasks? Are the improvements consistently observed across these models and tasks?

- Could the authors provide more detailed information on the implementation of the tile-shaped regions?

- The submodular-based destination selection appears analogous to Farthest Point Sampling (FPS). To my understanding, in most 3D applications, the FPS algorithm is implemented with CUDA to achieve acceptable speed. This step seems to contribute significantly to the computational overhead of the proposed method. Could the authors clarify the distinctions between the submodular approach and FPS, particularly in terms of efficiency?

- In the original ToMeSD paper (applied in SD 1.5), the results indicate a reduction in inference time (s/img). However, in Table 1, even at higher compression rates (0.5 and 0.75), this reduction is not evident. Could the authors provide an explanation for this discrepancy?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
To address the two main challenges in token merging, this paper introduces the TOMA method. TOMA first uses a submodular-based approach to select diverse tokens for merging. It then leverages efficient attention implementations to minimize merge overhead. By abstracting (un-)merging as (inverse) linear transformations, TOMA enables shared computation across layers and further accelerates processing by operating on tokens within local blocks to exploit image locality.

### Strengths
1.	The method uses a submodular function to identify a representative subset of tokens for merging and applies a GPU-efficient vectorized optimization algorithm.
2.	The design of ToMA carefully considers the advantages and limitations of GPU computations.
3.	ToMA achieves 30%-50% speedups without noticeable sacrifice in image quality.

### Weaknesses
1. This work seems like an enhanced version of ToMeSD, focusing on updated merge rules and additional locality optimizations, but the contributions may not be substantial enough.
2. Regarding experimental results:
- The paper only tests on the SDXL architecture, limiting generalization claims. As noted in line 372, this method could be extended to SD2 and SD3, so more results on these structures are needed. Actually, using token merging in the DiT structure could theoretically offer greater speedups.
- The results in Table 1 for ToMeSD are strange, as its inference time is longer than the baseline. Were torch and xformer versions verified to match the official implementation during testing? Without a correct ToMeSD implementation, comparisons may lose significance.
- FID scores in Figure 5 exceed 25, unusually high for ImageNet.
- The speedup achieved by ToMA is limited. At a ratio of 0.25, the improvement is just 10%, and while a ratio of 0.75 yields a 20% speedup, it comes with a significant decline in quality metrics.
- The comparison methods are limited; it would be beneficial to include approaches such as “Token Downsampling for Efficient Generation of High-Resolution Images.”
3. Some figures and explanations are unclear, e.g., the X-axis in Figure 5.

### Questions
Please refer to the weaknesses part.

### Soundness
2

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
5

### Summary
This paper introduces Token Merge with Attention (ToMA) to optimize transformer-based diffusion models, addressing inefficiencies in existing token merging methods. By utilizing submodular optimization for token selection, efficient attention mechanisms, and leveraging token locality, ToMA achieves substantial computational speedups with minimal impact on image quality, making it compatible with modern GPU architectures.

### Strengths
1. The use of submodular optimization for token selection effectively reduces information loss during merging, improving quality retention compared to previous approaches.

2. The paper's experiments, which utilize metrics such as CLIP, DINO, and FID on high-quality datasets, demonstrate ToMA's balance between efficiency and image quality.

### Weaknesses
1. The use of locality to limit the scope of attention for computational efficiency, as implemented in ToMA, is not sufficiently novel. Similar approaches have already been explored in methods such as Sparse Transformer[1], DiffRate[2], ToFu (Token Fusion)[3], making it difficult to assess the unique contribution of ToMA.

2. The experimental comparisons are primarily limited to ToMeSD, without benchmarking against other prevalent methods such as Token Pruning, Flash Attention, DiffRate[2], ToFu[3], and FRDiff[4].

3. The paper is lack of qualitative visual analysis. Without sufficient visual examples, it is challenging to assess ToMA's performance meaningfully, especially in comparison to other acceleration methods.

### Questions
Refer to Weaknesses.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes Token Merge with Attention (ToMA) to tackle the issues of limited image quality due to the loss of important tokens and the inefficiency of attention mechanisms. The authors establish ToMA through three major components: a submodular-based token selection method, an efficient attention implementation, and (un-)merging as (inverse-)linear transformations. Based on this design, the paper significantly reduces the inference time for text-to-image generation model (SDXL).

### Strengths
This paper exhibits several strengths:

1.	The motivation and methodology are both reasonable and intuitive.

2.	The generation model (SDXL) is significantly accelerated by merging and unmerging tokens before and after attention, along with additional speed-up settings, all without any loss in quantitative performance indicators.

### Weaknesses
This paper exhibits several Weaknesses:

1.	Lack of qualitative comparison with ToMeSD.

2.	The visual effects of ToMA are underrepresented, and quantitative indicators only partially reflect the quality of generation. More samples are needed to substantiate claims about "the best trade-off between image quality and speed."

3.	Current Text-to-Image models (such as Flux and SD3) based on diffusion transformers have achieved new state-of-the-art results. While the paper states that ToMA can be applied to any attention-based T2I model, it is recommended that the authors verify ToMA's performance on the latest T2I models to enhance persuasiveness.

4.	In the bottom of Figure 6, ToMA introduces considerable noise compared to the original result. Does this imply that, despite ToMA showing less performance loss in quantitative evaluations, it incurs greater performance loss in terms of visual perception?

### Questions
1.	I noticed that in the smaller steps of Figure 4, the average token intersections across different layers are significantly different. In these steps, could the sharing of both destinations and attention weights between layers lead to a notable loss in performance?

2.	How is the scale of the set of destinations determined? Specifically, how does the size of 𝐷.

3.	The terms "Dino" and "Clip" mentioned in line 475 should be aligned with the entries in Table. 3.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
Previous token selection methods have overlooked the relationships between tokens and have not utilized the latest attention implementations, limiting actual speedup.
This paper proposes a submodular function-based token selection mechanism and introduces an attention-based approach for merging and unmerging tokens. This design leverages the benefits of modern attention acceleration libraries and is reversible in nature.
As a result, the authors' method achieves an optimal trade-off between performance and efficiency.

### Strengths
- The use of attention-based operations for token merging is well-designed and makes sense. Additionally, the authors' choice to make it an invertible function is highly meaningful, and they thoughtfully consider GPU implementations.

- The authors also discuss sharing destination selections across steps, which indeed reduces computational costs and enhances the practicality of the overall approach.

- The experiments are comprehensive and well-executed.

### Weaknesses
 - The manuscript lacks discussion on the DiT model, focusing only on Stable Diffusion. In the "Local Region" section, it would be beneficial to include insights on how this technology could be adapted for DiT-like models. Without convolution layers, it is unclear if the locality is still evident enough to support the use of this method. A more detailed analysis is needed to understand how the locality assumptions might change for DiT models, specifically considering the reliance on positional embeddings rather than convolutional receptive fields, and whether any modifications to the proposed method would be needed to accommodate those differences. For instance, how does the submodular function behave when the input features are primarily determined by positional encodings rather than local pixel relationships?

- Some figures could be improved for better visualization.e.g., it is a little difficult to differentiate different methods in Figure 5. The use of distinct colors, line styles, or markers could significantly improve the clarity of the plots, making it easier to compare the performance of different techniques. Additionally, providing error bars or confidence intervals would give a better sense of the statistical significance of the results.

- The manuscript contains redundant content, specifically in lines L142-L150 and L151-L155, where identical information is repeated. This repetition detracts from the overall clarity and conciseness of the paper and should be removed.

### Questions
My primary concern is the lack of discussion regarding the DiT model. Could the authors provide additional results or discussions specifically related to DiT image generation models, such as PixelArt-Alpha?

### Soundness
4

### Presentation
2

### Contribution
3
