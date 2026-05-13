# HarmoniCa: Harmonizing Training and Inference for Better Feature Cache in Diffusion Transformer Acceleration

- Decision: Reject
- Scores: 6, 6, 5, 8

## Abstract
Diffusion Transformers (DiTs) have gained prominence for outstanding scalability and extraordinary performance in generative tasks. However, their considerable inference costs impede practical deployment. The feature cache mechanism, which involves storing and retrieving redundant computations across timesteps, holds promise for reducing per-step inference time in diffusion models. Most existing caching methods for DiT are manually designed. Although the learning-based approach attempts to optimize strategies adaptively, it suffers from discrepancies between training and inference, which hampers both the performance and acceleration ratio. 
Upon detailed analysis, we pinpoint that these discrepancies primarily stem from two aspects: (1) \textit{Prior Timestep Disregard}, where training ignores the effect of cache usage at earlier timesteps, and (2) \textit{Objective Mismatch}, where the training target (align predicted noise in each timestep) deviates from the goal of inference (generate the high-quality image). To alleviate these discrepancies, we propose \textbf{HarmoniCa}, a novel method that \textbf{Harmoni}zes training and inference with a novel learning-based \textbf{Ca}ching framework built upon \textit{Step-Wise Denoising Training} (SDT) and \textit{Image Error Proxy-Guided Objective} (IEPO). Compared to the traditional training paradigm, the newly proposed SDT maintains the continuity of the denoising process, enabling the model to leverage information from prior timesteps during training, similar to the way it operates during inference. Furthermore, we design IEPO, which integrates an efficient proxy mechanism to approximate the final image error caused by reusing the cached feature. Therefore, IEPO helps balance final image quality and cache utilization, resolving the issue of training that only considers the impact of cache usage on the predicted output at each timestep. Extensive experiments on class-conditional and text-to-image (T2I) tasks for 7 models and 4 samplers with resolutions ranging from $256\times256$ to $2048\times2048$ demonstrate the exceptional performance and speedup capabilities of our HarmoniCa. For example, HarmoniCa is the first feature cache method applied to the 20-step \textsc{PixArt}-$\alpha$ $1024\times1024$ that achieves over 1.5$\times$ speedup in latency with an improved FID compared to the non-accelerated model. Remarkably, HarmoniCa requires no image data during training and reduces about 25\% of training time compared to the existing learning-based approach.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a new framework, HarmoniCa, which is a learning-based cache mechanism. The authors discover two main issues with previous methods: prior timestep disregard and objective mismatch. Step-wise Denoising Training (SDT) and Image Error-Aware Optimization Objective (IEPO) are proposed to address these two issues. Experiments show that the proposed framework can achieve a better performance and efficiency with lower training costs.

### Strengths
1. This paper is clearly written and easy to follow, presenting a new learning-based Caching framework that can address the two discrepancies between training and inference identified by the authors.
2. Extensive experiments on different models manifest the efficacy and universality of HarmoniCa with much lower training costs.

### Weaknesses
1. This paper lacks experimental comparisons with other cache-based methods, such as DeepCache [R1] and Faster Diffusion [R2].
2. A performance comparison with other related methods under the same acceleration ratio, such as pruning or quantization, should be provided for further validation.

### Questions
The questions are similar to those mentioned in weaknesses.

1. Can the authors provide more comprehensive comparison results with other cache-based models?
2. What are the comparative results of other related methods under the same acceleration ratio?

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
3

### Summary
This paper introduces Harmonica, a learning-based caching method that accelerates the sampling of the diffusion model by reusing the neural network features. Harmonica improves the training algorithm and training objective for the learnable router, building upon the Learning-to-cache framework. Extensive experiments on ImageNet and MS-COCO demonstrate the sampling efficiency of Harmonica across different models and resolutions.

### Strengths
1. The proposed method, Harmonica, is clean and effective with strong empirical performance. 
2. Harmonica eliminates the need for external datasets, unlike the existing learning-based method.
3. Demonstrates practical benefits across different architectures and scales. 
4. Comprehensive ablation study.

### Weaknesses
1. Harmonica introduces additional hyperparameters, such as the coefficient $ \beta$ and update interval $ C$, which require more computation to tune. While this additional offline cost does not affect the inference speedup, the paper should still provide the cost spent on tuning the hyperparameters to help readers better understand the full implementation costs. Specifically, the paper lacks details on the search space for these parameters, the sensitivity of performance to different values, and the computational resources required for the tuning process. Without this information, it is difficult to assess the practical overhead of implementing Harmonica.
2. Overall, the writing could be largely improved by breaking the long sentences into shorter ones. Here are some typos I caught :
	1. Line 127, "much lower training costs" -> "much lower training cost".
	2. Line 213, "Harmonize" -> "harmonize".
	3. Line 261, "The student" -> "the student".
	4. The second DiT block of the bottom row has the same format as Teacher DiT in Figure 4 (b).
3. Terminology: "discrepancy" could be replaced with "mismatch" (as used in line 237) for better accuracy as discrepancy often refers to a lack of similarity between quantities.

### Questions
1. The authors explore different standard metrics for $\lambda (t)$, but none are designed for natural images. Would perceptual metrics like LPIPS be more effective in measuring image similarity? 
2. Why is $\lambda (t)$ designed to be multiplied with $L_{MSE}$ ? Are there any other alternative design choices there? 
3. Can the router trained with one diffusion sampler be applied to a different diffusion sampler? For example, the training uses a DDIM sampler, but the sampling uses a DPM solver. 
4. Implementation details: 
	1. Is $r_{t,i}$ implemented as an output of sigmoid function following Learning-to-Cache? 
	2. Is $r_{r,i}$ updated using the vanilla gradient descent or other optimizers? 
	3. Does Harmonica apply the stop gradient to `gen_proxy`? In other words, $\lambda (t)$ is an adaptive weight of $L_{MSE}$.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces HarmoniCa, a learnable caching method designed for the Diffusion Transformer architecture. It primarily addresses the issues of Prior Timestep Disregard and Objective Mismatch found in previous learnable caching methods.

### Strengths
1.	This paper identifies issues of Prior Timestep Disregard and Objective Mismatch in current learning-based feature caching methods and proposes SDT and IEPO to address them, respectively.
2.	Experiments on the DiT-XL/2, PixART-α, and PIXART-Σ families, including eight models, four samplers, and four resolutions, demonstrate the effectiveness and generality of harmonica.
3.	The paper is well organized and clearly presented.

### Weaknesses
1. This work appears to be an incremental improvement on Learn-to-Cache, which initially made caching mechanisms learnable. The main contribution here is refining the learning mechanism of Learn-to-Cache. However, in terms of both efficiency and generation metrics, HarmoniCa shows only limited improvements. The core idea of making caching learnable was already established, and this paper focuses on fine-tuning the training process. The gains in performance, while present, do not appear to be substantial enough to warrant the complexity of a new training paradigm.
2. In Table 2, HarmoniCa’s results are only slightly better than those of Learn-to-Cache. In Table 3, under similar latency and computational requirements, HarmoniCa’s generation metrics are nearly the same as those of SA-Solver, a method that requires no training. Thus, the need for training in HarmoniCa does not offer a clear advantage, with similar observations across other solvers. The marginal improvements in FID and IS scores compared to Learn-to-Cache, especially when considering the added training overhead, raise questions about the practical utility of HarmoniCa. Furthermore, the fact that a non-trainable method like SA-Solver achieves comparable results under similar constraints further diminishes the appeal of the proposed approach.

### Questions
Please refer to the weaknesses part.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
1

### Summary
The paper titled "HarmoniCa: Harmonizing Training and Inference for Better Feature Cache in Diffusion Transformer Acceleration" proposes a method to enhance the efficiency of Diffusion Transformers (DiTs) in generative models by harmonizing the training and inference phases. DiTs, while powerful in generative tasks, face high inference costs due to redundant computations. HarmoniCa addresses this through a novel feature caching framework that includes two key components:

1. **Step-Wise Denoising Training (SDT)**: This component aligns the training process with the inference phase by maintaining continuity in the denoising trajectory, allowing the model to effectively reuse cached features across timesteps, as it would in inference.
   
2. **Image Error Proxy-Guided Objective (IEPO)**: IEPO incorporates a proxy mechanism that approximates the final image error caused by cached feature reuse. This helps balance image quality with efficient cache usage, bridging the gap between training objectives and inference goals.

The paper demonstrates that HarmoniCa significantly reduces training time (by around 25%) and achieves faster inference with improved image quality compared to non-cached and traditional learning-based methods. Through extensive experiments, HarmoniCa shows promising speedup ratios and better performance across multiple models and resolutions, highlighting its effectiveness and applicability in high-resolution generative tasks.

### Strengths
### Strengths of the Paper

The paper, "HarmoniCa: Harmonizing Training and Inference for Better Feature Cache in Diffusion Transformer Acceleration," offers a robust contribution to optimizing Diffusion Transformers (DiTs) for generative tasks through innovative feature caching techniques. Below, I evaluate the paper’s strengths across originality, quality, clarity, and significance.

---


The HarmoniCa framework addresses longstanding challenges in generative model efficiency by rethinking the training-inference dichotomy in Diffusion Transformers. This originality stems from its introduction of **Step-Wise Denoising Training (SDT)** and the **Image Error Proxy-Guided Objective (IEPO)**, both of which directly tackle the inefficiencies introduced by common feature caching methods. HarmoniCa’s approach to caching involves harmonizing the training and inference phases rather than optimizing each separately. This unique alignment of caching goals across both phases is not only original but also has substantial implications for generative model performance.
HarmoniCa’s emphasis on bridging the gap between training and inference caching, specifically addressing **Prior Timestep Disregard** and **Objective Mismatch**, reframes typical caching strategies by focusing on end-to-end generative quality. The **IEPO** component, which approximates final image error using a proxy, is a novel way to reconcile training objectives with final image quality, enabling more practical feature reuse in diffusion models.

---
The paper’s methodological rigor is evident in its clear experimental protocols and validation against state-of-the-art methods. The authors provide comprehensive experiments across multiple high-resolution models and resolutions, including **class-conditional** and **text-to-image (T2I)** tasks. HarmoniCa’s performance gains (e.g., 1.5× speedup with no significant loss in image quality) underscore the quality of the proposed solution. Additionally, the experiments carefully balance different cache utilization ratios (CUR), demonstrating HarmoniCa’s adaptability to varying model requirements. Extensive comparisons with current methods like **Learning-to-Cache** and **FORA** show that HarmoniCa consistently improves upon existing feature cache methods, providing concrete evidence for its efficacy and robustness. The inclusion of detailed **ablation studies** on the impact of IEPO and SDT further reinforces the work’s quality. These studies examine the effects of cache ratios, loss coefficients, and proxy metrics, showcasing a thorough understanding of the parameters that influence HarmoniCa’s success.

---
The paper is well-organized, with each section systematically addressing a specific aspect of the proposed solution: **Introduction and Background** sections clearly frame the limitations of existing methods, paving the way for the presentation of HarmoniCa as a targeted solution. **Methodology** is presented with sufficient depth, balancing detailed technical explanations and visual aids. For instance, **Figure 3** and **Figure 4** effectively illustrate how SDT and IEPO integrate into the DiT framework, making the mechanisms of HarmoniCa accessible even to readers less familiar with diffusion model architectures. **Algorithmic Details**: The paper includes equations and structured pseudo-code, enhancing reproducibility and understanding of HarmoniCa’s inner workings.  the authors provide context for critical terms (e.g., CUR, SDT), allowing readers to grasp the innovative elements without requiring extensive prior knowledge in feature caching.

---
The HarmoniCa framework represents a substantial step forward in making high-resolution generative models more practical by **lowering inference and training costs**. Its significance extends to several dimensions: **Practical Utility**: By reducing training time by ~25% and inference latency by ~1.5×, HarmoniCa enables more efficient deployment of generative models in real-world applications, such as **text-to-image synthesis** and **class-conditional generation**. These improvements address critical barriers to the broader adoption of diffusion models in industry.  **Broad Applicability**: The framework’s adaptability across multiple architectures and resolution settings underscores its broad utility. The ability to apply HarmoniCa without image data during training expands its applicability to scenarios with limited training resources.  **Scientific Advancement**: This paper advances research in efficient generative modeling by proposing an original, learning-based caching strategy that can inform future developments in DiTs and potentially inspire similar approaches in other transformer-based generative models.

### Weaknesses
 - The HarmoniCa framework’s reliance on multiple components (SDT, IEPO, and the custom cache router) could limit its accessibility and reproducibility for practitioners, especially those with limited computational resources. While the model is described in detail, implementing and integrating SDT and IEPO into an existing Diffusion Transformer may pose a significant challenge due to the additional computational and architectural overhead. The paper does not fully clarify the complexity of integrating these components, particularly regarding the modifications required within the DiT architecture itself and the potential for increased memory footprint during training and inference.
  
 - While HarmoniCa is tested across multiple models and resolutions, it is evaluated only on **ImageNet** (for class-conditioned tasks) and **MS-COCO** (for text-to-image tasks). These datasets are popular benchmarks but may not represent the variety of distributions found in real-world data, especially in domains like video generation or multi-modal applications where diffusion models are increasingly applied. The paper lacks a discussion on how the performance of HarmoniCa might vary when applied to datasets with different characteristics, such as those with more complex textures or object arrangements, or in tasks beyond image generation.
   
 - The **Image Error Proxy-Guided Objective (IEPO)** is a central contribution but relies on approximating final image quality based on intermediate denoising steps. The validity of this proxy could vary significantly depending on the task and model architecture, yet the paper provides limited empirical analysis of IEPO’s sensitivity to different proxy metrics. The paper does not explore how the choice of proxy metric (e.g., MSE, SSIM, LPIPS) affects the overall performance of HarmoniCa, nor does it discuss the potential for the proxy to introduce biases or inaccuracies in the training process.
   
 
 -  While the paper includes several ablation studies, it does not provide a fine-grained analysis of the **Step-Wise Denoising Training (SDT)** component and the specific elements of the cache router. These elements are integral to HarmoniCa's efficacy, but without a breakdown of their contributions, it remains unclear how each sub-component (e.g., caching frequency, router sensitivity) directly impacts performance and efficiency. The paper lacks detailed experiments that isolate the effects of individual components, making it difficult to understand the precise contribution of each to the overall performance gain.
 
- The paper provides comparisons with **Learning-to-Cache** and **FORA** but lacks discussion of other potential caching and acceleration techniques, such as model pruning or quantization, commonly explored in efficiency research for generative models. While these techniques are mentioned, a more in-depth comparison or consideration of combining methods could contextualize HarmoniCa’s strengths and limitations relative to other optimizations. The paper would benefit from a more thorough analysis of how HarmoniCa compares to or could be combined with other orthogonal acceleration techniques.
 
- Although HarmoniCa shows improvements in image quality (e.g., FID, IS), the paper could benefit from qualitative analyses of generated images. This would help illustrate how the framework’s focus on harmonizing training and inference affects visual output, potentially highlighting differences in quality between HarmoniCa and baseline methods. The paper does not provide a visual comparison of the generated images, which could reveal artifacts or other quality issues not captured by quantitative metrics alone.

### Questions
- **Question**: Could the authors elaborate on the criteria for selecting the error proxy in the Image Error Proxy-Guided Objective (IEPO)? Specifically, how was the proxy choice validated across different image generation tasks, and did the authors observe any trade-offs when experimenting with alternative metrics?
   
- **Question**: Could the authors provide additional insights into the computational resources required to implement HarmoniCa, especially the hardware and memory demands for training and inference?
  
- **Question**: Does HarmoniCa generalize well beyond the specific tasks demonstrated, such as high-resolution image generation? Have the authors considered exploring HarmoniCa’s effectiveness for video generation or other data-intensive applications where DiTs are applied?
   


- **Question**: How sensitive is HarmoniCa’s performance to the configuration of the cache router? Specifically, does adjusting parameters such as the caching threshold or the router’s update frequency significantly impact model performance, or is HarmoniCa robust across a range of these values?
   

- **Question**: Could the authors provide qualitative insights into the visual differences observed between HarmoniCa-generated images and those from baseline methods, especially in scenarios with aggressive caching? Are there specific artifacts or benefits visible that illustrate HarmoniCa’s impact on image quality?
 

- **Question**: Could HarmoniCa’s SDT and IEPO components be integrated into other popular architectures, such as U-Net-based diffusion models? If so, do the authors foresee any challenges or modifications needed to adapt HarmoniCa for such architectures?
 

- **Question**: Have the authors considered combining HarmoniCa with other model efficiency techniques, such as quantization or model pruning? What limitations or synergies do the authors anticipate in hybridizing HarmoniCa with these techniques?

### Soundness
2

### Presentation
2

### Contribution
2
