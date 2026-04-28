# Multidimensional Trajectory Optimization for Flow and Diffusion

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 5, 6, 5

## Abstract
In flow and diffusion-based generative modeling, conventional methods rely on unidimensional coefficients for the trajectory of differential equations. In this work, we first introduce a multidimensional coefficient that generalizes the conventional unidimensional coefficient into multiple dimensions. We also propose a new problem called multidimensional trajectory optimization, which suggests a novel trajectory optimality determined by the final transportation quality rather than predefined properties like straightness. Our approach pre-trains flow and diffusion models with various coefficients sampled from a hypothesis space and subsequently optimizes inference trajectories through adversarial training of a generator comprising the flow or diffusion model and the parameterized coefficient. To empirically validate our method, we conduct experiments on various generative models, including EDM and Stochastic Interpolant, across multiple datasets such as 2D synthetic datasets, CIFAR-10, FFHQ, and AFHQv2. Remarkably, inference using our optimized multidimensional trajectory achieves significant performance improvements with low NFE (e.g., 5), achieving state-of-the-art results in CIFAR-10 conditional generation. The introduction of multidimensional trajectory optimization enhances model efficiency and opens new avenues for exploration in flow and diffusion-based generative modeling.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents a novel approach to trajectory optimization in generative models by introducing Multidimensional Trajectory Optimization (MTO). This method extends traditional flow and diffusion models by employing multidimensional coefficients, optimizing the trajectories of differential equations based on final sample quality rather than predefined trajectory shapes. The authors combine this with adversarial training to improve generative performance. The approach is validated across several datasets and generative models, with the results showing improvements in performance (e.g., CIFAR-10) with low function evaluations (NFEs). The proposed method outperforms or matches the state-of-the-art models in terms of quality, with a focus on optimizing the efficiency of the inference process.

### Strengths
**1. Interesting Introductions of the Multidimensional Coefficient**: The core innovation of the paper lies in the introduction of a multidimensional coefficient for trajectory optimization. This new formulation allows for more flexible and adaptive trajectories in flow and diffusion-based generative models, potentially improving generative model performance in a way that traditional unidimensional coefficients cannot.

**2. Comprehensive Empirical Validation**: The authors conduct extensive experiments on both synthetic 2D datasets and high-dimensional datasets like CIFAR-10, FFHQ, and AFHQv2. The experimental results demonstrate that MTO provides clear performance improvements, particularly with lower NFE, showcasing its practical benefits for high-quality sample generation.

### Weaknesses
 **1. Incremental Contribution and Lack of Novelty**: While the multidimensional coefficient is an interesting extension of traditional trajectory optimization, adversarial training—the method used to optimize these trajectories—has already been explored in previous works (e.g., Adversarial Diffusion Distillation and Consistency Trajectory Models). The primary novelty in this work lies in the multidimensional coefficient rather than the adversarial training component itself. However, after a careful reading of the paper, I think the few-step generation with a multidimensional coefficient seems like a direct generalization of single-step generations such as CTM, UFOGen, etc, with incremental contributions. Another weakness is that the similar one-step generative model such as GDD and GDD-I on CIFAR10-unsound in Table 2, and results in Tables 3 and 4 outperform MTO models with up to 5 generation steps. This makes the contribution and practical performances of MTO questionable. The authors should more explicitly highlight how their method differs from and improves upon these existing adversarial training approaches. A more thorough discussion of this relationship would clarify the unique contributions of this paper.

**2. Clarity and Accessibility**: Some of the mathematical formulations, particularly those related to the multidimensional coefficients and their integration into the trajectory optimization process, may be challenging for readers unfamiliar with the specifics of generative models or differential equations. Including additional illustrations or intuitive explanations could improve the accessibility of the work. Additionally, clearer descriptions of the adversarial loss function and its interaction with the multidimensional coefficients would help readers better understand the core mechanics of the method.

**3. Limitations and Theoretical Insights**: The paper briefly mentions the lack of a theoretical foundation for the effectiveness of MTO. This could be addressed by offering some initial theoretical insights. Discussing the computational complexity of training models with multidimensional coefficients and potential limitations in scalability would also be valuable.

**4. Insufficiently related works**: Another weakness of the paper is the insufficient presentation of related works. The few and one-step diffusion distillation is a pretty mature research direction. However, the author fails to mention a lot of well-established approaches such as DMD [1], UFOGen [2], Diffusion-GAN [3], Diff-Instruct [4], iCT [5], GET-onestep [6], TRACT [7], etc. Besides, the authors compare MTO   on FFHQ and AFHQ datasets with a limited comparison with broader domains of other few-step generative models. I am curious why the authors do not conduct experiments on the well-established ImageNet-64 generation benchmark. 

### Questions
**1.** What is the intuition of the $L(\theta)$ objective in Equation (14). 

**2.** I think it would be good if the authors could show the performances on the ImageNet64 benchmark.

**3.** Is MTO a direct generation of diffusion-induced GAN? What is the technical novelty behind MTO?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a learning-based method to optimize the coefficients used in constructing the forward processes of flow- or diffusion-based models. When combined with an adversarial training objective, this method performs well on one benchmark dataset. The approach involves a two-stage process: pretraining followed by simulation-based tuning.

### Strengths
1. Extensive experiments were conducted on some of the latest models.
2. The method is easy to understand, and the writing is clear.

### Weaknesses
1. **Flow Matching Results**: If possible, please provide results on the image dataset based on the flow-matching model.

2. **Image Dataset Experiment with $N=5$**: In the image dataset experiment, $N=5$ was selected, seemingly for efficiency in image generation (simulating Equation (13)). Is this correct? Can a different sampler or time scheduler be used to draw samples after training?

3. **Ablation Study Findings**: The ablation study shows that EDM-$γ$ + Adv. $\theta$ achieves comparable performance. This adversarial objective was previously proposed and appears to be the critical component, rather than the proposed trajectory optimization coefficients.

4. **State-dependent Multidimensional Coefficients**: Can the multidimensional coefficients also depend on the state $x(t)$?

5. **Optimization of the $\gamma$ Model**: The $\gamma$ model is optimized only at specific time schedules (used in Equation (13)) during the second-stage training. Does this imply that the inference schedule used during training must match the schedule used during sampling?

6. **Training Efficiency in Simulation Dynamics**: Please include a discussion on the training efficiency.

**Writing Adjustments**:

- Verify the correctness of $\gamma_0(T)$ on the right-hand side of Equation (8).

### Questions
See above.

### Soundness
3

### Presentation
3

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
This paper proposes a novel multi-dimensional parameterization of diffusion/flow coefficients along with an adversarial learning objective to optimize the sample trajectories. Experiments on a synthetic dataset and several real-world image datasets are conducted to verify the effectiveness of the proposed method.

### Strengths
- The idea of learning multi-dimensional diffusion/flow coefficients is novel. The proposed parameterized family of the coefficients not only ensures the boundary condition but also permits efficient learning, as suggested by the empirical results. I could imagine follow-up work that further explores the design space.  

&nbsp;

- The experimental results look promising. The proposed method consistently achieves lower Wasserstein distances in the synthetic case and is on par with or slightly better on the challenging real-world image generation tasks.

&nbsp;

- The paper is clearly written, except that some technical details are sparse (possibly due to the space limit).

### Weaknesses
 - For a better understanding of the design of the adversarial loss, I’d like to hear authors’ feedback on the following questions. Moreover, it would be great if the authors could improve the writing in Section 4.4.

  1) The loss $L_{\psi}$ in Eq. (14) is also a function of $\phi$ and $\theta$ since it takes generated samples as input. Does the notation $L_{\psi}$ mean that the gradient is stopped so that this loss is only with respect to $\psi$? Similar questions apply to $L_{\phi}$ and $L_{\theta}$. This part is not explained and can not be deduced from Algorithm 1 since Line 12 of Algorithm 1 is also vague.

  2) Minimizing the loss $L_{\psi}$ with respect to $\psi$ encourages the discriminator $D_{\psi}$ outputs $\ge 1$ value for $x_0 \sim \rho_0$ and $\le -1$ value for $x_1 \sim \rho_1$. Minimizing the loss $L_{\phi}$ with respect to $\phi$ encourages the generator to make the discriminator output values for $x_1 \sim \rho_1$ that are as large as possible. This contradicts the effect of minimizing $L_{\psi}$, which makes sense following the adversarial principle. However, minimizing $L{\theta}$ is hard to interpret. To follow the adversarial principle, i.e., $L_{\theta}$ and $L_{\psi}$ are contradictory, one would hope the model $H_{\theta}$ makes the discriminator $D_{\psi}$ outputs $\le 1$ value for $x_0 \sim \rho_0$. But the current design actually encourages the discriminator $D_{\psi}$ output value as large as possible for $x_t$. Can you explain the rationale of the current design?

&nbsp;

- While optimizing the coefficients $\gamma$ via the generator $G$, it seems that backpropagation through the ODE solver is inevitable. This is also shown in Fig. 3. Given the high computational cost, could you comment on the scalability of your method?

&nbsp;

- In the pretraining stage, how exactly are randomly sampled trajectories obtained? Do you still use the proposed parameterized family of coefficients $\gamma$ in this stage? If so, which parameters are set to random, and what distributions do they follow? How do you ensure the pre-training does not degrade performance much and effectively explores the parameter space?

&nbsp;

- The authors do not explain the design choice of the discriminator $D_{\psi}$ in Section 4.4 when it was first introduced.

&nbsp;

- Can you discuss the motivation for using hinge loss in the adversarial training in more detail? The authors just follow the previous work in GAN training without giving motivation.

&nbsp;

- In Section 5.2, the authors mention that the NFE of the proposed method is 6 (+1 for $\gamma_{\phi}$). What exactly does this mean? Why “+1 for $\gamma_{\phi}$” rather than using learned $\gamma_{\phi}$ through the whole sampling? 

&nbsp;

- In Table 2-4, when comparing with other distillation methods, it would be more fair to run other methods under the same NFE. For example, how do CD and CTM perform with 5 or 6 NFE?

&nbsp;

- It would be great to add some comments in the caption of Figure 2 to help better explain the difference and illustrate the idea.

### Questions
Please see my comments in the weakness section.

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
This paper proposes an extension of flow/diffusion models which allows for the interpolant coefficient to now be multi-dimensional, i.e. with one coefficient per data dimension. The authors propose to optimize these coefficients to obtain learnable trajectories in order to improve model performance. To do so, a specific parametric form for the trajectories is specified, followed by adversarial training. The proposed method is evaluated on a few low-dimensional image datasets.

### Strengths
- The idea of having learnable trajectories is interesting
- The experiments show that the learnable trajectories can indeed give you better performance

### Weaknesses
 - The paper is a little hard to read, and could generally benefit from additional exposition and improved clarity.
     - For example, in definition 1, what is the reason behind the boundary conditions on $\gamma$? This might generally be clear to readers well-versed in flows and diffusion, but explaining this would help the clarity in the paper. 
     - Another place where clarity is lacking is that in Def. 1 the coefficients $\gamma$ are not allowed to depend on $x_1$, but only a few lines later the authors now allow $\gamma$ to depend on $x_1$. 
     - Or, in lines 125, the authors use $\rho_1$ as the noise distribution for EDM, but then in line $130$ are using $\rho_T$ to denote the noise distribution.
     - I found the description of the adversarial training in Section 4.4 to be generally unclear, e.g. a discriminator $D_\psi$ is introduced in the equations but never really explained.
- One of the major benefits of flow and diffusion models is that they are simulation-free during training, making training generally straightforward to carry out. This paper moves in the opposite direction and now requires not only simulation from the model, but also a fairly complex adversarial setup. I would be interested in seeing an evaluation of the training cost of the proposed method, which I'd guess is significantly higher than other flow/diffusion methods. 
- The datasets considered are all quite low-dimensional (2d synthetic datasets, CIFAR-10, and some 64x64 image datasets). This makes me wonder if the proposed method is scalable to higher-dimensional datasets.

### Questions
- The proposed method generally performs worse than methods based on diffusion + distillation in Tables 3 and 4, despite having a 5x higher NFE than these baselines. Do the authors have an explanation for why this is the case?
- There is some existing work on learning trajectories in diffusion models. e.g. [Where to Diffuse...](https://arxiv.org/abs/2302.07261) and [Neural Flow Diffusion Models](https://arxiv.org/abs/2404.12940v2). What is the relationship between these methods (and other existing learnable diffusions) and this work?

### Soundness
3

### Presentation
2

### Contribution
2
