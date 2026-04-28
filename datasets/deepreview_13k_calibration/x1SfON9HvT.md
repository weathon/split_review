# Diffusion Modulation via Environment Mechanism Modeling for Planning

- Decision: Reject
- Avg Score: 3.75
- Scores: 3, 3, 6, 3

## Abstract
Diffusion models have shown promising capabilities in trajectory generation for planning in offline reinforcement learning (RL). However, conventional diffusion-based planning methods often fail to account for the fact that generating trajectories in RL requires unique consistency between transitions to ensure coherence in real environments. This oversight can result in considerable discrepancies between the generated trajectories and the underlying mechanisms of a real environment. To address this problem, we propose a novel diffusion-based planning method, termed as Diffusion Modulation via Environment Mechanism Modeling (DMEMM). DMEMM modulates diffusion model training by incorporating key RL environment mechanisms, particularly transition dynamics and reward functions. Experimental results demonstrate that DMEMM achieves state-of-the-art performance for planning with offline reinforcement learning.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper introduces a new diffusion-based RL planning method named DMEMM. Unlike previous methods that use fixed isotropic variance and disregard the rewards which may lead to a mismatch between generated trajectories and those desirable for RLs, DMEMM explicitly incorporates transition-based, reward-based, and reward-aware diffusion modulation loss. By doing so, DMEMM enhances both the coherence and quality of generated trajectories, achieving state-of-the-art performance.

### Strengths
1. The presentation of this paper is great and easy to follow.
2. The idea of this paper is simple and clear. 
3. The experimental result looks good.

### Weaknesses
1. The tested diffusion-based offline RL planning algorithm missed the Decision Diffuser[1], which performance is much better than the original Diffuser. Also, it's important that the Decision Diffuser doesn't have the issue of inaccurate transition as it only predicts the state sequence and calculates the actions by inverse dynamics.

2. The motivation of this paper is ambiguous. I assume that the initial motivation is to improve the consistency of the dynamic by explicitly incorporating the loss of the difference between the real states after transition and the generated states. However, the initial idea of diffusion models is to measure the distribution of the trajectories, which has already included the dynamics. I'm wondering if adding such a loss can really improve the consistency of dynamics. The authors need to seriously discuss this problem.

3. Same as previous papers, this paper also uses the paradigm of autoregressive generation, where each time only the first action will be executed. In this case, generating accurate transitions seems to be less important. 

4. The paper is lack of novelty, the idea of adding a loss on the transitions is an incremental work.

### Questions
1. The authors need to include Decision Diffuser as the baseline.

2. Why there are only part of the environments in the ablation study in Table 3.

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper focused on offline reinforcement learning (offline RL) with diffusion models as planner. Following Diffuser (Janner et al. 2022), a series of studies have been proposed the improved the performance. This paper discussed the problem of generating trajectories with consistency between transitions to ensure coherence. The being proposed methods includes a transition-based diffusion modulation loss, and dual reward guidance. Using the mixed loss function, the being proposed method was tested on D4RL locomotion, showing SOTA performance compared to previous diffusion planning algorithms; and on Maze2D, showing similar performance with previous best.

### Strengths
1. The paper was written in a very straightforward way, making it easy to follow and understand
2. The being discussed problem is important and the paper proposed a practical method to solve it.

### Weaknesses
1. The being tested benchmarks are too narrow, recent diffusion planning studies usually included other D4RL environments AntMaze, Franka Kitchen, etc. But this paper only examined D4RL locomotion, thus it remains unclear whether the being proposed method work well in general tasks.

2. While the being proposed method performs well in D4RL locomotion compared with previous diffusion planning methods (avg. normed. return  = 87.9, Table 1), it should be discussed that the previous best diffusion model-based method on this benchmark was from diffusion policy [1] (avg. normed. return  = 88.0 [1], and 89.0 in [2]).

3. When compared with HD-DA, the performance on the Maze2D (Table 2) is worse when the size becomes large. Since I do not see other experimental results on planning, I am skeptical about the scalability of the being proposed method when task becomes more challenging.

Overall, the paper provides limited insights. There lack both theoretical and empirical insights about the problems being touched, due to limited variety of benchmarks and limited analysis (with only a very formulaic ablation study), making this paper not qualified for the ICLR bar.

### Questions
- Will the authors publish the source code?

I do not have further questions since the paper was written in a very straightforward way and easy to understand. To improve the work, please see the comments above.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper addresses the challenge of improving diffusion model-based trajectory generation for offline reinforcement learning (RL) by incorporating transition dynamics and reward functions through a new framework, Diffusion Modulation via Environment Mechanism Modeling (DMEMM). Experiments show that DMEMM achieves state-of-the-art results on D4RL and Maze2D tasks, with ablation studies highlighting the effectiveness of each framework component. This work addresses a key gap by enhancing trajectory coherence with real-world constraints in diffusion-based RL planning.

### Strengths
1. **Motivation and intuition**: The motivation for improving trajectory generation in RL through transition-consistent diffusion models is convincing.

2. **Novelty**: The way of how to utilize transition dynamics and cumulative reward modulation in the diffusion model is intuitive and novel. This paper presents an effective way to implement this idea.

3. **Technical contribution**: The transition-based modulation loss for enforcing transition consistency seems particularly effective for producing coherent trajectories in complex environments.

4. **Ablation study**: The ablation studies are comprehensive, breaking down each framework component and showing its role in improving trajectory quality.

### Weaknesses
1. **Clarity**: The meaning of some notations, such as the subscripts and superscripts on τ, is not clearly explained. While the intended meaning can be inferred after careful review, a clearer definition of each notation would improve the paper's readability. Specifically, the paper should explicitly define what each index on τ represents (e.g., time step, trajectory segment, etc.) and how these indices are used in the context of the diffusion process. The lack of precise definitions makes it harder to follow the mathematical formulations. 

2. **Completeness**: The paper lacks a discussion on the application of diffusion models within imitation learning [1, 2], a subset of reinforcement learning, which is necessary to clarify the advantages of using diffusion models in planning. The paper should address how diffusion models compare to other imitation learning techniques, such as behavioral cloning, and discuss the specific benefits of using diffusion models for generating diverse and high-quality trajectories in this context. The absence of this discussion leaves a gap in the understanding of the method's broader applicability.

3. **Experiment details**: The experiments are not sufficient, as they focus only on locomotion and Maze2D environments. Adding other environments, such as manipulation and image-based tasks, would enhance the credibility of the results. Given that diffusion models originated in image domains, testing on image-based environments would be valuable. The current experiments do not fully demonstrate the method's ability to handle complex, high-dimensional state spaces or tasks with visual inputs. Furthermore, the paper should include a more detailed analysis of the computational cost of the method, particularly in comparison to other diffusion-based planning approaches.

4. **Reproducibility**: The authors did not provide code nor commit to releasing it upon acceptance, which limits the reproducibility of the results. This lack of code makes it difficult for other researchers to verify the claims made in the paper and to build upon this work. The paper should at least commit to releasing the code upon acceptance to facilitate reproducibility and further research.

### Questions
1. The paper needs to explain how diffusion models can be applied within imitation learning [1, 2], a subset of reinforcement learning.

2. The experiments, limited to locomotion and Maze2D, are insufficient. Adding manipulation and image-based tasks would strengthen credibility, especially given diffusion models’ origins in image domains.

3. How does DMEMM handle environments with highly stochastic transitions or non-stationary reward functions, and what are the main challenges it faces in such contexts?

4. What are the primary computational trade-offs introduced by incorporating dual-guided sampling in DMEMM, and how does it perform compared to standard model-based and model-free RL approaches in terms of efficiency?

5. To what extent is DMEMM sensitive to the weighting of transition- and reward-based modulation losses, and what practical guidelines can be provided for setting these parameters across various RL environments?

6. Can the proposed transition-guided sampling in DMEMM be further adapted to handle hierarchical or multi-step decision-making tasks, and if so, what modifications might enhance its applicability?

I would be inclined to raise the score if you clear up my cnofusion and discuss diffusion model's applicability to imitation learning.

[1] Tim Pearce, Tabish Rashid, Anssi Kanervisto, David Bignell, Mingfei Sun, Raluca Georgescu, Sergio Valcarcel Macua, Shan Zheng Tan, Ida Momennejad, Katja Hofmann, and Sam Devlin. Imitating human behaviour with diffusion models. In International Conference on Learning Representations, 2023.

[2] Shang-Fu Chen, Hsiang-Chun Wang, Ming-Hao Hsu, Chun-Mao Lai, and Shao-Hua Sun. Diffusion model-augmented behavioral cloning. In International Conference on Machine Learning, 2024.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes a model-based offline diffusion RL method. By adding auxiliary loss about state transitions and cumulative rewards to the conventional diffusion loss, the authors claim to solve the problem of generating trajectory discontinuity when diffusion is applied to reinforcement learning. The authors validate the proposed method on D4RL and claim that their method achieves SOTA.

### Strengths
1. The paper is well-written and easy to follow.

### Weaknesses
1. The PRELIMINARIES are not convincing enough. The author claims in the PRELIMINARIES that reinforcement learning is modeled as a quadruple $(S,A,T,R)$ in (Sutton & Barto, 2018), whereas in general, we model reinforcement learning as a quintuple $(S, A,T,R,\gamma)$. The objective of reinforcement learning policy optimization is generally to maximize the cumulative \textbf{discount} reward, and this paper does not mention anything about reward discount $\gamma$. Given that this is significantly different from the normal research paradigm of reinforcement learning, if this is by design, the author should explain the purpose of doing so. If this is an oversight, I hope the author will correct it in future research.

2. The motive is unclear. the motivation presented by the authors is that "the use of fixed isotropic variance and the disregard for rewards may lead to a mismatch between generated trajectories and those desirable for RL ". I don't understand how this problem relates to the method proposed by the author. The authors claim that this problem comes from (Wu et al., 2019). However, after browsing the paper, I did not find that the author of the original article claimed this problem. If this is proposed for the first time, please provide more detailed analysis and examples to prove that it does exist and will have an impact on offline reinforcement learning, and it is necessary to prove in the experiment that the method proposed in this paper will indeed solve or link this problem.

3. The novelty of the method is limited. Since the reverse process of the diffusion model is to predict the denoising error, I do not quite understand how the formula (9) in the paper is attached to the loss of the diffusion model. From the formula (10) in the paper, I believe that the reward model fits the Q function in reinforcement learning (of course, there is no discount term $\gamma$). Formula (11) is the Q-weighted fitting error. Overall, whether it is learning state transition or using the Q function, it can not impress me.

4. The results are not convincing. The authors' experimental results on D4RL did not live up to their claims of SOTA. Many studies using diffusion models for offline reinforcement learning have provided more competitive experimental results, such as [1, 2]. In addition, "Notably, both DMEMM-w/o-\lambda tr and DMEMM-w/o-tr-guide exhibit significant performance drops," the authors said in the ablation experiment. emphasizing the crucial role of incorporating transition dynamics in our method." However, from the experimental results in Table 3, The difference between dMEMm-w /o-\lambda tr and dMEMm-w /o-tr-guide and DMEMM is insignificant. If the author sticks to his point, I hope the author can come up with more convincing evidence, such as significance testing.

### Questions
See weaknesses

### Soundness
2

### Presentation
3

### Contribution
2
