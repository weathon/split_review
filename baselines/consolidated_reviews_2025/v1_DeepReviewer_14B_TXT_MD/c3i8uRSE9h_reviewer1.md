### Summary

The paper proposes a new method for solving inverse problems using pre-trained diffusion models. The authors propose to solve the inverse problem by solving for the noisy latent using a gradient descent type method. The gradient is computed using a numerical approximation, which is shown to be much faster than the backprop approach used in many prior works. The proposed method is evaluated on ImageNet for inpainting and superresolution tasks.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

- The proposed method is simple and fast. The numerical approximation of the gradient is simple to implement and is faster than the backprop approach used by prior works. 
- The proposed method is shown to outperform prior works in inpainting tasks. The performance of the proposed method is on par with prior works on superresolution.

### Weaknesses

#### Some Related Works


#### comment

 - The experiments in the paper are limited. The proposed method is only evaluated on ImageNet for inpainting and superresolution tasks. It would be interesting to see if the proposed method can be used to solve other types of inverse problems, e.g., inverse graphics or vision tasks (see some of the works listed below). It would also be interesting to see the performance of the proposed method on other types of datasets, e.g., faces (CelebA) or text-rich images (TextImageNet).
- The qualitative results for superresolution in Figure 6 and Figure 7 show that the proposed method produces artifacts. 
- The quantitative results for superresolution in Table 1 show that the proposed method performs on par with prior works. For example, the PSNR achieved by the proposed method is slightly lower than the PSNR achieved by P2L and LDPS. 
- The paper lacks an ablation study. For example, it would be interesting to see how the performance of the method changes with the choice of numerical approximation (number of function evaluations).

### Suggestions

The paper would benefit from a more thorough experimental evaluation. While the ImageNet results are a good starting point, the scope of the experiments is too narrow. The authors should consider expanding their evaluation to include other datasets, such as CelebA for face super-resolution or TextImageNet for text-rich image restoration. This would demonstrate the robustness and generalizability of the proposed method across different types of image content. Furthermore, exploring other inverse problems beyond inpainting and super-resolution, such as inverse graphics or deblurring, would significantly strengthen the paper's contribution. These additional experiments would provide a more comprehensive understanding of the method's capabilities and limitations.

In addition to expanding the scope of the experiments, the authors should also conduct a more detailed analysis of the method's performance. The qualitative results for super-resolution show noticeable artifacts, and the quantitative results are only on par with existing methods. A more in-depth analysis of the causes of these artifacts and the limitations of the method would be valuable. For example, the authors could investigate the impact of different hyperparameter settings on the quality of the results. This could involve varying the step size, the number of iterations, or the parameters of the numerical approximation. Furthermore, a comparison with other state-of-the-art methods, especially those that achieve higher PSNR values, would provide a more complete picture of the method's performance relative to the current state of the art.

Finally, the paper lacks a proper ablation study. The authors should investigate the impact of different design choices on the performance of the method. For example, they could explore the effect of using different numerical approximation schemes for the gradient, such as forward or central differences, and analyze the trade-off between accuracy and computational cost. It would also be interesting to see how the number of function evaluations affects the performance of the method. This would provide a better understanding of the method's sensitivity to different parameters and help to identify the optimal settings for different tasks. Furthermore, an ablation study on the number of warm restarts and the perturbation added to the gradient during super-resolution would be beneficial.

### Questions

- The proposed method adds perturbations to the gradient during superresolution. It would be interesting to see the superresolution performance of the method without these perturbations. 
- The proposed method uses warm restarts for both inpainting and superresolution. Did the authors try performing superresolution without warm restarts? How does the performance change without warm restarts?

### Rating

3

### Confidence

4

**********
