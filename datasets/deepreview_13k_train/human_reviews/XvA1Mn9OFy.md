# Generalization Aware Minimization

- Decision: Reject
- Scores: 6, 6, 6, 3, 3

## Abstract
Sharpness-Aware Minimization (SAM) algorithms have effectively improved neural network generalization by steering model parameters away from sharp regions of the training loss landscape, which tend to generalize poorly. However, the underlying mechanisms of SAM are not fully understood, and recent studies question whether its bias toward flatter regions is why it improves generalization. In this work, we introduce Generalization-Aware Minimization (GAM), a generalized version of SAM that employs multiple perturbation steps instead of SAM's single-step perturbations. This allows GAM to directly guide model parameters toward areas of the landscape that generalize better. We show that the expected true (test) loss landscape is a rescaled version of the observed training loss landscape and demonstrate how GAM's multiple perturbative updates can be designed to optimize this expected true loss. Finally, we present a practical online algorithm that adapts GAM's perturbative steps during training to improve generalization, and we empirically validate its superior performance over SAM on benchmark datasets. We believe GAM sheds light on the generalization improvements of sharpness-based algorithms and can inspire the development of optimizers with even better generalization.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces Generalization-Aware Minimization (GAM), an optimization algorithm that aims to improve neural network generalization by optimizing for expected test loss. The authors extend the Sharpness-Aware Minimization (SAM) concept by using multiple perturbation steps and adaptive perturbation sizes. The key theoretical contribution shows that the expected test loss landscape is a rescaled version of the training loss landscape for quadratic losses. The method consistently outperforms SAM and standard SGD on several benchmark datasets.

### Strengths
- Provides a rigorous theoretical analysis of the relationship between training and test loss landscapes

- Offers insights into why SAM works, moving beyond the simple "flat minima" explanation

- Shows consistent improvements over baseline methods

### Weaknesses
 - The method requires multiple perturbation steps, each involving forward and backward passes. While the authors dismiss computational concerns with a brief statement that "the overhead remains manageable," this deserves more thorough treatment. The paper would benefit from a detailed analysis of computational costs, especially for larger models or when more perturbation steps are needed. Specifically, the authors should provide a breakdown of the time complexity of each perturbation step and how it scales with model size and input dimensionality. Furthermore, a comparison of wall-clock time against standard SGD and SAM on various hardware configurations would be beneficial to understand the practical implications of the proposed method.

- Theorem 1, a cornerstone of the paper's theoretical contribution, is preceded by 14 lines of dense assumptions without adequate explanation. The presentation would be more accessible if the authors could provide clear motivation and intuition for critical assumptions and better explain the theorem's implications and practical significance. For example, the assumption of quadratic loss functions should be justified in the context of non-convex neural network loss landscapes. Additionally, the implications of rotational and location invariance should be explained more clearly, especially how these assumptions might limit the applicability of the theory to real-world scenarios.

- While the theory is primarily based on quadratic loss assumptions with convex landscapes, the authors do address this limitation
The extension to non-quadratic losses in the practical considerations section provides important context.

### Questions
- Could you explain more intuitively what it means for "the expected test loss landscape is a rescaled version of the training loss landscape"?  Why this is important for generalization?


- Have you explored any techniques to reduce the computational cost while maintaining the benefits of multiple perturbation steps?

### Soundness
2

### Presentation
2

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
This paper introduces Generalization-Aware Minimization (GAM), which is a generalized version of SAM which employs multiple perturbation steps (whereas SAM employs a single-step perturbation). GAM directly optimizes for the expected test loss in order to achieve better generalization.

### Strengths
1. The paper is written clearly. Theoretical insights are supported empirically.
2. The theoretical insights can provide valuable insights into how sharpness-based algorithms work.

### Weaknesses
1. While I agree that the performance gains in table 1 illustrate that GAM > SAM > SGD, the relative gains of GAM over SAM seem relatively small.
2. It would be nice to see some results in other modalities (e.g., maybe some language related tasks. Aside: for language related tasks, people care about OOD performance as well, so maybe expected test loss is not as meaningful?)

### Questions
As suggested in the paper, the curvature of the expected test loss is a rescaled version of train loss, aligned along the same principle directions. Is there any connection to CR-SAM: Curvature Regularized Sharpness-Aware Minimization (https://arxiv.org/abs/2312.13555)?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a new optimization procedure, Generalization-Aware Minimization (GAM), based on the analysis which shows that the curvature of the true loss landscape is a rescaled version of that of the observed loss landscape. Multiple perturbation step is used to calculate the gradient update such that it is a good approximation of the gradient update in the true loss landscape. Experiments on small-scale datasets show the effectiveness of GAM.

### Strengths
1. The theoretical analysis looks plausible, with a clear explanation of the rationale of assumptions. 

2. The idea of multiple perturbation steps, and learning a perturbation coefficient via the difference between the perturbed gradient and the original gradient looks interesting.

### Weaknesses
1. More explanation about understanding why the true loss landscape is a rescaled version of the observed loss landscape should be introduced. When $D(\tilde{\Lambda})=\tilde{\Lambda}$, the analysis seems trivial. Intuition or examples of the when and why $D(\tilde{\Lambda})$ differ from $\tilde{\Lambda}$, and what implications this has for the optimization process can be given.

2. I would like to see more discussion on the effect of batch size, perturbation step, and $\epsilon$, as these parameters affect GAM's approximation of the true loss landscape. Analysis of how they impact the trade-off between computational cost and performance will gives a better understanding of  the effectiveness of the proposed GAM.

3. Experiments are not convincing enough. The baseline experiment can be more complete. it seems that as $\gamma$ increases, SAM's performance also increases. GAM should be compared to SAM with larger $\gamma$. I understand that it is computationally intensive to calculate the gradient $d$ and $\gamma$. However, experiments on larger architecture and datasets are expected to show GAM's effectiveness (refer to the empirical evaluation of SAM [1]).

### Questions
1. In Appendix A, how does (15) come out? It is not clear why $\theta^*$ is eliminated. 
2. Please give more explanation of equation 7, especially on $D(\tilde{\Lambda})$. 
3. How would batch size, perturbation step, and $\epsilon$ affect the empirical performance of GAM? Ablation studies on these parameters will be helpful.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper finds that the test loss landscape can be regarded as a rescaled version of the training loss landscape. Based on this finding, this paper proposes a novel training strategy called Generalization-Aware Minimization (GAM). This strategy aligns the training loss gradient with the test loss gradient through multiple perturbations, guiding the model parameters towards region which has better generalization, thereby improving performance.

### Strengths
Originality: 

The paper seems original. This paper theoretically demonstrates that for quadratic loss functions, the test loss landscape is a rescaled version of the training loss landscape. Moreover, this paper proposes that the test loss gradient can be obtained from the training loss gradient through multiple perturbations. 

Significance:

The perspective of this paper is meaningful.

### Weaknesses
1. **Insufficient experiments**. The experiments are conducted only on three small datasets (i.e., MNIST, CIFAR-10, and SVHN) and three models (i.e., MLP, CNN, and WN), **lacking experiments on commonly used models** (e.g., ResNet, ViT). The absence of experiments on more complex architectures and larger datasets limits the generalizability of the findings. Specifically, the paper does not demonstrate the efficacy of the proposed method on models with skip connections or attention mechanisms, which are prevalent in modern deep learning.

2. **Marginal improvement**. Despite introducing significant computational complexity, the gains provided by GAM are not very evident. The reported improvements are not substantial enough to justify the added computational cost, especially when compared to simpler optimization techniques. The paper needs to show more significant performance gains to demonstrate the practical value of the proposed method.

3. **Computation cost**. The computation cost introduced by GAM is significant and cannot be overlooked. The multiple perturbation steps required by GAM lead to a substantial increase in training time, making it less practical for large-scale applications. A detailed analysis of the computational overhead compared to standard optimization methods is needed.

4. **Poor writing**.
For example,

Line 159: The vertical relationships are not clearly defined, and '$p$' is not defined here.

Line 264:  I suggest that the authors clarify the definition of $\Delta$ in the main paper.

Line 409: "$\gamma_1 \in $ 0.001, 0.01, 0.1" should be "$\gamma_1 \in $ {0.001, 0.01, 0.1}".

### Questions
1. Could you provide more comprehensive experimental results, such as those on ResNet and ViT?

2. Could you provide an ablation study and analysis on the GAM steps $T$, discussing how the size of $T$ affects the model's performance?

3. How was the discrepancy function used in the method determined?

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposed Generalization Aware Minimization (GAM), a generalized version of SAM. The method were grounded on two theorems where the first theorem presents the relationship between the curvature of the general and empirical losses, and the second theorem shows a sequence of transformations that transform the Hessian of the training loss to that of the test loss. The method were tested on CIFAR10, CIFAR100, SVHN using some architectures including

### Strengths
The algorithm is based on an interesting theoretical framework that could motivate new insights. Specifically, Theorem 1 demonstrates the relationship between the curvature directions of expected and training losses. Additionally, Theorem 2 presents a series of efficient transformations that align the Hessian of the training loss with that of the test loss. Even though there were certain limitations with the theoretical analysis, I believe that if the limitations were addressed properly, these insights could demonstrate potential applications to various domains.

### Weaknesses
Despite the novel insights from the theory, the theoretical results have certain limitations, notably that they are restricted to scenarios where losses are quadratic. While Section 3.4 mentions that the approach could be extended to general loss functions using local quadratic approximations, the analysis would benefit from a deeper investigation of how these results generalize to broader loss functions and what additional assumptions might be necessary for such extensions. Specifically, the paper should address how the curvature of the local quadratic approximation relates to the true curvature of the loss function, and how this approximation affects the generalization guarantees. Additionally, there may be an issue with Theorem 1; further details are provided in the Questions section.

On the other hand, the experimental evaluation is limited and could be substantially improved. The experiments were conducted on a narrow set of datasets and older architectures, and the method only demonstrates less than a 1% improvement, which is relatively minor. Broadening the scope to include larger datasets, such as CIFAR-100, and more modern architectures, such as WideResNet [1] or EfficientNet [2], would make the experimental results more robust and impactful. Furthermore, the paper lacks an analysis of the computational overhead introduced by the proposed method, which is crucial for practical applications. The paper should also include a comparison with other state-of-the-art generalization techniques to better contextualize the performance of the proposed method.

### Questions
Here are a few questions I have for the authors:

+ There might be a substantial issue with Theorem 1, where the statement appears somewhat trivial. Specifically, for any values $x$ and $y$ in general, it’s possible to express  $\mathbb{E}[x|y]$ as a function of  $y$, allowing us to set $D = 0$ and write $\mathbb{E}[L(\theta) | \tilde{\theta}^*, \tilde{M}, \tilde{c}] $ as a scalar function of \$\tilde{\theta}^*, \tilde{M}, \tilde{c}$, hence make the result of this theorem trivial. Can you clarify the non-trivial aspects of this theorem, for instance, are there any specific constraints on $D$ or $\tilde{c}$?
+ Could you clarify with a concrete example or a mathematical formulation showing that SAM can be derived as a special case of GAM? I believe that including a brief explanation of this relationship would enhance the clarity of the contribution of the paper.
+ Could you elaborate on the meaning of Equations (16) and (17)? Specifically, does this mean that the right-hand side of Equation (15) is equivalent to both Equations (16) and (17)?
+ Can you provide the results on WN or clarify why these results on WN were omitted?
+ I am also interested in the performance of GAM under different hyperparameter settings. It would be useful to include the details on the sensitivity of GAM with respect to the key hyperparameters including $\epsilon$ and the number of GAM steps $T$.


**References:**

[1] Zagoruyko, S., & Komodakis, N. (2016). Wide Residual Networks. In Proceedings of the British Machine Vision Conference (BMVC) 2016.

[2] Tan, M., & Le, Q. V. (2019). EfficientNet: Rethinking Model Scaling for Convolutional Neural Networks. In Proceedings of the 36th International Conference on Machine Learning (ICML) 2019.

### Soundness
2

### Presentation
3

### Contribution
2
