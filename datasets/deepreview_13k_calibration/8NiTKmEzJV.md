# NETS: A Non-Equilibrium Transport Sampler

- Decision: Reject
- Avg Score: 6.25
- Scores: 5, 6, 6, 8

## Abstract
We propose an algorithm, termed the Non-Equilibrium Transport Sampler (NETS), to sample from unnormalized probability distributions. NETS can be viewed as a variant of annealed importance sampling (AIS) based on Jarzynski's equality, in which the stochastic differential equation used to perform the non-equilibrium sampling is augmented with an additional learned drift term that lowers the impact of the unbiasing weights used in AIS. We show that this drift is the minimizer of a variety of objective functions, which can all be estimated in an unbiased fashion without backpropagating through solutions of the stochastic differential equations governing the sampling. We also prove that some these objectives control the Kullback-Leibler divergence of the estimated distribution from its target. NETS is shown to be unbiased and, in addition, has a tunable diffusion coefficient which can be adjusted post-training to maximize the effective sample size. We demonstrate the efficacy of the method on standard benchmarks, high-dimensional Gaussian mixture distributions, and a model from statistical lattice field theory, for which it surpasses the performances of related work and existing baselines.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work presents an approach to sample from densities specified up to a normalizing constant using controlled annealed Langevin dynamics. The approach is first motivated by Jarzynski's equality, which can be interpreted as a time-continuous variant of annealed importance sampling (AIS). Then, the paper extends this framework to *controlled* Langevin dynamics and proposes to learn the drift either by physics-informed neural networks (PINNs) or a version of action matching. The resulting method, called Non-Equilbrium Transport Sampler (NETS), is numerically evaluated on Gaussian mixtures, the Funnel distribution, and the simulation of a lattice field theory.

### Strengths
The paper is generally well-structured and theoretically sound. In view of existing work (see weaknesses below), the paper provides the following contributions:
1. New (and arguably simpler) derivation of existing results on (controlled) annealed Langevin dynamics,
2. Novel objective based on action matching (AM),
3. Evaluation of additional tricks, such as usage of importance weights for the PINN objective, curriculum learning for the time interval, and combination with resampling.

### Weaknesses
 **Related works:** Large parts of the paper are already included in existing work:

- *Controlled Langevin dynamics:* While Vargas et al. (2024) are mentioned in the related works, it is important to note that the *main* proposition of the present paper, Proposition 3 (Nonequilibrium Transport Sampler (NETS)), is already presented in Vargas et al. (2024, Proposition 3.3). Using the data processing inequality, the latter result also seems to yield the bound on the KL divergence in Proposition 5. The connection between the PINN loss and the weighting factors is also present in Vargas et al. (2024, Proposition 3.3), even though the PINN loss is not explicitly written down. Moreover, the fact that the minimizer of the action matching loss corresponds to the unique gradient field satisfying the corresponding continuity equation seems to be derived in the "action matching" paper.

- *PINN objective:* The PINN objective in Section 2.5 is already stated in https://arxiv.org/abs/2301.07388 (Section 3, "The continuity loss"), https://arxiv.org/pdf/2405.06672 (Section 2.2), and https://arxiv.org/pdf/2407.07873 (Section 3.2, "Annealing"), where also on- ("uniform") and off-policy ("along trajectories") methods for $\hat{p}_t$ are explored. While both sampling variants do not require backpropagating through the SDE integrator, the latter *does* need to simulate the SDE (at least periodically if using a buffer). Thus, I would not say that NETS-PINN is "simulation-free even if used on-policy," as stated in line 344. It should also be noted that backpropagating through the solution of the SDE can also be prevented for KL-based losses using an "optimize-then-discretize" approach via the adjoint SDE.

Because of these observations, the present work only provides little *novel* contributions (see strengths above). In particular, the PINN objective seems to outperform the AM objective in the first two experiments, and curriculum learning is a relatively standard trick for time-dependent PINNs.

Moreover, many of the shortcomings mentioned in related works are either not completely accurate or have already been tackled. In particular, there seem to be several methods having checkmarks for all columns of the table on page 2. Some details (see also questions below):

1. There exist several off-policy losses for samplers based on dynamical transport, which, in particular, do not require backpropagating through the SDE integrator and lead to unbiased sampling methods; see (sub-)trajectory/detailed-balance losses for GFlowNets (e.g., https://arxiv.org/abs/2210.00580, https://arxiv.org/abs/2310.02679, https://arxiv.org/pdf/2402.05098) and log-variance (LV) losses (https://arxiv.org/abs/2307.01198; also used in Vargas et al. (2024)). In particular, these losses also fall into the category of "optimize-then-discretize".

2. I assume the LV loss is meant in the second part of the sentence "this objective either needs backpropagating through the SDE or has to be computed with a reference measure which may make it high variance". However, for the typical choice of using the on-policy drift, the reference measure is actually *reducing* variance (as compared to the KL divergence) (https://arxiv.org/abs/2307.01198, https://arxiv.org/abs/2005.05409). While it might be numerically unstable in certain settings, it seems that the LV and trajectory-balance loss can achieve strong performance. Moreover, it should at least be mentioned that *in theory* also competing methods do not rely on a "fixed grid" and could be used with randomized time steps.

3. The fact that the objectives of DDS (and DIS, see Berner et al., 2024) can also be viewed as SOC problems shows that methods based on SOC do *not* need to start with samples from a point mass.

---

**Experiments:** Important baselines and ablations seem to be missing:

1. CMCD: As argued above, CMCD has the same theoretical framework, and it can also be viewed as a BSDE (instead of PINN) loss, as shown in https://arxiv.org/pdf/2407.07873 (Prop. 3.1). However, NETS is currently not compared against CMCD. It seems that CMCD has only been evaluated for GMM and Funnel, but not for MoS or the $\phi^4$ experiments. Moreover, it seems that the log-variance loss in CMCD also gives control over the Jarzynski/importance weights.

2. ODE importance weights: The advantage of using the SDE instead of the ODE during generation should be validated. Specifically, one could also use the learned vector field $\hat{b}$ to simulate the ODE (aka continuous-time normalizing flow) and compute the importance weights using the change-of-variables formula (as is done in some of the works mentioned above that also use the PINN objective).

3. Sections 4.3 and 4.4 do not provide any baselines except for AIS and only evaluate one of the proposed NETS versions. Moreover, no details on the AIS settings seem to be provided.

4. Since NETS seems to require a very high number of discretization steps (all experiments use >= 200 and some up to 1500-2000 steps), it would be interesting to see how well NETS is working for fewer steps (which is relevant in settings where target evaluations are expensive). Is the same number of steps also used during training?

5. More benchmarks (e.g., from Blessing et al. (2024)) are required to judge the performance of NETS against other state-of-the-art samplers, and it would be good to see an ablation of some components of NETS (e.g., the curriculum learning or the importance weights in the PINN objective).

When quoting baseline results from other works, it is crucial to follow the same evaluation protocol, in particular, the number of integrator steps and evaluation samples:

1. *Funnel:* NETS: 200 steps and 10000 samples. Baseline: 128 steps and 2000 samples.
2. *Gaussian Mixture:* NETS: 250 steps and 2000 samples. Baseline: 100 steps (at least for PIS; it might also be that ESS is computed using an "exact likelihood from a continuous normalizing flow (CNF) model [trained] using optimal transport flow matching on samples from each model," which "keeps the number of function evaluations per integration around 100 in practice") and 1000 samples.

Please reevaluate your results using the same protocol. Finally, it would be interesting to also compare training costs, e.g., time and number of target (& gradient) evals, etc.

### Questions
1. It is unclear why the paper writes that off-policy objectives do not need samples from the "target density" (line 63) since we do not seem to have samples from the target density for both on- and off-policy losses. In this context, "off-policy" typically means that the trajectories do not need to follow the ones from the *learned* model. 

2. What exactly is meant by "grid-free learning," i.e., why are PIS and NETS grid-free but DDS and CMCD are not? All these methods are based on simulating SDEs on some time grid. In particular, for off-policy methods, the time grid can basically be chosen arbitrarily.

3. It is unclear why DDS is only "partially" unbiased. For diffusion-based samplers, one can perform importance weighting in path-space, which is unbiased (up to bias introduced from self-normalization as also used in NETS).

4. What prevents other samplers based on diffusion models (such as DDS and DIS) from using "arbitrary step size and time-dependent diffusion after learning the model"? As already shown in https://arxiv.org/abs/2106.02808, there is a family of equivalent SDE that can be used for inference and which only requires knowledge of the score. Naturally, the approaches might overfit to a fixed time discretization. However, the time steps can be randomized during training, as is done in NETS.

5. How does the last step in (52) follow (since $\hat{b}$ is not at the optimum)?

---

**Suggestions:** While the largely algebraic calculations might yield easier proofs of existing results, the paper would benefit from providing further explanations and context. Two examples:

- The sentence "The effect of the last term at the right hand-side of this equation can be accounted for by using weights." only becomes clear after reading Remark 1. It might generally be good to add some more intuition to these algebraic calculations, e.g., (5) is just showing that $\rho_t$ is the invariant measure of the Langevin dynamics (with noise $\sqrt{2\varepsilon_t}$).

- One could also mention that Eq. (13) is just the continuity equation with predefined density evolution, and Eq. (14) are the FPEs of the corresponding family of SDEs with the same marginals (by standard manipulations of FPEs, e.g., Appendix G in https://arxiv.org/pdf/2106.02808). This also directly implies the statement of Prop. 2.

See weaknesses above for additional suggestions and questions.

---

**Typos:**

- $R^d$ on line 122

- $\partial_t \log F_t$ on line 140

- $R^{d+1}$ in line 160

- $U$ (without time index) in (10) and line 123

- 9 in line 183 should probably be (8)

- 46 in lines 272 and 275 should probably be (25)

- THe in line 852

- These in line 971

- There seem to be $\hat{cdot}$ missing over the $\phi$ in Section 2.6 and the corresponding proofs.

- closing $)$ missing in (18).

- it should be integration against $\hat{\rho}_t$ at several places in the proof of Prop. 5.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a sampling algorithm using annealed Langevin dynamics and additional learnable transport, which can be viewed as a variant of annealed importance sampling. The additional learnable transport can be used to reduce the high variance appeared in original annealed importance sampling. The paper proposes to learn the additional transport by minimizing two objective functions. Theoretically, they show the PINN objective controls the KL divergence between the model and its target. Last, they provide numerical examples outperforming several baseline state-of-the-art techniques and testify the scalability of the method.

### Strengths
- The idea of combining annealed importance sampling and additional transport is interesting and novel.
- The theoretical result of the KL control for the PINN objective is interesting.
- Considering both $\hat{b}_t$ and $\hat{F}_t$ simultaneously in the PINN objective is interesting and novel.
- This method contains correction for sampling errors if the additional transport is imperfectly learned.

### Weaknesses
 -  In practice, using PINN objective need compute the divergence of a velocity field in $\mathbb{R}^d$, which can be extremely inefficient in high-dimensional case.
-  Several studies have investigated sampling algorithms by solving the velocity field through partial differential equations ([1], [2]). Therefore, a more detailed discussion of these related works would enhance the author’s contribution by clarifying connections and advancements in this area.
-  Although the PINN objective is off-policy, making it more computationally efficient, the performance of the algoirthm can be sensitive to the choice of $\hat{\rho}_t$. For example, it may lead to poor exploration when $\hat{\rho}_t$ is significantly far away from $\rho_t$.  A more detailed discussion on this trade-off would strengthen and complete the author’s analysis in this context.

### Questions
see weaknesses.

Minor comments: typo in Line 140-142: $\partial_t \log F_t$ should be $\partial_t F_t$.

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
4

### Summary
This paper proposed NETS which targets sampling from unnormalized probability distributions.
NETS originates from annealed importance sampling, which is widely known to result in biased samples and relies on importance sampling for correction.
NETS views AIS as an SDE augmented with important weights and incorporates a learnable transport drift function $b(x)$ to correct this biasedness.
This idea is similar to the stochastic control.
The core ingredient of NETS, $b(x)$, can be learned by PINN or action matching, and in the first case, the learning is off-policy and does not require backpropagating the SDE.
The alternative perspective on AIS is very interesting and insightful, and improving it with an additional transport map seems novel and effective in practical applications.

### Strengths
- To the best of my knowledge, the proposed method is novel and firstly tackles the biasedness problem of AIS with an additional transport function. The weight-augmented SDE formulation is also inspiring for follow-up works.
- The authors derive two practical training methods for the transport function $b$. Especially, for the action matching objective, computing the Hessian matrix of $\phi_t(x)$ can be avoided by a smart trick on $A_t^b$.
- The experiments are illustrative and well-designed to demonstrate the superiority of NETS. I especially favor the illustration in Figure 1 that shows the effectiveness of the transport.

### Weaknesses
 - NETS is somewhat similar to stochastic control for me. I suggest the authors clarify the similarities and differences between them.
- There are some critical hyperparameters that can affect the performance of NETS, e.g., the $\varepsilon_t$ parameter and the stepsize of discretization. I would like to see how these parameters affect the convergence of the proposed method. Besides, it would be better for the authors to give some instructions on how to select these hyperparameters in practice.
- Although the authors target sampling tasks, an important application of NETS is to calculate expectations based on equation (21). Exploring or discussing this application would be interesting.
- For methods that require simulating the trajectories or computing divergence/hessian, computational cost is always a major concern. The authors should report the training time and memory consumption of NETS and other baselines, to fairly compare different methods.
- There are many typos in mathematical equations that can cause misunderstanding. I strongly suggest the authors carefully check their manuscript.
    - The expression of $\rho_t(x)$ in equation (9).
    - The reference to equation (9) in line 193 seems incorrect.
    - The expression of the RHS in equation (18).
    - The expression of $g_t$ in equation (40).
    - 'Them' in line 38; 'resut' in line 312; and so on.
- The authors give a guarantee of convergence in KL divergence. However, no KL divergence results have been compared or reported in the experiments.

### Questions
- For the PINN loss in equation (25), we need to compute the divergence of $\hat{b}_t(x)$ to obtain the gradient. Then how do you efficiently compute it, especially in the high-dimensional case?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The paper proposes a novel sampler for unnormalized probability distributions by augmenting the Stochastic Differential Equations (SDE) framework of Annealed Importance Sampling (AIS). The method introduces an additional drift term in the SDE, which enhances the effective sample size of the collected samples, thus reducing bias. The drift term can be estimated through either a Physics-Informed Neural Network (PINN) or Action matching objectives, which encourages the SDE to be nearly unbiased.

### Strengths
The paper presents a diffusion-based, simulation-free method for multi-modal sampling, which demonstrates significant potential in sampling efficiency and effectiveness. The method provides a powerful alternative to traditional sampling techniques and is applicable to complex, multi-modal distributions.

### Weaknesses
1. Equation 46, frequently referenced in Section 2.5, would be more accessible if directly included in that section or if Equation 25 were referenced instead.
1. The computational cost for evaluating the objective from $t=0$ to $T$ seems a lot. An analysis of wall-clock time or time complexity compared to baseline methods would be beneficial.
1. The paper's comparisons with diffusion-based baseline samplers focus on low-dimensional examples (e.g., 2D Gaussian Mixture Model and 10D funnel distribution). However, high-dimensional comparisons are only performed as part of an ablation study. To show a practical scalability, comparisons in a high-dimensional setting would strengthen the argument for the method’s applicability beyond small-scale examples. I think the section 4.3 is showing a possibility to scale, not a powerful performance even in high dimensions.

### Questions
1. In Line 342, could you clarify how $(X^{\hat{b}}_t, A^{\hat{b}}_t)$ can be considered independent of $\hat{b}_t(x)$? A detailed explanation would be helpful.
1. Could you provide insight into how the method achieves multi-modal sampling without simulation? Without simulation, it seems challenging to capture information on unexplored modes.

### Soundness
3

### Presentation
3

### Contribution
4
