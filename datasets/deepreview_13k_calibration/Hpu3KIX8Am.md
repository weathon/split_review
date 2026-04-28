# Dreamguider: Improved Training free Diffusion-based Conditional Generation

- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 5, 3, 5

## Abstract
Diffusion models have emerged as a formidable tool for training-free conditional generation.
However, a key hurdle in inference-time guidance techniques is the need for compute-heavy backpropagation through the diffusion network for estimating the guidance direction. Moreover, these techniques often require handcrafted parameter tuning on a case-by-case basis.
Although some recent works have introduced minimal compute methods for linear inverse problems, a generic lightweight guidance solution to both linear and non-linear guidance problems is still missing. To this end, we propose Dreamguider, a method that enables inference-time guidance without compute-heavy backpropagation through the diffusion network. The key idea is to regulate the gradient flow through a time-varying factor. Moreover, we propose an empirical guidance scale that works for a wide variety of tasks, hence removing the need for handcrafted parameter tuning. We further introduce an effective lightweight augmentation strategy that significantly boosts the performance during inference-time guidance. We present experiments using Dreamguider on multiple  tasks across multiple datasets and models to show the effectiveness of the proposed modules. To facilitate further research, we will make the code public after the review process.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The authors propose a generic lightweight guidance solution, named Dreamguider, which enables inference-time guidance without the need for backpropagation through the entire diffusion network. Dreamguider can address both linear and non-linear guidance problems. The authors also introduce an empirical guidance scale strategy to removing the need for handcrafted parameter tuning. This paper showcases experiments across multiple tasks, datasets, and models to demonstrate the effectiveness of the proposed methods. The key contributions include: 1) Dreamguider, a zeroth-order loss-guided diffusion guidance applicable to both linear and non-linear inverse problems, 2) a time-varying guidance scale, and 3) a differentiable augmentation strategy.

### Strengths
1. The paper tackles a relevant and challenging problem in the realm of conditional (controllable) generation for unconditional diffusion models.
2. It proposed two useful tricks to improve the generation quality: 1) an empirical guidance scale and 2) differentiable augmentation for classifier guidance.

### Weaknesses
1. Overall, the contributions of this paper are limited. The proposed Dreamguider is built upon MGD [1], an earlier proposed zeroth-order loss-guided guidance method that also eliminates the need for backpropagation through the diffusion network. The authors claim that Dreamguider can address non-linear inverse problems, unlike MGD. However, they should provide a detailed description and evidence to support this claim. In the current manuscript, I cannot find the intuition or evidence needed to substantiate this. The paper lacks a clear explanation of why directly guiding the diffusion process through \(\epsilon_\theta(x_t)\) enables handling of non-linear problems, while MGD's guidance through \(\hat{x}_t\) does not. A more rigorous analysis of the gradient flow and its impact on different types of tasks is needed.

2. The paper should clarify the intuition behind the methodological design discussed in Section 3.1, which currently lacks depth and clarity. Given that Dreamguider is closely related to MGD, a comprehensive comparison of each designed component should be included to enhance understanding. Specifically, the paper should elaborate on how the proposed time-varying guidance scale is derived and why it is effective. A detailed comparison of the guidance mechanisms, including the specific mathematical formulations and their impact on the diffusion process, is necessary to highlight the differences between Dreamguider and MGD.

3. MGD is capable of handling latent diffusion models, so it is ridiculous that an improved method like Dreamguider loses this important capability. The authors should provide a detailed explanation for this shortcoming, and consider addressing it rather than deferring the issue to future work. The paper needs to analyze the specific reasons why Dreamguider struggles with latent diffusion models, such as potential gradient vanishing issues through the VAE, and provide a more thorough discussion of the limitations of the proposed approach. The current explanation is insufficient and leaves the reader questioning the practical applicability of the method.

4. The showcased results are not appealing, as the performance differences between Dreamguider and MGD on some tasks are marginal. If possible, incorporating a user study could significantly enhance the experimental validation. The quantitative results should be more thoroughly analyzed, with a focus on statistical significance. The paper should also include qualitative results that clearly demonstrate the advantages of Dreamguider over MGD, especially for non-linear tasks. The current visual comparisons are not compelling enough to justify the proposed method.

### Questions
Please refer to the weakness for my questions.

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this paper, the authors propose a new method for training-free diffusion posterior guidance. In particular, instead of only modifying the Tweedie’s (MMSE) estimation in DDIM sampling, they propose to also guide the noise/score prediction to obtain a better guided sample. They also provide a way to perform data augmentation and a closed form solution to the step size of these guidance, which is a critical contribution to the field as so far there is no principle way to determine these hyperparameters. Their experiments show superior performance in comparison to baselines across many different tasks.

### Strengths
Almost all prior works in training-free diffusion guidance are very sensitive to hyperparameters, especially the step size, and currently there is no principled way to determine these hyperparameters. In fact, I think this is one of the biggest problems with these methods that prevent them from being applied widely. This paper provides a concrete way to decide these hyperparameters, which is extremely valuable for this field. The authors also propose a very creative way to perform the guidance by modifying the noise/score estimation directly (as opposed to the Tweedie’s clean data estimation only), which I find to be very interesting as well. The authors also provide a very effective way to perform data augmentation in this diffusion guidance task, which is also very useful.

Overall I really like the methods proposed in this paper, and I really want to accept it. However, there are certain aspects in this paper that I think need to be improved before it gets accepted.

### Weaknesses
 - The novelty is somewhat limited. The proposed algorithm seems to be an extension of the previous work of MGD (also a zeroth-order guidance scheme) and the contributions are not clear enough. Out of the four contributions mentioned in the introduction the ones that are clearly presented are regarding the tuning of the constraint guidance and the differentiable augmentations.
- In Table 2 and Table 3 the citation for MGD is incorrect (points to DPS).
- The core mechanism of the proposed method, which involves applying gradients with respect to both $\hat{x}_t$ and $\epsilon_{\theta}(x_t)$, is not sufficiently justified. While the authors claim a difference in the timing of when these gradients are applied, the underlying reason for this specific schedule is not clear. The connection between the schedule and the formation of semantic features is not rigorously established, making the choice seem somewhat arbitrary. The method's effectiveness might be due to a specific weighting of the gradients rather than a fundamental difference in the approach.

### Questions
It would be great if the authors can address the weakness mentioned above.
In addition, I am wondering if the authors have used techniques such as time traveling/repaint to stabilize the sampling process?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes a training-free algorithm for conditional inference in diffusion models. The authors improve upon previous works by coming up with a guidance schedule that balances better the conditioning signal during the inference process. They also propose a differentiable augmentation strategy that improves the guidance by averaging it over different augmentations of the input and the condition. They validate their method experimentally on a set of linear and non-linear inverse problems, across different diffusion models.

### Strengths
- The proposed algorithm seems to overall improve upon the results attained by previous methods. When comparing with the similar work done in MGD, the results show that there is a clear advantage for the proposed algorithm, both quantitatively and qualitatively.
- The augmentation guidance scheme proposed, could be of wider applicability and improve other training-free conditional inference methods in the future. Since the augmentation is not dependent on the method used it has the potential to be adopted by other works in the future.

### Weaknesses
 - The topic looks promising. Solving the inverse problem with less compute is important.
- The performance gap between existing method looks good.

 - The motivation of proposed method is "fast sampling", but speed comparison to existing method is missing for table 2,3,4. I can only see Figure 6 about the speed, but this is self ablation study. I want see the figure that x-axis = speed / y-axis=performance compared to existing method.

- Can you apply this method on "solving inverse problem with unconditional flow-matching model"?

### Questions
- What is the main difference between the proposed method and MGD? Both algorithms compute the gradient $\nabla_{\hat{x}_t} r(\hat{x}_t, y)$ and add it to $x\_{t-1}$. The proposed algorithm also adds $\nabla\_{\epsilon\_{\theta}(x\_t)} r(\hat{x}_t, y)$ but $\hat{x}_t$ and $\epsilon\_{\theta}(x\_t)$ are related by Eq. 10. It seems like that the gradient $\nabla\_{\epsilon\_{\theta}(x\_t)} r(\hat{x}_t, y)$ is not providing any extra guidance/information for the inference process but is rather used as a proxy to correctly weigh the change of $x\_{t-1}$ to match the constraint at timestep $t-1$. Given the above, could someone reformulate your method as MGD with different weighting?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper propose Dreamguider which solve both linear and non-linear inverse problem. While all the previous work requires to contain back propagation path including the diffusion model, this paper find the way to compute MMSE estimates without diffusion network.

### Strengths
- The topic looks promising. Solving the inverse problem with less compute is important.
- The performance gap between existing method looks good.

### Weaknesses
- The motivation of proposed method is "fast sampling", but speed comparison to existing method is missing for table 2,3,4. I can only see Figure 6 about the speed, but this is self ablation study. I want see the figure that x-axis = speed / y-axis=performance compared to existing method.

- Can you apply this method on "solving inverse problem with unconditional flow-matching model"?

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3
