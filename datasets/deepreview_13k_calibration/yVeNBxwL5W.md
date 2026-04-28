# MRS: A Fast Sampler for Mean Reverting Diffusion based on ODE and SDE Solvers

- Decision: Accept
- Avg Score: 7.50
- Scores: 8, 6, 8, 8

## Abstract
In applications of diffusion models, controllable generation is of practical significance, but is also challenging. Current methods for controllable generation primarily focus on modifying the score function of diffusion models, while Mean Reverting (MR) Diffusion directly modifies the structure of the stochastic differential equation (SDE), making the incorporation of image conditions simpler and more natural. However, current training-free fast samplers are not directly applicable to MR Diffusion. And thus MR Diffusion requires hundreds of NFEs (number of function evaluations) to obtain high-quality samples. In this paper, we propose a new algorithm named MRS (MR Sampler) to reduce the sampling NFEs of MR Diffusion. We solve the reverse-time SDE and the probability flow ordinary differential equation (PF-ODE) associated with MR Diffusion, and derive semi-analytical solutions. The solutions consist of an analytical function and an integral parameterized by a neural network. Based on this solution, we can generate high-quality samples in fewer steps. Our approach does not require training and supports all mainstream parameterizations, including noise prediction, data prediction and velocity prediction. Extensive experiments demonstrate that MR Sampler maintains high sampling quality with a speedup of 10 to 20 times across ten different image restoration tasks. Our algorithm accelerates the sampling procedure of MR Diffusion, making it more practical in controllable generation.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
Standard MR Diffusion models typically require a high number of function evaluations to obtain high-quality samples. To address this limitation, MR Sampler introduces a novel approach that combines an analytical function with an integral parameterized by a neural network. The proposed method demonstrates a 10 to 20-fold speedup across various image restoration tasks, obtaining efficient sampling without compromising quality.

### Strengths
1). The paper is very well written, and easy to understand especially very coherent even with the math part.

2). The core idea of the paper is very interesting. Especially how the authors have formulated  the core idea.

3). The shown results are very impressive and competitive.

4). Even though the concept behind the "sampling trajectory" part is simple, the visualizations obtained through it really helps to understand the core concept and contrast with existing methods. 

5). The MRS is plug and play.

### Weaknesses
I believe this is a great paper with solid reasoning and a well-thought-out approach. However, I have some questions regarding the numerical implementation and the comparison methods used.

1). Can the authors elaborate on why only the backward difference method is used? Are there specific benefits to this approach over others?

2). The proposed MR Sampler is only compared with posterior sampling, and Euler-Maruyama discretization. What are the current SOTA methods? How does the proposed approach compare with these, beyond posterior sampling and Euler-Maruyama?

3). I would like to understand why the authors say "frequently fall outside" in this part (line304)
 "Although the standard deviation of this Gaussian noise is set to 1, the values of samples can frequently fall outside the range of [-1,1]"

4). Could the authors specify the neural network architecture they used?

### Questions
Please see the weaknesses section.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a fast sampling algorithm for mean-reverting diffusion. This addresses a gap for mean-reverting diffusion SDE solvers, as current fast samplers for SDEs do not readily apply to mean-reverting SDEs. Two flavors of solvers are proposed, one based on noise prediction, and the other on data prediction. Results show both perform similarly for larger NFEs, but the latter outperforms the former for fewer NFEs.

### Strengths
- Addresses a gap in fast sampling for mean-reverting diffusion
- Provides two alternatives focusing on noise/data prediction
- Relevant ablation studies for some parameter choices
- Evaluates performance in image restoration tasks

### Weaknesses
 - No ablation study on n, k
- Wall clock time not reported, only NFE improvement is discussed
- No comparison to standard SDE fast samplers 
- The whole description is for unconditional sampling, but all results are for image restoration. How is the guidance incorporated?

### Questions
- Why wasn't an ablation study done on n, k?
- Why wasn't wall clock time reported? Please provide.
- Why weren't there comparison to standard (non-MR) SDE fast samplers? This comparison should include both reconstruction quality for inverse problems (since this is given as the main motivation for MR diffusion) and computational time.
- How was guidance incorporated for image restoration? Does the particular method for incorporating the degraded observation make a difference for the performance of MR sampler?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors propose a novel algorithm, named MRS, designed as a sampler to reduce the number of sampling steps required for Mean Reverting Diffusion. To achieve this, they solve the reverse-time stochastic differential equation (SDE) alongside the probability flow ordinary differential equation, resulting in a reduction of required steps to between 5 and 15 while maintaining high-quality outcomes. The method is compatible with mainstream parameterizations, making it broadly applicable. The authors conduct an extensive evaluation across 16 different image perturbations, demonstrating that their proposed sampler generally outperforms others in both efficiency and speed.

### Strengths
- The authors' proposed method demonstrates robust performance across a variety of experiments, consistently showing strong results in both quality and efficiency. Notably, it outperforms posterior-based and Euler-based samplers when using a high number of sampling steps. The performance advantage becomes even more pronounced as the number of steps is reduced, underscoring the method's effectiveness with low-step counts.

- It is particularly encouraging to see that the proposed method performs best across almost all of the 16 tested image perturbations. This breadth of performance suggests that the approach is not only effective but also adaptable to different types of image perturbations.

- The paper is generally well-organized and written. Key concepts and technical choices are clearly explained.

- Overall, this is a well-rounded paper that offers convincing results and provides a method that should be straightforward to integrate with existing frameworks. I also appreciate the authors’ decision to release the code for easy reproducibility.

### Weaknesses
 - The choice of the number of sampling steps is not entirely clear. While it seems that setting this value to 20 yields acceptable results, this may not fully leverage the acceleration benefits of the proposed method. Further guidance on selecting an optimal number of steps or a discussion on its trade-offs would make this aspect more transparent. Specifically, the paper lacks a clear explanation of how the step size impacts the trade-off between solution accuracy and computational cost. A more detailed analysis of how the error accumulates with fewer steps, and how this relates to the specific characteristics of the Mean Reverting Diffusion process, would be beneficial.
- There is some ambiguity regarding the number of function evaluations (NFEs) required for MR Diffusion. The authors mention that MR Diffusion typically requires hundreds of NFEs, but in the current paper, this value is set to 100, consistent with the original paper. This raises questions about whether the maximum performance of the Posterior and Euler-based sampling methods could be higher if a larger number of steps were used. Given the performance gains depicted in Figure 2, it would be helpful to clarify if the efficiency improvements observed are partly due to these optimized sampling steps. It is unclear whether the comparison is entirely fair, as the baseline methods might benefit from a larger number of function evaluations, potentially narrowing the performance gap. The paper should provide a more detailed discussion on the limitations of the baseline methods under different NFE settings.
- Table 15 in the appendix contains incorrect highlight

### Questions
- How did you determine the optimal number of sampling steps? The choice of steps varies across different experiments, but the selection criteria are not immediately clear. Could you provide more explanation on how to select the number of steps to balance efficiency and performance?
- What was the rationale behind choosing a low-light and motion-blurry dataset for the visualizations in Figure 2? 
- In reference to the related paper [1], it is mentioned that solving the SDE typically requires only 22 steps, although they still use 100 steps. Since you opted to use 100 steps aswell, I am wondering why the performance with 20 steps is still so substantially different.

[1] Luo, Ziwei, et al. "Image restoration with mean-reverting stochastic differential equations." arXiv preprint arXiv:2301.11699 (2023).

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
5

### Summary
The paper proposes a new perspective on improving the efficiency of sampling in Mean Reverting  Diffusion models. This approach introduces MR Sampler, which leverages both ordinary differential equations (ODE) and stochastic differential equations (SDE) to enhance the speed of the sampling process. While MR Diffusion provides a fresh perspective by modifying the structure of the SDE to make controllable image generation simpler and more natural, the main challenge it addresses is the inefficiency of sampling, which typically requires hundreds of function evaluations (NFEs) to generate high-quality outputs.

The authors build on prior work that primarily focused on denoising tasks using ODE solvers, and they extend this framework to a broader set of tasks without requiring additional training. The key technical contribution is the semi-analytical solution they derive, which reduces the number of NFEs significantly while maintaining competitive sampling quality. In fact, MR Sampler shows a speedup of 10 to 20 times across ten different image restoration tasks.

### Strengths
The paper introduces a novel approach to sampling in Mean Reverting  Diffusion models, which itself is a relatively new paradigm compared to more conventional diffusion processes like Variance Preserving and Variance Exploding SDEs. The key originality lies in the way the authors combine semi-analytical solutions derived from ODE and SDE solvers with MR Diffusion, enabling faster sampling. This combination is innovative as it offers a fresh perspective on accelerating diffusion models by altering the underlying stochastic differential equation structure rather than focusing solely on the score function as in prior work.

Additionally, the Mean Reverting SDE framework offers a natural integration of image conditions into the generation process, making it more applicable to tasks that require controllable generation, such as image restoration and inpainting. This is a novel contribution compared to prior work that has typically used Diffusion Schrödinger Bridge or Optimal Transport methods for similar purposes. The MR Diffusion model’s ability to address multiple tasks beyond denoising is a creative and valuable extension of existing frameworks.

The technical depth of the paper is commendable. The authors offer a rigorous derivation of the semi-analytical solution and provide substantial theoretical grounding for their approach. The use of probability flow ODEs (PF-ODEs) and reverse-time SDEs in the MR Diffusion context is clearly explained and well-justified. The semi-analytical solution, which combines an analytical function and a neural network-based integral, reduces computational complexity without compromising sampling quality.

The experiments are comprehensive and cover ten different image restoration tasks, providing strong empirical support for the proposed method. The use of multiple performance metrics (e.g., FID, LPIPS, PSNR, SSIM) demonstrates that the authors took a thorough approach to evaluating both the quality and speed of the generated samples. The speedups of 10-20x, without a significant drop in sample quality, highlight the robustness and practical value of the proposed method.

The paper is well-structured, with clear sections on the methodology, theoretical contributions, and experimental validation. The technical content, while complex, is made accessible through the use of visual aids (e.g., Figure 1 comparing qualitative sampling results, and charts showing performance metrics) and clear explanations of the mathematical formulations. The distinction between noise prediction and data prediction models, and the impact of these choices on sampling quality and stability, is clearly delineated and contributes to a deeper understanding of the technique.

The authors also provide appendices with detailed proofs and further experimental results, ensuring that the methodology is reproducible and the claims are verifiable. Overall, the clarity in presenting a technically complex subject is a strong point of the paper.

The proposed MR Sampler addresses a significant challenge in the field of diffusion models: accelerating the sampling process without sacrificing quality. The speedups achieved in this work, which range from 10x to 20x across multiple tasks, are substantial and have clear practical implications, particularly in real-time applications such as image restoration. This makes the method highly relevant for use cases that demand controllable and fast generation, such as medical imaging, video processing, and computational photography.

The method’s plug-and-play nature is another strength. It is adaptable to a variety of existing diffusion models and does not require retraining, making it easy to integrate into different applications. The broad applicability to various image restoration tasks (e.g., dehazing, inpainting, motion-blur reduction) enhances the significance of the work.

### Weaknesses
A notable limitation is that the paper places more emphasis on the speed of sampling rather than the quality. While the authors claim comparable quality in terms of metrics such as FID and LPIPS, they do not provide an in-depth analysis of the trade-off between sampling speed and output quality. This is a  gap, as accelerating sampling without sacrificing quality is one of the central challenges in diffusion models. The authors could have benefited from comparing their approach with other speed-quality trade-off techniques, such as those mentioned in prior work (e.g., the 'Come-Closer-Diffuse-Faster' approach). Although these methods might be older, they are relevant in establishing a clear benchmark and providing a deeper understanding of the trade-offs at play. (like https://openaccess.thecvf.com/content/CVPR2022/papers/Chung_Come-Closer-Diffuse-Faster_Accelerating_Conditional_Diffusion_Models_for_Inverse_Problems_Through_Stochastic_CVPR_2022_paper.pdf  and https://arxiv.org/abs/2108.01073 )

The experiments demonstrate a clear focus on speedups, and while they are rigorous and cover a variety of tasks (e.g., image dehazing, inpainting), the lack of comparison with more state-of-the-art methods suggests that the method may not yet be positioned as a new state of the art but rather as a faster alternative with comparable performance under specific conditions. Specifically, the paper lacks a clear comparison with established methods that also explore the speed-quality trade-off, such as those employing adaptive step size control or learned samplers. This makes it difficult to assess the true novelty and practical advantages of the proposed approach in the broader landscape of diffusion model acceleration techniques. The absence of such comparisons leaves open the question of whether the observed speedups come at the cost of subtle but important quality degradations that are not captured by the chosen metrics.

Overall, the introduction of the Mean Reverting SDE into the posterior sampling stage with ODE solvers is a fresh and promising perspective. However, the paper would benefit from addressing the broader implications of their method, particularly how the mean-reverting approach impacts the balance between speed and quality. Including more comprehensive comparisons with established trade-off techniques would further strengthen the contribution but overall this is a good paper, potentially worth discussing at ICLR.

### Questions
1. How does reducing NFEs affect sampling quality? Could you compare this with speed-quality trade-off methods like "Come-Closer-Diffuse-Faster"?

2. Do different image restoration tasks benefit differently from the MR Sampler in terms of speed or quality?

3. Why is Mean-Reverting SDE better for posterior sampling compared to other methods like Optimal Transport or Schrödinger Bridge?

4. Can you provide more details on the stability of data prediction models at low NFEs, and when would noise prediction be preferable?

5. Can MR Sampler be extended to larger or multi-modal tasks, such as video generation or text-to-image models?

6. Why are there no comparisons with SOTA models in terms of both speed and quality? Would this strengthen the paper?

### Soundness
3

### Presentation
4

### Contribution
3
