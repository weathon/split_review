# SafeDiffuser: Safe Planning with Diffusion Probabilistic Models

- Decision: Accept
- Avg Score: 6.75
- Scores: 6, 8, 8, 5

## Abstract
Diffusion model-based approaches have shown promise in data-driven planning, but there are no safety guarantees,  thus making it hard to be applied for safety-critical applications. To address these challenges, we propose a new method, called SafeDiffuser, to ensure diffusion probabilistic models satisfy specifications by using a class of control barrier functions. The key idea of our approach is to embed the proposed finite-time diffusion invariance into the denoising diffusion procedure, which enables trustworthy diffusion data generation. Moreover, we demonstrate that our finite-time diffusion invariance method through generative models not only maintains generalization performance but also creates robustness in safe data generation. We test our method on a series of safe planning tasks, including maze path generation, legged robot locomotion, and 3D space manipulation, with results showing the advantages of robustness and guarantees over vanilla diffusion models\footnote{\color{blue} Videos can be found in the anonymous website: \url{https://safediffuser.io/safediffuser/}}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors propose a method to use control barrier functions (CBFs) with diffusion planning, enabling safety guarantees. The results are demonstrated on a 2D maze problem, Walker2D and a manipulation problem from related work.

### Strengths
- Safety guarantees are important for some applications and of interest to the safe planning community
- This may be the first (only?) safety method for diffusion planning.

### Weaknesses
 - Some parts are a bit difficult to read and have unusual terminology (e.g., "local traps"?) and the paper contains some minor grammar and cosmetic issues which make the quite complex approach harder to understand.
- The method is actually three methods, and the user is to pick the one most suitable for their problem. This seems a bit complicated, why not go for the most general?

Example presentation issues (I recommend you do another polish pass):
- General: excessive underlining
- 470: typo: physical simulator
- 474: typo: can work in general safety guarantees

### Questions
1) Are "local traps" = local minima?
2) Isn't it a big problem that the method gets stuck in "local traps" between 39% and 100% of the time for some of the benchmarks? What does this mean in practice?
3) What is trap rate 1 vs. trap rate 2 in the table?
4) Could you comment on why you chose to use CBF here instead of e.g. lagrangian objectives common in safe RL?
5) Why three methods instead of the most general, or one that picks the best solution approach?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors present SafeDiffuser, a modified version of the Diffuser model proposed by Janner et al. (2022), adapted to ensure the satisfaction of safety constraints. They introduces "Finite-Time Diffusion Invariance," leveraging Control Barrier Functions (CBFs) within the denoising diffusion process to enforce specified safety constraints. The authors propose three approaches for implementing their methodology—ROS, RES, and TVS—that demonstrate competitive performance compared to baseline methods, achieving significantly fewer constraint violations. Experiments were conducted across Maze2D-large, locomotion, and manipulation tasks, validating the effectiveness of the proposed approaches in diverse settings.

### Strengths
1. The proposed method introduces a novel formulation of Control Barrier Functions (CBFs) within diffuser-family models, ensuring that safety constraints are satisfied throughout the diffusion denoising process.
2. The authors provide a systematic approach for selecting the appropriate variant based on the safety constraints.
3. Results demonstrate improvements in safety-related metrics while maintaining comparable performance in the downstream task.
4. The method can be trained using data that violates safety constraints, yet during testing, it reliably generates safe trajectories.

### Weaknesses
 1. The proposed methods require solving Quadratic Programs (QPs) at each diffusion step, which is computationally inefficient.
2. [Minor Weakness] The approach requires predefined safety constraints. However, I think that this limitation is relatively minor, such a setup is not a major weakness.
3. It would strengthen the paper if the authors included comparisons with other methods, such as CDT [1], which also employ sequential modeling techniques to address offline RL problems with safety constraints.

[1] Liu, Zuxin, et al. "Constrained decision transformer for offline safe reinforcement learning." *International Conference on Machine Learning*. PMLR, 2023.

### Questions
1. In terms of data and experimental results, could you clarify the rationale for selecting D4RL over [2], which is specifically designed for Safe Offline RL?
2. Can you clarify the motivation of applying CBFs in the diffusion denoising process steps instead of trajectory planning steps? It was not very clear.
3. Why were the experiments conducted solely in Maze2D-large? Could you clarify the choice of tasks for the locomotion experiments? Specifically, why was only the Medium-Expert variant used for the locomotion environment? What about Cheetah?
4. Could you elaborate on the generalization capabilities of the model when encountering new safety constraints beyond those specified during training? It would be valuable to understand how well the approach adapts to previously unseen constraints.


[2] Liu, Zuxin, et al. "Datasets and benchmarks for offline safe reinforcement learning." arXiv preprint arXiv:2306.09303 (2023).

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents control barrier function-based methods to enforce safety constraints on diffusion models. The main idea is to modify the diffusion denoizing step to satisfy safety constraints within a finite number of steps (finite-time diffusion invariance). This is done by formulating a quadratic program to compute a perturbation that steers the generated trajectory towards the safe set in every denoizing step. Evaluations in simulated maze and robotics domains show that the proposed method is superior to baselines in satisfying safety constraints at the cost of longer planning time.

### Strengths
- Diffusion models are an important and effective class of conditional generative models. However, existing methods for guidance do no provide safety guarantees. Hence, the propose algorithm is an important contribution.
    
- Applying CBF-based technique to diffusion models is novel to my knowledge. In particular, modifying the denoizing steps seem to be more effective than generating safe trajectories through classifier-free guidance.
    
- Proposed extension to handle local traps are effective.
    
- Experimental results in simulation demonstrate the effectiveness and robustness of the algorithm.

### Weaknesses
 - Safety specifications have to be differentiable.
    
- SafeDiffuser is significantly slower (by an order of magnitude) than vanilla diffusion.


### Questions
- The forward invariance in control theory (equation 2) assumes that the control system is governed by Lipschitz functions. Is any such requirement not required for extending the definition to diffusion neural networks?
    
- Diffusion dynamics is estimated online. How does error in this estimation affect the guarantees and performance in practice?
    
- In theorem 3.2 what is the intuitive meaning of the robust term?
    
- If would be interesting to continually retrain the diffusion models on the generated safe data. Can this improve performance or speed up safediffuser?

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
The paper introduces SafeDiffuser, a method to add safety guarantees to diffusion models when used for planning tasks. The key innovation is incorporating control barrier functions (CBFs) into the diffusion process to ensure generated trajectories satisfy safety constraints.

### Strengths
The approach maintains the model performance while adding safety guarantees.

### Weaknesses
1. The definition of diffusion invariance seems too strict. Essentially we only care about the safety at t=0, and trajectories satisfying t=0 safety don’t necessarily need to satisfy t=1 safety. However the method actively encourages the intermediate trajectories to be safe. This doesn’t mean the method is wrong, but I’m hoping to see a softer way to guarantee the safety. See Q2.
2. Along with the above weakness, the design choice seems too complex. There’re $\epsilon$, $w$, $r$, $\gamma$, $\sigma$, all of them seem hyper-parameters that need careful tuning.
3. CBF itself is meant to design for dynamics that are (1) time-invariant; and (2) deterministic. The diffusion process doesn’t belong to any of these two parts. For (1), the alpha bar changes over time steps. For (2), most of the diffusion sampler constantly adds noise to the dynamics (unless the approach is specifically using DDIM). Applying CBF-based technique to the diffusion seems counter-intuitive.
4. Scaling up seems challenging. I’m hoping to see a highly nonlinear dynamics like drone/quadcopter to see whether the method could scale up. Another challenge for scaling up is from the selection criteria. Page 6 discusses the principle to select different safediffusers. As mentioned, it requires the unsafe set to be known to determine the convexity. This seems challenging for high-dimensional control tasks.

### Questions
1. Regarding to the design choice, the TVS diffuser seems to be the most general safediffuser. Is it possible to further simplify the forward invariance equation (theorem 3.4) by fully discarding the reliance on b, and directly using sigma? For example, imagine sigma at t=0 converges to exactly b. This sigma can be used in analogy to the time-varying CBF and should impose a more relaxed restriction to the intermediate samples. I guess it would need clever design of sigma (or even learning-based), but do you think it is worth the effort?
2. Another question is the motivation of using CBF. From first principle, all we care about here is the safety at the final timestep, ie, t=0. It sounds more similar to a goal-reaching/liveness problem, where you don’t need to enforce every intermediate sample satisfy the safety. Compared to control Lyapunov function or reachability-based method, why is CBF used for the problem? Applying the other two concepts seem more natural to me.
3. In control, CBF can usually be compared to potential-field based method to show their effective in terms of avoiding obstacle in a longer time horizon rather than reactively avoiding. Similarly, is it possible to include [1] as a baseline to show the approach’s effectiveness? 

[1] Luo, Y., Sun, C., Tenenbaum, J. B., & Du, Y. (2024). Potential based diffusion motion planning. arXiv preprint arXiv:2407.06169.

### Soundness
2

### Presentation
2

### Contribution
2
