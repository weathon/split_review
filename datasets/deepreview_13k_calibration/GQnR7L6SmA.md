# Masked, Regularized Fidelity With Diffusion Models For Highly Ill-posed Inverse Problems

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 5, 6

## Abstract
Diffusion models have been well-investigated for solving ill-posed inverse problems to yield excellent performance. However, their application to highly ill-posed inverse problems remains challenging. In this work, we propose zero-shot diffusion model for large and complex kernels, dubbed Dilack, incorporating novel data fidelity terms. Based on our analyses on the ill-posedness for challenging inverse problems, we propose *regularized fidelity* called pseudo-inverse anchor for constraining (PiAC) fidelity loss. Inspired by locally acting classical regularizers, we also propose to incorporate *masked fidelity* within PiAC loss that can interact with globally acting diffusion models, which adaptively enforces spatially and step-wisely local fidelity via masks. Our proposed scheme effectively reduces erratic behavior and inherent artifacts in diffusion models, thereby improving restoration quality including perceptual aspects and outperforming prior arts on both synthetic and real-world datasets for modern lensless imaging and large motion deblurring.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presented a diffusion model designed to tackle highly ill-posed inverse problems involving large and complex kernels. It introduced extra data fidelity terms, including pseudo-inverse anchor for constraining (PiAC) fidelity loss, and employed a masked fidelity approach that dynamically emphasizes local consistency.

### Strengths
The methodology includes the development of the pseudo-inverse anchor which reflects a certain level of theoretical insight.

The authors claim improvements in restoration quality for specific applications like lensless imaging and large motion deblurring.

### Weaknesses
The central concept of the proposed approach is not clearly, and the overall description of the methodology lacks clarity.

The proposed algorithm incorporates many hyperparameters, which may complicate the implementation and optimization processes. This abundance of hyperparameters can also raise concerns regarding the stability and generalizability of the algorithm, as tuning them effectively may be challenging for practitioners.

The experimental results presented in the manuscript are unconvincing. For example, in the table above Figure 4 regarding Large Motion Deblurring, the proposed method only outperforms other methods in 1 out of 8 cases. The authors should also discuss the computational cost associated with their method, as this is crucial for evaluating its practicality.

The parameters L_{PS} and L_{Pi} are defined in formulas (9) and (10), respectively, but are used in Figure 1 without reference to their definitions. It is essential for the authors to mention these definitions in the caption of Figure 1 to ensure clarity for readers.

The authors increase the kernel size from 64^2 to 256^2 without providing any intermediary states or specifying the size of the images being processed. Additionally, the condition numbers related to these kernels are not clearly demonstrated. Clarification on these points is necessary for reproducibility and understanding.

While the authors use a total variation (TV)-regularized solution tilde(x^*) for the pseudo-inverse anchor, they should discuss how about replacing TV with other deblurring techniques, such as BM3D. This comparison could provide valuable context regarding the effectiveness of their approach.

The authors incorporate TV into their algorithm but do not specify the boundary conditions used for the TV regularization. Moreover, guidance on how to select the parameter lambda_t before the TV term is missing. The authors also mention that the patch size and top percentage threshold for the MROI are hyperparameters that need optimal settings. They should address the practicality of including numerous hyperparameters and their potential impact on the algorithm's stability.

The inclusion of skip step guidance in Algorithm 1 lacks sufficient justification and introduction, making it difficult to assess its effectiveness. The authors should provide a rationale for this component to strengthen their argument.

The authors state, "Each element of MROI is set to 1 if the patch-wise difference between tilde{x}^* and hat{x}_{0|t} falls within the top percentage threshold of all sums of differences observed; otherwise, it is set to 0." This explanation is confusing and requires further clarification. The authors should provide a clear methodology for setting the MROI to enhance understanding.

### Questions
The experimental results presented in the manuscript are unconvincing. For example, in the table above Figure 4 regarding Large Motion Deblurring, the proposed method only outperforms other methods in 1 out of 8 cases. The authors should also discuss the computational cost associated with their method, as this is crucial for evaluating its practicality.

The parameters L_{PS} and L_{Pi} are defined in formulas (9) and (10), respectively, but are used in Figure 1 without reference to their definitions. It is essential for the authors to mention these definitions in the caption of Figure 1 to ensure clarity for readers.

The authors increase the kernel size from 64^2 to 256^2 without providing any intermediary states or specifying the size of the images being processed. Additionally, the condition numbers related to these kernels are not clearly demonstrated. Clarification on these points is necessary for reproducibility and understanding.

While the authors use a total variation (TV)-regularized solution tilde(x^*) for the pseudo-inverse anchor, they should discuss how about replacing TV with other deblurring techniques, such as BM3D. This comparison could provide valuable context regarding the effectiveness of their approach.

The authors incorporate TV into their algorithm but do not specify the boundary conditions used for the TV regularization. Moreover, guidance on how to select the parameter lambda_t before the TV term is missing. The authors also mention that the patch size and top percentage threshold for the MROI are hyperparameters that need optimal settings. They should address the practicality of including numerous hyperparameters and their potential impact on the algorithm's stability.

The inclusion of skip step guidance in Algorithm 1 lacks sufficient justification and introduction, making it difficult to assess its effectiveness. The authors should provide a rationale for this component to strengthen their argument.

The authors state, "Each element of MROI is set to 1 if the patch-wise difference between tilde{x}^* and hat{x}_{0|t} falls within the top percentage threshold of all sums of differences observed; otherwise, it is set to 0." This explanation is confusing and requires further clarification. The authors should provide a clear methodology for setting the MROI to enhance understanding.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes a zero-shot method for highly ill-posed inverse problems (IP) based on a pre-trained diffusion model. The authors demonstrate that existing zero-shot IP methods tend to fail under conditions of severe degradation. This method introduces a pseudo-inverse anchor to constrain fidelity loss, utilizing an existing total variation (TV)-regularized solution. Additionally, they incorporate a locally masked loss, where the loss is dynamically activated or deactivated based on its similarity to the TV-regularized solution. The method achieves state-of-the-art (SOTA) results in highly ill-posed cases, such as lensless imaging and image deblurring.

### Strengths
1. The method is training-free which makes it computationally practical.

### Weaknesses
1. The other compared methods address the original (highly ill-posed) input, whereas the proposed method basically restores a more well-posed input (the TV-regularized solution). This raises the question of how fair the comparison is. It may make more sense to view the proposed method as a framework that can be integrated with existing methods rather than as a standalone inverse problem solution.

2. The setup presented in the paper is questionable; for example, how realistic is the kernel blur used in the study for real-world scenarios where the signal is almost completely lost?

3. The paper focuses on the non-blind case, assuming that the degradation forward model is known. It would be more interesting to investigate the more general, blind case instead, where the degradation model is unknown.

### Questions
1. In Figure 1, it appears that the diffusion model used is an unconditional model trained on ImageNet, which is known to be relatively weak due to the limited amount of training data compared to the large number of classes. One potential reason for the failure of existing IP methods may be the use of this weak pre-trained model. It would be interesting if the authors could reproduce the same analysis on the FFHQ dataset, where the model is much stronger, to determine whether the failures of existing methods are due to the weak pre-trained model or intrinsic issues.

### Soundness
2

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
In this paper, the authors introduce a new data-fidelity term for solving challenging inverse problems using diffusion models. Noting the limitations of existing approaches on highly ill-posed problems, they propose replacing the standard $L_2$  data-fidelity term with the $L_2$ distance between the solution obtained by regularizing the inverse problem with a TV prior and the posterior mean derived from the diffusion denoiser. They demonstrate the effectiveness of this approach through experiments on lensless imaging and large-motion deblurring tasks.

### Strengths
- The main idea, which is to replace the pseudo-inverse by a TV-regularized solution, is interesting. The approach of modifying the data-fidelity term is flexible and could potentially be adapted for other types of priors, opening doors for future work on similar challenging inverse problems.
- By using the posterior mean from a diffusion model, and the ADMM prior, the paper effectively combines generative modeling with traditional regularization, a creative fusion of modern and classical techniques.
- The paper provides comprehensive experiments on nontrivial tasks, such as lensless imaging and deblurring, that highlight the practical advantages of the proposed method.

### Weaknesses
 - **Readability Issues**: The paper is sometimes challenging to read due to long, complex sentences, particularly in the abstract and Remark 1. Simplifying these sections could improve readability and flow.

- **Sampling vs. Maximization**: The method proposed here, like DPS and DiffPIR, is a **sampling** method aimed at sampling from the posterior distribution. However, this crucial point seems to be overlooked or misunderstood by the authors, as the paper appears to focus on solving equation (2) for posterior maximization rather than posterior sampling. The introduction frames the problem as finding a single optimal solution, which is inconsistent with the stochastic nature of diffusion models and their use for posterior sampling.

- **Explanation of $x$ Replacement in Equation (14)**: It is unclear why $x$ in line 298 is replaced by $x_{0|t}$ in equation (14). Why is the data-fidelity term $|| x_{TV} - x ||^2$ not used instead? The new data-fidelity term appears significantly different from $L_{PI}$, making it unclear whether a comparison between the two terms is justified. On what basis can Equation (15) be considered approximately true? Has it been verified, for example, for simpler inverse problems that $L_{PI}$ approximates $L_{PIAC}$? The justification for replacing $x$ with $x_{0|t}$ is not clear, and the connection to the original $L_{PI}$ term is weak, raising concerns about the validity of the proposed data-fidelity term.

- **Comparison with State-of-the-Art Methods**: It would be beneficial to compare the proposed approach with other state-of-the-art methods in image inverse problems, such as Plug-and-Play (PnP) methods like DPIR.

- **Comparison with DPS Method**: The comparison with DPS may be unfair, as DPS’s performance could likely be improved with step-size optimization. This omission may explain DPS’s lower performance in the experiments. The lack of a step-size optimization for DPS raises concerns about the fairness of the comparison, as it is a critical parameter for gradient-based optimization methods.

- **Mismatch Between Equation (17) and Algorithm 1**: Equation (17) does not match the steps in Algorithm 1 due to the addition of noise in the algorithm. The discrepancy between the theoretical update rule and the actual implementation with added noise needs to be addressed for clarity and correctness.

- **PSNR Comparison in Posterior Sampling Context**: Since the goal is to sample from the posterior distribution, comparing PSNR values may not be meaningful unless comparing the posterior means. Are PSNR values in the paper calculated based on a single sample from each method? The use of PSNR as an evaluation metric is questionable in the context of posterior sampling, as it does not capture the diversity of samples, and it is unclear if the reported values are based on single samples or posterior means.

- **Algorithm Structure for Clarity**: Since \( G = 1 \) is used in practice, restructuring the algorithm into two main steps—1) ADMM-TV and 2) Diffusion—could improve clarity and make the methodology easier to understand.

### Questions
1. **Consistency in Comparisons**: Why do Tables 2 and 3 compare against different methods? Consistently using the same methods across both tables would allow for a more direct comparison of results.

2. **Code Release**: Is there a plan to release the code for this method? 

3. **Clarification on Appendix Statement about ADMM and Regularization**: The sentence in the Appendix, “Incorporating Total Variation (TV) regularization into the Alternating Direction Method of Multipliers (ADMM) enhances the algorithm’s performance across various applications,” is somewhat misleading. It is not the use of TV specifically but rather the addition of a regularization term that enables the solution of the inverse problem. Additionally, any proximal splitting algorithm—not just ADMM—could be used for this purpose. Could you clarify this?

4. **Applicability of Data-Fidelity Term with Other Priors**: If the primary contribution is to modify the data-fidelity term, could this approach work with priors other than diffusion models? This generalization could broaden the method’s applicability.

5. **Comparison with Standard \( L_2 \) Data-Fidelity Term**: Would it be useful to compare your method to an approach that minimizes the standard $L_2$ data-fidelity term combined with a diffusion prior and a TV prior? 

6. **Gradient Calculation Method**: For calculating the gradient of your data-fidelity term, do you use automatic differentiation? If so, does this require backpropagation through the diffusion model? If yes, is this process computationally intensive, and how does it impact runtime?

Raising my score to 5 after the discussion period.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes an improved diffusion posterior sampling algorithm for solving highly ill-posed inverse problems. By identifying inconsistent local regions and using it to guide some sparse iterations, the proposed method is capable of solving inverse problems in modern lensless imaging and large motion deblurring which most currently available diffusion-based posterior sampling algorithms fail to do.

### Strengths
1. The main contribution would be the extension of current diffusion-based posterior sampling algorithms on highly ill-posed inverse problems. The contribution is significant and groundbreaking.
2. The paper is well-written and has detailed theoretical deductions as well as comprehensive experiments.
3. The authors identify some critical challenges that current diffusion-based posterior sampling algorithms have.

### Weaknesses
1. In real-world applications (see Appendix G8), the restored images exhibit a smoother appearance compared to the ground truth. This suggests that there is still room for improvement in the number of steps used by the Dilack algorithm. The smoothing effect could be due to an over-reliance on the diffusion model's prior, potentially obscuring fine details present in the ground truth. This is particularly noticeable in high-frequency regions of the images, where the reconstructed textures appear less sharp and detailed than the original.

2. The computational complexity of the algorithm is quite high. While the paper mentions a modest increase in computation time, the absolute time of 390 seconds per image is still significant, making it impractical for real-time or high-throughput applications. The iterative nature of the algorithm, particularly the TV-regularized optimization component, contributes to this high computational cost. Furthermore, the need to perform multiple diffusion steps adds to the overall processing time.

### Questions
1. How effective is the algorithm when applied to synthetic images and other tasks, such as super-resolution and denoising?
2. In the TV-regularized optimization component of the Dilack algorithm, is it feasible to perform just a single optimization step instead of seeking the minimum value? What would be the anticipated impact on overall performance?

### Soundness
3

### Presentation
3

### Contribution
3
