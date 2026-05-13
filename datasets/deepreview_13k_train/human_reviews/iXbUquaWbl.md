# End-to-end Learning of Gaussian Mixture Priors for Diffusion Sampler

- Decision: Accept
- Scores: 6, 8, 6, 6

## Abstract
Diffusion models optimized via variational inference (VI) have emerged as a promising tool for generating samples from unnormalized target densities. These models create samples by simulating a stochastic differential equation, starting from a simple, tractable prior, typically a Gaussian distribution. However, when the support of this prior differs greatly from that of the target distribution, diffusion models often struggle to explore effectively or suffer from large discretization errors. Moreover, learning the prior distribution can lead to mode-collapse, exacerbated by the mode-seeking nature of reverse Kullback-Leibler divergence commonly used in VI.
To address these challenges, we propose end-to-end learnable Gaussian mixture priors (GMPs). GMPs offer improved control over exploration, adaptability to target support, and increased expressiveness to counteract mode collapse. We further leverage the structure of mixture models by proposing a strategy to iteratively refine the model through the addition of mixture components during training. Our experimental results demonstrate significant performance improvements across a diverse range of real-world and synthetic benchmark problems when using GMPs without requiring additional target evaluations.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a novel approach to diffusion-based sampling that incorporates end-to-end learnable Gaussian Mixture Priors (GMP), offering a more expressive alternative to conventional Gaussian priors. The flexibility of GMP mitigates mode collapse, enhances exploration capabilities, and reduces the need for extensive diffusion steps by alleviating non-linear dynamics. The authors also propose an Iterative Model Refinement (IMR) strategy, progressively increasing model complexity to optimize performance on high-dimensional, multi-modal targets. Extensive experiments demonstrate that using GMP in place of Gaussian priors in existing diffusion-based sampling methods achieves improved sampling performance and outperforms previous methods across synthetic and real-world datasets.

### Strengths
- The paper is well-structured, first identifying the limitations of Gaussian priors in diffusion-based sampling and then logically progressing to propose end-to-end learnable Gaussian Mixture Priors (GMP) as a solution. Each step in this argument is clearly justified, supported by sufficient background information and helpful illustrations, making it easy for readers to follow.

- The experimental design effectively supports the theoretical claims, providing empirical evidence of the advantages offered by GMP over traditional Gaussian priors. Additionally, the comprehensive review of related work and background offers readers a useful overview of recent developments in this field.

- The proposed method enables end-to-end learning of the prior distribution, allowing existing diffusion-based sampling methods, which previously relied on fixed naive priors, to benefit from a more optimized starting prior. This adaptability enhances sampling performance and broadens the applicability of the approach across various diffusion-based sampling methods.

### Weaknesses
 - Although GMP can achieve competitive performance with a single Gaussian prior using fewer steps, high-dimensional data often require more complex dynamics and an increased number of components to handle multiple modes effectively. As both the number of components $K$ and steps $N$ grow, the computational cost increases substantially, raising concerns about the scalability of this approach for even higher-dimensional applications in the future. Specifically, the computational cost scales linearly with both $N$ and $K$, which could become prohibitive for very large models or datasets. Furthermore, the memory requirements for storing intermediate results during the diffusion process also increase with $N$ and $K$, potentially limiting the size of problems that can be tackled on available hardware.
- As acknowledged in the paper, there is no clear criterion for determining the appropriate number of mixture components needed for optimal performance. Furthermore, IMR relies on heuristic rules, such as a fixed number of iterations, to add new components, introducing additional hyperparameter tuning requirements for model optimization. The fixed number of iterations for adding new components in IMR lacks a theoretical basis, and it is unclear how this choice affects the final performance. A more principled approach for determining when to add new components, perhaps based on monitoring the convergence of the ELBO or other relevant metrics, would be beneficial.
- Some minor inconsistencies and certain claims in the paper are not fully supported by the experimental results, which would benefit from further clarification. For instance, additional explanation may be needed for the DIS results in Figure 4. Specifically, the observation that DIS-GMP performs worse than DIS-GP across all metrics of sampling quality is not adequately addressed. This outcome contradicts the paper's central claim that GMPs offer an advantage over Gaussian priors. Moreover, while DIS-GMP + IMR shows better Sinkhorn distance and qualitative sampling results, its ELBO and $\triangle$ log Z performance is lower than that of DIS-GP and DIS-GMP, suggesting that ELBO may not be a reliable metric for evaluating sampling performance for multi-modal target distributions.

### Questions
- In Section 5, it seems that the positioning of challenges C1 and C2 may have been reversed. Specifically, in lines 308–310, reducing the complexity of dynamics to minimize the required diffusion steps seems more directly related to the issue identified in the Introduction as C2 (lines 51–53). Conversely, enhancing the exploration capability of diffusion-based sampling methods to cover diverse regions seems more relevant to addressing C1.
- While Figure 6 presents wall-clock time for relatively low-dimensional cases, it would be helpful to understand how computational demands scale in higher-dimensional scenarios. Could you provide an analysis of the computational cost associated with varying the number of mixture components $K$ and diffusion steps $N$ for a more formal comparison? (e.g. Big-O notation)
- How does estimated memory consumption vary with changes in $K$ and $N$?
- In Figure 4, DIS-GMP performs worse than DIS-GP across all metrics of sampling quality. This outcome seems contrary to what the paper suggests; how might this be explained? Furthermore, while DIS-GMP + IMR with progressively learned components shows better Sinkhorn distance and qualitative sampling results, its ELBO and $\triangle$ log Z performance is lower than that of DIS-GP and DIS-GMP. This observation suggests that ELBO may have limitations in evaluating sampling performance for multi-modal target distributions (as also seen in Figure 9).
- Table 2 presents only ELBO results; does the Sinkhorn distance follow a similar trend to what was observed in the Funnel case?
- The IMR approach uses a criterion of adding components every 500 training iterations. Are there any ablation study results regarding this criterion for IMR?

Minor:
- In Equation 31 of Appendix A.1, the term $(-\frac{2}{\sigma^2})^2$ seems to have a sign inconsistency with Equation 32, where the third term should perhaps be positive.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The paper proposes using learned Gaussian mixture priors in diffusion samplers instead of the standard fixed, unimodal Gaussian. The authors experimentally demonstrate the advantages of having a multi-modal prior; better exploration, fewer diffusion steps, and avoiding mode collapse. To effectively train the learned Gaussian mixture prior model, the authors introduce an iterative refinement approach that gradually adds new modes to the prior distribution.

### Strengths
- **Novelty**: The idea of learning a mixture prior in a diffusion process is underexplored and could have significant impact on future works. To the best of my knowledge, there have been few papers that explore a learned prior in diffusion models. Additionally, the idea of gradually adding complexity to the prior is very interesting.
- **Evaluation**: The authors provide adequate comparisons between the proposed method and existing approaches that demonstrate the overall improvements when using the proposed model. The results show that their method better captures the different modes of the distributions learned.
- **Presentation**: The writing is succinct and helps the reader understand the necessary preliminaries before diving into the details of the proposed method. Even with limited prior knowledge of the different diffusion samplers out there, the paper is easy to follow.

### Weaknesses
 - Some more ablations could help with understanding the specific advantages of the proposed method better. One of the issues of the unimodal Gaussian prior that is mentioned is the increased complexity in the learned dynamics. In some examples of Fig. 5 the EES only marginally improves with more modes, making the number of diffusion steps the more impactful hyperparameter. This hints towards the dynamics not being simpler with more modes, as we would expect fewer diffusion steps to also yield good EES in those cases. A more in-depth experiment that demonstrates the differences in dynamics could help ground the overall argument for a mixture prior.

 - For the exploration and mode collapse issues discussed, is it not possible to transform the target data distribution such that its support is covered by a single unit Gaussian, given that you use the knowledge of the support of the true distribution when adding new modes? How much worse is the base DIS compared to the learned and learned+mixture variants under this experiment setting?

### Questions
- For the exploration and mode collapse issues discussed, is it not possible to transform the target data distribution such that its support is covered by a single unit Gaussian, given that you use the knowledge of the support of the true distribution when adding new modes? How much worse is the base DIS compared to the learned and learned+mixture variants under this experiment setting?

### Soundness
3

### Presentation
4

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
This paper proposes an end-to-end learnable Gaussian mixture priors (GMPs) to address challenges in diffusion-based sampling methods including poor exploration, non-linear dynamics and mode collapse. Generally speaking, the paper contains some interesting ideas, and some experimental results are provided to demonstrate the performance improvement of the proposed method.

### Strengths
The paper presents an approach for improving diffusion-based sampling techniques by introducing end-to-end learnable Gaussian Mixture Priors (GMPs). The authors identify three key challenges in diffusion models: lack of exploration capabilities (C1), non-linear dynamics requiring many diffusion steps (C2), and mode collapse due to reverse KL minimization (C3). To address these challenges, the paper proposes GMPs, which offer improved control over exploration, adaptability to target support, and increased expressiveness to counteract mode collapse. Experimental results are provided to demonstrate performance improvement of the proposed methods.

### Weaknesses
The main concern of the paper is that the considered numerical experiments are oversimplified. The authors only considered logistic regression models and the fashion target on the MNIST fashion dataset in experiments. It is well known that diffusion models are widely used for generating samples with complicated priors, such as high-quality real-world images. Yet, from the numeral results provided in the paper, the reviewer cannot see any potential of the proposed method in this respect. As such, it is not convincing to claim that the proposed methodology can indeed solve the problems (C1)-(C3) of the existing diffusion models. Specifically, the experiments lack the complexity to demonstrate the claimed benefits, such as improved exploration and reduced mode collapse. The use of a relatively simple logistic regression model and a target derived from a normalizing flow on Fashion MNIST does not adequately represent the challenges encountered in more complex, high-dimensional sampling tasks. The paper needs to demonstrate the method's effectiveness on more challenging distributions, such as those found in image generation or other complex data modalities, to support the claims made about addressing the limitations of existing diffusion models.

### Questions
1. How can the proposed iterative model refinement (IMR) strategy be further improved to optimize the selection criteria for adding new components and dynamically adjust the number of components during training?

2. As shown in the left side of Figure 4, the proposed IMR strategy seems not work well in all metrics (DIS-GMP, DIS-GMP-IMR), how could this be explained?

3. As introduced in Section 5, the IMR strategy requires to optimize parameters until a predefined criterion is met, how to choose the criterion and how does the criterion affect the training result?

4. The mean of a new added Gaussian component is chosen according to (22), how about the choice of variance?

5. What are the potential limitations or drawbacks of using Gaussian mixture priors compared to other types of learnable priors, and how could these be addressed?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this paper, the authors propose an innovative sampling approach using the framework of controlled diffusions. They address current limitations in diffusion samplers, such as poor exploration, mode collapse, and numerical instabilities, which hinder model effectiveness. To counter these issues, they suggest parametrizing the prior of the backward diffusion process as a Gaussian Mixture Model (GMM). The authors detail how this adjustment can be applied to both denoising diffusions and Langevin diffusions. They introduce an iterative learning procedure that jointly optimizes the control networks and the GMM prior parameters. Through extensive experiments, the authors demonstrate that their approach outperforms traditional diffusion samplers across a wide range of tasks.

### Strengths
- The paper is well written
- The idea of parametrizing the prior seems novel

### Weaknesses
 - Lack of multimodal experiments (while it was the main motivation according to Fig. 1)
- Competing algorithms seems to have been wrongly implemented as the control networks lack the $\nabla \log \pi$ information (according to L927-928)
- Sec 6 only considers metrics known to be unsuited for multimodal distributions (and especially to detect mode collapse C3) as per [1] (cited by the authors)
- The computational procedure is very heavy
- Fig 4 and Fig 9 clearly show that the model mode collapsed as most of the generated images are almost identical.
- It seems like SMC and CRAFT have been unfairly implemented. Indeed, as those algorithms use a different annealing scheme, there are no reasons to keep the same number of intermediate distributions. Moreover, as they are cheaper, this number should be increased.
- The problem of overparameterisation of the GMM (when the GMM as more mode than the target distribution) has two different interpretations between L479-483 and Fig 9.

### Questions
- Why not using the log-variance objective which as proven to be very effective ? [2] (Note that this objective wouldn't require the reparameterization trick on the prior)
- Could you provide an ablation study in a controlled environment (typically sampling Mixture of Gaussian) to actually challenge the procedure and assess that the claims were addressed ?
- How does your algorithm scale with the number of modes $K$ as GMM notoriously showcase numerical instabilities in this scenario ?
- Fig 4 and Fig 9 clearly show that the model mode collapsed as most of the generated images are almost identical. How do you explain this behavior ?
- According to Fig 6, the Funnel sampling procedure (for DIS) took over 5 hours. Is it actually competitive against MCMC samplers like MALA or HMC under the same computational budget ?
- It seems like SMC and CRAFT have been unfairly implemented. Indeed, as those algorithms use a different annealing scheme, there are no reasons to keep the same number of intermediate distributions. Moreover, as they are cheaper, this number should be increased. Could you re-run the experiments with increased budget ?
- Could you compare X-GMP against X-GP but adding the target informed parametrization of the controlled networks ? It seems like it could make a big difference.
- The problem of overparameterisation of the GMM (when the GMM as more mode than the target distribution) has two different interpretations between L479-483 and Fig 9. Could you clarify it ?
- Could you compute mode-collapse aware metrics such as the EUBO (and derivations) or the EMC from [1] ?

[1] Blessing, D., Jia, X., Esslinger, J., Vargas, F., & Neumann, G. (2024). Beyond ELBOs: A Large-Scale Evaluation of Variational Methods for Sampling. In Proceedings of the 41st International Conference on Machine Learning (pp. 4205–4229). PMLR.

[2] Nüsken, N., Richter, L. Solving high-dimensional Hamilton–Jacobi–Bellman PDEs using neural networks: perspectives from the theory of controlled diffusions and measures on path space. Partial Differ. Equ. Appl. 2, 48 (2021). https://doi.org/10.1007/s42985-021-00102-x

### Soundness
4

### Presentation
3

### Contribution
3
