# Truncated Consistency Models

- Decision: Accept
- Avg Score: 6.80
- Scores: 8, 6, 6, 6, 8

## Abstract
Consistency models have recently been introduced to accelerate sampling from diffusion models by directly predicting the solution~(i.e., data) of the probability flow ODE (PF ODE) from initial noise.
However, the training of consistency models requires learning to map all intermediate points along PF ODE trajectories to their corresponding endpoints. This task is much more challenging than the ultimate objective of one-step generation, which only concerns the PF ODE's noise-to-data mapping.
We empirically find that this training paradigm limits the one-step generation performance of consistency models.
To address this issue, we generalize consistency training to the truncated time range, which allows the model to ignore denoising tasks at earlier time steps and focus its capacity on generation.
We propose a new parameterization of the consistency function and a two-stage training procedure that prevents the truncated-time training from collapsing to a trivial solution.
Experiments on CIFAR-10 and ImageNet $64\times64$ datasets show that our method achieves better one-step and two-step FIDs than the state-of-the-art consistency models such as iCT-deep,
using more than 2$\times$ smaller networks. Project page: \href{https://truncated-cm.io/}{https://truncated-cm.io/}

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This work proposes a novel training technique for consistency models by truncating the time intervals into two splits: one is the boundary/denoising part near $t=0$, and the other is the consistency/generation part near $t=T$. By training with a weighted sum of the two objectives and introducing a dedicated proposal distribution for sampling the time, the proposed method beats previous 1-step and 2-step models on CIFAR10 and ImageNet64.

### Strengths
- The paper is well-written and is easy to follow. The math derivations are technically correct.
- The idea of truncating is novel, and the proposed method can further address the training instability of consistency models which are important to the community.
- The empirical results are strong, showing the effectiveness of the method.

### Weaknesses
It is unclear whether the effectiveness is from the truncation or is just from the changing of proposal distribution by focusing more on the boundary parts. Specifically, the major techniques in this paper include two parts:

1. two-stage truncated training to avoid the overtraining of denoising tasks;
2. changing proposal distribution to focus more on the boundary conditions.

However, with only the first method, the training still diverges (L241-L242), which shows that the part 2 seems to be more important. Intuitively, as the supervision signals of consistency training only come from the boundary condition, the model will suffer from error accumulations as t increases from 0 to T. Therefore, focusing more on the boundary parts seem to be a natural idea to address such error accumulations and may be the reason why the proposed method is more stable than previous methods. Given such understanding, it is unclear whether the first part (truncation) is even necessary.

Therefore, this paper does not fully sound to me. It would be great if the author could conduct more rigorous ablations for the part 2, such as:

- Training consistency models by the original loss (i.e. the method used in stage-1) with the improved proposal distribution by focusing more on [0, t']. The optimal proposal distribution may be different from the stage-2 so it should be tuned a little bit for such task. Will the optimal result be comparable to the 2-stage training method?

Besides, there is another minor weakness but I think it does not affect the conclusions in this paper:

- Consistency models include both consistency training (CT) and consistency distillation (CD), but this paper only shows the results of CT. Note that the original CT has the same gradient limit as CD as $\Delta t \to 0$. However, with truncation training, this conclusion will not hold anymore for t near to t'. What is the performance of CD by the truncated method?

### Questions
- Training consistency models by the original loss (i.e. the method used in stage-1) with the improved proposal distribution by focusing more on [0, t']. The optimal proposal distribution may be different from the stage-2 so it should be tuned a little bit for such task. Will the optimal result be comparable to the 2-stage training method?
- Consistency models include both consistency training (CT) and consistency distillation (CD), but this paper only shows the results of CT. Note that the original CT has the same gradient limit as CD as $\Delta t \to 0$. However, with truncation training, this conclusion will not hold anymore for t near to t'. What is the performance of CD by the truncated method?

(Please refer to Weakness section for detailed explanations)

### Soundness
2

### Presentation
3

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
The paper divides the training of consistency models into two stages, where the first stage is the standard one, and the second stage only learns the consistency function in a truncated time region $[t',T]$. The training loss for the second stage is a mixture of the consistency loss and an extra boundary loss in $[t',t'+\Delta t]$. After careful tuning of the weighing functions and timestep schedules, the second stage model can achieve better 1-step and 2-step FID on CIFAR-10 and ImageNet 64x64 than standard consistency models.

### Strengths
- The motivation is the difficulty of learning the consistency function across the whole time zone, which is sound. The second stage model only needs to map noised data to clean data in a limited time interval, which is an easier task, and it is no surprise to bring better fitting for the ODE trajectory.
- The phenomenon that the consistency training gradually weakens the model's denoising capabilities at small $t$ is well illustrated in Figure 2.
- The method achieves better FID on standard image datasets than previous consistency models, especially in 1-step generation.
- Ablation studies for the dividing time and the number of stages are comprehensive.

### Weaknesses
 - The overall idea and motivation are actually not new. ECT already points out the trade-off between the denoising capacity and the consistency capacity, suggesting the initialization of a consistency model with a diffusion model. The authors' work, in my opinion, is to use a two-stage method to replace the dedicated iteration-dependent training schedule in ECT. While the two-stage approach is a reasonable exploration, it does not fundamentally address the core issue of balancing denoising and consistency, but rather shifts the problem to a different training paradigm.
- The 2-step performance improvement is relatively marginal compared to ECT. As suggested by ECT, it is better to use a 2-step generation with a small model instead of a 1-step generation with a large one. Therefore, the actual benefits provided by truncated training are limited, especially considering that it requires careful tuning of the weighing functions and timestep schedules. The improvement in 2-step FID is not substantial enough to justify the added complexity of the two-stage training and the associated hyperparameter tuning, particularly when compared to the simpler approach of using a smaller model with a 2-step generation.
- The paper lacks a thorough discussion on the implications of the truncated training region. Specifically, the choice of the dividing time $t'$ and the width of the boundary loss region $[t', t' + \Delta t]$ seem somewhat arbitrary. The paper does not provide a clear theoretical justification or a detailed analysis of how these parameters affect the model's ability to learn the consistency function. The empirical justification provided is insufficient to fully understand the impact of these choices on the final performance.

### Questions
- Could the authors discuss the relation with PCM [1]?
- What are the total training iterations and time for the first and second stages, respectively? Is the first stage exactly the same as previous consistency models? If so, why the authors only initialize the truncated training stage with ECT for EDM2-XL?
- I think a limit case for the truncated training is to only learn the 1-step mapping $T\rightarrow 0$, i.e., limiting the truncated region to a single point $T$. The model can be directly trained on noise-data pairs. Can this method achieve better 1-step FID?


[1] Phased Consistency Model

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
This work proposes a two-stage consistency training (CT) approach by dividing the time interval into two segments. Stage 1 employs standard CT, serving as a boundary anchor for Stage 2, which focuses on larger time consistency training. This method, the authors claim, emphasizes generation over denoising.

### Strengths
The paper is well-structured and clear. I appreciate the extensive experiments illustrating the trade-off between denoising and generation in consistency training. Additionally, the empirical results seem competitive to baselines.

### Weaknesses
1. The approach appears a bit over-engineered, with numerous handcrafted designs and hyperparameters, such as the weighting function $\psi_t(t)$, $\lambda_b$, $N_B$, $\Delta_t$, $\Delta_{t'}$, and the interval division $t'$.

2. How should one determine the terminate point of Stage 1 training? Monitoring its progress may introduce additional complexity. The number of training iterations for Stage 1 may also represent a crucial hyperparameter that may require further ablation studies.

3. The paper lacks ablation studies for certain hyperparameters relevant to the proposed method, such as $N_B$ (or $\rho$), $\Delta_t$, $\Delta_{t'}$.

4. Several studies, such as [1, 2], have proposed truncating the time interval in diffusion model training to address issues like the unbounded score problem or high Lipschitz continuity when $t\approx0$. In principle, similar phenomena could arise in consistency training, as it aims to learn a noise-to-data mapping that may also exhibit large Lipschitz continuity. How does the proposed method relate to this existing literature?


5. How can one ensure that the trained CT model, using the proposed parameterization in Eq. (5), will ultimately be continuous at the splitting time $t'$? If one performs multi-step sampling and selects (some) sampling timesteps close to $t'$, this could potentially cause issues?

### Questions
1. Several studies, such as [1, 2], have proposed truncating the time interval in diffusion model training to address issues like the unbounded score problem or high Lipschitz continuity when $t\approx0$. In principle, similar phenomena could arise in consistency training, as it aims to learn a noise-to-data mapping that may also exhibit large Lipschitz continuity. How does the proposed method relate to this existing literature?


2. How can one ensure that the trained CT model, using the proposed parameterization in Eq. (5), will ultimately be continuous at the splitting time $t'$? If one performs multi-step sampling and selects (some) sampling timesteps close to $t'$, this could potentially cause issues?



[1] Kim, D., Shin, S., Song, K., Kang, W., & Moon, I. C. (2021). Soft truncation: A universal training technique of score-based diffusion model for high precision score estimation.

[2] Yang, Z., Feng, R., Zhang, H., Shen, Y., Zhu, K., Huang, L., ... & Cheng, F. (2023). Eliminating lipschitz singularities in diffusion models.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes an interesting way to improve the training of consistency models. It points out, simutaneously learn to denoise and generate can require more capacity. Based on the belief, the paper proposes to separately use two models for denoising and generation, with a two-stage training procedure that first train a standard consistency model, and then train a generation model. The challenging part is the training loss and weighting function need to be carefully designed to enforce the boundary condition between two time ranges. The proposed approach seems to successfully train stably with continuously decreased FID, and improves upon existing work ECM.

### Strengths
- The paper largely focus on an orthogonal problem of network capacity, which can be possibly combined with many consistency distillation works.
- Train two separate models with a boundary condition to enforce consistency is empirically challenging (though theoretically straightforward), but the paper shows that it is possible. This might be informative for subsequent works that require different models across time ranges.

### Weaknesses
 - While the proposed method improves considerably on small models and few time steps, the improvement on the highest quality 2-step EDM2-XL is negible. The applicability of the proposed method on large-scale models is questionable.
- The proposed method seems to still perform worse than SiD.

### Questions
Besides the weaknesses listed above, I also have some questions.
- I am not an expert on consistency models. But there are many other works on consistency distillation, such as CTM / TCD. Why not comparing against them?
- SiD seems to get better FID with significantly fewer parameters. Why variational score distillation methods are listed in separate categories and not compared against consistency models?
- How does the proposed method apply to guided sampling / text-to-image applications? How does guidance scale impact the proposed method? (Including more guided sampling results would improve the submission.)

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper identifies a shortcoming of consistency models: their joint temporal parameterization via a single network which limits their learnability. By noticing that early denoising timesteps, irrelevant for the final generation task, are neglected at the end of the training, the authors propose to train a consistency model on large noise levels only, with a pretrained consistency model serving as initial condition at the cutoff point. The relevance and the advantage of this approach are empirically demonstrated as the resulting model obtains state-of-the-art performance with limited number of parameters and reduced instability.

### Strengths
This paper is **very well written**: it is easy to read and understand. All ideas are presented and articulated clearly. The method's description and results are presented in a **simple and efficient manner**, making it easy to reimplement. Given its generality, I believe that Truncated Consistency Models may **become a widespread trick** to improve consistency models' performance.

The model is particularly **well motivated**, and its design **well supported** by sound experiments. The latter suscessfully highlight the denoising-generation tradeoff of standard consistency models. The efficiency of the proposed method to improve the generation performance at later training steps is demonstrated in the experiments. **Additional insights on design choices** (cutoff time, relevance of more training stages, etc.) are appreciated.

To my knowledge, both the presented insights and model are novel, even though the truncation principle has become a standard technique in diffusion (Balaji et al., 2022; Zheng et al., 2023 -- that could be cited in the related work) and consistency (Heek et al., 2024) models. Overall, the paper's contribution has a **good significance potential** as the presented insights are valuable for all practitioners, the experimental results are appealing and the method is generally applicable. The denoising-generation duality also echoes more fundamental work unveiling phase transition phenomena in diffusion models (Ambrogioni, 2023; Biroli et al., 2024; Sclocchi et al., 2024).

Ambrogioni. The statistical thermodynamics of generative diffusion models: Phase transitions, symmetry breaking and critical instability. arXiv:2310.17467, 2023.\
Balaji et al. eDiff-I: Text-to-Image Diffusion Models with Ensemble of Expert Denoisers. arXiv:2211.01324, 2022.\
Zheng et al. Truncated Diffusion Probabilistic Models and Diffusion-based Adversarial Auto-Encoders. ICLR 2023.\
Biroli et al. Dynamical Regimes of Diffusion Models. arXiv:2402.18491, 2024.\
Heek et al. Multistep Consistency Models. arXiv:2403.06807, 2024.\
Sclocchi et al. A Phase Transition in Diffusion Models Reveals the Hierarchical Nature of Data. arXiv:2402.16991, 2024.

### Weaknesses
While they are not critical and may not significantly change my assessment, I would like the authors to tackle the following weaknesses.

### Unnecessary decomposition of the loss

I do not understand the necessity of the loss decomposition in Eq. (6). To my understanding, it amounts to giving a specific sampling weight for timesteps close to $t'$ in $\psi$. The parameterization of Eq. (5) should then handle the corner case. Additionally, it appears that $S_{t'} = \{t'\}$, so the notations may be simplified in this part of the paper.

### Additional insights & reproducibility

The following discussions / content would benefit the paper.
- The code used by the authors for the presented experiments should be included in the supplementary material for further reproducibility.
- One can notice in Figure 3 that the denoising FID increases at the beginning of stage 2. I would be interested in the authors' opinion on this phenomenon.
- Still in Figure 3, can the authors explain why the denoising FIDs do not start from the same value between stage 1 and stage 2 (assuming they start from the same checkpoint)?
- While the authors acknowledge an additional training and memory cost in Section 6, I am not sure they include the additional cost induced by the supplemental training iterations to complement the pretrained consistency model (up to 200k additional optimization steps based on the different plots).

### Minor issues

- Section 4.2 insists on the forgetting by the truncated model on the lower noise levels. This is not an advantage or a confirmation of the model's abilities, but a byproduct of the truncated training loss.
- The number of optimization steps is not specified in the hyperparameters listed in Section D.
- In Figure 3, the timestep $t = 1$ should be placed in the second row to be consistent with the rest of the paper.
- The paper should specify where the baseline results from Tables 1 and 2 are reported from.

### Questions
I have no specific question -- cf. the above comments. Overall, I recommend an "accept" but am waiting for the authors' response to my comments and look forward to discussing with the other reviewers on the matter.

### Soundness
3

### Presentation
4

### Contribution
2
