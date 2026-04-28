# Physics-Informed Diffusion Models

- Decision: Accept
- Avg Score: 5.75
- Scores: 6, 6, 6, 5

## Abstract
Generative models such as denoising diffusion models are quickly advancing their ability to approximate highly complex data distributions. They are also increasingly leveraged in scientific machine learning, where samples from the implied data distribution are expected to adhere to specific governing equations. We present a framework to inform denoising diffusion models of underlying constraints on such generated samples during model training. Our approach improves the alignment of the generated samples with the imposed constraints and significantly outperforms existing methods without affecting inference speed. Additionally, our findings suggest that incorporating such constraints during training provides a natural regularization against overfitting. Our framework is easy to implement and versatile in its applicability for imposing equality and inequality constraints as well as auxiliary optimization objectives.}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes a method which introduces a virtual observable (Rixner & Koutsourelakis, 2021) to the score-matching denoising diffusion training objective (Song et al., 2021). 
The authors provide a theoretical argument (see Appendix A.1) showing that, in ideal settings, this enables the diffusion model to recover the true distribution while enforcing physical constraints. 
Additionally, the authors theoretically motivate a simplification of the augmented objective (see Appendix A.3), ignoring the likelihood ratio, and justify this by assuming that ongoing optimization will reduce the introduced bias. 
The authors present experiments on fluid flow (Darcy flow) and structural optimization (topology optimization). 
These experiments indicate improved reduction in PDE residual compared to state-of-the-art methods and provide evidence that the additional training objective does not compromise data likelihood and may instead serve as an effective regularizer against overfitting.

### Strengths
1. Originality: The paper incorporates previous work on virtual observables (Rixner & Koutsourelakis, 2021) to train denoising diffusion models with embedded physical constraints. In the realm of physics-informed diffusion models, this approach contrasts with methods like PG-Diffusion (Shu et al., 2023) and CoCoGen (Jacobsen et al., 2023), which incorporate physics via auxiliary models or adjustments post-training.
2. Quality: The paper provides coherent theoretical arguments for the application of virtual observables in diffusion models (see Appendix A.1 and A.3) and implements an experimental setup on benchmark tasks, following configurations from established related work (see Appendix A.6.2 and A.6.3).
3. Clarity: The paper is clearly structured and well-written.
4. Significance: The method could enhance generative modeling for scientific applications by producing physically consistent samples, as shown in fluid dynamics and structural optimization benchmarks.

### Weaknesses
1. Clarity: The approach is substantially grounded in prior work on virtual observables (Rixner & Koutsourelakis, 2021), making the contribution more incremental than suggested. 
Greater clarity would be achieved by explicitly framing the contribution as an adaptation of this framework tailored for denoising diffusion models.

### Questions
The augmentation of the denoising diffusion model objective to incorporate virtual residuals represents a noteworthy contribution to the field. However, it would enhance clarity and rigor if the authors explicitly positioned this adaptation as their primary theoretical contribution.

### Soundness
3

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
4

### Summary
The paper aims to model random variables using diffusion-based models on data spaces, whose samples follow certain physical constraints described by partial differential equations (PDEs) and boundary conditions. Specifically, these PDE constraints are expressed in the form $\mathcal{F}(x) = 0$ for $x$ in the domain $\Omega$, where $\mathcal{F}$ is a differential operator governing the physical constraints. For example, consider a data space where each data point represents a uniform discretization over a fixed time interval of projectile motion; in this scenario, each data point must comply with the physical laws related to gravity. The paper proposes a regularization objective applied to the generated samples of the diffusion-based models., which does not alter the common training objectives of the models.

To incorporate the physical constraints, the paper introduces a residual term defined as $R(x) = \mathcal{F}(x)$. They model the likelihood of the residual given $x$ as $p(r \mid x) = N(r; R(x), \sigma^2 I)$, where $N$ denotes the normal distribution and $\sigma > 0$ is a positive constant. The training process aims to maximize the likelihood $p(r = 0 \mid x)$, effectively encouraging the residuals to be zero and thus satisfying the physical constraints. With this likelihood function, the paper proposes maximizing the expected log-likelihood of the residuals with respect to the model, in addition to maximizing the evidence lower bound (ELBO) of the diffusion-based models.

Since computing the expected log-likelihood of the residuals with respect to the model is computationally expensive—requiring sampling from the diffusion-based models—the paper proposes sampling $x_0$ for a given $x_t$ instead of generating samples from the prior.

The paper demonstrates the effectiveness of the proposed method through various experiments.

----
Updated the soundness from 3 to 4 and the presentation & contribution from 2 to 3 after the authors' rebuttal.

### Strengths
The paper introduces an interesting approach by modeling random variables using diffusion-based models that adhere to physical constraints defined by PDEs and boundary conditions. This integration of physical laws into the modeling process through a regularization objective is particularly compelling. This novel framework has some potential to positively influence the machine-learning community, especially in domains where physical consistency is essential. 

The demonstrated effectiveness across various experiments underscores the practicality and impact of the proposed method.

### Weaknesses
The paper would benefit from significant improvements in writing clarity. 

To fully understand and summarize the contributions, I had to reference several previous studies, which suggests that the paper is not entirely self-contained. For instance, lines 127-129 appear to cover a key concept, yet there is no explanation provided, nor is the term $R$ properly defined. Specifically, the paper introduces a residual term $R(x) = \mathcal{F}(x)$ but doesn't explicitly define the differential operator $\mathcal{F}$ or provide examples of how it is constructed for different PDEs. This lack of clarity makes it challenging to understand how the method is applied in practice. The description of the likelihood function $p(r \mid x) = N(r; R(x), \sigma^2 I)$ also lacks sufficient detail on how the residual $r$ is obtained or what its dimensionality is, given that $R(x)$ is a function of $x$ which can be high-dimensional.

Additionally, there are ambiguities in the notation—for example, it’s unclear if $x$ in Section 2.1 is intended to represent the same variable as $\xi$ in Equations (5) and (6), raising questions about consistency. This lack of notational consistency makes it difficult to follow the mathematical derivations and understand the relationships between different variables. Furthermore, the relationship between the data point $x_0$ and the spatial coordinates $\xi$ is not clearly established, leaving the reader to infer how the physical constraints are applied to the data space. 

Furthermore, the abstract is overly vague, making it difficult to grasp the paper’s main content and contributions at a glance.

### Questions
N/A

### Soundness
4

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
4

### Summary
The authors proposed a new strategy to generate physical data under the physical constraints by directly combing the training target of diffusion models and the physical PDEs in the loss function. The data used in PDEs are estimated via one-step score-based mean estimation or two-step DDIM sampling. The authors compared their method to other physical-guided machine learning models in the darcy flow generation and topology optimization tasks, which shows their models outperformed others in conforming to the physical constraints but underperformed in other criteria.

### Strengths
Compared to previous methods [1][2] that integrates physical constraints by projecting the PDE residuals to the latent space, the authors introduced the PDE residuals as virtual observables and explicitly optimized on the physical constraints.

[1] Christian Jacobsen, Yilin Zhuang, and Karthik Duraisamy. CoCoGen: Physically-Consistent and Conditioned Score-based Generative Models for Forward and Inverse Problems. pp. 1–25, 2023.

[2] Dule Shu, Zijie Li, and Amir Barati Farimani. A physics-informed diffusion model for high-fidelity flow field reconstruction. Journal of Computational Physics, 478:111972, 2023.

### Weaknesses
In their experiment, although their proposed method performs best in satisfying physical constraints, it shows suboptimal performance on other metrics. Moreover, the approach of adding a physical residual term to the loss function is straightforward and offers limited innovation.

### Questions
1.	What advantages does the proposed method have in topological optimization task compared to the traditional methods (SIMP)? For optimization problems, it does not seem to be necessary to generate a distribution. The authors mentioned that their method can also provide the displacement fields. Is it a feature that exclusively can be obtained with their method? Could the authors explain in detail?
2.	How does the sampling step in the sample estimation (DDIM) affect the performance? Will the performance improve with more steps?
3.	How much will the scaling c in the loss function affect the performance? Could the authors show the experiment results of different scaling c?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper employs Diffusion Models to satisfy constraints, with applications to Partial Differential Equations (PDEs) and Topology Optimization. The diffusion model is trained using a combination of a data-free loss term and a data-driven diffusion loss.

### Strengths
The setting of combining a data-based diffusion loss with a data-free diffusion loss in general is an interesting question.

### Weaknesses
1. The core contribution of this paper is the use of Diffusion Models to sample from an unnormalized target distribution. However, there is extensive prior work on this topic (see [1], [2], [3], [4]), which the authors have not cited. The paper's approach includes an additional Physics-Informed Neural Network (PINN) regularization loss, which can be considered a special case of Eq. 6 in Sanokowski et al. [4], where the temperature is set to $0$. The authors of [4] emphasize that temperature regularization, combined with annealing, is crucial for avoiding local minima (see Fig. 2, middle panel, in their paper). Thus, the current approach may perform poorly in the absence of a supervised loss term.

   Additionally, the "Noise Distribution" described in Eq. 12 of the paper is essentially the "Annealed Noise Distribution" introduced in Sec. 3.2 of [4]. The authors should also cite [5], which discusses training neural networks with PINN losses in a generative manner without using any data.

   The authors could address these concerns by properly citing these works in the related literature. Furthermore, the proposed method might benefit from adopting the loss function used in [4] and incorporating annealing during training. It would be interesting to study the combination of a data-driven loss with a data-free annealing-based loss.

2. Experimental Evaluation:
The experimental evaluation is limited and should be expanded to cover a broader range of settings.

### Questions
1. **Clarification Needed:**  
   The paper states:  
   > "Since the remaining derivations hold true for both estimation techniques, we introduce \(x_0^*\) to denote either the mean or the sample estimate on which the residual is evaluated."

   The rationale for introducing \(x_0^*\) is unclear. What advantage does this provide? Why not directly sample \(X_0\) from the model? How is \(x_0^*\) computed?

Can you make an ablation on this choice?

2. How does your method perform when the data-based loss term is removed?

### Soundness
2

### Presentation
3

### Contribution
2
