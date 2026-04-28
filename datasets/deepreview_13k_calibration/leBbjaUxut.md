# Multi-Scale Image Diffusion Transformers: Explainability Leads to Faster Training

- Decision: Reject
- Avg Score: 5.00
- Scores: 3, 3, 6, 8

## Abstract
Diffusion models have significantly advanced image synthesis but often face high computational demands and slow convergence rates during training. To tackle these challenges, we propose the Multi-Scale Diffusion Transformer (MDiT), which incorporates heterogeneous, asymmetric, scale-specific transformer blocks to reintroduce explicit inductive structural biases into diffusion transformers (DiTs). Using explainable AI techniques, we demonstrate that DiTs inherently learn these biases, exhibiting distinct encode-decode behaviors, effectively functioning as semantic autoencoders. Our optimized MDiT architecture leverages this understanding to achieve a $\ge 3\times$ increase in convergence speed on FFHQ-256x256 and ImageNet-256x256, culminating in a $7\times$ training speedup on ImageNet compared with state-of-the-art models. This acceleration significantly reduces the computational requirements for training, measured in FLOPs, enabling more efficient resource use and enhancing performance on  smaller datasets. Additionally, we develop a variance matching regularization technique to correct sample variance discrepancies which can occur in latent diffusion models, enhancing image contrast and vibrancy, and further accelerating convergence.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes a multitude of modifications to diffusion models for image generation that are based on vision transformers.  A primary focus is on architectural details of the transformer network which is being trained to denoise.  A combined result of these modifications is faster training for similar generation quality in comparison to baseline diffusion models.

### Strengths
Explores many design choices inherent in diffusion transformers, including both model architecture and regularization.

Extensive experiments, including thorough documentation in the appendix, quantify the consequences of the proposed changes.

The cumulative result of the many modifications is faster training and faster inference (fewer sampling steps) for similar quality image generation (measured by FID on ImageNet) as recently published diffusion-based image generators.

### Weaknesses
The many tweaks to model architecture and regularization seem to be individually minor and not obviously related to each other.  These tweaks include: patch resolution (1x1 vs 2x2 embedding), time embedding as a token, cross-attention for class conditioning, rotary positional embeddings, layer normalization on Q and K vectors, number of attention heads, and a variance-matching regularization term in the loss.  While the paper provides individual justifications for these design elements, there is an absence of high-level motivating principles to explain them.  The different tweaks are not obviously related, giving the impression that the chosen collection of changes may be akin to a product of architecture search.

There appears to be a disconnect between the analysis and the claims of explainability put forth in the title and introduction.  It is unclear why this architecture is any more or less explainable than existing transformer-based diffusion models.  While Section 4 presents a story about explainability based on probing network behavior, it is unclear whether this post-hoc analysis yields any predictive power or is a heuristic that supports confirmation bias.

In terms of presentation, the main text needs to better communicate what impact each architecture design decision has on the overall system (both in isolation and, if there are dependencies, in combination with others).  Perhaps these messages are buried in the 28 pages of appendices with additional text, tables, and figures.  However, it is not presented in an accessible manner in the main paper, reinforcing the impression that results stem from a collection of engineering tweaks, rather than fundamental insights.

### Questions
Is there a coherent motivation connecting the many proposed architectural changes?  How large of a design space was explored to arrive at the chosen configuration?  Do the claims regarding explainability yield any predictive power in terms of model behavior or design trade-offs (and if so, can you provide experimental validation)?

---

Post-rebuttal: As explained in the discussion below, the author response does not resolve my concerns.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces the Multi-Scale Diffusion Transformer (MDiT), which integrates diverse, scale-specific transformer blocks into diffusion models to incorporate structural biases and enhance encoding-decoding behavior, akin to semantic autoencoders. The MDiT significantly speeds up training—up to 7x faster on ImageNet datasets—while improving image vibrancy and contrast, and reducing computational demands and memory use in image synthesis tasks.

### Strengths
1. The proposed MDiT has a significant speed improvement compared with the original DiT.

2. The paper incorprates many recent advencements of LLMs into diffusion transformers, yielding improved performance.

### Weaknesses
1. Some core contributions are overclaimed. For example, the new components like ROPE and GLU were initially introduced in large language models (LLMs). While these modules have been adopted in many recent visual models and show superior performances, MDiT is not the first to incorporate them, so its architectural design does not provide too many innovations. Also, although the paper emphasizes its processing of image features in the full latent space, the core component of the model, self-attention, actually receives downsampled representations, that is, the features only enter the attention layer after passing through pixel-shuffle as shown in equation (1).

2. The motivation of the paper is not sufficiently substantiated. DiT originally replaced the common UNet structure in latent diffusion models with plain Transformers, which, at higher image resolutions, leads to increased computation but also improves performance and scalability. This paper attempts to revert DiT back to a U-shaped structure, but no substantial benefits have been observed.

3. Important ablation studies are missing: the authors have not provided a clear ablation to show where their performance improvements come from. For instance, it is unclear which part of the model—Llama-like components or the new structural design—has a greater impact on performance.

4. Minor comments: the paper is not very easy to understand, with many details of the model described overly concise in Section 3.

### Questions
-- update after rebuttal --

I have carefully read other reviewers' comments as well as the authors' rebuttal. The current version of the paper still cannot convince me to give an accept. As the authors claimed, the LLM-like components are not the innovation of the paper and they foucs on hierarchical designs for Diffusion Transformers. However, the authors did not provide sufficient reasons for me to accept the view that a hierarchical structure is superior to a plain structure. In fact, latent diffusion originally utilized a hierarchical UNet, while DiT transformed it into a plain structure and discovered better scalability. This paper seems to discuss a "Revenge of UNet" concept, but there's nothing novel about the model's approach; it merely combines some recent tricks. I am not surprised that the method proposed in this paper can outperform DiT in certain scenarios, as hierarchical models are often easier to train and converge, which is true for both visual understanding and generative tasks. However, the biggest issue with the U-shape architecture is that it is difficult to scale up (e.g., in terms of parameters) and inconvenient to integrate into multiple modalities, which I consider more crucial in designing architecture. Therefore, based on my unresolved concerns, I maintain my original score.

### Soundness
2

### Presentation
2

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
The paper proposes a novel method called the Multi-Scale Diffusion Transformer (MDiT), which aims to address the challenges of high computational demands and slow convergence rates in diffusion models for image synthesis. MDiT incorporates a heterogeneous, asymmetric, scale-specific transformer block design that leverages inductive biases to improve training efficiency. The paper demonstrates that by reintroducing structural biases, the MDiT can achieve a significant increase in convergence speed on FFHQ-256x256 and ImageNet-256x256, with a notable reduction in computational requirements. Additionally, the paper introduces a variance matching regularization technique to enhance image quality and further accelerate convergence.

I have read the response of the authors and the comments of other reviewers. I would keep my original score.

### Strengths
1. MDiT achieves faster training times and reduces computational costs, which leverages distinct transformer blocks for image feature processing.
2. This paper introduces explainable AI techniques to understand and optimize the process of diffusion transformers.
3. This paper also proposes a variance matching regularization module  to correct sample variance discrepancies.

### Weaknesses
1. What are the specific contributions of each architectural choice (e.g., partial head Rotary Positional Embeddings, Aggregate Blocks) to the overall performance? It's unclear how much each component contributes independently to the reported improvements in convergence speed and image quality. For example, do the partial head Rotary Positional Embeddings primarily affect high-frequency details, while the Aggregate Blocks focus on mid-level structural features? A more granular analysis of each component's impact is needed.
2. This paper shows a lot of visualization generation results. Are there any failure cases? While the presented samples look promising, it is crucial to understand the limitations of the method. Are there specific types of images or scenarios where the model struggles? For instance, does the model have difficulty with complex textures, unusual object poses, or specific color distributions? The absence of failure cases raises concerns about the completeness of the evaluation.
3. How does the MDiT architecture scale with increasing model size, and can it be flexibly adapted to different image resolutions and datasets? The paper lacks a thorough investigation into the scalability of the proposed architecture. It's important to know if the performance gains are maintained when the model is scaled up in terms of parameters or when applied to higher-resolution images. Furthermore, the ability to adapt to different datasets without significant architectural changes is crucial for practical applications. The paper should provide more information on these aspects.

### Questions
For details, please see weaknesses.

### Soundness
3

### Presentation
3

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
This paper proposes the Multi-Scale Diffusion Transformer (MDiT), a novel architecture that introduces heterogeneous, asymmetric, scale-specific transformer blocks to diffusion transformers (DiTs) for image synthesis. MDiT addresses the slow convergence issues in traditional DiTs by reintroducing inductive biases typically found in convolutional models, such as multi-scale features and translation invariance, to accelerate training. Using explainability techniques, the authors analyze MDiT’s architectural behavior, showing it functions like a semantic autoencoder, learning image structures more effectively and speeding up training by up to 7x compared to state-of-the-art models. Additionally, a variance matching regularization method is introduced to correct discrepancies in sample variance, enhancing image quality and further accelerating convergence.

### Strengths
- This paper is well-written and easy to follow. 
- The proposed architecture is novel. By integrating heterogeneous, multi-scale transformer blocks, MDiT adds flexibility and specificity to DiTs.
- The variance matching regularization reduces discrepancies in variance for latent diffusion models, leading to enhanced image contrast and vibrancy.
- The efficiency of the proposed model is remarkable.

### Weaknesses
Overall the paper is great! A few minor weaknesses include: 
- The MDiT is a little complex, with multiple configurations. This makes it challenging to find the optimal config. 
- MDiT particularly focuses on DiT architecture. Are some of the techniques also applicable to UNet-based architecture? 
- While MDiT shows promising results on FFHQ and ImageNet, additional tests on diverse and large-scale benchmarks are encouraged.

### Questions
This paper includes a comprehensive evaluation of different prospects. No further questions were raised from me.

### Soundness
3

### Presentation
4

### Contribution
3
