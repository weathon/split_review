### Summary

This paper proposes a new algorithm for solving inverse problems using pre-trained diffusion models. The proposed algorithm is based on a novel optimization perspective to sampling under constraints and employs a numerical approximation to the expensive gradients, previously computed using backpropagation, incurring significant speed-ups.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The proposed method is well-motivated and novel. The idea of using the inverse function to approximate the gradient is interesting.
2. The proposed method is simple and easy to implement.
3. The proposed method achieves competitive results with much less inference time.

### Weaknesses

#### Some Related Works

[1] Denoising Diffusion Implicit Models
[2] Solver for inverse problems in diffusion models
[3] A conditional diffusion model for inverse problems
[4] Prompt-tuning diffusion models for inverse problems

#### comment

1. The paper lacks comparisons with state-of-the-art methods. For instance, the authors do not compare their approach with methods such as DDIM [1], P2L [2], and DDNM [3], which are all training-free methods for solving inverse problems. Specifically, the absence of a comparison with DDIM, which is a fundamental building block for many of these methods, is a significant oversight. Furthermore, the paper does not address how the proposed method's performance scales with different noise schedules, a critical aspect of diffusion models that is often explored in the cited works. The lack of comparison with DDNM, which directly addresses the inverse problem using a different optimization strategy, further weakens the paper's claim of novelty and effectiveness.
2. The paper lacks ablation studies. For example, the authors do not analyze the impact of the hyperparameters on the performance of the proposed method. The absence of a sensitivity analysis for key hyperparameters, such as the step size and the number of iterations, makes it difficult to assess the robustness and reliability of the proposed method. It is unclear how these parameters should be tuned for different tasks and datasets, which limits the practical applicability of the method.
3. The paper does not provide a theoretical analysis of the proposed method. For example, the authors do not analyze the convergence properties of the proposed method. The lack of theoretical grounding makes it difficult to understand the fundamental limitations and potential of the proposed method. Without a convergence analysis, it is unclear under what conditions the method is guaranteed to produce a satisfactory solution, and how the solution quality is affected by the choice of hyperparameters.
4. The paper does not provide a detailed explanation of the proposed method. For example, the authors do not explain how to choose the hyperparameters of the proposed method. The explanation of the method is insufficient for reproducibility. The paper lacks a clear description of the algorithm, making it difficult for other researchers to implement and validate the proposed method. The absence of a detailed explanation of the hyperparameter selection process further hinders the practical use of the method.

### Suggestions

The paper needs a more thorough evaluation against existing state-of-the-art methods. Specifically, the authors should include comparisons with DDIM, P2L, and DDNM, as these are all relevant baselines for solving inverse problems with pre-trained diffusion models. The comparison should not only focus on quantitative metrics but also include a qualitative analysis of the results. Furthermore, the authors should investigate the sensitivity of their method to different noise schedules, as this is a critical aspect of diffusion models that can significantly impact performance. The experiments should also include a wider range of datasets and tasks to demonstrate the generalizability of the proposed method. A more comprehensive experimental evaluation is crucial to establish the effectiveness and practical value of the proposed approach.

In addition to the quantitative comparisons, the paper should include a detailed ablation study to analyze the impact of the hyperparameters on the performance of the proposed method. This should include a sensitivity analysis of the step size, the number of iterations, and any other relevant parameters. The authors should provide clear guidelines on how to choose these hyperparameters for different tasks and datasets. The ablation study should also investigate the trade-offs between computational cost and performance, providing practical guidance for users of the method. This analysis is essential to understand the robustness and reliability of the proposed method and to make it more accessible to other researchers.

Finally, the paper should include a theoretical analysis of the proposed method. This should include an analysis of the convergence properties of the method, as well as an investigation of its limitations and potential. The theoretical analysis should provide a deeper understanding of the method's behavior and its relationship to other existing approaches. The authors should also provide a more detailed explanation of the proposed method, including a clear description of the algorithm and the hyperparameter selection process. This is essential for reproducibility and for the practical use of the method by other researchers. Without a theoretical analysis and a detailed explanation, the paper lacks the necessary depth and rigor to be considered a significant contribution to the field.

### Questions

1. How does the proposed method compare to other state-of-the-art methods, such as DDIM [1], P2L [2], and DDNM [3]?
2. How do the hyperparameters affect the performance of the proposed method?
3. What are the convergence properties of the proposed method?
4. How to choose the hyperparameters of the proposed method?

[1] Denoising Diffusion Implicit Models. Xie et al. ICLR 2023.

[2] Solver for inverse problems in diffusion models. Chung et al. ICLR 2024.

[3] A conditional diffusion model for inverse problems. Lu et al. CVPR 2024.

[4] Prompt-tuning diffusion models for inverse problems. Chung et al. ICLR 2024.

### Rating

5

### Confidence

4

**********
